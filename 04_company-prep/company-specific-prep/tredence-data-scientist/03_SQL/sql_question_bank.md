# 03 — SQL Analytical Question Bank (50 Solved Problems)
## Enterprise Analytical Queries, Windowing Challenges & Business Intelligence Questions

> **Document Status**: Technical Practice Question Bank `[TIER 5 / PEDAGOGICAL BANK]`  
> **Target Role**: Data Scientist / Associate Data Scientist | Tredence Analytics  
> **Coverage**: 50 Solved ANSI SQL Queries across Aggregations, Joins, Window Functions, Retention Cohorts, Gaps & Islands, and Rolling Statistics.

---

### Part 1: Core Aggregation, Joins & Subqueries (Q01 – Q15)

#### Q01. Second Highest Salary per Department
- **Business Question**: Find the employee(s) earning the second highest salary in each department.
- **Difficulty**: Medium | **Target Time**: 3 min
- **SQL Solution**:
  ```sql
  WITH RankedSalaries AS (
      SELECT 
          dept_id, employee_id, employee_name, salary,
          DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rnk
      FROM employees
  )
  SELECT dept_id, employee_id, employee_name, salary
  FROM RankedSalaries
  WHERE rnk = 2;
  ```
- **Explanation**: `DENSE_RANK()` ensures that if multiple employees share the highest salary, the next distinct salary receives rank 2.
- **Common Mistake**: Using `LIMIT 1 OFFSET 1`, which fails when departments have ties or when grouping across multiple departments.

---

#### Q02. Customers Who Never Placed an Order (Anti-Join)
- **Business Question**: Identify all registered customers who have zero purchase transactions.
- **Difficulty**: Easy | **Target Time**: 2 min
- **SQL Solution**:
  ```sql
  SELECT c.customer_id, c.customer_name
  FROM customers c
  LEFT JOIN orders o ON c.customer_id = o.customer_id
  WHERE o.order_id IS NULL;
  ```
- **Alternative**: `WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id)`.
- **Common Mistake**: Using `NOT IN (SELECT customer_id FROM orders)` when `customer_id` contains `NULL`s, which causes the entire `NOT IN` clause to return zero rows.

---

#### Q03. Monthly Sales Growth Rate
- **Business Question**: Calculate month-over-month percentage revenue growth across 2024.
- **Difficulty**: Medium | **Target Time**: 3 min
- **SQL Solution**:
  ```sql
  WITH MonthlyRevenue AS (
      SELECT 
          DATE_TRUNC('month', order_date) AS order_month,
          SUM(order_amount) AS total_revenue
      FROM orders
      GROUP BY DATE_TRUNC('month', order_date)
  )
  SELECT 
      order_month,
      total_revenue,
      LAG(total_revenue, 1) OVER (ORDER BY order_month) AS prev_month_revenue,
      ROUND(
          (total_revenue - LAG(total_revenue, 1) OVER (ORDER BY order_month)) * 100.0 /
          NULLIF(LAG(total_revenue, 1) OVER (ORDER BY order_month), 0), 2
      ) AS mom_growth_pct
  FROM MonthlyRevenue;
  ```
- **Common Mistake**: Forgetting `NULLIF(..., 0)` to handle division by zero.

---

#### Q04. Finding Duplicate Records Across Key Columns
- **Business Question**: Retrieve duplicate customer email records and their counts.
- **Difficulty**: Easy | **Target Time**: 2 min
- **SQL Solution**:
  ```sql
  SELECT email, COUNT(*) AS occurrences
  FROM customers
  GROUP BY email
  HAVING COUNT(*) > 1;
  ```

---

#### Q05. Deduplicating a Table Keeping the Lowest ID
- **Business Question**: Delete duplicate customer records keeping only the earliest inserted ID.
- **Difficulty**: Medium | **Target Time**: 3 min
- **SQL Solution**:
  ```sql
  DELETE FROM customers
  WHERE customer_id NOT IN (
      SELECT MIN(customer_id)
      FROM customers
      GROUP BY email
  );
  ```

---

#### Q06. Running Total of Orders per Customer
- **Business Question**: Calculate cumulative spend per customer across order dates.
- **Difficulty**: Easy | **Target Time**: 2 min
- **SQL Solution**:
  ```sql
  SELECT 
      customer_id, order_date, order_amount,
      SUM(order_amount) OVER (
          PARTITION BY customer_id 
          ORDER BY order_date 
          ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
      ) AS running_spend
  FROM orders;
  ```

