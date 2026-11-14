# Consulting-Grade Resume Bullets (Google X-Y-Z Formula)

**Target Role:** Data Scientist / Associate Data Scientist | Tredence Analytics  
**Context:** IIT Kanpur Placement Season 2026–27  
**Formula:** *Accomplished [X], as measured by [Y], by doing [Z]*

---

## 1. Machine Learning & Predictive Modeling

- **Accomplished** a high-precision infrastructure failure risk prediction framework, **achieving a ROC-AUC of 0.983 and PR-AUC of 0.854** on severe imbalanced telemetry data ($< 5\%$ failure events), **by engineering** domain-specific stress covariates, implementing cost-sensitive LightGBM/XGBoost ensembles, and enforcing leak-free walk-forward stratified cross-validation.
- **Improved** model transparency and engineering adoption across multidisciplinary stakeholders **by deploying** an exact TreeSHAP attribution pipeline ($\mathcal{O}(TLD^2)$ complexity), generating local waterfall reason codes and global beeswarm feature impacts to explain individual high-risk warnings.
- **Engineered** an automated customer churn mitigation and probability calibration pipeline, **achieving a Brier score of 0.038**, **by developing** custom Scikit-Learn `ColumnTransformer` pipelines with median imputation, one-hot encoding, and Isotonic regression calibration.

---

## 2. Time-Series Analysis & Demand Forecasting

- **Developed** a multi-step stochastic time-series forecasting framework for daily river discharge and extreme flood return periods, **reducing peak volume forecasting error by 18% (WAPE $< 12\%$)**, **by applying** Augmented Dickey-Fuller (ADF) stationarity diagnostics and fitting $\text{SARIMAX}$ models with exogenous precipitation covariates.
- **Modeled** extreme tail-risk recurrence intervals **by formulating and fitting** Generalized Extreme Value (GEV) and Gumbel distributions using Maximum Likelihood Estimation (MLE), establishing dynamic 95% confidence interval safety buffers for physical risk mitigation.
- **Engineered** an end-to-end retail SKU demand forecasting engine, **delivering a 14-day out-of-sample forecast accuracy of 88.5%**, **by incorporating** 7-day day-of-week seasonality, trend differencing, and probabilistic quantile loss optimization.

---

## 3. SQL & Relational Database Analytics

- **Architected** an enterprise ANSI SQL analytical query suite across a multi-table retail transactional schema, **automating** RFM customer segmentation, month-over-month growth velocity, and 7-day moving averages **by writing** optimized Common Table Expressions (CTEs) and window functions (`DENSE_RANK`, `LAG`, explicit `ROWS BETWEEN` frames).
- **Constructed** an longitudinal customer cohort retention matrix and trade promotion lift analysis, **isolating incremental promotional volume lift vs baseline sales**, **by developing** multi-table conditional aggregation queries and market basket affinity co-purchase self-joins.
- **Optimized** database execution performance across large-scale relational datasets **by designing** composite B-tree index schemas (equality-then-range alignment) and eliminating non-sargable predicate filters.

---

## 4. Scientific Computing & Prescriptive Optimization

- **Accelerated** complex multi-dimensional partial differential equation numerical simulations **by $38\times$ (reducing runtime from 14 hours to 22 minutes)**, **by refactoring** serial CPU loops into vectorized NumPy SIMD operations and compiling performance-critical kernels in C++.
- **Formulated and solved** an omnichannel commercial marketing budget allocation problem across 5 channels, **maximizing expected revenue by 24% subject to spend caps and digital mandates**, **by implementing** constrained Linear Programming via `scipy.optimize.linprog` (HiGHS interior-point solver) and extracting marginal shadow prices for executive sensitivity analysis.
- **Built and validated** a modular enterprise Hybrid Search RAG pipeline, **achieving a 100% RAG Triad Faithfulness score**, **by integrating** BM25 sparse keyword search, dense semantic vector retrieval, Reciprocal Rank Fusion ($k=60$), and simulated cross-encoder neural re-ranking.
