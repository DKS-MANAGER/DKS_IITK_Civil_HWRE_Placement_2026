# Mock Test — Business Analyst

> **Timed test:** 60 minutes · 3 sections · 50 marks. Simulates a business analyst technical round (SQL + business case + communication).

---

## Section A — SQL & Data (5 × 4 = 20 marks) · 20 min

Given tables `sales(transaction_id, product_id, region, amount, date)` and `products(product_id, category, price)`:

1. Write a query to find total sales per region.
2. Write a query to find the best-selling product category.
3. Write a query to find sales in the last 30 days.
4. Write a query to find the month with highest sales.
5. Write a query to find products with zero sales.

---

## Section B — Business Case (2 × 8 = 16 marks) · 20 min

**Q1.** A retail chain wants to increase revenue by 20%. Build a framework covering customer, product, pricing, and channel levers.

**Q2.** A company's conversion rate dropped from 5% to 3%. List the hypotheses you would test and the data you would pull.

---

## Section C — Communication / Behavioral (2 × 7 = 14 marks) · 20 min

1. "Explain a complex analysis you did to a non-technical stakeholder." (7 marks)
2. "Tell me about a time you identified a business problem through data." (STAR, 7 marks)

---

## Answer Key / Evaluation Guide

**Section A:**
- Q1: `SELECT region, SUM(amount) FROM sales GROUP BY region;`
- Q2: `SELECT p.category, SUM(s.amount) FROM sales s JOIN products p ON s.product_id=p.product_id GROUP BY p.category ORDER BY 2 DESC LIMIT 1;`
- Q3: `SELECT * FROM sales WHERE date >= CURDATE() - INTERVAL 30 DAY;`
- Q4: `SELECT DATE_FORMAT(date,'%Y-%m') ym, SUM(amount) FROM sales GROUP BY ym ORDER BY 2 DESC LIMIT 1;`
- Q5: `SELECT * FROM products p LEFT JOIN sales s ON p.product_id=s.product_id WHERE s.product_id IS NULL;`

**Section B:**
- Q1: Assess MECE levers: customer acquisition/retention, product mix, pricing, channel optimization.
- Q2: Assess funnel analysis, A/B testing, cohort analysis, data sources (traffic, checkout, payment).

**Section C:** Assess clarity, stakeholder communication, business acumen, STAR structure.

---

## Scorecard

| Section | Max | Your Score |
|:--------|:---:|:----------:|
| A — SQL & Data | 20 | |
| B — Business Case | 16 | |
| C — Communication | 14 | |
| **Total** | **50** | |

**Rating:** 40+ Excellent · 30–39 Good · 20–29 Needs Work · <20 Revisit SQL/business

---

## Related

- [Role Study Plan](../../non-core/business-analyst/role-study-plan.md)
- [BA Overview](../../non-core/business-analyst/ba-overview.md)
- [SQL Practice](../../non-core/business-analyst/sql-practice.md)
- [Mock Test Hub](README.md)
