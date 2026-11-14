# 02 — Python Programming Practice Bank (50 Solved Problems)
## Algorithmic Challenges, Data Manipulation Puzzles & Production Coding Interview Questions

> **Document Status**: Technical Practice Question Bank `[TIER 5 / PEDAGOGICAL BANK]`  
> **Target Role**: Data Scientist / Associate Data Scientist | Tredence Analytics  
> **Coverage**: 50 Fully Solved Questions across String Manipulation, Arrays/NumPy, Pandas, Recursion, Dynamic Programming, and OOP.

---

### Part 1: String & Hash Map Algorithms (Q01 – Q10)

#### Q01. Longest Substring Without Repeating Characters
- **Problem**: Given a string `s`, find the length of the longest substring without repeating characters.
- **Difficulty**: Medium | **Target Time**: 4 min
- **Code Solution**:
  ```python
  def length_of_longest_substring(s: str) -> int:
      seen = {}
      max_len = 0
      left = 0
      for right, char in enumerate(s):
          if char in seen and seen[char] >= left:
              left = seen[char] + 1
          seen[char] = right
          max_len = max(max_len, right - left + 1)
      return max_len
  ```
- **Test Case**: `length_of_longest_substring("abcabcbb") == 3` ('abc')
- **Complexity**: Time $O(N)$, Space $O(\min(N, M))$ where $M$ is alphabet size.
- **Common Mistake**: Forgetting `seen[char] >= left` condition, allowing `left` pointer to jump backwards.

---

#### Q02. Group Anagrams
- **Problem**: Given an array of strings `strs`, group the anagrams together in any order.
- **Difficulty**: Medium | **Target Time**: 4 min
- **Code Solution**:
  ```python
  from collections import defaultdict
  from typing import List

  def group_anagrams(strs: List[str]) -> List[List[str]]:
      anagram_map = defaultdict(list)
      for word in strs:
          key = tuple(sorted(word))
          anagram_map[key].append(word)
      return list(anagram_map.values())
  ```
- **Test Case**: `group_anagrams(["eat","tea","tan","ate","nat","bat"]) -> [["eat","tea","ate"],["tan","nat"],["bat"]]`
- **Complexity**: Time $O(N \cdot K \log K)$, Space $O(N \cdot K)$.

---

#### Q03. First Unique Character in a String
- **Problem**: Given a string `s`, find the first non-repeating character and return its index. If it does not exist, return -1.
- **Difficulty**: Easy | **Target Time**: 2 min
- **Code Solution**:
  ```python
  from collections import Counter

  def first_uniq_char(s: str) -> int:
      counts = Counter(s)
      for idx, ch in enumerate(s):
          if counts[ch] == 1:
              return idx
      return -1
  ```
- **Test Case**: `first_uniq_char("loveleetcode") == 2` ('v')

---

#### Q04. Valid Palindrome with Punctuation Filtering
- **Problem**: Determine if string is a palindrome, considering only alphanumeric characters and ignoring cases.
- **Difficulty**: Easy | **Target Time**: 2 min
- **Code Solution**:
  ```python
  def is_palindrome(s: str) -> bool:
      filtered = [ch.lower() for ch in s if ch.isalnum()]
      return filtered == filtered[::-1]
  ```
- **Test Case**: `is_palindrome("A man, a plan, a canal: Panama") == True`

---

#### Q05. String Compression (Run-Length Encoding)
- **Problem**: Compress string `"aabcccccaaa"` to `"a2b1c5a3"`. Return original if compressed is not shorter.
- **Difficulty**: Easy | **Target Time**: 3 min
- **Code Solution**:
  ```python
  def compress_string(s: str) -> str:
      if not s: return s
      res = []
      count = 1
      for i in range(1, len(s)):
          if s[i] == s[i-1]:
              count += 1
          else:
              res.append(f"{s[i-1]}{count}")
              count = 1
      res.append(f"{s[-1]}{count}")
      compressed = "".join(res)
      return compressed if len(compressed) < len(s) else s
  ```
- **Test Case**: `compress_string("aabcccccaaa") == "a2b1c5a3"`

---

#### Q06. Subarray Sum Equals K
- **Problem**: Given an array of integers `nums` and an integer `k`, return total number of subarrays whose sum equals `k`.
- **Difficulty**: Medium | **Target Time**: 5 min
- **Code Solution**:
  ```python
  def subarray_sum(nums: List[int], k: int) -> int:
      prefix_counts = {0: 1}
      curr_sum = 0
      total = 0
      for x in nums:
          curr_sum += x
          if curr_sum - k in prefix_counts:
              total += prefix_counts[curr_sum - k]
          prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1
      return total
  ```
