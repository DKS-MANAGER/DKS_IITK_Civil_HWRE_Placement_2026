# HirePro Vibe Coding & Interactive Software Engineering Practice Module

> **Document Code**: DEL-VIBE-01  
> **Target Assessment**: HirePro Interactive Coding & Automated Software Engineering Assessments  
> **Purpose**: Hands-on simulation of modern recruitment coding environments where candidates are evaluated on modifying starter code, fixing latent bugs, satisfying enterprise requirements, passing public/hidden test suites, and writing production-grade unit tests.

---

## 1. Understanding the HirePro Assessment Platform

### 1.1 Architecture & Workflow of HirePro Coding Tests
HirePro is an enterprise-grade automated assessment platform utilized by Deloitte USI for campus technical hiring. The platform differs significantly from pure competitive programming portals:

1. **Integrated Web-Based IDE**:
   - The browser interface provides an editor (Monaco/VS Code-based) with syntax highlighting, an execution terminal, a problem description sidebar, and a test runner panel.
   - The candidate is given pre-scaffolded starter code (functions or classes) rather than an empty file.
2. **Standard I/O vs Function Stub**:
   - Some problems require implementing a specific function signature (`def process_data(records: list) -> dict:`).
   - Other tasks require reading from standard input (`sys.stdin`) and writing results to standard output (`sys.stdout`).
3. **Two-Tier Test Suite Architecture**:
   - **Public Test Cases (Visible)**: Usually 2 to 3 basic examples. You can run code against them interactively to verify baseline functionality.
   - **Hidden Test Cases (Blind)**: 5 to 10 comprehensive edge cases (null inputs, empty sequences, maximum scale bounds, negative numbers, extreme float precision) evaluated only upon final submission.
4. **Time Management & Strategy**:
   - Total coding duration is typically 45 to 60 minutes for 2 coding tasks.
   - Allocate 5 minutes to read and understand requirements, 15 minutes to implement, and 5 minutes to test edge cases per problem.
   - **Never make reckless edits in the last 2 minutes**. Always ensure your code compiles and passes all public tests before submitting.

---

## 2. Simulated Practice Task 1: Enterprise Timesheet Billing & Overtime Engine

### 2.1 Business Requirement & User Story
As a Technology Consulting Analyst at Deloitte, you are building an automated billing microservice for a global client engagement. The engine receives a batch of daily timesheet entries and must calculate:
1. **Regular Hours**: Up to 8.0 hours per calendar day for each consultant.
2. **Overtime Hours**: Any hours worked in excess of 8.0 hours in a single day, billed at $1.5\times$ the consultant's standard hourly rate.
3. **Approved Project Filtering**: If a timesheet entry references a `project_id` marked as `"Unapproved"` or `"Suspended"`, the entry must be rejected with 0 billable hours and logged under `rejected_entries`.
4. **Validation Constraints**: Hours cannot be negative or exceed 24.0 hours per day. Any invalid entry must raise a `ValueError` or be flagged in `validation_errors`.

---

### 2.2 Starter Code with Existing Latent Bugs
*(This is the starter code loaded into your HirePro editor. It contains multiple bugs that you must diagnose and fix).*

```python
# STARTER CODE (BUGGY) - DO NOT SUBMIT AS-IS
def calculate_billing(timesheet_entries, approved_projects, hourly_rates):
    billing_summary = {}
    rejected_entries = []
    
    for entry in timesheet_entries:
        emp_id = entry['emp_id']
        pid = entry['project_id']
        hrs = entry['hours']
        
        # BUG 1: Checks project existence naively without verifying status
        if pid not in approved_projects:
            rejected_entries.append(entry['entry_id'])
            continue
            
        # BUG 2: Overtime logic does not aggregate daily hours per employee
        # If an employee logs 5 hours on Project A and 5 hours on Project B on the same day,
        # overtime is missed because each entry is evaluated independently!
        if hrs > 8:
            reg_hrs = 8
            ot_hrs = hrs - 8
        else:
            reg_hrs = hrs
            ot_hrs = 0
            
        rate = hourly_rates.get(emp_id, 0)
        # BUG 3: Integer division truncates fractional hours (e.g., 7.5 hrs)
        amount = (reg_hrs * rate) + (ot_hrs * rate * 3 // 2)
        
        billing_summary[emp_id] = billing_summary.get(emp_id, 0) + amount
        
    return {"billing_summary": billing_summary, "rejected_entries": rejected_entries}
```

