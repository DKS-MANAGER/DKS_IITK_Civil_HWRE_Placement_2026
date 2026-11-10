# 08 — IFRS 9 Impairment, Staging & Lifetime Expected Credit Loss

## IIT Kanpur Placement Preparation — Barclays Quantitative Analytics (QA Model Monitoring)

---

### Executive Overview & Regulatory Mandate

Following the 2007–2008 Global Financial Crisis, global banking regulators identified a fatal flaw in the legacy **IAS 39 Incurred Loss Model**: banks were permitted to recognize credit losses only *after* an observable loss event (such as missed payments or formal default) occurred. This "too little, too late" provisioning worsened the credit crunch, as banks suffered sudden, massive loan-loss spikes precisely when their capital was most depleted.

To rectify this pro-cyclical vulnerability, the International Accounting Standards Board (IASB) issued **IFRS 9 Financial Instruments** (effective January 1, 2018), mandating a forward-looking **Expected Credit Loss (ECL)** framework. In the US, the Financial Accounting Standards Board (FASB) introduced the analogous **CECL (Current Expected Credit Losses)** standard under ASC 326.

In Barclays Risk QA, the Model Monitoring team is responsible for ongoing surveillance of IFRS 9 PD, LGD, and EAD models, monitoring staging migration rates, auditing macroeconomic scenario conditioning, and assessing the validity of Post-Model Adjustments (PMAs).

---

### 1. The IFRS 9 Three-Stage Impairment Model

IFRS 9 classifies all financial assets evaluated at amortized cost (or fair value through other comprehensive income — FVOCI) into one of three distinct stages based on changes in credit quality since initial recognition:

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              IFRS 9 Three-Stage Impairment Framework                            │
├───────────────────────────────┬─────────────────────────────────┬───────────────────────────────┤
│ Stage 1: Performing           │ Stage 2: Underperforming        │ Stage 3: Credit-Impaired      │
├───────────────────────────────┼─────────────────────────────────┼───────────────────────────────┤
│ • Credit quality has NOT      │ • Significant Increase in       │ • Objective evidence of       │
│   deteriorated significantly   │   Credit Risk (SICR) since      │   impairment / formal         │
│   since origination.          │   origination.                  │   default event.              │
│ • Provision:                  │ • Provision:                    │ • Provision:                  │
│   12-Month ECL                │   Lifetime ECL                  │   Lifetime ECL                │
│ • Interest Recognition:       │ • Interest Recognition:         │ • Interest Recognition:       │
│   Gross Carrying Amount       │   Gross Carrying Amount         │   Net Carrying Amount         │
│   (Balance × EIR)             │   (Balance × EIR)               │   ((Balance - ECL) × EIR)     │
│ • Delinquency status:         │ • Delinquency status:           │ • Delinquency status:         │
│   0–29 Days Past Due (DPD)    │   Usually 30–89 DPD or SICR     │   90+ DPD, Bankruptcy, Fraud  │
└───────────────────────────────┴─────────────────────────────────┴───────────────────────────────┘
```

#### The Staging Cliff-Effect
When an account breaches SICR thresholds and transitions from **Stage 1 to Stage 2**, the impairment provision jumps from a 12-month horizon to the entire remaining contractual (or behavioral) lifetime. For medium-to-long term portfolios (e.g., 5-year loans or 25-year mortgages), this staging transition often produces an immediate **300% to 600% increase in loan-loss provisions**, creating a significant P&L impact.

---

### 2. Significant Increase in Credit Risk (SICR) Framework

The determination of SICR is the operational core of IFRS 9. Banks must evaluate credit deterioration by comparing the risk of default occurring over the expected life of the financial instrument at the reporting date against the risk of default estimated at initial origination.

```
                  ┌──────────────────────────────────────────────┐
                  │          SICR Evaluation Pipeline            │
                  └──────────────────────┬───────────────────────┘
                                         │
         ┌───────────────────────────────┼───────────────────────────────┐
         ▼                               ▼                               ▼
