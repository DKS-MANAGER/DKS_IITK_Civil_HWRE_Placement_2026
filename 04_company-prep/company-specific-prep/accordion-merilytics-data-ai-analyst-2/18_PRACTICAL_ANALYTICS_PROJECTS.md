# Module 18 — Practical Analytics Portfolio Projects

This module contains **7 comprehensive, end-to-end simulated client analytics projects** tailored for Accordion (Merilytics). Each project contains business objectives, synthetic data schemas, mathematical formulations, quality checks, findings, and executive recommendations.

---

## Portfolio Overview

```
┌────┬───────────────────────────────────────┬───────────────────────────────────┬───────────────────────────────────────┐
│ #  │             Project Title             │          Core Technology          │            Business Focus             │
├────┼───────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│ 01 │ Business Performance Analytics        │ Multi-Dimensional SQL & Python    │ Revenue, Gross Margin & EBITDA Walk   │
├────┼───────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│ 02 │ Dynamic Excel Management Model        │ PowerPivot, DAX, Star Schema      │ SaaS ARR, Churn & Net Retention (NRR) │
├────┼───────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│ 03 │ SQL Complex Business Analytics        │ ANSI SQL, CTEs, Window Functions  │ RFM Segmentation, DSO & Duplicates    │
├────┼───────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│ 04 │ Python Predictive Churn Pipeline      │ Pandas, Scikit-learn, XGBoost, SHAP│ Customer Churn & LTV Risk Scoring     │
├────┼───────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│ 05 │ Snowflake Cloud Data Warehouse        │ Snowflake SQL, Stages, Cloning    │ ERP Staging & Zero-Copy Sandboxes     │
├────┼───────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│ 06 │ Databricks PySpark Lakehouse          │ PySpark, Delta Lake, Medallion    │ Bronze -> Silver -> Gold Architecture │
├────┼───────────────────────────────────────┼───────────────────────────────────┼───────────────────────────────────────┤
│ 07 │ Client Decision-Support Turnaround    │ Consulting MECE & BI Dashboard    │ Private Equity Portco Turnaround Case │
└────┴───────────────────────────────────────┴───────────────────────────────────┴───────────────────────────────────────┘
```

---

## Project 01: Business Performance & EBITDA Decomposition

### 1. Business Context & Objective
A private equity sponsor acquires an industrial distributor generating \$120M in revenue. Post-acquisition, EBITDA compressed by 240 basis points despite 8% volume growth. The deal team requires a granular decomposition of revenue, price realization, and cost inflation to identify margin leakage.

### 2. Dataset Description (`[SYNTHETIC BENCHMARK]`)
- `Fact_Sales`: 250,000 transaction records containing `txn_id`, `date`, `customer_id`, `sku_id`, `units_sold`, `gross_invoice_amt`, `off_invoice_discount`, `standard_cogs`, `actual_shipping_cost`.
- `Dim_Product`: `sku_id`, `category`, `product_tier` (Core, Premium, Value).

### 3. Methodology & Variance Math
Apply a 5-factor mathematical variance decomposition:
$$\Delta \text{Gross Profit} = \Delta \text{Volume} + \Delta \text{Price} + \Delta \text{Mix} + \Delta \text{Discount} + \Delta \text{Freight}$$

### 4. Findings & Business Recommendation
- **Key Finding**: Sales representatives offered unauthorized off-invoice discounts averaging 7.8% on Core SKUs to achieve annual volume quotas, eroding \$3.2M in margin. Furthermore, expedited freight costs rose by 35% due to warehouse stockouts.
- **Strategic Recommendation**: Enforce automated CRM price-floor guards prohibiting discounts > 3% without VP approval. Establish regional safety stock buffers to eliminate expedited freight, recovering **\$2.6M in EBITDA (216 bps expansion)**.

---

## Project 02: Dynamic Excel Management Model (PowerPivot & DAX)

### 1. Business Context & Objective
The CFO of a PE-backed B2B SaaS portco needs a dynamic executive management reporting model to track Annual Recurring Revenue (ARR), logo churn, and cohort Net Revenue Retention (NRR).

### 2. Workbook Architecture
- `Assumptions_Tab`: Documented macro parameters (discount rate, tax, target NRR).
- `Data_Model_Tab`: Star schema with `Fact_Subscriptions` (1.2M rows), `Dim_Customer`, `Dim_Product`, and `Dim_Date`.
- `Executive_Dashboard`: Interactive PivotTables, slicers (Region, ARR Tier), and sparkline trends.

### 3. Core DAX Formulations
```dax
// Ending ARR for active accounts
Ending_ARR := 
CALCULATE(
    SUM(Fact_Subscriptions[Monthly_Rate]) * 12,
    Fact_Subscriptions[Start_Date] <= MAX(Dim_Date[Date]) &&
    (ISBLANK(Fact_Subscriptions[End_Date]) || Fact_Subscriptions[End_Date] > MAX(Dim_Date[Date]))
)

// Cohort Net Revenue Retention (NRR %)
Cohort_NRR_Pct := 
DIVIDE([Current_Cohort_ARR], [Baseline_Cohort_ARR], 1.0)
```

### 4. Executive Finding
Enterprise customers (ARR > \$100k) exhibited strong 118% NRR, whereas the SMB tier experienced severe 78% NRR due to onboarding friction. Recommends shifting 15 customer success reps from Enterprise to SMB onboarding.

---

## Project 03: SQL Complex Business Analytics Engine

### 1. Business Context & Objective
Build an automated SQL analytical view suite on a PostgreSQL/Snowflake data warehouse to monitor customer recency-frequency-monetary (RFM) segmentation and working capital Accounts Receivable aging.