---

### 2.3 Explicit Acceptance Criteria
1. Must group all timesheets by `(emp_id, work_date)` prior to evaluating daily overtime thresholds.
2. Regular daily hours capped at 8.0 across all approved projects combined. Any daily aggregate above 8.0 is overtime.
3. Overtime rate is strictly $1.5 \times \text{hourly rate}$ as a floating-point calculation rounded to 2 decimal places.
4. Any entry with `hours < 0` or `hours > 24` must be logged in `validation_errors` and excluded from billing.
5. Must return a structured dictionary containing:
   - `"total_billing_by_emp"`: `{emp_id: total_amount_rounded_2_decimals}`
   - `"total_regular_hours"`: `{emp_id: float}`
   - `"total_overtime_hours"`: `{emp_id: float}`
   - `"rejected_entries"`: `[entry_id, ...]`
   - `"validation_errors"`: `[entry_id, ...]`

---

### 2.4 Test Suite

#### Public Test Case 1
```python
timesheets = [
    {"entry_id": 1, "emp_id": "E101", "project_id": "P01", "work_date": "2026-10-01", "hours": 6.0},
    {"entry_id": 2, "emp_id": "E101", "project_id": "P02", "work_date": "2026-10-01", "hours": 4.0}, # Total = 10 hrs on same date!
    {"entry_id": 3, "emp_id": "E102", "project_id": "P99", "work_date": "2026-10-01", "hours": 8.0}  # P99 is unapproved
]
approved_projects = {"P01": "Active", "P02": "Active", "P99": "Suspended"}
hourly_rates = {"E101": 100.0, "E102": 80.0}

# Expected Result:
# E101: 8 hrs regular ($800) + 2 hrs overtime (2 * 100 * 1.5 = $300) = $1100.00
# E102: Project P99 is Suspended -> Rejected -> $0.00
# Rejected entries: [3]
```

#### Hidden Test Case 2 (Edge Case: Boundary Floats & Negative Hours)
```python
timesheets = [
    {"entry_id": 10, "emp_id": "E103", "project_id": "P01", "work_date": "2026-10-02", "hours": -2.0}, # Invalid!
    {"entry_id": 11, "emp_id": "E103", "project_id": "P01", "work_date": "2026-10-02", "hours": 7.5}
]
# Expected: Entry 10 in validation_errors; Entry 11 billed at 7.5 * rate.
```

---

### 2.5 Production-Grade Fixed Solution

