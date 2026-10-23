# Module 02: Python Programming, Data Structures, and Algorithmic Problem Solving

> **Module Code**: DEL-M02  
> **Priority**: P1 (Core Technical Foundation)  
> **Target Assessment**: HirePro Online Coding Assessment (2 Live Coding Tasks) & Technical Interview Live Problem Solving  
> **Coverage**: Python Internals, Memory Model, OOP, Core Data Structures, Algorithmic Patterns, 15 Solved Enterprise Coding Problems, Big-O Proofs, and Platform Test Harnesses.

---

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
