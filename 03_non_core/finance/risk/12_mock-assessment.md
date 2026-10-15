# 12. Full-Length Risk Analytics Placement Mock Assessment

> Comprehensive 90-minute quantitative assessment simulating placement selection tests for Risk Analyst, Credit Risk Specialist, and Quantitative Risk profiles (American Express, Citi, Barclays, Goldman Sachs Risk, Nomura).
> 
> *Notice: Time limits, test weighting, and scoring cutoffs in this document are internal practice heuristics designed for self-assessment and placement preparation, not official company or IIT Kanpur placement specifications ([PREPARATION HEURISTIC]). All scenario figures are illustrative ([PRACTICE ASSUMPTION]).*

---

## Assessment Instructions & Structure

- **Total Time Allowed**: 90 minutes
- **Total Marks**: 100 marks
- **Calculators**: Scientific calculators permitted.
- **Passing Benchmark**: $\ge 70\text{ marks}$ indicates interview-readiness for quantitative risk and banking analytics roles.

| Section | Topic Area | Questions | Marks | Recommended Time |
|:---|:---|:---:|:---:|:---:|
| **Section 1** | Probability, Statistics & Market Risk | Q1–Q5 | 25 Marks | 20 mins |
| **Section 2** | Credit Scoring, WoE/IV & Model Validation | Q6–Q9 | 25 Marks | 25 mins |
| **Section 3** | Risk Data Analytics & Relational SQL | Q10–Q12 | 25 Marks | 20 mins |
| **Section 4** | Risk Strategy & Stress-Testing Caselet | Q13 | 25 Marks | 25 mins |

---

# Part I: Examination Paper (Questions)

### Section 1: Probability, Statistics & Market Risk (25 Marks)

#### Q1 (5 Marks)
A retail lending portfolio has an unconditional 1-year default rate of 4.0%. An automated transaction fraud detection model has a sensitivity of 85.0% (probability of raising an alert given the account defaults). For non-defaulting accounts, the model has a false alarm rate of 5.0%.
- If a fraud alert is raised on an account, calculate the posterior probability that the account actually defaults using Bayes' Theorem.

#### Q2 (5 Marks)
A corporate loan portfolio experiences defaults according to a Poisson process with an average rate of $\lambda = 2.5\text{ defaults per quarter}$.
- (a) What is the probability of observing exactly 1 default in a given quarter? (2 Marks)
- (b) What is the probability of observing 4 or more defaults in a given quarter? (3 Marks)

#### Q3 (5 Marks)
A multi-asset investment portfolio worth ₹500 Cr has an annualized return volatility of 20.0%. Assuming 256 trading days in a year:
- (a) Calculate the daily return volatility $\sigma_{\text{daily}}$. (2 Marks)
- (b) Compute the 1-day 99% Parametric Value at Risk (VaR), where $Z_{99\%} = 2.326$. (1.5 Marks)
- (c) Using the Basel square-root-of-time scaling rule, calculate the regulatory 10-day 99% VaR. (1.5 Marks)

#### Q4 (5 Marks)
A risk manager holds two asset classes: Asset 1 ($V_1 = ₹60\text{ Cr}$, $\text{VaR}_1 = ₹6.0\text{ Cr}$) and Asset 2 ($V_2 = ₹40\text{ Cr}$, $\text{VaR}_2 = ₹5.0\text{ Cr}$).
- (a) If the correlation between the two assets is $\rho = +0.20$, compute the diversified portfolio VaR. (3 Marks)
- (b) During a liquidity crisis, correlation spikes to $\rho = +0.85$. Calculate the new stressed portfolio VaR and explain the risk implication. (2 Marks)

#### Q5 (5 Marks)
In statistical credit underwriting, define Type I Error ($\alpha$) and Type II Error ($\beta$). If an underwriter lowers the credit score approval threshold to accept more applicants, which error increases, and what is the direct economic consequence for a retail bank?

---

### Section 2: Credit Scoring, WoE/IV & Model Validation (25 Marks)

#### Q6 (8 Marks)
An analyst evaluates applicant Debt-to-Income (DTI) ratio for an application scorecard. The training dataset consists of 1,000 borrowers (800 Good / non-defaulters, 200 Bad / defaulters):

