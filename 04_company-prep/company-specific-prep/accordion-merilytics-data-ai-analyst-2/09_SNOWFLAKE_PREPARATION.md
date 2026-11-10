# Module 09 — Snowflake Cloud Data Warehousing Preparation

In modern private equity analytics at Accordion (Merilytics), portfolio companies frequently migrate legacy on-premise ERP databases (SQL Server, Oracle) into **Snowflake** to establish a single source of truth for financial reporting, executive dashboards, and AI modeling.

---

## 1. Snowflake's Three-Tier Architecture

Snowflake separates **Storage**, **Compute**, and **Services**, solving the classic concurrency bottlenecks of legacy relational data warehouses:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                CLOUD SERVICES LAYER                                    │
│   • Authentication & RBAC       • Metadata Management       • Query Optimization       │
│   • Transaction Management      • Access Control            • Encryption & Security    │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                           QUERY PROCESSING (COMPUTE) LAYER                             │
│   ┌──────────────────────┐  ┌──────────────────────┐  ┌──────────────────────┐        │
│   │ Virtual Warehouse A  │  │ Virtual Warehouse B  │  │ Virtual Warehouse C  │        │
│   │   (Finance / FP&A)   │  │   (ETL / Ingestion)  │  │  (BI / Power BI Apps)│        │
│   │  Size: Medium (4 N)  │  │   Size: Large (8 N)  │  │  Size: Small (2 N)   │        │
│   └──────────────────────┘  └──────────────────────┘  └──────────────────────┘        │
│    * Compute clusters operate independently with zero resource contention or locking   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│                          DATABASE STORAGE LAYER (CLOUD BLOB)                           │
│   • Amazon S3 / Azure Blob Storage / Google Cloud Storage                              │
│   • Data organized into immutable, encrypted, columnar Micro-Partitions                │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### 1.1 Key Architectural Benefits for PE Portcos
1. **Zero Resource Contention**: The data engineering team running heavy nightly ingestion batch jobs on `Warehouse B` does NOT slow down the CFO's interactive Power BI dashboard queries running on `Warehouse C`.
2. **Auto-Suspend & Auto-Resume**: Virtual warehouses automatically shut down after 5 minutes of inactivity, reducing cloud compute costs for portcos with irregular reporting cycles.
3. **Instant Elasticity**: Sizing can be scaled up instantly from Small (2 nodes) to 2X-Large (32 nodes) with a single SQL command to process quarter-end financial reconciliations.

---

## 2. Micro-Partitioning & Automated Pruning

Unlike traditional databases that require manual B-Tree indexing, partition key definitions, and periodic `VACUUM` maintenance, Snowflake organizes all tables automatically into **Micro-Partitions**:
- Each micro-partition contains between **50 MB and 500 MB** of uncompressed data stored in columnar format.
- **Metadata-Driven Pruning**: The Cloud Services layer stores min/max values for every column within every micro-partition. When a query runs with `WHERE transaction_date BETWEEN '2025-01-01' AND '2025-01-31'`, Snowflake skips 98% of micro-partitions without reading disk.

---

## 3. Data Loading: Stages & The `COPY INTO` Command

Loading transactional data into Snowflake follows a two-step pattern: Staging $\rightarrow$ Ingestion.

```
┌───────────────────────┐         ┌───────────────────────┐         ┌───────────────────────┐
│ Raw Files (S3 / Blob) │────────►│    Snowflake STAGE    │────────►│  Snowflake Target     │
│ (CSV, Parquet, JSON)  │         │ (External or Internal)│         │     Fact Table        │
└───────────────────────┘         └───────────────────────┘         └───────────────────────┘
```

### 3.1 Production Ingestion Workflow Script
```sql
-- 1. Create Storage Integration & File Format
CREATE OR REPLACE FILE FORMAT csv_portco_format
    TYPE = 'CSV'
    FIELD_DELIMITER = ','
    SKIP_HEADER = 1
    NULL_IF = ('NULL', 'null', '')
    FIELD_OPTIONALLY_ENCLOSED_BY = '"'
    ERROR_ON_COLUMN_COUNT_MISMATCH = FALSE;

-- 2. Create Stage pointing to AWS S3 bucket
CREATE OR REPLACE STAGE s3_portco_stage
    URL = 's3://accordion-portco-raw-data/finance/'
    STORAGE_INTEGRATION = portco_s3_int
    FILE_FORMAT = csv_portco_format;

-- 3. Execute High-Speed Bulk Loading with Validation
COPY INTO raw_general_ledger_transactions
FROM @s3_portco_stage/2025/q3/
FILES = ('gl_extract_q3.csv')
ON_ERROR = 'SKIP_FILE_3%' -- Skips file if corrupt rows < 3%, else aborts
VALIDATION_MODE = RETURN_ERRORS; -- Dry-run syntax check without loading
```

---

## 4. Game-Changing Snowflake Features in PE Advisory

### 4.1 Time Travel & Accidental Drop Recovery
Snowflake maintains historical micro-partition states for up to **90 days** (Enterprise Edition), enabling point-in-time querying and instant table recovery:

```sql
-- Querying a table as it existed 2 hours ago (before an accidental update)
SELECT * 
FROM fact_revenue_reconciliation
AT(OFFSET => -60*120); -- 120 minutes ago

-- Querying table before a specific query ID ran
SELECT * 
FROM dim_customer_master
BEFORE(STATEMENT => '01b23456-789a-bcde-0001-23456789abcd');

-- Restoring an accidentally dropped table
UNDROP TABLE fact_revenue_reconciliation;
```

### 4.2 Zero-Copy Cloning
Zero-Copy Cloning creates a new table, schema, or entire database **instantaneously with zero storage cost** by copying metadata pointers to existing micro-partitions:

```sql
-- Create an instant staging sandbox for financial modeling without duplicating 2TB of storage
CREATE OR REPLACE DATABASE portco_finance_dev CLONE portco_finance_prod;
```
- Developers can update, insert, or delete data in `portco_finance_dev`. Only newly modified micro-partitions consume additional storage.

---

## 5. Snowpark: Python in Snowflake

**Snowpark** allows data analysts to write Python DataFrames that execute natively inside Snowflake's virtual warehouses:

```python
import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col, sum as _sum, round as _round

def compute_monthly_ebitda(session: snowpark.Session) -> snowpark.DataFrame:
    # Executes inside Snowflake virtual warehouse (no local data extraction)
    df = session.table("portco_finance_prod.analytics.fact_gl_entries")
    
    ebitda_summary = df.filter(col("fiscal_year") == 2025) \
                       .group_by("cost_center", "fiscal_quarter") \
                       .agg(
                           _round(_sum("credit_amount") - _sum("debit_amount"), 2).alias("net_ebitda")
                       ) \
                       .sort("cost_center", "fiscal_quarter")
                       
    return ebitda_summary
```

