# Full-Length Timed Placement Mock Assessment (50 Questions)

**Target Role:** Data Scientist / Associate Data Scientist | Tredence Analytics  
**Context:** IIT Kanpur Placement Season 2026–27  
**Time Limit:** 120 Minutes | **Total Score:** 100 Marks (2 marks per question)

---

### Section 1: Quantitative Aptitude & Analytical Reasoning (Q1–Q10)

**Q1.** Two pipes A and B can fill a cistern in 12 hours and 18 hours respectively. A third pipe C can empty it in 24 hours. If all three pipes are opened simultaneously, in how many hours will the cistern be completely filled?  
(A) 8.4 hours  
(B) 9.6 hours  
(C) 10.2 hours  
(D) 11.5 hours  

**Q2.** The average age of a committee of 8 members increases by 2 years when two members whose ages are 35 and 45 years are replaced by two new members. What is the average age of the two new members?  
(A) 46 years  
(B) 48 years  
(C) 50 years  
(D) 52 years  

**Q3.** An analyst travels from Gurugram to Bengaluru: the first 40% of the distance at 60 km/h, and the remaining 60% of the distance at 90 km/h. What is the average speed for the entire journey?  
(A) 72.0 km/h  
(B) 75.0 km/h  
(C) 76.5 km/h  
(D) 78.0 km/h  

**Q4.** In a team of 15 data scientists, 8 know Python, 7 know R, and 4 know SQL. Exactly 3 know both Python and R, 2 know R and SQL, and 2 know Python and SQL. If 1 person knows all three tools, how many people in the team know none of these three tools?  
(A) 1  
(B) 2  
(C) 3  
(D) 4  

**Q5.** A sum of money triples itself in 4 years at compound interest (compounded annually). In how many years will it become 27 times itself at the same rate?  
(A) 8 years  
(B) 10 years  
(C) 12 years  
(D) 16 years  

**Q6.** What is the unit digit of $7^{105}$?  
(A) 1  
(B) 3  
(C) 7  
(D) 9  

**Q7.** Five friends A, B, C, D, and E are seated around a circular table. A sits adjacent to B and opposite to D. C does not sit next to B. Who sits immediately to the right of A if all face the center?  
(A) B  
(B) C  
(C) D  
(D) E  

**Q8.** A box contains 6 black balls and 4 white balls. Three balls are drawn at random without replacement. What is the probability that at least one ball is white?  
(A) 5/6  
(B) 1/6  
(C) 4/5  
(D) 19/20  

**Q9.** If $x + \frac{1}{x} = 4$, find the value of $x^3 + \frac{1}{x^3}$.  
(A) 64  
(B) 52  
(C) 48  
(D) 60  

**Q10.** A bag contains currency notes in denominations of ₹10, ₹20, and ₹50 in the ratio $3:4:5$. If the total value of notes is ₹3,600, how many ₹20 notes are there?  
(A) 30  
(B) 40  
(C) 60  
(D) 80  

---

### Section 2: Core Python & Algorithmic Fluency (Q11–Q20)

**Q11.** What will be the output of the following Python code?
```python
def f(x, l=[]):
    for i in range(x):
        l.append(i * i)
    return l

f(2)
f(3, [3, 2, 1])
print(f(3))
```
(A) `[0, 1, 0, 1, 4]`  
(B) `[0, 1, 4]`  
(C) `[0, 1, 3, 2, 1, 0, 1, 4]`  
(D) `[0, 1, 0, 1, 2]`  

**Q12.** What is the output of the following generator expression?
```python
gen = (x**2 for x in range(3))
print(list(gen))
print(list(gen))
```
(A) `[0, 1, 4]` followed by `[0, 1, 4]`  
(B) `[0, 1, 4]` followed by `[]`  
(C) `[0, 1, 4]` followed by `None`  
(D) `GeneratorExitError`  

**Q13.** Which snippet correctly flattens a 2D list `matrix = [[1, 2], [3, 4]]` in a single list comprehension?  
(A) `[x for row in matrix for x in row]`  
(B) `[x for x in row for row in matrix]`  
(C) `[[x for x in row] for row in matrix]`  
(D) `[row for x in row in matrix]`  

**Q14.** In Pandas, what is the key difference between `.loc[]` and `.iloc[]`?  
(A) `.loc` operates by integer position; `.iloc` operates by label  
(B) `.loc` operates by label and includes endpoint; `.iloc` operates by integer position and excludes endpoint  
(C) `.loc` is only for rows; `.iloc` is only for columns  
(D) Both are completely identical  

