# 12. Analytics: Full Timed Placement Mock Assessment

> Full 90-minute timed mock assessment simulating real campus selection tests for Analytics and Decision Science profiles (Fractal, EXL, Flipkart, American Express).

---

## ⏱️ Assessment Structure
- **Section 1: Quantitative Aptitude & Probability** (15 Questions, 25 Mins)
- **Section 2: Data Interpretation & Charts** (10 Questions, 20 Mins)
- **Section 3: SQL Live Querying** (3 Problems, 25 Mins)
- **Section 4: Product Analytics Caselet** (1 Problem, 20 Mins)

---

## Section 1: Quantitative Aptitude & Probability

1. An e-commerce A/B test has a baseline conversion of 5%. What sample size is needed per variant to detect an absolute lift of 0.5% at 95% confidence and 80% power?
   - *Solution*: $N pprox rac{16 \cdot p(1-p)}{\Delta^2} = rac{16 \cdot 0.05 \cdot 0.95}{(0.005)^2} = rac{0.76}{0.000025} = \mathbf{30,400	ext{ users per variant}}$.

2. A taxi-hailing app receives cancellation events following a Poisson process with $\lambda = 6$ per hour. What is the probability of observing exactly 2 cancellations in a 20-minute window?
   - *Solution*: $\mu = 6 	imes rac{20}{60} = 2$. $P(X=2) = rac{e^{-2} \cdot 2^2}{2!} = 2 e^{-2} pprox \mathbf{27.06\%}$.

---

## Section 2: Data Interpretation

**Exhibit**: 4-Stage User Funnel Across Platforms
| Stage | iOS Users | Android Users | Web Users |
|:---|:---:|:---:|:---:|
| 1. Landing Page | 50,000 | 120,000 | 80,000 |
| 2. Product Search | 40,000 | 90,000 | 48,000 |
| 3. Add to Cart | 16,000 | 27,000 | 9,600 |
| 4. Completed Checkout | 8,000 | 8,100 | 2,880 |

**Question**: Which platform has the highest overall conversion efficiency from Landing Page to Checkout?
- *Solution*:
  - iOS: $rac{8,000}{50,000} = \mathbf{16.0\%}$
  - Android: $rac{8,100}{120,000} = 6.75\%$
  - Web: $rac{2,880}{80,000} = 3.6\%$
  - **iOS** is by far the highest converting platform ($16\%$).

---

## Section 3: SQL Live Querying

**Problem**: Given `UserPurchases(user_id, purchase_date, amount)`:
Write a query to calculate the cumulative lifetime spend for each user, and flag whether their latest purchase was above their average historical purchase amount.

```sql
WITH UserMetrics AS (
    SELECT 
        user_id,
        purchase_date,
        amount,
        SUM(amount) OVER (PARTITION BY user_id ORDER BY purchase_date) as cumulative_spend,
        AVG(amount) OVER (PARTITION BY user_id) as avg_spend,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY purchase_date DESC) as rnk
    FROM UserPurchases
)
SELECT 
    user_id,
    purchase_date as latest_purchase_date,
    amount as latest_amount,
    cumulative_spend,
    avg_spend,
    CASE WHEN amount > avg_spend THEN 1 ELSE 0 END AS is_above_average
FROM UserMetrics
WHERE rnk = 1;
```

---

## Section 4: Product Analytics Caselet

**Problem**: A food delivery app noticed that weekly search-to-cart conversion dropped from 22% to 16% in Delhi NCR over the last 10 days.
1. Outline a MECE mathematical decomposition to isolate the drop.
2. State 3 distinct hypotheses and the SQL data queries you would run to validate each.

---

## 📊 Objective Scoring Rubric
- **Score $\ge 85\%$**: Placement Offer Ready (Tier 1 Analytics / Tech Firms).
- **Score $70\% - 84\%$**: Strong Technical Foundation; polish speed SQL and case structuring.
- **Score $< 70\%$**: Revise [04_tools-and-technical-stack.md](04_tools-and-technical-stack.md) and repeat mock assessment.
