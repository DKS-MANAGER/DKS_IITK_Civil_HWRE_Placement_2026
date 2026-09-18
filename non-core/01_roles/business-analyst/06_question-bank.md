# 06. Business Analyst: Comprehensive 60+ Question Bank

> High-yield, categorized placement interview questions covering SQL, Excel, Applied Statistics, Business Acumen, KPI Cases, and Behavioral Fit.

---

## 📑 Question Bank Index
- **Section 1**: SQL Querying & Schema Logic (Q1 - Q15)
- **Section 2**: Excel & Spreadsheet Modeling (Q16 - Q25)
- **Section 3**: Applied Statistics & A/B Testing (Q26 - Q35)
- **Section 4**: Business Acumen & Unit Economics (Q36 - Q45)
- **Section 5**: KPI Drops & Metric Diagnostic Cases (Q46 - Q55)
- **Section 6**: Behavioral & Civil-to-BA Fit (Q56 - Q65)

---

## Section 1: SQL Querying & Schema Logic

### Q1 [P0][SQL]: Write a query to find the 3rd highest salary from an `Employee` table without using `LIMIT` or `TOP`.
```sql
SELECT DISTINCT salary 
FROM Employee e1
WHERE 2 = (
    SELECT COUNT(DISTINCT e2.salary)
    FROM Employee e2
    WHERE e2.salary > e1.salary
);
```
*Interviewer Follow-Up*: How would you write this using window functions?
```sql
WITH RankedSalaries AS (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rnk
    FROM Employee
)
SELECT salary FROM RankedSalaries WHERE rnk = 3;
```

### Q2 [P0][SQL]: Given an `Orders(order_id, customer_id, order_date, amount)` table, calculate Month-over-Month (MoM) revenue growth %.
```sql
WITH MonthlyRevenue AS (
    SELECT 
        DATE_TRUNC('month', order_date) AS month,
        SUM(amount) AS total_rev
    FROM Orders
    GROUP BY 1
),
LaggedRevenue AS (
    SELECT 
        month,
        total_rev,
        LAG(total_rev, 1) OVER (ORDER BY month) AS prev_month_rev
    FROM MonthlyRevenue
)
SELECT 
    month,
    total_rev,
    prev_month_rev,
    ROUND(100.0 * (total_rev - prev_month_rev) / prev_month_rev, 2) AS mom_growth_pct
FROM LaggedRevenue;
```

### Q3 [P0][SQL]: Find all customers who placed an order in January 2026 but did NOT place any order in February 2026.
```sql
SELECT DISTINCT customer_id 
FROM Orders
WHERE order_date >= '2026-01-01' AND order_date < '2026-02-01'
EXCEPT
SELECT DISTINCT customer_id
FROM Orders
WHERE order_date >= '2026-02-01' AND order_date < '2026-03-01';
```

### Q4 [P0][SQL]: Calculate Day-30 User Retention Rate for each registration cohort.
```sql
WITH UsersReg AS (
    SELECT user_id, DATE_TRUNC('day', signup_date) as cohort_date
    FROM Users
),
Activity AS (
    SELECT user_id, DATE_TRUNC('day', activity_date) as active_date
    FROM UserLogins
)
SELECT 
    u.cohort_date,
    COUNT(DISTINCT u.user_id) AS cohort_size,
    COUNT(DISTINCT a.user_id) AS retained_users,
    ROUND(100.0 * COUNT(DISTINCT a.user_id) / COUNT(DISTINCT u.user_id), 2) AS d30_retention_pct
FROM UsersReg u
LEFT JOIN Activity a 
    ON u.user_id = a.user_id 
    AND a.active_date = u.cohort_date + INTERVAL '30 days'
GROUP BY 1 ORDER BY 1;
```

### Q5 [P1][SQL]: What is the difference between `RANK()`, `DENSE_RANK()`, and `ROW_NUMBER()`?
- `ROW_NUMBER()`: Assigns unique sequential integers (1, 2, 3, 4) regardless of ties.
- `RANK()`: Assigns same rank to ties but skips subsequent numbers (1, 2, 2, 4).
- `DENSE_RANK()`: Assigns same rank to ties without skipping numbers (1, 2, 2, 3).

### Q6 [P0][SQL]: How do you handle `NULL` values in `COUNT()` vs `AVG()`?
- `COUNT(column)` ignores `NULL`s, whereas `COUNT(*)` counts all rows including `NULL`s.
- `AVG(column)` ignores `NULL`s in the denominator. To treat `NULL` as 0: `AVG(COALESCE(column, 0))`.

