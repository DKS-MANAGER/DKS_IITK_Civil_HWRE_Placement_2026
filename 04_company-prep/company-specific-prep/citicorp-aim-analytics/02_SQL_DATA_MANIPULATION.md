# 02. SQL & Data Manipulation — Complete Study Material & Problem Bank

> **Target Role**: Spec Analytics Analyst — Business Analytics (SBS), Citi AIM  
> **Relevance**: Tested in OA Section 5 and tested live on a shared editor in Technical Interview Round 1.

---

## 1. SQL Logical Processing Order

In SQL, queries are evaluated in an exact sequence that differs fundamentally from how they are written:

```
[Written Order]                       [Logical Execution Order]
1. SELECT                              1. FROM & JOIN
2. FROM                                2. WHERE
3. JOIN ... ON                         3. GROUP BY
4. WHERE                               4. HAVING
5. GROUP BY                            5. SELECT (Expressions & Window Functions)
6. HAVING                              6. DISTINCT
7. ORDER BY                            7. ORDER BY
8. LIMIT / OFFSET                      8. LIMIT / OFFSET
```

> **Why this matters in interviews**:
> * You cannot use a column alias created in `SELECT` within a `WHERE` clause because `WHERE` runs before `SELECT`.
> * `HAVING` filters aggregated values post-`GROUP BY`. `WHERE` filters individual records before `GROUP BY`.

---

## 2. Joins & Handling NULLs

### 2.1 The 5 Fundamental Joins

```
   Table A                  Table B
 ┌───────────┐            ┌───────────┐
 │ id │ valA │            │ id │ valB │
 ├────┼──────┤            ├────┼──────┤
 │  1 │  100 │            │  1 │  999 │
 │  2 │  200 │            │  1 │  888 │
 │  3 │  300 │            │  2 │  777 │
 │NULL│  400 │            │  4 │  666 │
 └───────────┘            └───────────┘
```

1. **`INNER JOIN`**: Returns records with matching keys in both tables.
   * Key `1` produces 2 rows, Key `2` produces 1 row $\implies 3$ rows. Keys `3`, `4`, and `NULL` are omitted.
2. **`LEFT JOIN`**: Returns all rows from Table A, plus matched rows from Table B (unmatched filled with `NULL`).
   * Key `3` and Key `NULL` are included with `valB = NULL`.
3. **`RIGHT JOIN`**: Returns all rows from Table B, plus matched rows from Table A.
   * Key `4` is included with `valA = NULL`.
4. **`FULL OUTER JOIN`**: Returns all rows from both tables, filling `NULL` on either side where keys do not match.
5. **`CROSS JOIN`**: Cartesian product ($N \times M$ rows).

### 2.2 The SQL `NULL` Pitfall in Joins & Comparisons
* In SQL three-valued logic, `NULL = NULL` evaluates to **`UNKNOWN`** (falsy), **NOT TRUE**.
* Two records with `NULL` keys will **never match** in an equality join (`ON A.id = B.id`).
* `COUNT(*)` counts all rows including `NULL`s.
* `COUNT(column_name)` counts only non-NULL occurrences.
* `SUM(column_name)` ignores `NULL`s. If all rows are `NULL`, it returns `NULL`, not 0.

---

## 3. Window Functions: The #1 Tested Topic at Citi

A **Window Function** computes values over a specified set of rows (the "window") while **preserving the individual row identities**.

### 3.1 Syntax Structure
```sql
<function>() OVER (
    PARTITION BY <partition_column>
    ORDER BY <sort_column> [ASC | DESC]
    [ROWS | RANGE BETWEEN <start_frame> AND <end_frame>]
)
```

### 3.2 Ranking Functions Comparison

| Function | Data: `[500, 500, 300, 100]` | Behavior / Arbitration |
| :--- | :--- | :--- |
| **`ROW_NUMBER()`** | `1, 2, 3, 4` | Assigns sequential integers. Ties are arbitrated arbitrarily. |
| **`RANK()`** | `1, 1, 3, 4` | Ties share rank; **skips** subsequent ranks. |
| **`DENSE_RANK()`** | `1, 1, 2, 3` | Ties share rank; **does NOT skip** subsequent ranks. |

