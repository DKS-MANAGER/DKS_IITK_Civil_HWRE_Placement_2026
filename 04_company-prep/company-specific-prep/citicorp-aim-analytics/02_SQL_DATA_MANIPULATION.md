# 02. SQL & Data Manipulation — Complete Study Guide & 30 Practice Problems

> **Target Role**: Spec Analytics Analyst — Business Analytics (SBS), Citi AIM  
> **Relevance**: Explicitly required by the job description ("Familiarity with Tools: Identifies and compiles data sets using a variety of tools (e.g. SQL, Access)"). Evaluated in OA Section 5 and technical interviews.  
> **Synthetic Data Disclaimer**: All schemas, tables, customer IDs, and transaction records in this module are `[PRACTICE CASE ASSUMPTION]` synthetic benchmarks created for interview preparation.

---

## 1. Relational Foundations & Table Grain

### 1.1 Relational Architecture in Financial Systems
In an enterprise banking data warehouse, data is structured into normalized entities:
* **Primary Key (PK)**: A column (or set of columns) that uniquely identifies each row in a table (e.g., `cust_id` in `customers`). Cannot be NULL.
* **Foreign Key (FK)**: A column in one table that references the Primary Key of another table, enforcing referential integrity (e.g., `cust_id` in `accounts`).
* **Table Grain**: The exact business definition of what a single row represents:
  * Transaction grain: One row per card authorization swipe.
  * Account grain: One row per credit card account.
  * Customer grain: One row per unique legal individual/entity.
  * Snapshot grain: One row per customer per calendar month-end.

> **The Grain Mismatch Trap**: Joining a customer-level table (1 row per customer) to a transaction-level table (50 rows per customer) without prior aggregation causes a **one-to-many Cartesian fan-out**. Summing balances after such a join will multiply the customer's balance by 50! Always clarify the grain of every table before writing joins.

---

## 2. SQL Logical Processing Order

SQL is not executed top-to-bottom. It follows a strict logical processing pipeline:

```
[Written Order]                       [Logical Execution Sequence]
1. SELECT                              1. FROM & JOIN (Establishes source dataset & applies join criteria)
2. FROM                                2. WHERE (Row-level filtering before any grouping)
3. JOIN ... ON                         3. GROUP BY (Collapses records into aggregation buckets)
4. WHERE                               4. HAVING (Filters aggregated group summaries)
5. GROUP BY                            5. SELECT (Evaluates column expressions, aliases, & window functions)
6. HAVING                              6. DISTINCT (Removes duplicate result rows)
7. ORDER BY                            7. ORDER BY (Sorts final result set)
8. LIMIT / OFFSET                      8. LIMIT / OFFSET (Truncates rows returned to client)
```

### Essential Rules Derived from Execution Order:
1. **Cannot filter an aggregate alias in `WHERE`**: `SELECT cust_id, SUM(amount) AS total_spend FROM txns WHERE total_spend > 500` will fail with an error. `WHERE` executes before `total_spend` is computed. You must filter using `HAVING SUM(amount) > 500` or use a CTE.
2. **Window functions execute in `SELECT`**: Window functions cannot be placed inside `WHERE` or `HAVING` clauses. To filter by a window function (e.g., `WHERE rnk = 1`), wrap the query in a CTE or subquery.

---

## 3. Joins, Relational Algebra & NULL Semantics

### 3.1 Relational Joins Visualized

```
   Table A (Accounts)                 Table B (Transactions)
 ┌────────────┬───────────┐         ┌────────────┬────────────┐
 │ account_id │ cust_id   │         │ account_id │ txn_amount │
 ├────────────┼───────────┤         ├────────────┼────────────┤
 │    101     │   C-1     │         │    101     │    50.0    │
 │    102     │   C-2     │         │    101     │   150.0    │
 │    103     │   C-3     │         │    102     │   200.0    │
 │   NULL     │   C-4     │         │    104     │   400.0    │
 └────────────┴───────────┘         └────────────┴────────────┘
```

* **`INNER JOIN`**: Returns rows where keys match in both tables.
  * Accounts 101 (2 matches) and 102 (1 match) $\implies 3$ rows returned.
* **`LEFT JOIN`**: All rows from Table A, plus matching rows from Table B (unmatched filled with NULL).
  * Account 103 returned with `txn_amount = NULL`. Account NULL returned with `txn_amount = NULL`.
* **`RIGHT JOIN`**: All rows from Table B, plus matching rows from Table A.
  * Account 104 returned with Table A columns as NULL.
* **`FULL OUTER JOIN`**: All rows from both tables, with NULLs filled where keys do not match.
* **`CROSS JOIN`**: Cartesian product ($N \times M$ rows).

### 3.2 SQL NULL Three-Valued Logic
* Any comparison with `NULL` (`= NULL`, `!= NULL`, `< NULL`) evaluates to **`UNKNOWN`** (falsy in WHERE conditions).
* **`IS NULL` and `IS NOT NULL`**: The only valid operators to test for NULL presence.
* **`COALESCE(val1, val2, ...)`**: Returns the first non-NULL expression in the argument list.
* **`NULLIF(val1, val2)`**: Returns `NULL` if `val1 = val2`; otherwise returns `val1`. Essential for preventing divide-by-zero errors:
  $$\text{Margin} = \frac{\text{Profit}}{\text{NULLIF}(\text{Revenue}, 0)}$$
* **`COUNT(*)` vs `COUNT(col)`**: `COUNT(*)` counts all rows including NULLs; `COUNT(col)` counts only non-NULL rows.

---

## 4. Window Functions Mastery