| DTI Bin | Total Borrowers | Non-Defaulters (Goods, $G_i$) | Defaulters (Bads, $B_i$) |
|:---:|:---:|:---:|:---:|
| Low ($\le 25\%$) | 400 | 360 | 40 |
| Medium ($25\% - 45\%$) | 400 | 340 | 60 |
| High ($> 45\%$) | 200 | 100 | 100 |

- (a) Calculate the Weight of Evidence ($WoE_i$) for each bin. (4 Marks)
- (b) Calculate the Information Value ($IV$) of the DTI feature and state whether it should be included in the scorecard based on standard heuristics. (4 Marks)

#### Q7 (6 Marks)
A commercial bank extends a ₹100 Cr committed credit line to a manufacturing firm. Currently, ₹60 Cr is drawn, and ₹40 Cr is undrawn.
- Under Basel guidelines, the Credit Conversion Factor (CCF) for undrawn commitments is 50.0%.
- The 1-year Probability of Default ($PD$) is 2.5%.
- In the event of default, the bank expects a physical asset recovery rate of 40.0%.
Calculate Exposure at Default (EAD), Loss Given Default (LGD), and the 1-year Expected Loss ($EL$).

#### Q8 (6 Marks)
The Model Risk Governance team audits an existing credit scorecard after 18 months. Development vs current score distributions are:
- Band 1 (High Risk): $E_1 = 20.0\%$, $A_1 = 30.0\%$
- Band 2 (Medium Risk): $E_2 = 50.0\%$, $A_2 = 50.0\%$
- Band 3 (Low Risk): $E_3 = 30.0\%$, $A_3 = 20.0\%$
Calculate the Population Stability Index (PSI). Based on regulatory thresholds ($PSI < 0.10$, $0.10 \le PSI < 0.25$, $PSI \ge 0.25$), state the required model governance action.

#### Q9 (5 Marks)
Define the Kolmogorov-Smirnov (KS) statistic and explain how it differs conceptually from ROC-AUC in evaluating credit scorecards. Why do retail credit underwriters focus specifically on the decile location of maximum KS?

---

### Section 3: Risk Data Analytics & Relational SQL (25 Marks)

#### Q10 (8 Marks)
Given table `loan_repayments(loan_id, billing_cycle_date, due_date, payment_date, installment_amount, amount_paid)`:
- Write a SQL query using window functions to identify all `loan_id`s that have been delinquent ($\text{payment\_date} > \text{due\_date}$ or $\text{payment\_date IS NULL}$) for **at least 3 consecutive billing cycles**.

#### Q11 (8 Marks)
Given table `portfolio_accounts(account_id, origination_month, loan_amount, current_status, default_date)`:
- Write a SQL query to generate a vintage cohort analysis showing:
  - `origination_month`
  - Total loans originated
  - Total disbursed principal
  - Cumulative default rate at 6 months from origination ($\text{default\_date} \le \text{origination\_month} + 6\text{ months}$).

#### Q12 (9 Marks)
Given table `corporate_exposures(exposure_id, borrower_group_id, sector_name, drawn_amount, credit_rating)`:
- A bank's risk policy stipulates that no single borrower group may exceed 15.0% of the total wholesale portfolio, and no single sector may exceed 25.0%.
- Write a SQL query that calculates the total exposure per borrower group and per sector, flagging any entity currently in violation of policy caps.

---

### Section 4: Risk Strategy & Stress-Testing Caselet (25 Marks)

#### Q13 (25 Marks)
"VedicFin" is a digital consumer lender with an active loan portfolio of ₹1,000 Cr across 200,000 borrowers. The average loan ticket is ₹50,000, and the loan tenor is 12 months with flat monthly repayments.
- Current underwriting cutoff: Credit Score $\ge 700$.
  - Approval rate: 60%.
  - Annual default rate: 2.0%.
  - Net interest yield earned: 16.0% per annum.
  - Recovery rate on defaulted loans: 30.0% ($\implies LGD = 70.0\%$).
- **The Growth Proposal**:
  To expand market share, product leadership proposes lowering the cutoff from 700 to 660.
  - Estimated new borrower volume in score band 660–699: ₹300 Cr in new originations.
  - Expected default rate in band 660–699: 8.0%.
  - Annual net interest yield in band 660–699: 18.0% (risk-based pricing).
  - Expected LGD on new cohort: 75.0%.

