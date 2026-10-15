# Tools Lab 03: SQL, Analytics & Data Interpretation for Consulting

> **Lab Objective**: Master SQL cohort queries, interpret regression & machine learning outputs for business executives, and clean messy client datasets.  
> **Target Roles**: Essential for Analytics-Led Consulting (ZS, EXL, Mu Sigma, Fractal) and Digital Consulting (Accenture, Deloitte Tech); highly useful as a differentiator for generalist consulting candidates.  
> **Prerequisites**: Basic knowledge of relational tables.  
> **Estimated Lab Time**: 1.5 hours.

---

## 1. When Does a Consultant Need SQL and Python?

Do not assume every management consultant writes code:
- **Generalist Strategy (McKinsey, BCG, Bain, Strategy&)**: 95% of analysis is executed in Excel and PowerPoint. Coding is **not tested** in case interviews. However, understanding data concepts (cohorts, sample bias, p-values, regression slopes) is essential for evaluating client exhibits.
- **Analytics-Led & Digital Consulting (ZS, Accenture Tech, Deloitte Analytics)**: Candidates face mandatory technical online assessments and technical case interviews requiring SQL queries and predictive model interpretation.

---

## 2. Production SQL: Multi-Month Customer Retention Cohort Query

Client problem: An e-commerce platform wants to measure whether customers acquired in January 2024 repeat-purchase in subsequent months (Months 1 to 6).

### Table Schema:
- `users (user_id INT, signup_date DATE)`
- `orders (order_id INT, user_id INT, order_date DATE, order_amount NUMERIC)`

### Production SQL Query:
```sql
WITH user_cohorts AS (
    -- Step 1: Assign each customer to their initial signup month cohort
    SELECT 
        user_id,
        DATE_TRUNC('month', signup_date) AS cohort_month
    FROM users
),
order_activity AS (
    -- Step 2: Calculate elapsed months between order date and signup cohort
    SELECT 
        o.user_id,
        uc.cohort_month,
        DATE_TRUNC('month', o.order_date) AS order_month,
        (EXTRACT(YEAR FROM o.order_date) - EXTRACT(YEAR FROM uc.cohort_month)) * 12 +
        (EXTRACT(MONTH FROM o.order_date) - EXTRACT(MONTH FROM uc.cohort_month)) AS period_month
    FROM orders o
    JOIN user_cohorts uc ON o.user_id = uc.user_id
)
-- Step 3: Aggregate unique active purchasers by cohort and elapsed period
SELECT 
    cohort_month,
    COUNT(DISTINCT user_id) AS total_cohort_users,
    COUNT(DISTINCT CASE WHEN period_month = 0 THEN user_id END) AS m0_active,
    COUNT(DISTINCT CASE WHEN period_month = 1 THEN user_id END) AS m1_active,
    COUNT(DISTINCT CASE WHEN period_month = 2 THEN user_id END) AS m2_active,
    COUNT(DISTINCT CASE WHEN period_month = 3 THEN user_id END) AS m3_active
FROM order_activity
GROUP BY cohort_month
ORDER BY cohort_month ASC;
```

#### How a Consultant Interprets This Output:
If the January cohort drops from 10,000 users in Month 0 to 2,500 in Month 1 (25% retention), but flattens at 2,400 in Month 2 and 2,350 in Month 3, the retention curve has **flattened into a loyal core base**. Churn is an onboarding issue, not product-market fit failure!

---

## 3. Interpreting Regression Outputs for Business CXOs

Consultants frequently receive statistical regression outputs from client data science teams. You must translate mathematical metrics into commercial insights:

### Sample Regression Table: Predicting Churn Propensity
$$\text{Churn Probability} = f(\text{Monthly Spend}, \text{Customer Age}, \text{Support Tickets}, \text{App Sessions})$$

| Variable | Coefficient ($\beta$) | Standard Error | t-Statistic | p-Value | 95% Confidence Interval |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Intercept** | `0.450` | `0.052` | `8.65` | `<0.001` | `[0.348, 0.552]` |
| **Monthly Spend ($)** | `-0.004` | `0.001` | `-4.00` | `<0.001` | `[-0.006, -0.002]` |
| **Customer Age (Years)**| `-0.001` | `0.002` | `-0.50` | `0.617` | `[-0.005, 0.003]` |
| **Support Tickets Filed**| `+0.120` | `0.015` | `+8.00` | `<0.001` | `[0.091, 0.149]` |
| **Weekly App Sessions** | `-0.035` | `0.008` | `-4.38` | `<0.001` | `[-0.051, -0.019]` |

*Model Summary*: $R^2 = 0.38$, $N = 45,000\text{ accounts}$.

### The Consultant's 4-Point Interpretation for the CEO:
1. **Statistical Significance Check**:
   - `Support Tickets` ($p < 0.001$) and `App Sessions` ($p < 0.001$) are highly statistically significant ($p < 0.05$).
   - `Customer Age` ($p = 0.617 > 0.05$) is statistically indistinguishable from zero. **Recommendation**: Advise marketing to stop wasting budget on age-targeted retention campaigns.
2. **Economic Effect Size**:
   - Each unresolved support ticket filed increases customer churn probability by **+12.0 percentage points**.
   - If a customer files 3 support tickets, their churn risk spikes by 36%!
3. **Actionable Business Decision**:
   - The root driver of customer churn is support ticket friction.
   - Investing $500k to expand tier-2 technical support staff and resolve complaints within 24 hours directly protects millions in customer lifetime value.
