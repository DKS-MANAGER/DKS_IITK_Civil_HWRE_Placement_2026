# 02. Analytics: Required Skills & Competencies

> Comprehensive competency framework, skill hierarchy, and pre-interview technical benchmarks for Analytics and Decision Science placements.

---

## 1. Technical Competency Breakdown

```text
                        ┌──────────────────────────────────────────────┐
                        │          ANALYTICS CORE SKILL STACK          │
                        └──────────────────────┬───────────────────────┘
                                               │
        ┌──────────────────────┬───────────────┴───────────────┬──────────────────────┐
        │                      │                               │                      │
 ┌──────▼──────┐        ┌──────▼──────┐                 ┌──────▼──────┐        ┌──────▼──────┐
 │     SQL     │        │    PYTHON   │                 │  STATISTICS │        │  BUSINESS   │
 │ (CTEs, Window│       │ (Pandas,    │                 │ (A/B Tests, │        │ (AARRR,     │
 │  Functions) │        │  NumPy, EDA)│                 │  Hypothesis)│        │  KPI Trees) │
 └─────────────┘        └─────────────┘                 └─────────────┘        └─────────────┘
```

### Pre-Interview Technical Checklist
| Competency Area | Priority | Specific Capabilities Tested | Placement Verification Benchmark |
|:---|:---:|:---|:---|
| **SQL Data Querying** | **P0** | Multi-table `JOIN`s, `GROUP BY / HAVING`, CTEs (`WITH`), Window functions (`ROW_NUMBER`, `DENSE_RANK`, `LAG`, `LEAD`, `SUM() OVER(PARTITION BY)`), Date intervals, Cohort retention queries. | Solve Hard HackerRank/LeetCode SQL problems in <10 mins with zero syntax errors. |
| **Python & Pandas** | **P0** | Vectorized operations in NumPy, Pandas `groupby()`, `merge()`, `pivot_table()`, `apply()`, lambda functions, missing value imputation, datetime manipulations. | Clean, merge, and aggregate a 500k-row dataframe in <15 mins. |
| **Applied Statistics & A/B Tests**| **P0**| Sample size calculation ($N pprox rac{16\sigma^2}{\Delta^2}$), MDE, Statistical Power ($1-eta=80\%$), Type I/II errors, Two-sample t-test, Chi-Square test for SRM, Simpson's Paradox. | Formulate null hypothesis and calculate required sample size in <90s. |
| **Machine Learning Fundamentals**| **P1**| Linear & Logistic Regression, Decision Trees, Random Forests, XGBoost, Cross-Validation (K-Fold), ROC-AUC, Precision-Recall curve, Confusion Matrix, SHAP values. | Explain precision vs recall trade-off and train a classifier in scikit-learn. |
| **Business Metrics & Funnels** | **P0**| Pirate Metrics (AARRR: Acquisition, Activation, Retention, Revenue, Referral), $CAC$, $LTV$, Churn rate, North Star metric trees, Funnel drop-off diagnosis. | Build a mathematical driver tree for a metric decline in 90 seconds. |
| **Data Visualization & BI** | **P1**| Power BI / Tableau dashboards, chart selection (scatter, bar, line, waterfall, cohort heatmaps), executive storytelling. | Design a clean executive dashboard layout from a raw dataset in 20 mins. |

---

## 2. The 3-Tier Placement Readiness Ladder

```text
TIER 1: OA & CODING SCREEN READY
├── Flawless SQL: Solves multi-table joins, subqueries, and window ranking queries in <8 mins.
├── Rapid Python wrangling: Performs Pandas data cleaning, reshaping, and aggregations effortlessly.
└── Fast quantitative probability: Solves Bayes' theorem, permutations, and expected value math in <60s.

TIER 2: TECHNICAL ROUND READY
├── Can write clean, modular Pandas & SQL code live on Coderpad while explaining algorithmic logic out loud.
├── Designs statistically sound A/B tests with sample size, MDE, primary/guardrail metrics, and SRM checks.
└── Evaluates ML models using appropriate metrics (ROC-AUC for imbalanced data, RMSE/MAE for regression).

TIER 3: CASE & OFFER READY
├── Diagnoses metric drops (e.g. 12% drop in DAU or 150 bps drop in conversion) using structured MECE cuts.
├── Seamlessly bridges Civil/HWRE predictive modeling (BridgeRisk / Streamflow telemetry) to commercial analytics.
└── Confidently defends statistical and business trade-offs under tough interviewer pushback.
```
