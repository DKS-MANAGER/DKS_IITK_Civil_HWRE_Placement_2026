# 04. Banking Business Cases, Puzzles & Practice Workbook

> **Target Role**: Spec Analytics Analyst — Business Analytics (SBS), Citi AIM  
> **Relevance**: Evaluated in Technical Round 2, Case Interviews, and Commercial Acumen Discussions.  
> **Evidence Policy**: All scenarios, customer counts, monetary values, and model outputs in this module are `[PRACTICE CASE ASSUMPTION]` synthetic benchmarks designed for interview practice.

---

## 1. End-to-End Banking Analytics Business Cases

Every business case in this section is analyzed using a standard 10-point structure:
`1. Problem Statement | 2. Questions to Clarify | 3. Structure / Framework | 4. Data Required | 5. Analysis Plan | 6. Calculations & Synthetic Data | 7. Interpretation | 8. Recommendation & Trade-Offs | 9. Risks & Limitations | 10. Follow-Up Interviewer Questions`

---

### Case 01: Credit Card Default Risk & Approval Cut-Off Optimization
*Topic: Predictive-Model Evaluation & Threshold Setting*

1. **Problem Statement**: Citi's consumer credit division is launching an unsecured digital credit card. A logistic regression scorecard has been trained to output an estimated Probability of Default ($PD \in [0, 1]$). What is the optimal decision threshold ($PD_{cutoff}$) to approve versus decline applicants?
2. **Questions to Clarify**:
   * What constitutes a "Default"? (Typically $90+$ Days Past Due within 12 months of booking).
   * What are the unit economics of an approved account? (Average lifetime revenue from a good customer vs net loss from a charge-off).
   * Is our strategic objective maximizing total net profit, or expanding market share subject to a maximum portfolio loss rate constraint?
3. **Analytical Framework**:
   * Expected Profit per approved applicant as a function of default probability $p$:
     $$E[\text{Profit}(p)] = (1 - p) \cdot R - p \cdot L$$
     Where $R$ is average lifetime revenue from a non-defaulter, and $L$ is net charge-off loss from a defaulter.
4. **Data Required**:
   * Scorecard predicted default probabilities on out-of-time validation set.
   * Historical unit economics: Interchange fees, revolving interest, annual fees, recovery rates on collections.
5. **Analysis Plan**:
   * Set $E[\text{Profit}] \ge 0$ to derive the mathematical break-even threshold.
   * Incorporate cost of capital, operational underwriting cost, and target Return on Equity (ROE) to establish operational buffer.
6. **Calculations (`[PRACTICE CASE ASSUMPTION]` applied)**:
   * Revenue per Good Customer ($R$) = $+\$600$.
   * Net Loss per Bad Customer ($L$) = $-\$2,400$.
   * Break-even equation:
     $$(1 - p)(600) - p(2400) = 0 \implies 600 - 3000p = 0 \implies p^* = \frac{600}{3000} = \mathbf{0.20} \quad (20.0\%)$$
7. **Interpretation**: Pure mathematical break-even occurs at $PD = 20\%$. Approving any customer with model risk $PD \le 20\%$ produces non-negative expected cash flow.
8. **Recommendation & Trade-Offs**:
   * **Recommendation**: Do NOT set operational cutoff at the $20\%$ mathematical ceiling. Factor in a required cost-of-capital hurdle (15% ROE) and regulatory provisioning reserves (CECL). Set operational cutoff at $PD_{cutoff} = \mathbf{10.0\%}$.
   * **Trade-Off**: Lowering cutoff from $20\%$ to $10\%$ sacrifices $\approx 12\%$ of marginal application volume, but cuts projected portfolio write-offs by $45\%$, ensuring resilient asset quality through macroeconomic cycles.
9. **Risks & Limitations**: Model calibration drift over time; macroeconomic downturns (e.g., rising unemployment) shift the actual default probability upward for any given model score.
10. **Follow-Up Questions**:
    * *"What if management demands increasing approval volume by 15% without increasing the credit loss budget?"* $\implies$ Recommend offering conditional approvals with reduced initial credit limits (e.g., $\$1,000$ limit instead of $\$5,000$) to cap absolute loss exposure while acquiring the customer.

