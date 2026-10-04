# 02. Risk Analyst: Required Skills & Competencies

> Comprehensive competency framework, skill priority hierarchy, and technical evaluation benchmarks for Risk Management placements.

---

## 1. Technical Competency Breakdown

```text
                        ┌──────────────────────────────────────────────┐
                        │            RISK ANALYST SKILL STACK          │
                        └──────────────────────┬───────────────────────┘
                                               │
        ┌──────────────────────┬───────────────┴───────────────┬──────────────────────┐
        │                      │                               │                      │
 ┌──────▼──────┐        ┌──────▼──────┐                 ┌──────▼──────┐        ┌──────▼──────┐
 │ CREDIT RISK │        │ MARKET RISK │                 │ QUANT & ML  │        │  SQL & DATA │
 │ (PD, LGD,   │        │ (VaR, CVaR, │                 │ (Logistic,  │        │ (Cohorts,   │
 │  Scorecards)│        │  Volatility)│                 │  Monte Carlo│        │  Roll Rates)│
 └─────────────┘        └─────────────┘                 └─────────────┘        └─────────────┘
```

### Pre-Interview Technical Checklist
| Competency Area | Priority | Specific Capabilities Tested | Placement Verification Benchmark |
|:---|:---:|:---|:---|
| **Credit Risk Modeling** | **P0** | Probability of Default ($PD$), Loss Given Default ($LGD$), Exposure at Default ($EAD$), Expected Credit Loss ($ECL$), Weight of Evidence ($WoE$), Information Value ($IV$), KS Statistic, Gini Coefficient, ROC-AUC, Population Stability Index ($PSI$). | Build and evaluate a complete credit scorecard in Python in <30 mins. |
| **Market Risk & Portfolios** | **P0** | Parametric VaR, Historical Simulation VaR, Monte Carlo VaR, Expected Shortfall ($ES / CVaR$), Volatility scaling ($\sqrt{t}$ rule), Greeks ($\Delta, \Gamma, \Theta, 	ext{Vega}$), Correlation breakdown. | Calculate 1-day and 10-day 99% portfolio VaR given covariance matrix in <5 mins. |
| **Probability & Distributions**| **P0** | Bayes' theorem, Poisson processes, Normal, Log-normal, Binomial, Extreme Value distributions (Gumbel/GEV), Central Limit Theorem, Hypothesis testing. | Solve conditional probability and distribution problems mentally in <90s. |
| **SQL & Portfolio Analytics** | **P0** | Window functions, CTEs, multi-table joins, delinquency vintage tracking, roll-rate migration matrices, customer risk bucketing. | Write a delinquency cohort migration query in <10 mins with zero syntax errors. |
| **Machine Learning & Python** | **P1** | Logistic regression, XGBoost / LightGBM for classification, feature binning, handling imbalanced datasets (SMOTE, Class Weights), SHAP explainability. | Train and evaluate an imbalanced default classifier in Python/scikit-learn. |
| **Regulatory & Governance** | **P1** | Basel II/III framework, Capital Adequacy Ratio ($CAR$), Risk-Weighted Assets ($RWA$), Three Lines of Defense, Model Risk Management (SR 11-7). | Explain Basel III Tier 1 capital requirements and stress-testing mandates. |

---

## 2. The 3-Tier Placement Readiness Ladder

```text
TIER 1: OA & SCREENING READY
├── Flawless quantitative probability: Solves Bayes' theorem, combinatorics, and normal distribution math in <60s.
├── Solid SQL fundamentals: Writes joins, aggregations, and basic window functions.
└── High numerical accuracy: Calculates expected values, variances, and bond yields with zero paper mistakes.

TIER 2: TECHNICAL ROUND READY
├── Can mathematically derive and explain WoE, Information Value, and Logistic Regression log-odds.
├── Calculates Parametric VaR, Historical VaR, and Expected Shortfall while explaining trade-offs out loud.
└── Interprets Model Performance Metrics: KS curve separation, Gini $= 2 	imes 	ext{AUC} - 1$, and PSI thresholds ($<0.1$ stable).

TIER 3: CASE & PARTNER READY
├── Solves complex portfolio trade-off cases: Balances approval rate vs credit loss provisioning under macroeconomic shocks.
├── Seamlessly bridges Civil/HWRE uncertainty modeling (BridgeRisk / flood extremes) to financial risk modeling.
└── Displays calm executive judgment under tough interviewer pushback.
```
