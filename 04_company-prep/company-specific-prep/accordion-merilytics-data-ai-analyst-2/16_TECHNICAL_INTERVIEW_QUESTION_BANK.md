# Module 16 — Technical Interview Question Bank

This question bank contains **60 technical and business analytics questions** organized across three difficulty tiers (Foundational, Intermediate, Advanced) designed to simulate the technical interview rounds at Accordion (Merilytics).

---

## Tier 1: Foundational Questions (Q01 – Q20)

#### Q01: "What is the difference between VLOOKUP, INDEX/MATCH, and XLOOKUP in Excel?"
- **Expected Answer**:
  - `VLOOKUP`: Searches only from left to right; breaks if a column is inserted; defaults to approximate match if `, FALSE` is omitted; memory intensive on large sheets.
  - `INDEX/MATCH`: Separates the retrieval array (`INDEX`) from the search array (`MATCH`); works left-to-right and right-to-left; robust against column insertions; faster calculation speed.
  - `XLOOKUP`: Modern replacement; defaults to exact match; supports bi-directional lookups, native error handling (`if_not_found`), and returns entire row/column arrays.
- **Common Candidate Mistake**: Forgetting that `INDEX/MATCH` can perform 2D matrix lookups by supplying both row and column match arguments.

#### Q02: "Explain the difference between `WHERE` and `HAVING` in SQL."
- **Expected Answer**: `WHERE` filters individual rows *before* aggregation takes place (Step 4 of logical query processing) and cannot reference aggregate functions. `HAVING` filters aggregated groups *after* `GROUP BY` execution (Step 6) and can reference aggregate calculations like `SUM()`, `AVG()`, or `COUNT()`.
- **Follow-Up Trap**: *"Can you use `HAVING` without a `GROUP BY` clause?"*  
  - *Answer*: Yes, `SELECT 1 FROM table HAVING COUNT(*) > 10;` treats the entire table as a single aggregated group.

#### Q03: "What happens when you perform an `INNER JOIN` vs. a `LEFT JOIN` on tables with non-matching keys?"
- **Expected Answer**: An `INNER JOIN` returns only rows with matching keys in both tables; rows with keys existing in only one table are dropped. A `LEFT JOIN` preserves all rows from the left table; where no matching key exists in the right table, right-table columns are populated with `NULL`.

#### Q04: "Why do we downcast numeric types in Pandas?"
- **Expected Answer**: Pandas defaults integer columns to `int64` (8 bytes) and floats to `float64` (8 bytes). For a column with 10 million rows containing small integers (e.g., age 0–100 or month 1–12), downcasting to `uint8` (1 byte) reduces the column's memory footprint from 80 MB to 10 MB, preventing memory overflow errors.

#### Q05: "What is the difference between Correlation and Causation in commercial analytics?"
- **Expected Answer**: Correlation measures the statistical association between two variables ($r \in [-1, 1]$). Causation proves that a change in variable $X$ directly produces a change in variable $Y$. In portfolio analytics, confusing correlation with causation leads to flawed capital allocation (e.g., noticing that marketing spend and revenue both peaked in December, failing to account for holiday seasonality).

---

## Tier 2: Intermediate Questions (Q21 – Q40)

#### Q21: "Explain how window functions differ from standard `GROUP BY` aggregations in SQL."
- **Expected Answer**: A standard `GROUP BY` collapses multiple individual rows into a single summary row per group. A window function (`OVER(...)`) computes aggregate metrics across a partitioned set of rows while **preserving the individual row identity and returning the original row count**.
- **Practical Example**: Computing an employee's salary and their department's average salary on the same row:
  ```sql
  SELECT emp_name, dept_id, salary, 
         AVG(salary) OVER(PARTITION BY dept_id) AS dept_avg_salary
  FROM employees;
  ```

#### Q22: "What is the difference between `ROW_NUMBER()`, `RANK()`, and `DENSE_RANK()`?"
- **Expected Answer**:
  - `ROW_NUMBER()`: Always assigns distinct sequential integers (1, 2, 3, 4) arbitrarily breaking ties.
  - `RANK()`: Assigns identical ranks to ties, but skips subsequent rank numbers (1, 2, 2, 4).
  - `DENSE_RANK()`: Assigns identical ranks to ties without skipping subsequent numbers (1, 2, 2, 3).
- **PE Use Case**: Identifying the second-highest supplier contract cost requires `DENSE_RANK()` so that tied top-cost contracts don't cause the query to skip rank 2.

