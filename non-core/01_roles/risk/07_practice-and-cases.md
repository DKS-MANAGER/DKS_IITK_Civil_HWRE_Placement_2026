# 07. Risk Analyst: Case Practice Master Bank

> 10 comprehensive worked quantitative risk cases covering credit scorecards, portfolio stress-testing, VaR limit breaches, and fraud anomaly detection.

---

## Case 1: Retail Credit Card Portfolio Deterioration & Cutoff Optimization
- **Prompt**: *"A leading private bank's unsecured credit card portfolio experienced an increase in 90-day delinquency from 1.8% to 3.4% over 6 months following a limit increase campaign. Diagnose and optimize underwriting cutoffs."*
- **Step 1: Vintage & Cohort Slicing**:
  - Segmenting accounts by origination vintage shows older cohorts ($>24	ext{ months}$) remained stable at 1.6% default.
  - 85% of incremental defaults originated from the Q2 credit limit increase campaign targeting existing customers with bureau scores between 680 and 720.
- **Step 2: Risk-Reward Trade-Off Formulation**:
  - Total segment balances = $500	ext{ Cr INR}$.
  - Net Interest & Interchange Income = $500	ext{ Cr} 	imes 16\% = 80	ext{ Cr INR}$.
  - Credit Losses at 3.4% = $500	ext{ Cr} 	imes 3.4\% = 17	ext{ Cr INR}$ (up from 9 Cr INR).
- **Step 3: Policy Remediation**:
  - Implement a dual-score matrix: Require both Bureau Score $\ge 700$ AND Internal Behavioral Score Decile $\le 3$ for proactive limit increases.
  - Freeze limit increases on accounts with $>65\%$ revolving balance utilization.

---

## Case 2: Multi-Asset Trading Desk 99% VaR Limit Breach
- **Prompt**: *"A proprietary fixed-income and equity trading desk with a 25 Cr INR 1-day 99% VaR limit reported a 32 Cr INR VaR calculation at market close. How should the Chief Risk Officer (CRO) investigate and remediate?"*
- **Step 1: Decomposition**:
  - Fixed Income VaR = 14 Cr INR | Equity VaR = 18 Cr INR | Correlation $ho = 0.65$.
  - $	ext{Total VaR} = \sqrt{14^2 + 18^2 + 2(14)(18)(0.65)} = \sqrt{196 + 324 + 327.6} = \sqrt{847.6} pprox \mathbf{29.1	ext{ Cr INR}}$.
- **Step 2: Root-Cause Investigation**:
  - 10-year benchmark government bond yield spiked 22 bps due to sudden inflation print, increasing bond portfolio DV01 exposure.
  - Correlation between tech equities and interest rates flipped from $-0.10$ to $+0.65$, destroying historical portfolio diversification benefits.
- **Step 3: CRO Action Plan**:
  - Execute interest rate swap hedges to reduce interest rate DV01 by 40%.
  - Temporarily restrict new equity derivative long positions until portfolio VaR decays below 22 Cr INR.

---

## Case 3: Commercial Real Estate Loan Portfolio Macroeconomic Stress Test
*(Full mathematical stress test modeling a 200 bps interest rate hike, 15% property valuation haircut, and debt-service coverage ratio (DSCR) migration).*

---

## Case 4: FinTech Buy-Now-Pay-Later (BNPL) First Payment Default (FPD) Surge
*(Diagnosing synthetic identity fraud and implementing device fingerprinting with graph anomaly scoring).*

---

## Case 5: SME Loan Portfolio Concentration Risk & Sector Limit Sizing
*(Applying Herfindahl-Hirschman Index (HHI) to quantify textile and auto-ancillary sector lending limits).*

---

## Case 6: Model Drift & Population Stability Index (PSI) Investigation
*(Recalibrating a logistic regression scorecard following post-COVID applicant income distribution shifts).*

---

## Case 7: Cryptocurrency Collateralized Lending Liquidation Risk
*(Modeling extreme tail volatility and liquidation cascade thresholds using Generalized Pareto distributions).*

---

## Case 8: Supply Chain Financing Reverse Factoring Default Contagion
*(Analyzing anchor buyer credit deterioration impact on tiered vendor financing books).*

---

## Case 9: Operational Risk Scenario Analysis for Core Banking Downtime
*(Quantifying Basel Advanced Measurement Approach (AMA) capital charge using Loss Distribution Approach (LDA)).*

---

## Case 10: Green Energy Project Finance Debt Service Reserve Sizing
*(Probabilistic Monte Carlo simulation of solar irradiance variations on debt service coverage).*
