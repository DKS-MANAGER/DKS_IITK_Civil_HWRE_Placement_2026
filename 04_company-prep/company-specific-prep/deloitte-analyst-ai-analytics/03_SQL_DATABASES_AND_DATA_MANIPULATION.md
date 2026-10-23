# Module 03: SQL, Relational Databases, and Advanced Data Manipulation

> **Module Code**: DEL-M03  
> **Priority**: P1 (Core Foundation — Absolute Assessment Gate)  
> **Target Assessment**: Online Technical MCQs, Coding Tests, and Live Technical Interview Query Writing  
> **Standard**: Complete theoretical foundations, ANSI/PostgreSQL SQL queries, synthetic schemas, expected table outputs, window functions, and query optimization.

---

## 1. Relational Database Foundations & Query Execution Mechanics

### 1.1 The Relational Model, Grain, and Normalization

* **Table Grain**: The fundamental real-world business event or entity that a single row in the table represents. If the grain of a table is not clearly identified, analytical queries produce disastrous join fan-outs and multiplied sums.
* **Database Normalization**:
  * **1NF (First Normal Form)**: Atomic column values; no repeating groups; unique primary key identifying every row.
  * **2NF (Second Normal Form)**: Must be in 1NF and exhibit **no partial dependencies** (every non-key attribute must depend on the whole primary key, not a subset of a composite key).
  * **3NF (Third Normal Form)**: Must be in 2NF and exhibit **no transitive dependencies** (non-key columns cannot depend on other non-key columns: $X \to Y$ and $Y \to Z$).
  * **BCNF (Boyce-Codd Normal Form)**: A stricter 3NF where for every functional dependency $X \to Y$, $X$ must be a super key.

---

### 1.2 The Logical SQL Query Execution Order

Understanding the logical execution order is essential for avoiding syntax errors such as attempting to reference a column alias created in `SELECT` inside a `WHERE` clause:

```
1. FROM         -> Identifies source tables and performs Cartesian products
2. ON           -> Evaluates join condition filters
3. JOIN         -> Materializes joined virtual table
4. WHERE        -> Filters rows before aggregation (cannot see aggregate aliases)
5. GROUP BY     -> Aggregates records into distinct groups
6. HAVING       -> Filters aggregated groups (can use aggregate expressions)
7. SELECT       -> Evaluates expressions, selects output columns, assigns aliases
8. DISTINCT     -> Deduplicates output rows
9. ORDER BY     -> Sorts rows (CAN reference SELECT aliases and ordinal numbers)
10. LIMIT / OFFSET -> Restricts returned row count (pagination)
```

---

### 1.3 Three-Valued Logic and NULL Semantics

SQL uses a three-valued logic system: `TRUE`, `FALSE`, and `UNKNOWN`.
* `NULL` represents missing or unknown information.
* Any comparison with `NULL` using `=`, `!=`, `<`, or `>` yields `UNKNOWN`.
  ```sql
  NULL = NULL;    -- Evaluates to UNKNOWN
  NULL != NULL;   -- Evaluates to UNKNOWN
  NULL IS NULL;   -- Evaluates to TRUE
  ```
* In `WHERE` and `HAVING` filters, a row is retained **only if the predicate evaluates strictly to `TRUE`**. Rows evaluating to `UNKNOWN` or `FALSE` are filtered out.
* **The Dangerous `NOT IN` Trap**:
  ```sql
  -- If subquery returns ANY null value:
  SELECT * FROM employees WHERE department_id NOT IN (10, 20, NULL);
  -- Logically rewrites to:
  -- (department_id != 10) AND (department_id != 20) AND (department_id != NULL)
  -- Since (col != NULL) is UNKNOWN, the entire condition evaluates to UNKNOWN!
  -- Result: ZERO rows returned! Always use NOT EXISTS or filter out NULLs in subquery!
  ```

---

## 2. Synthetic Enterprise Schema & Sample Data

All queries in this module run against this realistic enterprise consulting, client transaction, and payroll database:

```sql
-- DDL Definitions
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50),
    location VARCHAR(50)
);

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(100),
    dept_id INT REFERENCES departments(dept_id),
    salary NUMERIC(10, 2),
    manager_id INT REFERENCES employees(emp_id),
    join_date DATE
);

CREATE TABLE clients (
    client_id INT PRIMARY KEY,
    client_name VARCHAR(100),
    industry VARCHAR(50),
    region VARCHAR(50)
);

CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100),
    client_id INT REFERENCES clients(client_id),
    budget NUMERIC(12, 2),
    status VARCHAR(20)
);

CREATE TABLE timesheets (
    entry_id INT PRIMARY KEY,
    project_id INT REFERENCES projects(project_id),
    emp_id INT REFERENCES employees(emp_id),
    work_date DATE,
    hours_billed NUMERIC(5, 2)
);
```

