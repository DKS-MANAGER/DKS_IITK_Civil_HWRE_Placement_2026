# Deloitte Analyst (AI, Analytics & Consulting) — Rapid Revision & Formula Cheatsheet

> **Target Role**: Analyst (AI, Analytics & Technology Consulting) — Deloitte US-India (Campus 2026)  
> **Purpose**: High-density, last-mile revision sheet designed for the final 24–48 hours before online assessments and technical/partner interviews.  
> **Coverage**: Core Aptitude Formulas, Python DSA Cheat Sheet, Essential SQL Window Templates, Inferential Statistics & ML Metrics, GenAI / RAG Architecture Reminders, ERP & Business Math, and Behavioral Traps.

---

## 1. High-Yield Quantitative & Commercial Math Formulas

### 1.1 Alligation & Weighted Averages
* **Cross-Rule of Alligation**:
  $$\frac{Q_{\text{cheaper}}}{Q_{\text{dearer}}} = \frac{P_{\text{dearer}} - P_{\text{mean}}}{P_{\text{mean}} - P_{\text{cheaper}}}$$
* **Blended Billing Rate**:
  $$\text{Blended Rate} = \frac{(H_{\text{onshore}} \times R_{\text{onshore}}) + (H_{\text{offshore}} \times R_{\text{offshore}})}{H_{\text{onshore}} + H_{\text{offshore}}}$$

### 1.2 Compounded Growth & Financial Math
* **CAGR (Compound Annual Growth Rate)**:
  $$\text{CAGR} = \left(\frac{V_{\text{final}}}{V_{\text{initial}}}\right)^{\frac{1}{n}} - 1$$
* **Rule of 72**: Years to double investment $\approx \frac{72}{\text{Annual Rate (\%)}}$.
* **Profit Margin vs. Markup**:
  $$\text{Margin} = \frac{\text{Profit}}{\text{Revenue}}, \quad \text{Markup} = \frac{\text{Profit}}{\text{Cost}}, \quad \text{Margin} = \frac{\text{Markup}}{1 + \text{Markup}}$$

### 1.3 Probability & Bayes' Theorem
* **Bayes' Theorem**:
  $$P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)} = \frac{P(B \mid A) \cdot P(A)}{P(B \mid A)P(A) + P(B \mid A^c)P(A^c)}$$
* **Independence Check**: $P(A \cap B) = P(A) \cdot P(B) \iff P(A \mid B) = P(A)$.
* **Base-Rate Fallacy Reminder**: When background disease/fraud prevalence $P(F)$ is tiny ($< 0.1\%$), even a $99\%$ accurate test yields a low posterior probability ($P(F \mid \text{Alert}) < 10\%$).

---

## 2. Python Programming & DSA Cheat Sheet

### 2.1 Big-O Complexity Quick Reference

| Data Structure / Operation | Access | Search | Insertion | Deletion |
| :--- | :--- | :--- | :--- | :--- |
| **Python List (`[]`)** | $O(1)$ | $O(N)$ | End: $O(1)$ amortized; Middle: $O(N)$ | $O(N)$ |
| **Python Dict (`{}`) / Set (`set()`)** | N/A | $O(1)$ avg | $O(1)$ avg | $O(1)$ avg |
| **`collections.deque`** | $O(N)$ | $O(N)$ | Both Ends: $O(1)$ | Both Ends: $O(1)$ |
| **`heapq` (Min-Heap)** | Min: $O(1)$ | $O(N)$ | Push: $O(\log N)$ | Pop-Min: $O(\log N)$ |

### 2.2 Top 5 Algorithmic Patterns (Python Idioms)

```python
# 1. Sliding Window (Maximum Sum Subarray of size k)
def max_sub_array_k(nums, k):
    w_sum = sum(nums[:k])
    max_s = w_sum
    for i in range(k, len(nums)):
        w_sum += nums[i] - nums[i - k]
        max_s = max(max_s, w_sum)
    return max_s

# 2. Two Pointers (Target Sum on Sorted Array)
def two_sum_sorted(nums, target):
    l, r = 0, len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s == target: return [l, r]
        elif s < target: l += 1
        else: r -= 1
    return []

# 3. Kadane's Algorithm (Max Subarray Sum in O(N))
def max_sub_array(nums):
    cur_sum = max_sum = nums[0]
    for x in nums[1:]:
        cur_sum = max(x, cur_sum + x)
        max_sum = max(max_sum, cur_sum)
    return max_sum

# 4. Monotonic Stack (Next Greater Element)
def next_greater(nums):
    res = [-1] * len(nums)
    stack = []  # stores indices
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            res[stack.pop()] = x
        stack.append(i)
    return res

# 5. Fast Grouping / Frequency Counter
from collections import Counter, defaultdict
freq = Counter(["apple", "banana", "apple"])  # Counter({'apple': 2, 'banana': 1})
```

---

## 3. Essential SQL Syntax Templates

