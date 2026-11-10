# 14 — SQL for Banking Risk & Model Monitoring

## IIT Kanpur Placement Preparation — Barclays Quantitative Analytics (QA Model Monitoring)

---

### Executive Overview & Banking Data Architecture

In quantitative credit risk analytics, data extraction and snapshot construction represent over 60% of the operational workflow. Banking data warehouses (e.g., Teradata, Oracle Exadata, Snowflake, AWS Redshift) store billions of transactional, balance, and delinquency records across multi-year observation windows.

A QA Model Monitoring Analyst must write performant, bug-free SQL to:
1. Reconstruct historical point-in-time credit states without data leakage (look-ahead bias).
2. Track delinquency progression across rolling performance horizons (e.g., 12-month forward default flags).
3. Compute vintage delinquency curves, roll-rate transition matrices, and decile distributions directly within the database engine before loading into Python.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        Barclays Credit Risk Relational Schema                          │
├───────────────────────────────┬────────────────────────────────┬───────────────────────┤
│ Dimension: dim_account        │ Fact: fact_monthly_snapshot    │ Fact: fact_model_score│
├───────────────────────────────┼────────────────────────────────┼───────────────────────┤
│ • account_id (PK)             │ • snapshot_month (PK)          │ • scoring_date (PK)   │
│ • customer_id (FK)            │ • account_id (PK, FK)          │ • account_id (PK, FK) │
│ • origination_date            │ • balance_outstanding          │ • model_id            │
│ • product_type (Card, Loan)   │ • drawn_amount                 │ • model_version       │
│ • credit_limit                │ • days_past_due (DPD)          │ • raw_score           │
│ • contractual_interest_rate   │ • delinquency_bucket (0, 1, 2) │ • predicted_pd        │
│ • channel (Branch, Digital)   │ • impairment_stage (1, 2, 3)   │ • internal_grade      │
└───────────────────────────────┴────────────────────────────────┴───────────────────────┘
```

---

### 1. Generating 12-Month Outcome Windows & Basel Default Flags

To monitor a 1-year probability of default (PD) model, each account scored at baseline date $T_0$ must be tracked across the subsequent 12 calendar months ($T_1$ to $T_{12}$) to observe whether it breached the regulatory default definition (e.g., 90+ Days Past Due, bankruptcy, or debt write-off).

```sql
-- ============================================================================
-- QUERY 1: 12-Month Performance Window Default Flag Generation
-- Dialect: ANSI SQL / Snowflake / Teradata / Oracle
-- ============================================================================

WITH monthly_delinquency_timeline AS (
    SELECT
        account_id,
        snapshot_month,
        days_past_due,
        -- Regulatory default indicator: 90+ DPD or written off
        CASE 
            WHEN days_past_due >= 90 THEN 1 
            ELSE 0 
        END AS is_defaulted_current_month,
        -- Look forward 12 months using window aggregation
        MAX(CASE WHEN days_past_due >= 90 THEN 1 ELSE 0 END) OVER (
            PARTITION BY account_id
            ORDER BY snapshot_month
            ROWS BETWEEN 1 FOLLOWING AND 12 FOLLOWING
        ) AS defaulted_in_next_12m,
        -- Count how many post-observation months exist (to filter censored accounts)
        COUNT(snapshot_month) OVER (
            PARTITION BY account_id
            ORDER BY snapshot_month
            ROWS BETWEEN 1 FOLLOWING AND 12 FOLLOWING
        ) AS subsequent_months_available
    FROM fact_monthly_snapshot
    WHERE snapshot_month BETWEEN DATE '2023-01-01' AND DATE '2024-12-31'
),

baseline_scoring_cohort AS (
    SELECT
        s.account_id,
        s.scoring_date,
        s.raw_score,
        s.predicted_pd,
        s.internal_grade,
        t.defaulted_in_next_12m,
        t.subsequent_months_available
    FROM fact_model_score s
    INNER JOIN monthly_delinquency_timeline t
        ON s.account_id = t.account_id
       AND s.scoring_date = t.snapshot_month
    WHERE s.model_id = 'CARD_ACQ_V2'
      AND s.scoring_date = DATE '2023-06-01'
)

SELECT
    account_id,
    scoring_date,
    raw_score,
    predicted_pd,
    internal_grade,
    defaulted_in_next_12m
FROM baseline_scoring_cohort
WHERE subsequent_months_available = 12  -- Exclude right-censored accounts with < 12M history
  AND raw_score IS NOT NULL;
```

---

### 2. Vintage Cohort Delinquency Analysis (Months on Book — MOB)

Vintage analysis tracks the credit quality of loan cohorts originated in the same month across their lifecycle. Delinquency rates typically follow a characteristic seasoning curve: near zero during months 1–3, peaking around months 18–24, and leveling off as bad accounts are purged.

```sql
-- ============================================================================
-- QUERY 2: Vintage Delinquency Matrix (Cumulative 30+ DPD by Months on Book)
-- ============================================================================

