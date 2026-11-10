# Module 10 — Databricks & PySpark Distributed Analytics

In large-scale private equity portfolio analytics at Accordion (Merilytics), companies generating multi-gigabyte or terabyte-scale transactional logs (e.g., e-commerce clickstreams, high-frequency logistics telemetry, multi-entity ERP ledgers) leverage **Databricks and Apache Spark** to build scalable lakehouse data pipelines.

---

## 1. The Lakehouse Paradigm & Medallion Architecture

A **Data Lakehouse** merges the best attributes of two historical architectures:
- **Data Lake (e.g., raw S3/ADLS)**: Highly scalable, low cost, supports unstructured/semi-structured data, but suffers from slow query speeds, lack of ACID transactions, and data swamp degradation.
- **Data Warehouse (e.g., Snowflake, Redshift)**: Fast, schema-enforced, transactional consistency, but expensive for raw multi-TB storage and inflexible for unstructured data.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              MEDALLION LAKEHOUSE ARCHITECTURE                          │
├────────────────────┬───────────────────────────────────┬───────────────────────────────┤
│       Layer        │              Purpose              │          Format / State       │
├────────────────────┼───────────────────────────────────┼───────────────────────────────┤
│ Bronze Layer       │ Raw Ingestion: Preserves original │ Append-only raw logs, JSON,   │
│ (Raw / Landing)    │ state; immutable historical log.  │ CSV, unchanged schema.        │
├────────────────────┼───────────────────────────────────┼───────────────────────────────┤
│ Silver Layer       │ Cleansed & Conformed: Deduplicated│ Delta Parquet, enforced schema│
│ (Curated / Staging)│ validated data; standard schemas. │ joins, missing values imputed.│
├────────────────────┼───────────────────────────────────┼───────────────────────────────┤
│ Gold Layer         │ Business Aggregate: Star schemas, │ Dimensional fact/dim tables,  │
│ (Business / Ready) │ aggregated KPIs, executive views. │ read-optimized for Power BI.  │
└────────────────────┴───────────────────────────────────┴───────────────────────────────┘
```

---

## 2. Apache Spark Engine Internals

Apache Spark is a distributed, in-memory compute engine designed for big data processing:

```
                          ┌───────────────────────────┐
                          │        DRIVER NODE        │
                          │ • SparkSession / Context  │
                          │ • Builds DAG Execution Plan│
                          │ • Distributes Task Batches │
                          └─────────────┬─────────────┘
                                        │ Cluster Manager
                 ┌──────────────────────┼──────────────────────┐
                 ▼                      ▼                      ▼
      ┌────────────────────┐ ┌────────────────────┐ ┌────────────────────┐
      │  EXECUTOR NODE 1   │ │  EXECUTOR NODE 2   │ │  EXECUTOR NODE 3   │
      │ • Worker Process   │ │ • Worker Process   │ │ • Worker Process   │
      │ • In-Memory Cache  │ │ • In-Memory Cache  │ │ • In-Memory Cache  │
      │ • Executes Tasks   │ │ • Executes Tasks   │ │ • Executes Tasks   │
      └────────────────────┘ └────────────────────┘ └────────────────────┘
```

### 2.1 Lazy Evaluation & The DAG Scheduler
Spark operates via **Lazy Evaluation**:
- **Transformations** (e.g., `filter()`, `select()`, `groupBy()`) are not executed immediately. Instead, Spark registers them into a **Directed Acyclic Graph (DAG)** of execution stages.
- Processing only starts when an **Action** (e.g., `show()`, `count()`, `collect()`, `write()`) is triggered.
- *Advantage*: Spark’s Catalyst Optimizer examines the entire DAG before running, reordering filters, pruning unused columns, and combining operations to minimize disk I/O.

### 2.2 Narrow vs. Wide Transformations (The Shuffling Bottleneck)
```
┌─────────────────────────────────┬─────────────────────────────────────────────────────────────┐
│      Narrow Transformation      │                     Wide Transformation                     │
├─────────────────────────────────┼─────────────────────────────────────────────────────────────┤
│ No data movement across nodes   │ Requires data exchange across cluster nodes (SHUFFLE)       │
│ Each input partition maps to 1  │ Multiple input partitions combine into new output partitions│
│ output partition. Very fast.    │ Network I/O intensive. Primary performance bottleneck.      │
│ Examples: filter(), select(),   │ Examples: groupBy(), distinct(), join() on non-partitioned  │
│           map(), drop()         │ keys, repartition()                                         │
└─────────────────────────────────┴─────────────────────────────────────────────────────────────┘
```

---

## 3. Delta Lake: ACID Transactions on Object Storage

**Delta Lake** is an open-source storage layer that brings reliability to data lakes by storing a JSON-based transaction log (`_delta_log/`) alongside Apache Parquet data files.

### 3.1 Delta Lake Capabilities
1. **ACID Transactions**: Guarantees that concurrent read/write jobs never corrupt data or return partial reads.
2. **Schema Enforcement**: Prevents accidental ingestion of bad records that do not match expected column types.
3. **Time Travel**: Querying or rolling back tables to prior historical timestamps:
   ```sql
   SELECT * FROM portco_sales TIMESTAMP AS OF '2025-10-15 12:00:00';
   RESTORE TABLE portco_sales TO VERSION AS OF 42;
   ```

---

## 4. End-to-End PySpark Lakehouse Pipeline Walkthrough

Below is a complete PySpark script demonstrating a Bronze-to-Silver-to-Gold data pipeline for private equity portfolio company sales data:

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, when, sum as _sum, countDistinct, round as _round

# 1. Initialize Spark Session with Delta Lake support
spark = SparkSession.builder \
    .appName("Accordion_Portco_Lakehouse_Pipeline") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# ==============================================================================
# STAGE 1: BRONZE TO SILVER (Ingestion, Cleansing & Deduplication)
# ==============================================================================

# Read raw JSON stream/files from Bronze landing zone
df_bronze = spark.read.format("json").load("/mnt/lakehouse/bronze/raw_pos_transactions/")

# Cleanse, cast dates, handle nulls, and deduplicate
df_silver = df_bronze \
    .filter(col("transaction_id").isNotNull()) \
    .withColumn("order_date", to_date(col("timestamp_str"), "yyyy-MM-dd HH:mm:ss")) \
    .withColumn("clean_amount", when(col("amount") < 0, 0.0).otherwise(col("amount"))) \
    .dropDuplicates(["transaction_id"])

# Write to Silver Delta Table with Schema Enforcement
df_silver.write.format("delta") \
    .mode("append") \
    .option("mergeSchema", "false") \
    .save("/mnt/lakehouse/silver/curated_transactions/")

# ==============================================================================
# STAGE 2: SILVER TO GOLD (Business Aggregation & PE KPIs)
# ==============================================================================

# Read curated Silver Delta table
df_curated = spark.read.format("delta").load("/mnt/lakehouse/silver/curated_transactions/")

# Compute Gold Aggregations: Monthly Region Performance
df_gold = df_curated.groupBy("store_region", "fiscal_year", "fiscal_month") \
    .agg(
        _round(_sum("clean_amount"), 2).alias("total_net_sales"),
        countDistinct("customer_id").alias("unique_customers"),
        countDistinct("transaction_id").alias("total_transactions")
    ) \
    .withColumn(
        "avg_basket_size", 
        _round(col("total_net_sales") / col("total_transactions"), 2)
    )

# Save to Gold Layer optimized for Power BI reporting
df_gold.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("gold_executive_regional_kpis")

print("Lakehouse pipeline executed successfully. Gold tables ready for CFO dashboard.")
```