┌──────────────────┐           ┌──────────────────┐            ┌──────────────────┐
│  Quantitative    │           │   Qualitative    │            │    Regulatory    │
│    Criterion     │           │    Indicators    │            │     Backstop     │
├──────────────────┤           ├──────────────────┤            ├──────────────────┤
│• Relative &      │           │• Forbearance /   │            │• 30 Days Past    │
│  absolute change │           │  Concession flag │            │  Due (DPD)       │
│  in Lifetime PD: │           │• Internal Early  │            │  rebuttable      │
│  ΔPD_Lifetime    │           │  Warning Watch   │            │  presumption.    │
│• Scorecard notch │           │• Industry sector │            │• Irrespective of │
│  deterioration   │           │  macroeconomic   │            │  PD score, 30+   │
│  (e.g., ≥ 3-step │           │  vulnerability   │            │  DPD must enter  │
│  downgrade)      │           │• Fraud / Legal   │            │  Stage 2.        │
└──────────────────┘           └──────────────────┘            └──────────────────┘
```

#### 2.1 Quantitative Criteria: Dual-Threshold Lifetime PD Test
In Barclays retail and wholesale portfolios, an account triggers quantitative SICR if both a **relative threshold** and an **absolute threshold** are breached simultaneously:

$$\text{SICR}_{\text{Quant}} = \mathbb{I}\left( \frac{\text{PD}_{\text{current}}^{\text{lifetime}}}{\text{PD}_{\text{origination}}^{\text{lifetime}}} \ge \theta_{\text{rel}} \;\; \mathbf{AND} \;\; \left( \text{PD}_{\text{current}}^{\text{lifetime}} - \text{PD}_{\text{origination}}^{\text{lifetime}} \right) \ge \theta_{\text{abs}} \right)$$

##### Why Both Thresholds Are Required:
1. **If only Relative Threshold ($\theta_{\text{rel}} = 3.0$) were used:**  
   A super-prime mortgage with an origination lifetime PD of $0.05\%$ increasing to $0.16\%$ represents a $3.2\times$ relative increase, triggering SICR. However, the borrower remains extremely safe ($99.84\%$ non-default probability). The absolute threshold ($\theta_{\text{abs}} = 100\text{ bps} = 1.0\%$) prevents spurious transitions of low-risk borrowers.
2. **If only Absolute Threshold ($\theta_{\text{abs}} = 1.0\%$) were used:**  
   A high-risk loan with an origination lifetime PD of $20.0\%$ increasing to $20.8\%$ (+80 bps) would not trigger SICR despite already operating near severe distress.

#### 2.2 Qualitative Indicators & Early Warning Systems (EWS)
Regardless of the quantitative lifetime PD delta, accounts are immediately transferred to Stage 2 upon triggering qualitative risk flags:
- **Forbearance / Restructuring:** Borrower requested debt consolidation, interest payment holiday, or tenure extension due to financial distress.
- **Credit Bureau Adverse Events:** Borrower defaulted on an external loan at another financial institution (detected via cross-banking bureau feed).
- **Internal Watchlist:** Wholesale borrowers assigned to "Amber" or "Red" risk review status by credit committee.

#### 2.3 Regulatory 30 DPD Backstop
IFRS 9 includes a rebuttable presumption that credit risk has increased significantly no later than when contractual payments are **more than 30 days past due (30 DPD)**. In practice, major UK and international banks treat 30 DPD as a strict hard floor: any loan with $30 \le \text{DPD} \le 89$ is automatically placed in Stage 2.

#### 2.4 Low Credit Risk Exemption (LCRE)
Under paragraph 5.5.10 of IFRS 9, financial instruments determined to have "low credit risk" at the reporting date (typically external investment grade: S&P/Fitch $\text{BBB}-$ or higher, Moody's $\text{Baa3}$ or higher) may be presumed not to have experienced an SICR, remaining in Stage 1 without historical origination tracking. Barclays restricts LCRE primarily to sovereign debt, supranationals, and high-grade treasury holdings.

---

### 3. Forward-Looking Macroeconomic Conditioning & Multi-Scenario ECL

Unlike regulatory Basel IRB (which computes a point-in-time or downturn capital charge under conservative supervisory rules), IFRS 9 explicitly requires **unbiased, probability-weighted estimates of expected credit loss** conditioned on forward-looking macroeconomic scenarios.

$$\text{ECL}_{\text{Total}} = \sum_{s=1}^{S} w_s \times \text{ECL}_s$$

where:
- $S$ is the number of macroeconomic scenarios (typically $S = 4$ in Barclays).
- $w_s$ is the assigned scenario probability weight, with $\sum_{s=1}^{S} w_s = 1.0$.
- $\text{ECL}_s$ is the expected credit loss calculated under the conditioning path of scenario $s$.

#### Barclays Four-Scenario Framework
Barclays Economics and Risk Analytics teams generate macroeconomic forecast distributions covering:

```
┌─────────────────┬──────────┬─────────────────────────────────────────────────────────────┐
│ Scenario        │ Weight   │ Macroeconomic Trajectory (UK / US / Global)                 │
├─────────────────┼──────────┼─────────────────────────────────────────────────────────────┤
│ 1. Baseline     │ 50%      │ Central consensus view: steady GDP growth (1.5%), moderate  │
│                 │          │ unemployment (4.2%), gradual central bank rate easing.      │
├─────────────────┼──────────┼─────────────────────────────────────────────────────────────┤
│ 2. Upside       │ 15%      │ Favorable expansion: accelerated GDP (2.8%), lower jobless  │
│                 │          │ rate (3.5%), resilient house prices (+4% p.a.).             │
├─────────────────┼──────────┼─────────────────────────────────────────────────────────────┤
│ 3. Downside     │ 25%      │ Mild recession: GDP contraction (-1.0%), rising jobless     │
│                 │          │ rate (6.5%), property price deflation (-8%).               │
├─────────────────┼──────────┼─────────────────────────────────────────────────────────────┤
│ 4. Severe       │ 10%      │ Stagflation / Systemic shock: steep recession (-3.2%), high │
│    Downside     │          │ unemployment (8.8%), aggressive property drop (-20%).       │
└─────────────────┴──────────┴─────────────────────────────────────────────────────────────┘
```

#### Jensen's Inequality and ECL Non-Linearity
A central quant principle in IFRS 9 is that **ECL is a non-linear convex function of macroeconomic stress**:

$$f(\mathbb{E}[\text{Macro}]) < \mathbb{E}[f(\text{Macro})] = \text{ECL}_{\text{weighted}}$$

When the macroeconomic environment deteriorates:
1. Marginal default probabilities ($PD$) spike exponentially (due to the logistic link $\frac{1}{1 + e^{-z}}$).
2. Loss Given Default ($LGD$) increases due to falling collateral / real estate valuations.
3. Exposure at Default ($EAD$) increases as distressed borrowers draw down credit card and revolving credit lines.
4. Accounts cross SICR thresholds, moving from 12-month ECL to Lifetime ECL.

Because of this severe convexity, evaluating ECL solely on the single "Baseline" scenario systematically underestimates actual credit losses. The multi-scenario probability-weighted architecture captures this tail skewness.

---

### 4. Mathematical Formulation of ECL & Discounting

#### 4.1 Marginal Default Probability & Survival Architecture
Let the lifetime of a credit facility be divided into discrete monthly or annual projection periods $t \in \{1, 2, \dots, T\}$.

Let $h_t$ represent the **marginal hazard rate (conditional default probability)** in period $t$, given survival up to period $t-1$:
$$h_t = P(\tau = t \mid \tau > t-1)$$

The **survival probability** $S_t = P(\tau > t)$ that the facility has not defaulted through the end of period $t$ is:
$$S_0 = 1.0, \quad S_t = \prod_{k=1}^{t} (1 - h_k) = S_{t-1} \times (1 - h_t)$$

The **marginal probability of default in period $t$** ($d_t = P(\tau = t)$) is:
$$d_t = S_{t-1} - S_t = S_{t-1} \times h_t$$

The **cumulative default probability** through period $t$ is:
$$\text{PD}_{\text{cum}}(t) = 1 - S_t = \sum_{k=1}^{t} d_k$$

#### 4.2 12-Month Expected Credit Loss (Stage 1)
For Stage 1 accounts, the loss horizon is truncated at month 12 (or the remaining life if less than 12 months):

$$\text{ECL}_{\text{12M}} = \sum_{t=1}^{12} \frac{d_t \times \text{LGD}_t \times \text{EAD}_t}{(1 + \text{EIR})^t}$$

where $\text{EIR}$ is the monthly Effective Interest Rate determined at origination.

#### 4.3 Lifetime Expected Credit Loss (Stage 2 and Stage 3)
For Stage 2 and Stage 3 accounts, losses are discounted across the entire remaining contractual term $T$:

$$\text{ECL}_{\text{Lifetime}} = \sum_{t=1}^{T} \frac{d_t \times \text{LGD}_t \times \text{EAD}_t}{(1 + \text{EIR})^t}$$

For revolving products without fixed contractual maturity (e.g., Barclaycard credit cards, revolving overdrafts), $T$ is determined based on the **behavioral life** (the historical time required for the bank to detect credit deterioration and cancel the available limit, typically 36 to 60 months).

#### 4.4 Why Discounting Must Use the Effective Interest Rate (EIR)
Under IFRS 9 paragraph 5.5.17, cash shortfalls must be discounted using the **Effective Interest Rate (EIR)** established at initial recognition, rather than a market risk-free rate or WACC:
- The EIR is the exact rate that discounts future contractual contractual cash flows to the initial net carrying amount.
- Using a market rate would conflate credit impairment with general interest rate risk (duration risk).
- If variable interest rates apply, the current floating EIR is utilized.

---

### 5. Post-Model Adjustments (PMA) & Management Overlays

In real-world banking operations, statistical models trained on historical data cannot anticipate unprecedented economic regimes or structural policy changes. A **Post-Model Adjustment (PMA)** (or Management Overlay) is a documented, quantified manual adjustment added to or subtracted from model-generated ECL provisions.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              PMA Governance Life Cycle                                 │
├────────────────────────────────────────────────────────────────────────────────────────┤
│  1. Identification: Quantitative surveillance reveals model under/over-prediction.    │
│  2. Quantification: Analytical sizing based on stress testing or benchmark proxies.    │
│  3. Governance Review: Formal review by Barclays Model Risk Governance Committee.      │
│  4. External Audit: Scrutiny and signed approval by PRA / external statutory auditors. │
│  5. Remediation & Sunset: Model recalibration or rebuild to absorb PMA into code.      │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

#### Typical Drivers of PMAs in Barclays Risk QA:
1. **Government Intervention Distortions:** Historical COVID-19 furlough schemes and payment holidays temporarily suppressed default rates, making empirical models predict unrealistically low default rates during economic recessions. PMAs were applied to inject realistic distress.
2. **Cost-of-Living & Energy Price Shocks:** Rapid inflation and interest rate hikes in the UK directly impact borrower disposable income in ways not captured in 10-year historical training data.
3. **Data Quality Flaws:** Temporary latency in third-party credit bureau feeds.

> **Barclays QA Monitoring Role in PMAs:**  
> QA Model Monitoring conducts quarterly audits on all active PMAs. The regulatory standard (PRA SS1/23) requires that PMAs must have an **explicit sunset clause**: a bank cannot carry a PMA indefinitely. If a model requires a persistent PMA for more than 4 consecutive quarters, Risk QA mandates a formal model recalibration or rebuild.

---

### 6. Fully Worked Numerical Calculation: Stage 1 vs. Stage 2 ECL

Consider a fixed-rate unsecured personal loan facility with the following specifications:
- **Origination Balance:** $EAD_0 = \$10,000$
- **Term:** 3 years ($T = 3$ annual evaluation periods)
- **Effective Interest Rate:** $\text{EIR} = 8.0\%$ p.a.
- **Amortizing EAD Profile at Start of Years:**
  - Year 1: $EAD_1 = \$10,000$
  - Year 2: $EAD_2 = \$6,800$
  - Year 3: $EAD_3 = \$3,500$
- **Loss Given Default:** $\text{LGD} = 55.0\%$ across all periods.

Let the conditional marginal default hazard rates $h_t$ be evaluated under two distinct credit states:
- **Scenario A (Performing — Stage 1):** Annual hazard rates remain low: $h_1 = 1.5\%$, $h_2 = 2.0\%$, $h_3 = 2.5\%$.
- **Scenario B (Deteriorated — Stage 2 SICR):** Macro-shock causes elevated hazards: $h_1 = 4.0\%$, $h_2 = 6.0\%$, $h_3 = 7.5\%$.

---

#### Step 1: Compute Survival Probabilities and Marginal Default Probabilities

##### Under Performing State (Stage 1):
- $S_0 = 1.0000$
- Period 1:
  $$d_1 = S_0 \times h_1 = 1.0000 \times 0.015 = \mathbf{0.0150} \quad (1.50\%)$$
  $$S_1 = S_0 \times (1 - h_1) = 1.0000 \times 0.985 = 0.9850$$
- Period 2:
  $$d_2 = S_1 \times h_2 = 0.9850 \times 0.020 = \mathbf{0.0197} \quad (1.97\%)$$
  $$S_2 = S_1 \times (1 - h_2) = 0.9850 \times 0.980 = 0.9653$$
- Period 3:
  $$d_3 = S_2 \times h_3 = 0.9653 \times 0.025 = \mathbf{0.0241} \quad (2.41\%)$$
  $$S_3 = S_2 \times (1 - h_3) = 0.9653 \times 0.975 = 0.9412$$

Lifetime Default Probability $\text{PD}_{\text{Lifetime}} = 1 - S_3 = 1 - 0.9412 = \mathbf{5.88\%}$.

##### Under Deteriorated State (Stage 2):
- $S_0 = 1.0000$
- Period 1:
  $$d_1 = 1.0000 \times 0.040 = \mathbf{0.0400} \quad (4.00\%)$$
  $$S_1 = 1.0000 \times 0.960 = 0.9600$$
- Period 2:
  $$d_2 = 0.9600 \times 0.060 = \mathbf{0.0576} \quad (5.76\%)$$
  $$S_2 = 0.9600 \times 0.940 = 0.9024$$
- Period 3:
  $$d_3 = 0.9024 \times 0.075 = \mathbf{0.0677} \quad (6.77\%)$$
  $$S_3 = 0.9024 \times 0.925 = 0.8347$$

Lifetime Default Probability $\text{PD}_{\text{Lifetime}} = 1 - 0.8347 = \mathbf{16.53\%}$.

---

#### Step 2: Discount Factor Evaluation ($\text{EIR} = 8\%$)
- Discount factor Year 1: $DF_1 = \frac{1}{(1 + 0.08)^1} = 0.9259$
- Discount factor Year 2: $DF_2 = \frac{1}{(1 + 0.08)^2} = 0.8573$
- Discount factor Year 3: $DF_3 = \frac{1}{(1 + 0.08)^3} = 0.7938$

---

#### Step 3: ECL Calculation

##### Stage 1 Provision (Performing Account — 12-Month ECL):
In Stage 1, the bank is legally required to provision **only for Period 1** ($t = 1$):
$$\text{ECL}_{\text{Stage 1}} = \frac{d_1 \times \text{LGD} \times EAD_1}{(1 + \text{EIR})^1} = 0.0150 \times 0.55 \times \$10,000 \times 0.9259 = \mathbf{\$76.39}$$

##### Stage 2 Provision (Deteriorated Account — Lifetime ECL):
When SICR is triggered, the account transitions to Stage 2, requiring discounting over the **entire 3-year lifetime**:
- Year 1 Loss:
  $$\text{Loss}_1 = 0.0400 \times 0.55 \times \$10,000 \times 0.9259 = \$203.70$$
- Year 2 Loss:
  $$\text{Loss}_2 = 0.0576 \times 0.55 \times \$6,800 \times 0.8573 = \$184.66$$
- Year 3 Loss:
  $$\text{Loss}_3 = 0.0677 \times 0.55 \times \$3,500 \times 0.7938 = \$103.45$$

$$\text{ECL}_{\text{Stage 2}} = \text{Loss}_1 + \text{Loss}_2 + \text{Loss}_3 = \$203.70 + \$184.66 + \$103.45 = \mathbf{\$491.81}$$

##### Quantitative Finding for Interview:
$$\text{Provisional Increase} = \frac{\$491.81}{\$76.39} = \mathbf{6.44\times} \quad (+544\%)$$
Transitioning from Stage 1 to Stage 2 causes the credit impairment provision to multiply by **6.44 times**. This demonstrates why precise calibration of SICR triggers and monthly monitoring of staging migration matrices is a high-priority risk management task in Barclays QA.

---

### 7. Comparison: IFRS 9 ECL vs. Basel III IRB Regulatory Capital

| Dimension | IFRS 9 ECL | Basel III IRB Capital |
| :--- | :--- | :--- |
| **Primary Purpose** | Financial accounting loan-loss provisioning on balance sheet / P&L. | Prudential capital buffer against catastrophic unexpected losses (UL). |
| **Loss Horizon** | 12 months (Stage 1) or Full Lifetime (Stage 2 & 3). | Fixed 12-month horizon for all performing assets. |
| **Probability of Default (PD)** | Point-in-Time (PIT), forward-looking, multi-scenario conditioned. | Through-the-Cycle (TTC) or conservative hybrid. |
| **Loss Given Default (LGD)** | PIT economic loss including future recovery forecasts. | Downturn LGD reflecting worst economic distress in 10+ years. |
| **Macro Conditioning** | Probability-weighted across Baseline, Upside, Downside scenarios. | Single severe stress condition embedded into regulatory formula. |
| **Discounting Rate** | Contractual Effective Interest Rate (EIR). | Contractual interest rate or regulatory zero floor. |
| **P&L Impact** | Direct charge to quarterly Income Statement (Provision for Credit Losses). | Regulatory capital deduction; does not flow through accounting P&L. |

---

*Authoritative cross-reference: IFRS 9 Financial Instruments (IASB, 2014); Bank of England Prudential Regulation Authority (PRA) Supervisory Statement SS1/23; European Banking Authority (EBA) Guidelines on Credit Risk Management Practices and Accounting for Expected Credit Losses.*