> **Citi Rule**: When asked to find the "$N$-th highest" value (e.g., 2nd largest transaction or 3rd top customer), **always use `DENSE_RANK()`** inside a CTE.

### 3.3 Value Window Functions
* **`LAG(col, offset, default)`**: Returns value from $N$ rows prior in the window. Used for month-over-month growth, velocity detection, and consecutive declines.
* **`LEAD(col, offset, default)`**: Returns value from $N$ rows subsequent in the window.
* **`FIRST_VALUE(col)` / `LAST_VALUE(col)`**: Returns initial or final value in the frame.

### 3.4 Running & Cumulative Totals
```sql
-- Running cumulative total per account
SUM(txn_amount) OVER (
    PARTITION BY account_id 
    ORDER BY txn_date 
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
)
```

---

## 4. Common Table Expressions (CTEs) vs Subqueries

```sql
-- Production Structured Pattern using CTE
WITH CustomerSpend AS (
    SELECT 
        cust_id,
        DATE_TRUNC('month', txn_date) AS txn_month,
        SUM(amount) AS total_spend
    FROM transactions
    WHERE txn_status = 'APPROVED'
    GROUP BY cust_id, DATE_TRUNC('month', txn_date)
),
RankedSpenders AS (
    SELECT 
        cust_id,
        txn_month,
        total_spend,
        DENSE_RANK() OVER (PARTITION BY txn_month ORDER BY total_spend DESC) AS rnk
    FROM CustomerSpend
)
SELECT cust_id, txn_month, total_spend
FROM RankedSpenders
WHERE rnk <= 3;
```
* **Advantages**: Far more readable than nested subqueries; query planner optimizes CTE execution plans; allows recursive queries (`WITH RECURSIVE`).

---

## 5. 10 Production Banking SQL Problems (Fully Solved)

### Problem 1: Top 2 Highest Transactions per Customer per Month
**Schema**: `transactions (txn_id, cust_id, txn_date, txn_amount, txn_status)`  
**Question**: Write a query to find the top 2 highest approved transactions for each customer in each calendar month.  
**Query**:
```sql
WITH RankedTxn AS (
    SELECT 
        cust_id,
        txn_id,
        txn_date,
        txn_amount,
        DENSE_RANK() OVER (
            PARTITION BY cust_id, EXTRACT(YEAR FROM txn_date), EXTRACT(MONTH FROM txn_date)
            ORDER BY txn_amount DESC
        ) AS rnk
    FROM transactions
    WHERE txn_status = 'APPROVED'
)
SELECT cust_id, txn_id, txn_date, txn_amount
FROM RankedTxn
WHERE rnk <= 2
ORDER BY cust_id, txn_date;
```

---

### Problem 2: Rolling 30-Day Cumulative Spending per Credit Card
**Schema**: `card_txns (card_id, txn_date, txn_amount)`  
**Question**: For every transaction, calculate the cumulative rolling sum of expenditures over the trailing 30 days for that card.  
**Query**:
```sql
SELECT 
    card_id,
    txn_date,
    txn_amount,
    SUM(txn_amount) OVER (
        PARTITION BY card_id 
        ORDER BY txn_date 
        RANGE BETWEEN INTERVAL '30 DAYS' PRECEDING AND CURRENT ROW
    ) AS rolling_30d_spend
FROM card_txns
ORDER BY card_id, txn_date;
```

---

### Problem 3: Identify Customers with 3 Consecutive Months of Balance Decline
**Schema**: `monthly_balances (cust_id, balance_date, closing_balance)`  
**Question**: Return all customer IDs whose closing deposit balance decreased for 3 consecutive months (an attrition risk signal).  
**Query**:
```sql
WITH PriorBalances AS (
    SELECT 
        cust_id,
        balance_date,
        closing_balance,
        LAG(closing_balance, 1) OVER (PARTITION BY cust_id ORDER BY balance_date) AS bal_m1,
        LAG(closing_balance, 2) OVER (PARTITION BY cust_id ORDER BY balance_date) AS bal_m2
    FROM monthly_balances
)
SELECT DISTINCT cust_id
FROM PriorBalances
WHERE closing_balance < bal_m1 
  AND bal_m1 < bal_m2;
```

