# Topic Master 02: Python Algorithmic Logic, Runtime Internals & Code Puzzles

> **Consolidated Module**: ACC-JAPAN-TOPIC-02 (Python Programming & Algorithmic Logic)  
> **Target Assessment**: Online Technical/Coding Assessment (Python Track) & Technical Interview Live Coding  
> **Structure**:
> - **SECTION A**: Python Runtime Internals, Memory Management, Slicing Complexity & Big-O Reference Cheat Sheet
> - **SECTION B**: Algorithmic Patterns & 20 Master Solved Code Problems with Verifiable Python Assertions
> - **SECTION C**: High-Frequency Coding & Algorithmic Logic Question Bank with Common Candidate Traps

---


# SECTION A: Programming Logic, Python Internals & Algorithmic Mechanics

Programming Logic, Python Internals & Algorithmic Mechanics (Priority 1)

### Explainer A.1: Python Execution Model, PyObject, Memory Allocation & Garbage Collection

#### 1. Mental Model: The CPython Runtime & "Everything is an Object"
In native compiled languages like C/C++, variables correspond to fixed memory addresses on the stack or heap holding primitive binary data (e.g., an 8-byte IEEE 754 float). In CPython, **every variable is a pointer to a heap-allocated `PyObject` structure**.

```text
CPython PyObject Architecture (64-bit architecture):
+-----------------------------------------------------------+
| ob_refcnt  (8 bytes) -> 64-bit reference counter          |
| ob_type    (8 bytes) -> Pointer to type object structure  |
| [Type-specific payload, e.g., ob_size, ob_digit array]    |
+-----------------------------------------------------------+
```
Even a simple integer `x = 42` is not a raw 4-byte scalar; it is a full 28-byte `PyLongObject` allocated on the heap containing reference tracking metadata and arbitrary-precision integer digit buffers.

#### 2. Memory Allocation & Small Object Allocator (PyMalloc)
To prevent constant calls to the OS kernel `malloc()` (which introduces severe fragmentation for tiny objects), CPython incorporates **PyMalloc**:
* **Arenas**: 256 KB memory chunks allocated from the OS.
* **Pools**: 4 KB subdivisions within arenas, dedicated to specific size classes (8 bytes, 16 bytes, up to 512 bytes).
* **Blocks**: Fixed-size memory chunks inside pools. When an integer or small string is created, CPython assigns an available block in $O(1)$ time without kernel context switches.
```python
a = 100
b = 100
assert a is b  # True: Both names point to the singleton cached PyLongObject!

c = 1000
d = 1000
# c is d may evaluate to False because integers outside [-5, 256] allocate distinct objects.
```

#### 3. Garbage Collection Mechanics (Reference Counting + Generational Cycler)
CPython employs a two-tier memory reclamation engine:
1. **Reference Counting (Primary Engine)**:
   - Every `PyObject` tracks how many references point to it (`ob_refcnt`).
   - When a reference goes out of scope, is reassigned, or deleted (`del`), `ob_refcnt` decrements by 1.
   - The instant `ob_refcnt == 0`, memory is immediately deallocated back to PyMalloc.
   - *Limitation*: Reference counting cannot reclaim **cyclic references** (e.g., node $A$ points to node $B$, and node $B$ points back to node $A$; deleting external pointers leaves both with `refcnt == 1`, causing an permanent memory leak).
2. **Generational Cyclic Garbage Collector (Secondary Engine)**:
   - Scans container objects (`list`, `dict`, `set`, custom classes, tuples containing mutable elements).
   - Groups objects into three generations: **Generation 0** (newly allocated), **Generation 1** (survived 1 collection), and **Generation 2** (long-lived objects).
   - *Collection Frequency*: Gen 0 is inspected frequently (e.g., after 700 net allocations). Objects surviving inspection are promoted to Gen 1. If Gen 1 collections exceed 10 cycles, Gen 2 is collected.
   - *Algorithm*: Uses pointer subtraction to identify isolated unreachable cyclic reference graphs and frees them.

