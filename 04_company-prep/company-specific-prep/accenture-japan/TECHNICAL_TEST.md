# Technology, Technical & Coding Test — Master Study & Practice Suite

> **Document Status**: Complete Technical Assessment Practice Bank  
> **Target Role**: Digital Consultant, Accenture Japan Ltd. (`[JD VERIFIED]`)  
> **Platform & Format**: Designated Online Platform (`[JD VERIFIED]`), Timed Sectional Assessment  
> **Classification**: `[PREPARATION RECOMMENDATION]` for problem structures; `[PRACTICE ASSUMPTION]` for synthetic schemas and data.

---

## 1. Assessment Overview & Test Architecture

The Technical / Coding Test at Accenture Japan evaluates quantitative thinking, data querying precision, and programming fundamentals across three primary sections:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                       TECHNICAL TEST STRUCTURE                              │
├──────────────────────────────┬──────────────────────────────┬───────────────┤
│ SECTION 1: SQL & Data        │ SECTION 2: Python Coding &   │ SECTION 3:    │
│ Analytics (30 Problems)      │ Algorithmic Logic (20 Probs) │ Quant & Math  │
│ Multi-table, CTEs, Windows   │ Sliding window, Hash, Arrays │ (20 Problems) │
└──────────────────────────────┴──────────────────────────────┴───────────────┘
```

---

## 2. Section 1: SQL & Data Analytics (30 Enterprise Problems)

All 30 SQL queries are formulated against the following **Synthetic Enterprise Digital Transformation Schema** (`[PRACTICE ASSUMPTION]`):

### Relational Schema Definition
```sql
-- 1. Clients Table (Grain: 1 row per enterprise client)
CREATE TABLE clients (
    client_id INT PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    industry VARCHAR(50) NOT NULL,            -- 'Automotive', 'Banking', 'Retail', 'Insurance', 'Healthcare'
    region VARCHAR(50) NOT NULL,              -- 'Tokyo', 'Osaka', 'Nagoya', 'Fukuoka'
    onboarded_date DATE NOT NULL
);

-- 2. Digital Projects Table (Grain: 1 row per consulting engagement)
CREATE TABLE digital_projects (
    project_id INT PRIMARY KEY,
    client_id INT NOT NULL REFERENCES clients(client_id),
    project_name VARCHAR(150) NOT NULL,
    domain VARCHAR(50) NOT NULL,              -- 'Cloud Migration', 'Enterprise AI', 'Industry X', 'Cybersecurity', 'ERP Modernization'
    status VARCHAR(30) NOT NULL,              -- 'Planning', 'Active', 'Completed', 'Paused'
    contract_value_jpy BIGINT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE
);

-- 3. Project Milestones Table (Grain: 1 row per engagement milestone)
CREATE TABLE project_milestones (
    milestone_id INT PRIMARY KEY,
    project_id INT NOT NULL REFERENCES digital_projects(project_id),
    milestone_name VARCHAR(100) NOT NULL,
    target_date DATE NOT NULL,
    actual_completion_date DATE,
    budget_allocated_jpy BIGINT NOT NULL,
    actual_cost_jpy BIGINT NOT NULL,
    delivered_on_time_flag INT NOT NULL       -- 1 if on-time, 0 if delayed
);

-- 4. System Metrics Table (Grain: 1 row per telemetry ping per server)
CREATE TABLE system_metrics (
    metric_id INT PRIMARY KEY,
    project_id INT NOT NULL REFERENCES digital_projects(project_id),
    recorded_at TIMESTAMP NOT NULL,
    server_id VARCHAR(50) NOT NULL,
    cpu_utilization_pct NUMERIC(5,2) NOT NULL,
    memory_utilization_pct NUMERIC(5,2) NOT NULL,
    latency_ms INT NOT NULL,
    error_count INT NOT NULL
);
```

---

### Part 1A: Basic & Intermediate Queries (Problems 1–10)

#### Problem 1: High-Value Engagements by Industry
* **Task**: List each `industry` with total contract value in JPY and the count of active projects. Filter for industries with at least 2 active projects. Order by total contract value descending.
```sql
SELECT 
    c.industry,
    COUNT(p.project_id) AS active_project_count,
    SUM(p.contract_value_jpy) AS total_contract_value_jpy
FROM clients c
JOIN digital_projects p ON c.client_id = p.client_id
WHERE p.status = 'Active'
GROUP BY c.industry
HAVING COUNT(p.project_id) >= 2
ORDER BY total_contract_value_jpy DESC;
```
* **Explanation**: Uses `JOIN`, `WHERE` to pre-filter active projects, `GROUP BY` to aggregate by industry, and `HAVING` to enforce the minimum project threshold.

#### Problem 2: Budget Variance Analysis
* **Task**: For each completed project, calculate the total budget allocated, total actual cost, and cost overrun percentage: `((total_actual - total_budget) / total_budget) * 100`. Only show projects with cost overruns $> 10\%$.
```sql
SELECT 
    p.project_id,
    p.project_name,
    SUM(m.budget_allocated_jpy) AS total_budget,
    SUM(m.actual_cost_jpy) AS total_actual_cost,
    ROUND(((SUM(m.actual_cost_jpy) - SUM(m.budget_allocated_jpy)) * 100.0) / 
          NULLIF(SUM(m.budget_allocated_jpy), 0), 2) AS overrun_pct
FROM digital_projects p
JOIN project_milestones m ON p.project_id = m.project_id
WHERE p.status = 'Completed'
GROUP BY p.project_id, p.project_name
HAVING ((SUM(m.actual_cost_jpy) - SUM(m.budget_allocated_jpy)) * 100.0) / 
       NULLIF(SUM(m.budget_allocated_jpy), 0) > 10.0
ORDER BY overrun_pct DESC;
```
* **Explanation**: Protects against divide-by-zero using `NULLIF` and computes aggregate cost overrun per completed engagement.

#### Problem 3: Client Onboarding Milestone SLA
* **Task**: Find the on-time delivery rate (percentage of milestones where `delivered_on_time_flag = 1`) for each client company. Round to 1 decimal place and sort by rate descending.
```sql
SELECT 
    c.company_name,
    COUNT(m.milestone_id) AS total_milestones,
    ROUND(SUM(m.delivered_on_time_flag) * 100.0 / NULLIF(COUNT(m.milestone_id), 0), 1) AS on_time_rate_pct
