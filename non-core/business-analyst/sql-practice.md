# SQL Practice — From Basics to Advanced

> 30+ SQL problems with dataset schemas, expected outputs, solutions, explanations, and business interpretations. Not just syntax — business thinking.

---

## How to Use This

1. **Read the problem** and the dataset schema
2. **Write your query** before looking at the solution
3. **Compare** with the provided solution
4. **Understand the business interpretation** — why does this query matter?
5. **Practice** on a real database (SQLite, PostgreSQL, or online platforms)

---

## Dataset Schemas

### E-Commerce Database

```sql
-- customers
customer_id (PK), name, city, signup_date, age

-- orders
order_id (PK), customer_id (FK), order_date, total_amount, status

-- order_items
order_item_id (PK), order_id (FK), product_id (FK), quantity, price

-- products
product_id (PK), product_name, category, price, cost
```

### Sample Data

```sql
customers:
1 | Alice | Mumbai | 2023-01-15 | 28
2 | Bob   | Delhi  | 2023-02-20 | 32
3 | Carol | Mumbai | 2023-03-10 | 25
4 | Dave  | Delhi  | 2023-04-05 | 40
5 | Eve   | Pune   | 2023-05-12 | 35

orders:
101 | 1 | 2023-06-01 | 1500 | completed
102 | 2 | 2023-06-02 | 2500 | completed
103 | 1 | 2023-06-05 | 800  | pending
104 | 3 | 2023-06-08 | 3200 | completed
105 | 4 | 2023-06-10 | 1200 | cancelled
106 | 5 | 2023-06-12 | 2000 | completed
107 | 2 | 2023-06-15 | 900  | completed
108 | 3 | 2023-06-18 | 1500 | pending
```

---

## Level 1: Filtering & Basics

### Q1: Select all customers from Mumbai
```sql
SELECT * FROM customers WHERE city = 'Mumbai';
```
**Expected output:** Alice, Carol
**Business interpretation:** Segmenting customers by geography for regional marketing.

### Q2: Find orders above ₹2000
```sql
SELECT * FROM orders WHERE total_amount > 2000;
```
**Expected output:** Orders 102, 104, 106
**Business interpretation:** Identifying high-value orders for VIP customer treatment.

### Q3: Find customers older than 30
```sql
SELECT * FROM customers WHERE age > 30;
```
**Expected output:** Bob, Dave, Eve
**Business interpretation:** Understanding demographic profile of customer base.

### Q4: Find pending orders
```sql
SELECT * FROM orders WHERE status = 'pending';
```
**Expected output:** Orders 103, 108
**Business interpretation:** Identifying revenue at risk (pending orders may not convert).

---

## Level 2: Aggregation & GROUP BY

### Q5: Count orders per customer
```sql
SELECT customer_id, COUNT(*) AS order_count
FROM orders
GROUP BY customer_id;
```
**Expected output:**
```
1 | 2
2 | 2
3 | 2
4 | 1
5 | 1
```
**Business interpretation:** Identifying your most frequent customers (loyalty).

### Q6: Total revenue per customer
```sql
SELECT customer_id, SUM(total_amount) AS total_revenue
FROM orders
WHERE status = 'completed'
GROUP BY customer_id;
```
**Expected output:**
```
1 | 1500
2 | 3400
3 | 3200
5 | 2000
```
**Business interpretation:** Customer lifetime value (LTV) — who are your best customers?

### Q7: Average order value
```sql
SELECT AVG(total_amount) AS avg_order_value
FROM orders
WHERE status = 'completed';
```
**Expected output:** 1500 + 2500 + 3200 + 2000 = 9200 / 4 = 2300
**Business interpretation:** AOV is a key e-commerce KPI — increasing it directly boosts revenue.

### Q8: Orders per city (via join)
```sql
SELECT c.city, COUNT(o.order_id) AS order_count
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.city;
```
**Expected output:**
```
Mumbai | 4
Delhi  | 3
Pune   | 1
```
**Business interpretation:** Geographic demand analysis for logistics planning.

### Q9: Customers with more than 1 order
```sql
SELECT customer_id, COUNT(*) AS order_count
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 1;
```
**Expected output:** Customers 1, 2, 3
**Business interpretation:** Repeat customers are your most valuable — target retention efforts here.

---

## Level 3: JOINs

### Q10: Orders with customer names
```sql
SELECT o.order_id, c.name, o.total_amount, o.status
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id;
```
**Business interpretation:** Enriching order data with customer info for reporting.

### Q11: Customers with no orders (LEFT JOIN)
```sql
SELECT c.name
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
```
**Expected output:** (none in this dataset — all have orders)
**Business interpretation:** Identifying inactive customers for re-engagement campaigns.

### Q12: Revenue by city
```sql
SELECT c.city, SUM(o.total_amount) AS revenue
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.status = 'completed'
GROUP BY c.city;
```
**Business interpretation:** Regional revenue analysis for market prioritization.

---

## Level 4: Subqueries & CTEs

### Q13: Customers who spent more than average
```sql
SELECT customer_id, SUM(total_amount) AS total_spent
FROM orders
WHERE status = 'completed'
GROUP BY customer_id
HAVING SUM(total_amount) > (SELECT AVG(total_amount) FROM orders WHERE status = 'completed');
```
**Business interpretation:** Identifying high-value customers above the average spend.