---

#### Q07. Daily Active Users (DAU) and Monthly Active Users (MAU)
- **Business Question**: Compute daily active user count for platform telemetry.
- **Difficulty**: Easy | **Target Time**: 2 min
- **SQL Solution**:
  ```sql
  SELECT 
      CAST(activity_timestamp AS DATE) AS active_date,
      COUNT(DISTINCT user_id) AS dau
  FROM user_logins
  GROUP BY CAST(activity_timestamp AS DATE);
  ```

---

#### Q08. Top 3 Products by Revenue in Each Category
- **Business Question**: Identify the top 3 revenue-generating products per category.
- **Difficulty**: Medium | **Target Time**: 3 min
- **SQL Solution**:
  ```sql
  WITH ProductRevenue AS (
      SELECT 
          category_id, product_id, SUM(sales_amount) AS revenue,
          DENSE_RANK() OVER (PARTITION BY category_id ORDER BY SUM(sales_amount) DESC) AS rnk
      FROM sales
      GROUP BY category_id, product_id
  )
  SELECT category_id, product_id, revenue
  FROM ProductRevenue
  WHERE rnk <= 3;
  ```

---

#### Q09. Consecutive Logins (Gaps and Islands)
- **Business Question**: Find users who logged into the platform for at least 3 consecutive days.
- **Difficulty**: Hard | **Target Time**: 5 min
- **SQL Solution**:
  ```sql
  WITH DistinctLogins AS (
      SELECT DISTINCT user_id, CAST(login_time AS DATE) AS login_date
      FROM user_logins
  ),
  GroupedLogins AS (
      SELECT 
          user_id, login_date,
          login_date - (ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY login_date) * INTERVAL '1 day') AS grp
      FROM DistinctLogins
  )
  SELECT user_id, MIN(login_date) AS streak_start, COUNT(*) AS streak_length
  FROM GroupedLogins
  GROUP BY user_id, grp
  HAVING COUNT(*) >= 3;
  ```
- **Explanation**: Subtracting `ROW_NUMBER()` from consecutive dates produces a constant group identifier `grp` for unbroken daily streaks!

---

#### Q10. Percentage of Total Sales per Product
- **Business Question**: Return each product's sales and its percentage of store total revenue.
- **Difficulty**: Easy | **Target Time**: 2 min
- **SQL Solution**:
  ```sql
  SELECT 
      store_id, product_id, sales_amount,
      ROUND(
          sales_amount * 100.0 / SUM(sales_amount) OVER (PARTITION BY store_id), 2
      ) AS pct_of_store_revenue
  FROM store_sales;
  ```

---

#### Q11. Customers with Repeat Purchases Within 7 Days
- **Business Question**: Identify customers who made another purchase within 7 days of their prior purchase.
- **Difficulty**: Medium | **Target Time**: 4 min
- **SQL Solution**:
  ```sql
  WITH PriorOrders AS (
      SELECT 
          customer_id, order_id, order_date,
          LAG(order_date, 1) OVER (PARTITION BY customer_id ORDER BY order_date) AS prev_date
      FROM orders
  )
  SELECT DISTINCT customer_id
  FROM PriorOrders
  WHERE prev_date IS NOT NULL 
    AND order_date - prev_date <= INTERVAL '7 days';
  ```

---

#### Q12. Median Salary Without Built-in `MEDIAN()`
- **Business Question**: Calculate median salary per department in ANSI SQL.
- **Difficulty**: Hard | **Target Time**: 5 min
- **SQL Solution**:
  ```sql
  WITH Ranked AS (
      SELECT 
          dept_id, salary,
          ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary) AS row_asc,
          ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS row_desc
      FROM employees
  )
  SELECT dept_id, AVG(salary * 1.0) AS median_salary
  FROM Ranked
  WHERE ABS(row_asc - row_desc) <= 1
  GROUP BY dept_id;
  ```

---

#### Q13. Manager and Subordinate Salary Discrepancy
- **Business Question**: Find all employees who earn more than their direct manager.
- **Difficulty**: Easy | **Target Time**: 3 min
- **SQL Solution**:
  ```sql
  SELECT 
      e.employee_id, e.employee_name, e.salary AS emp_salary,
      m.employee_name AS manager_name, m.salary AS mgr_salary
  FROM employees e
  INNER JOIN employees m ON e.manager_id = m.employee_id
  WHERE e.salary > m.salary;
  ```

