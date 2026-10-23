# Topic Master 02: Coding, Data Structures, Algorithms & Software Engineering Practice

> **Consolidated Module**: TOPIC-02 (Coding & Software Engineering)  
> **Target Assessment**: HirePro Online Coding Assessment (2 Live Tasks) & Technical Live Interview Problem Solving  
> **Structure**:
> - **SECTION A**: Python Language Internals, Memory Model, Big-O Complexity & OOP Architecture
> - **SECTION B**: 15 Master Solved Enterprise Coding Problems (Binary Search, Paint House DP, Sliding Window, Trapping Rain Water, etc.)
> - **SECTION C**: HirePro Vibe Coding & Interactive Software Engineering Tasks (3 Complete Simulated Tasks with Starter Bugs, Test Suites & Scoring Rubrics)
> - **SECTION D**: Technical Interview Live Coding Framework & Speed Strategies

---

# SECTION A & B: Python Foundations, Algorithmic Patterns & 15 Master Solved Problems

## 1. Python Language Internals & Engineering Foundations

### 1.1 Memory Model, Mutability, and Object References

In Python, **everything is an object**. A variable is not a memory box that stores a value; it is a **name bound to an object reference** in the Python runtime.

#### Mutable vs Immutable Types
* **Immutable Types**: `int`, `float`, `bool`, `str`, `tuple`, `frozenset`, `bytes`.
  - When an immutable object is modified, Python allocates a new object in memory and updates the variable reference.
  - They are hashable (if their constituent elements are hashable) and can serve as dictionary keys or set members.
* **Mutable Types**: `list`, `dict`, `set`, `bytearray`.
  - Can be mutated in-place without altering their memory identity (`id(obj)`).
  - Cannot be used as dictionary keys because in-place mutations would invalidate hash table buckets.

```python
# Demonstrating Identity vs Equality
a = [1, 2, 3]
b = a          # Reference copy: b references the exact same object as a
c = [1, 2, 3]  # Value equality: c references a distinct list object

print(a == b)  # True  (Value equality)
print(a is b)  # True  (Identity check: id(a) == id(b))
print(a == c)  # True  (Value equality)
print(a is c)  # False (Different heap allocations)

# The Dangerous Default Argument Trap
def append_event(event_id: int, log_buffer: list = []):  # ANTI-PATTERN!
    log_buffer.append(event_id)
    return log_buffer

print(append_event(101))  # [101]
print(append_event(102))  # [101, 102] -- The default list persists across function invocations!

# The Correct Idiomatic Pattern
def safe_append_event(event_id: int, log_buffer: list = None):
    if log_buffer is None:
        log_buffer = []
    log_buffer.append(event_id)
    return log_buffer
```

#### Shallow Copy vs Deep Copy
```python
import copy

original = [[1, 2, 3], [4, 5, 6]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][0] = 999
print(shallow[0][0])  # 999 (Inner nested lists share references)
print(deep[0][0])     # 1   (Completely independent clone recursively)
```

---

### 1.2 Time & Space Complexity Reference (Big-O Cheat Sheet)

| Data Structure | Access by Index | Search by Value | Insert (Beginning) | Insert (End) | Delete | Memory Overhead |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Python `list`** | $O(1)$ | $O(N)$ | $O(N)$ | $O(1)$ amortized | $O(N)$ | Low (contiguous dynamic array) |
| **Python `collections.deque`** | $O(N)$ | $O(N)$ | $O(1)$ | $O(1)$ | $O(1)$ at ends | Moderate (doubly linked blocks) |
| **Python `dict` (Hash Map)** | N/A | $O(1)$ avg / $O(N)$ worst | N/A | $O(1)$ avg / $O(N)$ worst | $O(1)$ avg | High (hash table with compact keys) |
| **Python `set` (Hash Set)** | N/A | $O(1)$ avg / $O(N)$ worst | N/A | $O(1)$ avg / $O(N)$ worst | $O(1)$ avg | High (sparse hash table) |
| **Python `heapq` (Binary Heap)**| $O(1)$ min element | $O(N)$ | N/A | $O(\log N)$ push | $O(\log N)$ pop | Low (stored in standard list) |

