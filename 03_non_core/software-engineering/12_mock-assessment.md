# 12. Software Engineering: Comprehensive Technical Mock Assessment

> **Exam Focus**: Data Structures & Algorithms (DSA), Relational Databases (SQL), Computer Systems & Architecture  
> **Target Audience**: IIT Kanpur students preparing for SDE, Software Engineering, and Technology Analyst placement tests.  
> **Duration**: 60 Minutes  
> **Total Marks**: 50 Marks (+2 for correct MCQ, -0.66 for incorrect; Full stepwise credit for code implementations and SQL queries).

---

## Section A: Computer Science Foundations & Big-O MCQs (10 Marks)

### Q1. Binary Search Tree Time Complexity
In an unbalanced Binary Search Tree (BST) containing $n$ elements, what is the worst-case time complexity of searching for an element?
- **(a)** $O(1)$
- **(b)** $O(\log n)$
- **(c)** $O(n)$
- **(d)** $O(n \log n)$

### Q2. TCP vs. UDP Protocol Characteristics
Which statement accurately describes the transport layer difference between TCP and UDP?
- **(a)** UDP establishes a 3-way handshake to guarantee in-order packet delivery.
- **(b)** TCP provides reliable, ordered, and error-checked byte streams at the cost of connection overhead; UDP sends connectionless datagrams with minimal latency.
- **(c)** TCP operates strictly in hardware, while UDP operates strictly in the kernel.
- **(d)** UDP packets cannot exceed 64 bytes.

### Q3. Database Composite Indexing (Leftmost Prefix Rule)
A PostgreSQL table `orders` has a composite B-tree index on columns `(customer_id, order_date, status)`. Which of the following SQL `WHERE` clauses will **NOT** utilize this index for fast index-range scanning?
- **(a)** `WHERE customer_id = 1042 AND order_date = '2026-10-21'`
- **(b)** `WHERE customer_id = 1042`
- **(c)** `WHERE order_date = '2026-10-21' AND status = 'COMPLETED'`
- **(d)** `WHERE customer_id = 1042 AND order_date >= '2026-10-01' AND status = 'PENDING'`

### Q4. Hash Map Collision Resolution
In a Hash Map using Separate Chaining, if the hash function distributes keys uniformly across $m$ buckets and $n$ total elements are stored, what is the average-case time complexity of `get(key)`?
- **(a)** $O(1 + \frac{n}{m})$
- **(b)** $O(n)$
- **(c)** $O(\log m)$
- **(d)** $O(m \log n)$

### Q5. Process vs. Thread Memory Sharing
In standard operating system process management:
- **(a)** Threads within the same process share the same heap memory and address space, but each thread has its own private execution stack and registers.
- **(b)** Threads have separate heap memory, but share the same execution stack.
- **(c)** Processes can directly read each other's memory without OS inter-process communication (IPC).
- **(d)** Context switching between processes is faster than context switching between threads.

---

## Section B: Algorithmic Coding Challenge (15 Marks)

### Problem 6: Longest Substring Without Repeating Characters
Given a string `s`, find the length of the **longest substring** without repeating characters.

#### Examples:
- Input: `s = "abcabcbb"` $\implies$ Output: `3` (The answer is `"abc"`, with length 3).
- Input: `s = "bbbbb"` $\implies$ Output: `1` (The answer is `"b"`, with length 1).
- Input: `s = "pwwkew"` $\implies$ Output: `3` (The answer is `"wke"`, with length 3).

#### Candidate Tasks:
1. Write a clean, working solution in Python (or C++/Java).
2. Achieve optimal **$O(n)$ time complexity** and **$O(\min(n, m))$ auxiliary space complexity** (where $m$ is the character alphabet size).
3. Explain the sliding window logic and how edge cases (empty string, single character string) are handled.

---

## Section C: Database Architecture & SQL Optimization (15 Marks)

### Problem 7: High-Volume E-Commerce Order Aggregation
You are provided two tables in a high-concurrency PostgreSQL relational database:
1. `users` (`user_id` PK, `name`, `signup_date`, `city`)
2. `transactions` (`txn_id` PK, `user_id` FK, `amount`, `txn_timestamp`, `status`)

#### Candidate Tasks:
1. Write an optimized SQL query to find the **Top 5 users in 'Kanpur' by total successful transaction spend in the year 2026**. Output: `user_id`, `name`, `total_spend_inr`, and `transaction_count`.
2. If the `transactions` table contains $100\text{ Million rows}$, identify which indexes you must create to prevent a sequential full table scan and ensure the query returns in under $50\text{ ms}$.

---

## Section D: Systems Architecture & Trade-Offs (10 Marks)

### Scenario: High-Concurrency Ticket Booking System (BookMyShow / IRCTC)
During the first 60 seconds of opening ticket sales for an India-Pakistan cricket match, 500,000 concurrent users attempt to book 50,000 available seats.
1. Describe how you would prevent **double-booking** (two users reserving the exact same seat) using database locking mechanisms (Pessimistic vs. Optimistic locking or Redis distributed locks).
2. Design a **virtual waiting room / queueing architecture** to prevent incoming traffic from crashing the core database.

