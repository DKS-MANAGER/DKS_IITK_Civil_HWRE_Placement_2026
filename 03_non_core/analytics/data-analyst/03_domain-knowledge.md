# 03. Data Analyst: Relational Architecture & Data Hygiene

> Database normalization, indexing, query optimization, exploratory data analysis, and dashboard architecture.

---

## 1. Database Normalization (3NF) & Schema Design
- **1NF**: Atomic values, no repeating groups.
- **2NF**: In 1NF + all non-key attributes fully dependent on the primary key.
- **3NF**: In 2NF + no transitive dependencies (no non-key attribute depends on another non-key attribute).

## 2. SQL Query Execution Order & Index Optimization
```text
FROM / JOIN  →  WHERE  →  GROUP BY  →  HAVING  →  SELECT  →  DISTINCT  →  ORDER BY  →  LIMIT
```
- **B-Tree Indexes**: Optimize range queries and exact lookups on high-cardinality columns (e.g., `user_id`, `created_at`).
- **Composite Indexes**: Leftmost prefix rule must match query filter order.
