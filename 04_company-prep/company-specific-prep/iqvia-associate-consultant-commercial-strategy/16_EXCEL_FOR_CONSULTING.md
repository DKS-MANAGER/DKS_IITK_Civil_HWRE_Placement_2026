# Module 16 — Advanced Excel Financial & Commercial Modeling

## 1. Consulting Excel Standards & Best Practices

In management consulting at IQVIA, spreadsheets are not personal scratchpads; they are client-facing corporate assets. Commercial models must be auditable, transparent, dynamic, and strictly formatted according to universal consulting conventions.

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
1. **Never Hardcode Numbers in Formulas**: Never write `=C14 * 1.05`. Always write `=C14 * (1 + $C$5)` where `$C$5` is a documented inflation or growth rate cell in an Assumptions block.
2. **One Row, One Formula**: Across any time-series row (e.g., Year 1 to Year 10), the formula in every column must be structurally identical. Do not alter formulas mid-row.
3. **Left-to-Right, Top-to-Bottom Flow**: Raw data / assumptions flow from the top or left; calculation engines sit in the middle; executive KPI summaries sit at the top or bottom right.
4. **Dynamic Units in Headers**: Every table header must state units explicitly (e.g., `Patient Volume ('000s)`, `USD Millions ($M)`, `WAC Price ($ / Vial)`).

---

## 2. Essential Excel Functions for Commercial Strategy

```
┌──────────────────────┬─────────────────────────────────────────────────┬─────────────────────────────────────────────────────┐
│       Function       │                     Syntax                      │                   Pharma Use Case                   │
├──────────────────────┼─────────────────────────────────────────────────┼─────────────────────────────────────────────────────┤
│ XLOOKUP              │ =XLOOKUP(lookup, lookup_rng, return_rng, [if_not])│ Look up drug pricing across multi-indication lists. │
├──────────────────────┼─────────────────────────────────────────────────┼─────────────────────────────────────────────────────┤
│ INDEX + MATCH        │ =INDEX(return_rng, MATCH(val, lookup_rng, 0))   │ 2D matrix lookups (Territory vs. Sales Rep quota).   │
├──────────────────────┼─────────────────────────────────────────────────┼─────────────────────────────────────────────────────┤
│ SUMIFS               │ =SUMIFS(sum_rng, crit_rng1, crit1, crit_rng2, c2)│ Aggregate script volumes by HCP specialty & region. │
├──────────────────────┼─────────────────────────────────────────────────┼─────────────────────────────────────────────────────┤
│ CHOOSE / SWITCH      │ =CHOOSE($C$2, Base_Val, Bull_Val, Bear_Val)     │ Dynamic scenario toggles for commercial valuation.  │
├──────────────────────┼─────────────────────────────────────────────────┼─────────────────────────────────────────────────────┤
│ XNPV                 │ =XNPV(rate, cash_flows, dates)                  │ Precise discounted cash flows with irregular dates. │
├──────────────────────┼─────────────────────────────────────────────────┼─────────────────────────────────────────────────────┤
│ XIRR                 │ =XIRR(cash_flows, dates)                        │ Internal rate of return on pipeline in-licensing.   │
├──────────────────────┼─────────────────────────────────────────────────┼─────────────────────────────────────────────────────┤
│ LET                  │ =LET(x, A1*B1, y, x*0.2, x - y)                 │ Clean readability for complex GTN waterfall logic.  │
└──────────────────────┴─────────────────────────────────────────────────┴─────────────────────────────────────────────────────┘
```

---

## 3. Advanced Modeling Techniques in Consulting

### 3.1 Two-Way Sensitivity Data Tables
A two-way sensitivity table evaluates how a primary outcome metric (e.g., Year 5 Net Revenue or eNPV) responds across a matrix of two independent variables (e.g., Peak Market Share vs. Net Realized Price per Patient).