### Sample Data State
```sql
INSERT INTO departments VALUES
(1, 'AI & Data Analytics', 'Hyderabad'),
(2, 'Cloud Engineering', 'Bengaluru'),
(3, 'Technology Strategy', 'Gurugram');

INSERT INTO employees VALUES
(101, 'Aditi Sharma', 1, 150000.00, NULL, '2020-01-15'),
(102, 'Rohan Verma', 2, 120000.00, 101, '2021-03-10'),
(103, 'Sneha Patel', 1, 135000.00, 101, '2021-07-01'),
(104, 'Vikram Nair', 2, 95000.00, 102, '2022-09-15'),
(105, 'Ananya Roy', 1, 135000.00, 101, '2023-02-20'),
(106, 'Karan Joshi', 3, 110000.00, 101, '2022-11-05'),
(107, 'Pooja Iyer', 3, 110000.00, 106, '2023-08-12');

INSERT INTO clients VALUES
(1, 'Global Retail Corp', 'Retail', 'US-East'),
(2, 'Apex Healthcare', 'Healthcare', 'US-West'),
(3, 'FinTech Solutions', 'Banking', 'EMEA');

INSERT INTO projects VALUES
(201, 'GenAI Customer Assistant', 1, 450000.00, 'Active'),
(202, 'Cloud Lakehouse Migration', 1, 600000.00, 'Active'),
(203, 'EHR Data Interoperability', 2, 350000.00, 'Active'),
(204, 'Core Banking Modernization', 3, 900000.00, 'On-Hold');

INSERT INTO timesheets VALUES
(1, 201, 101, '2024-03-01', 8.0),
(2, 201, 103, '2024-03-01', 7.5),
(3, 202, 102, '2024-03-01', 8.0),
(4, 201, 101, '2024-03-02', 8.5),
(5, 203, 103, '2024-03-02', 6.0),
(6, 201, 105, '2024-03-02', 8.0),
(7, 202, 104, '2024-03-03', 7.0);
```

---

## 3. 15 Master Enterprise SQL Queries for Technical Tests & Interviews

---

### Query 1: Second Highest Salary (Generalizable to N-th Highest)
* **Relevance**: **Explicitly asked in Ayush Kumar's Deloitte USI technical interview**.
* **Problem**: Write a SQL query to find the second highest salary from the `employees` table. If there is no second highest salary, return `NULL`.

#### Approach 1: Dense Rank CTE (Recommended Production Standard)
```sql
WITH RankedSalaries AS (
    SELECT 
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) AS salary_rank
    FROM employees
)
SELECT MAX(salary) AS second_highest_salary
FROM RankedSalaries
WHERE salary_rank = 2;
```

#### Approach 2: Correlated Subquery / Limit-Offset
```sql
-- Using Subquery to handle duplicate salaries correctly:
SELECT MAX(salary) AS second_highest_salary
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- Generalized N-th highest salary using LIMIT / OFFSET:
SELECT DISTINCT salary AS nth_highest_salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1; -- OFFSET 1 returns the 2nd highest; OFFSET (N-1) returns N-th
```

**Expected Output:**
```
+-----------------------+
| second_highest_salary |
+-----------------------+
| 135000.00             |
+-----------------------+
```
*(Notice: Aditi has 150k. Sneha and Ananya both earn 135k. DENSE_RANK assigns rank 2 to both 135k values, correctly identifying 135k as the distinct second highest salary).*

---

### Query 2: Highest Salary in Each Department
* **Problem**: Find the employees who have the highest salary in their respective departments.

```sql
WITH RankedEmployees AS (
    SELECT 
        e.emp_id,
        e.name AS employee_name,
        d.dept_name,
        e.salary,
        DENSE_RANK() OVER (
            PARTITION BY e.dept_id 
            ORDER BY e.salary DESC
        ) AS dept_rank
    FROM employees e
    JOIN departments d ON e.dept_id = d.dept_id
)
SELECT 
    dept_name,
    employee_name,
    salary
FROM RankedEmployees
WHERE dept_rank = 1
ORDER BY dept_name;
```