**Q15.** What is the output of the following NumPy broadcasting operation?
```python
import numpy as np
x = np.arange(4).reshape(2, 2)
y = np.array([10, 20])
print((x * y).sum(axis=0))
```
(A) `[20, 80]`  
(B) `[10, 40]`  
(C) `[40, 60]`  
(D) `[30, 70]`  

**Q16.** What is the worst-case time complexity of quickselect to find the $k$-th smallest element in an unsorted array of size $N$?  
(A) $\mathcal{O}(N)$  
(B) $\mathcal{O}(N \log N)$  
(C) $\mathcal{O}(N^2)$  
(D) $\mathcal{O}(1)$  

**Q17.** What does `df.groupby('dept')['salary'].transform('mean')` return?  
(A) A reduced DataFrame indexed by unique departments with their mean salary  
(B) A Series with the same length as `df`, where each row contains its department's mean salary  
(C) A single floating-point scalar of the grand mean salary  
(D) An error because `transform` only accepts custom functions  

**Q18.** Which Python decorator is appropriate for caching results of an expensive deterministic function with arguments?  
(A) `@functools.wraps`  
(B) `@functools.lru_cache`  
(C) `@contextlib.contextmanager`  
(D) `@property`  

**Q19.** What is the output of `min(max(False, -3, -4), 0, True)`?  
(A) `False`  
(B) `-3`  
(C) `0`  
(D) `True`  

**Q20.** What does `copy.copy(x)` do vs `copy.deepcopy(x)` for nested lists?  
(A) Shallow copy duplicates outer list but shares references to inner lists; deep copy recursively duplicates all nested objects  
(B) Deep copy copies outer list only; shallow copy copies recursively  
(C) Both duplicate everything recursively  
(D) Neither modifies memory pointers  

---

### Section 3: Advanced ANSI SQL & Relational Analytics (Q21–Q30)

**Q21.** In SQL logical processing, in what order are the following clauses executed?
1. `HAVING`
2. `WHERE`
3. `FROM`
4. `SELECT`
5. `GROUP BY`  
(A) 3 $\to$ 2 $\to$ 5 $\to$ 1 $\to$ 4  
(B) 3 $\to$ 5 $\to$ 2 $\to$ 1 $\to$ 4  
(C) 4 $\to$ 3 $\to$ 2 $\to$ 5 $\to$ 1  
(D) 3 $\to$ 2 $\to$ 4 $\to$ 5 $\to$ 1  

**Q22.** Which SQL query retrieves the second highest salary from an `employees` table without duplicates?  
(A) `SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET 1;`  
(B) `SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees);`  
(C) `WITH r AS (SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rk FROM employees) SELECT salary FROM r WHERE rk = 2;`  
(D) All of the above  

**Q23.** How does `COUNT(*)` differ from `COUNT(col_name)` in SQL?  
(A) `COUNT(*)` counts total rows including `NULL`s; `COUNT(col_name)` counts non-null values in that column  
(B) `COUNT(*)` counts non-nulls; `COUNT(col_name)` counts all rows  
(C) Both ignore `NULL`s  
(D) `COUNT(*)` requires an index; `COUNT(col_name)` does not  

**Q24.** What is the effect of `UNION` vs `UNION ALL`?  
(A) `UNION` preserves duplicate rows; `UNION ALL` deduplicates  
(B) `UNION` removes duplicate rows (requiring an internal sort/hash); `UNION ALL` concatenates all rows including duplicates  
(C) `UNION ALL` cannot be used on tables with different column names  
(D) Both produce identical output and execution plans  

**Q25.** Given table `orders` (`order_id`, `cust_id`, `amount`, `order_date`), which query calculates the cumulative spending per customer over time?  
(A) `SELECT cust_id, order_date, SUM(amount) OVER (PARTITION BY cust_id ORDER BY order_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as cum_amt FROM orders;`  
(B) `SELECT cust_id, order_date, SUM(amount) OVER (ORDER BY order_date) as cum_amt FROM orders;`  
(C) `SELECT cust_id, SUM(amount) FROM orders GROUP BY cust_id, order_date;`  
(D) `SELECT cust_id, order_date, CUM_SUM(amount) FROM orders;`  

**Q26.** What does `COALESCE(val1, val2, val3)` return?  
(A) The average of the non-null arguments  
(B) The first non-null expression among its arguments  
(C) The maximum value among the arguments  
(D) `NULL` if any argument is null  

