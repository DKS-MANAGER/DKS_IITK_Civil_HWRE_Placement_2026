# Module 06 — SQL & Database Analytics for Business Intelligence

SQL is the foundational data manipulation engine evaluated in Accordion (Merilytics) assessments and live technical interviews. Candidates must write clean, optimized, production-grade ANSI SQL queries under whiteboard and screen-share scrutiny.

---

## 1. Logical Query Processing Order

Writing and debugging SQL requires understanding the **10-step logical execution order** executed by relational database engines (PostgreSQL, MySQL, Snowflake, SQL Server):

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        LOGICAL QUERY PROCESSING SEQUENCE                               │
├────────────────────┬───────────────────────────────────────────────────────────────────┤
│ 1. FROM            │ Identifies source tables and builds Cartesian product             │
├────────────────────┼───────────────────────────────────────────────────────────────────┤
│ 2. ON              │ Applies join condition filters to cross-product                   │
├────────────────────┼───────────────────────────────────────────────────────────────────┤
│ 3. JOIN            │ Adds outer rows for LEFT, RIGHT, or FULL OUTER joins              │
├────────────────────┼───────────────────────────────────────────────────────────────────┤
│ 4. WHERE           │ Filters rows prior to aggregation (cannot reference aliases)      │
├────────────────────┼───────────────────────────────────────────────────────────────────┤
│ 5. GROUP BY        │ Groups rows into summary buckets based on specified keys          │
├────────────────────┼───────────────────────────────────────────────────────────────────┤
│ 6. HAVING          │ Filters aggregated groups (can reference aggregate functions)     │
├────────────────────┼───────────────────────────────────────────────────────────────────┤
│ 7. SELECT          │ Evaluates column expressions, window functions, and aliases       │
├────────────────────┼───────────────────────────────────────────────────────────────────┤
│ 8. DISTINCT        │ Eliminates duplicate result rows                                  │
├────────────────────┼───────────────────────────────────────────────────────────────────┤
│ 9. ORDER BY        │ Sorts final result set (can reference SELECT aliases)             │
├────────────────────┼───────────────────────────────────────────────────────────────────┤
│ 10. LIMIT / OFFSET │ Restricts final row count returned to client                      │
└────────────────────┴───────────────────────────────────────────────────────────────────┘
```

> [!WARNING]
> **Common Interview Mistake**: Attempting to use a column alias defined in `SELECT` inside the `WHERE` clause. Because `WHERE` (Step 4) executes *before* `SELECT` (Step 7), the database engine does not yet know the alias. Use a CTE or repeat the underlying expression.

---

## 2. NULL Semantics & Three-Valued Logic (3VL)

SQL operates on **Three-Valued Logic**: expressions evaluate to `TRUE`, `FALSE`, or `UNKNOWN`.

- `NULL = NULL` evaluates to **UNKNOWN**, never `TRUE`.
- `WHERE column = NULL` will return **zero rows**. Always write `WHERE column IS NULL`.
- `NOT IN` with a NULL in the subquery returns **zero rows** because `val NOT IN (1, 2, NULL)` expands to `val != 1 AND val != 2 AND val != NULL`. If any comparison is UNKNOWN, the entire condition evaluates to UNKNOWN. Always use `NOT EXISTS` instead of `NOT IN`.

```sql
-- Safe NULL Replacement
COALESCE(discount_rate, 0.0) -- Returns discount_rate if present, else 0.0

