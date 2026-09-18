# 09. Business Analyst: Rapid Revision Sheet

> High-density, 1-page formula and framework cheat sheet for test day and interview morning.

---

## 1. SQL Query Architecture & Quick Syntax

### Clause Execution Order
```text
1. FROM / JOIN
2. WHERE (Row-level filter)
3. GROUP BY (Aggregation buckets)
4. HAVING (Aggregate filter)
5. SELECT (Column projection)
6. DISTINCT
7. ORDER BY
8. LIMIT / OFFSET
```

### Essential Snippets
```sql
-- Monthly Cohort Aggregation with Window Lag
WITH monthly_rev AS (
    SELECT 
        DATE_TRUNC('month', order_date) AS order_month,
        category,
        SUM(total_amount) AS revenue
    FROM orders o
    JOIN products p ON o.product_id = p.product_id
    WHERE status = 'Completed'
    GROUP BY 1, 2
)
SELECT 
    order_month,
    category,
    revenue,
    LAG(revenue, 1) OVER (PARTITION BY category ORDER BY order_month) AS prev_month_rev,
    ROUND(100.0 * (revenue - LAG(revenue, 1) OVER (PARTITION BY category ORDER BY order_month)) / NULLIF(LAG(revenue, 1) OVER (PARTITION BY category ORDER BY order_month), 0), 2) AS mom_growth_pct
FROM monthly_rev;
```

---

## 2. Business Metric Equations & Ratios

| Metric | Formula | Benchmark / Target |
|:---|:---|:---:|
| **Customer Acquisition Cost (CAC)** | $\frac{\text{Total Sales \& Marketing Expenses}}{\text{Number of New Customers Acquired}}$ | Lower is better |
| **Customer Lifetime Value (LTV)** | $\frac{\text{ARPU} \times \text{Gross Margin \%}}{\text{Monthly Churn Rate}}$ | $\ge 3\times \text{CAC}$ |
| **Conversion Rate** | $\frac{\text{Total Successful Conversions}}{\text{Total Unique Visitors}} \times 100\%$ | $2\% - 5\%$ (E-commerce) |
| **Average Order Value (AOV)** | $\frac{\text{Total Revenue}}{\text{Total Orders Placed}}$ | Growth driver |
| **Net Promoter Score (NPS)** | $\% \text{Promoters (9-10)} - \% \text{Detractors (0-6)}$ | $> +40$ (Good), $> +70$ (World-class) |

---

## 3. Emergency Case Deconstruction Heuristic

When asked to diagnose any metric drop:
1. **Define Metric**: What is the numerator and denominator?
2. **Segment the Drop**: Segment across Geography, Platform (iOS/Android/Web), User Cohort (New vs Retained).
3. **External Checks**: Seasonality, holidays, network outage, competitor campaign.
4. **Internal Checks**: Bug in latest deployment, checkout policy change, pricing adjustment.
5. **Formulate Hypothesis $\to$ Request Data $\to$ Quantify ROI of Fix**.
