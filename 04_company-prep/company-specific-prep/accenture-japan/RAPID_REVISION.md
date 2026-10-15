# Rapid Revision — Complete Assessment Revision Guide

> **Document Status**: Complete, High-Density Revision Guide for Immediate Assessment Preparation  
> **Target Role**: Digital Consultant (Analyst Entry Level), Accenture Japan Ltd. (`[JD VERIFIED]`)  
> **Target Audience**: IIT Engineering Candidates (Graduating by June 2027)  
> **Evidence & Scope Disclosure**:  
> * Accenture Japan's official Job Description confirms that Digital Consultants operate across Cloud, AI, Big Data, IoT, and Manufacturing Digitalization (`[JD VERIFIED]`), but does not publish a universal fixed test blueprint.  
> * Recent candidate reports (e.g., October 2026) describe formats such as 20 MCQs in 20 minutes followed by 1 coding question in 60 minutes, while other hiring announcements describe a 90-minute technical and cognitive assessment.  
> * **Always follow your specific test invitation** for exact section timing. This guide provides prioritized, high-density preparation across all high-probability technical domains.

---

## 🗺️ Master Table of Contents & Navigation

* [1. How to Use This Revision Guide](#1-how-to-use-this-revision-guide) (30-min, 60-min & 90-min routes)
* [2. Five Questions You Must Answer Immediately](#2-five-questions-you-must-answer-immediately)
* [3. Section A: Programming Logic, Pseudocode and Python](#3-section-a-programming-logic-pseudocode-and-python-priority-1)
* [4. Section B: SQL and Relational Databases](#4-section-b-sql-and-relational-databases-priority-1)
* [5. Section C: Quantitative Aptitude and Logical Reasoning](#5-section-c-quantitative-aptitude-and-logical-reasoning-priority-1)
* [6. Section D: Computer Science and IT Fundamentals](#6-section-d-computer-science-and-it-fundamentals-priority-2)
* [7. Section E: Cloud Computing and Digital Infrastructure](#7-section-e-cloud-computing-and-digital-infrastructure-priority-2)
* [8. Section F: Cybersecurity Fundamentals](#8-section-f-cybersecurity-fundamentals-priority-2)
* [9. Section G: AI, Machine Learning, GenAI and LLMs](#9-section-g-ai-machine-learning-genai-and-llms-priority-2)
* [10. Section H: Digital Consulting and Business Problem-Solving](#10-section-h-digital-consulting-and-business-problem-solving-priority-2)
* [11. Section I: Japan-Specific and Accenture Company Context](#11-section-i-japan-specific-and-accenture-company-context-priority-2)
* [12. Section J: Rapid Formula and Command Reference Sheet](#12-section-j-rapid-formula-and-command-reference-sheet)
* [13. Section K: Common Traps and MCQ Elimination Strategies](#13-section-k-common-traps-and-mcq-elimination-strategies)
* [14. Section L: Self-Test Assessment (15 Questions)](#14-section-l-self-test-assessment-15-questions)
* [15. Section M: Comprehensive Answer Key and Explanations](#15-section-m-comprehensive-answer-key-and-explanations)
* [16. Section N: Final 5-Minute Pre-Test Checklist](#16-section-n-final-5-minute-pre-test-checklist)

---

## 1. How to Use This Revision Guide

### 1.1 Priority Taxonomy
* **Priority 1 (Must Know)**: Programming logic, basic Python, SQL queries, and core quantitative aptitude. These appear in nearly all online screening assessments.
* **Priority 2 (Useful / Differentiating)**: CS fundamentals, cloud concepts, cybersecurity basics, AI/LLM concepts, and digital consulting trade-offs.
* **Priority 3 (Optional / Deeper Study)**: Advanced graph algorithms, heavy dynamic programming, deep ML mathematics, or complex financial valuation. Skip these under time pressure.

### 1.2 Timed Revision Routes

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                           TIMED REVISION ROUTES                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ 30-MINUTE ROUTE:                                                            │
│   • Min 00–10: Section J (Formula Sheet) + Section 2 (5 Immediate Questions)│
│   • Min 10–20: Section B (SQL Mistakes to Avoid & Core Queries)             │
│   • Min 20–30: Section A (Python Patterns: Two-Sum, Frequency Count)        │
├─────────────────────────────────────────────────────────────────────────────┤
│ 60-MINUTE ROUTE:                                                            │
│   • Min 00–20: Section A (Python/Pseudocode) & Section B (SQL Queries)      │
│   • Min 20–35: Section C (Quantitative Aptitude & Margins)                  │
│   • Min 35–50: Section D & E (CS Basics, Cloud & Security)                  │
│   • Min 50–60: Section J & K (Formula Sheet & MCQ Traps)                    │
├─────────────────────────────────────────────────────────────────────────────┤
│ 90-MINUTE ROUTE:                                                            │
│   • Complete 60-minute route above (60 mins)                                │
│   • Min 60–75: Section G (AI & GenAI/RAG) + Section H (Digital Consulting)  │
│   • Min 75–90: Section L & M (Take 15-Question Self-Test & Review Answers)   │
└─────────────────────────────────────────────────────────────────────────────┘
```

> **Important Distinction**: The revision routes above represent your **pre-test study time**, not the assessment duration itself.

### 1.3 Handling Unknown Test Formats
If your invitation does not specify the exact breakdown:
1. Expect a mix of **timed multiple-choice questions (MCQs)** and **1–2 hands-on coding/SQL tasks**.
2. Allocate your first pass strictly to quick MCQs; never spend more than 90 seconds on a single conceptual MCQ.
3. For coding tasks, write clean, brute-force solutions first to secure partial test cases before optimizing for $O(N)$ complexity.

---

## 2. Five Questions You Must Answer Immediately

Before proceeding, confirm you can answer these five foundational checks without hesitation:

1. **SQL — `WHERE` vs `HAVING`**:
   * *Answer*: `WHERE` filters individual rows *before* grouping occurs; `HAVING` filters aggregated groups *after* `GROUP BY` execution.
2. **Python — Element Frequency Counting**:
   * *Answer*: Use a dictionary: `counts[x] = counts.get(x, 0) + 1` or `collections.Counter(lst)`.
3. **OS — Process vs Thread**:
   * *Answer*: A process is an independent executing program with its own virtual memory space; threads are lightweight execution units within a process that share the process's heap, code, and address space.
4. **Cloud — IaaS vs PaaS vs SaaS**:
   * *Answer*: IaaS provides raw virtualized infrastructure (e.g., AWS EC2); PaaS provides a managed application runtime environment (e.g., Azure App Service); SaaS provides a fully hosted, ready-to-use software application (e.g., Salesforce).
5. **Aptitude — Margin vs Markup**:
   * *Answer*: $\text{Margin} = \frac{\text{Profit}}{\text{Revenue}} \times 100\%$; $\text{Markup} = \frac{\text{Profit}}{\text{Cost}} \times 100\%$. If cost is $80 and price is $100, profit is $20 -> Margin is 20.0%, Markup is 25.0%.

---

## 3. Section A: Programming Logic, Pseudocode and Python (Priority 1)

### 3.1 Python Syntax & Core Mechanics

* **Operators & Integer Division**:
  * `/` performs floating-point division: `7 / 2 == 3.5`.
  * `//` performs floor division (rounds down to negative infinity): `7 // 2 == 3`, but `-7 // 2 == -4`!
  * `%` is the modulo operator: `7 % 2 == 1`, `-7 % 2 == 1` in Python (result matches sign of divisor).
  * `**` is exponentiation: `2 ** 3 == 8`. Precedence: `**` > `*, /, //, %` > `+, -`.
* **String Operations & Immutability**:
  * Strings in Python are immutable. Any modification (`s.replace()`, `s.upper()`) creates a new string object.
  * Slicing: `s[start:stop:step]`. `s[::-1]` reverses a string in $O(N)$ time.
  * Efficient joining: Always use `"".join(list_of_strings)` ($O(N)$) instead of repeated `+` concatenation in a loop ($O(N^2)$).
* **Lists, Indexing & Slicing**:
  * Indexing is 0-based. Negative indices count from right: `arr[-1]` is the last element.
  * Slicing `arr[1:4]` extracts indices 1, 2, 3 (upper bound is exclusive). Slicing creates a shallow copy ($O(K)$ time and memory).
* **Mutable Default Arguments Trap**:
```python
# TRAP: Mutable default list persists across multiple function invocations!
def append_to(element, target_list=[]):
    target_list.append(element)
    return target_list

assert append_to(1) == [1]
assert append_to(2) == [1, 2]  # Unintended mutation side effect!

# CORRECT PATTERN:
def append_to_safe(element, target_list=None):
    if target_list is None:
        target_list = []
    target_list.append(element)
    return target_list

assert append_to_safe(1) == [1]
assert append_to_safe(2) == [2]
```

---

### 3.2 High-Yield Python Algorithmic Patterns

#### Pattern 1: Frequency Counting & Duplicate Detection
```python
def count_frequencies(items: list) -> dict:
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq

assert count_frequencies(['a', 'b', 'a', 'c']) == {'a': 2, 'b': 1, 'c': 1}
```

#### Pattern 2: Two-Sum (Complement Lookup in $O(N)$)
```python
def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    seen = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], idx)
        seen[num] = idx
    return None

assert two_sum([2, 7, 11, 15], 9) == (0, 1)
assert two_sum([3, 2, 4], 6) == (1, 2)
assert two_sum([3, 3], 6) == (0, 1)
assert two_sum([1, 2], 5) is None
```

#### Pattern 3: Second-Largest Distinct Element
```python
def second_largest_distinct(nums: list[int]) -> int | None:
    first = second = None
    for x in nums:
        if first is None or x > first:
            second = first
            first = x
        elif x != first and (second is None or x > second):
            second = x
    return second

assert second_largest_distinct([10, 20, 20, 5, 8]) == 10
assert second_largest_distinct([5, 5, 5]) is None
assert second_largest_distinct([]) is None
assert second_largest_distinct([-10, -5, -20]) == -10
```

#### Pattern 4: Sliding Window (Dynamic Active Window)
```python
def longest_window_with_one_flip(events: str) -> int:
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

assert longest_window_with_one_flip("110110111") == 6
assert longest_window_with_one_flip("11111") == 5
assert longest_window_with_one_flip("0000") == 1
assert longest_window_with_one_flip("") == 0
```

---

### 3.3 Big-O Complexity Quick Reference

| Big-O Notation | Name | Typical Example Operations | Scalability (N=10,000) |
| :--- | :--- | :--- | :--- |
| **$O(1)$** | Constant | Hash map lookup, array index access, stack push/pop | Instant ($\approx 1\text{ op}$) |
| **$O(\log N)$** | Logarithmic | Binary search in sorted array, balanced BST search | Fast ($\approx 14\text{ ops}$) |
| **$O(N)$** | Linear | Single loop, array scan, frequency count | Fast ($\approx 10^4\text{ ops}$) |
| **$O(N \log N)$** | Linearithmic | Efficient sorting (`Timsort`, Merge Sort, Heap Sort) | Feasible ($\approx 1.4 \times 10^5\text{ ops}$) |
| **$O(N^2)$** | Quadratic | Nested loops, Bubble/Insertion Sort, pairwise checks | Dangerous ($\approx 10^8\text{ ops}$ — TLE risk!) |

---

## 4. Section B: SQL and Relational Databases (Priority 1)

### 4.1 Logical Query Execution Order
Remember this exact conceptual sequence:
$$\text{FROM} \longrightarrow \text{JOIN} \longrightarrow \text{WHERE} \longrightarrow \text{GROUP BY} \longrightarrow \text{HAVING} \longrightarrow \text{SELECT} \longrightarrow \text{DISTINCT} \longrightarrow \text{ORDER BY} \longrightarrow \text{LIMIT}$$

*Consequence*: You **cannot** use a column alias created in `SELECT` within a `WHERE` or `GROUP BY` clause.

---

### 4.2 Essential SQL Query Patterns

#### 1. Second-Highest Salary
```sql
-- Standard Window Function Approach:
WITH ranked_salaries AS (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employees
)
SELECT salary AS second_highest_salary
FROM ranked_salaries
WHERE rnk = 2
LIMIT 1;

-- Subquery Approach (Fallback for older engines):
SELECT MAX(salary) AS second_highest_salary
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);
```

#### 2. Top-N Records per Category (e.g., Top 2 Highest Value Projects per Department)
```sql
WITH ranked_projects AS (
    SELECT 
        dept_id,
        project_name,
        budget,
        ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY budget DESC) AS rnk
    FROM projects
)
SELECT dept_id, project_name, budget
FROM ranked_projects
WHERE rnk <= 2;
```

#### 3. Window Functions: `ROW_NUMBER()` vs `RANK()` vs `DENSE_RANK()`
Given salaries: `[1000, 1000, 800]`:
* `ROW_NUMBER()`: Assigns sequential integers without ties: `[1, 2, 3]`.
* `RANK()`: Assigns same rank to ties, skips subsequent rank: `[1, 1, 3]`.
* `DENSE_RANK()`: Assigns same rank to ties, does **not** skip: `[1, 1, 2]`.

#### 4. Cumulative Running Total & Moving Average
```sql
SELECT 
    client_id,
    expense_date,
    amount,
    -- Running Total:
    SUM(amount) OVER (
        PARTITION BY client_id 
        ORDER BY expense_date ASC 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total_spend,
    -- 7-Day Moving Average:
    AVG(amount) OVER (
        PARTITION BY client_id 
        ORDER BY expense_date ASC 
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS moving_avg_7d
FROM client_expenses;
```

---

### 4.3 SQL Mistakes to Avoid

1. **`WHERE` vs `HAVING` Misplacement**:
   * *Mistake*: `WHERE COUNT(*) > 5` (Fails! Aggregates cannot appear in `WHERE`).
   * *Correction*: Put row filters in `WHERE` and aggregate filters in `HAVING`.
2. **`COUNT(*)` vs `COUNT(column)`**:
   * `COUNT(*)` counts every row in the table, including rows containing `NULL` values.
   * `COUNT(column)` counts only rows where `column` is strictly `NOT NULL`.
3. **The `NULL` Comparison Trap**:
   * *Mistake*: `WHERE status = NULL` or `WHERE status != NULL` (Always evaluates to `UNKNOWN`/no rows returned!).
   * *Correction*: Always use `WHERE status IS NULL` or `WHERE status IS NOT NULL`.
4. **Join Fanout / Multiplication Trap**:
   * Joining Table A (1 row) to Table B (3 matching rows) causes Table A's monetary values to appear 3 times. If you run `SUM(A.amount)`, it triples the true total!
   * *Remedy*: Pre-aggregate Table B in a CTE before joining to Table A.
5. **Filtering the Right Table After `LEFT JOIN`**:
   * *Mistake*: `SELECT ... FROM A LEFT JOIN B ON A.id = B.a_id WHERE B.status = 'ACTIVE'`.
   * *Why it breaks*: The `WHERE` clause filters out rows where `B.status IS NULL`, inadvertently converting your `LEFT JOIN` into an `INNER JOIN`!
   * *Correction*: Move the filter into the `ON` clause: `ON A.id = B.a_id AND B.status = 'ACTIVE'`.

---

## 5. Section C: Quantitative Aptitude and Logical Reasoning (Priority 1)

### 5.1 Percentages, Margins & Growth Rates

* **Percentage Change vs Percentage-Point Change**:
  * If a website conversion rate increases from 4.0% to 5.0%:
    * **Percentage-Point Difference**: $5.0\% - 4.0\% = +1.0\text{ percentage point}$ (+100 bps).
    * **Relative Percentage Change**: $\frac{5.0 - 4.0}{4.0} \times 100\% = \frac{1.0}{4.0} \times 100\% = +25.0\%$.
* **Margin vs Markup**:
  $$\text{Gross Margin} = \frac{\text{Profit}}{\text{Revenue}} \times 100\% = \frac{P - C}{P} \times 100\%$$
  $$\text{Markup} = \frac{\text{Profit}}{\text{Cost}} \times 100\% = \frac{P - C}{C} \times 100\%$$
  *Conversion*: If Markup is 25.0% ($1/4$), Margin is $1 / (1 + 4) = 1/5 = 20.0\%$.
* **Successive Percentage Changes**:
  * An increase of $a\%$ followed by an increase of $b\%$ yields a net effective change of:
    $$\text{Net Change} = a + b + \frac{a \times b}{100}\%$$
  * *Example*: $+20\%$ followed by $+10\% = 20 + 10 + \frac{200}{100} = +32.0\%$ (NOT 30%!).
* **Break-Even Analysis**:
  $$\text{Unit Contribution Margin} = \text{Selling Price per unit } (P) - \text{Variable Cost per unit } (VC)$$
  $$\text{Break-Even Volume} = \frac{\text{Total Fixed Costs}}{\text{Unit Contribution Margin}} = \frac{FC}{P - VC}$$
  $$\text{Break-Even Revenue} = \text{Break-Even Volume} \times P$$
* **Compound Annual Growth Rate (CAGR) vs Rule of 72**:
  $$\text{Exact CAGR} = \left(\frac{V_{\text{final}}}{V_{\text{initial}}}\right)^{1/t} - 1$$
  $$\text{Rule of 72}: \text{Years to double} \approx \frac{72}{\text{Annual Growth Rate \%}}$$

---

### 5.2 Speed, Work & Probability

* **Average Speed for Round Trip (Harmonic Mean)**:
  * If a vehicle travels distance $D$ at speed $v_1 = 60\text{ km/h}$ and returns the same distance at $v_2 = 40\text{ km/h}$:
    $$\text{Average Speed} = \frac{2 \times v_1 \times v_2}{v_1 + v_2} = \frac{2 \times 60 \times 40}{60 + 40} = \frac{4800}{100} = 48.0\text{ km/h} \quad (\text{NOT } 50\text{ km/h}!)$$
* **Work-Rate Formula**:
  * If Worker A finishes a job in $T_A = 6\text{ hours}$ and Worker B finishes in $T_B = 3\text{ hours}$:
    $$\frac{1}{T_{\text{together}}} = \frac{1}{T_A} + \frac{1}{T_B} = \frac{1}{6} + \frac{1}{3} = \frac{3}{6} = \frac{1}{2} \implies T_{\text{together}} = 2.0\text{ hours}$$
* **Basic Probability Rules**:
  * Independent Events: $P(A \cap B) = P(A) \times P(B)$.
  * Mutually Exclusive: $P(A \cup B) = P(A) + P(B)$.
  * Complement Rule: $P(\text{at least one success in } n \text{ trials}) = 1 - P(\text{all failures})^n$.

---

## 6. Section D: Computer Science and IT Fundamentals (Priority 2)

### 6.1 Operating Systems & Architecture

* **Process vs Thread**:
  * **Process**: Isolated execution container. Own virtual memory space, file descriptors, and environment. IPC (Inter-Process Communication) required for sharing data. Context switch is heavyweight.
  * **Thread**: Lightweight execution unit within a process. Shares heap memory, address space, and global variables with sibling threads; has its own program counter and stack. Context switch is lightweight.
* **Stack vs Heap Memory**:
  * **Stack**: Fast, structured, contiguous memory managed automatically by CPU/compiler (LIFO). Stores local variables and function call frames. Fixed size (can trigger Stack Overflow).
  * **Heap**: Dynamic memory pool allocated at runtime (`malloc` / `new` / Python object creation). Slower allocation; requires manual deallocation or Garbage Collection (GC). Risk of memory leaks.
* **Deadlock (The 4 Necessary Coffman Conditions)**:
  Deadlock occurs if and only if all four conditions hold simultaneously:
  1. *Mutual Exclusion*: Resources cannot be shared simultaneously.
  2. *Hold and Wait*: Processes hold allocated resources while requesting new ones.
  3. *No Preemption*: Resources cannot be forcibly seized from a process.
  4. *Circular Wait*: A closed chain of processes exists where each waits for a resource held by the next.

---

### 6.2 Networking & REST APIs

* **TCP vs UDP**:
  * **TCP (Transmission Control Protocol)**: Connection-oriented (3-way handshake SYN $\rightarrow$ SYN-ACK $\rightarrow$ ACK), guaranteed delivery, in-order packets, flow control, congestion control. Used for HTTP/HTTPS, SSH, SQL.
  * **UDP (User Datagram Protocol)**: Connectionless, "fire-and-forget", no handshake, no delivery guarantee, minimal latency. Used for video streaming, VoIP, DNS, online gaming.
* **Common Ports & Protocols**:
  * Port 80: HTTP | Port 443: HTTPS | Port 22: SSH | Port 53: DNS | Port 3306: MySQL | Port 5432: PostgreSQL.
* **HTTP Methods & Idempotency**:
  * `GET`: Read resource (Safe, Idempotent).
  * `POST`: Create resource (Not Idempotent — calling twice creates 2 resources).
  * `PUT`: Replace resource completely (Idempotent — calling twice results in identical state).
  * `DELETE`: Remove resource (Idempotent).
* **Common HTTP Status Codes**:
  * `200 OK`, `201 Created`
  * `400 Bad Request` (Client syntax error)
  * `401 Unauthorized` (Authentication missing/invalid)
  * `403 Forbidden` (Authenticated, but insufficient permissions/authorization)
  * `404 Not Found`
  * `500 Internal Server Error`, `502 Bad Gateway`, `504 Gateway Timeout`

---

## 7. Section E: Cloud Computing and Digital Infrastructure (Priority 2)

### 7.1 Cloud Service Models

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                          CLOUD SHARED RESPONSIBILITY                        │
├───────────────────┬───────────────────┬───────────────────┬─────────────────┤
│ ON-PREMISES       │ IaaS (Infrastructure) PaaS (Platform) │ SaaS (Software) │
├───────────────────┼───────────────────┼───────────────────┼─────────────────┤
│ [Applications]    │ [Applications]    │ [Applications]    │ [Cloud Provider]│
│ [Data]            │ [Data]            │ [Data]            │ [Cloud Provider]│
│ [Runtime]         │ [Runtime]         │ [Cloud Provider]  │ [Cloud Provider]│
│ [Middleware]      │ [Middleware]      │ [Cloud Provider]  │ [Cloud Provider]│
│ [Operating System]│ [Operating System]│ [Cloud Provider]  │ [Cloud Provider]│
│ [Virtualization]  │ [Cloud Provider]  │ [Cloud Provider]  │ [Cloud Provider]│
│ [Servers/Storage] │ [Cloud Provider]  │ [Cloud Provider]  │ [Cloud Provider]│
│ [Networking]      │ [Cloud Provider]  │ [Cloud Provider]  │ [Cloud Provider]│
└───────────────────┴───────────────────┴───────────────────┴─────────────────┘
```

* **IaaS Examples**: AWS EC2, Azure Virtual Machines, Google Compute Engine.
* **PaaS Examples**: AWS Elastic Beanstalk, Azure App Service, Google App Engine, Heroku.
* **SaaS Examples**: Salesforce, Microsoft 365, Google Workspace, ServiceNow.

---

### 7.2 Core Architectural Distinctions

* **Scalability vs Elasticity**:
  * **Scalability**: The system's ability to handle growing workload by adding resources.
  * **Elasticity**: The ability to *dynamically* provision and de-provision resources in real-time to match fluctuating demand (e.g., auto-scaling down after peak hours to save money).
* **Horizontal Scaling (Scale Out) vs Vertical Scaling (Scale Up)**:
  * **Scale Out**: Adding more machine instances behind a load balancer. Higher fault tolerance, no downtime.
  * **Scale Up**: Adding more CPU, RAM, or SSD storage to a single server. Limited by hardware ceiling; requires downtime.
* **Virtual Machines vs Docker Containers**:
  * **VMs**: Virtualize physical hardware via Hypervisor. Each VM packages a full Guest Operating System (GBs in size, minutes to boot).
  * **Containers**: Virtualize at the OS kernel level. Share host OS kernel, package only application binaries and dependencies (MBs in size, seconds to boot).
* **Disaster Recovery Metrics**:
  * **RPO (Recovery Point Objective)**: Maximum acceptable age of data lost during a disaster (e.g., RPO = 15 mins means at most 15 minutes of transactional data loss).
  * **RTO (Recovery Time Objective)**: Maximum acceptable downtime duration to restore service availability.
* **High Availability SLA Downtime Budget**:
  * **99.9% ("Three Nines")**: $8.76\text{ hours/year}$ allowable downtime.
  * **99.99% ("Four Nines")**: $52.56\text{ minutes/year}$ allowable downtime.
  * **99.999% ("Five Nines")**: $5.26\text{ minutes/year}$ allowable downtime.

---

## 8. Section F: Cybersecurity Fundamentals (Priority 2)

* **Authentication vs Authorization**:
  * **Authentication (AuthN)**: Verifying *identity* ("Who are you?"). Verified via passwords, biometrics, hardware tokens, MFA.
  * **Authorization (AuthZ)**: Verifying *permissions* ("What are you allowed to access?"). Controlled via Role-Based Access Control (RBAC), Access Control Lists (ACLs).
* **Encryption vs Hashing vs Encoding**:
  * **Encryption**: Two-way reversible mathematical transformation using an encryption key. Protects data confidentiality (e.g., AES-256, RSA).
  * **Hashing**: One-way irreversible mathematical digest. Any tiny change in input completely scrambles the output hash (avalanche effect). Used for passwords and integrity checks (e.g., SHA-256, bcrypt).
  * **Encoding**: Reversible data format conversion without any secret key (e.g., Base64, ASCII, URL encoding). Provides **zero** security.
* **Symmetric vs Asymmetric Encryption**:
  * **Symmetric**: Single shared secret key for encryption and decryption (e.g., AES-GCM). Fast, used for bulk data at rest.
  * **Asymmetric**: Public key encrypts, private key decrypts (e.g., RSA, ECC). Slower, used for key exchange, TLS handshakes, and digital signatures.
* **Principle of Least Privilege**:
  * Every user, application, and service account must only be granted the minimum necessary permissions required to perform its designated task.

---

## 9. Section G: AI, Machine Learning, GenAI and LLMs (Priority 2)

### 9.1 Core ML Concepts & Classifications

* **AI Taxonomy**: Artificial Intelligence $\supset$ Machine Learning $\supset$ Deep Learning $\supset$ Generative AI.
* **Supervised vs Unsupervised Learning**:
  * **Supervised**: Labeled training data. Tasks: *Classification* (discrete classes: fraud vs non-fraud) and *Regression* (continuous values: forecasting revenue).
  * **Unsupervised**: Unlabeled data. Tasks: *Clustering* (customer segmentation via K-Means), *Dimensionality Reduction* (PCA).
* **Overfitting vs Underfitting**:
  * **Overfitting**: High training accuracy, poor test generalization (model memorized noise; high variance). Remediated by regularization, dropout, simpler models, more training data.
  * **Underfitting**: Poor training and test performance (model too simple to capture patterns; high bias). Remediated by increasing model complexity, feature engineering.

---

### 9.2 Classification Metrics & Confusion Matrix

$$\text{Precision} = \frac{TP}{TP + FP} \quad (\text{Of all predicted positives, how many were correct?})$$
$$\text{Recall (Sensitivity)} = \frac{TP}{TP + FN} \quad (\text{Of all actual positives, how many did we catch?})$$
$$\text{Specificity} = \frac{TN}{TN + FP} \quad (\text{Of all actual negatives, how many did we correctly identify?})$$
$$\text{F1-Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} \quad (\text{Harmonic mean of Precision and Recall})$$

* **The Accuracy Paradox (Class Imbalance)**:
  * In a medical test evaluating 1,000 patients where only 10 have a disease: A trivial "dumb" model that always predicts *Negative* achieves **99.0% accuracy** while having **0% Recall**! Accuracy is fundamentally misleading under severe class imbalance.

---

### 9.3 Generative AI & Enterprise RAG Architecture

* **LLM Core Concepts**:
  * **Tokens**: Sub-word text units ($\approx 0.75\text{ words}$ in English).
  * **Embeddings**: Dense high-dimensional vectors representing semantic meaning. Related concepts have high cosine similarity.
  * **Vector Database**: Optimized engine for approximate nearest neighbor (ANN) vector search (e.g., Pinecone, Milvus, Azure AI Search).
* **Enterprise RAG (Retrieval-Augmented Generation) Pipeline**:
  $$\text{User Query} \longrightarrow \text{Embedding Model} \longrightarrow \text{Vector Search (Retrieve Top-K Chunks)} \longrightarrow \text{Augment Context} \longrightarrow \text{LLM Output + Citations}$$
* **When to Prompt vs RAG vs Fine-Tune**:
  * **Prompt Engineering**: Best for quick prototyping, formatting, and general reasoning.
  * **RAG**: Best for enterprise dynamic knowledge, proprietary manuals, real-time updates, and eliminating hallucinations via exact document citations.
  * **Fine-Tuning**: Best for changing model tone/style, domain vocabulary, or specialized task formatting. Does **not** reliably inject new factual knowledge.

---

## 10. Section H: Digital Consulting and Business Problem-Solving (Priority 2)

### 10.1 The 8-Step Problem Solving Framework
1. **Clarify Objective**: Pinpoint the business goal, target KPI, and time horizon.
2. **Establish Baseline**: Quantify current performance (e.g., current defect rate = 12%).
3. **Deconstruct Root Causes**: Use MECE issue trees to isolate drivers (Internal vs External, Cost vs Revenue).
4. **Identify Stakeholders**: Align business users, IT operators, and executive sponsors.
5. **Architect Solutions**: Evaluate technology options vendor-agnostically (AWS vs Azure vs Custom vs SaaS).
6. **Quantify Financial Impact**: Compute CapEx, OpEx, net savings, payback period, and ROI.
7. **Mitigate Risks**: Address user adoption, cybersecurity, and data privacy.
8. **Synthesize with Pyramid Principle**: Lead with the answer, followed by 3 supporting pillars and a 3-phase implementation roadmap.

---

### 10.2 Worked Mini-Case: Enterprise Invoice Processing Automation

* **Client Context**: A Tokyo logistics enterprise manually processes 40,000 vendor invoices per month. Clerks take 12 minutes per invoice (cost = JPY 600 per invoice). Total manual cost = JPY 24M/month (JPY 288M/year). Error rate is 4.0%, causing JPY 30M in penalty fees.
* **Proposed Solution**: Deploy Cloud AI OCR + RPA automated ingestion into SAP ERP.
* **Financial Calculations (`[HYPOTHETICAL PRACTICE]`)**:
  * Automation rate: 85% of invoices processed without human touch.
  * Annual labor savings: $85\% \times \text{JPY } 288\text{M} = \text{JPY } 244.8\text{M/year}$.
  * Penalty reduction: 80% error reduction saves $80\% \times \text{JPY } 30\text{M} = \text{JPY } 24.0\text{M/year}$.
  * Gross Annual Savings = $\text{JPY } 268.8\text{M/year}$.
  * Implementation CapEx = JPY 80M. Annual Cloud SaaS OpEx = JPY 25M/year.
  * Net Annual Benefit = $\text{JPY } 268.8\text{M} - 25\text{M} = \text{JPY } 243.8\text{M/year}$.
  * **Payback Period**: $\frac{\text{JPY } 80\text{M}}{\text{JPY } 243.8\text{M}} \times 12\text{ months} \approx 3.9\text{ months}$.

---

## 11. Section I: Japan-Specific and Accenture Company Context (Priority 2)

* **Official Role Facts (`[JD VERIFIED]`)**:
  * **Role**: Digital Consultant (Analyst level entry).
  * **Location**: Tokyo Office affiliation (nationwide projects centered on Tokyo metropolitan area).
  * **Eligibility**: IIT Bachelor's degree or higher (earned or expected by June 2027); **zero** full-time post-bachelor experience.
  * **Tentative Joining**: December 2027.
* **Accenture's Technology-Agnostic Value Proposition (`[JD VERIFIED]`)**:
  * Unlike software vendors selling proprietary licenses, Accenture is strictly **technology-agnostic**. The mission is selecting the best-fit technology across AWS, Azure, GCP, SAP, Salesforce, or open-source to deliver measurable commercial value.
* **The 3 Career Progression Tracks (`[JD VERIFIED]`)**:
  1. *Business × Technology Path*: Upstream requirements, IT strategy, enterprise solution architecture.
  2. *Project Management Path*: Leading multidisciplinary transformation teams.
  3. *Technology Specialist Path*: Technical architecture mastery in Cloud, AI, Security, or Industry X.
* **Language & Cultural Philosophy (`[JD VERIFIED]`)**:
  * Japanese language is **not required at entry**, but **mandatory post-joining**.
  * Accenture sponsors comprehensive Japanese training (JPY 664,658 value). Candidates must demonstrate an open mindset toward learning and cross-cultural adaptability.
  * Cultural awareness: Respect for *Nemawashi* (informal consensus-building before formal decisions) and *Kaizen* (continuous incremental improvement).

---

## 12. Section J: Rapid Formula and Command Reference Sheet

### Mathematics & Economics Formulas
| Concept | Mathematical Formula | Key Variable Definitions & Notes |
| :--- | :--- | :--- |
| **Gross Margin** | $\frac{P - C}{P} \times 100\%$ | $P = \text{Price}, C = \text{Cost per unit}$. Margin is based on Revenue. |
| **Markup** | $\frac{P - C}{C} \times 100\%$ | Markup is based on Cost. |
| **Break-Even Units** | $\frac{FC}{P - VC}$ | $FC = \text{Fixed Costs}, VC = \text{Variable Cost per unit}$. |
| **CAGR** | $\left(\frac{V_f}{V_i}\right)^{1/t} - 1$ | $V_f = \text{Final Value}, V_i = \text{Initial Value}, t = \text{Years}$. |
| **Rule of 72** | $t_{\text{double}} \approx \frac{72}{g\%}$ | Mental approximation of doubling time at annual growth rate $g\%$. |
| **LTV** | $\frac{\text{ARPU} \times \text{Gross Margin}}{\text{Churn Rate}}$ | $\text{ARPU} = \text{Monthly Revenue per User}$. |
| **CAC Payback** | $\frac{\text{CAC}}{\text{Monthly Gross Contribution}}$ | Measures months to recover customer acquisition investment. |
| **OEE** | $\text{Availability} \times \text{Performance} \times \text{Quality}$ | Manufacturing effectiveness benchmark ($\ge 85\%$ is world-class). |
| **PUE** | $\frac{\text{Total Facility Energy}}{\text{IT Equipment Energy}}$ | Ideal PUE is 1.0; legacy data centers operate around 1.6–1.8. |

---

### SQL Command Snippets
| Task | SQL Syntax Template |
| :--- | :--- |
| **Safe Division** | `ROUND(conversions * 100.0 / NULLIF(impressions, 0), 2)` |
| **Null Fallback** | `COALESCE(primary_email, secondary_email, 'N/A')` |
| **Deduplication** | `WITH r AS (SELECT *, ROW_NUMBER() OVER(PARTITION BY email ORDER BY id) as rn FROM tbl) SELECT * FROM r WHERE rn=1;` |
| **Second Highest**| `WITH r AS (SELECT val, DENSE_RANK() OVER(ORDER BY val DESC) as rnk FROM t) SELECT val FROM r WHERE rnk=2 LIMIT 1;` |
| **Running Total** | `SUM(amount) OVER (PARTITION BY acct_id ORDER BY txn_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)` |
| **Moving Average**| `AVG(val) OVER (PARTITION BY node ORDER BY dt ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)` |

---

### Python Collection Operations
| Operation | Syntax Snippet | Time Complexity |
| :--- | :--- | :--- |
| **Dict Frequency** | `counts[x] = counts.get(x, 0) + 1` | $O(1)$ average |
| **Two-Sum Lookup** | `if (target - x) in seen: return (seen[target - x], i)` | $O(1)$ average |
| **Min-Heap Push** | `heapq.heappush(heap, val)` | $O(\log K)$ |
| **String Reverse** | `s[::-1]` | $O(N)$ |
| **Deque Queue** | `q = deque(); q.append(x); q.popleft()` | $O(1)$ |

---

## 13. Section K: Common Traps and MCQ Elimination Strategies

1. **MCQ Binary Elimination**:
   * In 4-option MCQs, two options are almost always conceptual opposites (e.g., "Increases latency" vs "Decreases latency"). The correct answer is usually one of these two.
   * Discard absolute extremes containing words like *"always"*, *"never"*, or *"guarantees zero failure"*. In cloud and AI systems, trade-offs always exist.
2. **Pseudocode Tracing Checks**:
   * Watch loop boundary conditions carefully: Does the loop run `for i = 0 to N-1` or `for i = 1 to N`?
   * Watch integer division truncation: `5 / 2` in C/Java/pseudocode truncates to `2`, whereas in Python `/` produces `2.5`.
3. **SQL NULL Evaluation**:
   * Any condition like `WHERE col = NULL` or `WHERE col != NULL` evaluates to `UNKNOWN` and returns 0 rows. Select the option with `IS NULL`.
4. **Weighted Average Traps**:
   * You cannot average percentages directly if sample sizes differ. If Group A has 100 users at 10% conversion and Group B has 900 users at 20% conversion:
     $$\text{Blended Rate} = \frac{(100 \times 0.10) + (900 \times 0.20)}{100 + 900} = \frac{10 + 180}{1000} = 19.0\% \quad (\text{NOT } 15.0\%!)$$

---

## 14. Section L: Self-Test Assessment (15 Questions)

Test your knowledge under time pressure. Attempt these 15 questions before looking at the answers in Section M.

#### Q1 (SQL): Which clause executes FIRST in logical SQL processing?
(A) `WHERE`  
(B) `SELECT`  
(C) `FROM`  
(D) `HAVING`  

#### Q2 (Python): What is the output of the following Python snippet?
```python
x = [1, 2, 3]
y = x
y.append(4)
print(len(x))
```
(A) 3  
(B) 4  
(C) `TypeError`  
(D) 1  

#### Q3 (Quantitative): A product's selling price is $120 and cost is $90. What are the Gross Margin and Markup percentages respectively?
(A) 25.0% margin, 33.3% markup  
(B) 33.3% margin, 25.0% markup  
(C) 25.0% margin, 25.0% markup  
(D) 30.0% margin, 33.3% markup  

#### Q4 (Operating Systems): Which of the following is SHARED between threads of the same process?
(A) Program counter  
(B) CPU registers  
(C) Stack memory  
(D) Heap memory  

#### Q5 (Cloud): A client requires a multi-tier web application where the cloud provider manages OS updates, runtime patching, and web server software, while the client maintains application code. Which cloud model is best?
(A) IaaS  
(B) PaaS  
(C) SaaS  
(D) Private On-Premise  

#### Q6 (SQL): Given table `salaries` with rows `[5000, 5000, 4000, 3000]`, what rank is assigned to salary 4000 by `DENSE_RANK() OVER (ORDER BY salary DESC)`?
(A) 1  
(B) 2  
(C) 3  
(D) 4  

#### Q7 (Cybersecurity): Which statement correctly distinguishes Encryption from Hashing?
(A) Encryption is one-way; Hashing is two-way.  
(B) Encryption requires a secret key to reverse; Hashing is an irreversible one-way digest.  
(C) Hashing can be decrypted using a private key.  
(D) Hashing and Encoding are identical.  

#### Q8 (AI / ML): In a rare fraud detection system where 1% of transactions are fraudulent, a model flags 90% of actual frauds correctly, but also raises false alarms on 5% of legitimate transactions. Why is Accuracy a poor metric to evaluate this model?
(A) Accuracy cannot be calculated on imbalanced data.  
(B) A naive baseline predicting all transactions as legitimate achieves 99% accuracy while catching zero frauds.  
(C) Accuracy only applies to regression problems.  
(D) Accuracy is always equal to Recall.  

#### Q9 (Quantitative): Machine A completes a job in 4 hours; Machine B completes it in 12 hours. Working together, how many hours will they take?
(A) 8.0 hours  
(B) 3.0 hours  
(C) 2.5 hours  
(D) 4.0 hours  

#### Q10 (Digital Consulting): An enterprise wants to migrate a mission-critical billing engine to the cloud. Which migration strategy involves moving applications without changing core code or architecture?
(A) Refactor / Re-architect  
(B) Rehost (Lift-and-Shift)  
(C) Repurchase (Drop-and-Shop)  
(D) Retire  

#### Q11 (Networking): What status code should a REST API return when a client makes a valid request but lacks authorization permissions to view that resource?
(A) `401 Unauthorized`  
(B) `403 Forbidden`  
(C) `404 Not Found`  
(D) `502 Bad Gateway`  

#### Q12 (Python): What is the time complexity of looking up a key in a standard Python dictionary with $N$ elements on average?
(A) $O(\log N)$  
(B) $O(1)$  
(C) $O(N)$  
(D) $O(N \log N)$  

#### Q13 (Quantitative): A retail website conversion rate increases from 2.0% to 2.5%. What is the percentage-point increase and relative percentage increase?
(A) 0.5 percentage points, 20.0% relative increase  
(B) 0.5 percentage points, 25.0% relative increase  
(C) 1.0 percentage points, 25.0% relative increase  
(D) 0.5 percentage points, 50.0% relative increase  

#### Q14 (AI / GenAI): Which approach is best for an enterprise seeking to let employees query internal proprietary HR policy PDFs with exact clause citations while preventing hallucinations?
(A) Training a custom Foundation Model from scratch  
(B) Fine-tuning an open-source LLM on the PDFs  
(C) Retrieval-Augmented Generation (RAG) with a Vector Database  
(D) Increasing the LLM temperature parameter  

#### Q15 (Accenture Company Fit): Which of the following statements about Accenture Japan's Digital Consultant role is confirmed by the official JD?
(A) Japanese proficiency at JLPT N1 level is strictly mandatory before receiving an offer.  
(B) Accenture is proprietary software vendor-locked to AWS.  
(C) Japanese is not required at the time of entry, but is required post-joining, supported by sponsored language training.  
(D) Candidates with 3 years of post-bachelor software engineering experience are preferred.  

---

## 15. Section M: Comprehensive Answer Key and Explanations

#### Q1: (C) `FROM`
* **Explanation**: Logical query processing starts with `FROM` (identifying data sources and joins), followed by `WHERE`, `GROUP BY`, `HAVING`, `SELECT`, `ORDER BY`, and `LIMIT`.

#### Q2: (B) 4
* **Explanation**: In Python, list assignment `y = x` copies the object reference, not the underlying array. Both `x` and `y` point to the identical list in memory. Appending to `y` modifies `x`, making `len(x) == 4`. To create an independent copy, use `y = x.copy()` or `y = list(x)`.

#### Q3: (A) 25.0% margin, 33.3% markup
* **Explanation**: $\text{Profit} = 120 - 90 = \$30$.  
  $\text{Margin} = \frac{30}{120} \times 100\% = 25.0\%$.  
  $\text{Markup} = \frac{30}{90} \times 100\% = 33.33\% \approx 33.3\%$.

#### Q4: (D) Heap memory
* **Explanation**: Threads share their parent process's global heap memory, address space, and open files. However, each thread maintains its own independent stack memory, program counter, and CPU register state.

#### Q5: (B) PaaS
* **Explanation**: In Platform as a Service (PaaS), the cloud provider manages infrastructure, operating systems, and runtime platforms, while the customer focuses strictly on deploying application code. In IaaS, the customer must manage OS patching.

#### Q6: (B) 2
* **Explanation**: Both 5000 salaries receive rank 1. Because `DENSE_RANK()` does not skip rank values after ties, the next distinct salary (4000) receives rank 2. (If `RANK()` were used, 4000 would receive rank 3).

#### Q7: (B) Encryption requires a secret key to reverse; Hashing is an irreversible one-way digest.
* **Explanation**: Encryption protects confidentiality and can be decrypted with the appropriate key. Hashing transforms input into a fixed-length mathematical digest that cannot be decrypted.

#### Q8: (B) A naive baseline predicting all transactions as legitimate achieves 99% accuracy while catching zero frauds.
* **Explanation**: When class distributions are skewed (1% positive), overall accuracy is dominated by true negatives. A useless model predicting all negatives scores 99% accuracy. Precision, Recall, and F1-Score are required.

#### Q9: (B) 3.0 hours
* **Explanation**: Machine A rate = $1/4$; Machine B rate = $1/12$. Combined rate = $\frac{1}{4} + \frac{1}{12} = \frac{3}{12} + \frac{1}{12} = \frac{4}{12} = \frac{1}{3}\text{ job/hour}$. Total time = $\frac{1}{1/3} = 3.0\text{ hours}$.

#### Q10: (B) Rehost (Lift-and-Shift)
* **Explanation**: Rehost copies physical or virtual servers to the cloud without making changes to core software architecture. Refactoring involves redesigning the application to be cloud-native.

#### Q11: (B) `403 Forbidden`
* **Explanation**: `401 Unauthorized` means the client identity has not been authenticated. `403 Forbidden` means identity is confirmed, but access rights are denied.

#### Q12: (B) $O(1)$
* **Explanation**: Python dictionaries use hash tables, providing average $O(1)$ time complexity for key lookups, insertions, and deletions.

#### Q13: (B) 0.5 percentage points, 25.0% relative increase
* **Explanation**: Percentage point increase: $2.5 - 2.0 = +0.5\text{ pp}$. Relative increase: $\frac{2.5 - 2.0}{2.0} \times 100\% = \frac{0.5}{2.0} \times 100\% = +25.0\%$.

#### Q14: (C) Retrieval-Augmented Generation (RAG) with a Vector Database
* **Explanation**: RAG retrieves exact relevant policy chunks from a vector database and provides them as context to the LLM, enabling verbatim clause citations with page numbers and avoiding hallucination.

#### Q15: (C) Japanese is not required at the time of entry, but is required post-joining, supported by sponsored language training.
* **Explanation**: Directly confirmed in the official Job Description (`[JD VERIFIED]`). English must be native level; Japanese is taught post-hiring (JPY 664,658 sponsored training). Candidates with post-bachelor full-time work experience are strictly ineligible.

---

## 16. Section N: Final 5-Minute Pre-Test Checklist

- [ ] Testing environment verified (stable webcam, reliable internet, quiet room).
- [ ] Scratchpad and pen ready for tracing pseudocode loops and computing mental math.
- [ ] Memorized the difference: Margin (over Revenue) vs Markup (over Cost).
- [ ] Remembered SQL clause order: `FROM` $\rightarrow$ `WHERE` $\rightarrow$ `GROUP BY` $\rightarrow$ `HAVING` $\rightarrow$ `SELECT` $\rightarrow$ `ORDER BY`.
- [ ] Checked for zero division (`NULLIF(val, 0)`) and NULL checks (`IS NULL`).
- [ ] Kept time discipline: Flag difficult MCQs and move forward; never get trapped on a single question.
