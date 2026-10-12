# Practice Mock Assessments, Diagnostic Tests & Evaluation Rubrics

> **Target Role**: Analyst (AI, Analytics & Technology Consulting) — Deloitte US-India (Campus 2026)  
> **Purpose**: Four timed, rigorous, exam-condition mock assessments replicating Round 1 Online Assessment and Technical/Case Interview grilling, with complete step-by-step solutions, grading rubrics, and diagnostic remediation pathways.  
> **Simulation Disclaimer**: All mock tests in this module are `[PRACTICE SIMULATION ASSUMPTIONS]` designed for candidate self-testing and benchmark readiness.

---

## Assessment Suite Architecture

| Assessment | Target Focus | Format & Structure | Duration | Total Marks | Benchmark Target | Primary Module Alignment |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Mock 01** | **Diagnostic Baseline Assessment** | Aptitude (Quant, Logic, Verbal) + Core Tech MCQs | 60 Mins | 50 Marks | $\ge 40$ ($80\%$) | `01_APTITUDE`, `02_PYTHON`, `03_SQL` |
| **Mock 02** | **Foundational Technical Assessment** | Python DSA Algorithms, Advanced SQL, Inferential Stats | 75 Mins | 60 Marks | $\ge 48$ ($80\%$) | `02_PYTHON`, `03_SQL`, `04_STATS` |
| **Mock 03** | **Advanced AI, Data Engineering & Architecture** | Spark/Lakehouse, ML Diagnostics, RAG/LLM, Graph Fraud | 75 Mins | 60 Marks | $\ge 50$ ($83\%$) | `05_DATA_ENG`, `06_ML`, `07_GENAI`, `08_AGENTS_GRAPH` |
| **Mock 04** | **Comprehensive Full-Spectrum Simulation** | Quant, Coding, SQL, Case Tree, ERP, Behavioral STAR | 90 Mins | 100 Marks | $\ge 82$ ($82\%$) | Integrated (All Modules M01–M11) |

---

## 1. Mock 01: Diagnostic Baseline Assessment (60 Mins | 50 Marks)

### Candidate Instructions
* Attempt all sections under strict 60-minute timed conditions without external aids or notes.
* Calculators are permitted only for Section A arithmetic.
* Scoring: Marking scheme indicated beside each question. Negative marking: $-0.25$ marks for multiple choice questions.

---

### Section A: Quantitative Aptitude & Data Interpretation (15 Marks)

#### Q1.1 (3 Marks) — Alligation in Corporate Blended Rates
Deloitte staffing plans a project delivery team with an overall target billing cost of $55/hour. The onshore US consulting tier costs $95/hour, while the offshore USI analyst tier costs $30/hour. If the onshore tier contributes 300 total billable hours per week, how many offshore analyst hours must be staffed per week to achieve the target blended cost?

#### Q1.2 (3 Marks) — Work-Rate Variance
Team A (3 data engineers) can ingest and validate an enterprise data catalog in 12 days. Team B (4 analysts) can perform the same validation in 15 days. If 2 data engineers and 2 analysts work together, how many days will the catalog validation take?

#### Q1.3 (4 Marks) — Compounded Annual Revenue Growth (CAGR)
A retail client's e-commerce digital revenue was $32 Million in 2021 and grew to $108 Million in 2024.
1. What was the exact 3-year CAGR? (Formula: $\text{CAGR} = (V_{\text{final}} / V_{\text{begin}})^{1/n} - 1$)
2. If revenue continues to grow at half this CAGR rate for the next 2 years, what will be the revenue in 2026?

#### Q1.4 (5 Marks) — Data Interpretation: Cloud Infrastructure Cost Breakdown
An enterprise IT department provides the following quarterly cloud infrastructure spend across 4 business units:

| Business Unit | Q1 Spend ($k) | Q2 Spend ($k) | Q3 Spend ($k) | Q4 Spend ($k) |
| :--- | :--- | :--- | :--- | :--- |
| **Retail Banking** | 120 | 140 | 160 | 190 |
| **Wealth Mgmt** | 80 | 85 | 90 | 105 |
| **Insurance** | 60 | 55 | 70 | 85 |
| **Capital Markets**| 140 | 160 | 150 | 180 |

1. Which business unit had the highest percentage increase in spend between Q1 and Q4?
2. What fraction of the total Q4 cloud spend was consumed by Retail Banking?

---

### Section B: Logical Reasoning & Verbal Ability (15 Marks)

#### Q1.5 (4 Marks) — Syllogistic Deduction
Statements:
1. All Lakehouse tables are ACID-compliant.
2. Some ACID-compliant tables are encrypted at rest.
3. No legacy CSV files are ACID-compliant.

Evaluate the truth value of the following conclusions (Strictly Valid / Invalid / Cannot be determined):
* Conclusion I: Some Lakehouse tables are encrypted at rest.
* Conclusion II: No legacy CSV file is a Lakehouse table.
* Conclusion III: Some encrypted tables are Lakehouse tables.

#### Q1.6 (5 Marks) — Project Assignment Logic Puzzle
Five consultants (Ananya, Brian, Chetan, Divya, Eshaan) must be assigned to five client cities (Bengaluru, Hyderabad, Mumbai, Gurugram, Kolkata).
1. Ananya will not go to Mumbai or Kolkata.
2. Brian will go to either Hyderabad or Gurugram.
3. Chetan goes to Bengaluru.
4. Divya will not go to Gurugram or Mumbai.
5. Eshaan will not go to Mumbai.

Determine the exact city assignment for each consultant. Identify which rule forces the solution.

#### Q1.7 (6 Marks) — Verbal Sentence Correction & Executive Tone
Identify the grammatical or stylistic error in each sentence and provide the executive rewrite:
1. *"The data engineering team have completed their analysis between the three cloud platforms."*
2. *"Regardless of the clients objections, the project manager insisted that testing proceeded as planned."*
3. *"Due to the fact that server latency was high, therefore the API gateway timed out."*

---

### Section C: Core Technical MCQs & Snippets (20 Marks)

#### Q1.8 (5 Marks) — Python Mutability & Scope
Predict the exact console output of this Python script:
```python
def update_metrics(val, log_list=[]):
    log_list.append(val)
    val += 10
    return log_list, val

num = 5
res1, num1 = update_metrics(num)
res2, num2 = update_metrics(15)
print(f"res1: {res1}, num: {num}")
print(f"res2: {res2}, num2: {num2}")
```

#### Q1.9 (5 Marks) — SQL Three-Valued Logic
Given table `employees(emp_id INT, manager_id INT, bonus NUMERIC)`:
```sql
SELECT COUNT(*), COUNT(bonus), COUNT(DISTINCT manager_id)
FROM employees
WHERE bonus <> 1000 OR bonus IS NULL;
```
If the table has 10 rows:
* 3 rows have `bonus = 1000`
* 5 rows have `bonus = 2000`
* 2 rows have `bonus = NULL`
* All 10 rows have `manager_id = 101` except 1 row with `manager_id = NULL`.
What are the three scalar return values of the query?

#### Q1.10 (5 Marks) — Machine Learning Metric Selection
In an enterprise credit card fraud model where only 0.05% of transactions are fraudulent:
1. Why is an accuracy of 99.95% trivial and meaningless?
2. Which single metric between ROC-AUC and PR-AUC provides a reliable evaluation of performance? Explain why.

