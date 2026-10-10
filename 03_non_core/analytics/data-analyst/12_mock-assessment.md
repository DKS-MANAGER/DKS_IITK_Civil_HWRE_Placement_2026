# 12. Data Analyst: Technical Mock Assessment & Scoring Rubric

> **Assessment Type**: Comprehensive Timed Practice Mock (`[PREPARATION HEURISTIC]`)  
> **Simulated Duration**: 90 Minutes | **Total Marks**: 100  
> **Target Roles**: Data Analyst, Business Intelligence Analyst, Analytics Associate  
> **Core Skills Evaluated**: Advanced SQL Live Querying, Data Quality & Cleaning Diagnostics, Statistical Inference, Dashboard & KPI Design, Real-World Business Reporting.

---

## ⏱️ Assessment Structure & Time Management

| Section | Domain Focus | Question Count | Recommended Time | Marks |
| :---: | :--- | :---: | :---: | :---: |
| **Section 1** | **Advanced SQL Live Querying** | 3 Problems | 25 Minutes | 30 Marks |
| **Section 2** | **Data Quality & Pipeline Hygiene** | 3 Problems | 15 Minutes | 20 Marks |
| **Section 3** | **Descriptive Statistics & Inference** | 3 Problems | 15 Minutes | 15 Marks |
| **Section 4** | **Dashboard Architecture & Visualization** | 2 Problems | 15 Minutes | 15 Marks |
| **Section 5** | **Business Reporting & Cohort Caselet** | 1 Caselet (3 Parts) | 20 Minutes | 20 Marks |
| **TOTAL** | **Comprehensive Evaluation** | **12 Tasks** | **90 Minutes** | **100 Marks** |

---

## SECTION 1: Advanced SQL Live Querying (30 Marks)

### Problem 1.1: Rolling 3-Day Revenue & Anomaly Flag (10 Marks)
**Table Schema**: `orders(order_id INT, customer_id INT, order_date DATE, order_amount DECIMAL(10,2), status VARCHAR(20))`  
*Assumption*: Filter for `status = 'COMPLETED'`. Orders occur multiple times per day.

