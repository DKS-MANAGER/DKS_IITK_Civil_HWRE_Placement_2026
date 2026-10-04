# 📊 Excel for Civil Engineering

> **Priority:** P0 — Required (Universal) | **Target Level:** L3
> **Time to L2:** 10–15 hrs | **Time to L3:** 20–30 hrs
> **Canonical source.** All tracks link here.

---

## 1. What It Is

Microsoft Excel is a **spreadsheet** tool for calculations, data analysis, and reporting. In Civil Engineering it is the **universal calculator** — used for design calculations, BOQ, rate analysis, data processing, and dashboards.

## 2. Where It Is Used

| Application | Branch | Context |
|:------------|:-------|:--------|
| Design calculations | Structural | Beam/slab/column design sheets per IS 456 |
| BOQ & rate analysis | Construction | Quantity takeoff, billing, cost estimation |
| Hydraulic calculations | HWRE | Manning's, pipe flow, rating curves |
| Data analysis | All | Sensor data, lab results, field measurements |
| Scheduling support | Construction | Resource loading, earned value |
| Dashboards | Data/PM | Project tracking, KPI visualization |

## 3. Why Your Target Role Needs It

**Company evidence:** Excel is required by **ALL 25 civil companies** — from L&T (BOQ) to Vassarlabs (data processing) to Axis Bank (analytics). It is the single most transferable skill.

| Company | Excel Use |
|:--------|:----------|
| L&T | BOQ, rate analysis, billing |
| Godrej | Billing, measurement sheets, MIS |
| Reliance New Energy | BOQ, MTO, SPT analysis |
| Vassarlabs | Data processing, flood analysis |
| Axis Bank / Accenture | Analytics, dashboards |

---

## 4. Installation / Setup

Excel is part of Microsoft 365. Students get it via:
- **IITK Microsoft 365** (free via institute email)
- **Excel Online** (free, browser-based — sufficient for L2)
- **Google Sheets** (free alternative — 90% transferable)

---

## 5. Core Interface

```
Workbook → Worksheets → Cells (A1, B2, ...)
Ribbon: Home | Insert | Formulas | Data | Review
Key areas: Formula bar, Name box, Status bar
```

---

## 6. Essential Features (Civil-Relevant Only)

### Must-Know (L2–L3) — 3 High-Value Blocks

#### Block 1: Formulas & Functions

| Function | Purpose | Civil Example |
|:---------|:--------|:--------------|
| `SUM`, `AVERAGE`, `MAX`, `MIN` | Aggregates | Average cube strength |
| `IF`, `AND`, `OR` | Logic | Pass/fail check (fck ≥ required) |
| `VLOOKUP` / `XLOOKUP` | Lookup | Steel table lookup (IS 800) |
| `INDEX` + `MATCH` | Advanced lookup | Rebar area from diameter |
| `SUMIF`, `COUNTIF` | Conditional sum | BOQ quantity by item |
| `ROUND`, `CEILING` | Rounding | Bar length rounding |

**Example — Rebar area lookup:**
```
=PI()*D2^2/4          → Area of one bar (D2 = diameter in mm)
=VLOOKUP(D2, SteelTable, 2, FALSE)  → Lookup area from IS table
```

#### Block 2: Data Tools

| Feature | Purpose | Civil Example |
|:--------|:--------|:--------------|
| **Pivot Table** | Summarize large data | Summarize BOQ by work type |
| **Filter / Sort** | Find specific data | Filter failed cube tests |
| **Conditional Formatting** | Highlight | Red if strength < fck |
| **Data Validation** | Input control | Dropdown for concrete grade |
| **Charts** | Visualize | Strength vs time curve |

#### Block 3: BOQ & Calculation Sheets

| Feature | Purpose |
|:--------|:--------|
| **Cell referencing** (`$A$1` vs `A1`) | Lock references when copying formulas |
| **Named ranges** | `=fck` instead of `=Sheet1!$B$2` |
| **Sheet protection** | Lock formula cells, allow input cells |
| **Print setup** | Headers, footers, page breaks for reports |

### What NOT to Waste Time On

```
- VBA/Macros (unless targeting automation roles — P2)
- Power Pivot / DAX (use Power BI instead)
- Every chart type — only Column, Line, Scatter matter for civil
- Array formulas (rarely needed at L3)
```

---

## 7. Typical Engineering Workflow

```
Step 1: Input — Enter raw data (dimensions, loads, test results)
Step 2: Calculate — Apply formulas (IS code checks, quantities)
Step 3: Check — Conditional formatting for pass/fail
Step 4: Summarize — Pivot table or summary sheet
Step 5: Visualize — Chart for report
Step 6: Report — Formatted print-ready sheet
```

---

## 8. Worked Example — Beam Design Check (IS 456)

**Task:** Check if a 300×450 mm beam with 4-Ø20 bars is adequate for Mu = 120 kN·m.

