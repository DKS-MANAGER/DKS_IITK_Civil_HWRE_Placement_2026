# Technical Interview Guide: Strategy, Structure, and Rubrics

**Target Role:** Data Scientist / Associate Data Scientist | Tredence Analytics  
**Context:** IIT Kanpur Placement Season 2026–27  
**Duration:** Typically 45–60 Minutes per Technical Round (1 to 2 Rounds)

---

## 1. Technical Interview Architecture

The Tredence technical interview is split into 4 distinct phases:

```
 Total Duration: 45 - 60 Minutes
 ┌────────────────────────────────────────────────────────────────────────┐
 │ Phase 1: Candidate Background & Project Deep-Dive (15 mins)            │
 │ • Rigorous questioning on ML project architecture, feature engineering,│
 │   leakage defense, and business applicability.                         │
 ├────────────────────────────────────────────────────────────────────────┤
 │ Phase 2: Live SQL & Python Algorithmic Problem Solving (15-20 mins)    │
 │ • Writing live ANSI SQL (Window functions, CTEs) on a shared screen.   │
 │ • Python/Pandas data manipulation and time complexity analysis.        │
 ├────────────────────────────────────────────────────────────────────────┤
 │ Phase 3: Machine Learning & Statistical Theory (15 mins)               │
 │ • GBDT mechanics, XGBoost vs LightGBM, TreeSHAP, Bias-Variance, A/B.   │
 ├────────────────────────────────────────────────────────────────────────┤
 │ Phase 4: Candidate Reverse Q&A (5 mins)                                │
 │ • Thoughtful questions demonstrating knowledge of Tredence products    │
 │   (MLWorks, Sancus, Atoms) and "Last-Mile Adoption".                   │
 └────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Technical Evaluation Rubric

Interviewers score candidates on 5 core competencies:

| Competency | Exceeds Bar (Strong Hire) | Meets Bar (Hire) | Below Bar (Reject) |
|---|---|---|---|
| **Mathematical & ML Foundations** | Derives loss functions, explains second-order Hessians in XGBoost, derives Shapley axioms. | Explains GBDT vs Random Forest, knows ROC vs PR-AUC. | Memorized definitions without understanding mathematical mechanics. |
| **Code & SQL Fluency** | Writes clean, sargable ANSI SQL using CTEs and window frames on the first pass; optimizes Python complexity. | Writes working queries with minor prompt hints; uses basic joins. | Syntax errors, confusion on `GROUP BY` vs `HAVING`, brute-force $\mathcal{O}(N^2)$ loops. |
| **Statistical Rigor** | Detects sample ratio mismatch, understands CUPED, SUTVA violations, and multiple hypothesis correction (FDR). | Knows standard two-sample t-test, p-value definition, Type I/II errors. | Misinterprets p-value as probability that null is true. |
| **Consulting Mindset ("Now What?")** | Translates technical metrics ($\Delta\text{AUC}$) into dollar EBITDA savings; structures frontline adoption workflows. | Mentions business metrics but requires prompting to link with model output. | Purely academic; treats model deployment as the end of the project. |
| **Communication & Composure** | Clear, structured, uses Minto Pyramid / SCQA; thinks aloud during coding. | Generally clear; answers the question directly. | Disorganized, defensive when challenged on project limitations. |
