# 04. Management Consulting: Practical Tools & Technical Handbook

> **Document Type**: Technical Skills & Delivery Manual
> **Audience**: Candidates preparing for consulting modeling assessments, case presentations, and analytics-driven interview rounds.
> **Scope**: Advanced Excel Modeling → Executive PowerPoint Storylining → Consulting Analytics & Data Interpretation (SQL, Python, Regressions).

---

## 1. Advanced Excel & Business Modeling Architecture

In management consulting, Excel models must be **transparent, modular, auditable, and dynamic**. An unorganized spreadsheet with hardcoded numbers embedded in formulas will immediately fail partner review.

### 1.1 The Golden Rules of Financial & Operational Modeling

1. **Strict Color Coding Standard**:
   - **Blue Text**: Hardcoded inputs, user assumptions, historical data (e.g., `450`, `0.15`).
   - **Black Text**: Dynamic formulas and calculations (e.g., `=C5*D5`).
   - **Green Text**: Cross-sheet links referencing other tabs within the workbook.
   - **Red Text**: External workbook links or warnings.
2. **Never Hardcode Inside Formulas**:
   - *Wrong*: `=B5 * 1.18` (Where did 1.18 come from? GST tax? Inflation? An auditor cannot tell).
   - *Right*: `=B5 * (1 + $C$2)` where Cell `$C$2` is clearly labeled `GST_Rate = 18.0%`.
3. **Left-to-Right Timeline Consistency**: Historical periods on the left, forecast periods on the right. Formulas in a row must be consistent from column to column.

---

### 1.2 Essential Excel Formulas Every Consultant Must Master

| Function Category | Function Syntax | Operational Consulting Use Case | Exact Working Example |
| :--- | :--- | :--- | :--- |
| **Dynamic Lookups** | `=XLOOKUP(lookup_val, lookup_arr, return_arr, [if_not_found])` | Merging SKU pricing catalogs or regional cost tables without VLOOKUP column-counting fragility. | `=XLOOKUP(A5, Products!A:A, Products!D:D, "Missing SKU")` |
| **Two-Way Lookups** | `=INDEX(data_range, MATCH(row_val, row_range, 0), MATCH(col_val, col_range, 0))` | Pulling values from complex 2D matrices (e.g., Product vs. Region margin table). | `=INDEX(PricingMatrix, MATCH("SKU_10", SKU_List, 0), MATCH("South", Regions, 0))` |
| **Conditional Sums** | `=SUMIFS(sum_range, criteria_range1, criteria1, criteria_range2, criteria2)` | Aggregating revenue for specific customer segments across designated fiscal quarters. | `=SUMIFS(Sales[Amount], Sales[Region], "North", Sales[Quarter], "Q3")` |
| **Conditional Counts**| `=COUNTIFS(criteria_range1, criteria1, criteria_range2, criteria2)` | Sizing customer cohort sizes with high churn risk or low NPS scores. | `=COUNTIFS(Users[Tenure_Months], "<6", Users[NPS], "<=6")` |
| **Logic & Error Traps**| `=IF(logical_test, val_if_true, val_if_false)`<br>`=IFERROR(value, value_if_error)` | Toggle scenario switches (Base/Bull/Bear) and prevent `#DIV/0!` errors from breaking presentation summaries. | `=IFERROR(B10/C10, 0)` |
| **Discounting & TVM** | `=NPV(rate, value1, [value2], ...)`<br>`=IRR(values)` | Evaluating capital expenditure feasibility, plant automation payback, and M&A returns. | `=NPV(10%, CashFlows) - InitialCapex` |

---

### 1.3 Practical Excel Modeling Exercise: 2-Variable Sensitivity Data Table

Consultants frequently present 2-variable sensitivity tables to executive leadership showing how EBITDA responds to simultaneous changes in **Price Realization** and **Raw Material Inflation**:

