# Project 3: ANSI SQL Enterprise Retail & CPG Analytics Suite

**Domain:** Enterprise Retail Relational Analytics  
**Stack:** ANSI SQL (PostgreSQL / Snowflake / Databricks SQL compliant)  
**Schema:** Multi-table relational schema (`stores`, `products`, `customers`, `promotions`, `transactions`, `transaction_items`)  
**Focus:** Window Functions, Recursive CTEs, Cohort Retention, Performance Tuning

---

## 1. Project Overview

This project provides an industry-grade ANSI SQL analytical suite modeling core retail business intelligence workflows.

### Analytical Workflows Solved:
1. **Customer RFM Segmentation:** Recency, Frequency, Monetary scoring via `NTILE()`.
2. **Growth Analytics:** Month-over-Month (MoM) sales velocity using `LAG()`.
3. **Operational Trend Smoothing:** Rolling 7-day sales moving average with explicit window frames.
4. **Competitive Product Ranking:** Top-3 revenue drivers per category via `DENSE_RANK()`.
5. **Customer Retention:** Longitudinal cohort retention matrix.
6. **Trade Promotion Lift:** Incremental promotional revenue vs non-promo baselines.
7. **Market Basket Affinity:** Bipartite co-purchase pair frequency.
8. **Churned Account Detection:** Inactive customer identification via date intervals.
9. **Hierarchical Categorical Rollup:** Recursive Common Table Expression (CTE) tree traversal.

---

## 2. File Structure

- `analytics_queries.sql`: Fully commented, production-grade ANSI SQL script with 10 complex analytical queries.
- `interview_defense.md`: Technical defense explaining query execution order, window frames, index optimization, and Snowflake partition pruning.