**Expected Output:**
```
+---------------------+---------------+-----------+
| dept_name           | employee_name | salary    |
+---------------------+---------------+-----------+
| AI & Data Analytics | Aditi Sharma  | 150000.00 |
| Cloud Engineering   | Rohan Verma   | 120000.00 |
| Technology Strategy | Karan Joshi   | 110000.00 |
| Technology Strategy | Pooja Iyer    | 110000.00 |
+---------------------+---------------+-----------+
```
*(Notice: In Technology Strategy, Karan and Pooja tie with 110k; DENSE_RANK correctly returns both candidates).*

---

### Query 3: Employees Earning More than Their Direct Managers (Self-Join)
* **Problem**: Identify all employees whose compensation strictly exceeds that of their direct managers.

```sql
SELECT 
    e.name AS employee_name,
    e.salary AS employee_salary,
    m.name AS manager_name,
    m.salary AS manager_salary
FROM employees e
JOIN employees m ON e.manager_id = m.emp_id
WHERE e.salary > m.salary;
```

**Mechanics**:
- `employees e` represents the subordinate record.
- `employees m` represents the manager record matched on `e.manager_id = m.emp_id`.
- The `WHERE` clause filters only pairs where subordinate salary exceeds manager salary.
- Self-joins must always use clear alias naming conventions (`e` for employee, `m` for manager).

---

### Query 4: Clients with No Active Projects (Anti-Join / NOT EXISTS)
* **Problem**: Find all clients who currently have no projects with `'Active'` status.

```sql
-- Preferred Idiomatic Approach using NOT EXISTS:
SELECT c.client_id, c.client_name, c.industry
FROM clients c
WHERE NOT EXISTS (
    SELECT 1 
    FROM projects p
    WHERE p.client_id = c.client_id 
      AND p.status = 'Active'
);
```

**Why NOT EXISTS over NOT IN?**
- `NOT EXISTS` short-circuits as soon as a single match is found.
- `NOT EXISTS` handles `NULL` values safely, unlike `NOT IN` which evaluates to `UNKNOWN` if any subquery row contains `NULL`.

---

### Query 5: Join Fan-Out Prevention in Multi-Table Aggregation
* **Problem**: Calculate total budget allocated to each client and the total hours billed across all their projects, without inflating budgets due to timesheet row multiplication.

```sql
-- CORRECT: Aggregate timesheets BEFORE joining to projects and clients
WITH aggregated_hours AS (
    SELECT 
        project_id, 
        SUM(hours_billed) AS total_project_hours
    FROM timesheets
    GROUP BY project_id
),
client_project_summary AS (
    SELECT 
        p.client_id,
        SUM(p.budget) AS total_client_budget,
        SUM(COALESCE(ah.total_project_hours, 0)) AS total_client_hours
    FROM projects p
    LEFT JOIN aggregated_hours ah ON p.project_id = ah.project_id
    GROUP BY p.client_id
)
SELECT 
    c.client_name,
    c.industry,
    COALESCE(cps.total_client_budget, 0) AS total_budget,
    COALESCE(cps.total_client_hours, 0) AS total_hours_billed
FROM clients c
LEFT JOIN client_project_summary cps ON c.client_id = cps.client_id
ORDER BY total_budget DESC;
```

---

### Query 6: Running Total and Moving Average of Billed Hours
* **Problem**: For each employee, compute a cumulative running total of hours billed ordered by date, alongside a 2-entry moving average.

```sql
SELECT 
    t.emp_id,
    e.name,
    t.work_date,
    t.hours_billed,
    SUM(t.hours_billed) OVER (
        PARTITION BY t.emp_id 
        ORDER BY t.work_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total_hours,
    ROUND(AVG(t.hours_billed) OVER (
        PARTITION BY t.emp_id 
        ORDER BY t.work_date
        ROWS BETWEEN 1 PRECEDING AND CURRENT ROW
    ), 2) AS moving_2day_avg_hours
FROM timesheets t
JOIN employees e ON t.emp_id = e.emp_id
ORDER BY t.emp_id, t.work_date;
```

---

### Query 7: Month-over-Month (MoM) Growth using LAG()
* **Problem**: Given monthly project revenue billing, calculate the percentage revenue change compared to the previous month.

```sql
WITH monthly_billing AS (
    SELECT 
        DATE_TRUNC('month', t.work_date) AS bill_month,
        SUM(t.hours_billed * 150.00) AS total_revenue -- Assume flat $150/hr billing
    FROM timesheets t
    GROUP BY DATE_TRUNC('month', t.work_date)
)
SELECT 
    bill_month,
    total_revenue,
    LAG(total_revenue, 1) OVER (ORDER BY bill_month) AS prev_month_revenue,
    ROUND(
        ((total_revenue - LAG(total_revenue, 1) OVER (ORDER BY bill_month)) / 
         NULLIF(LAG(total_revenue, 1) OVER (ORDER BY bill_month), 0)) * 100.0, 
        2
    ) AS mom_growth_pct
FROM monthly_billing
ORDER BY bill_month;
```