**Required Tasks**:
- (a) Compute current annual net revenue, credit losses, and net economic profit for the existing baseline portfolio. (5 Marks)
- (b) Compute the incremental revenue, incremental expected credit losses, and incremental net profit generated by the proposed 660–699 cohort. (8 Marks)
- (c) Calculate the combined portfolio default rate post-expansion. Does this breach a risk appetite limit of 3.5% portfolio default rate? (5 Marks)
- (d) Provide a structured Chief Risk Officer recommendation: Would you approve this policy change? If approved with conditions, recommend three concrete risk controls. (7 Marks)

---

# Part II: Complete Solutions & Marking Scheme

### Section 1 Solutions (25 Marks)

#### Solution 1 (5 Marks)
Using Bayes' Theorem:
- Prior probability of default: $P(D) = 0.04 \implies P(D^c) = 0.96$.
- True Positive Rate (Sensitivity): $P(\text{Alert} \mid D) = 0.85$.
- False Positive Rate: $P(\text{Alert} \mid D^c) = 0.05$.
- Total Probability of an Alert:
  $$P(\text{Alert}) = P(D) \cdot P(\text{Alert} \mid D) + P(D^c) \cdot P(\text{Alert} \mid D^c)$$
  $$P(\text{Alert}) = (0.04 \times 0.85) + (0.96 \times 0.05) = 0.0340 + 0.0480 = \mathbf{0.0820\text{ (8.20\%)}}$$
- Posterior Probability of Default given an Alert:
  $$P(D \mid \text{Alert}) = \frac{P(D) \cdot P(\text{Alert} \mid D)}{P(\text{Alert})} = \frac{0.0340}{0.0820} = \mathbf{41.46\%}$$
- *Interpretation*: Even with an alert, there is only a 41.46% chance of default due to the low base rate of default (Base Rate Fallacy).

#### Solution 2 (5 Marks)
Poisson distribution: $P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}$ with $\lambda = 2.5$.
- **(a) Exactly 1 default** (2 Marks):
  $$P(X = 1) = \frac{e^{-2.5} (2.5)^1}{1!} = 0.082085 \times 2.5 = \mathbf{0.2052\text{ (20.52\%)}}$$
- **(b) 4 or more defaults** (3 Marks):
  $$P(X \ge 4) = 1 - [P(X=0) + P(X=1) + P(X=2) + P(X=3)]$$
  - $P(X=0) = e^{-2.5} = 0.082085$
  - $P(X=1) = 0.205212$
  - $P(X=2) = \frac{0.082085 \times (2.5)^2}{2} = \frac{0.082085 \times 6.25}{2} = 0.256516$
  - $P(X=3) = \frac{0.082085 \times (2.5)^3}{6} = \frac{0.082085 \times 15.625}{6} = 0.213763$
  - $P(X \le 3) = 0.082085 + 0.205212 + 0.256516 + 0.213763 = 0.757576$
  $$P(X \ge 4) = 1 - 0.757576 = \mathbf{0.2424\text{ (24.24\%)}}$$

#### Solution 3 (5 Marks)
- **(a) Daily volatility** (2 Marks):
  $$\sigma_{\text{daily}} = \frac{\sigma_{\text{annual}}}{\sqrt{256}} = \frac{20.0\%}{16} = \mathbf{1.25\%\text{ per day (0.0125)}}$$
- **(b) 1-Day 99% Parametric VaR** (1.5 Marks):
  $$\text{VaR}_{1\text{d}} = Z_{99\%} \times \sigma_{\text{daily}} \times V = 2.326 \times 0.0125 \times ₹500\text{ Cr} = \mathbf{₹14.5375\text{ Cr}}$$
- **(c) 10-Day 99% Basel VaR** (1.5 Marks):
  $$\text{VaR}_{10\text{d}} = \text{VaR}_{1\text{d}} \times \sqrt{10} = 14.5375 \times 3.16228 = \mathbf{₹45.97\text{ Cr}}$$

