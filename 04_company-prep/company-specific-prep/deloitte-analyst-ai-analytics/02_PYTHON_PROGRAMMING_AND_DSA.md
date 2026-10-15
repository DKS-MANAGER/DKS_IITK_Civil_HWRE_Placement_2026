# Module 02: Python Programming, Data Structures, and Algorithmic Problem Solving

> **Module Code**: DEL-M02  
> **Priority**: P1 (Core Foundation)  
> **Target Assessment**: Technical Screening & Live Coding / Whiteboard Problem Solving  
> **Standard**: Complete textbook explanations, Big-O analysis, runnable idiomatic Python, edge case handling, and solved coding tasks.

---

## 1. Python Language Foundations for Enterprise Analytics

### 1.1 Memory Model, Mutability, and References

In Python, **everything is an object**. Variables are not memory boxes that hold values; they are **names bound to object references** in memory.

* **Immutable Types**: `int`, `float`, `bool`, `str`, `tuple`, `frozenset`. When modified, a new object is allocated in memory.
* **Mutable Types**: `list`, `dict`, `set`, `bytearray`. Modifications mutate the object in place without changing its memory address (`id`).

```python
# Demonstrating Mutability & Reference Aliasing
def append_item(item, target_list=[]):  # ANTI-PATTERN: Mutable default argument!
    target_list.append(item)
    return target_list

print(append_item(1))  # [1]
print(append_item(2))  # [1, 2] -- The default list persists across calls!

# Correct Idiomatic Pattern:
def safe_append(item, target_list=None):
    if target_list is None:
        target_list = []
    target_list.append(item)
    return target_list
```

---

### 1.2 Time & Space Complexity (Big-O Fundamentals)

| Operation | List (`list`) | Hash Map (`dict`) | Hash Set (`set`) | Deque (`collections.deque`) |
| :--- | :---: | :---: | :---: | :---: |
| Append / Push | $O(1)$ amortized | $O(1)$ average | $O(1)$ average | $O(1)$ |
| Pop Right | $O(1)$ | $O(1)$ average | $O(1)$ average | $O(1)$ |
| Pop Left / Insert Left | $O(N)$ (requires shifting) | N/A | N/A | $O(1)$ |
| Lookup by Key/Value | $O(N)$ search | $O(1)$ average / $O(N)$ worst | $O(1)$ average / $O(N)$ worst | $O(N)$ |
| Delete Element | $O(N)$ | $O(1)$ average | $O(1)$ average | $O(N)$ |

---

## 2. Core Data Structures & Practical Implementations

### 2.1 Stacks & Queues

* **Stack**: Last-In-First-Out (LIFO). Supported natively via Python `list.append()` and `list.pop()`.
* **Queue**: First-In-First-Out (FIFO). Must use `collections.deque` (`append()`, `popleft()`). Never use `list.pop(0)` in production because it incurs an $O(N)$ memory copy per pop.

#### Worked Coding Problem 1: Valid Parentheses & Structural Parsing
**Problem**: An enterprise data payload contains nested grouping tokens `()`, `{}`, and `[]`. Given a string `s`, determine if the input string is valid (brackets must close in the correct order).

```python
def is_valid_parentheses(s: str) -> bool:
    """
    Time Complexity: O(N) where N is length of string s.
    Space Complexity: O(N) worst-case memory for stack.
    """
    matching_map = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for char in s:
        if char in matching_map:
            # Pop top element or use sentinel if stack is empty
            top_element = stack.pop() if stack else '#'
            if matching_map[char] != top_element:
                return False
        else:
            # Opening bracket: push to stack
            stack.append(char)
            
    # Valid only if stack is completely empty
    return len(stack) == 0

# Test Cases
print(is_valid_parentheses("()[]{}"))     # True
print(is_valid_parentheses("([{}])"))     # True
print(is_valid_parentheses("([)]"))       # False
print(is_valid_parentheses(""))           # True (boundary condition)
```

---

## 3. Algorithmic Problem-Solving Patterns

### 3.1 Two Pointers Pattern

* **Concept**: Maintain two array indices traversing towards each other or in the same direction to reduce time complexity from $O(N^2)$ to $O(N)$ on sorted or structured sequences.

#### Worked Coding Problem 2: Two Sum on Sorted Array
**Problem**: Given a 1-indexed sorted integer array `numbers` and a target sum `target`, find two numbers such that they add up to `target`. Return their 1-based indices.

