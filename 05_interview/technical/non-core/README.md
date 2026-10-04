# Non-Core Technical Interview Question Bank

> **Target Roles**: Software Engineer, Data Analyst, Business Analyst, Product Manager, Financial Analyst.  
> **Key Principle**: Technical interview questions belong in this execution layer; foundational domain concepts remain in `03_non_core/`.

---

## 1. Software Engineering & Programming

### Q1: "Explain the difference between mutable and immutable data types in Python, and how they behave as function arguments."
* **Answer**: Immutable types (`int`, `float`, `str`, `tuple`, `frozenset`) cannot be modified in place after creation; modifying them allocates a new object in memory. Mutable types (`list`, `dict`, `set`) can be updated in place. In Python, arguments are passed by **assignment (object reference)**. If a mutable object is passed and modified inside a function, the changes persist outside the function. Default arguments should never be mutable (e.g., `def fn(a=[])` is a common anti-pattern).

### Q2: "What is an index in a relational SQL database, and what are the trade-offs between B-Tree and Hash indexing?"
* **Answer**: An index is an auxiliary data structure that accelerates data retrieval queries without scanning every row in a table.
  * **B-Tree Index**: Self-balancing tree structure; optimal for equality searches, range queries (`BETWEEN`, `>`, `<`), and sorted ordering (`ORDER BY`).
  * **Hash Index**: Key-value hash map; provides $O(1)$ point lookups for exact equality (`=`), but cannot be used for range queries or partial matching.
  * **Trade-Off**: Indexes speed up `SELECT` read queries, but slow down write operations (`INSERT`, `UPDATE`, `DELETE`) due to index maintenance overhead.

---

## 2. Business Analytics & Data Science

### Q3: "What is the difference between Correlation and Causation, and how would you establish causality in a business scenario?"
* **Answer**: Correlation indicates a statistical association between two variables, whereas Causation proves that a change in variable $X$ directly produces a change in variable $Y$. Correlation can be spurious due to confounding variables (e.g., ice cream sales and drowning rates both correlate with summer temperature). To establish causality in business, run a randomized controlled trial (A/B testing) or use quasi-experimental methods (Difference-in-Differences, Instrumental Variables).

### Q4: "How do you handle severe class imbalance in a classification model?"
* **Answer**:
  1. **Evaluation Metrics**: Abandon Accuracy (which is misleading under imbalance); use Precision, Recall, F1-Score, and PR-AUC.
  2. **Data-Level Resampling**: Apply SMOTE (Synthetic Minority Over-sampling Technique) on the minority class or random under-sampling on the majority class.
  3. **Algorithm-Level Tuning**: Use cost-sensitive loss functions (`class_weight='balanced'` in Scikit-Learn/XGBoost) to heavily penalize false negatives on the minority class.

---

## 3. Product Management

### Q5: "If daily active users (DAU) on an e-commerce app drops by 10% overnight, how would you diagnose the problem?"
* **Answer (Structured Framework)**:
  1. **Data Verification**: Check whether the telemetry pipeline or logging service failed (rule out data tracking bugs).
  2. **Internal Factors**: Did the engineering team push a buggy app update? Did checkout or login fail? Was there an outage on iOS vs Android?
  3. **External Factors**: Was there a regional holiday, ISP/telecom outage, or aggressive marketing campaign by a major competitor?
  4. **Segmentation**: Break down the drop by Geography (cities), Platform (iOS vs Android vs Web), and User Cohort (New vs Power vs Dormant users).

---

## 4. Corporate Finance

### Q6: "Walk me through how a ₹100 increase in depreciation flows through the three financial statements (assuming 30% tax rate)."
* **Answer**:
  1. **Income Statement**: Operating expenses increase by ₹100 $\implies$ Pre-tax income decreases by ₹100. Tax decreases by ₹30 ($30\% \times 100$). Net income drops by **₹70**.
  2. **Cash Flow Statement**: Net income starts down ₹70. Depreciation is a non-cash expense, so it is added back (+₹100). Net cash flow from operations increases by **+₹30** (tax shield benefit).
  3. **Balance Sheet**: Cash is up by +₹30. Property, Plant & Equipment (PP&E) drops by -₹100 due to depreciation. Assets side is down by **-₹70**. Retained earnings on Liabilities & Equity side is down by **-₹70** (from Net Income). Both sides balance.