---

### Case 02: Retail Deposit Balance Inflow Deterioration
*Topic: Business KPI Deterioration & Root-Cause Diagnostics*

1. **Problem Statement**: Citi Corporate Banking observes a **15% year-over-year decline** in quarterly deposit balances across salaried corporate accounts in India. You are tasked with diagnosing the cause and formulating an analytical recovery plan.
2. **Questions to Clarify**:
   * Is the decline driven by customer churn (fewer accounts) or lower balance per account?
   * Is the decline uniform across all salary tiers or concentrated in specific income bands?
   * Have corporate partners changed payroll providers?
3. **Diagnostic Framework (Issue Tree)**:
   $$\text{Total Deposits} = \text{Active Accounts} \times \text{Average Balance per Account}$$
   * *Branch A (Account Count)*: Corporate client contract losses? Employee layoffs? Competitor switching?
   * *Branch B (Balance per Account)*: Lower salary inflows? Or higher outgoing fund transfers?
   * *Branch C (Outflow Destinations)*: Wire transfers (NEFT/RTGS/UPI) to third-party investment brokerages vs competing banks vs loan prepayments.
4. **Data Required**:
   * Transaction-level outflow records, account balance snapshots, corporate employer rosters over trailing 24 months.
5. **Analysis Plan (SQL & Cohort Analysis)**:
   * Query outgoing transfer categories by merchant and recipient bank IFSC codes.
   * Cross-tabulate balance decline against customer wealth tiers.
6. **Calculations (`[PRACTICE CASE ASSUMPTION]` applied)**:
   * Account count remained completely flat (zero corporate contract loss).
   * Inflows from corporate payroll grew $+4\%$ YoY.
   * Outgoing wire transfers to online discount brokerages (mutual funds, equity SIPs) increased by $+48\%$ YoY, representing $78\%$ of total net deposit drain.
7. **Interpretation**: Salaried customers are not leaving Citi; they are actively siphoning idle cash into higher-yielding capital market investment instruments due to inflation and low savings interest rates ($3.0\%$).
8. **Recommendation & Trade-Offs**:
   * **Recommendation**: Launch an automated **Multi-Option Deposit (Auto-Sweep)** product. Balances over ₹50,000 automatically sweep into liquid flexi-fixed deposits earning $6.8\%$ with instant liquidity. Simultaneously offer in-app mutual fund investment integration.
   * **Trade-Off**: Increases bank interest expense, but completely halts deposit flight and captures fee revenue through wealth management cross-selling.
9. **Risks & Limitations**: Interest margin compression if low-cost CASA (Current Account Savings Account) ratio declines too fast.
10. **Follow-Up Questions**:
    * *"How would you measure the success of the auto-sweep launch?"* $\implies$ Track 90-day Net Deposit Retention, Wealth Product Penetration Rate, and Net Interest Margin (NIM) variance.

---

### Case 03: Optimizing Real-Time Fraud Alert Thresholds
*Topic: Transaction Anomalies & Operational Performance*

1. **Problem Statement**: Citi's real-time debit card fraud detection system screens 10 million transactions daily. The current model flags 50,000 transactions daily ($0.50\%$) as suspicious, generating an automated card block and an alert to the operations review desk. However, manual investigations reveal that **only 1,000 of the 50,000 alerts are genuine fraud** ($\text{Precision} = 2.0\%$). The review team can only handle 20,000 cases per day. How do you optimize the system?
2. **Questions to Clarify**:
   * What is the average dollar loss of an uncaught fraudulent transaction?
   * What is the cost (customer friction, churn, operational call cost) of a false positive card block?
   * Does the review desk examine transactions before or after authorization?
3. **Analytical Framework**:
   * Replace single binary alert threshold with a **Tiered Risk Matrix** combining Model Predicted Probability ($p$) with Transaction Monetary Value ($V$).
4. **Data Required**:
   * Historical transaction authorization logs, fraud confirmation labels, operational case review times, customer churn logs following false blocks.
5. **Analysis Plan**:
   * Evaluate Precision-Recall curves. Segment transactions into risk-value matrix buckets.