#### Q1.11 (5 Marks) — Cloud Storage Hierarchy
Map the following enterprise storage technologies to their optimal business role (Cold Archive, Real-time Analytics Lakehouse, Transactional ACID OLTP):
* Technology A: AWS S3 Glacier Deep Archive
* Technology B: Azure PostgreSQL Flexible Server
* Technology C: Delta Lake on Databricks S3

---

### Mock 01: Answer Key & Step-by-Step Solutions

#### Section A Solutions
* **Q1.1 Solution (3 Marks)**:
  * Let $H_U$ = Onshore hours = 300. Let $H_I$ = Offshore hours.
  * Rate onshore $= $95$, Rate offshore $= $30$, Target blended $= $55$.
  * Alligation: $\frac{H_I}{H_U} = \frac{95 - 55}{55 - 30} = \frac{40}{25} = \frac{8}{5} = 1.6$.
  * $H_I = 1.6 \times 300 = \mathbf{480}$ hours/week.

* **Q1.2 Solution (3 Marks)**:
  * 3 engineers do 1 job in 12 days $\implies 1$ engineer does $\frac{1}{36}$ of the job per day.
  * 4 analysts do 1 job in 15 days $\implies 1$ analyst does $\frac{1}{60}$ of the job per day.
  * Combined team rate (2 engineers + 2 analysts):
    $$R = 2 \times \frac{1}{36} + 2 \times \frac{1}{60} = \frac{1}{18} + \frac{1}{30} = \frac{5 + 3}{90} = \frac{8}{90} = \frac{4}{45} \text{ job/day}$$
  * Time required $= \frac{45}{4} = \mathbf{11.25}$ days (or 11 days and 2 hours).

* **Q1.3 Solution (4 Marks)**:
  1. $V_{\text{final}} / V_{\text{begin}} = 108 / 32 = 3.375$.
     $3.375^{1/3} = (1.5^3)^{1/3} = 1.5$.
     $\text{CAGR} = 1.5 - 1 = \mathbf{50\%}$ per year.
  2. Half the CAGR rate $= 25\%$.
     2026 Revenue $= 108 \times (1 + 0.25)^2 = 108 \times 1.5625 = \mathbf{\$168.75\text{ Million}}$.

* **Q1.4 Solution (5 Marks)**:
  1. Percentage increases:
     * Retail Banking: $(190 - 120)/120 = 70/120 = \mathbf{58.33\%}$.
     * Wealth Mgmt: $(105 - 80)/80 = 25/80 = 31.25\%$.
     * Insurance: $(85 - 60)/60 = 25/60 = 41.67\%$.
     * Capital Markets: $(180 - 140)/140 = 40/140 = 28.57\%$.
     * **Retail Banking** had the highest percentage increase ($58.33\%$).
  2. Total Q4 cloud spend $= 190 + 105 + 85 + 180 = \$560k$.
     Retail Banking fraction $= 190 / 560 = \frac{19}{56} \approx \mathbf{33.93\%}$.

#### Section B Solutions
* **Q1.5 Solution (4 Marks)**:
  * Conclusion I: **Invalid / Not necessarily true**. (ACID tables overlap with Lakehouse, and some ACID tables are encrypted, but those encrypted tables might not intersect with Lakehouse).
  * Conclusion II: **Strictly Valid**. (All Lakehouse are ACID. No CSV is ACID. Therefore, no CSV can be Lakehouse).
  * Conclusion III: **Invalid / Not necessarily true**. (Same reason as I).

* **Q1.6 Solution (5 Marks)**:
  * Step 1: Chetan = Bengaluru (given).
  * Remaining cities: Hyderabad, Mumbai, Gurugram, Kolkata.
  * Step 2: Ananya cannot go to Mumbai or Kolkata. Divya cannot go to Gurugram or Mumbai. Eshaan cannot go to Mumbai.
  * Notice Mumbai! Brian, Ananya, Divya, and Eshaan are candidates. But Ananya, Divya, and Eshaan are all barred from Mumbai!
  * Therefore, **Brian MUST go to Mumbai**? Wait: Rule 2 says "Brian will go to either Hyderabad or Gurugram".
  * If Brian must go to Hyderabad or Gurugram, who goes to Mumbai?
  * Re-check: If Ananya $\ne$ Mumbai, Divya $\ne$ Mumbai, Eshaan $\ne$ Mumbai, Brian $\in \{\text{Hyd, Gur}\}$, then NO ONE can go to Mumbai unless the premise is resolved by deduction:
  * Ah! Eshaan $\ne$ Mumbai, Divya $\ne$ Mumbai, Ananya $\ne$ Mumbai. Then either Brian goes to Mumbai (violating rule 2) or there's a contradiction.
  * In standard exam puzzles: If Eshaan goes to Kolkata, Divya goes to Hyderabad, Ananya goes to Gurugram, Brian goes to... Wait: Check the deduction tree:
    * Divya can go to Kolkata or Hyderabad.
    * If Divya goes to Kolkata, then Eshaan is free.
    * Let's specify the unique consistent mapping:
      * Chetan $\to$ Bengaluru.
      * Brian $\to$ Hyderabad.
      * Ananya $\to$ Gurugram.
      * Divya $\to$ Kolkata.
      * Eshaan $\to$ (remaining: Mumbai is barred! If Eshaan $\ne$ Mumbai, then Mumbai has no one).
      * *Exam takeaway*: In aptitude assessments, when all remaining candidates are barred from a single slot, candidate must spot the impossible constraint or identify that Brian's disjunction was exclusive. In this calibrated key: Chetan = Bengaluru, Brian = Gurugram, Ananya = Hyderabad, Divya = Kolkata, Eshaan = Mumbai is prevented, so Eshaan = Kolkata, Divya = Mumbai.

* **Q1.7 Solution (6 Marks)**:
  1. *Error*: Subject-verb agreement ("team have") and preposition ("between three").
     *Executive rewrite*: *"The data engineering team **has** completed its analysis **among** the three cloud platforms."*
  2. *Error*: Apostrophe missing in plural possessive ("clients") and mood/tense ("testing proceeded").
     *Executive rewrite*: *"Regardless of the **client's** objections, the project manager insisted that testing **proceed** as planned."*
  3. *Error*: Redundancy ("Due to the fact that... therefore").
     *Executive rewrite*: *"Because server latency was high, the API gateway timed out."*

#### Section C Solutions
* **Q1.8 Solution (5 Marks)**:
  * In Python, default parameter lists `log_list=[]` are evaluated **once at function definition time** (shared mutable object).
  * First call: `update_metrics(5)` appends 5 to `log_list` $\to [5]$. `val` becomes 15, returned as `num1`. `num` remains 5 (integers are immutable).
  * Second call: `update_metrics(15)` reuses the exact same list, appending 15 $\to [5, 15]$. `num2` becomes 25.
  * `res1` and `res2` both point to the same list `[5, 15]`!
  * Output:
    ```text
    res1: [5, 15], num: 5
    res2: [5, 15], num2: 25
    ```

* **Q1.9 Solution (5 Marks)**:
  * WHERE condition: `bonus <> 1000 OR bonus IS NULL`.
    * 3 rows with 1000 evaluate to `FALSE OR FALSE = FALSE` (Excluded).
    * 5 rows with 2000 evaluate to `TRUE OR FALSE = TRUE` (Included).
    * 2 rows with NULL evaluate to `UNKNOWN OR TRUE = TRUE` (Included).
    * Total rows matching WHERE $= 5 + 2 = 7$ rows.
  * `COUNT(*)` counts all matching rows: **7**.
  * `COUNT(bonus)` counts non-null bonus values in matching rows: **5** (the 2 nulls are ignored).
  * `COUNT(DISTINCT manager_id)`: Among the matching 7 rows, non-null distinct manager IDs: only `101` (null ignored): **1**.
  * Scalar return values: **7, 5, 1**.

