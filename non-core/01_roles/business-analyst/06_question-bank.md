# 06. Business Analyst: Question Bank

> Comprehensive categorized interview question bank covering conceptual, technical SQL, metrics, and scenario-based questions.

---

## 1. Conceptual & Foundational Questions (Basic)

1. **What is the difference between a Business Analyst and a Data Analyst?**
   - *Sample Answer*: A Data Analyst focuses heavily on statistical data extraction, modeling, and deep exploratory analysis. A Business Analyst operates at the intersection of business strategy and data, focusing on defining requirements, evaluating process workflows, root-causing KPI deviations, and driving executive decisions with stakeholders.
2. **Explain the difference between `WHERE` and `HAVING` in SQL.**
   - *Sample Answer*: `WHERE` filters rows before any groupings or aggregations take place. `HAVING` filters aggregated groups after the `GROUP BY` clause has been executed.
3. **What is the difference between `INNER JOIN` and `LEFT JOIN`?**
   - *Sample Answer*: `INNER JOIN` returns only the rows with matching values in both tables. `LEFT JOIN` returns all rows from the left table, and the matched rows from the right table (with NULL for non-matching right records).
4. **How do you handle missing or NULL values in a dataset?**
   - *Sample Answer*: Depends on business context: (1) Ignore/drop if missing completely at random and sample size is large; (2) Impute with mean/median (continuous) or mode (categorical); (3) Treat NULL as a distinct category (e.g., "Unknown/Unspecified"); (4) Use forward-fill or backward-fill for time series data.
5. **What is a Primary Key vs. a Foreign Key?**
   - *Sample Answer*: A Primary Key uniquely identifies each record in a database table (cannot be NULL). A Foreign Key is a field in one table that refers to the Primary Key in another table, establishing relational integrity.

---

## 2. Analytical & Technical Questions (Intermediate)

6. **What is the difference between `ROW_NUMBER()`, `RANK()`, and `DENSE_RANK()`?**
   - *Sample Answer*: For values `[100, 90, 90, 80]`:
     - `ROW_NUMBER()` $\to 1, 2, 3, 4$ (strictly sequential, arbitrary tie breaker).
     - `RANK()` $\to 1, 2, 2, 4$ (assigns same rank to ties, skips subsequent rank).
     - `DENSE_RANK()` $\to 1, 2, 2, 3$ (assigns same rank to ties, no skips).
7. **Explain the difference between Correlation and Causation.**
   - *Sample Answer*: Correlation means two variables move together in a measurable linear or non-linear pattern. Causation means a change in one variable directly produces a change in the other. Correlation does not imply causation due to potential confounding variables or reverse causality.
8. **How would you design a KPI dashboard for a Regional Sales Manager?**
   - *Sample Answer*: (1) Top-line North Star: Total Regional Revenue vs. Monthly Target; (2) Performance Breakdown: Sales by Territory, Rep, and Product Line; (3) Operational Health: Conversion Rate per Pipeline Stage, Average Deal Size; (4) Risk Flags: Accounts with inactive touchpoints for $>14$ days.
9. **When would you use a Common Table Expression (CTE) over a Subquery?**
   - *Sample Answer*: CTEs (`WITH cte_name AS (...)`) improve query readability, enable modular stepwise logic, can be referenced multiple times within the same main query, and support recursive hierarchical queries.

---

## 3. Advanced Diagnostic & Business Case Questions

10. **A company's revenue increased 12% YoY, but net profit contracted 8%. How do you diagnose?**
    - *Approach*: Deconstruct into Revenue side (Volume vs. Price vs. Product Mix) and Cost side (COGS, Operating Expenses, Marketing/CAC, Logistics). Check if revenue growth was driven by heavy discounting or low-margin product lines, or if fixed operational costs / customer acquisition costs expanded disproportionately.
11. **A major e-commerce client observes a 25% surge in Cart Abandonment Rate. Walk me through your diagnosis.**
    - *Approach*: Segment by: (1) Platform (Web vs iOS vs Android app update); (2) Payment gateway error rates; (3) Shipping cost policy changes introduced at checkout; (4) Geographic delivery pin-code constraints.
12. **How would you measure the incremental return on investment (ROI) of an influencer marketing campaign?**
    - *Approach*: Use matched-market testing (synthetic control group) or unique coupon/referral tracking codes. Measure incremental lift = $(\text{Test Group Conversions} - \text{Control Group Conversions}) \times \text{Margin} - \text{Campaign Cost}$.

---

## 4. Scenario & Stakeholder Management Prompts

| Scenario Prompt | Key Evaluation Focus |
|:---|:---|
| *"A VP of Marketing disagrees with your data analysis and insists their campaign was successful. How do you respond?"* | Objective validation, walking through raw data assumptions collaboratively, finding common ground on shared metrics. |
| *"You discover a critical data pipeline bug that inflated reported revenue for the past 3 months. What steps do you take?"* | Immediate transparent communication to manager, quantify financial deviation, work with data engineering to patch pipeline, issue revised restatement. |
| *"A stakeholder asks for an ad-hoc dashboard with 2 hours before an executive meeting. How do you handle it?"* | Scope triage: Deliver top 3 critical metrics immediately via quick summary sheet, set expectations for full automated dashboard delivery. |
