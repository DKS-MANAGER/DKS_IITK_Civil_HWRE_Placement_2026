# Tools Lab 01: Practical Excel Financial Modeling & Sensitivity Analysis

> **Lab Objective**: Build reproducible, error-free financial models, dynamic sensitivity tables, and price-volume decomposition worksheets in Microsoft Excel / Google Sheets for consulting casework.  
> **Prerequisites**: Basic familiarity with spreadsheets.  
> **Estimated Lab Time**: 2 hours.

---

## 1. Professional Spreadsheet Standards for Consultants

In management consulting, client executives and partners review your models. Follow these universal modeling rules:
1. **Color-Coding Discipline**:
   - **Blue text**: Hardcoded historical inputs, raw data, or empirical assumptions (e.g., `150`, `0.25`).
   - **Black text**: Formulas, calculations, and mathematical references (e.g., `=B4*C4`).
   - **Green text**: External links referencing other sheets or workbooks.
2. **Never Hardcode Numbers Inside Formulas**:
   - ❌ *Weak / Unacceptable*: `=B4 * 1.18` (Where did 1.18 come from? Tax? Inflation? Growth?)
   - ✅ *Professional*: `=B4 * (1 + $C$1)` where Cell `$C$1` is clearly labeled `Tax Rate: 18.0%`.
3. **Dynamic Cell Referencing**: Use relative references (`A1`), absolute references (`$A$1`), and mixed column/row locks (`$A1` or `A$1`) to ensure formulas can be copied across matrices without breaking.

---

## 2. Core Consulting Formula Suite

| Function Syntax | Business Consulting Use Case | Syntax Breakdown & Example |
| :--- | :--- | :--- |
| `=XLOOKUP(lookup, lookup_range, return_range, [if_not_found])` | Merging client ERP price lists with SKU transactional order tables. | `=XLOOKUP(A2, SKU_Table!A:A, SKU_Table!D:D, "SKU Not Found")` |
| `=SUMIFS(sum_range, crit_range1, crit1, crit_range2, crit2)` | Aggregating revenue filtered by region AND product tier. | `=SUMIFS(D:D, A:A, "South", B:B, "Premium")` |
| `=COUNTIFS(crit_range1, crit1, ...)` | Counting customer accounts with overdue receivables >60 days. | `=COUNTIFS(Aging!C:C, ">60", Aging!D:D, "Unpaid")` |
| `=IFERROR(formula, value_if_error)` | Trapping `#DIV/0!` errors during blank-cell margin calculations. | `=IFERROR((Revenue - Cost)/Revenue, 0)` |
| `=INDEX(array, MATCH(val, r_range, 0), MATCH(val, c_range, 0))` | 2-dimensional matrix lookup across year columns and cost rows. | Standard backward-compatible matrix lookup. |

---

## 3. Hands-On Lab Exercise 1: Reproducible P&L & Break-Even Model

Enter the following raw data into a new worksheet starting at Cell `A1`:

### Input Data Table:
| Row / Col | A (Parameter Label) | B (Baseline Value) | C (Unit / Note) |
| :---: | :--- | :---: | :--- |
| **1** | **Industrial Valve Manufacturing Model** | | |
| **2** | Selling Price per Unit ($P$) | `250.00` | USD / valve |
| **3** | Direct Material Cost per Unit ($VC_1$) | `90.00` | USD / valve |
| **4** | Direct Assembly Labor per Unit ($VC_2$)| `45.00` | USD / valve |
| **5** | Packaging & Freight per Unit ($VC_3$) | `15.00` | USD / valve |
| **6** | Annual Fixed Factory Rent ($FC_1$) | `1,500,000` | USD / year |
| **7** | Annual Fixed Administrative SG&A ($FC_2$)| `900,000` | USD / year |
| **8** | Current Annual Production Volume ($Q$) | `35,000` | Units / year |

---

### Step-by-Step Model Construction Formulas:

Enter these formulas in Rows 10 to 18:

