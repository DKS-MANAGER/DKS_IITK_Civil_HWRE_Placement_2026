# Module 17: MS Excel, PowerPoint & Commercial Storytelling

> **Document Status**: Production-Grade Executive Reference `[TIER 2 / CONSULTING STANDARDS & TIER 4 / EXECUTIVE COMMUNICATION]`  
> **Core Focus**: Advanced Excel (XLOOKUP, Power Query, Solver), Slide Architecture, Data Storytelling, and Complete 6-Slide MMM Client Deck Blueprint  
> **Target Role**: Analyst (IQVIA India)  

---

## 1. Advanced MS Excel for Commercial Analytics

While code is developed in Python and SQL, the primary deliverable medium shared with pharmaceutical brand managers and onshore consulting directors is **Microsoft Excel**.

### 1.1 Essential Formula Architecture
* **`XLOOKUP` (Modern Replacement for VLOOKUP / HLOOKUP)**:
  `=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])`
  * Eliminates fragile hardcoded column index numbers; defaults to exact match; allows leftward lookups.
* **`INDEX-MATCH` (The Legacy Gold Standard)**:
  `=INDEX(return_range, MATCH(lookup_value, lookup_range, 0))`
  * Computationally faster than VLOOKUP across 100,000+ rows; robust to inserted columns.
* **Multi-Condition Aggregations**:
  `=SUMIFS(Brand_TRx_Range, Territory_Range, "Northeast", Specialty_Range, "Oncology")`

### 1.2 Interactive Dashboard Engineering
1. **Pivot Tables & Calculated Fields**:
   * Layout: Tabular form with subtotals at the bottom of groups.
   * Calculated Field: `='Brand TRx' / 'Market TRx'` to dynamically compute brand market share.
2. **Slicers & Timelines**: Connecting multiple pivot tables to unified interactive slicers for territory, specialty, and product brand filters.
3. **Power Query (M Language)**: Automating the ingestion, merging, and unpivoting of 52 weekly CSV transaction reports into a single consolidated schema with a single click (`Data > Refresh All`).

### 1.3 Optimization via Excel Solver Add-In
* **Setting up Marketing Reallocation**:
  * Set Objective: Cell `$E$10` (Total Net Brand Revenue) $\to$ `Max`.
  * By Changing Variable Cells: `$B$2:$B$5` (Promotional Channel Spends).
  * Subject to Constraints:
    * `$E$6 = $H$1` (Total Spend = Total Available Budget).
    * `$B$2 >= 1000000` (Minimum Field Force Contractual Requirement).
    * `$B$3 <= 2500000` (Maximum Digital Spend Capacity).
  * Solving Method: `GRG Nonlinear` (for Hill saturation curves) or `Simplex LP` (for linear response).

---

## 2. Consulting Slide Architecture & Visual Hierarchy

In client-facing delivery, a slide should never merely display data; it must communicate an **insight that drives a business decision**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       THE PYRAMID SLIDE ARCHITECTURE                        │
├─────────────────────────────────────────────────────────────────────────────┤
│ **ACTION TITLE**: Reallocate $1.5M from Medical Congresses to Digital Video │
│                  to capture $4.2M in incremental net brand revenue.         │
├──────────────────────────────────────┬──────────────────────────────────────┤
│ LEAD VISUAL / CHART (60% Area)       │ STRATEGIC TAKEAWAYS (40% Area)       │
│                                      │                                      │
│ [ Water-fall Chart or Saturation     │ • **Channel Saturation**: Detailing  │
│   Response Curve showing current vs  │   has reached the 88% plateau of its │
│   optimal spend allocation ]         │   Hill curve (mROI = $0.85 per $1).  │
│                                      │ • **Digital Opportunity**: Digital   │
│                                      │   video is operating at steep initial│
│                                      │   slope (mROI = $3.80 per $1).       │
│                                      │ • **Net Financial Impact**: Portfolio│
│                                      │   ROI increases from 2.8x to 3.4x.   │
├──────────────────────────────────────┴──────────────────────────────────────┤
│ FOOTNOTE / DATA SOURCE: Source: IQVIA NPA Audit, Xponent® (Q1 2024–Q4 2025).│
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Chart Selection Taxonomy for Commercial Presentations

