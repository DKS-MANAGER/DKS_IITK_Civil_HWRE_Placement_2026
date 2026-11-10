# Model Monitoring & Credit Risk QA — 60-Minute Interview Cheat Sheet
## Barclays Quantitative Analytics Graduate Analyst (BA4) | QA Model Monitoring | Noida

> **Candidate Profile**: M.Tech Civil Engineering (Hydraulics & Water Resources Engineering), IIT Kanpur  
> **Strict Privacy Compliance**: Zero personal names, undergraduate college names, or private project titles.

---

## 1. Golden Formulas & Mathematical Definitions

### 1.1 Expected Loss (EL) & Unexpected Loss (UL)
$$\text{Expected Loss (EL)} = \text{PD} \times \text{LGD} \times \text{EAD}$$
- **Exposure at Default (EAD)**: $\text{EAD} = \text{Drawn Balance} + (\text{Undrawn Commitment} \times \text{CCF})$
- **Credit Conversion Factor (CCF)**: Typically 20% to 50% for revolving facilities.
- **Unexpected Loss (UL)**: $\text{UL} = \text{VaR}_{99.9\%} - \text{EL}$ (Capital buffer funded by equity).

### 1.2 Discrimination Metrics
- **ROC-AUC**: Integral of TPR against FPR across all classification cutoffs. $\text{AUC} \in [0.5, 1.0]$.
- **Gini Coefficient (Accuracy Ratio)**:
  $$\text{Gini} = 2 \times \text{AUC} - 1 = \frac{A}{A + B}$$
  - *Benchmark*: $\text{Gini} > 0.40$ (Good), $\text{Gini} > 0.55$ (Strong), Drop $> 10\%$ triggers Amber.
- **Kolmogorov-Smirnov (KS) Statistic**:
  $$\text{KS} = \max_s |F_{\text{bads}}(s) - F_{\text{goods}}(s)|$$
  - *Benchmark*: $\text{KS} \in [0.30, 0.50]$ (Standard retail scorecard).

### 1.3 Calibration & Goodness-of-Fit
- **Hosmer-Lemeshow $\chi^2$ Test**:
  $$H = \sum_{g=1}^{10} \frac{(O_g - N_g \bar{\pi}_g)^2}{N_g \bar{\pi}_g (1 - \bar{\pi}_g)} \sim \chi^2(8)$$
  - *Decision*: Reject $H_0$ if $p < 0.05 \implies$ Systematic miscalibration.
- **Brier Score**: $\text{BS} = \frac{1}{N} \sum_{i=1}^N (p_i - y_i)^2 \in [0, 1]$. Lower is superior.

### 1.4 Population Stability Index (PSI) & Characteristic Stability (CSI)
$$\text{PSI} = \sum_{k=1}^K (A_k - E_k) \times \ln\left(\frac{A_k}{E_k}\right)$$
- **RAG Governance Thresholds**:
  - **$\text{PSI} < 0.10$ [GREEN]**: Insignificant shift; population is stable.
  - **$0.10 \le \text{PSI} \le 0.25$ [AMBER]**: Moderate drift; analyze CSI feature drivers; monitor monthly.
  - **$\text{PSI} > 0.25$ [RED]**: Significant drift; model predictions invalid; mandate PMA or recalibration.

---

## 2. Regulatory & Accounting Frameworks

### 2.1 IFRS 9 Financial Instruments (ECL)
```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              IFRS 9 THREE-STAGE FRAMEWORK                              │
├─────────────────────┬────────────────────────────────────┬─────────────────────────────┤
│ Stage               │ Credit Quality Definition          │ Loss Allowance Horizon      │
├─────────────────────┼────────────────────────────────────┼─────────────────────────────┤
│ Stage 1 (Performing)│ Low credit risk / no SICR          │ 12-Month Expected Loss      │
│ Stage 2 (Underperf) │ Significant Increase in Credit Risk│ Lifetime Expected Loss      │
│ Stage 3 (Impaired)  │ Default / 90+ DPD / Restructured   │ Lifetime ECL (Net Interest) │
└─────────────────────┴────────────────────────────────────┴─────────────────────────────┘
```
- **SICR Triggers**:
  - Quantitative: Doubling/tripling of lifetime PD ($>2\times$ or $200\text{ bps}$ increase since origination).
  - Qualitative: Forbearance, watchlist entry, debt restructuring.
  - Backstop: 30 Days Past Due (DPD).