6. **Calculations (`[PRACTICE CASE ASSUMPTION]` applied)**:
   * Current State: 50,000 alerts, 1,000 true frauds, 49,000 false positives ($\text{Precision} = 2\%$). Operational capacity = 20,000 alerts (backlog of 30,000 unreviewed alerts).
   * Proposed 3-Tier Policy Matrix:
     * *Tier 1 ($p \ge 0.80$)*: High-confidence fraud. $\approx 1,500$ txns/day (captures 850 true frauds). Action: **Immediate Hard Block** + SMS notification.
     * *Tier 2 ($0.25 \le p < 0.80$ AND Amount $> \$200$)*: Medium confidence, high financial exposure. $\approx 12,000$ txns/day (captures 120 true frauds). Action: **Push Notification / Interactive 2FA**. Cardholder approves in-app within seconds.
     * *Tier 3 ($p < 0.25$ OR Amount $\le \$50$)*: Low risk / low value. $\approx 36,500$ txns/day. Action: **Silent Post-Auth Asynchronous Batch Monitoring**.
7. **Interpretation**: Manual desk review burden drops from 50,000 to $<14,000$ cases/day (comfortably below 20,000 staffing capacity). Review precision surges from $2\%$ to $>25\%$.
8. **Recommendation & Trade-Offs**:
   * **Recommendation**: Deploy tiered rule matrix.
   * **Trade-Off**: Letting micro-value transactions ($< \$20$) pass without blocking accepts $\approx \$15,000$ in annual gross loss, but saves $\$450,000$ in operational call center staffing and prevents customer churn.
9. **Risks & Limitations**: Fraudsters testing cards with small micro-charges (card testing attacks) before placing large transactions. Mitigate via velocity rules (count of attempts within 5 minutes).
10. **Follow-Up Questions**:
    * *"What metric should be monitored on day 1 of rollout?"* $\implies$ Cardholder complaint volume and False Positive Rate by merchant category.

---

### Case 04: A/B Testing a Personal Loan Cross-Sell Campaign
*Topic: Campaign Performance & A/B Testing*

1. **Problem Statement**: Citi's consumer lending team wants to test whether adding personalized pre-approved personal loan offers inside the mobile banking app increases loan bookings. How do you design, size, and evaluate this A/B test?
2. **Questions to Clarify**:
   * What is the primary success metric? (Loan booking conversion rate).
   * What is the secondary / guardrail metric? (App load speed, customer opt-outs, 90-day early delinquency).
   * What is the baseline conversion rate and Minimum Detectable Effect (MDE)?
3. **Analytical Framework**:
   * Randomized Controlled Trial (RCT): Control ($A$) = standard generic banner; Treatment ($B$) = personalized pre-approved loan card with calculated monthly installment.
4. **Data Required**:
   * Eligible active mobile app user base ($N \approx 500,000$), baseline historical conversion rate ($p_0 = 2.0\%$).
5. **Analysis Plan**:
   * Power analysis to determine minimum sample size per variant for $\alpha = 0.05, \text{Power} = 0.80, \text{MDE} = +0.4\%$ absolute ($20\%$ relative lift).
   * Two-proportion $Z$-test on completed bookings.
6. **Calculations (`[PRACTICE CASE ASSUMPTION]` applied)**:
   * Sample size formula: $n \approx \frac{2(Z_{\alpha/2} + Z_\beta)^2 p(1 - p)}{\Delta^2} \approx \frac{2(1.96 + 0.84)^2 (0.02 \times 0.98)}{(0.004)^2} \approx \frac{2(7.84)(0.0196)}{0.000016} \approx \mathbf{19,208\text{ users per variant}}$.
   * Round to 20,000 users per group. Test run duration = 14 days (to account for day-of-week seasonality).
   * Test Results:
     * Control: $n_1 = 20,000$, Conversions = 410 ($\hat{p}_1 = 2.05\%$).
     * Treatment: $n_2 = 20,000$, Conversions = 530 ($\hat{p}_2 = 2.65\%$).
     * Two-proportion test yields $Z = 3.98, p < 0.001$.