#### 4. The Global Interpreter Lock (GIL) Explainer
* CPython's memory allocator is not thread-safe. To prevent race conditions on `ob_refcnt` updates, CPython uses the **GIL (Global Interpreter Lock)** — a mutual exclusion lock that permits only **one native thread to execute Python bytecode at any given moment**, regardless of how many CPU cores are physically available.
* **CPU-Bound Code**: Spawning 8 Python `threading.Thread` instances on an 8-core CPU does *not* speed up calculation; lock contention and thread switching actually make it run slower! For CPU-bound acceleration, you must use `multiprocessing` (separate OS processes with independent memory spaces and separate GILs) or offload computation to vectorized C/C++ libraries (NumPy, Polars).
* **I/O-Bound Code**: Python threads release the GIL during network I/O, disk operations, and database calls (`time.sleep()`, socket reads). Thus, multi-threading is highly effective for concurrent API scraping, database queries, and web servers.

---

### Explainer A.2: Dynamic Array Resizing, Slicing Mechanics & Shallow vs Deep Copy

#### 1. Under-the-Hood: How Python `list` Over-Allocates
A Python `list` is not a linked list; it is a **contiguous array of pointers to `PyObject` instances** (`PyObject** ob_item`).
When you call `list.append()`, CPython cannot afford to call `realloc()` on every single element because memory reallocation is an $O(N)$ memory copying operation. Instead, it uses **geometric amortized over-allocation**:

$$\text{new\_allocated} = \text{newsize} + (\text{newsize} \gg 3) + (\text{newsize} < 9 \ ? \ 3 : 6)$$

* **Growth Sequence**: 0, 4, 8, 16, 24, 32, 40, 52, 64, 76, ...
* **Amortized Complexity**: Appending $N$ elements takes $O(N)$ total time, yielding **$O(1)$ amortized cost per append**.
* **The `insert(0, x)` Disaster**: Inserting at index 0 requires shifting every existing pointer in memory rightward by one slot — a strictly **$O(N)$ operation**. If an assessment problem requires a double-ended queue, always use `collections.deque` (implemented as a doubly-linked list of 64-element block arrays), providing strictly $O(1)$ `appendleft()` and `popleft()`.

#### 2. Slicing Mechanics & Off-by-One Protection
Slicing `arr[start:stop:step]` constructs a brand new `list` containing shallow copies of the pointer references in the range $[start, stop)$.
* `start`: Inclusive boundary (defaults to 0 if omitted).
* `stop`: Exclusive boundary (defaults to `len(arr)` if omitted).
* `step`: Index delta (negative values step backwards).
* **Slice Length Identity**: When `step = 1`, the number of elements extracted is strictly $\max(0, stop - start)$.

```python
data = [10, 20, 30, 40, 50, 60]
# Indices:  0   1   2   3   4   5
# Negatives:-6  -5  -4  -3  -2  -1

assert data[2:5] == [30, 40, 50]       # Length = 5 - 2 = 3 elements
assert data[-3:] == [40, 50, 60]       # Last 3 elements
assert data[:3]  == [10, 20, 30]       # First 3 elements
assert data[::2] == [10, 30, 50]       # Even indices
assert data[::-1] == [60, 50, 40, 30, 20, 10]  # O(N) reverse
```

#### 3. Shallow Copy vs Deep Copy
* **Shallow Copy (`list.copy()`, `arr[:]`, `dict.copy()`)**: Allocates a new outer container, but **copies the object references** of its contents. If the elements are themselves mutable (e.g., nested lists, dictionaries), modifying an inner element through the clone mutates the original!
* **Deep Copy (`copy.deepcopy()`)**: Recursively traverses the object graph, allocating brand new memory for every nested mutable container and mapping traversed object IDs to avoid infinite loops on cyclic graphs.

```python
import copy

original = [[1, 2], [3, 4]]
shallow = original.copy()
deep = copy.deepcopy(original)

shallow[0][0] = 999
assert original[0][0] == 999  # Mutated original! Because pointer was shared!

deep[1][1] = 888
assert original[1][1] == 4    # Untouched! Deep copy allocated distinct memory!
```

---

### Explainer A.3: Hash Table Internals, Collision Resolution & Two Sum Invariants

#### 1. CPython Compact Hash Table Architecture
Since Python 3.6+, dictionaries are ordered by insertion. CPython achieves this using a **two-table compact array design**:
1. **Sparse Hash Index Table (`indices`)**: An array of small integers (e.g., int8, int16) indexed by `hash(key) % table_size`.
2. **Dense Entries Table (`entries`)**: An array of contiguous structs storing `[hash_code, key_pointer, value_pointer]`.

