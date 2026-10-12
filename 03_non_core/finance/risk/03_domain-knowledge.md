# 03. Risk Analytics: Credit Risk, Market Risk, Portfolio Theory & Basel Governance

> **Scope**: Master reference textbook covering Credit Risk Modeling, Scorecard Engineering, Loss Provisioning, Market Risk (VaR & Expected Shortfall), Fixed Income Greeks, and Basel III Regulatory Capital Governance for quantitative campus placements. `[PREPARATION HEURISTIC]`

---

## 1. Credit Risk Foundations & Mathematical Formulations

Credit risk is the risk of economic financial loss resulting from a counterparty or borrower failing to meet their contractual debt obligations (repayment of principal or interest).

```text
                             CREDIT LOSS MODELING PIPELINE
┌─────────────────────────┐     ┌─────────────────────────┐     ┌─────────────────────────┐
│     PROBABILITY OF      │     │       EXPOSURE AT       │     │       LOSS GIVEN        │
│      DEFAULT (PD)       │  ×  │      DEFAULT (EAD)      │  ×  │      DEFAULT (LGD)      │
│  (Scorecard / Logistic) │     │ (Drawn + CCF × Undrawn) │     │   (1 - Recovery Rate)   │
└─────────────────────────┘     └─────────────────────────┘     └─────────────────────────┘
                                             │
                                             ▼
                                ┌───────────────────────────┐
                                │   EXPECTED LOSS (EL)      │
                                │   EL = PD × EAD × LGD     │
                                └─────────────┬─────────────┘
                                              │ (Covered by Accounting Provisions)
                                              ▼
                                ┌───────────────────────────┐
                                │  UNEXPECTED LOSS (UL)     │
                                │  Volatility of Losses     │
                                └───────────────────────────┘
                                  (Covered by Regulatory Equity Capital)
```

---

### 1.1 Expected Loss ($EL$) vs. Unexpected Loss ($UL$)

#### A. Expected Loss ($EL$)
The anticipated statistical mean credit loss of a portfolio over a 1-year planning horizon:
$$EL = PD \times LGD \times EAD$$

* **Components**:
  1. **Probability of Default ($PD$)**: The calibrated likelihood that a borrower defaults within a 1-year window (typically defined under Basel as 90+ days past due or bankruptcy).
  2. **Loss Given Default ($LGD$)**: The percentage of exposure lost if default occurs:
     $$LGD = 1 - \text{Recovery Rate} = \frac{\text{Defaulted Balance} - \text{Net Recoveries}}{\text{Defaulted Balance}}$$
     * *Downturn LGD Nuance*: During macroeconomic recessions, asset values drop simultaneously with defaults, suppressing collateral recoveries. Regulators enforce using **Downturn LGD** ($LGD_{\text{downturn}} > LGD_{\text{mean}}$).
  3. **Exposure at Default ($EAD$)**: The gross nominal obligation owed by the borrower at the precise moment of default:
     $$EAD = \text{Drawn Balance} + \left(\text{Credit Conversion Factor (CCF)} \times \text{Undrawn Credit Limit}\right)$$
     * *CCF*: Fraction of unutilized revolving lines of credit drawn down by a distressed borrower prior to default (typically $50\% - 75\%$ for corporate credit lines).
* **Accounting Treatment**: Expected Losses are recognized on the Income Statement as **Credit Impairment Provisions** (IFRS 9 / CECL / RBI ECL Framework) and held as balance sheet loan loss reserves.

#### B. Unexpected Loss ($UL$)
The statistical standard deviation of portfolio credit losses around the expected loss:
$$UL = EAD \times \sqrt{PD \times \sigma_{LGD}^2 + LGD^2 \times \sigma_{PD}^2}$$
* **Capital Protection**: Unexpected Losses cannot be covered by ongoing operating earnings. They must be absorbed by **Equity Capital Reserves (Economic Capital & Regulatory Capital)**.

---

### 1.2 Credit Scorecard Engineering: WoE & Information Value

To predict borrower default probability, retail credit scorecards transform raw applicant features into linear log-odds inputs using **Weight of Evidence (WoE)** binning:

#### A. Weight of Evidence (WoE)
For continuous or categorical feature bin $i$:
$$WoE_i = \ln \left( \frac{\% \text{ Non-Defaulters (Goods)}_i + \epsilon}{\% \text{ Defaulters (Bads)}_i + \epsilon} \right) = \ln \left( \frac{G_i / G_{\text{total}} + \epsilon}{B_i / B_{\text{total}} + \epsilon} \right)$$

