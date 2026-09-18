# 04. Business Analyst: Excel & Spreadsheet Mastery

> Operational guide, essential function reference, and 10 hands-on placement drills for Excel assessments and modeling rounds.

---

## 1. High-Yield Excel Functions Reference

```text
                             EXCEL CORE FUNCTION MAP
┌─────────────────────────┬─────────────────────────┬─────────────────────────┐
│     LOOKUPS & DATA      │      AGGREGATION        │     LOGIC & DATES       │
├─────────────────────────┼─────────────────────────┼─────────────────────────┤
│ • XLOOKUP               │ • SUMIFS                │ • IF / IFS              │
│ • INDEX / MATCH         │ • COUNTIFS              │ • IFERROR               │
│ • VLOOKUP (Exact Match) │ • AVERAGEIFS            │ • DATEDIF               │
│ • FILTER / UNIQUE       │ • SUMPRODUCT            │ • EOMONTH / EDATE       │
└─────────────────────────┴─────────────────────────┴─────────────────────────┘
```

### Essential Functions with Placement Syntax:
1. **`XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode])`**:
   - Modern replacement for VLOOKUP/HLOOKUP. Does not break when columns move.
   - Example: `=XLOOKUP(A2, Customers!A:A, Customers!D:D, "Unknown Customer")`
2. **`INDEX(array, MATCH(lookup_val, lookup_col, 0))`**:
   - Universal lookup compatible with all legacy Excel versions.
   - Example: `=INDEX(Prices!C:C, MATCH(B2, Prices!A:A, 0))`
3. **`SUMIFS(sum_range, criteria_range1, criteria1, criteria_range2, criteria2)`**:
   - Multi-criteria aggregation.
   - Example: `=SUMIFS(Orders!E:E, Orders!B:B, "Delivered", Orders!C:C, ">=2026-01-01")`
4. **`SUMPRODUCT(array1, array2)`**:
   - Weighted average and conditional matrix multiplication without array formulas.
   - Weighted Price: `=SUMPRODUCT(Prices, Volumes) / SUM(Volumes)`
5. **`EOMONTH(start_date, months)`**:
   - Returns last day of month. Useful for cohort date grouping.

---

## 2. 10 Hands-On Excel Placement Drills

### Drill 01: Data Cleaning & Deduplication (10 mins)
- **Task**: Given a messy 5,000-row export with trailing spaces, mixed text cases, and duplicate customer records:
  1. Trim whitespace: `=TRIM(CLEAN(A2))`
  2. Standardize text: `=PROPER(B2)`
  3. Extract Domain from Email: `=MID(C2, FIND("@", C2)+1, LEN(C2))`
  4. Flag duplicate transactions using `=IF(COUNTIF($A$2:A2, A2)>1, "Duplicate", "Unique")`.

### Drill 02: Building a Multi-Criteria KPI Dashboard (15 mins)
- **Task**: Given a transaction table `(Order_ID, Date, Customer_ID, Category, Revenue, Margin_INR, Status)`:
  1. Build summary table calculating Total Revenue, Total Margin, and Average Margin % for "Delivered" orders per Category.
  2. Formula: `=SUMIFS(Orders!E:E, Orders!D:D, A2, Orders!G:G, "Delivered")`

### Drill 03: Cohort Retention Table using Pivot Tables (15 mins)
- **Task**:
  1. Add helper column `First_Order_Month` using `=TEXT(MINIFS(Orders!B:B, Orders!C:C, Orders!C2), "YYYY-MM")`.
  2. Add `Order_Month` using `=TEXT(Orders!B2, "YYYY-MM")`.
  3. Create Pivot Table: Rows = `First_Order_Month`, Columns = `Order_Month`, Values = `Distinct Count of Customer_ID`.

### Drill 04: E-Commerce Sales Funnel Analysis (10 mins)
- **Task**: Compute conversion rates across 4 stages: `Visits -> Product Views -> Add to Cart -> Checkout Completed`.
- Calculate Step-to-Step Drop-off % and Overall Conversion Rate.

### Drill 05: Dynamic Pricing & Margin Simulator (15 mins)
- **Task**: Build a dynamic price elasticity simulator where changing Price by $\pm 5\%, \pm 10\%$ dynamically updates Estimated Volume based on assumed elasticity ($E_d = -1.5$), computing new Total Revenue and Gross Profit.

### Drill 06: Break-Even Capacity Utilization Model (10 mins)
- **Task**: Calculate Break-Even Units and Break-Even Revenue given Fixed Costs ($F = 25	ext{ Lakh}$), Unit Price ($P = 850$), and Unit Variable Cost ($V = 450$).
- $Q_{	ext{BE}} = rac{2,500,000}{850 - 450} = 6,250	ext{ units}$.

### Drill 07: 2-Variable Sensitivity Data Table (10 mins)
- **Task**: Create a $5 	imes 5$ sensitivity matrix calculating EBITDA when Unit Selling Price varies from 800 to 1,200 INR (row) and Raw Material Cost varies from 300 to 500 INR (column) using Excel `Data -> What-If Analysis -> Data Table`.

### Drill 08: Financial Reconciliation & Discrepancy Matching (10 mins)
- **Task**: Match bank statement settlement credits against internal payment gateway records using `XLOOKUP` with Boolean discrepancy flags `=IF(ABS(Bank_Amt - Internal_Amt) > 0.01, "Mismatch", "Reconciled")`.

### Drill 09: Month-over-Month (MoM) Growth & Waterfall Analysis (10 mins)
- **Task**: Calculate absolute MoM growth, percentage MoM growth, and 3-month rolling moving average using `=AVERAGE(B2:B4)`.

### Drill 10: Executive KPI Summary Deck (15 mins)
- **Task**: Combine Summary Cards (Revenue, GMV, Orders, AOV, Gross Margin), a Top-10 Customer bar chart, and conditional formatting heatmap into a single print-ready executive view.
