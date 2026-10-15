# 08. Practice Mock Assessments, Diagnostic Tests & Rubrics

> **Target Role**: Spec Analytics Analyst — Business Analytics (SBS), Citi AIM  
> **Evidence Policy**: The IIT Kanpur placement proforma establishes core competencies (basic statistics, hypothesis testing, SQL, Access, predictive modeling, segmentation, stakeholder management, compliance) but **does not specify official time limits, question formats, sectional cutoffs, or interview round structures**.  
> **Simulation Disclaimer**: All assessments in this module are `[PRACTICE SIMULATION ASSUMPTIONS]` designed for candidate self-testing and benchmark readiness.

---

## Assessment Suite Overview

| Assessment | Focus Area | Format / Difficulty | Duration | Total Marks | Target Mastery Score |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Diag-01** | **Diagnostic Baseline Assessment** | Mixed Multiple Choice & Numerical | 30 Mins | 25 Marks | $\ge 20$ ($80\%$) |
| **Mock-01** | **Statistics & Probability Sectional** | Numerical & Analytical (Standard & Difficult) | 45 Mins | 40 Marks | $\ge 32$ ($80\%$) |
| **Mock-02** | **SQL & Data Manipulation Sectional** | Query Writing & Query Debugging | 45 Mins | 40 Marks | $\ge 34$ ($85\%$) |
| **Mock-03** | **Predictive Modeling & Scorecards** | Metric Calculation & Threshold Setting | 45 Mins | 35 Marks | $\ge 28$ ($80\%$) |
| **Mock-04** | **Banking Business Analytics Cases** | 2 End-to-End Case Interviews | 45 Mins | 40 Marks | $\ge 32$ ($80\%$) |
| **Mock-05** | **Visualization & Executive Communication** | Chart Audits & Executive Minto Briefs | 30 Mins | 25 Marks | $\ge 20$ ($80\%$) |
| **Mock-06** | **Stakeholders, Ethics & Compliance** | Scenario Judgment & Escalation | 30 Mins | 25 Marks | $\ge 21$ ($84\%$) |
| **Full-01** | **Comprehensive Mixed Technical Mock** | Integrated Timed Simulation (All Domains) | 75 Mins | 100 Marks | $\ge 80$ ($80\%$) |
| **Def-01** | **Project & Resume Defense Simulation** | Grilling Rubric & Transferable Defense | 30 Mins | Qualitative | Grade: Ready |

---

## 1. Diag-01: Baseline Diagnostic Assessment (30 Mins | 25 Marks)

### Candidate Instructions:
* Attempt all 5 questions without using notes or internet searches.
* Calculators permitted for arithmetic. Show all intermediate steps.

#### Question 1 (5 Marks): Bayes' Theorem Alert Precision
A credit card fraud model monitors a transaction stream where the base rate of fraud is $P(F) = 0.001$ ($0.1\%$). When a transaction is fraudulent, the system triggers an alert with probability $98\%$. When a transaction is legitimate, it triggers a false alarm with probability $2\%$. Calculate the probability that an alerted transaction is genuine fraud.

#### Question 2 (5 Marks): SQL Logical Execution Sequence
Rank the following SQL clauses in their exact logical query-processing order:
`SELECT`, `WHERE`, `GROUP BY`, `HAVING`, `FROM & JOIN`, `ORDER BY`, `LIMIT`.  
Explain why a column alias defined in `SELECT` cannot be referenced inside `WHERE`.

#### Question 3 (5 Marks): Two-Sample Hypothesis Testing Choice
You want to test whether average card spend increased after an app redesign. You have monthly spend per user for 5,000 customers in August (before) and the same 5,000 customers in October (after). Which statistical test should you choose, and why is an independent-sample two-group $t$-test inappropriate?

#### Question 4 (5 Marks): Classification Metrics Under Imbalance
In a validation sample of 10,000 corporate loans, 100 borrowers default. A baseline model predicts "No Default" for all 10,000 loans.  
(a) What is the model's Accuracy?  
(b) What is the model's Recall?  
(c) Why is this model completely unacceptable for credit risk management?

#### Question 5 (5 Marks): Logistic Regression Odds Interpretation
In a loan approval model, the coefficient for `applicant_age` is $\beta = -0.02$. What is the odds ratio associated with an increase of 10 years in age? Interpret the numerical result.

---

### Diag-01 Answer Key & Explanations

