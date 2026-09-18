# 04. Management Consulting: Tools & Technical Stack

> Operational guide to the quantitative models, spreadsheet architectures, executive slide structures, and mental math systems required for consulting recruitment and casework.

---

## 1. Advanced Excel & Business Modeling

Consulting analysts and associates must build transparent, audit-ready financial and operational models.

```text
                           EXCEL MODEL ARCHITECTURE
┌─────────────────────────┐     ┌─────────────────────────┐     ┌─────────────────────────┐
│     INPUTS & DRIVERS    │ ──> │   CALCULATION ENGINE    │ ──> │    EXECUTIVE SUMMARY    │
│  (Hardcoded Blue Text,  │     │   (Dynamic Formulas,    │     │   (KPI Dashboard,       │
│   Assumptions Table)    │     │    Modular Schedules)   │     │    Sensitivity Matrix)  │
└─────────────────────────┘     └─────────────────────────┘     └─────────────────────────┘
```

### Essential Function Library
| Category | Key Functions | High-Yield Placement Use Case |
|:---|:---|:---|
| **Lookups & Indexing** | `XLOOKUP`, `INDEX(MATCH, MATCH)` | Merging operational cost datasets across disparate plant locations |
| **Aggregation with Criteria** | `SUMIFS`, `COUNTIFS`, `AVERAGEIFS` | Segmenting revenue by customer cohort, product SKU, or geographic tier |
| **Logic & Error Handling** | `IF`, `IFS`, `IFERROR`, `SWITCH` | Scenario toggles (Base, Bull, Bear cases) without formula breakdown |
| **Financial Calculations** | `NPV`, `XNPV`, `IRR`, `XIRR`, `PMT` | Capital budgeting for plant expansion, battery swapping station payback |
| **Matrix & Sensitivity** | `Data Tables` (1-variable & 2-variable) | Generating sensitivity tables for Price vs. Volume EBITDA impacts |

### Timed Excel Modeling Drills
1. **Unit Economics Drill (15 mins)**: Build a dynamic model calculating Customer Lifetime Value ($LTV = rac{ARPU 	imes 	ext{Gross Margin}}{	ext{Churn Rate}}$) and $LTV / CAC$ ratio across 3 customer tiers with sensitivity to CAC inflation.
2. **Break-Even & Operating Leverage Drill (15 mins)**: Model fixed vs. variable cost structures for a manufacturing plant to determine operating leverage $\left(rac{\% \Delta 	ext{EBIT}}{\% \Delta 	ext{Revenue}}ight)$ and break-even capacity utilization.

---

## 2. PowerPoint & Executive Storylining

Consulting presentations follow strict structural standards designed for C-level consumption.

```text
                    ANATOMY OF A CONSULTING SLIDE (SCR FRAMEWORK)
┌──────────────────────────────────────────────────────────────────────────────────────────┐
│ ACTION TITLE (Lead): Renegotiating regional logistics contracts will recover 320 Cr INR   │
│                      EBITDA within 6 months by capping freight radius at 200 km.         │
├────────────────────────────────────────┬─────────────────────────────────────────────────┤
│ EXHIBIT / DATA VISUALIZATION           │ EXECUTIVE SYNTHESIS & KEY TAKEAWAYS             │
│ [Waterfall Chart / Freight Cost Breakdown]│ • Freight cost per bag rose from 60 -> 76 INR.   │
│                                        │ • 80% of escalation driven by out-of-zone routes│
│                                        │ • Action: Terminate 42 low-margin distributors. │
├────────────────────────────────────────┴─────────────────────────────────────────────────┤
│ FOOTER / SOURCE: Client ERP data FY24-FY26; Field audit of 18 Southern distribution hubs.│
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

### Core Slide Design Rules:
1. **Action Titles**: Never use category headers (e.g., *"Cost Analysis"*). Use declarative conclusion titles (e.g., *"Logistics Costs Increased 26% Due to Sub-Optimal Rail-to-Road Split"*).
2. **Horizontal & Vertical Flow**:
   - **Horizontal (Lead)**: Reading across slide action titles tells a complete, logical narrative.
   - **Vertical (Proof)**: Every chart and bullet directly validates the action title above it.
3. **MECE Exhibit Layouts**: Use 2-column or 3-column structured comparisons, waterfall bridges, or 2x2 prioritization matrices (Effort vs. Impact).

---

## 3. Quantitative Mental Math & Speed Arithmetic

In live case interviews, candidates must calculate rapidly without paper or Excel.

### Mental Math Shortcuts & Fast Formulas
| Mathematical Target | Formula / Shortcut | Real-World Consulting Example |
|:---|:---|:---|
| **Rule of 72 (Doubling Time)** | $t pprox rac{72}{g\%}$ | At 8% annual growth, a 500 Cr market doubles in $rac{72}{8} = 9$ years (1,000 Cr). |
| **CAGR Approximation** | $	ext{CAGR} pprox rac{	ext{Total Growth } \%}{n} 	imes 0.9$ | Market grows 80% over 5 years $ightarrow 	ext{CAGR} pprox rac{80}{5} 	imes 0.9 pprox 14.4\%$. |
| **Fractions to Percentages** | Memorize $rac{1}{6}=16.67\%, rac{1}{7}=14.28\%, rac{1}{8}=12.5\%, rac{1}{12}=8.33\%$ | $rac{5}{7} 	imes 490 = 5 	imes 70 = 350	ext{ Cr INR}$. |
| **Contribution Margin** | $	ext{CM} = rac{	ext{Price} - 	ext{Variable Cost}}{	ext{Price}}$ | Price = 50 INR, VC = 35 INR $ightarrow 	ext{CM} = rac{15}{50} = 30\%$. |
| **Break-Even Volume** | $Q_{	ext{BE}} = rac{	ext{Fixed Costs}}{	ext{Price} - 	ext{Variable Cost}}$ | Fixed Costs = 6 Cr, Unit Margin = 150 INR $ightarrow Q = rac{60,000,000}{150} = 400,000	ext{ units}$. |
| **Return on Investment (ROI)**| $	ext{ROI} = rac{	ext{Net Annual Benefit}}{	ext{Initial Investment}}$ | Investment = 20 Cr, Savings = 6 Cr/yr $ightarrow 	ext{ROI} = 30\%$, Payback = 3.33 yrs. |

### 5-Minute Daily Speed Math Drills
- $18 	imes 24 = (18 	imes 20) + (18 	imes 4) = 360 + 72 = 432$
- $15\%$ of $840	ext{ Cr} = 84 + 42 = 126	ext{ Cr}$
- $3.5	ext{ Million} 	imes 400	ext{ INR} = 1.4	ext{ Billion INR} = 140	ext{ Cr INR}$
- $rac{45	ext{ Cr}}{1.8	ext{ Cr}} = 25	imes$
