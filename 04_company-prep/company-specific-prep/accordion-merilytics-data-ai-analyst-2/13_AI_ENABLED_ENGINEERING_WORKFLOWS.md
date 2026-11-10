# Module 13 — AI-Enabled Engineering Workflows & Governance

The Data & AI Analyst 2 job description explicitly specifies: **"Apply AI-enabled engineering tools across the build cycle. Write SQL and Python code. Perform testing and documentation. Own the accuracy of analytical deliverables."**

At Accordion (Merilytics), AI is not a magic button or a substitute for fundamental thinking; it is a **productivity amplifier** embedded into the analytics development lifecycle.

---

## 1. AI Across the Analytics Build Cycle

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        AI-ENABLED ENGINEERING DEVELOPMENT CYCLE                        │
├────────────────────┬───────────────────────────────────┬───────────────────────────────┤
│    Build Phase     │          AI Tool Utility          │        Human Ownership        │
├────────────────────┼───────────────────────────────────┼───────────────────────────────┤
│ 1. Architecture &  │ Drafting initial SQL queries, CTE │ Verifying business logic, join│
│    Scaffolding     │ structures, and Python templates. │ keys, and aggregation grains. │
├────────────────────┼───────────────────────────────────┼───────────────────────────────┤
│ 2. Optimization &  │ Refactoring slow Python loops into│ Profiling runtime execution   │
│    Refactoring     │ vectorized NumPy; dialect tuning. │ in Snowflake / Databricks.    │
├────────────────────┼───────────────────────────────────┼───────────────────────────────┤
│ 3. Automated Test  │ Generating edge-case synthetic    │ Ensuring business invariants  │
│    Generation      │ data (nulls, duplicates, outliers)│ (Assets = Liab + Equity).     │
├────────────────────┼───────────────────────────────────┼───────────────────────────────┤
│ 4. Documentation   │ Generating function docstrings,   │ Reviewing technical accuracy  │
│    & Data Catalog  │ data dictionaries, and handovers. │ for client C-suite audience.  │
└────────────────────┴───────────────────────────────────┴───────────────────────────────┘
```

---

## 2. Verification Protocols & Preventing AI Hallucinations

Large Language Models (LLMs) frequently generate syntactically plausible but logically flawed code. A professional analyst follows strict verification guardrails:

```
┌─────────────────────────────────┬─────────────────────────────────┬─────────────────────────────────┐
│        AI Hallucination Risk    │      Real-World Manifestation   │        Verification Protocol    │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Dialect Confusion               │ Using PostgreSQL `GENERATE_     │ Check Snowflake / Databricks    │
│                                 │ SERIES` inside Snowflake or T-  │ documentation for supported     │
│                                 │ SQL `TOP` in ANSI SQL.          │ native functions.               │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Silent Aggregation Errors       │ Summing average percentages or  │ Verify dimensional granularity; │
│                                 │ taking an average of ratios.    │ compute weighted averages from  │
│                                 │                                 │ raw numerator & denominator.    │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Cartesian Fan-Out               │ Joining multiple one-to-many    │ Run row-count checks before and │
│                                 │ tables in a single query block. │ after joins: output rows must   │
│                                 │                                 │ match expected transaction grain│
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Boundary Edge Cases             │ Missing leap years, negative    │ Write explicit unit assertions: │
│                                 │ balances, or 3VL NULL traps.    │ `assert df['balance'].min() >= 0`│
└─────────────────────────────────┴─────────────────────────────────┴─────────────────────────────────┘
```

---

## 3. Client Confidentiality & Data Privacy Safeguards

In private equity consulting, breaching client confidentiality or uploading proprietary financial ledgers to external public AI systems is grounds for immediate termination.

### 3.1 Strict Security Rules
1. **Zero Client Data in Public AI**: Never paste proprietary client transaction rows, customer PII (names, emails, credit card tokens), or confidential quarterly P&L numbers into public LLM interfaces.
2. **Schema-Only Obfuscation**: When using AI for complex query scaffolding, provide **abstract synthetic schemas with dummy column names**:
   ```sql
   -- SAFE PROMPT FORMAT:
   -- "Given Table A (entity_id INT, metric_val NUMERIC, event_date DATE) 
   -- and Table B (entity_id INT, status_flag INT), write a window query 
   -- to compute running totals partitioned by entity_id."
   ```
3. **Approved Enterprise Tenants Only**: Use company-provisioned, private enterprise instances (e.g., Azure OpenAI with zero data retention policies) where data is not used for model retraining.

---

## 4. Demonstration: AI-Assisted SQL Generation with Independent Verification

### Scenario
An analyst needs a query to calculate **Customer Recency, Frequency, and Monetary (RFM) Scores** in Snowflake SQL.

### Step 1: AI Prompting (Abstracted Schema)
```text
PROMPT:
Given a Snowflake table `fact_orders` with columns `customer_id` (INT), `order_date` (DATE), 
and `order_amount` (FLOAT), write an optimized query to compute:
1. Recency: Days since most recent order as of '2025-12-31'.
2. Frequency: Total completed order count.
3. Monetary: Total cumulative order spend.
4. Segment each metric into 4 quartiles (1 to 4) using NTILE.
```

### Step 2: AI-Generated Query
```sql
WITH CustomerAggregates AS (
    SELECT 
        customer_id,
        DATEDIFF('day', MAX(order_date), '2025-12-31'::DATE) AS recency_days,
        COUNT(order_id) AS frequency_count,
        SUM(order_amount) AS monetary_total
    FROM fact_orders
    WHERE order_date <= '2025-12-31'
    GROUP BY customer_id
)
SELECT 
    customer_id,
    recency_days,
    frequency_count,
    monetary_total,
    -- Quartile ranking
    NTILE(4) OVER(ORDER BY recency_days ASC) AS recency_quartile,
    NTILE(4) OVER(ORDER BY frequency_count DESC) AS frequency_quartile,
    NTILE(4) OVER(ORDER BY monetary_total DESC) AS monetary_quartile
