# Topic Master 03: Relational Database Architecture, SQL Analytics & Query Execution

> **Consolidated Module**: ACC-JAPAN-TOPIC-03 (SQL & Enterprise Data Manipulation)  
> **Target Assessment**: Online SQL Assessment & Technical Interview Live Query Writing  
> **Structure**:
> - **SECTION A**: Relational Engines, Logical Execution Order, Three-Valued Logic & Join Fan-Out Mechanics
> - **SECTION B**: Synthetic Enterprise ERP Schema & 20 Production SQL Analytics Queries (Window Functions, CTEs, Running Totals)
> - **SECTION C**: Query Performance Optimization: Indexing, EXPLAIN Query Plans & Database Normalization (1NF–3NF)

---


# SECTION A: Relational Engines, SQL Internals & Query Execution

Relational Engines, SQL Internals & Query Execution (Priority 1)

### Explainer B.1: The 11-Step Logical Query Processing Pipeline

SQL is a **declarative language** where the developer specifies *what* data to retrieve, not the procedural execution steps. The RDBMS query optimizer translates this declarative statement into an imperative execution plan following a strict mathematical sequence:

```text
Logical Query Execution Pipeline:
(1)  FROM        -> Identifies, loads, and Cartesian-crosses base physical tables
(2)  ON          -> Applies join predicates to filter the Cartesian product
(3)  JOIN        -> Emits matched rows (or injects outer NULLs for LEFT/RIGHT/FULL JOIN)
(4)  WHERE       -> Evaluates row-level predicates before any aggregation occurs
(5)  GROUP BY    -> Organizes surviving rows into distinct partition groups
(6)  HAVING      -> Evaluates aggregate predicates across grouped partitions
(7)  WINDOW      -> Computes analytical functions (OVER PARTITION BY ... ORDER BY ...)
(8)  SELECT      -> Evaluates projection expressions, scalar functions, and assigns aliases
(9)  DISTINCT    -> Eliminates duplicate projected output rows
(10) ORDER BY    -> Sorts final result rows according to specified collations
(11) LIMIT/OFFSET-> Applies pagination bounds and truncates the streaming cursor
```

#### Why This Explains Common Assessment Errors:
* **The `WHERE` Alias Prohibition**: Because Step 4 (`WHERE`) executes long before Step 8 (`SELECT`), writing `WHERE total_revenue > 1000` causes an immediate `Column does not exist` error if `total_revenue` is an alias created in the `SELECT` clause.
* **The `ORDER BY` Alias Permission**: Because Step 10 (`ORDER BY`) executes after Step 8 (`SELECT`), referencing aliases created in `SELECT` is completely valid and encouraged.
* **`WHERE` vs `HAVING` Performance Traps**: Placing a non-aggregate filter into `HAVING` (e.g., `HAVING region = 'Kanto'`) forces the database engine to group *all* rows across the entire company before discarding non-Kanto groups. Moving that predicate into `WHERE region = 'Kanto'` discards non-Kanto rows in Step 4, reducing grouping memory and CPU cycles by $80\%\text{--}90\%$.

---

### Explainer B.2: B+ Tree Index Architecture, Clustered vs Secondary Indexes & SARGability

#### 1. Why RDBMSs Use B+ Trees Instead of Binary Search Trees or Hash Tables
* **High Fanout & Low Tree Depth**: A B+ Tree node matches the operating system disk page size (typically 4 KB or 8 KB). A single node can hold hundreds of keys ($B \approx 100\text{--}500$), keeping tree height to just 3 or 4 levels for hundreds of millions of rows.
* **Sequential Range Scans**: Unlike standard B-Trees, **B+ Trees store data records exclusively in the leaf nodes**. All leaf nodes are linked as a doubly-linked list. To execute `WHERE date BETWEEN '2026-01-01' AND '2026-03-31'`, the engine performs 1 tree traversal ($O(\log N)$) to find the start date, then simply walks the linked leaf list sequentially ($O(K)$) without re-traversing upper tree levels.

#### 2. Clustered Index vs Secondary Non-Clustered Index
* **Clustered Index**: Defines the **physical ordering** of rows on disk. A table can possess **at most one clustered index** (typically the Primary Key). Leaf nodes contain the actual complete table row data pages.
* **Secondary (Non-Clustered) Index**: A separate B+ Tree structure whose leaf nodes contain the indexed column keys plus a pointer back to the base data row:
  - In PostgreSQL: A tuple physical address (`TID` = block number + item offset).
  - In MySQL InnoDB / SQL Server: The clustered index Primary Key value.
* **Index Lookup vs Index Scan vs Index Seek**:
  - **Index Seek**: Engine uses B+ Tree root-to-leaf traversal to pinpoint exact keys ($O(\log N)$). Fastest access path.
  - **Covering Index**: A secondary index that contains all columns requested by the `SELECT` query (either in key or `INCLUDE` clause). Avoids expensive secondary "Bookmark / Key Lookups" back to the clustered table!

#### 3. SARGability (Search Argument Able) Traps
A query is **SARGable** if the optimizer can leverage an index seek rather than resorting to a full index/table scan:
* **Non-SARGable (Index Invalidation)**:
  - Wrapping indexed columns in functions: `WHERE YEAR(order_date) = 2026` (Forces engine to compute `YEAR()` on every single row).
  - *SARGable Fix*: `WHERE order_date >= '2026-01-01' AND order_date < '2027-01-01'`.
  - Leading-edge wildcards: `WHERE customer_name LIKE '%Tanaka'` (B+ Tree cannot use alphabetical prefix ordering; forces full scan).
  - Implicit type conversions: `WHERE phone_number = 9012345678` (where `phone_number` is `VARCHAR`).