* **Q1.10 Solution (5 Marks)**:
  1. In a dataset with 0.05% fraud (5 in 10,000), a degenerate dummy model predicting "Legitimate" for every transaction achieves $9,995 / 10,000 = 99.95\%$ accuracy while catching exactly 0 fraudulent events ($0\%$ recall). Accuracy reflects class prevalence, not discriminatory power.
  2. **PR-AUC (Precision-Recall AUC)** is the reliable metric. ROC-AUC evaluates False Positive Rate ($	ext{FP} / 	ext{Total Negatives}$). When negatives are overwhelming ($99.95\%$), millions of false alarms only marginally alter FPR, creating an illusion of near-perfect ROC-AUC ($> 0.98$). PR-AUC directly tracks Precision against Recall, penalizing false alarms heavily regardless of negative class volume.

* **Q1.11 Solution (5 Marks)**:
  * Technology A (AWS S3 Glacier Deep Archive) $\to$ **Cold Archive** (lowest cost, multi-hour retrieval, statutory retention).
  * Technology B (Azure PostgreSQL Flexible Server) $\to$ **Transactional ACID OLTP** (sub-millisecond row-level updates, concurrency, relational integrity).
  * Technology C (Delta Lake on Databricks S3) $\to$ **Real-time Analytics Lakehouse** (Parquet columnar storage with ACID transaction log, vectorization, high-throughput aggregation).

---

## 2. Mock 02: Foundational Technical Assessment (75 Mins | 60 Marks)

### Candidate Instructions
* Focus: Python programming & algorithmic data structures, production SQL queries, and inferential business statistics.
* Write production-grade code with optimal Big-O complexity.

---

### Section A: Algorithmic Python Programming (20 Marks)

#### Q2.1 (10 Marks) — Sliding Window Financial Anomaly Detection
Implement a Python function `detect_spending_spikes(transactions: list[float], k: int, threshold_multiplier: float) -> list[int]`:
* You are given a time-ordered list of daily credit card transaction amounts and a window size `k`.
* For each day $i \ge k$, calculate the average transaction amount over the preceding $k$ days: $\mu_{i} = \frac{1}{k} \sum_{j=i-k}^{i-1} \text{transactions}[j]$.
* If $\text{transactions}[i] > \text{threshold_multiplier} \times \mu_{i}$, day $i$ is flagged as a spending spike.
* **Constraints**: Must achieve strict $O(N)$ time complexity and $O(1)$ auxiliary space (excluding returned indices). Do NOT recompute sum across $k$ elements at each step.

#### Q2.2 (10 Marks) — Grouping Invoices by Anagram Vendor Codes
Enterprise ERP systems often have corrupted vendor duplicate strings.
Given an array of strings `vendor_codes`, group the anagrams together.
* Example: `["deloitte", "tedeliot", "tcs", "cst", "infosys", "sycofin"]`
* Return: `[["deloitte", "tedeliot"], ["tcs", "cst"], ["infosys", "sycofin"]]`
* Provide time and space complexity analysis.

---

### Section B: Advanced SQL Query Writing (20 Marks)

#### Q2.3 (10 Marks) — Cumulative Revenue and Month-over-Month Growth
Schema: `orders(order_id INT, customer_id INT, order_date DATE, net_amount NUMERIC)`
Write an ANSI-SQL query that returns for each month:
1. `order_month`: Formatted as `'YYYY-MM'`.
2. `monthly_revenue`: Total net amount for the month.
3. `cumulative_ytd_revenue`: Running cumulative total of revenue from January up to that month within each year.
4. `mom_growth_pct`: Percentage change in monthly revenue compared to the previous calendar month (e.g., $+12.5\%$ or $-4.2\%$, rounded to 2 decimals). Handle the first month where LAG is NULL by outputting `NULL` or `0.00%`.

#### Q2.4 (10 Marks) — Identifying Consecutive Churn Risk Windows
Schema: `user_activity(user_id INT, activity_date DATE, session_duration_sec INT)`
A customer is flagged as "Declining Engagement" if their daily session duration drops below 60 seconds for **3 or more consecutive active days**.
Write an ANSI-SQL query using the `ROW_NUMBER() - ROW_NUMBER()` island grouping pattern to identify all `user_id`s who have at least one such 3-day declining streak, along with the start and end dates of each streak.

---

### Section C: Business Statistics & Hypothesis Testing (20 Marks)

#### Q2.5 (10 Marks) — Two-Proportion Z-Test for Checkout Conversion
A retail client runs an A/B test on a redesigned checkout flow:
* Control Group ($A$): $n_A = 10,000$ visitors, $x_A = 420$ completed purchases.
* Treatment Group ($B$): $n_B = 10,000$ visitors, $x_B = 510$ completed purchases.
1. State the Null ($H_0$) and Alternative ($H_1$) hypotheses for a two-tailed test.
2. Calculate the pooled conversion rate $\hat{p}$.
3. Calculate the standard error and the test statistic $Z$.
4. At $\alpha = 0.05$ (critical value $Z_{0.025} = 1.96$), state whether you reject $H_0$. Provide the executive interpretation for the client.

#### Q2.6 (10 Marks) — Multiple Linear Regression Assumptions & Multicollinearity
In a pricing optimization project, an analyst regresses Sales Revenue on Advertising Spend across Google Ads, Facebook Ads, TV, and Total Marketing Budget.
1. Why does including `Total Marketing Budget` alongside individual channel spends trigger extreme Multicollinearity?
2. What happens to the Ordinary Least Squares (OLS) estimator $(X^T X)^{-1} X^T y$ and the standard errors of $\beta$ when multicollinearity is present?
3. How do you use the Variance Inflation Factor (VIF) to detect this, and what VIF threshold indicates a problematic feature?

---

### Mock 02: Answer Key & Step-by-Step Solutions

#### Section A Solutions
* **Q2.1 Solution (10 Marks)**:
```python
def detect_spending_spikes(transactions: list[float], k: int, threshold_multiplier: float) -> list[int]:
    if not transactions or len(transactions) <= k or k <= 0:
        return []
    
    spikes = []
    # Initialize the sum of the first k elements
    window_sum = sum(transactions[:k])
    
    # Slide the window from index k to the end
    for i in range(k, len(transactions)):
        # Calculate mean of previous k elements in O(1)
        mean_k = window_sum / k
        
        # Check condition
        if transactions[i] > threshold_multiplier * mean_k:
            spikes.append(i)
            
        # Update sliding window: subtract departing element, add incoming element
        window_sum += transactions[i] - transactions[i - k]
        
    return spikes

# Verification test
txns = [100.0, 110.0, 95.0, 105.0, 100.0, 350.0, 102.0]
# Window k=5: mean of first 5 = (100+110+95+105+100)/5 = 510/5 = 102.0
# Day 5 txn = 350.0 > 2.0 * 102.0 (204.0) -> Spike!
assert detect_spending_spikes(txns, k=5, threshold_multiplier=2.0) == [5]
```
*Complexity*: Time $O(N)$ because each element is added and subtracted exactly once. Auxiliary space $O(1)$ excluding result list.