```text
Visualizing CPython Dict ("compact table"):
indices: [ -1,  0, -1,  1, -1, -1, -1, -1 ]  <- hash(key) % 8 points here
entries:
  0: hash=39481, key="tokyo", value="HQ"
  1: hash=12093, key="kyoto", value="Branch"
```
* **Memory Savings**: Replaces 24-byte sparse bucket tables with 1-byte indices arrays, cutting dictionary memory consumption by $30\%\text{--}40\%$.
* **Collision Resolution**: Uses open addressing with **pseudo-random perturbation probing**:
  $$j = (5j + 1 + \text{perturb}) \pmod{2^i}$$
  where `perturb` is initialized to the full hash code and shifted right by 5 bits on each probe iteration (`perturb >>= 5`). This decorrelates linear clustering and rapidly scans the table.

#### 2. The Two-Sum Mathematical Invariant
* **Problem**: Given array $A$ and target integer $K$, find indices $(i, j)$ such that $A[i] + A[j] = K$ with $i \ne j$.
* **Brute Force**: Two nested loops testing all $\frac{N(N-1)}{2}$ pairs $\implies O(N^2)$ time, $O(1)$ space.
* **Hash Invariant Transformation**: Rearrange the equation:
  $$A[i] + A[j] = K \iff A[i] = K - A[j]$$
* **Algorithm**: Iterate through array with pointer $j$. The required complement is $C_j = K - A[j]$. If $C_j$ exists in our hash table, we have discovered the exact matching pair in $O(1)$ lookup time. If not, record $A[j]$ and its index $j$ into the hash table.
* **Time Complexity**: Exactly 1 pass over array $\implies \mathbf{O(N)}$ time, $\mathbf{O(N)}$ auxiliary space.

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    lookup = {}  # complement -> index
    for current_idx, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], current_idx]
        lookup[num] = current_idx
    return []

assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
assert two_sum([3, 3], 6) == [0, 1]
```

---

### Explainer A.4: Algorithmic Invariants — Two Pointers & Sliding Window Proofs

#### 1. Two Pointers Invariant Proof (Sorted Array Target Sum)
* **Precondition**: Array $A$ is sorted monotonically ($A[0] \le A[1] \le \dots \le A[N-1]$).
* **Pointers**: `left = 0`, `right = N - 1`.
* **Invariant**: At any step, the search space for valid solutions is strictly confined to the subsegment $A[\text{left} \dots \text{right}]$.
* **Deduction Steps**:
  1. Compute $S = A[\text{left}] + A[\text{right}]$.
  2. If $S == \text{Target}$, return indices.
  3. If $S < \text{Target}$: Since $A[\text{right}]$ is the largest available element in the search window, pairing $A[\text{left}]$ with any other element in $A[\text{left} \dots \text{right}]$ would produce an even smaller sum $< S < \text{Target}$. Thus, $A[\text{left}]$ cannot be part of any valid pair. We safely discard it by incrementing `left += 1`.
  4. If $S > \text{Target}$: By symmetric logic, $A[\text{right}]$ paired with any element in $A[\text{left} \dots \text{right}]$ produces a sum $\ge A[\text{left}] + A[\text{right}] > \text{Target}$. We safely discard $A[\text{right}]$ by decrementing `right -= 1`.
* **Complexity**: Each comparison eliminates at least one element. Maximum comparisons $= N \implies \mathbf{O(N)}$ time, $\mathbf{O(1)}$ space.

#### 2. Sliding Window Dynamic Constraint Maintenance
Sliding windows solve contiguous subarray optimization problems.
* **Invariant**: Maintain a window $[L, R]$ such that a state predicate $P(L, R)$ remains satisfied.
* **State Expansion**: Increment $R$, assimilating $A[R]$ into the running window telemetry.
* **State Contraction**: If incorporating $A[R]$ causes $P(L, R)$ to become `FALSE`, increment $L$ iteratively, removing $A[L]$ from running metrics until $P(L, R)$ is restored to `TRUE`.

```python
def max_ones_after_one_flip(s: str) -> int:
    # Longest contiguous subarray of 1s with at most one 0 flipped.
    # Predicate P(L, R): count('0' in s[L:R+1]) <= 1.
    left = 0
    zero_count = 0
    best_len = 0
    
    for right in range(len(s)):
        if s[right] == '0':
            zero_count += 1
            
        # Contract while invariant is violated
        while zero_count > 1:
            if s[left] == '0':
                zero_count -= 1
            left += 1
            
        # Here P(L, R) is guaranteed TRUE
        best_len = max(best_len, right - left + 1)
        
    return best_len