---

### 1.3 Comprehensions, Generators, and Lazy Evaluation

Enterprise data processing often deals with millions of records. Loading all data into memory at once triggers Out-Of-Memory (OOM) errors. Python generators evaluate lazily:

```python
from typing import Generator

# List comprehension: Computes immediately and occupies O(N) memory
eager_squares = [x**2 for x in range(1_000_000)]  # ~8 MB heap allocation

# Generator expression: Computes lazily on-demand with O(1) memory
lazy_squares = (x**2 for x in range(1_000_000))   # ~120 bytes memory

# Generator Function
def stream_sensor_readings(limit: int) -> Generator[float, None, None]:
    for i in range(limit):
        yield 25.0 + (i * 0.1)

stream = stream_sensor_readings(3)
print(next(stream))  # 25.0
print(next(stream))  # 25.1
print(next(stream))  # 25.2
```

---

### 1.4 Object-Oriented Programming (OOP) for Enterprise Analytics

Deloitte technical interviewers evaluate code organization, modularity, encapsulation, and interface design.

```python
from abc import ABC, abstractmethod
from typing import List, Dict, Any

class DataConnector(ABC):
    """Abstract base class establishing the contract for data ingestion."""
    
    def __init__(self, connection_string: str):
        self._connection_string = connection_string  # Protected attribute
        self.__is_connected = False                  # Private attribute (name-mangled)
        
    @property
    def is_connected(self) -> bool:
        return self.__is_connected
        
    def connect(self) -> None:
        # Simulate connection handshake
        self.__is_connected = True
        
    @abstractmethod
    def fetch_batch(self, limit: int) -> List[Dict[str, Any]]:
        """Subclasses must implement actual retrieval."""
        pass

class CloudSqlConnector(DataConnector):
    """Concrete implementation for enterprise relational databases."""
    
    def __init__(self, host: str, port: int, database: str):
        super().__init__(f"postgresql://{host}:{port}/{database}")
        self.database = database
        
    def fetch_batch(self, limit: int) -> List[Dict[str, Any]]:
        if not self.is_connected:
            raise ConnectionError("Database connection not established. Call connect() first.")
        # Return mock records
        return [{"record_id": i, "db": self.database} for i in range(limit)]

# Verification
db = CloudSqlConnector(host="db.deloitte.internal", port=5432, database="analytics_dw")
db.connect()
print(db.fetch_batch(2))  # [{'record_id': 0, 'db': 'analytics_dw'}, {'record_id': 1, 'db': 'analytics_dw'}]
```

---

## 2. Core Algorithmic Patterns & Techniques

When solving coding tasks on HirePro or live in technical interviews, recognize the underlying pattern immediately:

1. **Two Pointers**: Used when working with sorted arrays, finding pairs, or partitioning. Reduces $O(N^2)$ to $O(N)$.
2. **Sliding Window**: Used for contiguous subarray or substring problems with constraints (e.g., maximum sum of size $K$, longest substring with distinct characters).
3. **Prefix Sums & Frequency Maps**: Used for subarray sum queries, range accumulations, and anagram matching.
4. **Binary Search**: Used on sorted arrays, search spaces with monotonic properties, or optimization problems ("find minimum capacity that satisfies condition").
5. **Monotonic Stack**: Used for finding the "next greater element" or "largest rectangle in histogram".
6. **Dynamic Programming (DP)**: Used for problems exhibiting optimal substructure and overlapping subproblems (e.g., house coloring, knapsack, coin change).

---

## 3. 15 Master Solved Enterprise Coding Problems

Each problem below is presented with:
- Formal Problem Specification
- Conceptual Intuition & Mathematical Basis
- Full Runnable Python 3 Solution with Type Annotations
- Complexity Analysis (Time & Space)
- Comprehensive Test Assertions

---

### Problem 1: Valid Parentheses & Syntax Verification
* **Category**: Stacks & String Parsing  
* **Relevance**: Standard HirePro screening problem; syntax tree validation.