Window functions calculate metrics across a set of table rows related to the current row without collapsing rows into a single summary.

### 4.1 Syntax Anatomy
```sql
<window_function>() OVER (
    [PARTITION BY partition_col1, partition_col2]
    [ORDER BY sort_col1 ASC | DESC]
    [ROWS | RANGE BETWEEN frame_start AND frame_end]
)
```

### 4.2 Ranking Functions Comparison

| Function | Output on values: `[900, 900, 750, 600]` | Behavior on Ties |
| :--- | :--- | :--- |
| **`ROW_NUMBER()`** | `1, 2, 3, 4` | Strict sequential integer; arbitrates ties non-deterministically unless tiebreaker added. |
| **`RANK()`** | `1, 1, 3, 4` | Ties receive identical rank; **skips** subsequent ranks. |
| **`DENSE_RANK()`** | `1, 1, 2, 3` | Ties receive identical rank; **does NOT skip** subsequent ranks. |
| **`NTILE(k)`** | `1, 1, 2, 2` (for $k=2$) | Divides rows into $k$ equal buckets (deciles, quartiles). |

> **Interview Standard**: "Find the 2nd highest transaction per account." Always use `DENSE_RANK()` inside a CTE to handle identical high values without missing the second tier.

### 4.3 Value Functions
* **`LAG(col, offset, default)`**: Accesses a preceding row's value. Used for month-over-month growth, transaction velocity, and detecting sequential balance declines.
* **`LEAD(col, offset, default)`**: Accesses a succeeding row's value.
* **`FIRST_VALUE(col)` / `LAST_VALUE(col)`**: Returns the initial or terminal value in the current window frame.

### 4.4 Frame Specifications (`ROWS` vs `RANGE`)
* `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`: Physical running sum from start to current row.
* `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW`: 3-row moving calculation.
* `RANGE BETWEEN INTERVAL '30 DAYS' PRECEDING AND CURRENT ROW`: Value-based moving window across calendar intervals.

---

## 5. Dialect Syntax Nuances (PostgreSQL vs Oracle vs MySQL vs Access)

| Feature | PostgreSQL / Standard ANSI | Oracle Database (Common at Citi) | MySQL (8.0+) | Microsoft Access SQL |
| :--- | :--- | :--- | :--- | :--- |
| **Date Truncation** | `DATE_TRUNC('month', dt)` | `TRUNC(dt, 'MM')` | `DATE_FORMAT(dt, '%Y-%m-01')` | `DateSerial(Year(dt), Month(dt), 1)` |
| **Current Date** | `CURRENT_DATE` | `SYSDATE` | `CURDATE()` | `Date()` |
| **NULL Handling** | `COALESCE(a, b)` | `NVL(a, b)` | `IFNULL(a, b)` | `Nz(a, b)` |
| **String Concat** | `a || b` | `a || b` | `CONCAT(a, b)` | `a & b` |
| **Row Limiting** | `LIMIT n` | `FETCH FIRST n ROWS ONLY` | `LIMIT n` | `SELECT TOP n` |
| **Window Functions**| Full Support | Full Support | Full Support | **Not Supported natively** |

---

## 6. Synthetic Banking Database Schema (`[PRACTICE CASE ASSUMPTION]`)

The following relational schema is used for all 30 exercises:

```
TABLE: customers
┌─────────────┬──────────────┬────────────────────────────────────────────────────────┐
│ Column Name │ Data Type    │ Constraints / Description                              │
├─────────────┼──────────────┼────────────────────────────────────────────────────────┤
│ cust_id     │ VARCHAR(20)  │ PRIMARY KEY. Unique customer identifier.               │
│ full_name   │ VARCHAR(100) │ Customer full name.                                    │
│ segment     │ VARCHAR(20)  │ Customer tier: 'RETAIL', 'WEALTH', 'COMMERCIAL'.       │
│ join_date   │ DATE         │ Date customer onboarded.                               │
│ city        │ VARCHAR(50)  │ Residential city.                                      │
└─────────────┴──────────────┴────────────────────────────────────────────────────────┘

TABLE: accounts
┌─────────────┬──────────────┬────────────────────────────────────────────────────────┐
│ Column Name │ Data Type    │ Constraints / Description                              │
├─────────────┼──────────────┼────────────────────────────────────────────────────────┤
│ account_id  │ VARCHAR(20)  │ PRIMARY KEY. Unique account identifier.                │
│ cust_id     │ VARCHAR(20)  │ FOREIGN KEY -> customers(cust_id).                     │
│ acct_type   │ VARCHAR(20)  │ 'SAVINGS', 'CHECKING', 'CREDIT_CARD', 'PERSONAL_LOAN'. │
│ open_date   │ DATE         │ Date account opened.                                   │
│ status      │ VARCHAR(20)  │ 'ACTIVE', 'DORMANT', 'CLOSED'.                         │
│ credit_limit│ DECIMAL(12,2)│ Credit limit assigned (NULL for deposit accounts).     │
└─────────────┴──────────────┴────────────────────────────────────────────────────────┘

TABLE: transactions
┌─────────────┬──────────────┬────────────────────────────────────────────────────────┐
│ Column Name │ Data Type    │ Constraints / Description                              │
├─────────────┼──────────────┼────────────────────────────────────────────────────────┤
│ txn_id      │ VARCHAR(30)  │ PRIMARY KEY. Unique transaction identifier.            │
│ account_id  │ VARCHAR(20)  │ FOREIGN KEY -> accounts(account_id).                   │
│ txn_date    │ TIMESTAMP    │ Date and timestamp of transaction.                     │
│ amount      │ DECIMAL(12,2)│ Transaction monetary value (positive).                 │
│ txn_type    │ VARCHAR(20)  │ 'DEBIT', 'CREDIT', 'FEE', 'INTEREST'.                  │
│ merchant    │ VARCHAR(100) │ Merchant description (e.g. 'Amazon', 'Shell').         │
│ status      │ VARCHAR(20)  │ 'APPROVED', 'DECLINED', 'FLAGGED'.                     │
└─────────────┴──────────────┴────────────────────────────────────────────────────────┘

TABLE: monthly_snapshots
┌─────────────┬──────────────┬────────────────────────────────────────────────────────┐
│ Column Name │ Data Type    │ Constraints / Description                              │
├─────────────┼──────────────┼────────────────────────────────────────────────────────┤
│ snapshot_id │ VARCHAR(30)  │ PRIMARY KEY. Unique snapshot row key.                  │
│ account_id  │ VARCHAR(20)  │ FOREIGN KEY -> accounts(account_id).                   │
│ month_end   │ DATE         │ Calendar month ending date (e.g. '2026-09-30').        │
│ balance     │ DECIMAL(14,2)│ Closing balance at month end.                          │
│ dpd         │ INT          │ Days Past Due (0 = Current, 30 = 30+ DPD).             │
└─────────────┴──────────────┴────────────────────────────────────────────────────────┘
```