* **Mathematical Properties**:
  * $\epsilon = 0.0001$: Laplace smoothing parameter to eliminate division by zero.
  * $WoE_i > 0$: Bin has a higher concentration of Good customers relative to the overall population $\implies$ **Low Risk**.
  * $WoE_i < 0$: Bin has a higher concentration of Bad customers $\implies$ **High Risk**.
  * Replaces raw feature values with monotonically sorted log-odds scores, linearizing non-linear relationships for Logistic Regression.

#### B. Information Value (IV)
Quantifies the overall discriminatory power of a feature across all $k$ bins:
$$IV = \sum_{i=1}^{k} \left( \frac{G_i}{G_{\text{total}}} - \frac{B_i}{B_{\text{total}}} \right) \times WoE_i$$

| Information Value ($IV$) | Predictive Power Interpretation & Action Rule |
| :---: | :--- |
| $< 0.02$ | **Unpredictable / Useless** $\implies$ Drop feature immediately. |
| $0.02 - 0.10$ | **Weak Predictor** $\implies$ Secondary feature; include only if complementary. |
| $0.10 - 0.30$ | **Medium Predictor** $\implies$ Standard scorecard inclusion. |
| $0.30 - 0.50$ | **Strong Predictor** $\implies$ Core scorecard driver (e.g., Credit Bureau Score, DTI). |
| $> 0.50$ | **Suspiciously High** $\implies$ Check for data leakage, forward-looking variables, or extreme overfitting. |

---

### 1.3 Scorecard Discrimination & Calibration Metrics

```text
 ┌────────────────────────────────────────────────────────┐
 │            KOLMOGOROV-SMIRNOV (KS) SEPARATION          │
 ├────────────────────────────────────────────────────────┤
 │  Cumulative %                                          │
 │  100% ┼                                   ┌─── F_Bad   │
 │       │                                 ┌─┘            │
 │       │                       ▲       ┌─┘              │
 │       │                 KS ───┼───► ┌─┘                │
 │       │                       ▼   ┌─┘                  │
 │       │                         ┌─┘                    │
 │       │                       ┌─┘                      │
 │       │                     ┌─┘ ◄────── F_Good         │
 │    0% ┼─────────────────────┴────────────────────────  │
 │       Lowest Risk Score                 Highest Risk   │
 └────────────────────────────────────────────────────────┘
```

#### A. Kolmogorov-Smirnov (KS) Statistic
Measures the maximum vertical separation between the empirical cumulative distribution functions of Good borrowers ($F_{\text{Good}}$) and Bad borrowers ($F_{\text{Bad}}$):
$$KS = \max_{s} |F_{\text{Good}}(s) - F_{\text{Bad}}(s)|$$
* **Benchmark Target**: $KS \ge 40\% - 45\%$, achieved within the top 3 deciles of scores, indicates an excellent credit underwriting model. A $KS < 30\%$ model requires retraining.

#### B. ROC-AUC and the Gini Coefficient
* **Receiver Operating Characteristic (ROC-AUC)**: Area under the True Positive Rate vs False Positive Rate curve.
* **Gini Coefficient (Accuracy Ratio)**:
  $$\text{Gini} = 2 \times \text{AUC} - 1$$
  * *Benchmark*: $\text{AUC} \ge 0.75 \implies \text{Gini} \ge 0.50$ for application scorecards.

#### C. Population Stability Index (PSI)
Monitors whether the underlying applicant credit distribution has drifted between the development baseline ($E_i$) and the current active production pipeline ($A_i$):
$$PSI = \sum_{i=1}^k (A_i - E_i) \times \ln \left( \frac{A_i + \epsilon}{E_i + \epsilon} \right)$$

| PSI Score Range | Population Drift Interpretation | Required Governance Action |
| :---: | :--- | :--- |
| **$PSI < 0.10$** | **Stable Population** | No changes required; continue standard monitoring. |
| **$0.10 \le PSI < 0.25$** | **Moderate Shift** | Investigate origin channels, credit policies, or macroeconomic shifts. |
| **$PSI \ge 0.25$** | **Significant Drift** | **Halt automatic approvals; recalibrate or rebuild model immediately.** |

---

### 1.4 Vintage Analysis & Roll Rate Transition Matrices
* **Vintage Analysis (Cohort Curves)**: Tracks cumulative defaults of loans originated in a specific cohort month (e.g., January 2025) as they season over $6, 12, 18, 24$ months. Upward-shifting vintage curves signal deteriorating underwriting quality.
* **Roll Rate Matrix**: Probability of an account transitioning across delinquency states over a 30-day billing cycle:
  $$\begin{bmatrix}
  P_{\text{Current} \to \text{Current}} & P_{\text{Current} \to 30} & 0 & 0 \\
  P_{30 \to \text{Current}} & P_{30 \to 30} & P_{30 \to 60} & 0 \\
  0 & P_{60 \to 30} & P_{60 \to 60} & P_{60 \to 90} \\
  0 & 0 & 0 & P_{90 \to \text{Default}}
  \end{bmatrix}$$