WITH vintage_base AS (
    SELECT
        a.account_id,
        DATE_TRUNC('month', a.origination_date) AS origination_vintage,
        s.snapshot_month,
        -- Calculate Months on Book (MOB)
        DATEDIFF(month, DATE_TRUNC('month', a.origination_date), s.snapshot_month) AS months_on_book,
        s.balance_outstanding,
        CASE WHEN s.days_past_due >= 30 THEN 1 ELSE 0 END AS is_30_dpd
    FROM dim_account a
    INNER JOIN fact_monthly_snapshot s
        ON a.account_id = s.account_id
    WHERE a.origination_date >= DATE '2023-01-01'
      AND a.product_type = 'UNSECURED_PERSONAL_LOAN'
),

vintage_aggregations AS (
    SELECT
        origination_vintage,
        months_on_book,
        COUNT(DISTINCT account_id) AS active_accounts,
        SUM(balance_outstanding) AS total_balance,
        SUM(is_30_dpd) AS count_30_dpd,
        CAST(SUM(is_30_dpd) AS FLOAT) / NULLIF(COUNT(DISTINCT account_id), 0) AS rate_30_dpd
    FROM vintage_base
    WHERE months_on_book BETWEEN 0 AND 24
    GROUP BY origination_vintage, months_on_book
)

-- Pivot or summarize vintage curves for Model Monitoring Packs
SELECT
    origination_vintage,
    active_accounts,
    MAX(CASE WHEN months_on_book = 3 THEN ROUND(rate_30_dpd * 100, 2) END) AS dpd30_pct_mob_3,
    MAX(CASE WHEN months_on_book = 6 THEN ROUND(rate_30_dpd * 100, 2) END) AS dpd30_pct_mob_6,
    MAX(CASE WHEN months_on_book = 12 THEN ROUND(rate_30_dpd * 100, 2) END) AS dpd30_pct_mob_12,
    MAX(CASE WHEN months_on_book = 18 THEN ROUND(rate_30_dpd * 100, 2) END) AS dpd30_pct_mob_18,
    MAX(CASE WHEN months_on_book = 24 THEN ROUND(rate_30_dpd * 100, 2) END) AS dpd30_pct_mob_24
FROM vintage_aggregations
GROUP BY origination_vintage, active_accounts
ORDER BY origination_vintage DESC;
```

---

### 3. Monthly Roll-Rate Delinquency Transition Matrix

Roll-rate matrices track the movement of accounts between delinquency states between consecutive months (e.g., Current $\to$ 30 DPD $\to$ 60 DPD $\to$ 90 DPD Default).

```sql
-- ============================================================================
-- QUERY 3: Monthly Roll-Rate Transition Matrix (Markovian State Migration)
-- ============================================================================

WITH account_monthly_states AS (
    SELECT
        account_id,
        snapshot_month,
        CASE
            WHEN days_past_due = 0 THEN '0. Current'
            WHEN days_past_due BETWEEN 1 AND 29 THEN '1. 1-29 DPD'
            WHEN days_past_due BETWEEN 30 AND 59 THEN '2. 30-59 DPD'
            WHEN days_past_due BETWEEN 60 AND 89 THEN '3. 60-89 DPD'
            ELSE '4. 90+ DPD (Default)'
        END AS state_t0,
        -- Get the state in the immediately following month (T+1)
        LEAD(
            CASE
                WHEN days_past_due = 0 THEN '0. Current'
                WHEN days_past_due BETWEEN 1 AND 29 THEN '1. 1-29 DPD'
                WHEN days_past_due BETWEEN 30 AND 59 THEN '2. 30-59 DPD'
                WHEN days_past_due BETWEEN 60 AND 89 THEN '3. 60-89 DPD'
                ELSE '4. 90+ DPD (Default)'
            END
        ) OVER (PARTITION BY account_id ORDER BY snapshot_month) AS state_t1
    FROM fact_monthly_snapshot
    WHERE snapshot_month IN (DATE '2024-05-01', DATE '2024-06-01')
)

SELECT
    state_t0 AS transition_from_may,
    state_t1 AS transition_to_june,
    COUNT(account_id) AS account_count,
    ROUND(
        COUNT(account_id) * 100.0 / SUM(COUNT(account_id)) OVER (PARTITION BY state_t0), 
        2
    ) AS roll_rate_probability_pct
FROM account_monthly_states
WHERE snapshot_month = DATE '2024-05-01'
  AND state_t1 IS NOT NULL
GROUP BY state_t0, state_t1
ORDER BY state_t0, state_t1;
```

---

### 4. Decile Discrimination & Scorecard Performance Extraction

This query aggregates scored accounts into 10 deciles directly in SQL, computing Decile Bad Rates and inputs for KS / Gini evaluation.

```sql
-- ============================================================================
-- QUERY 4: Scorecard Decile Discrimination Aggregation
-- ============================================================================