assert max_ones_after_one_flip("110110111") == 6  # Flipping second zero yields "110111111" -> 6 ones
assert max_ones_after_one_flip("000") == 1
assert max_ones_after_one_flip("1111") == 4
```

---

### Explainer A.5: Monotonic Structures, Recursion Stack Frames & Trace Tables

#### 1. Monotonic Stack Mechanics (Next Greater Element)
A **Monotonic Stack** enforces strict element ordering (either monotonically increasing or decreasing).
* **Use Case**: Finding the **Next Greater Element (NGE)** or Nearest Smaller Element for every position in an array in $O(N)$ linear time, avoiding $O(N^2)$ brute-force scans.
* **Invariant**: Elements in the stack are strictly decreasing from bottom to top.
* **Execution**:
  When element $A[i]$ arrives, while stack is non-empty and $A[i] > A[\text{stack.top()}]$, $A[i]$ is the Next Greater Element for $\text{stack.top()}$. We pop the stack and record $A[i]$. Then we push index $i$.

```python
def next_greater_elements(nums: list[int]) -> list[int]:
    result = [-1] * len(nums)
    stack = []  # stores indices
    
    for i, val in enumerate(nums):
        while stack and nums[stack[-1]] < val:
            popped_idx = stack.pop()
            result[popped_idx] = val
        stack.append(i)
        
    return result

assert next_greater_elements([2, 1, 2, 4, 3]) == [4, 2, 4, -1, -1]
```

#### 2. Trace Table: Tracking Recursion & Stack State
Consider recursive binary search on sorted array `[2, 5, 8, 12, 16, 23, 38, 56, 72, 91]`, searching for `Target = 23`:

| Call # | `low` | `high` | `mid` | `arr[mid]` | Condition Check | Action / Next Frame |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | 0 | 9 | $0 + (9-0)//2 = 4$ | 16 | $16 < 23$ | `low = mid + 1 = 5` |
| **2** | 5 | 9 | $5 + (9-5)//2 = 7$ | 56 | $56 > 23$ | `high = mid - 1 = 6` |
| **3** | 5 | 6 | $5 + (6-5)//2 = 5$ | 23 | $23 == 23$ | **Target Found at index 5!** |

* **Total Iterations**: $\lceil\log_2(10)\rceil = 3\text{ comparisons}$. Brute force would require 6 comparisons.

---

### Explainer A.6: Common Pseudocode Traps, Operator Precedence & Bitwise Math

#### 1. Operator Precedence Hierarchy (Highest to Lowest)
1. Parentheses: `()`
2. Exponentiation: `**` (Evaluates **right-to-left**: `2 ** 3 ** 2 == 2 ** 9 == 512`, NOT `8 ** 2 == 64`)
3. Unary Operators: `+x`, `-x`, `~x`
4. Multiplication, Division, Floor Div, Modulo: `*`, `/`, `//`, `%`
5. Addition, Subtraction: `+`, `-`
6. Bitwise Shifts: `<<`, `>>`
7. Bitwise AND: `&`
8. Bitwise XOR: `^`
9. Bitwise OR: `|`
10. Comparison Operators: `<`, `<=`, `>`, `>=`, `==`, `!=`, `is`, `in`
11. Boolean NOT: `not`
12. Boolean AND: `and`
13. Boolean OR: `or`

#### 2. Bitwise Logic & Fast Power-of-Two Invariant
* **Check if $N$ is a power of 2**:
  A positive integer $N$ is a power of 2 if and only if its binary representation contains exactly one `1` bit (e.g., $16 = 10000_2$).
  Subtracting 1 flips all bits up to the lowest set bit: $15 = 01111_2$.
  Therefore, bitwise AND produces identically zero:
  $$N > 0 \quad \text{and} \quad (N \ \& \ (N - 1)) == 0$$
