# 60-Minute Diagnostic Test 1 (30 Questions)

**Target Role:** Data Scientist / Associate Data Scientist | Tredence Analytics  
**Context:** IIT Kanpur Placement Season 2026–27  
**Time Limit:** 60 Minutes | **Total Score:** 30 Marks

---

### Questions

#### Part A: Quantitative Aptitude & Probability (Q1–Q6)
**Q1.** A box contains 5 red balls and 3 green balls. Two balls are drawn at random without replacement. What is the probability that both balls are red?  
(A) 5/14  
(B) 25/64  
(C) 5/28  
(D) 15/56  

**Q2.** An engine component has an exponential lifetime distribution with mean $\mu = 100$ hours. What is the probability that it survives beyond 200 hours?  
(A) $e^{-1}$  
(B) $e^{-2}$  
(C) $1 - e^{-2}$  
(D) $0.5$  

**Q3.** In how many distinct ways can the letters of the word `ANALYTICS` be arranged?  
(A) 362,880  
(B) 181,440  
(C) 90,720  
(D) 45,360  

**Q4.** A shopkeeper marks up an item by 40% and then offers a 20% discount. What is the net profit percentage?  
(A) 20%  
(B) 12%  
(C) 16%  
(D) 8%  

**Q5.** A bag contains 4 fair coins and 1 two-headed coin. A coin is picked at random and flipped; it shows Heads. What is the posterior probability that the chosen coin was the two-headed coin?  
(A) 1/5  
(B) 1/3  
(C) 2/5  
(D) 1/2  

**Q6.** The mean of 50 numbers is 38. If two numbers, namely 45 and 55, are discarded, what is the mean of the remaining numbers?  
(A) 36.5  
(B) 37.5  
(C) 37.0  
(D) 38.0  

---

#### Part B: Core Python & Algorithmic Foundations (Q7–Q12)
**Q7.** What is the output of the following Python snippet?
```python
def append_val(val, lst=[]):
    lst.append(val)
    return lst

print(append_val(1), append_val(2))
```
(A) `[1] [2]`  
(B) `[1, 2] [1, 2]`  
(C) `[1] [1, 2]`  
(D) `TypeError`  

**Q8.** What is the time complexity of checking membership in a standard Python `set` vs a `list` of size $N$?  
(A) $\mathcal{O}(1)$ for both  
(B) $\mathcal{O}(N)$ for set, $\mathcal{O}(1)$ for list  
(C) $\mathcal{O}(1)$ average for set, $\mathcal{O}(N)$ for list  
(D) $\mathcal{O}(\log N)$ for set, $\mathcal{O}(N)$ for list  

**Q9.** What does the following expression return?
```python
import numpy as np
a = np.array([1, 2, 3])
b = np.array([[10], [20]])
print((a + b).shape)
```
(A) `(3, 2)`  
(B) `(2, 3)`  
(C) `ValueError: operands could not be broadcast`  
(D) `(6,)`  

**Q10.** Which method modifies a Pandas DataFrame in-place without generating a copy in memory?  
(A) `df.reset_index(inplace=True)`  
(B) `df = df.dropna()`  
(C) `df.assign(new_col=1)`  
(D) `df.loc[:, 'a'] = df['a'] * 2` (direct column assignment)  

**Q11.** What is the output of `bool([]) or bool([0])`?  
(A) `False`  
(B) `True`  
(C) `[0]`  
(D) `None`  

**Q12.** In Scikit-Learn, what is the crucial methodological error in this code?
```python
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)
```
(A) Scaling before splitting leaks test set distribution statistics into training.  
(B) StandardScaler cannot handle continuous features.  
(C) Train-test split should only be applied to `y`.  
(D) `fit_transform` can only be called on `y`.  

---

#### Part C: SQL & Relational Analytics (Q13–Q18)
**Q13.** Which clause in SQL is evaluated FIRST during query execution?  
(A) `SELECT`  
(B) `WHERE`  
(C) `FROM`  
(D) `GROUP BY`  

**Q14.** What is the difference between `RANK()` and `DENSE_RANK()` when ranking scores $[100, 90, 90, 80]$?  
(A) `RANK`: 1, 2, 2, 4; `DENSE_RANK`: 1, 2, 2, 3  
(B) `RANK`: 1, 2, 3, 4; `DENSE_RANK`: 1, 2, 2, 3  
(C) `RANK`: 1, 2, 2, 3; `DENSE_RANK`: 1, 2, 2, 4  
(D) Both produce identical rankings  

