# 03. Risk Analyst: Comprehensive Domain Knowledge & Mathematical Foundations

> Complete mathematical formulations, regulatory frameworks, and analytical methodologies across Credit Risk, Market Risk, Operational Risk, and Model Governance.

---

## 1. Credit Risk Foundations & Mathematical Formulations

Credit risk is the risk of economic loss resulting from a borrower's failure to repay a loan or meet contractual debt obligations.

```text
                             CREDIT RISK FORMULATION PIPELINE
┌─────────────────────────┐     ┌─────────────────────────┐     ┌─────────────────────────┐
│     PROBABILITY OF      │     │       EXPOSURE AT       │     │       LOSS GIVEN        │
│      DEFAULT (PD)       │  ×  │      DEFAULT (EAD)      │  ×  │      DEFAULT (LGD)      │
│  (Scorecard / Logistic) │     │ (Drawn + Factor × Undr.)│     │   (1 - Recovery Rate)   │
└─────────────────────────┘     └─────────────────────────┘     └─────────────────────────┘
                                             │
                                             ▼
                               ┌───────────────────────────┐
                               │   EXPECTED LOSS (EL)      │
                               │   EL = PD × EAD × LGD     │
                               └───────────────────────────┘
```

### 1. Expected Loss ($EL$) vs. Unexpected Loss ($UL$)
- **Expected Loss ($EL$)**: Anticipated average credit loss over a 1-year horizon. Covered via **provisions and product pricing**:
  $$EL = PD 	imes LGD 	imes EAD$$
- **Unexpected Loss ($UL$)**: Standard deviation / volatility of losses around the expected loss. Covered via **equity capital reserves (Regulatory & Economic Capital)**:
  $$UL = EAD 	imes \sqrt{PD 	imes \sigma_{LGD}^2 + LGD^2 	imes \sigma_{PD}^2}$$

### 2. Credit Scorecards, Weight of Evidence (WoE) & Information Value (IV)
To transform non-linear continuous and categorical features into monotonic linear inputs for logistic regression:

- **Weight of Evidence (WoE)**:
  $$WoE_i = \ln \left( rac{\% 	ext{ Non-Defaulters (Goods)}_i}{\% 	ext{ Defaulters (Bads)}_i} ight) = \ln \left( rac{G_i / G_{	ext{total}}}{B_i / B_{	ext{total}}} ight)$$
  - $WoE > 0 \implies$ Category has higher concentration of good customers (low risk).
  - $WoE < 0 \implies$ Category has higher concentration of bad customers (high risk).

- **Information Value (IV)**: Measures the overall predictive power of a feature:
  $$IV = \sum_{i=1}^{k} \left( rac{G_i}{G_{	ext{total}}} - rac{B_i}{B_{	ext{total}}} ight) 	imes WoE_i$$

| Information Value ($IV$) | `[PREPARATION HEURISTIC]` Predictive Power Interpretation |
|:---:|:---|
| $< 0.02$ | Unpredictable / Useless (Drop feature) |
| $0.02 - 0.10$ | Weak predictive power |
| $0.10 - 0.30$ | Medium predictive power (Standard scorecard inclusion) |
| $0.30 - 0.50$ | Strong predictive power (Core scorecard feature) |
| $> 0.50$ | Suspiciously high (Check for data leakage or overfitting) |

### 3. Scorecard Model Discrimination & Calibration Metrics
- **Kolmogorov-Smirnov (KS) Statistic**: Maximum vertical separation between cumulative Good and cumulative Bad distributions:
  $$KS = \max |F_{	ext{Good}}(s) - F_{	ext{Bad}}(s)|$$
  - Target placement benchmark: $KS \ge 35\% - 45\%$ in Top 3 deciles.
- **Gini Coefficient & ROC-AUC**:
  $$	ext{Gini} = 2 	imes AUC - 1$$
  - Target benchmark: $AUC \ge 0.75 \implies 	ext{Gini} \ge 0.50$.
- **Population Stability Index (PSI)**: Monitors population drift over time:
  $$PSI = \sum \left( \% 	ext{ Actual}_i - \% 	ext{ Expected}_i ight) 	imes \ln \left( rac{\% 	ext{ Actual}_i}{\% 	ext{ Expected}_i} ight)$$
  - $PSI < 0.10 \implies$ Stable population.
  - $0.10 \le PSI < 0.25 \implies$ Moderate drift; monitor closely.
  - $PSI \ge 0.25 \implies$ Significant drift; **recalibrate or rebuild model**.

---

## 2. Market Risk, Value at Risk (VaR) & Expected Shortfall

Market risk represents the potential loss in portfolio value due to movements in market factors (equity prices, interest rates, foreign exchange rates, commodity prices).

