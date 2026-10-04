# Placement Math — Business & Engineering Quantitative Reasoning

> **Scope Boundary**: Business arithmetic, financial ratios, break-even analysis, unit economics, CAGR, estimation math, and Excel data modeling.  
> **Differentiation**:  
> * **Aptitude (`01_common/aptitude/`)** = Speed-math, competitive tests (Time & Work, Speed-Distance, Syllogisms, Permutations).  
> * **Placement Math (`01_common/placement-math/`)** = Real-world business/engineering numerical analysis used in consulting cases, business analytics, tech tests, and corporate management.

---

## 1. Corporate Financial & Profitability Metrics

### 1. Margins & Profitability Breakdown
$$\text{Gross Profit} = \text{Revenue} - \text{COGS (Direct Material + Direct Labor)}$$
$$\text{Gross Margin \%} = \frac{\text{Gross Profit}}{\text{Revenue}} \times 100$$
$$\text{EBITDA} = \text{Revenue} - \text{COGS} - \text{Operating Expenses (OpEx, excluding D&A)}$$
$$\text{Operating Margin (EBIT \%)} = \frac{\text{Operating Profit}}{\text{Revenue}} \times 100$$
$$\text{Net Profit Margin \%} = \frac{\text{Net Income}}{\text{Revenue}} \times 100$$

* **Rule of Thumb**: Gross margin measures production efficiency; Operating margin measures business model health; Net margin measures bottom-line shareholder return.

---

## 2. Break-Even & Contribution Economics

$$\text{Contribution Margin (per unit)} = \text{Price per Unit} - \text{Variable Cost per Unit}$$
$$\text{Contribution Margin Ratio (CMR)} = \frac{\text{Contribution Margin}}{\text{Price per Unit}}$$
$$\text{Break-Even Volume (Units)} = \frac{\text{Total Fixed Costs}}{\text{Price per Unit} - \text{Variable Cost per Unit}}$$
$$\text{Break-Even Revenue (Currency)} = \frac{\text{Total Fixed Costs}}{\text{Contribution Margin Ratio}}$$

### Worked Example:
* An infrastructure equipment rental provider incurs fixed monthly depot overhead of ₹36 Lakhs.
* Rental charge per excavator-day = ₹12,000.
* Variable operating cost (diesel + operator + maintenance) = ₹7,000 / day.
* **Contribution Margin** = $12,000 - 7,000 = ₹5,000/\text{day}$.
* **Break-Even Volume** = $\frac{₹3,600,000}{5,000} = \mathbf{720\text{ excavator-days/month}}$.
* If the company owns 30 excavators operating 30 days/month (900 available excavator-days), the break-even utilization rate is $\frac{720}{900} = \mathbf{80\%}$.

---

## 3. Growth Rates, CAGR & The Rule of 72

### 1. Compound Annual Growth Rate (CAGR)
$$\text{CAGR} = \left(\frac{\text{End Value}}{\text{Start Value}}\right)^{\frac{1}{n}} - 1$$

### 2. The Rule of 72 (Mental Growth Shortcut)
$$\text{Years to Double} \approx \frac{72}{\text{Annual Growth Rate \%}}$$

* At 6% annual growth, size doubles in $\frac{72}{6} = 12\text{ years}$.
* At 12% annual growth, size doubles in $\frac{72}{12} = 6\text{ years}$.
* At 18% annual growth, size doubles in $\frac{72}{18} = 4\text{ years}$.
* At 24% annual growth, size doubles in $\frac{72}{24} = 3\text{ years}$.

---

## 4. Digital & Subscription Unit Economics

| Metric | Formula | Target Benchmark |
| :--- | :--- | :--- |
| **Customer Acquisition Cost (CAC)** | $\frac{\text{Total Sales \& Marketing Spend}}{\text{New Customers Acquired}}$ | Payback period $< 12\text{ months}$ |
| **Customer Lifetime Value (LTV)** | $\text{AOV} \times \text{Gross Margin \%} \times \frac{1}{\text{Churn Rate}}$ | $\text{LTV} / \text{CAC} \ge 3.0$ |
| **Churn Rate** | $\frac{\text{Lost Customers in Period}}{\text{Total Customers at Start of Period}}$ | SaaS: $< 5\text{--}7\% / \text{year}$ |
| **Payback Period** | $\frac{\text{CAC}}{\text{Average Monthly Contribution per Customer}}$ | High efficiency $< 9\text{ months}$ |

---

## 5. Excel Modeling & Spreadsheet Analytical Tools

For enterprise and corporate analytics interviews, candidates are expected to demonstrate mastery of core data functions:
* **Lookup & Reference**: `XLOOKUP(lookup_value, lookup_array, return_array)` and `INDEX(array, MATCH(...))`.
* **Conditional Aggregations**: `SUMIFS`, `COUNTIFS`, `AVERAGEIFS`.
* **Sensitivity Analysis**: Data Tables (1-variable and 2-variable), Goal Seek.
* **Pivot Tables**: Grouping temporal data, calculated fields, running totals.
* See full tutorial in [`Excel.md`](Excel.md).