FROM CustomerAggregates;
```

### Step 3: Human Verification & Quality Control
The analyst reviews the generated code and identifies **two critical logical flaws**:
1. *Flaw 1 (Recency Logic)*: `NTILE(4) OVER(ORDER BY recency_days ASC)` assigns Quartile 1 to the lowest days (most recent customers). In standard RFM scoring, Quartile 4 represents the best (most recent) customers. The order should be `DESC` or the quartile flipped.
2. *Flaw 2 (Zero Handling)*: If a customer has negative order amounts (returns/refunds), `monetary_total` could be negative. A `HAVING monetary_total > 0` or `COALESCE` check is required.

### Step 4: Final Production-Ready Refactored Query
```sql
WITH CustomerAggregates AS (
    SELECT 
        customer_id,
        DATEDIFF('day', MAX(order_date), '2025-12-31'::DATE) AS recency_days,
        COUNT(DISTINCT order_id) AS frequency_count,
        SUM(order_amount) AS monetary_total
    FROM fact_orders
    WHERE order_date <= '2025-12-31'
      AND order_status = 'Completed' -- Added filter to exclude canceled orders
    GROUP BY customer_id
    HAVING SUM(order_amount) > 0
)
SELECT 
    customer_id,
    recency_days,
    frequency_count,
    ROUND(monetary_total, 2) AS monetary_total,
    -- Corrected RFM Scoring: 4 = Best, 1 = Worst
    5 - NTILE(4) OVER(ORDER BY recency_days ASC) AS r_score, -- Lower days = higher score (4)
    NTILE(4) OVER(ORDER BY frequency_count ASC) AS f_score,  -- Higher frequency = higher score (4)
    NTILE(4) OVER(ORDER BY monetary_total ASC) AS m_score    -- Higher spend = higher score (4)
FROM CustomerAggregates;
```

This demonstrates true **AI-enabled engineering ownership**: using AI for rapid code scaffolding, then applying rigorous human verification to guarantee business accuracy.