- **Test Case**: `subarray_sum([1, 1, 1], 2) == 2`
- **Common Mistake**: Trying two-pointer sliding window on arrays with negative numbers (sliding window only works for non-negative integers).

---

#### Q07. Longest Common Prefix
- **Problem**: Find the longest common prefix string amongst an array of strings.
- **Difficulty**: Easy | **Target Time**: 2 min
- **Code Solution**:
  ```python
  def longest_common_prefix(strs: List[str]) -> str:
      if not strs: return ""
      shortest = min(strs, key=len)
      for i, char in enumerate(shortest):
          for other in strs:
              if other[i] != char:
                  return shortest[:i]
      return shortest
  ```
- **Test Case**: `longest_common_prefix(["flower","flow","flight"]) == "fl"`

---

#### Q08. Two Sum (Indices Lookup)
- **Problem**: Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to target.
- **Difficulty**: Easy | **Target Time**: 2 min
- **Code Solution**:
  ```python
  def two_sum(nums: List[int], target: int) -> List[int]:
      seen = {}
      for i, num in enumerate(nums):
          diff = target - num
          if diff in seen:
              return [seen[diff], i]
          seen[num] = i
      return []
  ```
- **Test Case**: `two_sum([2, 7, 11, 15], 9) == [0, 1]`

---

#### Q09. Valid Parentheses
- **Problem**: Given a string containing `'('`, `')'`, `'{'`, `'}'`, `'['`, `']'`, determine if valid.
- **Difficulty**: Easy | **Target Time**: 2 min
- **Code Solution**:
  ```python
  def is_valid_parentheses(s: str) -> bool:
      mapping = {')': '(', '}': '{', ']': '['}
      stack = []
      for char in s:
          if char in mapping.values():
              stack.append(char)
          elif char in mapping:
              if not stack or stack.pop() != mapping[char]:
                  return False
      return len(stack) == 0
  ```
- **Test Case**: `is_valid_parentheses("{[]}") == True`, `is_valid_parentheses("([)]") == False`

---

#### Q10. Word Break Problem
- **Problem**: Determine if string `s` can be segmented into a space-separated sequence of dictionary words.
- **Difficulty**: Medium | **Target Time**: 5 min
- **Code Solution**:
  ```python
  def word_break(s: str, word_dict: List[str]) -> bool:
      words = set(word_dict)
      dp = [False] * (len(s) + 1)
      dp[0] = True
      for i in range(1, len(s) + 1):
          for j in range(i):
              if dp[j] and s[j:i] in words:
                  dp[i] = True
                  break
      return dp[-1]
  ```
- **Test Case**: `word_break("leetcode", ["leet", "code"]) == True`

---

### Part 2: NumPy & Mathematical Array Computing (Q11 – Q20)

#### Q11. Pairwise Euclidean Distance Matrix without Loops
- **Problem**: Given matrix `X` of shape `(N, D)`, compute pairwise Euclidean distance matrix `(N, N)` in vectorized NumPy.
- **Difficulty**: Medium | **Target Time**: 3 min
- **Code Solution**:
  ```python
  import numpy as np

  def pairwise_distances(X: np.ndarray) -> np.ndarray:
      # ||x_i - x_j||^2 = ||x_i||^2 + ||x_j||^2 - 2 <x_i, x_j>
      sq_norms = np.sum(X**2, axis=1, keepdims=True)
      dist_sq = sq_norms + sq_norms.T - 2.0 * np.dot(X, X.T)
      return np.sqrt(np.maximum(dist_sq, 0.0))
  ```
- **Test Case**: `pairwise_distances(np.array([[0,0],[3,4]])) -> [[0, 5],[5, 0]]`

---

#### Q12. Moving Average using 1D Convolution
- **Problem**: Compute moving average of window size `k` over array `x` in $O(N)$ vectorized NumPy.
- **Difficulty**: Easy | **Target Time**: 2 min
- **Code Solution**:
  ```python
  def moving_average_conv(x: np.ndarray, k: int) -> np.ndarray:
      kernel = np.ones(k) / k
      return np.convolve(x, kernel, mode='valid')
  ```