* **Q1 Solution (5 Marks)**:
  * Prior: $P(F) = 0.001, P(F^c) = 0.999$. Sensitivity: $P(A \mid F) = 0.98$. False Positive Rate: $P(A \mid F^c) = 0.02$.
  * Total Probability: $P(A) = (0.98 \times 0.001) + (0.02 \times 0.999) = 0.00098 + 0.01998 = 0.02096$.
  * Posterior: $P(F \mid A) = \frac{0.00098}{0.02096} \approx \mathbf{0.04676} \quad (\mathbf{4.68\%})$. [3 marks for formula, 2 for calculation].
* **Q2 Solution (5 Marks)**:
  * Order: 1. `FROM & JOIN` $\to$ 2. `WHERE` $\to$ 3. `GROUP BY` $\to$ 4. `HAVING` $\to$ 5. `SELECT` $\to$ 6. `ORDER BY` $\to$ 7. `LIMIT`. [3 marks]
  * Explanation: `WHERE` filters individual rows in Step 2, before column expressions and aliases are evaluated in Step 5 (`SELECT`). [2 marks]
* **Q3 Solution (5 Marks)**:
  * Choice: **Paired-sample $t$-test** (Dependent $t$-test). [2 marks]
  * Reason: The measurements are taken on the exact same subjects before and after, violating the independence assumption of an independent two-sample test. A paired test controls for customer-specific baseline variance. [3 marks]
* **Q4 Solution (5 Marks)**:
  * (a) Accuracy $= \frac{9,900}{10,000} = \mathbf{99.0\%}$. [1 mark]
  * (b) Recall $= \frac{\text{TP}}{\text{TP} + \text{FN}} = \frac{0}{0 + 100} = \mathbf{0.0\%}$. [2 marks]
  * (c) Unacceptable because it fails to intercept a single defaulting loan, exposing the bank to 100% of unmitigated credit write-offs despite 99% accuracy. [2 marks]
* **Q5 Solution (5 Marks)**:
  * Change in log-odds for $\Delta X = 10$: $\Delta Z = 10 \times (-0.02) = -0.20$. [2 marks]
  * Odds Ratio $= e^{-0.20} \approx \mathbf{0.8187}$. [2 marks]
  * Interpretation: An applicant who is 10 years older has approximately **$18.1\%$ lower odds of default** ($1 - 0.8187$), holding all other variables constant. [1 mark]

---

## 2. Mock-01: Statistics & Probability Sectional (45 Mins | 40 Marks)

### Section A: Standard Level (20 Marks)
1. **Problem 1 (10 Marks)**: Daily customer service chat inquiries follow a Poisson distribution with mean $\lambda = 4\text{ inquiries/hour}$.
   * (a) What is the probability that exactly 2 inquiries arrive in a given hour? (3 Marks)
   * (b) What is the probability that at least 1 inquiry arrives in a 30-minute window? (4 Marks)
   * (c) What is the expected time (in minutes) between consecutive inquiries, and what distribution models this waiting time? (3 Marks)
2. **Problem 2 (10 Marks)**: An automated underwriting system samples $n = 100$ loan applications. Sample mean credit score is $\bar{X} = 712$, with sample standard deviation $s = 40$.
   * (a) Calculate the $95\%$ confidence interval for the population mean credit score ($Z_{0.025} = 1.96$). (5 Marks)
   * (b) A business manager claims: *"There is a 95% probability that the true mean is between the calculated bounds."* Explain precisely why this statement is technically flawed. (5 Marks)

### Section B: Difficult Level (20 Marks)
3. **Problem 3 (10 Marks)**: A retail bank tests whether a reduction in ATM surcharge fees increases customer monthly cash withdrawal frequency.
   * Control: $n_1 = 250, \bar{X}_1 = 4.2\text{ withdrawals/mo}, s_1 = 1.8$.
   * Treatment: $n_2 = 250, \bar{X}_2 = 4.6\text{ withdrawals/mo}, s_2 = 2.0$.
   * (a) Conduct a two-tailed Welch's $t$-test at $\alpha = 0.05$. Show test statistic and compare to critical value $\pm 1.96$. (6 Marks)
   * (b) If rolling out the fee reduction costs the bank $\$500,000$ annually in lost ATM fees and generates $\$320,000$ in new account revenue, should leadership roll it out based on the statistical significance? Explain the distinction between statistical and economic significance. (4 Marks)
