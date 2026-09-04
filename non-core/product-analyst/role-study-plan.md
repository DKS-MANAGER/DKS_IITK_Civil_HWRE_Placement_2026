# Product Analyst — Role Study Plan

## Role Overview

The Product Analyst role targets **product analytics positions** at tech companies (Google, Microsoft, Amazon), **fintech firms** (Paytm, PhonePe, Razorpay), **SaaS companies** (Freshworks, Zoho, Atlassian), and **digital platforms** (Swiggy, Zomato, Ola). The role sits at the intersection of data analysis and product management — using data to drive product decisions, measure feature success, and optimize user experience. Civil engineers' analytical skills and systematic problem-solving transfer well.

**Who targets this role:** B.Tech/M.Tech graduates with SQL/Python skills, students interested in tech products, those who enjoy data-driven decision making, GATE qualifiers transitioning to tech.

---

## 3–4 Highest-Value Preparation Blocks

### Topic 1: SQL & Data Analysis

#### Why This Matters
SQL is the single most tested skill in product analyst interviews. Every company expects you to write complex queries, handle edge cases, and explain your logic. This is non-negotiable.

#### What to Learn
- [ ] SELECT, WHERE, GROUP BY, HAVING, ORDER BY
- [ ] JOINs: INNER, LEFT, RIGHT, FULL, CROSS
- [ ] Window functions: ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD, NTILE
- [ ] Aggregate functions: COUNT, SUM, AVG, MIN, MAX
- [ ] Subqueries: Correlated, non-correlated
- [ ] CTEs (Common Table Expressions) and temp tables
- [ ] CASE WHEN for conditional logic
- [ ] Data cleaning: NULL handling, duplicates, type casting
- [ ] Performance basics: Indexing, EXPLAIN, query optimization

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`pa-overview.md`](pa-overview.md) | SQL fundamentals, analytics | Full |
| [`non-core-prep.md`](../analytics/non-core-prep.md) | SQL practice | Reference |

#### Worked Example
**Problem:** Given two tables:

**users** (user_id, signup_date, country, age)
**orders** (order_id, user_id, order_date, amount, category)

Write queries to:
1. Find the top 5 countries by total revenue in 2024
2. Find users who made orders in every month of 2024
3. Calculate month-over-month revenue growth rate

**Solution:**

**Query 1:** Top 5 countries by revenue
```sql
SELECT u.country, SUM(o.amount) AS total_revenue
FROM users u
INNER JOIN orders o ON u.user_id = o.user_id
WHERE YEAR(o.order_date) = 2024
GROUP BY u.country
ORDER BY total_revenue DESC
LIMIT 5;
```

**Query 2:** Users who ordered every month
```sql
SELECT user_id
FROM orders
WHERE YEAR(order_date) = 2024
GROUP BY user_id
HAVING COUNT(DISTINCT MONTH(order_date)) = 12;
```

**Query 3:** Month-over-month growth
```sql
WITH monthly_revenue AS (
    SELECT 
        MONTH(order_date) AS month,
        SUM(amount) AS revenue
    FROM orders
    WHERE YEAR(order_date) = 2024
    GROUP BY MONTH(order_date)
)
SELECT 
    month,
    revenue,
    LAG(revenue) OVER (ORDER BY month) AS prev_month,
    ROUND((revenue - LAG(revenue) OVER (ORDER BY month)) / 
          LAG(revenue) OVER (ORDER BY month) * 100, 2) AS growth_pct
FROM monthly_revenue;
```

**Key insight:** "For Query 2, I use COUNT(DISTINCT MONTH) because a user might order multiple times in a month — we only care that they ordered in each distinct month."

#### Practice
**Basic (3–5):**
1. Write a query to find the total number of orders and revenue per user.
2. Find users who have never placed an order (LEFT JOIN with NULL check).
3. Write a query to find the second highest order amount per category.
4. Calculate average order value per country, sorted descending.
5. Find duplicate email entries in a users table.

**Intermediate (3–5):**
6. Write a query to find the running total of orders per user (ordered by date).
7. Find the month with the highest revenue for each country.
8. Calculate the percentage of total revenue each category contributes.
9. Write a query to find consecutive days where revenue increased.
10. Using window functions, rank users by total spend within each country.

