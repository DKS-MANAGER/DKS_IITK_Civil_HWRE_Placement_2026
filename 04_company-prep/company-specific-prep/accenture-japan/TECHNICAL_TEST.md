# Technology / Technical / Coding Test — Master Preparation Curriculum & Problem Bank

> **Document Status**: Complete Mock Assessment & Technical Preparation Suite  
> **Target Role**: Digital Consultant, Accenture Japan Ltd. (`[JD VERIFIED]`)  
> **Testing Medium**: Designated Online Testing Platform (`[JD VERIFIED]`), Timed Sectional Test.  
> **Curriculum Standard**: High-yield algorithmic logic, production SQL querying, and quantitative business mathematics.  
> **Classification Standard**: `[JD VERIFIED]` for JD assessment references; `[PREPARATION INFERENCE]` for problem types; `[HYPOTHETICAL PRACTICE]` for synthetic data tables and scenarios.

---

## 🏛️ Curriculum Architecture & Pedagogical Roadmap

The Accenture Japan Digital Consultant technical assessment evaluates how candidates structure logic, query enterprise databases, and compute business metrics under time pressure.

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                       TECHNICAL TEST STRUCTURE & ROADMAP                    │
├──────────────────────────────┬──────────────────────────────┬───────────────┤
│ PART 1: Python Algorithmic   │ PART 2: Relational SQL       │ PART 3: Quant │
│ Logic (20 Progressive        │ Analytics (30 Comprehensive  │ Mathematics   │
│ Tested Challenges)           │ Query Solutions)             │ (20 Problems) │
├──────────────────────────────┴──────────────────────────────┴───────────────┤
│ PART 4: Technology & Architecture Comprehension (Cloud, AI, IoT, APIs)      │
├─────────────────────────────────────────────────────────────────────────────┤
│ PART 5: Full Timed 90-Minute Mock Assessment Simulation                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🐍 PART 1: Python Algorithmic Logic Curriculum

### 1.1 Foundational Concepts & Core Patterns

Before tackling the challenge bank, candidates must master these foundational paradigms:

1. **Variables, Slicing & Iteration**:
   * String and array slicing: `arr[start:stop:step]`. Negative indices count from the end (`arr[-1]`).
   * Memory & time: Slicing creates a shallow copy ($O(K)$ time and space). For in-place two-pointer traversal, use indices directly without slicing.
2. **Hash Maps & Frequency Counting**:
   * Python `dict` and `collections.Counter` provide average $O(1)$ lookup, insertion, and deletion.
   * Key pattern: Two-Sum complement lookup (`complement = target - num`), frequency counting, and anagram grouping.
3. **Two-Pointer Technique & Sliding Window**:
   * **Opposite-Direction Pointers**: For sorted arrays (e.g., target sum, container with most water). Converges in $O(N)$ time.
   * **Sliding Window (Same Direction)**: For contiguous subarray/substring optimization. Expand `right` to explore, contract `left` when constraints are violated. Always maintains an invariant.
4. **Prefix Sums**:
   * Precomputing cumulative sums (`prefix[i + 1] = prefix[i] + arr[i]`) converts repeated range sum queries from $O(N)$ to $O(1)$.
5. **Binary Search**:
   * Applied on sorted arrays or monotonic condition spaces (`O(\log N)`). Calculate `mid = left + (right - left) // 2` to prevent overflow.
6. **Stacks & Queues**:
   * Stacks (LIFO) handle nested structures, bracket validation, and monotonic trends.
   * Queues (FIFO) via `collections.deque` provide $O(1)$ `append` and `popleft`, essential for streaming buffers and BFS.
7. **Heaps / Priority Queues**:
   * `heapq` implements a min-heap by default. For top-$K$ frequent elements, maintain a min-heap of size $K$ to achieve $O(N \log K)$ time.

---

### 1.2 The 20 Progressive Algorithmic Challenges

Every challenge includes problem constraints, complete runnable Python 3 code, time/space complexity analysis, and assertion test suites.

---

#### Challenge 01: System Log Latency Spike Detection
* **Pattern**: Array Traversal / Adjacent Differences
* **Difficulty**: Easy | **Target Time**: 6 Mins
* **Problem**: Given a list of integers `timestamps` representing server log access times in seconds (sorted in non-decreasing order), write a function `find_latency_spikes(timestamps, threshold)` that returns the indices of all logs where the gap between consecutive timestamps strictly exceeds `threshold` seconds.
* **Complexity**: Time: $O(N)$, Space: $O(1)$ auxiliary.

```python
def find_latency_spikes(timestamps: list[int], threshold: int) -> list[int]:
    if not timestamps or len(timestamps) < 2:
        return []
    spikes = []
    for i in range(1, len(timestamps)):
        if timestamps[i] - timestamps[i - 1] > threshold:
            spikes.append(i)
    return spikes

# Verifiable Assertions
assert find_latency_spikes([10, 12, 15, 45, 48, 90], 20) == [3, 5]
assert find_latency_spikes([], 10) == []
assert find_latency_spikes([10], 10) == []
assert find_latency_spikes([10, 20, 30], 10) == []
assert find_latency_spikes([10, 21, 30], 10) == [1]
```

---

#### Challenge 02: Customer Session Inactivity Timeout
* **Pattern**: Sliding Window (Dynamic Size)
* **Difficulty**: Medium | **Target Time**: 8 Mins
* **Problem**: Given a binary string `events` where `'1'` denotes active user interaction and `'0'` denotes idle time, return the length of the longest contiguous sequence of active interactions allowing at most **one** idle `'0'` to be converted to active `'1'` (representing keep-alive session extension).
* **Important Note**: If `events = "110110111"`, flipping the second zero yields `"110111"` -> length 6. Flipping the first zero yields `"11011"` -> length 5. Maximum is 6.
* **Complexity**: Time: $O(N)$, Space: $O(1)$.

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

# Verifiable Assertions
assert longest_active_window("110110111") == 6
assert longest_active_window("11011011") == 5
assert longest_active_window("11111") == 5
assert longest_active_window("0000") == 1
assert longest_active_window("") == 0
```

---

#### Challenge 03: Valid API Payload Brackets
* **Pattern**: Stack Data Structure
* **Difficulty**: Easy | **Target Time**: 5 Mins
* **Problem**: Given a string `s` containing brackets `()`, `{}`, `[]`, determine if the input string is valid (every open bracket is closed by the same type of bracket in the correct order).
* **Complexity**: Time: $O(N)$, Space: $O(N)$.

```python
def is_valid_payload_brackets(s: str) -> bool:
    matching = {')': '(', '}': '{', ']': '['}
    stack = []
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack or stack[-1] != matching[ch]:
                return False
            stack.pop()
    return len(stack) == 0

# Verifiable Assertions
assert is_valid_payload_brackets("{[()]}") is True
assert is_valid_payload_brackets("{[(])}") is False
assert is_valid_payload_brackets("API_call(data[id])") is True
assert is_valid_payload_brackets("((((") is False
assert is_valid_payload_brackets("") is True
```

---

#### Challenge 04: Two-Sum Cloud Cost Optimization
* **Pattern**: Hash Map Complement Lookup
* **Difficulty**: Easy | **Target Time**: 6 Mins
* **Problem**: Given a list of integers `costs` and an integer `budget`, return the zero-based indices of two distinct services whose costs sum exactly to `budget`. If no pair exists, return `None`.
* **Complexity**: Time: $O(N)$, Space: $O(N)$.

```python
def two_sum_cloud_costs(costs: list[int], budget: int) -> tuple[int, int] | None:
    seen = {}
    for idx, cost in enumerate(costs):
        complement = budget - cost
        if complement in seen:
            return (seen[complement], idx)
        seen[cost] = idx
    return None

# Verifiable Assertions
assert two_sum_cloud_costs([150, 300, 450, 200, 700], 500) == (1, 3)
assert two_sum_cloud_costs([100, 200], 400) is None
assert two_sum_cloud_costs([250, 250], 500) == (0, 1)
```

---

#### Challenge 05: Merge Maintenance Intervals
* **Pattern**: Sorting & Interval Sweep
* **Difficulty**: Medium | **Target Time**: 8 Mins
* **Problem**: Given a collection of maintenance time intervals `intervals = [[start_i, end_i]]`, merge all overlapping intervals and return an array of the non-overlapping intervals that cover all the original intervals.
* **Complexity**: Time: $O(N \log N)$, Space: $O(N)$ for sorting/output.

```python
def merge_service_maintenance_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    merged = [sorted_intervals[0]]
    for start, end in sorted_intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])
    return merged

# Verifiable Assertions
assert merge_service_maintenance_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert merge_service_maintenance_intervals([[1, 4], [4, 5]]) == [[1, 5]]
assert merge_service_maintenance_intervals([]) == []
assert merge_service_maintenance_intervals([[5, 7]]) == [[5, 7]]
```

---

#### Challenge 06: Real-time Telemetry Moving Average Stream
* **Pattern**: Queue / Deque Buffer
* **Difficulty**: Easy | **Target Time**: 6 Mins
* **Problem**: Design a class `MovingAverageStream` that calculates the moving average of all values in the sliding window of size `size`.
* **Complexity**: Time: $O(1)$ per operation, Space: $O(\text{size})$.

```python
from collections import deque

