# 05. Analytics: Comprehensive Interview Playbook

> Stage-by-stage guide from Online Assessment (OA) screening to Live SQL, Python/Pandas coding, Product Analytics cases, and Behavioral/Fit rounds.

---

## 1. Selection Process Stages

```text
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                            ANALYTICS SELECTION PIPELINE                                 │
├────────────────────────────┬─────────────────────────────┬──────────────────────────────┤
│    STAGE 1: ONLINE TEST    │  STAGE 2: TECHNICAL CODING  │  STAGE 3: ANALYTICS CASE & HR│
├────────────────────────────┼─────────────────────────────┼──────────────────────────────┤
│ • Quant Aptitude (30m)     │ • Live Coderpad SQL (30m)   │ • Metric Drop Diagnosis (30m)│
│ • Data Interpretation (20m)│ • Python / Pandas EDA (30m) │ • A/B Test Design & Trade-off│
│ • SQL & Stats MCQs (30m)   │ • ML / Stats Concepts (20m) │ • "Why Analytics from Civil?"│
└────────────────────────────┴─────────────────────────────┴──────────────────────────────┘
```

---

## 2. Stage 2: Technical & Live Coding Rounds

### What the Interviewer Evaluates:
- **SQL Cleanliness**: Explaining schema assumptions, filter order, and edge cases (`NULL` handling with `COALESCE`, avoiding integer division).
- **Python Efficiency**: Writing vectorized Pandas code rather than slow Python `for` loops across rows.
- **Statistical Rigor**: Explaining confidence intervals, p-values, and statistical power without confusing correlation with causation.

---

## 3. Stage 3: Product Analytics Case Framework (The 5-Step System)

When asked: *"Our e-commerce app's Daily Active Users (DAU) dropped 12% week-over-week. How do you diagnose it?"*:

```text
                               METRIC DROP DIAGNOSTIC FLOW
┌─────────────────────────┐     ┌─────────────────────────┐     ┌─────────────────────────┐
│  1. CLARIFY & VALIDATE  │ ──> │ 2. MATHEMATICAL TREE    │ ──> │ 3. SEGMENTATION CUTS    │
│ • Data pipeline bug?    │     │ • DAU = New Users +     │     │ • OS: iOS vs Android    │
│ • Sudden vs Gradual?    │     │   Resurrected + Retained│     │ • Country / City Tier   │
│ • Seasonality / Holiday?│     │ • Isolate which bucket! │     │ • Traffic: Organic/Paid │
└─────────────────────────┘     └─────────────────────────┘     └─────────────────────────┘
                                                                             │
┌─────────────────────────┐     ┌─────────────────────────┐                  │
│ 5. ACTION & EXPERIMENT  │ <── │ 4. ROOT-CAUSE AUDIT     │ <────────────────┘
│ • Revert buggy release  │     │ • App release crash?    │
│ • Fix notification push │     │ • Competitor launch?    │
│ • A/B test re-engagement│     │ • Marketing spend cut?  │
└─────────────────────────┘     └─────────────────────────┘
```

---

## 4. Stage 4: HR & Fit Round ("Why Analytics from Civil Engineering?")

### Verbatim Placement-Ready Script:
```text
"During my Civil and Water Resources Engineering curriculum at IIT Kanpur, my coursework and thesis
research centered around quantitative problem solving—analyzing large environmental time-series datasets,
building predictive hydrodynamic models, and optimizing resource distribution under physical constraints.

Through projects like BridgeRisk and computational flow simulations, I discovered that my strongest passion
lies in applied data science—querying large datasets, building predictive statistical models, and translating
quantitative patterns into actionable decisions.

An Analytics & Decision Science role sits at the exact intersection of statistical modeling, data querying,
and commercial strategy. My engineering background gives me strong mathematical fluency, comfort with
unstructured datasets, and a disciplined habit of verifying assumptions with data—skills that allow me to
create immediate impact as a Decision Analytics Associate."
```
