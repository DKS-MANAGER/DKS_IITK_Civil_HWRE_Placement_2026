# 03. Data Analyst: Relational Architecture, Data Hygiene & Analytics Domain Knowledge

> **Scope**: Essential theoretical and practical domain knowledge required for Data Analyst and Business Intelligence technical interviews. `[PREPARATION HEURISTIC]`

---

## 1. Relational Database Architecture & Normalization

### 1.1 The Normal Forms (OLTP Optimization)
In transactional systems (OLTP), normalization minimizes data redundancy and prevents update anomalies:

* **First Normal Form (1NF)**:
  - Each column contains atomic (indivisible) values.
  - No repeating groups or arrays stored in a single field.
  - Every table must have a designated Primary Key.
* **Second Normal Form (2NF)**:
  - Table is in 1NF.
  - No partial dependency: Every non-key attribute must depend on the *entire* primary key (relevant for composite keys).
* **Third Normal Form (3NF)**:
  - Table is in 2NF.
  - No transitive dependency: Non-key attributes must NOT depend on other non-key attributes ($X \to Y$ and $Y \to Z \implies X \to Z$ eliminated).
  - *Classic Rule*: "Every non-key attribute must provide a fact about the key, the whole key, and nothing but the key."

### 1.2 Dimensional Modeling (OLAP Data Warehousing)
In analytical data warehouses (Snowflake, BigQuery, Redshift), highly normalized 3NF schemas cause slow queries due to excessive joins. Analysts use **Dimensional Modeling**:

```text
                             STAR SCHEMA ARCHITECTURE
                             
    ┌──────────────────────┐                     ┌──────────────────────┐
    │    dim_customer      │                     │     dim_product      │
    ├──────────────────────┤                     ├──────────────────────┤
    │ customer_id (PK)     │                     │ product_id (PK)      │
    │ customer_name        │                     │ product_name         │
    │ segment              │                     │ category             │
    │ city, state          │                     │ unit_price           │
    └──────────┬───────────┘                     └───────────┬──────────┘
               │                                             │
               │         ┌─────────────────────────┐         │
               └────────►│      fact_orders        │◄────────┘
                         ├─────────────────────────┤
                         │ order_id (PK)           │
                         │ customer_id (FK)        │
                         │ product_id (FK)         │
                         │ date_id (FK)            │
                         │ order_amount (Measure)  │
                         │ quantity (Measure)      │
                         │ discount_amount(Measure)│
                         └───────────▲─────────────┘
                                     │
                         ┌───────────┴─────────────┐
                         │        dim_date         │
                         ├─────────────────────────┤
                         │ date_id (PK)            │
                         │ full_date, day_of_week  │
                         │ month, quarter, year    │
                         └─────────────────────────┘
```

* **Star Schema**: Central Fact table surrounded by de-normalized Dimension tables. Fast querying, simple joins, optimal for BI tools.
* **Snowflake Schema**: Dimension tables are normalized into sub-dimensions (e.g., `dim_product` joins to `dim_category`). Saves storage, but adds join complexity.
* **Fact Tables**: Contain quantitative numerical measurements (revenue, quantity, latency) and foreign keys.
  - *Additive Facts*: Can be summed across all dimensions (e.g., `revenue`).
  - *Semi-Additive Facts*: Can be summed across some dimensions but not time (e.g., `account_balance`).
  - *Non-Additive Facts*: Ratios and percentages (e.g., `margin_pct` must be recalculated as $\frac{\sum \text{profit}}{\sum \text{revenue}}$).

---

## 2. SQL Query Execution Order & Performance Optimization

### 2.1 The Logical Query Processing Pipeline
Understanding the database engine execution sequence prevents common SQL syntax and grouping errors:

```text
 1. FROM / JOIN     ► Identify source tables, evaluate Cartesian products, apply ON filters
 2. WHERE           ► Filter individual rows prior to grouping (Cannot reference aliases or window functions)
 3. GROUP BY        ► Aggregate rows into distinct categorical buckets
 4. HAVING          ► Filter aggregated groups (Evaluated after aggregation; operates on group metrics)
 5. SELECT          ► Evaluate column expressions, mathematical formulas, and window functions
 6. DISTINCT        ► Eliminate duplicate rows from the final result set
 7. ORDER BY        ► Sort result rows (Can reference column aliases created in SELECT)
 8. LIMIT / OFFSET  ► Truncate final result set to specified record count
```

### 2.2 Indexing & Query Tuning
* **B-Tree Index**: Balanced tree structure ($O(\log N)$ search). Best for high-cardinality columns frequently filtered via `=` or range `<, >, BETWEEN`.
* **Composite Index & Leftmost Prefix Rule**: An index on `(country, signup_date)` accelerates queries filtering by `country` OR `(country AND signup_date)`. It will NOT accelerate queries filtering by `signup_date` alone.
* **Costly Operations to Avoid**:
  - `SELECT *`: Ingests unnecessary columns, increasing disk I/O and network bandwidth.
  - Functions on Indexed Columns: Writing `WHERE YEAR(order_date) = 2026` invalidates index lookups (forces full table scan). Write `WHERE order_date >= '2026-01-01' AND order_date < '2027-01-01'`.
  - Cartesian Joins (`CROSS JOIN`): Joining without an `ON` condition multiplies rows ($N \times M$).

