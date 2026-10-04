# 06. Analytics: Comprehensive 65+ Question Bank

> High-yield interview questions across SQL, Python/Pandas, Applied Statistics, A/B Testing, Machine Learning, Analytics Cases, and Behavioral Fit.

---

## 📑 Question Bank Index
- **Section 1**: SQL Querying & Schema Logic (Q1 - Q15)
- **Section 2**: Python, Pandas & Data Wrangling (Q16 - Q25)
- **Section 3**: Applied Statistics & Probability (Q26 - Q35)
- **Section 4**: A/B Testing & Experimentation (Q36 - Q45)
- **Section 5**: Machine Learning Fundamentals (Q46 - Q55)
- **Section 6**: Analytics Cases & Behavioral Fit (Q56 - Q65)

---

## Section 1: SQL Querying & Schema Logic

### Q1 [P0][SQL]: Write a query to find the 3rd highest purchase amount per customer.
```sql
WITH RankedPurchases AS (
    SELECT 
        customer_id,
        amount,
        DENSE_RANK() OVER (PARTITION BY customer_id ORDER BY amount DESC) as rnk
    FROM Purchases
)
SELECT customer_id, amount
FROM RankedPurchases
WHERE rnk = 3;
```

### Q2 [P0][SQL]: Given a `UserLogins(user_id, login_date)` table, find all users who logged in for at least 3 consecutive days.
```sql
WITH GroupedLogins AS (
    SELECT 
        user_id,
        login_date,
        login_date - (ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY login_date) * INTERVAL '1 day') AS grp
    FROM (SELECT DISTINCT user_id, login_date FROM UserLogins) sub
)
SELECT user_id, MIN(login_date) as streak_start, COUNT(*) as streak_length
FROM GroupedLogins
GROUP BY user_id, grp
HAVING COUNT(*) >= 3;
```

### Q3 [P0][SQL]: Calculate Day-1, Day-7, and Day-30 user retention percentages.
```sql
WITH Signups AS (
    SELECT user_id, DATE_TRUNC('day', signup_date) as signup_day
    FROM Users
),
Activity AS (
    SELECT DISTINCT user_id, DATE_TRUNC('day', activity_date) as active_day
    FROM UserEvents
)
SELECT 
    s.signup_day,
    COUNT(DISTINCT s.user_id) as cohort_size,
    ROUND(100.0 * COUNT(DISTINCT CASE WHEN a.active_day = s.signup_day + INTERVAL '1 day' THEN a.user_id END) / COUNT(DISTINCT s.user_id), 2) as d1_retention_pct,
    ROUND(100.0 * COUNT(DISTINCT CASE WHEN a.active_day = s.signup_day + INTERVAL '7 day' THEN a.user_id END) / COUNT(DISTINCT s.user_id), 2) as d7_retention_pct,
    ROUND(100.0 * COUNT(DISTINCT CASE WHEN a.active_day = s.signup_day + INTERVAL '30 day' THEN a.user_id END) / COUNT(DISTINCT s.user_id), 2) as d30_retention_pct
FROM Signups s
LEFT JOIN Activity a ON s.user_id = a.user_id
GROUP BY 1 ORDER BY 1;
```

### Q4 [P1][SQL]: Calculate the 30-day rolling sum of revenue for each product category.
```sql
SELECT 
    category_id,
    order_date,
    amount,
    SUM(amount) OVER (
        PARTITION BY category_id 
        ORDER BY order_date 
        RANGE BETWEEN INTERVAL '29 days' PRECEDING AND CURRENT ROW
    ) as rolling_30d_category_rev
FROM Orders;
```

### Q5 [P0][SQL]: Differentiate between `WHERE` and `HAVING` clauses.
- `WHERE` filters individual rows *before* aggregation occurs; cannot contain aggregate functions.
- `HAVING` filters aggregated groups *after* `GROUP BY` execution.

---

## Section 2: Python, Pandas & Data Wrangling

### Q16 [P0][PYTHON]: How do you find and remove duplicate rows based on specific columns in Pandas?
```python
# Keep first occurrence, drop subsequent duplicates
df_cleaned = df.drop_duplicates(subset=['customer_id', 'order_date'], keep='first')
```

### Q17 [P0][PYTHON]: How do you calculate Month-over-Month percentage growth in a Pandas dataframe?
```python
df['monthly_rev'] = df.groupby('month')['amount'].transform('sum')
df['mom_growth_pct'] = df['monthly_rev'].pct_change() * 100
```

### Q18 [P1][PYTHON]: Explain the difference between `df.apply()` and vectorized NumPy operations.
- Vectorized NumPy operations execute in pre-compiled C code directly on contiguous memory arrays, running 50x–200x faster than `df.apply()` which incurs Python interpreter overhead on every individual row.

### Q19 [P0][PYTHON]: How do you handle missing values in numeric and categorical columns?
- Numeric: Impute with median (for skewed distributions) or mean, or model-based imputation (KNN/IterativeImputer).
- Categorical: Impute with mode or add a distinct `"Unknown"` category to preserve missingness signal.

