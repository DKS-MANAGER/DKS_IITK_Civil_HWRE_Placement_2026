# Module 05: Data Engineering, Cloud Ecosystems, and Governance

> **Module Code**: DEL-M05  
> **Priority**: P2 (Core Role Alignment)  
> **Target Assessment**: Technology Architecture Interviews & Data Engineering Screening  
> **Standard**: Complete architectural explanations, ETL vs. ELT trade-offs, Lakehouse design, distributed computing intuition, multi-cloud service mapping, and data governance frameworks.

---

## 1. Modern Data Architectures & Pipeline Engineering

### 1.1 Evolution of Analytical Data Platforms

```text
Generation 1: Traditional Data Warehouse (1990s - 2010s)
  Operational DBs ──► ETL Server (Informatica) ──► Relational Warehouse (Teradata, Oracle)
  • Pros: High query performance on clean structured data; ACID compliance.
  • Cons: Expensive proprietary hardware; rigid schemas; cannot store images/JSON/audio.

Generation 2: Data Lake (2010s - 2020)
  Raw Sources ──► Cheap Object Storage (AWS S3, ADLS, Hadoop HDFS) ──► Query Engines (Spark, Hive)
  • Pros: Inexpensive storage; handles unstructured data; decoupled compute from storage.
  • Cons: "Data Swamps"; no ACID transactions; slow updates/deletes; data consistency issues.

Generation 3: Modern Data Lakehouse (Current Enterprise Standard)
  Raw Sources ──► Cloud Object Storage (S3 / ADLS / GCS)
                        │
                        ▼ Open Table Formats (Delta Lake, Apache Iceberg, Hudi)
                        ├── ACID Transactions & Time Travel (Git for Data)
                        ├── Schema Enforcement & Evolution
                        └── Parquet-based columnar storage with metadata caching
                        │
                        ▼ Pluggable Compute Engines (Snowflake, Databricks Spark, BigQuery)
```

---

### 1.2 ETL versus ELT Paradigms

| Feature / Dimension | Traditional ETL (Extract, Transform, Load) | Modern ELT (Extract, Load, Transform) |
| :--- | :--- | :--- |
| **Transformation Location** | Dedicated intermediate compute server (e.g., ETL engine). | Inside the destination analytical cloud warehouse. |
| **Data Ingestion Speed** | Slower; pipeline breaks immediately if schema drifts. | Extremely fast; raw data lands directly in object storage. |
| **Compute Scaling** | Bound to hardware size of the ETL server. | Elastic cloud compute (auto-scales with data volume). |
| **Raw Data Retention** | Often discards raw unneeded attributes during transform. | Preserves full raw fidelity in Bronze layer forever. |
| **Primary Tooling** | Informatica, Talend, SSIS. | Fivetran, Airbyte, dbt (data build tool), Snowflake. |

---

### 1.3 Batch versus Streaming Pipelines

* **Batch Processing**: Processes data in discrete chunks at scheduled intervals (hourly, nightly). Optimal for historical reporting, reconciliation, and large-scale aggregations.
* **Streaming Processing**: Ingests and transforms records continuously as events occur (millisecond to second latency). Essential for fraud detection, IoT telemetry, and real-time inventory tracking.
* **Lambda vs. Kappa Architecture**:
  * **Lambda**: Dual-path architecture maintaining a speed layer (stream processing) and a batch layer (master accurate storage). Higher operational complexity.
  * **Kappa**: Single stream-native architecture where all data is treated as an append-only event stream through message brokers (Kafka, Kinesis).

---

## 2. Distributed Computing Principles (Spark & Partitioning)

### 2.1 The Distributed Bottleneck: Shuffling & Data Skew