#### Q23: "In PowerPivot DAX, what is the difference between Row Context and Filter Context?"
- **Expected Answer**:
  - **Row Context**: Exists during row-by-row iteration (e.g., in a Calculated Column or iterator function like `SUMX`). It knows the values of the *current row*, but is blind to other rows or active visual slicers.
  - **Filter Context**: Exists across the entire data model. It is the set of all active filters applied by PivotTable rows, columns, slicers, and explicit `CALCULATE` statements.
  - **Context Transition**: Occurs when `CALCULATE` is called inside a row context; it converts the current row's primary key into an active filter context.

#### Q24: "How do you detect and handle multicollinearity in regression models?"
- **Expected Answer**: Multicollinearity occurs when independent predictor variables are highly correlated with each other, inflating standard errors and making coefficients unstable.
  - *Detection*: Compute the **Variance Inflation Factor (VIF)**. A $\text{VIF} > 5.0$ indicates moderate multicollinearity; $\text{VIF} > 10.0$ indicates severe collinearity.
  - *Remediation*: Remove one of the redundant variables, combine them via Principal Component Analysis (PCA), or apply regularized regression (Ridge / Lasso).

#### Q25: "How would you diagnose an unexpected 300 bps EBITDA margin drop in a portfolio company?"
- **Expected Answer**: Decompose the variance using an **EBITDA Bridge (Walk)** across five mutually exclusive levers:
  1. *Volume Variance*: Did physical unit sales drop, failing to absorb fixed overhead?
  2. *Price Variance*: Did sales reps give off-invoice discounts to close deals?
  3. *Mix Variance*: Did customer demand shift toward lower-margin product tiers?
  4. *Cost Inflation (COGS)*: Did raw materials, shipping, or direct labor hours increase?
  5. *SG&A Overruns*: Did administrative overhead, executive travel, or marketing spend spike?

---

## Tier 3: Advanced Questions (Q41 – Q60)

#### Q41: "Explain the architecture of Snowflake and why it outperforms traditional on-premise data warehouses."
- **Expected Answer**: Snowflake separates **Storage**, **Compute (Virtual Warehouses)**, and **Cloud Services**:
  - Traditional warehouses tightly couple storage and compute on fixed servers; a heavy ETL job slows down executive reporting.
  - In Snowflake, the CFO's Power BI warehouse and the Data Engineering ingestion warehouse operate independently against the same centralized cloud storage (Amazon S3 / Azure Blob) with zero contention.
  - Tables are organized into immutable, encrypted columnar **Micro-Partitions** (50–500MB), eliminating manual indexing through automated metadata pruning.

#### Q42: "In Databricks and Apache Spark, what is the difference between a Narrow and a Wide Transformation?"
- **Expected Answer**:
  - **Narrow Transformation**: Each input partition contributes to at most one output partition (e.g., `filter()`, `select()`, `map()`). Data processing occurs locally within the worker node with zero network exchange. Very fast.
  - **Wide Transformation**: Multiple input partitions contribute to multiple output partitions (e.g., `groupBy()`, `distinct()`, `join()`). Spark must perform a **Shuffle**, redistributing data across cluster nodes over the physical network. Shuffling is the primary performance bottleneck in big data pipelines.

#### Q43: "How does Delta Lake ensure ACID transactions on top of object storage?"
- **Expected Answer**: Delta Lake maintains an append-only JSON transaction log in a directory named `_delta_log/`. Whenever a transaction commits, Spark writes a new atomic commit file (e.g., `000001.json`). Readers query a snapshot of the table by reading the transaction log first to identify which Parquet files are valid, enabling atomicity, isolation, and point-in-time Time Travel.

#### Q44: "How do you responsibly apply AI-enabled engineering tools while protecting client confidentiality?"
- **Expected Answer**:
  - Never upload proprietary financial ledgers, transactional records, or customer PII into public AI tools.
  - Use structural schema obfuscation: Provide abstract dummy schemas when prompting for complex SQL queries or Python scripts.
  - Implement mandatory human code reviews: Verify that AI-generated queries do not introduce Cartesian joins, dialect errors, or flawed financial logic.
  - Use company-provisioned enterprise tenants where data retention for model training is disabled.

#### Q45: "How do you explain a complex machine learning churn model to a non-technical portfolio company CFO?"
- **Expected Answer**:
  > *"I avoid technical jargon like hyperparameter tuning or gradient boosting. Instead, I frame the model as an **early-warning operational radar**:
  > - I explain that the model examines 20 historical behavior patterns (payment delays, ticket volumes, usage drops) to flag at-risk accounts 60 days before contract renewal.
  > - I show them the **SHAP feature waterfall**: showing that accounts with > 3 unresolved tickets have a 4.2× higher churn risk.
  > - Finally, I translate this into bottom-line EBITDA: 'If our Customer Success team intervenes on the top 50 flagged accounts, we protect \$2.4M in recurring annual revenue.'"*