---

#### Q14. Department with Highest Average Salary
- **Business Question**: Find department name with the highest average employee salary.
- **Difficulty**: Easy | **Target Time**: 2 min
- **SQL Solution**:
  ```sql
  SELECT d.dept_name, AVG(e.salary) AS avg_sal
  FROM employees e
  INNER JOIN departments d ON e.dept_id = d.dept_id
  GROUP BY d.dept_name
  ORDER BY avg_sal DESC
  LIMIT 1;
  ```

---

#### Q15. Rolling 7-Day Revenue Moving Average
- **Business Question**: Calculate daily sales and its 7-day trailing simple moving average.
- **Difficulty**: Medium | **Target Time**: 3 min
- **SQL Solution**:
  ```sql
  SELECT 
      sale_date, daily_sales,
      AVG(daily_sales) OVER (
          ORDER BY sale_date 
          ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
      ) AS rolling_7d_sma
  FROM daily_sales_summary;
  ```

---

### Part 2: Advanced Windowing & Analytical Business Queries (Q16 – Q35)

#### Q16. Year-over-Year (YoY) Same-Store Sales Growth
- **Business Question**: Calculate YoY revenue growth for stores open in both 2023 and 2024.
- **Difficulty**: Medium | **Target Time**: 4 min
- **SQL Solution**:
  ```sql
  WITH StoreYearly AS (
      SELECT 
          store_id, EXTRACT(YEAR FROM sale_date) AS yr,
          SUM(amount) AS revenue
      FROM pos_transactions
      WHERE EXTRACT(YEAR FROM sale_date) IN (2023, 2024)
      GROUP BY store_id, EXTRACT(YEAR FROM sale_date)
  )
  SELECT 
      s24.store_id,
      s23.revenue AS rev_2023,
      s24.revenue AS rev_2024,
      ROUND((s24.revenue - s23.revenue) * 100.0 / s23.revenue, 2) AS yoy_growth_pct
  FROM StoreYearly s24
  INNER JOIN StoreYearly s23 ON s24.store_id = s23.store_id 
                            AND s24.yr = 2024 AND s23.yr = 2023;
  ```

---

#### Q17. Customer Cohort Retention (Month 0 to Month 6)
- **Business Question**: Calculate monthly cohort retention counts based on first order date.
- **Difficulty**: Hard | **Target Time**: 6 min
- **SQL Solution**:
  ```sql
  WITH FirstOrder AS (
      SELECT customer_id, DATE_TRUNC('month', MIN(order_date)) AS cohort_month
      FROM orders
      GROUP BY customer_id
  ),
  Activity AS (
      SELECT 
          o.customer_id,
          f.cohort_month,
          EXTRACT(MONTH FROM AGE(DATE_TRUNC('month', o.order_date), f.cohort_month)) AS period_num
      FROM orders o
      JOIN FirstOrder f ON o.customer_id = f.customer_id
  )
  SELECT 
      cohort_month,
      COUNT(DISTINCT CASE WHEN period_num = 0 THEN customer_id END) AS m0,
      COUNT(DISTINCT CASE WHEN period_num = 1 THEN customer_id END) AS m1,
      COUNT(DISTINCT CASE WHEN period_num = 2 THEN customer_id END) AS m2,
      COUNT(DISTINCT CASE WHEN period_num = 3 THEN customer_id END) AS m3
  FROM Activity
  GROUP BY cohort_month
  ORDER BY cohort_month;
  ```

---

#### Q18. Top-Spending Customer in Each City
- **Business Question**: Identify highest spending customer per city.
- **Difficulty**: Medium | **Target Time**: 3 min
- **SQL Solution**:
  ```sql
  WITH CustCitySpend AS (
      SELECT 
          c.city, c.customer_id, c.customer_name, SUM(o.order_amount) AS total_spend,
          ROW_NUMBER() OVER (PARTITION BY c.city ORDER BY SUM(o.order_amount) DESC) AS rnk
      FROM customers c
      JOIN orders o ON c.customer_id = o.customer_id
      GROUP BY c.city, c.customer_id, c.customer_name
  )
  SELECT city, customer_id, customer_name, total_spend
  FROM CustCitySpend
  WHERE rnk = 1;
  ```

