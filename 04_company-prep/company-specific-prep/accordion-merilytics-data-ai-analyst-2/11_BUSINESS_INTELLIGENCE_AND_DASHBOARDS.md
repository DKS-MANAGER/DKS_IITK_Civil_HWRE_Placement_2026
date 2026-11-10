# Module 11 — Business Intelligence, Dashboard Design & PE KPIs

In private equity consulting at Accordion (Merilytics), **Business Intelligence (BI) dashboards** (Power BI, Tableau, Excel) are executive decision instruments. They are not decorative charts or dense data dumps; they exist to give portfolio company CFOs and PE operating partners immediate operational visibility into EBITDA drivers, working capital health, and customer risk.

---

## 1. Enterprise BI Philosophy: The Decision-First Principle

Most corporate dashboards fail because of **"Data Dump Syndrome"**—displaying 40 disconnected charts without a clear narrative hierarchy. 

A world-class BI dashboard follows the **Decision-First Principle**:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                               THE DASHBOARD DESIGN PYRAMID                             │
├────────────────────┬───────────────────────────────────┬───────────────────────────────┤
│ Tier 1: Headline   │ Executive KPI Scorecards          │ "Are we winning or losing?"   │
│ (Top 15% Screen)   │ (Revenue, EBITDA, Churn, Cash)    │ Instant red/yellow/green flag │
├────────────────────┼───────────────────────────────────┼───────────────────────────────┤
│ Tier 2: Trend      │ Time-Series & Trajectory Line     │ "Where are we heading?"       │
│ (Middle 45% Screen)│ (12-Mo Trend vs Budget & Prior Yr)│ Momentum & inflection points  │
├────────────────────┼───────────────────────────────────┼───────────────────────────────┤
│ Tier 3: Breakdown  │ Granular Segment Heatmaps & Tables│ "Why is this happening?"      │
│ (Bottom 40% Screen)│ (By Region, SKU, Customer Tier)   │ Operational root-cause triage │
└────────────────────┴───────────────────────────────────┴───────────────────────────────┘
```

### 1.1 Cognitive Layout Architecture (The Z-Pattern Flow)
Executive eyes naturally scan screens in a **Z-pattern** (left-to-right, then top-to-bottom):
- **Top-Left (Highest Priority)**: Primary North Star KPI (e.g., TTM EBITDA or Net Revenue).
- **Top-Right**: Primary Financial Health Check (e.g., Ending Cash Liquidity and Headroom).
- **Center**: Trailing 12-Month Performance vs. Board Budget.
- **Bottom**: Drill-down variance breakdown (e.g., EBITDA bridge walk or customer churn matrix).

---

## 2. Visual Encoding Rules & Common Dashboard Pitfalls

```
┌─────────────────────────────────┬─────────────────────────────────┬─────────────────────────────────┐
│        Analytical Objective     │      Recommended Visual Type    │       Visual Traps to AVOID     │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Trend over Continuous Time      │ Clean Line Chart                │ Spline/curved smoothed lines    │
│                                 │ (Solid line: Actual; Dot: Fcst) │ that distort data points.       │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Discrete Category Comparison    │ Horizontal / Vertical Bar Chart │ Pie charts with > 3 slices;     │
│                                 │ (Sorted descending by value)    │ 3D isometric bar charts.        │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Variance / Bridge Decomposition │ Waterfall Chart                 │ Stacked column charts with      │
│                                 │ (Starting -> Levers -> Ending)  │ positive & negative fluctuations│
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Correlation / Multi-Variable    │ Scatter Plot                    │ Radar / Spider charts           │
│                                 │ (Bubble size = Total Revenue)   │ (hard for human eyes to decode) │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Target vs. Actual Attainment    │ Bullet Graph or Gauge Card      │ Dial gauges with confusing      │
│                                 │ (Target line + Actual bar)      │ multi-colored rainbows.         │
└─────────────────────────────────┴─────────────────────────────────┴─────────────────────────────────┘
```

---

## 3. Eight Essential Private Equity Executive KPIs

Candidates must understand how to calculate, interpret, and defend these 8 core PE financial and operational metrics:

```
┌───┬───────────────────────────────┬────────────────────────────────────────────────────────┬────────────────────────────────────────┐
│ # │             KPI               │                   Mathematical Formula                 │            Target Benchmark            │
├───┼───────────────────────────────┼────────────────────────────────────────────────────────┼────────────────────────────────────────┤
│ 1 │ LTV : CAC Ratio               │ \frac{\text{Gross Margin} \times \text{ARPU} / \text{Churn}}{\text{Customer Acquisition Cost}} │ > 3.0× (Healthy); < 1.0× (Destroying $)│
├───┼───────────────────────────────┼────────────────────────────────────────────────────────┼────────────────────────────────────────┤
│ 2 │ CAC Payback Period            │ \frac{\text{CAC}}{\text{ARPU} \times \text{Gross Margin \%}} │ < 12 Months (SaaS); < 18 Mo (Enterprise│
├───┼───────────────────────────────┼────────────────────────────────────────────────────────┼────────────────────────────────────────┤
│ 3 │ Net Revenue Retention (NRR)   │ \frac{\text{Starting ARR} + \text{Expansion} - \text{Contraction} - \text{Churn}}{\text{Starting ARR}} │ > 110% (Best-in-class SaaS); > 100% min│
├───┼───────────────────────────────┼────────────────────────────────────────────────────────┼────────────────────────────────────────┤
│ 4 │ EBITDA Margin %               │ \frac{\text{EBITDA}}{\text{Total Revenue}} \times 100\%│ 20% – 35% (Target expansion lever)     │
├───┼───────────────────────────────┼────────────────────────────────────────────────────────┼────────────────────────────────────────┤
│ 5 │ Days Sales Outstanding (DSO)  │ \frac{\text{Accounts Receivable}}{\text{Credit Sales}} \times \text{Days} │ < 45 Days (Working capital efficiency) │
├───┼───────────────────────────────┼────────────────────────────────────────────────────────┼────────────────────────────────────────┤
│ 6 │ Cash Conversion Cycle (CCC)   │ \text{DIO} + \text{DSO} - \text{DPO}                   │ Lower is better; negative CCC is ideal │
├───┼───────────────────────────────┼────────────────────────────────────────────────────────┼────────────────────────────────────────┤
│ 7 │ Rule of 40 (SaaS)             │ \text{Revenue Growth \%} + \text{EBITDA Margin \%}     │ \ge 40\% (High valuation multiple)     │
├───┼───────────────────────────────┼────────────────────────────────────────────────────────┼────────────────────────────────────────┤
│ 8 │ Magic Number (Sales Engine)   │ \frac{(\text{Quarterly ARR}_t - \text{Quarterly ARR}_{t-1}) \times 4}{\text{Quarterly S\&M Expense}_{t-1}} │ > 1.0× (Accelerate sales spend); < 0.75│
└───┴───────────────────────────────┴────────────────────────────────────────────────────────┴────────────────────────────────────────┘
```

---

## 4. End-to-End Executive Dashboard Blueprint

**Client Engagement**: Private Equity Turnaround Audit of *Apex Industrial Supplies* (\$180M Revenue Manufacturer).

```
========================================================================================================================
EXECUTIVE DASHBOARD: THE OFFICE OF THE CFO | PORTFOLIO PERFORMANCE MONITOR
========================================================================================================================
[1. HEADLINE CARDS]
┌───────────────────────────┐ ┌───────────────────────────┐ ┌───────────────────────────┐ ┌───────────────────────────┐
│ Net Revenue (TTM)         │ │ EBITDA (TTM)              │ │ Working Capital DSO       │ │ Customer Net Churn Rate   │
│ $182.4M (+8.2% vs Budget) │ │ $29.2M (16.0% Margin)     │ │ 52.4 Days (-4.2 Days MoM) │ │ 6.8% (Target < 8.0%)      │
│ [Green Up Arrow]          │ │ [Yellow Warning: -120 bps]│ │ [Green Down Arrow: Good]  │ │ [Green Circle: Stable]    │
└───────────────────────────┘ └───────────────────────────┘ └───────────────────────────┘ └───────────────────────────┘

[2. PERFORMANCE TREND: 12-MONTH REVENUE & EBITDA TRAJECTORY]
Monthly Revenue ($M) vs Budget Line | Monthly EBITDA Margin % (Secondary Right Axis)
• Jan to Jul: Strong 9.5% volume growth, margins steady at 17.5%.
• Aug to Oct: Inflation spike in raw resin compressed Gross Margin from 58% to 52%, dragging EBITDA.
• Nov to Dec: Surcharge pricing implementation restored margin to 16.0%.

[3. ROOT CAUSE BREAKDOWN: EBITDA BRIDGE (WALK FROM BUDGET TO ACTUAL)]
Waterfall Chart ($M Variance):
Budget EBITDA ($32.0M) 
  + Volume Expansion (+$3.4M) 
  + Base Price Increase (+$2.1M) 
  - Raw Material Resin Cost Inflation (-$5.2M) 
  - Freight Surcharges (-$1.8M) 
  - Overtime Labor Overruns (-$1.3M) 
= Actual EBITDA ($29.2M) [Net Deficit: -$2.8M]

[4. DRILL-DOWN: CUSTOMER CONCENTRATION & DSO MATRIX]
• Top 10 Customers generate 48% of total revenue.
• Customer C (Apex's largest automotive client, $14M ARR) has DSO at 88 days (38 days overdue).
• Actionable Recommendation: Enforce 2/10 Net 30 early payment discounts to unlock $3.5M in immediate trapped cash.
========================================================================================================================
```

