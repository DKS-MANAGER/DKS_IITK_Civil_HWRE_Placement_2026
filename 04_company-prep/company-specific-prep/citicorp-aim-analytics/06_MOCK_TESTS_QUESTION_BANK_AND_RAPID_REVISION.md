# Topic Master 06: Full Mocks, Multi-Tier Question Bank & Rapid Revision Cheat Sheet

> **Consolidated Module**: CITI-TOPIC-06 (Assessments, Practice Bank & Final Revision)  
> **Target Assessment**: Timed Screening Test Practice, Topic Mastery Drills & Night-Before Rapid Revision  
> **Scope**:
> - **SECTION A**: Timed Mock Assessments: Diagnostic Baseline Assessment (Diag-01), 3 Focused Sectional Tests, and 75-Minute Mixed Full Placement Mock Test (Full-01) with Answer Keys & Rubrics
> - **SECTION B**: Multi-Tier Practice Question Bank (Levels 1 to 4: Foundational, Standard Placement, Advanced Scenario, Grilling Technical) across all 6 Citi AIM domains with Step-by-Step Solutions
> - **SECTION C**: Rapid Revision Cheat Sheet: High-Yield Formulas, Top 10 SQL Banking Snippets, Scorecard Metric Reference (WoE, IV, KS, PSI), and Common Interview Traps

---

# PART I: Full-Length Timed Mock Assessments with Solutions

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


---

# PART II: Multi-Tier Banking Analytics Question Bank (Levels 1–4)

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


---

# PART III: Rapid Revision Cheat Sheet & High-Yield Formulas

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