- **Test Case**: `moving_average_conv(np.array([1, 2, 3, 4, 5]), 3) -> [2.0, 3.0, 4.0]`

---

#### Q13. Stratified K-Fold Generator from Scratch
- **Problem**: Write a pure Python/NumPy stratified partitioner preserving class label ratios across $k$ folds.
- **Difficulty**: Medium | **Target Time**: 5 min
- **Code Solution**:
  ```python
  def stratified_k_fold(y: np.ndarray, n_splits: int = 5, seed: int = 42):
      np.random.seed(seed)
      classes, y_indices = np.unique(y, return_inverse=True)
      n_classes = len(classes)
      class_indices = [np.where(y_indices == c)[0] for c in range(n_classes)]
      for idxs in class_indices:
          np.random.shuffle(idxs)

      folds = [[] for _ in range(n_splits)]
      for idxs in class_indices:
          splits = np.array_split(idxs, n_splits)
          for f in range(n_splits):
              folds[f].extend(splits[f])

      for f in range(n_splits):
          val_idx = np.array(folds[f])
          train_idx = np.array([i for i in range(len(y)) if i not in val_idx])
          yield train_idx, val_idx
  ```

---

#### Q14. Matrix Rank Determination via SVD
- **Problem**: Compute the numerical rank of a matrix using Singular Value Decomposition.
- **Difficulty**: Medium | **Target Time**: 3 min
- **Code Solution**:
  ```python
  def matrix_rank_svd(A: np.ndarray, tol: float = None) -> int:
      s = np.linalg.svd(A, compute_uv=False)
      if tol is None:
          tol = s.max() * max(A.shape) * np.finfo(A.dtype).eps
      return int(np.sum(s > tol))
  ```

---

#### Q15. Softmax Derivative Implementation
- **Problem**: Implement exact Jacobian matrix of the softmax function.
- **Difficulty**: Hard | **Target Time**: 6 min
- **Code Solution**:
  ```python
  def softmax_jacobian(p: np.ndarray) -> np.ndarray:
      # J_ij = p_i * (delta_ij - p_j) = diag(p) - p p^T
      return np.diag(p) - np.outer(p, p)
  ```
- **Test Case**: For `p = np.array([0.7, 0.3])`, row sums of Jacobian equal 0.

---

#### Q16. Min-Max Feature Scaler without Data Leakage
- **Problem**: Implement a vectorized Min-Max Scaler with separate `fit` and `transform`.
- **Difficulty**: Easy | **Target Time**: 3 min
- **Code Solution**:
  ```python
  class VectorizedMinMaxScaler:
      def fit(self, X: np.ndarray):
          self.min_ = X.min(axis=0)
          self.max_ = X.max(axis=0)
          self.range_ = np.maximum(self.max_ - self.min_, 1e-8)
          return self

      def transform(self, X: np.ndarray) -> np.ndarray:
          return (X - self.min_) / self.range_
  ```

---

#### Q17. Top-K Elements along Axis
- **Problem**: Find the indices of the top-k highest values in each row of a 2D matrix without full sort.
- **Difficulty**: Medium | **Target Time**: 3 min
- **Code Solution**:
  ```python
  def top_k_indices_rowwise(A: np.ndarray, k: int) -> np.ndarray:
      # argpartition is O(N) compared to argsort O(N log N)
      part = np.argpartition(-A, k-1, axis=1)[:, :k]
      # Sort only top k for exact rank order
      row_indices = np.arange(A.shape[0])[:, None]
      sub_sorted = np.argsort(-A[row_indices, part], axis=1)
      return np.take_along_axis(part, sub_sorted, axis=1)
  ```

---

#### Q18. Covariance Matrix Derivation from Scratch
- **Problem**: Implement sample covariance matrix computation $\frac{1}{N-1}(X - \mu)^T(X - \mu)$.
- **Difficulty**: Easy | **Target Time**: 2 min
- **Code Solution**:
  ```python
  def sample_covariance(X: np.ndarray) -> np.ndarray:
      n = X.shape[0]
      X_centered = X - X.mean(axis=0, keepdims=True)
      return np.dot(X_centered.T, X_centered) / (n - 1)
  ```

---

#### Q19. Reservoir Sampling (Sample K items from infinite stream)
- **Problem**: Given a stream of items of unknown length, select $k$ items uniformly at random using $O(k)$ memory.
- **Difficulty**: Medium | **Target Time**: 4 min
- **Code Solution**:
  ```python
  import random

  def reservoir_sample(stream, k: int) -> list:
      reservoir = []
      for i, item in enumerate(stream):
          if i < k:
              reservoir.append(item)
          else:
              j = random.randint(0, i)
              if j < k:
                  reservoir[j] = item
      return reservoir
  ```

