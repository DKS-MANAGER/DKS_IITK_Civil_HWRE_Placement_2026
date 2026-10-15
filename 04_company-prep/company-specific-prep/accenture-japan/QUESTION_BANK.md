# Master Question Bank — Tagged Assessment & Interview Database

> **Document Status**: Comprehensive Question-and-Answer Knowledge Base  
> **Target Role**: Digital Consultant, Accenture Japan Ltd. (`[JD VERIFIED]`)  
> **Tagging Taxonomy**:  
> * `[JD VERIFIED]`: Directly supported by official Accenture Japan job description and recruitment documents.  
> * `[EXTERNAL VERIFIED]`: Supported by official vendor documentation (AWS, Azure, Python, ANSI SQL).  
> * `[PREPARATION INFERENCE]`: Standard interview questions mapped to required consulting competencies.  
> * `[HYPOTHETICAL PRACTICE]`: Illustrative practice cases and synthetic enterprise scenarios.

---

## 🏛️ Structure of the Question Bank

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                         MASTER QUESTION BANK MODULES                        │
├──────────────────────────────┬──────────────────────────────┬───────────────┤
│ PART 1: Coding & Algorithmic │ PART 2: SQL & Enterprise     │ PART 3: Cloud,│
│ Logic (Python)               │ Relational Databases         │ AI & Systems  │
├──────────────────────────────┴──────────────────────────────┴───────────────┤
│ PART 4: Manager Round Technical Project Defense & Mini DX Cases             │
├─────────────────────────────────────────────────────────────────────────────┤
│ PART 5: Director Round Strategic Vision, Culture Fit & Japan Readiness      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 💻 PART 1: Coding & Algorithmic Logic Questions

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

---

## 🗄️ PART 2: Relational SQL & Database Queries

### Q2.1: `WHERE` vs `HAVING` Clause Difference (`[EXTERNAL VERIFIED]`)
* **Definition**: `WHERE` filters individual table rows *prior* to grouping. `HAVING` filters aggregated group records *after* the `GROUP BY` clause has been executed.
* **Mechanics**:
  ```sql
  -- Correct: WHERE filters active status; HAVING filters high-count departments
  SELECT dept_id, COUNT(*) AS emp_count
  FROM employees
  WHERE status = 'ACTIVE'
  GROUP BY dept_id
  HAVING COUNT(*) >= 10;
  ```
* **Follow-up**: *"Can `HAVING` be used without a `GROUP BY` clause?"*  
  *Answer*: *"Yes. In ANSI SQL, `HAVING` without `GROUP BY` treats the entire table as a single aggregated group."*

---

### Q2.2: Second-Highest Salary Extraction (`[PREPARATION INFERENCE]`)
* **Question**: Write an ANSI SQL query to extract the second-highest employee salary, returning `NULL` if no second-highest salary exists.
* **Query Solution**:
  ```sql
  WITH ranked AS (
      SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
      FROM employees
  )
  SELECT salary AS second_highest_salary
  FROM ranked
  WHERE rnk = 2
  LIMIT 1;
  ```
* **Why `DENSE_RANK`?**: If two executives share the highest salary ($100,000, $100,000), `RANK()` would assign ranks 1, 1, 3 (skipping rank 2). `DENSE_RANK()` assigns 1, 1, 2, correctly identifying the next highest salary.

---

### Q2.3: Join Fanout & Row Multiplication (`[EXTERNAL VERIFIED]`)
* **Question**: Why does joining an `orders` table to a `payments` table sometimes inflate total revenue in financial reporting?
* **Explanation**: If an order has 3 installment payments, a standard `INNER JOIN` produces 3 rows for that single order. Running `SUM(o.order_amount)` sums the order amount 3 times.
* **Remedy**: Always pre-aggregate the child table in a Common Table Expression (CTE) to a 1-to-1 relationship before joining.

---

## ☁️ PART 3: Cloud, AI, Security & Architecture Concepts

### Q3.1: Technology-Agnostic Cloud Strategy (`[JD VERIFIED]`)
* **Question**: *"If a client asks whether to migrate to AWS or Azure, how should a Digital Consultant advise them?"*
* **Model Answer Framework**:
  1. **Affirm Technology Agnosticism**: State clearly that Accenture does not sell software licenses and has no proprietary bias.
  2. **Diagnostic Criteria**: Evaluate client context across:
     * *Existing Landscape*: Active Microsoft enterprise agreements (favouring Azure AD/Office 365 integration) vs Linux/open-source microservices (AWS/GCP).
     * *Regulatory Compliance*: Data sovereignty and FSA/FISC financial regulations in Tokyo and Osaka regions.
     * *Total Cost of Ownership (TCO)*: Reserved instances, hybrid licensing benefits (Azure Hybrid Benefit), and network egress costs.
  3. **Deliverable**: Present a structured multi-criteria decision matrix with risk mitigations.