---

## 7. 30 Progressive Banking SQL Practice Problems

### Part A: Basic Aggregation, Filtering & Case Logic (Problems 01–05)

#### Problem 01: Summary of High-Value Debit Transactions
* **Task**: Find total count and sum of all approved DEBIT transactions exceeding $\$1,000$ per account during calendar year 2026. Only include accounts with at least 3 such transactions.
* **SQL Query**:
```sql
SELECT 
    account_id,
    COUNT(txn_id) AS high_value_count,
    SUM(amount) AS total_high_value_spend
FROM transactions
WHERE status = 'APPROVED'
  AND txn_type = 'DEBIT'
  AND amount > 1000.00
  AND txn_date >= '2026-01-01' AND txn_date < '2027-01-01'
GROUP BY account_id
HAVING COUNT(txn_id) >= 3
ORDER BY total_high_value_spend DESC;
```
* **Explanation**: Demonstrates `WHERE` filtering prior to aggregation and `HAVING` condition filtering post-aggregation.

---

#### Problem 02: Customer Segment Account Distribution
* **Task**: For each customer `segment`, count total distinct customers, total active accounts, and total closed accounts.
* **SQL Query**:
```sql
SELECT 
    c.segment,
    COUNT(DISTINCT c.cust_id) AS total_customers,
    COUNT(DISTINCT CASE WHEN a.status = 'ACTIVE' THEN a.account_id END) AS active_accounts,
    COUNT(DISTINCT CASE WHEN a.status = 'CLOSED' THEN a.account_id END) AS closed_accounts
FROM customers c
LEFT JOIN accounts a ON c.cust_id = a.cust_id
GROUP BY c.segment
ORDER BY total_customers DESC;
```
* **Explanation**: Uses conditional aggregation with `CASE WHEN` inside `COUNT(DISTINCT ...)`.

---

#### Problem 03: Categorizing Credit Card Utilization Tiers
* **Task**: Calculate each active credit card account's utilization percentage as of latest snapshot (`balance / credit_limit * 100`). Categorize into:
  * 'LOW': Utilization $\le 30\%$
  * 'MEDIUM': Utilization between $30.01\%$ and $70\%$
  * 'HIGH': Utilization $> 70\%$
  * 'NO_LIMIT': If credit limit is NULL or zero.
* **SQL Query**:
```sql
SELECT 
    a.account_id,
    a.credit_limit,
    s.balance,
    ROUND((s.balance / NULLIF(a.credit_limit, 0)) * 100, 2) AS utilization_pct,
    CASE 
        WHEN a.credit_limit IS NULL OR a.credit_limit = 0 THEN 'NO_LIMIT'
        WHEN (s.balance / a.credit_limit) * 100 <= 30.0 THEN 'LOW'
        WHEN (s.balance / a.credit_limit) * 100 <= 70.0 THEN 'MEDIUM'
        ELSE 'HIGH'
    END AS utilization_tier
FROM accounts a
JOIN monthly_snapshots s ON a.account_id = s.account_id
WHERE a.acct_type = 'CREDIT_CARD'
  AND a.status = 'ACTIVE'
  AND s.month_end = '2026-09-30';
```
* **Explanation**: Protects against divide-by-zero using `NULLIF(a.credit_limit, 0)`.

---

#### Problem 04: Handling Missing City Records (Data Cleansing)
* **Task**: Group customers by city, treating missing or NULL city values as 'UNKNOWN'. Return total customer count and earliest join date per city.
* **SQL Query**:
```sql
SELECT 
    COALESCE(NULLIF(TRIM(city), ''), 'UNKNOWN') AS clean_city,
    COUNT(cust_id) AS customer_count,
    MIN(join_date) AS earliest_join_date
FROM customers
GROUP BY COALESCE(NULLIF(TRIM(city), ''), 'UNKNOWN')
ORDER BY customer_count DESC;
```
* **Explanation**: Cleans whitespace and handles both empty strings and actual NULL values with `COALESCE(NULLIF(TRIM(city), ''), 'UNKNOWN')`.

---