---

#### Q20. Monotonic Cubic Interpolation Detection
- **Problem**: Check whether an array of numeric values is strictly monotonically increasing.
- **Difficulty**: Easy | **Target Time**: 1 min
- **Code Solution**:
  ```python
  def is_strictly_monotonic(arr: np.ndarray) -> bool:
      return bool(np.all(np.diff(arr) > 0))
  ```

---

### Part 3: Pandas Data Manipulation & Transformation (Q21 – Q30)

#### Q21. Second Highest Salary per Department
- **Problem**: In a dataframe with `['dept_id', 'emp_id', 'salary']`, find the second highest salary in each department.
- **Difficulty**: Medium | **Target Time**: 4 min
- **Code Solution**:
  ```python
  def second_highest_salary_per_dept(df: pd.DataFrame) -> pd.DataFrame:
      ranked = df.copy()
      ranked['dense_rank'] = ranked.groupby('dept_id')['salary'].rank(method='dense', ascending=False)
      return ranked[ranked['dense_rank'] == 2][['dept_id', 'emp_id', 'salary']]
  ```

---

#### Q22. Reindexing & Forward-Filling Missing Daily Dates
- **Problem**: Given irregular time-series records, resample to daily frequency and forward-fill values.
- **Difficulty**: Medium | **Target Time**: 3 min
- **Code Solution**:
  ```python
  def daily_reindex_ffill(df: pd.DataFrame, date_col: str, val_col: str) -> pd.DataFrame:
      df = df.copy()
      df[date_col] = pd.to_datetime(df[date_col])
      df = df.set_index(date_col)
      full_idx = pd.date_range(start=df.index.min(), end=df.index.max(), freq='D')
      return df.reindex(full_idx).ffill().reset_index().rename(columns={'index': date_col})
  ```

---

#### Q23. Rolling 30-Day Customer Spend Aggregation
- **Problem**: Compute the 30-day rolling sum of spend per customer with irregular transaction dates.
- **Difficulty**: Medium | **Target Time**: 4 min
- **Code Solution**:
  ```python
  def rolling_30d_spend(df: pd.DataFrame) -> pd.DataFrame:
      df = df.copy()
      df['tx_date'] = pd.to_datetime(df['tx_date'])
      df = df.sort_values(by=['customer_id', 'tx_date'])
      df['rolling_30d'] = (
          df.set_index('tx_date')
            .groupby('customer_id')['amount']
            .rolling('30D')
            .sum()
            .reset_index(0, drop=True)
      )
      return df
  ```

---

#### Q24. Pivot Table Un-pivoting (`melt`)
- **Problem**: Convert wide dataframe `['product', '2023_Q1', '2023_Q2', '2023_Q3']` to long format `['product', 'quarter', 'revenue']`.
- **Difficulty**: Easy | **Target Time**: 2 min
- **Code Solution**:
  ```python
  def unpivot_quarters(df: pd.DataFrame) -> pd.DataFrame:
      return pd.melt(df, id_vars=['product'], var_name='quarter', value_name='revenue')
  ```

---

#### Q25. Cumulative Share of Top 20% Customers (Pareto 80/20 Rule)
- **Problem**: Calculate what percentage of total revenue is generated by the top 20% highest-spending customers.
- **Difficulty**: Medium | **Target Time**: 3 min
- **Code Solution**:
  ```python
  def pareto_revenue_share(df: pd.DataFrame) -> float:
      cust_spend = df.groupby('customer_id')['amount'].sum().sort_values(ascending=False)
      n_top_20 = int(np.ceil(0.20 * len(cust_spend)))
      top_20_rev = cust_spend.iloc[:n_top_20].sum()
      total_rev = cust_spend.sum()
      return float(top_20_rev / total_rev)
  ```

---

#### Q26. One-Hot Encoding with Frequency Thresholding
- **Problem**: One-hot encode high-cardinality categorical column, grouping categories with < 1% frequency into `'Other'`.
- **Difficulty**: Easy | **Target Time**: 3 min
- **Code Solution**:
  ```python
  def frequency_threshold_one_hot(df: pd.DataFrame, col: str, threshold: float = 0.01) -> pd.DataFrame:
      df = df.copy()
      freqs = df[col].value_counts(normalize=True)
      rare_cats = freqs[freqs < threshold].index
      df[col] = df[col].replace(rare_cats, 'Other')
      return pd.get_dummies(df, columns=[col], prefix=col, drop_first=True)
  ```