---

#### Q19. Identifying Churned Customers (Inactive for 90+ Days)
- **Business Question**: Retrieve customers whose last purchase was over 90 days ago.
- **Difficulty**: Easy | **Target Time**: 2 min
- **SQL Solution**:
  ```sql
  SELECT customer_id, MAX(order_date) AS last_order_date
  FROM orders
  GROUP BY customer_id
  HAVING MAX(order_date) < CURRENT_DATE - INTERVAL '90 days';
  ```

---

#### Q20. Finding Gaps in Booking Rooms (Hotel/Hospitality)
- **Business Question**: Detect dates where a specific room had no reservations.
- **Difficulty**: Hard | **Target Time**: 5 min
- **SQL Solution**:
  ```sql
  WITH OrderedBookings AS (
      SELECT 
          room_id, check_out_date,
          LEAD(check_in_date) OVER (PARTITION BY room_id ORDER BY check_in_date) AS next_check_in
      FROM bookings
  )
  SELECT room_id, check_out_date AS vacant_from, next_check_in AS vacant_until
  FROM OrderedBookings
  WHERE next_check_in > check_out_date;
  ```

---

#### Q21. Second Purchase Time Elapsed (Days to Second Order)
- **Business Question**: Calculate average number of days between customer's 1st and 2nd purchase.
- **Difficulty**: Medium | **Target Time**: 4 min
- **SQL Solution**:
  ```sql
  WITH RankedOrders AS (
      SELECT 
          customer_id, order_date,
          ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) AS rn
      FROM orders
  ),
  FirstTwo AS (
      SELECT 
          customer_id,
          MAX(CASE WHEN rn = 1 THEN order_date END) AS d1,
          MAX(CASE WHEN rn = 2 THEN order_date END) AS d2
      FROM RankedOrders
      WHERE rn <= 2
      GROUP BY customer_id
      HAVING COUNT(*) = 2
  )
  SELECT ROUND(AVG(d2 - d1), 1) AS avg_days_to_second_purchase
  FROM FirstTwo;
  ```

---

#### Q22. Basket Affinity (Frequently Bought Together Items)
- **Business Question**: Find pairs of products purchased in the same order most frequently.
- **Difficulty**: Medium | **Target Time**: 4 min
- **SQL Solution**:
  ```sql
  SELECT 
      i1.product_id AS product_a,
      i2.product_id AS product_b,
      COUNT(DISTINCT i1.order_id) AS times_bought_together
  FROM order_items i1
  INNER JOIN order_items i2 ON i1.order_id = i2.order_id 
                           AND i1.product_id < i2.product_id -- Prevents self-pairing & duplicate (B,A)
  GROUP BY i1.product_id, i2.product_id
  ORDER BY times_bought_together DESC
  LIMIT 10;
  ```

---

#### Q23. Customer Lifetime Value (CLTV) Decile Partitioning
- **Business Question**: Segment customers into 10 deciles based on lifetime revenue.
- **Difficulty**: Easy | **Target Time**: 3 min
- **SQL Solution**:
  ```sql
  SELECT 
      customer_id, SUM(order_amount) AS total_spend,
      NTILE(10) OVER (ORDER BY SUM(order_amount) DESC) AS ltv_decile
  FROM orders
  GROUP BY customer_id;
  ```

---

#### Q24. Out-of-Stock (OOS) Duration Calculation
- **Business Question**: Compute total hours a store SKU spent with zero inventory before restock.
- **Difficulty**: Hard | **Target Time**: 5 min
- **SQL Solution**:
  ```sql
  WITH StockStatus AS (
      SELECT 
          store_id, sku_id, snapshot_time, stock_qty,
          LEAD(snapshot_time) OVER (PARTITION BY store_id, sku_id ORDER BY snapshot_time) AS next_time
      FROM inventory_snapshots
  )
  SELECT 
      store_id, sku_id,
      SUM(EXTRACT(EPOCH FROM (next_time - snapshot_time)) / 3600.0) AS total_oos_hours
  FROM StockStatus
  WHERE stock_qty = 0 AND next_time IS NOT NULL
  GROUP BY store_id, sku_id;
  ```

---