4. **Problem 4 (10 Marks)**: An analyst runs 20 simultaneous independent hypothesis tests comparing product retention across 20 distinct sub-demographics, using standard $\alpha = 0.05$ on each test.
   * (a) What is the probability of observing at least one False Positive (Type I error) by pure random chance if all 20 null hypotheses are true? (5 Marks)
   * (b) What is the Bonferroni-corrected significance threshold $\alpha^*$ required to control family-wise error rate at $0.05$? (5 Marks)

---

### Mock-01 Answer Key & Solutions

* **Problem 1**:
  * (a) $P(X=2) = \frac{4^2 e^{-4}}{2!} = \frac{16 \times 0.018316}{2} = \mathbf{0.1465} \quad (14.65\%)$.
  * (b) For 30 mins, $\lambda' = 4 \times 0.5 = 2$. $P(X \ge 1) = 1 - P(X = 0) = 1 - e^{-2} = 1 - 0.1353 = \mathbf{0.8647} \quad (86.47\%)$.
  * (c) Expected time $= \frac{1}{\lambda} = \frac{1}{4}\text{ hour} = \mathbf{15\text{ minutes}}$. Modeled by the **Exponential distribution** ($\lambda = 4\text{ hr}^{-1}$).
* **Problem 2**:
  * (a) $\text{SE} = \frac{s}{\sqrt{n}} = \frac{40}{\sqrt{100}} = 4.0$. $\text{CI} = 712 \pm 1.96(4.0) = 712 \pm 7.84 = [\mathbf{704.16, 719.84}]$.
  * (b) The true population parameter $\mu$ is a fixed, non-random constant, not a random variable. The calculated interval is also fixed. The parameter is either in the interval or it is not (probability is 1 or 0). The 95% confidence refers to the *procedure*: across repeated independent samples, 95% of constructed intervals will cover the true parameter.
* **Problem 3**:
  * (a) $\text{SE} = \sqrt{\frac{1.8^2}{250} + \frac{2.0^2}{250}} = \sqrt{\frac{3.24 + 4.00}{250}} = \sqrt{\frac{7.24}{250}} = \sqrt{0.02896} \approx \mathbf{0.17018}$.
    $t = \frac{4.6 - 4.2}{0.17018} = \frac{0.4}{0.17018} \approx \mathbf{2.35}$.
    Since $|t| = 2.35 > 1.96$, **Reject $H_0$** ($p \approx 0.019$).
  * (b) **Do not roll out.** The lift is statistically significant, but economically value-destroying: Net P&L $= \$320,000 - \$500,000 = -\$180,000/\text{year}$. Statistical significance proves the effect is not sampling noise; economic significance evaluates whether the financial return exceeds capital and operating costs.
* **Problem 4**:
  * (a) $\alpha_{\text{family}} = 1 - (1 - \alpha)^m = 1 - (0.95)^{20} = 1 - 0.3585 = \mathbf{0.6415} \quad (\mathbf{64.15\%})$.
  * (b) Bonferroni threshold: $\alpha^* = \frac{\alpha}{m} = \frac{0.05}{20} = \mathbf{0.0025}$.

---

## 3. Mock-02: SQL & Data Manipulation Sectional (45 Mins | 40 Marks)

### Schema Provided (`[PRACTICE CASE ASSUMPTION]`):
* `customers (cust_id VARCHAR, name VARCHAR, join_date DATE, tier VARCHAR)`
* `accounts (account_id VARCHAR, cust_id VARCHAR, acct_type VARCHAR, credit_limit DECIMAL, status VARCHAR)`
* `transactions (txn_id VARCHAR, account_id VARCHAR, txn_date TIMESTAMP, amount DECIMAL, txn_type VARCHAR, status VARCHAR)`
* `monthly_snapshots (account_id VARCHAR, month_end DATE, balance DECIMAL, dpd INT)`

---

#### Task 1: Deduplication & Clean Join (10 Marks)
Find all distinct customers who hold at least one active credit card and have spent over $\$5,000$ in total approved debit transactions across their credit cards in 2026.
* **Solution**:
  ```sql
  SELECT 
      c.cust_id,
      c.name,
      SUM(t.amount) AS total_card_spend
  FROM customers c
  JOIN accounts a 
      ON c.cust_id = a.cust_id 
     AND a.acct_type = 'CREDIT_CARD' 
     AND a.status = 'ACTIVE'
  JOIN transactions t 
      ON a.account_id = t.account_id 
     AND t.txn_type = 'DEBIT' 
     AND t.status = 'APPROVED'
     AND t.txn_date >= '2026-01-01' AND t.txn_date < '2027-01-01'
  GROUP BY c.cust_id, c.name
  HAVING SUM(t.amount) > 5000.00
  ORDER BY total_card_spend DESC;
  ```

