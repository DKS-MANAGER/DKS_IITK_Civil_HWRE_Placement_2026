# 09 — Regulatory Capital, Basel Framework & Stress Testing

## IIT Kanpur Placement Preparation — Barclays Quantitative Analytics (QA Model Monitoring)

---

### Executive Overview & Prudential Banking Architecture

Commercial and investment banks operate under strict supervisory oversight to ensure solvency and protect depositor funds against catastrophic financial systemic failure. While financial accounting (IFRS 9) focuses on recognizing **Expected Losses (EL)** as provisions against quarterly revenue, prudential regulation (the **Basel Framework**) mandates that banks hold a buffer of equity capital against **Unexpected Losses (UL)** at an extreme confidence level (99.9% over a one-year horizon).

In Barclays Risk QA, the Model Monitoring team surveils internal models approved under the **Internal Ratings-Based (IRB)** approach. Analysts back-test Through-The-Cycle (TTC) PDs, Downturn LGDs, and Downturn EADs, ensure compliance with Basel 3.1 input and output floors, and validate the quantitative execution of Bank of England PRA and US Federal Reserve regulatory stress tests.

```
Loss Distribution
     Probability
        Density
          ▲
          │      Expected Loss (EL)
          │    [Covered by IFRS 9 ECL]
          │       ┌─────────┐
          │       │         │       Unexpected Loss (UL)
          │       │         │   [Covered by Basel Regulatory Capital]
          │      ███        │    ┌───────────────────────────┐
          │     █████       │    │                           │
          │    ███████      │    │                           │
          │   █████████     │    │                           │
          │  ███████████    │    │                           │        Catastrophic Stress
          │ █████████████   │    │                           │     [Covered by Stress Testing]
          └─┴───────────┴───┴────┴───────────────────────────┴─────────────────►
           0               EL                               VaR 99.9%       Credit Loss ($)
                            ◄───────────────── UL ──────────►
```

---

### 1. The Basel Evolution & Internal Ratings-Based (IRB) Approaches

The Basel Committee on Banking Supervision (BCBS) establishes international capital accords:
1. **Basel I (1988):** Crude, uniform risk weights (e.g., 100% for all commercial loans, 50% for all residential mortgages) irrespective of borrower creditworthiness.
2. **Basel II (2004):** Introduced the 3-Pillar structure and permitted internal risk models:
   - **Pillar 1:** Minimum Capital Requirements (Credit, Market, Operational risk).
   - **Pillar 2:** Supervisory Review Process and Internal Capital Adequacy Assessment Process (ICAAP).
   - **Pillar 3:** Market Discipline and public disclosure of risk exposures.
3. **Basel III (2010):** Enforced higher common equity quality (CET1), capital conservation buffers, countercyclical buffers, leverage ratios, and liquidity requirements (LCR and NSFR).
4. **Basel 3.1 / Basel IV (2020–2025):** Introduces an aggregate **72.5% output floor** on internally modeled RWAs, restricts A-IRB for large corporates, and introduces strict parameter input floors.

#### Three Regulatory Approaches to Credit Risk
Banks calculate Risk-Weighted Assets (RWA) under one of three supervisory approaches:

```
┌──────────────────────────────┬──────────────────────────────┬──────────────────────────────┐
│ Standardized Approach (SA)   │ Foundation IRB (F-IRB)       │ Advanced IRB (A-IRB)         │
├──────────────────────────────┼──────────────────────────────┼──────────────────────────────┤
│ • Prescribed by supervisor.  │ • Bank models its own PD.    │ • Bank models its own PD,    │
│ • Fixed risk weights by      │ • Supervisor prescribes:     │   LGD (Downturn), and EAD    │
│   external credit rating     │   - LGD: 45% (senior unsec)  │   (Downturn CCF).            │
│   or standardized asset      │   - EAD: Drawn + 75% unavail │ • Requires formal regulatory │
│   category.                  │   - Effective Maturity: 2.5y │   model approval & QA        │
│ • No internal quant models.  │ • Used for large corporates. │   ongoing monitoring.        │
└──────────────────────────────┴──────────────────────────────┴──────────────────────────────┘
```

---

### 2. The Asymptotic Single Risk Factor (ASRF) Model (Vasicek)

The core mathematical engine of Basel IRB capital requirements is Oldrich Vasicek's **Asymptotic Single Risk Factor (ASRF)** credit portfolio model (Vasicek, 1987, 2002).