#### Q25. Running Active Subscriptions Count
- **Business Question**: Calculate active subscribers count at each day start.
- **Difficulty**: Hard | **Target Time**: 6 min
- **SQL Solution**:
  ```sql
  WITH Events AS (
      SELECT start_date AS event_date, 1 AS delta FROM subscriptions
      UNION ALL
      SELECT end_date AS event_date, -1 AS delta FROM subscriptions WHERE end_date IS NOT NULL
  ),
  DailyDeltas AS (
      SELECT event_date, SUM(delta) AS net_change
      FROM Events
      GROUP BY event_date
  )
  SELECT 
      event_date,
      SUM(net_change) OVER (ORDER BY event_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS active_subs
  FROM DailyDeltas;
  ```

---

#### Q26. Identifying Sudden Spikes (> 3x 30-Day Average)
- **Business Question**: Detect sales days where revenue exceeded 3x trailing 30-day average.
- **Difficulty**: Medium | **Target Time**: 4 min
- **SQL Solution**:
  ```sql
  WITH TrailingStats AS (
      SELECT 
          sale_date, daily_revenue,
          AVG(daily_revenue) OVER (
              ORDER BY sale_date 
              ROWS BETWEEN 30 PRECEDING AND 1 PRECEDING
          ) AS trailing_30d_avg
      FROM daily_sales
  )
  SELECT sale_date, daily_revenue, trailing_30d_avg
  FROM TrailingStats
  WHERE daily_revenue > 3.0 * trailing_30d_avg;
  ```

---

#### Q27. Conversion Rate Funnel Analytics
- **Business Question**: Compute step-by-step conversion rates across 4 funnel stages.
- **Difficulty**: Medium | **Target Time**: 4 min
- **SQL Solution**:
  ```sql
  SELECT 
      COUNT(DISTINCT session_id) AS visitors,
      COUNT(DISTINCT product_view_session) AS viewers,
      COUNT(DISTINCT cart_session) AS add_to_cart,
      COUNT(DISTINCT purchase_session) AS purchases,
      ROUND(COUNT(DISTINCT purchase_session) * 100.0 / COUNT(DISTINCT session_id), 2) AS end_to_end_cvr
  FROM web_funnel_sessions;
  ```

---

#### Q28. Finding the Longest Consecutive Days of Positive Profit
- **Business Question**: Find the maximum number of consecutive profitable days.
- **Difficulty**: Hard | **Target Time**: 5 min
- **SQL Solution**:
  ```sql
  WITH ProfitableDays AS (
      SELECT 
          sale_date,
          sale_date - (ROW_NUMBER() OVER (ORDER BY sale_date) * INTERVAL '1 day') AS grp
      FROM store_daily_pnl
      WHERE daily_profit > 0
  )
  SELECT COUNT(*) AS max_streak_days
  FROM ProfitableDays
  GROUP BY grp
  ORDER BY max_streak_days DESC
  LIMIT 1;
  ```

---

#### Q29. Fill Missing Hourly Sensor Readings with Last Value (LOCF)
- **Business Question**: Forward fill temperature readings for missing timestamp hours.
- **Difficulty**: Hard | **Target Time**: 5 min
- **SQL Solution**:
  ```sql
  SELECT 
      sensor_id, reading_hour,
      COALESCE(
          temperature,
          LAST_VALUE(temperature IGNORE NULLS) OVER (
              PARTITION BY sensor_id 
              ORDER BY reading_hour 
              ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
          )
      ) AS ffilled_temp
  FROM sensor_hourly;
  ```

---

#### Q30. Employee Reporting Chain Depth
- **Business Question**: Calculate organizational depth level of each employee.
- **Difficulty**: Medium | **Target Time**: 4 min
- **SQL Solution**:
  ```sql
  WITH RECURSIVE Hierarchy AS (
      SELECT employee_id, employee_name, manager_id, 1 AS depth
      FROM employees WHERE manager_id IS NULL
      UNION ALL
      SELECT e.employee_id, e.employee_name, e.manager_id, h.depth + 1
      FROM employees e JOIN Hierarchy h ON e.manager_id = h.employee_id
  )
  SELECT * FROM Hierarchy ORDER BY depth;
  ```

---

#### Q31. Third Transaction Date per User
- **Business Question**: Return the date of the third transaction for each user.
- **Difficulty**: Easy | **Target Time**: 2 min
- **SQL Solution**:
  ```sql
  WITH Ranked AS (
      SELECT user_id, transaction_date,
             ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY transaction_date) AS rn
      FROM transactions
  )
  SELECT user_id, transaction_date FROM Ranked WHERE rn = 3;
  ```