class MovingAverageStream:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.window_sum = 0.0

    def next(self, val: float) -> float:
        self.queue.append(val)
        self.window_sum += val
        if len(self.queue) > self.size:
            self.window_sum -= self.queue.popleft()
        return round(self.window_sum / len(self.queue), 4)

# Verifiable Assertions
stream = MovingAverageStream(3)
assert stream.next(10.0) == 10.0
assert stream.next(20.0) == 15.0
assert stream.next(30.0) == 20.0
assert stream.next(40.0) == 30.0
```

---

#### Challenge 07: Top-K Frequent API Endpoints
* **Pattern**: Hash Map & Min-Heap
* **Difficulty**: Medium | **Target Time**: 10 Mins
* **Problem**: Given an array of string `logs` and an integer `k`, return the `k` most frequent API endpoints sorted by frequency descending. Break ties lexicographically ascending.
* **Complexity**: Time: $O(N \log K)$, Space: $O(N)$.

```python
from collections import Counter
import heapq

def top_k_frequent_api_endpoints(logs: list[str], k: int) -> list[str]:
    counts = Counter(logs)
    heap = []
    for endpoint, count in counts.items():
        heapq.heappush(heap, (count, endpoint))
        if len(heap) > k:
            heapq.heappop(heap)
    return [item[1] for item in sorted(heap, key=lambda x: (-x[0], x[1]))]

# Verifiable Assertions
endpoints = ["/login", "/checkout", "/login", "/products", "/checkout", "/login", "/cart"]
assert top_k_frequent_api_endpoints(endpoints, 2) == ["/login", "/checkout"]
```

---

#### Challenge 08: First Missing Positive Transaction ID
* **Pattern**: Cyclic Sort / In-place Hashing
* **Difficulty**: Hard | **Target Time**: 12 Mins
* **Problem**: Given an unsorted integer array `ids`, return the smallest positive integer that is not present in `ids`. Must run in $O(N)$ time and use $O(1)$ auxiliary space.
* **Complexity**: Time: $O(N)$, Space: $O(1)$.

```python
def find_first_missing_transaction_id(ids: list[int]) -> int:
    n = len(ids)
    for i in range(n):
        while 1 <= ids[i] <= n and ids[ids[i] - 1] != ids[i]:
            correct_idx = ids[i] - 1
            ids[i], ids[correct_idx] = ids[correct_idx], ids[i]
    for i in range(n):
        if ids[i] != i + 1:
            return i + 1
    return n + 1

# Verifiable Assertions
assert find_first_missing_transaction_id([3, 4, -1, 1]) == 2
assert find_first_missing_transaction_id([1, 2, 0]) == 3
assert find_first_missing_transaction_id([7, 8, 9, 11, 12]) == 1
assert find_first_missing_transaction_id([1, 2, 3]) == 4
```

---

#### Challenge 09: Binary Search Response Time Threshold
* **Pattern**: Binary Search (Lower Bound)
* **Difficulty**: Easy-Medium | **Target Time**: 6 Mins
* **Problem**: Given a sorted list of integer latencies `latencies` and a target threshold `target`, return the index of the first latency that is greater than or equal to `target`. If no such element exists, return `-1`.
* **Complexity**: Time: $O(\log N)$, Space: $O(1)$.

```python
def binary_search_response_time_threshold(latencies: list[int], target: int) -> int:
    left, right = 0, len(latencies) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if latencies[mid] >= target:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

# Verifiable Assertions
assert binary_search_response_time_threshold([120, 150, 180, 200, 250, 300], 190) == 3
assert binary_search_response_time_threshold([100, 200, 300], 50) == 0
assert binary_search_response_time_threshold([100, 200, 300], 400) == -1
```

---

#### Challenge 10: Prefix Sum Server Traffic Range Query
* **Pattern**: Prefix Sum Array
* **Difficulty**: Easy | **Target Time**: 6 Mins
* **Problem**: Design an immutable data structure `TrafficRangeQuery` that accepts an array of hourly network traffic packets and answers range sum queries from index `left` to `right` in $O(1)$ time.
* **Complexity**: Precompute: $O(N)$ time & space; Query: $O(1)$ time.

```python
class TrafficRangeQuery:
    def __init__(self, traffic: list[int]):
        self.prefix = [0] * (len(traffic) + 1)
        for i in range(len(traffic)):
            self.prefix[i + 1] = self.prefix[i] + traffic[i]

    def query(self, left: int, right: int) -> int:
        if left < 0 or right >= len(self.prefix) - 1 or left > right:
            return 0
        return self.prefix[right + 1] - self.prefix[left]

# Verifiable Assertions
tq = TrafficRangeQuery([10, 20, 30, 40, 50])
assert tq.query(1, 3) == 90
assert tq.query(0, 4) == 150
assert tq.query(2, 2) == 30
```

---

#### Challenge 11: Group Similar Device Alerts (Anagrams)
* **Pattern**: Hash Map Categorization
* **Difficulty**: Medium | **Target Time**: 8 Mins
* **Problem**: Given a list of string alert codes, group all alerts that are anagrams of each other. Return groups sorted lexicographically.
* **Complexity**: Time: $O(N \cdot K \log K)$ where $K$ is string length.

```python
def group_similar_device_alerts(alerts: list[str]) -> list[list[str]]:
    groups = {}
    for alert in alerts:
        sorted_key = "".join(sorted(alert))
        groups.setdefault(sorted_key, []).append(alert)
    return [sorted(group) for group in sorted(groups.values(), key=lambda g: g[0])]

# Verifiable Assertions
res11 = group_similar_device_alerts(["cpu_high", "high_cpu", "mem_leak", "leak_mem", "disk_full"])
assert res11 == [["cpu_high", "high_cpu"], ["disk_full"], ["leak_mem", "mem_leak"]]
```

---

#### Challenge 12: Max Consecutive Active Days with K Downtimes
* **Pattern**: Sliding Window
* **Difficulty**: Medium | **Target Time**: 8 Mins
* **Problem**: Given a binary array `logs` where `1` represents uptime and `0` downtime, and an integer `k`, return the maximum number of consecutive `1`s you can obtain by flipping at most `k` zeros.
* **Complexity**: Time: $O(N)$, Space: $O(1)$.

```python
def max_consecutive_active_days(logs: list[int], k: int) -> int:
    left = 0
    zero_count = 0
    max_len = 0
    for right in range(len(logs)):
        if logs[right] == 0:
            zero_count += 1
        while zero_count > k:
            if logs[left] == 0:
                zero_count -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len

