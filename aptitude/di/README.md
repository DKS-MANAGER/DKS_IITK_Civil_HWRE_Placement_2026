# Data Interpretation (DI) Master Curriculum

> **IIT Kanpur Campus Placements 2026** · **Curriculum Scope:** 10 Comprehensive Modules · 400 Placement-Caliber Questions across 8 Difficulty Tiers · 100% Fully Worked Mathematical Derivations & Verified Answer Keys.

---

## 1. Curriculum Architecture & Directory Map

The Data Interpretation suite is engineered to transition students from fundamental visual parsing to the analytical rigors demanded by premier global recruiters (Tier-1 Management Consulting, Quantitative Trading, Tech Product Strategy, Investment Banking, and Core Engineering Leadership).

```
aptitude/di/
├── README.md                      # Master Curriculum Map & Diagnostic Matrix (This file)
├── bar-and-line-graphs.md         # P0: Dual-axis trajectories, CAGR, index drift, and volume-value divergence
├── pie-charts.md                  # P0: Degree-percentage conversions, concentric doughnuts, and sub-allocation
├── tables-and-caselets.md         # P0: High-density relational matrices, fleet routing, and SaaS cohorts
├── mixed-graphs.md                # P0: Multi-chart relational synthesis, cross-graph reconciliation, and capacity
├── data-sufficiency.md            # P0: 3-Statement sufficiency, geometric/algebraic uniqueness, and bounds
├── missing-data-di.md             # P0: Matrix row/column conservation, algebraic infill, and inventory cascades
├── quantitative-caselets.md       # P0: Narrative translation, multi-stage process flows, and supply chain logistics
├── advanced-di-caselets.md        # P0: McKinsey/Bain/PE standards, LBO debt schedules, unit economics, and PVM
├── data-comparison.md             # P1: Relative vs %-point shifts, multi-criteria normalization, and index re-basing
└── radar-area-graphs.md           # P2: Radial Kiviat geometry, stacked dispatch envelopes, and duck curves
```

### The 8-Level Hierarchical Progression
Every module follows an identical 8-level cognitive taxonomy designed to eliminate gaps between standard textbook problems and real-world placement assessments:

```
+-----------------------------------------------------------------------------------+
|                        THE 8-LEVEL COGNITIVE TAXONOMY                             |
+-----------------------------------------------------------------------------------+
| Tier       | Designation             | Target Competency                          |
|------------+-------------------------+--------------------------------------------|
| Level 1    | Foundation              | Direct coordinate lookup, basic arithmetic |
| Level 2    | Intermediate            | 2-step calculations, simple percentage deltas|
| Level 3    | Hard                    | Ratios, CAGRs, multi-variable combinations |
| Level 4    | Very Hard               | Multi-condition filtering, cross-chart ties|
| Level 5    | Expert                  | Non-linear bounds, optimization, constraints|
| Level 6    | Extreme                 | Mathematical edge cases, systems of eqns   |
| Level 7    | Trap / Distortions      | Optical illusions, Simpson's paradox, traps|
| Level 8    | Hybrid Caselet          | Consulting/finance/infrastructure synthesis|
+-----------------------------------------------------------------------------------+
```

---

## 2. Company-Specific Weightage & Focus Matrix

