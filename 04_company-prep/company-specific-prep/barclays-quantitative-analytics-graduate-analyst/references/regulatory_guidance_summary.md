# Regulatory Guidance & Supervisory Standards in Banking Risk QA
## Comprehensive Reference: PRA SS1/23, US Fed SR 11-7, Basel III/IV & IFRS 9
### Barclays Quantitative Analytics (QA Model Monitoring) | IIT Kanpur Placement 2026–27

> **Target Audience**: Graduate Analyst (BA4) candidates in Risk Quantitative Analytics (Risk QA)  
> **Corporate Entity**: Barclays Global Service Centre India / Barclays Bank PLC  
> **Privacy Isolation**: Strict compliance — zero candidate personal names or private identifiers.

---

## 1. Executive Summary of Global Regulatory Regimes

Banking quantitative models are subject to rigorous statutory and supervisory governance. A Model Monitoring Analyst at Barclays must navigate multiple overlapping regulatory frameworks:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        GLOBAL BANKING REGULATORY MATRIX                                │
├─────────────────────────┬────────────────────────────┬─────────────────────────────────┤
│ Regulatory Authority    │ Supervisory Standard       │ Core Operational Mandate        │
├─────────────────────────┼────────────────────────────┼─────────────────────────────────┤
│ UK Prudential           │ PRA SS1/23                 │ Model Risk Management (MRM) for │
│ Regulation Authority    │                            │ banks; 5 Principles; PMAs       │
├─────────────────────────┼────────────────────────────┼─────────────────────────────────┤
│ US Federal Reserve &    │ SR 11-7 / OCC 2011-12      │ Supervisory Guidance on Model   │
│ OCC                     │                            │ Risk Management (Global benchmark│
├─────────────────────────┼────────────────────────────┼─────────────────────────────────┤
│ Basel Committee on      │ Basel III/IV (BCBS)        │ A-IRB Capital Requirements;     │
│ Banking Supervision     │ CRE20 / CRE30 / CRE36      │ 99.9% Vasicek Single Factor     │
├─────────────────────────┼────────────────────────────┼─────────────────────────────────┤
│ International Accounting│ IFRS 9 Financial           │ 3-Stage Expected Credit Loss    │
│ Standards Board (IASB)  │ Instruments                │ Forward-looking macro scenarios │
└─────────────────────────┴────────────────────────────┴─────────────────────────────────┘
```

---

## 2. Bank of England PRA Supervisory Statement SS1/23

Published in May 2023 with full implementation required by May 2024, **SS1/23** establishes the UK PRA's explicit supervisory expectations for Model Risk Management across UK-headquartered banks.

### The Five Core Principles of PRA SS1/23

#### Principle 1: Model Identification & Model Risk Classification
- **Definition of a Model**: "A quantitative method, system, or approach that applies statistical, economic, financial, or mathematical theories, techniques, and assumptions to process input data into quantitative estimates."
- **Model Inventory**: Comprehensive, centralized register of all active models, decommissioned models, models under development, and third-party vendor models.
- **Tiering**: Categorization into Tier 1 (High materiality), Tier 2 (Medium), and Tier 3 (Low) based on financial materiality, legal/regulatory exposure, and complexity.

#### Principle 2: Governance & Board Oversight
- Explicit Board and Senior Management accountability for model risk appetite and policy approval.
- Independent Model Risk Oversight committees (e.g., Barclays Credit Risk Model Oversight Committee - CRMOC).

#### Principle 3: Model Development, Implementation & Use
- Rigorous conceptual soundness, theoretical foundation, mathematical specification, and data quality standards.
- Documentation of model limitations, assumptions, and known weaknesses.

#### Principle 4: Independent Model Validation & Ongoing Monitoring
- **Validation (2LoD)**: Independent challenge conducted by teams separate from model developers (Barclays Independent Model Review - IMR).
- **Ongoing Monitoring (1LoD)**: **This is the core mandate of QA Model Monitoring.**
  - Regular surveillance of model performance, discrimination, calibration, and stability.
  - Objective quantitative triggers and RAG traffic lights.
  - Analysis of benchmark models, back-testing against realized outcomes, and out-of-time validation.

#### Principle 5: Model Risk Controls & Post-Model Adjustments (PMAs)
- **Post-Model Adjustments (PMAs) / Management Overlays**:
  - Defined as adjustments applied outside the core model algorithm when the model fails to capture emerging risks, macroeconomic shocks, or data anomalies.
  - PRA mandates that PMAs must have:
    1. Clear quantitative rationale and calculation methodology.
    2. Documented materiality assessment.
    3. Sunsetting / exit plans with explicit remediation timelines.
    4. Senior governance committee approval.

---

## 3. US Federal Reserve Supervisory Letter SR 11-7

Jointly issued by the Federal Reserve and OCC in April 2011, **SR 11-7** remains the foundational global benchmark for Model Risk Management.

### Key Conceptual Pillars of SR 11-7
1. **Model Risk Definition**:
   - Adverse consequences from decisions based on incorrect or misused model outputs.
   - Two fundamental causes:
     * *Fundamental errors*: Flawed theoretical design, programming bugs, unrepresentative training data.
     * *Incorrect usage*: Applying a model outside its intended operational boundary.
2. **Three Lines of Defense Model**:
   - **First Line (1LoD)**: Front Office, Business Units, and **Risk Quantitative Analytics (QA)**. Owns model development, ongoing monitoring, operational controls, and quarterly surveillance packs.
   - **Second Line (2LoD)**: Risk Management and **Independent Model Review (IMR)**. Validates models independently, challenges assumptions, verifies code, and sets risk appetite.
   - **Third Line (3LoD)**: **Barclays Internal Audit (BIA)**. Independently assesses whether 1LoD and 2LoD are complying with the Model Risk Policy.

---

## 4. Basel III / IV Internal Ratings-Based (IRB) Framework

Under the Basel framework established by the Basel Committee on Banking Supervision (BCBS), banks are permitted to calculate regulatory capital using internal models subject to supervisory approval.

### 4.1 Foundation IRB (F-IRB) vs Advanced IRB (A-IRB)
```
┌────────────────────────────┬────────────────────────────┬────────────────────────────┐
│ Parameter                  │ Foundation IRB (F-IRB)     │ Advanced IRB (A-IRB)       │
├────────────────────────────┼────────────────────────────┼────────────────────────────┤
│ Probability of Default (PD)│ Internal Model (TTC)       │ Internal Model (TTC)       │
│ Loss Given Default (LGD)   │ Supervisory Prescribed     │ Internal Model (Downturn)  │
│ Exposure at Default (EAD)  │ Supervisory Prescribed     │ Internal Model (CCF Model) │
│ Effective Maturity (M)     │ Fixed (2.5 years)          │ Facility Specific          │
└────────────────────────────┴────────────────────────────┴────────────────────────────┘
```

### 4.2 Vasicek Single-Factor Model Derivation
The Basel IRB capital formula derives from the asymptotic single-risk factor model (Vasicek, 2002):
$$Y_i = \sqrt{\rho} X + \sqrt{1 - \rho} Z_i$$
Where:
- $X \sim \mathcal{N}(0, 1)$ is the systemic macroeconomic factor.
- $Z_i \sim \mathcal{N}(0, 1)$ is the idiosyncratic borrower-specific factor.
- $\rho$ is the asset return correlation parameter.

Default occurs when latent asset return falls below threshold $c_i = \Phi^{-1}(\text{PD}_i)$.  
Evaluating solvency at the 99.9th percentile worst-case systemic realization ($X = -\Phi^{-1}(0.999)$):
$$\text{Conditional PD}(0.999) = \Phi\left( \frac{\Phi^{-1}(\text{PD}) + \sqrt{\rho}\Phi^{-1}(0.999)}{\sqrt{1 - \rho}} \right)$$

Regulatory Capital Requirement ($K$):
$$K = \left[ \text{LGD}_{\text{downturn}} \times \text{Conditional PD}(0.999) - (\text{PD} \times \text{LGD}) \right] \times \text{Maturity Adjustment}$$
$$\text{Risk-Weighted Assets (RWA)} = K \times 12.5 \times \text{EAD}$$

---

## 5. IFRS 9 Financial Instruments Impairment Standard

Effective January 1, 2018, IFRS 9 replaced IAS 39's incurred-loss model with an **Expected Credit Loss (ECL)** model to prevent late recognition of credit losses during downturns.

### Core Differences Between IFRS 9 and Basel IRB
```
┌─────────────────────────────────┬─────────────────────────────────┬─────────────────────────────────┐
│ Dimension                       │ Basel III/IV IRB Framework      │ IFRS 9 Financial Instruments    │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Objective                       │ Statutory Solvency & Capital    │ Financial Reporting & Impairment│
│ Time Horizon                    │ Fixed 12-Month Horizon          │ 12-Month (Stg 1) / Lifetime (2&3│
│ Economic Cycle View             │ Through-the-Cycle (TTC) PD      │ Point-in-Time (PIT) PD          │
│ Loss Given Default (LGD)        │ Economic Downturn LGD           │ Current / Point-in-Time LGD     │
│ Macroeconomic Scenarios         │ Single Severe Stress Scenario   │ Probability-Weighted Multi-Scen │
│ Discounting                     │ Not explicitly discounted       │ Discounted at EIR to Report Date│
└─────────────────────────────────┴─────────────────────────────────┴─────────────────────────────────┘
```