---

### Explainer B.3: Query Optimizer Join Algorithms — Nested Loops vs Hash Join vs Merge Join

The Cost-Based Optimizer (CBO) evaluates table statistics histograms and picks among three fundamental join physical operators:

| Join Algorithm | Mechanism & Memory Behavior | Best Fit Scenario | Worst Fit Scenario |
|:---|:---|:---|:---|
| **Nested Loop Join** | Outer loop scans driving table; for each row, inner loop probes index on target table ($O(M \log N)$). | One small table ($M < 100$) joining an indexed large table. | Two massive unindexed tables ($O(M \times N)$ Cartesian explosion). |
| **Hash Join** | Build phase: Hashes smaller table into in-memory hash table. Probe phase: Streams larger table, checking hash keys ($O(M + N)$). | Large unindexed tables where memory is sufficient to store the build table. | Memory-constrained environments where hash spills to disk (*Grace Hash Join*). |
| **Merge Join** | Both tables are sorted by join key, then walked in unison with two pointers ($O(M \log M + N \log N)$). | Massive tables that are already physically sorted by clustered indexes. | Unsorted tables requiring high-cost external sorting. |

---

### Explainer B.4: Aggregation Mechanics, GROUP BY Pipeline & WHERE vs HAVING

* **The Projection Rule**: Every column in `SELECT` must either appear in `GROUP BY` or be wrapped in an aggregate function (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`).
* **`COUNT(*)` vs `COUNT(col)`**:
  - `COUNT(*)` counts physical row emissions from Step 3/4, including all-null rows.
  - `COUNT(col)` evaluates the column value and ignores rows where `col IS NULL`.
  - `COUNT(DISTINCT col)` builds a hash set of non-null values in memory to count cardinality.

```sql
-- Production Analytical Pattern: Regional Revenue & Basket Sizing
SELECT 
    region,
    store_id,
    COUNT(order_id) AS total_orders,
    SUM(order_amount) AS total_revenue,
    ROUND(AVG(order_amount), 2) AS avg_basket_value
FROM store_transactions
WHERE transaction_status = 'SETTLED'     -- Step 4: Row-level filter
GROUP BY region, store_id               -- Step 5: Partition groups
HAVING SUM(order_amount) >= 10000000    -- Step 6: Group aggregate filter
ORDER BY total_revenue DESC             -- Step 10: Sort by alias
LIMIT 5;                                -- Step 11: Top 5 stores
```

---

### Explainer B.5: Window Functions Deep-Dive — Partitioning, Ordering & ROWS vs RANGE Frames

Window functions compute values across sets of rows related to the current row without collapsing rows into a single output.

#### 1. The Ranking Trinity: `ROW_NUMBER()` vs `RANK()` vs `DENSE_RANK()`
Given employee sales: `[¥10M, ¥10M, ¥8M, ¥6M]`:
* `ROW_NUMBER()`: `1, 2, 3, 4` (Strictly sequential; ties broken arbitrarily).
* `RANK()`: `1, 1, 3, 4` (Ties share rank; skips subsequent ranks).
* `DENSE_RANK()`: `1, 1, 2, 3` (Ties share rank; **no gaps** in ranking sequence).

#### 2. Analytical Offsets: `LEAD()` and `LAG()`
* `LAG(col, offset, default)`: Accesses data from $N$ rows prior to the current row. Essential for calculating Month-over-Month (MoM) revenue growth:
  $$\text{MoM Growth \%} = \frac{\text{Revenue} - \text{LAG}(\text{Revenue}, 1)}{\text{LAG}(\text{Revenue}, 1)} \times 100$$
* `LEAD(col, offset, default)`: Accesses data from $N$ rows ahead of the current row.

#### 3. Framing Mechanics: `ROWS` vs `RANGE`
* `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW`: Exact physical 3-row moving average.
* **The Dangerous Default**: Specifying `ORDER BY` without an explicit frame clause defaults to:
  `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`
  In `RANGE` mode, SQL groups all duplicate values of the ordering key together, causing duplicate cumulative sums and performance degradation! Always specify `ROWS` when calculating physical moving averages.

```sql
-- Production Pattern: 7-Day Moving Average & Day-over-Day Growth
SELECT 
    report_date,
    daily_revenue,
    -- Exact 7-day physical moving average
    ROUND(AVG(daily_revenue) OVER (
        ORDER BY report_date 
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ), 2) AS mavg_7d_revenue,
    -- Day-over-Day variance
    daily_revenue - LAG(daily_revenue, 1) OVER (ORDER BY report_date) AS dod_change
FROM factory_daily_output;
```

---

### Explainer B.6: Common Table Expressions (CTEs), Recursive Queries & Join Fanout Traps

#### 1. Preventing Join Fanout Revenue Multiplication
When a parent table (`clients`) has a 1-to-many relationship with `orders` (e.g., 3 orders) and another 1-to-many relationship with `complaints` (e.g., 4 complaints), joining both directly produces a **Cartesian fanout of $3 \times 4 = 12$ rows**. Summing revenue across this joined table multiplies client spending by a factor of 4!
* **The Fix**: Pre-aggregate each 1-to-many child table in an isolated CTE before executing the final `LEFT JOIN`:

```sql
WITH client_orders AS (
    SELECT client_id, SUM(order_total) AS total_spent
    FROM sales_orders
    WHERE order_status = 'COMPLETED'
    GROUP BY client_id
),
client_complaints AS (
    SELECT client_id, COUNT(ticket_id) AS total_tickets
    FROM support_tickets
    GROUP BY client_id
)
SELECT 
    c.client_id,
    c.client_name,
    COALESCE(o.total_spent, 0) AS total_spent,
    COALESCE(t.total_tickets, 0) AS total_tickets
FROM enterprise_clients c
LEFT JOIN client_orders o ON c.client_id = o.client_id
LEFT JOIN client_complaints t ON c.client_id = t.client_id;
```

#### 2. Recursive CTEs (Organizational Hierarchies)
A Recursive CTE consists of an **Anchor Member** (initial base query) followed by `UNION ALL` and a **Recursive Member** referencing the CTE itself:

```sql
WITH RECURSIVE org_chart AS (
    -- Anchor Member: Root CEO (reports_to IS NULL)
    SELECT employee_id, name, reports_to, 1 AS depth_level
    FROM employees
    WHERE reports_to IS NULL
    
    UNION ALL
    
    -- Recursive Member: Subordinates reporting to previous level
    SELECT e.employee_id, e.name, e.reports_to, o.depth_level + 1
    FROM employees e
    INNER JOIN org_chart o ON e.reports_to = o.employee_id
)
SELECT * FROM org_chart ORDER BY depth_level, employee_id;
```

---

### Explainer B.7: Three-Valued Logic (3VL), NULL Semantics & Safe Arithmetic

In SQL, `NULL` represents the total absence of a value or an unknown condition.

#### 1. Truth Tables under Three-Valued Logic
* `TRUE AND UNKNOWN` $\rightarrow$ `UNKNOWN`
* `FALSE AND UNKNOWN` $\rightarrow$ `FALSE`
* `TRUE OR UNKNOWN` $\rightarrow$ `TRUE`
* `FALSE OR UNKNOWN` $\rightarrow$ `UNKNOWN`
* `NOT UNKNOWN` $\rightarrow$ `UNKNOWN`

#### 2. The Equality Trap
Never write `WHERE status = NULL`. In SQL, `NULL = NULL` evaluates to `UNKNOWN`. In a `WHERE` filter, rows are returned **only if the predicate evaluates strictly to `TRUE`**; `UNKNOWN` is rejected. Always use `IS NULL` or `IS NOT NULL`.

#### 3. The Catastrophic `NOT IN (Subquery)` Trap
If a subquery returns even a single `NULL`, `WHERE id NOT IN (SELECT supervisor_id FROM ...)` evaluates to:
`id != 1 AND id != 2 AND id != NULL`
Since `id != NULL` evaluates to `UNKNOWN`, the entire `AND` chain becomes `UNKNOWN`. The query returns **0 rows**, silently dropping all valid data!
* *Fix*: Use `NOT EXISTS`:
  ```sql
  WHERE NOT EXISTS (
      SELECT 1 FROM employees s WHERE s.supervisor_id = e.employee_id
  )
  ```

#### 4. Safe Divide-by-Zero Protection
Division by zero crashes database batch jobs. Protect every ratio:
$$\text{Safe Ratio} = \frac{\text{Numerator}}{\text{NULLIF}(\text{Denominator}, 0)}$$
If `Denominator == 0`, `NULLIF` converts it to `NULL`. Since any number divided by `NULL` yields `NULL`, the calculation safely returns `NULL` without aborting the transaction.

---

# SECTION B & C: Relational SQL Analytics Curriculum & 20 Production Queries

Relational SQL Analytics Curriculum

### 2.1 Foundational SQL Teaching & Principles

1. **Clause Execution Order**:
   Unlike procedural languages, SQL executes in a strict conceptual order:
   $$\text{FROM} \longrightarrow \text{ON} \longrightarrow \text{JOIN} \longrightarrow \text{WHERE} \longrightarrow \text{GROUP BY} \longrightarrow \text{HAVING} \longrightarrow \text{SELECT} \longrightarrow \text{DISTINCT} \longrightarrow \text{ORDER BY} \longrightarrow \text{LIMIT / OFFSET}$$
   *Notice*: Column aliases defined in `SELECT` cannot be referenced in `WHERE` or `GROUP BY` because those clauses execute *before* `SELECT`.
2. **Three-Valued Logic & NULL Comparisons**:
   * In SQL, comparisons with `NULL` yield `UNKNOWN`, not `FALSE`.
   * Never write `WHERE col = NULL`. Always use `WHERE col IS NULL` or `WHERE col IS NOT NULL`.
   * Use `COALESCE(val1, val2, ...)` to supply fallback values.
3. **Safe Division**:
   * Dividing by zero causes immediate query execution failure. Always protect denominators with `NULLIF(denominator, 0)`.
4. **Join Cardinality & Fanout Multiplication**:
   * When joining Table A (1 row) to Table B (3 rows) on a 1-to-many relationship, `SUM(A.amount)` will multiply the amount by 3!
   * *Remedy*: Pre-aggregate the "many" side in a CTE or subquery before joining to the "one" side.
5. **Window Functions vs Ordinary Aggregations**:
   * Ordinary `GROUP BY` collapses multiple rows into a single summary row.
   * Window functions (`OVER (...)`) calculate aggregates across a partition while preserving individual row identity.
   * Window Framing: `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` computes cumulative running totals; `ROWS BETWEEN 6 PRECEDING AND CURRENT ROW` computes 7-period rolling windows.
6. **Dialect Nuances**:
   * ANSI SQL standard uses `CURRENT_DATE`, `EXTRACT(YEAR FROM col)`.
   * PostgreSQL uses `DATE_TRUNC('month', col)`, `INTERVAL '7 days'`.
   * MySQL uses `DATE_SUB(NOW(), INTERVAL 7 DAY)`, `DATE_FORMAT()`.

---

### 2.2 The 30 Comprehensive SQL Problems & Solutions

---

#### Problem 01: Active Cloud License Filtering & Sorting
* **Focus**: `SELECT`, `WHERE`, `ORDER BY`
* **Dialect**: ANSI SQL
* **Schema**: `licenses(license_id INT, client_name VARCHAR, seat_count INT, status VARCHAR, renewal_date DATE)`
* **Task**: List all licenses with `status = 'ACTIVE'` and `seat_count >= 50`, ordered by `seat_count` descending, then `renewal_date` ascending.

```sql
SELECT 
    license_id,
    client_name,
    seat_count,
    renewal_date
FROM licenses
WHERE status = 'ACTIVE' 
  AND seat_count >= 50
ORDER BY seat_count DESC, renewal_date ASC;
```

---

#### Problem 02: Safe NULL Handling for Client Contacts
* **Focus**: `IS NULL`, `COALESCE`
* **Dialect**: ANSI SQL
* **Schema**: `clients(client_id INT, company_name VARCHAR, primary_email VARCHAR, secondary_email VARCHAR, phone_number VARCHAR)`
* **Task**: Return `company_name`, effective contact email (`primary_email` if present, else `secondary_email`, else `'no_email@company.com'`), and flag whether phone is missing.

```sql
SELECT 
    company_name,
    COALESCE(primary_email, secondary_email, 'no_email@company.com') AS contact_email,
    CASE WHEN phone_number IS NULL THEN 'MISSING' ELSE 'VERIFIED' END AS phone_status
FROM clients;
```

---

#### Problem 03: Safe Conversion Rate with Zero-Division Protection
* **Focus**: Safe Division, `NULLIF`
* **Dialect**: ANSI SQL
* **Schema**: `campaign_metrics(campaign_id INT, impressions INT, conversions INT)`
* **Task**: Calculate conversion percentage rounded to 2 decimal places. Ensure campaigns with 0 impressions return `0.00%` rather than throwing division-by-zero error.

```sql
SELECT 
    campaign_id,
    impressions,
    conversions,
    ROUND(COALESCE(conversions * 100.0 / NULLIF(impressions, 0), 0.0), 2) AS conversion_rate_pct
FROM campaign_metrics;
```

---

#### Problem 04: Project Billing Reconciliation (Inner vs Left Join)
* **Focus**: `LEFT JOIN`, Unmatched Records
* **Dialect**: ANSI SQL
* **Schema**: `clients(client_id INT, client_name VARCHAR)`, `projects(project_id INT, client_id INT, total_budget NUMERIC)`
* **Task**: Output all clients and their total project budget. Include clients who currently have zero assigned projects (show budget as `0.00`).

```sql
SELECT 
    c.client_id,
    c.client_name,
    COALESCE(SUM(p.total_budget), 0.00) AS total_assigned_budget
FROM clients c
LEFT JOIN projects p ON c.client_id = p.client_id
GROUP BY c.client_id, c.client_name
ORDER BY total_assigned_budget DESC;
```

---

#### Problem 05: Preventing Join Fanout Revenue Inflation
* **Focus**: Multi-table Join Fanout, Subquery Pre-aggregation
* **Dialect**: ANSI SQL
* **Schema**: `orders(order_id INT, client_id INT, order_amount NUMERIC)`, `payments(payment_id INT, order_id INT, payment_amount NUMERIC)`
* **Task**: Calculate each client's total order amount and total payments made. Ensure multiple payments per order do not artificially multiply the order amount.

```sql
WITH payment_summary AS (
    SELECT order_id, SUM(payment_amount) AS total_paid
    FROM payments
    GROUP BY order_id
)
SELECT 
    o.client_id,
    SUM(o.order_amount) AS total_ordered,
    COALESCE(SUM(ps.total_paid), 0.00) AS total_paid
FROM orders o
LEFT JOIN payment_summary ps ON o.order_id = ps.order_id
GROUP BY o.client_id;
```

---

#### Problem 06: Server Latency Aggregation with Sample Threshold
* **Focus**: `GROUP BY`, `HAVING`, `AVG`
* **Dialect**: ANSI SQL
* **Schema**: `telemetry_logs(server_id VARCHAR, region VARCHAR, latency_ms NUMERIC, logged_at TIMESTAMP)`
* **Task**: Find regions with average latency > 120 ms, restricted only to regions that have logged at least 100 telemetry records.

```sql
SELECT 
    region,
    COUNT(*) AS total_samples,
    ROUND(AVG(latency_ms), 2) AS avg_latency_ms
FROM telemetry_logs
GROUP BY region
HAVING COUNT(*) >= 100 
   AND AVG(latency_ms) > 120.0
ORDER BY avg_latency_ms DESC;
```

---

#### Problem 07: Client Digital Tool Adoption Rate
* **Focus**: Conditional Aggregation, `HAVING`
* **Dialect**: ANSI SQL
* **Schema**: `departments(dept_id INT, dept_name VARCHAR)`, `employees(emp_id INT, dept_id INT, has_digital_license INT)`
* **Task**: Identify departments with >= 30 employees where the digital tool adoption rate exceeds 75.0%.

```sql
SELECT 
    d.dept_name,
    COUNT(e.emp_id) AS total_employees,
    ROUND(SUM(e.has_digital_license) * 100.0 / COUNT(e.emp_id), 2) AS adoption_pct
FROM departments d
JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_id, d.dept_name
HAVING COUNT(e.emp_id) >= 30 
   AND (SUM(e.has_digital_license) * 100.0 / COUNT(e.emp_id)) > 75.0
ORDER BY adoption_pct DESC;
```

---

#### Problem 08: Monthly Revenue Pivot by Service Line
* **Focus**: Pivot via `CASE WHEN`
* **Dialect**: ANSI SQL
* **Schema**: `monthly_revenue(month_name VARCHAR, service_line VARCHAR, revenue NUMERIC)`
* **Task**: Pivot the table to display `month_name` with separate columns for `'Cloud'`, `'AI'`, and `'Cybersecurity'` revenues.

```sql
SELECT 
    month_name,
    SUM(CASE WHEN service_line = 'Cloud' THEN revenue ELSE 0 END) AS cloud_revenue,
    SUM(CASE WHEN service_line = 'AI' THEN revenue ELSE 0 END) AS ai_revenue,
    SUM(CASE WHEN service_line = 'Cybersecurity' THEN revenue ELSE 0 END) AS cybersecurity_revenue
FROM monthly_revenue
GROUP BY month_name
ORDER BY month_name;
```

---

#### Problem 09: Customer User Activity Segmentation
* **Focus**: Tier Categorization, Subquery Counting
* **Dialect**: ANSI SQL
* **Schema**: `user_activity(user_id INT, login_count_30d INT)`
* **Task**: Categorize users into `'Power User'` (>= 50 logins), `'Regular User'` (10-49 logins), and `'Dormant User'` (< 10 logins). Count total users and percentage in each tier.

```sql
WITH categorized AS (
    SELECT 
        user_id,
        CASE 
            WHEN login_count_30d >= 50 THEN 'Power User'
            WHEN login_count_30d >= 10 THEN 'Regular User'
            ELSE 'Dormant User'
        END AS user_tier
    FROM user_activity
)
SELECT 
    user_tier,
    COUNT(*) AS user_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM user_activity), 2) AS pct_of_total