-- Safe Division to Prevent Division by Zero
NULLIF(denominator, 0) -- Returns NULL if denominator is 0, avoiding runtime crash
```

---

## 3. Window Functions Architecture

Window functions perform calculations across a set of table rows related to the current row without collapsing rows into a single summary output (unlike `GROUP BY`).

$$\text{FUNCTION}() \text{ OVER} (\text{PARTITION BY } \text{col}_1 \text{ ORDER BY } \text{col}_2 \text{ [FRAME CLAUSE]})$$

```
┌─────────────────────┬────────────────────────────────────────────────────────────────────────┐
│   Window Function   │                               Behavior                                 │
├─────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ ROW_NUMBER()        │ Assigns unique sequential integer (1, 2, 3, 4) regardless of ties.     │
├─────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ RANK()              │ Leaves gaps upon ties (1, 2, 2, 4).                                    │
├─────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ DENSE_RANK()        │ No gaps upon ties (1, 2, 2, 3). Ideal for "Nth highest" questions.     │
├─────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ LAG(col, n)         │ Accesses value from n rows prior within partition.                     │
├─────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ LEAD(col, n)        │ Accesses value from n rows forward within partition.                   │
├─────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ SUM() OVER(...)     │ Computes running cumulative totals or moving averages over frame.      │
└─────────────────────┴────────────────────────────────────────────────────────────────────────┘
```

---

## 4. 15 Production SQL Business Analytics Scenarios

### Scenario 01: Departments with Zero Active Employees
*Problem*: Return department names that currently have no employees assigned.
```sql
-- Approach: Anti-Join using NOT EXISTS (optimal performance)
SELECT d.dept_name
FROM departments d
WHERE NOT EXISTS (
    SELECT 1 
    FROM employees e 
    WHERE e.dept_id = d.dept_id
);
```

---

### Scenario 02: Second-Highest Salary per Department
*Problem*: Retrieve the employee name and salary of the second-highest earner in each department. If multiple employees tie for second, return all.
```sql
WITH RankedSalaries AS (
    SELECT 
        dept_id,
        emp_name,
        salary,
        DENSE_RANK() OVER(PARTITION BY dept_id ORDER BY salary DESC) AS salary_rank
    FROM employees
)
SELECT dept_id, emp_name, salary
FROM RankedSalaries
WHERE salary_rank = 2;
```

---

### Scenario 03: Detecting Duplicate Transactions Within 5 Minutes
*Problem*: Identify potential fraudulent or accidental duplicate charges where the same customer made an identical transaction amount within 5 minutes of a prior charge.
```sql
WITH TransactionLags AS (
    SELECT 
        txn_id,
        customer_id,
        amount,
        txn_timestamp,
        LAG(txn_timestamp) OVER(PARTITION BY customer_id, amount ORDER BY txn_timestamp) AS prev_txn_timestamp
    FROM transactions
)
SELECT 
    txn_id,
    customer_id,
    amount,
    txn_timestamp,
    prev_txn_timestamp,
    TIMESTAMPDIFF(MINUTE, prev_txn_timestamp, txn_timestamp) AS minutes_diff
FROM TransactionLags
WHERE prev_txn_timestamp IS NOT NULL
  AND TIMESTAMPDIFF(MINUTE, prev_txn_timestamp, txn_timestamp) <= 5;
