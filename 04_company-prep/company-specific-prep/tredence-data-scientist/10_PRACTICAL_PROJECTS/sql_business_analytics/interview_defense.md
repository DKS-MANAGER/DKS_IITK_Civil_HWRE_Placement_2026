# Project 3: Interview Defense & Technical Q&A

**Candidate Defense Readiness:** ANSI SQL & Relational Analytics  
**Role:** Data Scientist / Associate Data Scientist | Tredence Analytics

---

### Q1. Why did you use `DENSE_RANK()` instead of `RANK()` or `ROW_NUMBER()` in Query 4?
**Defense:**  
- `ROW_NUMBER()` assigns strictly unique sequential integers, arbitrarily breaking ties when two products tie for third place in revenue, unfairly omitting one product.
- `RANK()` leaves gaps in rank numbering after ties (e.g., if two products tie for first place, the next rank is 3, skipping rank 2 entirely).
- `DENSE_RANK()` assigns consecutive integers without gaps (1, 1, 2, 3), ensuring that all top 3 performance tiers are fully captured regardless of tied revenue.

---

### Q2. What is the execution difference between `ROWS BETWEEN` and `RANGE BETWEEN` in window functions?
**Defense:**  
- `ROWS BETWEEN` operates on physical row offsets relative to the current row (e.g., `ROWS BETWEEN 6 PRECEDING AND CURRENT ROW` counts exactly 7 physical rows regardless of duplicate values).
- `RANGE BETWEEN` operates on logical value offsets based on the values in the `ORDER BY` column (e.g., calendar date ranges). If multiple rows share the identical timestamp, `RANGE` treats them as a single logical frame peer, which can cause unexpected duplicate aggregations.
- In production moving averages on daily pre-aggregated sales, `ROWS BETWEEN` ensures deterministic performance and avoids unintended sorting overhead.

---

### Q3. How would you optimize Query 1 (RFM Segmentation) for multi-million row datasets in Snowflake or Databricks?
**Defense:**  
1. **Cluster / Partition Pruning:** Cluster the `transactions` table by `(transaction_date, customer_id)`. Since RFM calculates recency relative to the current date, we can filter `WHERE transaction_date >= CURRENT_DATE - INTERVAL '365 days'`, pruning 80%+ of cold micro-partitions.
2. **Pushdown Aggregation:** Pre-aggregate transactions into daily or monthly customer summaries via materialized views or delta tables, avoiding a massive shuffle join between raw item transactions and customer dimension tables.
3. **Avoid Broad Window Shuffles:** `NTILE()` requires a full partition sort across the entire dataset. In massive distributed clusters, approximate percentiles (`APPROX_PERCENTILE()`) can be used to set threshold cuts without a single-node sorting bottleneck.