### Q7 [P1][SQL]: Find the top 2 highest-selling product SKUs within each category.
```sql
WITH CategoryRanks AS (
    SELECT 
        category_id,
        product_id,
        SUM(sales_amount) as total_sales,
        DENSE_RANK() OVER (PARTITION BY category_id ORDER BY SUM(sales_amount) DESC) as rnk
    FROM Sales
    GROUP BY 1, 2
)
SELECT category_id, product_id, total_sales
FROM CategoryRanks
WHERE rnk <= 2;
```

### Q8 [P0][SQL]: What happens to row counts in `INNER JOIN`, `LEFT JOIN`, `CROSS JOIN` when table A has 10 rows and table B has 5 rows?
- `INNER JOIN`: Between 0 and $10 	imes 5 = 50$ rows (depending on matching keys).
- `LEFT JOIN`: Minimum 10 rows, maximum 50 rows.
- `CROSS JOIN`: Exactly $10 	imes 5 = 50$ rows.

### Q9 [P1][SQL]: Identify duplicate email records in a `Users` table and write a query to keep only the record with the lowest `user_id`.
```sql
DELETE FROM Users
WHERE user_id NOT IN (
    SELECT MIN(user_id)
    FROM Users
    GROUP BY email
);
```

### Q10 [P1][SQL]: Calculate a 7-day rolling average of daily active users (DAU).
```sql
SELECT 
    date,
    dau,
    AVG(dau) OVER (
        ORDER BY date 
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS rolling_7d_dau
FROM DailyMetrics;
```

### Q11 [P2][SQL]: Write a query to find the median transaction value without using built-in median functions.
```sql
WITH OrderedTxns AS (
    SELECT 
        amount,
        ROW_NUMBER() OVER (ORDER BY amount) as row_id,
        COUNT(*) OVER () as total_rows
    FROM Transactions
)
SELECT AVG(amount) as median_val
FROM OrderedTxns
WHERE row_id IN ((total_rows + 1)/2, (total_rows + 2)/2);
```

### Q12 [P1][SQL]: Explain the SQL execution order.
1. `FROM` & `JOIN` $ightarrow$ 2. `WHERE` $ightarrow$ 3. `GROUP BY` $ightarrow$ 4. `HAVING` $ightarrow$ 5. `SELECT` $ightarrow$ 6. `DISTINCT` $ightarrow$ 7. `ORDER BY` $ightarrow$ 8. `LIMIT / OFFSET`.
*(Aliasing defined in SELECT cannot be used in WHERE because WHERE executes before SELECT).*

### Q13 [P1][SQL]: Query to find consecutive active days (login streaks $\ge 3$ consecutive days).
- **Approach**: Use `date - ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY date)` to generate a grouped streak identifier (`grp`), then `GROUP BY user_id, grp HAVING COUNT(*) >= 3`.

### Q14 [P0][SQL]: Explain `UNION` vs `UNION ALL`.
- `UNION` removes duplicate rows by executing an internal sort/hash operation (slower).
- `UNION ALL` concatenates datasets directly preserving all duplicates (faster).

### Q15 [P1][SQL]: Find the second most recent order date for each customer.
```sql
WITH RankedOrders AS (
    SELECT 
        customer_id,
        order_date,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date DESC) as rnk
    FROM Orders
)
SELECT customer_id, order_date as second_latest_order
FROM RankedOrders WHERE rnk = 2;
```

---

## Section 2: Excel & Spreadsheet Modeling

### Q16 [P0][EXCEL]: When would you use `XLOOKUP` over `INDEX/MATCH`?
- `XLOOKUP` is simpler, defaults to exact match, searches from bottom to top easily, and handles errors cleanly with `[if_not_found]`. `INDEX/MATCH` is preserved for backwards compatibility with legacy `.xls` files.

### Q17 [P0][EXCEL]: How do you calculate weighted average cost in Excel?
`=SUMPRODUCT(Units_Range, Cost_Per_Unit_Range) / SUM(Units_Range)`

### Q18 [P1][EXCEL]: How does a 2-variable Data Table work in Excel?
- It performs multi-scenario sensitivity analysis by feeding a matrix of row and column variables into a single core calculation cell without writing 25 separate formulas.

### Q19 [P0][EXCEL]: How do you prevent `#DIV/0!` and `#N/A` errors from breaking dashboard formulas?
- Wrap calculations in `=IFERROR(formula, 0)` or `=IFNA(formula, "Not Found")`.

