# 01 — 7-Day Emergency Revision Plan
## High-Intensity Sprint for Fast-Approaching Tredence Technical Assessments & Interviews

> **Target Schedule**: 7 Days | 6–8 Hours Daily | Total: ~50 Hours  
> **Philosophy**: Maximum yield on P0 elimination topics (SQL, Python, Stats, ML) + Candidate Research Defense.

---

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 7-DAY EMERGENCY PREPARATION CALENDAR                                   │
├─────────┬──────────────────────────────────────────┬───────────────────────────────────────────────────┤
│ Day     │ Core Technical Focus                     │ Targeted Modules & Practical Output               │
├─────────┼──────────────────────────────────────────┼───────────────────────────────────────────────────┤
│ **D-1** │ Advanced SQL & Query Optimization        │ Module 03: 50 SQL questions + Window Functions    │
├─────────┼──────────────────────────────────────────┼───────────────────────────────────────────────────┤
│ **D-2** │ Vectorized Python, NumPy & Pandas        │ Module 02: 50 Python exercises + EDA pipelines    │
├─────────┼──────────────────────────────────────────┼───────────────────────────────────────────────────┤
│ **D-3** │ Applied Statistics, Probability & A/B    │ Module 04: Hypothesis tests, sample size & power  │
├─────────┼──────────────────────────────────────────┼───────────────────────────────────────────────────┤
│ **D-4** │ Supervised ML, Ensembles & TreeSHAP      │ Module 05: Loss math, LightGBM, PR-AUC, SHAP      │
├─────────┼──────────────────────────────────────────┼───────────────────────────────────────────────────┤
│ **D-5** │ Time-Series & Candidate Project Defense  │ Module 06 (Time-Series) + Module 12 (Project Def) │
├─────────┼──────────────────────────────────────────┼───────────────────────────────────────────────────┤
│ **D-6** │ Business Problem Framing & "Now What?"   │ Module 09: 20 Industry Cases (Retail/CPG/Telecom) │
├─────────┼──────────────────────────────────────────┼───────────────────────────────────────────────────┤
│ **D-7** │ Timed Mock Assessments & Final Polish    │ Module 08: Full-Length Timed Mock + SPEED Values  │
└─────────┴──────────────────────────────────────────┴───────────────────────────────────────────────────┘
```

---

### Detailed Daily Schedules

#### Day 1: Advanced SQL Mastery
- **Morning (3h)**: Review SQL execution order, multi-table joins, self-joins, Common Table Expressions (CTEs). Solve questions 1–25 in `03_SQL/sql_question_bank.md`.
- **Afternoon (3h)**: Master analytical window functions (`ROW_NUMBER`, `DENSE_RANK`, `LAG`, `LEAD`, moving averages). Solve questions 26–50 in `03_SQL/sql_question_bank.md`.
- **Evening (2h)**: Write retail cohort retention and rolling 7-day revenue queries against `03_SQL/practice_datasets/mock_retail_cpg_schema.sql`.

#### Day 2: Vectorized Python & Pandas Wrangling
- **Morning (3h)**: NumPy vectorization, array slicing, broadcasting rules, matrix operations. Review OOP and generator patterns in `02_PYTHON_AND_DATA_ANALYSIS/python_fundamentals.md`.
- **Afternoon (3h)**: Pandas advanced aggregation, `groupby().transform()`, missingness handling (MCAR/MAR), categorical encoding. Solve 50 coding exercises in `02_PYTHON_AND_DATA_ANALYSIS/coding_questions.md`.
- **Evening (2h)**: Build an automated, clean EDA script reproducing the 5-step `quick_eda(df)` pattern.

#### Day 3: Statistical Inference & Experimental Design
- **Morning (3h)**: Distributions (Normal, Binomial, Poisson, Beta, Gumbel), Central Limit Theorem, confidence intervals. Work through formulas in `04_STATISTICS_AND_EXPERIMENTATION/probability_and_statistics.md`.
- **Afternoon (3h)**: Hypothesis testing ($t$-test, $z$-test, $\chi^2$, ANOVA), $p$-value interpretation, Type I/II errors, and sample size derivation: $n = \frac{2(z_{\alpha/2} + z_{\beta})^2 \sigma^2}{\delta^2}$.
- **Evening (2h)**: A/B testing workflow, minimum detectable effect (MDE), variance reduction (CUPED), and solving numerical problems 1–25 in `04_STATISTICS_AND_EXPERIMENTATION/numerical_problems.md`.

#### Day 4: Core Machine Learning & Model Explainability
- **Morning (3h)**: Linear & Logistic regression mathematical foundations, loss function derivations, regularization ($L_1$ Lasso, $L_2$ Ridge), assumptions.
- **Afternoon (3h)**: Tree-based algorithms: Decision trees (Gini vs Entropy), Random Forest bagging, Gradient Boosting (XGBoost, LightGBM). Class imbalance techniques (SMOTE, class weights, focal loss).
- **Evening (2h)**: Model evaluation metrics (PR-AUC vs ROC-AUC, Brier score), TreeSHAP cooperative game theory mechanics, and solving ML deep-dive questions in `05_MACHINE_LEARNING/interview_questions.md`.

#### Day 5: Time-Series Forecasting & Candidate Project Defense
- **Morning (3h)**: Time-series components, stationarity (ADF test), ACF/PACF interpretation, ARIMA/SARIMA formulations, rolling-window validation in `06_ADVANCED_ANALYTICS/time_series.md`.
- **Afternoon (3h)**: Master the 5-stage project defense script in `12_CANDIDATE_FIT_AND_CV/project_explanation_frameworks.md` for core technical project archetypes:
  1. *[Technical Project Archetype 1: Machine Learning Failure Risk Prediction & SHAP Explainability]*
  2. *[Technical Project Archetype 2: Time-Series Forecasting & Extreme Value Analysis]*
- **Evening (2h)**: Rehearse the 30-second and 3-minute "Engineering-to-Data Science Pivot" pitch out loud.

#### Day 6: Business Problem Framing & The "Now What?"
- **Morning (3h)**: Study MECE issue tree decomposition in `09_BUSINESS_CASES_AND_COMMUNICATION/business_problem_framing.md`. Practice breaking down retail out-of-stock and telecom churn problems.
- **Afternoon (3h)**: Review the 20 industry cases across Retail, CPG, Telecom, and Healthcare in `09_BUSINESS_CASES_AND_COMMUNICATION/industry_cases.md`. Focus on translating model metrics to dollar impact.
- **Evening (2h)**: Review executive slide design principles (Minto Pyramid Model) in `09_BUSINESS_CASES_AND_COMMUNICATION/executive_storytelling.md`.

#### Day 7: Timed Mock Simulation & Cultural Alignment
- **Morning (3h)**: Take the full-length timed mock assessment in `08_ASSESSMENT_PREPARATION/mock_tests/full_length_timed_mock.md` (60 min, 50 questions) under exam conditions. Score and review mistakes.
- **Afternoon (3h)**: Review GenAI fundamentals, RAG architecture, and agentic workflows in `07_GENAI_AND_AGENTS/`.
- **Evening (2h)**: Rehearse STAR behavioral responses mapped to Tredence SPEED values in `11_INTERVIEW_PREPARATION/behavioural_interview.md`. Rest early.