---

### Problem 4: Fraud Velocity Rule (Multiple Large Swipes within 5 Minutes)
**Schema**: `auth_logs (auth_id, card_id, swipe_time, amount, merchant)`  
**Question**: Detect all transactions where the same credit card had a prior transaction of $\ge \$500$ within the preceding 5 minutes.  
**Query**:
```sql
WITH VelocityCheck AS (
    SELECT 
        auth_id,
        card_id,
        swipe_time,
        amount,
        LAG(swipe_time) OVER (PARTITION BY card_id ORDER BY swipe_time) AS prev_time,
        LAG(amount) OVER (PARTITION BY card_id ORDER BY swipe_time) AS prev_amount
    FROM auth_logs
)
SELECT 
    auth_id,
    card_id,
    swipe_time,
    amount,
    prev_time,
    prev_amount,
    ROUND(EXTRACT(EPOCH FROM (swipe_time - prev_time)) / 60, 2) AS minutes_apart
FROM VelocityCheck
WHERE (swipe_time - prev_time) <= INTERVAL '5 MINUTES'
  AND amount >= 500
  AND prev_amount >= 500;
```

---

### Problem 5: Monthly Customer Churn Rate Calculation
**Schema**: `transactions (cust_id, txn_date, amount)`  
**Question**: For each calendar month, calculate the number of active transacting customers, the number who churned (no transactions next month), and the churn percentage.  
**Query**:
```sql
WITH MonthlyActivity AS (
    SELECT DISTINCT 
        cust_id,
        DATE_TRUNC('month', txn_date) AS active_month
    FROM transactions
),
ChurnComparison AS (
    SELECT 
        curr.active_month,
        COUNT(DISTINCT curr.cust_id) AS total_active,
        COUNT(DISTINCT CASE WHEN next_m.cust_id IS NULL THEN curr.cust_id END) AS churned
    FROM MonthlyActivity curr
    LEFT JOIN MonthlyActivity next_m 
        ON curr.cust_id = next_m.cust_id 
       AND next_m.active_month = curr.active_month + INTERVAL '1 MONTH'
    GROUP BY curr.active_month
)
SELECT 
    active_month,
    total_active,
    churned,
    ROUND((churned::DECIMAL / total_active) * 100, 2) AS churn_rate_pct
FROM ChurnComparison
ORDER BY active_month;
```

---

### Problem 6: Classify Credit Card Customers as "Transactors" vs "Revolvers"
**Schema**: `statements (card_id, cycle_date, statement_balance, payment_received)`  
**Business Context**:
* *Transactor*: Pays $100\%$ of statement balance every cycle (zero interest revenue, low credit risk).
* *Revolver*: Carries a balance forward ($0 < \text{payment} < \text{statement\_balance}$, highly profitable via interest fees, moderate risk).
* *Delinquent*: Pays zero or less than minimum payment.  
**Query**:
```sql
SELECT 
    card_id,
    cycle_date,
    statement_balance,
    payment_received,
    CASE 
        WHEN payment_received >= statement_balance THEN 'Transactor'
        WHEN payment_received > 0 AND payment_received < statement_balance THEN 'Revolver'
        ELSE 'Delinquent'
    END AS customer_profile
FROM statements;
```

---