#### Problem 05: Net Monthly Deposit vs Withdrawal Flow
* **Task**: For account 'ACC-101', calculate total monthly inflow (CREDIT), total monthly outflow (DEBIT), and net cash flow per calendar month.
* **SQL Query**:
```sql
SELECT 
    DATE_TRUNC('month', txn_date) AS txn_month,
    SUM(CASE WHEN txn_type = 'CREDIT' THEN amount ELSE 0 END) AS total_inflow,
    SUM(CASE WHEN txn_type = 'DEBIT' THEN amount ELSE 0 END) AS total_outflow,
    SUM(CASE WHEN txn_type = 'CREDIT' THEN amount 
             WHEN txn_type = 'DEBIT' THEN -amount 
             ELSE 0 END) AS net_cash_flow
FROM transactions
WHERE account_id = 'ACC-101'
  AND status = 'APPROVED'
GROUP BY DATE_TRUNC('month', txn_date)
ORDER BY txn_month;
```

---

### Part B: Joins, Relational Integrity & Deduplication (Problems 06–10)

#### Problem 06: Customers with Zero Transactions (Anti-Join)
* **Task**: Return all customers who opened an account in 2026 but have recorded zero approved transactions across any account.
* **SQL Query**:
```sql
SELECT 
    c.cust_id,
    c.full_name,
    c.join_date
FROM customers c
JOIN accounts a ON c.cust_id = a.cust_id
LEFT JOIN transactions t ON a.account_id = t.account_id AND t.status = 'APPROVED'
WHERE a.open_date >= '2026-01-01'
GROUP BY c.cust_id, c.full_name, c.join_date
HAVING COUNT(t.txn_id) = 0;
```

---

#### Problem 07: Deduplicating Potential Accidental Double Swipes
* **Task**: Detect duplicate transaction entries: same `account_id`, same `amount`, same `merchant`, and exact same `txn_date` timestamp. Return only the duplicated `txn_id`s that should be marked for deletion (keep the smallest `txn_id`).
* **SQL Query**:
```sql
WITH RankedDuplicates AS (
    SELECT 
        txn_id,
        account_id,
        txn_date,
        amount,
        merchant,
        ROW_NUMBER() OVER (
            PARTITION BY account_id, txn_date, amount, merchant 
            ORDER BY txn_id ASC
        ) AS duplicate_rnk
    FROM transactions
)
SELECT txn_id, account_id, txn_date, amount, merchant
FROM RankedDuplicates
WHERE duplicate_rnk > 1;
```

---

#### Problem 08: Multi-Account Cross-Holdings
* **Task**: Find customers who hold BOTH an active 'CREDIT_CARD' and an active 'SAVINGS' account.
* **SQL Query**:
```sql
SELECT 
    c.cust_id,
    c.full_name
FROM customers c
JOIN accounts a ON c.cust_id = a.cust_id
WHERE a.status = 'ACTIVE'
  AND a.acct_type IN ('CREDIT_CARD', 'SAVINGS')
GROUP BY c.cust_id, c.full_name
HAVING COUNT(DISTINCT a.acct_type) = 2;
```

---

#### Problem 09: Resolving Join Row Multiplication
* **Task**: Calculate each customer's total checking account balance as of 2026-09-30 and their total credit card transactions in September 2026 without causing Cartesian row explosion.
* **SQL Query**:
```sql
WITH SeptBalances AS (
    SELECT 
        a.cust_id,
        SUM(s.balance) AS total_checking_balance
    FROM accounts a
    JOIN monthly_snapshots s ON a.account_id = s.account_id
    WHERE a.acct_type = 'CHECKING'
      AND s.month_end = '2026-09-30'
    GROUP BY a.cust_id
),
SeptCardSpend AS (
    SELECT 
        a.cust_id,
        SUM(t.amount) AS total_card_spend
    FROM accounts a
    JOIN transactions t ON a.account_id = t.account_id
    WHERE a.acct_type = 'CREDIT_CARD'
      AND t.status = 'APPROVED'
      AND t.txn_date >= '2026-09-01' AND t.txn_date < '2026-10-01'
    GROUP BY a.cust_id
)
SELECT 
    c.cust_id,
    c.full_name,
    COALESCE(b.total_checking_balance, 0.00) AS total_checking_balance,
    COALESCE(s.total_card_spend, 0.00) AS total_card_spend
FROM customers c
LEFT JOIN SeptBalances b ON c.cust_id = b.cust_id
LEFT JOIN SeptCardSpend s ON c.cust_id = s.cust_id
ORDER BY total_card_spend DESC;
```
* **Explanation**: Aggregates datasets separately in CTEs before joining to customer table, eliminating Cartesian product distortion.

---

#### Problem 10: Full Outer Reconciliation Audit
* **Task**: Perform a ledger reconciliation between internal transaction debits and monthly snapshot balance delta for account 'ACC-101'. Return all calendar months showing any discrepancy.
* **SQL Query**:
```sql
WITH TxnDebits AS (
    SELECT 
        DATE_TRUNC('month', txn_date)::DATE AS m_date,
        SUM(amount) AS sum_debit
    FROM transactions
    WHERE account_id = 'ACC-101' AND txn_type = 'DEBIT' AND status = 'APPROVED'
    GROUP BY DATE_TRUNC('month', txn_date)::DATE
),
BalanceDeltas AS (
    SELECT 
        month_end,
        balance,
        LAG(balance) OVER (ORDER BY month_end) AS prev_bal,
        (LAG(balance) OVER (ORDER BY month_end) - balance) AS implied_debit
    FROM monthly_snapshots
    WHERE account_id = 'ACC-101'
)
SELECT 
    COALESCE(t.m_date, DATE_TRUNC('month', b.month_end)::DATE) AS audit_month,
    t.sum_debit AS recorded_txn_debits,
    b.implied_debit AS ledger_implied_debits,
    ABS(COALESCE(t.sum_debit, 0) - COALESCE(b.implied_debit, 0)) AS variance
FROM TxnDebits t
FULL OUTER JOIN BalanceDeltas b 
    ON t.m_date = DATE_TRUNC('month', b.month_end)::DATE
WHERE ABS(COALESCE(t.sum_debit, 0) - COALESCE(b.implied_debit, 0)) > 0.01;
```