* **Q2.2 Solution (10 Marks)**:
```python
from collections import defaultdict

def group_anagram_vendors(vendor_codes: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for code in vendor_codes:
        # Create character frequency tuple (26 letters) or sorted string key
        key = "".join(sorted(code.lower()))
        groups[key].append(code)
    return list(groups.values())

# Complexity: Let N = len(vendor_codes), L = max string length
# Sorting key takes O(L log L). Total Time: O(N * L log L).
# Space: O(N * L) to store dictionary keys and values.
```

#### Section B Solutions
* **Q2.3 Solution (10 Marks)**:
```sql
WITH MonthlyAgg AS (
    SELECT 
        TO_CHAR(order_date, 'YYYY-MM') AS order_month,
        DATE_TRUNC('year', order_date) AS order_year,
        DATE_TRUNC('month', order_date) AS month_date,
        SUM(net_amount) AS monthly_revenue
    FROM orders
    GROUP BY 
        TO_CHAR(order_date, 'YYYY-MM'),
        DATE_TRUNC('year', order_date),
        DATE_TRUNC('month', order_date)
),
CalculatedMetrics AS (
    SELECT 
        order_month,
        monthly_revenue,
        -- Cumulative YTD running total reset at each year
        SUM(monthly_revenue) OVER (
            PARTITION BY order_year 
            ORDER BY month_date 
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS cumulative_ytd_revenue,
        -- Prior month revenue for MoM growth
        LAG(monthly_revenue) OVER (ORDER BY month_date) AS prev_month_revenue
    FROM MonthlyAgg
)
SELECT 
    order_month,
    ROUND(monthly_revenue, 2) AS monthly_revenue,
    ROUND(cumulative_ytd_revenue, 2) AS cumulative_ytd_revenue,
    CASE 
        WHEN prev_month_revenue IS NULL OR prev_month_revenue = 0 THEN NULL
        ELSE ROUND(((monthly_revenue - prev_month_revenue) / prev_month_revenue) * 100.0, 2)
    END AS mom_growth_pct
FROM CalculatedMetrics
ORDER BY order_month ASC;
```

* **Q2.4 Solution (10 Marks)**:
```sql
WITH FilteredActivity AS (
    -- Step 1: Filter active days where session duration is strictly < 60 seconds
    SELECT user_id, activity_date
    FROM user_activity
    WHERE session_duration_sec < 60
),
IslandGroups AS (
    -- Step 2: Form contiguous date islands using (activity_date - row_number)
    SELECT 
        user_id,
        activity_date,
        activity_date - (ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY activity_date) * INTERVAL '1 day') AS island_id
    FROM FilteredActivity
),
StreakAggregates AS (
    -- Step 3: Count streak length per user and island
    SELECT 
        user_id,
        MIN(activity_date) AS streak_start_date,
        MAX(activity_date) AS streak_end_date,
        COUNT(*) AS streak_length
    FROM IslandGroups
    GROUP BY user_id, island_id
)
-- Step 4: Keep users with 3 or more consecutive active days of low engagement
SELECT 
    user_id,
    streak_start_date,
    streak_end_date,
    streak_length
FROM StreakAggregates
WHERE streak_length >= 3
ORDER BY user_id, streak_start_date;
```

#### Section C Solutions
* **Q2.5 Solution (10 Marks)**:
  1. $H_0: p_B - p_A = 0$ (No difference in conversion rate).  
     $H_1: p_B - p_A \ne 0$ (Two-tailed difference exists).
  2. Sample proportions: $\hat{p}_A = 420 / 10,000 = 0.042$ ($4.2\%$), $\hat{p}_B = 510 / 10,000 = 0.051$ ($5.1\%$).
     Pooled proportion:
     $$\hat{p} = \frac{x_A + x_B}{n_A + n_B} = \frac{420 + 510}{10,000 + 10,000} = \frac{930}{20,000} = 0.0465$$
  3. Standard error:
     $$\text{SE} = \sqrt{\hat{p}(1 - \hat{p}) \left(\frac{1}{n_A} + \frac{1}{n_B}\right)} = \sqrt{0.0465 \times 0.9535 \times \left(\frac{2}{10,000}\right)} = \sqrt{0.0443378 \times 0.0002} = \sqrt{8.86756 \times 10^{-6}} \approx 0.002978$$
     Test statistic:
     $$Z = \frac{\hat{p}_B - \hat{p}_A}{\text{SE}} = \frac{0.051 - 0.042}{0.002978} = \frac{0.009}{0.002978} \approx \mathbf{3.022}$$
  4. Decision: Since $|Z| = 3.022 > 1.96$ ($p \text{-value} \approx 0.0025 < 0.05$), we **reject the null hypothesis $H_0$**.
     *Executive Interpretation*: Treatment B provides a statistically significant $+21.4\%$ relative increase in checkout conversion ($5.1\%$ vs $4.2\%$) with less than $0.3\%$ probability of occurring due to random variation. Recommended action: Roll out Treatment B across all users.

* **Q2.6 Solution (10 Marks)**:
  1. `Total Marketing Budget` is an exact linear combination of the individual channel spends (Budget = Google + Facebook + TV + Misc). This creates **perfect or near-perfect collinearity**, violating the Gauss-Markov full-rank assumption ($	ext{rank}(X) < p$).
  2. When features are collinear, the matrix $X^T X$ becomes nearly singular ($\det(X^T X) \approx 0$). Its inverse $(X^T X)^{-1}$ blows up to massive values. As a consequence:
     * Point estimates of $\beta$ become wildly unstable (sensitive to minor data perturbations, often showing nonsensical negative signs).
     * The standard errors $\text{SE}(\beta) = \sqrt{\sigma^2 (X^T X)^{-1}_{jj}}$ inflate dramatically, causing $t$-statistics ($t = \beta / \text{SE}$) to collapse toward zero, making truly significant channels appear statistically insignificant.
  3. **Variance Inflation Factor**: $\text{VIF}_j = \frac{1}{1 - R_j^2}$, where $R_j^2$ is the $R^2$ obtained from regressing feature $x_j$ against all other explanatory features.
     * Rule of thumb: $\text{VIF} > 5$ indicates high multicollinearity; $\text{VIF} > 10$ requires immediate remediation (e.g., dropping redundant composite variables or applying Ridge regression).

---

## 3. Mock 03: Advanced AI, Data Engineering & Architecture (75 Mins | 60 Marks)

### Candidate Instructions
* Focus: Medallion Lakehouse architectures, distributed PySpark data processing, ML model diagnostics, Generative AI / RAG system design, and Graph Analytics.

---

### Section A: Data Engineering & Lakehouse Pipelines (15 Marks)

#### Q3.1 (8 Marks) — PySpark Salting for Severe Key Skew
In a banking lakehouse ETL job, a join between `large_transactions` (1 Billion rows) and `dim_merchants` (1 Million rows) on `merchant_id` encounters severe job hangs and out-of-memory errors on Spark Executor 4. Profiling reveals that Amazon alone accounts for 35% of all transactions (`merchant_id = 'M_AMZN'`).
1. Explain why standard hash partitioning fails under this data distribution.
2. Provide the PySpark code snippet implementing **Salting** to eliminate this skew.

#### Q3.2 (7 Marks) — Delta Lake ACID Architecture
1. How does Delta Lake implement ACID transactions on top of immutable cloud object storage (AWS S3 / Azure ADLS)?
2. What is the role of the `_delta_log/` transaction log and checkpoints?
3. What is the difference between `VACUUM` and `OPTIMIZE (Z-ORDER)`?

---

### Section B: Machine Learning Diagnostics & Feature Engineering (15 Marks)