### Q20 [P1][PYTHON]: How do you reshape a dataframe from Long to Wide format and vice versa?
- Long to Wide: `df.pivot(index='date', columns='category', values='revenue')` or `df.pivot_table()`.
- Wide to Long: `df.melt(id_vars=['date'], value_vars=['tech', 'fashion'], var_name='category', value_name='revenue')`.

---

## Section 3: Applied Statistics & Probability

### Q26 [P0][STATS]: Calculate sample size required for an A/B test with 4% baseline conversion and 10% target relative lift.
- Baseline $p = 0.04$, MDE $\Delta = 0.04 	imes 0.10 = 0.004$.
- $N pprox rac{16 \cdot p(1-p)}{\Delta^2} = rac{16 \cdot 0.04 \cdot 0.96}{(0.004)^2} = rac{0.6144}{0.000016} pprox \mathbf{38,400	ext{ users per variant}}$ (Total = ~76,800 users).

### Q27 [P0][STATS]: How do you detect and resolve Sample Ratio Mismatch (SRM)?
- Perform a Chi-Square Goodness-of-Fit test on observed vs expected traffic counts: $\chi^2 = \sum rac{(O - E)^2}{E}$. If $p < 0.001$, significant SRM exists. Immediate actions: Check user redirection redirects, bot-filtering discrepancies, and variant assignment hashing logic in backend.

### Q28 [P1][STATS]: Explain Simpson's Paradox with an analytics example.
- Overall conversion of Variant B is higher because it had 80% mobile traffic (higher converting device), but Variant A won on both Desktop and Mobile individually.

### Q29 [P0][STATS]: What is Central Limit Theorem (CLT)?
- The distribution of sample means approximates a normal distribution as sample size increases ($N \ge 30$), regardless of the underlying population distribution.

### Q30 [P1][STATS]: What is the difference between Statistical Significance and Practical/Business Significance?
- Statistical significance proves an effect is not due to random chance ($p < 0.05$). Practical significance evaluates if the absolute magnitude of lift justifies engineering and operational deployment costs.

---

## Section 4: A/B Testing & Experimentation

### Q36 [P0][EXPERIMENT]: What are Primary, Secondary, and Guardrail metrics in an A/B test?
- **Primary**: The North Star metric the experiment is designed to move (e.g. Checkout conversion rate).
- **Secondary**: Diagnostics that explain *why* the primary metric moved (e.g. Add-to-cart rate, search clicks).
- **Guardrail**: Organizational health metrics that must *not* degrade (e.g. App crash rate, page latency, refund rate).

### Q37 [P1][EXPERIMENT]: Why must an A/B test run for a minimum of 2 full weekly cycles even if it reaches statistical significance in 3 days?
- To eliminate day-of-week seasonality bias (weekday vs weekend shopping behavior), novelty effects, and to ensure adequate exposure to weekly cyclical user cohorts.

### Q38 [P1][EXPERIMENT]: What is the Peeking Problem and how do you prevent it?
- Checking p-values continuously and stopping the test as soon as $p < 0.05$ inflates false-positive rate from 5% to $>30\%$. Prevented via fixed-sample horizon enforcement or sequential testing algorithms (e.g. Always Valid p-values).

---

## Section 5: Machine Learning Fundamentals

### Q46 [P0][ML]: What evaluation metric is appropriate for a highly imbalanced classification dataset (e.g. 1% fraud rate)?
- Use **Precision-Recall AUC (PR-AUC)** or **ROC-AUC** with F1-Score; never rely on raw Accuracy (a naive model predicting all non-fraud achieves 99% accuracy but is useless).

### Q47 [P0][ML]: Explain the difference between Bagging (Random Forest) and Boosting (XGBoost).
- **Bagging**: Trains independent models in parallel on bootstrap samples; reduces variance.
- **Boosting**: Trains sequential models where each subsequent model focuses on correcting the residual errors of prior models; reduces bias and variance.

### Q48 [P1][ML]: What are SHAP (SHapley Additive exPlanations) values and why are they superior to Gini feature importance?
- SHAP values are rooted in cooperative game theory, providing mathematically consistent, directionally aware ($+/-$ impact), and model-agnostic feature attributions for individual predictions.

---

## Section 6: Analytics Cases & Behavioral Fit

### Q56 [P0][CASE]: "Our food delivery app's 30-day retention dropped from 45% to 32% for the January cohort. Walk me through your diagnosis."
- **Approach**: Segment by acquisition channel (paid performance ads vs organic referral), delivery SLA delays (did winter fog/storms cause late deliveries?), restaurant mix shift, and promo discount depth.

### Q61 [P0][FIT]: "Why are you interested in Analytics & Decision Science coming from Civil Engineering?"
- (See verbatim high-conviction answer in [05_interview-preparation.md](05_interview-preparation.md)).

### Q65 [P0][FIT]: "Do you have any questions for our Decision Science team?"
- Ask about the firm's experimentation infrastructure (e.g. In-house A/B testing platform vs third-party), or how causal inference models are used to optimize customer incentives.