```python
from collections import defaultdict
from typing import List, Dict, Any

def process_enterprise_billing(
    timesheet_entries: List[Dict[str, Any]], 
    approved_projects: Dict[str, str], 
    hourly_rates: Dict[str, float]
) -> Dict[str, Any]:
    """
    Calculates enterprise billing with multi-project daily overtime aggregation.
    Time Complexity: O(N log N) or O(N) where N is number of timesheet entries.
    Space Complexity: O(N) auxiliary tracking memory.
    """
    rejected_entries = []
    validation_errors = []
    
    # Step 1: Validate individual entries and filter unapproved projects
    valid_entries_by_emp_date = defaultdict(list)
    
    for entry in timesheet_entries:
        eid = entry.get('entry_id')
        emp_id = entry.get('emp_id')
        pid = entry.get('project_id')
        hrs = entry.get('hours', 0.0)
        date = entry.get('work_date')
        
        # Check boundary validation
        if hrs < 0.0 or hrs > 24.0:
            validation_errors.append(eid)
            continue
            
        # Check project approval status
        if approved_projects.get(pid) != 'Active':
            rejected_entries.append(eid)
            continue
            
        valid_entries_by_emp_date[(emp_id, date)].append(hrs)
        
    # Step 2: Compute daily regular and overtime hours
    total_billing = defaultdict(float)
    total_reg = defaultdict(float)
    total_ot = defaultdict(float)
    
    for (emp_id, date), hours_list in valid_entries_by_emp_date.items():
        daily_total = sum(hours_list)
        rate = float(hourly_rates.get(emp_id, 0.0))
        
        if daily_total <= 8.0:
            reg_hrs = daily_total
            ot_hrs = 0.0
        else:
            reg_hrs = 8.0
            ot_hrs = daily_total - 8.0
            
        amount = (reg_hrs * rate) + (ot_hrs * rate * 1.5)
        
        total_billing[emp_id] += amount
        total_reg[emp_id] += reg_hrs
        total_ot[emp_id] += ot_hrs
        
    # Format and round outputs
    return {
        "total_billing_by_emp": {k: round(v, 2) for k, v in total_billing.items()},
        "total_regular_hours": {k: round(v, 2) for k, v in total_reg.items()},
        "total_overtime_hours": {k: round(v, 2) for k, v in total_ot.items()},
        "rejected_entries": sorted(rejected_entries),
        "validation_errors": sorted(validation_errors)
    }

# Interactive Verification
if __name__ == "__main__":
    t_test = [
        {"entry_id": 1, "emp_id": "E101", "project_id": "P01", "work_date": "2026-10-01", "hours": 6.0},
        {"entry_id": 2, "emp_id": "E101", "project_id": "P02", "work_date": "2026-10-01", "hours": 4.0},
        {"entry_id": 3, "emp_id": "E102", "project_id": "P99", "work_date": "2026-10-01", "hours": 8.0},
        {"entry_id": 4, "emp_id": "E103", "project_id": "P01", "work_date": "2026-10-02", "hours": -5.0}
    ]
    p_test = {"P01": "Active", "P02": "Active", "P99": "Suspended"}
    r_test = {"E101": 100.0, "E102": 80.0, "E103": 50.0}
    
    res = process_enterprise_billing(t_test, p_test, r_test)
    assert res["total_billing_by_emp"]["E101"] == 1100.00
    assert res["rejected_entries"] == [3]
    assert res["validation_errors"] == [4]
    print("Simulated Task 1 Passed All Test Criteria.")
```

---

## 3. Simulated Practice Task 2: Resilient REST API Telemetry Ingestion & JSON Log Normalizer

### 3.1 Business Requirement & User Story
A Deloitte data engineering team is deploying an ingestion pipeline for IoT smart-infrastructure sensors. Data arrives as raw JSON payload strings. You must construct a resilient normalizer that:
1. Deserializes JSON payloads, handling malformed syntax without terminating the application.
2. Extracts required fields: `device_id` (str), `timestamp` (ISO UTC str), `reading` (float), and `battery_pct` (int).
3. Normalizes timestamp strings to a uniform standard format (`YYYY-MM-DDTHH:MM:SSZ`).
4. Deduplicates records based on `(device_id, timestamp)`: If duplicate timestamps occur for a device, retain the record with the higher `battery_pct`.

---

### 3.2 Starter Code with Existing Latent Bugs

```python
# STARTER CODE (BUGGY)
import json

def parse_telemetry(raw_payloads):
    cleaned = []
    # BUG 1: Unhandled JSONDecodeError crashes entire batch on first malformed string
    for item in raw_payloads:
        data = json.loads(item)
        
        # BUG 2: KeyError if 'reading' or 'battery_pct' is missing from payload
        device = data['device_id']
        ts = data['timestamp']
        val = float(data['reading'])
        bat = int(data['battery_pct'])
        
        # BUG 3: Does not deduplicate records
        cleaned.append({
            "device_id": device,
            "timestamp": ts,
            "reading": val,
            "battery_pct": bat
        })
    return cleaned
```

---

### 3.3 Production-Grade Fixed Solution