**Q15.** What is the result of the expression `SELECT NULL = NULL;` in standard ANSI SQL?  
(A) `TRUE`  
(B) `FALSE`  
(C) `UNKNOWN` (evaluates as falsy/null)  
(D) `SyntaxError`  

**Q16.** Which window frame specification computes a rolling 3-day sum including the current day and previous 2 days ordered by transaction date?  
(A) `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW`  
(B) `ROWS BETWEEN CURRENT ROW AND 2 FOLLOWING`  
(C) `RANGE BETWEEN 3 PRECEDING AND CURRENT ROW`  
(D) `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`  

**Q17.** How does a `LEFT JOIN` handle rows from the right table that do not match the join predicate?  
(A) Excludes them from the output  
(B) Populates right table columns with `NULL`  
(C) Throws a runtime constraint exception  
(D) Repeats the last matching row  

**Q18.** To filter aggregated groups (e.g., keep departments where `COUNT(*) > 5`), which clause MUST be used?  
(A) `WHERE`  
(B) `HAVING`  
(C) `QUALIFY`  
(D) `FILTER`  

---

#### Part D: Statistics, Hypothesis Testing & Experimentation (Q19–Q24)
**Q19.** Which theorem guarantees that the distribution of the sample mean approaches normal as sample size increases, regardless of the underlying population distribution?  
(A) Law of Total Probability  
(B) Central Limit Theorem  
(C) Gauss-Markov Theorem  
(D) Bayes' Theorem  

**Q20.** In an A/B test, committing a Type I error ($\alpha$) means:  
(A) Failing to reject $H_0$ when a real effect exists  
(B) Rejecting $H_0$ when there is no true difference (False Alarm)  
(C) Getting an unequal sample size across variants  
(D) Miscalculating the test power  

**Q21.** If an intended 50:50 A/B test registers 45,000 visitors in Control and 55,000 in Treatment ($N = 100,000$), what must the data scientist do?  
(A) Proceed normally; t-tests adjust for unequal sample size  
(B) Downsample the Treatment group randomly to 45,000  
(C) Invalidate the test immediately due to Sample Ratio Mismatch (SRM)  
(D) Apply Bonferroni correction  

**Q22.** What is the primary purpose of CUPED in experimentation?  
(A) To eliminate Type II errors completely  
(B) To reduce metric variance using pre-experiment covariates, reducing required sample size  
(C) To automate multivariate testing  
(D) To eliminate the need for an A/B test control group  

**Q23.** Which statistical test is appropriate for comparing customer retention rates across 4 different marketing campaigns?  
(A) Paired t-test  
(B) $\chi^2$ (Chi-Square) Test of Independence  
(C) One-sample z-test  
(D) Mann-Whitney U test  

**Q24.** When testing 20 metrics simultaneously at $\alpha = 0.05$, the Bonferroni-adjusted significance threshold is:  
(A) 0.05  
(B) 0.01  
(C) 0.0025  
(D) 0.001  

---

#### Part E: Machine Learning & GenAI (Q25–Q30)
**Q25.** Which ensemble technique trains base models sequentially on the errors of previous models?  
(A) Bagging  
(B) Boosting  
(C) Stacking  
(D) Blending  

**Q26.** Why is PR-AUC preferred over ROC-AUC for fraud detection where fraud prevalence is 0.1%?  
(A) ROC-AUC cannot be calculated for binary targets  
(B) High volume of True Negatives artificially depresses FPR, making ROC-AUC deceptively high  
(C) PR-AUC is faster to compute  
(D) ROC-AUC requires equal class balance  

**Q27.** In LightGBM, what is the primary role of GOSS (Gradient-based One-Side Sampling)?  
(A) Automatically prune deep trees  
(B) Retain all instances with large gradients and sample from instances with small gradients  
(C) Convert categorical variables into one-hot vectors  
(D) Quantize weights to 8-bit integers  

**Q28.** What do Shapley values (SHAP) provide that standard GBDT feature gain does not?  
(A) Faster inference speed  
(B) Exact, theoretically grounded local and global additive feature attributions  
(C) Automatic hyperparameter optimization  
(D) Elimination of the need for validation splits  

**Q29.** In Low-Rank Adaptation (LoRA), how are matrices $\mathbf{B}$ and $\mathbf{A}$ initialized?  
(A) Both initialized to zeros  
(B) $\mathbf{B}$ to zeros, $\mathbf{A}$ to Gaussian random noise  
(C) Both initialized to Gaussian noise  
(D) Both initialized to identity matrices  

**Q30.** What does "Faithfulness" evaluate in the RAG Triad framework?  
(A) Whether the retrieved context is relevant to the query  
(B) Whether the user's question was polite  
(C) Whether claims in the generated response are factually grounded in the retrieved context  
(D) Whether the LLM latency was under 500 ms  

