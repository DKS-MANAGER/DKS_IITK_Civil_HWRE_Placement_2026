# Module 04 — Advanced Excel & Financial/Business Modelling

## 1. Consulting Excel Standards & Best Practices

In Private Equity consulting at Accordion (Merilytics), spreadsheets are client-facing corporate deliverables. Models must be auditable, dynamic, structurally sound, and adhere to universal financial modeling conventions.

### 1.1 Universal Cell Formatting & Color-Coding Rules
```
┌─────────────────────────┬──────────────────────┬────────────────────────────────────────────────────────┐
│        Cell Type        │      Font Color      │                     Fill / Style                       │
├─────────────────────────┼──────────────────────┼────────────────────────────────────────────────────────┤
│ Hardcoded Inputs        │ Blue (#0000FF)       │ Clean white background (no fill)                       │
├─────────────────────────┼──────────────────────┼────────────────────────────────────────────────────────┤
│ Internal Formulas       │ Black (#000000)      │ Standard transparent / white                           │
├─────────────────────────┼──────────────────────┼────────────────────────────────────────────────────────┤
│ Cross-Sheet Links       │ Green (#008000)      │ Indicates calculation references another worksheet     │
├─────────────────────────┼──────────────────────┼────────────────────────────────────────────────────────┤
│ External Workbook Links │ Red (#FF0000)        │ Warning: Depends on external files (minimize use)      │
├─────────────────────────┼──────────────────────┼────────────────────────────────────────────────────────┤
│ Scenario Toggles / Drop │ Bold Navy (#002060)  │ Soft yellow fill (#FFF2CC) with data validation border  │
├─────────────────────────┼──────────────────────┼────────────────────────────────────────────────────────┤
│ Key KPI Output Headers  │ White (#FFFFFF)      │ Dark Navy fill (#1F4E78), Bold, Top/Bottom double line │
└─────────────────────────┴──────────────────────┴────────────────────────────────────────────────────────┘
```

### 1.2 Core Architectural Principles
1. **Never Hardcode Constants in Formulas**: Never write `=C14 * 1.05`. Always write `=C14 * (1 + $C$5)` where `$C$5` is a documented assumption cell.
2. **One Row, One Formula**: Across any time-series row (e.g., Month 1 to Month 12), the formula in every column must be structurally identical.
3. **Reconciliation Checks**: Every model must feature automated integrity checks (e.g., `=IF(ROUND(Total_Assets - Total_Liab_Equity, 2) = 0, "OK", "ERROR")`).

---

## 2. Essential Excel Functions for Financial Analytics

```
┌──────────────────────┬─────────────────────────────────────────────────┬─────────────────────────────────────────────────────┐
│       Function       │                     Syntax                      │                   PE Consulting Use Case            │
├──────────────────────┼─────────────────────────────────────────────────┼─────────────────────────────────────────────────────┤
│ XLOOKUP              │ =XLOOKUP(lookup, lookup_rng, return_rng, [if_not])│ Look up pricing, customer terms, or SKU costs.      │
├──────────────────────┼─────────────────────────────────────────────────┼─────────────────────────────────────────────────────┤
│ INDEX + MATCH        │ =INDEX(return_rng, MATCH(val, lookup_rng, 0))   │ 2D matrix lookups (Territory vs. Sales Tier quota). │
├──────────────────────┼─────────────────────────────────────────────────┼─────────────────────────────────────────────────────┤
│ SUMIFS               │ =SUMIFS(sum_rng, crit_rng1, crit1, crit_rng2, c2)│ Aggregate monthly sales by customer & product SKU.  │
├──────────────────────┼─────────────────────────────────────────────────┼─────────────────────────────────────────────────────┤
│ CHOOSE / SWITCH      │ =CHOOSE($C$2, Base_Val, Bull_Val, Bear_Val)     │ Dynamic scenario toggles for portfolio valuation.   │
├──────────────────────┼─────────────────────────────────────────────────┼─────────────────────────────────────────────────────┤
│ XNPV / XIRR          │ =XNPV(rate, cash_flows, dates)                  │ Precise discounted cash flows with irregular dates. │
├──────────────────────┼─────────────────────────────────────────────────┼─────────────────────────────────────────────────────┤
│ FILTER / UNIQUE      │ =FILTER(array, include, [if_empty])             │ Dynamic extraction of high-churn customer accounts. │
├──────────────────────┼─────────────────────────────────────────────────┼─────────────────────────────────────────────────────┤
│ LET                  │ =LET(rev, A1*B1, cogs, rev*0.6, rev - cogs)     │ Complex financial formulas with named variables.    │
└──────────────────────┴─────────────────────────────────────────────────┴─────────────────────────────────────────────────────┘
```

### 2.1 Deep-Dive: Two-Way Lookups with INDEX & MATCH
While `XLOOKUP` is modern, PE legacy models frequently use `INDEX-MATCH-MATCH` for 2D matrix lookups (e.g., extracting gross margin given a dynamic Product Row and Region Column):

```excel
=INDEX($C$5:$G$20, MATCH($B$25, $B$5:$B$20, 0), MATCH($C$24, $C$4:$G$4, 0))
```
- `MATCH($B$25, $B$5:$B$20, 0)` finds the row index corresponding to the selected Product.
- `MATCH($C$24, $C$4:$G$4, 0)` finds the column index corresponding to the selected Region.
- `INDEX` extracts the exact intersection value.