7. **Interpretation**: The personalized pre-approved feature produced a statistically significant $+29.3\%$ relative lift in loan conversions ($p < 0.001$).
8. **Recommendation & Trade-Offs**:
   * **Recommendation**: Roll out Variant B across all eligible mobile banking users.
   * **Trade-Off**: Requires ongoing data pipeline integration to refresh pre-approval limits nightly, adding cloud data processing costs ($\approx \$15,000/\text{year}$), which is easily justified by the projected $\$2.4\text{M}$ incremental annual interest margin.
9. **Risks & Limitations**: "Novelty effect" (click-through rates temporarily high because feature is new); long-term default rate of pre-approved borrowers must be tracked for 12 months.
10. **Follow-Up Questions**:
    * *"What if the product manager wanted to stop the test on Day 3 because $p < 0.05$ already?"* $\implies$ Explain the Peeking Problem: Early stopping on unadjusted alpha inflates false positive risk from 5% to $>30\%$. Enforce running to full pre-determined sample size.

---

### Case 05: RFM Customer Segmentation for Wealth Management
*Topic: Customer Segmentation & Unsupervised Learning*

1. **Problem Statement**: Citi Wealth Management wants to identify the most promising retail banking clients for cross-selling high-margin wealth advisory services. How do you design an analytical segmentation model?
2. **Questions to Clarify**:
   * What features define wealth propensity? (Balances, investment history, transaction stability).
   * What is the capacity of the wealth advisory sales desk? (e.g., 5,000 clients/quarter).
3. **Analytical Framework**:
   * Recency, Frequency, Monetary (RFM) composite score combined with K-Means clustering.
4. **Data Required**:
   * Trailing 12-month transaction counts, salary inflow magnitude, liquid deposit balances, debit card spend.
5. **Analysis Plan**:
   * Normalize features using RobustScaler (to handle high-net-worth outliers).
   * Compute Silhouette score to identify optimal $K$ ($K = 4$ clusters).
6. **Calculations (`[PRACTICE CASE ASSUMPTION]` applied)**:
   * Cluster 1: "Emerging Affluent" ($R \uparrow, F \uparrow, M \text{ moderate}$, high salary growth) $\implies 8\%$ of base.
   * Cluster 2: "High-Net-Worth Whales" ($R \text{ moderate}, F \text{ low}, M \text{ very high}$) $\implies 2\%$ of base.
   * Cluster 3: "Active Daily Transactors" ($R \uparrow, F \text{ very high}, M \text{ low}$) $\implies 45\%$ of base.
   * Cluster 4: "Dormant Low-Value" ($R \downarrow, F \downarrow, M \downarrow$) $\implies 45\%$ of base.
7. **Interpretation**: Cluster 1 ("Emerging Affluent") represents the prime conversion target: young professionals with rising monthly inflows who currently maintain high cash balances without investment products.
8. **Recommendation & Trade-Offs**:
   * Target Cluster 1 with digital automated wealth portfolios, and Cluster 2 with dedicated relationship managers.
9. **Risks & Limitations**: K-Means assumes spherical clusters; financial wealth data exhibits extreme Pareto tails. Ensure log-transformation prior to distance calculation.
10. **Follow-Up Questions**:
    * *"How would you validate that these clusters are commercially meaningful?"* $\implies$ Evaluate distinct campaign response rates across clusters in a pilot outbound sales test.

---

### Case 06: Data Quality Anomaly in Transaction Reporting
*Topic: Data-Quality Problems & Ledger Reconciliation*

1. **Problem Statement**: An executive dashboard suddenly reports a **$40\%$ drop in total transaction revenue** on Monday morning, triggering panic among business heads. As the analytics analyst, how do you investigate and determine if this is real commercial drop or a data pipeline failure?
2. **Questions to Clarify**:
   * Did customer transaction counts drop, or only reported dollar amounts?
   * Was there an upstream schema migration, ETL job failure, or holiday weekend?
3. **Analytical Framework**:
   * Systematic Root-Cause Triage: **Data Pipeline Layer $\rightarrow$ Infrastructure Layer $\rightarrow$ External Commercial Reality**.
4. **Data Required**:
   * ETL pipeline execution logs, raw incoming transaction landing tables, batch job timestamps, merchant clearing house feeds.
5. **Analysis Plan**:
   * Query raw database landing tables to check if raw records were ingested.
   * Check join keys in the aggregation pipeline for missing values or unexpected nulls.