```python
from typing import List

def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum
            
    return []

# Test
print(two_sum_sorted([2, 7, 11, 15], 9))  # [1, 2]
print(two_sum_sorted([1, 2, 3, 4, 6], 10)) # [4, 5]
```

---

### 3.2 Sliding Window Pattern

* **Concept**: Maintain a contiguous subarray window $[L, R]$ over a stream or sequence. Expand $R$ to satisfy a condition; shrink $L$ when the window violates constraints. Converts nested loops ($O(N^2)$) into linear $O(N)$ passes.

#### Worked Coding Problem 3: Longest Substring Without Repeating Characters
**Problem**: Given a string `s`, find the length of the longest substring without repeating characters.

```python
def length_of_longest_substring(s: str) -> int:
    """
    Time Complexity: O(N) single pass.
    Space Complexity: O(min(N, M)) where M is alphabet size.
    """
    char_index_map = {}
    max_length = 0
    left = 0
    
    for right, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= left:
            # Shrink window past the prior duplicate occurrence
            left = char_index_map[char] + 1
            
        char_index_map[char] = right
        current_len = right - left + 1
        if current_len > max_length:
            max_length = current_len
            
    return max_length

# Test
print(length_of_longest_substring("abcabcbb"))  # 3 ("abc")
print(length_of_longest_substring("bbbbb"))     # 1 ("b")
print(length_of_longest_substring("pwwkew"))    # 3 ("wke")
print(length_of_longest_substring(""))          # 0
```

---

### 3.3 Dynamic Programming (DP) Fundamentals

* **Core Principles**:
  1. **Optimal Substructure**: The optimal solution to the problem incorporates optimal solutions to subproblems.
  2. **Overlapping Subproblems**: The same subproblems are solved repeatedly in naive recursion.

#### Worked Coding Problem 4: Maximum Subarray Sum (Kadane's Algorithm)
**Problem**: Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

```python
def max_sub_array(nums: List[int]) -> int:
    """
    Time Complexity: O(N)
    Space Complexity: O(1)
    """
    if not nums:
        return 0
        
    current_sum = nums[0]
    global_max = nums[0]
    
    for x in nums[1:]:
        # Decide whether to extend the prior contiguous subarray or start fresh from x
        current_sum = max(x, current_sum + x)
        if current_sum > global_max:
            global_max = current_sum
            
    return global_max

# Test
print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6 (Subarray: [4, -1, 2, 1])
print(max_sub_array([-1, -2, -3]))                     # -1
```

---

## 4. Object-Oriented Programming (OOP) for Data Pipelines

Enterprise Python code requires modular class architectures with encapsulation and inheritance.

```python
from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseDataIngestor(ABC):
    """Abstract base pipeline component for data ingestion."""
    
    def __init__(self, source_name: str):
        self.source_name = source_name
        self._record_count = 0  # Protected member
        
    @abstractmethod
    def fetch_records(self) -> list:
        """Subclasses must implement actual retrieval logic."""
        pass
        
    def log_summary(self) -> Dict[str, Any]:
        return {"source": self.source_name, "records_processed": self._record_count}

class RestApiIngestor(BaseDataIngestor):
    def __init__(self, endpoint_url: str):
        super().__init__(source_name=f"REST:{endpoint_url}")
        self.endpoint_url = endpoint_url
        
    def fetch_records(self) -> list:
        # Simulated payload
        mock_data = [{"id": 101, "status": "active"}, {"id": 102, "status": "pending"}]
        self._record_count = len(mock_data)
        return mock_data

# Client verification
ingestor = RestApiIngestor("https://api.deloitte-client.internal/v1/telemetry")
data = ingestor.fetch_records()
print(ingestor.log_summary())  # {'source': 'REST:https://api...', 'records_processed': 2}
```

---

## 5. Self-Assessment Checklist

- [ ] Can explain Python object mutability and why mutable default arguments cause bugs.
- [ ] Understand why `collections.deque` is preferred over `list` for queue implementations.
- [ ] Can implement sliding window and two-pointer algorithms with optimal $O(N)$ runtime.
- [ ] Able to trace Kadane's algorithm and dynamic programming state transitions.
- [ ] Can write modular, encapsulated Python classes utilizing abstract base classes (`abc.ABC`).