**Task**: Write a standard SQL query to calculate:
1. The total daily completed revenue.
2. The trailing 3-day moving average of daily revenue (current day and prior 2 days).
3. An anomaly flag (`1` if current day's revenue exceeds $1.5 \times$ the 3-day moving average, else `0`).

---

### Problem 1.2: Customer First-Purchase to Second-Purchase Latency (10 Marks)
**Table Schema**: `transactions(transaction_id INT, user_id INT, transaction_timestamp TIMESTAMP, amount DECIMAL(10,2))`  
*Assumption*: Table contains repeat customer transactions.

**Task**: Write a SQL query using window functions (`ROW_NUMBER` or `LEAD`) to calculate:
1. For customers with $\ge 2$ transactions, find the date of their 1st transaction and 2nd transaction.
2. The latency in days between 1st and 2nd transaction.
3. The overall platform average latency (in days) between 1st and 2nd purchase across all qualifying users.

---

### Problem 1.3: Resolving Duplicate Records with Non-Unique Grain (10 Marks)
**Table Schema**: `user_logins(session_id VARCHAR(50), user_id INT, login_time TIMESTAMP, device_type VARCHAR(20), ip_address VARCHAR(45))`  
*Context*: An ETL glitch inserted exact duplicates for some `(user_id, login_time)` pairs, plus near-duplicates where `device_type` differed due to parallel browser tabs.

**Task**: Write a single SQL deduplication script using a Common Table Expression (CTE) and `ROW_NUMBER()` that:
1. Groups logins by `(user_id, CAST(login_time AS DATE), device_type)`.
2. Retains strictly the earliest `login_time` per user per device per calendar day.
3. Outputs clean rows ready for downstream analytics insertion.

---

## SECTION 2: Data Quality & Pipeline Hygiene (20 Marks)

### Problem 2.1: Join Grain Mismatch & Multiplication Bug (7 Marks)
An analyst runs this query to report monthly department payroll:
```sql
SELECT d.dept_name, SUM(e.salary) AS total_payroll
FROM departments d
JOIN employees e ON d.dept_id = e.dept_id
JOIN projects p ON d.dept_id = p.dept_id
GROUP BY d.dept_name;
```
1. **Diagnosis**: Why will `total_payroll` be grossly overstated in departments that have multiple active projects?
2. **Remediation**: Rewrite the query or explain the correct architectural approach to eliminate the row duplication.

---

### Problem 2.2: Missing Value Strategy in Transaction Logs (6 Marks)
In an e-commerce event table with 2,000,000 rows, the column `delivery_cost` has 12% `NULL` values.
1. When is it appropriate to impute `delivery_cost` using the median versus dropping the records?
2. How does using `COALESCE(delivery_cost, 0)` distort calculations of `AVG(delivery_cost)`?

---

### Problem 2.3: Data Type & Timezone Integrity (7 Marks)
A global rideshare platform stores timestamps as strings: `"2026-10-01 14:30:00+05:30"`.
1. Explain two failure modes that occur if timestamps are filtered or ordered as raw `VARCHAR` strings without casting to UTC `TIMESTAMP WITH TIME ZONE`.
2. How does daylight saving time (DST) transition introduce artificial gaps or duplicate timestamps in localized timestamps?

---

## SECTION 3: Descriptive Statistics & Inference (15 Marks)

### Problem 3.1: Skewness & Central Tendency in Customer Spend (5 Marks)
A subscription app records monthly spending across 100,000 users. The distribution has:
- $\text{Mean} = \$48.50$
- $\text{Median} = \$19.00$
- $\text{Mode} = \$9.99$
- $\text{Standard Deviation} = \$112.00$

1. Is the distribution symmetric, left-skewed, or right-skewed? Explain with mathematical justification.
2. In an executive meeting with the Chief Product Officer, which metric (Mean or Median) should you present as the typical customer's monthly value? Why?

---

### Problem 3.2: Confidence Intervals on Click-Through Rate (5 Marks)
A marketing email campaign was delivered to $n = 2,500$ recipients, generating $X = 200$ clicks.
1. Calculate the sample proportion $\hat{p}$.
2. Compute the 95% Wald confidence interval for the true population CTR ($Z_{0.025} = 1.96$). Show all intermediate steps.

---

### Problem 3.3: Interpreting P-Values & Statistical Significance (5 Marks)
An analyst runs an A/B test on checkout page button colors. The test yields a difference in conversion with $p = 0.038$.
1. True or False: "There is a 96.2% probability that the new button is better than the old button." Explain why this statement is correct or incorrect.
2. If the baseline conversion was $2.00\%$ and the new button achieved $2.02\%$ ($p = 0.038$, $n = 500,000$ per variant), distinguish between **statistical significance** and **practical business significance**.

---

## SECTION 4: Dashboard Architecture & Visualization (15 Marks)

### Problem 4.1: Chart Selection Matrix (7 Marks)
For each analytical objective below, select the most effective visualization type from the choices (Bar Chart, Stacked Bar Chart, Line Chart, Scatter Plot, Heatmap, Box Plot) and justify your choice:
1. Comparing the monthly churn rate trends across 4 geographic regions over 24 consecutive months.
2. Showing the distribution and outlier spread of order fulfillment times across 6 warehouse distribution centers.
3. Evaluating the correlation between discount percentage offered and customer return rate across 10,000 products.

---

### Problem 4.2: Audit of a Misleading Executive Visual (8 Marks)
An analyst presents a bar chart claiming: *"Revenue doubled after the Q3 platform redesign!"*
Upon inspection:
- The y-axis starts at $\$480,000$ rather than $\$0$.
- Q2 Revenue was $\$500,000$ (bar height: 20 units above axis).
- Q3 Revenue was $\$520,000$ (bar height: 40 units above axis).

1. What visual perception flaw occurred? By what visual factor does the bar height difference exaggerate the actual percentage revenue increase?
2. Propose two concrete design standards that should be added to the company's Business Intelligence style guide to prevent deceptive reporting.

---

## SECTION 5: Real-World Business Reporting & Cohort Caselet (20 Marks)

### Case Scenario: SaaS B2B Retention Drop
You are the Data Analyst for a B2B project-management SaaS product. Management observed that Annual Recurring Revenue (ARR) growth slowed from $+35\%$ YoY to $+12\%$ YoY. You extract the following monthly cohort retention matrix:

| Cohort Month | New Accounts | Month 1 Retention | Month 3 Retention | Month 6 Retention | Month 12 Retention |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Jan 2025** | 1,000 | 85% | 72% | 65% | 61% |
| **Apr 2025** | 1,200 | 84% | 71% | 63% | 59% |
| **Jul 2025** | 1,500 | 81% | 64% | 51% | 42% |
| **Oct 2025** | 1,800 | 74% | 52% | 38% | — |

#### Part A: Quantitative Diagnostics (7 Marks)
1. What pattern is evident when comparing the Jul 2025 and Oct 2025 cohorts against the baseline Jan 2025 cohort?
2. Calculate the number of retained paying accounts from the **Jul 2025** cohort at Month 6 versus the **Jan 2025** cohort at Month 6.

#### Part B: Root Cause Decomposition (7 Marks)
List 3 hypotheses that explain why later cohorts degraded faster than early cohorts (e.g., changes in customer acquisition channels, product pricing tier changes, onboard feature friction). Outline the specific SQL queries or dataset joins needed to test each hypothesis.

#### Part C: Executive Recommendation (6 Marks)
Draft a 4-bullet executive synthesis for the VP of Operations and VP of Product following the Pyramid Principle: lead with the core finding, provide two supporting data points, and outline immediate recommended operational interventions.

---

# 📝 Comprehensive Solutions & Scoring Rubric

## Section 1 Solutions (SQL Live Querying)

### Solution 1.1: Rolling 3-Day Revenue
```sql
WITH DailyRevenue AS (
    SELECT 
        order_date,
        SUM(order_amount) AS daily_rev
    FROM orders
    WHERE status = 'COMPLETED'
    GROUP BY order_date
),
RollingStats AS (
    SELECT 
        order_date,
        daily_rev,
        AVG(daily_rev) OVER (
            ORDER BY order_date 
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ) AS moving_avg_3d
    FROM DailyRevenue
)
SELECT 
    order_date,
    daily_rev,
    ROUND(moving_avg_3d, 2) AS moving_avg_3d,
    CASE 
        WHEN daily_rev > 1.5 * moving_avg_3d THEN 1 
        ELSE 0 
    END AS anomaly_flag
FROM RollingStats
ORDER BY order_date;
```
*Grading Rubric (10 Marks)*:
- Correct aggregation to daily grain: 3 Marks
- Correct `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW`: 4 Marks
- Correct anomaly flag logic & clean syntax: 3 Marks

---

### Solution 1.2: Customer First-to-Second Purchase Latency
```sql
WITH RankedPurchases AS (
    SELECT 
        user_id,
        CAST(transaction_timestamp AS DATE) AS tx_date,
        ROW_NUMBER() OVER (
            PARTITION BY user_id 
            ORDER BY transaction_timestamp ASC
        ) AS order_num
    FROM transactions
),
FirstTwoOrders AS (
    SELECT 
        user_id,
        MAX(CASE WHEN order_num = 1 THEN tx_date END) AS first_order_date,
        MAX(CASE WHEN order_num = 2 THEN tx_date END) AS second_order_date
    FROM RankedPurchases
    WHERE order_num IN (1, 2)
    GROUP BY user_id
    HAVING COUNT(order_num) = 2
),
LatencyPerUser AS (
    SELECT 
        user_id,
        first_order_date,
        second_order_date,
        (second_order_date - first_order_date) AS days_to_second_purchase
    FROM FirstTwoOrders
)
SELECT 
    ROUND(AVG(days_to_second_purchase), 2) AS platform_avg_days_to_second_purchase,
    COUNT(user_id) AS qualifying_users_count
FROM LatencyPerUser;
```
*Grading Rubric (10 Marks)*:
- Window function partitioning by `user_id` ordered by time: 3 Marks
- Filtering customers with $\ge 2$ transactions correctly: 3 Marks
- Correct date difference arithmetic and platform aggregation: 4 Marks

---

### Solution 1.3: Deduplication Script
```sql
WITH DeduplicatedLogins AS (
    SELECT 
        session_id,
        user_id,
        login_time,
        device_type,
        ip_address,
        ROW_NUMBER() OVER (
            PARTITION BY user_id, CAST(login_time AS DATE), device_type
            ORDER BY login_time ASC, session_id ASC
        ) AS rnk
    FROM user_logins
)
SELECT 
    session_id,
    user_id,
    login_time,
    device_type,
    ip_address
FROM DeduplicatedLogins
WHERE rnk = 1;
```
*Grading Rubric (10 Marks)*:
- Correct partition grain `(user_id, CAST(login_time AS DATE), device_type)`: 4 Marks
- Deterministic ordering by `login_time ASC`: 3 Marks
- Clean CTE filtering `WHERE rnk = 1`: 3 Marks

---

## Section 2 Solutions (Data Quality & Hygiene)

### Solution 2.1: Join Grain Mismatch
1. **Diagnosis (3 Marks)**: A department with 5 employees and 4 projects produces $5 \times 4 = 20$ joined rows. Each employee's salary is duplicated 4 times across the project join, inflating `SUM(salary)` by $4\times$.
2. **Remediation (4 Marks)**: Aggregate payroll independently before joining:
```sql
WITH DeptPayroll AS (
    SELECT dept_id, SUM(salary) AS total_payroll
    FROM employees
    GROUP BY dept_id
)
SELECT d.dept_name, COALESCE(p.total_payroll, 0) AS total_payroll
FROM departments d
LEFT JOIN DeptPayroll p ON d.dept_id = p.dept_id;
```

---

### Solution 2.2: Missing Value Strategy
1. **Median vs Drop (3 Marks)**: Drop records only if missing completely at random (MCAR) and dataset loss is trivial ($<1\%$). For 12% missing, dropping introduces severe selection bias. Median imputation is appropriate if missingness is due to unmetered standard shipping; otherwise, model shipping cost by distance/weight segment.
2. **Coalesce Distortion (3 Marks)**: `COALESCE(delivery_cost, 0)` treats missing values as $0.00. This artificially drags the mean downwards by adding 240,000 zero-value entries into the denominator of `AVG()`.

---

### Solution 2.3: Timezone & Timestamp Integrity
1. **Failure Modes (4 Marks)**:
   - String sorting orders alphabetically rather than chronologically (e.g., offsets `+05:30` vs `+00:00` sort incorrectly).
   - Date truncations like `SUBSTRING(..., 10)` group records into wrong local days during midnight crossovers.
2. **DST Impact (3 Marks)**: During clock fall-back (e.g., 2:00 AM back to 1:00 AM), events between 1:00 AM and 2:00 AM appear twice in local timestamps, making time-difference calculations negative or zero.

---

## Section 3 Solutions (Statistics & Inference)

### Solution 3.1: Skewness & Central Tendency
1. **Mathematical Justification (2.5 Marks)**: $\text{Mean } (\$48.50) > \text{Median } (\$19.00) > \text{Mode } (\$9.99)$. The distribution is **right-skewed (positively skewed)** with a long right tail of high spenders.
2. **Metric Selection (2.5 Marks)**: Present the **Median** ($\$19.00$). The mean ($\$48.50$) is heavily inflated by top 1% power users and misrepresents the typical customer's spending.

---

### Solution 3.2: Confidence Intervals on CTR
1. **Sample Proportion (2 Marks)**: $\hat{p} = \frac{200}{2,500} = 0.080 \text{ (8.00\%)}$.
2. **Standard Error & 95% CI (3 Marks)**:
   $$SE = \sqrt{\frac{\hat{p}(1-\hat{p})}{n}} = \sqrt{\frac{0.08 \times 0.92}{2,500}} = \sqrt{\frac{0.0736}{2,500}} = \sqrt{0.00002944} \approx 0.005426 \text{ (0.543\%)}$$
   $$\text{CI}_{95\%} = 0.08 \pm 1.96 \times 0.005426 = 0.08 \pm 0.01064 \implies [0.0694, 0.0906] \text{ or } [6.94\%, 9.06\%]$$

---

### Solution 3.3: Interpreting P-Values
1. **True/False (2.5 Marks)**: **False**. A p-value is $P(\text{Data as extreme or more} \mid H_0 \text{ is true})$, NOT the posterior probability that $H_1$ is true. That inverse probability requires Bayesian inference with prior probability.
2. **Statistical vs Business Significance (2.5 Marks)**: With $n = 500,000$, standard error is tiny, detecting a tiny $+0.02\%$ lift with $p = 0.038$. However, an increase of $+0.02\%$ may yield negligible additional revenue that fails to cover the engineering cost of deploying the change.

---

## Section 4 Solutions (Visualization & Dashboard Architecture)

### Solution 4.1: Chart Selection Matrix
1. **Monthly Churn across 4 Regions over 24 Months (2.5 Marks)**: **Multi-Line Chart**. Continuous temporal trend with distinct colored lines for each region allows immediate comparative trend evaluation.
2. **Fulfillment Time Distribution across 6 Warehouses (2.5 Marks)**: **Box Plot (Box-and-Whisker)**. Accurately visualizes medians, interquartile ranges (IQR), and extreme operational outliers across categories.
3. **Discount % vs Product Return Rate across 10,000 items (2 Marks)**: **Scatter Plot (with opacity/alpha or Hexbin)**. Displays bivariate relationship, non-linear clustering, and correlation without aggregation loss.

---

### Solution 4.2: Audit of Misleading Visual
1. **Visual Flaw (4 Marks)**: Truncated y-axis (baseline starting at $\$480\text{k}$). A $4\%$ actual revenue increase ($\$500\text{k} \to \$520\text{k}$) was represented as a $100\%$ bar height increase ($20\text{ units} \to 40\text{ units}$), exaggerating visual perception by **$25\times$**.
2. **BI Governance Standards (4 Marks)**:
   - Standard 1: All bar and column charts must include a zero-origin baseline ($y = 0$).
   - Standard 2: If truncated axes are necessary (e.g., stock price indices), visual broken-axis indicators must be mandatory and paired with explicit percentage labels.

---

## Section 5 Solutions (Business Reporting & Cohort Caselet)

### Part A: Diagnostics (7 Marks)
1. **Pattern (3.5 Marks)**: Severe cohort decay over calendar time. Month 6 retention dropped monotonically from $65\%$ in Jan 2025 to $51\%$ in Jul 2025, and Month 3 retention crashed from $72\%$ (Jan) to $52\%$ (Oct).
2. **Cohort Size Calculation (3.5 Marks)**:
   - Jan 2025 Month 6 Retained: $1,000 \times 65\% = \mathbf{650 \text{ accounts}}$.
   - Jul 2025 Month 6 Retained: $1,500 \times 51\% = \mathbf{765 \text{ accounts}}$.
   - *Observation*: Despite acquiring 50% more users in July, the platform retains only 115 more accounts due to accelerated churn.

---

### Part B: Root Cause Decomposition (7 Marks)
1. **Channel Quality Dilution**: Influx of low-intent users from aggressive paid marketing. *SQL test*: Join `cohort_users` with `acquisition_channel` and compare retention curves by channel (Organic vs Paid Ads).
2. **Product Redesign / Onboarding Friction**: A feature update launched around June/July broken onboarding. *SQL test*: Query user activation event completion within the first 7 days across cohort signup dates.
3. **Discount Expiration Shock**: Free trial or deep discount introduced in Q3 expired at Month 3. *SQL test*: Join billing table and check churn timestamp correlation with first full-price invoice date.

---

### Part C: Executive Recommendation (6 Marks)
* **Core Finding**: *"Platform acquisition growth (+80% signup volume) is masking critical structural cohort decay: 6-month retention has dropped 14 percentage points (65% to 51%), threatening annual recurring revenue renewal."*
* **Supporting Data**:
  1. Oct cohort Month 3 retention collapsed to 52% (vs 72% in Jan baseline).
  2. 49% of July accounts churned before Month 6, eroding Customer Lifetime Value (LTV).
* **Operational Action**:
  - Immediately audit Q3 marketing channels for low-intent signup inflation.
  - Implement automated in-app onboarding telemetry checkpoints to identify week-1 drop-off triggers.

---

## 📊 Comprehensive Scoring & Performance Rubric

| Composite Score | Performance Classification | Diagnostic Profile & Recommended Action |
| :---: | :---: | :--- |
| **85 – 100** | **Strong (Tier 1 Ready)** | Demonstrates complete mastery of SQL window functions, statistical inference, data hygiene, and business synthesis. Ready for Day 1 Analyst roles. |
| **70 – 84** | **Interview-Ready** | Solves core SQL and statistical questions with minor syntax or calculation flaws. Capable of passing standard campus technical assessments. |
| **50 – 69** | **Developing** | Solves standard queries but struggles with window frame semantics, grain mismatches, or executive communication. Focus on Section 1 & Section 5 drills. |
| **< 50** | **Awareness Stage** | Fundamental gaps in relational modeling and statistical confidence intervals. Prioritize studying [`04_tools-and-technical-stack.md`](04_tools-and-technical-stack.md) and [`03_domain-knowledge.md`](03_domain-knowledge.md). |