---

## 2. Market Risk, Value at Risk (VaR) & Portfolio Analytics

Market risk is the potential reduction in portfolio value resulting from adverse movements in financial market asset prices, interest rates, currency exchange rates, and commodity prices.

### 2.1 Value at Risk (VaR) Methodologies

$$\text{VaR}_{\alpha} = \text{Maximum monetary loss not exceeded with confidence level } 1 - \alpha \text{ over time horizon } T$$

```text
                                PARAMETRIC VAR SPECTRUM
 ┌────────────────────────────────────────────────────────────────────────┐
 │                                                                        │
 │  Normal Distribution: μ = 0, σ                                         │
 │       │                                                                │
 │       │                  ┌──────────┐                                  │
 │       │                ┌─┘          └─┐                                │
 │       │              ┌─┘              └─┐                              │
 │       │            ┌─┘                  └─┐                            │
 │       │          ┌─┘                      └─┐                          │
 │       └──────────┴──────────────────────────┴────────┬─────────────>   │
 │                  │ <──── 99% Normal Outcomes ─────-> │ 1% Tail     │   │
 │                                                      ▲                 │
 │                                                  99% 1-Day VaR         │
 │                                                  Threshold (Z=2.326)   │
 └────────────────────────────────────────────────────────────────────────┘
```

#### A. Parametric (Variance-Covariance) VaR
Assumes continuous asset returns follow a normal distribution $R \sim \mathcal{N}(\mu, \sigma^2)$:
$$\text{VaR}_{\alpha} = Z_{\alpha} \times \sigma_p \times V_p$$
* Where $V_p$ is portfolio market value, $\sigma_p$ is daily return volatility, and $Z_{\alpha}$ is the standard normal critical value:
  * $95\%$ 1-tailed confidence: $Z_{0.05} = 1.645$.
  * $99\%$ 1-tailed confidence: $Z_{0.01} = 2.326$.

#### B. Portfolio VaR with Correlation:
For a 2-asset portfolio:
$$\sigma_p = \sqrt{w_1^2 \sigma_1^2 + w_2^2 \sigma_2^2 + 2 w_1 w_2 \rho_{12} \sigma_1 \sigma_2}$$
$$\text{VaR}_p = \sqrt{\text{VaR}_1^2 + \text{VaR}_2^2 + 2 \rho_{12} \text{VaR}_1 \text{VaR}_2}$$

#### C. Historical Simulation VaR
Applies the exact historical percentage price movements of market factors over the past $N$ trading days (typically $N = 250$ to $500$ days) to today's portfolio.
* **Advantage**: Makes **zero distribution assumptions**; naturally incorporates fat tails, skewness, and non-linear derivative payouts.
* **Method**: Sort the $N$ simulated dollar profit/loss changes from worst to best. For 250 days at 99% confidence, the 99% VaR is the **3rd worst historical loss** ($250 \times 1\% = 2.5$).

#### D. Monte Carlo Simulation VaR
Generates tens of thousands of random price paths using Geometric Brownian Motion with correlated Wiener processes:
$$S_{t + \Delta t} = S_t \exp\left( \left(\mu - \frac{\sigma^2}{2}\right)\Delta t + \sigma \sqrt{\Delta t} \epsilon \right)$$
* Optimal for complex multi-asset derivatives portfolios with path dependency.

---

### 2.2 Time Horizon Scaling ($\sqrt{T}$ Rule) & Limitations
$$\text{VaR}_{T\text{-day}} = \text{VaR}_{1\text{-day}} \times \sqrt{T}$$
* **The Basel 10-Day Horizon**: $\text{VaR}_{10\text{d}} = \text{VaR}_{1\text{d}} \times \sqrt{10} \approx 3.162 \times \text{VaR}_{1\text{d}}$.
* **Fatal Theoretical Flaws**:
  * Assumes daily returns are **independent and identically distributed (i.i.d.)**.
  * During real market crises, financial returns exhibit **volatility clustering** (autocorrelation of variance) and structural jumps, causing multi-day losses to drastically exceed $\sqrt{T}$ predictions.

---

### 2.3 Expected Shortfall (Conditional VaR - CVaR)
Value at Risk tells you *how often* you lose, but tells you *nothing about how bad the loss will be* once the threshold is breached.
**Expected Shortfall (ES)** is the conditional expectation of losses exceeding the VaR cutoff:
$$\text{ES}_{\alpha} = \mathbb{E}[L \mid L > \text{VaR}_{\alpha}]$$

