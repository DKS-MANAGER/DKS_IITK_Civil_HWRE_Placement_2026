# 12. Product Analytics: Comprehensive Technical Mock Assessment

> **Exam Focus**: Experimentation Design, A/B Testing Statistics, Product SQL & Telemetry Analytics  
> **Target Audience**: IIT Kanpur candidates preparing for Product Analyst, Experimentation Scientist, and Growth Analytics assessments.  
> **Duration**: 60 Minutes  
> **Total Marks**: 50 Marks (+2 for correct MCQ, -0.66 for incorrect; Full stepwise credit for analytical derivations and SQL queries).  
> **Calculators**: Scientific calculator permitted.

---

## Section A: Conceptual & Quantitative Analytics MCQs (10 Marks)

### Q1. Sample Ratio Mismatch (SRM) Significance
An A/B test configured for a $50:50$ traffic allocation records $98,000$ users in Control and $102,000$ users in Treatment across a 2-week run ($N = 200,000$). What is the Chi-Square test statistic ($\chi^2$) for Sample Ratio Mismatch?
- **(a)** $4.00$
- **(b)** $8.00$
- **(c)** $16.00$
- **(d)** $40.00$

### Q2. Statistical Power and Errors in Experimentation
In product A/B testing, a Type II error ($\beta$) occurs when:
- **(a)** The analyst concludes there is a difference when no true difference exists (false positive).
- **(b)** The analyst concludes there is no difference when a true difference actually exists (false negative).
- **(c)** The test sample size is smaller than 10,000 users.
- **(d)** Two variants have different sample sizes.

### Q3. DAU/MAU Ratio ("Stickiness")
A social audio platform reports $3,60,000\text{ Monthly Active Users (MAU)}$ and an average of $90,000\text{ Daily Active Users (DAU)}$. What is the DAU/MAU ratio, and what does it indicate?
- **(a)** $25\%$; on average, an active user opens the app approximately 7.5 days per month.
- **(b)** $40\%$; the app is considered hyper-sticky.
- **(c)** $12.5\%$; severe user churn is imminent.
- **(d)** $30\%$; an active user opens the app every 3 days.

### Q4. Variance Reduction via CUPED
If the correlation between users' pre-experiment metric values ($X$) and post-experiment metric values ($Y$) is $\rho = 0.60$, by what percentage does applying CUPED reduce the metric variance?
- **(a)** $36\%$
- **(b)** $40\%$
- **(c)** $60\%$
- **(d)** $64\%$

### Q5. Client vs. Server-Side Telemetry Accuracy
Which event in an e-commerce marketplace should **NEVER** rely exclusively on client-side JavaScript/mobile tracking?
- **(a)** `product_card_scrolled_into_view`
- **(b)** `search_bar_focused`
- **(c)** `user_order_payment_settled`
- **(d)** `image_carousel_swiped`

---

## Section B: Analytical A/B Test Sample Size Derivation (15 Marks)

### Problem 6: Calculating Minimum Test Duration
An e-commerce checkout page has a baseline conversion rate of $p = 8.0\%$ ($0.080$). 
The growth team designs a streamlined one-page checkout and wants to detect an absolute Minimum Detectable Effect (MDE) of $\delta = 0.8\%$ ($0.008$, i.e., conversion rising from $8.0\%$ to $8.8\%$).
- Significance level: $\alpha = 0.05$ (two-tailed, $Z_{\alpha/2} = 1.960$).
- Statistical power: $1 - \beta = 0.80$ ($Z_{\beta} = 0.842$).
- Average daily traffic arriving at the checkout page: $15,000\text{ unique visitors/day}$.
- Traffic split: $50\%$ Control, $50\%$ Treatment.

#### Tasks:
1. Calculate the required sample size ($n$) per variant.
2. Determine the total sample size ($2n$) across both variants.
3. Calculate the minimum number of days the experiment must run to achieve sufficient statistical power.
4. If business stakeholders demand finishing the test in half the time, by what factor must the MDE ($\delta$) increase?

---

## Section C: Product Analytics SQL Querying (15 Marks)

### Problem 7: Multi-Day Retention Cohort Matrix
You are provided a PostgreSQL event table `user_activity_log` with the following schema:
- `user_id` (VARCHAR): Unique identifier for the registered user.
- `activity_date` (DATE): Date of user session.
- `signup_date` (DATE): Date the user created their account.

#### Candidate Task:
Write a clean, optimized SQL query to calculate the **Day 1, Day 7, and Day 30 retention rates** for each daily signup cohort that registered between `'2026-09-01'` and `'2026-09-07'`.
The query must output:
`signup_date`, `cohort_size`, `day_1_retention_pct`, `day_7_retention_pct`, `day_30_retention_pct`.

---

## Section D: Metric Trees & Product Guardrails (10 Marks)