#### Problem Statement
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid. An input string is valid if open brackets are closed by the same type of brackets in the correct order, and every close bracket has a corresponding open bracket of the same type.

```python
def is_valid_parentheses(s: str) -> bool:
    """
    Time Complexity: O(N) where N is the length of string s.
    Space Complexity: O(N) worst-case auxiliary memory for the stack.
    """
    mapping = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for char in s:
        if char in mapping:
            # If closing bracket, pop matching opening bracket
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            # Opening bracket: push onto stack
            stack.append(char)
            
    # Valid only if stack is completely balanced and empty
    return len(stack) == 0

# Verification Suite
assert is_valid_parentheses("()") == True
assert is_valid_parentheses("()[]{}") == True
assert is_valid_parentheses("(]") == False
assert is_valid_parentheses("([)]") == False
assert is_valid_parentheses("{[]}") == True
assert is_valid_parentheses("") == True
print("Problem 1 Verified.")
```

---

### Problem 2: Two Sum — Hash Map vs Two Pointers
* **Category**: Arrays, Hash Map & Two Pointers  
* **Relevance**: Core screening test question.

#### Problem Statement
Given an integer array `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`. You may assume that each input has exactly one solution, and you may not use the same element twice.

```python
from typing import List

def two_sum_hash_map(nums: List[int], target: int) -> List[int]:
    """
    Optimal for Unsorted Arrays.
    Time Complexity: O(N) single-pass.
    Space Complexity: O(N) hash map memory.
    """
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i
    return []

def two_sum_sorted_two_pointers(nums: List[int], target: int) -> List[int]:
    """
    Optimal for Sorted Arrays (1-based indices).
    Time Complexity: O(N).
    Space Complexity: O(1) auxiliary space.
    """
    left = 0
    right = len(nums) - 1
    
    while left < right:
        curr = nums[left] + nums[right]
        if curr == target:
            return [left + 1, right + 1]
        elif curr < target:
            left += 1
        else:
            right -= 1
    return []

# Verification Suite
assert two_sum_hash_map([2, 7, 11, 15], 9) == [0, 1]
assert two_sum_hash_map([3, 2, 4], 6) == [1, 2]
assert two_sum_sorted_two_pointers([2, 7, 11, 15], 9) == [1, 2]
print("Problem 2 Verified.")
```

---

### Problem 3: Longest Substring Without Repeating Characters
* **Category**: Sliding Window & Hash Map  
* **Relevance**: Classic interview problem testing pointer bounds.

#### Problem Statement
Given a string `s`, find the length of the longest substring without duplicate characters.

```python
def length_of_longest_substring(s: str) -> int:
    """
    Time Complexity: O(N) where N is the length of string s.
    Space Complexity: O(min(N, M)) where M is the charset size.
    """
    char_map = {}
    max_len = 0
    left = 0
    
    for right, char in enumerate(s):
        if char in char_map and char_map[char] >= left:
            # Advance left pointer past previous duplicate occurrence
            left = char_map[char] + 1
            
        char_map[char] = right
        max_len = max(max_len, right - left + 1)
        
    return max_len

# Verification Suite
assert length_of_longest_substring("abcabcbb") == 3
assert length_of_longest_substring("bbbbb") == 1
assert length_of_longest_substring("pwwkew") == 3
assert length_of_longest_substring("") == 0
assert length_of_longest_substring(" ") == 1
print("Problem 3 Verified.")
```

---

### Problem 4: Maximum Subarray Sum (Kadane's Algorithm)
* **Category**: Dynamic Programming / Greedy  
* **Relevance**: Essential array algorithm frequently asked in preliminary tests.

#### Problem Statement
Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

```python
def max_sub_array(nums: List[int]) -> int:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    if not nums:
        return 0
        
    current_max = nums[0]
    global_max = nums[0]
    
    for x in nums[1:]:
        current_max = max(x, current_max + x)
        global_max = max(global_max, current_max)
        
    return global_max

# Verification Suite
assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6  # [4, -1, 2, 1]
assert max_sub_array([1]) == 1
assert max_sub_array([5, 4, -1, 7, 8]) == 23
assert max_sub_array([-5, -2, -9]) == -2
print("Problem 4 Verified.")
```