**Interview-Level (5+):**
11. Write a query to find the median order amount (without using MEDIAN function).
12. Find the retention rate: % of users who placed an order in month N who also ordered in month N+1.
13. Write a query to detect anomalous orders (amount > 3× standard deviation above mean).
14. Create a cohort analysis showing monthly retention of users by signup month.
15. Write an optimized query for finding the top 10 users by order frequency in a billion-row table.

#### Interview Questions (What Interviewer Tests)
| Question | What They're Testing |
|:---------|:---------------------|
| Write a query for top-N by category | Basic SQL proficiency |
| Use window functions for ranking | Advanced SQL |
| Handle edge cases (NULLs, duplicates) | Data quality awareness |
| Optimize a slow query | Performance thinking |
| Explain your approach before coding | Communication |

#### Common Mistakes
- **Forgetting** GROUP BY when using aggregates
- **Using** WHERE instead of HAVING for post-aggregation filters
- **Not handling** NULLs — NULL ≠ 0 in comparisons
- **Ignoring** data type issues (string vs numeric)
- **Writing** inefficient queries without thinking about index usage

#### Completion Criterion
✅ Can write queries using JOINs, subqueries, and window functions
✅ Can handle NULLs, duplicates, and edge cases
✅ Can optimize queries for performance
✅ Can explain logic clearly before and after coding

---

### Topic 2: Product Metrics & A/B Testing

#### Why This Matters
Product analysts live and die by metrics. Knowing which metrics to track, how to calculate them, and how to run experiments (A/B tests) to validate product changes is the core of the role.

#### What to Learn
- [ ] North Star Metric vs supporting metrics
- [ ] Acquisition → Activation → Revenue → Retention (AARRR / Pirate Metrics)
- [ ] DAU/MAU (Daily/Monthly Active Users), stickiness ratio
- [ ] Conversion funnel: awareness → interest → action
- [ ] Retention curves: Day 1, Day 7, Day 30 retention
- [ ] Cohort analysis: Tracking user groups over time
- [ ] A/B testing: Hypothesis, sample size, significance, p-value
- [ ] Common pitfalls: Peeking, multiple comparisons, novelty effect

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`pa-overview.md`](pa-overview.md) | Metrics, experimentation | Full |

#### Worked Example
**Problem:** A food delivery app has:
- DAU = 500,000
- MAU = 2,000,000
- New users this month = 200,000
- Users who ordered = 800,000
- Users who ordered 2+ times = 400,000
- Total orders = 1,600,000
- Total revenue = ₹32,00,00,000

Calculate: (a) DAU/MAU ratio, (b) Conversion rate, (c) Repeat purchase rate, (d) Orders per user, (e) Revenue per order, (f) Revenue per user.

**Solution:**
1. **DAU/MAU stickiness** = 500,000 / 2,000,000 = **25%** (good — >20% is healthy for apps)
2. **Conversion rate** = 800,000 / 2,000,000 = **40%** (users who placed at least 1 order)
3. **Repeat purchase rate** = 400,000 / 800,000 = **50%** (of those who ordered, 50% ordered again)
4. **Orders per user** = 1,600,000 / 800,000 = **2.0 orders/user**
5. **Revenue per order** = ₹32,00,00,000 / 16,00,000 = **₹200/order**
6. **Revenue per user** = ₹32,00,00,000 / 2,00,000 = **₹160/user (MAU)** or ₹32,00,00,000 / 8,00,000 = **₹400/user (transacting)**

**Key insight:** "The 50% repeat purchase rate is strong. The metric to improve is conversion (40% → ?) — can we reduce friction in the first-order experience?"

#### A/B Test Example
**Problem:** We changed the checkout button color from blue to green. Results:
- Control (blue): 10,000 visitors, 450 conversions (4.50%)
- Treatment (green): 10,000 visitors, 520 conversions (5.20%)
- Is this statistically significant at 95% confidence?

**Solution:**
1. **H₀:** p_treatment = p_control (no difference)
2. **H₁:** p_treatment > p_control (green is better)
3. **Pooled proportion:** p = (450+520)/(10000+10000) = 970/20000 = 0.0485
4. **Standard error:** SE = √[p(1-p)(1/n₁ + 1/n₂)] = √[0.0485 × 0.9515 × 0.0002] = √0.00000923 = 0.00304
5. **Z-statistic:** Z = (0.052 - 0.045) / 0.00304 = 0.007 / 0.00304 = **2.30**
6. **P-value:** P(Z > 2.30) = 0.0107 < 0.05 → **Statistically significant!**
7. **Conclusion:** Reject H₀. The green button has a significantly higher conversion rate.