6. **Calculations (`[PRACTICE CASE ASSUMPTION]` applied)**:
   * Raw transaction ingest count was normal ($1.2\text{M}$ txns on Sunday).
   * Investigation of ETL join: An upstream database migration altered `merchant_id` from integer to varchar, causing the aggregation `INNER JOIN` against the `merchants` dimension table to fail, silently dropping $40\%$ of rows.
7. **Interpretation**: The revenue drop was entirely an artifact of an ETL join key type mismatch, not an actual commercial decline.
8. **Recommendation & Trade-Offs**:
   * **Immediate Action**: Fix the join type cast in the SQL pipeline, re-run Sunday's batch job, and immediately send an executive communication clarifying that actual customer revenue remained stable.
   * **Systemic Fix**: Implement automated automated data quality assertions (row count drop alerts, null key checks) that halt report publishing and alert the on-call engineer before flawed executive decks are refreshed.
9. **Risks & Limitations**: Publishing false operational panics damages management confidence in the analytics team.
10. **Follow-Up Questions**:
    * *"What automated data test would have prevented this?"* $\implies$ A pre-publish assertion: `ASSERT current_day_rows >= 0.90 * previous_week_avg_rows`.

---

### Case 07: Operational Contact Center SLA Degradation
*Topic: Operational Performance & Capacity Modeling*

1. **Problem Statement**: Citi Customer Service contact center SLA specifies that $80\%$ of calls must be answered within 30 seconds. In August, SLA achievement collapsed from $84\%$ to $68\%$. Average Wait Time rose from 22 seconds to 78 seconds. Diagnose the cause and propose staffing adjustments.
2. **Questions to Clarify**:
   * Did incoming call volume spike, or did Average Handle Time (AHT) per call increase?
   * Did agent staffing / attendance decrease?
3. **Analytical Framework**:
   * Erlang-C Queueing Model:
     $$\text{Total Workload} = \text{Call Volume} \times \text{Average Handle Time (AHT)}$$
4. **Data Required**:
   * Telephony logs: Arrival timestamps, queue duration, talk time, wrap-up time, agent login hours, call reason taxonomy.
5. **Analysis Plan**:
   * Decompose workload delta into Volume Effect vs AHT Effect vs Staffing Effect.
6. **Calculations (`[PRACTICE CASE ASSUMPTION]` applied)**:
   * Call volume increased $+5\%$ (within normal seasonal forecast).
   * Agent scheduled hours were stable ($-1\%$).
   * Average Handle Time (AHT) surged by **$+34\%$** (from $180\text{ seconds}$ to $241\text{ seconds}$).
   * Reason analysis: 42% of calls were related to a recent mobile banking app update that moved the "Download Statement" button, confusing users and extending call explanation times.
7. **Interpretation**: Staffing was not the primary bottleneck; a confusing UI update generated prolonged customer inquiry calls that overwhelmed agent capacity.
8. **Recommendation & Trade-Offs**:
   * **Immediate Operational Fix**: Update the IVR (automated voice menu) with an automated recording: *"Looking for your statement? Find it under Profile > Documents in the new app."*
   * **Product Fix**: Work with mobile app product team to restore prominent statement download link on the main home screen.
9. **Risks & Limitations**: Hiring temporary customer service agents incurs significant training costs ($\approx \$80,000$) to treat a symptom caused by poor UI design.
10. **Follow-Up Questions**:
    * *"How would you measure the impact of the IVR announcement?"* $\implies$ Track daily deflection rate of statement-related inquiries and corresponding AHT drop.

---

### Case 08: Model Evaluation Disagreement (Accuracy vs Precision)
*Topic: Competing Analytical Recommendations*

1. **Problem Statement**: A junior analyst builds an anti-money laundering (AML) alert model that achieves **$99.4\%$ accuracy**. A senior analyst builds an alternative model that achieves only **$96.2\%$ accuracy** but claims their model is vastly superior. Management asks you to arbitrate. Which model is better and why?
2. **Questions to Clarify**:
   * What is the baseline incidence rate of true AML violations? (Typically $0.2\%$, or 2 per 1,000 transactions).
   * What are the full confusion matrices of both models?