| Analytical Objective | Preferred Chart Type | Avoid Using |
| :--- | :--- | :--- |
| **Sales Trend Over Time** | Line Chart with rolling 4-week smoothed trendline. | 3D Line Chart or Area Chart with obscured layers. |
| **Channel Contribution Breakdown**| 100% Horizontal Stacked Bar Chart with data labels. | Pie Charts with $> 4$ slices (hard to compare angles).|
| **Gross-to-Net (GTN) Price Erosion**| **Waterfall Chart** (List Price $\to$ Rebates $\to$ Net Price). | Clustered Column Chart (obscures cumulative cascade).|
| **Physician Detailing Response Curve**| Scatter Plot with non-linear fitted Hill saturation curve.| Line chart connecting discrete noisy weekly points. |
| **Sales Territory Performance** | Heatmap or Horizontal Bar Chart ordered by volume. | Alphabetic Bar Chart (forces viewer to scan for top). |

---

## 4. Complete 6-Slide Executive MMM Client Deck Blueprint

*This blueprint provides the exact verbatim structure to present Marketing Mix Modelling findings to a Brand Director or Chief Commercial Officer:*

### Slide 1: Executive Summary & Strategic Context
* **Action Title**: *Brand OncoRelief achieved \$48.2M in annual revenue; promotional reallocation can unlock +\$3.8M without expanding budget.*
* **Content**: 3 key KPI callout cards: (1) Total 2025 Revenue (\$48.2M, $+8\%$ YoY), (2) Overall Promotional ROI (\$3.10 net return per \$1 spent), (3) Optimization Opportunity (+\$3.8M incremental revenue via channel rebalancing).

### Slide 2: Econometric Model Methodology & Calibration
* **Action Title**: *Multi-channel econometric regression demonstrates high predictive validity ($R^2 = 0.91$) with verified carryover.*
* **Content**: Visual schematic showing raw spends feeding into Geometric Adstock decay ($\lambda_{\text{detail}} = 0.70, \lambda_{\text{digital}} = 0.30$) and Hill saturation curves. Model diagnostics callout box confirming Durbin-Watson $= 1.94$ and all VIF values $< 3.5$.

### Slide 3: Sales Volume Decomposition: Baseline vs Promotion
* **Action Title**: *Baseline brand equity drives 74% of prescription volume; active promotion generated 26% of annual revenue.*
* **Content**: Horizontal stacked bar decomposing 320,000 total prescriptions:
  * Baseline (Organic Refills & Disease Prevalence): 236,800 TRx ($74.0\%$).
  * Field Detailing Contribution: 51,200 TRx ($16.0\%$).
  * Digital Channels Contribution: 22,400 TRx ($7.0\%$).
  * Medical Congresses: 9,600 TRx ($3.0\%$).

### Slide 4: Channel Efficiency & Return on Investment (ROI)
* **Action Title**: *Digital engagement delivers the highest average ROI (\$5.25), while detailing drives the largest absolute volume.*
* **Content**: Grouped bar chart comparing Total Spend vs Average ROI vs Marginal ROI across channels:
  * Detailing: Spend \$6.0M | Avg ROI \$3.20 | Marginal ROI \$1.15
  * Digital: Spend \$1.5M | Avg ROI \$5.25 | Marginal ROI \$2.80
  * Congresses: Spend \$1.0M | Avg ROI \$1.80 | Marginal ROI \$0.65

### Slide 5: The Optimization Recommendation: Portfolio Reallocation
* **Action Title**: *Reallocating \$800k from Congresses and mature Detailing into Digital expands net margin by \$3.8M.*
* **Content**: Before vs After spend allocation waterfall. Highlight that Congress spending has passed its inflection point (diminishing marginal returns), whereas Digital operates on the steep upward slope of its response curve.

### Slide 6: Governance, Implementation Roadmap & Risk Mitigation
* **Action Title**: *Phased Q1–Q4 rollout ensures contractual sales-force compliance while scaling digital automation.*
* **Content**: 4-quarter Gantt implementation timeline with risk mitigation callouts: (1) Minimum contractually committed rep calls preserved in Tier 1 territories, (2) Closed-loop CRM feedback instituted to track monthly digital response velocity.