* **Fast Multiplications and Divisions**:
  - $N \ll k \iff N \times 2^k$ (Bitwise Left Shift).
  - $N \gg k \iff \lfloor N / 2^k \rfloor$ (Bitwise Right Shift).

---

# SECTION B: Algorithmic Logic Curriculum & 20 Verifiable Code Problems

Python Algorithmic Logic Curriculum

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

---

# SECTION C: Additional Algorithmic Question Bank

Coding & Algorithmic Logic Questions

### Q1.1: Two-Sum Target Budget Optimization (`[PREPARATION INFERENCE]`)
* **Question**: Given an array of integers `costs` and an integer `budget`, return the indices of two distinct cloud services whose combined cost equals `budget`. What is the optimal time and space complexity?
* **Definition & Mechanics**: Brute-force checking all pairs requires $O(N^2)$ time. Using a hash map (dictionary), we store each encountered element and its index. As we iterate through the array, we check if the complement (`budget - cost`) already exists in the hash map.
* **Code Example**:
  ```python
  def two_sum_budget(costs: list[int], budget: int) -> tuple[int, int] | None:
      seen = {}
      for idx, cost in enumerate(costs):
          diff = budget - cost
          if diff in seen:
              return (seen[diff], idx)
          seen[cost] = idx
      return None

  assert two_sum_budget([150, 300, 450, 200, 700], 500) == (1, 3)
  ```
* **Complexity & Trade-offs**: Time: $O(N)$ linear scan; Space: $O(N)$ auxiliary memory for the hash map.
* **Limitations**: Hash map lookups degrade from $O(1)$ to $O(N)$ in the pathological event of catastrophic hash collisions (rare with Python's randomized hash seed).
* **Interviewer Follow-Up**: *"What if the input array is already sorted? How would you solve it with $O(1)$ space?"*  
  *Answer*: *"Use the two-pointer technique with pointers at `left = 0` and `right = N - 1`. If `costs[left] + costs[right] < budget`, increment `left`; if greater, decrement `right`. Converges in $O(N)$ time with zero extra memory."*

---

### Q1.2: Sliding Window Active Session Timeout (`[PREPARATION INFERENCE]`)
* **Question**: Given a binary event stream string `events` ('1' = user interaction, '0' = idle), find the length of the longest contiguous active window allowing at most one idle flip.
* **Definition & Mechanics**: A dynamic sliding window maintains an invariant: `zero_count <= 1`. Expand the `right` pointer to include elements; when `zero_count > 1`, contract the `left` pointer until the invariant is restored.
* **Code Example**:
  ```python
  def longest_active_window(events: str) -> int:
      left = zero_count = max_len = 0
      for right in range(len(events)):
          if events[right] == '0':
              zero_count += 1
          while zero_count > 1:
              if events[left] == '0':
                  zero_count -= 1
              left += 1
          max_len = max(max_len, right - left + 1)
      return max_len

  assert longest_active_window("110110111") == 6
  ```
* **Complexity**: Time: $O(N)$ (each element is visited at most twice); Space: $O(1)$.
* **Common Trap**: Assuming the first zero flip always yields the maximum. In `"110110111"`, flipping the second zero yields length 6, whereas flipping the first zero yields length 5.

---

### Q1.3: Second-Largest Distinct Value in an Array (`[PREPARATION INFERENCE]`)
* **Question**: Write an $O(N)$ single-pass algorithm to find the second-largest distinct integer in an unsorted list without sorting.
* **Code Example**:
  ```python
  def second_largest(nums: list[int]) -> int | None:
      first = second = None
      for x in nums:
          if first is None or x > first:
              second = first
              first = x
          elif x != first and (second is None or x > second):
              second = x
      return second

  assert second_largest([10, 20, 20, 5, 8]) == 10
  assert second_largest([5, 5, 5]) is None
  ```
* **Complexity**: Time: $O(N)$; Space: $O(1)$.
* **Edge Cases**: Handled: duplicate maximums (`[20, 20]`), all identical elements (`[5, 5, 5]` returns `None`), negative numbers (`[-10, -5, -20]` returns `-10`).