| Target Sector | Top Recruiting Companies | Key Focus Modules | Common Question Archetypes |
|:---|:---|:---|:---|
| **Management Consulting** | McKinsey, BCG, Bain, Kearney, Strategy&, Oliver Wyman | [Advanced DI Caselets](file:///aptitude/di/advanced-di-caselets.md)<br>[Tables & Caselets](file:///aptitude/di/tables-and-caselets.md)<br>[Data Comparison](file:///aptitude/di/data-comparison.md) | Price-Volume-Mix (PVM) decomposition, SaaS unit economics (CAC, LTV, Churn), market sizing, margin dilution |
| **Quant Trading & Prop Shops** | Jane Street, WorldQuant, Optiver, Tower Research, Graviton | [Data Sufficiency](file:///aptitude/di/data-sufficiency.md)<br>[Data Comparison](file:///aptitude/di/data-comparison.md)<br>[Mixed Graphs](file:///aptitude/di/mixed-graphs.md) | Uniqueness proofs, 3-statement sufficiency, strict inequality bounds, normalization, Z-scores |
| **Investment Banking & PE** | Goldman Sachs, Morgan Stanley, J.P. Morgan, Blackstone | [Advanced DI Caselets](file:///aptitude/di/advanced-di-caselets.md)<br>[Bar & Line Graphs](file:///aptitude/di/bar-and-line-graphs.md)<br>[Missing Data DI](file:///aptitude/di/missing-data-di.md) | LBO cash flow waterfalls, EBITDA bridge, debt repayment schedules, inventory working capital cycles |
| **Tech Product & Analytics** | Google, Microsoft, Uber, Amazon, Flipkart | [Quantitative Caselets](file:///aptitude/di/quantitative-caselets.md)<br>[Mixed Graphs](file:///aptitude/di/mixed-graphs.md)<br>[Pie Charts](file:///aptitude/di/pie-charts.md) | Funnel conversion drops, multi-cohort retention matrices, A/B test relative lifts vs %-points |
| **Core Engineering & PSUs** | IOCL, ONGC, NTPC, Tata Steel, L&T | [Radar & Stacked Area](file:///aptitude/di/radar-area-graphs.md)<br>[Bar & Line Graphs](file:///aptitude/di/bar-and-line-graphs.md)<br>[Tables & Caselets](file:///aptitude/di/tables-and-caselets.md) | Power grid merit-order dispatch, refinery yield balances, heat rate efficiency, equipment uptime |
| **Banking & Public Service** | SBI PO, RBI Grade B, SEBI Grade A, IBPS PO | [Missing Data DI](file:///aptitude/di/missing-data-di.md)<br>[Data Sufficiency](file:///aptitude/di/data-sufficiency.md)<br>[Bar & Line Graphs](file:///aptitude/di/bar-and-line-graphs.md) | High-speed missing table in-fill, 3-statement sufficiency, compound interest and NPA trends |

---

## 3. Benchmark Speed & Accuracy Thresholds

In placement tests (such as HirePro, AMCAT, CoCubes, Mettl, and company-proprietary platforms), the time budget is strictly limited. Candidates should benchmark their speed against these operational standards:

```
+-----------------------------------------------------------------------------------+
|                        BENCHMARK TIME BUDGET ALLOCATION                           |
+-----------------------------------------------------------------------------------+
| Problem Complexity Tier     | Target Speed  | Key Mental Speed Technique          |
|-----------------------------+---------------+-------------------------------------|
| Direct Lookup / Single Delta| 35–50 sec     | Visual scanning without re-reading  |
| 2-Step Ratio / % Calculation| 50–75 sec     | Fractional equivalences (1/7, 1/8)  |
| Multi-Chart Cross-Synthesis | 80–110 sec    | Pivot-variable anchoring            |
| Missing Data Matrix In-fill | 90–130 sec    | Degree-of-Freedom sweep strategy    |
| Dense Consulting Caselet    | 110–150 sec   | Algebraic structuring & unit checks |
+-----------------------------------------------------------------------------------+
```

---

## 4. Master Mathematical & Mental Arithmetic Toolkit

### 4.1 Percentage & Growth Formulae
- **Relative Percentage Change:**
  $$\Delta\% = \frac{Y_t - Y_0}{Y_0} \times 100\%$$
- **Percentage Point Change:**
  $$\Delta p = p_t - p_0 \quad (\text{Note: Never confuse } \Delta p \text{ with } \Delta\%)$$
- **Compounded Annual Growth Rate (CAGR):**
  $$\text{CAGR} = \left(\frac{Y_n}{Y_0}\right)^{1/n} - 1 \approx \frac{1}{n} \left(\frac{Y_n - Y_0}{Y_0}\right) \quad (\text{First-order approximation for small } r)$$
- **Mental Doubling Rules:**
  - **Rule of 72:** Doubling time $T \approx 72 / r\%$
  - **Rule of 114:** Tripling time $T \approx 114 / r\%$
  - **Rule of 144:** Quadrupling time $T \approx 144 / r\%$

### 4.2 Pie Chart Degree-to-Percentage Conversions
- **Full Circle Identity:** $360^\circ \equiv 100\%$
- **Conversion Multiplier:**
  $$1^\circ = \frac{100\%}{360} = \frac{5}{18}\% \approx 0.2778\%$$
  $$1\% = \frac{360^\circ}{100} = 3.6^\circ$$
- **Rapid Anchors:**
  - $36^\circ = 10\%$
  - $54^\circ = 15\%$
  - $72^\circ = 20\%$
  - $90^\circ = 25\%$
  - $108^\circ = 30\%$
  - $126^\circ = 35\%$
  - $144^\circ = 40\%$

### 4.3 Radar (Kiviat) Geometric Polygon Area
For an equiangular $n$-axis radar chart with central angle $\theta = \frac{360^\circ}{n}$:
$$\text{Area} = \frac{1}{2} \sin\left(\frac{360^\circ}{n}\right) \sum_{i=1}^n r_i r_{i+1} \quad (\text{with } r_{n+1} \equiv r_1)$$
- **5-Axis Pentagonal Radar:** $A = \frac{1}{2} \sin(72^\circ) \sum_{i=1}^5 r_i r_{i+1} \approx 0.4755 \sum r_i r_{i+1}$
- **6-Axis Hexagonal Kiviat:** $A = \frac{\sqrt{3}}{4} \sum_{i=1}^6 r_i r_{i+1} \approx 0.4330 \sum r_i r_{i+1}$

### 4.4 Price-Volume-Mix (PVM) Variance Decomposition
$$\Delta \text{Revenue} = \text{Revenue}_1 - \text{Revenue}_0 = \Delta_{\text{Volume}} + \Delta_{\text{Price}} + \Delta_{\text{Mix}}$$
- **Volume Effect:** $(V_1 - V_0) \times \bar{P}_0$
- **Price Effect:** $\sum V_{1, i} \times (P_{1, i} - P_{0, i})$
- **Mix Effect:** $V_1 \times \sum (w_{1, i} - w_{0, i}) \times P_{0, i}$

---

## 5. Module-by-Module Curriculum Guide

### 1. [Bar and Line Graphs](file:///aptitude/di/bar-and-line-graphs.md)
- **Core Topics:** Single/grouped/stacked bar charts, dual-axis line charts, secondary axis scaling, index re-basing, CAGR, volume vs value divergence.
- **Key Traps:** Left vs right Y-axis misattribution, non-zero truncated baselines, deceptive visual slopes.
- **Problem Set:** 40 Questions (Levels 1–8) with complete solutions.

### 2. [Pie Charts](file:///aptitude/di/pie-charts.md)
- **Core Topics:** Single pie degree/percentage conversions, concentric doughnuts, multi-year share shifts, sub-category decomposition.
- **Key Traps:** Expanding percentage on a shrinking total base (Small-Base Fallacy), degree vs percent symbol confusion.
- **Problem Set:** 40 Questions (Levels 1–8) with complete solutions.

### 3. [Tables and Caselets](file:///aptitude/di/tables-and-caselets.md)
- **Core Topics:** Dense multi-column financial statements, fleet routing matrices, SaaS cohort retention grids, conditional filtering.
- **Key Traps:** Denominator misidentification, selective row exclusion, subtle footnote constraints.
- **Problem Set:** 40 Questions (Levels 1–8) with complete solutions.

### 4. [Mixed Graphs](file:///aptitude/di/mixed-graphs.md)
- **Core Topics:** Bar + Line + Pie cross-chart reconciliation, production-cost-profit pipelines, yield optimization.
- **Key Traps:** Mismatched time horizons between charts, inconsistent currency/metric units across sources.
- **Problem Set:** 40 Questions (Levels 1–8) with complete solutions.

### 5. [Data Sufficiency](file:///aptitude/di/data-sufficiency.md)
- **Core Topics:** 2-Statement & 3-Statement sufficiency, geometric/algebraic uniqueness proofs, sufficiency vs calculability.
- **Key Traps:** Statement 1 bias (carrying over Statement 1 assumptions into Statement 2), positive/negative root ambiguity.
- **Problem Set:** 40 Questions (Levels 1–8) with complete solutions.

### 6. [Missing Data DI](file:///aptitude/di/missing-data-di.md)
- **Core Topics:** Row/column sum conservation, inventory balance equations, single degree-of-freedom sweep, multi-cell linked systems.
- **Key Traps:** Over-specifying equations, circular dependency loops, sign inversion in inventory reconciliation.
- **Problem Set:** 40 Questions (Levels 1–8) with complete solutions.

### 7. [Quantitative Caselets](file:///aptitude/di/quantitative-caselets.md)
- **Core Topics:** Translating unstructured descriptive text into algebraic models, multi-echelon supply chains, project scheduling.
- **Key Traps:** Implicit constraints hidden in narrative prose, double-counting intermediate transshipments.
- **Problem Set:** 40 Questions (Levels 1–8) with complete solutions.

### 8. [Advanced DI Caselets](file:///aptitude/di/advanced-di-caselets.md)
- **Core Topics:** McKinsey/Bain/PE standards, LBO debt waterfall modeling, SaaS unit economics, multi-facility logistics dispatch.
- **Key Traps:** Amortization interest tax shields, working capital lead-time drag, multi-product cannibalization.
- **Problem Set:** 40 Questions (Levels 1–8) with complete solutions.

### 9. [Data Comparison](file:///aptitude/di/data-comparison.md)
- **Core Topics:** Absolute vs percentage deltas, percentage point shifts, min-max normalization, Z-scores, Price-Volume-Mix.
- **Key Traps:** Simpson's paradox, small-base mirage, comparing compounding frequencies without standardization.
- **Problem Set:** 40 Questions (Levels 1–8) with complete solutions.

### 10. [Radar and Stacked Area Graphs](file:///aptitude/di/radar-area-graphs.md)
- **Core Topics:** Radial Kiviat geometry, polygon area calculations, stacked area layer subtraction, power grid merit-order dispatch.
- **Key Traps:** Spoke-ordering area illusion (permuting axes changes area by 30%+), wavy baseline optical illusion.
- **Problem Set:** 40 Questions (Levels 1–8) with complete solutions.

---

## 6. Recommended 6-Week Placement Preparation Schedule

```
+-----------------------------------------------------------------------------------+
|                        6-WEEK DI MASTERY STUDY PLAN                               |
+-----------------------------------------------------------------------------------+
| Week     | Modules to Cover                  | Analytical Focus                           |
|----------+-----------------------------------+--------------------------------------------|
| Week 1   | Module 1 (Bar/Line) & 2 (Pie)     | Visual speed, degree conversion, CAGR      |
| Week 2   | Module 3 (Tables) & 4 (Mixed)     | Dense table scanning, cross-chart ties     |
| Week 3   | Module 5 (Data Sufficiency)       | Strict uniqueness proofs, 3-statement logic|
| Week 4   | Module 6 (Missing Data) & 7 (Q-C) | Infill sweeps, narrative algebraic parsing |
| Week 5   | Module 8 (Advanced Consulting)    | PVM, LBO waterfalls, SaaS unit economics   |
| Week 6   | Module 9 (Data Comp) & 10 (Radar) | Normalization, Kiviat geometry, mock speed |
+-----------------------------------------------------------------------------------+
```

---

*Curated for the students of IIT Kanpur preparing for the 2026 Placement Season.*
