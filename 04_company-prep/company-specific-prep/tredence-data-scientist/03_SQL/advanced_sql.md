# 03 — Advanced SQL: Window Functions, CTEs & Analytics Queries
## Analytical Windowing Frames, Recursive CTEs & Enterprise Query Design

> **Document Status**: Technical Core Curriculum `[TIER 5 / PEDAGOGICAL MODULE]`

---

## 1. Analytical Window Functions Architecture

Unlike standard `GROUP BY` aggregations that collapse rows into a single summary line, window functions calculate aggregates, rankings, and moving statistics across a slice of rows **while preserving the individual identity of every row in the result set**.

```sql
SELECT 
    column_name,
    FUNCTION() OVER (
        PARTITION BY partition_col
        ORDER BY sort_col [ASC|DESC]
        ROWS|RANGE BETWEEN frame_start AND frame_end
    ) AS windowed_metric
FROM table_name;
```

### 1.1 Ranking Functions Comparison
```sql
SELECT 
    store_id, product_id, sales_amount,
    ROW_NUMBER() OVER(PARTITION BY store_id ORDER BY sales_amount DESC) as row_num,
    RANK()       OVER(PARTITION BY store_id ORDER BY sales_amount DESC) as rnk,
    DENSE_RANK() OVER(PARTITION BY store_id ORDER BY sales_amount DESC) as dense_rnk
FROM store_inventory;
```
- For sales values `[500, 400, 400, 250]`:
  - `ROW_NUMBER()` yields: `[1, 2, 3, 4]` (Deterministic arbitrary tie-break)
  - `RANK()` yields: `[1, 2, 2, 4]` (Ties share rank; leaves a gap at 3)
  - `DENSE_RANK()` yields: `[1, 2, 2, 3]` (Ties share rank; zero gaps)

---

## 2. Window Framing: `ROWS` vs `RANGE`

The frame specification controls which subset of rows within the partition are included in the calculation:
- `ROWS BETWEEN 6 PRECEDING AND CURRENT ROW`: Evaluates exactly the previous 6 rows plus current row (fixed count).
- `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`: Cumulative running total from partition start to current row.
- `RANGE BETWEEN INTERVAL 7 DAY PRECEDING AND CURRENT ROW`: Evaluates all rows whose date falls within the calendar window (dynamic value-based frame).

```sql
SELECT 
    customer_id, transaction_date, amount,
    -- Running Cumulative Spend
    SUM(amount) OVER (
        PARTITION BY customer_id 
        ORDER BY transaction_date 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_spend,
    -- 7-Day Trailing Average Spend
    AVG(amount) OVER (
        PARTITION BY customer_id 
        ORDER BY transaction_date 
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS rolling_7d_avg
FROM customer_transactions;
```

---

## 3. Recursive Common Table Expressions (CTEs)

Recursive CTEs are indispensable for querying hierarchical data structures (such as supply chain bill of materials, organizational charts, or customer referral trees):

```sql
WITH RECURSIVE OrgHierarchy AS (
    -- Anchor Member: Root executives with no manager
    SELECT employee_id, employee_name, manager_id, 1 AS org_level
    FROM corporate_employees
    WHERE manager_id IS NULL

    UNION ALL

    -- Recursive Member: Join with subordinates
    SELECT e.employee_id, e.employee_name, e.manager_id, h.org_level + 1
    FROM corporate_employees e
    INNER JOIN OrgHierarchy h ON e.manager_id = h.employee_id
)
SELECT * FROM OrgHierarchy ORDER BY org_level, employee_id;
```

---

## 4. Conditional Aggregation & Pivot Reporting

Converting raw row events into columnar business KPIs without using expensive dynamic pivots:

```sql
SELECT 
    store_id,
    COUNT(transaction_id) AS total_transactions,
    SUM(CASE WHEN payment_method = 'Credit Card' THEN amount ELSE 0 END) AS credit_card_revenue,
    SUM(CASE WHEN payment_method = 'UPI' THEN amount ELSE 0 END) AS upi_revenue,
    SUM(CASE WHEN payment_method = 'Cash' THEN amount ELSE 0 END) AS cash_revenue,
    ROUND(
        SUM(CASE WHEN is_discounted = 1 THEN amount ELSE 0 END) * 100.0 / 
        NULLIF(SUM(amount), 0), 2
    ) AS promo_revenue_pct
FROM pos_transactions
GROUP BY store_id;
```
