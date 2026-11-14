# 03 — SQL Foundations, Processing Order & Query Optimization
## Relational Algebra, Logical Execution Hierarchy & Indexing Performance

> **Document Status**: Technical Core Curriculum `[TIER 5 / PEDAGOGICAL MODULE]`  
> **Target Role**: Data Scientist / Associate Data Scientist | Tredence Analytics

---

## 1. Logical SQL Query Execution Order

Writing optimal SQL queries requires understanding that the database engine executes clauses in a fundamentally different order than written:

```
WRITTEN SYNTAX:                     LOGICAL EXECUTION PIPELINE:
1. SELECT                           1. FROM & JOINs (Cartesian product, filter ON)
2. FROM & JOINs                     2. WHERE (Row-level filtering before grouping)
3. WHERE                            3. GROUP BY (Aggregate rows into buckets)
4. GROUP BY                         4. HAVING (Filter aggregated group rows)
5. HAVING                           5. WINDOW FUNCTIONS (Evaluate partitions/frames)
6. WINDOW FUNCTIONS                 6. SELECT (Projection, scalar expressions)
7. DISTINCT                         7. DISTINCT (Deduplicate projected rows)
8. ORDER BY                         8. ORDER BY (Sort final result set)
9. LIMIT / OFFSET                   9. LIMIT / OFFSET (Slice top-N rows)
```

### Critical Implications:
1. **Column Aliases in `WHERE` Clause**: You **cannot** reference a column alias created in `SELECT` within the `WHERE` clause because `WHERE` executes *before* `SELECT`.
2. **Filtering Aggregates**: Aggregate functions (e.g., `SUM(revenue) > 10000`) cannot appear in `WHERE`. They must be filtered in `HAVING` (or via an outer CTE).
3. **Window Functions in `WHERE`**: Window functions cannot appear in `WHERE` or `HAVING` because they execute *after* grouping. To filter on a window rank, wrap the query in a Common Table Expression (CTE) or subquery.

---

## 2. Join Semantics & Set Theory

```
┌───────────────┬─────────────────────────────────────────────────────────────┐
│ Join Type     │ Relational Mechanics                                        │
├───────────────┼─────────────────────────────────────────────────────────────┤
│ `INNER JOIN`  │ Returns only rows with matching keys in BOTH tables.        │
│ `LEFT JOIN`   │ Returns all rows from left table; unmatched right keys = NULL│
│ `RIGHT JOIN`  │ Returns all rows from right table; unmatched left keys = NULL│
│ `FULL JOIN`   │ Union of left and right joins; all unmatched keys = NULL    │
│ `CROSS JOIN`  │ Cartesian product of all rows: Size = |A| × |B|.            │
│ `SELF JOIN`   │ Table joined with itself (hierarchies, manager-employee).   │
│ `ANTI JOIN`   │ `LEFT JOIN ... WHERE right.key IS NULL` (find non-matches). │
│ `SEMI JOIN`   │ `WHERE EXISTS (SELECT 1 ...)` (checks existence, no dups).  │
└───────────────┴─────────────────────────────────────────────────────────────┘
```

---

## 3. Query Execution Plans & Optimization Fundamentals

When querying massive enterprise retail tables (e.g., billions of scanner POS sales rows in Snowflake / Databricks), poorly optimized queries can result in full table scans and high compute costs:

### 3.1 Sargable Queries (Search Argument Able)
A query is **sargable** if the database engine can utilize an existing index to satisfy the filter predicate:
- **Non-Sargable (Forces Full Table Scan)**:
  ```sql
  -- Bad: Function wrapped around indexed column prevents index seek!
  SELECT * FROM transactions WHERE YEAR(transaction_date) = 2024;
  SELECT * FROM customers WHERE SUBSTRING(phone_number, 1, 3) = '555';
  ```
- **Sargable (Enables Efficient Index Seek)**:
  ```sql
  -- Good: Column left bare, constants evaluated once
  SELECT * FROM transactions 
  WHERE transaction_date >= '2024-01-01' AND transaction_date < '2025-01-01';
  SELECT * FROM customers WHERE phone_number LIKE '555%';
  ```

### 3.2 Partition Pruning & Predicate Pushdown
- Modern analytical cloud engines (Snowflake, Databricks Delta Lake, Google BigQuery) organize data into micro-partitions or Parquet files.
- **Partition Pruning**: Always include partition keys (such as `event_date` or `region_id`) in your `WHERE` filter so the query engine skips 95%+ of irrelevant physical storage files.