### Q20 [P1][EXCEL]: What is the difference between an absolute reference (`$A$1`), mixed reference (`$A1` or `A$1`), and relative reference (`A1`)?
- `$A$1` freezes both column and row when dragged; `$A1` freezes column A while row changes; `A$1` freezes row 1 while column changes.

### Q21 [P0][EXCEL]: How do you extract the first name from a full name string in cell A2?
`=LEFT(A2, FIND(" ", A2) - 1)`

### Q22 [P1][EXCEL]: How would you dynamically highlight all revenue cells that are below the 20th percentile?
- Use Conditional Formatting $ightarrow$ New Rule $ightarrow$ Format values that rank in bottom $20\%$.

### Q23 [P0][EXCEL]: Explain the difference between `COUNT`, `COUNTA`, and `COUNTBLANK`.
- `COUNT`: Counts cells containing numbers.
- `COUNTA`: Counts non-empty cells (numbers, text, errors).
- `COUNTBLANK`: Counts empty cells.

### Q24 [P1][EXCEL]: How do you dynamically calculate the total sales for the last 30 days relative to today's date?
`=SUMIFS(Sales_Range, Date_Range, ">=" & (TODAY() - 30), Date_Range, "<=" & TODAY())`

### Q25 [P2][EXCEL]: How do you calculate Internal Rate of Return (IRR) for irregular cash flows occurring on specific dates?
- Use `=XIRR(values_range, dates_range)` instead of standard `=IRR()`.

---

## Section 3: Applied Statistics & A/B Testing

### Q26 [P0][STATS]: Calculate sample size required for an A/B test with 4% baseline conversion and 10% target relative lift.
- Baseline $p = 0.04$, MDE $\Delta = 0.04 	imes 0.10 = 0.004$.
- $N pprox rac{16 \cdot p(1-p)}{\Delta^2} = rac{16 \cdot 0.04 \cdot 0.96}{(0.004)^2} = rac{0.6144}{0.000016} pprox \mathbf{38,400	ext{ users per variant}}$ (Total = ~76,800 users).

### Q27 [P0][STATS]: How do you detect and resolve Sample Ratio Mismatch (SRM)?
- Perform Chi-Square test on observed vs expected traffic counts ($\chi^2 = \sum rac{(O - E)^2}{E}$). If $p < 0.001$, SRM is present. Root causes: Redirection delay, bot-filtering imbalance, or sticky hashing bugs.

### Q28 [P1][STATS]: What is the p-value and what does it NOT tell you?
- P-value is the probability of observing test results at least as extreme as the observed data, assuming the null hypothesis ($H_0$) is true. It does NOT measure the probability that $H_0$ is true or the business magnitude of the effect.

### Q29 [P1][STATS]: Explain Simpson's Paradox with an e-commerce example.
- Overall conversion of Variant B is higher because it had 80% mobile traffic (higher converting device), but Variant A won on both Desktop and Mobile individually.

### Q30 [P0][STATS]: What are guardrail metrics in an A/B test?
- Metrics that must not degrade while optimizing the primary metric (e.g., Optimizing checkout conversion must not increase refund rate or customer support ticket volume).

### Q31 [P1][STATS]: When should you use a Median instead of a Mean?
- When the data distribution is heavily skewed or has extreme outliers (e.g. User income, delivery delay time, order values).

### Q32 [P0][STATS]: What is Central Limit Theorem (CLT)?
- The distribution of sample means approximates a normal distribution as sample size increases ($N \ge 30$), regardless of the underlying population distribution.

### Q33 [P1][STATS]: What is the difference between Statistical Significance and Practical/Business Significance?
- Statistical significance proves an effect is not due to random chance ($p < 0.05$). Practical significance evaluates if the absolute magnitude of lift justifies engineering and operational deployment costs.

### Q34 [P2][STATS]: What is the Peeking Problem in A/B testing and how is it solved?
- Repeatedly checking test results and stopping early inflates Type I false positive error rate from 5% to $>30\%$. Solved using Sequential Testing (e.g. Always Valid p-values) or fixed-horizon sample enforcement.

### Q35 [P1][STATS]: How do you treat outliers in customer transaction datasets?
- Trim/Winsorize extreme percentiles ($>99.5	ext{th}$ percentile), analyze them separately as potential fraud or enterprise B2B accounts, or use non-parametric rank tests.

---

## Section 4: Business Acumen & Unit Economics