### Problem 7: Month-over-Month (MoM) Loan Repayment Growth Rate
**Schema**: `loan_payments (payment_id, payment_date, amount)`  
**Question**: Calculate total loan repayments per calendar month, the prior month's repayment, and the percentage MoM growth.  
**Query**:
```sql
WITH MonthlyCollections AS (
    SELECT 
        DATE_TRUNC('month', payment_date) AS pay_month,
        SUM(amount) AS total_repaid
    FROM loan_payments
    GROUP BY DATE_TRUNC('month', payment_date)
),
MoMCalculations AS (
    SELECT 
        pay_month,
        total_repaid,
        LAG(total_repaid) OVER (ORDER BY pay_month) AS prev_month_repaid
    FROM MonthlyCollections
)
SELECT 
    pay_month,
    total_repaid,
    prev_month_repaid,
    ROUND(((total_repaid - prev_month_repaid)::DECIMAL / prev_month_repaid) * 100, 2) AS mom_growth_pct
FROM MoMCalculations
ORDER BY pay_month;
```

---

### Problem 8: Identify Inactive Credit Cards (Zero Spend in Trailing 90 Days)
**Schema**: `cards (card_id, cust_id, issue_date, status)` and `card_txns (txn_id, card_id, txn_date, amount)`  
**Question**: Find all active cards that have recorded zero transactions in the last 90 days.  
**Query**:
```sql
SELECT 
    c.card_id,
    c.cust_id,
    MAX(t.txn_date) AS last_txn_date
FROM cards c
LEFT JOIN card_txns t ON c.card_id = t.card_id
WHERE c.status = 'ACTIVE'
GROUP BY c.card_id, c.cust_id
HAVING MAX(t.txn_date) < CURRENT_DATE - INTERVAL '90 DAYS' 
    OR MAX(t.txn_date) IS NULL;
```

---

### Problem 9: Customer Lifetime Value (CLV) & Revenue Tier Segmentation
**Schema**: `customers (cust_id, name)` and `transactions (cust_id, txn_date, fee_revenue)`  
**Question**: Compute each customer's total fee revenue generated. Segment customers into Tiers:
* Tier 1 (Platinum): Total Fee Revenue $\ge \$1,000$
* Tier 2 (Gold): Total Fee Revenue between $\$500$ and $\$999.99$
* Tier 3 (Silver): Total Fee Revenue $< \$500$  
**Query**:
```sql
WITH CustomerRevenue AS (
    SELECT 
        c.cust_id,
        c.name,
        COALESCE(SUM(t.fee_revenue), 0) AS total_fee_rev
    FROM customers c
    LEFT JOIN transactions t ON c.cust_id = t.cust_id
    GROUP BY c.cust_id, c.name
)
SELECT 
    cust_id,
    name,
    total_fee_rev,
    CASE 
        WHEN total_fee_rev >= 1000 THEN 'Platinum'
        WHEN total_fee_rev >= 500 THEN 'Gold'
        ELSE 'Silver'
    END AS customer_tier
FROM CustomerRevenue
ORDER BY total_fee_rev DESC;
```

---

### Problem 10: Cohort Retention by Signup Month
**Schema**: `users (user_id, signup_date)` and `user_logins (user_id, login_date)`  
**Question**: Group users into signup monthly cohorts, and find the percentage of users from each cohort who logged in during Month 1 (the following calendar month).  
**Query**:
```sql
WITH Cohorts AS (
    SELECT 
        user_id,
        DATE_TRUNC('month', signup_date) AS signup_cohort
    FROM users
),
Month1Activity AS (
    SELECT DISTINCT 
        c.signup_cohort,
        c.user_id,
        CASE WHEN l.user_id IS NOT NULL THEN 1 ELSE 0 END AS retained_m1
    FROM Cohorts c
    LEFT JOIN user_logins l 
        ON c.user_id = l.user_id 
       AND DATE_TRUNC('month', l.login_date) = c.signup_cohort + INTERVAL '1 MONTH'
)
SELECT 
    signup_cohort,
    COUNT(DISTINCT user_id) AS cohort_size,
    SUM(retained_m1) AS retained_m1_count,
    ROUND((SUM(retained_m1)::DECIMAL / COUNT(DISTINCT user_id)) * 100, 2) AS m1_retention_rate_pct
FROM Month1Activity
GROUP BY signup_cohort
ORDER BY signup_cohort;
```