---

#### Task 2: Second Highest Transaction per Account (10 Marks)
For each account, find the **exact details of their second highest approved debit transaction**. If an account has multiple transactions sharing the highest amount, the second distinct tier must be returned.
* **Solution**:
  ```sql
  WITH RankedTransactions AS (
      SELECT 
          account_id,
          txn_id,
          txn_date,
          amount,
          DENSE_RANK() OVER (
              PARTITION BY account_id 
              ORDER BY amount DESC
          ) AS spend_rank
      FROM transactions
      WHERE status = 'APPROVED' AND txn_type = 'DEBIT'
  )
  SELECT account_id, txn_id, txn_date, amount
  FROM RankedTransactions
  WHERE spend_rank = 2;
  ```
  *(Explains why `DENSE_RANK` is required instead of `ROW_NUMBER` or `RANK`).*

---

#### Task 3: Month-over-Month Balance Growth & Delinquency Surge (10 Marks)
From `monthly_snapshots`, identify all credit card accounts whose balance increased by more than $50\%$ between August 31, 2026 and September 30, 2026, AND whose Days Past Due (`dpd`) rose from 0 to $>0$.
* **Solution**:
  ```sql
  SELECT 
      aug.account_id,
      aug.balance AS aug_balance,
      sept.balance AS sept_balance,
      ROUND(((sept.balance - aug.balance) / NULLIF(aug.balance, 0)) * 100, 2) AS balance_growth_pct,
      sept.dpd AS current_dpd
  FROM monthly_snapshots aug
  JOIN monthly_snapshots sept 
      ON aug.account_id = sept.account_id 
     AND aug.month_end = '2026-08-31' 
     AND sept.month_end = '2026-09-30'
  WHERE aug.dpd = 0 
    AND sept.dpd > 0
    AND sept.balance >= 1.50 * aug.balance
  ORDER BY balance_growth_pct DESC;
  ```

---

#### Task 4: Consecutive Month Inactivity (Gaps Analysis) (10 Marks)
Find active accounts that have generated zero transactions in the trailing 90 days as of `2026-09-30`.
* **Solution**:
  ```sql
  SELECT 
      a.account_id,
      a.cust_id,
      a.acct_type,
      MAX(t.txn_date) AS last_txn_date
  FROM accounts a
  LEFT JOIN transactions t 
      ON a.account_id = t.account_id 
     AND t.status = 'APPROVED'
  WHERE a.status = 'ACTIVE'
  GROUP BY a.account_id, a.cust_id, a.acct_type
  HAVING MAX(t.txn_date) < '2026-09-30'::DATE - INTERVAL '90 DAYS'
      OR MAX(t.txn_date) IS NULL;
  ```

---

## 4. Full-01: Comprehensive Mixed Technical Mock Exam (75 Mins | 100 Marks)

### Section Structure:
* **Part I: Quantitative Reasoning & Probability (25 Marks)**
* **Part II: SQL Architecture & Complex Queries (25 Marks)**
* **Part III: Predictive Modeling, Metrics & Scorecards (25 Marks)**
* **Part IV: Commercial Banking Analytics & Governance (25 Marks)**

---

### Part I: Quantitative Reasoning & Probability (25 Marks)

#### Q1 (10 Marks): Joint Probability & Risk Exposures
Two loan portfolios $X$ and $Y$ have default rates $P(X) = 0.05$ and $P(Y) = 0.08$. The joint default probability is $P(X \cap Y) = 0.015$.
* (a) Are defaults in Portfolio $X$ and $Y$ independent? Prove mathematically. (4 Marks)
* (b) What is the probability that at least one portfolio defaults? (3 Marks)
* (c) Given that Portfolio $Y$ has defaulted, what is the conditional probability that Portfolio $X$ defaults? (3 Marks)
* **Solution**:
  * (a) If independent, $P(X \cap Y) = P(X) \times P(Y) = 0.05 \times 0.08 = 0.0040$. Since observed $P(X \cap Y) = 0.015 \neq 0.0040$, defaults are **NOT independent**; they are positively correlated.
  * (b) $P(X \cup Y) = P(X) + P(Y) - P(X \cap Y) = 0.05 + 0.08 - 0.015 = \mathbf{0.115} \quad (11.5\%)$.
  * (c) $P(X \mid Y) = \frac{P(X \cap Y)}{P(Y)} = \frac{0.015}{0.08} = \mathbf{0.1875} \quad (18.75\%)$. Default in $Y$ almost quadruples the default risk of $X$ from $5\%$ to $18.75\%$.