```text
                  EBITDA SENSITIVITY MATRIX (₹ CRORES)
┌───────────────┬────────────────────────────────────────────────────────┐
│               │             Raw Material Inflation (%)                 │
│ Price Change  ├───────────┬───────────┬───────────┬───────────┬────────┤
│     (%)       │   -5.0%   │    0.0%   │   +5.0%   │  +10.0%   │ +15.0% │
├───────────────┼───────────┼───────────┼───────────┼───────────┼────────┤
│    -10.0%     │    180    │    140    │    100    │     60    │    20  │
│     -5.0%     │    230    │    190    │    150    │    110    │    70  │
│      0.0%     │    280    │  240 (Base)   200    │    160    │   120  │
│     +5.0%     │    330    │    290    │    250    │    210    │   170  │
│    +10.0%     │    380    │    340    │    300    │    260    │   220  │
└───────────────┴───────────┴───────────┴───────────┴───────────┴────────┘
```

#### How to Build This in Excel (Step-by-Step):
1. Set up the baseline calculation model: Revenue = ₹1,000 Cr, Raw Materials = ₹500 Cr, Other Opex = ₹260 Cr $\implies$ Base EBITDA = ₹240 Cr.
2. In the top-left cell of the table matrix, link to the output cell: `=B15` (the EBITDA calculation cell).
3. Put Price Variations ($-10\%$ to $+10\%$) down the column; put Raw Material Inflation ($-5\%$ to $+15\%$) across the row.
4. Highlight the entire table $\implies$ Navigate to **Data Ribbon** $	o$ **What-If Analysis** $	o$ **Data Table**.
5. Select **Row Input Cell** as the Raw Material Inflation assumption cell; select **Column Input Cell** as the Price Change assumption cell $\implies$ Click OK.
6. Format output cells with green-to-red conditional formatting.

---

## 2. PowerPoint & Executive Storylining (The Pyramid Principle in Slides)

A consulting slide is **not a collection of bullet points**; it is a rigorous, message-driven argument designed to convince a CXO.

### 2.1 The Anatomy of an Executive Slide

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ ACTION TITLE: Complete sentence stating the "So What?" (Not a category heading)        │
│ "Reallocating 15% of marketing spend to digital channels will capture ₹40 Cr in EBITDA"│
├───────────────────────────────────────────────────┬────────────────────────────────────┤
│ TRACKER / SUB-HEADER: Context & scope             │ DATE / SOURCE: Verified data origin│
├───────────────────────────────────────────────────┴────────────────────────────────────┤
│                                                                                        │
│          CHART OR QUANTITATIVE EXHIBIT                   STRUCTURED COMMENTARY         │
│                                                                                        │
│     ┌────────────────────────────────────┐         • Lead with quantitative takeaway   │
│     │                                    │           (Digital CAC is 45% lower than TV)│
│     │   [ Clean, labeled bar chart       │                                             │
│     │     with explicit variance callout]│         • Address operational dependency    │
│     │                                    │           (Requires hiring 4 digital media  │
│     │                                    │            buyers within 60 days)           │
│     └────────────────────────────────────┘                                             │
│                                                                                        │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ FOOTER / TAKEAWAY CALLOUT: Single summary sentence anchoring the decision              │
│ "Recommendation: Approve ₹6 Cr pilot program in Delhi-NCR beginning Q2."               │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

### 2.2 Contrastive Slide Design: Weak vs. Executive-Ready

#### Example Case: Retail Bank Customer Churn Presentation

#### The Weak Slide (What 90% of Novices Build):
- **Slide Title**: *"Customer Retention Analysis"* (Weak: Tells the reader the topic, but reveals zero insights or decisions).
- **Body Content**:
  - *"We analyzed our retail banking customers over the last 6 months."*
  - *"Many customers are leaving because competitors have better mobile apps."*
  - *"Interest rates on savings accounts are also an issue."*
  - *"We should improve our digital banking features."*
  - *(Includes an unreadable 3D pie chart with 14 slices and no percentage labels).*
- **Interviewer / CXO Reaction**: Completely unconvincing, passive, offers no actionable data, wastes executive time.

#### The Executive-Ready Slide (Consulting Standard):
- **Action Title**: *"Mobile app login crashes drive 68% of affluent customer churn, representing ₹85 Crore in lost annual deposit value"* (Strong: Leads with root cause, quantification, and business impact).
- **Visual Exhibit**: A 3-step waterfall chart showing customer churn deconstructed:
  - App Stability Bugs: -68% of churned deposits (₹85 Cr)
  - Competitor Savings Rate Spread: -22% of churned deposits (₹28 Cr)
  - Relocation / Life Events: -10% of churned deposits (₹12 Cr)