**Lift:** (5.20 - 4.50) / 4.50 = **15.6% improvement**

#### Practice
**Basic (3–5):**
1. Define DAU, MAU, and stickiness ratio. What's a good stickiness?
2. Explain the AARRR framework with an example for a food delivery app.
3. What is a conversion funnel? Draw one for e-commerce.
4. Define cohort analysis. Why is it important?
5. What is statistical significance in A/B testing?

**Intermediate (3–5):**
6. Calculate retention rate from a cohort table (given data for 6 months).
7. Design an A/B test for a new feature that changes the search algorithm.
8. A product has DAU=1M, MAU=5M. Is this healthy? What would you recommend?
9. What is the difference between absolute and relative lift?
10. Design metrics for a new ride-sharing feature.

**Interview-Level (5+):**
11. What metrics would you track for a new product launch? Why?
12. An A/B test shows no difference. What could have gone wrong?
13. How do you handle multiple comparisons (testing 5 variants simultaneously)?
14. What is a "guardrail metric"? Give examples.
15. How would you measure the success of a recommendation engine?

#### Common Mistakes
- **Confusing** correlation with causation
- **Not running** A/B tests long enough (novelty effect)
- **Peeking** at results before the test is complete (inflates false positive rate)
- **Choosing** the wrong metric (vanity metrics vs actionable metrics)
- **Ignoring** sample size requirements before starting a test

#### Completion Criterion
✅ Can define and calculate 10+ product metrics
✅ Can design a proper A/B test with hypothesis, sample size, and analysis
✅ Can interpret cohort analysis and retention curves
✅ Can recommend the right metrics for different product scenarios

---

### Topic 3: Product Thinking & Feature Analysis

#### Why This Matters
Beyond numbers, product analysts need to think like product managers — understanding user needs, prioritizing features, and making recommendations. This separates data analysts from product analysts.

#### What to Learn
- [ ] User personas and jobs-to-be-done (JTBD)
- [ ] Feature prioritization: RICE, MoSCoW, Kano model
- [ ] Product-market fit metrics
- [ ] User journey mapping
- [ ] Impact vs effort matrix
- [ ] Product requirements document (PRD) basics
- [ ] Wireframing and prototyping concepts
- [ ] OKRs (Objectives and Key Results)

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`pa-overview.md`](pa-overview.md) | Product thinking, frameworks | Full |
| [`role-study-plan.md`](../product-management/role-study-plan.md) | PM context | Reference |

#### Worked Example
**Problem:** A food delivery app is seeing declining repeat orders. The funnel shows:
- App opens: 1,000,000
- Search: 600,000 (60%)
- Restaurant viewed: 300,000 (50% of search)
- Add to cart: 150,000 (50% of viewed)
- Checkout started: 100,000 (67% of cart)
- Order placed: 80,000 (80% of checkout)
- Delivery: 75,000 (94% of placed)
- Rated order: 20,000 (27% of delivered)

Identify the biggest drop-off points and propose 3 product improvements.

**Solution:**
1. **Funnel Analysis:**

| Stage | Users | Drop-off | Conversion to Next |
|:------|------:|:--------:|:-------------------:|
| Opens → Search | 600K | 400K (40%) | 60% |
| Search → Viewed | 300K | 300K (50%) | 50% ⚠️ |
| Viewed → Cart | 150K | 150K (50%) | 50% ⚠️ |
| Cart → Checkout | 100K | 50K (33%) | 67% |
| Checkout → Placed | 80K | 20K (20%) | 80% |
| Placed → Delivered | 75K | 5K (6%) | 94% |
| Delivered → Rated | 20K | 55K (73%) | 27% ⚠️ |

2. **Biggest drop-offs:**
   - **Opens → Search (40%):** Users open but don't search → Maybe push notifications are irrelevant?
   - **Search → Viewed (50%):** Search results not compelling → Improve search ranking, show popular items
   - **Viewed → Cart (50%):** Users see restaurants but don't order → Price perception, delivery time visibility
   - **Delivered → Rated (73%):** Low review rate → Simplify rating, incentivize reviews