---

#### Q32. Products with Zero Sales in Last 60 Days
- **Business Question**: Identify active SKUs that generated zero sales in the last 60 days.
- **Difficulty**: Easy | **Target Time**: 2 min
- **SQL Solution**:
  ```sql
  SELECT p.product_id, p.product_name
  FROM products p
  LEFT JOIN sales s ON p.product_id = s.product_id 
                   AND s.sale_date >= CURRENT_DATE - INTERVAL '60 days'
  WHERE s.product_id IS NULL;
  ```

---

#### Q33. Finding Overlapping Employee Project Assignments
- **Business Question**: Detect employees assigned to overlapping projects simultaneously.
- **Difficulty**: Medium | **Target Time**: 4 min
- **SQL Solution**:
  ```sql
  SELECT DISTINCT p1.employee_id
  FROM project_assignments p1
  JOIN project_assignments p2 ON p1.employee_id = p2.employee_id 
                             AND p1.project_id <> p2.project_id
                             AND p1.start_date <= p2.end_date 
                             AND p1.end_date >= p2.start_date;
  ```

---

#### Q34. Customer Tier Upgrades (Silver to Gold Transition Dates)
- **Business Question**: Find the exact timestamp when a customer transitioned from Silver to Gold tier.
- **Difficulty**: Medium | **Target Time**: 3 min
- **SQL Solution**:
  ```sql
  WITH StatusHistory AS (
      SELECT 
          customer_id, change_time, new_tier,
          LAG(new_tier) OVER (PARTITION BY customer_id ORDER BY change_time) AS old_tier
      FROM customer_tier_audit
  )
  SELECT customer_id, change_time AS upgraded_at
  FROM StatusHistory
  WHERE old_tier = 'Silver' AND new_tier = 'Gold';
  ```

---

#### Q35. Sales Contribution by Store Quartile
- **Business Question**: Divide stores into 4 quartiles and compute total revenue per quartile.
- **Difficulty**: Medium | **Target Time**: 3 min
- **SQL Solution**:
  ```sql
  WITH StoreSpend AS (
      SELECT store_id, SUM(amount) AS rev,
             NTILE(4) OVER (ORDER BY SUM(amount) DESC) AS quartile
      FROM store_sales
      GROUP BY store_id
  )
  SELECT quartile, COUNT(store_id) AS store_count, SUM(rev) AS quartile_revenue
  FROM StoreSpend
  GROUP BY quartile
  ORDER BY quartile;
  ```

---

### Part 3: Retail, CPG & Scenario Analytics (Q36 – Q50)

#### Q36. Trade Promotion Incrementality
- **Business Question**: Compare daily sales during promotion periods vs non-promo baseline.
- **Difficulty**: Medium | **Target Time**: 4 min
- **SQL Solution**:
  ```sql
  SELECT 
      sku_id,
      AVG(CASE WHEN is_promo = 1 THEN units_sold END) AS promo_avg_units,
      AVG(CASE WHEN is_promo = 0 THEN units_sold END) AS non_promo_avg_units,
      ROUND(
          (AVG(CASE WHEN is_promo = 1 THEN units_sold END) - AVG(CASE WHEN is_promo = 0 THEN units_sold END)) * 100.0 /
          NULLIF(AVG(CASE WHEN is_promo = 0 THEN units_sold END), 0), 2
      ) AS lift_pct
  FROM daily_sku_sales
  GROUP BY sku_id;
  ```

---

#### Q37. Cross-Category Purchase Ratio
- **Business Question**: Find percentage of shoppers who purchased both Dairy and Bakery items in a single basket.
- **Difficulty**: Medium | **Target Time**: 3 min
- **SQL Solution**:
  ```sql
  WITH BasketCats AS (
      SELECT 
          order_id,
          MAX(CASE WHEN category = 'Dairy' THEN 1 ELSE 0 END) AS has_dairy,
          MAX(CASE WHEN category = 'Bakery' THEN 1 ELSE 0 END) AS has_bakery
      FROM order_details
      GROUP BY order_id
  )
  SELECT 
      COUNT(*) AS total_orders,
      SUM(has_dairy * has_bakery) AS dual_orders,
      ROUND(SUM(has_dairy * has_bakery) * 100.0 / COUNT(*), 2) AS dual_basket_pct
  FROM BasketCats;
  ```