---

### Problem 5: Search in Rotated Sorted Array (Binary Search)
* **Category**: Modified Binary Search  
* **Relevance**: **Explicitly asked in Ayush Kumar's Deloitte USI technical interview**.

#### Problem Statement
There is an integer array `nums` sorted in ascending order (with distinct values). Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k`. Given the rotated array `nums` and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`. You must write an algorithm with $O(\log N)$ runtime complexity.

```python
def search_rotated_sorted_array(nums: List[int], target: int) -> int:
    """
    Time Complexity: O(log N)
    Space Complexity: O(1)
    """
    if not nums:
        return -1
        
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
            
        # Determine which half of the array is normally sorted
        if nums[left] <= nums[mid]:
            # Left half is monotonically sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is monotonically sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
                
    return -1

# Verification Suite
assert search_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert search_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert search_rotated_sorted_array([1], 0) == -1
assert search_rotated_sorted_array([1, 3], 3) == 1
print("Problem 5 Verified.")
```

---

### Problem 6: Paint House / Minimum Cost to Paint Houses
* **Category**: Dynamic Programming  
* **Relevance**: **Explicitly asked in Ayush Kumar's Deloitte USI technical interview**.

#### Problem Statement
There are $N$ houses in a row. Each house can be painted in one of three colors: Red, Blue, or Green. The cost of painting each house with a certain color is represented by an $N \times 3$ cost matrix `costs` where `costs[i][0]`, `costs[i][1]`, and `costs[i][2]` are the costs of painting house $i$ with Red, Blue, and Green respectively. No two adjacent houses may have the same color. Return the minimum total cost to paint all houses.

#### Mathematical Recurrence
For house $i$ from 1 to $N-1$:
$$DP[i][0] = \text{costs}[i][0] + \min(DP[i-1][1], DP[i-1][2])$$
$$DP[i][1] = \text{costs}[i][1] + \min(DP[i-1][0], DP[i-1][2])$$
$$DP[i][2] = \text{costs}[i][2] + \min(DP[i-1][0], DP[i-1][1])$$

```python
def min_cost_paint_houses(costs: List[List[int]]) -> int:
    """
    Time Complexity: O(N) where N is number of houses.
    Space Complexity: O(1) auxiliary space by mutating running state.
    """
    if not costs:
        return 0
        
    # Maintain running minimum costs for the previous house painted in [R, B, G]
    prev_r, prev_b, prev_g = costs[0][0], costs[0][1], costs[0][2]
    
    for i in range(1, len(costs)):
        curr_r = costs[i][0] + min(prev_b, prev_g)
        curr_b = costs[i][1] + min(prev_r, prev_g)
        curr_g = costs[i][2] + min(prev_r, prev_b)
        
        prev_r, prev_b, prev_g = curr_r, curr_b, curr_g
        
    return min(prev_r, prev_b, prev_g)

# Verification Suite
assert min_cost_paint_houses([[17, 2, 17], [16, 16, 5], [14, 3, 19]]) == 10
# House 0: Blue (2) + House 1: Green (5) + House 2: Blue (3) = 10
assert min_cost_paint_houses([[7, 6, 2]]) == 2
assert min_cost_paint_houses([]) == 0
print("Problem 6 Verified.")
```

---

### Problem 7: Merge Intervals & Time Slot Consolidation
* **Category**: Sorting & Greedy Interval Processing  
* **Relevance**: Standard consulting scheduling and data reconciliation problem.

#### Problem Statement
Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

```python
def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Time Complexity: O(N log N) dominated by sorting.
    Space Complexity: O(N) to store merged intervals.
    """
    if not intervals:
        return []
        
    # Sort intervals by starting time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for curr in intervals[1:]:
        prev = merged[-1]
        if curr[0] <= prev[1]:
            # Overlap exists: extend previous interval's end boundary
            prev[1] = max(prev[1], curr[1])
        else:
            # Disjoint interval: append to results
            merged.append(curr)
            
    return merged

# Verification Suite
assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
assert merge_intervals([[6, 8], [1, 9], [2, 4]]) == [[1, 9]]
print("Problem 7 Verified.")
```