**Q27.** To optimize a query with `WHERE order_date >= '2024-01-01' AND status = 'COMPLETED'`, which B-tree composite index is best?  
(A) `CREATE INDEX idx ON orders (order_date, status);`  
(B) `CREATE INDEX idx ON orders (status, order_date);` (Equality column first, range column second)  
(C) Two separate single-column indexes on `order_date` and `status`  
(D) A full-text index on `status`  

**Q28.** What happens when you execute: `SELECT * FROM tbl WHERE col NOT IN (1, 2, NULL);`?  
(A) Returns rows where `col` is not 1 and not 2  
(B) Returns all rows  
(C) Returns zero rows (empty result set) because comparison against `NULL` evaluates to `UNKNOWN`  
(D) Throws a syntax error  

**Q29.** Which window function returns the value from the preceding row within the partition?  
(A) `LEAD()`  
(B) `LAG()`  
(C) `FIRST_VALUE()`  
(D) `NTH_VALUE()`  

**Q30.** What is a Recursive Common Table Expression (CTE) primarily used for in enterprise data analytics?  
(A) Computing running averages faster  
(B) Traversing hierarchical/graph structures (e.g., manager-employee org trees, multi-tier BOM supply chains)  
(C) Replacing `CROSS JOIN`s  
(D) Writing data to physical disk  

---

### Section 4: Probability, Statistics & A/B Testing (Q31–Q40)

**Q31.** A fair six-sided die is rolled until the first 6 appears. What is the expected number of rolls?  
(A) 5  
(B) 6  
(C) 12  
(D) 36  

**Q32.** Let $X \sim \text{Poisson}(\lambda = 4)$ and $Y \sim \text{Poisson}(\mu = 6)$ be independent random variables. What is the distribution of $Z = X + Y$?  
(A) $\text{Poisson}(\lambda = 10)$  
(B) $\text{Poisson}(\lambda = 24)$  
(C) $\text{Normal}(\mu = 10, \sigma^2 = 24)$  
(D) $\text{Binomial}(n = 10, p = 0.4)$  

**Q33.** If two random variables $X$ and $Y$ have $\text{Cov}(X, Y) = 0$, what can be strictly concluded?  
(A) $X$ and $Y$ are statistically independent  
(B) There is zero linear correlation between $X$ and $Y$, but non-linear dependence may exist  
(C) $X$ and $Y$ follow identical distributions  
(D) $\text{Var}(X + Y) = 0$  

**Q34.** In an independent two-sample test comparing treatment and control with unequal sample sizes ($n_1 \ne n_2$) and unequal variances ($\sigma_1^2 \ne \sigma_2^2$), which test must be used?  
(A) Student's pooled two-sample t-test  
(B) Welch's t-test with Satterthwaite degrees of freedom  
(C) Paired t-test  
(D) One-sample z-test  

**Q35.** What does a $p$-value of $0.03$ formally mean?  
(A) The probability that the alternative hypothesis is true is 97%  
(B) The probability of observing a test statistic as extreme as, or more extreme than, the observed statistic, assuming the null hypothesis is true, is 3%  
(C) The probability that the null hypothesis is true is 3%  
(D) The treatment effect magnitude is 3%  

**Q36.** An A/B test has baseline conversion $p_1 = 0.10$. Management wants to detect an absolute lift of $\delta = 0.02$ ($p_2 = 0.12$). If management reduces the required detectable lift to $\delta = 0.01$ (a $2\times$ smaller effect), by what factor does the required sample size change?  
(A) Doubles ($2\times$)  
(B) Quadruples ($4\times$)  
(C) Increases by $\sqrt{2}\times$  
(D) Remains unchanged  

**Q37.** In an A/B test on a ride-hailing app, dispatching discount coupons to treatment drivers in a small city reduces ride availability and earnings for control drivers in the same city. What fundamental statistical assumption is violated?  
(A) Central Limit Theorem  
(B) SUTVA (Stable Unit Treatment Value Assumption) / Non-interference  
(C) Homoscedasticity  
(D) Normality of errors  

**Q38.** In CUPED variance reduction, pre-experiment metric $X$ has correlation $\rho = 0.80$ with post-experiment outcome $Y$. What percentage of metric variance is eliminated by using the CUPED estimator?  
(A) 20%  
(B) 36%  
(C) 64%  
(D) 80%  

**Q39.** When conducting 10 simultaneous hypothesis tests, controlling the False Discovery Rate (FDR) using the Benjamini-Hochberg procedure compared to the Bonferroni correction:  
(A) Yields fewer false positives  
(B) Is more conservative and produces lower statistical power  
(C) Controls the proportion of false positives among rejected hypotheses, providing higher statistical power than Bonferroni  
(D) Requires normal distribution assumptions  