---

### Part C: Common Table Expressions (CTEs) & Subqueries (Problems 11–15)

#### Problem 11: Customers Exceeding Segment Average Spend
* **Task**: Find all retail customers (`segment = 'RETAIL'`) whose total approved 2026 spend exceeds the average 2026 spend of all retail customers.
* **SQL Query**:
```sql
WITH RetailCustomerSpend AS (
    SELECT 
        c.cust_id,
        c.full_name,
        SUM(t.amount) AS cust_spend
    FROM customers c
    JOIN accounts a ON c.cust_id = a.cust_id
    JOIN transactions t ON a.account_id = t.account_id
    WHERE c.segment = 'RETAIL'
      AND t.status = 'APPROVED'
      AND t.txn_type = 'DEBIT'
      AND t.txn_date >= '2026-01-01' AND t.txn_date < '2027-01-01'
    GROUP BY c.cust_id, c.full_name
),
SegmentAverage AS (
    SELECT AVG(cust_spend) AS avg_retail_spend
    FROM RetailCustomerSpend
)
SELECT 
    s.cust_id,
    s.full_name,
    s.cust_spend,
    ROUND(a.avg_retail_spend, 2) AS benchmark_avg
FROM RetailCustomerSpend s
CROSS JOIN SegmentAverage a
WHERE s.cust_spend > a.avg_retail_spend
ORDER BY s.cust_spend DESC;
```

---

#### Problem 12: Second Largest Transaction per Account
* **Task**: Return the exact transaction details for the 2nd highest transaction ever recorded for each account. If an account has multiple transactions tied for 2nd, return all.
* **SQL Query**:
```sql
WITH RankedTxns AS (
    SELECT 
        account_id,
        txn_id,
        txn_date,
        amount,
        merchant,
        DENSE_RANK() OVER (PARTITION BY account_id ORDER BY amount DESC) AS spend_rank
    FROM transactions
    WHERE status = 'APPROVED'
)
SELECT account_id, txn_id, txn_date, amount, merchant
FROM RankedTxns
WHERE spend_rank = 2
ORDER BY account_id;
```

---

#### Problem 13: High-Growth Customer Flag
* **Task**: Identify customers whose Q3 2026 spend (July–Sept) was at least $50\%$ higher than their Q2 2026 spend (April–June), with minimum Q2 spend of $\$1,000$.
* **SQL Query**:
```sql
WITH QuarterlySpend AS (
    SELECT 
        a.cust_id,
        SUM(CASE WHEN t.txn_date >= '2026-04-01' AND t.txn_date < '2026-07-01' THEN t.amount ELSE 0 END) AS q2_spend,
        SUM(CASE WHEN t.txn_date >= '2026-07-01' AND t.txn_date < '2026-10-01' THEN t.amount ELSE 0 END) AS q3_spend
    FROM accounts a
    JOIN transactions t ON a.account_id = t.account_id
    WHERE t.status = 'APPROVED' AND t.txn_type = 'DEBIT'
    GROUP BY a.cust_id
)
SELECT 
    cust_id,
    q2_spend,
    q3_spend,
    ROUND(((q3_spend - q2_spend) / q2_spend) * 100, 2) AS growth_pct
FROM QuarterlySpend
WHERE q2_spend >= 1000.00
  AND q3_spend >= 1.50 * q2_spend
ORDER BY growth_pct DESC;
```

---

#### Problem 14: Merchant Concentration per Customer
* **Task**: For each customer, determine the merchant where they spent the highest total dollar volume in 2026.
* **SQL Query**:
```sql
WITH MerchantSpend AS (
    SELECT 
        a.cust_id,
        t.merchant,
        SUM(t.amount) AS total_merchant_spend,
        DENSE_RANK() OVER (PARTITION BY a.cust_id ORDER BY SUM(t.amount) DESC) AS merchant_rnk
    FROM accounts a
    JOIN transactions t ON a.account_id = t.account_id
    WHERE t.status = 'APPROVED'
      AND t.txn_type = 'DEBIT'
      AND t.txn_date >= '2026-01-01' AND t.txn_date < '2027-01-01'
    GROUP BY a.cust_id, t.merchant
)
SELECT cust_id, merchant AS top_merchant, total_merchant_spend
FROM MerchantSpend
WHERE merchant_rnk = 1;
```

---

#### Problem 15: Accounts Approaching Credit Limit
* **Task**: Identify active credit cards where current balance exceeds $90\%$ of credit limit, but previous month's balance was below $70\%$ of credit limit.
* **SQL Query**:
```sql
WITH SnapHistory AS (
    SELECT 
        account_id,
        month_end,
        balance,
        LAG(balance) OVER (PARTITION BY account_id ORDER BY month_end) AS prev_balance
    FROM monthly_snapshots
)
SELECT 
    a.account_id,
    a.cust_id,
    a.credit_limit,
    s.month_end,
    s.balance AS curr_bal,
    s.prev_balance AS prev_bal,
    ROUND((s.balance / a.credit_limit) * 100, 2) AS curr_util_pct,
    ROUND((s.prev_balance / a.credit_limit) * 100, 2) AS prev_util_pct
FROM accounts a
JOIN SnapHistory s ON a.account_id = s.account_id
WHERE a.acct_type = 'CREDIT_CARD'
  AND a.status = 'ACTIVE'
  AND (s.balance / a.credit_limit) > 0.90
  AND (s.prev_balance / a.credit_limit) < 0.70;
```

