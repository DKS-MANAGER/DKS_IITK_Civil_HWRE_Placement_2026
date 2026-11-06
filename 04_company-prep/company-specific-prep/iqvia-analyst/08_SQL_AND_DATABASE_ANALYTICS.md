# Module 08: SQL & Relational Database Analytics

> **Document Status**: Production-Grade Applied Reference `[TIER 4 / ANSI SQL & RELATIONAL DBMS BENCHMARKS]`  
> **Core Focus**: Commercial Schema Design, Window Functions, CTEs, Joins, Query Optimization, and Pharma Live Interview Coding Bank  
> **Target Role**: Analyst (IQVIA India)  

---

## 1. Relational Healthcare Commercial Data Architecture

Commercial analysts at IQVIA query enterprise data warehouses (Snowflake, AWS Redshift, Google BigQuery, PostgreSQL) to join syndicated prescription data with sales-force activity logs.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 SIMULATED PHARMA COMMERCIAL RELATIONAL SCHEMA               │
├──────────────────────────┬──────────────────────────┬───────────────────────┤
│ TABLE: dim_hcp           │ TABLE: fact_prescription │ TABLE: fact_detailing │
├──────────────────────────┼──────────────────────────┼───────────────────────┤
│ • npi_id (PK, VARCHAR)   │ • trx_id (PK, BIGINT)    │ • call_id (PK, BIGINT)│
│ • first_name (VARCHAR)   │ • npi_id (FK, VARCHAR)   │ • npi_id (FK, VARCHAR)│
│ • last_name (VARCHAR)    │ • product_id (FK, INT)   │ • rep_id (VARCHAR)    │
│ • specialty (VARCHAR)    │ • claim_date (DATE)      │ • call_date (DATE)    │
│ • territory_id (VARCHAR) │ • trx_count (INT)        │ • channel (VARCHAR)   │
│ • state (CHAR(2))        │ • nrx_count (INT)        │ • details_count (INT) │
│ • decile_tier (INT)      │ • units_dispensed (INT)  │ • sample_units (INT)  │
└──────────────────────────┴──────────────────────────┴───────────────────────┘
```

---

## 2. Logical Query Processing Order (Execution Flow)

Writing optimized SQL requires understanding that the SQL engine does not execute clauses in the order they are written (`SELECT ... FROM ... WHERE`):

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      LOGICAL SQL QUERY PROCESSING PHASES                    │
│ 1. FROM & JOIN     : Identify and join source tables                         │
│ 2. WHERE           : Filter individual rows before grouping                 │
│ 3. GROUP BY        : Collapse rows into aggregated buckets                  │
│ 4. HAVING          : Filter collapsed groups based on aggregate results     │
│ 5. SELECT          : Compute expressions, aliases, and projection columns   │
│ 6. WINDOW FUNCTIONS: Evaluate OVER (PARTITION BY ... ORDER BY ...) clauses  │
│ 7. DISTINCT        : Eliminate duplicate result rows                        │
│ 8. ORDER BY        : Sort final projected result set                        │
│ 9. LIMIT / OFFSET  : Paginate and restrict output row count                 │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. High-Yield Window Functions (Analytical Functions)

Window functions perform calculations across a set of table rows related to the current row, without collapsing the individual rows into a single summary line.

### 3.1 Ranking Functions: `ROW_NUMBER()` vs `RANK()` vs `DENSE_RANK()` vs `NTILE()`
* **`ROW_NUMBER()`**: Unique sequential integer ($1, 2, 3, 4$). Ties receive arbitrary distinct numbers.
* **`RANK()`**: Assigns identical rank to ties, but leaves gaps ($1, 2, 2, 4$).
* **`DENSE_RANK()`**: Assigns identical rank to ties without gaps ($1, 2, 2, 3$). **Preferred for top-$N$ prescriber queries**.
* **`NTILE(n)`**: Divides ordered rows into $n$ equal frequency buckets (used to compute Deciles 1–10).

### 3.2 Value & Framing Functions: `LAG()`, `LEAD()`, and Sliding Frames
```sql
-- Calculating 4-week rolling total prescriptions and week-over-week growth
SELECT 
    product_id,
    week_date,
    weekly_trx,
    -- 1. Lag function: Sales 1 week prior
    LAG(weekly_trx, 1) OVER (
        PARTITION BY product_id 
        ORDER BY week_date
    ) AS prior_week_trx,
    
    -- 2. Sliding window frame: 4-week moving average (current row + 3 preceding weeks)
    AVG(weekly_trx) OVER (
        PARTITION BY product_id 
        ORDER BY week_date 
        ROWS BETWEEN 3 PRECEDING AND CURRENT ROW
    ) AS rolling_4w_avg_trx,
    
    -- 3. Week-over-week percentage velocity
    ROUND(
        (weekly_trx - LAG(weekly_trx, 1) OVER (PARTITION BY product_id ORDER BY week_date)) 
        * 100.0 / NULLIF(LAG(weekly_trx, 1) OVER (PARTITION BY product_id ORDER BY week_date), 0), 
        2
    ) AS wow_growth_pct