---

# Comprehensive Solutions & Marking Rubric

---

### Solution Q1: BST Worst-Case Complexity
- **Correct Option: (c)** $O(n)$
- **Explanation**: If elements are inserted in sorted order ($1, 2, 3, 4, \dots$), an unbalanced BST degenerates into a linear linked list where tree height $h = n$, resulting in $O(n)$ search time. (Balanced trees like AVL or Red-Black guarantee $O(\log n)$).

---

### Solution Q2: TCP vs. UDP
- **Correct Option: (b)** TCP provides reliable, ordered, error-checked byte streams; UDP provides low-latency connectionless datagrams.

---

### Solution Q3: Composite Indexing (Leftmost Prefix Rule)
- **Correct Option: (c)** `WHERE order_date = '2026-10-21' AND status = 'COMPLETED'`
- **Explanation**: The composite index begins with `customer_id`. Because Query (c) omits the leading column `customer_id`, the database engine cannot traverse the B-tree hierarchically and must fall back to a full table scan.

---

### Solution Q4: Hash Map Collision Time
- **Correct Option: (a)** $O(1 + \frac{n}{m})$
- **Explanation**: The load factor is $\alpha = n/m$, representing the average chain length. The expected time to hash the key is $O(1)$, and traversing the average chain takes $O(n/m)$ time.

---

### Solution Q5: Process vs. Thread Memory
- **Correct Option: (a)** Threads share heap and text segments, but each thread possesses its own private stack and registers.

---

### Solution Problem 6: Longest Substring Without Repeating Characters

```python
def length_of_longest_substring(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.
    Time Complexity: O(n) - each character is visited at most twice.
    Space Complexity: O(min(n, m)) - storing character indices in a hash map.
    """
    char_index_map = {}  # char -> most recent index
    left = 0
    max_length = 0
    
    for right, char in enumerate(s):
        # If character is already in window, jump 'left' pointer past its previous occurrence
        if char in char_index_map and char_index_map[char] >= left:
            left = char_index_map[char] + 1
            
        char_index_map[char] = right
        current_window_len = right - left + 1
        if current_window_len > max_length:
            max_length = current_window_len
            
    return max_length
```

#### Stepwise Logic & Edge Cases:
- **Sliding Window**: We maintain a dynamic window `[left, right]`. As `right` advances, if `char` was seen at `prev_idx >= left`, we slide `left` forward to `prev_idx + 1` in $O(1)$ without backtracking.
- **Edge Cases**:
  - `s = ""` (empty string): loop does not run, returns `0` (Correct).
  - `s = "a"` (single char): returns `1` (Correct).
  - All identical characters (`"aaaa"`): window constantly resets to length 1, returns `1` (Correct).

---

### Solution Problem 7: Database & SQL Optimization

#### 1. Optimized Query:

```sql
SELECT 
    u.user_id,
    u.name,
    SUM(t.amount) AS total_spend_inr,
    COUNT(t.txn_id) AS transaction_count
FROM users u
INNER JOIN transactions t 
    ON u.user_id = t.user_id
WHERE u.city = 'Kanpur'
  AND t.status = 'SUCCESS'
  AND t.txn_timestamp >= '2026-01-01 00:00:00'
  AND t.txn_timestamp < '2027-01-01 00:00:00'
GROUP BY u.user_id, u.name
ORDER BY total_spend_inr DESC
LIMIT 5;
```

#### 2. Index Optimization Strategy:
1. `CREATE INDEX idx_users_city ON users(city) INCLUDE (name);`
   - Enables fast index-scan of only Kanpur users ($< 2\%$ of total user base).
2. `CREATE INDEX idx_transactions_user_status_time ON transactions(user_id, status, txn_timestamp) INCLUDE (amount);`
   - A **Covering Index**: Stores `amount` in the leaf pages, allowing the database to execute an **Index-Only Scan** without touching the heavy 100M-row table heap on disk.

---

### Solution Section D: High-Concurrency Ticket Booking System
1. **Preventing Double Booking**:
   - **Distributed Lock in Redis (Redlock / `SETNX`)**: When a user selects Seat 42A, write `SET seat:42A usr_1042 NX EX 600` (sets key only if not exists, expiring in 10 minutes). If another user attempts the same seat, Redis returns `null` instantly without touching the SQL database.
   - **Optimistic Locking at Database Level**:
     ```sql
     UPDATE seats SET status = 'BOOKED', user_id = 1042, version = version + 1 
     WHERE seat_id = '42A' AND version = 5 AND status = 'AVAILABLE';
     ```
     If another transaction updated `version` first, the row count is 0, cleanly rejecting the second purchase.
2. **Virtual Waiting Room Architecture**:
   - Do not allow 500,000 users to query seat availability simultaneously.
   - Direct incoming traffic to an edge queue (e.g., Cloudflare Waiting Room or Kafka token queue).
   - Rate-limit admissions to the seat selection engine to 2,000 users per minute, matching database write capacity and preventing server crashes.