3. **Analytical Framework**:
   * Confusion matrix analysis under extreme class imbalance.
4. **Data Required**:
   * Test set of $100,000$ transactions containing $200$ actual money-laundering violations ($0.2\%$) and $99,800$ legitimate transactions ($99.8\%$).
5. **Analysis Plan**:
   * Deconstruct both models' predictions into TP, FP, TN, and FN.
6. **Calculations (`[PRACTICE CASE ASSUMPTION]` applied)**:
   * **Junior Model ($99.4\%$ accuracy)**:
     * Simply predicts "Legitimate" for all transactions.
     * $\text{TN} = 99,400, \text{FP} = 400$.
     * $\text{TP} = 0, \text{FN} = 200$.
     * Accuracy = $\frac{99,400}{100,000} = 99.4\%$.
     * **Recall = $0\%$** (Caught ZERO money launderers! Regulatory disaster).
   * **Senior Model ($96.2\%$ accuracy)**:
     * $\text{TN} = 96,020, \text{FP} = 3,780$.
     * $\text{TP} = 180, \text{FN} = 20$.
     * Accuracy = $\frac{96,020 + 180}{100,000} = 96.2\%$.
     * **Recall = $\frac{180}{200} = \mathbf{90.0\%}$** (Intercepts 90% of money laundering activity).
7. **Interpretation**: The junior model's high accuracy is an illusion created by predicting the majority class. The senior model is vastly superior because it intercepts $90\%$ of illegal transactions, safeguarding Citi against severe regulatory fines.
8. **Recommendation & Trade-Offs**:
   * Select the Senior Model. Accuracy is completely invalid for AML evaluation; models must be evaluated on **Recall (Sensitivity)** and **Precision-Recall AUC**.
9. **Risks & Limitations**: The 3,780 false positives must be reviewed by compliance analysts. Staffing costs must be budgeted.
10. **Follow-Up Questions**:
    * *"How would you explain this arbitration to a non-technical audit committee?"* $\implies$ "Model A is like an alarm system that never rings—it is correct 99% of the time only because burglars rarely visit, but it catches zero burglars. Model B catches 9 out of 10 burglars."

---

### Case 09: Resolving Stakeholder Disagreement on Metric Definitions
*Topic: Stakeholder Disagreement & Metric Governance*

1. **Problem Statement**: Marketing defines "Active Customer" as *anyone who logged into the app in the last 90 days* (showing strong $+15\%$ growth). Finance defines "Active Customer" as *anyone who generated at least $\$5$ in fee or interest revenue in the last 30 days* (showing a $-4\%$ decline). Both groups present contradictory slides to the CEO. How do you resolve this?
2. **Questions to Clarify**:
   * What strategic decision does the "Active Customer" metric drive?
   * Can a multi-tier metric taxonomy be established to satisfy both teams?
3. **Analytical Framework**:
   * Metric Disaggregation & Lifecycle Taxonomy.
4. **Data Required**:
   * Digital login logs, fee revenue records, transaction volumes per customer.
5. **Analysis Plan**:
   * Cross-tabulate digital engagement against financial monetization.
6. **Calculations (`[PRACTICE CASE ASSUMPTION]` applied)**:
   * Out of $1,000,000$ digital users:
     * $300,000$ log in regularly but never swipe cards or borrow (Monetization = $\$0$).
     * $700,000$ actively transact and generate revenue.
   * Marketing's metric grew because app login improvements increased visits from non-transacting users. Finance's metric fell because average spend per transactor declined slightly.
7. **Interpretation**: Neither group is mathematically incorrect; they are measuring different stages of the customer lifecycle. Marketing is measuring **Digital Reach**, while Finance is measuring **Commercial Monetization**.
8. **Recommendation & Trade-Offs**:
   * **Recommendation**: Establish an official enterprise **Data Governance Metric Dictionary**:
     * Rename Marketing's metric to **"Digitally Engaged Users (DEU)"**.
     * Rename Finance's metric to **"Revenue-Generating Users (RGU)"**.
     * Introduce the bridge metric: **"Monetization Conversion Rate"** ($\text{RGU} / \text{DEU}$).