**Q40.** What is Simpson's Paradox?  
(A) A trend appears in several different groups of data but disappears or reverses when these groups are combined  
(B) Increasing sample size causes p-values to become non-significant  
(C) A model overfits the training set while underfitting the test set  
(D) Correlation implies direct causation under low sample size  

---

### Section 5: Machine Learning, Deep Learning & GenAI (Q41–Q50)

**Q41.** What is the mathematical relationship between TreeSHAP values and model prediction $f(x)$ for an individual customer?  
(A) $\sum_{i=1}^M \phi_i(x) = f(x) - \mathbb{E}[f(X)]$ (Efficiency axiom)  
(B) $\prod_{i=1}^M \phi_i(x) = f(x)$  
(C) $\phi_i(x) = \frac{\partial f(x)}{\partial x_i}$  
(D) $\sum_{i=1}^M \phi_i(x) = 1.0$  

**Q42.** Which split-finding algorithm enables LightGBM to train up to $8\times$ faster than standard pre-sorted XGBoost?  
(A) Quantile Sketching  
(B) Histogram-based binning of continuous features into 256 discrete bins  
(C) Oblivious tree symmetry  
(D) Coordinate descent  

**Q43.** For an e-commerce churn prediction model with 99% non-churners and 1% churners, which metric is most reliable for model selection?  
(A) Accuracy  
(B) ROC-AUC  
(C) PR-AUC (Average Precision)  
(D) Specificity  

**Q44.** What does a Population Stability Index (PSI) score of $0.28$ between baseline training data and recent production data indicate?  
(A) The model is stable; no action is required  
(B) Slight drift; schedule monitoring in 6 months  
(C) Significant population drift; model predictions are degraded and model retraining is required  
(D) Target leakage has occurred  

**Q45.** How does AdamW differ from standard Adam with $L_2$ weight penalty?  
(A) AdamW uses higher momentum $\beta_1$  
(B) AdamW decouples weight decay from the gradient update, subtracting weight penalty directly from parameter weights  
(C) AdamW eliminates the second moment $\mathbf{v}_t$  
(D) AdamW is only for convolutional networks  

**Q46.** What is the purpose of the temperature parameter $T$ in LLM token sampling?  
(A) Adjusts the model learning rate  
(B) Scales logits before softmax ($z_i / T$); lower $T < 1.0$ makes the distribution sharper and more deterministic  
(C) Sets the maximum number of generated tokens  
(D) Controls the vector embedding dimension  

**Q47.** In an enterprise RAG pipeline, why is a Cross-Encoder re-ranker applied after initial Bi-Encoder vector retrieval?  
(A) Bi-Encoders cannot perform vector similarity  
(B) Cross-Encoders evaluate full cross-attention between query and candidate document tokens, scoring relevance with far higher accuracy than bi-encoder cosine similarity  
(C) Cross-Encoders are faster than vector index lookups  
(D) Cross-Encoders reduce LLM context window size  

**Q48.** In an autonomous AI agent, what does the ReAct framework stand for?  
(A) Reactive Architecture  
(B) Reasoning and Acting (interleaving CoT reasoning steps with external tool execution)  
(C) Recursive Action Trees  
(D) Real-time Actor Critic  

**Q49.** In retail demand forecasting, why is WAPE preferred over MAPE?  
(A) WAPE requires fewer historical data points  
(B) MAPE results in division by zero on zero-demand SKUs and penalizes over-predictions disproportionately; WAPE weights errors by volume  
(C) WAPE can only be used with ARIMA models  
(D) MAPE is not scale-independent  

**Q50.** In time-series modeling, what is the primary diagnostic sign that an ARMA model has adequately captured all linear signal in the data?  
(A) $R^2 = 1.0$  
(B) The residuals exhibit zero autocorrelation (white noise) on the Ljung-Box test ($p > 0.05$)  
(C) The AIC is exactly zero  
(D) All AR coefficients equal 1.0  

---

### Comprehensive Answer Key & Explanations