#### Step-by-Step Construction:
1. In cell `B4`, reference the primary model output formula: `=Summary!C25` (e.g., 10-Year eNPV).
2. Set horizontal column headers across `C4:G4` with Net Price variations (\$60k, \$75k, \$90k, \$105k, \$120k).
3. Set vertical row headers down `B5:B9` with Peak Market Share variations (10%, 15%, 20%, 25%, 30%).
4. Select the full matrix range `B4:G9`.
5. Navigate to: `Data` $\rightarrow$ `What-If Analysis` $\rightarrow$ `Data Table...`
6. In **Row Input Cell**, select the model's Net Price input cell (`Assumptions!C8`).
7. In **Column Input Cell**, select the model's Peak Share input cell (`Assumptions!C12`).
8. Press Enter. Excel calculates the 25 iterations instantly.
9. Format output with conditional formatting (Soft Green to Soft Red 3-color heatmap).

### 3.2 Dynamic Scenario Switching Architecture
Build a single master model that dynamically re-computes under Bull, Base, and Bear conditions without overwriting cells:

```excel
Cell C2: Dropdown Menu [1 = Bear Case | 2 = Base Case | 3 = Bull Case]

Cell C6 (Peak Market Share Formula):
=CHOOSE($C$2, 12%, 20%, 28%)

Cell C7 (Gross-to-Net Discount % Formula):
=CHOOSE($C$2, 38%, 30%, 24%)

Cell C8 (Duration of Therapy in Months):
=CHOOSE($C$2, 7.5, 9.0, 11.0)
```

### 3.3 Goal Seek & Solver for Commercial Optimization
- **Goal Seek**: Determine the exact Net Price required to achieve an eNPV of \$500 Million:
  - `Set cell`: `eNPV_Cell`
  - `To value`: `500000000`
  - `By changing cell`: `Net_Price_Cell`
- **Solver**: Optimize commercial sales force allocation across 3 therapeutic indications to maximize revenue subject to budget and headcount constraints:
  - `Objective`: Maximize Total Net Revenue.
  - `Changing Cells`: Headcount in Oncology, Cardiology, Rare Disease.
  - `Constraints`:
    - Total Reps $\le 150$.
    - Oncology Reps $\ge 40$.
    - Total Sales Budget $\le \$35 \text{ Million}$.

---

## 4. End-to-End Life Sciences Commercial Model Blueprint

Below is the complete architectural layout of a 10-year biopharma commercial P&L forecast model for an oncology pipeline asset.

