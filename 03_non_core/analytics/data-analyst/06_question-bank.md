# 06. Data Analyst: Comprehensive 50+ Question Bank

> **Target Role**: Data Analyst / Product Data Analyst / Business Intelligence Analyst  
> **Structure**: Categorized interview questions with model SQL queries, Python scripts, statistical formulations, and interviewer follow-up questions.

---

## 📑 Question Bank Index
- **Section 1**: Advanced SQL Queries & Window Functions (Q1 – Q15)
- **Section 2**: Python Data Wrangling & Pandas Logic (Q16 – Q25)
- **Section 3**: Probability, Statistics & A/B Testing (Q26 – Q35)
- **Section 4**: Exploratory Data Analysis & Metric Diagnostics (Q36 – Q45)
- **Section 5**: Behavioral, Resume & Civil-to-Analytics Bridge (Q46 – Q52)

---

## Section 1: Advanced SQL Queries & Window Functions

### Q1 [P0][SQL]: Write a SQL query to calculate Month-over-Month (MoM) user retention percentage from a `user_activity(user_id, activity_date)` table.
```sql
WITH user_monthly AS (
    SELECT DISTINCT 
        user_id, 
        DATE_TRUNC('month', activity_date) AS activity_month
    FROM user_activity
),
retention_calc AS (
    SELECT 
        m1.activity_month AS current_month,
        COUNT(DISTINCT m1.user_id) AS active_users,
        COUNT(DISTINCT m2.user_id) AS retained_users
    FROM user_monthly m1
    LEFT JOIN user_monthly m2 
        ON m1.user_id = m2.user_id 
        AND m2.activity_month = m1.activity_month + INTERVAL '1 month'
    GROUP BY m1.activity_month
)
SELECT 
    current_month,
    active_users,
    retained_users,
    ROUND(100.0 * retained_users / active_users, 2) AS next_month_retention_pct
FROM retention_calc
ORDER BY current_month;
```
*Interviewer Follow-Up*: Why do we use `LEFT JOIN` instead of `INNER JOIN`?  
*(Inner join would eliminate the last available month in the dataset where next-month activity hasn't occurred yet, and would drop cohorts with zero retained users).*

---

### Q2 [P0][SQL]: Calculate the 7-day rolling average revenue for each product category from `sales(transaction_id, category_id, sale_date, amount)`.
```sql
SELECT 
    category_id,
    sale_date,
    amount,
    AVG(amount) OVER (
        PARTITION BY category_id 
        ORDER BY sale_date 
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS rolling_7d_avg_rev
FROM sales
ORDER BY category_id, sale_date;
```
*Interviewer Follow-Up*: What is the difference between `ROWS BETWEEN` and `RANGE BETWEEN` when there are multiple sales on the same date?  
*(`ROWS` operates on physical row offsets, while `RANGE` operates on logical date values, aggregating all duplicates within the value window).*

---

### Q3 [P0][SQL]: Find the top 3 spending customers per city, including ties, from `customers(customer_id, city)` and `orders(order_id, customer_id, amount)`.
```sql
WITH customer_spending AS (
    SELECT 
        c.city,
        c.customer_id,
        SUM(o.amount) AS total_spent,
        DENSE_RANK() OVER (
            PARTITION BY c.city 
            ORDER BY SUM(o.amount) DESC
        ) AS spending_rank
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.city, c.customer_id
)
SELECT city, customer_id, total_spent, spending_rank
FROM customer_spending
WHERE spending_rank <= 3
ORDER BY city, spending_rank;
```
*Interviewer Follow-Up*: Why choose `DENSE_RANK()` over `ROW_NUMBER()` or `RANK()`?  
*(`DENSE_RANK()` ensures that if two users tie for 1st place, the next user gets 2nd place without skipping numbers).*

---

### Q4 [P0][SQL]: Deduplicate a table `user_events(event_id, user_id, event_type, created_at)` keeping only the most recent record per user and event type.
```sql
WITH ranked_events AS (
    SELECT 
        event_id,
        user_id,
        event_type,
        created_at,
        ROW_NUMBER() OVER (
            PARTITION BY user_id, event_type 
            ORDER BY created_at DESC
        ) AS rn
    FROM user_events
)
DELETE FROM user_events
WHERE event_id IN (
    SELECT event_id FROM ranked_events WHERE rn > 1
);
```

---

### Q5 [P1][SQL]: Identify consecutive login streaks of 3 or more days for each user from `logins(user_id, login_date)`.
```sql
WITH distinct_logins AS (
    SELECT DISTINCT user_id, CAST(login_date AS DATE) AS log_date
    FROM logins
),
grouped_streaks AS (
    SELECT 
        user_id,
        log_date,
        log_date - (ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY log_date) * INTERVAL '1 day') AS grp
    FROM distinct_logins
)
SELECT 
    user_id,
    MIN(log_date) AS streak_start,
    MAX(log_date) AS streak_end,
    COUNT(*) AS streak_length
FROM grouped_streaks
GROUP BY user_id, grp
HAVING COUNT(*) >= 3
ORDER BY user_id, streak_start;
```

---

## Section 2: Python Data Wrangling & Pandas Logic

### Q16 [P0][PYTHON]: Write a Pandas snippet to compute customer churn where churn is defined as no transaction in the last 90 days.
```python
import pandas as pd
from datetime import timedelta

def identify_churn(df: pd.DataFrame, reference_date: pd.Timestamp) -> pd.DataFrame:
    # df has columns: ['customer_id', 'transaction_date', 'amount']
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    last_purchase = df.groupby('customer_id')['transaction_date'].max().reset_index()
    last_purchase['days_inactive'] = (reference_date - last_purchase['transaction_date']).dt.days
    last_purchase['is_churned'] = last_purchase['days_inactive'] > 90
    return last_purchase
```

---

### Q17 [P0][PYTHON]: Implement vectorized calculation of Interquartile Range (IQR) outlier detection for transaction amounts by category.
```python
import pandas as pd

def flag_outliers_iqr(df: pd.DataFrame) -> pd.DataFrame:
    def get_bounds(series):
        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1
        return q1 - 1.5 * iqr, q3 + 1.5 * iqr

    bounds = df.groupby('category_id')['amount'].transform(get_bounds)
    lower_bound = bounds.apply(lambda x: x[0])
    upper_bound = bounds.apply(lambda x: x[1])
    
    df['is_outlier'] = (df['amount'] < lower_bound) | (df['amount'] > upper_bound)
    return df
```

---

## Section 3: Probability, Statistics & A/B Testing

### Q26 [P0][STATS]: How do you determine sample size for an A/B test on website conversion rate?
**Formula**:
$$n = rac{2 \cdot (Z_{lpha/2} + Z_{eta})^2 \cdot p(1-p)}{\delta^2}$$
Where:
- $lpha = 0.05 \implies Z_{lpha/2} = 1.96$ (95% Significance / 5% False Positive Rate)
- $eta = 0.20 \implies Z_{eta} = 0.84$ (80% Statistical Power)
- $p = 	ext{Baseline Conversion Rate}$
- $\delta = 	ext{Minimum Detectable Effect (MDE)}$

*Interviewer Follow-Up*: What is p-hacking and how do you prevent it?  
*(P-hacking occurs when experimenters continuously check p-values and stop tests early as soon as significance is reached. Prevent via fixed sample sizes or sequential testing frameworks like SPRT).*

---

### Q27 [P0][STATS]: Explain Simpson's Paradox with an enterprise analytics example.
**Explanation**: Simpson's Paradox occurs when a trend appears in several groups of data but disappears or reverses when the groups are combined.  
*Example*: Product conversion rate is higher for Variant B in both Mobile (5% vs 4%) and Desktop (20% vs 18%). However, Variant A has higher overall conversion (16% vs 8%) because Variant A was served predominantly to Desktop traffic (80% desktop), while Variant B was served predominantly to Mobile traffic (80% mobile). Segmenting by device isolates the true effect.

---

## Section 4: Exploratory Data Analysis & Metric Diagnostics

### Q36 [P0][CASE]: Overall platform conversion dropped 8% week-over-week. Walk me through your diagnostic tree.
```text
                          [Conversion Drops 8%]
                                    │
        ┌───────────────────────────┴───────────────────────────┐
        ▼                                                       ▼
[Mix Shift Effect]                                      [True Performance Drop]
        │                                                       │
 ┌──────┴──────┐                                         ┌──────┴──────┐
 ▼             ▼                                         ▼             ▼
[Traffic Shift][Channel Shift]                          [Technical Bug][Campaign Fatigue]
(More Mobile)  (Organic vs Paid)                        (Payment Gateway)
```
1. **Mix Shift vs Rate Shift**: Check if traffic shifted toward lower-converting segments (e.g. increase in mobile visitors who convert at 2% vs desktop at 6%).
2. **Funnel Decomposition**: Step 1 (Homepage) -> Step 2 (Product Page) -> Step 3 (Cart) -> Step 4 (Payment Success). Pinpoint which specific step suffered the drop.
3. **External Factors**: Public holidays, regional festivals, competitor promotional campaigns.

---

## Section 5: Behavioral & Civil-to-Analytics Bridge

### Q46 [P0][CAREER]: Why transition from Civil/HWRE to Data Analytics?
* **Model Structure**:
  * *"In Civil and Water Resources Engineering, we model complex physical phenomena (streamflow forecasting, flood frequency, sediment transport) using large time-series datasets, statistical probability distributions, and Python numerical libraries."*
  * *"I realized my core passion is finding actionable patterns in unstructured data and optimizing systems mathematically. Transitioning to Data Analytics allows me to apply the same statistical rigor to commercial metrics, user behavior, and enterprise decision-making."*