FROM clients c
JOIN digital_projects p ON c.client_id = p.client_id
JOIN project_milestones m ON p.project_id = m.project_id
GROUP BY c.client_id, c.company_name
ORDER BY on_time_rate_pct DESC;
```

#### Problem 4: Server Peak Latency Anomaly Detection
* **Task**: Find servers that recorded an average `latency_ms` $> 250$ and total `error_count` $> 50$ on `'2026-10-01'`.
```sql
SELECT 
    server_id,
    ROUND(AVG(latency_ms), 2) AS avg_latency_ms,
    SUM(error_count) AS total_errors
FROM system_metrics
WHERE recorded_at >= '2026-10-01 00:00:00' 
  AND recorded_at < '2026-10-02 00:00:00'
GROUP BY server_id
HAVING AVG(latency_ms) > 250 AND SUM(error_count) > 50
ORDER BY total_errors DESC;
```

#### Problem 5: Regional Engagement Distribution
* **Task**: Output the number of clients, distinct project domains, and total contract value per `region`.
```sql
SELECT 
    c.region,
    COUNT(DISTINCT c.client_id) AS client_count,
    COUNT(DISTINCT p.domain) AS distinct_domains,
    COALESCE(SUM(p.contract_value_jpy), 0) AS total_regional_contract_jpy
FROM clients c
LEFT JOIN digital_projects p ON c.client_id = p.client_id
GROUP BY c.region
ORDER BY total_regional_contract_jpy DESC;
```

#### Problem 6: Unassigned Clients (Zero Engagements)
* **Task**: Identify clients who have been onboarded for over 90 days but have zero projects logged.
```sql
SELECT 
    c.client_id,
    c.company_name,
    c.onboarded_date
FROM clients c
LEFT JOIN digital_projects p ON c.client_id = p.client_id
WHERE p.project_id IS NULL
  AND c.onboarded_date <= CURRENT_DATE - INTERVAL '90 days';
```

#### Problem 7: Average Project Duration by Domain
* **Task**: Calculate the average duration in days for completed projects across each `domain`.
```sql
SELECT 
    domain,
    COUNT(project_id) AS completed_projects,
    ROUND(AVG(end_date - start_date), 1) AS avg_duration_days
FROM digital_projects
WHERE status = 'Completed' AND end_date IS NOT NULL
GROUP BY domain
ORDER BY avg_duration_days DESC;
```

#### Problem 8: Multi-Domain Clients
* **Task**: Find clients that have contracted projects across at least 3 distinct digital `domain`s.
```sql
SELECT 
    c.client_id,
    c.company_name,
    COUNT(DISTINCT p.domain) AS domain_count
FROM clients c
JOIN digital_projects p ON c.client_id = p.client_id
GROUP BY c.client_id, c.company_name
HAVING COUNT(DISTINCT p.domain) >= 3;
```

#### Problem 9: Critical Resource Saturation Hours
* **Task**: Count how many hourly records exhibited both `cpu_utilization_pct > 90.0` and `memory_utilization_pct > 85.0` per project.
```sql
SELECT 
    project_id,
    COUNT(*) AS saturation_pings_count,
    ROUND(AVG(cpu_utilization_pct), 2) AS avg_saturation_cpu
FROM system_metrics
WHERE cpu_utilization_pct > 90.0 AND memory_utilization_pct > 85.0
GROUP BY project_id
ORDER BY saturation_pings_count DESC;
```

#### Problem 10: Milestone Delay Days Summary
* **Task**: For milestones completed after their `target_date`, compute the average delay in days per domain.
```sql
SELECT 
    p.domain,
    COUNT(m.milestone_id) AS delayed_milestones,
    ROUND(AVG(m.actual_completion_date - m.target_date), 1) AS avg_delay_days
FROM digital_projects p
JOIN project_milestones m ON p.project_id = m.project_id
WHERE m.actual_completion_date > m.target_date
GROUP BY p.domain
ORDER BY avg_delay_days DESC;
```

---

### Part 1B: Advanced Analytical & Window Functions (Problems 11–20)

#### Problem 11: Top-2 Most Valuable Projects per Industry (`DENSE_RANK`)
* **Task**: For each industry, return the top-2 projects by `contract_value_jpy`. Include ties without skipping rank numbers.
```sql
WITH RankedProjects AS (
    SELECT 
        c.industry,
        p.project_name,
        p.contract_value_jpy,
        DENSE_RANK() OVER (
            PARTITION BY c.industry 
            ORDER BY p.contract_value_jpy DESC
        ) AS rnk
    FROM clients c
    JOIN digital_projects p ON c.client_id = p.client_id
)
SELECT 
    industry,
    project_name,
    contract_value_jpy,
    rnk
FROM RankedProjects
WHERE rnk <= 2
ORDER BY industry, rnk;
```
* **Explanation**: Uses `DENSE_RANK()` partitioned by industry so that projects with equal values share the same rank without creating gaps.

#### Problem 12: Month-over-Month Telemetry Error Growth (`LAG`)
* **Task**: Calculate the total errors recorded per month for each server, and the month-over-month percentage change in errors.
```sql
WITH MonthlyErrors AS (
    SELECT 
        server_id,
        DATE_TRUNC('month', recorded_at) AS metric_month,
        SUM(error_count) AS monthly_errors
    FROM system_metrics
    GROUP BY server_id, DATE_TRUNC('month', recorded_at)
),
MoMGrowth AS (
    SELECT 
        server_id,
        metric_month,
        monthly_errors,
        LAG(monthly_errors) OVER (
            PARTITION BY server_id 
            ORDER BY metric_month
        ) AS prev_month_errors
    FROM MonthlyErrors
)
SELECT 
    server_id,
    metric_month,
    monthly_errors,
    prev_month_errors,
    ROUND(((monthly_errors - prev_month_errors) * 100.0) / 
          NULLIF(prev_month_errors, 0), 2) AS mom_growth_pct