---

#### Q38. Unreturned Equipment Detection (Rental Analytics)
- **Business Question**: List assets rented > 30 days ago that have not been marked returned.
- **Difficulty**: Easy | **Target Time**: 2 min
- **SQL Solution**:
  ```sql
  SELECT asset_id, customer_id, rental_date
  FROM asset_rentals
  WHERE return_date IS NULL AND rental_date < CURRENT_DATE - INTERVAL '30 days';
  ```

---

#### Q39. Price Elasticity Regression Inputs Preparation
- **Business Question**: Extract weekly average price and total sales quantity per product for regression modeling.
- **Difficulty**: Easy | **Target Time**: 3 min
- **SQL Solution**:
  ```sql
  SELECT 
      product_id,
      DATE_TRUNC('week', transaction_date) AS sales_week,
      SUM(quantity) AS total_units,
      ROUND(SUM(revenue) / NULLIF(SUM(quantity), 0), 2) AS weighted_avg_unit_price
  FROM store_sales
  GROUP BY product_id, DATE_TRUNC('week', transaction_date);
  ```

---

#### Q40. Finding First Touch and Last Touch Marketing Attribution
- **Business Question**: Identify first and last marketing channel touched by customer before order.
- **Difficulty**: Medium | **Target Time**: 4 min
- **SQL Solution**:
  ```sql
  WITH Touchpoints AS (
      SELECT 
          customer_id, channel, touch_time,
          FIRST_VALUE(channel) OVER (PARTITION BY customer_id ORDER BY touch_time 
                                     ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS first_touch,
          LAST_VALUE(channel)  OVER (PARTITION BY customer_id ORDER BY touch_time 
                                     ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS last_touch
      FROM marketing_clicks
  )
  SELECT DISTINCT customer_id, first_touch, last_touch FROM Touchpoints;
  ```

---

#### Q41. Warehouse Inventory Days of Supply (DOS)
- **Business Question**: Calculate Days of Supply given current stock and 30-day average daily velocity.
- **Difficulty**: Medium | **Target Time**: 4 min
- **SQL Solution**:
  ```sql
  WITH Velocity AS (
      SELECT sku_id, SUM(units_sold) / 30.0 AS avg_daily_velocity
      FROM sales_history
      WHERE sale_date >= CURRENT_DATE - INTERVAL '30 days'
      GROUP BY sku_id
  )
  SELECT 
      i.sku_id, i.on_hand_stock,
      ROUND(i.on_hand_stock / NULLIF(v.avg_daily_velocity, 0), 1) AS days_of_supply
  FROM inventory i
  JOIN Velocity v ON i.sku_id = v.sku_id;
  ```

---

#### Q42. Telecom Plan Downgrade Detection
- **Business Question**: Identify subscribers whose monthly bill decreased by > 30% month-over-month.
- **Difficulty**: Easy | **Target Time**: 3 min
- **SQL Solution**:
  ```sql
  WITH MonthlyBills AS (
      SELECT 
          subscriber_id, billing_month, amount,
          LAG(amount) OVER (PARTITION BY subscriber_id ORDER BY billing_month) AS prev_amount
      FROM telecom_bills
  )
  SELECT subscriber_id, billing_month, prev_amount, amount
  FROM MonthlyBills
  WHERE prev_amount IS NOT NULL AND (prev_amount - amount) / prev_amount > 0.30;
  ```

---

#### Q43. Patient Readmission Within 30 Days (Healthcare Analytics)
- **Business Question**: Find all hospital discharge events followed by readmission within 30 days.
- **Difficulty**: Medium | **Target Time**: 4 min
- **SQL Solution**:
  ```sql
  WITH Admissions AS (
      SELECT 
          patient_id, admission_id, discharge_date,
          LEAD(admission_date) OVER (PARTITION BY patient_id ORDER BY admission_date) AS next_admit_date
      FROM hospital_stays
  )
  SELECT patient_id, admission_id, discharge_date, next_admit_date
  FROM Admissions
  WHERE next_admit_date IS NOT NULL 
    AND next_admit_date - discharge_date <= INTERVAL '30 days';
  ```

---

