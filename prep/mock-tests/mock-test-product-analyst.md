# Mock Test — Product Analyst

> **Timed test:** 60 minutes · 3 sections · 50 marks. Simulates a product analyst technical round (SQL + metrics + product thinking).

---

## Section A — SQL & Metrics (5 × 4 = 20 marks) · 20 min

Given tables `events(user_id, event_type, timestamp)` and `users(user_id, signup_date, plan)`:

1. Write a query to find daily active users (DAU) for the last 7 days.
2. Write a query to find the conversion rate from signup to first purchase.
3. Write a query to find the retention rate of users who signed up last month.
4. Write a query to find the most common event type.
5. Write a query to find users who have not been active in 30 days.

---

## Section B — Product Metrics (2 × 8 = 16 marks) · 20 min

**Q1.** Define activation for a productivity app. What metric would you track and why?

**Q2.** A feature has 10% adoption but users who adopt it have 2× retention. How would you decide whether to invest more in it?

---

## Section C — Case / Behavioral (2 × 7 = 14 marks) · 20 min

1. "A key product metric dropped. How would you investigate it as a product analyst?" (7 marks)
2. "Tell me about a time you used data to influence a product decision." (STAR, 7 marks)

---

## Answer Key / Evaluation Guide

**Section A:**
- Q1: `SELECT DATE(timestamp), COUNT(DISTINCT user_id) FROM events WHERE timestamp >= CURDATE() - INTERVAL 7 DAY GROUP BY DATE(timestamp);`
- Q2: `SELECT COUNT(DISTINCT e.user_id)/COUNT(DISTINCT u.user_id) FROM users u LEFT JOIN events e ON u.user_id=e.user_id AND e.event_type='purchase';`
- Q3: Cohort analysis: users who signed up last month and were active this month / total signups.
- Q4: `SELECT event_type, COUNT(*) FROM events GROUP BY event_type ORDER BY 2 DESC LIMIT 1;`
- Q5: `SELECT * FROM users WHERE user_id NOT IN (SELECT DISTINCT user_id FROM events WHERE timestamp >= CURDATE() - INTERVAL 30 DAY);`

**Section B:**
- Q1: Activation = completing the "aha moment" (e.g., first project created). Track activation rate.
- Q2: Assess cohort analysis, cost-benefit, feature impact on core metric, A/B testing.

**Section C:** Assess analytical framework, metric decomposition, product thinking, STAR structure.

---

## Scorecard

| Section | Max | Your Score |
|:--------|:---:|:----------:|
| A — SQL & Metrics | 20 | |
| B — Product Metrics | 16 | |
| C — Case / Behavioral | 14 | |
| **Total** | **50** | |

**Rating:** 40+ Excellent · 30–39 Good · 20–29 Needs Work · <20 Revisit SQL/metrics

---

## Related

- [Role Study Plan](../../non-core/product-analyst/role-study-plan.md)
- [Mock Test Hub](README.md)