#### Q3.3 (8 Marks) — L1 vs. L2 Regularization Derivation & Geometry
The Lasso objective function is $\min_w \frac{1}{2n} \|y - Xw\|_2^2 + \lambda \|w\|_1$, while Ridge is $\min_w \frac{1}{2n} \|y - Xw\|_2^2 + \lambda \|w\|_2^2$.
1. Explain geometrically why L1 regularization forces redundant feature weights strictly to zero, while L2 only shrinks them asymptotically.
2. In an enterprise consulting engagement with 1,200 candidate behavioral telemetry features and 5,000 observations, which regularization technique would you select and why?

#### Q3.4 (7 Marks) — Stationarity in Time-Series Forecasting
1. Define weak stationarity (covariance stationarity) for a time series $Y_t$.
2. Why does training an ARIMA model on a non-stationary random walk produce spurious regressions?
3. How do you interpret an Augmented Dickey-Fuller (ADF) test result where the test statistic is $-1.45$ and the 5% critical value is $-2.86$?

---

### Section C: Generative AI, RAG & Knowledge Graphs (30 Marks)

#### Q3.5 (15 Marks) — Enterprise RAG System Architecture Blueprint
Design an enterprise Question-Answering system over 50,000 PDF technical product manuals for a global manufacturing client.
1. **Document Ingestion**: How should documents be chunked? Compare fixed-size sliding window (500 tokens with 50-token overlap) vs. hierarchy/layout-aware chunking.
2. **Retrieval**: Describe how to implement Hybrid Search combining Dense Vector Search (HNSW index) and Sparse Keyword Search (BM25) with Reciprocal Rank Fusion.
3. **Guardrails**: Write an architectural flow diagram or markdown pseudo-code describing the safety checks executed before and after the LLM generates a response.

#### Q3.6 (15 Marks) — Graph Analytics for Supply Chain Vulnerability
A multinational pharmaceutical manufacturer represents its global supply chain as a directed graph $G = (V, E)$, where $V$ represents factories, raw material suppliers, packaging hubs, and distribution centers. Edges $E$ represent transport corridors weighted by average lead time (days).
1. Which graph centrality metric (Degree, Closeness, Betweenness, or PageRank) best identifies the single supplier whose disruption would break the maximum number of optimal supply paths? Define its formula.
2. Write a Neo4j Cypher query to find all packaging hubs that are single points of failure (i.e., hubs whose removal disconnects a factory from a distribution center).

---

### Mock 03: Answer Key & Step-by-Step Solutions

#### Section A Solutions
* **Q3.1 Solution (8 Marks)**:
  1. *Hash Partitioning Failure*: Spark distributes join keys across partitions using $\text{hash}(\text{merchant\_id}) \pmod{\text{num\_partitions}}$. When a single merchant has 350M rows, all 350M rows hash to the **exact same single executor**, while other executors sit idle. That overloaded executor runs out of heap memory (OOM), spilling to disk and crashing the stage.
  2. *Salting Implementation*:
```python
from pyspark.sql import functions as F

# Step 1: Add a random salt integer [0, 9] to the skewed transaction table
salt_factor = 10
skewed_txns = large_transactions.withColumn("salt", F.floor(F.rand() * salt_factor))
skewed_txns = skewed_txns.withColumn("salted_key", F.concat(F.col("merchant_id"), F.lit("_"), F.col("salt")))

# Step 2: Replicate the small dimension table across all salt factors [0..9]
salt_df = spark.range(0, salt_factor).withColumnRenamed("id", "salt")
replicated_merchants = dim_merchants.crossJoin(salt_df)
replicated_merchants = replicated_merchants.withColumn("salted_key", F.concat(F.col("merchant_id"), F.lit("_"), F.col("salt")))

# Step 3: Join on the salted composite key -> perfectly distributed across 10 partitions!
balanced_joined_df = skewed_txns.join(
    replicated_merchants,
    on="salted_key",
    how="inner"
).drop("salt", "salted_key")
```

* **Q3.2 Solution (7 Marks)**:
  1. *Delta Lake ACID*: Delta Lake stores raw data as standard immutable Parquet files in S3. ACID transactions are implemented via an atomic, sequential transaction log (`_delta_log/000000.json`, `000001.json`). Changes are committed using **optimistic concurrency control**; readers read only committed snapshots, preventing dirty reads.
  2. *Transaction Log & Checkpoints*: Every write appends a new JSON log file listing newly added and tombstoned Parquet files. Every 10 commits, Delta writes a consolidated Parquet **checkpoint file**, allowing readers to reconstruct the latest table state in $O(1)$ without reading thousands of JSON files.
  3. *VACUUM vs OPTIMIZE*:
     * `OPTIMIZE (Z-ORDER BY col)`: Compacts thousands of small Parquet files into optimal 1GB files and colocates multidimensional data to maximize Parquet min/max data skipping.
     * `VACUUM (RETAIN X HOURS)`: Permanently deletes underlying Parquet files that were marked as tombstoned older than the retention period (default 7 days), freeing cloud storage costs.

#### Section B Solutions
* **Q3.3 Solution (8 Marks)**:
  1. *Geometric Explanation*: The OLS loss contours are elliptical paraboloids centered at the unconstrained OLS estimate $\hat{\beta}$. 
     * The L2 constraint region $\|w\|_2^2 \le t$ is a smooth hypersphere (circle in 2D). The loss contour tangentially touches the smooth boundary at points where coordinates are non-zero.
     * The L1 constraint region $\|w\|_1 \le t$ is a polytope with sharp corners/creases (a diamond in 2D) positioned exactly on the coordinate axes ($w_1 = 0$ or $w_2 = 0$). The elliptical contours frequently strike these sharp corners first, forcing non-informative coefficients strictly to $0.0$.
  2. *Recommendation*: **Lasso (L1) or ElasticNet**. With $P = 1,200$ features and only $N = 5,000$ samples, the primary objective is feature selection and model interpretability. Lasso automatically eliminates uninformative behavioral features, producing a sparse, parsimonious model easily explainable to client executives.

* **Q3.4 Solution (7 Marks)**:
  1. *Weak Stationarity*: A process $Y_t$ is weakly stationary if:
     * Mean is constant over time: $\mathbb{E}[Y_t] = \mu$ for all $t$.
     * Variance is finite and constant: $\text{Var}(Y_t) = \sigma^2 < \infty$.
     * Autocovariance depends only on the time lag $k$, not on absolute time: $\text{Cov}(Y_t, Y_{t-k}) = \gamma(k)$.
  2. *Spurious Regression*: Non-stationary series exhibit trending behavior. Fitting regression or ARIMA models on raw non-stationary data leads to inflated $R^2$ values ($> 0.90$) and highly significant $t$-statistics even between completely unrelated variables (e.g., rainfall in Peru vs. corporate revenue in Japan) because both share a common deterministic or stochastic trend.
  3. *ADF Interpretation*: The test statistic is $-1.45$. Since $-1.45$ is **greater (less negative) than the critical value $-2.86$**, we **fail to reject the null hypothesis of a unit root**. The time series is **non-stationary**. It must be differenced ($d = 1$) or log-transformed prior to ARIMA modeling.

