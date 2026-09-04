# Product Analyst — Rapid Revision Sheet

> Last-minute cheat sheet. Covers SQL patterns, product metrics, A/B testing, and quick-fire Q&A.

---

## Framework 1: SQL Essential Patterns

### JOIN Types Cheat Sheet

| JOIN | Returns |
|:-----|:--------|
| INNER JOIN | Only matching rows from both tables |
| LEFT JOIN | All rows from left + matching from right (NULL if no match) |
| RIGHT JOIN | All rows from right + matching from left |
| FULL JOIN | All rows from both (NULL where no match) |
| CROSS JOIN | Every combination (Cartesian product) |

### Window Functions

```sql
-- Ranking
ROW_NUMBER() OVER (PARTITION BY group_col ORDER BY value)  -- Unique rank
RANK() OVER (ORDER BY value)           -- Skips ranks after ties
DENSE_RANK() OVER (ORDER BY value)     -- No gaps after ties

-- Lag/Lead
LAG(value, 1) OVER (ORDER BY date)     -- Previous row's value
LEAD(value, 1) OVER (ORDER BY date)    -- Next row's value

-- Running totals
SUM(value) OVER (ORDER BY date ROWS UNBOUNDED PRECEDING)  -- Cumulative sum

-- Percent of total
value * 100.0 / SUM(value) OVER ()     -- % contribution
```

### Common SQL Patterns

**Top N per group:**
```sql
SELECT * FROM (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY category ORDER BY revenue DESC) AS rn
    FROM orders
) t WHERE rn <= 3;
```

**Year-over-year growth:**
```sql
WITH yearly AS (
    SELECT YEAR(order_date) AS yr, SUM(amount) AS revenue
    FROM orders GROUP BY YEAR(order_date)
)
SELECT yr, revenue,
    LAG(revenue) OVER (ORDER BY yr) AS prev_year,
    ROUND((revenue - LAG(revenue) OVER (ORDER BY yr)) / 
          LAG(revenue) OVER (ORDER BY yr) * 100, 1) AS yoy_growth
FROM yearly;
```

**Retention (month N+1):**
```sql
WITH first_order AS (
    SELECT user_id, MIN(MONTH(order_date)) AS first_month
    FROM orders GROUP BY user_id
),
month_n AS (
    SELECT user_id, MONTH(order_date) AS order_month
    FROM orders
)
SELECT f.first_month,
    COUNT(DISTINCT f.user_id) AS cohort_size,
    COUNT(DISTINCT CASE WHEN m.order_month = f.first_month + 1 THEN f.user_id END) AS retained,
    ROUND(COUNT(DISTINCT CASE WHEN m.order_month = f.first_month + 1 THEN f.user_id END) * 100.0 / 
          COUNT(DISTINCT f.user_id), 1) AS retention_pct
FROM first_order f
LEFT JOIN month_n m ON f.user_id = m.user_id
GROUP BY f.first_month;
```

**Median (without MEDIAN function):**
```sql
WITH ranked AS (
    SELECT amount, ROW_NUMBER() OVER (ORDER BY amount) AS rn,
           COUNT(*) OVER () AS total
    FROM orders
)
SELECT AVG(amount) AS median_amount
FROM ranked
WHERE rn IN (FLOOR((total+1)/2.0), CEIL((total+1)/2.0));
```

---

## Framework 2: Product Metrics

### Core Metrics Table

| Metric | Formula | Benchmark |
|:-------|:--------|:----------|
| **DAU/MAU** | Daily Active / Monthly Active | >20% healthy |
| **Stickiness** | DAU/MAU × 100 | >25% good for social |
| **Retention (D1)** | % users returning next day | >40% good |
| **Retention (D7)** | % users returning after 7 days | >20% good |
| **Retention (D30)** | % users returning after 30 days | >10% good |
| **Conversion Rate** | Conversions / Total visitors | Varies by industry |
| **AOV** | Revenue / Number of orders | Track trends |
| **ARPU** | Revenue / Active users | Compare segments |
| **CLV** | AOV × Purchase frequency × Lifespan | Maximize |
| **CAC** | Total acquisition cost / New customers | CLV > 3× CAC |
| **Churn Rate** | Lost customers / Total customers at start | <5% monthly |