* **Why Regulators (Basel III) Replaced VaR with Expected Shortfall**:
  * **Coherent Risk Measure**: Expected Shortfall satisfies **Subadditivity**:
    $$\text{ES}(X + Y) \le \text{ES}(X) + \text{ES}(Y)$$
    The risk of a combined portfolio is always less than or equal to the sum of individual risks (diversification is respected). VaR can violate subadditivity for fat-tailed non-normal distributions.

---

### 2.4 Fixed Income Duration, Convexity & Option Greeks
* **Modified Duration & Convexity Approximation**:
  $$\% \Delta P \approx -D_{\text{mod}} \times \Delta y + \frac{1}{2} C \times (\Delta y)^2$$
  * Duration provides a linear first-order approximation; **Convexity ($C$)** accounts for curvature, ensuring price drops less when yields rise and gains more when yields fall.
* **The Option Greeks**:
  * **Delta ($\Delta$)**: First derivative of option price with respect to underlying asset price: $\frac{\partial V}{\partial S}$.
  * **Gamma ($\Gamma$)**: Second derivative; rate of change of Delta: $\frac{\partial^2 V}{\partial S^2}$.
  * **Vega ($\nu$)**: Sensitivity to implied volatility: $\frac{\partial V}{\partial \sigma}$.
  * **Theta ($\Theta$)**: Sensitivity to passage of time (time decay): $\frac{\partial V}{\partial t}$.
  * **Rho ($\rho$)**: Sensitivity to interest rate: $\frac{\partial V}{\partial r}$.

---

### 2.5 VaR Backtesting & The Basel Traffic Light System
To validate model accuracy, internal models must be backtested over the preceding 250 trading days at the 99% confidence level:
* Expected breaches per year: $250 \times (1 - 0.99) = 2.5$ days.
* **The Basel Zones**:
  * **Green Zone (0–4 exceptions)**: Model accepted; standard regulatory multiplier $k = 3.0$.
  * **Yellow Zone (5–9 exceptions)**: Supervisory scrutiny triggered; regulatory capital multiplier increases incrementally from $3.40$ to $3.85$.
  * **Red Zone ($\ge 10$ exceptions)**: Model rejected; immediate regulatory penalty.

---

## 3. Regulatory Capital Frameworks: Basel III & RBI Guidelines

### 3.1 The Capital to Risk-Weighted Assets Ratio (CRAR)
Commercial banks must hold sufficient equity capital to absorb unexpected losses across three distinct risk pillars:
$$\text{CRAR} = \frac{\text{Eligible Capital (Tier 1 + Tier 2)}}{\text{Total Risk-Weighted Assets (RWA)}}$$

$$\text{Total RWA} = \text{Credit Risk RWA} + \text{Market Risk RWA} + \text{Operational Risk RWA}$$

#### A. Capital Tiers
1. **Common Equity Tier 1 (CET1)**: Pure loss-absorbing capital (Common shares, share premium, audited retained earnings).
2. **Additional Tier 1 (AT1)**: Perpetual non-cumulative preferred stock, contingent convertible (CoCo) bonds.
3. **Tier 2 Capital**: Subordinated term debt (maturity $\ge 5$ years), general loan loss provisions (up to 1.25% of credit RWA).

#### B. Regulatory Minimum Thresholds (Basel III vs. RBI Mandates)

| Capital Ratio Component | Basel III International Minimum | Reserve Bank of India (RBI) Mandate |
| :--- | :---: | :---: |
| **Minimum CET1 Ratio** | $4.50\%$ | **$5.50\%$** |
| **Minimum Tier 1 Capital** | $6.00\%$ | **$7.00\%$** |
| **Minimum Total Capital (CRAR)** | $8.00\%$ | **$9.00\%$** |
| **Capital Conservation Buffer (CCB)** | $2.50\%$ (CET1) | **$2.50\%$ (CET1)** |
| **Total Minimum CRAR including CCB** | **$10.50\%$** | **$11.50\%$** |

---

### 3.2 Liquidity Metrics: LCR and NSFR
To prevent liquidity runs during systemic bank panics:
1. **Liquidity Coverage Ratio (LCR)**:
   $$\text{LCR} = \frac{\text{High-Quality Liquid Assets (HQLA)}}{\text{Total Net Cash Outflows over 30-Day Stress Period}} \ge 100\%$$
   * HQLA consists of cash, central bank reserves, and unencumbered sovereign government bonds.
2. **Net Stable Funding Ratio (NSFR)**:
   $$\text{NSFR} = \frac{\text{Available Stable Funding (ASF)}}{\text{Required Stable Funding (RSF)}} \ge 100\%$$
   * Enforces structural 1-year liquidity balance, limiting over-reliance on volatile short-term wholesale funding to finance illiquid long-term assets.
