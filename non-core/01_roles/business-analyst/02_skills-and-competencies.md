# 02. Business Analyst: Required Skills & Competencies

> Detailed competency hierarchy and pre-interview technical checklists for Business Analyst placement preparation.

---

## 1. Technical Competency Breakdown

```text
                        ┌──────────────────────────────────────────────┐
                        │         BUSINESS ANALYST SKILL STACK         │
                        └──────────────────────┬───────────────────────┘
                                               │
        ┌──────────────────────┬───────────────┴───────────────┬──────────────────────┐
        │                      │                               │                      │
 ┌──────▼──────┐        ┌──────▼──────┐                 ┌──────▼──────┐        ┌──────▼──────┐
 │     SQL     │        │    EXCEL    │                 │ STATISTICS  │        │  BUSINESS   │
 │ (CTEs, Window│       │ (XLOOKUP,   │                 │ (A/B Tests, │        │ (Unit Econ, │
 │  Functions) │        │  Pivots)    │                 │  Hypothesis)│        │  KPI Trees) │
 └─────────────┘        └─────────────┘                 └─────────────┘        └─────────────┘
```

### Pre-Interview Technical Checklist
| Competency Area | Priority | Specific Capabilities Tested | Placement Verification Metric |
|:---|:---:|:---|:---|
| **SQL Querying** | **P0** | Multi-table `JOIN`s, `GROUP BY / HAVING`, `CASE WHEN`, CTEs (`WITH`), Window functions (`ROW_NUMBER`, `DENSE_RANK`, `LAG`, `LEAD`, `SUM() OVER()`), Date truncation & interval math, cohort retention queries. | Write 10 complex queries in 45 mins with zero syntax errors. |
| **Excel & Spreadsheets** | **P0** | `XLOOKUP`, `INDEX(MATCH)`, `SUMIFS`, `COUNTIFS`, Pivot Tables, 2-variable Data Tables, conditional aggregation, charting. | Clean and summarize a 10,000-row raw CSV in <15 mins. |
| **Applied Statistics** | **P0** | A/B testing sample size calculation ($N pprox rac{16\sigma^2}{\Delta^2}$), p-value interpretation, Type I/II errors, Simpson's Paradox, central tendency vs. variance. | Explain A/B test results and statistical significance to non-technical stakeholders. |
| **Data Interpretation** | **P0** | Extracting actionable insights from multi-line charts, cohort heatmaps, and funnel conversion waterfalls. | Identify the primary bottleneck from a 4-stage funnel exhibit in <60 seconds. |
| **Business Acumen** | **P0** | Unit economics decomposition ($CAC$, $LTV$, Contribution Margin, Payback Period, Churn, Take Rate). | Build a profitability tree for an e-commerce or SaaS business in 90 seconds. |
| **Executive Synthesis** | **P1** | Pyramid Principle: State the recommendation first, supported by 3 quantified data points and implementation risks. | 90-second case conclusion delivery. |

---

## 2. The 3-Tier Placement Readiness Ladder

```text
TIER 1: OA & CODING SCREEN READY
├── Flawless SQL: Solves Hard LeetCode / HackerRank SQL questions in <10 mins.
├── Fast quantitative reasoning: Solves speed math, percentage, and ratio questions in <60s.
└── Data interpretation fluency: Reads bar/line/scatter/waterfall charts effortlessly.

TIER 2: TECHNICAL ROUND READY
├── Can write clean, formatted SQL live while explaining query execution order out loud.
├── Explains difference between correlation and causation with concrete business examples.
└── Designs end-to-end A/B tests with sample size, MDE, and primary/guardrail metrics.

TIER 3: BUSINESS CASE & OFFER READY
├── Diagnoses metric drops (e.g. 15% revenue drop) using MECE mathematical trees.
├── Translates engineering/thesis data modeling into commercial business value.
└── Defends analytical trade-offs calmly under tough interviewer pushback.
```