---

### Query 8: Consecutive Active Days / Gaps and Islands Problem
* **Problem**: Find employees who billed hours for at least 2 consecutive calendar days.

```sql
WITH unique_dates AS (
    SELECT DISTINCT emp_id, work_date
    FROM timesheets
),
dated_groups AS (
    SELECT 
        emp_id,
        work_date,
        work_date - (ROW_NUMBER() OVER (PARTITION BY emp_id ORDER BY work_date) * INTERVAL '1 day') AS island_group
    FROM unique_dates
)
SELECT 
    emp_id,
    island_group,
    COUNT(*) AS consecutive_days,
    MIN(work_date) AS streak_start,
    MAX(work_date) AS streak_end
FROM dated_groups
GROUP BY emp_id, island_group
HAVING COUNT(*) >= 2;
```

**Mathematical Insight**:
If dates are consecutive ($D_1, D_2, D_3$), subtracting the sequential index ($1, 2, 3$) days yields the exact same constant base date ($D_i - i \cdot \text{day} = C$). When a gap occurs, the base date shifts to a new "island". Grouping by this calculated base date collapses consecutive streaks into distinct groups.

---

### Query 9: Deduplicating Records While Keeping Lowest ID
* **Problem**: In a table with duplicate entries (e.g. repeated timesheet entries), delete the duplicate rows, keeping only the row with the minimum `entry_id`.

```sql
-- Syntax for PostgreSQL / MySQL 8.0:
DELETE FROM timesheets
WHERE entry_id IN (
    SELECT entry_id
    FROM (
        SELECT 
            entry_id,
            ROW_NUMBER() OVER (
                PARTITION BY project_id, emp_id, work_date 
                ORDER BY entry_id ASC
            ) AS row_num
        FROM timesheets
    ) duplicates
    WHERE duplicates.row_num > 1
);
```

---

### Query 10: Pivot Table / Cross-Tabulation using CASE WHEN
* **Problem**: Summarize employee headcount and total salary expenditure across departments into a horizontal executive matrix.

```sql
SELECT 
    d.location,
    COUNT(CASE WHEN d.dept_name = 'AI & Data Analytics' THEN e.emp_id END) AS ai_headcount,
    SUM(CASE WHEN d.dept_name = 'AI & Data Analytics' THEN e.salary ELSE 0 END) AS ai_payroll,
    COUNT(CASE WHEN d.dept_name = 'Cloud Engineering' THEN e.emp_id END) AS cloud_headcount,
    SUM(CASE WHEN d.dept_name = 'Cloud Engineering' THEN e.salary ELSE 0 END) AS cloud_payroll,
    COUNT(e.emp_id) AS total_headcount,
    SUM(e.salary) AS total_payroll
FROM departments d
LEFT JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.location
ORDER BY total_payroll DESC;
```

---

### Query 11: Median Salary by Department (Without Built-in MEDIAN)
* **Problem**: Compute the exact median salary for each department.

```sql
WITH RankedSalaries AS (
    SELECT 
        dept_id,
        salary,
        ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary ASC) AS asc_rank,
        ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS desc_rank
    FROM employees
)
SELECT 
    dept_id,
    ROUND(AVG(salary), 2) AS median_salary
FROM RankedSalaries
WHERE asc_rank = desc_rank        -- For odd number of elements (middle element)
   OR asc_rank = desc_rank + 1    -- For even number of elements (lower middle)
   OR asc_rank + 1 = desc_rank    -- For even number of elements (upper middle)
GROUP BY dept_id;
```

---

### Query 12: Finding Gaps in Sequential IDs
* **Problem**: Detect missing `entry_id` integers in the `timesheets` table.

```sql
WITH numbered_sequence AS (
    SELECT 
        entry_id,
        LEAD(entry_id, 1) OVER (ORDER BY entry_id) AS next_id
    FROM timesheets
)
SELECT 
    entry_id + 1 AS gap_start,
    next_id - 1 AS gap_end
FROM numbered_sequence
WHERE next_id - entry_id > 1;
```

---

### Query 13: Top-N Percentile Distribution using NTILE()
* **Problem**: Segment employees into 4 compensation quartiles (`NTILE(4)`) within each department.

```sql
SELECT 
    emp_id,
    name,
    dept_id,
    salary,
    NTILE(4) OVER (
        PARTITION BY dept_id 
        ORDER BY salary DESC
    ) AS salary_quartile
FROM employees;
```