```python
import json
from datetime import datetime, timezone
from typing import List, Dict, Any, Optional

def normalize_timestamp(ts_str: str) -> Optional[str]:
    """Converts various timestamp formats into uniform UTC ISO format."""
    formats = [
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%d %H:%M:%S",
        "%d/%m/%Y %H:%M:%S",
        "%Y-%m-%d"
    ]
    for fmt in formats:
        try:
            dt = datetime.strptime(ts_str.strip(), fmt)
            return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            continue
    return None

def ingest_resilient_telemetry(raw_payloads: List[str]) -> Dict[str, Any]:
    """
    Resilient telemetry ingestion pipeline with deduplication and normalization.
    Time Complexity: O(N) where N is number of raw payload strings.
    Space Complexity: O(N) deduplication hash map.
    """
    dedup_map = {}
    corrupted_count = 0
    
    for payload in raw_payloads:
        try:
            data = json.loads(payload)
            if not isinstance(data, dict):
                corrupted_count += 1
                continue
        except (json.JSONDecodeError, TypeError):
            corrupted_count += 1
            continue
            
        device_id = data.get('device_id')
        raw_ts = data.get('timestamp')
        raw_reading = data.get('reading')
        raw_battery = data.get('battery_pct')
        
        # Validate existence of essential attributes
        if not device_id or not raw_ts or raw_reading is None:
            corrupted_count += 1
            continue
            
        norm_ts = normalize_timestamp(str(raw_ts))
        if not norm_ts:
            corrupted_count += 1
            continue
            
        try:
            val = float(raw_reading)
            bat = int(raw_battery) if raw_battery is not None else 100
        except (ValueError, TypeError):
            corrupted_count += 1
            continue
            
        key = (device_id, norm_ts)
        candidate_record = {
            "device_id": device_id,
            "timestamp": norm_ts,
            "reading": round(val, 2),
            "battery_pct": bat
        }
        
        # Deduplication rule: Retain record with highest battery_pct
        if key not in dedup_map or bat > dedup_map[key]["battery_pct"]:
            dedup_map[key] = candidate_record
            
    # Sort output chronologically by timestamp, then device_id
    sorted_records = sorted(dedup_map.values(), key=lambda x: (x["timestamp"], x["device_id"]))
    
    return {
        "valid_records": sorted_records,
        "valid_count": len(sorted_records),
        "corrupted_count": corrupted_count
    }

# Verification Suite
if __name__ == "__main__":
    payloads = [
        '{"device_id": "SN-01", "timestamp": "2026-10-01 12:00:00", "reading": 23.45, "battery_pct": 80}',
        '{"device_id": "SN-01", "timestamp": "2026-10-01T12:00:00Z", "reading": 23.45, "battery_pct": 95}', # Duplicate! Higher battery
        'INVALID JSON MALFORMED PAYLOAD',
        '{"device_id": "SN-02", "timestamp": "2026-10-01 12:05:00", "reading": "corrupt"}'
    ]
    out = ingest_resilient_telemetry(payloads)
    assert out["valid_count"] == 1
    assert out["corrupted_count"] == 2
    assert out["valid_records"][0]["battery_pct"] == 95
    print("Simulated Task 2 Passed All Test Criteria.")
```

---

## 4. Simulated Practice Task 3: Hydro-Flow Anomaly Detection & Spillway Rule Engine