```
Inputs (cells B2:B6):
    b = 300 mm, d = 415 mm, fck = 25 MPa, fy = 415 MPa, Ast = 1256 mm²

Formulas:
    B7: xu = 0.87*fy*Ast / (0.36*fck*b)           → Neutral axis depth
    B8: xu_max = 0.48*d  (for Fe415)              → Limiting xu
    B9: =IF(B7<=B8, "Under-reinforced ✓", "Over-reinforced ✗")
    B10: Mu_lim = 0.36*fck*b*xu*(d - 0.42*xu)/1e6  → Moment capacity (kN·m)
    B11: =IF(B10>=120, "Safe ✓", "Unsafe ✗")

Output: Mu_lim = 138 kN·m → Safe (138 > 120)
```

**Check:** Conditional formatting turns B11 green if Safe, red if Unsafe.

---

## 9. Practice Exercises

### Basic
1. Build a **cube test register**: 10 cube results → average, max, min, pass/fail (fck check)
2. Build a **steel weight calculator**: diameter + length → weight (use `PI()*D^2/4 * L * 7850`)
3. Use `VLOOKUP` to look up rebar areas from a steel table

### Intermediate
4. Build a **BOQ sheet**: 15 items → quantity × rate = amount, with `SUMIF` by category
5. Build a **rate analysis** for M25 concrete (cement, sand, aggregate, water, labour)
6. Create a **Pivot Table** from 50 rows of site data (material received by date)

### Role-Specific
7. **Structural:** Design calculation sheet for a singly reinforced beam (IS 456)
8. **Construction:** Running bill format with measurement, rate, amount, deduction
9. **HWRE:** Manning's equation solver — given Q, n, S → find normal depth

---

## 10. Mini-Project — BOQ + Rate Analysis Workbook

```
Objective: Prepare a BOQ and rate analysis for a small RCC building
Input: Building dimensions, IS 1200 measurement rules, market rates
Workflow:
    1. Sheet 1 — Quantity takeoff (excavation, PCC, RCC, brickwork, plaster)
    2. Sheet 2 — Rate analysis per item (material + labour + overhead)
    3. Sheet 3 — BOQ summary (quantity × rate, with Pivot by category)
    4. Sheet 4 — Abstract cost + chart
Expected Output: A 4-sheet workbook, print-ready, with formulas and checks
Interview Questions It Prepares You For:
    - "How do you prepare a BOQ from a drawing?"
    - "Walk me through your rate analysis"
    - "How do you ensure your Excel sheet is error-free?"
```

---

## 11. Common Mistakes

| Mistake | Why It's Wrong | Correct Approach |
|:--------|:---------------|:-----------------|
| Hardcoded values in formulas | Can't audit, breaks on change | Reference input cells |
| No `$` in copied formulas | References shift incorrectly | Use `$A$1` for fixed refs |
| No input validation | Wrong grade entered silently | Use Data Validation dropdown |
| No checks | Errors hidden | Add pass/fail checks with `IF` |
| Merged cells | Breaks sorting/filtering | Use Center Across Selection |
| No documentation | Can't explain in interview | Add a "Notes" sheet |

---

## 12. Interview Questions

### Basic
- What is the difference between `VLOOKUP` and `INDEX`/`MATCH`?
- How do you create a Pivot Table?
- What does `$A$1` mean vs `A1`?

### Workflow
- Walk me through how you build a BOQ in Excel.
- How do you ensure your calculation sheet is error-free?

### Troubleshooting
- Your `VLOOKUP` returns `#N/A`. What do you check?
- Formulas show wrong results after copying. Why?

### Engineering Judgment
- Why did you choose Excel over Python for this BOQ?
- How do you handle rate changes in your BOQ template?

---

## 13. Rapid Revision

| Property | Value |
|:---------|:------|
| **Type** | Spreadsheet |
| **Developer** | Microsoft |
| **License** | Commercial (free via IITK) |
| **Platform** | Windows, macOS, Web |
| **Difficulty** | Easy |
| **Time to L2** | 10–15 hrs |
| **Time to L3** | 20–30 hrs |
| **Primary use** | Calculations, BOQ, data |
| **Alternative** | Google Sheets |

**Top 5 functions:** `IF`, `VLOOKUP`, `SUMIF`, `INDEX`+`MATCH`, `Pivot Table`

---

## Theory Linkage

```
Excel → Quantity Surveying → IS 1200 (measurement)
      → RCC Design → IS 456 (design checks)
      → Construction Management → BOQ, billing, cost control
      → Data Analysis → Statistics, visualization
```

---

## Company Linkage

| Company | What to Prepare |
|:--------|:----------------|
| L&T | BOQ, rate analysis, billing sheets |
| Godrej | Running bill, measurement sheets, MIS |
| Reliance New Energy | BOQ template, SPT data analysis |
| Vassarlabs | Data processing, flood analysis |
| Axis Bank / Accenture | Analytics, dashboards |

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| Role Matrix | [`SOFTWARE_ROLE_MATRIX.md`](../SOFTWARE_ROLE_MATRIX.md) |
| Interview Questions | [`software-interview-questions.md`](../software-interview-questions.md) |
| Resume Strategy | [`SOFTWARE_RESUME_STRATEGY.md`](../SOFTWARE_RESUME_STRATEGY.md) |
| Python (alternative) | [`programming/python.md`](../programming/python.md) |

---

*Canonical source for Excel. Do not duplicate in branch pages.*