# 02. Data Analyst: Required Skills, Competencies & Evaluation Rubrics

> **Scope**: Detailed evaluation framework breaking down the core technical, analytical, architectural, and communication competencies tested by top recruiting firms during campus placement evaluations. `[PREPARATION HEURISTIC]`

---

## 1. Core Competency Taxonomy

Campus evaluators assess Data Analyst candidates across six primary competency pillars:

```text
                               DATA ANALYST COMPETENCY ENGINE
                                              │
         ┌──────────────────┬─────────────────┼──────────────────┬──────────────────┐
         ▼                  ▼                 ▼                  ▼                  ▼
   1. ADVANCED SQL    2. PYTHON & EDA   3. SPREADSHEETS    4. BI & DASHBOARDS  5. DATA QUALITY
   Window functions   Pandas, NumPy     Nested formulas,   Tableau, Power BI,  Deduplication,
   CTEs, Joins,       Data cleaning,    Pivot tables,      Star schemas,       Grain validation,
   Execution plans    Vectorization     Scenario modeling  KPI hierarchies     Outlier handling
```

---

## 2. Four-Tier Skill Benchmark Ladder

| Competency Dimension | Level 1: Awareness | Level 2: Developing | Level 3: Interview-Ready (`[TARGET]`) | Level 4: Strong (Day-1 Lead) |
| :--- | :--- | :--- | :--- | :--- |
| **Relational SQL** | Writes basic `SELECT`, `WHERE`, `GROUP BY`, and inner joins on clean schemas. | Writes multi-table joins, subqueries, and standard aggregations with `HAVING`. | Fluent in window functions (`ROW_NUMBER`, `DENSE_RANK`, `LAG`, `LEAD`), CTEs, rolling metrics, and handles NULLs correctly. | Analyzes `EXPLAIN` query execution plans, optimizes indexes, resolves complex grain mismatches, and prevents cartesian fanouts. |
| **Python & EDA** | Uses basic syntax, lists, dictionaries, and simple control flow loops. | Loads CSVs via Pandas, performs basic filtering, groupby, and simple Matplotlib plots. | Performs vectorized transformations, missing value imputation, datetime manipulations, and detects multi-variate outliers. | Builds modular ETL pipelines, engineers automated data quality checks, and creates interactive visualization components. |
| **Spreadsheets (Excel/Sheets)** | Basic arithmetic, `SUM`, `AVERAGE`, simple cell formatting. | `VLOOKUP`, basic pivot tables, conditional formatting, basic chart creation. | `XLOOKUP`, `INDEX(MATCH)`, dynamic arrays (`FILTER`, `UNIQUE`), nested logicals, and sensitivity tables. | Complex financial/operational scenario models, automated macro scripts (VBA/Apps Script), and audit-proof financial templates. |
| **Business Intelligence (BI)** | Views pre-built reports and interacts with static dashboard slicers. | Builds basic bar, line, and pie charts with standard drag-and-drop tools. | Designs Dimensional Star Schemas, creates custom DAX / Tableau calculated fields, and structures executive visual hierarchies. | Implements Row-Level Security (RLS), incremental refresh policies, optimized semantic models, and cross-filter governance. |
| **Data Quality & Hygiene** | Assumes raw data is clean and runs queries directly. | Detects missing values and obvious data entry errors via visual inspection. | Identifies join multiplication, grain mismatches, timezone discrepancies, and writes automated reconciliation tests. | Establishes end-to-end data governance protocols, lineage tracking, anomaly detection alert thresholds, and SLA monitoring. |
| **Executive Synthesis** | Explains raw numbers, tables, and describes tool steps taken. | Explains findings in paragraphs but requires prompting for business context. | Uses the Pyramid Principle: leads with core recommendation, supports with 3 data points, and states actionable next steps. | Navigates high-stakes executive pushback, quantifies financial risk/upside trade-offs, and aligns competing stakeholder goals. |

---

## 3. Detailed Competency Profiles