### 2.2 Basel III/IV Internal Ratings-Based (IRB) Formula (Vasicek)
$$\text{Conditional PD} = \Phi\left( \frac{\Phi^{-1}(\text{TTC PD}) + \sqrt{\rho} \Phi^{-1}(0.999)}{\sqrt{1 - \rho}} \right)$$
- **Capital Requirement ($K$)**: $K = \left[\text{LGD}_{\text{downturn}} \times \text{Conditional PD} - (\text{PD} \times \text{LGD})\right] \times \text{Maturity Adjustment}$
- **Risk-Weighted Assets (RWA)**: $\text{RWA} = K \times 12.5 \times \text{EAD}$.

### 2.3 PRA SS1/23 & SR 11-7 (Model Risk Management)
- **Model Risk**: Financial loss, regulatory sanction, or poor decision resulting from flawed models.
- **Three Lines of Defense**:
  - *1LoD*: Quantitative Analytics (Model Development & **QA Model Monitoring**).
  - *2LoD*: Independent Model Review (IMR) & Enterprise Risk Management.
  - *3LoD*: Barclays Internal Audit (BIA).
- **Post-Model Adjustment (PMA)**: An overlay applied when models under-predict risk due to external shocks. Requires explicit root-cause justification, size quantification, and exit criteria.

---

## 3. High-Yield Interview Traps & Model Answers

### Q1: "Why might Gini remain stable while Hosmer-Lemeshow fails?"
> **Answer**:  
> "Gini evaluates **discrimination** (relative rank-ordering): whether riskier borrowers receive higher predicted default probabilities than safer ones. It is invariant to monotonic transformations. In contrast, Hosmer-Lemeshow evaluates **calibration** (absolute level accuracy): whether an average predicted PD of 4% actually translates to 4 defaults per 100 loans.  
> If a macroeconomic shock increases default rates uniformly across all deciles, the model may rank borrowers perfectly (preserving Gini), but severely under-predict the absolute event frequency (failing Hosmer-Lemeshow). In Risk QA, this requires a calibration scalar or Post-Model Adjustment rather than a complete feature rebuild."

### Q2: "How do you distinguish between Point-in-Time (PIT) and Through-the-Cycle (TTC) PD?"
> **Answer**:  
> "**Point-in-Time (PIT) PD** incorporates current macroeconomic conditions and represents the actual conditional default expectation over the next 12 months. It moves procyclically with the business cycle and is required for **IFRS 9 accounting impairment**.  
> **Through-the-Cycle (TTC) PD** measures long-term average default risk across a full economic cycle, smoothing out temporary cyclical volatility. It is used for **Basel regulatory capital** to prevent wild fluctuations in statutory capital reserves."

### Q3: "What is your immediate workflow if quarterly PSI breaches 0.28 (Red)?"
> **Answer**:  
> "1. **Validate Pipeline**: Verify data integrity, check for missing fields, binning edge cases, or upstream ETL changes.  
> 2. **CSI Decomposition**: Calculate Characteristic Stability Index on all input variables (e.g., DTI, utilization, delinquency history) to identify the specific drivers of the score shift.  
> 3. **Sub-Segment Analysis**: Segment the population by acquisition channel, product variant, or vintage cohort to isolate whether the shift is driven by business strategy (e.g., loosening underwriting criteria) or macroeconomic headwinds.  
> 4. **Governance Notification**: Issue an interim Model Monitoring Alert to the Model Owner and Independent Model Review (IMR).  
> 5. **Remediation**: Size a Post-Model Adjustment (PMA) if capital underestimation is suspected, and schedule the model for formal recalibration."

---

## 4. The 30-Second Engineering-to-Quant Pivot Script

> *"At IIT Kanpur, my research in Hydraulics and Water Resources Engineering focused on modeling stochastic, non-linear dynamic systems under uncertainty.*  
> *When predicting infrastructure failure, I trained tree-based machine learning models with extreme class imbalance, evaluating them using ROC-AUC, Precision-Recall curves, and TreeSHAP explainability—the exact analytical toolkit used to evaluate credit scorecards under PRA SS1/23.*  
> *Furthermore, calibrating 100-year flood events using Gumbel extreme-value distributions is mathematically isomorphic to Basel's 99.9% VaR tail-risk capital calculations.*  
> *Joining Barclays QA Model Monitoring allows me to direct this rigorous quantitative, statistical, and pipeline automation background toward safeguarding the bank's global balance sheet."*