FROM categorized
GROUP BY user_tier
ORDER BY user_count DESC;
```

---

#### Problem 10: Employees Earning Above Department Average
* **Focus**: CTE + Join on Aggregated Subquery
* **Dialect**: ANSI SQL
* **Schema**: `employees(emp_id INT, emp_name VARCHAR, dept_id INT, salary NUMERIC)`
* **Task**: Return all employees whose salary exceeds their department's average salary. Include employee salary and department average.

```sql
WITH dept_avg AS (
    SELECT dept_id, AVG(salary) AS avg_sal
    FROM employees
    GROUP BY dept_id
)
SELECT 
    e.emp_id,
    e.emp_name,
    e.dept_id,
    e.salary,
    ROUND(da.avg_sal, 2) AS department_avg_salary
FROM employees e
JOIN dept_avg da ON e.dept_id = da.dept_id
WHERE e.salary > da.avg_sal
ORDER BY e.dept_id, e.salary DESC;
```

---

#### Problem 11: Rapid Second Purchase Interval
* **Focus**: CTE, Self-Join / Window Matching
* **Dialect**: ANSI SQL / PostgreSQL
* **Schema**: `orders(order_id INT, customer_id INT, order_date DATE, amount NUMERIC)`
* **Task**: Identify customers whose second order occurred within 7 days of their first order.

```sql
WITH ranked_orders AS (
    SELECT 
        customer_id,
        order_date,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date ASC) AS order_seq
    FROM orders
)
SELECT 
    r1.customer_id,
    r1.order_date AS first_order,
    r2.order_date AS second_order,
    (r2.order_date - r1.order_date) AS days_between