3. **Proposed Improvements:**
   - **Quick Reorder:** Add "Order Again" button on home screen → reduces search friction
   - **Price Transparency:** Show total cost (including delivery) on restaurant page → reduces cart abandonment
   - **In-App Rating:** Simplify to 1-tap rating after delivery → increases review rate

**Key insight:** "The 40% drop at opens→search is alarming. Are we sending push notifications to users who aren't hungry? Personalize notification timing based on past order patterns."

#### Practice
**Basic (3–5):**
1. What is a user persona? Create one for a food delivery app.
2. Explain the RICE scoring framework.
3. What is the Kano model? Name the three categories of features.
4. Draw a user journey map for booking a flight on an app.
5. What is the difference between a feature and a benefit?

**Intermediate (3–5):**
6. Given funnel data, identify the biggest drop-off and recommend improvements.
7. Prioritize 5 features using RICE scoring.
8. How would you measure the success of adding a "dark mode" feature?
9. Design metrics for a new social sharing feature.
10. What is product-market fit? How do you measure it?

**Interview-Level (5+):**
11. You're the product analyst for Google Maps. What metrics do you track?
12. A feature launch shows 20% engagement increase but 5% decrease in retention. What do you do?
13. How do you balance between experimentation speed and statistical rigor?
14. Design a metrics dashboard for a subscription SaaS product.
15. What is the difference between a product analyst and a data analyst?

#### Common Mistakes
- **Listing** metrics without explaining why they matter
- **Not connecting** data insights to actionable product recommendations
- **Ignoring** qualitative data (user interviews, feedback) alongside quantitative
- **Over-indexing** on a single metric (goodhart's law)
- **Not considering** business impact — a 1% improvement on a small metric < a 0.1% improvement on revenue

#### Completion Criterion
✅ Can analyze product funnels and identify bottlenecks
✅ Can prioritize features using structured frameworks
✅ Can connect data insights to product recommendations
✅ Can design metrics for new features and products

---

### Topic 4: Case Studies & Communication

#### Why This Matters
Product analyst interviews often include case studies: "How would you analyze this problem?" or "What metrics would you track for X?" Structured thinking and clear communication are as important as technical skill.

#### What to Learn
- [ ] Structured problem-solving: MECE, issue trees
- [ ] Product case frameworks: Metrics definition, root cause analysis
- [ ] Stakeholder communication: Translating data into insights
- [ ] Data storytelling: Narrative + visualization + recommendation
- [ ] Executive summary writing

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`case-frameworks.md`](../consulting/case-frameworks.md) | Structured problem-solving | Reference |
| [`pa-overview.md`](pa-overview.md) | Case study prep | Full |

#### Worked Example
**Problem:** "Netflix sees a 10% drop in streaming hours. How would you investigate?"

**Solution (Structured Approach):**
1. **Clarify:** "10% drop compared to what? Last month? Same time last year? Overall or in specific regions?"

2. **Break down the problem (MECE):**
   - Is it a data quality issue? (tracking error, metric definition change)
   - Is it user-side? (fewer users, users streaming less)
   - Is it content-side? (fewer new releases, popular show ended)
   - Is it competitive? (new competitor launched, exclusive content elsewhere)
   - Is it technical? (app issues, streaming quality problems)

3. **Data analysis plan:**
   - Segment by: Geography, device, user tenure, content type
   - Check: DAU, sessions per user, duration per session
   - Compare: Week-over-week, same period YoY
   - Check: New content releases schedule, competitor launches

4. **Likely root causes:**
   - Seasonality (summer = less indoor time)
   - Content gap (no major new releases)
   - Technical issue (app crash on new Android update)
   - Pricing change (recent price increase → cancellations)

5. **Recommendation:** "First, rule out data quality. Then segment by geography and device. If the drop is concentrated in a specific segment, investigate that. If it's uniform, check content calendar and competitive landscape."

#### Practice
**Basic (3–5):**
1. "How would you measure the success of Instagram Reels?"
2. "WhatsApp sees a 20% increase in group creation. What does this mean?"
3. "A new feature increases engagement but also increases customer support tickets. What do you do?"
4. "Design metrics for an online learning platform."
5. "How would you analyze why users are abandoning their shopping carts?"

