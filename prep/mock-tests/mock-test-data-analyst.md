# Mock Test — Data Analyst

> **Timed test:** 60 minutes · 3 sections · 50 marks. Simulates a data analyst technical round (SQL + statistics + case).

---

## Section A — SQL (5 × 4 = 20 marks) · 20 min

Given tables `orders(order_id, customer_id, amount, order_date)` and `customers(customer_id, name, city)`:

1. Write a query to find total revenue per city.
2. Write a query to find the top 3 customers by total spend.
3. Write a query to find customers who have not placed any orders.
4. Write a query to find the month-over-month revenue growth.
5. Write a query to find the average order value per customer.

---

## Section B — Statistics & Probability (2 × 8 = 16 marks) · 20 min

**Q1.** A dataset has mean 50 and standard deviation 10. Assuming a normal distribution, what percentage of values lie between 30 and 70?

**Q2.** Explain the difference between correlation and causation. Give an example where two metrics are correlated but not causally related.

---

## Section C — Case / Behavioral (2 × 7 = 14 marks) · 20 min

1. "A key business metric dropped 15% last week. How would you investigate it as a data analyst?" (7 marks)
2. "Tell me about a time you used data to drive a decision." (STAR, 7 marks)

---

## Answer Key / Evaluation Guide

**Section A:**
- Q1: `SELECT c.city, SUM(o.amount) FROM orders o JOIN customers c ON o.customer_id=c.customer_id GROUP BY c.city;`
- Q2: `SELECT customer_id, SUM(amount) total FROM orders GROUP BY customer_id ORDER BY total DESC LIMIT 3;`
- Q3: `SELECT * FROM customers c LEFT JOIN orders o ON c.customer_id=o.customer_id WHERE o.customer_id IS NULL;`
- Q4: Use LAG() over month to compute growth.
- Q5: `SELECT customer_id, AVG(amount) FROM orders GROUP BY customer_id;`

**Section B:**
- Q1: 30 and 70 are ±2σ. ~95% of values lie within ±2σ.
- Q2: Correlation ≠ causation. Example: ice cream sales and drowning are correlated (both driven by summer) but not causal.

**Section C:** Assess analytical framework, metric decomposition, data literacy, STAR structure.

---

## Scorecard

| Section | Max | Your Score |
|:--------|:---:|:----------:|
| A — SQL | 20 | |
| B — Statistics | 16 | |
| C — Case / Behavioral | 14 | |
| **Total** | **50** | |

**Rating:** 40+ Excellent · 30–39 Good · 20–29 Needs Work · <20 Revisit SQL/stats

---

## Related

- [Role Study Plan](../../non-core/data-analyst/role-study-plan.md)
- [DA Overview](../../non-core/data-analyst/da-overview.md)
- [Statistics Practice](../../non-core/data-analyst/statistics-practice.md)
- [Mock Test Hub](README.md)
