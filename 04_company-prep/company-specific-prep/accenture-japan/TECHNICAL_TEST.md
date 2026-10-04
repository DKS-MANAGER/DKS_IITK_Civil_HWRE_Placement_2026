# Technology / Technical / Coding Test — Master Prep & Mock System

> **Document Status**: Complete Mock Assessment & Technical Preparation Suite  
> **Target Role**: Digital Consultant, Accenture Japan Ltd.  
> **Platform & Format**: Designated Online Platform (`[JD VERIFIED]`), Timed Sectional Test.

---

## 1. Test Overview & Structure

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                       TECHNICAL TEST STRUCTURE                              │
├──────────────────────────────┬──────────────────────────────┬───────────────┤
│ Section 1: Coding & Logic    │ Section 2: Data & SQL        │ Section 3: Tech│
│ Fundamentals (Python/C++)    │ Analytics                    │ Comprehension │
│ (Array/String/Algorithms)    │ (Queries/Tables/Aggregates)  │ (Cloud/AI/IoT)│
└──────────────────────────────┴──────────────────────────────┴───────────────┘
```

---

## 2. Section 1 — Coding & Algorithmic Logic

### Question 1.1: System Log Timestamp Anomaly Detection
* **Difficulty**: Easy-Medium
* **Estimated Time**: 8 Minutes
* **Problem**: Given an array of integers `timestamps` representing server log access times in seconds (sorted in non-decreasing order), write a function `find_latency_spikes(timestamps, threshold)` that returns the indices of all logs where the gap between consecutive timestamps exceeds `threshold` seconds.
* **Input**: `timestamps = [10, 12, 15, 45, 48, 90]`, `threshold = 20`
* **Output**: `[3, 5]` (Gap between 15 and 45 is 30 > 20; gap between 48 and 90 is 42 > 20).

#### Solution (Python 3):
```python
def find_latency_spikes(timestamps: list[int], threshold: int) -> list[int]:
    if not timestamps or len(timestamps) < 2:
        return []
    
    spike_indices = []
    for i in range(1, len(timestamps)):
        if timestamps[i] - timestamps[i - 1] > threshold:
            spike_indices.append(i)
            
    return spike_indices

# Test run
print(find_latency_spikes([10, 12, 15, 45, 48, 90], 20)) # Expected: [3, 5]
```
* **Explanation**: We iterate through the list starting from index 1 and compare each timestamp with its predecessor. If the difference is strictly greater than `threshold`, we record the current index. Time Complexity: \(O(N)\), Space Complexity: \(O(1)\) aux.

---

### Question 1.2: Customer Session Inactivity Timeout
* **Difficulty**: Medium
* **Estimated Time**: 10 Minutes
* **Problem**: Write a function `longest_active_window(events)` that takes a string of binary events where `'1'` represents active user interaction and `'0'` represents idle time. Return the length of the longest contiguous sequence of active interactions `'1'` allowing at most **one** idle `'0'` to be converted to active `'1'` (representing user session auto-keep-alive).
* **Input**: `events = "110110111"`
* **Output**: `5` (Flipping the first `'0'` yields `"11111"`, length 5).

#### Solution (Python 3):
```python
def longest_active_window(events: str) -> int:
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

# Test run
print(longest_active_window("110110111")) # Expected: 5
```
* **Explanation**: We use a sliding window approach with two pointers (`left` and `right`). We expand `right` and track the count of zeros in the current window. If `zero_count > 1`, we shrink `left` until `zero_count <= 1`. The maximum window size seen is the answer. Time Complexity: \(O(N)\), Space Complexity: \(O(1)\).

---

## 3. Section 2 — Data & SQL Analytics

### Question 2.1: Cloud Server Resource Utilization SQL
* **Difficulty**: Medium
* **Estimated Time**: 7 Minutes
* **Problem**: Given a database table `server_metrics`:

```text
Table: server_metrics
+-------------+-------------+---------------+---------------------+
| server_id   | region      | cpu_usage_pct | recorded_at         |
+-------------+-------------+---------------+---------------------+
| srv-tokyo-1 | ap-northeast| 88.5          | 2026-10-01 10:00:00 |
| srv-tokyo-2 | ap-northeast| 42.0          | 2026-10-01 10:00:00 |
| srv-osaka-1 | ap-northeast| 92.1          | 2026-10-01 10:00:00 |
| srv-tokyo-1 | ap-northeast| 91.0          | 2026-10-01 10:05:00 |
+-------------+-------------+---------------+---------------------+
```

Write an ANSI SQL query to output each `region` and the `average_cpu_usage` rounded to 2 decimal places, considering ONLY servers where `cpu_usage_pct >= 80.0`. Group the results by `region` and order by `average_cpu_usage` descending.

#### Solution (SQL):
```sql
SELECT 
    region,
    ROUND(AVG(cpu_usage_pct), 2) AS average_cpu_usage
FROM server_metrics
WHERE cpu_usage_pct >= 80.0
GROUP BY region
ORDER BY average_cpu_usage DESC;
```
* **Explanation**: The `WHERE` clause filters out non-critical metrics before aggregation. `AVG()` computes the mean for remaining high-utilization metrics per region, and `ROUND(..., 2)` formats the result.

---

## 4. Section 3 — Technology & Architecture Comprehension

### Question 3.1: Cloud Deployment Architecture Trade-off
* **Difficulty**: Easy-Medium
* **Estimated Time**: 5 Minutes
* **Scenario**: A Tokyo-based retail client with 500 physical stores wants to modernize their point-of-sale (POS) system. They currently experience severe transaction slowdowns during seasonal sale spikes. They are deciding between:
  * Option A: Deploying monolithic software on local store servers.
  * Option B: Migrating to a Cloud-Native Serverless Microservices Architecture (AWS Lambda / Azure Functions) with edge caching.
* **Question**: Explain why Option B provides better scalability and cost efficiency for peak seasonal sales.

#### Answer & Explanation:
1. **Elastic Scalability**: Serverless functions automatically scale horizontally up to thousands of concurrent transaction requests during flash sales without requiring manual server provisioning.
2. **Cost Efficiency (OpEx)**: Instead of maintaining high-capacity local servers idling at 10% capacity during off-peak months (CapEx waste), serverless follows a pay-per-execution pricing model, drastically reducing annual operating costs.
3. **Resilience**: Edge caching ensures store POS terminals process payments locally even if primary cloud connectivity drops intermittently.

---

## 5. Technical Test Practice Checklist

- [ ] Practice 10 Array & String manipulation problems in Python or C++.
- [ ] Review basic SQL queries (`JOIN`, `GROUP BY`, `HAVING`, `CASE WHEN`).
- [ ] Review Cloud concepts (IaaS vs PaaS vs SaaS, Public vs Hybrid Cloud).
- [ ] Review IoT & AI terminology (Edge AI, RAG, Digital Twin, Predictive Maintenance).