---

### Part D: Ranking & Value Window Functions (Problems 16–20)

#### Problem 16: Top 3 Highest Transactions per Customer per Month
* **Task**: Return the top 3 highest approved debit transactions for each customer in each calendar month of 2026.
* **SQL Query**:
```sql
WITH RankedMonthlyTxns AS (
    SELECT 
        a.cust_id,
        DATE_TRUNC('month', t.txn_date) AS txn_month,
        t.txn_id,
        t.txn_date,
        t.amount,
        t.merchant,
        DENSE_RANK() OVER (
            PARTITION BY a.cust_id, DATE_TRUNC('month', t.txn_date) 
            ORDER BY t.amount DESC
        ) AS rank_in_month
    FROM accounts a
    JOIN transactions t ON a.account_id = t.account_id
    WHERE t.status = 'APPROVED'
      AND t.txn_type = 'DEBIT'
      AND t.txn_date >= '2026-01-01' AND t.txn_date < '2027-01-01'
)
SELECT cust_id, txn_month, txn_id, txn_date, amount, merchant
FROM RankedMonthlyTxns
WHERE rank_in_month <= 3
ORDER BY cust_id, txn_month, rank_in_month;
```

---

#### Problem 17: Decile Bucket Assignment (`NTILE`)
* **Task**: Assign all active savings accounts into 10 risk deciles based on closing balance as of 2026-09-30 (Decile 1 = lowest balance, Decile 10 = highest balance).
* **SQL Query**:
```sql
SELECT 
    a.account_id,
    a.cust_id,
    s.balance,
    NTILE(10) OVER (ORDER BY s.balance ASC) AS balance_decile
FROM accounts a
JOIN monthly_snapshots s ON a.account_id = s.account_id
WHERE a.acct_type = 'SAVINGS'
  AND a.status = 'ACTIVE'
  AND s.month_end = '2026-09-30'
ORDER BY balance_decile DESC, s.balance DESC;
```

---

#### Problem 18: Time Interval Between Successive Transactions
* **Task**: For customer 'C-1001', calculate the time difference in hours between each consecutive approved transaction.
* **SQL Query**:
```sql
SELECT 
    t.txn_id,
    t.txn_date,
    t.amount,
    t.merchant,
    LAG(t.txn_date) OVER (ORDER BY t.txn_date ASC) AS prev_txn_date,
    ROUND(
        EXTRACT(EPOCH FROM (t.txn_date - LAG(t.txn_date) OVER (ORDER BY t.txn_date ASC))) / 3600.0, 
        2
    ) AS hours_since_prior_txn
FROM accounts a
JOIN transactions t ON a.account_id = t.account_id
WHERE a.cust_id = 'C-1001'
  AND t.status = 'APPROVED'
ORDER BY t.txn_date ASC;
```

---

#### Problem 19: Accounts with 3 Consecutive Months of Balance Decline
* **Task**: Return all account IDs whose closing balance decreased for 3 consecutive months in 2026.
* **SQL Query**:
```sql
WITH BalanceTrends AS (
    SELECT 
        account_id,
        month_end,
        balance,
        LAG(balance, 1) OVER (PARTITION BY account_id ORDER BY month_end ASC) AS bal_lag1,
        LAG(balance, 2) OVER (PARTITION BY account_id ORDER BY month_end ASC) AS bal_lag2
    FROM monthly_snapshots
    WHERE month_end >= '2026-01-01' AND month_end <= '2026-09-30'
)
SELECT DISTINCT account_id
FROM BalanceTrends
WHERE balance < bal_lag1
  AND bal_lag1 < bal_lag2
ORDER BY account_id;
```

---

#### Problem 20: First and Most Recent Transaction per Account
* **Task**: For every account, return account ID, open date, first transaction date, and most recent transaction date using window functions.
* **SQL Query**:
```sql
SELECT DISTINCT 
    a.account_id,
    a.open_date,
    FIRST_VALUE(t.txn_date) OVER (
        PARTITION BY a.account_id 
        ORDER BY t.txn_date ASC 
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS first_txn_date,
    LAST_VALUE(t.txn_date) OVER (
        PARTITION BY a.account_id 
        ORDER BY t.txn_date ASC 
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS latest_txn_date
FROM accounts a
LEFT JOIN transactions t ON a.account_id = t.account_id;
```

---

### Part E: Cumulative & Rolling Calculations (Problems 21–25)

#### Problem 21: Rolling 30-Day Cumulative Spend
* **Task**: For each card account, compute the cumulative spend over the trailing 30 days for each transaction row.
* **SQL Query**:
```sql
SELECT 
    account_id,
    txn_id,
    txn_date,
    amount,
    SUM(amount) OVER (
        PARTITION BY account_id 
        ORDER BY txn_date ASC 
        RANGE BETWEEN INTERVAL '30 DAYS' PRECEDING AND CURRENT ROW
    ) AS rolling_30d_spend
FROM transactions
WHERE status = 'APPROVED'
ORDER BY account_id, txn_date;
```

---