```

---

### Scenario 04: Cumulative Running Total & 7-Day Moving Average Revenue
*Problem*: For each calendar day, compute total daily revenue, the cumulative year-to-date running total, and the 7-day rolling moving average revenue.
```sql
WITH DailySales AS (
    SELECT 
        CAST(order_timestamp AS DATE) AS sale_date,
        SUM(order_amount) AS daily_revenue
    FROM orders
    GROUP BY CAST(order_timestamp AS DATE)
)
SELECT 
    sale_date,
    daily_revenue,
    SUM(daily_revenue) OVER(
        ORDER BY sale_date 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total_revenue,
    AVG(daily_revenue) OVER(
        ORDER BY sale_date 
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS moving_avg_7day_revenue
FROM DailySales
ORDER BY sale_date;
```

---

### Scenario 05: Identifying Churned Customers (No Orders in 90 Days)
*Problem*: In a subscription/e-commerce business, identify customers who made purchases historically but have had zero purchases in the last 90 days.
```sql
SELECT 
    c.customer_id,
    c.customer_name,
    MAX(o.order_date) AS last_order_date,
    DATEDIFF(CURRENT_DATE, MAX(o.order_date)) AS days_since_last_order
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name
HAVING DATEDIFF(CURRENT_DATE, MAX(o.order_date)) > 90
ORDER BY days_since_last_order DESC;
```

---

### Scenario 06: Month-over-Month (MoM) Revenue Growth Rate
*Problem*: Calculate monthly net revenue and percentage MoM revenue growth rate.
```sql
WITH MonthlyRevenue AS (
    SELECT 
        DATE_TRUNC('month', order_date) AS order_month,
        SUM(net_amount) AS current_month_revenue
    FROM orders
    GROUP BY DATE_TRUNC('month', order_date)
),
RevenueLags AS (
    SELECT 
        order_month,
        current_month_revenue,
        LAG(current_month_revenue) OVER(ORDER BY order_month) AS prev_month_revenue
    FROM MonthlyRevenue
)
SELECT 
    order_month,
    current_month_revenue,
    prev_month_revenue,
    ROUND(
        (current_month_revenue - prev_month_revenue) * 100.0 / NULLIF(prev_month_revenue, 0),
        2
    ) AS mom_growth_pct
FROM RevenueLags
ORDER BY order_month;
```

---

### Scenario 07: Top 10% High-Value Customers (Decile / NTILE Segmentation)
*Problem*: Segment customers into 10 equal spend deciles and return the total revenue contribution of the top 10% tier.
```sql
WITH CustomerSpend AS (
    SELECT 
        customer_id,
        SUM(order_total) AS total_spend,
        NTILE(10) OVER(ORDER BY SUM(order_total) DESC) AS spend_decile
    FROM orders
    GROUP BY customer_id
)
SELECT 
    spend_decile,
    COUNT(customer_id) AS customer_count,
    ROUND(SUM(total_spend), 2) AS decile_revenue,
    ROUND(
        SUM(total_spend) * 100.0 / (SELECT SUM(order_total) FROM orders),
        2
    ) AS revenue_share_pct
FROM CustomerSpend
GROUP BY spend_decile
ORDER BY spend_decile;
```

---

### Scenario 08: Consecutive Purchase Days (Gaps and Islands Problem)
*Problem*: Find all customers who completed purchases on 3 or more consecutive calendar days.
```sql
WITH DistinctDays AS (
    SELECT DISTINCT 
        customer_id, 
        CAST(order_date AS DATE) AS purchase_date
    FROM orders
),
GroupedSequences AS (
    SELECT 
        customer_id,
        purchase_date,
        -- Subtracting row_number days produces an identical anchor date for consecutive days
        DATE_SUB(purchase_date, INTERVAL ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY purchase_date) DAY) AS streak_group
    FROM DistinctDays
)
SELECT 
    customer_id,
    MIN(purchase_date) AS streak_start,
    MAX(purchase_date) AS streak_end,
    COUNT(*) AS consecutive_days
FROM GroupedSequences
GROUP BY customer_id, streak_group
HAVING COUNT(*) >= 3
ORDER BY consecutive_days DESC;
```

---

### Scenario 09: Year-over-Year (YoY) Sales Comparison by Product Category
```sql
WITH AnnualCategorySales AS (
    SELECT 
        p.category_name,
        EXTRACT(YEAR FROM o.order_date) AS sales_year,
        SUM(o.revenue) AS annual_sales
    FROM orders o
    JOIN products p ON o.product_id = p.product_id
    GROUP BY p.category_name, EXTRACT(YEAR FROM o.order_date)
)
SELECT 
    category_name,
    sales_year,
    annual_sales,
    LAG(annual_sales) OVER(PARTITION BY category_name ORDER BY sales_year) AS prior_year_sales,
    ROUND(
        (annual_sales - LAG(annual_sales) OVER(PARTITION BY category_name ORDER BY sales_year)) * 100.0 /
        NULLIF(LAG(annual_sales) OVER(PARTITION BY category_name ORDER BY sales_year), 0),
        2
    ) AS yoy_growth_pct
FROM AnnualCategorySales
ORDER BY category_name, sales_year;
```

---

### Scenario 10: First and Last Order Timestamp per Customer
```sql
SELECT 
    customer_id,
    MIN(order_timestamp) AS first_order_time,
    MAX(order_timestamp) AS most_recent_order_time,
    COUNT(order_id) AS total_orders,
    ROUND(SUM(order_value), 2) AS cumulative_ltv
FROM orders
GROUP BY customer_id;
```

---

### Scenario 11: Obsolete Inventory Aging
```sql
SELECT 
    sku_id,
    sku_name,
    current_inventory_units,
    last_sale_date,
    DATEDIFF(CURRENT_DATE, last_sale_date) AS days_idle,
    CASE 
        WHEN DATEDIFF(CURRENT_DATE, last_sale_date) > 180 THEN 'Obsolete / Dead Stock'
        WHEN DATEDIFF(CURRENT_DATE, last_sale_date) > 90  THEN 'Slow Moving'
        ELSE 'Active'
    END AS inventory_health_status
FROM inventory
WHERE current_inventory_units > 0
ORDER BY days_idle DESC;
```

---

### Scenario 12: Customer Cohort Retention Matrix (Month 0 to Month 3)
```sql
WITH CohortBase AS (
    SELECT 
        customer_id,
        DATE_TRUNC('month', MIN(order_date)) AS cohort_month
    FROM orders
    GROUP BY customer_id
),
ActivitySummary AS (
    SELECT 
        o.customer_id,
        c.cohort_month,
        TIMESTAMPDIFF(MONTH, c.cohort_month, DATE_TRUNC('month', o.order_date)) AS month_number
    FROM orders o
    JOIN CohortBase c ON o.customer_id = c.customer_id
)
SELECT 
    cohort_month,
    COUNT(DISTINCT CASE WHEN month_number = 0 THEN customer_id END) AS cohort_size,
    ROUND(COUNT(DISTINCT CASE WHEN month_number = 1 THEN customer_id END) * 100.0 / 
          COUNT(DISTINCT CASE WHEN month_number = 0 THEN customer_id END), 1) AS m1_retention_pct,
    ROUND(COUNT(DISTINCT CASE WHEN month_number = 2 THEN customer_id END) * 100.0 / 
          COUNT(DISTINCT CASE WHEN month_number = 0 THEN customer_id END), 1) AS m2_retention_pct,
    ROUND(COUNT(DISTINCT CASE WHEN month_number = 3 THEN customer_id END) * 100.0 / 
          COUNT(DISTINCT CASE WHEN month_number = 0 THEN customer_id END), 1) AS m3_retention_pct
FROM ActivitySummary
GROUP BY cohort_month
ORDER BY cohort_month;
```

---

### Scenario 13: Accounts Receivable DSO (Days Sales Outstanding)
$$\text{DSO} = \frac{\text{Ending Accounts Receivable}}{\text{Total Credit Sales}} \times \text{Days in Period}$$
```sql
WITH PeriodMetrics AS (
    SELECT 
        SUM(credit_sales) AS total_sales,
        DATEDIFF(MAX(invoice_date), MIN(invoice_date)) AS period_days
    FROM invoices
    WHERE invoice_date BETWEEN '2025-01-01' AND '2025-12-31'
),
EndingAR AS (
    SELECT SUM(open_balance) AS total_ar
    FROM invoices
    WHERE status = 'Unpaid' AND invoice_date <= '2025-12-31'
)
SELECT 
    e.total_ar,
    p.total_sales,
    p.period_days,
    ROUND((e.total_ar / NULLIF(p.total_sales, 0)) * p.period_days, 1) AS dso_days
FROM EndingAR e
CROSS JOIN PeriodMetrics p;
```

---

### Scenario 14: Preventing Cartesian Fan-Out in Multi-Table Joins
*The Trap*: Joining `Orders` to both `Order_Discounts` and `Order_Shipping` directly causes a Cartesian explosion where sales amounts are duplicated across multiple shipping legs.
```sql
-- Solution: Aggregate sub-tables before joining to master order table
WITH DiscountTotals AS (
    SELECT order_id, SUM(discount_amount) AS total_discount
    FROM order_discounts
    GROUP BY order_id
),
ShippingTotals AS (
    SELECT order_id, SUM(shipping_fee) AS total_shipping
    FROM order_shipping
    GROUP BY order_id
)
SELECT 
    o.order_id,
    o.order_amount,
    COALESCE(d.total_discount, 0) AS total_discount,
    COALESCE(s.total_shipping, 0) AS total_shipping,
    o.order_amount - COALESCE(d.total_discount, 0) + COALESCE(s.total_shipping, 0) AS net_invoiced_amount
FROM orders o
LEFT JOIN DiscountTotals d ON o.order_id = d.order_id
LEFT JOIN ShippingTotals s ON o.order_id = s.order_id;
```

---

### Scenario 15: Query Optimization & SARGable Predicates
- **Non-SARGable (Bypasses Indexes)**: `WHERE YEAR(order_date) = 2025` (forces full table scan).
- **SARGable (Uses B-Tree / Clustered Index)**: `WHERE order_date >= '2025-01-01' AND order_date < '2026-01-01'`.
- **Eliminating Correlated Subqueries**: Replace scalar subqueries in `SELECT` with CTE joins.