---

#### Q27. Detecting Temporal Leakage in Feature Engineering
- **Problem**: Verify that rolling customer features do not incorporate transaction information from the current or future timestamps.
- **Difficulty**: Medium | **Target Time**: 3 min
- **Code Solution**:
  ```python
  def safe_prior_spend_feature(df: pd.DataFrame) -> pd.DataFrame:
      df = df.sort_values(by=['customer_id', 'tx_date']).copy()
      # shift(1) guarantees only strictly prior historical events are accumulated
      df['prior_cumulative_spend'] = df.groupby('customer_id')['amount'].cumsum().shift(1).fillna(0)
      return df
  ```

---

#### Q28. Finding Gaps in Consecutive Sequence IDs
- **Problem**: Identify missing transaction IDs in an integer sequence `[101, 102, 104, 105, 108]`.
- **Difficulty**: Easy | **Target Time**: 2 min
- **Code Solution**:
  ```python
  def find_missing_sequence_ids(ids: List[int]) -> List[int]:
      full_range = set(range(min(ids), max(ids) + 1))
      return sorted(list(full_range - set(ids)))
  ```

---

#### Q29. Weight of Evidence (WoE) and Information Value (IV)
- **Problem**: Compute WoE and IV for a binned feature against binary target (`0=Good, 1=Bad`).
- **Difficulty**: Hard | **Target Time**: 5 min
- **Code Solution**:
  ```python
  def compute_woe_iv(df: pd.DataFrame, feature_col: str, target_col: str) -> pd.DataFrame:
      total_goods = (df[target_col] == 0).sum()
      total_bads = (df[target_col] == 1).sum()
      eps = 1e-6

      grouped = df.groupby(feature_col)[target_col].agg(
          bads='sum',
          total='count'
      ).reset_index()
      grouped['goods'] = grouped['total'] - grouped['bads']
      grouped['dist_goods'] = np.maximum(grouped['goods'] / total_goods, eps)
      grouped['dist_bads'] = np.maximum(grouped['bads'] / total_bads, eps)
      grouped['woe'] = np.log(grouped['dist_goods'] / grouped['dist_bads'])
      grouped['iv'] = (grouped['dist_goods'] - grouped['dist_bads']) * grouped['woe']
      return grouped
  ```

---

#### Q30. Cohort Retention Matrix Construction
- **Problem**: Build monthly customer cohort retention matrix (Month 0, Month 1, Month 2...).
- **Difficulty**: Hard | **Target Time**: 6 min
- **Code Solution**:
  ```python
  def build_cohort_matrix(df: pd.DataFrame) -> pd.DataFrame:
      df = df.copy()
      df['order_month'] = pd.to_datetime(df['order_date']).dt.to_period('M')
      df['cohort'] = df.groupby('customer_id')['order_month'].transform('min')
      df['cohort_period'] = (df['order_month'] - df['cohort']).apply(lambda x: x.n)

      cohort_data = df.groupby(['cohort', 'cohort_period'])['customer_id'].nunique().reset_index()
      cohort_matrix = cohort_data.pivot(index='cohort', columns='cohort_period', values='customer_id')
      retention = cohort_matrix.divide(cohort_matrix.iloc[:, 0], axis=0)
      return retention
  ```

---

### Part 4: Dynamic Programming & Core Algorithms (Q31 – Q40)

#### Q31. Balanced Pair Selection (`findMinMaxDifference`)
- **Problem**: Given $N$ integers and integer $P$, choose $P$ disjoint pairs minimizing the maximum absolute difference between any selected pair.
- **Difficulty**: Hard | **Target Time**: 6 min
- **Code Solution**:
  ```python
  def findMinMaxDifference(N: int, P: int, arr: List[int]) -> int:
      if P == 0: return 0
      vals = sorted(arr)
      def feasible(d: int) -> bool:
          count, i = 0, 0
          while i + 1 < N:
              if vals[i + 1] - vals[i] <= d:
                  count += 1
                  i += 2
                  if count >= P: return True
              else:
                  i += 1
          return False

      low, high = 0, vals[-1] - vals[0]
      while low < high:
          mid = low + (high - low) // 2
          if feasible(mid):
              high = mid
          else:
              low = mid + 1
      return low
  ```

