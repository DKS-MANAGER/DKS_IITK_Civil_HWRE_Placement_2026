# 08. Data Analyst: Milestone Preparation Roadmaps

> **Scope**: Multi-timeline preparation schedules designed for IIT Kanpur candidates preparing for Data Analyst campus placements. `[PREPARATION HEURISTIC]`

---

## 1. 30-Day Comprehensive Placement Blueprint

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                       30-DAY DATA ANALYST MILESTONE ROADMAP                 │
├──────────────────┬──────────────────┬──────────────────┬────────────────────┤
│ WEEK 1: SQL &    │ WEEK 2: PYTHON & │ WEEK 3: METRICS, │ WEEK 4: MOCK TESTS │
│ RELATIONAL CORE  │ DATA WRANGLING   │ BI & CASE STUDY  │ & INTERVIEW DRILLS │
│ CTEs, Window Fns,│ Pandas, NumPy,   │ LTV, CAC, Cohort,│ Timed 90-min mocks,│
│ Grain, Joins     │ Missing data, EDA│ Star schemas, BI │ Live coding, STAR  │
└──────────────────┴──────────────────┴──────────────────┴────────────────────┘
```

### Week 1: Advanced Relational SQL & Data Modeling
* **Day 1–2: Relational Fundamentals & Joins**:
  - Master `INNER`, `LEFT`, `RIGHT`, `FULL OUTER`, and `CROSS` joins.
  - Understand join multiplication and grain mismatches ([`03_domain-knowledge.md`](03_domain-knowledge.md)).
  - Practice 15 multi-table join problems.
* **Day 3–4: Advanced Window Functions**:
  - Master `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `NTILE(4)`.
  - Practice offset functions: `LAG()` and `LEAD()` with explicit default values.
  - Understand window frame semantics: `ROWS BETWEEN N PRECEDING AND CURRENT ROW`.
* **Day 5–7: CTEs, Subqueries & Complex Aggregations**:
  - Solve 15 real-world queries in [`../citicorp-aim-analytics/02_SQL_DATA_MANIPULATION.md`](../../../04_company-prep/company-specific-prep/citicorp-aim-analytics/02_SQL_DATA_MANIPULATION.md).
  - Practice deduplication patterns and running cumulative metrics.
  - **Milestone Output**: 40 complex SQL queries written and validated without errors.

---

### Week 2: Python Data Wrangling, EDA & Statistical Inference
* **Day 8–10: Pandas & Vectorized Data Cleaning**:
  - Ingest messy CSV/JSON datasets; inspect dtypes and handle missing values (MCAR, MAR, MNAR).
  - Master `.groupby()`, `.pivot_table()`, `.melt()`, and datetime manipulation.
  - Solve 10 data wrangling drills in Python.
* **Day 11–12: Exploratory Data Analysis (EDA) & Outliers**:
  - Detect outliers using IQR and Z-score methods.
  - Plot univariate and bivariate distributions using Seaborn/Matplotlib.
  - Identify and explain Simpson's Paradox on synthetic datasets.
* **Day 13–14: Statistical Inference & Hypothesis Testing**:
  - Study Central Limit Theorem, confidence intervals, and hypothesis tests ($Z$, $t$, $\chi^2$, ANOVA).
  - Review sample size calculation formulas and assumptions in [`../analytics/03_domain-knowledge.md`](../analytics/03_domain-knowledge.md).
  - **Milestone Output**: 2 end-to-end Python exploratory analyses with clean markdown summaries.

---

### Week 3: Business Metrics, Dashboard Design & Analytical Cases
* **Day 15–17: Core Business Metrics & Unit Economics**:
  - Master formulas and edge cases for CAC, LTV, Churn, NRR, and DAU/MAU ([`03_domain-knowledge.md`](03_domain-knowledge.md)).
  - Calculate cohort retention matrices manually and via SQL.
* **Day 18–19: Dashboard Architecture & Visualization Governance**:
  - Study dimensional modeling: Star Schema vs Snowflake Schema.
  - Master chart selection rules and review deceptive visualization audits ([`02_skills-and-competencies.md`](02_skills-and-competencies.md)).
  - Design a wireframe dashboard for an e-commerce executive.