FROM ranked_orders r1
JOIN ranked_orders r2 ON r1.customer_id = r2.customer_id
WHERE r1.order_seq = 1 
  AND r2.order_seq = 2
  AND (r2.order_date - r1.order_date) <= 7;
```

---

#### Problem 12: Distinct Event Counting Rigor
* **Focus**: `COUNT(*)`, `COUNT(col)`, `COUNT(DISTINCT)`
* **Dialect**: ANSI SQL
* **Schema**: `api_logs(request_id INT, session_id VARCHAR, response_payload VARCHAR)`
* **Task**: Return total requests logged, total requests with a non-null payload, and total unique sessions.

```sql
SELECT 
    COUNT(*) AS total_raw_requests,
    COUNT(response_payload) AS requests_with_payload,
    COUNT(DISTINCT session_id) AS unique_active_sessions
FROM api_logs;
```

---

#### Problem 13: Top-3 Japanese Enterprise Contracts per Prefecture (Ties Handling)
* **Focus**: `DENSE_RANK()`, Window Function Filtering
* **Dialect**: ANSI SQL
* **Schema**: `contracts(contract_id INT, prefecture VARCHAR, client_name VARCHAR, contract_value NUMERIC)`
* **Task**: Return top-3 contracts per prefecture by value. In case of ties, assign identical ranks without skipping subsequent ranks (`DENSE_RANK`).

```sql
WITH ranked_contracts AS (
    SELECT 
        prefecture,
        client_name,
        contract_value,
        DENSE_RANK() OVER (PARTITION BY prefecture ORDER BY contract_value DESC) AS val_rank
    FROM contracts
)
SELECT 
    prefecture,
    val_rank,
    client_name,
    contract_value
