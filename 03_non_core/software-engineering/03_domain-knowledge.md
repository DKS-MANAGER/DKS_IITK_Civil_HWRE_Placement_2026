# 03. Software Engineering: Core Architecture, DSA & Systems Design

> **Track**: Software Engineering (SWE) & Technology Roles  
> **Target Audience**: IIT Kanpur students preparing for entry-level Software Development Engineer (SDE), Technology Analyst, and Systems Engineering interviews.  
> **Methodological Focus**: Algorithmic problem-solving patterns, computational complexity, memory architecture, relational/NoSQL databases, and entry-level distributed systems.

---

## 1. Computational Foundations: Memory & Asymptotic Complexity

Writing efficient, scalable software requires understanding how hardware executes code:

### A. Memory Hierarchy: Stack vs. Heap
- **The Stack**:
  - Linear, contiguous memory automatically allocated and deallocated as function call frames enter and exit.
  - Extremely fast allocation ($O(1)$, moving the stack pointer).
  - Stores local primitive variables and function return addresses.
  - Limited in size (typically $1\text{--}8\text{ MB}$); deep recursion without a base case triggers a **Stack Overflow**.
- **The Heap**:
  - Dynamically allocated memory managed at runtime (`malloc`/`free` in C/C++, `new` in Java, managed garbage collection in Python/Go).
  - Slower allocation with potential memory fragmentation.
  - Stores objects, dynamic arrays, and structures whose lifetimes extend beyond the creating function.

### B. Asymptotic Complexity (Big-O Notation)
Big-O characterizes the upper bound of resource consumption as input size $n \to \infty$:
- **Time Complexity**: Number of basic CPU operations executed.
- **Auxiliary Space Complexity**: Extra memory allocated by the algorithm *excluding* the input memory.

```text
Complexity Hierarchy (Fastest to Slowest):
O(1) [Constant] ──► O(log n) [Binary Search] ──► O(n) [Linear Scan] ──► 
O(n log n) [Merge/Quick Sort] ──► O(n²) [Nested Loops] ──► O(2ⁿ) [Recursion] ──► O(n!) [Permutations]
```

---

## 2. Core Data Structures & Interview Algorithmic Patterns

Mastering technical coding rounds requires recognizing standard algorithmic archetypes:

### Pattern 1: Two Pointers & Sliding Window
- **When to Use**: Linear sequences (arrays, strings) seeking contiguous subarrays, palindromes, or target pair sums in sorted arrays.
- **Advantage**: Reduces brute-force $O(n^2)$ nested search to optimal $O(n)$ time by maintaining left ($L$) and right ($R$) boundaries dynamically.
- *Classic Problems*: Longest Substring Without Repeating Characters, Container With Most Water, 3Sum.

### Pattern 2: Hash Maps & Collision Resolution
- **Mechanism**: A hash function maps arbitrary keys to an integer index in an underlying array.
- **Average Time**: $O(1)$ search, insertion, and deletion.
- **Worst Case**: $O(n)$ if all keys hash to the same bucket (collision). Modern engines resolve collisions via:
  1. *Separate Chaining*: Linked lists or balanced red-black trees at each bucket (Java 8+ `HashMap`).
  2. *Open Addressing*: Linear probing or double hashing within the contiguous table.

### Pattern 3: Monotonic Stacks & Queues
- **When to Use**: Finding the "Next Greater Element" or "Previous Smaller Element" in an array.
- **Advantage**: Maintains elements in strictly increasing or decreasing order, guaranteeing each element is pushed and popped at most once ($O(n)$ total time).
- *Classic Problems*: Daily Temperatures, Largest Rectangle in Histogram, Trapping Rain Water.

### Pattern 4: Trees & Graphs (BFS vs. DFS)
- **Breadth-First Search (BFS)**: Uses a `Queue`. Explores neighbors level by level. Guarantees the **shortest path in an unweighted graph**. Time: $O(V + E)$, Space: $O(V)$.
- **Depth-First Search (DFS)**: Uses recursion or an explicit `Stack`. Explores down each branch before backtracking. Ideal for connected components, topological sorting, and cycle detection. Time: $O(V + E)$, Space: $O(V)$.

