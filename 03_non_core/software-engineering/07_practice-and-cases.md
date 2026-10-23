# 07. Software Engineering: System Architecture Cases & Coding Patterns

> **Track**: Software Development Engineer (SDE) & Systems Engineering  
> **Target Audience**: IIT Kanpur candidates preparing for technical problem-solving rounds, low-level design (LLD), and entry-level high-level design (HLD) interviews.  
> **Content Structure**: Complete production-grade code implementations, algorithmic complexity analyses, system trade-offs, and interviewer follow-up defenses.

---

## Case 1: Low-Level Design (LLD): Least Recently Used (LRU) Cache

### Problem Statement
Design and implement a data structure that follows the constraints of a **Least Recently Used (LRU) Cache**.
The cache must support two operations in strictly **$O(1)$ average time complexity**:
1. `get(key)`: Returns the value of the key if it exists in the cache, otherwise returns `-1`.
2. `put(key, value)`: Updates the value of the key if it exists, or inserts the key-value pair. If the number of keys exceeds the `capacity` from this operation, evict the least recently used key.

---

### Architectural Design & Data Structure Choice
- A raw array or list requires $O(n)$ search and eviction time.
- A raw Hash Map provides $O(1)$ lookup, but cannot maintain ordering of recency.
- **The Optimal Architecture**: Combine a **Hash Map** with a **Doubly Linked List**:
  - The **Hash Map** maps `key -> Node pointer` ($O(1)$ lookup).
  - The **Doubly Linked List** stores nodes ordered by recency. Moving a node to the front (head) or removing the least recently used node from the rear (tail) takes $O(1)$ pointer operations.
  - Using dummy `head` and `tail` sentinel nodes completely eliminates boundary `NULL` pointer checks.

```text
[Dummy Head] <===> [Most Recently Used Node] <===> ... <===> [Least Recently Used Node] <===> [Dummy Tail]
```

### Complete, Tested Python Implementation

```python
class Node:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node pointer
        
        # Initialize dummy sentinel nodes
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_to_front(self, node: Node) -> None:
        """Inserts a node immediately after dummy head (marks as MRU)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: Node) -> None:
        """Unlinks a node from the doubly linked list in O(1)."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_front(self, node: Node) -> None:
        """Moves an existing node to head (refreshes recency)."""
        self._remove_node(node)
        self._add_to_front(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                # Evict LRU node (node immediately preceding dummy tail)
                lru_node = self.tail.prev
                self._remove_node(lru_node)
                del self.cache[lru_node.key]
                
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)
```

### Complexity Analysis
- **Time Complexity**:
  - `get(key)`: $O(1)$ hash map lookup + $O(1)$ pointer rewiring.
  - `put(key, value)`: $O(1)$ hash map insertion + $O(1)$ linked list manipulation.
- **Space Complexity**:
  - $O(C)$, where $C$ is the capacity of the cache. Stores at most $C$ key-value pairs in the hash map and $C + 2$ nodes in the doubly linked list.

---

## Case 2: High-Level System Design (HLD): Scalable URL Shortener (TinyURL)

### 1. Functional & Non-Functional Requirements
- **Functional**:
  - Given a long URL (e.g., `https://example.com/very/long/path/document.pdf`), generate a unique 7-character short URL (`https://tiny.url/aZ9xK2q`).
  - Accessing the short URL redirects the client via HTTP 301 or 302 to the original destination.
- **Non-Functional**:
  - High Availability ($99.99\%$) and sub-10ms redirect latency.
  - High read-to-write ratio ($100:1$ read heavy).

### 2. Back-of-the-Envelope Capacity Estimations
- **Write Volume**: 10 million new URLs created per month $\implies \frac{10,000,000}{30 \times 86400} \approx \mathbf{4 \text{ writes/second}}$.
- **Read Volume (Redirects)**: $100 \times \text{Writes} \approx \mathbf{400 \text{ reads/second}}$ (Peak: $1,200\text{ reads/sec}$).
- **Storage Calculation (5 Years)**:
  - $10\text{ M/month} \times 12\text{ months} \times 5\text{ years} = 600\text{ Million URLs}$.
  - Average URL size: $500\text{ bytes}$.
  - Total Storage $= 600\text{ M} \times 500\text{ B} = \mathbf{300 \text{ GB}}$ (Fits on a single modern SSD, but replicated for redundancy).

### 3. URL Encoding Strategy: Base62 vs. MD5 Hash Collisions
- Using Base62 encoding (`[a-z, A-Z, 0-9]`: 62 alphanumeric characters):
- A 7-character token provides:
  $$62^7 = 3,521,614,606,208 \approx \mathbf{3.5 \text{ Trillion unique URLs}}$$
  *(Sufficient for thousands of years at current write velocity).*
- **How to generate unique tokens without collisions**:
  Do NOT hash the string with MD5/SHA256 (requires expensive collision resolution). Instead, use a distributed auto-incrementing integer ID generator (e.g., Snowflake ID or Redis `INCR`), then convert the base-10 integer to Base62!

```python
BASE62_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def id_to_base62(unique_id: int) -> str:
    if unique_id == 0:
        return BASE62_CHARS[0]
    token = []
    while unique_id > 0:
        unique_id, rem = divmod(unique_id, 62)
        token.append(BASE62_CHARS[rem])
    return "".join(reversed(token)).rjust(7, '0')
```

### 4. High-Level Architecture Diagram
```text
[Client] ──► [Load Balancer] ──► [Web App Servers] ──► [Redis Cache (Top 20% URLs)]
                                       │                   │ Cache Miss
                                       ▼                   ▼
                            [Snowflake ID Generator] ──► [PostgreSQL Database]
```

### 5. HTTP 301 vs. 302 Redirection Trade-off
- **HTTP 301 (Moved Permanently)**: Browser caches the redirect destination locally. Subsequent clicks bypass your server entirely. *Pros*: Fastest response, zero server load. *Cons*: You cannot track click analytics or user telemetry.
- **HTTP 302 (Found / Temporary Redirect)**: Browser always hits the server first before redirecting. *Pros*: Accurate click telemetry, fraud detection, and monetization tracking. *Cons*: Slightly higher server load.
- *Production Standard*: Use **HTTP 302** if click metrics and analytics are required.

---

## Executive Interview Defense Probes

> **Q1**: *"In the TinyURL design, what happens if the Redis cache runs out of memory?"*  
> **Model Answer**: "We configure the Redis instance with an **LRU (Least Recently Used) eviction policy** (`allkeys-lru`). According to the Pareto 80/20 rule, $20\%$ of popular URLs drive $80\%$ of redirect traffic. Caching only that active $20\%$ working set requires less than $5\text{ GB}$ of RAM. If memory fills up, Redis automatically purges the cold URLs without crashing, falling back to the database on demand."

> **Q2**: *"How do you handle race conditions if two users try to register the exact same custom alias (e.g., `tiny.url/iitk`) at the exact same millisecond?"*  
> **Model Answer**: "We enforce a **UNIQUE constraint** on the `short_token` column at the database level. Additionally, we wrap the check-and-insert operation in a serializable transaction or use a distributed lock (e.g., Redis `SETNX`). If two concurrent requests arrive simultaneously, the first acquires the lock, while the second fails with a `409 Conflict` HTTP error, cleanly alerting the user that the custom alias is taken."