*(This problem directly connects the candidate's Civil/HWRE domain background to production software engineering, demonstrating how domain physics translates into algorithmic consulting code).*

### 4.1 Business Requirement & User Story
A municipal smart-water authority has commissioned Deloitte to design an automated real-time flood advisory system for a river basin. Sensor telemetry records inflow discharge rates in cubic meters per second ($m^3/s$). Your microservice must:
1. Maintain a sliding window of the last $W$ discharge readings.
2. Calculate the sample mean $\mu$ and sample standard deviation $\sigma$ of the current window.
3. Compute the z-score of the newest incoming reading: $z = \frac{x - \mu}{\sigma}$.
4. **Trigger Rules**:
   - If $|z| > 2.5$ and $\sigma > 10^{-6}$, mark reading as `"Statistical Anomaly"`.
   - If $x > \text{spillway\_threshold}$, immediately emit `"SPILLWAY_DISCHARGE_WARNING"`.
   - If $\sigma < 10^{-6}$ (all sensor readings identical), flag `"SENSOR_STUCK_FAILURE"`.

---

### 4.2 Production-Grade Fixed Solution

```python
import math
from collections import deque
from typing import List, Dict, Any

class HydroDischargeMonitor:
    def __init__(self, window_size: int, spillway_threshold: float):
        if window_size < 2:
            raise ValueError("Window size must be at least 2 for sample variance.")
        self.window_size = window_size
        self.threshold = spillway_threshold
        self.window = deque()
        self._sum = 0.0
        self._sum_sq = 0.0
        
    def process_reading(self, reading: float) -> Dict[str, Any]:
        """
        Processes incoming discharge reading in O(1) amortized time using running sums.
        """
        if math.isnan(reading) or math.isinf(reading) or reading < 0:
            return {"status": "INVALID_INPUT", "reading": reading, "alerts": ["SENSOR_HARDWARE_FAULT"]}
            
        # Add to window
        self.window.append(reading)
        self._sum += reading
        self._sum_sq += reading * reading
        
        # Evict oldest if window exceeds maximum capacity
        if len(self.window) > self.window_size:
            evicted = self.window.popleft()
            self._sum -= evicted
            self._sum_sq -= evicted * evicted
            
        n = len(self.window)
        alerts = []
        
        # Check Spillway Absolute Threshold
        if reading >= self.threshold:
            alerts.append("SPILLWAY_DISCHARGE_WARNING")
            
        if n < 2:
            return {
                "reading": reading,
                "window_count": n,
                "mean": reading,
                "std_dev": 0.0,
                "z_score": 0.0,
                "alerts": alerts
            }
            
        mean = self._sum / n
        # Sample variance formula: (sum_sq - (sum^2 / n)) / (n - 1)
        variance = (self._sum_sq - (self._sum * self._sum / n)) / (n - 1)
        # Numerical guard against small negative float artifacts
        variance = max(0.0, variance)
        std_dev = math.sqrt(variance)
        
        if std_dev < 1e-6:
            alerts.append("SENSOR_STUCK_FAILURE")
            z_score = 0.0
        else:
            z_score = (reading - mean) / std_dev
            if abs(z_score) > 2.5:
                alerts.append("STATISTICAL_ANOMALY")
                
        return {
            "reading": reading,
            "window_count": n,
            "mean": round(mean, 2),
            "std_dev": round(std_dev, 2),
            "z_score": round(z_score, 2),
            "alerts": alerts
        }

# Verification Suite
if __name__ == "__main__":
    monitor = HydroDischargeMonitor(window_size=5, spillway_threshold=500.0)
    
    # Ingest baseline flows: 100, 105, 95, 102, 98
    for q in [100.0, 105.0, 95.0, 102.0, 98.0]:
        res = monitor.process_reading(q)
        
    # Sudden flash flood surge: 550 m^3/s (exceeds threshold and huge z-score)
    res_surge = monitor.process_reading(550.0)
    assert "SPILLWAY_DISCHARGE_WARNING" in res_surge["alerts"]
    assert "STATISTICAL_ANOMALY" in res_surge["alerts"]
    print("Simulated Task 3 Passed All Test Criteria.")
```

---

## 5. Self-Scoring Rubric for HirePro Assessments

Evaluate your practice coding submissions against these 5 pillars:

| Evaluation Pillar | Weight | Passing Threshold | Description |
| :--- | :---: | :---: | :--- |
| **Correctness & Public Tests** | 35% | 100% | All visible test cases pass cleanly without syntax errors or runtime exceptions. |
| **Hidden Edge-Case Coverage** | 35% | $\ge 80\%$ | Handles empty collections, negative numbers, extreme inputs, and null references. |
| **Time & Space Complexity** | 15% | Optimal | Uses $O(N)$ or $O(N \log N)$ algorithms; avoids quadratic $O(N^2)$ loops. |
| **Code Modularity & Naming** | 10% | Professional | Descriptive variable names (`total_hours` vs `x`), type hints, clean functions. |
| **Defensive Exception Handling** | 5% | Robust | Catches conversion errors, guards against division by zero, checks existence. |