#### Solution 4 (5 Marks)
- **(a) Diversified VaR at $\rho = +0.20$** (3 Marks):
  $$\text{VaR}_p = \sqrt{\text{VaR}_1^2 + \text{VaR}_2^2 + 2 \rho \text{VaR}_1 \text{VaR}_2}$$
  $$\text{VaR}_p = \sqrt{6.0^2 + 5.0^2 + 2(0.20)(6.0)(5.0)} = \sqrt{36 + 25 + 12} = \sqrt{73} = \mathbf{₹8.544\text{ Cr}}$$
  - Diversification benefit $= (6.0 + 5.0) - 8.544 = ₹2.456\text{ Cr}$.
- **(b) Stressed VaR at $\rho = +0.85$** (2 Marks):
  $$\text{VaR}_{p,\text{stressed}} = \sqrt{36 + 25 + 2(0.85)(6.0)(5.0)} = \sqrt{61 + 51} = \sqrt{112} = \mathbf{₹10.583\text{ Cr}}$$
  - *Risk Implication*: Stressed correlation increases portfolio VaR by 23.9% ($₹8.54\text{ Cr} \to ₹10.58\text{ Cr}$), nearly eliminating portfolio diversification benefits.

#### Solution 5 (5 Marks)
- **Definitions** (2.5 Marks):
  - **Type I Error ($\alpha$)**: Rejecting a good applicant (False Positive / False Alarm). In underwriting: rejecting a creditworthy borrower who would have repaid in full.
  - **Type II Error ($\beta$)**: Accepting a bad applicant (False Negative / Missed Defaulter). In underwriting: approving a borrower who subsequently defaults.
- **Economic Consequence of Lowering Threshold** (2.5 Marks):
  - Lowering the score cutoff accepts more applicants $\implies$ **Type II Error ($\beta$) increases** (more defaulters are approved).
  - Economic consequence: Direct increase in credit losses and loan write-offs. Since default losses ($LGD \approx 60\% - 80\%$) typically dwarf single-loan interest margins (~5%–15%), an uncontrolled rise in Type II error threatens bank capital solvency.

---

### Section 2 Solutions (25 Marks)

#### Solution 6 (8 Marks)
Total Goods $G_{\text{total}} = 800$, Total Bads $B_{\text{total}} = 200$.
- **(a) Weight of Evidence ($WoE_i$)** (4 Marks):
  $$WoE_i = \ln \left( \frac{G_i / G_{\text{total}}}{B_i / B_{\text{total}}} \right)$$
  - **Low DTI**:
    - $\% \text{Goods} = \frac{360}{800} = 0.450$, $\% \text{Bads} = \frac{40}{200} = 0.200$.
    - $WoE_{\text{Low}} = \ln \left( \frac{0.450}{0.200} \right) = \ln(2.25) = \mathbf{+0.8109}$.
  - **Medium DTI**:
    - $\% \text{Goods} = \frac{340}{800} = 0.425$, $\% \text{Bads} = \frac{60}{200} = 0.300$.
    - $WoE_{\text{Med}} = \ln \left( \frac{0.425}{0.300} \right) = \ln(1.4167) = \mathbf{+0.3483}$.
  - **High DTI**:
    - $\% \text{Goods} = \frac{100}{800} = 0.125$, $\% \text{Bads} = \frac{100}{200} = 0.500$.
    - $WoE_{\text{High}} = \ln \left( \frac{0.125}{0.500} \right) = \ln(0.25) = \mathbf{-1.3863}$.

- **(b) Information Value ($IV$)** (4 Marks):
  $$IV = \sum_{i=1}^3 (\% G_i - \% B_i) \times WoE_i$$
  - Low DTI: $(0.450 - 0.200) \times 0.8109 = 0.250 \times 0.8109 = \mathbf{0.2027}$
  - Med DTI: $(0.425 - 0.300) \times 0.3483 = 0.125 \times 0.3483 = \mathbf{0.0435}$
  - High DTI: $(0.125 - 0.500) \times (-1.3863) = -0.375 \times (-1.3863) = \mathbf{0.5199}$
  $$\mathbf{IV_{\text{total}}} = 0.2027 + 0.0435 + 0.5199 = \mathbf{0.7661}$$
  - *Heuristic Assessment*: $IV = 0.7661 > 0.50$. While highly predictive, an $IV > 0.50$ is "suspiciously high" ([PREPARATION HEURISTIC]); the risk analyst must verify that DTI does not suffer from data leakage (e.g., recorded after delinquency occurred) before including it in the production scorecard.