#### Mathematical Derivation of Conditional Default Probability
Consider a portfolio of $N$ loans. The creditworthiness (asset return) of borrower $i$ over a one-year horizon is governed by a latent normalized variable $R_i$:

$$R_i = \sqrt{\rho} \cdot X + \sqrt{1 - \rho} \cdot \epsilon_i$$

where:
- $X \sim \mathcal{N}(0, 1)$ is the **single systematic risk factor** affecting all borrowers in the economy (e.g., macroeconomic state).
- $\epsilon_i \sim \mathcal{N}(0, 1)$ is the **idiosyncratic (firm-specific) risk factor**, mutually independent across all $i$ and independent of $X$.
- $\rho \in (0, 1)$ is the **asset correlation** between any two distinct borrowers:
  $$\text{Corr}(R_i, R_j) = \mathbb{E}[R_i R_j] = \mathbb{E}\left[(\sqrt{\rho} X + \sqrt{1-\rho}\epsilon_i)(\sqrt{\rho} X + \sqrt{1-\rho}\epsilon_j)\right] = \rho \quad (\forall i \ne j)$$

Borrower $i$ defaults if their asset return falls below a critical default threshold $C_i$:
$$P(\text{Default}_i) = P(R_i < C_i) = \Phi(C_i) = PD_i \implies C_i = \Phi^{-1}(PD_i)$$

where $\Phi(\cdot)$ is the standard normal cumulative distribution function.

Now, condition the default probability on a specific realization of the macroeconomic factor $X = x$:
$$PD_i(x) = P(R_i < C_i \mid X = x) = P\left(\sqrt{\rho} x + \sqrt{1 - \rho} \epsilon_i < \Phi^{-1}(PD_i)\right)$$
$$PD_i(x) = P\left(\epsilon_i < \frac{\Phi^{-1}(PD_i) - \sqrt{\rho} x}{\sqrt{1 - \rho}}\right) = \Phi\left( \frac{\Phi^{-1}(PD_i) - \sqrt{\rho} x}{\sqrt{1 - \rho}} \right)$$

#### Derivation of the 99.9% Value at Risk (VaR)
Under Basel regulations, capital is designed to withstand economic conditions that occur once every 1,000 years (a $0.1\%$ severe macroeconomic shock, or the $99.9\%$ confidence limit).
Since lower values of $X$ represent worse economic recessions, the 0.1-percentile worst macroeconomic state is:
$$x_{0.001} = \Phi^{-1}(0.001) = -\Phi^{-1}(0.999) \approx -3.0902$$

Substituting $x_{0.001}$ into the conditional default probability:
$$\text{Conditional PD}_{99.9\%} = \Phi\left( \frac{\Phi^{-1}(PD_i) - \sqrt{\rho}(-\Phi^{-1}(0.999))}{\sqrt{1 - \rho}} \right) = \Phi\left( \frac{\Phi^{-1}(PD_i) + \sqrt{\rho} \, \Phi^{-1}(0.999)}{\sqrt{1 - \rho}} \right)$$

#### Regulatory Capital Requirement Formula ($K$)
The capital charge $K$ represents the **Unexpected Loss (UL)**, calculated as the difference between the 99.9% conditional loss and the expected loss ($PD \times LGD$):

$$K = \left[ LGD \times \Phi\left( \frac{\Phi^{-1}(PD) + \sqrt{\rho} \, \Phi^{-1}(0.999)}{\sqrt{1 - \rho}} \right) - (PD \times LGD) \right] \times \text{Maturity Adjustment}(M)$$

For retail exposures, no maturity adjustment applies ($\text{Maturity Adjustment} = 1.0$).  
For wholesale/corporate exposures, a maturity adjustment factor accounts for credit migration risk prior to loan maturity $M$:

$$\text{Maturity Adjustment}(M) = \frac{1 + (M - 2.5) \cdot b(PD)}{1 - 1.5 \cdot b(PD)}$$
$$\text{where } b(PD) = \left(0.11852 - 0.05478 \times \ln(PD)\right)^2$$

#### Risk-Weighted Assets (RWA)
Risk-Weighted Assets are calculated by scaling the capital charge $K$ by $12.5$ (the reciprocal of the 8.0% minimum capital requirement, $\frac{1}{0.08} = 12.5$) and multiplying by Exposure at Default:

$$\text{RWA} = K \times 12.5 \times \text{EAD}$$

$$\text{Minimum Regulatory Capital} = 8\% \times \text{RWA} = 0.08 \times (K \times 12.5 \times \text{EAD}) = K \times \text{EAD}$$