| Cell | Metric Label | Exact Excel Formula | Expected Output |
| :---: | :--- | :--- | :---: |
| **B10** | **Total Variable Cost per Unit** | `=SUM(B3:B5)` | **`$150.00`** |
| **B11** | **Unit Contribution Margin** | `=B2 - B10` | **`$100.00`** |
| **B12** | **Contribution Margin Ratio** | `=B11 / B2` | **`40.0%`** |
| **B13** | **Total Fixed Overhead** | `=SUM(B6:B7)` | **`$2,400,000`** |
| **B14** | **Gross Revenue** | `=B2 * B8` | **`$8,750,000`** |
| **B15** | **Total Operating Costs** | `=B13 + (B10 * B8)` | **`$7,650,000`** |
| **B16** | **Operating Profit (EBIT)** | `=B14 - B15` | **`$1,100,000`** |
| **B17** | **Operating Profit Margin** | `=B16 / B14` | **`12.57%`** |
| **B18** | **Break-Even Volume (Units)** | `=B13 / B11` | **`24,000 units`** |

---

## 4. Hands-On Lab Exercise 2: Building a Two-Variable Data Sensitivity Table

Consulting clients frequently ask: *"What happens to our operating profit if selling price fluctuates by $\pm 10\%$ and material costs fluctuate by $\pm 15\%$?"*

Do not calculate scenarios manually. Build a native Excel **What-If Analysis Two-Variable Data Table**:

```text
       Price ($) ──►  $220      $235      $250      $265      $280
Mat ($)
  $75               $825k    $1.35M    $1.87M    $2.40M    $2.92M
  $90 (Base)        $300k    $825k    $1.10M    $1.87M    $2.40M
  $105             -$225k    $300k     $825k    $1.35M    $1.87M
```

### Setup Instructions in Excel:
1. In Cell `D1`: Reference the target formula `=B16` (Operating Profit).
2. In Cells `E1:I1`: Enter the candidate Selling Prices: `220`, `235`, `250`, `265`, `280`.
3. In Cells `D2:D4`: Enter candidate Material Costs: `75`, `90`, `105`.
4. Select the entire rectangular range `D1:I4`.
5. Go to the Excel Ribbon: **Data** $\to$ **What-If Analysis** $\to$ **Data Table...**
6. In the dialog box:
   - **Row input cell**: Select Cell `$B$2` (Selling Price).
   - **Column input cell**: Select Cell `$B$3` (Direct Material Cost).
7. Click **OK**. Excel automatically calculates all 15 permutations in under one second!

---

## 5. Hands-On Lab Exercise 3: Price-Volume-Mix Decomposition in Excel

When given two years of multi-product data, use this formula layout to verify Volume, Price, and Mix:

```text
Col A: Product Name
Col B: Year 1 Volume (Q1)
Col C: Year 1 Price (P1)
Col D: Year 1 Revenue (=B2*C2)
Col E: Year 2 Volume (Q2)
Col F: Year 2 Price (P2)
Col G: Year 2 Revenue (=E2*F2)
Col H: Volume Effect Formula: =(SUM($E$2:$E$10)-SUM($B$2:$B$10))*(D2/SUM($D$2:$D$10))*C2 ...
Col I: Price Effect Formula:  =E2*(F2-C2)
Col J: Mix Effect Formula:    =G2 - D2 - H2 - I2
```
Verify that `SUM(H:H) + SUM(I:I) + SUM(J:J) = SUM(G:G) - SUM(D:D)`.

---

## 6. Common Spreadsheet Errors & Auditing Shortcuts

1. **`#DIV/0!` Trap**: Occurs when computing percentage changes over empty base cells. Fix with `=IFERROR((New - Old)/Old, 0)`.
2. **`#N/A` Lookup Failure**: Occurs when text values contain trailing whitespace. Fix by wrapping keys in `=TRIM(CLEAN(A2))`.
3. **Formula Auditing Hotkeys**:
   - **Ctrl + [**: Trace Precedents (jump to the cells feeding the current formula).
   - **F5 + Enter**: Jump back to previous cell.
   - **Ctrl + ~**: Toggle formula display view (displays all formulas simultaneously instead of calculated values).