**Intermediate (3–5):**
6. "YouTube sees watch time declining 5%. Investigate."
7. "Your A/B test shows a 2% increase in clicks but a 1% decrease in conversion. What happened?"
8. "Design a dashboard for the CEO of a food delivery company."
9. "How would you prioritize between improving existing features vs building new ones?"
10. "An e-commerce app's search-to-purchase conversion dropped 15%. What would you investigate?"

**Interview-Level (5+):**
11. "Build a metrics framework for a new product at your company."
12. "The CEO asks: Should we launch in a new country? What analysis would you do?"
13. "How do you handle disagreements with engineers about what to build?"
14. "A stakeholder asks for data that doesn't exist. How do you handle it?"
15. "Present a data-driven recommendation in 3 minutes."

#### Common Mistakes
- **Jumping** to solutions without structuring the problem
- **Not asking clarifying questions** before analyzing
- **Overwhelming** with data instead of insights
- **Not tailoring** communication to the audience (engineer vs CEO)
- **Ignoring** qualitative context behind numbers

#### Completion Criterion
✅ Can structure any product problem using MECE frameworks
✅ Can analyze a case study with data and qualitative insights
✅ Can communicate findings clearly to different stakeholders
✅ Can design metrics frameworks for new products/features

---

## Mock Test (45 Minutes)

| # | Question | Topic | Marks |
|---|:---------|:------|------:|
| 1 | Write SQL queries: (a) Find top 3 categories by revenue per country, (b) Calculate month-over-month revenue growth, (c) Find users who ordered in 3+ consecutive months. | SQL & Data | 25 |
| 2 | Given: DAU=300K, MAU=1.5M, new users=100K, orders=600K, revenue=₹18Cr. Calculate stickiness, conversion, repeat rate, AOV, ARPU. If DAU drops 10% next month, what would you investigate? | Product Metrics | 25 |
| 3 | A food delivery app's conversion funnel shows: Opens 800K → Search 400K → Restaurant 200K → Cart 100K → Checkout 60K → Order 50K. Identify drop-off points and recommend 3 product improvements. | Funnel Analysis | 25 |
| 4 | "YouTube wants to increase creator monetization. What metrics would you track? How would you measure success of a new monetization feature?" | Product Thinking | 15 |
| 5 | Explain A/B testing. What is p-value? What sample size do you need for a test with 5% significance and 80% power, given baseline conversion = 10% and minimum detectable effect = 1%? | Experimentation | 10 |
| | | **Total** | **100** |

---

## Interview Strategy

### SQL / Technical Round (20 minutes)
1. **Clarify** the problem before writing code
2. **Think aloud** — explain your approach before and during coding
3. **Handle edge cases** — NULLs, duplicates, empty results
4. **Optimize** — mention indexing, avoid unnecessary JOINs

### Product Sense Round (15 minutes)
1. **Start with metrics** — "The key metric to track would be..."
2. **Structure your thinking** — "Let me break this down into..."
3. **Connect data to action** — "Based on this, I would recommend..."
4. **Consider trade-offs** — "This could improve X but might impact Y"

### Behavioral Round (10 minutes)
- **Have STAR stories** about data-driven decisions
- **Show curiosity** — "I noticed something interesting in the data..."
- **Demonstrate ownership** — "I proactively investigated and found..."

### Unique Positioning (Civil → Product Analyst)
- "Engineering background gives me strong analytical and problem-solving skills"
- "I understand systems thinking — how changing one part affects the whole"
- "Construction scheduling taught me about resource optimization and constraints"

---

## Cross-Links

**Next:**
→ [PA Overview](pa-overview.md) — Complete preparation system

**Study:**
→ [Data Analyst Study Plan](../data-analyst/role-study-plan.md) — For deeper SQL/stats
→ [Product Management Study Plan](../product-management/role-study-plan.md) — For PM context

**Interview:**
→ [Technical Interview Bank](../../prep/interview/technical/technical-interview-bank.md)
→ [Behavioral Guide](../../prep/behavioral/behavioral-interview-guide.md)
→ [HR Questions](../../prep/behavioral/hr_questions/hr-questions-bank.md)

**Related:**
→ [Technology Overview](../technology/tech-overview.md) — For tech-adjacent roles
→ [Finance Study Plan](../finance/role-study-plan.md) — For fintech product roles

---

*This study plan follows the [Role Study Plan Template](../../prep/templates/role-study-plan-template.md).*
*Last updated: 2026-09-04*
