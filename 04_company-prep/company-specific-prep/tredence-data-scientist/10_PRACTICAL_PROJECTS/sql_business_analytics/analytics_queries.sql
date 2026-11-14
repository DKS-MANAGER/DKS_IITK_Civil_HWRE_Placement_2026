-- ============================================================================
-- Project 3: Enterprise Retail & CPG Analytical Query Suite
-- ANSI SQL Compliant (PostgreSQL, Snowflake, Databricks SQL)
-- Schema: stores, products, customers, promotions, transactions, transaction_items
-- ============================================================================

-- ----------------------------------------------------------------------------
-- QUERY 1: Customer RFM Segmentation (Recency, Frequency, Monetary)
-- ----------------------------------------------------------------------------
WITH customer_aggregates AS (
    SELECT
        c.customer_id,
        c.customer_name,
        CURRENT_DATE - MAX(t.transaction_date) AS recency_days,
        COUNT(DISTINCT t.transaction_id) AS frequency_orders,
        COALESCE(SUM(t.total_amount), 0) AS monetary_spend
    FROM customers c
    LEFT JOIN transactions t ON c.customer_id = t.customer_id
    GROUP BY c.customer_id, c.customer_name
),
rfm_scores AS (
    SELECT
        customer_id,
        customer_name,
        recency_days,
        frequency_orders,
        monetary_spend,
        NTILE(5) OVER (ORDER BY recency_days DESC) AS r_score,   -- lower recency_days = higher score
        NTILE(5) OVER (ORDER BY frequency_orders ASC) AS f_score,
        NTILE(5) OVER (ORDER BY monetary_spend ASC) AS m_score
    FROM customer_aggregates
)
SELECT
    customer_id,
    customer_name,
    recency_days,
    frequency_orders,
    monetary_spend,
    r_score,
    f_score,
    m_score,
    CASE
        WHEN r_score >= 4 AND f_score >= 4 AND m_score >= 4 THEN 'Champions / VIP'
        WHEN r_score >= 3 AND f_score >= 3 THEN 'Loyal Customers'
        WHEN r_score <= 2 AND f_score >= 3 THEN 'At Risk / Churning'
        WHEN r_score <= 2 AND f_score <= 2 THEN 'Hibernating / Dormant'
        ELSE 'Promising / Growth'
    END AS customer_segment
FROM rfm_scores
ORDER BY monetary_spend DESC;


-- ----------------------------------------------------------------------------
-- QUERY 2: Month-over-Month (MoM) Revenue Growth and Trailing Velocity
-- ----------------------------------------------------------------------------
WITH monthly_revenue AS (
    SELECT
        DATE_TRUNC('month', transaction_date) AS sales_month,
        SUM(total_amount) AS total_revenue
    FROM transactions
    GROUP BY DATE_TRUNC('month', transaction_date)
)
SELECT
    sales_month,
    total_revenue,
    LAG(total_revenue, 1) OVER (ORDER BY sales_month) AS prev_month_revenue,
    ROUND(
        100.0 * (total_revenue - LAG(total_revenue, 1) OVER (ORDER BY sales_month)) /
        NULLIF(LAG(total_revenue, 1) OVER (ORDER BY sales_month), 0),
        2
    ) AS mom_growth_pct
FROM monthly_revenue
ORDER BY sales_month;


-- ----------------------------------------------------------------------------
-- QUERY 3: Store-Level 7-Day Rolling Moving Average Sales
-- ----------------------------------------------------------------------------
WITH daily_store_sales AS (
    SELECT
        store_id,
        transaction_date,
        SUM(total_amount) AS daily_revenue
    FROM transactions
    GROUP BY store_id, transaction_date
)
SELECT
    store_id,
    transaction_date,
    daily_revenue,
    ROUND(
        AVG(daily_revenue) OVER (
            PARTITION BY store_id
            ORDER BY transaction_date
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ),
        2
    ) AS rolling_7day_avg_revenue
