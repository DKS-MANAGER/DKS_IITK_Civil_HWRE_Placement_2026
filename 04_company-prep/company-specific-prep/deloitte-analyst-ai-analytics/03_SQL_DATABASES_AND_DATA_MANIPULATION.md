# Module 03: SQL, Relational Databases, and Advanced Data Manipulation

> **Module Code**: DEL-M03  
> **Priority**: P1 (Core Foundation — Absolute Assessment Gate)  
> **Target Assessment**: Online Technical MCQs, Coding Tests, and Live Technical Interview Query Writing  
> **Standard**: Complete theoretical explanations, three-valued logic proofs, executable ANSI/PostgreSQL SQL queries, synthetic schemas, window functions, and query optimization.

---

## 1. Relational Database Foundations & Three-Valued Logic

### 1.1 Relational Schema, Grain, and Normalization

* **Table Grain**: The fundamental business event or entity that a single row in the table represents. If the grain is not explicitly defined, queries produce catastrophic aggregations and join fan-outs.
* **Database Normalization (1NF to 3NF)**:
  * **1NF (First Normal Form)**: Atomic values in each column; no repeating groups or arrays stored as delimited text; primary key uniquely identifies every record.
  * **2NF (Second Normal Form)**: In 1NF and **no partial dependency** (every non-key attribute must depend on the whole candidate key, not a proper subset of a composite key).
  * **3NF (Third Normal Form)**: In 2NF and **no transitive dependency** ($X \to Y$ and $Y \to Z$ where $Z$ depends on non-key $Y$).

---

### 1.2 NULL Semantics and Three-Valued Logic

SQL does not use two-valued boolean logic (`TRUE`/`FALSE`). It operates on **Three-Valued Logic**: `TRUE`, `FALSE`, and `UNKNOWN`.

* `NULL` represents the **absence of a value** or **unknown state**.
* Comparing any value with `NULL` using `=` or `!=` yields `UNKNOWN`, never `TRUE` or `FALSE`.
  ```sql
  -- Both evaluate to UNKNOWN!
  NULL = NULL;   -- UNKNOWN
  NULL != NULL;  -- UNKNOWN
  ```
* In `WHERE` clauses, records are kept **only if the predicate evaluates strictly to `TRUE`**. Rows yielding `UNKNOWN` or `FALSE` are discarded.
* **The `NOT IN` Trap with NULLs**:
  ```sql
  -- If subquery returns ANY null value:
  SELECT * FROM employees WHERE department_id NOT IN (10, 20, NULL);
  -- Rewrites internally to:
  -- (department_id != 10) AND (department_id != 20) AND (department_id != NULL)
  -- Since (department_id != NULL) is UNKNOWN, the entire condition evaluates to UNKNOWN!
  -- RESULT: Returns ZERO rows! Always use NOT EXISTS or filter out NULLs in subquery!
  ```

---

## 2. Synthetic Enterprise Schema for Practice

To ground all queries, we define a realistic enterprise consulting and client transaction database:

```sql
-- DDL Definitions
CREATE TABLE clients (
    client_id INT PRIMARY KEY,
    client_name VARCHAR(100),
    industry VARCHAR(50),
    contract_start_date DATE
);

CREATE TABLE consultants (
    consultant_id INT PRIMARY KEY,
    name VARCHAR(100),
    practice VARCHAR(50),       -- 'AI & Data', 'Cloud', 'ERP'
    hourly_rate NUMERIC(10, 2),
    manager_id INT
);

CREATE TABLE project_engagements (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100),
    client_id INT REFERENCES clients(client_id),
    total_budget NUMERIC(12, 2),
    status VARCHAR(20)           -- 'Active', 'Completed', 'On-Hold'
);

CREATE TABLE timesheet_entries (
    entry_id INT PRIMARY KEY,
    project_id INT REFERENCES project_engagements(project_id),
    consultant_id INT REFERENCES consultants(consultant_id),
    work_date DATE,
    hours_logged NUMERIC(5, 2)
);
```

### Synthetic Data Population
```sql
INSERT INTO clients VALUES
(1, 'Global Retail Corp', 'Retail', '2023-01-15'),
(2, 'Apex Healthcare', 'Healthcare', '2023-06-01'),
(3, 'FinTech Solutions', 'Banking', '2024-02-10');

INSERT INTO consultants VALUES
(101, 'Aditi Sharma', 'AI & Data', 95.00, NULL),
(102, 'Rohan Verma', 'Cloud', 75.00, 101),
(103, 'Sneha Patel', 'AI & Data', 85.00, 101),
(104, 'Vikram Nair', 'ERP', 65.00, 102);

INSERT INTO project_engagements VALUES
(201, 'GenAI Customer Assistant', 1, 450000.00, 'Active'),
(202, 'Cloud Lakehouse Migration', 1, 600000.00, 'Active'),
(203, 'EHR Data Interoperability', 2, 350000.00, 'Active'),
(204, 'Core Banking Modernization', 3, 900000.00, 'On-Hold');

INSERT INTO timesheet_entries VALUES
(1, 201, 101, '2024-03-01', 8.0),
(2, 201, 103, '2024-03-01', 7.5),
(3, 202, 102, '2024-03-01', 8.0),
(4, 201, 101, '2024-03-02', 8.5),
(5, 203, 103, '2024-03-02', 6.0);
```

---

## 3. Advanced Querying Patterns & Technical Mechanics