* **Day 20–21: Analytical Business Problem Solving**:
  - Master the 5-step funnel drop-off deconstruction framework ([`05_interview-preparation.md`](05_interview-preparation.md)).
  - Solve all business cases in [`07_practice-and-cases.md`](07_practice-and-cases.md).
  - **Milestone Output**: 5 completed business cases with structured issue trees.

---

### Week 4: Timed Mock Simulations, Behavioral HR & Peer Drills
* **Day 22–24: Timed Assessment Drills**:
  - Take the comprehensive timed 90-minute test in [`12_mock-assessment.md`](12_mock-assessment.md).
  - Score against the official rubric; identify remaining weak areas.
* **Day 25–27: Live Technical Screen-Share Rehearsal**:
  - Practice explaining SQL query execution plans out loud in $< 5\text{ mins}$.
  - Rehearse the 10 core technical grilling questions in [`06_question-bank.md`](06_question-bank.md).
* **Day 28–30: Behavioral Polish & Rapid Revision**:
  - Finalize 5 STAR stories connecting Civil/HWRE coursework to analytics ([`11_projects.md`](11_projects.md)).
  - Review high-yield cheat sheets in [`09_rapid-revision.md`](09_rapid-revision.md).
  - **Milestone Output**: Mock assessment score $\ge 75/100$; fluent 90-second transition pitch.

---

## 2. 14-Day Fast-Track Sprint Schedule

| Days | Focus Area | Mandatory Deliverables & Study Resources |
| :---: | :--- | :--- |
| **Day 1–4** | **SQL Heavy Artillery** | Solve 25 SQL problems: CTEs, window functions (`ROW_NUMBER`, `DENSE_RANK`, `LAG`, `LEAD`), joins. Review [`04_tools-and-technical-stack.md`](04_tools-and-technical-stack.md). |
| **Day 5–7** | **Data Quality & Python EDA** | Master join multiplication diagnosis, missing value imputation, and groupby aggregations in Pandas. |
| **Day 8–10** | **Business Metrics & Cases** | Calculate cohort retention, CAC/LTV, and solve 3 funnel drop-off cases in [`07_practice-and-cases.md`](07_practice-and-cases.md). |
| **Day 11–12**| **Mock Evaluation** | Complete the 90-minute timed mock in [`12_mock-assessment.md`](12_mock-assessment.md). Score $\ge 70$. |
| **Day 13–14**| **Behavioral & Revision** | Polish "Why Non-Core?" pitch, review cheat sheet in [`09_rapid-revision.md`](09_rapid-revision.md). |

---

## 3. 7-Day High-Intensity Sprint

* **Day 1**: Advanced SQL Joins, Grain Mismatch, and NULL handling (8 hours).
* **Day 2**: Window functions: `ROW_NUMBER`, `LAG`, `LEAD`, moving averages (8 hours).
* **Day 3**: Python Pandas wrangling, groupby, and outlier detection (6 hours).
* **Day 4**: Business metrics: LTV, CAC, Churn, Retention cohorts, Star schemas (6 hours).
* **Day 5**: Analytical case solving & MECE issue trees (6 hours).
* **Day 6**: Complete timed mock assessment in [`12_mock-assessment.md`](12_mock-assessment.md) (4 hours).
* **Day 7**: Formula revision, STAR stories, and mental review (4 hours).

---

## 4. 3-Day Emergency Test-Eve Checklist

- [ ] **SQL Flashcard Review**: Review the syntax for `ROW_NUMBER()`, `LAG(col, 1, 0) OVER (PARTITION BY ... ORDER BY ...)`.
- [ ] **Data Hygiene Rules**: Remember: Always check table grain and primary keys before joining.
- [ ] **Metric Formulas**: Review formulas for CAC, LTV, Logo Churn, and NRR.
- [ ] **Interview Pitch**: Rehearse the 3-step Civil-to-Analytics transition answer in $< 90\text{ seconds}$.
- [ ] **Cheat Sheet**: Read [`09_rapid-revision.md`](09_rapid-revision.md) three times before the test.