WITH scored_accounts AS (
    SELECT
        s.account_id,
        s.raw_score,
        s.predicted_pd,
        o.is_bad_12m,
        -- Decile partition: Decile 1 = Lowest Score / Highest Risk
        NTILE(10) OVER (ORDER BY s.raw_score ASC) AS risk_decile
    FROM fact_model_score s
    INNER JOIN target_12m_outcomes o
        ON s.account_id = o.account_id
       AND s.scoring_date = o.scoring_date
    WHERE s.model_id = 'RETAIL_SCORECARD_2022'
      AND s.scoring_date = DATE '2023-01-01'
),

decile_metrics AS (
    SELECT
        risk_decile,
        MIN(raw_score) AS min_score,
        MAX(raw_score) AS max_score,
        COUNT(account_id) AS total_accounts,
        SUM(is_bad_12m) AS bad_accounts,
        COUNT(account_id) - SUM(is_bad_12m) AS good_accounts,
        AVG(predicted_pd) AS avg_predicted_pd,
        CAST(SUM(is_bad_12m) AS FLOAT) / COUNT(account_id) AS observed_bad_rate
    FROM scored_accounts
    GROUP BY risk_decile
)

SELECT
    risk_decile,
    min_score || ' - ' || max_score AS score_range,
    total_accounts,
    bad_accounts,
    good_accounts,
    ROUND(observed_bad_rate * 100.0, 2) AS observed_bad_rate_pct,
    ROUND(avg_predicted_pd * 100.0, 2) AS expected_pd_pct,
    -- Ratio of Observed vs Expected
    ROUND(observed_bad_rate / NULLIF(avg_predicted_pd, 0), 3) AS oe_ratio
FROM decile_metrics
ORDER BY risk_decile ASC;
```

---

### 5. In-Database Population Stability Index (PSI) Binning

Executing the PSI calculation directly inside the database minimizes data transfer to local analytics environments.

```sql
-- ============================================================================
-- QUERY 5: In-Database Score Distribution & PSI Binning
-- ============================================================================

WITH baseline_distribution AS (
    SELECT
        internal_rating_grade,
        COUNT(*) * 1.0 / SUM(COUNT(*)) OVER () AS expected_pct
    FROM fact_model_score
    WHERE scoring_date = DATE '2022-12-01' -- Development / Baseline Quarter
      AND model_id = 'CORP_RATING_V3'
    GROUP BY internal_rating_grade
),

monitoring_distribution AS (
    SELECT
        internal_rating_grade,
        COUNT(*) * 1.0 / SUM(COUNT(*)) OVER () AS actual_pct
    FROM fact_model_score
    WHERE scoring_date = DATE '2024-06-01' -- Current Monitoring Quarter
      AND model_id = 'CORP_RATING_V3'
    GROUP BY internal_rating_grade
)

SELECT
    COALESCE(b.internal_rating_grade, m.internal_rating_grade) AS rating_grade,
    ROUND(b.expected_pct * 100.0, 2) AS expected_pct,
    ROUND(m.actual_pct * 100.0, 2) AS actual_pct,
    ROUND((m.actual_pct - b.expected_pct) * 100.0, 2) AS delta_pct,
    -- Individual bin PSI contribution: (A - E) * ln(A / E)
    ROUND(
        (m.actual_pct - b.expected_pct) * LN(m.actual_pct / NULLIF(b.expected_pct, 0)),
        5
    ) AS psi_contribution
FROM baseline_distribution b
FULL OUTER JOIN monitoring_distribution m
    ON b.internal_rating_grade = m.internal_rating_grade
ORDER BY rating_grade;
```

---

### 6. Production Database Query Optimization Best Practices

1. **Partition Pruning:** Banking tables are partitioned by date keys (e.g., `snapshot_month` or `accounting_date`). Always filter directly on the partition column using immutable literals (`snapshot_month = DATE '2024-06-01'`) rather than applying functions (`WHERE YEAR(snapshot_month) = 2024`), which force full-table scans.
2. **Deterministic Tie-Breaking:** In quant score decile rankings (`NTILE` or `ROW_NUMBER`), always provide a unique secondary sort key (e.g., `ORDER BY score DESC, account_id ASC`) to guarantee that results are strictly reproducible.
3. **Prevent Null Dividends:** Always wrap denominators in `NULLIF(col, 0)` to eliminate run-time division-by-zero crashes.
4. **Window Function Scoping:** Restrict window frames explicitly using `ROWS BETWEEN ...` rather than default `RANGE BETWEEN ...` to avoid massive temp-space spills in large-scale banking environments.

---

*Authoritative cross-reference: ANSI SQL:2016 Standards; Snowflake Query Optimization Documentation; Teradata Financial Services Logical Data Model (FS-LDM).*