#### Q44. Top 5% High-Value Transactions
- **Business Question**: Retrieve transactions belonging to the top 5th percentile of transaction amount.
- **Difficulty**: Medium | **Target Time**: 3 min
- **SQL Solution**:
  ```sql
  WITH Percentiles AS (
      SELECT 
          tx_id, amount,
          PERCENT_RANK() OVER (ORDER BY amount) AS p_rank
      FROM pos_transactions
  )
  SELECT tx_id, amount
  FROM Percentiles
  WHERE p_rank >= 0.95;
  ```

---

#### Q45. Vendor On-Time Delivery Rate
- **Business Question**: Calculate on-time in-full (OTIF) percentage per vendor.
- **Difficulty**: Easy | **Target Time**: 3 min
- **SQL Solution**:
  ```sql
  SELECT 
      vendor_id,
      COUNT(po_id) AS total_orders,
      ROUND(
          SUM(CASE WHEN actual_delivery_date <= promised_delivery_date AND fulfilled_qty >= ordered_qty THEN 1 ELSE 0 END) * 100.0 / 
          COUNT(po_id), 2
      ) AS otif_rate_pct
  FROM purchase_orders
  GROUP BY vendor_id;
  ```

---

#### Q46. Rolling 12-Month Customer Spend (Annual Rolling Window)
- **Business Question**: Calculate trailing 12-month spend for each transaction date.
- **Difficulty**: Medium | **Target Time**: 4 min
- **SQL Solution**:
  ```sql
  SELECT 
      customer_id, tx_date, amount,
      SUM(amount) OVER (
          PARTITION BY customer_id 
          ORDER BY tx_date 
          RANGE BETWEEN INTERVAL '365 days' PRECEDING AND CURRENT ROW
      ) AS trailing_365d_spend
  FROM customer_transactions;
  ```

---

#### Q47. Detecting Shift Inversions (Data Quality Check)
- **Business Question**: Find records where start timestamp is greater than end timestamp.
- **Difficulty**: Easy | **Target Time**: 1 min
- **SQL Solution**:
  ```sql
  SELECT session_id, user_id, start_time, end_time
  FROM user_sessions
  WHERE start_time > end_time;
  ```

---

#### Q48. Identifying Discontinued SKUs with Residual Stock
- **Business Question**: Find discontinued products that still have positive warehouse inventory.
- **Difficulty**: Easy | **Target Time**: 2 min
- **SQL Solution**:
  ```sql
  SELECT p.product_id, p.product_name, i.stock_quantity
  FROM products p
  JOIN inventory i ON p.product_id = i.product_id
  WHERE p.is_discontinued = 1 AND i.stock_quantity > 0;
  ```

---

#### Q49. Customer Return Rate by Product Category
- **Business Question**: Calculate return rate percentage per merchandise category.
- **Difficulty**: Medium | **Target Time**: 3 min
- **SQL Solution**:
  ```sql
  SELECT 
      p.category_name,
      COUNT(oi.order_item_id) AS total_units_sold,
      SUM(CASE WHEN oi.return_flag = 1 THEN 1 ELSE 0 END) AS returned_units,
      ROUND(SUM(CASE WHEN oi.return_flag = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(oi.order_item_id), 2) AS return_rate_pct
  FROM order_items oi
  JOIN products p ON oi.product_id = p.product_id
  GROUP BY p.category_name;
  ```

---

#### Q50. Executive Summary: RFM (Recency, Frequency, Monetary) Segmentation
- **Business Question**: Generate an RFM segmentation score (1 to 5) for every customer.
- **Difficulty**: Hard | **Target Time**: 6 min
- **SQL Solution**:
  ```sql
  WITH CustomerMetrics AS (
      SELECT 
          customer_id,
          CURRENT_DATE - MAX(order_date) AS recency_days,
          COUNT(order_id) AS frequency_orders,
          SUM(order_amount) AS monetary_spend
      FROM orders
      GROUP BY customer_id
  )
  SELECT 
      customer_id,
      recency_days, frequency_orders, monetary_spend,
      NTILE(5) OVER (ORDER BY recency_days ASC) AS R_Score,    -- Lower recency days = higher score
      NTILE(5) OVER (ORDER BY frequency_orders DESC) AS F_Score,-- Higher orders = higher score
      NTILE(5) OVER (ORDER BY monetary_spend DESC) AS M_Score   -- Higher spend = higher score
  FROM CustomerMetrics;
  ```