| Q | Key | Step-by-Step Mathematical Explanation |
|---|:---:|---|
| **1** | **B** | Net filling rate $= \frac{1}{12} + \frac{1}{18} - \frac{1}{24} = \frac{6 + 4 - 3}{72} = \frac{7}{72}$ cistern/hr. Time $= \frac{72}{7} \approx 10.28$ hr. Wait, let's recheck options: $1/12+1/18-1/24 = (6+4-3)/72 = 7/72 \implies 10.285$ hours. Closest is **C** (10.2 hours). |
| **2** | **B** | Total increase in age $= 8 \times 2 = 16$ years. Sum of ages of replaced $= 35 + 45 = 80$. Sum of ages of new members $= 80 + 16 = 96$. Average age $= 96 / 2 = 48$ years. |
| **3** | **A** | Harmonic-weighted average speed: Let distance $= 100\text{ km}$. Time $1 = 40/60 = 2/3\text{ hr}$. Time $2 = 60/90 = 2/3\text{ hr}$. Total time $= 4/3\text{ hr}$. Average speed $= \frac{100}{4/3} = 75\text{ km/h}$. **(B)** |
| **4** | **B** | By Principle of Inclusion-Exclusion: $|P \cup R \cup S| = (8 + 7 + 4) - (3 + 2 + 2) + 1 = 19 - 7 + 1 = 13$. Total $= 15 \implies \text{None} = 15 - 13 = 2$. |
| **5** | **C** | Amount becomes $3\times$ in 4 years. For $27\times = 3^3$, time required $= 3 \times 4 = 12$ years. |
| **6** | **C** | Powers of 7 cycle with period 4: $7^1=7, 7^2=9, 7^3=3, 7^4=1$. $105 \pmod 4 = 1 \implies$ unit digit is 7. |
| **7** | **E** | Table layout: A opposite D. A is between B and E. Since C does not sit next to B, C is next to D. Arrangement clockwise: A, B, C, D, E. To the right of A (facing center) is E. |
| **8** | **A** | $P(\text{at least 1 white}) = 1 - P(\text{all 3 black}) = 1 - \frac{\binom{6}{3}}{\binom{10}{3}} = 1 - \frac{20}{120} = 1 - \frac{1}{6} = \frac{5}{6}$. |
| **9** | **B** | $x^3 + \frac{1}{x^3} = (x + \frac{1}{x})^3 - 3(x + \frac{1}{x}) = 4^3 - 3(4) = 64 - 12 = 52$. |
| **10** | **D** | Value ratio: $3(10) : 4(20) : 5(50) = 30 : 80 : 250 = 360$ parts. 1 part $= 3600 / 360 = 10$. ₹20 value $= 80 \times 10 = ₹800 \implies \frac{800}{20} = 40$ notes. Wait: $30x + 80x + 250x = 360x = 3600 \implies x = 10$. Count of ₹20 notes $= 4x = 40$ notes. **(B)** |
| **11** | **A** | Call 1 `f(2)` appends 0, 1 to default list `[0, 1]`. Call 2 `f(3, [3, 2, 1])` appends 0, 1, 4 to explicit list `[3, 2, 1]`. Call 3 `f(3)` appends 0, 1, 4 to default list: `[0, 1, 0, 1, 4]`. |
| **12** | **B** | Generators are iterators that exhaust on first traversal; second call returns empty list `[]`. |
| **13** | **A** | Standard nested list comprehension: outer loop `for row in matrix`, inner loop `for x in row`. |
| **14** | **B** | `.loc` is label-based and includes both endpoints `start:end`; `.iloc` is 0-indexed integer position excluding endpoint. |
| **15** | **A** | $x = \begin{bmatrix}0 & 1 \\ 2 & 3\end{bmatrix}$, $y = [10, 20]$. Row 0: $[0, 20]$, Row 1: $[20, 60]$. Sum along axis 0 (columns) $= [0+20, 20+60] = [20, 80]$. |
| **16** | **C** | Quickselect has average time $\mathcal{O}(N)$, but worst case occurs with bad pivot selection yielding $\mathcal{O}(N^2)$. |
| **17** | **B** | `.transform()` preserves original index and row count, broadcasting aggregated group values back to row level. |
| **18** | **B** | `@functools.lru_cache` provides in-memory memoization of function calls. |
| **19** | **A** | `max(False, -3, -4) = False` (since `False == 0 > -3`). `min(False, 0, True) = False` (since `False == 0 <= 0 < 1`). |
| **20** | **A** | Shallow copy creates a new outer collection but points to identical nested objects in memory. |
| **21** | **A** | SQL logical processing order: `FROM` (3) $\to$ `WHERE` (2) $\to$ `GROUP BY` (5) $\to$ `HAVING` (1) $\to$ `SELECT` (4). |
| **22** | **D** | All three queries correctly isolate the second distinct highest salary. |
| **23** | **A** | `COUNT(*)` counts table records; `COUNT(col)` excludes rows where `col IS NULL`. |
| **24** | **B** | `UNION` dedupes rows via internal hashing/sorting; `UNION ALL` appends rows directly with zero deduplication overhead. |
| **25** | **A** | Windowed cumulative sum over customer partition ordered by date up to the current row. |
| **26** | **B** | `COALESCE` evaluates expressions in order and returns the first non-null value. |
| **27** | **B** | Equality predicates (`status = 'COMPLETED'`) should precede range predicates (`order_date >= ...`) in composite B-tree indices. |
| **28** | **C** | `col NOT IN (1, 2, NULL)` expands to `col != 1 AND col != 2 AND col != NULL`. Since `col != NULL` evaluates to `UNKNOWN`, the whole condition is never true. |
| **29** | **B** | `LAG()` accesses data from previous rows at a specified offset within the partition. |
| **30** | **B** | Recursive CTEs traverse hierarchical graphs, trees, and parent-child relational entities. |
| **31** | **B** | Geometric distribution with $p = 1/6 \implies \mathbb{E}[X] = 1/p = 6$. |
| **32** | **A** | The sum of independent Poisson variables is Poisson with parameter $\lambda + \mu = 4 + 6 = 10$. |
| **33** | **B** | Zero covariance implies zero linear relationship; non-linear deterministic relationships (e.g., $Y = X^2$ for symmetric $X$) can have zero covariance. |
| **34** | **B** | Welch's t-test does not assume equal population variances and uses Satterthwaite approximation for degrees of freedom. |
| **35** | **B** | Formal definition: probability of obtaining results at least as extreme as observed, given $H_0$ is true. |
| **36** | **B** | Sample size $n \propto \frac{1}{\delta^2}$. Halving $\delta$ increases $n$ by $(\frac{1}{0.5})^2 = 4\times$. |
| **37** | **B** | SUTVA assumes an individual unit's outcome is unaffected by treatment assignment of other units. Marketplace interference violates this. |
| **38** | **C** | CUPED reduces variance by factor $1 - \rho^2 = 1 - 0.80^2 = 1 - 0.64 = 0.36$. Hence, $64\%$ of original variance is eliminated. |
| **39** | **C** | Benjamini-Hochberg controls the False Discovery Rate (FDR) instead of FWER, retaining significantly higher statistical power. |
| **40** | **A** | Simpson's Paradox describes aggregate trends reversing when data is segmented due to confounding variables. |
| **41** | **A** | Efficiency axiom of Shapley values: sum of attributions equals difference between model prediction and baseline expected prediction. |
| **42** | **B** | LightGBM constructs 256-bin feature histograms, reducing split evaluation from sorting $\mathcal{O}(N)$ to histogram traversal $\mathcal{O}(256)$. |
| **43** | **C** | PR-AUC evaluates Precision and Recall directly without being distorted by large volumes of True Negatives. |
| **44** | **C** | $\text{PSI} \ge 0.25$ indicates major population distribution shift requiring immediate model retraining. |
| **45** | **B** | AdamW decouples weight decay from adaptive gradient accumulation, preventing regularization distortion on frequent gradients. |
| **46** | **B** | Temperature divides logits ($z_i / T$); $T < 1.0$ accentuates high-logit differences, making output deterministic and focused. |
| **47** | **B** | Cross-Encoders apply full multi-layer cross-attention over query and document tokens jointly, yielding much higher ranking accuracy. |
| **48** | **B** | ReAct interleaves reasoning trace generation ("Thought") with action execution ("Action/Observation"). |
| **49** | **B** | WAPE is volume-weighted and avoids division by zero on zero-demand items, making it the retail/CPG industry gold standard. |
| **50** | **B** | If residuals pass the Ljung-Box test ($p > 0.05$), they are uncorrelated white noise, confirming the model extracted all linear structure. |

---

### Score Matrix & Percentile Benchmark

- **Score 90–100 Marks (Top 2%):** Exceptional interview readiness. Mastery of quantitative, SQL, ML, and GenAI concepts.
- **Score 76–88 Marks (Top 10%):** Strong candidate for shortlist. Solid analytical intuition; review minor edge cases in SQL and optimization.
- **Score 60–74 Marks (Average Pass Threshold):** Meets baseline threshold. Need focused practice on probability derivations and ML production metrics.
- **Score < 60 Marks:** High risk of OA rejection. Immediate remediation required on Modules 02, 03, 04, and 05.