### Pattern 5: Dynamic Programming (DP)
- **Core Criteria**: (1) **Overlapping Subproblems** and (2) **Optimal Substructure**.
- **Top-Down (Memoization)**: Natural recursive formulation augmented with an array or hash map caching computed sub-states.
- **Bottom-Up (Tabulation)**: Iteratively fills a state table from base cases upward, eliminating recursion call-stack overhead and enabling space optimization (e.g., keeping only the last two rows).

---

## 3. Databases: Relational (RDBMS) vs. NoSQL

### A. ACID Properties (Relational Databases: PostgreSQL, MySQL)
- **A (Atomicity)**: Transactions execute as an all-or-nothing unit; if any query fails, the entire transaction rolls back.
- **C (Consistency)**: Transactions transition the database from one valid state to another, enforcing schema constraints, unique keys, and foreign key cascades.
- **I (Isolation)**: Concurrent transactions do not interfere with each other (Isolation levels: Read Uncommitted, Read Committed, Repeatable Read, Serializable).
- **D (Durability)**: Once a transaction commits, its modifications are permanently recorded on non-volatile disk via Write-Ahead Logging (WAL).

### B. Indexing Mechanics: B+ Trees vs. Hash Indexes
- **B+ Tree Indexes**: Balanced search tree storing sorted keys in internal nodes and data pointers strictly in linked leaf nodes.
  - Supports both point lookups ($O(\log N)$) and range scans (`WHERE age BETWEEN 20 AND 30`).
  - **Leftmost Prefix Rule**: A composite index on `(city, department, salary)` accelerates queries filtering by `city` or `(city, department)`, but provides **zero speedup** for a query filtering only on `department` or `salary`.

### C. When to Choose NoSQL
- **Document Stores (MongoDB)**: Semi-structured JSON documents with flexible, evolving schemas; ideal for catalogs and user profiles.
- **Key-Value Stores (Redis)**: In-memory hash stores delivering sub-millisecond lookups for caching, session management, and rate limiting.
- **Wide-Column / Time-Series (Cassandra, InfluxDB)**: High-throughput sequential write performance for IoT sensor telemetry and financial tick data.

---

## 4. Systems Design Fundamentals for Entry-Level Interviews

### A. The CAP Theorem Qualified (Brewer, 2000; Gilbert & Lynch, 2002)
In any distributed data store, three properties compete:
1. **Consistency (Linearizability)**: Every read receives the most recent write or an error.
2. **Availability**: Every non-failing node returns a non-error response for every request (without guaranteeing it is the latest write).
3. **Partition Tolerance**: The system continues to operate despite arbitrary message loss or network partitions between nodes.

> **Crucial Interview Qualification**: Network partitions ($P$) are a physical inevitability of real-world networks (cables get cut, switches fail). Therefore, a distributed system **cannot choose "CA"**. When a network partition occurs, the system must choose between:
> - **CP (Consistency over Availability)**: Reject writes or block reads to prevent reading stale/conflicting data (e.g., Google Spanner, HBase, ZooKeeper).
> - **AP (Availability over Consistency)**: Accept writes on both sides of the network split, allowing temporary divergence and resolving conflicts later via eventual consistency (e.g., Amazon DynamoDB, Cassandra).

### B. Caching Architecture & Eviction Policies
To prevent database connection exhaustion under high traffic, place an in-memory cache (Redis) in front of the database:
- **Cache-Aside (Lazy Loading)**: Application first checks cache. On cache miss, it reads from DB, writes result to cache, and returns to client.
- **Eviction Policies**:
  - **LRU (Least Recently Used)**: Discards the item that has not been accessed for the longest time (implemented via Doubly Linked List + Hash Map in $O(1)$).
  - **TTL (Time to Live)**: Keys expire automatically after a set duration.

---

## 5. Civil & HWRE Engineering Transferable Skills to Software

| Civil / HWRE Principle | Software Engineering Equivalent |
| :--- | :--- |
| **Finite Difference Grid Discretization (Navier-Stokes)** | Multidimensional array data structures and matrix computation algorithms. |
| **Water Pipe Network Loop Balancing (Hardy Cross)** | Graph algorithms, cycle detection, and topological sorting. |
| **Reservoir Spillway Discharge Capacity Under Peak Floods** | System rate-limiting, load shedding, and leaky bucket/token bucket throttling. |
| **Structural Redundancy & Trusses (Static Indeterminacy)** | Distributed high availability, active-passive failover, and fault tolerance. |