### 3.1 Advanced SQL & Query Performance (`[P0]` — Priority 0)
* **What Interviewers Test**: Can you retrieve and manipulate complex enterprise data without generating duplicate rows or crashing the server?
* **Core Technical Checklist**:
  - **Window Frame Clauses**: Explicitly specifying `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW` vs `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`.
  - **Deduplication Patterns**: Using `ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)` vs `DISTINCT`.
  - **Date Arithmetic**: Calculating month-over-month (MoM) growth, year-over-year (YoY) metrics, and retention cohort matrices.
  - **Self-Joins & Hierarchy**: Finding manager-employee relationships or session-to-session event progressions.

### 3.2 Python for Analytics & Data Wrangling (`[P0]` — Priority 0)
* **What Interviewers Test**: Can you ingest messy real-world datasets, diagnose anomalies, and generate reproducible summaries?
* **Core Technical Checklist**:
  - **Pandas Data Manipulation**: Mastering `.groupby()`, `.agg()`, `.pivot_table()`, `.melt()`, and `.merge()`.
  - **Vectorization**: Avoiding slow Python `for` loops across large DataFrames; utilizing NumPy vectorized logic.
  - **Missing Value Handling**: Distinguishing between Missing Completely at Random (MCAR), Missing at Random (MAR), and Missing Not at Random (MNAR).
  - **Datetime Indexing**: Handling timezone conversions, resampling time series data (e.g., hourly to daily grain), and extracting calendar features.

### 3.3 Dashboard Architecture & Data Storytelling (`[P1]` — Priority 1)
* **What Interviewers Test**: Can you turn multi-million-row database tables into an intuitive executive dashboard that guides operational decisions?
* **Core Technical Checklist**:
  - **Information Hierarchy**: Placing North Star Metrics (KPI cards) at top-left, secondary breakdowns in the center, and granular transaction tables at the bottom.
  - **Chart Choice Rules**: Using Bar Charts for discrete categories, Line Charts for continuous time, and Scatter Plots for bivariate correlation.
  - **Cognitive Load Reduction**: Limiting color palettes to 3–4 functional colors; avoiding 3D charts, pie charts with $>4$ slices, and dual-axis scales with mismatched units.

### 3.4 Data Quality Assurance & Pipeline Hygiene (`[P0]` — Priority 0)
* **What Interviewers Test**: Before sharing analysis with leadership, do you rigorously audit the underlying numbers?
* **Core Technical Checklist**:
  - **Primary Key Uniqueness**: Verifying `COUNT(*) = COUNT(DISTINCT id)` before performing relational joins.
  - **Reconciliation Queries**: Ensuring `SUM(metric)` before a join exactly matches `SUM(metric)` after the join.
  - **Boundary & Outlier Audits**: Checking for negative prices, future dates, unrealistic quantities, and extreme outlier leverage.

---

## 4. Evaluation Rubric by Placement Round

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CAMPUS RECRUITMENT SELECTION RUBRIC                      │
├─────────────────────┬───────────────────────┬───────────────────────────────┤
│ ROUND TYPE          │ PRIMARY CAPABILITIES  │ PASS BENCHMARK (INTERVIEW-RDY)│
├─────────────────────┼───────────────────────┼───────────────────────────────┤
│ 1. Online Assessment│ Complex SQL queries,  │ ≥ 80% accuracy in SQL; zero   │
│    (OA Test)        │ Speed data interpreta-│ arithmetic errors on timed    │
│                     │ tion, Logical puzzles │ data interpretation charts.   │
├─────────────────────┼───────────────────────┼───────────────────────────────┤
│ 2. Live Technical   │ Screen-share SQL, EDA │ Writes clean CTEs in < 5 mins;│
│    & Coding         │ in Python, Data debug │ explains join grain & index   │
│                     │ & schema design       │ execution trade-offs out loud.│
├─────────────────────┼───────────────────────┼───────────────────────────────┤
│ 3. Case & Business  │ Funnel diagnosis,     │ Deconstructs business problem │
│    Interpretation   │ Metric drop root cause│ via MECE tree; designs metric │
│                     │ Dashboard design      │ architecture with clear KPIs. │
├─────────────────────┼───────────────────────┼───────────────────────────────┤
│ 4. Partner / HR     │ Stakeholder management│ Delivers structured STAR story│
│    Behavioral       │ Handling ambiguity,   │ in < 90s; justifies Civil-to- │
│                     │ Engineering fit       │ Analytics transition fluently.│
└─────────────────────┴───────────────────────┴───────────────────────────────┘
```
