# 05. Business Analyst: Comprehensive Interview Playbook

> Stage-by-stage guide from Online Assessment (OA) screening to Live SQL, Business Case, and HR/Fit rounds.

---

## 1. Selection Process Overview

```text
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                           BUSINESS ANALYST SELECTION PIPELINE                           │
├────────────────────────────┬─────────────────────────────┬──────────────────────────────┤
│   STAGE 1: ONLINE TEST     │   STAGE 2: TECHNICAL / SQL  │  STAGE 3: BUSINESS CASE & HR │
├────────────────────────────┼─────────────────────────────┼──────────────────────────────┤
│ • Quant & Aptitude (30m)   │ • Live Coderpad SQL (30m)   │ • Metric Drop Diagnosis (30m)│
│ • Data Interpretation (20m)│ • Schema Querying & Joins   │ • A/B Testing & Trade-offs   │
│ • SQL / Coderpad MCQs (30m)│ • Window Functions & Cohorts│ • "Why BA from Civil?" Fit   │
└────────────────────────────┴─────────────────────────────┴──────────────────────────────┘
```

---

## 2. Stage 1: Online Assessment (OA) Mastery

### Typical Section Breakdown:
1. **Quantitative Aptitude & Speed Math (20-30 Questions, 30 Mins)**: Profit & loss, percentages, weighted averages, time & work, probability, permutations.
2. **Data Interpretation & Chart Reading (15-20 Questions, 25 Mins)**: Bar charts, multi-axis line graphs, pie charts, cross-tabulation tables.
3. **SQL & Analytical Logic (15-20 Questions, 25 Mins)**: Output prediction from SQL snippets, `NULL` handling, `LEFT JOIN` row count predictions, subquery logic.

### OA Speed Strategy:
- **Zero Calculation Error Rule**: Use fraction approximations ($rac{1}{7} pprox 14.3\%$) to eliminate wrong options in $<30$ seconds.
- **SQL Prediction Check**: When predicting `LEFT JOIN` output row count, check for duplicate keys in the right table (which causes row multiplication).

---

## 3. Stage 2: Technical & Live SQL Round

### What the Interviewer Evaluates:
- **Thinking Out Loud**: Explaining schema logic and filter order before writing queries.
- **Edge Case Awareness**: Handling `NULL` values with `COALESCE`, filtering cancelled/refunded transactions, avoiding integer division truncation (`1.0 * a / b`).
- **Query Optimization**: Using CTEs (`WITH`) instead of deeply nested subqueries for readability and performance.

---

## 4. Stage 3: Business Case Round (Metric Drop Framework)

When presented with an ambiguous problem like *"Our food delivery app's conversion rate dropped 15% last week"*, use the 5-step diagnostic framework:

```text
                               METRIC DROP DIAGNOSTIC FLOW
┌─────────────────────────┐     ┌─────────────────────────┐     ┌─────────────────────────┐
│  1. CLARIFY & VALIDATE  │ ──> │ 2. MATHEMATICAL TREE    │ ──> │ 3. SEGMENTATION CUTS    │
│ • Internal bug / data?  │     │ • Conversion =          │     │ • Platform (iOS/Android)│
│ • Sudden vs Gradual?    │     │   Checkouts / Visitors  │     │ • City / Geography      │
│ • One-off vs Trend?     │     │ • Isolate Num vs Denom  │     │ • New vs Repeat Users   │
└─────────────────────────┘     └─────────────────────────┘     └─────────────────────────┘
                                                                             │
┌─────────────────────────┐     ┌─────────────────────────┐                  │
│ 5. ACTION & MONITORING  │ <── │ 4. EXTERNAL / INTERNAL  │ <────────────────┘
│ • Revert buggy release  │     │ • Internal: App update  │
│ • Add merchant capacity │     │ • External: Competitor  │
│ • Set anomaly alerts    │     │   campaign, rain/storm  │
└─────────────────────────┘     └─────────────────────────┘
```

---

## 5. Stage 4: HR & Fit Round ("Why BA from Civil Engineering?")

### Verbatim Placement-Ready Script:
```text
"During my Civil and Water Resources Engineering studies at IIT Kanpur, my coursework and thesis research
revolved around quantitative problem solving—analyzing large environmental time-series datasets, building
predictive models for hydraulic systems, and optimizing resource distribution under physical constraints.

While working on these computational models, I realized that my core passion is applying structured data
analysis, statistical validation, and logical problem solving to real-world operational and business
challenges. 

A Business Analyst role sits at the exact intersection of data querying, quantitative modeling, and strategic
decision-making. My background gives me strong mathematical fluency, high comfort with complex datasets, and
a rigorous habit of validating every hypothesis with data—skills that allow me to create immediate impact in
this role."
```
