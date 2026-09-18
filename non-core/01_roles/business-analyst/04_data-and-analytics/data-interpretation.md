# Business Data Interpretation for Business Analysts

> Frameworks for evaluating business dashboards, telemetry charts, cohort retention heatmaps, and funnel drop-off analytics.

---

## 1. Structured Chart Deconstruction Framework

When presented with an analytical chart or table in an interview:
1. **Orientation**: Verify axes, units (Absolute vs. Percentage, Currency, Thousands/Millions), and time windows.
2. **Baseline & Trends**: Establish the normal operating baseline and identify inflections, step-changes, or seasonal cycles.
3. **Segmentation Drill-Down**: Slice high-level aggregates across sub-dimensions (Geography, Platform, User Persona, Acquisition Channel).
4. **Synthesis & Root Cause**: Formulate testable business hypotheses explaining anomalies.

---

## 2. Core Business Chart Archetypes

### Funnel Analytics
- **Stage Progression**: Impressions $\to$ Visits $\to$ Product Views $\to$ Add-to-Cart $\to$ Checkout $\to$ Payment Success.
- **Drop-off Diagnosis**: Identifying the single transition with highest relative % attrition and analyzing UX/technical blockers.

### Cohort Retention Heatmaps
- **Cohort Grouping**: Group users by acquisition month (e.g., Jan 2026 Cohort).
- **Decay Curves**: Track % active across Month 0, Month 1, Month 2...
- **Plateau Analysis**: Identifying whether the retention curve flattens out (indicating product-market fit) or decays to zero.

### Waterfall Charts
- **Step-wise Decomposition**: Visualizing step changes from Gross Revenue $\to$ Net Revenue $\to$ Gross Profit $\to$ EBITDA $\to$ Net Profit.