---

### Query 14: Recursive CTE for Organizational Reporting Hierarchy
* **Problem**: Starting from Aditi Sharma (CEO/Partner, `manager_id IS NULL`), generate the full reporting tree with depth level and reporting path.

```sql
WITH RECURSIVE OrgHierarchy AS (
    -- Anchor Member: Root executives
    SELECT 
        emp_id,
        name,
        manager_id,
        1 AS level,
        CAST(name AS VARCHAR(255)) AS reporting_chain
    FROM employees
    WHERE manager_id IS NULL
    
    UNION ALL
    
    -- Recursive Member: Subordinates joining to their managers
    SELECT 
        e.emp_id,
        e.name,
        e.manager_id,
        o.level + 1 AS level,
        CAST(o.reporting_chain || ' -> ' || e.name AS VARCHAR(255)) AS reporting_chain
    FROM employees e
    JOIN OrgHierarchy o ON e.manager_id = o.emp_id
)
SELECT 
    level,
    emp_id,
    name,
    reporting_chain
FROM OrgHierarchy
ORDER BY level, emp_id;
```

---

### Query 15: Cross Join Matrix Generation & Zero-Filling Aggregates
* **Problem**: Display all combinations of clients and departments, showing 0 for combinations that have zero active projects.

```sql
WITH all_client_depts AS (
    SELECT c.client_id, c.client_name, d.dept_id, d.dept_name
    FROM clients c
    CROSS JOIN departments d
),
active_project_counts AS (
    SELECT 
        p.client_id,
        1 AS dept_id, -- Assume AI projects map to dept 1
        COUNT(*) AS active_projects
    FROM projects p
    WHERE p.status = 'Active'
    GROUP BY p.client_id
)
SELECT 
    acd.client_name,
    acd.dept_name,
    COALESCE(apc.active_projects, 0) AS total_active_projects
FROM all_client_depts acd
LEFT JOIN active_project_counts apc 
       ON acd.client_id = apc.client_id 
      AND acd.dept_id = apc.dept_id
ORDER BY acd.client_name, acd.dept_name;
```

---

## 4. Database Performance, Indexing, and Concurrency

### 4.1 Index Architectures & Optimization Mechanics

* **B-Tree Index**: The standard balanced search tree (depth 3–4 for millions of rows).
  - Handles equality (`=`), range scans (`<`, `<=`, `>`, `>=`, `BETWEEN`), and prefix sorting (`ORDER BY`).
  - Index column order matters: In a composite index `(dept_id, salary)`, queries filtering on `salary` alone cannot utilize the index (Leftmost Prefix Rule).
* **Hash Index**: $O(1)$ equality lookups only. Does not support range queries or sorting.
* **Covering Index**: An index that includes all columns referenced in the query (`SELECT`, `WHERE`, `JOIN`, `ORDER BY`), enabling an **Index-Only Scan** without touching the underlying heap table.
* **Execution Plan Reading (`EXPLAIN ANALYZE`)**:
  - `Seq Scan` (Sequential Table Scan): Reads every page from disk; acceptable only for tiny tables or when fetching >30% of rows.
  - `Index Scan`: Traverses the B-tree to find matching row pointers, then visits table heap pages.
  - `Index Only Scan`: Reads purely from the index pages in memory; fastest execution.
  - `Hash Join` vs `Nested Loop` vs `Merge Join`.

---

### 4.2 ACID Transactions & Isolation Levels

* **Atomicity**: All operations commit or all roll back together.
* **Consistency**: DB transitions strictly from one valid schema state to another.
* **Isolation**: Concurrent transactions cannot observe incomplete intermediate states.
* **Durability**: Committed transactions survive hardware crashes via Write-Ahead Logging (WAL).

| Isolation Level | Dirty Read | Non-Repeatable Read | Phantom Read |
| :--- | :---: | :---: | :---: |
| **Read Uncommitted** | Possible | Possible | Possible |
| **Read Committed** | **Prevented** | Possible | Possible |
| **Repeatable Read** | **Prevented** | **Prevented** | Possible (Standard SQL) |
| **Serializable** | **Prevented** | **Prevented** | **Prevented** |

* **Concurrency Phenomena**:
  - **Dirty Read**: Transaction A reads data modified by uncommitted Transaction B.
  - **Non-Repeatable Read**: Transaction A reads a row, Transaction B updates that row and commits, Transaction A re-reads and sees different values.
  - **Phantom Read**: Transaction A queries a range of rows, Transaction B inserts a new row matching that range and commits, Transaction A re-queries and sees new "phantom" rows.