```text
                               VALUE AT RISK (VaR) SPECTRUM
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                         │
│  LOSS PROBABILITY DENSITY                                                               │
│       │                                                                                 │
│       │           ┌──────────┐                                                          │
│       │          ┌┘          └┐                                                         │
│       │        ┌─┘            └─┐                                                       │
│       │       ┌┘                └┐                                                      │
│       │     ┌─┘                  └─┐                                                    │
│       │   ┌─┘                      └─┐                                                  │
│       └───┴──────────────────────────┴─────────┬──────────────────────┬─────────────>   │
│           │ <── 99% Normal Outcomes ─────────> │   1% Tail Losses     │    Loss ($)     │
│                                                ▲                      ▲                 │
│                                           99% 1-Day VaR        Expected Shortfall       │
│                                           (Threshold)           (Average Tail Loss)     │
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

### 1. Parametric VaR (Variance-Covariance Method)
Assumes asset returns follow a normal distribution $R \sim \mathcal{N}(\mu, \sigma^2)$:
$$	ext{VaR}_{lpha} = Z_{lpha} 	imes \sigma_p 	imes V_p$$
- Where $V_p$ = Portfolio value, $\sigma_p$ = Portfolio standard deviation, $Z_{lpha}$ = Standard normal critical value:
  - $95\%$ Confidence ($1	ext{-tailed}$): $Z = 1.645$
  - $99\%$ Confidence ($1	ext{-tailed}$): $Z = 2.326$

### 2. Time Horizon Scaling ($\sqrt{t}$ Rule)
$$	ext{VaR}_{T	ext{-day}} = 	ext{VaR}_{1	ext{-day}} 	imes \sqrt{T}$$
- *10-day 99% VaR (Basel standard)*: $	ext{VaR}_{10	ext{d}} = 	ext{VaR}_{1	ext{d}} 	imes \sqrt{10} pprox 	ext{VaR}_{1	ext{d}} 	imes 3.162$.

### 3. Historical Simulation vs. Monte Carlo VaR
- **Historical Simulation**: Re-values current portfolio across the last $N$ days (e.g. 500 days) of historical market returns. No normality assumption; naturally captures fat tails and skewness.
- **Monte Carlo VaR**: Simulates thousands of price paths using stochastic differential equations (Geometric Brownian Motion: $dS_t = \mu S_t dt + \sigma S_t dW_t$). Captures non-linear derivative payouts.

### 4. Expected Shortfall ($ES$ / $CVaR$)
VaR is **not a coherent risk measure** because it violates sub-additivity ($	ext{VaR}(A+B) 
ot\le 	ext{VaR}(A) + 	ext{VaR}(B)$ under fat tails).
- **Expected Shortfall ($ES$)**: Average loss given that the loss exceeds VaR (coherent risk measure mandated by Basel III / FRTB):
  $$ES_{lpha} = \mathbb{E}[L \mid L > 	ext{VaR}_{lpha}]$$
  - For standard normal distribution: $ES_{99\%} pprox 2.665 	imes \sigma 	imes V_p$.

---

## 3. Regulatory Capital & Governance Frameworks

### 1. Basel III Framework & Capital Adequacy
- **Capital Adequacy Ratio (CAR)**:
  $$CAR = rac{	ext{Tier 1 Capital} + 	ext{Tier 2 Capital}}{	ext{Risk-Weighted Assets (RWA)}} \ge 8\% 	ext{ (RBI Mandate: } \ge 9\% + 2.5\% 	ext{ CCB = } 11.5\%)$$
- **Risk-Weighted Assets (RWA)**:
  $$	ext{Total RWA} = RWA_{	ext{Credit}} + RWA_{	ext{Market}} + RWA_{	ext{Operational}}$$

### 2. The Three Lines of Defense Governance Model
```text
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│ 1ST LINE: BUSINESS & REVENUE GENERATION                                                 │
│ • Front office, relationship managers, loan underwriting teams.                         │
│ • Owns and executes risk taking within approved limits.                                 │
├─────────────────────────────────────────────────────────────────────────────────────────┤
│ 2ND LINE: RISK MANAGEMENT & COMPLIANCE                                                  │
│ • Chief Risk Officer (CRO), Credit Risk, Market Risk, Model Validation teams.          │
│ • Sets risk policy, builds models, establishes limits, monitors risk independent of P&L.│
├─────────────────────────────────────────────────────────────────────────────────────────┤
│ 3RD LINE: INTERNAL AUDIT                                                                │
│ • Independent periodic evaluation of 1st and 2nd line controls for the Board of Direct. │
└─────────────────────────────────────────────────────────────────────────────────────────┘
```