* **Partition Pruning**: The query planner inspects metadata to read only relevant physical file blocks matching the `WHERE` clause (e.g., `WHERE date = '2024-03-01'`), skipping gigabytes of unneeded files.
* **Shuffling**: The process of redistributing data across physical cluster worker nodes across the network when executing `JOIN`, `GROUP BY`, or `DISTINCT`. Network I/O is the primary performance bottleneck in Big Data.
* **Data Skew**: Occurs when a partition key (e.g., `country_code = 'US'`) holds 90% of all records while other countries hold 10%. A single worker node struggles with the giant partition while other nodes sit idle. Mitigated via **salting** (appending random keys before joining).

---

## 3. Multi-Cloud Service Mapping (AWS vs. Azure vs. GCP)

Deloitte delivers technology solutions across all major hyperscalers. An Analyst must understand cross-cloud architectural equivalence:

| Enterprise Capability | Amazon Web Services (AWS) | Microsoft Azure | Google Cloud Platform (GCP) | Open Source / Neutral |
| :--- | :--- | :--- | :--- | :--- |
| **Object Storage** | Amazon S3 | Azure Data Lake Storage (ADLS Gen2) | Google Cloud Storage (GCS) | MinIO / Ceph |
| **Cloud Data Warehouse** | Amazon Redshift | Azure Synapse Analytics / Fabric | Google BigQuery | Snowflake / ClickHouse |
| **Distributed Big Data**| AWS EMR | Azure HDInsight / Databricks | GCP Dataproc | Apache Spark |
| **Pipeline Orchestration**| AWS Managed Workflows (MWAA)| Azure Data Factory (ADF) | Cloud Composer (Airflow) | Apache Airflow / Dagster |
| **Serverless Compute** | AWS Lambda | Azure Functions | Cloud Functions | OpenFaaS |
| **Streaming Broker** | Amazon Kinesis | Azure Event Hubs | Google Cloud Pub/Sub | Apache Kafka |
| **Identity & Access** | AWS IAM | Microsoft Entra ID (Azure AD) | Cloud IAM | Keycloak / Okta |

---

## 4. Data Governance, Quality, and Security

### 4.1 The Medallion Architecture (Bronze $\to$ Silver $\to$ Gold)

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                       MEDALLION DATA ARCHITECTURE                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  [Raw Sources] ──► BRONZE LAYER (Raw Landing)                               │
│                    • Append-only raw data; full historical fidelity.        │
│                    • JSON, CSV, API dumps with ingestion timestamps.        │
│                           │                                                 │
│                           ▼                                                 │
│                    SILVER LAYER (Cleansed & Enriched)                       │
│                    • Schema enforced; deduplicated; normalized data types.  │
│                    • Data quality checks passed; referential integrity.     │
│                           │                                                 │
│                           ▼                                                 │
│                    GOLD LAYER (Curated Business Marts)                      │
│                    • Dimensional star schemas; aggregated business KPIs.    │
│                    • Optimized for BI dashboards and client consumption.    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Data Governance & Regulatory Compliance
* **Data Lineage**: Tracing the end-to-end journey of a data point from its source transactional database, through transformations, to the executive dashboard. Crucial for regulatory audits (BCBS 239, SOX).
* **Access Control**:
  * **Role-Based Access Control (RBAC)**: Access granted based on job function (e.g., Financial Analyst).
  * **Attribute-Based Access Control (ABAC)**: Access evaluated dynamically based on user department, data classification tag, and geographical location.
* **Privacy & Masking (GDPR / HIPAA)**:
  * **PII (Personally Identifiable Information)**: Names, phone numbers, email addresses, national IDs.
  * Must be masked (pseudonymization, hashing with salt, or tokenization) before landing in non-production environments.

---

## 5. Self-Assessment Checklist

- [ ] Can articulate the architectural shift from Traditional Data Warehouses to Modern Lakehouses.
- [ ] Understand why ELT has overtaken ETL in modern cloud data pipelines.
- [ ] Able to explain distributed shuffle bottlenecks and data skew mitigation via salting.
- [ ] Can accurately map storage, compute, and orchestration services across AWS, Azure, and GCP.
- [ ] Mastered the Medallion Architecture (Bronze, Silver, Gold) and data lineage compliance requirements.