FROM ranked_contracts
WHERE val_rank <= 3
ORDER BY prefecture, val_rank;
```

---

#### Problem 14: Latest Status Snapshot per IoT Edge Device
* **Focus**: `ROW_NUMBER() OVER (PARTITION BY ...)`
* **Dialect**: ANSI SQL
* **Schema**: `device_heartbeats(device_id VARCHAR, recorded_at TIMESTAMP, battery_pct NUMERIC, firmware_version VARCHAR)`
* **Task**: Output the single most recent heartbeat record for each IoT device.

```sql
WITH latest_heartbeat AS (
    SELECT 
        device_id,
        recorded_at,
        battery_pct,
        firmware_version,
        ROW_NUMBER() OVER (PARTITION BY device_id ORDER BY recorded_at DESC) AS rn
    FROM device_heartbeats
)
SELECT 
    device_id,
    recorded_at,
    battery_pct,
    firmware_version
FROM latest_heartbeat
WHERE rn = 1;
```

---

#### Problem 15: Day-over-Day Server Error Growth
* **Focus**: `LAG()`, Window Offset
* **Dialect**: ANSI SQL
* **Schema**: `daily_errors(log_date DATE, error_count INT)`
* **Task**: For each day, display `log_date`, `error_count`, yesterday's error count, and the percentage change.

```sql
WITH daily_trend AS (
    SELECT 
        log_date,
        error_count,
        LAG(error_count, 1) OVER (ORDER BY log_date ASC) AS prev_day_errors
    FROM daily_errors
)
SELECT 
    log_date,
    error_count,
    prev_day_errors,
    ROUND((error_count - prev_day_errors) * 100.0 / NULLIF(prev_day_errors, 0), 2) AS dod_growth_pct