### 3.1 Multi-Table Joins & Join Fan-Out Prevention

* **Join Fan-Out**: Occurs when joining a parent table (grain: 1 row per project) to a child table with multiple matching rows (timesheets), causing rows from the parent table to duplicate. Subsequent sums on parent columns (like `total_budget`) produce falsely inflated numbers!

```sql
-- WRONG (Demonstrating Join Fan-Out on Budget):
SELECT p.project_name, SUM(p.total_budget) AS false_budget
FROM project_engagements p
JOIN timesheet_entries t ON p.project_id = t.project_id
GROUP BY p.project_name;
-- GenAI project will count 450,000 THREE times = 1,350,000!

-- CORRECT (Aggregate the Child First via CTE or Subquery):
WITH project_hours AS (
    SELECT project_id, SUM(hours_logged) AS total_hours
    FROM timesheet_entries
    GROUP BY project_id
)
SELECT 
    p.project_name,
    p.total_budget,
    COALESCE(ph.total_hours, 0) AS total_hours_billed
FROM project_engagements p
LEFT JOIN project_hours ph ON p.project_id = ph.project_id;
```

---

### 3.2 Window Functions: Mechanics, Framing, and Ranking

Window functions perform calculations across a set of table rows related to the current row without collapsing them into a single summary row.

$$\text{FUNCTION}() \; \text{OVER} \; (\text{PARTITION BY } col1 \; \text{ORDER BY } col2 \; \text{ROWS BETWEEN ...})$$

#### Ranking Functions Compared
* `ROW_NUMBER()`: Strict unique sequential integer ($1, 2, 3, 4$).
* `RANK()`: Ties get same rank; leaves gaps ($1, 2, 2, 4$).
* `DENSE_RANK()`: Ties get same rank; leaves **no gaps** ($1, 2, 2, 3$).

#### Worked Query 1: Top-2 Paid Consultants per Practice
```sql
WITH RankedConsultants AS (
    SELECT 
        consultant_id,
        name,
        practice,
        hourly_rate,
        DENSE_RANK() OVER (
            PARTITION BY practice 
            ORDER BY hourly_rate DESC
        ) AS rank_in_practice
    FROM consultants
)
SELECT 
    practice,
    name,
    hourly_rate,
    rank_in_practice
FROM RankedConsultants
WHERE rank_in_practice <= 2
ORDER BY practice, rank_in_practice;
```

#### Worked Query 2: Running Total and Moving Average
```sql
SELECT 
    consultant_id,
    work_date,
    hours_logged,
    -- Running Cumulative Total:
    SUM(hours_logged) OVER (
        PARTITION BY consultant_id 
        ORDER BY work_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total_hours,
    -- 7-Day Moving Average:
    AVG(hours_logged) OVER (
        PARTITION BY consultant_id 
        ORDER BY work_date
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS moving_7d_avg_hours
FROM timesheet_entries;
```

---

### 3.3 Conditional Aggregation & Matrix Pivoting

Transforming transactional rows into column-based executive summary tables using `CASE`:

```sql
SELECT 
    c.practice,
    COUNT(DISTINCT c.consultant_id) AS total_consultants,
    COUNT(CASE WHEN c.hourly_rate >= 80 THEN 1 END) AS senior_tier_count,
    COUNT(CASE WHEN c.hourly_rate < 80 THEN 1 END) AS junior_tier_count,
    ROUND(AVG(c.hourly_rate), 2) AS avg_practice_rate
FROM consultants c
GROUP BY c.practice;
```

---

## 4. Query Performance, Indexing, and Concurrency

### 4.1 Indexes: B-Tree vs. Hash
* **B-Tree Index**: The standard balanced search tree. Supports equality (`=`), range queries (`<`, `<=`, `>`, `>=`, `BETWEEN`), and prefix sorting (`ORDER BY`). Depth is typically 3 to 4 levels for millions of records.
* **Hash Index**: Supports only equality lookups ($O(1)$). No range or sorting capability.
* **Covering Index**: An index that contains all columns requested by the `SELECT` query, allowing the database engine to satisfy the query entirely from the index tree without performing expensive table heap lookups.

### 4.2 ACID Transactions & Concurrency Anomalies
* **Atomicity**: All changes succeed or entire transaction rolls back.
* **Consistency**: DB transitions strictly from one valid state to another satisfying all schema constraints.
* **Isolation**: Transactions executing concurrently do not interfere with one another.
* **Durability**: Committed data survives system crashes via Write-Ahead Logging (WAL).

| Isolation Level | Dirty Read | Non-Repeatable Read | Phantom Read |
| :--- | :---: | :---: | :---: |
| **Read Uncommitted** | Yes | Yes | Yes |
| **Read Committed** | **No** | Yes | Yes |
| **Repeatable Read** | **No** | **No** | Yes (in standard SQL) |
| **Serializable** | **No** | **No** | **No** |

---

## 5. Self-Assessment Checklist

- [ ] Can explain three-valued logic and demonstrate why `NOT IN` with `NULL` returns empty results.
- [ ] Understand the mechanism of Join Fan-Out and know how to avoid aggregating multiplied child rows.
- [ ] Confident writing `ROW_NUMBER`, `RANK`, and `DENSE_RANK` with correct partition definitions.
- [ ] Can write window frame specifications (`ROWS BETWEEN 3 PRECEDING AND CURRENT ROW`).
- [ ] Understand B-tree index structures, covering indexes, and ACID isolation levels.