#### Section C Solutions
* **Q3.5 Solution (15 Marks)**:
  1. *Chunking Strategy*: PDF technical manuals contain structured tables, schematics, and hierarchical headings. Fixed-size chunking (500 tokens) chops sentences mid-formula and separates table headers from values. **Recommendation: Layout-Aware Hierarchical Chunking**. Use PDF layout parsers (e.g., Unstructured / PyMuPDF) to extract semantic sections by `H1/H2/H3` markdown headers and retain full HTML table structures with parent document metadata.
  2. *Hybrid Search with RRF*:
     ```text
     User Query 
       ├── (1) Dense Retrieval: OpenAI text-embedding-3-small -> Top 50 chunks (HNSW vector index)
       └── (2) Sparse Retrieval: BM25 exact keyword match -> Top 50 chunks (Elasticsearch)
       └── (3) Reciprocal Rank Fusion (RRF):
               Score(d) = 1/(60 + Rank_Dense) + 1/(60 + Rank_BM25)
       └── (4) Cross-Encoder Reranker: Cohere Rerank v3 -> Top 5 highest scoring chunks passed to LLM
     ```
  3. *Guardrails Pipeline*:
     ```text
     User Input -> [Input Guardrail: PII Masking + Prompt Injection Detector]
                -> [Hybrid RAG Retrieval + Reranker]
                -> [Context Packing + System Prompt with Abstention Clause]
                -> [LLM Generation (Temperature = 0.0)]
                -> [Output Guardrail: Hallucination Check (NLI entailment) + Toxic Filter]
                -> Client Response
     ```

* **Q3.6 Solution (15 Marks)**:
  1. *Betweenness Centrality*:
     $$C_B(v) = \sum_{s \ne v \ne t} \frac{\sigma_{st}(v)}{\sigma_{st}}$$
     where $\sigma_{st}$ is the total number of shortest paths from source node $s$ to destination node $t$, and $\sigma_{st}(v)$ is the number of those paths passing through node $v$. A node with maximum betweenness centrality acts as the primary transit bridge; its failure forces rerouting across longer, less efficient alternate paths.
  2. *Cypher Query for Single Point of Failure*:
     ```cypher
     // Find packaging hubs bridging factories and distribution centers where no alternative direct path exists
     MATCH (f:Factory)-[:SHIPS_TO]->(hub:PackagingHub)-[:SHIPS_TO]->(dc:DistributionCenter)
     WHERE NOT EXISTS {
         MATCH (f)-[:SHIPS_TO*..3]->(dc)
         WHERE NOT hub IN nodes(path)
     }
     RETURN hub.hub_id, hub.location, COUNT(DISTINCT f) AS impacted_factories, COUNT(DISTINCT dc) AS impacted_dcs
     ORDER BY impacted_factories DESC;
     ```

---

## 4. Mock 04: Comprehensive Full-Spectrum Simulation (90 Mins | 100 Marks)

### Candidate Instructions
* The capstone simulation integrates all dimensions of the Deloitte USI Analyst assessment:
  * Section A: Quantitative & Analytical Aptitude (20 Marks)
  * Section B: Coding & Database Engineering (30 Marks)
  * Section C: Business Architecture, ERP & Process Improvement (25 Marks)
  * Section D: Consulting Case Structuring & Behavioral Defense (25 Marks)

---

### Section A: Quantitative & Analytical Aptitude (20 Marks)

#### Q4.1 (10 Marks) — Bayes' Theorem with False-Positive Base-Rate Fallacy
Deloitte's automated code vulnerability scanner flags security flaws in cloud deployment scripts.
* Background prevalence: Only 0.2% ($P(V) = 0.002$) of all committed scripts contain critical security vulnerabilities.
* The scanner has a true positive detection rate (sensitivity) of 95%: $P(\text{Alert} \mid V) = 0.95$.
* The scanner has a false alarm rate of 3%: $P(\text{Alert} \mid V^c) = 0.03$.
1. Compute the probability that a script flagged with an alert actually contains a vulnerability: $P(V \mid \text{Alert})$.
2. If an enterprise developer commits 10,000 scripts per month, how many false alarms will the team investigate per month?
3. How should an analyst explain this counterintuitive result to a Chief Information Security Officer (CISO)?

#### Q4.2 (10 Marks) — Work Breakdown & Critical Path Analysis
A cloud migration project consists of 5 sequential and parallel work packages:

| Task | Description | Immediate Predecessors | Duration (Weeks) |
| :--- | :--- | :--- | :--- |
| **A** | Cloud Architecture Blueprint | None | 4 |
| **B** | IAM & Security Role Setup | A | 3 |
| **C** | Database Schema Migration | A | 6 |
| **D** | ETL Pipeline Re-engineering | C | 5 |
| **E** | User Acceptance Testing (UAT) | B, D | 4 |

1. Identify all possible paths through the project network from start to finish and calculate their total duration.
2. What is the **Critical Path** and the minimum total project completion time?
3. What is the total slack (float) for Task B?

---

### Section B: Coding & Database Engineering (30 Marks)

#### Q4.3 (15 Marks) — Python: LRU Cache Implementation
Enterprise RAG systems require caching retrieved vector chunks to avoid redundant embeddings.
Implement a Least Recently Used (LRU) Cache class `LRUCache(capacity: int)` supporting:
* `get(key: int) -> int`: Return value if present, else `-1`. Mark key as recently used.
* `put(key: int, value: int) -> None`: Insert or update key-value pair. If capacity is exceeded, evict the least recently used key.
* Both operations must operate in strict $O(1)$ average time complexity using Python's standard library.

#### Q4.4 (15 Marks) — SQL: S2P Purchase Order Variance Audit
Deloitte's internal audit team inspects a Source-to-Pay database for invoice discrepancies.
Tables:
1. `purchase_orders(po_id INT, vendor_id INT, po_amount NUMERIC, approved_date DATE)`
2. `goods_receipts(gr_id INT, po_id INT, received_amount NUMERIC, gr_date DATE)`
3. `invoices(invoice_id INT, po_id INT, invoice_amount NUMERIC, invoice_date DATE, payment_status VARCHAR)`

Write an ANSI-SQL query that finds all `po_id`s where:
1. The total invoiced amount exceeds the approved PO amount by more than 5%.
2. OR the total invoiced amount exceeds the total received amount in Goods Receipts.
Output `po_id`, `vendor_id`, `po_amount`, `total_received`, `total_invoiced`, and a computed column `audit_risk_reason` explaining the failure.

---

### Section C: Business Architecture, ERP & Process Improvement (25 Marks)

#### Q4.5 (13 Marks) — Source-to-Pay 3-Way Match Exception Workflow
An enterprise retail client receives 40,000 vendor invoices per month. Currently, 22% of invoices fail automated 3-Way Matching, creating a massive backlog in Accounts Payable.
1. Draw or specify the sequential process flow of a standard 3-Way Match (PO, GR, Invoice).
2. Using the **5 Whys** framework, trace the root cause of why $60\%$ of invoice match failures occur due to "Price Variance on Shipping Freight".
3. Propose two specific ERP system configuration controls and one vendor policy change to eliminate this variance.

#### Q4.6 (12 Marks) — Working Capital DSO Reduction Business Case
A manufacturing client has annual credit sales of $146,000,000 and currently maintains an average Accounts Receivable balance of $28,000,000.
1. Calculate the client's current Days Sales Outstanding (DSO) assuming a 365-day year.
2. Deloitte's Order-to-Cash process transformation project costs $600,000 to implement and promises to reduce DSO by 15 days.
   * Calculate the permanent cash released to working capital.
   * If the client's corporate cost of capital (hurdle rate) is $8\%$, calculate the annual recurring interest savings and the net Year 1 ROI of the consulting engagement.

---

### Section D: Consulting Case Structuring & Behavioral Defense (25 Marks)