---

### 3. Supervisory Asset Correlation Formulas ($\rho$)

Under the Basel IRB framework, banks are not permitted to estimate asset correlation $\rho$ empirically; it is prescribed by regulatory formulas that reflect empirical findings that higher default probabilities correlate with smaller, idiosyncratic business dynamics, while high-grade borrowers are more sensitive to macro-cycles.

```
┌─────────────────────────────────┬────────────────────────────────────────────────────────────────────────┐
│ Basel Asset Class               │ Regulatory Asset Correlation Formula ρ(PD)                             │
├─────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ Corporate, Sovereign, Bank      │ ρ = 0.12 × ((1 - e^(-50×PD)) / (1 - e^(-50)))                          │
│                                 │     + 0.24 × (1 - (1 - e^(-50×PD)) / (1 - e^(-50)))                    │
│                                 │ (Ranges from 24% for low PD to 12% for high PD)                        │
├─────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ SME Corporate (Firm Size S,     │ ρ_SME = ρ_Corp - 0.04 × (1 - (S - 5) / 45)                             │
│ €5M <= S <= €50M revenue)       │ (Firm size adjustment provides up to 4% capital relief)                │
├─────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ Residential Mortgages           │ ρ = 0.15 (Fixed at 15%)                                                │
├─────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ Qualifying Revolving Retail     │ ρ = 0.04 (Fixed at 4% — reflects idiosyncratic consumer behavior)      │
│ Exposures (QRRE / Credit Cards) │                                                                        │
├─────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ Other Retail (Auto / Personal)  │ ρ = 0.03 × ((1 - e^(-35×PD)) / (1 - e^(-35)))                          │
│                                 │     + 0.16 × (1 - (1 - e^(-35×PD)) / (1 - e^(-35)))                    │
│                                 │ (Ranges from 16% for low PD to 3% for high PD)                         │
└─────────────────────────────────┴────────────────────────────────────────────────────────────────────────┘
```

---

### 4. Capital Ratios, Buffers & The Output Floor

```
Total Capital Requirement
┌───────────────────────────────────────────────────────────┐
│ Pillar 2B: PRA Buffer (Firm-specific stress buffer)       │
├───────────────────────────────────────────────────────────┤
│ G-SIB Surcharge: Barclays UK / Group (1.50%)              │
├───────────────────────────────────────────────────────────┤
│ Countercyclical Capital Buffer (CCyB: 0% – 2.50%)         │
├───────────────────────────────────────────────────────────┤
│ Capital Conservation Buffer (CCb: 2.50%)                  │
├───────────────────────────────────────────────────────────┤
│ Pillar 2A: Individual Capital Guidance (ICG)              │
├───────────────────────────────────────────────────────────┤
│ Pillar 1 Minimum CET1 (4.50%)                             │
└───────────────────────────────────────────────────────────┘
 ◄──────────────── Total CET1 Stack: ~13.5% – 15.0% ───────►
```

#### Regulatory Capital Ratios (Pillar 1)
- **Common Equity Tier 1 (CET1) Ratio:**
  $$\text{CET1 Ratio} = \frac{\text{CET1 Capital}}{\text{Total RWA}} \ge 4.5\%$$
- **Tier 1 Ratio:** $\frac{\text{Tier 1 Capital}}{\text{Total RWA}} \ge 6.0\%$
- **Total Capital Ratio:** $\frac{\text{Total Capital (Tier 1 + Tier 2)}}{\text{Total RWA}} \ge 8.0\%$
- **Tier 1 Leverage Ratio:**
  $$\text{Leverage Ratio} = \frac{\text{Tier 1 Capital}}{\text{Total Leverage Exposure (On + Off-Balance Sheet)}} \ge 3.25\%$$

#### Basel 3.1 Aggregate Output Floor
A central reform in the Basel 3.1 rules is the **72.5% Output Floor**:
$$\text{RWA}_{\text{Floor}} = \max\left(\text{RWA}_{\text{IRB}}, \; 0.725 \times \text{RWA}_{\text{Standardized}}\right)$$
If a bank's advanced internal quant models yield RWAs below 72.5% of what the Standardized Approach would dictate, the bank is legally required to hold capital based on the 72.5% floor. In QA Model Monitoring, analysts track the RWA gap between IRB and Standardized calculations.

---

### 5. Regulatory Stress Testing (BoE PRA & Fed CCAR)