### Scenario: Airbnb Instant Booking Trade-off
Airbnb considers making "Instant Book" mandatory for all hosts (eliminating the host's ability to review guest profiles before accepting a reservation).
1. Define the North Star metric for this feature launch.
2. Identify two primary input metrics that will drive this North Star metric.
3. Define two critical guardrail metrics that must not degrade, and explain why.

---

# Comprehensive Solutions, SQL & Scoring Rubric

---

### Solution Q1: Sample Ratio Mismatch (SRM)
- **Correct Option: (d)** $40.00$
- **Calculation**:
  - $N = 200,000 \implies E = 100,000$ per variant.
  - $O_{\text{control}} = 98,000$, $O_{\text{treatment}} = 102,000$.
  - $|O - E| = 2,000$.
  $$\chi^2 = \frac{(98,000 - 100,000)^2}{100,000} + \frac{(102,000 - 100,000)^2}{100,000} = \frac{(-2,000)^2}{100,000} + \frac{(2,000)^2}{100,000} = \frac{4,000,000}{100,000} + \frac{4,000,000}{100,000} = 20 + 20 = \mathbf{40.00}$$
- **Distractor Analysis**:
  - *(a) is wrong*: Arithmetic scaling error dividing by $1,000,000$.

---

### Solution Q2: Statistical Errors
- **Correct Option: (b)** Concluding no difference when a true difference exists (false negative).

---

### Solution Q3: DAU/MAU Ratio
- **Correct Option: (a)** $25\%$; approximately 7.5 days per month.
- **Calculation**: $\frac{90,000}{360,000} \times 100\% = \mathbf{25\%}$. Over 30 days, $25\% \times 30 = \mathbf{7.5 \text{ active days/month}}$.

---

### Solution Q4: CUPED Variance Reduction
- **Correct Option: (a)** $36\%$
- **Calculation**: Variance reduction $= \rho^2 = (0.60)^2 = 0.36 = \mathbf{36\%}$. Remaining variance $= 1 - \rho^2 = 64\%$.

---

### Solution Q5: Telemetry Reliability
- **Correct Option: (c)** Financial settlement must be tracked server-side to guarantee 100% accounting fidelity.

---

### Solution Problem 6: A/B Test Sample Size Derivation
1. **Sample Size per Variant ($n$)**:
   $$n = \frac{2 (Z_{\alpha/2} + Z_\beta)^2 \cdot p(1 - p)}{\delta^2}$$
   - $Z_{\alpha/2} + Z_\beta = 1.960 + 0.842 = 2.802 \implies (2.802)^2 \approx 7.8512$.
   - $p(1 - p) = 0.080 \times (1 - 0.080) = 0.080 \times 0.920 = 0.0736$.
   - $\delta^2 = (0.008)^2 = 0.000064$.
   $$n = \frac{2 \times 7.8512 \times 0.0736}{0.000064} = \frac{1.1557}{0.000064} \approx \mathbf{18,058 \text{ users per variant}}$$
2. **Total Sample Size**: $2n = 2 \times 18,058 = \mathbf{36,116 \text{ users}}$.
3. **Required Duration**:
   $$\text{Days} = \frac{36,116 \text{ total users}}{15,000 \text{ visitors/day}} = 2.41 \text{ days} \implies \mathbf{7 \text{ days minimum}}$$
   *(Note: Even though $2.41$ days provides statistical numbers, experiments must always run for at least 7 full days to account for day-of-week seasonality).*
4. **Halving Test Duration**:
   - Sample size scales as $n \propto 1/\delta^2 \implies \delta \propto 1/\sqrt{n}$.
   - To achieve statistical significance with half the sample size ($n/2$), the MDE must increase by a factor of $\sqrt{2} \approx \mathbf{1.414}$ (from $0.8\%$ to $1.13\%$).

---

### Solution Problem 7: SQL Cohort Retention Query

```sql
WITH cohort_users AS (
    SELECT 
        user_id,
        signup_date
    FROM user_activity_log
    WHERE signup_date BETWEEN '2026-09-01' AND '2026-09-07'
    GROUP BY user_id, signup_date
),
activity_deltas AS (
    SELECT 
        c.signup_date,
        c.user_id,
        (a.activity_date - c.signup_date) AS day_diff
    FROM cohort_users c
    INNER JOIN user_activity_log a 
        ON c.user_id = a.user_id
    WHERE a.activity_date >= c.signup_date
)
SELECT 
    signup_date,
    COUNT(DISTINCT user_id) AS cohort_size,
    ROUND(100.0 * COUNT(DISTINCT CASE WHEN day_diff = 1 THEN user_id END) / COUNT(DISTINCT user_id), 2) AS day_1_retention_pct,
    ROUND(100.0 * COUNT(DISTINCT CASE WHEN day_diff = 7 THEN user_id END) / COUNT(DISTINCT user_id), 2) AS day_7_retention_pct,
    ROUND(100.0 * COUNT(DISTINCT CASE WHEN day_diff = 30 THEN user_id END) / COUNT(DISTINCT user_id), 2) AS day_30_retention_pct
FROM activity_deltas
GROUP BY signup_date
ORDER BY signup_date ASC;
```

---

### Solution Section D: Metric Trees & Guardrails
1. **North Star Metric**: Total Booked Nights per Month.
2. **Input Metrics**:
   - Booking Funnel Conversion Rate (Search to Confirmed Booking).
   - Time-to-Confirmation (dropping from hours to instantaneous seconds).
3. **Guardrail Metrics**:
   - *Host Cancellation Rate*: Hosts may cancel after auto-booking if they dislike the guest. Must remain $< 1.5\%$.
   - *Host Net Promoter Score (NPS) / Host De-listings*: Hosts feeling stripped of control may leave Airbnb for VRBO.