FROM weekly_brand_sales;
```

---

## 4. Common Table Expressions (CTEs) & Anti-Joins

CTEs (`WITH ... AS (...)`) improve modular readability, eliminate redundant subqueries, and facilitate clean step-by-step business logic.

### 4.1 Anti-Join Logic: Detecting Churned or Dormant Prescribers
* **Business Problem**: Identify physicians who prescribed Brand X in Q1 2025, but generated zero prescriptions in Q2 2025 (Physician Churn).

```sql
WITH q1_prescribers AS (
    SELECT DISTINCT npi_id
    FROM fact_prescription
    WHERE product_id = 101 
      AND claim_date BETWEEN '2025-01-01' AND '2025-03-31'
),
q2_prescribers AS (
    SELECT DISTINCT npi_id
    FROM fact_prescription
    WHERE product_id = 101 
      AND claim_date BETWEEN '2025-04-01' AND '2025-06-30'
)
SELECT 
    h.npi_id,
    h.first_name,
    h.last_name,
    h.specialty,
    h.territory_id
FROM q1_prescribers q1
LEFT JOIN q2_prescribers q2 
    ON q1.npi_id = q2.npi_id
JOIN dim_hcp h 
    ON q1.npi_id = h.npi_id
WHERE q2.npi_id IS NULL  -- Prescribed in Q1, but absent in Q2 (Anti-Join)
ORDER BY h.territory_id, h.last_name;
```

---

## 5. Live Interview SQL Problem Bank (Pharma Scenarios)

### Problem 1: Top 3 Prescribers per Sales Territory
* **Task**: For each sales territory, find the top 3 highest-prescribing physicians for Brand 'OncoRelief' in the year 2025. If there are ties for 3rd place, include all tied physicians without skipping ranks.

```sql
WITH territory_prescriber_ranks AS (
    SELECT 
        h.territory_id,
        h.npi_id,
        h.first_name,
        h.last_name,
        h.specialty,
        SUM(p.trx_count) AS total_brand_trx,
        DENSE_RANK() OVER (
            PARTITION BY h.territory_id 
            ORDER BY SUM(p.trx_count) DESC
        ) AS prescriber_rank
    FROM dim_hcp h
    INNER JOIN fact_prescription p 
        ON h.npi_id = p.npi_id
    WHERE p.product_id = 502  -- OncoRelief
      AND p.claim_date BETWEEN '2025-01-01' AND '2025-12-31'
    GROUP BY h.territory_id, h.npi_id, h.first_name, h.last_name, h.specialty
)
SELECT 
    territory_id,
    prescriber_rank,
    npi_id,
    CONCAT(first_name, ' ', last_name) AS physician_name,
    specialty,
    total_brand_trx
FROM territory_prescriber_ranks
WHERE prescriber_rank <= 3
ORDER BY territory_id, prescriber_rank;
```

### Problem 2: Promotional Detailing Impact on Physician Conversion
* **Task**: Calculate the average time (in days) between an initial sales representative in-person detailing visit and the physician's very first brand prescription. Only consider physicians who converted within 90 days of their initial call.

```sql
WITH first_detailing AS (
    SELECT 
        npi_id,
        MIN(call_date) AS first_call_date
    FROM fact_detailing
    WHERE channel = 'In-Person Detailing'
    GROUP BY npi_id
),
first_prescription AS (
    SELECT 
        npi_id,
        MIN(claim_date) AS first_trx_date
    FROM fact_prescription
    WHERE product_id = 502
    GROUP BY npi_id
)
SELECT 
    h.specialty,
    COUNT(h.npi_id) AS converted_physicians_count,
    ROUND(AVG(p.first_trx_date - d.first_call_date), 1) AS avg_days_to_first_conversion,
    MIN(p.first_trx_date - d.first_call_date) AS min_days,
    MAX(p.first_trx_date - d.first_call_date) AS max_days
FROM first_detailing d
INNER JOIN first_prescription p 
    ON d.npi_id = p.npi_id
INNER JOIN dim_hcp h 
    ON d.npi_id = h.npi_id
WHERE p.first_trx_date >= d.first_call_date
  AND (p.first_trx_date - d.first_call_date) <= 90
GROUP BY h.specialty
ORDER BY avg_days_to_first_conversion ASC;
```

---

## 6. Query Optimization & Performance Tuning

1. **Indexing Strategy**:
   * Create Composite B-Tree Indexes on foreign keys and date filters: `CREATE INDEX idx_presc_npi_date ON fact_prescription(npi_id, claim_date) INCLUDE (trx_count);`
2. **SARGable WHERE Clauses (Search Argument Able)**:
   * **Bad (Non-SARGable)**: `WHERE YEAR(claim_date) = 2025` (forces full table scan because function must evaluate on every row).
   * **Optimized (SARGable)**: `WHERE claim_date >= '2025-01-01' AND claim_date < '2026-01-01'` (enables index range scan).
3. **Avoid `SELECT *`**:
   * In columnar databases (Snowflake, BigQuery), querying unneeded columns triggers massive I/O read penalties and inflates cloud billing costs.