FROM daily_store_sales
ORDER BY store_id, transaction_date;


-- ----------------------------------------------------------------------------
-- QUERY 4: Top 3 Revenue-Generating SKUs per Category
-- ----------------------------------------------------------------------------
WITH sku_revenue AS (
    SELECT
        p.category,
        p.product_id,
        p.product_name,
        SUM(ti.quantity * ti.unit_price) AS product_gross_revenue,
        DENSE_RANK() OVER (
            PARTITION BY p.category
            ORDER BY SUM(ti.quantity * ti.unit_price) DESC
        ) AS rank_in_category
    FROM products p
    JOIN transaction_items ti ON p.product_id = ti.product_id
    GROUP BY p.category, p.product_id, p.product_name
)
SELECT
    category,
    rank_in_category,
    product_name,
    product_gross_revenue
FROM sku_revenue
WHERE rank_in_category <= 3
ORDER BY category, rank_in_category;


-- ----------------------------------------------------------------------------
-- QUERY 5: Monthly Customer Cohort Retention Rate
-- ----------------------------------------------------------------------------
WITH customer_first_purchase AS (
    SELECT
        customer_id,
        DATE_TRUNC('month', MIN(transaction_date)) AS cohort_month
    FROM transactions
    GROUP BY customer_id
),
customer_activities AS (
    SELECT
        t.customer_id,
        cfp.cohort_month,
        DATE_TRUNC('month', t.transaction_date) AS activity_month,
        (EXTRACT(YEAR FROM t.transaction_date) - EXTRACT(YEAR FROM cfp.cohort_month)) * 12 +
        (EXTRACT(MONTH FROM t.transaction_date) - EXTRACT(MONTH FROM cfp.cohort_month)) AS month_index
    FROM transactions t
    JOIN customer_first_purchase cfp ON t.customer_id = cfp.customer_id
    GROUP BY t.customer_id, cfp.cohort_month, DATE_TRUNC('month', t.transaction_date), t.transaction_date
),
cohort_sizes AS (
    SELECT
        cohort_month,
        COUNT(DISTINCT customer_id) AS total_cohort_users
    FROM customer_first_purchase
    GROUP BY cohort_month
)
SELECT
    ca.cohort_month,
    cs.total_cohort_users,
    ca.month_index,
    COUNT(DISTINCT ca.customer_id) AS active_users,
    ROUND(100.0 * COUNT(DISTINCT ca.customer_id) / cs.total_cohort_users, 2) AS retention_rate_pct
FROM customer_activities ca
JOIN cohort_sizes cs ON ca.cohort_month = cs.cohort_month
GROUP BY ca.cohort_month, cs.total_cohort_users, ca.month_index
ORDER BY ca.cohort_month, ca.month_index;


-- ----------------------------------------------------------------------------
-- QUERY 6: Trade Promotion Lift Analysis (Promotional vs Non-Promo Sales)
-- ----------------------------------------------------------------------------
SELECT
    p.category,
    p.product_name,
    ROUND(AVG(CASE WHEN ti.discount_amount > 0 THEN ti.quantity END), 2) AS avg_promo_units_per_tx,
    ROUND(AVG(CASE WHEN ti.discount_amount = 0 THEN ti.quantity END), 2) AS avg_baseline_units_per_tx,
    ROUND(
        100.0 * (
            AVG(CASE WHEN ti.discount_amount > 0 THEN ti.quantity END) -
            AVG(CASE WHEN ti.discount_amount = 0 THEN ti.quantity END)
        ) / NULLIF(AVG(CASE WHEN ti.discount_amount = 0 THEN ti.quantity END), 0),
        2
    ) AS promotional_volume_lift_pct
FROM products p
JOIN transaction_items ti ON p.product_id = ti.product_id
GROUP BY p.category, p.product_name
HAVING COUNT(CASE WHEN ti.discount_amount > 0 THEN 1 END) >= 10
ORDER BY promotional_volume_lift_pct DESC;