- **Key Callout Box**:
  - *Observation*: Customers experiencing $>2$ app crashes within 30 days exhibit a $4.5\times$ higher probability of closing their salary account.
  - *Immediate Action*: Cloud infrastructure hotfix will resolve iOS biometric authentication crashes within 14 days for ₹1.2 Cr capex.
- **Interviewer / CXO Reaction**: Crystal clear, data-backed root cause, immediate high-ROI decision.

---

## 3. Data & Analytics in Consulting: SQL, Python & Regression

Technical requirements vary dramatically across consulting pathways. Generalist management consulting requires quantitative chart literacy and mental math; analytics-led and technology consulting require production SQL and statistical modeling.

### 3.1 Differentiating Technical Depth by Role Pathway

| Consulting Pathway | Excel Requirements | PowerPoint Requirements | SQL Requirements | Python / Stats Requirements |
| :--- | :--- | :--- | :--- | :--- |
| **Path A: MBB Strategy** | Intermediate (Data Tables, 3-Statement modeling) | **Mastery (Pyramid storylining, CXO decks)** | Conceptual / Minimal | Reading regression outputs ($R^2$, p-values) |
| **Path B: Corporate Strategy** | Advanced (DCF, M&A models, EVA) | **Mastery (Board decks, strategic memos)** | Minimal | Basic financial forecasting |
| **Path C: Big Four Operations** | Advanced (PivotTables, PowerQuery) | High (Deliverable slide decks) | Basic (SELECT, GROUP BY) | Basic scripting |
| **Path D: Digital / Tech** | High | High | Intermediate (JOINs, aggregations)| Cloud architectures, Agile sprints |
| **Path F: Analytics-Led (ZS/EXL)**| Advanced | High | **Mastery (Complex multi-table queries, Window functions)** | **Mastery (Pandas, Scikit-learn, Churn modeling)** |

---

### 3.2 Production SQL Query for Consulting Casework: Cohort Retention
In an analytics case interview (e.g., ZS Associates or Citi AIM), candidates are frequently asked to query customer transaction tables to detect cohort retention decay:

```sql
-- Production Consulting Query: Monthly Active Customer Retention Rate
WITH monthly_cohorts AS (
    SELECT 
        customer_id,
        DATE_TRUNC('month', MIN(transaction_date)) AS cohort_month
    FROM customer_transactions
    GROUP BY customer_id
),
customer_activity AS (
    SELECT 
        t.customer_id,
        c.cohort_month,
        DATE_PART('month', AGE(DATE_TRUNC('month', t.transaction_date), c.cohort_month)) AS month_number
    FROM customer_transactions t
    JOIN monthly_cohorts c ON t.customer_id = c.customer_id
)
SELECT 
    cohort_month,
    COUNT(DISTINCT CASE WHEN month_number = 0 THEN customer_id END) AS m0_acquired,
    COUNT(DISTINCT CASE WHEN month_number = 1 THEN customer_id END) AS m1_active,
    COUNT(DISTINCT CASE WHEN month_number = 3 THEN customer_id END) AS m3_active,
    ROUND(COUNT(DISTINCT CASE WHEN month_number = 3 THEN customer_id END)::NUMERIC / 
          COUNT(DISTINCT CASE WHEN month_number = 0 THEN customer_id END) * 100, 1) AS m3_retention_pct
FROM customer_activity
GROUP BY cohort_month
ORDER BY cohort_month;
```

---

### 3.3 Interpreting Regression & Statistical Forecasting Outputs

When presented with an econometric regression exhibit in a BCG or McKinsey interview:
$$\text{Sales (₹ Cr)} = 45.2 + 2.8 \times (\text{Digital Marketing Spend}) - 1.4 \times (\text{Price Discount \%}) + 0.35 \times (\text{Store Footfall})$$

1. **Check Statistical Significance (p-values / t-statistics)**:
   - If p-value $< 0.05$ (or $|t| > 2.0$), the variable is statistically significant.
   - If p-value $= 0.42$, **do not recommend increasing that spend**, as the observed correlation is statistically indistinguishable from random noise!
2. **Check $R^2$ (Goodness of Fit)**:
   - $R^2 = 0.82$ indicates that 82% of the variance in sales is explained by the three independent variables.
3. **Beware of Multicollinearity**: If Store Footfall and Marketing Spend have a correlation of 0.88, the individual coefficients may be unstable and biased.