### 3.1 Logical Execution Order
$$\text{FROM \& JOIN} \longrightarrow \text{WHERE} \longrightarrow \text{GROUP BY} \longrightarrow \text{HAVING} \longrightarrow \text{SELECT} \longrightarrow \text{ORDER BY} \longrightarrow \text{LIMIT}$$
*(Remember: Column aliases created in `SELECT` cannot be referenced in `WHERE` or `GROUP BY` in standard ANSI-SQL).*

### 3.2 Top 6 Production Window Query Patterns

```sql
-- 1. Nth Highest Value per Department (DENSE_RANK)
WITH Ranked AS (
    SELECT emp_id, dept_id, salary,
           DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rnk
    FROM employees
)
SELECT * FROM Ranked WHERE rnk = 2;

-- 2. Month-over-Month Growth with LAG
SELECT 
    TO_CHAR(txn_date, 'YYYY-MM') AS txn_month,
    SUM(amount) AS monthly_rev,
    ROUND(((SUM(amount) - LAG(SUM(amount)) OVER (ORDER BY TO_CHAR(txn_date, 'YYYY-MM'))) /
          LAG(SUM(amount)) OVER (ORDER BY TO_CHAR(txn_date, 'YYYY-MM'))) * 100.0, 2) AS mom_growth_pct
FROM transactions
GROUP BY TO_CHAR(txn_date, 'YYYY-MM');

-- 3. 7-Day Moving Average of Sales
SELECT 
    order_date,
    amount,
    AVG(amount) OVER (
        ORDER BY order_date 
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS mavg_7d
FROM daily_sales;

-- 4. Cumulative Running Total
SELECT 
    order_date,
    amount,
    SUM(amount) OVER (
        ORDER BY order_date 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_total
FROM daily_sales;

-- 5. Islands & Streaks (Consecutive Active Days)
WITH Grouped AS (
    SELECT user_id, active_date,
           active_date - (ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY active_date) * INTERVAL '1 day') AS island_id
    FROM user_logins
)
SELECT user_id, MIN(active_date) AS streak_start, MAX(active_date) AS streak_end, COUNT(*) AS streak_length
FROM Grouped
GROUP BY user_id, island_id
HAVING COUNT(*) >= 5;

-- 6. Eliminating Join Fan-Out Duplicates
SELECT o.order_id, o.total_amount, COUNT(DISTINCT i.item_id) AS items_count
FROM orders o
JOIN order_items i ON o.order_id = i.order_id
GROUP BY o.order_id, o.total_amount;
```

---

## 4. Statistics, Hypothesis Testing & Machine Learning Cheat Sheet

### 4.1 Inferential Statistics Formulas
* **Standard Error of Mean**: $\text{SE} = \frac{s}{\sqrt{n}}$.
* **Two-Sample Independent $Z$-Test for Proportions**:
  $$Z = \frac{\hat{p}_1 - \hat{p}_2}{\sqrt{\hat{p}(1 - \hat{p}) \left(\frac{1}{n_1} + \frac{1}{n_2}\right)}}, \quad \hat{p} = \frac{x_1 + x_2}{n_1 + n_2}$$
* **Chi-Square Test of Independence**:
  $$\chi^2 = \sum \frac{(O - E)^2}{E}, \quad E = \frac{\text{Row Total} \times \text{Column Total}}{\text{Grand Total}}, \quad df = (r-1)(c-1)$$
* **$p$-Value Definition**: Probability of observing a test statistic as extreme as, or more extreme than, the sample result, **assuming $H_0$ is strictly true**.

### 4.2 Machine Learning Classification Metrics

$$\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}} \quad (\text{Quality of alerts / avoid false alarms})$$

$$\text{Recall (Sensitivity)} = \frac{\text{TP}}{\text{TP} + \text{FN}} \quad (\text{Catch all true defects / fraud})$$

$$F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2\text{TP}}{2\text{TP} + \text{FP} + \text{FN}}$$

* **ROC-AUC vs. PR-AUC**:
  * Use **ROC-AUC** when classes are roughly balanced ($> 10\%$ minority class).
  * Use **PR-AUC** under extreme class imbalance ($< 1\%$ fraud/churn). ROC-AUC gives overly optimistic scores because FPR changes minimally under millions of true negatives.

### 4.3 Model Tuning & Diagnostics
* **L1 (Lasso)**: Adds $\lambda \sum |w_i|$ penalty. Drives non-informative weights strictly to **0.0** (embedded feature selection).
* **L2 (Ridge)**: Adds $\lambda \sum w_i^2$ penalty. Shrinks weights smoothly toward zero; handles multicollinearity.
* **Variance Inflation Factor (VIF)**: $\text{VIF}_j = \frac{1}{1 - R_j^2}$. Threshold: $\text{VIF} > 5$ indicates high multicollinearity; $\text{VIF} > 10$ is severe.
* **ADF Test (Stationarity)**: Test statistic must be **more negative than critical value** (e.g., $< -2.86$) to reject unit root ($H_0$) and confirm stationarity.

---

## 5. Generative AI, RAG & Agentic Systems Architecture