#### Solution 7 (6 Marks)
1. **Exposure at Default (EAD)** (2 Marks):
   $$EAD = \text{Drawn Amount} + (CCF \times \text{Undrawn Commitment})$$
   $$EAD = 60.0 + (0.50 \times 40.0) = 60.0 + 20.0 = \mathbf{₹80.0\text{ Cr}}$$
2. **Loss Given Default (LGD)** (2 Marks):
   $$LGD = 1 - \text{Recovery Rate} = 1 - 0.40 = \mathbf{0.60\text{ (60.0\%)}}$$
3. **1-Year Expected Loss (EL)** (2 Marks):
   $$EL = PD \times LGD \times EAD = 0.025 \times 0.60 \times ₹80.0\text{ Cr} = \mathbf{₹1.20\text{ Cr = 120 Lakh INR}}$$

#### Solution 8 (6 Marks)
Population Stability Index: $PSI = \sum (A_i - E_i) \times \ln(A_i / E_i)$
- **Band 1 (High Risk)**:
  - Difference: $0.30 - 0.20 = +0.10$
  - $\ln(0.30 / 0.20) = \ln(1.5) = +0.4055$
  - Contribution: $0.10 \times 0.4055 = \mathbf{0.04055}$
- **Band 2 (Medium Risk)**:
  - Difference: $0.50 - 0.50 = 0.00$
  - Contribution: $\mathbf{0.0000}$
- **Band 3 (Low Risk)**:
  - Difference: $0.20 - 0.30 = -0.10$
  - $\ln(0.20 / 0.30) = \ln(0.6667) = -0.4055$
  - Contribution: $-0.10 \times (-0.4055) = \mathbf{0.04055}$
$$\mathbf{PSI_{\text{total}}} = 0.04055 + 0.0000 + 0.04055 = \mathbf{0.0811}$$
- **Governance Action** (2 Marks):
  $PSI = 0.0811 < 0.10$. Under SR 11-7 regulatory guidelines, this indicates a **stable population**. No model recalibration or rebuild is required at this time; standard monthly monitoring continues.

#### Solution 9 (5 Marks)
- **KS Statistic vs ROC-AUC** (3 Marks):
  - **KS Statistic**: Measures the maximum vertical separation between the cumulative distribution functions of Goods and Bads ($KS = \max |F_G(s) - F_B(s)|$). It evaluates separation at a single specific decision cutoff.
  - **ROC-AUC**: Evaluates overall model discrimination across all possible cutoffs simultaneously.
- **Why Underwriters Focus on KS Decile** (2 Marks):
  Underwriters must choose an actionable operating score cutoff. In retail scorecards, the maximum KS should occur in the **top 3 deciles** (deciles 1–3). This ensures that the bank can reject the vast majority of future defaulters by declining only a small fraction of applicants, maximizing business throughput while minimizing credit loss.

---

### Section 3 Solutions (25 Marks)

#### Solution 10 (8 Marks)
```sql
-- Identify accounts with >= 3 consecutive delinquent billing cycles
WITH DelinquencyFlagged AS (
    SELECT 
        loan_id,
        billing_cycle_date,
        due_date,
        payment_date,
        CASE 
            WHEN payment_date > due_date OR payment_date IS NULL THEN 1 
            ELSE 0 
        END AS is_delinquent
    FROM loan_repayments
),
ConsecutiveStreaks AS (
    SELECT 
        loan_id,
        billing_cycle_date,
        is_delinquent,
        SUM(is_delinquent) OVER (
            PARTITION BY loan_id 
            ORDER BY billing_cycle_date 
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ) AS rolling_3m_delinquencies
    FROM DelinquencyFlagged
)
SELECT DISTINCT loan_id
FROM ConsecutiveStreaks
WHERE rolling_3m_delinquencies = 3;
```

#### Solution 11 (8 Marks)
```sql
-- Vintage Cohort Analysis: 6-Month Cumulative Default Rate
SELECT 
    origination_month,
    COUNT(account_id) AS total_loans_originated,
    SUM(loan_amount) AS total_principal_disbursed,
    COUNT(CASE 
        WHEN default_date IS NOT NULL 
         AND DATEDIFF(month, origination_month, default_date) <= 6 
        THEN account_id 
    END) AS defaulted_within_6m_count,
    ROUND(
        100.0 * COUNT(CASE 
            WHEN default_date IS NOT NULL 
             AND DATEDIFF(month, origination_month, default_date) <= 6 
            THEN account_id 
        END) / COUNT(account_id), 
        2
    ) AS cumulative_6m_default_rate_pct
FROM portfolio_accounts
GROUP BY origination_month
ORDER BY origination_month;
```