---

## 3. Advanced Financial Modeling Techniques

### 3.1 Two-Way Sensitivity Data Tables
A two-way sensitivity table evaluates how a primary outcome metric (e.g., Year 1 EBITDA or Enterprise Value) responds across a matrix of two independent variables (e.g., Unit Selling Price vs. Customer Churn Rate).

#### Step-by-Step Construction:
1. In cell `B4`, reference the primary model output formula: `=Summary!C30` (e.g., Portco EBITDA).
2. Set horizontal column headers across `C4:G4` with Unit Price variations (\$90, \$95, \$100, \$105, \$110).
3. Set vertical row headers down `B5:B9` with Churn Rate variations (4%, 6%, 8%, 10%, 12%).
4. Select the full matrix range `B4:G9`.
5. Navigate to: `Data` $\rightarrow$ `What-If Analysis` $\rightarrow$ `Data Table...`
6. In **Row Input Cell**, select the model's Price input cell (`Assumptions!C8`).
7. In **Column Input Cell**, select the model's Churn input cell (`Assumptions!C12`).
8. Excel calculates the 25 iterations. Apply conditional formatting (Soft Green to Soft Red heatmap).

### 3.2 Dynamic Scenario Switching Architecture
Build a single master model that dynamically re-computes under Bull, Base, and Bear conditions without overwriting cells:

```excel
Cell C2: Dropdown Menu [1 = Bear Case | 2 = Base Case | 3 = Bull Case]

Cell C6 (Annual Organic Revenue Growth):
=CHOOSE($C$2, 2.5%, 8.0%, 15.0%)

Cell C7 (Gross Margin %):
=CHOOSE($C$2, 52.0%, 58.0%, 64.0%)

Cell C8 (Working Capital % of Revenue):
=CHOOSE($C$2, 18.0%, 14.0%, 11.0%)
```

### 3.3 Goal Seek & Solver for Operational Optimization
- **Goal Seek**: Determine the exact price cut required to expand volume enough to achieve \$25M EBITDA:
  - `Set cell`: `EBITDA_Cell`
  - `To value`: `25000000`
  - `By changing cell`: `Unit_Price_Cell`
- **Solver**: Optimize plant production across 4 product lines to maximize gross margin subject to raw material and labor constraints:
  - `Objective`: Maximize Total Contribution Margin.
  - `By Changing Variable Cells`: Monthly units produced per line.
  - `Constraints`: Machine hours $\le 4,000$; Labor hours $\le 12,000$; Minimum contract delivery $\ge 500$ units per line.

---

## 4. Practical Financial Models for Private Equity

### 4.1 The 13-Week Cash Flow Forecast (TWCF)
In PE distress or turnaround engagements, cash is king. The 13-Week Cash Flow forecast models direct cash inflows and outflows on a weekly basis:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 13-WEEK CASH FLOW FORECAST ARCHITECTURE                                │
├────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ Line Item                   | Formula / Source              | W1 (Actual) | W2 (Fcst) | ... | W13 (Fcst)│
├─────────────────────────────┼───────────────────────────────┼─────────────┼───────────┼─────┼───────────┤
│ Beginning Cash Balance      | Prior Week Ending Cash        |   $12,500   |   $11,800 |     |   $14,200 │
│ (+) Cash Receipts           | AR Collections + Cash Sales   |    $4,200   |    $4,500 |     |    $5,100 │
│ (-) Operating Cash Outflows | Payroll + Rent + Vendors      |   ($3,800)  |   ($3,900)│     |   ($4,000)│
│ (-) Debt Service            | Scheduled Interest & Principal|   ($1,100)  |      $0   |     |   ($1,100)│
├─────────────────────────────┼───────────────────────────────┼─────────────┼───────────┼─────┼───────────┤
│ Net Weekly Cash Flow        | Receipts - Disbursements      |     ($700)  |     +$600 |     |      $0   │
│ Ending Cash Balance         | Beginning + Net Cash Flow     |   $11,800   |   $12,400 |     |   $14,200 │
│ Minimum Required Liquidity  | Revolver covenant threshold   |    $8,000   |    $8,000 |     |    $8,000 │
│ Liquidity Buffer / Headroom | Ending Cash - Min Liquidity   |    $3,800   |    $4,400 |     |    $6,200 │
└─────────────────────────────┴───────────────────────────────┴─────────────┴───────────┴─────┴───────────┘
```

### 4.2 The EBITDA Bridge Model (Walk)
PE sponsors require an EBITDA bridge decomposing the variance between Budget and Actual performance across 5 fundamental levers:

$$\Delta \text{EBITDA} = \Delta \text{Volume} + \Delta \text{Price} + \Delta \text{Mix} + \Delta \text{COGS/Cost} + \Delta \text{SG\&A}$$

```excel
1. Volume Impact: (Actual Volume - Budget Volume) * Budget Unit Contribution Margin
2. Price Impact: (Actual Price - Budget Price) * Actual Volume
3. Mix Impact: Actual Total Volume * SUM((Actual Mix% - Budget Mix%) * Budget Margin)
4. Cost Impact: (Budget Unit Cost - Actual Unit Cost) * Actual Volume
5. SG&A Impact: Budget SG&A - Actual SG&A
```

