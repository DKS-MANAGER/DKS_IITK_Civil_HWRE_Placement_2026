# 12. Business Analyst: Full Timed Placement Mock Assessment

> Full 90-minute timed mock assessment simulating real campus selection tests for Business Analyst profiles (Deloitte, EXL, Flipkart, Capital One).

---

## ⏱️ Assessment Structure
- **Section 1: Quantitative & Logical Aptitude** (20 Questions, 30 Mins)
- **Section 2: Data Interpretation & Charts** (10 Questions, 20 Mins)
- **Section 3: SQL Live Querying** (4 Problems, 25 Mins)
- **Section 4: Business Metric Caselet** (1 Problem, 15 Mins)

---

## Section 1: Quantitative Aptitude (Sample Problems)

1. A retailer marks up cost price by 40% and offers a 15% discount. If payment gateway fee is 2% of selling price, calculate net profit margin on cost.
   - *Solution*: $	ext{CP} = 100 \implies 	ext{MP} = 140 \implies 	ext{SP} = 140 	imes 0.85 = 119$. Gateway fee = $119 	imes 0.02 = 2.38$. Net Profit = $119 - 2.38 - 100 = 16.62\%$.

2. A machine produces 5% defective items. If a batch of 3 items is inspected at random, what is the probability that at least 1 item is defective?
   - *Solution*: $1 - P(	ext{No defects}) = 1 - (0.95)^3 = 1 - 0.857375 = \mathbf{14.26\%}$.

---

## Section 2: Data Interpretation

**Exhibit**: 4-Stage E-Commerce Funnel Data
| Stage | Users | Step Conversion | Drop-off |
|:---|:---:|:---:|:---:|
| 1. Home Page | 100,000 | - | - |
| 2. Product Search | 60,000 | 60% | 40% |
| 3. Add to Cart | 18,000 | 30% | 70% |
| 4. Completed Checkout | 7,200 | 40% | 60% |

**Question**: Which stage represents the largest absolute loss of prospective customers?
- *Solution*: Home $ightarrow$ Product Search lost 40,000 users; Search $ightarrow$ Cart lost 42,000 users; Cart $ightarrow$ Checkout lost 10,800 users. **Search to Cart** represents the largest leak (42,000 users).

---

## Section 3: SQL Live Querying

**Problem**: Given `UserPurchases(user_id, purchase_date, amount)`:
Write a query to find all users whose total purchase amount in the last 30 days is greater than their total purchase amount in the preceding 30-day window (Day 31 to Day 60).

```sql
WITH WindowedPurchases AS (
    SELECT 
        user_id,
        SUM(CASE WHEN purchase_date >= CURRENT_DATE - INTERVAL '30 days' THEN amount ELSE 0 END) as rev_last_30d,
        SUM(CASE WHEN purchase_date >= CURRENT_DATE - INTERVAL '60 days' AND purchase_date < CURRENT_DATE - INTERVAL '30 days' THEN amount ELSE 0 END) as rev_prev_30d
    FROM UserPurchases
    WHERE purchase_date >= CURRENT_DATE - INTERVAL '60 days'
    GROUP BY user_id
)
SELECT user_id, rev_last_30d, rev_prev_30d
FROM WindowedPurchases
WHERE rev_last_30d > rev_prev_30d;
```

---

## Section 4: Business Caselet

**Problem**: A subscription fitness app noticed that 30-day churn rose from 6% to 11% among users who joined via a "50% Off First Month" promo campaign.
1. Formulate 2 distinct hypotheses.
2. Outline 3 data cuts you would query in SQL to validate them.

---

## 📊 Objective Scoring Rubric
- **Score $\ge 85\%$**: Placement Offer Ready (Tier 1 Companies).
- **Score $70\% - 84\%$**: Technical Ready; polish speed arithmetic and case structuring.
- **Score $< 70\%$**: Revise [04_data-and-analytics/sql-practice.md](04_data-and-analytics/sql-practice.md) and repeat mock assessment.
