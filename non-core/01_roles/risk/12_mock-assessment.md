# 12. Risk Analyst: Full Timed Placement Mock Assessment

> Full 90-minute timed mock assessment simulating real campus selection tests for Risk Analyst profiles (American Express, Capital One, Goldman Sachs Risk, Nomura).

---

## ⏱️ Assessment Structure
- **Section 1: Probability & Quantitative Aptitude** (15 Questions, 25 Mins)
- **Section 2: Credit & Market Risk Concepts** (10 Questions, 25 Mins)
- **Section 3: SQL Portfolio Querying** (3 Problems, 20 Mins)
- **Section 4: Risk Case Problem** (1 Case, 20 Mins)

---

## Section 1: Probability & Quantitative Aptitude

1. An account has a 4% probability of default. If defaulted, a fraud flag is raised with 85% probability. If non-defaulted, a fraud flag is falsely raised with 5% probability. If a fraud flag is raised, what is the probability the account defaults?
   - *Solution*: $P(D) = 0.04, P(F \mid D) = 0.85, P(F \mid D^c) = 0.05$.
   - $P(F) = (0.04 	imes 0.85) + (0.96 	imes 0.05) = 0.034 + 0.048 = 0.082$.
   - $P(D \mid F) = rac{0.034}{0.082} = \mathbf{41.46\%}$.

2. A trading portfolio has annual volatility $\sigma = 24\%$. Assuming 256 trading days, what is the 10-day 95% Parametric VaR on a 100 Cr INR portfolio ($Z_{95\%} = 1.645$)?
   - *Solution*: $\sigma_{	ext{daily}} = rac{24\%}{16} = 1.5\%$.
   - $	ext{VaR}_{1	ext{d}} = 1.645 	imes 0.015 	imes 100	ext{ Cr} = 2.4675	ext{ Cr INR}$.
   - $	ext{VaR}_{10	ext{d}} = 2.4675 	imes \sqrt{10} = 2.4675 	imes 3.1623 = \mathbf{7.80	ext{ Cr INR}}$.

---

## Section 2: Credit & Market Risk Concepts

3. A bank holds 50 Cr INR in drawn loans and 20 Cr INR in undrawn credit lines (CCF = 40%). If 1-year PD is 3% and historical recovery rate is 60%, calculate the 1-year Expected Loss ($EL$).
   - *Solution*: $EAD = 50 + (0.40 	imes 20) = 58	ext{ Cr INR}$.
   - $LGD = 1 - 0.60 = 0.40$.
   - $EL = 0.03 	imes 0.40 	imes 58	ext{ Cr} = \mathbf{0.696	ext{ Cr INR} = 69.6	ext{ Lakh INR}}$.

---

## Section 3: SQL Live Querying

**Problem**: Given `LoanRepayments(account_id, due_date, payment_date, amount_due, amount_paid)`:
Write a query to identify all accounts that have been delinquent for $\ge 3$ consecutive monthly billing cycles.

```sql
WITH PaymentFlags AS (
    SELECT 
        account_id,
        due_date,
        CASE WHEN payment_date > due_date OR payment_date IS NULL THEN 1 ELSE 0 END AS is_delinquent
    FROM LoanRepayments
),
DelinquencyStreaks AS (
    SELECT 
        account_id,
        due_date,
        is_delinquent,
        SUM(is_delinquent) OVER (
            PARTITION BY account_id 
            ORDER BY due_date 
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ) AS trailing_3m_delinquencies
    FROM PaymentFlags
)
SELECT DISTINCT account_id
FROM DelinquencyStreaks
WHERE trailing_3m_delinquencies = 3;
```

---

## Section 4: Risk Business Case

**Problem**: A consumer fintech noticed that lowering credit score cutoffs from 720 to 680 increased loan originations by 40 Cr INR (generating 6 Cr INR in interest income), but 90-day default rates on the incremental cohort reached 12% (LGD = 70%).
1. Calculate incremental net economic profit/loss.
2. Recommend 2 dynamic risk mitigation mechanisms without fully reverting the score cutoff.

- *Solution*:
  - Incremental Revenue = $+6	ext{ Cr INR}$.
  - Incremental Credit Loss = $40	ext{ Cr} 	imes 12\% 	imes 70\% = 40 	imes 0.084 = \mathbf{3.36	ext{ Cr INR}}$.
  - Net Profit Contribution = $6 - 3.36 = +\mathbf{2.64	ext{ Cr INR}}$ (Profitable).
  - Mitigation: 1. Offer smaller initial credit limits (e.g. 25,000 INR instead of 100,000 INR) with step-up increases on clean 6-month repayment. 2. Implement mandatory auto-debit (eNACH) for sub-700 accounts.

---

## 📊 Objective Scoring Rubric
- **Score $\ge 85\%$**: Placement Offer Ready (Tier 1 Global Banks & Risk Strategy).
- **Score $70\% - 84\%$**: Strong Technical Foundation; polish speed probability and SQL.
- **Score $< 70\%$**: Revise [03_domain-knowledge.md](03_domain-knowledge.md) and repeat mock assessment.
