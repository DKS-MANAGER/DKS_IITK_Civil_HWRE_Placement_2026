# Excel & Spreadsheets for Business Analysts

> Essential Excel functions, lookup mechanisms, pivot tables, data modeling, and reporting best practices for BA interview tests.

---

## 1. Core Lookup & Reference Functions

### XLOOKUP vs. INDEX-MATCH vs. VLOOKUP
- **XLOOKUP (Modern Standard)**:
  `=XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])`
  *Advantages*: Leftward lookups, default exact match, no column index numbering errors, handles missing values gracefully.
- **INDEX-MATCH (Classic Robust Standard)**:
  `=INDEX(return_range, MATCH(lookup_value, lookup_range, 0))`
  *Advantages*: Highly dynamic, lower compute overhead on large enterprise sheets, compatible with all legacy versions.
- **VLOOKUP (Legacy)**:
  `=VLOOKUP(lookup_value, table_array, col_index_num, FALSE)`
  *Caveat*: Breaks if columns are inserted/reordered.

---

## 2. Aggregations & Conditional Logic

- **SUMIFS / COUNTIFS / AVERAGEIFS**:
  `=SUMIFS(sum_range, criteria_range1, criteria1, criteria_range2, criteria2)`
- **Conditional Categorization**:
  `=IFS(B2>=90, "Tier 1", B2>=75, "Tier 2", TRUE, "Tier 3")`
- **Error Handling**:
  `=IFERROR(A2/B2, 0)` — Essential for financial ratio formulas where zero denominators exist.

---

## 3. Pivot Tables & Data Summarization

### Key Pivot Table Workflows
1. **Source Data Preparation**: Ensure clean tabular layout (single header row, no merged cells, no blank row gaps).
2. **Field Layout**:
   - **Rows**: Primary dimensions (Region, Category, Customer Cohort).
   - **Columns**: Time periods (Year, Quarter, Month).
   - **Values**: Aggregated metrics (`Sum of Revenue`, `Count of Orders`).
3. **Calculated Fields**:
   - Creating custom margin calculations: `=(Revenue - Cost) / Revenue` inside the Pivot Table without modifying raw source data.
4. **Value Field Settings**:
   - Show Values As: `% of Column Total`, `% Difference From Previous Month` (MoM growth).

---

## 4. Analytical Modeling & Visualization

- **Sensitivity & Scenario Analysis**: Data Tables (1-variable and 2-variable sensitivity matrices for pricing vs volume).
- **Conditional Formatting**: Highlighting top 10% performers, gradient heatmaps for cohort decay, data bars for quick visual audits.
- **Dynamic Charting**: Linking charts to Pivot Tables (Pivot Charts) with interactive Slicers.