---

### Problem 8: Product of Array Except Self
* **Category**: Prefix & Suffix Accumulation  
* **Relevance**: Common screening question requiring $O(1)$ extra memory without using division.

#### Problem Statement
Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. You must write an algorithm that runs in $O(N)$ time and without using the division operator.

```python
def product_except_self(nums: List[int]) -> List[int]:
    """
    Time Complexity: O(N) two linear passes.
    Space Complexity: O(1) auxiliary space (excluding output array).
    """
    n = len(nums)
    res = [1] * n
    
    # Pass 1: Accumulate prefix products
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
        
    # Pass 2: Accumulate suffix products backwards
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
        
    return res

# Verification Suite
assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
print("Problem 8 Verified.")
```

---

### Problem 9: Group Anagrams
* **Category**: Hash Maps & String Canonicalization  
* **Relevance**: Tests hashing keys and string normalization.

#### Problem Statement
Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

```python
from collections import defaultdict

def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Time Complexity: O(N * K log K) where N is number of strings, K is maximum string length.
    Space Complexity: O(N * K) to store hash table keys and groupings.
    """
    anagram_map = defaultdict(list)
    
    for s in strs:
        # Canonical key: tuple of character counts or sorted characters
        key = tuple(sorted(s))
        anagram_map[key].append(s)
        
    return list(anagram_map.values())

# Verification Suite
res = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
res_sorted = sorted([sorted(group) for group in res])
expected = sorted([sorted(["bat"]), sorted(["nat", "tan"]), sorted(["ate", "eat", "tea"])])
assert res_sorted == expected
print("Problem 9 Verified.")
```

---

### Problem 10: Trapping Rain Water
* **Category**: Two Pointers / Monotonic Geometry  
* **Relevance**: Demonstrates physical elevation and fluid accumulation logic (excellent HWRE transferability).

#### Problem Statement
Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

```python
def trap_rain_water(height: List[int]) -> int:
    """
    Time Complexity: O(N) single-pass.
    Space Complexity: O(1) auxiliary memory.
    """
    if not height or len(height) < 3:
        return 0
        
    left = 0
    right = len(height) - 1
    left_max = 0
    right_max = 0
    trapped_water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                trapped_water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                trapped_water += right_max - height[right]
            right -= 1
            
    return trapped_water

# Verification Suite
assert trap_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert trap_rain_water([4, 2, 0, 3, 2, 5]) == 9
assert trap_rain_water([]) == 0
print("Problem 10 Verified.")
```

---

### Problem 11: Reverse a Singly Linked List
* **Category**: Linked List Pointer Manipulation  
* **Relevance**: Standard pointer manipulation test.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head: ListNode) -> ListNode:
    """
    Time Complexity: O(N)
    Space Complexity: O(1) iterative in-place pointer reversal.
    """
    prev = None
    curr = head
    
    while curr:
        next_node = curr.next  # Cache next node
        curr.next = prev       # Reverse pointer
        prev = curr            # Advance prev
        curr = next_node       # Advance curr
        
    return prev

# Helper to verify
def list_to_array(head: ListNode) -> list:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

# Test
n3 = ListNode(3)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
rev_head = reverse_linked_list(n1)
assert list_to_array(rev_head) == [3, 2, 1]
print("Problem 11 Verified.")
```

---

### Problem 12: Detect Cycle in a Linked List (Floyd's Tortoise & Hare)
* **Category**: Fast & Slow Pointers  
* **Relevance**: Classic interview question on cycle detection.

```python
def has_cycle(head: ListNode) -> bool:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    if not head or not head.next:
        return False
        
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
            
    return False