---

### Answer Key & Solutions

| Q | Key | Core Concept & Solution |
|---|:---:|---|
| **1** | **A** | $P = \frac{5}{8} \times \frac{4}{7} = \frac{20}{56} = \frac{5}{14}$. |
| **2** | **B** | Exponential survival $P(X > t) = e^{-\lambda t}$. $\lambda = 1/100$. $P(X > 200) = e^{-200/100} = e^{-2}$. |
| **3** | **B** | Word `ANALYTICS` has 9 letters with A appearing 2 times. $\frac{9!}{2!} = \frac{362880}{2} = 181,440$. |
| **4** | **B** | Marked price $= 1.40 \times \text{CP}$. Selling price $= 1.40 \times 0.80 \times \text{CP} = 1.12 \times \text{CP} \implies 12\%$ profit. |
| **5** | **B** | $P(2H \mid H) = \frac{1 \times 0.2}{(1 \times 0.2) + (0.5 \times 0.8)} = \frac{0.2}{0.2 + 0.4} = \frac{0.2}{0.6} = \frac{1}{3}$. |
| **6** | **B** | Initial sum $= 50 \times 38 = 1900$. Discarded sum $= 100$. New sum $= 1800$. New mean $= \frac{1800}{48} = 37.5$. |
| **7** | **B** | Mutable default arguments are evaluated once at function definition; both calls share the same list: `[1, 2]`. |
| **8** | **C** | Set lookup is $\mathcal{O}(1)$ average (hash table); list lookup is $\mathcal{O}(N)$ linear scan. |
| **9** | **B** | `(3,)` broadcasts with `(2, 1)` to produce `(2, 3)`. |
| **10** | **D** | Direct slice/column assignment writes directly into existing memory buffers. |
| **11** | **B** | `bool([])` is `False`. `bool([0])` is `True` because non-empty lists are truthy. `False or True` is `True`. |
| **12** | **A** | Data leakage: preprocessing must be fit strictly on training data after splitting. |
| **13** | **C** | Logical SQL order starts with `FROM` / `JOIN` to identify data sources. |
| **14** | **A** | `RANK()` skips ranks after ties (1, 2, 2, 4); `DENSE_RANK()` does not skip ranks (1, 2, 2, 3). |
| **15** | **C** | `NULL` comparisons yield `UNKNOWN` (three-valued logic). |
| **16** | **A** | `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW` captures 3 rows in total. |
| **17** | **B** | Unmatched rows from right table appear with `NULL` in all right table attributes. |
| **18** | **B** | `HAVING` filters aggregated groups; `WHERE` filters individual raw rows before aggregation. |
| **19** | **B** | Central Limit Theorem states sample mean distribution converges to normal. |
| **20** | **B** | Type I error is false positive (rejecting true null). |
| **21** | **C** | $\chi^2 = 1000 \implies p \ll 0.001$. SRM indicates broken test integrity; test must be invalidated. |
| **22** | **B** | CUPED leverages pre-experiment correlation $\rho$ to reduce metric variance by factor $1 - \rho^2$. |
| **23** | **B** | Chi-Square test of independence evaluates proportions across multiple categorical categories. |
| **24** | **C** | $\alpha_{\text{adj}} = \frac{0.05}{20} = 0.0025$. |
| **25** | **B** | Boosting sequentially fits weak learners on previous pseudo-residuals. |
| **26** | **B** | Large TN count inflates ROC-AUC; PR-AUC directly assesses precision and recall on the minority class. |
| **27** | **B** | GOSS retains all large-gradient instances and subsamples small-gradient instances to speed up training. |
| **28** | **B** | SHAP satisfies game-theoretic axioms (Efficiency, Symmetry, Additivity) for exact local/global attribution. |
| **29** | **B** | $\mathbf{B}=0$ guarantees $\Delta\mathbf{W}=0$ at start of training; $\mathbf{A}\sim\mathcal{N}$ breaks symmetry. |
| **30** | **C** | Faithfulness measures factual consistency between the generated answer and retrieved context. |

---

### Score Diagnosis & Action Plan

- **Score $\ge 25/30$ (Advanced):** Strong conceptual and technical readiness. Focus on Mock 1 timed execution and practical case studies.
- **Score $18–24/30$ (Proficient):** Solid baseline. Review incorrect questions; focus on SQL window framing and GBDT mechanics.
- **Score $< 18/30$ (Needs Remediation):** Revisit Module 02 (Python/Pandas), Module 03 (SQL questions), and Module 04 (Statistics notes) before attempting the full-length mock.