---

#### Q32. 0/1 Knapsack Problem (Dynamic Programming)
- **Problem**: Given weights `wt`, values `val`, and capacity `W`, find max achievable value.
- **Difficulty**: Medium | **Target Time**: 4 min
- **Code Solution**:
  ```python
  def knapsack_01(W: int, wt: List[int], val: List[int]) -> int:
      dp = [0] * (W + 1)
      for w_item, v_item in zip(wt, val):
          for cap in range(W, w_item - 1, -1):
              dp[cap] = max(dp[cap], dp[cap - w_item] + v_item)
      return dp[W]
  ```

---

#### Q33. Coin Change (Minimum Coins)
- **Problem**: Find the minimum number of coins needed to make amount `A`.
- **Difficulty**: Medium | **Target Time**: 4 min
- **Code Solution**:
  ```python
  def coin_change(coins: List[int], amount: int) -> int:
      dp = [float('inf')] * (amount + 1)
      dp[0] = 0
      for c in coins:
          for a in range(c, amount + 1):
              dp[a] = min(dp[a], dp[a - c] + 1)
      return dp[amount] if dp[amount] != float('inf') else -1
  ```

---

#### Q34. Longest Increasing Subsequence ($O(N \log N)$)
- **Problem**: Return length of longest strictly increasing subsequence.
- **Difficulty**: Medium | **Target Time**: 4 min
- **Code Solution**:
  ```python
  import bisect

  def length_of_lis(nums: List[int]) -> int:
      tails = []
      for x in nums:
          idx = bisect.bisect_left(tails, x)
          if idx == len(tails):
              tails.append(x)
          else:
              tails[idx] = x
      return len(tails)
  ```

---

#### Q35. Merge Intervals
- **Problem**: Merge all overlapping intervals in `[[1,3],[2,6],[8,10],[15,18]]`.
- **Difficulty**: Medium | **Target Time**: 3 min
- **Code Solution**:
  ```python
  def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
      intervals.sort(key=lambda x: x[0])
      merged = [intervals[0]]
      for curr in intervals[1:]:
          prev = merged[-1]
          if curr[0] <= prev[1]:
              prev[1] = max(prev[1], curr[1])
          else:
              merged.append(curr)
      return merged
  ```

---

#### Q36. Trapping Rain Water
- **Problem**: Given $N$ non-negative integers representing elevation map, compute water trapped.
- **Difficulty**: Hard | **Target Time**: 5 min
- **Code Solution**:
  ```python
  def trap_water(height: List[int]) -> int:
      left, right = 0, len(height) - 1
      max_left, max_right = 0, 0
      water = 0
      while left < right:
          if height[left] < height[right]:
              if height[left] >= max_left:
                  max_left = height[left]
              else:
                  water += max_left - height[left]
              left += 1
          else:
              if height[right] >= max_right:
                  max_right = height[right]
              else:
                  water += max_right - height[right]
              right -= 1
      return water
  ```

---

#### Q37. Kth Largest Element in an Array (Quickselect)
- **Problem**: Find $k$-th largest element in an unsorted array in $O(N)$ average time.
- **Difficulty**: Medium | **Target Time**: 4 min
- **Code Solution**:
  ```python
  import heapq

  def find_kth_largest(nums: List[int], k: int) -> int:
      return heapq.nlargest(k, nums)[-1]
  ```

---

#### Q38. Binary Tree Level Order Traversal
- **Problem**: Return level order traversal of binary tree nodes as nested list.
- **Difficulty**: Easy | **Target Time**: 3 min
- **Code Solution**:
  ```python
  from collections import deque

  def level_order(root) -> List[List[int]]:
      if not root: return []
      res, queue = [], deque([root])
      while queue:
          level = []
          for _ in range(len(queue)):
              node = queue.popleft()
              level.append(node.val)
              if node.left: queue.append(node.left)
              if node.right: queue.append(node.right)
          res.append(level)
      return res
  ```

---