### 2. SQL Implementation (Aging Buckets)
```sql
WITH OpenInvoices AS (
    SELECT 
        customer_id,
        invoice_id,
        invoice_date,
        open_balance,
        DATEDIFF('day', invoice_date, CURRENT_DATE()) AS aging_days
    FROM fact_invoices
    WHERE status = 'Unpaid' AND open_balance > 0
)
SELECT 
    customer_id,
    ROUND(SUM(open_balance), 2) AS total_ar_balance,
    ROUND(SUM(CASE WHEN aging_days <= 30 THEN open_balance ELSE 0 END), 2) AS current_0_30,
    ROUND(SUM(CASE WHEN aging_days BETWEEN 31 AND 60 THEN open_balance ELSE 0 END), 2) AS past_due_31_60,
    ROUND(SUM(CASE WHEN aging_days BETWEEN 61 AND 90 THEN open_balance ELSE 0 END), 2) AS past_due_61_90,
    ROUND(SUM(CASE WHEN aging_days > 90 THEN open_balance ELSE 0 END), 2) AS severely_past_due_90_plus
FROM OpenInvoices
GROUP BY customer_id
HAVING SUM(CASE WHEN aging_days > 60 THEN open_balance ELSE 0 END) > 50000
ORDER BY severely_past_due_90_plus DESC;
```

---

## Project 04: Python Predictive Churn Pipeline & SHAP Explainability

### 1. Business Context & Objective
Build an auditable predictive model to identify customers at risk of canceling subscriptions 60 days prior to contract renewal, enabling targeted retention incentives.

### 2. Technical Profile
- **Model**: Gradient Boosted Decision Trees (XGBoost Classifier).
- **Class Imbalance Resolution**: `scale_pos_weight = 7.5` (reflecting 12% baseline churn).
- **Explainability**: TreeExplainer with SHAP values.
- **Results**: Achieved **ROC-AUC of 0.884** and **PR-AUC of 0.742**.

### 3. SHAP Feature Attribution
```
Top Churn Drivers (SHAP Mean Impact):
1. Support Tickets Unresolved > 5 Days (+0.42 log-odds)
2. Monthly Portal Logins Drop > 40% YoY (+0.38 log-odds)
3. Month-to-Month Contract Type (+0.29 log-odds)
4. Payment Failure Retries (+0.18 log-odds)
```
- **Business Impact**: Intervening on the top decile of predicted churners recovers an estimated **\$1.8M in annualized recurring cash flow**.

---

## Project 05: Snowflake Cloud Data Warehouse & Ingestion Engine

### 1. Business Context & Objective
Design a scalable cloud data pipeline to ingest daily ERP transaction extracts from AWS S3 into Snowflake, implementing automated micro-partition pruning and zero-copy staging sandboxes for financial model testing.

### 2. Key Architecture & DDL
```sql
-- 1. Create Stage & File Format
CREATE OR REPLACE STAGE s3_portco_stage
    URL = 's3://portco-dw-raw/erp/'
    FILE_FORMAT = (TYPE = 'PARQUET');

-- 2. Bulk Ingestion with Copy Options
COPY INTO fact_ledger_entries
FROM @s3_portco_stage/daily/
MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE
ON_ERROR = 'SKIP_FILE';

-- 3. Zero-Copy Clone for Modeling Development
CREATE OR REPLACE DATABASE portco_finance_qa CLONE portco_finance_prod;
```

---

## Project 06: Databricks PySpark Medallion Lakehouse Pipeline

### 1. Business Context & Objective
Process 50 million clickstream and transaction records generated across 400 retail locations. Deploy an Apache Spark Medallion pipeline (Bronze raw JSON $\rightarrow$ Silver Delta Parquet $\rightarrow$ Gold Aggregated KPIs).

### 2. PySpark Execution Highlights
- Implemented lazy evaluation DAG transformations avoiding unnecessary wide shuffles.
- Enabled Delta Lake ACID transactions with schema enforcement.
- Generated Gold Star Schema dimensional tables refreshed nightly in < 18 minutes.

---

## Project 07: Client Decision-Support Case: Private Equity Turnaround

### 1. Executive Context
Private equity firm *Stonegate Capital* acquired *OmniLogistics* (\$250M revenue) 18 months ago. Year 2 EBITDA fell \$5.0M short of the investment thesis.

### 2. Root Cause Synthesis (The 5-Whys)
1. *Why did EBITDA miss budget by \$5M?* Operating expenses exceeded budget by \$3.8M, while gross revenue missed by \$1.2M.
2. *Why did OPEX exceed budget?* Fleet maintenance costs spiked by 42%.
3. *Why did fleet maintenance spike?* Older trucks (> 7 years) required emergency external repairs.
4. *Why were older trucks used?* Planned capital leasing for 80 new fuel-efficient trucks was delayed by supply chain bottlenecks.
5. *Why was capital delayed?* The procurement team failed to execute purchase orders before price escalators kicked in.

### 3. Actionable Consulting Recommendations
1. **Fleet Modernization**: Execute structured master lease agreement for 60 late-model tractors, cutting maintenance expense by \$2.4M annually.
2. **Dynamic Fuel Surcharges**: Update customer freight contracts to weekly indexed fuel surcharges, recovering \$1.6M in inflationary cost pass-through.
3. **Route Density Optimization**: Consolidate low-margin LTL (Less-than-Truckload) routes in the Southeast, improving route operating margin by 320 bps.
- **Combined Financial Impact**: Restores **\$4.8M in annualized EBITDA**, achieving 96% of the original investment underwriting thesis.