```
=======================================================================================================================
SHEET: Commercial_Forecast
=======================================================================================================================
Line | Line Item                      | Units  | Formula / Logic           | Yr 1 (2026) | Yr 2 (2027) | ... | Yr 10 (2035)
=======================================================================================================================
--- SECTION 1: EPIDEMIOLOGICAL PATIENT CASCADE ---
 1   | US Population                  | '000s  | =C1*(1+$Assump.$C$4)      |     335,000 |     336,675 |     |      350,500
 2   | Disease Incidence Rate         | %      | =$Assump.$C$5             |      0.070% |      0.070% |     |       0.070%
 3   | Incident Patients              | Counts | =C1*C2*1000               |     234,500 |     235,673 |     |      245,350
 4   | Stage IV Metastatic Split      | %      | =$Assump.$C$6             |       50.0% |       50.0% |     |        50.0%
 5   | Biomarker Eligible Pool        | Counts | =C3*C4*$Assump.$C$7       |      87,938 |      88,377 |     |       92,006
 6   | Biopsy & Diagnosis Rate        | %      | Dynamic ramp              |       75.0% |       78.0% |     |        90.0%
 7   | 1L Treatment Initiation Rate   | %      | =$Assump.$C$9             |       80.0% |       80.0% |     |        80.0%
 8   | Total Addressable 1L Patients  | Counts | =C5*C6*C7                 |      52,763 |      55,147 |     |       66,244
-----------------------------------------------------------------------------------------------------------------------
--- SECTION 2: ADOPTION & MARKET SHARE ---
 9   | Commercial Launch Flag         | Binary | IF(Year >= LaunchYr, 1, 0)|           1 |           1 |     |            1
10   | Client Brand Market Share      | %      | Logistic uptake S-curve   |        4.0% |        9.5% |     |        24.0%
11   | Treated Patient Volume         | Counts | =C8*C10                   |       2,111 |       5,239 |     |       15,899
-----------------------------------------------------------------------------------------------------------------------
--- SECTION 3: DOSING & REVENUE REALIZATION ---
12   | Duration of Therapy (Months)   | Months | =$Assump.$C$14            |         9.0 |         9.0 |     |          9.0
13   | Infusions per Patient Course   | Units  | =(C12/12)*17              |        12.8 |        12.8 |     |         12.8
14   | List Price (WAC) per Infusion  | $      | =Prior*(1+Price_Growth)   |     $10,000 |     $10,250 |     |      $12,497
15   | Gross Sales ($M)               | $M     | =(C11*C13*C14)/1E6        |      $270.2 |      $687.3 |     |     $2,543.2
16   | Gross-to-Net (GTN) Deductions  | %      | Statutory + Formulary     |       32.0% |       33.0% |     |        35.0%
17   | Net Realized Sales ($M)        | $M     | =C15*(1-C16)              |      $183.7 |      $460.5 |     |     $1,653.1
-----------------------------------------------------------------------------------------------------------------------
--- SECTION 4: OPERATING EXPENSES & MARGINS ---
18   | Cost of Goods Sold (COGS, 8%)  | $M     | =C17*0.08                 |       $14.7 |       $36.8 |     |       $132.2
19   | Field Sales Force (75 Reps)    | $M     | Headcount * $320k         |       $24.0 |       $24.7 |     |        30.2
20   | Marketing & Digital Omnichannel| $M     | Launch heavy % of sales   |       $40.0 |       $35.0 |     |        $45.0
21   | Medical Affairs & MSLs         | $M     | Medical liaisons budget   |       $12.0 |       $12.5 |     |        $15.0
22   | Total Commercial OPEX ($M)     | $M     | =SUM(C18:C21)             |       $90.7 |      $109.0 |     |       $222.4
-----------------------------------------------------------------------------------------------------------------------
--- SECTION 5: COMMERCIAL PROFITABILITY & VALUATION ---
23   | Contribution Margin (EBITDA)   | $M     | =C17-C22                  |       $93.0 |      $351.5 |     |     $1,430.7
24   | Operating Margin %             | %      | =C23/C17                  |       50.6% |       76.3% |     |        86.5%
25   | Corporate Tax Rate (21%)       | $M     | =C23*0.21                 |       $19.5 |       $73.8 |     |       $300.4
26   | Net Operating Profit (NOPAT)   | $M     | =C23-C25                  |       $73.5 |      $277.7 |     |     $1,130.3
27   | Unlevered Free Cash Flow (FCF) | $M     | =NOPAT - CapEx + D&A      |       $70.0 |      $270.0 |     |     $1,110.0
28   | Discount Factor (WACC = 10%)   | Factor | =1/(1+10%)^(Year-0.5)     |       0.953 |       0.867 |     |        0.397
29   | Present Value of Cash Flow     | $M     | =C27*C28                  |       $66.7 |      $234.1 |     |       $440.7
=======================================================================================================================
30   | 10-Year Cumulative eNPV ($M)   | $M     | =SUM(C29:L29)             |                                      $3,412.5 M
=======================================================================================================================
```

---

## 5. Consultant's Quality Assurance & Error Checking Checklist

Before submitting or presenting an Excel model to an Engagement Manager or Client:
- [ ] **Zero Hardcoded Numbers in Formula Rows**: Run `Ctrl + ~` (Show Formulas) to verify all constants are referenced from the Assumptions block.
- [ ] **No Circular References**: Ensure status bar shows `Ready` without the `Circular References: ...` warning.
- [ ] **Check Total Balance Integrity**: Every waterfall subtraction must reconcile:
  $$\text{Net Sales} + \text{GTN Deductions} = \text{Gross Sales}$$
- [ ] **Dynamic Time Headers**: Formulas referencing prior years must not break if column A/B are inserted.
- [ ] **Sense Checks on Extremes**: Set Peak Market Share to 0% $\rightarrow$ Net Sales must evaluate to \$0.00 (model cannot produce phantom revenue).
- [ ] **Gridlines and Print Area**: Gridlines enabled, default zoom set to 100%, print area configured to single page wide (`Fit to 1 page wide, automatic tall`).