### Q36 [P0][BUSINESS]: An e-commerce platform has 1,000 INR AOV, 15% take-rate, 60 INR payment/logistics cost, and 40 INR CAC. Calculate Contribution Margin 2 (CM2).
- Gross Revenue per order = $1,000 	imes 15\% = 150	ext{ INR}$.
- Direct Fulfillment/Payment Cost = $60	ext{ INR}$.
- $	ext{CM1} = 150 - 60 = 90	ext{ INR}$.
- $	ext{CM2} = 90 - 40 (	ext{CAC}) = \mathbf{50	ext{ INR per order}}$.

### Q37 [P0][BUSINESS]: If monthly churn rate is 5%, what is the expected customer lifetime in months?
- $	ext{Customer Lifetime} = rac{1}{	ext{Monthly Churn}} = rac{1}{0.05} = \mathbf{20	ext{ months}}$.

### Q38 [P1][BUSINESS]: Why can Net Revenue Retention (NRR) be $>100\%$ while Logo Churn is $10\%$?
- Existing accounts expanded their usage/licenses (Upselling/Cross-selling) by more than the revenue lost from the 10% churned logos.

### Q39 [P0][BUSINESS]: Differentiate between GMV, Gross Revenue, and Net Revenue for a ride-hailing platform.
- GMV = Total passenger fare paid ($500	ext{ INR}$).
- Gross Revenue = Platform Take-Rate commission ($20\% 	imes 500 = 100	ext{ INR}$).
- Net Revenue = Take-Rate minus driver incentives and customer discount coupons ($100 - 30 = 70	ext{ INR}$).

### Q40 [P1][BUSINESS]: What is Return to Origin (RTO) in Indian e-commerce and how does it destroy unit economics?
- Orders shipped via Cash on Delivery (COD) that are rejected at doorstep. The platform incurs forward shipping, reverse shipping, and inventory lockup costs without capturing revenue.

### Q41 [P0][BUSINESS]: Explain the trade-off between CAC and LTV during hyper-growth vs profitability phases.
- Hyper-growth prioritizes high CAC to capture market share and network effects; Profitability phases optimize $LTV / CAC \ge 3	imes$ by targeting organic channels and repeat retention.

### Q42 [P1][BUSINESS]: If a subscription business has 10,000 users paying 500 INR/month with 4% monthly churn and 100 INR/user server cost, calculate total business LTV.
- Unit Gross Margin = $rac{500 - 100}{500} = 80\%$.
- $LTV = rac{500 	imes 0.80}{0.04} = 10,000	ext{ INR per user}$.
- Total Portfolio LTV = $10,000 	imes 10,000 = \mathbf{10	ext{ Cr INR}}$.

### Q43 [P1][BUSINESS]: What is Burn Multiple in startup finance?
- $	ext{Burn Multiple} = rac{	ext{Net Cash Burn}}{	ext{Net New ARR Added}}$. A burn multiple $<1.0$ indicates exceptional capital efficiency.

### Q44 [P0][BUSINESS]: How does discounting affect price elasticity and brand equity?
- Deep discounting attracts low-LTV price-sensitive churners and degrades reference pricing, reducing willingness to pay at full price.

### Q45 [P2][BUSINESS]: Why is Day-1 retention higher than Day-30 retention, and what is a "retention smile"?
- Initial drop occurs as unengaged users drop off. A "retention smile" occurs when previously churned users are successfully resurrected through re-engagement campaigns.

---

## Section 5: KPI Drops & Metric Diagnostic Cases

### Q46 [P0][CASE]: "Our food delivery app's Daily Active Users (DAU) dropped 12% on Monday. Walk me through your diagnosis."
- **Approach**: 
  1. *Verify*: Check data telemetry, tracking pixel uptime, and logging pipelines.
  2. *Segment*: Segment by OS (iOS vs Android), Geography (North vs South India), App Version, User Cohort (New vs Repeat).
  3. *Isolate*: External factors (severe storm, festival, public holiday) vs Internal factors (buggy app release, push notification gateway failure, payment gateway downtime).

### Q47 [P0][CASE]: "Checkout conversion rate dropped from 4.5% to 3.2% after a redesign. Diagnose."
- **Approach**: Deconstruct checkout funnel: Cart $ightarrow$ Address $ightarrow$ Payment Selection $ightarrow$ OTP $ightarrow$ Success. Isolate step drop-off; evaluate payment gateway latency and auto-fill friction.

### Q48 [P1][CASE]: "Average Order Value (AOV) increased by 20%, but total daily revenue dropped by 10%. Why?"
- **Approach**: $	ext{Revenue} = 	ext{Orders} 	imes 	ext{AOV}$. If AOV rose $20\%$ ($1.20$) and Revenue fell $10\%$ ($0.90$), Total Orders fell by $1 - rac{0.90}{1.20} = 25\%$. Price increases or removal of low-cost entry SKUs crushed transaction volume.

