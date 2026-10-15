# 07. Risk Analyst: Worked Practice Cases & Numerical Scenarios

> 10 comprehensive, end-to-end quantitative risk management cases covering credit portfolio deterioration, market risk limit breaches, macro stress testing, model drift (PSI), and operational risk capital.
> 
> *Notice: All company names, portfolios, and figures in this module are hypothetical scenarios constructed for placement preparation ([PRACTICE ASSUMPTION]). Regulatory standards cited adhere to Basel Committee (BCBS) and RBI guidelines ([REGULATORY SOURCE]).*

---

## Table of Cases
1. [Case 1: Retail Credit Card Portfolio Deterioration & Cutoff Optimization](#case-1-retail-credit-card-portfolio-deterioration--cutoff-optimization)
2. [Case 2: Multi-Asset Trading Desk 99% VaR Limit Breach & Hedging](#case-2-multi-asset-trading-desk-99-var-limit-breach--hedging)
3. [Case 3: Commercial Real Estate Portfolio Macroeconomic Stress Testing](#case-3-commercial-real-estate-portfolio-macroeconomic-stress-testing)
4. [Case 4: FinTech Buy-Now-Pay-Later (BNPL) First Payment Default Surge](#case-4-fintech-buy-now-pay-later-bnpl-first-payment-default-surge)
5. [Case 5: Corporate Loan Portfolio Concentration Risk & Sector Limit Sizing](#case-5-corporate-loan-portfolio-concentration-risk--sector-limit-sizing)
6. [Case 6: Scorecard Model Drift & Population Stability Index (PSI) Remediation](#case-6-scorecard-model-drift--population-stability-index-psi-remediation)
7. [Case 7: Volatile Collateralized Lending & Liquidation Cascade Thresholds](#case-7-volatile-collateralized-lending--liquidation-cascade-thresholds)
8. [Case 8: Supply Chain Finance Reverse Factoring Contagion Analysis](#case-8-supply-chain-finance-reverse-factoring-contagion-analysis)
9. [Case 9: Operational Risk Capital Modeling via Loss Distribution Approach (LDA)](#case-9-operational-risk-capital-modeling-via-loss-distribution-approach-lda)
10. [Case 10: Project Finance Debt Service Reserve Account (DSRA) Stress Sizing](#case-10-project-finance-debt-service-reserve-account-dsra-stress-sizing)

---

## Case 1: Retail Credit Card Portfolio Deterioration & Cutoff Optimization

### 1. Scenario Context
A private retail bank's unsecured credit card portfolio experienced an increase in 90-day delinquency from 1.8% to 3.4% over 6 months following a proactive credit limit increase campaign. As Senior Risk Analyst, you must diagnose the root cause and optimize the score cutoff.

### 2. Quantitative Diagnostic Data ([PRACTICE ASSUMPTION])
- Total active portfolio balance: ₹2,000 Cr.
- Limit increase target group: ₹500 Cr balance across 250,000 cardholders with external credit bureau scores between 680 and 720.
- Portfolio economics:
  - Annual Net Interest Margin + Interchange Revenue: 18.0%.
  - Historical credit loss rate: 1.8% $\implies \text{Annual Net Margin} = 18.0\% - 1.8\% = 16.2\%$.
  - Post-campaign loss rate in target segment: 3.4% $\implies \text{Credit Losses} = ₹500\text{ Cr} \times 3.4\% = ₹17.0\text{ Cr}$ (up from ₹9.0 Cr).
- **Vintage Analysis**:
  - Accounts opened $>24$ months ago maintained flat delinquency (1.6%).
  - 82% of incremental bads occurred in accounts that accepted the credit limit increase and had revolving credit utilization $>70\%$ at the time of the offer.

### 3. Step-by-Step Risk Remediation
1. **Root-Cause Finding**:
   Adverse selection—borrowers with liquidity distress immediately drew down the higher limit to fund consumption, while prime non-revolvers left the higher limit untouched.
2. **Cutoff Optimization via Dual-Score Matrix**:
   - Establish a 2D cutoff requiring both **Bureau Score** $\ge 710$ AND **Internal Behavioral Score** Decile $\le 3$.
   - Enforce a hard utilization cap: accounts with revolving utilization $>60\%$ are excluded from automatic limit enhancements.
3. **Financial Outcome**:
   - Reduces eligible segment balance from ₹500 Cr to ₹320 Cr.
   - Expected credit losses in the segment fall from 3.4% back to 1.9% ($₹320\text{ Cr} \times 1.9\% = ₹6.08\text{ Cr}$).
   - Net profit in the segment: $(₹320 \times 18\%) - ₹6.08 = 57.6 - 6.08 = \mathbf{₹51.52\text{ Cr}}$, improving risk-adjusted return on capital (RAROC).

---

## Case 2: Multi-Asset Trading Desk 99% VaR Limit Breach & Hedging

### 1. Scenario Context
A proprietary trading desk holding an Indian equity portfolio and government bond positions has a Board-approved 1-day 99% Value at Risk (VaR) limit of **₹25.0 Cr**. At market close, the automated risk engine reports a calculated VaR of **₹32.4 Cr**, triggering a critical limit breach.

### 2. Position Breakdown & Volatility Inputs ([PRACTICE ASSUMPTION])
- **Equity Portfolio**: Market Value $V_1 = ₹200.0\text{ Cr}$, Daily Volatility $\sigma_1 = 1.8\%$.
  $$\text{Undiversified Equity VaR}_{99\%} = 2.326 \times 0.018 \times 200.0 = \mathbf{₹8.37\text{ Cr}}$$
- **Fixed Income (10-Yr G-Sec) Portfolio**: Market Value $V_2 = ₹800.0\text{ Cr}$, Modified Duration $D_{\text{mod}} = 6.5\text{ years}$, Daily Yield Volatility $\sigma_y = 12\text{ bps} = 0.0012$.
  $$\text{Daily Price Volatility } \sigma_2 = D_{\text{mod}} \times \sigma_y = 6.5 \times 0.0012 = 0.78\% = 0.0078$$
  $$\text{Undiversified Bond VaR}_{99\%} = 2.326 \times 0.0078 \times 800.0 = \mathbf{₹14.51\text{ Cr}}$$
- **Historical vs Stressed Correlation**:
  - Baseline correlation: $\rho = -0.20$ (equity gains offset bond selloffs).
  - Current market shock: Inflation spike causes bonds and equities to fall simultaneously; correlation jumped to **$\rho = +0.65$**.

### 3. Mathematical Calculations
1. **Baseline Diversified VaR (Normal Market, $\rho = -0.20$)**:
   $$\text{VaR}_{\text{base}} = \sqrt{8.37^2 + 14.51^2 + 2(8.37)(14.51)(-0.20)} = \sqrt{70.06 + 210.54 - 48.58} = \sqrt{232.02} = \mathbf{₹15.23\text{ Cr}} \quad (< ₹25\text{ Cr Limit})$$
2. **Current Stressed VaR ($\rho = +0.65$)**:
   $$\text{VaR}_{\text{stressed}} = \sqrt{8.37^2 + 14.51^2 + 2(8.37)(14.51)(0.65)} = \sqrt{70.06 + 210.54 + 157.88} = \sqrt{438.48} = \mathbf{₹20.94\text{ Cr}}$$
   *(If equity position was expanded to ₹300 Cr and volatility spiked to 2.5%, VaR exceeds ₹32.4 Cr).*
3. **CRO Remediation & Hedging**:
   - Short Interest Rate Futures (IRF) or execute an Interest Rate Swap (IRS) to reduce bond duration from 6.5 years to 4.0 years.
   - Buy Nifty put options to hedge equity tail delta.
   - Enforce an immediate freeze on new long positions until diversified VaR decays below ₹22.0 Cr.

---

## Case 3: Commercial Real Estate Portfolio Macroeconomic Stress Testing

### 1. Scenario Context
Under RBI macro-prudential stress testing guidelines, a commercial bank evaluates its ₹5,000 Cr Commercial Real Estate (CRE) loan portfolio against an adverse macroeconomic shock.

### 2. Adverse Macroeconomic Scenario Parameters ([PRACTICE ASSUMPTION])
- **Interest Rate Shock**: Benchmark policy repo rate increases by +200 bps (floating borrowing costs rise from 8.5% to 10.5%).
- **Asset Price Shock**: Commercial property capital values drop by 15.0% due to cap-rate expansion.
- **Vacancy Shock**: Rental occupancy drops by 10.0%, reducing Net Operating Income (NOI) by 12.0%.

### 3. Credit Migration & Loss Calculations
1. **Debt Service Coverage Ratio (DSCR) Migration**:
   - Base Case: $\text{NOI} = ₹650\text{ Cr}$, Annual Debt Service = ₹450 Cr $\implies \text{DSCR} = \frac{650}{450} = \mathbf{1.44\times}$.
   - Stressed Case:
     $$\text{Stressed NOI} = 650 \times (1 - 0.12) = ₹572.0\text{ Cr}$$
     $$\text{Stressed Debt Service} = ₹450 \times \left( \frac{10.5\%}{8.5\%} \right) \approx ₹555.88\text{ Cr}$$
     $$\text{Stressed DSCR} = \frac{572.0}{555.88} = \mathbf{1.029\times}$$
2. **Default Probability (PD) Shock**:
   - As DSCR collapses from $1.44\times$ to $1.03\times$, probability of default migrates from a baseline $\text{PD} = 2.0\%$ to a stressed **$\text{PD} = 8.5\%$**.
3. **Loss Given Default (LGD) Shock**:
   - Baseline property collateral value = ₹7,000 Cr against ₹5,000 Cr loans (Loan-to-Value $\text{LTV} = 71.4\%$). Baseline $\text{LGD} = 25\%$.
   - Under 15% property haircut: Stressed Collateral = $7000 \times 0.85 = ₹5,950\text{ Cr}$.
   - After 15% liquidation and legal costs, recoverable amount = $5950 \times 0.85 = ₹5,057.5\text{ Cr}$.
   - Stressed $\text{LGD}$ increases to **40.0%**.
4. **Expected Loss Impact**:
   $$\text{Base Expected Loss} = 2.0\% \times 25\% \times ₹5,000\text{ Cr} = \mathbf{₹25.0\text{ Cr}}$$
   $$\text{Stressed Expected Loss} = 8.5\% \times 40\% \times ₹5,000\text{ Cr} = \mathbf{₹170.0\text{ Cr}}$$
   - **Capital Impact**: The bank must allocate an incremental **₹145.0 Cr** in credit provisions, reducing CET1 capital ratio by 29 bps.

---

## Case 4: FinTech Buy-Now-Pay-Later (BNPL) First Payment Default Surge

### 1. Business Problem
A digital consumer lending FinTech offering 3-month interest-free BNPL checkout financing observes that First Payment Default ($FPD$) on the first 30-day installment jumped from 2.2% to 6.8% in its newly acquired merchant acquisition channel.

### 2. Diagnostic Investigation & Data Analysis
- **Channel Vintage Breakdown**:
  - Merchant Category A (Electronics): $FPD = 1.9\%$.
  - Merchant Category B (Digital Vouchers & Gift Cards): $FPD = \mathbf{14.2\%}$.
- **Anomaly Detection**:
  - Device fingerprint analysis reveals high velocity: multiple loan applications originated from the same IMEI/IP addresses using disposable email domains and synthetic identities.
  - Absence of SMS banking transaction history on applicant devices correlated with 80% of bads.

### 3. Model & Underwriting Adjustments
1. **Rule Engine Intervention**: Instant block on high-velocity IP/device clusters; impose mandatory UPI Auto-Pay mandate registration before loan approval on digital voucher merchants.
2. **Cost-Sensitive Threshold Optimization**:
   - Average Loan Ticket = ₹3,000. Merchant commission fee = 3.0% (₹90).
   - If applicant is good: Profit = ₹90.
   - If applicant defaults on FPD: Net Loss $\approx ₹3,000 \times (1 - \text{Recovery}) = 3000 \times 0.90 = ₹2,700$.
   - **Cost of False Negative ($C_{\text{FN}}$)** = ₹2,700. **Cost of False Positive ($C_{\text{FP}}$)** = ₹90.
   - Theoretical optimal decision threshold:
     $$p^* = \frac{C_{\text{FP}}}{C_{\text{FP}} + C_{\text{FN}}} = \frac{90}{90 + 2700} = \frac{90}{2790} \approx \mathbf{3.23\%}$$
   - Any applicant with a predicted default probability $> 3.23\%$ must be declined.

---

## Case 5: Corporate Loan Portfolio Concentration Risk & Sector Limit Sizing

### 1. Scenario Context
A commercial bank has a total wholesale corporate loan portfolio of ₹10,000 Cr distributed across 5 industry sectors. The CRO requires a quantitative concentration assessment using the Herfindahl-Hirschman Index (HHI).

### 2. Portfolio Sector Exposure Data ([PRACTICE ASSUMPTION])

| Sector | Exposure ($E_i$, ₹ Cr) | Share ($s_i = E_i / \text{Total}$) | Baseline Default Rate |
|:---|:---:|:---:|:---:|
| Infrastructure & Power | ₹3,500 Cr | 35.0% | 4.2% |
| Real Estate & Construction | ₹2,500 Cr | 25.0% | 3.8% |
| Information Technology | ₹1,500 Cr | 15.0% | 0.8% |
| Pharmaceuticals | ₹1,500 Cr | 15.0% | 1.2% |
| Textiles & Apparel | ₹1,000 Cr | 10.0% | 3.0% |
| **Total** | **₹10,000 Cr** | **100.0%** | **—** |

### 3. Mathematical Concentration Analysis
1. **Herfindahl-Hirschman Index (HHI)**:
   $$\text{HHI} = \sum_{i=1}^k (s_i \times 100)^2 = 35^2 + 25^2 + 15^2 + 15^2 + 10^2 = 1225 + 625 + 225 + 225 + 100 = \mathbf{2,400}$$
2. **Interpretation**:
   - In financial risk management, $\text{HHI} > 1,800$ denotes a **highly concentrated portfolio**.
   - Two cyclical sectors (Infrastructure + Real Estate) represent 60% of total loan exposure.
3. **Remediation & Sizing Strategy**:
   - Establish a board-approved single-sector cap: **No sector may exceed 25.0% of total wholesale exposure**.
   - Initiate loan syndication / portfolio securitization to sell off ₹1,000 Cr of Infrastructure debt.
   - Reallocate origination capacity into low-correlation, low-default sectors (Pharma and IT).

---

## Case 6: Scorecard Model Drift & Population Stability Index (PSI) Remediation

### 1. Scenario Context
An application scorecard developed in 2023 is being audited. The Model Validation team calculates the Population Stability Index (PSI) comparing 2023 development data against Q3 2025 actual applicant scores.

### 2. Score Decile Shift Data ([PRACTICE ASSUMPTION])

| Score Decile | Dev % (Expected, $E_i$) | Actual % ($A_i$) | Difference ($A_i - E_i$) | Ratio ($A_i / E_i$) | $\ln(A_i / E_i)$ | Decile Index Contribution |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Decile 1 (High Risk) | 10.0% (0.10) | 18.0% (0.18) | +0.080 | 1.800 | +0.5878 | $0.080 \times 0.5878 = \mathbf{0.0470}$ |
| Decile 2 | 10.0% (0.10) | 15.0% (0.15) | +0.050 | 1.500 | +0.4055 | $0.050 \times 0.4055 = \mathbf{0.0203}$ |
| Decile 3 | 10.0% (0.10) | 12.0% (0.12) | +0.020 | 1.200 | +0.1823 | $0.020 \times 0.1823 = \mathbf{0.0036}$ |
| Decile 4–7 (Middle) | 40.0% (0.40) | 35.0% (0.35) | -0.050 | 0.875 | -0.1335 | $-0.050 \times -0.1335 = \mathbf{0.0067}$ |
| Decile 8–10 (Prime) | 30.0% (0.30) | 20.0% (0.20) | -0.100 | 0.667 | -0.4049 | $-0.100 \times -0.4049 = \mathbf{0.0405}$ |
| **Total PSI** | **100.0%** | **100.0%** | **—** | **—** | **—** | $\mathbf{\Sigma = 0.1181}$ |

### 3. Validation Assessment & Action Plan
- **PSI Threshold Interpretation ([REGULATORY SOURCE] SR 11-7 Heuristic)**:
  - $\text{PSI} = 0.1181$ falls in the **$0.10 \le \text{PSI} < 0.25$ moderate drift zone**.
- **Root Cause**:
  Applicant quality has degraded—Decile 1 (highest risk) surged from 10% to 18%, while prime applicants shrunk from 30% to 20%.
- **Action Plan**:
  1. The model's score ranking is still functional, but probability calibration is drifting.
  2. Implement an immediate adjustment: tighten cutoff score upward by 15 points to maintain identical marginal default rates.
  3. Schedule a complete model re-estimation within 90 days.

---

## Case 7: Volatile Collateralized Lending & Liquidation Cascade Thresholds

### 1. Business Context
A digital lending desk offers short-term loans secured by liquid collateral (e.g., gold ETFs or approved crypto tokens). The desk lends ₹70 Cr against ₹100 Cr collateral (initial Loan-to-Value $\text{LTV} = 70.0\%$).

### 2. Market Risk Dynamics ([PRACTICE ASSUMPTION])
- Daily collateral volatility: $\sigma = 4.0\%$.
- Order book depth: Selling ₹50 Cr of collateral induces an estimated 5.0% market slippage.
- Liquidation buffer design: Lenders must issue a margin call before collateral drops below the outstanding loan balance.

### 3. Mathematical Thresholds
1. **Margin Call Threshold**: Set at $\text{LTV} = 80.0\%$.
   $$\text{Collateral Value for Margin Call} = \frac{₹70\text{ Cr}}{0.80} = \mathbf{₹87.50\text{ Cr}} \quad (\text{a } 12.5\%\text{ decline})$$
2. **Hard Liquidation Threshold**: Set at $\text{LTV} = 88.0\%$.
   $$\text{Collateral Value for Liquidation} = \frac{₹70\text{ Cr}}{0.88} = \mathbf{₹79.55\text{ Cr}} \quad (\text{a } 20.45\%\text{ decline})$$
3. **Loss Given Default (LGD) Under Slippage**:
   - If collateral drops to ₹79.55 Cr and is liquidated under market distress with 5% slippage and 1% exchange fee (net recovery = 94%):
     $$\text{Net Proceeds} = 79.55 \times (1 - 0.06) = ₹74.78\text{ Cr}$$
   - Since Net Proceeds (₹74.78 Cr) > Outstanding Debt (₹70 Cr), the lender suffers **zero credit loss** ($\text{LGD} = 0\%$).
   - If the liquidation threshold were set too loose at $\text{LTV} = 95\%$ (Collateral = ₹73.68 Cr): Net proceeds = $73.68 \times 0.94 = ₹69.26\text{ Cr}$, resulting in a ₹0.74 Cr default loss.

---

## Case 8: Supply Chain Finance Reverse Factoring Contagion Analysis

### 1. Scenario Context
A bank provides a ₹1,200 Cr Reverse Factoring supply chain finance program. The bank pays suppliers of a large conglomerate ("Anchor Buyer") immediately at a discount, relying on the Anchor Buyer's credit to repay the bank after 90 days.

### 2. Contagion Mechanism ([PRACTICE ASSUMPTION])
- The Anchor Buyer experiences an accounting scandal; credit rating is downgraded from **AA to BB+**.
- **The Contagion Trap**:
  - The bank has exposure to 400 small-and-medium enterprise (SME) suppliers.
  - The bank stops financing new invoices. The Anchor Buyer freezes payments on all existing invoices.
  - The SME suppliers, deprived of working capital, cannot pay their own bank loans.
- **Expected Loss Migration**:
  - Baseline: $\text{PD} = 0.5\%$, $\text{LGD} = 40\% \implies \text{EL} = 0.5\% \times 40\% \times ₹1,200\text{ Cr} = \mathbf{₹2.4\text{ Cr}}$.
  - Post-Downgrade: Stressed $\text{PD} = 25.0\%$, $\text{LGD} = 65\% \implies \text{EL} = 25.0\% \times 65\% \times ₹1,200\text{ Cr} = \mathbf{₹195.0\text{ Cr}}$.
- **Remediation**: Reclassify the program from corporate working capital to distressed recovery; enforce recourse clauses on suppliers where legally feasible.

---

## Case 9: Operational Risk Capital Modeling via Loss Distribution Approach (LDA)

### 1. Framework Context
Under the Basel Advanced Measurement Approach (AMA), banks model operational risk capital using the Loss Distribution Approach (LDA), combining an annual event frequency distribution with an individual event severity distribution.

### 2. Distribution Parameters ([PRACTICE ASSUMPTION])
- **Frequency Distribution**: Poisson distribution with mean $\lambda = 20\text{ events/year}$.
- **Severity Distribution**: Lognormal distribution $\ln(X) \sim \mathcal{N}(\mu = 12.0, \sigma^2 = 1.44)$ (where $X$ is loss amount in INR).
  - Note: $\mu = 12.0 \implies \text{Median Loss} = e^{12} \approx ₹1.63\text{ Lakh}$.
  - Heavy tail: $\sigma = 1.20$.

### 3. Capital Charge Formulation
$$\text{Operational Risk Capital} = \text{VaR}_{99.9\%}(S) - \mathbb{E}[S]$$
Where aggregate annual loss $S = \sum_{i=1}^N X_i$.
1. **Expected Annual Loss ($\mathbb{E}[S]$)**:
   $$\mathbb{E}[X] = e^{\mu + \frac{\sigma^2}{2}} = e^{12.0 + \frac{1.44}{2}} = e^{12.72} \approx ₹334,370$$
   $$\mathbb{E}[S] = \lambda \times \mathbb{E}[X] = 20 \times 334,370 = \mathbf{₹66.87\text{ Lakh}}$$
2. **99.9% Operational VaR (via Monte Carlo Simulation)**:
   - With 100,000 simulations of annual loss compounding, the 99.9th percentile loss is determined to be **₹8.40 Cr**.
   - **Economic Capital Required**: $8.40\text{ Cr} - 0.67\text{ Cr} = \mathbf{₹7.73\text{ Cr}}$ held as dedicated operational risk equity capital.

---

## Case 10: Project Finance Debt Service Reserve Account (DSRA) Stress Sizing

### 1. Scenario Context
A 150 MW solar power project has ₹600 Cr senior debt with annual debt service (Principal + Interest) of ₹72 Cr. Lenders require sizing a Debt Service Reserve Account (DSRA) to protect against monsoon variability and grid curtailment.

### 2. Stress Scenario Simulation ([PRACTICE ASSUMPTION])
- Base Case: Annual generation = 250 GWh $\implies \text{Revenue} = ₹75\text{ Cr}$, $\text{O\&M} = ₹10\text{ Cr}$, $\text{CFADS} = ₹65\text{ Cr}$.
  - Baseline $\text{DSCR} = \frac{65}{72} = 0.903\times$ (requires tariff or debt restructuring).
- **Corrected Base Financials**:
  - P50 Generation = 300 GWh at ₹3.00/kWh $\implies \text{Revenue} = ₹90\text{ Cr}$.
  - Fixed O&M Expenses = ₹12 Cr.
  - $\text{CFADS}_{\text{base}} = 90 - 12 = \mathbf{₹78\text{ Cr}}$.
  - Baseline $\text{DSCR} = \frac{78}{72} = \mathbf{1.083\times}$.
- **P90 Severe Weather Shock (Low Solar Radiation)**:
  - Generation falls by 18% to 246 GWh $\implies \text{Revenue} = ₹73.8\text{ Cr}$.
  - $\text{CFADS}_{\text{stressed}} = 73.8 - 12 = \mathbf{₹61.8\text{ Cr}}$.
  - Debt service cash shortfall = $72.0 - 61.8 = \mathbf{₹10.2\text{ Cr}}$.
- **DSRA Sizing Policy**:
  - Sizing DSRA to cover **6 months of debt service** ($₹72\text{ Cr} / 2 = \mathbf{₹36.0\text{ Cr}}$) ensures the project can survive 3.5 consecutive years of P90 severe solar drought without triggering a loan default.

---

## Cross-Module Links
- 📖 [Risk Domain Knowledge](03_domain-knowledge.md)
- 📖 [Risk Tools & Technical Stack](04_tools-and-technical.md)
- 📖 [Risk High-Yield Question Bank](06_question-bank.md)
- 📖 [Risk Mock Assessment](12_mock-assessment.md)
- 📖 [General Finance Worked Cases](../../finance/finance/07_practice-and-cases.md)
