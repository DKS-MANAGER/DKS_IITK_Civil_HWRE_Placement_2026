# 01 — Topic Priority Matrix & Coverage Tracker
## Granular Discipline Weightage, Interview Frequency & Readiness Benchmarks

> **Document Status**: Operational Study Planning Matrix `[TIER 5 / PEDAGOGICAL PLAN]`

---

## 1. Master Priority Matrix

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              TREDENCE TOPIC PRIORITY & WEIGHTAGE MATRIX                                │
├─────────────────────┬──────────┬──────────────┬────────────────────────────┬───────────────────────────┤
│ Topic Domain        │ Priority │ OA Weight %  │ Tech Interview Weight %    │ Minimum Mastery Benchmark │
├─────────────────────┼──────────┼──────────────┼────────────────────────────┼───────────────────────────┤
│ **Advanced SQL**    │ **P0**   │ **25%**      │ **25%**                    │ Write error-free window   │
│                     │          │              │                            │ functions & CTEs in 3 min │
├─────────────────────┼──────────┼──────────────┼────────────────────────────┼───────────────────────────┤
│ **Python & Pandas** │ **P0**   │ **25%**      │ **20%**                    │ Fluent Pandas transforms, │
│                     │          │              │                            │ memory downcast, vectoriz.│
├─────────────────────┼──────────┼──────────────┼────────────────────────────┼───────────────────────────┤
│ **Statistics & A/B**│ **P0**   │ **20%**      │ **20%**                    │ Derive sample size & test │
│                     │          │              │                            │ statistics without notes  │
├─────────────────────┼──────────┼──────────────┼────────────────────────────┼───────────────────────────┤
│ **Core ML Models**  │ **P0**   │ **15%**      │ **20%**                    │ Explain loss math & splits│
│                     │          │              │                            │ for LightGBM / XGBoost    │
├─────────────────────┼──────────┼──────────────┼────────────────────────────┼───────────────────────────┤
│ **Time-Series**     │ **P1**   │ **5%**       │ **10%**                    │ Formulate SARIMA, rolling │
│                     │          │              │                            │ validation & WAPE metrics │
├─────────────────────┼──────────┼──────────────┼────────────────────────────┼───────────────────────────┤
│ **Business Cases**  │ **P1**   │ **0%**       │ **15%**                    │ Structure 10-step MECE    │
│                     │          │              │                            │ solution & the "Now What" │
├─────────────────────┼──────────┼──────────────┼────────────────────────────┼───────────────────────────┤
│ **GenAI & RAG**     │ **P2**   │ **5%**       │ **5%**                     │ Explain RAG Triad, hybrid │
│                     │          │              │                            │ search & agent loops      │
├─────────────────────┼──────────┼──────────────┼────────────────────────────┼───────────────────────────┤
│ **Deep Learning**   │ **P2**   │ **5%**       │ **5%**                     │ Explain CNN / Transformer │
│                     │          │              │                            │ attention mechanics       │
└─────────────────────┴──────────┴──────────────┴────────────────────────────┴───────────────────────────┘
```

---

## 2. Topic-by-Topic Readiness Benchmarks

### Advanced SQL
- [ ] Understand SQL order of execution: `FROM/JOIN` $\to$ `WHERE` $\to$ `GROUP BY` $\to$ `HAVING` $\to$ `SELECT` $\to$ `WINDOW` $\to$ `DISTINCT` $\to$ `ORDER BY` $\to$ `LIMIT`.
- [ ] Implement ranking without ties (`ROW_NUMBER`), with gaps (`RANK`), and without gaps (`DENSE_RANK`).
- [ ] Calculate moving averages, running totals, and year-over-year growth using `LAG() / LEAD()`.
- [ ] Construct multi-level Common Table Expressions (CTEs) for customer cohort retention.

### Python & Scientific Stack
- [ ] Explain Python memory allocation, mutable vs immutable types, and list/dict comprehension internals.
- [ ] Vectorize nested loops using NumPy array broadcasting.
- [ ] Execute complex Pandas operations: `groupby.transform()`, `pivot_table()`, `merge(how='left')`, and `pd.qcut()`.
- [ ] Construct clean Scikit-learn pipelines with custom transformers and cross-validation folds.

### Applied Statistics & Experimentation
- [ ] Formulate null ($H_0$) and alternative ($H_1$) hypotheses for business scenarios.
- [ ] Calculate sample size: $n = \frac{2(z_{\alpha/2} + z_{\beta})^2 \sigma^2}{\delta^2}$.
- [ ] Differentiate between parametric ($t$-test, ANOVA) and non-parametric (Mann-Whitney U, Kruskal-Wallis) tests.
- [ ] Explain variance reduction in A/B testing via CUPED (Controlled-experiment Using Pre-Experiment Data).

### Core Machine Learning
- [ ] Derive the logistic sigmoid function from log-odds: $p = \frac{1}{1 + e^{-z}}$.
- [ ] Formulate binary cross-entropy (log-loss): $\mathcal{L} = -\frac{1}{N} \sum [y_i \ln p_i + (1 - y_i) \ln (1 - p_i)]$.
- [ ] Compare Gini Impurity ($1 - \sum p_i^2$) vs Information Gain / Entropy ($-\sum p_i \log_2 p_i$).
- [ ] Detail the difference between bagging (Random Forest: variance reduction) and boosting (Gradient Boosting: bias reduction).
- [ ] Explain exact TreeSHAP calculation based on Shapley values from cooperative game theory.

### Time-Series Forecasting
- [ ] Explain weak stationarity: constant mean, constant finite variance, autocovariance dependent only on lag.
- [ ] Interpret Augmented Dickey-Fuller (ADF) test $p$-values.
- [ ] Differentiate between autoregressive ($p$), integrated ($d$), and moving average ($q$) terms in $\text{ARIMA}(p,d,q)$.
- [ ] Execute rolling-window time-series validation without forward-looking data leakage.