### Q49 [P1][CASE]: "Ride-hailing driver cancellation rate increased from 8% to 18% in Mumbai. Root causes?"
- **Approach**: Check traffic congestion (longer pickup ETA), low fare pricing / high fuel costs, high cash payment preference, or surge pricing transparency mismatch.

### Q50 [P0][CASE]: "SaaS free-trial to paid conversion dropped from 8% to 5%. Diagnose."
- **Approach**: Evaluate lead quality source (paid ads vs organic), product onboarding tour friction, time-to-first-value (Aha moment), and trial length changes.

### Q51 [P1][CASE]: "Quick-commerce 10-minute delivery SLA compliance dropped from 95% to 78%. Diagnose."
- **Approach**: Deconstruct delivery timeline: Order Placement $ightarrow$ Dark Store Picking (seconds) $ightarrow$ Packing $ightarrow$ Rider Handover $ightarrow$ Last-Mile Transit. Check picking staffing deficit vs rider supply deficit vs weather.

### Q52 [P2][CASE]: "Search-to-click conversion on an e-commerce platform fell 15% while total search volume grew 30%."
- **Approach**: Marketing campaign brought low-intent exploratory traffic, or search algorithm ranking returned zero/irrelevant results for newly searched long-tail keywords.

### Q53 [P1][CASE]: "Credit card transaction volume declined 8% over the weekend. How do you investigate?"
- **Approach**: Isolate Merchant Category Codes (travel vs dining vs groceries), check bank core banking system downtime, POS terminal connectivity, and fraud rule false-positive spikes.

### Q54 [P0][CASE]: "User session length increased by 40%, but purchases remained flat. Is this good or bad?"
- **Approach**: Bad. Increased session length without conversion indicates navigation confusion, poor search relevancy, or checkout friction rather than genuine engagement.

### Q55 [P1][CASE]: "Subscription churn doubled in Month 3 for an annual-monthly billing plan. Why Month 3?"
- **Approach**: Expiry of 90-day introductory discount promotion, moving users to full price; or quarterly software review cycles by client procurement.

---

## Section 6: Behavioral & Civil-to-BA Fit

### Q56 [P0][FIT]: "Tell me about yourself in 90 seconds."
- Structure: Academic foundation at IIT Kanpur $ightarrow$ Quantitative & modeling research projects $ightarrow$ Data analytics / software proficiency $ightarrow$ Passion for business problem solving.

### Q57 [P0][FIT]: "Why do you want to join our firm as a Business Analyst rather than pursuing Civil Engineering?"
- Emphasize love for quantitative modeling, statistical decision-making, and high-velocity business impact. (See [05_interview-preparation.md](05_interview-preparation.md) for verbatim script).

### Q58 [P0][FIT]: "Tell me about a time you analyzed data and arrived at a non-obvious business insight."
- Frame using STAR: Describe dataset, the initial incorrect assumption, your statistical analysis isolating the true root cause, and the resulting business change.

### Q59 [P1][FIT]: "How do you explain complex statistical results to a non-technical marketing or sales executive?"
- Focus on business outcomes rather than statistical jargon: Replace "p-value < 0.01" with "We have 99% statistical confidence that this new checkout button will generate 50 Lakh INR in incremental monthly revenue."

### Q60 [P0][FIT]: "Describe a situation where you had a tight deadline and incomplete data. How did you proceed?"
- State how you identified the 80/20 critical assumptions, verified boundaries with senior peers, and established a tracking mechanism to iterate as new data arrived.

### Q61 [P1][FIT]: "Tell me about a project where your initial model or hypothesis failed."
- Discuss objective self-correction, debugging data assumptions, and pivoting to an alternate hypothesis.

### Q62 [P1][FIT]: "What is your favorite mobile application and how would you improve its North Star metric?"
- Name an app (e.g. Swiggy/Spotify), define its North Star metric, identify current user friction, and propose a 2-step experiment to optimize it.

### Q63 [P0][FIT]: "How do you handle disagreement with a product manager or developer on metric definitions?"
- Anchor the discussion on business goals, write out clear edge-case documentation, and seek alignment using historical data.

### Q64 [P1][FIT]: "What are your 3 strongest technical and professional qualities?"
- 1. Advanced SQL & quantitative rigor; 2. First-principles business structuring; 3. Clear executive communication.

### Q65 [P0][FIT]: "Do you have any questions for us?"
- Ask about current analytics stack challenges, experimentation culture, or specific business transformation initiatives.
