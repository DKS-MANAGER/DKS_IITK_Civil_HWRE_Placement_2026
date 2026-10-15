# Citi AIM Analytics — Rapid Revision & Formula Cheatsheet

> **Target Role**: Spec Analytics Analyst — Business Analytics (SBS), Citi AIM  
> **Purpose**: High-density revision sheet for the 24 hours prior to assessment or interview.

---

## 1. High-Yield Statistics & Probability Formulas

### Probability Axioms & Conditional
* **Addition Rule**: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
* **Conditional Probability**: $P(A | B) = \frac{P(A \cap B)}{P(B)}$.
* **Independence Condition**: $P(A \cap B) = P(A) \cdot P(B) \iff P(A | B) = P(A)$.
* **Bayes' Theorem**:
  $$P(B_j | A) = \frac{P(A | B_j) \cdot P(B_j)}{\sum_{i=1}^k P(A | B_i) \cdot P(B_i)}$$

### Core Distributions Summary
* **Binomial**: Mean = $np$, Variance = $np(1-p)$.
* **Poisson**: Mean = $\lambda$, Variance = $\lambda$. $P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$.
* **Geometric**: Mean = $\frac{1}{p}$, Variance = $\frac{1-p}{p^2}$.
* **Exponential**: Mean = $\frac{1}{\lambda}$, Variance = $\frac{1}{\lambda^2}$. $P(X > t) = e^{-\lambda t}$.
* **Normal**: $Z = \frac{X - \mu}{\sigma}$. Empirical: $\pm 1\sigma \approx 68.3\%, \pm 2\sigma \approx 95.5\%, \pm 3\sigma \approx 99.7\%$.

### Sampling & Inference
* **Central Limit Theorem**: As $n \to \infty$, $\bar{X} \sim \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)$.
* **Standard Error**: $\text{SE} = \frac{\sigma}{\sqrt{n}}$ (or $\frac{s}{\sqrt{n}}$).
* **Sample Variance (Unbiased)**: $s^2 = \frac{\sum (X_i - \bar{X})^2}{n - 1}$.
* **95% Confidence Interval for Mean**: $\bar{X} \pm 1.96 \frac{s}{\sqrt{n}}$ (or $\pm t_{0.025, n-1} \frac{s}{\sqrt{n}}$ for $n < 30$).

### Hypothesis Testing Formulas
* **One-Sample $Z$-Test**: $Z = \frac{\bar{X} - \mu_0}{\sigma / \sqrt{n}}$.
* **One-Sample $t$-Test**: $t = \frac{\bar{X} - \mu_0}{s / \sqrt{n}}, \quad df = n - 1$.
* **Two-Sample Independent $t$-Test (Welch)**:
  $$t = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$$
* **Paired $t$-Test**: $t = \frac{\bar{d}}{s_d / \sqrt{n}}, \quad df = n - 1$.
* **Chi-Square Test**: $\chi^2 = \sum \frac{(O - E)^2}{E}, \quad E = \frac{\text{Row Total} \times \text{Col Total}}{\text{Grand Total}}$.
* **p-Value Definition**: The probability of observing a test statistic at least as extreme as the sample outcome, **assuming $H_0$ is true**.

---

## 2. Top 10 SQL Syntax Templates

### 1. Second Highest Value per Partition (`DENSE_RANK`)
```sql
WITH Ranked AS (
    SELECT account_id, txn_id, amount,
           DENSE_RANK() OVER (PARTITION BY account_id ORDER BY amount DESC) AS rnk
    FROM transactions
)
SELECT * FROM Ranked WHERE rnk = 2;
```

### 2. Month-over-Month Growth Calculation (`LAG`)
```sql
WITH MonthlySpend AS (
    SELECT DATE_TRUNC('month', txn_date) AS m_date, SUM(amount) AS total_spend
    FROM transactions GROUP BY DATE_TRUNC('month', txn_date)
)
SELECT m_date, total_spend,
       ROUND(((total_spend - LAG(total_spend) OVER (ORDER BY m_date)) / 
              NULLIF(LAG(total_spend) OVER (ORDER BY m_date), 0)) * 100, 2) AS mom_growth_pct
FROM MonthlySpend;
```

### 3. Rolling 30-Day Cumulative Spend Window
```sql
SELECT account_id, txn_date, amount,
       SUM(amount) OVER (
           PARTITION BY account_id ORDER BY txn_date 
           RANGE BETWEEN INTERVAL '30 DAYS' PRECEDING AND CURRENT ROW
       ) AS rolling_30d_spend
FROM transactions;
```

### 4. Running Cumulative Balance Ledger
```sql
SELECT txn_id, txn_date,
       SUM(CASE WHEN txn_type = 'CREDIT' THEN amount ELSE -amount END) OVER (
           PARTITION BY account_id ORDER BY txn_date, txn_id 
           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
       ) AS running_balance
FROM transactions;
```