-- ----------------------------------------------------------------------------
-- QUERY 7: Market Basket Affinity: Top Co-Purchased Product Pairs
-- ----------------------------------------------------------------------------
WITH paired_items AS (
    SELECT
        ti1.product_id AS product_a,
        ti2.product_id AS product_b,
        COUNT(DISTINCT ti1.transaction_id) AS co_purchase_count
    FROM transaction_items ti1
    JOIN transaction_items ti2
        ON ti1.transaction_id = ti2.transaction_id
        AND ti1.product_id < ti2.product_id  -- eliminate self-pairs and duplicates
    GROUP BY ti1.product_id, ti2.product_id
)
SELECT
    pa.product_name AS product_1,
    pb.product_name AS product_2,
    pi.co_purchase_count
FROM paired_items pi
JOIN products pa ON pi.product_a = pa.product_id
JOIN products pb ON pi.product_b = pb.product_id
ORDER BY pi.co_purchase_count DESC
LIMIT 10;


-- ----------------------------------------------------------------------------
-- QUERY 8: Identifying Inactive / Churned Accounts (60+ Days Inactive)
-- ----------------------------------------------------------------------------
SELECT
    c.customer_id,
    c.customer_name,
    c.email,
    c.tier,
    MAX(t.transaction_date) AS last_purchase_date,
    CURRENT_DATE - MAX(t.transaction_date) AS days_inactive,
    SUM(t.total_amount) AS historical_lifetime_spend
FROM customers c
JOIN transactions t ON c.customer_id = t.customer_id
GROUP BY c.customer_id, c.customer_name, c.email, c.tier
HAVING MAX(t.transaction_date) <= CURRENT_DATE - INTERVAL '60 days'
ORDER BY historical_lifetime_spend DESC;


-- ----------------------------------------------------------------------------
-- QUERY 9: Contribution Margin by Retail Store Region
-- ----------------------------------------------------------------------------
SELECT
    s.region,
    COUNT(DISTINCT t.transaction_id) AS total_transactions,
    SUM(ti.quantity * ti.unit_price) AS gross_sales,
    SUM(ti.discount_amount) AS total_discounts,
    SUM(ti.quantity * p.cost_price) AS total_cogs,
    ROUND(
        SUM((ti.quantity * ti.unit_price) - ti.discount_amount - (ti.quantity * p.cost_price)),
        2
    ) AS contribution_margin_dollars,
    ROUND(
        100.0 * SUM((ti.quantity * ti.unit_price) - ti.discount_amount - (ti.quantity * p.cost_price)) /
        NULLIF(SUM(ti.quantity * ti.unit_price), 0),
        2
    ) AS contribution_margin_pct
FROM stores s
JOIN transactions t ON s.store_id = t.store_id
JOIN transaction_items ti ON t.transaction_id = ti.transaction_id
JOIN products p ON ti.product_id = p.product_id
GROUP BY s.region
ORDER BY contribution_margin_dollars DESC;


-- ----------------------------------------------------------------------------
-- QUERY 10: Recursive CTE: Multi-Tier Product Category Hierarchy Rollup
-- ----------------------------------------------------------------------------
WITH RECURSIVE category_tree AS (
    -- Anchor member: top-level parent categories (parent_category_id IS NULL)
    SELECT
        category_id,
        category_name,
        parent_category_id,
        1 AS hierarchy_level,
        CAST(category_name AS VARCHAR(255)) AS full_path
    FROM product_categories
    WHERE parent_category_id IS NULL

    UNION ALL

    -- Recursive member: child categories joined to their parents
    SELECT
        child.category_id,
        child.category_name,
        child.parent_category_id,
        parent.hierarchy_level + 1,
        CAST(parent.full_path || ' > ' || child.category_name AS VARCHAR(255))
    FROM product_categories child
    JOIN category_tree parent ON child.parent_category_id = parent.category_id
)
SELECT
    category_id,
    hierarchy_level,
    full_path
FROM category_tree
ORDER BY full_path;