### 5.1 Self-Attention Core Equation
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V$$
* Scaling factor $\sqrt{d_k}$ prevents dot products from growing excessively large, which pushes softmax into regions with vanishing gradients.
* Computational complexity: $O(N^2)$ FLOPS and memory for sequence length $N$.

### 5.2 Enterprise RAG Pipeline (The 4 Pillars)
1. **Hybrid Search**: Combine BM25 (exact keyword match) + Dense Embedding (semantic search) via Reciprocal Rank Fusion:
   $$\text{RRF Score}(d) = \frac{1}{60 + \text{Rank}_{\text{BM25}}} + \frac{1}{60 + \text{Rank}_{\text{Dense}}}$$
2. **Cross-Encoder Reranker**: Rerank top 50 candidates into top 5 chunks before context stuffing.
3. **Prompt Hardening**: Always include negative constraints:
   > *"If the answer is not explicitly stated in the context, output: 'Insufficient verified data.' Do not extrapolate."*
4. **RAGAS Evaluation Triad**:
   * **Faithfulness**: Is the answer derived solely from retrieved chunks? (Zero hallucination)
   * **Context Precision**: Are the relevant chunks at the top of the retrieved list?
   * **Answer Relevance**: Does the generated answer address the user's prompt directly?

### 5.3 Agentic Systems (ReAct Loop)
$$\text{User Goal} \longrightarrow \text{Thought (Reasoning)} \longrightarrow \text{Action (Tool Call)} \longrightarrow \text{Observation (Output)} \longrightarrow \text{Repeat / Emit Answer}$$
* **Safeguards**: Hard iteration threshold (max 10 steps), sliding-window loop detection, and Human-in-the-Loop gates before financial write operations.

---

## 6. Enterprise ERP & Business Process Equations

### 6.1 Order-to-Cash (O2C) & Working Capital
* **Days Sales Outstanding (DSO)**:
  $$\text{DSO} = \frac{\text{Accounts Receivable}}{\text{Total Credit Sales}} \times 365$$
* **Cash Released from DSO Improvement**:
  $$\Delta \text{Cash} = \frac{\Delta \text{DSO}}{365} \times \text{Annual Credit Sales}$$
* **Cash Conversion Cycle (CCC)**:
  $$\text{CCC} = \text{DIO (Days Inventory)} + \text{DSO (Receivables)} - \text{DPO (Payables)}$$

### 6.2 Source-to-Pay (S2P) 3-Way Match
$$\text{Purchase Order (PO)} \longleftrightarrow \text{Goods Receipt (GR)} \longleftrightarrow \text{Vendor Invoice (INV)}$$
* Automated ERP check verifies:
  1. $\text{INV Unit Price} = \text{PO Unit Price}$
  2. $\text{INV Billed Quantity} \le \text{GR Physical Received Quantity}$
  3. Mismatch triggers **Automated Payment Block** in AP ledger.

---

## 7. Consulting Problem Solving & Behavioral Traps

### 7.1 MECE Issue Tree Deconstruction
* **Revenue Decline Case**:
  ```text
  Revenue = Price * Volume
    ├── Volume Decline?
    │     ├── Customer acquisition dropped (new logos)?
    │     └── Customer churn surged (existing logos)?
    └── Average Realized Price Decline?
          ├── Product mix shift toward cheaper SKUs?
          └── Heavy promotional discounts or sales price erosion?
  ```

### 7.2 The Minto Pyramid Principle
* Start with the **Answer / Recommendation First (Executive Summary)**.
* Group supporting rationale into 3 MECE categories.
* Provide data evidence, calculations, and risk mitigation underneath each pillar.

### 7.3 Top 5 Interview Traps & Pitfalls

| Potential Trap | What the Interviewer Is Really Testing | The Winning Candidate Response |
| :--- | :--- | :--- |
| **"Our model has 98% accuracy, can we deploy it?"** | Awareness of class imbalance and baseline prevalence. | *"Not until we inspect precision, recall, and PR-AUC. If fraud prevalence is 1%, a dummy model has 99% accuracy."* |
| **"Can we replace our entire human team with GenAI?"** | Practical enterprise realism vs. hype; risk governance. | *"Recommend a gated PoC: start with human-in-the-loop AI Agent-Assist, pilot on low-risk FAQs, evaluate before core automation."* |
| **"A stakeholder rejects your analysis findings."** | Empathy, stakeholder diplomacy, and data defense without defensiveness. | *"Validate their intuition; walk through telemetry records together; verify underlying assumptions collaboratively."* |
| **"Are you comfortable working US overlap hours / night shifts?"** | Professional flexibility and dedication in global client delivery. | *"Yes, 100%. I understand global client consulting requires delivery alignment. It also provides direct exposure to onshore leadership."* |
| **"Why Deloitte USI over pure-play software engineering?"** | Triad understanding: engineering + business process + client communication. | *"At Deloitte, technical depth directly solves enterprise business challenges, rather than building isolated features in a silo."* |