### Q14: Top 3 customers by revenue (CTE)
```sql
WITH customer_revenue AS (
    SELECT customer_id, SUM(total_amount) AS revenue
    FROM orders
    WHERE status = 'completed'
    GROUP BY customer_id
)
SELECT customer_id, revenue
FROM customer_revenue
ORDER BY revenue DESC
LIMIT 3;
```
**Expected output:** Customer 2 (3400), Customer 3 (3200), Customer 1 (1500)
**Business interpretation:** Top customers drive disproportionate revenue — prioritize them.

### Q15: Monthly revenue trend
```sql
SELECT 
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    SUM(total_amount) AS revenue
FROM orders
WHERE status = 'completed'
GROUP BY DATE_FORMAT(order_date, '%Y-%m')
ORDER BY month;
```
**Business interpretation:** Tracking revenue trends over time to spot growth or decline.

---

## Level 5: Window Functions

### Q16: Running total of revenue
```sql
SELECT 
    order_id,
    total_amount,
    SUM(total_amount) OVER (ORDER BY order_date) AS running_total
FROM orders
WHERE status = 'completed';
```
**Business interpretation:** Cumulative revenue tracking — useful for annual targets.

### Q17: Rank customers by revenue
```sql
SELECT 
    customer_id,
    SUM(total_amount) AS revenue,
    RANK() OVER (ORDER BY SUM(total_amount) DESC) AS revenue_rank
FROM orders
WHERE status = 'completed'
GROUP BY customer_id;
```
**Business interpretation:** Customer ranking for tiered loyalty programs.

### Q18: Revenue by customer with previous order comparison
```sql
SELECT 
    customer_id,
    order_date,
    total_amount,
    LAG(total_amount) OVER (PARTITION BY customer_id ORDER BY order_date) AS prev_order_amount
FROM orders
WHERE status = 'completed';
```
**Business interpretation:** Tracking whether customers are spending more or less over time.

### Q19: Moving average of revenue (7-day)
```sql
SELECT 
    order_date,
    total_amount,
    AVG(total_amount) OVER (ORDER BY order_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS moving_avg
FROM orders
WHERE status = 'completed';
```
**Business interpretation:** Smoothing daily fluctuations to see underlying trends.

---

## Level 6: Advanced Business Problems

### Q20: Customer churn analysis
**Problem:** Find customers who haven't ordered in the last 60 days.
```sql
SELECT c.customer_id, c.name, MAX(o.order_date) AS last_order
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING MAX(o.order_date) < DATE_SUB(CURRENT_DATE, INTERVAL 60 DAY)
   OR MAX(o.order_date) IS NULL;
```
**Business interpretation:** Churn risk identification for retention campaigns.

### Q21: Repeat purchase rate
```sql
SELECT 
    COUNT(DISTINCT customer_id) AS total_customers,
    SUM(CASE WHEN order_count > 1 THEN 1 ELSE 0 END) AS repeat_customers
FROM (
    SELECT customer_id, COUNT(*) AS order_count
    FROM orders
    GROUP BY customer_id
) t;
```
**Business interpretation:** Repeat purchase rate is a key loyalty metric.

### Q22: Revenue contribution by product category
```sql
SELECT 
    p.category,
    SUM(oi.quantity * oi.price) AS revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
JOIN orders o ON oi.order_id = o.order_id
WHERE o.status = 'completed'
GROUP BY p.category
ORDER BY revenue DESC;
```
**Business interpretation:** Category-level revenue analysis for inventory and marketing decisions.

### Q23: Cohort retention analysis
```sql
SELECT 
    DATE_FORMAT(c.signup_date, '%Y-%m') AS cohort_month,
    DATE_FORMAT(o.order_date, '%Y-%m') AS order_month,
    COUNT(DISTINCT c.customer_id) AS active_customers
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY cohort_month, order_month
ORDER BY cohort_month, order_month;
```
**Business interpretation:** Cohort analysis shows retention over time — which cohorts stay engaged.

### Q24: Find the most valuable product
```sql
SELECT 
    p.product_name,
    SUM(oi.quantity * oi.price) AS revenue,
    SUM(oi.quantity * (oi.price - p.cost)) AS profit
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY profit DESC;
```
**Business interpretation:** Profit (not just revenue) determines which products to promote.

---

## SQL Interview Tips

### Common Mistakes

| Mistake | Fix |
|:--------|:-----|
| Forgetting WHERE vs HAVING | WHERE filters rows, HAVING filters groups |
| Wrong JOIN type | INNER = only matches, LEFT = all left rows |
| Not handling NULLs | Use COALESCE, IS NULL, IS NOT NULL |
| GROUP BY without aggregate | Every non-aggregated column must be in GROUP BY |
| Ignoring performance | Use indexes, avoid SELECT *, limit results |

### Mental Model

```
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```

**Execution order** (logical, not written order):
1. FROM (get tables)
2. WHERE (filter rows)
3. GROUP BY (group rows)
4. HAVING (filter groups)
5. SELECT (choose columns)
6. ORDER BY (sort)
7. LIMIT (limit rows)

---

## Practice Resources

| Resource | What It Covers |
|:---------|:---------------|
| [SQL Practice (this file)](sql-practice.md) | 24 problems with solutions |
| [Data Analyst Statistics](../data-analyst/statistics-practice.md) | Statistical analysis |
| [Analytics Resources](../analytics/non-core-prep.md) | External SQL resources |

---

*SQL is a means to an end — the end is business insight. Always ask "so what?" after every query.*