Barclays is subject to concurrent macro-prudential stress testing by:
1. **Bank of England PRA Annual Cyclical Scenario (ACS):** Tests UK and global banking stability under a hypothetical 5-year severe downturn.
2. **US Federal Reserve Comprehensive Capital Analysis and Review (CCAR):** Applies to Barclays US Intermediate Holding Company (IHC) under Dodd-Frank Act Stress Testing (DFAST).

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        Regulatory Stress Testing Execution Flow                        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  1. Macro Scenario: Central bank publishes severely adverse GDP, unemployment, HPI.    │
│  2. Satellite Models: Risk QA models translate macro paths into shifted PD, LGD, EAD.  │
│  3. Financial Engine: Multi-year projection of IFRS 9 ECL impairments & Basel RWA.     │
│  4. P&L & Balance Sheet: Net interest income compression, trading losses, cost shocks. │
│  5. Capital Depletion: Project CET1 ratio trajectory across 3 to 5 projection years.   │
│  6. Pass/Fail Decision: Capital must not breach minimum hurdle rates (plus CCb).       │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

#### Satellite Modeling Methodology
Risk QA develops and monitors **Satellite Models** (typically Vector Autoregressions, panel regressions, or state-space models) linking macroeconomic explanatory variables to portfolio default rates:

$$\text{logit}(PD_t) = \alpha + \beta_1 \Delta \text{GDP}_t + \beta_2 \text{Unemployment}_t + \beta_3 \Delta \text{HPI}_t + \beta_4 \text{BaseRate}_t + \epsilon_t$$

QA Model Monitoring regularly back-tests these satellite models against realized crisis quarters to ensure that elasticities ($\beta_j$) remain structurally valid.

---

### 6. Fully Worked Numerical Calculation: Basel IRB Capital & RWA

Let us calculate the Basel A-IRB Capital Requirement ($K$), Risk-Weighted Assets (RWA), and CET1 Capital Charge for a **Residential Mortgage Exposure** and compare it with a **Corporate Loan**.

#### Scenario A: Residential Mortgage Facility
- $\text{EAD} = \$500,000$
- 1-Year TTC $\text{PD} = 0.50\% = 0.0050$
- Downturn $\text{LGD} = 20.0\% = 0.20$
- Asset Correlation for Residential Mortgages: $\rho = 0.15$ (fixed by Basel rules)
- Maturity Adjustment: Not applicable for retail ($M = 1.0$)

##### Step 1: Compute Standard Normal Inverse Quantiles
$$\Phi^{-1}(PD) = \Phi^{-1}(0.0050) \approx -2.5758$$
$$\Phi^{-1}(0.999) \approx 3.0902$$

##### Step 2: Calculate Vasicek Conditional Default Probability at 99.9%
$$\text{Argument} = \frac{\Phi^{-1}(PD) + \sqrt{\rho} \, \Phi^{-1}(0.999)}{\sqrt{1 - \rho}} = \frac{-2.5758 + \sqrt{0.15} \times (3.0902)}{\sqrt{1 - 0.15}}$$
$$\sqrt{0.15} \approx 0.3873, \quad \sqrt{0.85} \approx 0.9220$$
$$\text{Numerator} = -2.5758 + (0.3873 \times 3.0902) = -2.5758 + 1.1968 = -1.3790$$
$$\text{Argument} = \frac{-1.3790}{0.9220} = -1.4957$$
$$\text{Conditional PD}_{99.9\%} = \Phi(-1.4957) = \mathbf{0.06736} \quad (6.736\%)$$

##### Step 3: Compute Capital Requirement Factor $K$
$$K = \left[ LGD \times \text{Conditional PD}_{99.9\%} \right] - \left[ PD \times LGD \right]$$
$$K = [0.20 \times 0.06736] - [0.0050 \times 0.20] = 0.013472 - 0.001000 = \mathbf{0.012472} \quad (1.247\%)$$

##### Step 4: Calculate RWA and Minimum Capital Charge
$$\text{RWA} = K \times 12.5 \times \text{EAD} = 0.012472 \times 12.5 \times \$500,000 = \mathbf{\$77,950}$$
$$\text{Risk Weight \%} = \frac{\$77,950}{\$500,000} = \mathbf{15.59\%}$$
$$\text{Minimum Total Capital (8\%)} = 0.08 \times \$77,950 = \mathbf{\$6,236}$$
$$\text{Target CET1 Capital (14\%)} = 0.14 \times \$77,950 = \mathbf{\$10,913}$$

---