#### Q2 (15 Marks): Minimum Detectable Effect in Card Spend A/B Test
A credit card portfolio has mean monthly spend $\mu = \$1,200$ with standard deviation $\sigma = \$600$. Management wants to test a cashback feature with $N = 2,500$ cardholders per variant at $\alpha = 0.05$ (two-sided, $Z_{0.025} = 1.96$) and Power $= 0.80$ ($Z_{0.20} = 0.84$).
* (a) Calculate the Minimum Detectable Effect (MDE in dollars). (8 Marks)
* (b) What is the relative MDE percentage? (3 Marks)
* (c) If management requires detecting an MDE of only $\$15$, what sample size per group is needed? (4 Marks)
* **Solution**:
  * (a) Formula: $\text{MDE} = (Z_{\alpha/2} + Z_\beta) \times \sigma \times \sqrt{\frac{2}{n}} = (1.96 + 0.84) \times 600 \times \sqrt{\frac{2}{2500}} = 2.80 \times 600 \times \sqrt{0.0008} = 1680 \times 0.028284 \approx \mathbf{\$47.52}$.
  * (b) Relative $\text{MDE} = \frac{\$47.52}{\$1,200} \approx \mathbf{3.96\%}$.
  * (c) Required $n = \frac{2 (Z_{\alpha/2} + Z_\beta)^2 \sigma^2}{\Delta^2} = \frac{2 (2.80)^2 (600)^2}{15^2} = \frac{2 \times 7.84 \times 360,000}{225} = \frac{5,644,800}{225} = \mathbf{25,088\text{ accounts per variant}}$.

---

### Part II: SQL Architecture & Complex Queries (25 Marks)

#### Q3 (25 Marks): Rolling 30-Day Velocity & Suspicious Activity SQL
Write a query to identify any account where the customer executed **3 or more transactions of amount $\ge \$1,000$ within any rolling 24-hour window** in October 2026. Return `account_id`, the start timestamp of the window, and the total transaction sum in that window.
* **Solution**:
  ```sql
  WITH QualifiedTxns AS (
      SELECT 
          account_id,
          txn_id,
          txn_date,
          amount
      FROM transactions
      WHERE status = 'APPROVED'
        AND amount >= 1000.00
        AND txn_date >= '2026-10-01' AND txn_date < '2026-11-01'
  ),
  WindowAggregations AS (
      SELECT 
          t1.account_id,
          t1.txn_id AS window_start_txn,
          t1.txn_date AS window_start_time,
          COUNT(t2.txn_id) AS txns_in_24h,
          SUM(t2.amount) AS total_24h_amount
      FROM QualifiedTxns t1
      JOIN QualifiedTxns t2 
          ON t1.account_id = t2.account_id
         AND t2.txn_date >= t1.txn_date
         AND t2.txn_date <= t1.txn_date + INTERVAL '24 HOURS'
      GROUP BY t1.account_id, t1.txn_id, t1.txn_date
  )
  SELECT 
      account_id,
      window_start_time,
      txns_in_24h,
      total_24h_amount
  FROM WindowAggregations
  WHERE txns_in_24h >= 3
  ORDER BY account_id, window_start_time;
  ```

---

### Part III: Predictive Modeling, Metrics & Scorecards (25 Marks)