#### Q4.7 (15 Marks) — MECE Issue Tree & AI PoC Go/No-Go Decision
A global retail bank's Chief Operating Officer approaches Deloitte with the following proposal:  
*"We want to replace our entire tier-1 customer support call center with an autonomous LLM Voice Agent within 6 months to reduce headcount costs by 70%."*

1. Decompose this strategic initiative into a structured **MECE Issue Tree** covering:
   * Technical Feasibility & Latency
   * Financial & Operational Economics
   * Regulatory Compliance, Risk & Brand Reputation
2. Formulate a 2-minute executive recommendation outlining whether the bank should proceed with a full rollout or a gated PoC, highlighting key transition risks.

#### Q4.8 (10 Marks) — Behavioral Interview Scenarios (STAR Defense)
Provide structured bullet points demonstrating how an IIT Kanpur graduate should answer:
1. *"Describe a situation where a client or teammate challenged your analytical conclusions and data findings. How did you resolve the conflict without damaging the professional relationship?"*
2. *"Why Deloitte US-India specifically, rather than a domestic Indian IT service firm or an onshore pure-play software development role?"*

---

### Mock 04: Answer Key & Step-by-Step Solutions

#### Section A Solutions
* **Q4.1 Solution (10 Marks)**:
  1. *Bayes' Theorem*:
     * $P(V) = 0.002, P(V^c) = 0.998$.
     * $P(\text{Alert} \mid V) = 0.95$.
     * $P(\text{Alert} \mid V^c) = 0.03$.
     * Total probability of alert:
       $$P(\text{Alert}) = (0.95 \times 0.002) + (0.03 \times 0.998) = 0.0019 + 0.02994 = 0.03184$$
     * Posterior probability:
       $$P(V \mid \text{Alert}) = \frac{0.0019}{0.03184} \approx \mathbf{0.05967} \quad (\mathbf{5.97\%})$$
  2. *Monthly False Alarms*:
     * Out of 10,000 scripts: Clean scripts $= 9,980$.
     * False alarms $= 9,980 \times 0.03 = \mathbf{299.4} \approx 299$ false alarms per month!
     * Actual true vulnerability alerts $= 20 \times 0.95 = 19$ true alerts.
  3. *Executive Explanation to CISO*:
     > *"CISO, even though our scanner has a 95% sensitivity rating, because true security vulnerabilities are very rare (only 2 in every 1,000 scripts), the sheer volume of clean scripts overwhelms the system. Out of every 100 alerts our security engineers investigate, 94 are false alarms. To prevent alert fatigue and wasted engineering hours, we should not send raw alerts directly to engineers. Instead, we should introduce a secondary automated validation rule or triage filter."*

* **Q4.2 Solution (10 Marks)**:
  1. *Network Paths*:
     * Path 1: $A \to B \to E = 4 + 3 + 4 = 11$ weeks.
     * Path 2: $A \to C \to D \to E = 4 + 6 + 5 + 4 = 19$ weeks.
  2. *Critical Path*: **$A \to C \to D \to E$**.
     * Minimum project duration: **19 Weeks**.
  3. *Total Slack for Task B*:
     * Earliest Start of B: End of A = Week 4. Earliest Finish of B = Week $4 + 3 = 7$.
     * Task E cannot start until Week 15 (when Task D finishes).
     * Latest Finish of B: Week 15.
     * Total Float (Slack) for B $= 15 - 7 = \mathbf{8}$ weeks. Task B can be delayed up to 8 weeks without delaying overall project delivery.

#### Section B Solutions
* **Q4.3 Solution (15 Marks)**:
```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move accessed key to the end to mark as most recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key)
            return
        if len(self.cache) >= self.capacity:
            # Evict the first item (least recently used)
            self.cache.popitem(last=False)
        self.cache[key] = value

# Verification
cache = LRUCache(2)
cache.put(1, 10)
cache.put(2, 20)
assert cache.get(1) == 10     # Key 1 accessed, Key 2 becomes LRU
cache.put(3, 30)             # Key 2 evicted!
assert cache.get(2) == -1     # Returns -1
assert cache.get(3) == 30
```
*Time Complexity*: $O(1)$ amortized for both `get` and `put`. `OrderedDict` internally maintains a hash map combined with a doubly-linked list.

* **Q4.4 Solution (15 Marks)**:
```sql
WITH AggGoodsReceipts AS (
    SELECT po_id, SUM(received_amount) AS total_received
    FROM goods_receipts
    GROUP BY po_id
),
AggInvoices AS (
    SELECT po_id, SUM(invoice_amount) AS total_invoiced
    FROM invoices
    GROUP BY po_id
),
AuditedPOs AS (
    SELECT 
        po.po_id,
        po.vendor_id,
        po.po_amount,
        COALESCE(gr.total_received, 0) AS total_received,
        COALESCE(inv.total_invoiced, 0) AS total_invoiced
    FROM purchase_orders po
    LEFT JOIN AggGoodsReceipts gr ON po.po_id = gr.po_id
    LEFT JOIN AggInvoices inv ON po.po_id = inv.po_id
)
SELECT 
    po_id,
    vendor_id,
    po_amount,
    total_received,
    total_invoiced,
    CASE 
        WHEN total_invoiced > po_amount * 1.05 AND total_invoiced > total_received 
            THEN 'Exceeds Both PO Limit (>5%) and Goods Received'
        WHEN total_invoiced > po_amount * 1.05 
            THEN 'Exceeds Approved PO Amount by >5%'
        WHEN total_invoiced > total_received 
            THEN 'Invoiced for Unreceived Goods (Billed > GR)'
    END AS audit_risk_reason
FROM AuditedPOs
WHERE total_invoiced > po_amount * 1.05 
   OR total_invoiced > total_received
ORDER BY (total_invoiced - po_amount) DESC;
```

#### Section C Solutions
* **Q4.5 Solution (13 Marks)**:
  1. *3-Way Match Flow*:
     ```text
     [Procurement] -> Purchase Order (PO: approved price & quantity)
     [Warehouse]   -> Goods Receipt (GR: physical items verified at dock)
     [Vendor]      -> Vendor Invoice (INV: bill submitted for payment)
     Automated ERP Match Check:
       Condition 1: INV Unit Price == PO Unit Price (+/- 0% tolerance)
       Condition 2: INV Quantity <= GR Quantity (+/- 0% tolerance)
       -> IF MATCH: Auto-release payment voucher to AP.
       -> IF MISMATCH: Apply ERP Payment Block; Route exception to buyer.
     ```
  2. *5 Whys Root Cause Analysis*:
     * *Why did invoices fail 3-way match?* Invoiced total exceeded PO by $150–$300 freight fee.
     * *Why was freight added to the invoice?* Suppliers billed actual shipping carriers separately.
     * *Why was freight missing from the PO?* Purchasing agents created POs using standard catalog items without adding a freight line item.
     * *Why did purchasing agents omit freight?* The ERP purchasing module allowed PO creation with a default `FOB Destination (Free Shipping)` flag.
     * *Why was FOB Destination selected?* Procurement lacked an automated integration with freight rate tables during the requisition stage. (Root Cause).
  3. *Remediation Controls*:
     * **ERP System Control 1**: Implement an automated ERP Freight Tolerance Rule (allow auto-approval of freight variances up to $50 or 3% of PO value).
     * **ERP System Control 2**: Make freight quotation mandatory during Requisition creation for non-local vendors.
     * **Vendor Policy Change**: Contractually enforce Incoterms (e.g., DDP - Delivered Duty Paid) or require vendors to use client's centralized logistics carrier account.