# Verifiable Assertions
assert max_consecutive_active_days([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2) == 6
assert max_consecutive_active_days([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3) == 10
```

---

#### Challenge 13: Detect Circular Dependency in Microservices
* **Pattern**: Topological Sort (Kahn's Algorithm)
* **Difficulty**: Medium-Hard | **Target Time**: 12 Mins
* **Problem**: There are `num_services` microservices labeled `0` to `n - 1`. Given a list of pairs `dependencies` where `[u, v]` means service `u` must initialize before service `v`, return a valid initialization sequence. If a cyclic dependency exists, return `[]`.
* **Complexity**: Time: $O(V + E)$, Space: $O(V + E)$.

```python
from collections import deque

def detect_circular_dependency_services(num_services: int, dependencies: list[list[int]]) -> list[int]:
    adj = {i: [] for i in range(num_services)}
    in_degree = [0] * num_services
    for u, v in dependencies:
        adj[u].append(v)
        in_degree[v] += 1
    queue = deque([i for i in range(num_services) if in_degree[i] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return order if len(order) == num_services else []

# Verifiable Assertions
assert detect_circular_dependency_services(4, [[0, 1], [0, 2], [1, 3], [2, 3]]) == [0, 1, 2, 3]
assert detect_circular_dependency_services(2, [[0, 1], [1, 0]]) == []
```

---

#### Challenge 14: Batch Task Scheduling with Cooldown
* **Pattern**: Greedy Scheduling / Mathematical Placement
* **Difficulty**: Medium | **Target Time**: 10 Mins
* **Problem**: Given a list of task names `tasks` and a cooling interval `cooldown`, return the minimum total time CPU units required to complete all tasks if identical tasks must be separated by at least `cooldown` units.
* **Complexity**: Time: $O(N)$, Space: $O(1)$ unique alphabet.

```python
from collections import Counter

def reorganize_task_stream(tasks: list[str], cooldown: int) -> int:
    task_counts = Counter(tasks)
    max_freq = max(task_counts.values())
    max_freq_count = sum(1 for count in task_counts.values() if count == max_freq)
    min_time = (max_freq - 1) * (cooldown + 1) + max_freq_count
    return max(len(tasks), min_time)

# Verifiable Assertions
assert reorganize_task_stream(["A", "A", "A", "B", "B", "B"], 2) == 8
assert reorganize_task_stream(["A", "A", "A", "B", "B", "B"], 0) == 6
assert reorganize_task_stream(["A", "A", "A", "A", "B", "C", "D", "E"], 2) == 10
```

---

#### Challenge 15: Minimum Cloud Instances for Concurrent Jobs
* **Pattern**: Interval Overlap / Min-Heap Sweep
* **Difficulty**: Medium | **Target Time**: 10 Mins
* **Problem**: Given job intervals `tasks = [[start_i, end_i]]`, find the minimum number of cloud servers required so that no two overlapping jobs share a server.
* **Complexity**: Time: $O(N \log N)$, Space: $O(N)$.

```python
import heapq

def minimum_cloud_instances_needed(tasks: list[list[int]]) -> int:
    if not tasks:
        return 0
    sorted_tasks = sorted(tasks, key=lambda x: x[0])
    heap = []
    for start, end in sorted_tasks:
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
    return len(heap)

# Verifiable Assertions
assert minimum_cloud_instances_needed([[0, 30], [5, 10], [15, 20]]) == 2
assert minimum_cloud_instances_needed([[7, 10], [2, 4]]) == 1
assert minimum_cloud_instances_needed([[1, 5], [2, 6], [3, 7], [4, 8]]) == 4
```

---

#### Challenge 16: Longest Common API Gateway Endpoint Prefix
* **Pattern**: String Traversal / Divide & Conquer
* **Difficulty**: Easy | **Target Time**: 5 Mins
* **Problem**: Write a function to find the longest common prefix string amongst an array of API paths. If none exists, return `""`.
* **Complexity**: Time: $O(S)$ where $S$ is total characters across all strings.

```python
def longest_common_endpoint_prefix(paths: list[str]) -> str:
    if not paths:
        return ""
    prefix = paths[0]
    for path in paths[1:]:
        while not path.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Verifiable Assertions
assert longest_common_endpoint_prefix(["/api/v1/users", "/api/v1/orders", "/api/v1/products"]) == "/api/v1/"
assert longest_common_endpoint_prefix(["serviceA", "serviceB", "serviceC"]) == "service"
assert longest_common_endpoint_prefix(["auth", "billing"]) == ""
```

---

#### Challenge 17: Coin Change Cloud Credits
* **Pattern**: Dynamic Programming (Bottom-Up)
* **Difficulty**: Medium | **Target Time**: 10 Mins
* **Problem**: Given an integer array `credits` representing credit denominations and an integer `target`, return the fewest number of voucher denominations needed to make up that target. If impossible, return `-1`.
* **Complexity**: Time: $O(\text{target} \cdot \text{len(credits)})$, Space: $O(\text{target})$.

```python
def coin_change_cloud_credits(credits: list[int], target: int) -> int:
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    for coin in credits:
        for x in range(coin, target + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[target] if dp[target] != float('inf') else -1

# Verifiable Assertions
assert coin_change_cloud_credits([1, 2, 5], 11) == 3
assert coin_change_cloud_credits([2], 3) == -1
assert coin_change_cloud_credits([1], 0) == 0
```

---

#### Challenge 18: Longest Increasing Throughput Sequence
* **Pattern**: Dynamic Programming + Binary Search (Patience Sort)
* **Difficulty**: Medium-Hard | **Target Time**: 10 Mins
* **Problem**: Given an array of hourly throughput records `records`, return the length of the longest strictly increasing subsequence.
* **Complexity**: Time: $O(N \log N)$, Space: $O(N)$.

```python
import bisect

def longest_increasing_throughput_subsequence(records: list[int]) -> int:
    tails = []
    for x in records:
        idx = bisect.bisect_left(tails, x)
        if idx == len(tails):
            tails.append(x)
        else:
            tails[idx] = x
    return len(tails)

# Verifiable Assertions
assert longest_increasing_throughput_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4
assert longest_increasing_throughput_subsequence([0, 1, 0, 3, 2, 3]) == 4
assert longest_increasing_throughput_subsequence([7, 7, 7, 7]) == 1
```

---

#### Challenge 19: Token Bucket API Rate Limiter
* **Pattern**: Object-Oriented System Modeling / State Machine
* **Difficulty**: Medium | **Target Time**: 10 Mins
* **Problem**: Implement a `TokenBucketRateLimiter` class with `capacity` and `refill_rate_per_sec`. Method `allow_request(current_time, tokens_needed)` returns `True` if enough tokens are available.
* **Complexity**: Time: $O(1)$, Space: $O(1)$.

```python
class TokenBucketRateLimiter:
    def __init__(self, capacity: int, refill_rate_per_sec: float):
        self.capacity = capacity
        self.refill_rate = refill_rate_per_sec
        self.tokens = float(capacity)
        self.last_timestamp = 0.0

    def allow_request(self, current_time: float, tokens_needed: int = 1) -> bool:
        elapsed = current_time - self.last_timestamp
        self.tokens = min(float(self.capacity), self.tokens + elapsed * self.refill_rate)
        self.last_timestamp = current_time
        if self.tokens >= tokens_needed:
            self.tokens -= tokens_needed
            return True
        return False

# Verifiable Assertions
limiter = TokenBucketRateLimiter(capacity=5, refill_rate_per_sec=1.0)
assert limiter.allow_request(0.0, 3) is True
assert limiter.allow_request(0.0, 3) is False
assert limiter.allow_request(1.0, 3) is True
```

---

#### Challenge 20: LRU Cache Database Query Engine
* **Pattern**: Hash Map + Doubly Linked List
* **Difficulty**: Medium-Hard | **Target Time**: 12 Mins
* **Problem**: Design a data structure that follows the Least Recently Used (LRU) cache eviction policy with $O(1)$ `get` and `put` operations.
* **Complexity**: Time: $O(1)$ for both operations, Space: $O(\text{capacity})$.

```python
class Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_front(node)
            return node.val
        return -1

    def put(self, key: int, value: int):
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._add_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)

# Verifiable Assertions
cache = LRUCache(2)
cache.put(1, 100)
cache.put(2, 200)
assert cache.get(1) == 100
cache.put(3, 300)
assert cache.get(2) == -1
cache.put(4, 400)
assert cache.get(1) == -1
assert cache.get(3) == 300
assert cache.get(4) == 400
```

---

## 🗄️ PART 2: Relational SQL Analytics Curriculum

### 2.1 Foundational SQL Teaching & Principles

1. **Clause Execution Order**:
   Unlike procedural languages, SQL executes in a strict conceptual order:
   $$\text{FROM} \longrightarrow \text{ON} \longrightarrow \text{JOIN} \longrightarrow \text{WHERE} \longrightarrow \text{GROUP BY} \longrightarrow \text{HAVING} \longrightarrow \text{SELECT} \longrightarrow \text{DISTINCT} \longrightarrow \text{ORDER BY} \longrightarrow \text{LIMIT / OFFSET}$$
   *Notice*: Column aliases defined in `SELECT` cannot be referenced in `WHERE` or `GROUP BY` because those clauses execute *before* `SELECT`.
2. **Three-Valued Logic & NULL Comparisons**:
   * In SQL, comparisons with `NULL` yield `UNKNOWN`, not `FALSE`.
   * Never write `WHERE col = NULL`. Always use `WHERE col IS NULL` or `WHERE col IS NOT NULL`.
   * Use `COALESCE(val1, val2, ...)` to supply fallback values.
3. **Safe Division**:
   * Dividing by zero causes immediate query execution failure. Always protect denominators with `NULLIF(denominator, 0)`.
4. **Join Cardinality & Fanout Multiplication**:
   * When joining Table A (1 row) to Table B (3 rows) on a 1-to-many relationship, `SUM(A.amount)` will multiply the amount by 3!
   * *Remedy*: Pre-aggregate the "many" side in a CTE or subquery before joining to the "one" side.
5. **Window Functions vs Ordinary Aggregations**:
   * Ordinary `GROUP BY` collapses multiple rows into a single summary row.
   * Window functions (`OVER (...)`) calculate aggregates across a partition while preserving individual row identity.
   * Window Framing: `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW` computes cumulative running totals; `ROWS BETWEEN 6 PRECEDING AND CURRENT ROW` computes 7-period rolling windows.
6. **Dialect Nuances**:
   * ANSI SQL standard uses `CURRENT_DATE`, `EXTRACT(YEAR FROM col)`.
   * PostgreSQL uses `DATE_TRUNC('month', col)`, `INTERVAL '7 days'`.
   * MySQL uses `DATE_SUB(NOW(), INTERVAL 7 DAY)`, `DATE_FORMAT()`.

---

### 2.2 The 30 Comprehensive SQL Problems & Solutions

---

#### Problem 01: Active Cloud License Filtering & Sorting
* **Focus**: `SELECT`, `WHERE`, `ORDER BY`
* **Dialect**: ANSI SQL
* **Schema**: `licenses(license_id INT, client_name VARCHAR, seat_count INT, status VARCHAR, renewal_date DATE)`
* **Task**: List all licenses with `status = 'ACTIVE'` and `seat_count >= 50`, ordered by `seat_count` descending, then `renewal_date` ascending.

```sql
SELECT 
    license_id,
    client_name,
    seat_count,
    renewal_date
FROM licenses
WHERE status = 'ACTIVE' 
  AND seat_count >= 50
ORDER BY seat_count DESC, renewal_date ASC;
```

---

#### Problem 02: Safe NULL Handling for Client Contacts
* **Focus**: `IS NULL`, `COALESCE`
* **Dialect**: ANSI SQL
* **Schema**: `clients(client_id INT, company_name VARCHAR, primary_email VARCHAR, secondary_email VARCHAR, phone_number VARCHAR)`
* **Task**: Return `company_name`, effective contact email (`primary_email` if present, else `secondary_email`, else `'no_email@company.com'`), and flag whether phone is missing.

```sql
SELECT 
    company_name,
    COALESCE(primary_email, secondary_email, 'no_email@company.com') AS contact_email,
    CASE WHEN phone_number IS NULL THEN 'MISSING' ELSE 'VERIFIED' END AS phone_status
FROM clients;
```

---

#### Problem 03: Safe Conversion Rate with Zero-Division Protection
* **Focus**: Safe Division, `NULLIF`
* **Dialect**: ANSI SQL
* **Schema**: `campaign_metrics(campaign_id INT, impressions INT, conversions INT)`
* **Task**: Calculate conversion percentage rounded to 2 decimal places. Ensure campaigns with 0 impressions return `0.00%` rather than throwing division-by-zero error.

```sql
SELECT 
    campaign_id,
    impressions,
    conversions,
    ROUND(COALESCE(conversions * 100.0 / NULLIF(impressions, 0), 0.0), 2) AS conversion_rate_pct
FROM campaign_metrics;
```

---

#### Problem 04: Project Billing Reconciliation (Inner vs Left Join)
* **Focus**: `LEFT JOIN`, Unmatched Records
* **Dialect**: ANSI SQL
* **Schema**: `clients(client_id INT, client_name VARCHAR)`, `projects(project_id INT, client_id INT, total_budget NUMERIC)`
* **Task**: Output all clients and their total project budget. Include clients who currently have zero assigned projects (show budget as `0.00`).

```sql
SELECT 
    c.client_id,
    c.client_name,
    COALESCE(SUM(p.total_budget), 0.00) AS total_assigned_budget
FROM clients c
LEFT JOIN projects p ON c.client_id = p.client_id
GROUP BY c.client_id, c.client_name
ORDER BY total_assigned_budget DESC;
```

---

#### Problem 05: Preventing Join Fanout Revenue Inflation
* **Focus**: Multi-table Join Fanout, Subquery Pre-aggregation
* **Dialect**: ANSI SQL
* **Schema**: `orders(order_id INT, client_id INT, order_amount NUMERIC)`, `payments(payment_id INT, order_id INT, payment_amount NUMERIC)`
* **Task**: Calculate each client's total order amount and total payments made. Ensure multiple payments per order do not artificially multiply the order amount.

```sql
WITH payment_summary AS (
    SELECT order_id, SUM(payment_amount) AS total_paid
    FROM payments
    GROUP BY order_id
)
SELECT 
    o.client_id,
    SUM(o.order_amount) AS total_ordered,
    COALESCE(SUM(ps.total_paid), 0.00) AS total_paid
FROM orders o
LEFT JOIN payment_summary ps ON o.order_id = ps.order_id
GROUP BY o.client_id;
```

---

#### Problem 06: Server Latency Aggregation with Sample Threshold
* **Focus**: `GROUP BY`, `HAVING`, `AVG`
* **Dialect**: ANSI SQL
* **Schema**: `telemetry_logs(server_id VARCHAR, region VARCHAR, latency_ms NUMERIC, logged_at TIMESTAMP)`
* **Task**: Find regions with average latency > 120 ms, restricted only to regions that have logged at least 100 telemetry records.

```sql
SELECT 
    region,
    COUNT(*) AS total_samples,
    ROUND(AVG(latency_ms), 2) AS avg_latency_ms
FROM telemetry_logs
GROUP BY region
HAVING COUNT(*) >= 100 
   AND AVG(latency_ms) > 120.0
ORDER BY avg_latency_ms DESC;
```

---

#### Problem 07: Client Digital Tool Adoption Rate
* **Focus**: Conditional Aggregation, `HAVING`
* **Dialect**: ANSI SQL
* **Schema**: `departments(dept_id INT, dept_name VARCHAR)`, `employees(emp_id INT, dept_id INT, has_digital_license INT)`
* **Task**: Identify departments with >= 30 employees where the digital tool adoption rate exceeds 75.0%.

```sql
SELECT 
    d.dept_name,
    COUNT(e.emp_id) AS total_employees,
    ROUND(SUM(e.has_digital_license) * 100.0 / COUNT(e.emp_id), 2) AS adoption_pct
FROM departments d
JOIN employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_id, d.dept_name
HAVING COUNT(e.emp_id) >= 30 
   AND (SUM(e.has_digital_license) * 100.0 / COUNT(e.emp_id)) > 75.0
ORDER BY adoption_pct DESC;
```

---

#### Problem 08: Monthly Revenue Pivot by Service Line
* **Focus**: Pivot via `CASE WHEN`
* **Dialect**: ANSI SQL
* **Schema**: `monthly_revenue(month_name VARCHAR, service_line VARCHAR, revenue NUMERIC)`
* **Task**: Pivot the table to display `month_name` with separate columns for `'Cloud'`, `'AI'`, and `'Cybersecurity'` revenues.

```sql
SELECT 
    month_name,
    SUM(CASE WHEN service_line = 'Cloud' THEN revenue ELSE 0 END) AS cloud_revenue,
    SUM(CASE WHEN service_line = 'AI' THEN revenue ELSE 0 END) AS ai_revenue,
    SUM(CASE WHEN service_line = 'Cybersecurity' THEN revenue ELSE 0 END) AS cybersecurity_revenue
FROM monthly_revenue
GROUP BY month_name
ORDER BY month_name;
```

---

#### Problem 09: Customer User Activity Segmentation
* **Focus**: Tier Categorization, Subquery Counting
* **Dialect**: ANSI SQL
* **Schema**: `user_activity(user_id INT, login_count_30d INT)`
* **Task**: Categorize users into `'Power User'` (>= 50 logins), `'Regular User'` (10-49 logins), and `'Dormant User'` (< 10 logins). Count total users and percentage in each tier.

```sql
WITH categorized AS (
    SELECT 
        user_id,
        CASE 
            WHEN login_count_30d >= 50 THEN 'Power User'
            WHEN login_count_30d >= 10 THEN 'Regular User'
            ELSE 'Dormant User'
        END AS user_tier
    FROM user_activity
)
SELECT 
    user_tier,
    COUNT(*) AS user_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM user_activity), 2) AS pct_of_total
FROM categorized
GROUP BY user_tier
ORDER BY user_count DESC;
```

---

#### Problem 10: Employees Earning Above Department Average
* **Focus**: CTE + Join on Aggregated Subquery
* **Dialect**: ANSI SQL
* **Schema**: `employees(emp_id INT, emp_name VARCHAR, dept_id INT, salary NUMERIC)`
* **Task**: Return all employees whose salary exceeds their department's average salary. Include employee salary and department average.

```sql
WITH dept_avg AS (
    SELECT dept_id, AVG(salary) AS avg_sal
    FROM employees
    GROUP BY dept_id
)
SELECT 
    e.emp_id,
    e.emp_name,
    e.dept_id,
    e.salary,
    ROUND(da.avg_sal, 2) AS department_avg_salary
FROM employees e
JOIN dept_avg da ON e.dept_id = da.dept_id
WHERE e.salary > da.avg_sal
ORDER BY e.dept_id, e.salary DESC;
```

---

#### Problem 11: Rapid Second Purchase Interval
* **Focus**: CTE, Self-Join / Window Matching
* **Dialect**: ANSI SQL / PostgreSQL
* **Schema**: `orders(order_id INT, customer_id INT, order_date DATE, amount NUMERIC)`
* **Task**: Identify customers whose second order occurred within 7 days of their first order.

```sql
WITH ranked_orders AS (
    SELECT 
        customer_id,
        order_date,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date ASC) AS order_seq
    FROM orders
)
SELECT 
    r1.customer_id,
    r1.order_date AS first_order,
    r2.order_date AS second_order,
    (r2.order_date - r1.order_date) AS days_between
FROM ranked_orders r1
JOIN ranked_orders r2 ON r1.customer_id = r2.customer_id
WHERE r1.order_seq = 1 
  AND r2.order_seq = 2
  AND (r2.order_date - r1.order_date) <= 7;
```

---

#### Problem 12: Distinct Event Counting Rigor
* **Focus**: `COUNT(*)`, `COUNT(col)`, `COUNT(DISTINCT)`
* **Dialect**: ANSI SQL
* **Schema**: `api_logs(request_id INT, session_id VARCHAR, response_payload VARCHAR)`
* **Task**: Return total requests logged, total requests with a non-null payload, and total unique sessions.

```sql
SELECT 
    COUNT(*) AS total_raw_requests,
    COUNT(response_payload) AS requests_with_payload,
    COUNT(DISTINCT session_id) AS unique_active_sessions
FROM api_logs;
```

---

#### Problem 13: Top-3 Japanese Enterprise Contracts per Prefecture (Ties Handling)
* **Focus**: `DENSE_RANK()`, Window Function Filtering
* **Dialect**: ANSI SQL
* **Schema**: `contracts(contract_id INT, prefecture VARCHAR, client_name VARCHAR, contract_value NUMERIC)`
* **Task**: Return top-3 contracts per prefecture by value. In case of ties, assign identical ranks without skipping subsequent ranks (`DENSE_RANK`).

```sql
WITH ranked_contracts AS (
    SELECT 
        prefecture,
        client_name,
        contract_value,
        DENSE_RANK() OVER (PARTITION BY prefecture ORDER BY contract_value DESC) AS val_rank
    FROM contracts
)
SELECT 
    prefecture,
    val_rank,
    client_name,
    contract_value
FROM ranked_contracts
WHERE val_rank <= 3
ORDER BY prefecture, val_rank;
```

---

#### Problem 14: Latest Status Snapshot per IoT Edge Device
* **Focus**: `ROW_NUMBER() OVER (PARTITION BY ...)`
* **Dialect**: ANSI SQL
* **Schema**: `device_heartbeats(device_id VARCHAR, recorded_at TIMESTAMP, battery_pct NUMERIC, firmware_version VARCHAR)`
* **Task**: Output the single most recent heartbeat record for each IoT device.

```sql
WITH latest_heartbeat AS (
    SELECT 
        device_id,
        recorded_at,
        battery_pct,
        firmware_version,
        ROW_NUMBER() OVER (PARTITION BY device_id ORDER BY recorded_at DESC) AS rn
    FROM device_heartbeats
)
SELECT 
    device_id,
    recorded_at,
    battery_pct,
    firmware_version
FROM latest_heartbeat
WHERE rn = 1;
```

---

#### Problem 15: Day-over-Day Server Error Growth
* **Focus**: `LAG()`, Window Offset
* **Dialect**: ANSI SQL
* **Schema**: `daily_errors(log_date DATE, error_count INT)`
* **Task**: For each day, display `log_date`, `error_count`, yesterday's error count, and the percentage change.

```sql
WITH daily_trend AS (
    SELECT 
        log_date,
        error_count,
        LAG(error_count, 1) OVER (ORDER BY log_date ASC) AS prev_day_errors
    FROM daily_errors
)
SELECT 
    log_date,
    error_count,
    prev_day_errors,
    ROUND((error_count - prev_day_errors) * 100.0 / NULLIF(prev_day_errors, 0), 2) AS dod_growth_pct
FROM daily_trend
ORDER BY log_date ASC;
```

---

#### Problem 16: Idle Gap Between Consecutive User Interactions
* **Focus**: `LEAD()`, Timestamp Difference
* **Dialect**: ANSI SQL / PostgreSQL
* **Schema**: `user_clicks(user_id INT, click_time TIMESTAMP)`
* **Task**: For each user, calculate the idle gap in minutes until their next click.

```sql
WITH click_sequence AS (
    SELECT 
        user_id,
        click_time,
        LEAD(click_time, 1) OVER (PARTITION BY user_id ORDER BY click_time ASC) AS next_click_time
    FROM user_clicks
)
SELECT 
    user_id,
    click_time,
    next_click_time,
    ROUND(EXTRACT(EPOCH FROM (next_click_time - click_time)) / 60.0, 2) AS idle_minutes
FROM click_sequence
WHERE next_click_time IS NOT NULL;
```

---

#### Problem 17: Customer Spend Quartiles vs Deciles
* **Focus**: `NTILE(4)` (Quartiles) vs `NTILE(10)` (Deciles)
* **Dialect**: ANSI SQL
* **Pedagogical Note**:
  * **Quartiles (`NTILE(4)`)**: Partitions rows into **4 equal groups** (Top 25%, 25-50%, 50-75%, Bottom 25%).
  * **Deciles (`NTILE(10)`)**: Partitions rows into **10 equal groups** (each representing 10% increments).
* **Schema**: `customer_annual_spend(customer_id INT, total_spend NUMERIC)`
* **Task**: Divide all customers into 4 spending quartiles using `NTILE(4)`. Output `customer_id`, `total_spend`, and assigned `spend_quartile` (1 = lowest, 4 = highest).

```sql
SELECT 
    customer_id,
    total_spend,
    NTILE(4) OVER (ORDER BY total_spend ASC) AS spend_quartile
FROM customer_annual_spend
ORDER BY spend_quartile DESC, total_spend DESC;
```

---

#### Problem 18: Running Cumulative Project Expenditure
* **Focus**: `SUM(...) OVER (...)`, Unbounded Preceding Window Frame
* **Dialect**: ANSI SQL
* **Schema**: `project_expenses(project_id INT, expense_date DATE, amount NUMERIC)`
* **Task**: Calculate the cumulative expenditure over time for each project.

```sql
SELECT 
    project_id,
    expense_date,
    amount,
    SUM(amount) OVER (
        PARTITION BY project_id 
        ORDER BY expense_date ASC 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_spent
FROM project_expenses
ORDER BY project_id, expense_date ASC;
```

---

#### Problem 19: 7-Day Rolling Average API Latency
* **Focus**: Moving Window Frame, `ROWS BETWEEN 6 PRECEDING AND CURRENT ROW`
* **Dialect**: ANSI SQL
* **Schema**: `service_daily_latency(service_name VARCHAR, metric_date DATE, avg_latency_ms NUMERIC)`
* **Task**: Calculate the 7-day moving average latency for each service.

```sql
SELECT 
    service_name,
    metric_date,
    avg_latency_ms,
    ROUND(AVG(avg_latency_ms) OVER (
        PARTITION BY service_name 
        ORDER BY metric_date ASC 
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ), 2) AS rolling_7d_avg_latency
FROM service_daily_latency
ORDER BY service_name, metric_date ASC;
```

---

#### Problem 20: Active Subscriptions During Q3 2026 (Date Overlaps)
* **Focus**: Temporal Interval Overlap
* **Dialect**: ANSI SQL
* **Schema**: `subscriptions(sub_id INT, client_id INT, start_date DATE, end_date DATE)`
* **Task**: Find all subscriptions that were active at any point during Q3 2026 (from `2026-07-01` to `2026-09-30`). Include ongoing subscriptions (`end_date IS NULL`).

```sql
SELECT 
    sub_id,
    client_id,
    start_date,
    end_date
FROM subscriptions
WHERE start_date <= '2026-09-30'
  AND (end_date IS NULL OR end_date >= '2026-07-01');
```

---

#### Problem 21: Date Truncation & Dialect Compatibility
* **Focus**: Monthly Grouping in PostgreSQL vs ANSI SQL
* **Dialect**: PostgreSQL / ANSI SQL
* **Schema**: `transactions(txn_id INT, txn_timestamp TIMESTAMP, amount NUMERIC)`
* **Task**: Calculate total transaction volume grouped by calendar month. Provide both PostgreSQL-specific and standard ANSI SQL formulations.

```sql
-- PostgreSQL Syntax:
SELECT 
    DATE_TRUNC('month', txn_timestamp) AS txn_month,
    COUNT(*) AS total_txns,
    SUM(amount) AS total_amount
FROM transactions
GROUP BY DATE_TRUNC('month', txn_timestamp)
ORDER BY txn_month ASC;

-- Standard ANSI SQL Syntax:
SELECT 
    EXTRACT(YEAR FROM txn_timestamp) AS txn_year,
    EXTRACT(MONTH FROM txn_timestamp) AS txn_month,
    COUNT(*) AS total_txns,
    SUM(amount) AS total_amount
FROM transactions
GROUP BY EXTRACT(YEAR FROM txn_timestamp), EXTRACT(MONTH FROM txn_timestamp)
ORDER BY txn_year, txn_month;
```

---

#### Problem 22: Project Expenditure Restricted Strictly to Completed Milestones
* **Focus**: Milestone Status Filtering, Premature Expenditure Prevention
* **Dialect**: ANSI SQL
* **Pedagogical Note**: When tracking project expenditure against allocated budget, costs must strictly reflect delivered work (`milestone_status = 'COMPLETED'`). Counting planned or in-progress milestones distorts financial audit reports.
* **Schema**: `projects(project_id INT, project_name VARCHAR, allocated_budget NUMERIC)`, `milestones(milestone_id INT, project_id INT, milestone_cost NUMERIC, status VARCHAR)`
* **Task**: For each project, compute the allocated budget, actual expenditure from completed milestones, and budget variance.

```sql
SELECT 
    p.project_id,
    p.project_name,
    p.allocated_budget,
    COALESCE(SUM(CASE WHEN m.status = 'COMPLETED' THEN m.milestone_cost ELSE 0 END), 0.00) AS completed_expenditure,
    p.allocated_budget - COALESCE(SUM(CASE WHEN m.status = 'COMPLETED' THEN m.milestone_cost ELSE 0 END), 0.00) AS budget_variance
FROM projects p
LEFT JOIN milestones m ON p.project_id = m.project_id
GROUP BY p.project_id, p.project_name, p.allocated_budget
ORDER BY budget_variance ASC;
```

---

#### Problem 23: Duplicate Telemetry Packet Detection
* **Focus**: `GROUP BY`, `COUNT(*) > 1`
* **Dialect**: ANSI SQL
* **Schema**: `sensor_stream(sensor_id VARCHAR, recorded_epoch BIGINT, telemetry_payload VARCHAR)`
* **Task**: Identify duplicate transmissions where the same `sensor_id` recorded multiple payloads at the identical `recorded_epoch`.

```sql
SELECT 
    sensor_id,
    recorded_epoch,
    COUNT(*) AS duplicate_count
FROM sensor_stream
GROUP BY sensor_id, recorded_epoch
HAVING COUNT(*) > 1
ORDER BY duplicate_count DESC;
```

---

#### Problem 24: Customer Record Deduplication Retaining Earliest Profile
* **Focus**: Deduplication CTE, `ROW_NUMBER()`
* **Dialect**: ANSI SQL
* **Schema**: `raw_customers(customer_id INT, email VARCHAR, created_at TIMESTAMP)`
* **Task**: Write a query that returns unique customers by `email`, retaining only the single earliest created `customer_id`.

```sql
WITH deduplicated AS (
    SELECT 
        customer_id,
        email,
        created_at,
        ROW_NUMBER() OVER (PARTITION BY email ORDER BY created_at ASC, customer_id ASC) AS rn
    FROM raw_customers
)
SELECT 
    customer_id,
    email,
    created_at
FROM deduplicated
WHERE rn = 1;
```

---

#### Problem 25: Monthly Cohort Retention Rate
* **Focus**: Cohort Analysis, Date Difference
* **Dialect**: ANSI SQL / PostgreSQL
* **Schema**: `user_actions(user_id INT, action_date DATE)`
* **Task**: Find each user's signup month (first action), and calculate Month-1 retention rate (% of users who performed an action in the month following signup).

```sql
WITH user_first_month AS (
    SELECT 
        user_id,
        DATE_TRUNC('month', MIN(action_date)) AS cohort_month
    FROM user_actions
    GROUP BY user_id
),
user_monthly_activity AS (
    SELECT DISTINCT
        user_id,
        DATE_TRUNC('month', action_date) AS activity_month
    FROM user_actions
)
SELECT 
    ufm.cohort_month,
    COUNT(DISTINCT ufm.user_id) AS cohort_size,
    COUNT(DISTINCT uma.user_id) AS retained_month_1,
    ROUND(COUNT(DISTINCT uma.user_id) * 100.0 / COUNT(DISTINCT ufm.user_id), 2) AS month_1_retention_pct
FROM user_first_month ufm
LEFT JOIN user_monthly_activity uma 
       ON ufm.user_id = uma.user_id 
      AND uma.activity_month = ufm.cohort_month + INTERVAL '1 month'
GROUP BY ufm.cohort_month
ORDER BY ufm.cohort_month ASC;
```

---

#### Problem 26: First vs Last Transaction Value
* **Focus**: `FIRST_VALUE()`, `LAST_VALUE()` with Framing
* **Dialect**: ANSI SQL
* **Schema**: `customer_orders(order_id INT, customer_id INT, order_date DATE, order_amount NUMERIC)`
* **Task**: For each customer, display their first order amount and their most recent order amount.

```sql
SELECT DISTINCT
    customer_id,
    FIRST_VALUE(order_amount) OVER (
        PARTITION BY customer_id 
        ORDER BY order_date ASC 
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS initial_order_val,
    LAST_VALUE(order_amount) OVER (
        PARTITION BY customer_id 
        ORDER BY order_date ASC 
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS latest_order_val
FROM customer_orders;
```

---

#### Problem 27: System Continuous Uptime (Gaps & Islands)
* **Focus**: Gaps & Islands, `ROW_NUMBER` Difference
* **Dialect**: ANSI SQL
* **Schema**: `system_daily_status(check_date DATE, is_operational INT)`
* **Task**: Group contiguous periods of operational uptime (`is_operational = 1`) into distinct islands and calculate island length.

```sql
WITH operational_days AS (
    SELECT 
        check_date,
        check_date - CAST(ROW_NUMBER() OVER (ORDER BY check_date ASC) AS INT) AS island_id
    FROM system_daily_status
    WHERE is_operational = 1
)
SELECT 
    MIN(check_date) AS island_start,
    MAX(check_date) AS island_end,
    COUNT(*) AS consecutive_uptime_days
FROM operational_days
GROUP BY island_id
ORDER BY island_start ASC;
```

---

#### Problem 28: Management Hierarchy Tenure Comparison
* **Focus**: Self-Join, Organizational Hierarchy
* **Dialect**: ANSI SQL
* **Schema**: `employees(emp_id INT, emp_name VARCHAR, manager_id INT, hire_date DATE)`
* **Task**: List all employees who have been with the firm longer than their direct manager.

```sql
SELECT 
    e.emp_id,
    e.emp_name AS employee_name,
    e.hire_date AS employee_hire_date,
    m.emp_name AS manager_name,
    m.hire_date AS manager_hire_date
FROM employees e
JOIN employees m ON e.manager_id = m.emp_id
WHERE e.hire_date < m.hire_date
ORDER BY e.hire_date ASC;
```

---

#### Problem 29: Cloud vs On-Premises Asset Reconciliation
* **Focus**: `EXCEPT` / Anti-Join
* **Dialect**: ANSI SQL
* **Schema**: `cloud_assets(asset_tag VARCHAR, region VARCHAR)`, `onprem_inventory(asset_tag VARCHAR, location VARCHAR)`
* **Task**: Find all asset tags registered in `cloud_assets` that have no corresponding record in `onprem_inventory`.

```sql
SELECT asset_tag FROM cloud_assets
EXCEPT
SELECT asset_tag FROM onprem_inventory;

-- Alternative Outer-Join formulation:
SELECT c.asset_tag
FROM cloud_assets c
LEFT JOIN onprem_inventory o ON c.asset_tag = o.asset_tag
WHERE o.asset_tag IS NULL;
```

---

#### Problem 30: High-Value Accounts with Zero Support Inquiries
* **Focus**: `NOT EXISTS` vs `LEFT JOIN ... WHERE IS NULL`
* **Dialect**: ANSI SQL
* **Schema**: `accounts(account_id INT, tier VARCHAR, annual_contract_val NUMERIC)`, `support_tickets(ticket_id INT, account_id INT, created_at DATE)`
* **Task**: Find all `'ENTERPRISE'` accounts with `annual_contract_val > 10000000` (JPY 10M) that have submitted zero support tickets in the last 180 days.

```sql
SELECT 
    a.account_id,
    a.annual_contract_val
FROM accounts a
WHERE a.tier = 'ENTERPRISE'
  AND a.annual_contract_val > 10000000
  AND NOT EXISTS (
      SELECT 1 
      FROM support_tickets s
      WHERE s.account_id = a.account_id
        AND s.created_at >= CURRENT_DATE - INTERVAL '180 days'
  );
```

---

## 📐 PART 3: Quantitative Mathematics & Business Economics

Every problem below has been independently calculated and verified in Python.

---

### Problem 01: Rule of 72 vs Exact Compound Annual Growth Rate (CAGR)
* **Question**: An IT consulting practice in Tokyo grows annual revenue from JPY 100M to JPY 200M over 6 years. Compare the Rule-of-72 mental approximation with the mathematically exact CAGR.
* **Exact Formula**:
  $$\text{Exact CAGR} = \left(rac{V_f}{V_i}
ight)^{1/t} - 1 = \left(rac{200}{100}
ight)^{1/6} - 1 = 2^{0.1667} - 1 = 12.2462\% pprox 12.25\%$$
* **Rule-of-72 Approximation**:
  $$g pprox rac{72}{t} = rac{72}{6} = 12.00\%$$
* **Evaluation**: The Rule of 72 yields 12.00%, underestimating the exact rate (12.25%) by only 0.25 percentage points. In interview math, cite: *"Using Rule of 72, growth is ~12%; exact calculation yields 12.25%."*

---

### Problem 02: Customer Lifetime Value (LTV) & Churn Mechanics
* **Question**: A SaaS enterprise product charges an Average Revenue Per User (ARPU) of $500/month with a 70% Gross Margin. The monthly customer churn rate is 3.5%. Calculate customer lifetime (in months) and expected LTV.
* **Formulas & Steps**:
  $$\text{Expected Lifetime (months)} = rac{1}{\text{Churn Rate}} = rac{1}{0.035} pprox 28.57\text{ months}$$
  $$\text{LTV} = rac{\text{ARPU} \times \text{Gross Margin}}{\text{Churn Rate}} = rac{500 \times 0.70}{0.035} = rac{350}{0.035} = \$10,000.00$$
* **Answer**: Expected customer lifetime is 28.57 months; LTV is exactly **$10,000.00**.

---

### Problem 03: Customer Acquisition Cost (CAC) Payback Period
* **Question**: A client invests $4,200 to acquire an enterprise software customer. The customer generates $600/month with a 70% gross margin. Calculate the CAC payback period in both months and decimal years.
* **Formulas & Steps**:
  $$\text{Monthly Gross Profit Contribution} = \$600 \times 0.70 = \$420/\text{month}$$
  $$\text{Payback Period (months)} = rac{\text{CAC}}{\text{Monthly Gross Contribution}} = rac{4200}{420} = 10.0\text{ months}$$
  $$\text{Payback Period (years)} = rac{10}{12} pprox 0.833\text{ years}$$
* **Answer**: Exactly **10.0 months** (0.833 years). This beats the consulting benchmark target of $<12$ months.

---

### Problem 04: Weighted Average Cost of Capital (WACC) with After-Tax Debt
* **Question**: An enterprise is funded by $60M Equity (cost $r_e = 12\%$) and $40M Debt (cost $r_d = 6\%$). The corporate tax rate is $T = 30\%$. Calculate WACC.
* **Formulas & Steps**:
  $$V = E + D = 60 + 40 = \$100M, \quad W_e = 0.60, \quad W_d = 0.40$$
  $$\text{After-Tax Cost of Debt} = r_d \times (1 - T) = 6\% \times (1 - 0.30) = 4.20\%$$
  $$\text{WACC} = W_e \cdot r_e + W_d \cdot r_d (1 - T) = 0.60 \times 12\% + 0.40 \times 4.20\% = 7.20\% + 1.68\% = 8.88\%$$
* **Answer**: **8.88%**.

---

### Problem 05: Overall Equipment Effectiveness (OEE) Decomposition
* **Question**: An automotive plant runs an 8-hour shift (480 mins) with 60 mins planned maintenance. Operating breakdown is 42 mins. Total parts produced is 700 units (ideal rate 0.5 mins/part). 28 parts were defective. Compute Availability, Performance, Quality, and composite OEE.
* **Decomposition**:
  * **Planned Production Time** = $480 - 60 = 420\text{ mins}$.
  * **Operating Time** = $420 - 42 = 378\text{ mins}$.
  * **Availability** = $rac{378}{420} = 0.9000$ (**90.00%**).
  * **Ideal Operating Time** = $700 \times 0.5 = 350\text{ mins}$.
  * **Performance** = $rac{350}{378} pprox 0.9259$ (**92.59%**).
  * **Good Parts** = $700 - 28 = 672\text{ units}$.
  * **Quality** = $rac{672}{700} = 0.9600$ (**96.00%**).
  $$\text{OEE} = 0.90 \times \left(rac{350}{378}
ight) \times 0.96 = 0.90 \times 0.925926 \times 0.96 = 0.8000 \quad (80.00\%)$$
* **Answer**: OEE is exactly **80.00%** (World-class manufacturing benchmark is $\ge 85\%$).

---

### Problem 06: High Availability SLA Downtime Budget
* **Question**: For a calendar year (365 days = 8,760 hours = 525,600 minutes), compute the allowed downtime for "three nines" (99.9%), "four nines" (99.99%), and "five nines" (99.999%).
* **Formulas & Exact Calculations**:
  * **99.9% ("Three Nines")**: $0.001 \times 8760 = 8.76\text{ hours/year}$ (525.6 minutes).
  * **99.99% ("Four Nines")**: $0.0001 \times 525600 = 52.56\text{ minutes/year}$ (0.876 hours).
  * **99.999% ("Five Nines")**: $0.00001 \times 525600 = 5.256\text{ minutes/year}$ (315.36 seconds).
* **Strategic Takeaway**: Moving from 99.9% to 99.99% reduces downtime from 8.76 hours to under 53 minutes, requiring multi-AZ failover and automated health checks.

---

### Problem 07: IoT Telemetry Storage: Decimal (GB) vs Binary (GiB)
* **Question**: 1,000 smart sensors transmit 50 bytes of telemetry per second continuously for 30 days. Compute the total storage requirement in decimal Gigabytes (GB, SI) and binary Gibibytes (GiB, IEC).
* **Calculations**:
  $$\text{Total Seconds} = 30 \times 86400 = 2,592,000\text{ seconds}$$
  $$\text{Total Bytes} = 1000 \times 50 \times 2,592,000 = 129,600,000,000\text{ bytes}$$
  $$\text{Decimal GB} = rac{129,600,000,000}{10^9} = 129.60\text{ GB}$$
  $$\text{Binary GiB} = rac{129,600,000,000}{2^{30}} = rac{129,600,000,000}{1,073,741,824} pprox 120.70\text{ GiB}$$
* **Answer**: **129.60 GB** vs **120.70 GiB** (Difference of 8.90 units due to base-10 vs base-2 definitions).

---

### Problem 08: Classification Threshold & Asymmetric Cost Optimization
* **Question**: In an enterprise fraud detection pipeline evaluating 10,000 transactions (200 fraudulent, 9,800 legitimate):
  * **Model A**: Recall = 95% (190 frauds caught, 10 missed False Negatives); False Positive Rate = 3.0% (294 False Positives).
  * **Model B**: Recall = 80% (160 frauds caught, 40 missed False Negatives); False Positive Rate = 0.5% (49 False Positives).
  * Cost of missed fraud (FN) = $1,500. Cost of reviewing a false alarm (FP) = $25.
  Determine which model minimizes total business loss.
* **Calculations**:
  $$\text{Total Cost Model A} = (10 \times \$1,500) + (294 \times \$25) = \$15,000 + \$7,350 = \$22,350$$
  $$\text{Total Cost Model B} = (40 \times \$1,500) + (49 \times \$25) = \$60,000 + \$1,225 = \$61,225$$
* **Answer**: **Model A saves $38,875** compared to Model B. In fraud detection, high recall is worth accepting higher false alarms due to the massive cost asymmetry ($1,500 vs $25).

---

### Problem 09: Plant Break-even Capacity Utilization
* **Question**: An industrial electronics plant has annual fixed operating costs of $1,800,000. Maximum plant capacity is 100,000 units/year. Selling price is $50/unit; variable cost is $20/unit. Find break-even volume and required capacity utilization.
* **Formulas & Steps**:
  $$\text{Unit Contribution Margin} = P - V = \$50 - \$20 = \$30/\text{unit}$$
  $$\text{Break-even Volume} = rac{\text{Fixed Costs}}{\text{Unit Contribution Margin}} = rac{1,800,000}{30} = 60,000\text{ units}$$
  $$\text{Capacity Utilization} = rac{60,000}{100,000} = 60.0\%$$
* **Answer**: Break-even occurs at **60,000 units** (**60.0%** plant capacity).

---

### Problem 10: 5-Year Cloud Migration Total Cost of Ownership (TCO)
* **Question**: Compare 5-year TCO between On-Premise and Public Cloud:
  * **On-Premise**: Hardware CapEx = $1,200,000 (Year 0). Annual power/cooling/space = $150,000/yr. Annual maintenance/licensing = $90,000/yr.
  * **Cloud**: One-time migration/setup = $300,000. 3-Year Reserved compute/storage = $320,000/yr.
* **Calculations**:
  $$\text{TCO}_{\text{On-Prem}} = \$1,200,000 + 5 \times (\$150,000 + \$90,000) = \$1,200,000 + \$1,200,000 = \$2,400,000$$
  $$\text{TCO}_{\text{Cloud}} = \$300,000 + 5 \times \$320,000 = \$300,000 + \$1,600,000 = \$1,900,000$$
  $$\text{Net 5-Year Savings} = \$2,400,000 - \$1,900,000 = \$500,000 \quad (20.83\%\text{ reduction})$$
* **Answer**: Cloud migration delivers **$500,000 net savings** (20.83% TCO reduction).

---

### Problem 11: Little's Law in API Microservice Concurrency
* **Question**: A payment microservice processes an average arrival rate of $\lambda = 250\text{ requests/sec}$. The average response latency is $W = 80\text{ milliseconds}$. Calculate the mean number of concurrent requests $L$ in the system.
* **Formula & Steps**:
  $$W = 80\text{ ms} = 0.080\text{ seconds}$$
  $$L = \lambda \times W = 250 \times 0.080 = 20\text{ concurrent requests}$$
* **Answer**: Exactly **20 concurrent in-flight requests**. If thread pool capacity is 30, the service operates safely at 66.7% capacity.

---

### Problem 12: Discounted Cash Flow & Net Present Value (NPV)
* **Question**: A digital transformation project requires an initial investment of $500,000. Projected cash inflows are: Year 1: $200k, Year 2: $250k, Year 3: $250k. The enterprise discount rate is 10%. Calculate undiscounted ROI and NPV.
* **Calculations**:
  $$\text{Undiscounted Net Gain} = (200k + 250k + 250k) - 500k = \$700,000 - \$500,000 = \$200,000$$
  $$\text{Undiscounted ROI} = rac{200,000}{500,000} \times 100\% = 40.0\%$$
  $$\text{PV}_{\text{Year 1}} = rac{200,000}{1.10^1} pprox \$181,818.18$$
  $$\text{PV}_{\text{Year 2}} = rac{250,000}{1.10^2} pprox \$206,611.57$$
  $$\text{PV}_{\text{Year 3}} = rac{250,000}{1.10^3} pprox \$187,828.70$$
  $$\text{Total Present Value} = \$576,258.45$$
  $$\text{NPV} = \$576,258.45 - \$500,000 = +\$76,258.45$$
* **Answer**: Undiscounted ROI is **40.0%**; Net Present Value at 10% discount is **+$76,258.45** (financially accretive).

---

### Problem 13: Compound Growth vs Simple Interest Accumulation
* **Question**: An endowment of $100,000 earns 8% per annum over 10 years. Compare future value under simple interest versus annual compounding.
* **Calculations**:
  $$\text{FV}_{\text{Simple}} = \$100,000 \times [1 + (0.08 \times 10)] = \$100,000 \times 1.80 = \$180,000.00$$
  $$\text{FV}_{\text{Compound}} = \$100,000 \times (1.08)^{10} = \$100,000 \times 2.158925 = \$215,892.50$$
  $$\text{Compounding Premium} = \$215,892.50 - \$180,000.00 = \$35,892.50$$
* **Answer**: Compounding yields an additional **$35,892.50** (+19.94% above simple interest).

---

### Problem 14: Data Migration Bandwidth & Transfer Time
* **Question**: A database snapshot of 4.5 Terabytes (TB) must be transferred over a 10 Gbps dedicated interconnect operating at 80% effective utilization. Calculate transfer time in seconds and hours.
* **Calculations**:
  $$\text{Total Bits} = 4.5\text{ TB} = 4.5 \times 10^{12}\text{ bytes} \times 8 = 36.0 \times 10^{12}\text{ bits}$$
  $$\text{Effective Bandwidth} = 10\text{ Gbps} \times 0.80 = 8.0\text{ Gbps} = 8.0 \times 10^9\text{ bits/sec}$$
  $$\text{Transfer Time (seconds)} = rac{36.0 \times 10^{12}}{8.0 \times 10^9} = 4,500\text{ seconds}$$
  $$\text{Transfer Time (hours)} = rac{4,500}{3,600} = 1.25\text{ hours} \quad (1\text{ hour } 15\text{ mins})$$
* **Answer**: Exactly **4,500 seconds** (1.25 hours).

---

### Problem 15: Multi-Cloud Blended Cost per Transaction
* **Question**: A distributed architecture processes 100,000 daily transactions across 3 cloud providers:
  * AWS: 50,000 tx @ $0.04/tx
  * Azure: 30,000 tx @ $0.06/tx
  * GCP: 20,000 tx @ $0.09/tx
  Calculate the weighted average cost per transaction.
* **Calculations**:
  $$\text{Total Spend} = (50,000 \times 0.04) + (30,000 \times 0.06) + (20,000 \times 0.09) = 2,000 + 1,800 + 1,800 = \$5,600$$
  $$\text{Blended Cost/tx} = rac{\$5,600}{100,000} = \$0.0560/\text{transaction} \quad (5.60\text{ cents})$$
* **Answer**: **$0.0560 per transaction**.

---

### Problem 16: Data Center Power Usage Effectiveness (PUE)
* **Question**: A Tokyo data center consumes 15.0 GWh/year total facility energy, of which 10.0 GWh powers IT server equipment and 5.0 GWh powers cooling/lighting. If liquid immersion cooling cuts overhead to 2.0 GWh, calculate PUE before and after, plus energy savings percentage.
* **Calculations**:
  $$\text{PUE}_{\text{Initial}} = rac{\text{Total Energy}}{\text{IT Energy}} = rac{15.0}{10.0} = 1.50$$
  $$\text{PUE}_{\text{New}} = rac{10.0 + 2.0}{10.0} = rac{12.0}{10.0} = 1.20$$
  $$\text{Total Energy Reduction} = rac{15.0 - 12.0}{15.0} \times 100\% = 20.0\%$$
* **Answer**: PUE improves from **1.50 to 1.20**, reducing total power consumption by **20.0%**.

---

### Problem 17: Machine Learning Confusion Matrix Performance
* **Question**: On an imbalanced test dataset of 1,000 samples (100 Positives, 900 Negatives), a model yields: $TP = 80, FN = 20, FP = 40, TN = 860$. Calculate Precision, Recall, Specificity, and F1-Score.
* **Formulas & Steps**:
  $$\text{Precision} = rac{TP}{TP + FP} = rac{80}{80 + 40} = rac{80}{120} pprox 66.67\%$$
  $$\text{Recall} = rac{TP}{TP + FN} = rac{80}{80 + 20} = rac{80}{100} = 80.00\%$$
  $$\text{Specificity} = rac{TN}{TN + FP} = rac{860}{860 + 40} = rac{860}{900} pprox 95.56\%$$
  $$\text{F1-Score} = 2 \times rac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = 2 \times rac{(2/3) \times 0.8}{(2/3) + 0.8} = rac{16/15}{22/15} = rac{8}{11} pprox 72.73\%$$
* **Answer**: Precision = **66.67%**, Recall = **80.00%**, Specificity = **95.56%**, F1-Score = **72.73%**.

---

### Problem 18: Inventory Turnover & Working Capital Unlocked
* **Question**: A retailer reports annual COGS of $48,000,000 and average inventory of $8,000,000. Calculate Inventory Turnover and Days Sales of Inventory (DSI). If digital demand sensing boosts turnover to 8.0x, how much cash working capital is unlocked?
* **Calculations**:
  $$\text{Turnover} = rac{\text{COGS}}{\text{Avg Inventory}} = rac{48,000,000}{8,000,000} = 6.0\text{ turns/year}$$
  $$\text{DSI} = rac{365}{\text{Turnover}} = rac{365}{6.0} pprox 60.83\text{ days}$$
  $$\text{Required Inventory @ 8.0x} = rac{\$48,000,000}{8.0} = \$6,000,000$$
  $$\text{Unlocked Working Capital} = \$8,000,000 - \$6,000,000 = \$2,000,000$$
* **Answer**: Current turnover is **6.0x** (DSI = 60.83 days). Accelerating turnover to 8.0x unlocks **$2,000,000** in cash.

---

### Problem 19: Cold Storage Lifecycle Tiering Cost Benefit
* **Question**: An enterprise retains 100 TB (100,000 GB) of compliance archives in standard cloud storage @ $0.023/GB/month ($27,600/year). Glacier Deep Archive costs $0.00099/GB/month ($1,188/year). If 2 TB is retrieved once annually at $0.02/GB retrieval fee + $0.09/GB egress fee ($220 total retrieval cost), calculate net annual financial savings.
* **Calculations**:
  $$\text{Standard Storage Annual Cost} = 100,000 \times 0.023 \times 12 = \$27,600.00$$
  $$\text{Deep Archive Storage Annual Cost} = 100,000 \times 0.00099 \times 12 = \$1,188.00$$
  $$\text{Storage Savings} = \$27,600 - \$1,188 = \$26,412.00$$
  $$\text{Retrieval & Egress Cost} = 2,000\text{ GB} \times (\$0.02 + \$0.09) = 2,000 \times \$0.11 = \$220.00$$
  $$\text{Net Annual Benefit} = \$26,412.00 - \$220.00 = \$26,192.00 \quad (94.90\%\text{ net savings})$$
* **Answer**: **$26,192.00 net annual savings** (94.90% cost reduction).

---

### Problem 20: Market Sizing TAM, SAM & SOM (Bottom-Up vs Top-Down)
* **Question**: Estimate the addressable market for Cloud ERP Modernization targeting mid-market manufacturing companies in Japan:
  * Top-Down: Total Japan Enterprise Software Market is $12B. Manufacturing comprises 35% ($4.2B); cloud modernization slice is 25% -> TAM = $1.05B.
  * Bottom-Up: 25,000 mid-market manufacturers in Japan. 40% operate legacy on-prem systems (10,000 firms). Average contract value is $50,000/year.
  * Compute Bottom-Up TAM. Sizing SAM (Kanto & Kansai industrial clusters, 65% of firms) and SOM (Accenture Japan target 12% market share).
* **Calculations**:
  $$\text{Bottom-Up TAM} = 10,000\text{ firms} \times \$50,000/\text{firm/year} = \$500,000,000/\text{year} \quad (\$500M)$$
  $$\text{SAM (65\% Cluster Focus)} = \$500,000,000 \times 0.65 = \$325,000,000/\text{year} \quad (\$325M)$$
  $$\text{SOM (12\% Target Share)} = \$325,000,000 \times 0.12 = \$39,000,000/\text{year} \quad (\$39M)$$
* **Answer**: Bottom-Up TAM is **$500M**, SAM is **$325M**, and attainable SOM is **$39M/year**.

---

## ☁️ PART 4: Technology & Architecture Comprehension

### Question 4.1: Cloud Architecture Selection (Monolith vs Serverless Microservices)
* **Scenario**: A Japanese retail enterprise with 800 physical stores suffers checkout stalls during flash sale events. Evaluate migrating from local store servers to AWS Lambda/Azure Functions with Edge Caching.
* **Evaluation & Trade-offs**:
  1. **Elastic Scaling**: Serverless handles 0 to 10,000 requests/sec automatically without manual server provisioning.
  2. **Cost Structure (CapEx -> OpEx)**: Replaces idle on-prem server depreciation with per-millisecond billing.
  3. **High Availability & Edge Continuity**: Local edge caching allows POS terminals to complete transactions during intermittent cloud network partitions.

### Question 4.2: Enterprise RAG Architecture Trade-offs
* **Scenario**: A Tokyo insurance provider requires an internal AI tool to search 50,000 policy contracts. Compare Retrieval-Augmented Generation (RAG) against Fine-Tuning.
* **Evaluation & Trade-offs**:
  1. **Dynamic Updates**: RAG updates instantly by inserting new policy embeddings into the vector database. Fine-tuning requires expensive re-training.
  2. **Hallucination & Auditability**: RAG provides exact page and clause citations.
  3. **Data Security**: Vector search enforces Role-Based Access Control (RBAC) so agents only retrieve policies matching their authorization tier.

---

## ⏱️ PART 5: Full Timed 90-Minute Mock Assessment Simulation

### Test Blueprint & Timing:
* **Section 1: Algorithmic Coding (Python)** — 2 Problems (35 mins)
  * Problem A: Challenge 02 (Sliding Window Inactivity Timeout)
  * Problem B: Challenge 07 (Top-K Frequent API Endpoints)
* **Section 2: Data & SQL Querying** — 2 Problems (25 mins)
  * Problem A: Problem 07 (Department Tool Adoption with HAVING)
  * Problem B: Problem 14 (Latest IoT Heartbeat Snapshot with ROW_NUMBER)
* **Section 3: Quantitative Math & Logic** — 3 Problems (20 mins)
  * Problem A: Problem 01 (CAGR vs Rule of 72)
  * Problem B: Problem 05 (OEE Decomposition)
  * Problem C: Problem 10 (Cloud TCO Analysis)
* **Section 4: Technical Comprehension** — 1 Scenario (10 mins)
  * Problem A: Question 4.1 (Cloud Migration Trade-offs)