FROM daily_trend
ORDER BY log_date ASC;
```

---

#### Problem 16: Idle Gap Between Consecutive User Interactions
* **Focus**: `LEAD()`, Timestamp Difference
* **Dialect**: ANSI SQL / PostgreSQL
* **Schema**: `user_clicks(user_id INT, click_time TIMESTAMP)`
* **Task**: For each user, calculate the idle gap in minutes until their next click.

```sql
WITH click_sequence AS (
    SELECT 
        user_id,
        click_time,
        LEAD(click_time, 1) OVER (PARTITION BY user_id ORDER BY click_time ASC) AS next_click_time
    FROM user_clicks
)
SELECT 
    user_id,
    click_time,
    next_click_time,
    ROUND(EXTRACT(EPOCH FROM (next_click_time - click_time)) / 60.0, 2) AS idle_minutes
FROM click_sequence
WHERE next_click_time IS NOT NULL;
```

---

#### Problem 17: Customer Spend Quartiles vs Deciles
* **Focus**: `NTILE(4)` (Quartiles) vs `NTILE(10)` (Deciles)
* **Dialect**: ANSI SQL
* **Pedagogical Note**:
  * **Quartiles (`NTILE(4)`)**: Partitions rows into **4 equal groups** (Top 25%, 25-50%, 50-75%, Bottom 25%).
  * **Deciles (`NTILE(10)`)**: Partitions rows into **10 equal groups** (each representing 10% increments).
* **Schema**: `customer_annual_spend(customer_id INT, total_spend NUMERIC)`
* **Task**: Divide all customers into 4 spending quartiles using `NTILE(4)`. Output `customer_id`, `total_spend`, and assigned `spend_quartile` (1 = lowest, 4 = highest).

```sql
SELECT 
    customer_id,
    total_spend,
    NTILE(4) OVER (ORDER BY total_spend ASC) AS spend_quartile