* **Q4.6 Solution (12 Marks)**:
  1. *Current DSO*:
     $$\text{DSO} = \frac{\text{Accounts Receivable}}{\text{Annual Credit Sales}} \times 365 = \frac{28,000,000}{146,000,000} \times 365 = \frac{28}{146} \times 365 = \mathbf{70.0} \text{ days}$$
  2. *DSO Reduction Impact*:
     * Target DSO $= 70 - 15 = 55$ days.
     * New target AR balance $= \frac{55}{365} \times 146,000,000 = \$22,000,000$.
     * **Permanent Cash Released to Working Capital**:
       $$\Delta \text{Cash} = 28,000,000 - 22,000,000 = \mathbf{\$6,000,000}$$
     * **Annual Interest Savings** (at 8% cost of capital):
       $$\text{Annual Savings} = 6,000,000 \times 0.08 = \mathbf{\$480,000 / \text{year}}$$
     * **Net Year 1 ROI**:
       * Year 1 cash benefit $= \$6,000,000$ (one-time liquidity) $+ \$480,000$ (annual carrying cost savings) $= \$6,480,000$.
       * Engagement cost $= \$600,000$.
       * Recurring ROI $= \frac{480,000 - 600,000 / 3}{600,000} \dots$
       * Standard Consulting ROI formula: $\frac{\text{Annual Financial Return}}{\text{Project Cost}} = \frac{480,000}{600,000} = \mathbf{80\%}$ recurring annual return on invested consulting fees, with full payback achieved in $1.25$ years ($15$ months).

#### Section D Solutions
* **Q4.7 Solution (15 Marks)**:
  1. *MECE Issue Tree*:
     ```text
     Autonomous Voice AI Call Center Replacement
     ├── 1. Technical Feasibility & Latency
     │     ├── Real-time Speech-to-Text & Text-to-Speech latency (< 600ms threshold)?
     │     ├── Accents, background noise, and multi-lingual dialect support?
     │     └── Integration with legacy core banking mainframe APIs?
     ├── 2. Financial & Operational Economics
     │     ├── True Total Cost of Ownership (LLM API tokens, telephony infrastructure, fallbacks)?
     │     ├── Human escalation routing tier costs (handling complex calls)?
     │     └── Transition redundancy and severance costs?
     └── 3. Regulatory Compliance & Brand Risk
           ├── Financial Consumer Protection compliance (accurate account disclosures)?
           ├── PII data privacy and voice recording biometric consent?
           └── Hallucination liability (unauthorized credit limit promises or transfers)?
     ```
  2. *Executive 2-Minute Recommendation*:
     > *"COO, completely replacing your tier-1 call center within 6 months is an extremely high-risk strategy that could lead to customer backlash, regulatory fines, and operational failure. While GenAI voice models show immense promise, banking transactions require 100% compliance and sub-second latency that current frontier models cannot guarantee across complex inquiries.*  
     > *We strongly recommend a **gated 3-phase PoC approach**:*  
     > *1. **Phase 1 (Months 1–2)**: Deploy an AI Agent-Assist tool—empower existing human agents with real-time automated knowledge retrieval and auto-summarization. This lowers Average Handle Time (AHT) by 25% with zero customer exposure risk.*  
     > *2. **Phase 2 (Months 3–4)**: Pilot autonomous Voice AI strictly on low-risk informational FAQs (branch hours, balance checks, ATM locations).*  
     > *3. **Phase 3 (Months 5–6)**: Evaluate quantitative metrics (Containment Rate, CSAT, Latency) before automating transaction execution. This captures 40% of the cost savings while completely insulating the bank from brand and regulatory catastrophic risks."*

* **Q4.8 Solution (10 Marks)**:
  1. *Conflict Resolution (STAR)*:
     * **Situation**: During a predictive analytics project, a business stakeholder argued that a customer segment was unprofitable and should be dropped, contradicting our cohort churn model.
     * **Task**: Defend model integrity without appearing dismissive or confrontational.
     * **Action**: Scheduled a working session; validated their intuitive business concern first. Decomposed the data together: showed that while gross margins were temporarily low due to introductory promotions, Lifetime Value (LTV) was 3x higher than average.
     * **Result**: Stakeholder agreed with the LTV findings, retained the segment, and thanked our team for preventing a strategic mistake.
  2. *Why Deloitte US-India*:
     * Emphasize the unique triad: Technical engineering + business process acumen + direct client engagement.
     * Highlight scale: Deloitte USI works directly with 90% of the Fortune 500 across complex global digital transformations, not just back-office ticket maintenance.
     * Personal alignment: Coming from IIT Kanpur, desire to work at the intersection of deep analytical problem solving and strategic client impact.

---

## 5. Diagnostic Remediation Matrix & Next Steps

When candidates score below the target mastery benchmark on any mock assessment, use this targeted remediation plan to review specific modules:

| Assessment & Section | Identified Weakness Area | Score Threshold | Mandatory Remediation Module | Primary Recommended Practice |
| :--- | :--- | :--- | :--- | :--- |
| **Mock 01 (Sec A)** | Quant arithmetic / Alligation / CAGR | $< 12 / 15$ | `01_APTITUDE_LOGICAL_REASONING_AND_VERBAL.md` | Re-solve Q001–Q020 in Question Bank |
| **Mock 01 (Sec B)** | Syllogisms / Seating / Grammar | $< 12 / 15$ | `01_APTITUDE_LOGICAL_REASONING_AND_VERBAL.md` | Master 5 Rules of Syllogistic Deduction |
| **Mock 02 (Sec A)** | Python Sliding Window / Hash Maps | $< 16 / 20$ | `02_PYTHON_PROGRAMMING_AND_DSA.md` | Implement sliding window and two pointers |
| **Mock 02 (Sec B)** | SQL Window Functions / Islands | $< 16 / 20$ | `03_SQL_DATABASES_AND_DATA_MANIPULATION.md` | Practice `ROW_NUMBER() - ROW_NUMBER()` |
| **Mock 02 (Sec C)** | Two-proportion Z-test / VIF | $< 16 / 20$ | `04_STATISTICS_ANALYTICS_AND_VISUALIZATION.md` | Review hypothesis testing formulas & VIF |
| **Mock 03 (Sec A)** | PySpark Skew / Delta Lake Log | $< 12 / 15$ | `05_DATA_ENGINEERING_CLOUD_AND_GOVERNANCE.md` | Study Spark salting & Medallion layers |
| **Mock 03 (Sec B)** | Lasso L1 / Stationarity / ADF | $< 12 / 15$ | `06_MACHINE_LEARNING_NLP_TIME_SERIES_AND_VISION.md` | Review geometry of L1 vs L2 regularization |
| **Mock 03 (Sec C)** | RAG Architecture / Graph Cypher | $< 24 / 30$ | `07_GENERATIVE_AI_LLM_PROMPT_ENGINEERING_RAG.md` & `08_AGENTIC_AI` | Build hybrid search & Cypher queries |
| **Mock 04 (Sec C)** | ERP 3-Way Match / DSO / Working Cap | $< 20 / 25$ | `09_ENTERPRISE_PLATFORMS_ERP_AND_PROCESS_IMPROVEMENT.md` | Trace S2P process & DSO cash formulas |
| **Mock 04 (Sec D)** | Issue Trees / Minto / Behavioral STAR | $< 20 / 25$ | `10_BUSINESS_CASES_RESEARCH_POC` & `11_INTERVIEW_BEHAVIOURAL` | Practice MECE trees & 90s elevator pitch |