9. **Risks & Limitations**: Political friction between departments defending their historical reporting numbers.
10. **Follow-Up Questions**:
    * *"Who should own the final definition of enterprise metrics?"* $\implies$ An independent Enterprise Data Governance Council, ensuring consistent single-source-of-truth across all reporting.

---

### Case 10: Protecting Privacy in Machine Learning Features (Fair Lending)
*Topic: Privacy, Compliance & Risk-Related Decisions*

1. **Problem Statement**: A data science team discovers that incorporating postal code (ZIP code) and mobile device operating system into an automated loan approval model increases AUC by $+0.04$. However, compliance flags that postal codes in this region are strongly correlated with minority demographic concentration. Can Citi deploy this model?
2. **Questions to Clarify**:
   * What fair lending regulations apply? (e.g., US Equal Credit Opportunity Act - ECOA, Fair Housing Act, RBI guidelines).
   * Does using postal code create **Disparate Impact** (unintentional discrimination against protected classes)?
3. **Analytical Framework**:
   * Disparate Impact Ratio Analysis (Four-Fifths Rule):
     $$\text{Adverse Impact Ratio} = \frac{\text{Approval Rate of Protected Group}}{\text{Approval Rate of Control Group}}$$
     If ratio $< 0.80$, disparate impact is legally presumed.
4. **Data Required**:
   * Historical approval rates across demographic proxy indicators.
5. **Analysis Plan**:
   * Measure adverse impact ratio with and without postal code features.
   * Perform feature ablation to evaluate incremental AUC gain versus legal exposure.
6. **Calculations (`[PRACTICE CASE ASSUMPTION]` applied)**:
   * Model with ZIP code: Approval rate for minority neighborhoods = $42\%$; approval rate for majority neighborhoods = $65\%$. Ratio = $\frac{42}{65} = 0.646$ ($< 0.80 \implies$ **Severe Disparate Impact**).
   * Model without ZIP code (using only credit history, income, DTI ratio): Ratio = $\frac{56}{62} = 0.903$ ($> 0.80 \implies$ **Compliant**). AUC drops marginally by $0.015$.
7. **Interpretation**: Postal code acts as a direct proxy for protected demographic characteristics, creating illegal disparate impact under fair lending laws.
8. **Recommendation & Trade-Offs**:
   * **Recommendation**: **Exclude postal code from the model immediately.**
   * **Trade-Off**: Sacrificing $0.015$ in AUC is mandatory to eliminate severe regulatory penalties, multi-million dollar legal fines, and catastrophic reputational damage to Citigroup.
9. **Risks & Limitations**: Proxy variables can hide in non-obvious features (e.g., specific merchant shopping habits). Continuous fair-lending bias testing is required.
10. **Follow-Up Questions**:
    * *"What if business leadership complains that rejecting the feature leaves money on the table?"* $\implies$ Cite the primary mandate in Citi's job description: *safeguarding Citigroup, its clients, and assets by driving compliance with applicable laws, rules, and regulations, and applying sound ethical judgment*.

---

## 2. Quantitative Puzzles & Analytical Brainteasers

### Puzzle 01: The 25 Horses Race
* **Problem**: 25 horses, 5 tracks, no stopwatch (only relative order within a race is observed). Find minimum races to identify top 3 fastest horses.
* **Solution**:
  1. Divide into 5 groups of 5 $\implies$ **5 races**.
  2. Race the 5 winners against each other $\implies$ **Race 6**.
     * Assume winner order is $A_1 > B_1 > C_1 > D_1 > E_1$.
     * $A_1$ is guaranteed fastest overall.
     * Eliminate groups D and E entirely. Eliminate $C_2, C_3$ (cannot beat $C_1$). Eliminate $B_3$.
  3. Eligible candidates for 2nd and 3rd: $A_2, A_3, B_1, B_2, C_1$ (exactly 5 horses).
  4. Race these 5 horses $\implies$ **Race 7**.
  5. **Total minimum races = 7**.

---