FROM customer_annual_spend
ORDER BY spend_quartile DESC, total_spend DESC;
```

---

#### Problem 18: Running Cumulative Project Expenditure
* **Focus**: `SUM(...) OVER (...)`, Unbounded Preceding Window Frame
* **Dialect**: ANSI SQL
* **Schema**: `project_expenses(project_id INT, expense_date DATE, amount NUMERIC)`
* **Task**: Calculate the cumulative expenditure over time for each project.

```sql
SELECT 
    project_id,
    expense_date,
    amount,
    SUM(amount) OVER (
        PARTITION BY project_id 
        ORDER BY expense_date ASC 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_spent
FROM project_expenses
ORDER BY project_id, expense_date ASC;
```

---

#### Problem 19: 7-Day Rolling Average API Latency
* **Focus**: Moving Window Frame, `ROWS BETWEEN 6 PRECEDING AND CURRENT ROW`
* **Dialect**: ANSI SQL
* **Schema**: `service_daily_latency(service_name VARCHAR, metric_date DATE, avg_latency_ms NUMERIC)`
* **Task**: Calculate the 7-day moving average latency for each service.

```sql
SELECT 
    service_name,
    metric_date,
    avg_latency_ms,
    ROUND(AVG(avg_latency_ms) OVER (
        PARTITION BY service_name 
        ORDER BY metric_date ASC 
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ), 2) AS rolling_7d_avg_latency
FROM service_daily_latency
ORDER BY service_name, metric_date ASC;
```

---

#### Problem 20: Active Subscriptions During Q3 2026 (Date Overlaps)
* **Focus**: Temporal Interval Overlap
* **Dialect**: ANSI SQL
* **Schema**: `subscriptions(sub_id INT, client_id INT, start_date DATE, end_date DATE)`
* **Task**: Find all subscriptions that were active at any point during Q3 2026 (from `2026-07-01` to `2026-09-30`). Include ongoing subscriptions (`end_date IS NULL`).

```sql
SELECT 
    sub_id,
    client_id,
    start_date,
    end_date
FROM subscriptions
WHERE start_date <= '2026-09-30'
  AND (end_date IS NULL OR end_date >= '2026-07-01');
```

---

#### Problem 21: Date Truncation & Dialect Compatibility
* **Focus**: Monthly Grouping in PostgreSQL vs ANSI SQL
* **Dialect**: PostgreSQL / ANSI SQL
* **Schema**: `transactions(txn_id INT, txn_timestamp TIMESTAMP, amount NUMERIC)`
* **Task**: Calculate total transaction volume grouped by calendar month. Provide both PostgreSQL-specific and standard ANSI SQL formulations.

```sql
-- PostgreSQL Syntax:
SELECT 
    DATE_TRUNC('month', txn_timestamp) AS txn_month,
    COUNT(*) AS total_txns,
    SUM(amount) AS total_amount
FROM transactions
GROUP BY DATE_TRUNC('month', txn_timestamp)
ORDER BY txn_month ASC;

-- Standard ANSI SQL Syntax:
SELECT 
    EXTRACT(YEAR FROM txn_timestamp) AS txn_year,
    EXTRACT(MONTH FROM txn_timestamp) AS txn_month,
    COUNT(*) AS total_txns,
    SUM(amount) AS total_amount
FROM transactions
GROUP BY EXTRACT(YEAR FROM txn_timestamp), EXTRACT(MONTH FROM txn_timestamp)
ORDER BY txn_year, txn_month;
```

---

#### Problem 22: Project Expenditure Restricted Strictly to Completed Milestones
* **Focus**: Milestone Status Filtering, Premature Expenditure Prevention
* **Dialect**: ANSI SQL
* **Pedagogical Note**: When tracking project expenditure against allocated budget, costs must strictly reflect delivered work (`milestone_status = 'COMPLETED'`). Counting planned or in-progress milestones distorts financial audit reports.
* **Schema**: `projects(project_id INT, project_name VARCHAR, allocated_budget NUMERIC)`, `milestones(milestone_id INT, project_id INT, milestone_cost NUMERIC, status VARCHAR)`
* **Task**: For each project, compute the allocated budget, actual expenditure from completed milestones, and budget variance.

```sql
SELECT 
    p.project_id,
    p.project_name,
    p.allocated_budget,
    COALESCE(SUM(CASE WHEN m.status = 'COMPLETED' THEN m.milestone_cost ELSE 0 END), 0.00) AS completed_expenditure,
    p.allocated_budget - COALESCE(SUM(CASE WHEN m.status = 'COMPLETED' THEN m.milestone_cost ELSE 0 END), 0.00) AS budget_variance
FROM projects p
LEFT JOIN milestones m ON p.project_id = m.project_id
GROUP BY p.project_id, p.project_name, p.allocated_budget
ORDER BY budget_variance ASC;
```

---

#### Problem 23: Duplicate Telemetry Packet Detection
* **Focus**: `GROUP BY`, `COUNT(*) > 1`
* **Dialect**: ANSI SQL
* **Schema**: `sensor_stream(sensor_id VARCHAR, recorded_epoch BIGINT, telemetry_payload VARCHAR)`
* **Task**: Identify duplicate transmissions where the same `sensor_id` recorded multiple payloads at the identical `recorded_epoch`.

```sql
SELECT 
    sensor_id,
    recorded_epoch,
    COUNT(*) AS duplicate_count
FROM sensor_stream
GROUP BY sensor_id, recorded_epoch
HAVING COUNT(*) > 1
ORDER BY duplicate_count DESC;
```

---

#### Problem 24: Customer Record Deduplication Retaining Earliest Profile
* **Focus**: Deduplication CTE, `ROW_NUMBER()`
* **Dialect**: ANSI SQL
* **Schema**: `raw_customers(customer_id INT, email VARCHAR, created_at TIMESTAMP)`
* **Task**: Write a query that returns unique customers by `email`, retaining only the single earliest created `customer_id`.

```sql
WITH deduplicated AS (
    SELECT 
        customer_id,
        email,
        created_at,
        ROW_NUMBER() OVER (PARTITION BY email ORDER BY created_at ASC, customer_id ASC) AS rn
    FROM raw_customers
)
SELECT 
    customer_id,
    email,
    created_at
FROM deduplicated
WHERE rn = 1;
```

---

#### Problem 25: Monthly Cohort Retention Rate
* **Focus**: Cohort Analysis, Date Difference
* **Dialect**: ANSI SQL / PostgreSQL
* **Schema**: `user_actions(user_id INT, action_date DATE)`
* **Task**: Find each user's signup month (first action), and calculate Month-1 retention rate (% of users who performed an action in the month following signup).

```sql
WITH user_first_month AS (
    SELECT 
        user_id,
        DATE_TRUNC('month', MIN(action_date)) AS cohort_month
    FROM user_actions
    GROUP BY user_id
),
user_monthly_activity AS (
    SELECT DISTINCT
        user_id,
        DATE_TRUNC('month', action_date) AS activity_month
    FROM user_actions
)
SELECT 
    ufm.cohort_month,
    COUNT(DISTINCT ufm.user_id) AS cohort_size,
    COUNT(DISTINCT uma.user_id) AS retained_month_1,
    ROUND(COUNT(DISTINCT uma.user_id) * 100.0 / COUNT(DISTINCT ufm.user_id), 2) AS month_1_retention_pct
FROM user_first_month ufm
LEFT JOIN user_monthly_activity uma 
       ON ufm.user_id = uma.user_id 
      AND uma.activity_month = ufm.cohort_month + INTERVAL '1 month'
GROUP BY ufm.cohort_month
ORDER BY ufm.cohort_month ASC;
```

---

#### Problem 26: First vs Last Transaction Value
* **Focus**: `FIRST_VALUE()`, `LAST_VALUE()` with Framing
* **Dialect**: ANSI SQL
* **Schema**: `customer_orders(order_id INT, customer_id INT, order_date DATE, order_amount NUMERIC)`
* **Task**: For each customer, display their first order amount and their most recent order amount.

```sql
SELECT DISTINCT
    customer_id,
    FIRST_VALUE(order_amount) OVER (
        PARTITION BY customer_id 
        ORDER BY order_date ASC 
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS initial_order_val,
    LAST_VALUE(order_amount) OVER (
        PARTITION BY customer_id 
        ORDER BY order_date ASC 
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS latest_order_val
FROM customer_orders;
```

---

#### Problem 27: System Continuous Uptime (Gaps & Islands)
* **Focus**: Gaps & Islands, `ROW_NUMBER` Difference
* **Dialect**: ANSI SQL
* **Schema**: `system_daily_status(check_date DATE, is_operational INT)`
* **Task**: Group contiguous periods of operational uptime (`is_operational = 1`) into distinct islands and calculate island length.

```sql
WITH operational_days AS (
    SELECT 
        check_date,
        check_date - CAST(ROW_NUMBER() OVER (ORDER BY check_date ASC) AS INT) AS island_id
    FROM system_daily_status
    WHERE is_operational = 1
)
SELECT 
    MIN(check_date) AS island_start,
    MAX(check_date) AS island_end,
    COUNT(*) AS consecutive_uptime_days
FROM operational_days
GROUP BY island_id
ORDER BY island_start ASC;
```

---

#### Problem 28: Management Hierarchy Tenure Comparison
* **Focus**: Self-Join, Organizational Hierarchy
* **Dialect**: ANSI SQL
* **Schema**: `employees(emp_id INT, emp_name VARCHAR, manager_id INT, hire_date DATE)`
* **Task**: List all employees who have been with the firm longer than their direct manager.

```sql
SELECT 
    e.emp_id,
    e.emp_name AS employee_name,
    e.hire_date AS employee_hire_date,
    m.emp_name AS manager_name,
    m.hire_date AS manager_hire_date
FROM employees e
JOIN employees m ON e.manager_id = m.emp_id
WHERE e.hire_date < m.hire_date
ORDER BY e.hire_date ASC;
```

---

#### Problem 29: Cloud vs On-Premises Asset Reconciliation
* **Focus**: `EXCEPT` / Anti-Join
* **Dialect**: ANSI SQL
* **Schema**: `cloud_assets(asset_tag VARCHAR, region VARCHAR)`, `onprem_inventory(asset_tag VARCHAR, location VARCHAR)`
* **Task**: Find all asset tags registered in `cloud_assets` that have no corresponding record in `onprem_inventory`.

```sql
SELECT asset_tag FROM cloud_assets
EXCEPT
SELECT asset_tag FROM onprem_inventory;

-- Alternative Outer-Join formulation:
SELECT c.asset_tag
FROM cloud_assets c
LEFT JOIN onprem_inventory o ON c.asset_tag = o.asset_tag
WHERE o.asset_tag IS NULL;
```

---

#### Problem 30: High-Value Accounts with Zero Support Inquiries
* **Focus**: `NOT EXISTS` vs `LEFT JOIN ... WHERE IS NULL`
* **Dialect**: ANSI SQL
* **Schema**: `accounts(account_id INT, tier VARCHAR, annual_contract_val NUMERIC)`, `support_tickets(ticket_id INT, account_id INT, created_at DATE)`
* **Task**: Find all `'ENTERPRISE'` accounts with `annual_contract_val > 10000000` (JPY 10M) that have submitted zero support tickets in the last 180 days.

```sql
SELECT 
    a.account_id,
    a.annual_contract_val
FROM accounts a
WHERE a.tier = 'ENTERPRISE'
  AND a.annual_contract_val > 10000000
  AND NOT EXISTS (
      SELECT 1 
      FROM support_tickets s
      WHERE s.account_id = a.account_id
        AND s.created_at >= CURRENT_DATE - INTERVAL '180 days'
  );
```

---

---

# SECTION D: Enterprise SQL Question Bank

Relational SQL & Database Queries

### Q2.1: `WHERE` vs `HAVING` Clause Difference (`[EXTERNAL VERIFIED]`)
* **Definition**: `WHERE` filters individual table rows *prior* to grouping. `HAVING` filters aggregated group records *after* the `GROUP BY` clause has been executed.
* **Mechanics**:
  ```sql
  -- Correct: WHERE filters active status; HAVING filters high-count departments
  SELECT dept_id, COUNT(*) AS emp_count
  FROM employees
  WHERE status = 'ACTIVE'
  GROUP BY dept_id
  HAVING COUNT(*) >= 10;
  ```
* **Follow-up**: *"Can `HAVING` be used without a `GROUP BY` clause?"*  
  *Answer*: *"Yes. In ANSI SQL, `HAVING` without `GROUP BY` treats the entire table as a single aggregated group."*

---

### Q2.2: Second-Highest Salary Extraction (`[PREPARATION INFERENCE]`)
* **Question**: Write an ANSI SQL query to extract the second-highest employee salary, returning `NULL` if no second-highest salary exists.
* **Query Solution**:
  ```sql
  WITH ranked AS (
      SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
      FROM employees
  )
  SELECT salary AS second_highest_salary
  FROM ranked
  WHERE rnk = 2
  LIMIT 1;
  ```
* **Why `DENSE_RANK`?**: If two executives share the highest salary ($100,000, $100,000), `RANK()` would assign ranks 1, 1, 3 (skipping rank 2). `DENSE_RANK()` assigns 1, 1, 2, correctly identifying the next highest salary.

---

### Q2.3: Join Fanout & Row Multiplication (`[EXTERNAL VERIFIED]`)
* **Question**: Why does joining an `orders` table to a `payments` table sometimes inflate total revenue in financial reporting?
* **Explanation**: If an order has 3 installment payments, a standard `INNER JOIN` produces 3 rows for that single order. Running `SUM(o.order_amount)` sums the order amount 3 times.
* **Remedy**: Always pre-aggregate the child table in a Common Table Expression (CTE) to a 1-to-1 relationship before joining.
