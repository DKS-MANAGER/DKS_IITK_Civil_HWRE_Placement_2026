# Enterprise Recommender Systems & Personalization Engines

**Target Role:** Data Scientist / Associate Data Scientist | Tredence Analytics  
**Context:** IIT Kanpur Placement Season 2026–27  
**Prerequisites:** Linear Algebra, Matrix Decompositions, Optimization

---

## 1. Recommender Paradigms Taxonomy

```
                       Recommender Systems
 ┌───────────────────────────────┼───────────────────────────────┐
 │                               │                               │
Collaborative Filtering      Content-Based Filtering      Hybrid Systems
 ├── Memory-Based             ├── TF-IDF Vector Spaces    ├── Weighted Ensemble
 │    ├── User-User CF        └── Item Feature Profiles   ├── Cascade Stacking
 │    └── Item-Item CF                                    └── Two-Tower Deep Models
 └── Model-Based
      ├── SVD / Funk SVD
      └── Implicit ALS
```

---

## 2. Memory-Based Collaborative Filtering

Predicts user $u$'s rating for item $i$ based on historical similarities.

### 2.1 Similarity Metrics
1. **Cosine Similarity:**
   $$\text{sim}(\mathbf{u}, \mathbf{v}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\|_2 \|\mathbf{v}\|_2} = \frac{\sum_k r_{uk} r_{vk}}{\sqrt{\sum r_{uk}^2} \sqrt{\sum r_{vk}^2}}$$
2. **Pearson Correlation Coefficient (PCC):** Accounts for user rating scale bias (e.g., harsh vs generous raters):
   $$\text{sim}_{\text{PCC}}(\mathbf{u}, \mathbf{v}) = \frac{\sum_{k \in I_{uv}} (r_{uk} - \bar{r}_u)(r_{vk} - \bar{r}_v)}{\sqrt{\sum_{k \in I_{uv}} (r_{uk} - \bar{r}_u)^2} \sqrt{\sum_{k \in I_{uv}} (r_{vk} - \bar{r}_v)^2}}$$

### 2.2 Item-Item vs User-User CF in Enterprise
- **Item-Item CF is strongly preferred in retail:**
  - The number of users $N$ ($10^6 - 10^8$) dwarfs the number of items $M$ ($10^3 - 10^5$). Computing and caching an $M \times M$ item similarity matrix is computationally manageable.
  - Item characteristics remain stable over time; user tastes evolve erratically.

---

## 3. Model-Based Collaborative Filtering: Matrix Factorization

Approximates the sparse rating matrix $\mathbf{R} \in \mathbb{R}^{|U| \times |I|}$ by the product of two low-rank dense matrices:
$$\mathbf{R} \approx \mathbf{P} \mathbf{Q}^T, \quad \text{where } \mathbf{P} \in \mathbb{R}^{|U| \times k}, \ \mathbf{Q} \in \mathbb{R}^{|I| \times k}, \ k \ll \min(|U|, |I|)$$
Predicted rating: $\hat{r}_{ui} = \mu + b_u + b_i + \mathbf{p}_u^T \mathbf{q}_i$.

### 3.1 Regularized Funk SVD Objective
$$\min_{\mathbf{P}, \mathbf{Q}, \mathbf{b}} \sum_{(u, i) \in \mathcal{K}} \left(r_{ui} - (\mu + b_u + b_i + \mathbf{p}_u^T \mathbf{q}_i)\right)^2 + \lambda \left(b_u^2 + b_i^2 + \|\mathbf{p}_u\|_2^2 + \|\mathbf{q}_i\|_2^2\right)$$
Optimized via Stochastic Gradient Descent (SGD) iterating strictly over observed ratings $\mathcal{K}$.

### 3.2 Implicit Feedback: Alternating Least Squares (ALS)
In enterprise retail, explicit 1–5 star ratings are rare; 99% of data is **implicit feedback** (clicks, page views, purchases, add-to-carts):
- Let preference $p_{ui} = \mathbb{I}(r_{ui} > 0) \in \{0, 1\}$.
- Confidence $c_{ui} = 1 + \alpha r_{ui}$ (higher frequency = greater confidence).

**Hu, Koren, Volinsky (2008) Objective:**
$$\mathcal{L}_{\text{ALS}} = \sum_{u, i} c_{ui} (p_{ui} - \mathbf{p}_u^T \mathbf{q}_i)^2 + \lambda \left(\sum_u \|\mathbf{p}_u\|_2^2 + \sum_i \|\mathbf{q}_i\|_2^2\right)$$
- Because loss sums over all $U \times I$ pairs, SGD is too slow.
- **ALS Solution:** Fix $\mathbf{Q}$, loss becomes quadratic in $\mathbf{P}$ with an analytical closed-form solution. Fix $\mathbf{P}$, solve for $\mathbf{Q}$. Alternate until convergence. Highly parallelizable in Apache Spark / Databricks.

---

## 4. Evaluation Metrics for Ranking

Predicting exact ratings is irrelevant in production; the system must rank the top $K$ items accurately.

### 4.1 Precision@K and Recall@K
$$\text{Precision}@K = \frac{|\text{Relevant Items} \cap \text{Top-}K \text{ Recommended}|}{K}$$
$$\text{Recall}@K = \frac{|\text{Relevant Items} \cap \text{Top-}K \text{ Recommended}|}{|\text{Total Relevant Items for User}|}$$

### 4.2 Mean Average Precision (MAP@K)
$$\text{AP}@K = \frac{1}{\min(m, K)} \sum_{k=1}^K P(k) \times \text{rel}(k), \quad \text{MAP}@K = \frac{1}{|U|} \sum_{u=1}^{|U|} \text{AP}_u@K$$
Where $P(k)$ is Precision at cutoff $k$, and $\text{rel}(k) \in \{0, 1\}$ indicates if the $k$-th item is relevant.

### 4.3 Normalized Discounted Cumulative Gain (NDCG@K)
Evaluates graded relevance with logarithmic positional discount:

$$\text{DCG}@K = \sum_{i=1}^K \frac{2^{\text{rel}_i} - 1}{\log_2(i + 1)}$$
$$\text{NDCG}@K = \frac{\text{DCG}@K}{\text{IDCG}@K}$$
Where $\text{IDCG}@K$ is the Ideal DCG obtained by sorting items in descending order of true relevance. $\text{NDCG} \in [0, 1]$, heavily penalizing relevant items ranked low in the recommendation slate.

---

## 5. Cold Start Problem & Retail Operationalization

### 5.1 Mitigation Strategies
1. **New User Cold Start:**
   - Default to segmented popularity baselines (e.g., top-selling items in user's geographic zip code).
   - Multi-Armed Bandit (Thompson Sampling / $\epsilon$-Greedy) to balance showing proven top-sellers (exploitation) vs exploring new product categories (exploration).
2. **New Item Cold Start:**
   - Content-based attribute embeddings (brand, category, price tier, textual product description via Transformer embeddings).
3. **The "Last-Mile" Retail Application:**
   - In CPG B2B commerce (Tredence client scenarios), recommenders drive **Next-Best-Action (NBA)** for retail sales reps: suggesting specific high-margin replenishment SKUs during distributor order intake.