#### Problem 22: Running Total Balance Ledger
* **Task**: Build a chronological ledger for checking account 'ACC-500' showing transaction date, amount, transaction type, and running account balance (starting from initial balance $0).
* **SQL Query**:
```sql
SELECT 
    txn_id,
    txn_date,
    txn_type,
    amount,
    SUM(CASE WHEN txn_type = 'CREDIT' THEN amount 
             WHEN txn_type = 'DEBIT' THEN -amount 
             ELSE 0 END) OVER (
        PARTITION BY account_id 
        ORDER BY txn_date ASC, txn_id ASC
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_balance
FROM transactions
WHERE account_id = 'ACC-500'
  AND status = 'APPROVED'
ORDER BY txn_date ASC;
```

---

#### Problem 23: 3-Month Moving Average of Card Spend
* **Task**: Calculate the 3-month moving average of total approved monthly credit card spend across all retail customers.
* **SQL Query**:
```sql
WITH MonthlySpend AS (
    SELECT 
        DATE_TRUNC('month', t.txn_date)::DATE AS spend_month,
        SUM(t.amount) AS total_spend
    FROM accounts a
    JOIN transactions t ON a.account_id = t.account_id
    WHERE a.acct_type = 'CREDIT_CARD'
      AND t.status = 'APPROVED'
      AND t.txn_type = 'DEBIT'
    GROUP BY DATE_TRUNC('month', t.txn_date)::DATE
)
SELECT 
    spend_month,
    total_spend,
    ROUND(
        AVG(total_spend) OVER (
            ORDER BY spend_month ASC 
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ), 
        2
    ) AS moving_avg_3m
FROM MonthlySpend
ORDER BY spend_month ASC;
```

---

#### Problem 24: Month-over-Month Growth Percentage
* **Task**: Compute total monthly portfolio collections (CREDIT) across all accounts, the prior month's collection, and percentage growth month-over-month.
* **SQL Query**:
```sql
WITH MonthlyCollections AS (
    SELECT 
        DATE_TRUNC('month', txn_date)::DATE AS col_month,
        SUM(amount) AS monthly_inflow
    FROM transactions
    WHERE txn_type = 'CREDIT'
      AND status = 'APPROVED'
    GROUP BY DATE_TRUNC('month', txn_date)::DATE
),
WithLag AS (
    SELECT 
        col_month,
        monthly_inflow,
        LAG(monthly_inflow) OVER (ORDER BY col_month ASC) AS prior_month_inflow
    FROM MonthlyCollections
)
SELECT 
    col_month,
    monthly_inflow,
    prior_month_inflow,
    ROUND(((monthly_inflow - prior_month_inflow) / NULLIF(prior_month_inflow, 0)) * 100, 2) AS mom_growth_pct
FROM WithLag
ORDER BY col_month ASC;
```

---

#### Problem 25: Year-to-Date (YTD) Fee Revenue per Customer
* **Task**: Calculate cumulative Year-to-Date fee revenue incurred by each customer for every fee transaction in 2026.
* **SQL Query**:
```sql
SELECT 
    a.cust_id,
    t.txn_id,
    t.txn_date,
    t.amount AS fee_amount,
    SUM(t.amount) OVER (
        PARTITION BY a.cust_id, EXTRACT(YEAR FROM t.txn_date)
        ORDER BY t.txn_date ASC
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS ytd_fee_total
FROM accounts a
JOIN transactions t ON a.account_id = t.account_id
WHERE t.txn_type = 'FEE'
  AND t.status = 'APPROVED'
  AND t.txn_date >= '2026-01-01' AND t.txn_date < '2027-01-01'
ORDER BY a.cust_id, t.txn_date ASC;
```

---

### Part F: Advanced Analytical & Anomaly Scenarios (Problems 26–30)

#### Problem 26: Real-Time Fraud Velocity Rule (Multiple Swipes $< 5$ Mins)
* **Task**: Detect all transactions where the same account had a prior transaction of $\ge \$500$ within the preceding 5 minutes.
* **SQL Query**:
```sql
WITH VelocityPrep AS (
    SELECT 
        txn_id,
        account_id,
        txn_date,
        amount,
        merchant,
        LAG(txn_date) OVER (PARTITION BY account_id ORDER BY txn_date ASC) AS prev_txn_date,
        LAG(amount) OVER (PARTITION BY account_id ORDER BY txn_date ASC) AS prev_amount
    FROM transactions
    WHERE status = 'APPROVED'
)
SELECT 
    txn_id,
    account_id,
    txn_date,
    amount,
    prev_txn_date,
    prev_amount,
    ROUND(EXTRACT(EPOCH FROM (txn_date - prev_txn_date)) / 60.0, 2) AS minutes_apart
FROM VelocityPrep
WHERE (txn_date - prev_txn_date) <= INTERVAL '5 MINUTES'
  AND amount >= 500.00
  AND prev_amount >= 500.00
ORDER BY account_id, txn_date;
```

---

#### Problem 27: Customer Monthly Churn Rate Calculation
* **Task**: Compute the monthly customer churn rate: percentage of active transacting customers in month $M$ who recorded zero transactions in month $M+1$.
* **SQL Query**:
```sql
WITH MonthlyActive AS (
    SELECT DISTINCT 
        a.cust_id,
        DATE_TRUNC('month', t.txn_date)::DATE AS active_month
    FROM accounts a
    JOIN transactions t ON a.account_id = t.account_id
    WHERE t.status = 'APPROVED'
),
ChurnAudit AS (
    SELECT 
        curr.active_month,
        COUNT(DISTINCT curr.cust_id) AS total_active_customers,
        COUNT(DISTINCT CASE WHEN next_m.cust_id IS NULL THEN curr.cust_id END) AS churned_customers
    FROM MonthlyActive curr
    LEFT JOIN MonthlyActive next_m 
        ON curr.cust_id = next_m.cust_id 
       AND next_m.active_month = (curr.active_month + INTERVAL '1 MONTH')::DATE
    GROUP BY curr.active_month
)
SELECT 
    active_month,
    total_active_customers,
    churned_customers,
    ROUND((churned_customers::DECIMAL / NULLIF(total_active_customers, 0)) * 100, 2) AS churn_rate_pct
FROM ChurnAudit
ORDER BY active_month ASC;
```