FROM MoMGrowth
ORDER BY server_id, metric_month;
```

#### Problem 13: Running Cumulative Milestone Spend
* **Task**: For each project, compute the running cumulative sum of `actual_cost_jpy` ordered by `actual_completion_date`.
```sql
SELECT 
    project_id,
    milestone_name,
    actual_completion_date,
    actual_cost_jpy,
    SUM(actual_cost_jpy) OVER (
        PARTITION BY project_id 
        ORDER BY actual_completion_date 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_cumulative_cost_jpy
FROM project_milestones
WHERE actual_completion_date IS NOT NULL
ORDER BY project_id, actual_completion_date;
```

#### Problem 14: Moving Average Latency (3-Period Rolling Window)
* **Task**: Compute the 3-reading centered moving average of `latency_ms` for each server.
```sql
SELECT 
    server_id,
    recorded_at,
    latency_ms,
    ROUND(AVG(latency_ms) OVER (
        PARTITION BY server_id 
        ORDER BY recorded_at 
        ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    ), 1) AS moving_avg_latency_ms
FROM system_metrics
ORDER BY server_id, recorded_at;
```

#### Problem 15: Milestone Lead Time to Next Milestone (`LEAD`)
* **Task**: For each project, calculate the gap in days between the current milestone's target date and the subsequent milestone's target date.
```sql
SELECT 
    project_id,
    milestone_name,
    target_date,
    LEAD(target_date) OVER (
        PARTITION BY project_id 
        ORDER BY target_date
    ) AS next_milestone_date,
    LEAD(target_date) OVER (
        PARTITION BY project_id 
        ORDER BY target_date
    ) - target_date AS gap_days_to_next
FROM project_milestones
ORDER BY project_id, target_date;
```

#### Problem 16: First and Last Completed Milestone per Engagement
* **Task**: Using `FIRST_VALUE` and `LAST_VALUE`, display for each milestone the earliest and latest completed milestone names for that project.
```sql
SELECT 
    project_id,
    milestone_name,
    actual_completion_date,
    FIRST_VALUE(milestone_name) OVER (
        PARTITION BY project_id 
        ORDER BY actual_completion_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS earliest_milestone,
    LAST_VALUE(milestone_name) OVER (
        PARTITION BY project_id 
        ORDER BY actual_completion_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS latest_milestone
FROM project_milestones
WHERE actual_completion_date IS NOT NULL;
```

#### Problem 17: Client Decile by Contract Value (`NTILE`)
* **Task**: Segment all clients into 4 quartiles based on their total contracted value across all projects.
```sql
WITH ClientSpend AS (
    SELECT 
        c.client_id,
        c.company_name,
        COALESCE(SUM(p.contract_value_jpy), 0) AS total_spend_jpy
    FROM clients c
    LEFT JOIN digital_projects p ON c.client_id = p.client_id
    GROUP BY c.client_id, c.company_name
)
SELECT 
    client_id,
    company_name,
    total_spend_jpy,
    NTILE(4) OVER (ORDER BY total_spend_jpy DESC) AS spend_quartile
FROM ClientSpend;
```

#### Problem 18: Consecutive Anomaly Streak Counter
* **Task**: Identify consecutive telemetry records for a server where `cpu_utilization_pct > 85.0`.
```sql
WITH FlaggedPings AS (
    SELECT 
        metric_id,
        server_id,
        recorded_at,
        cpu_utilization_pct,
        CASE WHEN cpu_utilization_pct > 85.0 THEN 1 ELSE 0 END AS is_high
    FROM system_metrics
),
GroupedStreaks AS (
    SELECT 
        metric_id,
        server_id,
        recorded_at,
        cpu_utilization_pct,
        ROW_NUMBER() OVER (PARTITION BY server_id ORDER BY recorded_at) - 
        ROW_NUMBER() OVER (PARTITION BY server_id, is_high ORDER BY recorded_at) AS streak_grp,
        is_high
    FROM FlaggedPings
)
SELECT 
    server_id,
    COUNT(*) AS consecutive_high_cpu_pings,
    MIN(recorded_at) AS streak_start,
    MAX(recorded_at) AS streak_end
FROM GroupedStreaks
WHERE is_high = 1
GROUP BY server_id, streak_grp
HAVING COUNT(*) >= 3
ORDER BY consecutive_high_cpu_pings DESC;
```

#### Problem 19: Percentage Contribution to Regional Revenue
* **Task**: For each project, compute what percentage its contract value represents of the total contract value in its client's region.
```sql
SELECT 
    c.region,
    p.project_name,
    p.contract_value_jpy,
    ROUND(p.contract_value_jpy * 100.0 / 
          SUM(p.contract_value_jpy) OVER (PARTITION BY c.region), 2) AS regional_revenue_share_pct
FROM clients c
JOIN digital_projects p ON c.client_id = p.client_id
ORDER BY c.region, regional_revenue_share_pct DESC;
```

#### Problem 20: Difference from Industry Average Project Size
* **Task**: For each project, calculate the difference between its contract value and the mean contract value of its industry.
```sql
SELECT 
    c.industry,
    p.project_name,
    p.contract_value_jpy,
    ROUND(AVG(p.contract_value_jpy) OVER (PARTITION BY c.industry), 0) AS industry_avg_contract,
    p.contract_value_jpy - ROUND(AVG(p.contract_value_jpy) OVER (PARTITION BY c.industry), 0) AS diff_from_industry_avg
FROM clients c
JOIN digital_projects p ON c.client_id = p.client_id
ORDER BY c.industry, diff_from_industry_avg DESC;
```

---

### Part 1C: Complex Business Transformations (Problems 21–30)

#### Problem 21: Customer Cohort Retention (Year-Over-Year)
* **Task**: Group clients by onboarding year (cohort), and count how many active projects each cohort generated in subsequent calendar years.
```sql
SELECT 
    EXTRACT(YEAR FROM c.onboarded_date) AS cohort_year,
    EXTRACT(YEAR FROM p.start_date) AS activity_year,
    COUNT(DISTINCT c.client_id) AS active_clients,
    COUNT(p.project_id) AS total_projects_initiated,
    SUM(p.contract_value_jpy) AS total_cohort_revenue
FROM clients c
JOIN digital_projects p ON c.client_id = p.client_id
GROUP BY EXTRACT(YEAR FROM c.onboarded_date), EXTRACT(YEAR FROM p.start_date)
ORDER BY cohort_year, activity_year;
```

#### Problem 22: Identifying Projects with Negative Margin Risk
* **Task**: Identify active projects where total spent on completed milestones already exceeds 80% of total allocated contract value while $< 50\%$ of milestones are complete.
```sql
WITH MilestoneSummary AS (
    SELECT 
        project_id,
        COUNT(milestone_id) AS total_milestones,
        SUM(CASE WHEN actual_completion_date IS NOT NULL THEN 1 ELSE 0 END) AS completed_milestones,
        SUM(actual_cost_jpy) AS cumulative_spent
    FROM project_milestones
    GROUP BY project_id
)
SELECT 
    p.project_id,
    p.project_name,
    p.contract_value_jpy,
    m.cumulative_spent,
    ROUND(m.cumulative_spent * 100.0 / NULLIF(p.contract_value_jpy, 0), 1) AS budget_consumed_pct,
    ROUND(m.completed_milestones * 100.0 / NULLIF(m.total_milestones, 0), 1) AS progress_pct
FROM digital_projects p
JOIN MilestoneSummary m ON p.project_id = m.project_id
WHERE p.status = 'Active'
  AND (m.cumulative_spent * 1.0 / NULLIF(p.contract_value_jpy, 0)) > 0.80
  AND (m.completed_milestones * 1.0 / NULLIF(m.total_milestones, 0)) < 0.50;
```

#### Problem 23: Top Error Producing Hours of Day
* **Task**: Find which hour of the day (0–23) across the entire fleet generates the highest total error count and average latency.
```sql
SELECT 
    EXTRACT(HOUR FROM recorded_at) AS hour_of_day,
    SUM(error_count) AS total_errors,
    ROUND(AVG(latency_ms), 1) AS avg_latency_ms,
    ROUND(AVG(cpu_utilization_pct), 1) AS avg_cpu_pct
FROM system_metrics
GROUP BY EXTRACT(HOUR FROM recorded_at)
ORDER BY total_errors DESC;
```

#### Problem 24: Pivot Domains by Region (Conditional Aggregation)
* **Task**: Create a matrix showing total contract value in JPY for 'Cloud Migration', 'Enterprise AI', and 'Industry X' across each region.
```sql
SELECT 
    c.region,
    COALESCE(SUM(CASE WHEN p.domain = 'Cloud Migration' THEN p.contract_value_jpy ELSE 0 END), 0) AS cloud_jpy,
    COALESCE(SUM(CASE WHEN p.domain = 'Enterprise AI' THEN p.contract_value_jpy ELSE 0 END), 0) AS ai_jpy,
    COALESCE(SUM(CASE WHEN p.domain = 'Industry X' THEN p.contract_value_jpy ELSE 0 END), 0) AS industry_x_jpy,
    COALESCE(SUM(p.contract_value_jpy), 0) AS total_jpy
FROM clients c
LEFT JOIN digital_projects p ON c.client_id = p.client_id
GROUP BY c.region
ORDER BY total_jpy DESC;
```

#### Problem 25: Identifying Clients with Zero On-Time Milestones
* **Task**: List clients who have contracted at least 2 projects, but have a 0% milestone on-time delivery rate.
```sql
SELECT 
    c.client_id,
    c.company_name,
    COUNT(DISTINCT p.project_id) AS project_count,
    COUNT(m.milestone_id) AS total_milestones
FROM clients c
JOIN digital_projects p ON c.client_id = p.client_id
JOIN project_milestones m ON p.project_id = m.project_id
GROUP BY c.client_id, c.company_name
HAVING COUNT(DISTINCT p.project_id) >= 2
   AND SUM(m.delivered_on_time_flag) = 0;
```

#### Problem 26: Deduplicating Concurrent Telemetry Logs
* **Task**: Write a deduplication query to return only the single most recent metric ping per server per minute.
```sql
WITH DeduplicatedPings AS (
    SELECT 
        metric_id,
        server_id,
        recorded_at,
        cpu_utilization_pct,
        memory_utilization_pct,
        ROW_NUMBER() OVER (
            PARTITION BY server_id, DATE_TRUNC('minute', recorded_at) 
            ORDER BY recorded_at DESC, metric_id DESC
        ) AS row_num
    FROM system_metrics
)
SELECT 
    metric_id,
    server_id,
    recorded_at,
    cpu_utilization_pct,
    memory_utilization_pct
FROM DeduplicatedPings
WHERE row_num = 1;
```

#### Problem 27: Cross-Join Industry Matrix Gap Analysis
* **Task**: Identify which combinations of `region` and `industry` currently have zero active digital projects.
```sql
WITH AllCombinations AS (
    SELECT DISTINCT r.region, i.industry
    FROM (SELECT DISTINCT region FROM clients) r
    CROSS JOIN (SELECT DISTINCT industry FROM clients) i
),
ActiveCombinations AS (
    SELECT DISTINCT c.region, c.industry
    FROM clients c
    JOIN digital_projects p ON c.client_id = p.client_id
    WHERE p.status = 'Active'
)
SELECT 
    a.region,
    a.industry AS unserved_industry
FROM AllCombinations a
LEFT JOIN ActiveCombinations act 
  ON a.region = act.region AND a.industry = act.industry
WHERE act.industry IS NULL
ORDER BY a.region, a.industry;
```

#### Problem 28: Rolling 7-Day Latency Peak
* **Task**: Calculate the maximum hourly latency recorded in the preceding 7 days for each server.
```sql
SELECT 
    server_id,
    recorded_at,
    latency_ms,
    MAX(latency_ms) OVER (
        PARTITION BY server_id 
        ORDER BY recorded_at 
        RANGE BETWEEN INTERVAL '7 days' PRECEDING AND CURRENT ROW
    ) AS max_latency_last_7_days
FROM system_metrics;
```

#### Problem 29: Fastest Milestone Completion per Engagement
* **Task**: Find the milestone that was completed in the fewest days relative to its target date (earliest completion before deadline).
```sql
WITH RankedEarlyMilestones AS (
    SELECT 
        project_id,
        milestone_name,
        target_date - actual_completion_date AS days_ahead_of_schedule,
        ROW_NUMBER() OVER (
            PARTITION BY project_id 
            ORDER BY (target_date - actual_completion_date) DESC
        ) AS rnk
    FROM project_milestones
    WHERE actual_completion_date IS NOT NULL 
      AND actual_completion_date <= target_date
)
SELECT 
    project_id,
    milestone_name,
    days_ahead_of_schedule
FROM RankedEarlyMilestones
WHERE rnk = 1;
```

#### Problem 30: Overall Engagement Health Scorecard
* **Task**: Build an executive summary query outputting each project's name, domain, on-time percentage, budget adherence percentage (`budget / actual * 100`), and a status label (`'HEALTHY'`, `'AT RISK'`, `'CRITICAL'`).
```sql
SELECT 
    p.project_name,
    p.domain,
    ROUND(SUM(m.delivered_on_time_flag) * 100.0 / NULLIF(COUNT(m.milestone_id), 0), 1) AS on_time_pct,
    ROUND(SUM(m.budget_allocated_jpy) * 100.0 / NULLIF(SUM(m.actual_cost_jpy), 0), 1) AS budget_adherence_pct,
    CASE 
        WHEN SUM(m.delivered_on_time_flag) * 1.0 / NULLIF(COUNT(m.milestone_id), 0) >= 0.80 
         AND SUM(m.actual_cost_jpy) <= SUM(m.budget_allocated_jpy) THEN 'HEALTHY'
        WHEN SUM(m.delivered_on_time_flag) * 1.0 / NULLIF(COUNT(m.milestone_id), 0) >= 0.50 
         AND SUM(m.actual_cost_jpy) <= SUM(m.budget_allocated_jpy) * 1.15 THEN 'AT RISK'
        ELSE 'CRITICAL'
    END AS engagement_health
FROM digital_projects p
JOIN project_milestones m ON p.project_id = m.project_id
GROUP BY p.project_id, p.project_name, p.domain
ORDER BY on_time_pct ASC;
```

---

## 3. Section 2: Python Coding & Algorithmic Logic (20 Problems)

### Problem 1: Latency Spike Detector (Array & Difference)
* **Problem**: Given a sorted list of timestamps `timestamps` and a threshold integer `T`, return indices $i$ where `timestamps[i] - timestamps[i-1] > T`.
```python
def find_latency_spikes(timestamps: list[int], threshold: int) -> list[int]:
    if not timestamps or len(timestamps) < 2:
        return []
    spikes = []
    for i in range(1, len(timestamps)):
        if timestamps[i] - timestamps[i - 1] > threshold:
            spikes.append(i)
    return spikes

# Verification
assert find_latency_spikes([10, 12, 15, 45, 48, 90], 20) == [3, 5]
```
* **Complexity**: Time $O(N)$, Space $O(1)$ auxiliary.

### Problem 2: Longest Contiguous Active Session (Sliding Window)
* **Problem**: In a binary string `events` ('1' = active, '0' = idle), find the maximum length of contiguous '1's allowing at most one '0' flip.
```python
def longest_active_session(events: str) -> int:
    left = 0
    zero_count = 0
    max_len = 0
    for right in range(len(events)):
        if events[right] == '0':
            zero_count += 1
        while zero_count > 1:
            if events[left] == '0':
                zero_count -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

assert longest_active_session("110110111") == 6  # Flipping second '0' yields "111111" (length 6)
assert longest_active_session("10110") == 4
```
* **Complexity**: Time $O(N)$, Space $O(1)$.

### Problem 3: Valid API Parameter Bracket Checker (Stack)
* **Problem**: Given a string containing brackets `()`, `{}`, `[]`, determine if the string is syntactically valid.
```python
def is_valid_payload(s: str) -> bool:
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        elif char in mapping.values():
            stack.append(char)
    return not stack

assert is_valid_payload("{[()]}") == True
assert is_valid_payload("{[(])}") == False
```
* **Complexity**: Time $O(N)$, Space $O(N)$.

### Problem 4: Server Load Pair Finder (Two Sum / Hash Map)
* **Problem**: Given server CPU capacities `loads` and a target limit `target`, find two indices whose sum equals `target`.
```python
def find_balanced_pair(loads: list[int], target: int) -> list[int]:
    seen = {}
    for i, val in enumerate(loads):
        diff = target - val
        if diff in seen:
            return [seen[diff], i]
        seen[val] = i
    return []

assert find_balanced_pair([20, 35, 45, 60], 80) == [1, 2]
```
* **Complexity**: Time $O(N)$, Space $O(N)$.

### Problem 5: Group Log Messages by API Endpoint (Hash Map)
* **Problem**: Given logs formatted as `"[TIMESTAMP] [ENDPOINT] [STATUS]"`, return a dictionary counting status codes per endpoint.
```python
def aggregate_endpoint_status(logs: list[str]) -> dict[str, dict[str, int]]:
    summary = {}
    for log in logs:
        parts = log.split()
        if len(parts) >= 3:
            endpoint, status = parts[1], parts[2]
            if endpoint not in summary:
                summary[endpoint] = {}
            summary[endpoint][status] = summary[endpoint].get(status, 0) + 1
    return summary

test_logs = [
    "10:00 /api/checkout 200",
    "10:01 /api/checkout 500",
    "10:02 /api/login 200"
]
assert aggregate_endpoint_status(test_logs) == {
    "/api/checkout": {"200": 1, "500": 1},
    "/api/login": {"200": 1}
}
```
* **Complexity**: Time $O(N)$, Space $O(U)$ where $U$ is distinct endpoints.

### Problem 6: Merge Deployment Time Intervals (Intervals)
* **Problem**: Merge overlapping deployment downtime intervals `[[start, end]]`.
```python
def merge_downtime_windows(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        prev = merged[-1]
        if current[0] <= prev[1]:
            prev[1] = max(prev[1], current[1])
        else:
            merged.append(current)
    return merged

assert merge_downtime_windows([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
```
* **Complexity**: Time $O(N \log N)$, Space $O(N)$.

### Problem 7: Minimum Number of Conference Rooms for Client Meetings
* **Problem**: Given meeting intervals `[[start, end]]`, return the minimum conference rooms required.
```python
import heapq

def min_meeting_rooms(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])
    rooms = [] # min-heap storing end times
    for meeting in intervals:
        if rooms and rooms[0] <= meeting[0]:
            heapq.heappop(rooms)
        heapq.heappush(rooms, meeting[1])
    return len(rooms)

assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
```
* **Complexity**: Time $O(N \log N)$, Space $O(N)$.

### Problem 8: Moving Average from Data Stream
* **Problem**: Design a moving average stream class with window size $K$.
```python
from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.total = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.total += val
        if len(self.queue) > self.size:
            self.total -= self.queue.popleft()
        return round(self.total / len(self.queue), 2)

m = MovingAverage(3)
assert m.next(10) == 10.0
assert m.next(20) == 15.0
assert m.next(30) == 20.0
assert m.next(40) == 30.0 # (20+30+40)/3 = 30.0
```
* **Complexity**: Time $O(1)$ per operation, Space $O(K)$.

### Problem 9: Peak Memory Anomaly in Circular Buffer
* **Problem**: In a list of numbers representing circular buffer metrics, find any local peak greater than both immediate neighbors.
```python
def find_local_peak(metrics: list[int]) -> int:
    n = len(metrics)
    if n == 1:
        return 0
    for i in range(n):
        prev_val = metrics[(i - 1 + n) % n]
        next_val = metrics[(i + 1) % n]
        if metrics[i] >= prev_val and metrics[i] >= next_val:
            return i
    return -1

assert find_local_peak([10, 25, 15, 8, 30]) in [1, 4]
```
* **Complexity**: Time $O(N)$, Space $O(1)$.

### Problem 10: Top-K Frequent Error Codes (Heap)
* **Problem**: Return the $K$ most frequent error codes from a stream of HTTP error logs.
```python
from collections import Counter
import heapq

def top_k_errors(errors: list[int], k: int) -> list[int]:
    counts = Counter(errors)
    return [item[0] for item in heapq.nlargest(k, counts.items(), key=lambda x: x[1])]

assert top_k_errors([500, 404, 500, 503, 404, 500, 401], 2) == [500, 404]
```
* **Complexity**: Time $O(N + U \log K)$, Space $O(U)$.

### Problem 11: Subarray Sum Equals Target (Prefix Sums)
* **Problem**: Find the total number of continuous subarrays whose elements sum to `k`.
```python
def subarray_sum(nums: list[int], k: int) -> int:
    prefix_counts = {0: 1}
    current_sum = 0
    total_subarrays = 0
    for num in nums:
        current_sum += num
        total_subarrays += prefix_counts.get(current_sum - k, 0)
        prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1
    return total_subarrays

assert subarray_sum([1, 1, 1], 2) == 2
assert subarray_sum([1, 2, 3], 3) == 2 # [1,2] and [3]
```
* **Complexity**: Time $O(N)$, Space $O(N)$.

### Problem 12: Binary Search in Rotated Server ID List
* **Problem**: Find target ID in an ascending list rotated at an unknown pivot.
```python
def search_rotated_servers(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        # Check if left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else: # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

assert search_rotated_servers([40, 50, 60, 10, 20, 30], 20) == 4
```
* **Complexity**: Time $O(\log N)$, Space $O(1)$.

### Problem 13: LRU Cache Implementation (OrderedDict / Doubly Linked List)
* **Problem**: Implement a Least Recently Used (LRU) Cache with $O(1)$ `get` and `put`.
```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

lru = LRUCache(2)
lru.put(1, 100)
lru.put(2, 200)
assert lru.get(1) == 100
lru.put(3, 300) # Evicts key 2
assert lru.get(2) == -1
```
* **Complexity**: Time $O(1)$ for both operations, Space $O(C)$.

### Problem 14: Automated Task Dependency Topological Sort (DAG)
* **Problem**: Given tasks and prerequisite pairs `[task, prereq]`, return a valid execution order.
```python
from collections import deque

def task_schedule_order(num_tasks: int, prereqs: list[list[int]]) -> list[int]:
    adj = {i: [] for i in range(num_tasks)}
    in_degree = [0] * num_tasks
    for task, pre in prereqs:
        adj[pre].append(task)
        in_degree[task] += 1

    queue = deque([i for i in range(num_tasks) if in_degree[i] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return order if len(order) == num_tasks else []

assert task_schedule_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 1, 2, 3]
```
* **Complexity**: Time $O(V + E)$, Space $O(V + E)$.

### Problem 15: String Compression Run-Length Encoding
* **Problem**: Compress consecutive identical characters in place.
```python
def compress_telemetry_string(chars: list[str]) -> int:
    write = 0
    read = 0
    while read < len(chars):
        char = chars[read]
        count = 0
        while read < len(chars) and chars[read] == char:
            read += 1
            count += 1
        chars[write] = char
        write += 1
        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1
    return write

c = ["a", "a", "b", "b", "c", "c", "c"]
length = compress_telemetry_string(c)
assert c[:length] == ["a", "2", "b", "2", "c", "3"]
```
* **Complexity**: Time $O(N)$, Space $O(1)$.

### Problem 16: Minimum Path Latency in Grid Network (Dynamic Programming)
* **Problem**: Find minimum latency path from top-left to bottom-right moving only right and down.
```python
def min_network_latency(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    return dp[m - 1][n - 1]

assert min_network_latency([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7
```
* **Complexity**: Time $O(M \times N)$, Space $O(M \times N)$ (reducible to $O(N)$).

### Problem 17: Valid IP Address Validator
* **Problem**: Check whether an IP string is valid IPv4.
```python
def is_valid_ipv4(ip: str) -> bool:
    octets = ip.split('.')
    if len(octets) != 4:
        return False
    for octet in octets:
        if not octet.isdigit():
            return False
        if len(octet) > 1 and octet[0] == '0':
            return False
        num = int(octet)
        if num < 0 or num > 255:
            return False
    return True

assert is_valid_ipv4("192.168.1.1") == True
assert is_valid_ipv4("256.100.0.1") == False
assert is_valid_ipv4("192.168.01.1") == False
```
* **Complexity**: Time $O(1)$, Space $O(1)$.

### Problem 18: Maximum Water Trapped (Two Pointers)
* **Problem**: Calculate total rainwater trapped between building elevations.
```python
def trap_water(height: list[int]) -> int:
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0
    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]
    return water

assert trap_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
```
* **Complexity**: Time $O(N)$, Space $O(1)$.

### Problem 19: Coin Change Minimum Tokens (DP)
* **Problem**: Minimum coins needed to make up a target amount.
```python
def min_coins(coins: list[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1

assert min_coins([1, 2, 5], 11) == 3 # 5 + 5 + 1
```
* **Complexity**: Time $O(C \times A)$, Space $O(A)$.

### Problem 20: Word Break Dictionary Lookup
* **Problem**: Determine if string `s` can be segmented into a space-separated sequence of dictionary words.
```python
def word_break(s: str, word_dict: list[str]) -> bool:
    words = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[len(s)]

assert word_break("accenturejapan", ["accenture", "japan"]) == True
assert word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
```
* **Complexity**: Time $O(N^2)$, Space $O(N)$.

---

## 4. Section 3: Quantitative Aptitude & Consulting Mathematics (20 Worked Problems)

#### Problem 1: Gross & Operating Margin Reconciliation
* **Scenario**: A Tokyo SaaS firm generates JPY 1,200M in annual revenue. Hosting and data center costs (COGS) are JPY 360M. Sales, R&D, and administrative salaries (OpEx) total JPY 480M. Calculate Gross Margin and Operating Margin.
* **Calculation**:
  $$\text{Gross Profit} = 1,200 - 360 = \text{JPY } 840\text{M} \implies \text{Gross Margin} = \frac{840}{1,200} = 70.0\%$$
  $$\text{Operating Profit (EBIT)} = 840 - 480 = \text{JPY } 360\text{M} \implies \text{Operating Margin} = \frac{360}{1,200} = 30.0\%$$
* **Answer**: Gross Margin = 70.0%, Operating Margin = 30.0%.

#### Problem 2: Break-Even Volume Analysis
* **Scenario**: Deploying an IoT sensor system incurs JPY 60M in fixed annual software licensing and maintenance costs. Each monitored machine yields JPY 150,000 in monthly downtime savings, but requires JPY 30,000 in monthly maintenance overhead. How many machines must be connected to break even annually?
* **Calculation**:
  $$\text{Net Contribution per machine/year} = (150,000 - 30,000) \times 12 = \text{JPY } 1,440,000$$
  $$\text{Break-Even Count} = \frac{60,000,000}{1,440,000} = 41.67 \implies 42 \text{ machines}$$
* **Answer**: 42 machines minimum.

#### Problem 3: Customer Lifetime Value (LTV) and CAC Payback
* **Scenario**: An enterprise analytics subscription charges JPY 2,000,000 annually per client with an 80% gross margin. The annual client churn rate is 10%. Customer acquisition cost (CAC) is JPY 4,000,000. Calculate LTV, LTV/CAC ratio, and CAC payback period.
* **Calculation**:
  $$\text{LTV} = \frac{\text{Annual Gross Profit per Client}}{\text{Churn Rate}} = \frac{2,000,000 \times 0.80}{0.10} = \text{JPY } 16,000,000$$
  $$\text{LTV / CAC Ratio} = \frac{16,000,000}{4,000,000} = 4.0\text{x (Healthy)}$$
  $$\text{CAC Payback Period} = \frac{\text{CAC}}{\text{Annual Gross Profit}} = \frac{4,000,000}{1,600,000} = 2.5 \text{ years (30 months)}$$
* **Answer**: LTV = JPY 16M; LTV/CAC = 4.0x; Payback = 30 months.

#### Problem 4: Rule of 72 & Compound Annual Growth Rate (CAGR)
* **Scenario**: A digital payments platform in Japan grows transaction volume from JPY 50B to JPY 200B in 6 years. Estimate the compound annual growth rate using the Rule of 72.
* **Calculation**:
  The volume quadrupled ($2 \times 2$), meaning it doubled twice in 6 years $\implies$ Doubling time = 3 years.
  $$\text{Estimated CAGR} \approx \frac{72}{3} = 24.0\% \text{ per annum}$$
  Exact check: $(1.24)^6 \approx 3.63$; $(1 + r)^6 = 4.0 \implies r = 4^{1/6} - 1 \approx 25.99\%$.
* **Answer**: ~24% (Rule of 72 approximation) / 26.0% (exact).

#### Problem 5: Weighted Average Cost of Capital (WACC) Heuristic
* **Scenario**: A client funds a JPY 500M cloud migration with 60% equity (cost of equity = 10%) and 40% debt (cost of debt = 3%). Corporate tax rate is 30%. Calculate WACC.
* **Calculation**:
  $$\text{After-tax cost of debt} = 3\% \times (1 - 0.30) = 2.1\%$$
  $$\text{WACC} = (0.60 \times 10\%) + (0.40 \times 2.1\%) = 6.0\% + 0.84\% = 6.84\%$$
* **Answer**: 6.84%.

#### Problem 6: Server Consolidation Cost Savings
* **Scenario**: A client currently runs 200 on-premise servers at JPY 150,000/month each (power, cooling, admin). Migrating to cloud requires 40 cloud instances at JPY 300,000/month each, plus JPY 36M in one-time migration consulting fees. What is the simple payback period for migration?
* **Calculation**:
  $$\text{Current annual cost} = 200 \times 150,000 \times 12 = \text{JPY } 360\text{M}$$
  $$\text{Cloud annual cost} = 40 \times 300,000 \times 12 = \text{JPY } 144\text{M}$$
  $$\text{Annual Net Savings} = 360 - 144 = \text{JPY } 216\text{M}$$
  $$\text{Payback Period} = \frac{\text{JPY } 36\text{M}}{\text{JPY } 216\text{M}} = \frac{1}{6} \text{ year} = 2 \text{ months!}$$
* **Answer**: 2 months.

#### Problem 7: Data Transfer Egress Cost Sensitivity
* **Scenario**: Cloud egress bandwidth costs JPY 12 per GB for the first 10 TB, and JPY 9 per GB thereafter. A client transfers 25 TB monthly. What is the total monthly egress cost? (1 TB = 1,000 GB).
* **Calculation**:
  $$\text{Tier 1 (10,000 GB)} = 10,000 \times 12 = \text{JPY } 120,000$$
  $$\text{Tier 2 (15,000 GB)} = 15,000 \times 9 = \text{JPY } 135,000$$
  $$\text{Total Monthly Egress} = 120,000 + 135,000 = \text{JPY } 255,000$$
* **Answer**: JPY 255,000.

#### Problem 8: Call Center Automation ROI
* **Scenario**: A Japanese insurer handles 500,000 customer inquiries annually at JPY 1,200 per call. Deploying an AI voice agent resolves 35% of calls automatically at JPY 150 per automated call. What is the annual net cost reduction?
* **Calculation**:
  $$\text{Baseline Cost} = 500,000 \times 1,200 = \text{JPY } 600\text{M}$$
  $$\text{Automated Calls} = 500,000 \times 0.35 = 175,000 \text{ calls} \implies 175,000 \times 150 = \text{JPY } 26.25\text{M}$$
  $$\text{Human Calls Remaining} = 325,000 \times 1,200 = \text{JPY } 390\text{M}$$
  $$\text{New Total Cost} = 390 + 26.25 = \text{JPY } 416.25\text{M}$$
  $$\text{Annual Savings} = 600 - 416.25 = \text{JPY } 183.75\text{M (30.6\% reduction)}$$
* **Answer**: JPY 183.75M.

#### Problem 9: Machine Learning Classification Threshold Trade-off
* **Scenario**: A fraud detection model screens 100,000 transactions daily with 1% true fraud rate (1,000 frauds). At Threshold A: Precision = 80%, Recall = 60%. At Threshold B: Precision = 50%, Recall = 90%. If an undetected fraud costs JPY 50,000 and investigating a false positive costs JPY 1,000, which threshold minimizes daily loss?
* **Calculation**:
  * **Threshold A**:
    * Caught Frauds = $1,000 \times 0.60 = 600$. Missed Frauds = 400. Missed cost = $400 \times 50,000 = \text{JPY } 20,000,000$.
    * Total Flagged = $600 / 0.80 = 750 \implies \text{False Positives} = 150$. Investigation cost = $150 \times 1,000 = \text{JPY } 150,000$.
    * Total Cost A = JPY 20,150,000.
  * **Threshold B**:
    * Caught Frauds = $1,000 \times 0.90 = 900$. Missed Frauds = 100. Missed cost = $100 \times 50,000 = \text{JPY } 5,000,000$.
    * Total Flagged = $900 / 0.50 = 1,800 \implies \text{False Positives} = 900$. Investigation cost = $900 \times 1,000 = \text{JPY } 900,000$.
    * Total Cost B = JPY 5,900,000.
* **Answer**: Threshold B saves JPY 14.25M daily because false negative penalty heavily outweighs false positive inspection cost.

#### Problem 10: Overall Equipment Effectiveness (OEE) Calculation
* **Scenario**: An automotive parts stamping line operates 8 hours daily (480 mins) with 30 mins scheduled lunch and 50 mins unscheduled downtime. Ideal cycle time is 0.5 mins per part. Total parts produced = 700 units, of which 35 are defective. Calculate Availability, Performance, Quality, and overall OEE.
* **Calculation**:
  $$\text{Planned Operating Time} = 480 - 30 = 450 \text{ mins}$$
  $$\text{Operating Time} = 450 - 50 = 400 \text{ mins} \implies \text{Availability} = \frac{400}{450} = 88.89\%$$
  $$\text{Ideal Run Time for 700 parts} = 700 \times 0.5 = 350 \text{ mins} \implies \text{Performance} = \frac{350}{400} = 87.50\%$$
  $$\text{Good Parts} = 700 - 35 = 665 \implies \text{Quality} = \frac{665}{700} = 95.00\%$$
  $$\text{OEE} = 0.8889 \times 0.8750 \times 0.9500 = 73.89\%$$
* **Answer**: Availability = 88.9%, Performance = 87.5%, Quality = 95.0%, OEE = 73.9%.

#### Problems 11–20: Mental Math & Aptitude Blitz
* **P11 (Market Sizing Check)**: If Tokyo has 14M population with average household size of 2.0, how many households? $\implies 7.0\text{M households}$.
* **P12 (Storage Estimation)**: An IoT sensor streams 200 bytes every second across 10,000 machines. Daily raw data volume? $\implies 10,000 \times 200 \text{ bytes/s} = 2 \text{ MB/s} \times 86,400\text{s} \approx 172.8 \text{ GB/day}$.
* **P13 (Network Bandwidth)**: 2 MB/s in megabits? $\implies 2 \times 8 = 16 \text{ Mbps}$.
* **P14 (Availability SLA)**: 99.9% uptime (three nines) in an annual 365-day year allows how much downtime? $\implies 365 \times 24 \times 60 \times 0.001 = 525.6 \text{ minutes} \approx 8.76 \text{ hours}$.
* **P15 (Four Nines SLA)**: 99.99% uptime allows? $\implies 52.56 \text{ minutes/year}$.
* **P16 (Consulting Conversion Rate)**: If website conversion rate improves from 2.0% to 2.5%, what is the percentage increase? $\implies \frac{0.5}{2.0} \times 100 = 25.0\%$ increase (not 0.5%).
* **P17 (Discount Margin)**: If product margin is 40% and a 20% discount is applied to selling price, what is new gross margin? $\implies \text{Let Price} = 100, \text{Cost} = 60$. New Price = 80. Margin = $\frac{80 - 60}{80} = 25.0\%$.
* **P18 (Probability - System Availability)**: If two independent redundant servers each have 95% individual reliability, what is the probability that the system is operational? $\implies 1 - (1 - 0.95)^2 = 1 - (0.05)^2 = 1 - 0.0025 = 99.75\%$.
* **P19 (Weighted Average Cost)**: 30% of work done in Tokyo at JPY 10,000/hr, 70% in offshore center at JPY 3,000/hr. Blended hourly rate? $\implies (0.30 \times 10,000) + (0.70 \times 3,000) = 3,000 + 2,100 = \text{JPY } 5,100/\text{hr}$.
* **P20 (Data Center Power PUE)**: A data center consumes 10 MW total power, of which 7.5 MW powers actual IT equipment. What is the Power Usage Effectiveness (PUE)? $\implies \text{PUE} = \frac{\text{Total Facility Power}}{\text{IT Equipment Power}} = \frac{10}{7.5} = 1.33$ (world-class efficiency).