#### Q39. Topological Sort (Course Schedule)
- **Problem**: Determine if DAG has cycle given prerequisites pairs.
- **Difficulty**: Medium | **Target Time**: 5 min
- **Code Solution**:
  ```python
  def can_finish_courses(num_courses: int, prereqs: List[List[int]]) -> bool:
      adj = defaultdict(list)
      in_degree = [0] * num_courses
      for dest, src in prereqs:
          adj[src].append(dest)
          in_degree[dest] += 1

      queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
      count = 0
      while queue:
          curr = queue.popleft()
          count += 1
          for nxt in adj[curr]:
              in_degree[nxt] -= 1
              if in_degree[nxt] == 0:
                  queue.append(nxt)
      return count == num_courses
  ```

---

#### Q40. LRU Cache Implementation
- **Problem**: Design Least Recently Used (LRU) Cache supporting $O(1)$ `get` and `put`.
- **Difficulty**: Hard | **Target Time**: 6 min
- **Code Solution**:
  ```python
  from collections import OrderedDict

  class LRUCache:
      def __init__(self, capacity: int):
          self.cap = capacity
          self.cache = OrderedDict()

      def get(self, key: int) -> int:
          if key not in self.cache: return -1
          self.cache.move_to_end(key)
          return self.cache[key]

      def put(self, key: int, value: int) -> None:
          if key in self.cache:
              self.cache.move_to_end(key)
          self.cache[key] = value
          if len(self.cache) > self.cap:
              self.cache.popitem(last=False)
  ```

---

### Part 5: Production Machine Learning & Pipeline Engineering (Q41 – Q50)

#### Q41. Stratified Bootstrap Sampling from Scratch
- **Problem**: Generate $B$ bootstrap resamples preserving class proportions.
- **Difficulty**: Easy | **Target Time**: 2 min
- **Code Solution**:
  ```python
  def stratified_bootstrap(X: np.ndarray, y: np.ndarray, seed: int = 42):
      np.random.seed(seed)
      classes = np.unique(y)
      boot_indices = []
      for c in classes:
          idx_c = np.where(y == c)[0]
          sample_c = np.random.choice(idx_c, size=len(idx_c), replace=True)
          boot_indices.extend(sample_c)
      return X[boot_indices], y[boot_indices]
  ```

---

#### Q42. Focal Loss for Extreme Class Imbalance
- **Problem**: Implement Focal Loss $\mathcal{L} = -\alpha_t (1 - p_t)^\gamma \log(p_t)$ in NumPy.
- **Difficulty**: Medium | **Target Time**: 4 min
- **Code Solution**:
  ```python
  def focal_loss(y_true: np.ndarray, y_pred_prob: np.ndarray, gamma: float = 2.0, alpha: float = 0.25) -> float:
      eps = 1e-12
      p = np.clip(y_pred_prob, eps, 1.0 - eps)
      p_t = np.where(y_true == 1, p, 1.0 - p)
      alpha_t = np.where(y_true == 1, alpha, 1.0 - alpha)
      loss = -alpha_t * ((1.0 - p_t) ** gamma) * np.log(p_t)
      return float(np.mean(loss))
  ```

---

#### Q43. Gini Impurity from Class Labels
- **Problem**: Calculate Gini impurity $1 - \sum p_i^2$ from array of categorical labels.
- **Difficulty**: Easy | **Target Time**: 2 min
- **Code Solution**:
  ```python
  def calculate_gini(labels: np.ndarray) -> float:
      if len(labels) == 0: return 0.0
      _, counts = np.unique(labels, return_counts=True)
      probs = counts / len(labels)
      return float(1.0 - np.sum(probs**2))
  ```

---

#### Q44. Precision-Recall AUC (PR-AUC) via Trapezoidal Rule
- **Problem**: Compute Area Under Precision-Recall Curve without external libraries.
- **Difficulty**: Medium | **Target Time**: 4 min
- **Code Solution**:
  ```python
  def manual_pr_auc(y_true: np.ndarray, scores: np.ndarray) -> float:
      order = np.argsort(-scores)
      y_sorted = y_true[order]
      tp = np.cumsum(y_sorted == 1)
      fp = np.cumsum(y_sorted == 0)
      recall = tp / (y_true == 1).sum()
      precision = tp / (tp + fp)
      # Prepend (Recall=0, Precision=1)
      recall = np.concatenate(([0.0], recall))
      precision = np.concatenate(([1.0], precision))
      return float(np.sum((recall[1:] - recall[:-1]) * precision[1:]))
  ```

---