### AARRR (Pirate Metrics)

```
Acquisition  → How users find you (downloads, signups)
Activation   → First "aha" moment (first order, first post)
Revenue      → Monetization (subscriptions, purchases)
Retention    → Users coming back (DAU, repeat rate)
Referral     → Users telling others (NPS, viral coefficient)
```

### Funnel Analysis Template

```
Stage 1: Awareness     → Impressions, reach
Stage 2: Interest      → Clicks, time on page
Stage 3: Consideration → Signups, add to cart
Stage 4: Action        → Purchase, subscription
Stage 5: Retention     → Repeat usage, renewal
Stage 6: Advocacy      → Reviews, referrals
```

**Drop-off analysis:** Calculate conversion from each stage to next. Focus on the biggest drop.

---

## Framework 3: A/B Testing

### A/B Test Process

```
1. Hypothesis:  "Changing X will improve Y because Z"
2. Metric:      Primary (conversion) + Guardrails (retention, revenue)
3. Sample size: Use calculator (e.g., Evan Miller's)
4. Randomize:   50/50 split, stratified if needed
5. Run:         Minimum 1-2 weeks (cover weekly cycles)
6. Analyze:     Check significance (p < 0.05), confidence intervals
7. Decide:      Ship, iterate, or kill
```

### Sample Size Formula (Simplified)

```
n = (Z² × 2 × p × (1-p)) / d²
```

Where:
- Z = 1.96 for 95% confidence
- p = baseline conversion rate
- d = minimum detectable effect (absolute)

**Example:** p=10%, d=1%, Z=1.96
n = (3.84 × 2 × 0.1 × 0.9) / 0.0001 = 6,912 per group

### P-Value Interpretation

| P-value | Interpretation |
|:--------|:---------------|
| < 0.01 | Very strong evidence against H₀ |
| < 0.05 | Strong evidence (industry standard) |
| 0.05-0.10 | Weak evidence, inconclusive |
| > 0.10 | No significant evidence |

### A/B Testing Pitfalls

| Pitfall | What Goes Wrong | Fix |
|:--------|:---------------|:----|
| **Peeking** | Inflated false positive | Fix sample size, don't peek early |
| **Novelty effect** | Initial spike, then drops | Run for 2+ weeks |
| **Multiple comparisons** | False positives increase | Bonferroni correction |
| **Sample ratio mismatch** | Unequal groups | Check randomization |
| **Interaction effects** | Tests interfere | Run sequentially |

---

## Framework 4: Product Thinking

### Feature Prioritization: RICE Score

```
RICE = (Reach × Impact × Confidence) / Effort
```

| Factor | Scale |
|:-------|:------|
| Reach | Users affected per quarter |
| Impact | 0.25 (minimal), 0.5 (low), 1 (medium), 2 (high), 3 (massive) |
| Confidence | 100% (high), 80% (medium), 50% (low) |
| Effort | Person-months |

### Kano Model

| Category | Description | Example |
|:---------|:-----------|:--------|
| **Must-have** | Expected, causes dissatisfaction if absent | Basic security, uptime |
| **Performance** | More is better, linear satisfaction | Faster load time |
| **Delighter** | Unexpected, creates delight | Surprise feature |
| **Indifferent** | No impact on satisfaction | Minor UI tweak |

### OKR Template

```
Objective: Improve user retention
  KR1: Increase D7 retention from 20% to 25%
  KR2: Reduce churn rate from 8% to 5%
  KR3: Achieve NPS score of 50+
```

---

## 10 Quick-Fire Interview Answers

**Q1: What is DAU/MAU and why does it matter?**
A: DAU/MAU is the ratio of daily to monthly active users, measuring "stickiness." A ratio of 25% means the average user opens the app 7.5 days/month. Higher stickiness = stronger product engagement. Facebook has ~50%; WhatsApp ~70%.

