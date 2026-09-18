# Analytics: 60-Minute Last-Minute Revision

> High-density formula and syntax cheat sheet for Analytics, Quant, and Data Science interviews.

---

## 1. SQL Execution & Window Functions
* **Clause Order**: FROM/JOIN $\to$ WHERE $\to$ GROUP BY $\to$ HAVING $\to$ SELECT $\to$ DISTINCT $\to$ ORDER BY $\to$ LIMIT
* **Window Template**: SUM(metric) OVER (PARTITION BY user_id ORDER BY event_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)
* **Rank Variants**: ROW_NUMBER() (sequential), RANK() (skips ties: 1,2,2,4), DENSE_RANK() (no skips: 1,2,2,3).

---

## 2. Statistics & Experimentation (A/B Testing)
* **Sample Size**:  \approx \frac{16 \sigma^2}{\Delta^2}$ for 80% power, 5% significance level.
* **Type I Error ($\alpha$)**: False Positive ($\alpha = 0.05$).
* **Type II Error ($\beta$)**: False Negative ($\beta = 0.20 \implies \text{Power} = 0.80$).
* **Metrics**: $\text{LTV} = \frac{\text{ARPU} \times \text{Gross Margin}}{\text{Churn Rate}}$; Benchmark: $\text{LTV}/\text{CAC} \ge 3$.