#### Solution 12 (9 Marks)
```sql
-- Portfolio Concentration Audit against Group and Sector Caps
WITH TotalPortfolio AS (
    SELECT SUM(drawn_amount) AS total_portfolio_drawn
    FROM corporate_exposures
),
GroupExposures AS (
    SELECT 
        ce.borrower_group_id,
        SUM(ce.drawn_amount) AS group_drawn,
        ROUND(100.0 * SUM(ce.drawn_amount) / tp.total_portfolio_drawn, 2) AS group_pct,
        CASE 
            WHEN (100.0 * SUM(ce.drawn_amount) / tp.total_portfolio_drawn) > 15.0 
            THEN 'BREACH (>15%)' 
            ELSE 'COMPLIANT' 
        END AS group_compliance_status
    FROM corporate_exposures ce
    CROSS JOIN TotalPortfolio tp
    GROUP BY ce.borrower_group_id, tp.total_portfolio_drawn
),
SectorExposures AS (
    SELECT 
        ce.sector_name,
        SUM(ce.drawn_amount) AS sector_drawn,
        ROUND(100.0 * SUM(ce.drawn_amount) / tp.total_portfolio_drawn, 2) AS sector_pct,
        CASE 
            WHEN (100.0 * SUM(ce.drawn_amount) / tp.total_portfolio_drawn) > 25.0 
            THEN 'BREACH (>25%)' 
            ELSE 'COMPLIANT' 
        END AS sector_compliance_status
    FROM corporate_exposures ce
    CROSS JOIN TotalPortfolio tp
    GROUP BY ce.sector_name, tp.total_portfolio_drawn
)
SELECT 'BORROWER_GROUP' AS entity_type, borrower_group_id AS entity_id, group_drawn AS exposure_amount, group_pct AS exposure_pct, group_compliance_status AS status
FROM GroupExposures WHERE group_compliance_status LIKE 'BREACH%'
UNION ALL
SELECT 'SECTOR' AS entity_type, sector_name AS entity_id, sector_drawn AS exposure_amount, sector_pct AS exposure_pct, sector_compliance_status AS status
FROM SectorExposures WHERE sector_compliance_status LIKE 'BREACH%';
```

---

### Section 4 Solutions: Risk Strategy & Stress-Testing Caselet (25 Marks)

#### Solution 13 (25 Marks)

**(a) Current Baseline Economics (Score $\ge 700$)** (5 Marks):
- Portfolio Size = ₹1,000 Cr.
- Gross Interest Revenue = $₹1,000\text{ Cr} \times 16.0\% = \mathbf{₹160.0\text{ Cr}}$.
- Expected Credit Losses ($EL = PD \times LGD \times EAD$):
  $$EL_{\text{base}} = 2.0\% \times 70.0\% \times ₹1,000\text{ Cr} = 0.02 \times 0.70 \times 1000 = \mathbf{₹14.0\text{ Cr}}$$
- **Baseline Net Economic Profit**:
  $$\text{Net Profit}_{\text{base}} = 160.0 - 14.0 = \mathbf{₹146.0\text{ Cr}}$$

**(b) Incremental Economics of 660–699 Expansion** (8 Marks):
- Incremental Disbursals = ₹300 Cr.
- Incremental Interest Revenue = $₹300\text{ Cr} \times 18.0\% = \mathbf{+₹54.0\text{ Cr}}$.
- Incremental Expected Credit Losses:
  $$EL_{\text{incr}} = 8.0\% \times 75.0\% \times ₹300\text{ Cr} = 0.08 \times 0.75 \times 300 = \mathbf{₹18.0\text{ Cr}}$$
- **Incremental Net Economic Profit Contribution**:
  $$\Delta \text{Net Profit} = 54.0 - 18.0 = \mathbf{+₹36.0\text{ Cr}}$$