# Test
c1 = ListNode(10)
c2 = ListNode(20)
c3 = ListNode(30)
c1.next = c2
c2.next = c3
c3.next = c2  # Cycle between 2 and 3
assert has_cycle(c1) == True
c3.next = None
assert has_cycle(c1) == False
print("Problem 12 Verified.")
```

---

### Problem 13: Lowest Common Ancestor in a Binary Search Tree (BST)
* **Category**: Binary Search Trees  
* **Relevance**: Recursion and BST property utilization.

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor_bst(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Time Complexity: O(H) where H is tree height.
    Space Complexity: O(1) iterative.
    """
    curr = root
    while curr:
        if p.val < curr.val and q.val < curr.val:
            curr = curr.left
        elif p.val > curr.val and q.val > curr.val:
            curr = curr.right
        else:
            return curr
    return None

# Test
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
lca = lowest_common_ancestor_bst(root, root.left.left, root.left.right)
assert lca.val == 2
print("Problem 13 Verified.")
```

---

### Problem 14: Top K Frequent Elements
* **Category**: Heaps & Hash Map  
* **Relevance**: Analytics ranking and frequency aggregation.

```python
import heapq
from collections import Counter

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Time Complexity: O(N log K) using min-heap of size K.
    Space Complexity: O(N) to store frequencies.
    """
    if k == len(nums):
        return nums
        
    counts = Counter(nums)
    # Min-heap based on frequency: (frequency, number)
    return heapq.nlargest(k, counts.keys(), key=counts.get)

# Test
assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
assert top_k_frequent([1], 1) == [1]
print("Problem 14 Verified.")
```

---

### Problem 15: Longest Increasing Subsequence (LIS)
* **Category**: Dynamic Programming & Binary Search  
* **Relevance**: Classic DP problem testing state formulation.

```python
import bisect

def length_of_lis(nums: List[int]) -> int:
    """
    Time Complexity: O(N log N) using patience sorting / binary search.
    Space Complexity: O(N) tails array.
    """
    tails = []
    for x in nums:
        idx = bisect.bisect_left(tails, x)
        if idx == len(tails):
            tails.append(x)
        else:
            tails[idx] = x
            
    return len(tails)

# Test
assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4  # [2, 3, 7, 101]
assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4
assert length_of_lis([7, 7, 7, 7]) == 1
print("Problem 15 Verified.")
```

---

## 4. HirePro Platform Fast I/O & Execution Template

HirePro runs automated test suites that pass input via standard input (`sys.stdin`) and check standard output (`sys.stdout`). Always structure your code to handle large streaming inputs cleanly:

```python
import sys

def solve():
    # Read all tokens from standard input efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    # Example: First token is N, followed by N integers
    n = int(input_data[0])
    nums = [int(x) for x in input_data[1:n+1]]
    
    # Process problem logic
    # result = compute(nums)
    # sys.stdout.write(str(result) + "\n")

if __name__ == "__main__":
    solve()
```

---

## 5. Technical Interview Live Problem Solving Framework

When an interviewer at Deloitte USI presents a technical coding problem:

1. **Clarify Inputs & Edge Cases (First 2 Minutes)**:
   - "Can the array be empty or contain negative numbers?"
   - "Are values bounded? What is the maximum $N$?"
   - "Can duplicate elements exist?"
2. **State the Brute-Force Baseline (1 Minute)**:
   - "The naive approach would be nested loops taking $O(N^2)$ time and $O(1)$ space."
3. **Propose the Optimal Solution & Big-O (2 Minutes)**:
   - "We can optimize this to $O(N)$ time by using a sliding window with a hash map to track indices."
4. **Write Clean, Idiomatic Code with Clear Variable Names (5-8 Minutes)**:
   - Use meaningful names (`left`, `right`, `char_frequency`, `max_profit`).
   - Add docstrings or quick inline comments.
5. **Dry Run on an Example & Test Edge Cases (2 Minutes)**:
   - Trace through a small array like `[2, 1, 4]`.
   - Explicitly mention edge cases: empty input, all identical elements, sorted descending.


---

# SECTION C: HirePro Vibe Coding & Interactive Software Engineering

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