---

## 3. Data Hygiene & Cleaning Lifecycle

```text
  RAW DATA INGESTION ──► STRUCTURAL VALIDATION ──► ANOMALY DETECTION ──► IMPUTATION & EXCLUSION ──► ANALYTICS READY
```

### 3.1 Taxonomy of Missing Data
* **Missing Completely at Random (MCAR)**: Missingness is independent of both observed and unobserved data (e.g., a random network packet drop). Safe to drop if sample loss is minimal.
* **Missing at Random (MAR)**: Missingness depends on observed data (e.g., female respondents are less likely to disclose age, but age is recorded for all who disclose gender). Handled via subgroup imputation.
* **Missing Not at Random (MNAR)**: Missingness depends on the unobserved value itself (e.g., high-income earners refusing to answer income questions). Dropping or mean-imputing introduces extreme bias; requires explicit missingness flagging.

### 3.2 Outlier Detection & Treatment
* **Interquartile Range (IQR) Method**:
  $$\text{IQR} = Q_3 - Q_1$$
  $$\text{Lower Bound} = Q_1 - 1.5 \times \text{IQR}, \quad \text{Upper Bound} = Q_3 + 1.5 \times \text{IQR}$$
* **Z-Score Method** (for approximately normal distributions):
  $$Z = \frac{X - \mu}{\sigma}, \quad \text{Outlier if } |Z| > 3$$
* **Treatment Decision**:
  - *Data Entry Error* (e.g., Age = 999): Correct if source available, else set to `NULL`.
  - *Genuine Extreme Observation* (e.g., enterprise B2B order): Do NOT delete. Winsorize (cap at 99th percentile) or segment enterprise accounts from consumer accounts.

---

## 4. Core Business Metrics & KPI Architecture

| Business Metric | Explicit Formula | Measurement Grain | Interpretation & Caveats |
| :--- | :--- | :--- | :--- |
| **Customer Acquisition Cost (CAC)** | $\frac{\text{Total S\&M Expenses in Period } t}{\text{New Customers Acquired in Period } t}$ | Monthly / Quarterly | Must include marketing tool costs, agency fees, and sales team salaries. |
| **Customer Lifetime Value (LTV)** | $\frac{\text{Average Revenue Per User (ARPU)} \times \text{Gross Margin \%}}{\text{Customer Churn Rate}}$ | Customer Lifetime | Assumes constant churn rate; invalid for high-volatility early-stage cohorts. |
| **LTV / CAC Ratio** | $\frac{\text{LTV}}{\text{CAC}}$ | Enterprise Benchmark | $<1.0\times$ Unsustainable; $3.0\times$ Healthy SaaS benchmark; $>5.0\times$ Under-investing in acquisition. |
| **Logo (Customer) Churn** | $\frac{\text{Customers Lost in Period } t}{\text{Customers at Start of Period } t}$ | Monthly / Annual | Measures account attrition. Exclude mid-month signups from the denominator. |
| **Net Revenue Retention (NRR)** | $\frac{\text{Starting ARR} + \text{Expansion} - \text{Contraction} - \text{Churn}}{\text{Starting ARR}} \times 100\%$ | Annual Cohort | Best SaaS health metric. $>100\%$ indicates portfolio grows even with zero new acquisitions. |
| **DAU / MAU Ratio (Stickiness)** | $\frac{\text{Daily Active Users}}{\text{Monthly Active Users}}$ | Daily Rolling | Measures user engagement frequency. $>50\%$ indicates daily essential habit (e.g., messaging/social). |

---

## 5. Statistical Pitfalls in Business Analytics

### 5.1 Simpson's Paradox
* **Definition**: A trend or correlation that appears across different subgroups reverses or disappears when the subgroups are combined.
* **Classic Placement Scenario**:
  - Channel A has a 10% conversion rate on Desktop and a 4% conversion rate on Mobile.
  - Channel B has a 9% conversion rate on Desktop and a 3% conversion rate on Mobile.
  - *Channel A outperforms Channel B in both individual segments.*
  - However, if Channel B receives 90% of its traffic from Desktop while Channel A receives 90% from Mobile, Channel B's aggregated conversion will appear significantly higher than Channel A's.
* **Analyst Rule**: Always segment aggregated business metrics by key confounding dimensions (Platform, Geography, Device, User Tenure).

### 5.2 Correlation vs Causation & Confounding
* Stating that *"Users who enable push notifications have a 30% higher retention rate"* does NOT prove push notifications cause retention.
* Highly engaged, loyal users naturally opt into notifications (self-selection bias).
* Proof of incremental lift requires a controlled randomized experiment (A/B Test).