- *Conclusion*: On a standalone basis, risk-based pricing (18% interest) comfortably covers credit losses (6.0% expected loss), generating ₹36 Cr in incremental economic profit.

**(c) Combined Portfolio Default Rate Audit** (5 Marks):
- Combined Exposure = $1,000 + 300 = ₹1,300\text{ Cr}$.
- Combined Default Volume (Disbursed default exposure):
  $$\text{Baseline Default Volume} = 1000 \times 2.0\% = ₹20.0\text{ Cr}$$
  $$\text{Incremental Default Volume} = 300 \times 8.0\% = ₹24.0\text{ Cr}$$
  $$\text{Total Default Volume} = 20.0 + 24.0 = ₹44.0\text{ Cr}$$
- **Blended Portfolio Default Rate**:
  $$\text{Blended Default Rate} = \frac{₹44.0\text{ Cr}}{₹1,300\text{ Cr}} = \mathbf{3.385\%}$$
- *Risk Appetite Compliance*:
  Blended Default Rate ($3.385\%$) **satisfies the Board Risk Appetite limit of $< 3.50\%$**.

**(d) Chief Risk Officer Recommendation & Controls** (7 Marks):
- **Recommendation**: **Approve with Conditions (Phased Rollout)**.
  - *Rationale*: Although the expansion is economically profitable (+₹36 Cr) and complies with the 3.5% portfolio default limit, a 3.385% default rate leaves almost zero headroom (only 11.5 bps) before breaching the Board risk appetite.
- **Three Mandatory Risk Controls**:
  1. *Staged Rollout & Volume Quota*: Cap originations in the 660–699 band at ₹75 Cr per month for the first 90 days. Monitor 30-day First Payment Default (FPD) before opening the full ₹300 Cr limit.
  2. *Ticket Size Truncation*: Restrict maximum loan ticket in the 660–699 band to ₹25,000 (50% of the normal ₹50,000 ticket) for first-time borrowers; allow step-up only after 6 months of flawless repayments.
  3. *Mandatory eNACH / UPI Auto-Debit*: Require automated bank mandate activation prior to loan disbursal for all applicants below 700 score to mitigate operational collection leakage.

---

## Performance Rubric & Gap Diagnosis

### Score Categorization
- **85–100 Marks (Strong / Offer Ready)**: Ready for bulge-bracket banks and top risk teams. Exceptional statistical accuracy and commercial maturity.
- **70–84 Marks (Interview-Ready)**: Strong command of credit scorecards, VaR, and SQL. Minor calculation slips under time pressure.
- **50–69 Marks (Developing)**: Theoretical understanding present, but struggles with SQL window functions or multi-step case trade-offs.
- **<50 Marks (Remedial Action Required)**: Foundational gaps in probability and credit risk metrics. Immediate structured review needed.

### Remedial Revision Matrix

| If you lost points in... | Review These Specific Chapters | Practice Drills |
|:---|:---|:---|
| **Section 1 (Probability & VaR)** | [03_domain-knowledge.md](03_domain-knowledge.md#2-market-risk-value-at-risk-var--expected-shortfall) | Re-derive Bayes' Theorem, Poisson, and 10-day VaR scaling. |
| **Section 2 (Credit Risk & WoE)** | [03_domain-knowledge.md](03_domain-knowledge.md#1-credit-risk-foundations--mathematical-formulations) | Compute WoE, IV, and PSI manually with a calculator. |
| **Section 3 (SQL Risk Analytics)** | [04_tools-and-technical.md](04_tools-and-technical.md) | Practice SQL window functions (`ROWS BETWEEN PRECEDING`). |
| **Section 4 (Risk Case Problem)** | [07_practice-and-cases.md](07_practice-and-cases.md#case-1-retail-credit-card-portfolio-deterioration--cutoff-optimization) | Practice cutoff optimization and RAROC trade-off cases. |

---

## Cross-Module Links
- 📖 [Risk Domain Knowledge](03_domain-knowledge.md)
- 📖 [Risk Practice Cases](07_practice-and-cases.md)
- 📖 [Risk High-Yield Question Bank](06_question-bank.md)
- 📖 [Risk Tools & Technical Stack](04_tools-and-technical.md)
- 📖 [General Finance Mock Assessment](../../finance/finance/12_mock-assessment.md)