### 5. Detecting Consecutive Monthly Declines
```sql
WITH Balances AS (
    SELECT account_id, month_end, balance,
           LAG(balance, 1) OVER (PARTITION BY account_id ORDER BY month_end) AS bal_m1,
           LAG(balance, 2) OVER (PARTITION BY account_id ORDER BY month_end) AS bal_m2
    FROM monthly_snapshots
)
SELECT DISTINCT account_id FROM Balances
WHERE balance < bal_m1 AND bal_m1 < bal_m2;
```

### 6. Transaction Velocity Alert (Swipes $< 5$ Minutes)
```sql
WITH Velocity AS (
    SELECT account_id, txn_date, amount,
           LAG(txn_date) OVER (PARTITION BY account_id ORDER BY txn_date) AS prev_date
    FROM transactions
)
SELECT * FROM Velocity
WHERE (txn_date - prev_date) <= INTERVAL '5 MINUTES';
```

### 7. Deduplicating Double Swipes
```sql
WITH RankedDuplicates AS (
    SELECT txn_id, ROW_NUMBER() OVER (
        PARTITION BY account_id, txn_date, amount ORDER BY txn_id ASC
    ) AS dup_rnk
    FROM transactions
)
DELETE FROM transactions WHERE txn_id IN (
    SELECT txn_id FROM RankedDuplicates WHERE dup_rnk > 1
);
```

### 8. Monthly Customer Churn Rate
```sql
WITH MonthlyActive AS (
    SELECT DISTINCT cust_id, DATE_TRUNC('month', txn_date) AS m_date FROM transactions
)
SELECT curr.m_date,
       COUNT(DISTINCT curr.cust_id) AS total_active,
       COUNT(DISTINCT CASE WHEN next_m.cust_id IS NULL THEN curr.cust_id END) AS churned,
       ROUND((COUNT(DISTINCT CASE WHEN next_m.cust_id IS NULL THEN curr.cust_id END)::DECIMAL / 
              COUNT(DISTINCT curr.cust_id)) * 100, 2) AS churn_rate_pct
FROM MonthlyActive curr
LEFT JOIN MonthlyActive next_m ON curr.cust_id = next_m.cust_id 
     AND next_m.m_date = curr.m_date + INTERVAL '1 MONTH'
GROUP BY curr.m_date;
```

### 9. Conditional Aggregation Cross-Holding Audit
```sql
SELECT cust_id
FROM accounts
WHERE status = 'ACTIVE' AND acct_type IN ('SAVINGS', 'CREDIT_CARD')
GROUP BY cust_id
HAVING COUNT(DISTINCT acct_type) = 2;
```

### 10. Resolving Divide-by-Zero with NULLIF
```sql
SELECT account_id,
       ROUND((balance / NULLIF(credit_limit, 0)) * 100, 2) AS utilization_pct
FROM accounts;
```

---

## 3. Core ML & Banking Scorecard Cheatsheet

### Classification Metrics Formulas
* $\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}$ (Quality of positive predictions; minimizes false alarms).
* $\text{Recall (Sensitivity)} = \frac{\text{TP}}{\text{TP} + \text{FN}}$ (Coverage of actual positives; minimizes missed fraud/defaults).
* $\text{Specificity} = \frac{\text{TN}}{\text{TN} + \text{FP}}$ (True negative rate).
* $F_1\text{-Score} = \frac{2 \cdot \text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$.
* **ROC-AUC**: Probability that a randomly chosen positive receives a higher risk score than a randomly chosen negative.

### Supplementary Scorecard Metrics (`[PREPARATION RECOMMENDATION]`)
* **KS Statistic**: $\text{KS} = \max_d |F_{bad}(d) - F_{good}(d)|$. Target: $\text{KS} > 40\%$, peak occurring in Deciles 2–4.
* **Gini**: $\text{Gini} = 2 \times \text{ROC-AUC} - 1$.
* **PSI (Population Stability Index)**:
  $$\text{PSI} = \sum (\text{Actual}_i - \text{Expected}_i) \cdot \ln\left(\frac{\text{Actual}_i}{\text{Expected}_i}\right)$$
  $\text{PSI} < 0.10 \implies \text{Stable}$; $\text{PSI} \ge 0.25 \implies \text{Recalibrate model}$.

---

## 4. Night-Before Interview Mental Checklist

1. **Self-Introduction Ready**: Delivered in 90–120 seconds. Connects quantitative engineering time-series research to financial risk modeling.
2. **First-Principles Confidence**: Ready to define p-value, Central Limit Theorem, Type I/II error trade-offs, and Gauss-Markov assumptions without hedging.
3. **Whiteboard SQL Fluency**: Ready to write CTEs with `DENSE_RANK()`, `LAG()`, and `SUM() OVER ()` on a blank document without an IDE.
4. **Commercial Trade-Off Mindset**: When answering business cases, always translate metrics into dollar impact ($P\&L$), and factor in operational/regulatory costs.
5. **Ethics & Risk Defense**: Ready to explain Citi's compliance culture: safeguarding client assets, escalating control defects transparently, and rejecting biased proxy variables.