---

### Q3.2: Enterprise RAG vs LLM Fine-Tuning (`[EXTERNAL VERIFIED]`)
* **Question**: Compare Retrieval-Augmented Generation (RAG) against Model Fine-Tuning for enterprise knowledge management.
* **Trade-off Comparison**:
  | Dimension | Retrieval-Augmented Generation (RAG) | Model Fine-Tuning |
  | :--- | :--- | :--- |
  | **Knowledge Freshness** | Real-time (instant vector DB insert) | Static (requires re-training) |
  | **Hallucination Risk** | Low (grounded with exact page citations) | High (model can invent facts confidently) |
  | **Access Control (RBAC)**| Native (vector filter on user credentials) | Difficult (all weights know all data) |
  | **Best Use Case** | Searching policy manuals, regulatory codes | Changing tone, style, or specific syntax |

---

### Q3.3: Authentication vs Authorization & Least Privilege (`[EXTERNAL VERIFIED]`)
* **Authentication (AuthN)** verifies identity ("Who are you?"), while **Authorization (AuthZ)** verifies access permissions ("What are you allowed to do?").
* **Principle of Least Privilege**: Users and applications are granted only the minimum necessary rights to perform their job, reducing the blast radius of compromised credentials.

---

## 👔 PART 4: Manager Round Interview Questions (Round 1)

### Q4.1: Technical Project Defense Walkthrough (`[PREPARATION INFERENCE]`)
* **Prompt**: *"Walk me through an engineering project from your IIT coursework or research. What was your technical ownership and quantifiable outcome?"*
* **Structured 4-Step Answer Framework (`[EXAMPLE TEMPLATE]`)**:
  1. *Context (30s)*: "In my final-year computational engineering project, our simulation took 4 hours per run, creating an experimental bottleneck."
  2. *Methodology (45s)*: "I took ownership of automating the pipeline using Python and parallelizing data processing."
  3. *Bottleneck Overcome (45s)*: "I profiled memory leaks, optimized vector queries, and eliminated redundant disk I/O."
  4. *Quantified Result (30s)*: "This reduced runtime by 65%, enabling 10x more sensitivity tests and improving model predictive accuracy by 14%."

---

### Q4.2: Mini DX Case: Manufacturing Machine Downtime (`[HYPOTHETICAL PRACTICE]`)
* **Prompt**: *"How would you digitize a Japanese manufacturing plant suffering 20% unscheduled machine breakdowns?"*
* **Answer Structure**:
  1. *Diagnose*: Retrofit critical spindle and welding machines with vibration and temperature sensors (Industry X).
  2. *Edge to Cloud*: Process high-frequency sensor streams at edge gateways to catch micro-anomalies in $<50\text{ ms}$; aggregate features to cloud data lake.
  3. *Predictive AI*: Run Remaining Useful Life (RUL) models to alert technicians 48 hours before component failure.
  4. *Business Impact*: Cuts downtime by 70%, boosting OEE from 72% to 85% with payback in $<7$ months.

---

## 🎯 PART 5: Director Round Interview Questions (Round 2)

### Q5.1: Why Digital Consulting Over Pure Software Engineering? (`[JD VERIFIED]`)
* **Model Answer Strategy (`[EXAMPLE TEMPLATE]`)**:
  > *"Software engineering focuses primarily on building specific software modules to specification. However, my passion lies at the intersection of enterprise business strategy and technology architecture — understanding the commercial bottleneck, selecting the best-fit technology vendor-agnostically, and driving end-to-end organizational transformation. Accenture Japan provides the premier platform in Tokyo to influence large-scale Japanese corporate transformation."*

---

### Q5.2: Japanese Language & Cultural Commitment (`[JD VERIFIED]`)
* **Prompt**: *"Japanese is not required at hire, but is mandatory post-joining (`[JD VERIFIED]`). How will you handle this linguistic and cultural transition?"*
* **Model Answer Strategy (`[EXAMPLE TEMPLATE]`)**:
  > *"I view learning Japanese as a foundational investment in building trust with Japanese colleagues and C-suite clients. I have already begun mastering Hiragana, Katakana, and basic conversational phrases. Supported by Accenture's sponsored JPY 664,658 training program, I will commit daily structured study hours to achieve conversational fluency before landing in Tokyo, and professional working fluency within my first 18 months."*