#### Q4 (25 Marks): Scorecard KS Separation & Decile Analysis
Given the following risk score validation distribution:
```
Decile 1 (High Risk): Total = 1,000 | Bads = 350 | Goods = 650
Decile 2            : Total = 1,000 | Bads = 250 | Goods = 750
Decile 3            : Total = 1,000 | Bads = 150 | Goods = 850
Decile 4            : Total = 1,000 | Bads = 100 | Goods = 900
Deciles 5 to 10     : Total = 6,000 | Bads = 150 | Goods = 5,850
Total               : Total = 10,000| Bads = 1,000| Goods = 9,000
```
* (a) Compute Cumulative Bad %, Cumulative Good %, and KS Separation for Deciles 1 through 4. (12 Marks)
* (b) Identify the peak KS statistic and its decile location. (5 Marks)
* (c) Is this model suitable for deployment in credit underwriting? Justify based on industry standards. (8 Marks)
* **Solution**:
  * Total Bads $= 1,000$. Total Goods $= 9,000$.
  * **Decile 1**:
    * Cum Bads $= 350 / 1000 = \mathbf{35.0\%}$.
    * Cum Goods $= 650 / 9000 = \mathbf{7.22\%}$.
    * KS Separation $= 35.0\% - 7.22\% = \mathbf{27.78\%}$.
  * **Decile 2**:
    * Cum Bads $= (350 + 250) / 1000 = 600 / 1000 = \mathbf{60.0\%}$.
    * Cum Goods $= (650 + 750) / 9000 = 1400 / 9000 = \mathbf{15.56\%}$.
    * KS Separation $= 60.0\% - 15.56\% = \mathbf{44.44\%}$.
  * **Decile 3**:
    * Cum Bads $= (600 + 150) / 1000 = 750 / 1000 = \mathbf{75.0\%}$.
    * Cum Goods $= (1400 + 850) / 9000 = 2250 / 9000 = \mathbf{25.0\%}$.
    * KS Separation $= 75.0\% - 25.0\% = \mathbf{50.00\%}$ (**Peak KS**).
  * **Decile 4**:
    * Cum Bads $= (750 + 100) / 1000 = 850 / 1000 = \mathbf{85.0\%}$.
    * Cum Goods $= (2250 + 900) / 9000 = 3150 / 9000 = \mathbf{35.0\%}$.
    * KS Separation $= 85.0\% - 35.0\% = \mathbf{50.00\%}$.
  * **Assessment**:
    * Peak KS $= \mathbf{50.0\%}$, occurring at Decile 3.
    * **Yes, highly suitable.** Industry standard considers $\text{KS} > 40\%$ strong separation. Crucially, peak separation occurs early (Decile 3), capturing $75\%$ of all defaults in the top $30\%$ of applications.

---

### Part IV: Commercial Banking Analytics & Governance (25 Marks)

#### Q5 (25 Marks): Case Brief — Digital Deposit Drainage Diagnostics
* **Problem**: A retail banking division discovers that average balances among primary salaried customers declined by $12\%$ over two quarters, despite a $+3\%$ increase in customer headcount.
  1. Draw an analytical issue tree decomposing this problem. (8 Marks)
  2. What SQL queries would you execute across transaction data to isolate the destination of departing funds? (8 Marks)
  3. Formulate an executive recommendation balancing interest expense against customer retention. (9 Marks)
* **Solution**:
  1. **Issue Tree**:
     * Total Balances $=$ Accounts $\times$ Average Balance. (Accounts $+3\%$, so Average Balance dropped $\approx 14.6\%$).
     * Average Balance $=$ Inflows $-$ Outflows.
     * Inflows: Payroll changes? Bonuses cut?
     * Outflows: Consumer spending (debit/credit)? Competitor bank transfers? Investment platforms (mutual funds/brokerages)? Debt prepayments?
  2. **SQL Investigation**:
     * Query outbound transfers grouped by beneficiary category (Merchant Category Codes, IFSC bank routing codes, NEFT/UPI recipient names).
     * Filter for high-growth outflow destinations: `WHERE txn_type = 'DEBIT' GROUP BY recipient_category`.
  3. **Executive Recommendation**:
     * If outflows are migrating to capital markets: Launch an **Auto-Sweep High-Yield Savings Account** that sweeps surplus funds over ₹50,000 into flexible fixed deposits, while integrating mutual fund advisory tools within the mobile app to capture fee revenue.

---

## 5. Topic-Level Performance Rubric & Mastery Standards

| Score Achieved | Overall Rating | Diagnostic Feedback & Action Plan |
| :--- | :--- | :--- |
| **$\ge 85$ Marks** | **Interview Ready (Top Tier)** | Excellent quantitative rigor, SQL query accuracy, and commercial acumen. Review Rapid Revision formula sheet and proceed to interview defense. |
| **70 — 84 Marks** | **Meets Standards (Passing)** | Strong foundations. Identify weak sectional areas (e.g. window frame defaults or Welch's $df$ formulas) and re-attempt corresponding practice problems. |
| **50 — 69 Marks** | **Developing (Needs Reinforcement)** | Foundational gaps identified in SQL execution order, confusion matrix asymmetric costs, or hypothesis test selection. Re-study Modules 01, 02, and 03 thoroughly. |
| **$< 50$ Marks** | **Unprepared** | Re-read the textbook modules from Module 01 in sequential order. Do not attempt technical mocks until worked examples are fully mastered. |