#### Scenario B: Corporate Loan Facility
- $\text{EAD} = \$10,000,000$
- 1-Year TTC $\text{PD} = 1.0\% = 0.010$
- Downturn $\text{LGD} = 45.0\% = 0.45$
- Contractual Effective Maturity $M = 3.0$ years

##### Step 1: Corporate Asset Correlation $\rho(PD)$
$$\rho = 0.12 \times \frac{1 - e^{-50 \times 0.01}}{1 - e^{-50}} + 0.24 \times \left[ 1 - \frac{1 - e^{-50 \times 0.01}}{1 - e^{-50}} \right]$$
$$e^{-50 \times 0.01} = e^{-0.5} \approx 0.6065 \implies 1 - 0.6065 = 0.3935$$
$$\rho = 0.12 \times 0.3935 + 0.24 \times (1 - 0.3935) = 0.04722 + 0.14556 = \mathbf{0.19278} \quad (19.28\%)$$

##### Step 2: Vasicek Conditional PD at 99.9%
$$\Phi^{-1}(0.01) \approx -2.3263, \quad \sqrt{\rho} = \sqrt{0.19278} \approx 0.4391, \quad \sqrt{1 - \rho} \approx 0.8985$$
$$\text{Argument} = \frac{-2.3263 + (0.4391 \times 3.0902)}{0.8985} = \frac{-2.3263 + 1.3569}{0.8985} = \frac{-0.9694}{0.8985} = -1.0789$$
$$\text{Conditional PD}_{99.9\%} = \Phi(-1.0789) = \mathbf{0.1403} \quad (14.03\%)$$

##### Step 3: Maturity Adjustment $b(PD)$
$$b(0.01) = (0.11852 - 0.05478 \times \ln(0.01))^2 = (0.11852 - 0.05478 \times (-4.6052))^2$$
$$b(0.01) = (0.11852 + 0.25227)^2 = (0.37079)^2 \approx \mathbf{0.13749}$$
$$\text{Maturity Adj}(M = 3.0) = \frac{1 + (3.0 - 2.5) \times 0.13749}{1 - 1.5 \times 0.13749} = \frac{1 + 0.06875}{1 - 0.20624} = \frac{1.06875}{0.79376} = \mathbf{1.3464}$$

##### Step 4: Capital Requirement $K$ & RWA
$$K_{\text{base}} = [0.45 \times 0.1403] - [0.010 \times 0.45] = 0.063135 - 0.004500 = 0.058635$$
$$K = K_{\text{base}} \times \text{Maturity Adj} = 0.058635 \times 1.3464 = \mathbf{0.078946} \quad (7.895\%)$$
$$\text{RWA} = K \times 12.5 \times \$10,000,000 = 0.078946 \times 12.5 \times \$10,000,000 = \mathbf{\$9,868,250}$$
$$\text{Risk Weight \%} = \frac{\$9,868,250}{\$10,000,000} = \mathbf{98.68\%}$$
$$\text{Minimum Total Capital (8\%)} = 0.08 \times \$9,868,250 = \mathbf{\$789,460}$$

---

### 7. Risk QA Monitoring Summary Reference

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│               Regulatory Capital & Monitoring Metrics Comparison Matrix                │
├─────────────────────┬──────────────────────────────┬───────────────────────────────────┤
│ Concept             │ Basel III IRB Framework      │ QA Model Monitoring Requirement   │
├─────────────────────┼──────────────────────────────┼───────────────────────────────────┤
│ Target Metric       │ 99.9% Unexpected Loss (UL)   │ Validate TTC PD, Downturn LGD     │
│ Default Definition  │ 90 DPD, bankruptcy, distress │ Confirm alignment with EBA/PRA    │
│ Economic Cycle      │ Through-The-Cycle (TTC)      │ Monitor Cyclicality index (Z-gap) │
│ Loss Horizon        │ 1-year forward               │ Quarterly 12-month back-testing   │
│ RWA Floor           │ 72.5% Basel 3.1 output floor │ Track IRB vs SA delta monthly     │
│ Stress Horizon      │ 3–5 year macroeconomic path  │ Check satellite model stability   │
└─────────────────────┴──────────────────────────────┴───────────────────────────────────┘
```

---

*Authoritative cross-reference: Basel Committee on Banking Supervision (BCBS) Basel III & Basel 3.1 Frameworks; Bank of England Prudential Regulation Authority (PRA) Supervisory Statements SS10/13 & SS11/13; Vasicek, O. (2002), "The Distribution of Loan Portfolio Value", Risk.*

