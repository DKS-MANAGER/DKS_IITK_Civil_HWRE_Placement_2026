# Citi AIM Business Analytics — Comprehensive Question Bank with Complete Solutions

> **Target Role**: Spec Analytics Analyst — Business Analytics (SBS), Citi AIM  
> **Course Layer**: Question & Answer Bank (`[PRACTICE CASE ASSUMPTION]` synthetic benchmarks)  
> **Difficulty Taxonomy**:  
> • **Level 1 — Foundational**: Direct mathematical/syntactic definitions and standard formula applications.  
> • **Level 2 — Applied**: Multi-step numerical calculation, explicit data tables, and joined SQL queries.  
> • **Level 3 — Interview-Level**: Method selection, edge cases, business trade-offs, and follow-up defenses.  
> • **Level 4 — Advanced**: Complex scenario diagnosis, asymmetric cost optimization, and integrated risk governance.

---

## Table of Contents
1. [Domain 1: Statistics, Probability & Experimentation](#domain-1-statistics-probability--experimentation)
2. [Domain 2: SQL, Data Manipulation & Database Architecture](#domain-2-sql-data-manipulation--database-architecture)
3. [Domain 3: Predictive Modeling, Scorecards & Machine Learning](#domain-3-predictive-modeling-scorecards--machine-learning)
4. [Domain 4: Banking Case Analysis & Business Metrics](#domain-4-banking-case-analysis--business-metrics)
5. [Domain 5: Data Visualization & Executive Communication](#domain-5-data-visualization--executive-communication)
6. [Domain 6: Behavioural, Matrix Stakeholders & Risk Compliance](#domain-6-behavioural-matrix-stakeholders--risk-compliance)

---

## Domain 1: Statistics, Probability & Experimentation

### QB-STAT-01 | Level 1 (Foundational)
* **Topic**: Bayes' Theorem & Conditional Probability
* **Question**: In an automated credit card fraud screening engine, the prior probability that an authorized transaction is fraudulent is $P(F) = 0.002$ ($0.2\%$). The algorithm triggers an alert with sensitivity $P(A \mid F) = 0.95$, and has a false positive rate $P(A \mid F^c) = 0.01$. If an alert is triggered, what is the posterior probability that the transaction is actually fraudulent?
* **What This Tests**: Fundamental Bayes' theorem formulation, base-rate fallacy awareness, and denominator total probability expansion.
* **Step-by-Step Solution**:
  1. Expand the denominator using the Law of Total Probability:
     $$P(A) = P(A \mid F)P(F) + P(A \mid F^c)P(F^c)$$
  2. Substitute values:
     $$P(F^c) = 1 - 0.002 = 0.998$$
     $$P(A) = (0.95 \times 0.002) + (0.01 \times 0.998) = 0.00190 + 0.00998 = 0.01188 \quad (1.188\%)$$
  3. Compute posterior probability:
     $$P(F \mid A) = \frac{P(A \mid F)P(F)}{P(A)} = \frac{0.00190}{0.01188} \approx \mathbf{0.1599} \quad (15.99\%)$$
* **Interpretation**: Despite $95\%$ sensitivity and only $1\%$ false alarm rate, only $\approx 16\%$ of alerted transactions are genuine fraud because legitimate transactions outnumber fraud by 499 to 1.
* **Common Mistakes**: Answering $95\%$ by confusing sensitivity $P(A \mid F)$ with precision $P(F \mid A)$.
* **Follow-up Interview Question**: *"If operations can only review alerts with $\ge 50\%$ precision, what must the false positive rate be reduced to?"*
  * *Answer*: Set $\frac{0.0019}{0.0019 + FPR \times 0.998} \ge 0.50 \implies FPR \times 0.998 \le 0.0019 \implies FPR \le \mathbf{0.001904} \approx 0.19\%$.

---

### QB-STAT-02 | Level 2 (Applied)
* **Topic**: Two-Sample Hypothesis Testing & Welch's $t$-Test
* **Question**: A credit card portfolio tests two marketing offers for personal loan cross-sell:
  * Variant A: $n_1 = 400$, mean balance transacted $\bar{X}_1 = \$2,450$, sample variance $s_1^2 = 360,000$ ($s_1 = \$600$).
  * Variant B: $n_2 = 300$, mean balance transacted $\bar{X}_2 = \$2,600$, sample variance $s_2^2 = 810,000$ ($s_2 = \$900$).
  Perform a two-tailed hypothesis test at $\alpha = 0.05$ to determine if the mean balance differs significantly. Do not assume equal population variances.
* **What This Tests**: Application of Welch's $t$-test, unpooled standard error calculation, and critical value decision rules.
* **Step-by-Step Solution**:
  1. Hypotheses: $H_0: \mu_1 - \mu_2 = 0$ vs $H_1: \mu_1 - \mu_2 \ne 0$.
  2. Unpooled Standard Error:
     $$\text{SE} = \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}} = \sqrt{\frac{360,000}{400} + \frac{810,000}{300}} = \sqrt{900 + 2,700} = \sqrt{3,600} = \mathbf{60.0}$$
  3. Test Statistic:
     $$t = \frac{\bar{X}_1 - \bar{X}_2}{\text{SE}} = \frac{2,450 - 2,600}{60} = \frac{-150}{60} = \mathbf{-2.50}$$
  4. Degrees of Freedom (Welch-Satterthwaite approximation):
     $$df \approx \frac{(900 + 2700)^2}{\frac{900^2}{399} + \frac{2700^2}{299}} = \frac{3600^2}{\frac{810000}{399} + \frac{7290000}{299}} = \frac{12,960,000}{2030.08 + 24381.27} \approx \frac{12,960,000}{26411.35} \approx \mathbf{490.7} \implies df \approx 490$$
  5. Critical Value: For $df > 120$ at $\alpha = 0.05$ two-tailed, $t_{crit} = \pm 1.965$.
  6. Decision: Since $|t_{obs}| = 2.50 > 1.965$, **Reject $H_0$** ($p \approx 0.0128$).
* **Common Mistakes**: Using pooled variance $s_p^2$ when sample variances are visibly unequal ($360,000$ vs $810,000$), violating the homoscedasticity assumption.
* **Follow-up Interview Question**: *"What if the data is heavily right-skewed with extreme wealth outliers?"*
  * *Answer*: Apply log-transformation $Y = \ln(X)$ or use non-parametric Mann-Whitney U test / bootstrapping.

---

### QB-STAT-03 | Level 3 (Interview-Level)
* **Topic**: A/B Testing Sample Sizing & Peeking Problem
* **Question**: A digital banking product manager wants to run an A/B test on a mobile app credit limit increase prompt. Baseline conversion rate is $p_0 = 5.0\%$. Target Minimum Detectable Effect is $+1.0\%$ absolute ($p_1 = 6.0\%$). With $\alpha = 0.05$ (two-sided) and Power $1 - \beta = 0.80$, compute required sample size per variant. Then explain why evaluating the test daily and stopping early when $p < 0.05$ is statistically invalid.
* **What This Tests**: Exact formula for two-proportion sample sizing and deep theoretical understanding of alpha inflation during continuous monitoring.
* **Step-by-Step Solution**:
  1. Standard formula for sample size per variant:
     $$n = \frac{\left(Z_{\alpha/2}\sqrt{2\bar{p}(1 - \bar{p})} + Z_\beta\sqrt{p_0(1-p_0) + p_1(1-p_1)}\right)^2}{\Delta^2}$$
     Where $Z_{0.025} = 1.96$, $Z_{0.20} = 0.8416$, $\Delta = 0.01$, $\bar{p} = \frac{0.05 + 0.06}{2} = 0.055$.
  2. Numerical Calculation:
     * Term 1: $1.96 \times \sqrt{2 \times 0.055 \times 0.945} = 1.96 \times \sqrt{0.10395} = 1.96 \times 0.3224 = 0.6319$.
     * Term 2: $0.8416 \times \sqrt{(0.05 \times 0.95) + (0.06 \times 0.94)} = 0.8416 \times \sqrt{0.0475 + 0.0564} = 0.8416 \times \sqrt{0.1039} = 0.8416 \times 0.3223 = 0.2713$.
     * Numerator: $(0.6319 + 0.2713)^2 = (0.9032)^2 \approx 0.8158$.
     * Denominator: $\Delta^2 = (0.01)^2 = 0.0001$.
     * $n = \frac{0.8158}{0.0001} \approx \mathbf{8,158\text{ users per variant}}$ (Round up to $\mathbf{8,200}$).
  3. The Peeking Problem Explanation:
     * A classical hypothesis test assumes a single evaluation at a fixed sample size.
     * Continuously testing p-values every day exposes the experiment to multiple looks. By the law of the iterated logarithm, random noise fluctuations will cross the $p < 0.05$ boundary at some point with probability $>30\%$ even when the null hypothesis is true.
     * Early stopping on nominal alpha inflates the Type I error rate from $5\%$ to $25\%\text{--}40\%$.
* **Follow-up Interview Question**: *"How do tech-forward banking platforms solve this if they MUST monitor daily for safety?"*
  * *Answer*: Implement Sequential Testing (e.g., Pocock or O'Brien-Fleming alpha-spending functions) or Bayesian A/B testing with continuous posterior updating.

---

### QB-STAT-04 | Level 4 (Advanced)
* **Topic**: Simpson's Paradox & Confounding in Credit Approval Rates
* **Question**: In an internal audit of loan approvals, two underwriting channels (Branch vs Digital) report approval rates across low-income and high-income applicants as follows:
  * **Low-Income**: Branch approves $20/100$ ($20.0\%$); Digital approves $180/600$ ($30.0\%$). Digital is higher.
  * **High-Income**: Branch approves $700/900$ ($77.8\%$); Digital approves $320/400$ ($80.0\%$). Digital is higher.
  * Yet, when management aggregates all applicants, Branch approves $720/1,000$ ($72.0\%$), while Digital approves $500/1,000$ ($50.0\%$).
  Demonstrate why this reversal occurs, identify the confounding variable, and explain which conclusion is valid.
* **What This Tests**: Detection and mathematical explanation of Simpson's Paradox; causal reasoning in observational banking data.
* **Step-by-Step Solution**:
  1. Aggregate Calculation Verification:
     * Branch: $\text{Total Approved} = 20 + 700 = 720$; $\text{Total Applicants} = 100 + 900 = 1,000 \implies \mathbf{72.0\%}$.
     * Digital: $\text{Total Approved} = 180 + 320 = 500$; $\text{Total Applicants} = 600 + 400 = 1,000 \implies \mathbf{50.0\%}$.
  2. The Confounding Mechanism:
     * The confounding variable is **Applicant Income Mix**.
     * High-income applicants have higher baseline approval rates ($\sim 78\%\text{--}80\%$) across both channels.
     * $90\%$ of Branch applicants are High-Income ($900/1000$).
     * In contrast, $60\%$ of Digital applicants are Low-Income ($600/1000$).
  3. Conclusion:
     * Comparing aggregate approval rates ($72\%$ vs $50\%$) is mathematically invalid because it confounds channel efficiency with applicant socioeconomic composition.
     * Controlled for income tier, **Digital actually has higher approval rates in both segments** ($30\%$ vs $20\%$ for low-income; $80\%$ vs $77.8\%$ for high-income).
* **Follow-up Interview Question**: *"How do you prevent this distortion in observational studies?"*
  * *Answer*: Use stratified analysis (Cochran-Mantel-Haenszel test) or propensity score matching before comparing groups.

---

## Domain 2: SQL, Data Manipulation & Database Architecture

### QB-SQL-01 | Level 1 (Foundational)
* **Topic**: SQL Execution Order & Aggregate Aliases
* **Question**: Why does the following query fail with an error in standard ANSI SQL, and how do you write the correct version?
  ```sql
  SELECT account_id, SUM(amount) AS total_spend
  FROM transactions
  WHERE total_spend > 5000
  GROUP BY account_id;
  ```
* **What This Tests**: Knowledge of the 8-stage logical query execution sequence.
* **Step-by-Step Solution**:
  1. **Why it fails**: SQL execution order evaluates `WHERE` (Step 2) before `GROUP BY` (Step 3) and `SELECT` (Step 5). The alias `total_spend` is defined in Step 5. When `WHERE` runs, `total_spend` does not exist in memory. Furthermore, row-level `WHERE` cannot filter on grouped aggregates.
  2. **The Correct Query**:
  ```sql
  SELECT account_id, SUM(amount) AS total_spend
  FROM transactions
  GROUP BY account_id
  HAVING SUM(amount) > 5000;
  ```
* **Follow-up Interview Question**: *"Can you use an alias defined in `SELECT` inside `ORDER BY`? Why?"*
  * *Answer*: Yes, because `ORDER BY` (Step 7) executes *after* `SELECT` (Step 5), so all column aliases are fully resolved.

---

### QB-SQL-02 | Level 2 (Applied)
* **Topic**: Join Fan-Out & Anti-Joins
* **Question**: Given two tables:
  * `customers`: `cust_id`, `cust_name`, `signup_date`
  * `accounts`: `account_id`, `cust_id`, `balance`, `status`
  Write a query to return all customers who signed up in 2026 and have **NO active accounts** (`status = 'ACTIVE'`).
* **Sample Data**:
  ```
  customers:
  | cust_id | cust_name | signup_date |
  | C1      | Alice     | 2026-02-15  |
  | C2      | Bob       | 2026-03-01  |
  | C3      | Charlie   | 2026-04-10  |

  accounts:
  | account_id | cust_id | balance | status   |
  | A1         | C1      | 500.00  | ACTIVE   |
  | A2         | C2      | 0.00    | CLOSED   |
  ```
* **Expected Output**:
  ```
  | cust_id | cust_name |
  | C2      | Bob       |
  | C3      | Charlie   |
  ```
* **Verified SQL Solution**:
  ```sql
  SELECT c.cust_id, c.cust_name
  FROM customers c
  WHERE c.signup_date >= '2026-01-01' AND c.signup_date < '2027-01-01'
    AND NOT EXISTS (
        SELECT 1 
        FROM accounts a 
        WHERE a.cust_id = c.cust_id 
          AND a.status = 'ACTIVE'
    );
  ```
* **Why Plausible Alternatives Fail**: Using `LEFT JOIN ... WHERE a.account_id IS NULL` will fail if Bob has a closed account, unless the join condition strictly restricts `ON a.cust_id = c.cust_id AND a.status = 'ACTIVE'`. `NOT EXISTS` is cleaner, faster, and immune to NULL join traps.

---

### QB-SQL-03 | Level 3 (Interview-Level)
* **Topic**: Window Functions & Running Totals with Frame Traps
* **Question**: For each account, compute the daily running balance. If multiple transactions occur on the exact same date, ensure each transaction is added deterministically one row at a time.
* **Sample Data**:
  ```
  transactions:
  | txn_id | account_id | txn_date   | amount |
  | T1     | ACC-101    | 2026-05-01 | 100.00 |
  | T2     | ACC-101    | 2026-05-02 | 50.00  |
  | T3     | ACC-101    | 2026-05-02 | 200.00 |
  | T4     | ACC-101    | 2026-05-03 | -30.00 |
  ```
* **Expected Output**:
  ```
  | txn_id | account_id | txn_date   | amount | running_balance |
  | T1     | ACC-101    | 2026-05-01 | 100.00 | 100.00          |
  | T2     | ACC-101    | 2026-05-02 | 50.00  | 150.00          |
  | T3     | ACC-101    | 2026-05-02 | 200.00 | 350.00          |
  | T4     | ACC-101    | 2026-05-03 | -30.00 | 320.00          |
  ```
* **Verified SQL Solution**:
  ```sql
  SELECT 
      txn_id,
      account_id,
      txn_date,
      amount,
      SUM(amount) OVER (
          PARTITION BY account_id
          ORDER BY txn_date, txn_id
          ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
      ) AS running_balance
  FROM transactions
  ORDER BY account_id, txn_date, txn_id;
  ```
* **The Silent Frame Trap**: If the candidate omits `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`, ANSI SQL defaults to `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`. On identical dates (`2026-05-02`), `RANGE` groups T2 and T3 together, displaying `350.00` on both rows instead of sequentially `150.00` then `350.00`!

---

### QB-SQL-04 | Level 4 (Advanced)
* **Topic**: Gaps-and-Islands (Consecutive Active Transaction Days)
* **Question**: Identify all customers who transacted on at least 3 **consecutive calendar days** during October 2026.
* **Schema**: `transactions (txn_id, cust_id, txn_date DATE)`
* **Technique**: Difference-of-Row-Numbers method (`txn_date - ROW_NUMBER() * INTERVAL '1 DAY'`).
* **Verified SQL Solution**:
  ```sql
  WITH DistinctActivityDays AS (
      SELECT DISTINCT 
          cust_id, 
          txn_date
      FROM transactions
      WHERE txn_date >= '2026-10-01' AND txn_date <= '2026-10-31'
  ),
  GroupedStreaks AS (
      SELECT 
          cust_id,
          txn_date,
          txn_date - (ROW_NUMBER() OVER (PARTITION BY cust_id ORDER BY txn_date) * INTERVAL '1 DAY') AS streak_island_key
      FROM DistinctActivityDays
  ),
  StreakSummary AS (
      SELECT 
          cust_id,
          streak_island_key,
          COUNT(*) AS consecutive_days,
          MIN(txn_date) AS streak_start,
          MAX(txn_date) AS streak_end
      FROM GroupedStreaks
      GROUP BY cust_id, streak_island_key
      HAVING COUNT(*) >= 3
  )
  SELECT DISTINCT cust_id, consecutive_days, streak_start, streak_end
  FROM StreakSummary
  ORDER BY cust_id, streak_start;
  ```
* **Why It Works**: When dates increment by exactly 1 day and row numbers increment by 1, the arithmetic difference `txn_date - (rn * 1 day)` remains invariant, grouping continuous daily runs into unique island keys.

---

## Domain 3: Predictive Modeling, Scorecards & Machine Learning

### QB-ML-01 | Level 1 (Foundational)
* **Topic**: Logistic Regression Odds Ratio vs Probability
* **Question**: In an underwriting logistic regression model, the coefficient for `has_past_delinquency` is $\beta = +0.693$. A candidate states: *"Having a past delinquency increases the applicant's probability of default by 69.3%."* Is this statement correct? Explain precisely.
* **What This Tests**: Strict mathematical distinction between change in log-odds, multiplicative change in odds, and additive change in probability.
* **Step-by-Step Answer**:
  1. The candidate's statement is **completely incorrect**.
  2. $\beta = 0.693$ represents the change in the **log-odds** ($\ln(\text{Odds})$).
  3. The multiplicative change in the **odds ratio** is:
     $$\text{Odds Ratio} = e^\beta = e^{0.693} \approx 2.00$$
     Having a past delinquency **doubles the odds of default** ($\text{Odds}_{new} = 2 \times \text{Odds}_{old}$).
  4. The impact on **probability** is non-linear and depends entirely on the applicant's baseline risk:
     * If baseline probability was $1\%$ ($\text{odds} \approx 0.01$), new odds $\approx 0.02 \implies \text{new probability} \approx 1.96\%$ (an absolute increase of only $+0.96\%$).
     * If baseline probability was $40\%$ ($\text{odds} = \frac{0.4}{0.6} = 0.667$), new odds $= 1.333 \implies \text{new probability} = \frac{1.333}{2.333} \approx 57.1\%$ (an absolute increase of $+17.1\%$).

---

### QB-ML-02 | Level 2 (Applied)
* **Topic**: Confusion Matrix & Asymmetric Cost Optimization
* **Question**: An automated personal loan scorecard evaluates 50,000 applicants. The empirical default rate is $4.0\%$ (2,000 defaults, 48,000 non-defaults).
  * Approving a defaulting borrower causes a net write-off loss of $\mathbf{\$4,000}$ ($\text{Cost}(\text{FN})$).
  * Rejecting a creditworthy borrower loses $\mathbf{\$250}$ in lifetime net interest margin ($\text{Cost}(\text{FP})$).
  Compare two candidate models:
  * **Model A**: $\text{TP} = 1,400, \text{FP} = 2,400, \text{FN} = 600, \text{TN} = 45,600$.
  * **Model B**: $\text{TP} = 1,800, \text{FP} = 7,200, \text{FN} = 200, \text{TN} = 40,800$.
  Which model should Citi deploy, and what is the net financial savings?
* **Step-by-Step Solution**:
  1. Calculate Total Expected Business Cost for Model A:
     $$\text{Cost}_A = (\text{FN} \times \$4,000) + (\text{FP} \times \$250)$$
     $$\text{Cost}_A = (600 \times \$4,000) + (2,400 \times \$250) = \$2,400,000 + \$600,000 = \mathbf{\$3,000,000}$$
  2. Calculate Total Expected Business Cost for Model B:
     $$\text{Cost}_B = (200 \times \$4,000) + (7,200 \times \$250)$$
     $$\text{Cost}_B = (800,000) + (1,800,000) = \mathbf{\$2,600,000}$$
  3. Compare Overall Metrics:
     * Model A Accuracy: $\frac{1400 + 45600}{50000} = 94.0\%$. Precision $= \frac{1400}{3800} = 36.8\%$.
     * Model B Accuracy: $\frac{1800 + 40800}{50000} = 85.2\%$. Precision $= \frac{1800}{9000} = 20.0\%$.
  4. Decision & Verdict:
     * Despite lower accuracy ($85.2\%$ vs $94.0\%$) and lower precision ($20\%$ vs $36.8\%$), **Model B is vastly superior** because catching 400 additional defaults saves $\$1.6\text{M}$ in charge-offs at an FP acquisition cost of $\$1.2\text{M}$.
     * **Net Financial Benefit**: Model B saves Citi $\mathbf{\$400,000}$ annually.

---

### QB-ML-03 | Level 3 (Interview-Level)
* **Topic**: KS Statistic & Scorecard Separation Capability
* **Question**: Explain how the Kolmogorov-Smirnov (KS) statistic is computed across deciles of a credit risk model. If an interviewer asks: *"Our scorecard achieves a KS of 48%, but the peak KS occurs in Decile 8. Is this a healthy model?"* How do you evaluate this?
* **Step-by-Step Answer**:
  1. **Definition**: The KS statistic measures the maximum vertical divergence between the cumulative distribution of defaulting borrowers ($F_{bad}$) and non-defaulting borrowers ($F_{good}$) when accounts are ranked from highest to lowest predicted risk:
     $$\text{KS} = \max_{d \in [1, 10]} |F_{bad}(d) - F_{good}(d)|$$
  2. **Evaluation of the Decile 8 Finding**:
     * A KS of $48\%$ appears high in the aggregate ($>40\%$ is standard threshold).
     * **However, having peak KS in Decile 8 is a severe red flag indicating a deeply flawed model.**
     * In a well-calibrated scorecard, high-risk defaults must concentrate in **Deciles 1, 2, and 3**, producing peak cumulative divergence early (by Decile 3 or 4).
     * If peak separation occurs at Decile 8, it means the model is failing to identify the worst borrowers upfront; instead, it is only separating prime from ultra-prime borrowers in the safe tail while mixing bad borrowers across the middle-to-high risk tranches.
     * **Verdict**: Reject model deployment; re-examine feature relationships and rank-ordering.

---

### QB-ML-04 | Level 4 (Advanced)
* **Topic**: Population Stability Index (PSI) & Model Governance
* **Question**: Following an interest rate hike, Citi's risk team observes that credit scores on new applications have shifted. Compute the PSI from the following table and specify the required model governance action:
  ```
  Bin 1 (Score < 600)   : Expected = 15%, Actual = 25%
  Bin 2 (Score 600-700) : Expected = 35%, Actual = 40%
  Bin 3 (Score 701-800) : Expected = 35%, Actual = 25%
  Bin 4 (Score > 800)   : Expected = 15%, Actual = 10%
  ```
* **Step-by-Step Solution**:
  1. Formula: $\text{PSI} = \sum (A_i - E_i) \times \ln(A_i / E_i)$
  2. Component Calculations:
     * Bin 1: $(0.25 - 0.15) \times \ln(0.25 / 0.15) = +0.10 \times \ln(1.6667) = +0.10 \times 0.5108 = \mathbf{0.0511}$
     * Bin 2: $(0.40 - 0.35) \times \ln(0.40 / 0.35) = +0.05 \times \ln(1.1429) = +0.05 \times 0.1335 = \mathbf{0.0067}$
     * Bin 3: $(0.25 - 0.35) \times \ln(0.25 / 0.35) = -0.10 \times \ln(0.7143) = -0.10 \times (-0.3365) = \mathbf{0.0336}$
     * Bin 4: $(0.10 - 0.15) \times \ln(0.10 / 0.15) = -0.05 \times \ln(0.6667) = -0.05 \times (-0.4055) = \mathbf{0.0203}$
  3. Summation:
     $$\text{Total PSI} = 0.0511 + 0.0067 + 0.0336 + 0.0203 = \mathbf{0.1117}$$
  4. Governance Action & Interpretation:
     * Thresholds: $\text{PSI} < 0.10$ (Stable), $0.10 \le \text{PSI} < 0.25$ (Moderate Shift), $\ge 0.25$ (Significant Shift).
     * $\text{PSI} = 0.1117$ indicates a **Moderate Population Shift**.
     * **Required Action**: The model does not need emergency suspension, but the analytics team must issue a Model Governance Early Warning notice, investigate whether applicant sourcing channels have shifted toward lower credit tiers, and monitor early vintage 30+ DPD roll rates.

---

## Domain 4: Banking Case Analysis & Business Metrics

### QB-CASE-01 | Level 2 (Applied)
* **Topic**: Credit Card Balance Attrition Diagnostics
* **Problem**: A retail card portfolio generates $\$120\text{M}$ in net interest revenue annually from an average revolving balance of $\$1.2\text{B}$ ($10\%$ Net Interest Margin). Over 6 months, revolving balance drops by $15\%$ to $\$1.02\text{B}$.
  Decompose this decline into customer churn vs lower balance per customer, and suggest 3 hypotheses.
* **Solution**:
  1. Mathematical Decomposition:
     $$\text{Total Revolving Balance} = \text{Active Revolving Accounts} \times \text{Average Revolving Balance per Account}$$
  2. Data Extraction Required:
     * Metric 1: Count of active revolvers ($N_{t} \text{ vs } N_{t-6}$).
     * Metric 2: Mean balance per revolver ($\bar{B}_t \text{ vs } \bar{B}_{t-6}$).
  3. Diagnostic Scenarios:
     * **Hypothesis 1 (Balance Transfer Cannibalization)**: Competitors launched 0% introductory APR balance transfer promotions, siphoning high-balance revolvers.
     * **Hypothesis 2 (Transactor Migration)**: Customers are paying off balances in full due to higher savings rates or tax refunds, converting from revolvers into interest-free transactors.
     * **Hypothesis 3 (Proactive Credit Limit Cuts)**: Automated risk policies tightened credit limits on subprime segments, capping balance expansion.

---

### QB-CASE-02 | Level 3 (Interview-Level)
* **Topic**: Real-Time Fraud Alert Desk Optimization
* **Problem**: Citi's debit card fraud model flags 40,000 transactions/day. Manual fraud investigators can only review 15,000 alerts/day. True fraud incidence among the alerts is $2.5\%$ (1,000 true frauds). How do you eliminate the 25,000 alert backlog without doubling headcount?
* **Solution**:
  1. Replace single binary threshold with a **Value-Weighted Tiered Risk Matrix**:
     * **Tier 1 (Extreme Confidence, $p \ge 0.85$)**: Auto-block transaction and send SMS verification code (Zero manual review; deflects $\sim 2,000$ alerts).
     * **Tier 2 (High Exposure: $p \ge 0.30$ AND $\text{Amount} > \$250$)**: Route to manual investigator desk (Staffed for 15,000 capacity; captures $\approx 850$ true frauds).
     * **Tier 3 (Low Exposure: $p < 0.30$ OR $\text{Amount} \le \$50$)**: Interactive App Push Notification (Customer confirms "Yes, it was me" or "No" in-app within 10 seconds; deflects $\sim 23,000$ alerts).
  2. **Result**: Manual desk burden drops from 40,000 to 15,000 cases/day. Investigator precision surges from $2.5\%$ to $>15\%$.

---

## Domain 5: Data Visualization & Executive Communication

### QB-VIZ-01 | Level 2 (Applied)
* **Topic**: Chart Selection & Visual Encoding
* **Question**: For each analytical scenario, name the optimal chart format and explain why common alternatives fail:
  1. Comparing monthly debit card transaction volumes over 36 consecutive months across 3 card tiers.
  2. Displaying the credit score distribution of 100,000 personal loan applicants to check for bimodality and outliers.
  3. Showing customer retention rates across 12 monthly lifecycle periods for 6 successive quarterly signup cohorts.
* **Answer**:
  1. **Multi-line Chart**: Continuous time on $X$-axis with 3 distinct colored lines. (Bar charts create visual clutter with $36 \times 3 = 108$ bars; pie charts fail on time-series).
  2. **Histogram with overlaid Kernel Density Estimate (KDE) or Box-and-Whisker Plot**: Shows skewness, secondary modal peaks (e.g., minimum score cutoff spikes), and extreme outliers. (A single mean and standard deviation completely conceals bimodality).
  3. **Cohort Retention Heatmap with embedded percentage labels**: Matrix with cohorts on rows, tenure months on columns, and color saturation showing retention decay.

---

### QB-VIZ-02 | Level 3 (Interview-Level)
* **Topic**: The Minto Pyramid Principle in Technical Presentations
* **Question**: You built an A/B test analysis of an automated credit limit increase pilot. How do you present the findings to a Managing Director in 60 seconds?
* **Answer Structure**:
  * **Lead with the Governing Recommendation (10 seconds)**:
    *"I recommend rolling out the automated credit limit increase feature to all 120,000 pre-qualified revolving cardholders, projected to generate $\$3.6\text{M}$ in incremental annual net interest revenue."*
  * **Present the Key Supporting Evidence (30 seconds)**:
    *"In our 90-day pilot across 20,000 accounts, treatment cardholders exhibited a statistically significant $18\%$ increase in average revolving balances with zero change in 30-day early delinquencies ($1.2\%\text{ vs } 1.1\%, p = 0.42$). The incremental interest margin comfortably exceeds credit provisioning costs by a 4-to-1 ratio."*
  * **Highlight Guardrails & Next Steps (20 seconds)**:
    *"We have implemented an automated circuit breaker that freezes limit increases if an account's bureau inquiries rise, and we will present our first 60-day post-launch audit in December."*

---

## Domain 6: Behavioural, Matrix Stakeholders & Risk Compliance

### QB-BEH-01 | Level 3 (Interview-Level)
* **Topic**: Ethical Pressure to Cherry-Pick Analytics
* **Question**: A marketing vice president is under severe pressure to meet annual acquisition targets. Your A/B test evaluation shows that while a new campaign increased customer signups by $+25\%$, the 6-month charge-off rate in that cohort is $3\times$ higher than baseline, making the campaign net-negative. The VP asks you: *"Please present only the signup lift and conversion velocity on the executive slide deck, and leave the delinquency metrics in the technical appendix."* How do you respond?
* **Model Answer**:
  1. **Empathy & Commercial Alignment**: Acknowledge the commercial achievement of delivering high signup volume.
  2. **Firm Commitment to Citi Risk Governance**: Politely but unequivocally refuse to conceal credit loss metrics. Cite Citigroup's explicit governance mandate: *appropriately assessing risk, safeguarding the firm's reputation and assets, and escalating control issues with transparency*.
  3. **Provide an Actionable Constructive Solution**:
     *"If we present only signups, leadership will approve full rollout, and the resulting credit write-offs will destroy portfolio P&L within 12 months. Instead, let's analyze which customer risk tiers drove the defaults. We can propose rolling out the campaign with tightened minimum credit score filters, capturing 70% of the conversion lift while filtering out the high-charge-off segment."*

---

### QB-BEH-02 | Level 3 (Interview-Level)
* **Topic**: Discovering an Error in a Published Report
* **Question**: You discover that a monthly regulatory reporting query you wrote contained an incorrect `INNER JOIN` instead of a `LEFT JOIN`, silently omitting accounts with zero balances for the past two quarters. The report has already been reviewed by internal audit. What do you do?
* **Model Answer**:
  1. **Never Conceal or Delay**: Immediately notify your direct team lead and the compliance oversight manager with full transparency.
  2. **Quantify the Exact Scope**: Immediately run an ad-hoc reconciliation query comparing the old output with the corrected output to determine exact account count and financial delta.
  3. **Propose the Remediation Plan**: Prepare an errata memo detailing the root cause, corrected numbers, and impact assessment.
  4. **Implement Systemic Preventive Controls**: Write an automated data-quality assertion test in the repository (e.g. `ASSERT reported_accounts == total_warehouse_accounts`) to ensure the bug can never recur.