---

#### Problem 28: Customer Signup Cohort Retention (Month 1, 2, 3)
* **Task**: Group customers by their account opening cohort month, and track how many transacted in Month 1, Month 2, and Month 3 after opening.
* **SQL Query**:
```sql
WITH CohortBase AS (
    SELECT 
        cust_id,
        DATE_TRUNC('month', join_date)::DATE AS cohort_month
    FROM customers
),
UserActivityMonths AS (
    SELECT DISTINCT 
        a.cust_id,
        DATE_TRUNC('month', t.txn_date)::DATE AS activity_month
    FROM accounts a
    JOIN transactions t ON a.account_id = t.account_id
    WHERE t.status = 'APPROVED'
)
SELECT 
    c.cohort_month,
    COUNT(DISTINCT c.cust_id) AS cohort_size,
    COUNT(DISTINCT CASE WHEN u.activity_month = (c.cohort_month + INTERVAL '1 MONTH')::DATE THEN c.cust_id END) AS m1_active,
    COUNT(DISTINCT CASE WHEN u.activity_month = (c.cohort_month + INTERVAL '2 MONTH')::DATE THEN c.cust_id END) AS m2_active,
    COUNT(DISTINCT CASE WHEN u.activity_month = (c.cohort_month + INTERVAL '3 MONTH')::DATE THEN c.cust_id END) AS m3_active
FROM CohortBase c
LEFT JOIN UserActivityMonths u ON c.cust_id = u.cust_id
GROUP BY c.cohort_month
ORDER BY c.cohort_month;
```

---

#### Problem 29: Delinquency Roll-Rate Transition Matrix (Current to 30+ DPD)
* **Task**: From `monthly_snapshots`, count how many credit card accounts rolled from current ($\text{dpd} = 0$) in August 2026 to delinquent ($\text{dpd} \ge 30$) in September 2026.
* **SQL Query**:
```sql
SELECT 
    COUNT(a.account_id) AS total_aug_current_accounts,
    COUNT(CASE WHEN s_sept.dpd >= 30 THEN a.account_id END) AS rolled_to_delinquent,
    ROUND(
        (COUNT(CASE WHEN s_sept.dpd >= 30 THEN a.account_id END)::DECIMAL / NULLIF(COUNT(a.account_id), 0)) * 100, 
        2
    ) AS roll_rate_pct
FROM accounts a
JOIN monthly_snapshots s_aug 
    ON a.account_id = s_aug.account_id AND s_aug.month_end = '2026-08-31'
JOIN monthly_snapshots s_sept 
    ON a.account_id = s_sept.account_id AND s_sept.month_end = '2026-09-30'
WHERE a.acct_type = 'CREDIT_CARD'
  AND s_aug.dpd = 0;
```

---

#### Problem 30: Identifying Inactive Accounts with Positive Balance
* **Task**: Find all active deposit accounts (`SAVINGS` or `CHECKING`) that have recorded ZERO transactions in the last 180 days, but maintain a positive balance $> \$100$.
* **SQL Query**:
```sql
SELECT 
    a.account_id,
    a.cust_id,
    a.acct_type,
    s.balance AS latest_balance,
    MAX(t.txn_date) AS last_activity_date
FROM accounts a
JOIN monthly_snapshots s 
    ON a.account_id = s.account_id AND s.month_end = '2026-09-30'
LEFT JOIN transactions t 
    ON a.account_id = t.account_id AND t.status = 'APPROVED'
WHERE a.status = 'ACTIVE'
  AND a.acct_type IN ('SAVINGS', 'CHECKING')
  AND s.balance > 100.00
GROUP BY a.account_id, a.cust_id, a.acct_type, s.balance
HAVING MAX(t.txn_date) < '2026-09-30'::DATE - INTERVAL '180 DAYS' 
    OR MAX(t.txn_date) IS NULL
ORDER BY s.balance DESC;
```

---

## 8. Legacy Desktop Database Context: Microsoft Access

The job description explicitly mentions: *"tools (e.g. SQL, Access)"*.

### Where Microsoft Access Fits in Banking Analytics:
1. **Desktop Prototyping**: Regional analytics teams or business managers frequently export CSV/Excel slices from SQL data warehouses (Teradata, Oracle, Snowflake) into local Access databases (`.accdb`) to build rapid forms, local ad-hoc joins, and department queries.
2. **Access SQL Limitations to Know in Interviews**:
   * Access does NOT support standard window functions (`ROW_NUMBER`, `DENSE_RANK`, `LAG`, `LEAD`).
   * Multi-table joins in Access require nested parentheses: `FROM (TableA INNER JOIN TableB ON TableA.id = TableB.id) INNER JOIN TableC ON TableA.id = TableC.id`.
   * Date literals use `#` delimiters instead of quotes: `WHERE txn_date >= #01/01/2026#`.
   * Wildcards in Access GUI use `*` and `?` instead of ANSI SQL `%` and `_`.
