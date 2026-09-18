# Analytics Rapid Revision

> Fast-recall cheat sheet for Analytics, Data Science, and Quantitative Problem Solving.

---

## 1. Core Technical Foundations

### SQL Essentials
- **Execution Order**: FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY → LIMIT/OFFSET
- **Window Functions**: ROW_NUMBER(), RANK(), DENSE_RANK(), LAG(col, 1) OVER (PARTITION BY ... ORDER BY ...)
- **Aggregation with HAVING**: Use HAVING to filter aggregated groups; WHERE filters raw rows before aggregation.
- **Join Archetypes**: INNER JOIN, LEFT JOIN (keep all left records, NULL if missing), FULL OUTER JOIN, CROSS JOIN.

### Key Statistical Distributions & Metrics
- **Normal**: Mean = Median = Mode, 68-95-99.7 rule.
- **Binomial vs. Poisson**: Binomial ($ trials, probability $), Poisson (count of events in continuous time $\lambda$).
- **Central Limit Theorem**: Sample mean converges to Normal distribution as  \to \infty$, regardless of population distribution (provided finite variance).
- **Hypothesis Testing**:  < \alpha$ (usually 0.05) $\implies$ Reject $. Type I error ($\alpha$) = False Positive; Type II error ($\beta$) = False Negative. Power =  - \beta$.

---

## 2. Business Metrics & KPI Cheatsheet
- **CAC (Customer Acquisition Cost)**: Total Marketing & Sales Spend / New Customers Acquired.
- **LTV (Lifetime Value)**: ARPU $\times$ Gross Margin $\times$ Average Lifetime (/\text{Churn}$).
- **LTV / CAC Ratio**: Benchmark $\ge 3\times$.
- **Conversion Rate**: (Conversions / Total Visitors) $\times 100\%$.
- **Cohort Retention**: % of users active in Day/Month $ post-signup.

---

## 3. Top Interview Drill Prompts
1. *"How would you detect outliers in skewed transaction data?"* (IQR method:  - 1.5 \times \text{IQR}$,  + 1.5 \times \text{IQR}$; or log-transform followed by Z-score).
2. *"How do you evaluate an A/B test with low sample size?"* (Power analysis, Mann-Whitney U non-parametric test, Bootstrap sampling).