### Puzzle 02: Measuring 45 Minutes with Burning Ropes
* **Problem**: Two non-uniform ropes, each taking exactly 60 minutes to burn completely. Measure 45 minutes.
* **Solution**:
  1. Light **both ends of Rope 1** and **one end of Rope 2** simultaneously.
  2. Rope 1 burns twice as fast and extinguishes in exactly **30 minutes**.
  3. The moment Rope 1 finishes, Rope 2 has 30 minutes of burn time remaining.
  4. Immediately light the **other end of Rope 2**.
  5. The remaining portion of Rope 2 burns from both ends, finishing in **15 minutes**.
  6. Total time = $30 + 15 = \mathbf{45\text{ minutes}}$.

---

### Puzzle 03: Simulating a Fair Coin from a Biased Coin (von Neumann Extractor)
* **Problem**: Given a coin that lands Heads with unknown probability $p \neq 0.5$, generate an unbiased event with $P = 0.50$.
* **Solution**:
  1. Flip the coin twice.
  2. Outcomes:
     * $\text{Heads-Tails (HT)} \implies P = p(1 - p)$.
     * $\text{Tails-Heads (TH)} \implies P = (1 - p)p$.
     * $\text{HH} \implies p^2$, $\text{TT} \implies (1 - p)^2$.
  3. Since $P(HT) = P(TH) = p(1 - p)$ for any $p$, if outcome is $HT \implies \text{Declare Heads}$; if $TH \implies \text{Declare Tails}$. If $HH$ or $TT$, discard and flip twice again.

---

### Puzzle 04: Poisoned Wine Bottles (Binary Search)
* **Problem**: 1,000 wine bottles, 1 poisoned. A mouse dies within 24 hours if it drinks even one drop. Find the poisoned bottle in 24 hours using minimum mice.
* **Solution**:
  * Simultaneous binary test: $M$ mice can represent $2^M$ states (alive/dead).
  * $2^{10} = 1024 \ge 1000 \implies \mathbf{10\text{ mice}}$ minimum.
  * Number bottles 1 to 1000 in 10-bit binary. Mouse $i$ drinks from all bottles where the $i$-th bit is 1. The binary pattern of dead mice identifies the exact poisoned bottle.

---

### Puzzle 05: The Monty Hall Problem
* **Problem**: 3 doors, 1 car, 2 goats. You pick Door 1. Host reveals a goat behind Door 3. Switch to Door 2 or stay?
* **Solution**:
  * Prior probability of car behind Door 1 = $1/3$.
  * Probability behind Door 2 or 3 = $2/3$.
  * Host's action reveals information: goat behind Door 3 collapses the entire $2/3$ probability onto Door 2.
  * Switching wins with probability $\mathbf{2/3 \approx 66.7\%}$. Always switch.

---

## 3. Financial Market Sizing & Guesstimates

### Guesstimate: Total Credit Card Transaction Volume in India on Diwali Day (`[PRACTICE CASE ASSUMPTION]`)
* **Formula**: $\text{Total Value} = \text{Total Active Cards} \times \text{Diwali Day Active Rate} \times \text{Average Spend per Active Card}$.
1. **Active Cards**:
   * Population $\approx 1.4\text{B}$; Banked urban population $\approx 200\text{M}$.
   * Credit card penetration $\approx 20\% \implies 40\text{M}$ cardholders with $2.5$ cards average $\approx \mathbf{100\text{ Million active cards}}$.
2. **Diwali Day Active Usage Rate**:
   * Normal daily usage $\approx 10\%$. On Diwali (peak shopping, gifting, electronics), usage surges to $\approx \mathbf{30\%}$.
   * Active cards used on Diwali = $100\text{M} \times 0.30 = \mathbf{30\text{ Million cards}}$.
3. **Average Spend per Active Card**:
   * Tier 1 (High value: Jewelry, Electronics, Home) $\approx 20\%$ spending ₹25,000 $\implies ₹5,000$.
   * Tier 2 (Apparel, Gifting, E-commerce) $\approx 50\%$ spending ₹5,000 $\implies ₹2,500$.
   * Tier 3 (Dining, Groceries, Fuel) $\approx 30\%$ spending ₹1,500 $\implies ₹450$.
   * Blended average spend $\approx \mathbf{₹8,000\text{ per card}}$.
4. **Total Daily Transaction Volume**:
   $$\text{Total Spend} = 30\text{M cards} \times ₹8,000 = \mathbf{₹24,000\text{ Crores}} \quad (\approx \$2.9\text{ Billion USD})$$