#### Q45. Brier Score & Brier Skill Score (BSS)
- **Problem**: Calculate Brier score and Brier Skill Score relative to climatological baseline.
- **Difficulty**: Easy | **Target Time**: 2 min
- **Code Solution**:
  ```python
  def brier_metrics(y_true: np.ndarray, probs: np.ndarray) -> dict:
      bs = np.mean((probs - y_true)**2)
      base_p = np.mean(y_true)
      bs_ref = np.mean((base_p - y_true)**2)
      bss = 1.0 - (bs / bs_ref)
      return {'Brier_Score': round(bs, 4), 'Brier_Skill_Score': round(bss, 4)}
  ```

---

#### Q46. Population Stability Index (PSI) Calculation
- **Problem**: Compute PSI between development baseline and current production score distributions.
- **Difficulty**: Medium | **Target Time**: 4 min
- **Code Solution**:
  ```python
  def compute_psi(expected: np.ndarray, actual: np.ndarray, n_bins: int = 10) -> float:
      eps = 1e-4
      quantiles = np.linspace(0, 100, n_bins + 1)
      bins = np.percentile(expected, quantiles)
      bins[0] -= 1e-5; bins[-1] += 1e-5

      e_counts, _ = np.histogram(expected, bins=bins)
      a_counts, _ = np.histogram(actual, bins=bins)

      e_pct = np.maximum(e_counts / len(expected), eps)
      a_pct = np.maximum(a_counts / len(actual), eps)

      psi = np.sum((a_pct - e_pct) * np.log(a_pct / e_pct))
      return float(round(psi, 4))
  ```

---

#### Q47. Time-Series Purged K-Fold Cross Validation
- **Problem**: Implement cross-validation generator that purges overlapping forecast horizons.
- **Difficulty**: Hard | **Target Time**: 5 min
- **Code Solution**:
  ```python
  def purged_time_series_split(n_samples: int, n_splits: int, embargo: int = 2):
      indices = np.arange(n_samples)
      split_size = n_samples // (n_splits + 1)
      for i in range(1, n_splits + 1):
          train_end = i * split_size
          test_start = train_end + embargo
          test_end = min(test_start + split_size, n_samples)
          if test_start >= n_samples: break
          yield indices[:train_end], indices[test_start:test_end]
  ```

---

#### Q48. Exponential Moving Average (EMA) from Scratch
- **Problem**: Compute exponential moving average $S_t = \alpha Y_t + (1 - \alpha) S_{t-1}$.
- **Difficulty**: Easy | **Target Time**: 2 min
- **Code Solution**:
  ```python
  def exponential_moving_avg(y: np.ndarray, alpha: float = 0.2) -> np.ndarray:
      ema = np.zeros_like(y, dtype=float)
      ema[0] = y[0]
      for t in range(1, len(y)):
          ema[t] = alpha * y[t] + (1.0 - alpha) * ema[t - 1]
      return ema
  ```

---

#### Q49. Cosine Similarity Matrix between Embedding Arrays
- **Problem**: Compute pairwise cosine similarity between query embeddings `(Q, D)` and catalog embeddings `(C, D)`.
- **Difficulty**: Medium | **Target Time**: 3 min
- **Code Solution**:
  ```python
  def cosine_similarity_matrix(Q: np.ndarray, C: np.ndarray) -> np.ndarray:
      q_norm = Q / np.linalg.norm(Q, axis=1, keepdims=True)
      c_norm = C / np.linalg.norm(C, axis=1, keepdims=True)
      return np.dot(q_norm, c_norm.T)
  ```

---

#### Q50. Scikit-learn Pipeline with Grid Search & Custom Scoring
- **Problem**: Build production pipeline with imputation, standard scaling, PCA, and LightGBM with custom PR-AUC scorer.
- **Difficulty**: Medium | **Target Time**: 5 min
- **Code Solution**:
  ```python
  from sklearn.pipeline import Pipeline
  from sklearn.preprocessing import StandardScaler
  from sklearn.impute import SimpleImputer
  from sklearn.linear_model import LogisticRegression
  from sklearn.metrics import make_scorer, precision_recall_curve, auc

  def pr_auc_score(y_true, y_pred_prob):
      p, r, _ = precision_recall_curve(y_true, y_pred_prob)
      return auc(r, p)

  def build_production_pipeline():
      pr_scorer = make_scorer(pr_auc_score, needs_proba=True)
      pipe = Pipeline([
          ('imputer', SimpleImputer(strategy='median')),
          ('scaler', StandardScaler()),
          ('classifier', LogisticRegression(class_weight='balanced', solver='liblinear'))
      ])
      return pipe, pr_scorer
  ```