**Q2: How do you measure the success of a new feature?**
A: Define a primary metric (the thing the feature is supposed to improve), guardrail metrics (things that shouldn't get worse), and run an A/B test. Compare treatment vs control over 2+ weeks. Ship if primary metric improves significantly without degrading guardrails.

**Q3: What is the difference between a data analyst and a product analyst?**
A: Data analyst answers questions about data (reporting, ad-hoc analysis). Product analyst proactively uses data to drive product decisions — defining metrics, running experiments, recommending features. Product analysts are closer to the product lifecycle.

**Q4: Explain p-value in simple terms.**
A: P-value is the probability of seeing results as extreme as yours if there were actually no real difference (null hypothesis is true). P < 0.05 means there's less than 5% chance the result is due to random noise — so we conclude the change is real.

**Q5: What is cohort analysis?**
A: Grouping users by a shared characteristic (signup date, first purchase) and tracking their behavior over time. For example, "January cohort" = users who signed up in January. Track their retention month by month to see how different cohorts perform.

**Q6: What metrics would you track for Instagram Reels?**
A: Primary: Watch time, completion rate, shares. Supporting: DAU, time spent in Reels, creator upload rate, content diversity. Guardrails: Overall app DAU, Stories engagement, feed engagement. North Star: Total time spent in Reels per DAU.

**Q7: What is a guardrail metric?**
A: A metric that should NOT degrade when you make a change. For example, if you're testing a new onboarding flow that increases signups, guardrail metrics would be Day-7 retention (ensuring we're not attracting low-quality users) and customer support tickets.

**Q8: An A/B test shows 2% improvement with p=0.08. What do you do?**
A: Don't ship — p=0.08 doesn't meet the 0.05 significance threshold. Options: (1) Run the test longer for more data, (2) Increase sample size, (3) Check if the test was properly powered, (4) Consider business significance — is 2% worth the engineering effort?

**Q9: How would you handle a stakeholder who wants to skip A/B testing?**
A: Explain the risk: "Without testing, we're making a $X bet based on opinion. An A/B test costs $Y and gives us confidence." Offer a compromise: fast test (smaller sample, shorter duration) or feature flag with monitoring.

**Q10: What is the North Star metric?**
A: The single metric that best captures the core value your product delivers to users. For Netflix = watch time. For Uber = rides completed. For Spotify = time listened. It should correlate with business success and be actionable by the team.

---

## Last-Minute Checklist

### Before Any PA Interview
- [ ] SQL window functions (ROW_NUMBER, LAG, RANK)
- [ ] AARRR framework (Acquisition → Retention → Revenue)
- [ ] A/B test process (hypothesis → sample size → significance)
- [ ] Core metrics: DAU/MAU, conversion, retention, AOV, CLV
- [ ] RICE scoring for feature prioritization

### Must-Know Formulas
- [ ] DAU/MAU = Daily Active / Monthly Active
- [ ] Retention = Users returning / Users in cohort × 100
- [ ] Conversion = Conversions / Total visitors × 100
- [ ] AOV = Revenue / Orders
- [ ] ARPU = Revenue / Active users
- [ ] CLV = AOV × Frequency × Lifespan
- [ ] RICE = (Reach × Impact × Confidence) / Effort
- [ ] Sample size n = Z² × 2p(1-p) / d²

### Behavioral Prep
- [ ] "Why product analytics?" (data + product impact)
- [ ] "Tell me about a data-driven decision" (STAR story)
- [ ] "How do you prioritize when data is ambiguous?"
- [ ] "Describe a feature you'd build for [this product]"

---

## Cross-Links

**Product Analyst:**
→ [PA Overview](pa-overview.md) — Complete preparation system
→ [Role Study Plan](role-study-plan.md) — Structured study plan

**Related:**
→ [Data Analyst Study Plan](../data-analyst/role-study-plan.md) — Deeper SQL/stats
→ [Product Management](../product-management/role-study-plan.md) — PM context
→ [Consulting Case Frameworks](../consulting/case-frameworks.md) — Case prep

---

*Last updated: 2026-09-04*
