# High-Yield Placement Revision Cheat Sheet (Final 24 Hours)

**Target Role:** Data Scientist / Associate Data Scientist | Tredence Analytics  
**Context:** IIT Kanpur Placement Season 2026–27 | Phase 1

---

## 1. Core Mathematical & Statistical Formulas

### 1.1 Probability & Distributions
- **Bayes' Rule:** $P(A \mid B) = \frac{P(B \mid A)P(A)}{P(B)}$
- **Binomial:** $\mathbb{E}[X] = np, \ \text{Var}(X) = np(1-p)$
- **Poisson:** $\mathbb{E}[X] = \lambda, \ \text{Var}(X) = \lambda, \ P(X=k) = \frac{\lambda^k e^{-\lambda}}{k!}$
- **Exponential:** $f(t) = \lambda e^{-\lambda t}, \ \mathbb{E}[T] = \frac{1}{\lambda}, \ \text{Var}(T) = \frac{1}{\lambda^2}$ (Memoryless)
- **Lognormal:** If $\ln X \sim \mathcal{N}(\mu, \sigma^2) \implies \mathbb{E}[X] = \exp\left(\mu + \frac{\sigma^2}{2}\right), \ \text{Median} = \exp(\mu)$
- **Central Limit Theorem:** $\bar{X}_n \xrightarrow{d} \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)$

### 1.2 Experimentation & A/B Testing
- **Continuous Sample Size (Evan Miller):**
  $$n = \frac{2\sigma^2 (Z_{1-\alpha/2} + Z_{1-\beta})^2}{\delta^2} \approx \frac{15.7 \sigma^2}{\delta^2} \quad (\text{for } \alpha=0.05, \text{power}=0.80)$$
- **Proportion Sample Size Rule of Thumb:** $n \approx \frac{16 \cdot p(1-p)}{\delta^2}$
- **CUPED Estimator:** $\hat{Y}_{\text{CUPED}} = Y - \theta(X - \mathbb{E}[X]), \ \theta^* = \frac{\text{Cov}(Y, X)}{\text{Var}(X)}$
  - $\text{Variance Reduction Factor} = 1 - \rho^2$
- **Sample Ratio Mismatch (SRM):** $\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i} \ (df = 1, \text{crit}_{0.001} = 10.83)$
- **Bonferroni:** $\alpha^* = \alpha / m$; **Benjamini-Hochberg:** Rank $p_{(k)} \le \frac{k}{m} \times Q$

---

## 2. Machine Learning & Optimization Mechanics

### 2.1 Loss Formulations & Tree Splitting
- **Binary Cross-Entropy (Log-Loss):** $\mathcal{L} = - \sum [y_i \ln p_i + (1 - y_i)\ln(1 - p_i)]$
- **Logistic Gradient & Hessian:** $g_i = p_i - y_i, \ h_i = p_i(1 - p_i)$
- **XGBoost Optimal Leaf Weight:** $w_j^* = -\frac{\sum g_i}{\sum h_i + \lambda}$
- **XGBoost Split Gain:** $\text{Gain} = \frac{1}{2}\left[\frac{G_L^2}{H_L + \lambda} + \frac{G_R^2}{H_R + \lambda} - \frac{G^2}{H + \lambda}\right] - \gamma$
- **LightGBM Speedup:** Histogram binning (256 bins), GOSS (gradient sampling), EFB (feature bundling), Leaf-wise growth.
- **TreeSHAP Efficiency Axiom:** $\sum_{i=1}^M \phi_i(x) = f(x) - \mathbb{E}[f(X)]$

### 2.2 Evaluation Metrics
- **PR-AUC vs ROC-AUC:** PR-AUC mandatory when positive class $< 5\%$ because False Positive Rate denominator ($\text{FP} + \text{TN}$) is diluted by massive True Negatives.
- **WAPE (Weighted Absolute Percentage Error):** $\frac{\sum |y_i - \hat{y}_i|}{\sum y_i}$ (Never divides by zero; retail gold standard).
- **Population Stability Index (PSI):** $\sum (T_k - B_k) \ln(T_k / B_k)$. ($< 0.1$ stable, $\ge 0.25$ retrain).

---

## 3. SQL Architecture & Quick Syntax Patterns

### 3.1 Logical Query Execution Order
$$\text{FROM} \to \text{ON} \to \text{JOIN} \to \text{WHERE} \to \text{GROUP BY} \to \text{HAVING} \to \text{WINDOW} \to \text{SELECT} \to \text{DISTINCT} \to \text{ORDER BY} \to \text{LIMIT}$$

### 3.2 High-Frequency SQL Patterns
- **Deduplication:**
  ```sql
  WITH ranked AS (
      SELECT *, ROW_NUMBER() OVER (PARTITION BY key_col ORDER BY updated_at DESC) as rn
      FROM tbl
  ) SELECT * FROM ranked WHERE rn = 1;
  ```
- **Top 3 per Group without Gaps:**
  ```sql
  WITH ranked AS (
      SELECT *, DENSE_RANK() OVER (PARTITION BY category ORDER BY revenue DESC) as dr
      FROM tbl
  ) SELECT * FROM ranked WHERE dr <= 3;
  ```
- **Rolling 7-Day Window Frame:**
  ```sql
  AVG(sales) OVER (PARTITION BY store_id ORDER BY tx_date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)
  ```
- **Month-over-Month Velocity:**
  ```sql
  ROUND(100.0 * (rev - LAG(rev) OVER (ORDER BY mth)) / NULLIF(LAG(rev) OVER (ORDER BY mth), 0), 2)
  ```

---

## 4. Generative AI & Vector Search Summary

- **Scaled Dot-Product Attention:** $\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}\right)\mathbf{V}$
- **LoRA Weight Update:** $\mathbf{W} = \mathbf{W}_0 + \frac{\alpha}{r}(\mathbf{B}\mathbf{A}), \ \mathbf{B}=0, \mathbf{A}\sim\mathcal{N}$. Deploys with zero added inference latency.
- **RRF Score:** $\text{RRF}(d) = \sum_{m \in M} \frac{1}{60 + r_m(d)}$ (Merges BM25 and Dense vectors).
- **RAG Triad:** Context Relevance $\to$ Faithfulness (Groundedness) $\to$ Answer Relevance.

---

## 5. Tredence Consulting "Last-Mile" Principles

1. **The Question Behind the Question:** Never jump to algorithms immediately. Clarify the business objective, P&L metric, and physical operational constraints first.
2. **The "Now What?":** An algorithm is useless if frontline workers don't act on it. Always explain the delivery tool (e.g., store tablet, CRM alert) and reason codes (TreeSHAP).
3. **The SPEED Values:**
   - **S**peed (rapid prototyping)
   - **P**assion (relentless customer impact)
   - **E**xcellence (statistical rigor, zero data leakage)
   - **E**mpathy (listening to frontline store managers)
   - **D**isruption (challenging static Excel heuristics with AI)
4. **The Non-CS Pivot Defense:**
   - Hydraulics & Water Resources is applied computational data science: continuous PDEs, stochastic time series, and extreme event modeling.
   - Engineering trains disciplined real-world problem solvers who respect constraints and messy data.
