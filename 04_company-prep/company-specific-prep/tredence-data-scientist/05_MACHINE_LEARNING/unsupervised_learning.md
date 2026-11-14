# Unsupervised Learning & Dimensionality Reduction

**Target Role:** Data Scientist / Associate Data Scientist | Tredence Analytics  
**Context:** IIT Kanpur Placement Season 2026–27  
**Prerequisites:** Linear Algebra (Eigendecomposition, SVD), Vector Calculus, Optimization

---

## 1. Clustering Algorithms

### 1.1 K-Means Clustering & K-Means++
Given $n$ observations $\{\mathbf{x}_1, \dots, \mathbf{x}_n\} \subset \mathbb{R}^d$, partition into $K$ disjoint clusters $S = \{S_1, \dots, S_K\}$ minimizing Within-Cluster Sum of Squares (WCSS / Inertia):

$$J(S) = \sum_{k=1}^K \sum_{\mathbf{x}_i \in S_k} \|\mathbf{x}_i - \boldsymbol{\mu}_k\|_2^2, \quad \text{where } \boldsymbol{\mu}_k = \frac{1}{|S_k|} \sum_{\mathbf{x}_i \in S_k} \mathbf{x}_i$$

**Lloyd's Alternating Minimization Algorithm:**
1. **Assignment Step:** Assign each $\mathbf{x}_i$ to the nearest centroid:
   $$c_i^{(t)} = \arg\min_k \|\mathbf{x}_i - \boldsymbol{\mu}_k^{(t)}\|^2$$
2. **Update Step:** Recompute centroids as cluster centers of mass:
   $$\boldsymbol{\mu}_k^{(t+1)} = \frac{\sum_{i=1}^n \mathbb{I}(c_i^{(t)} = k) \mathbf{x}_i}{\sum_{i=1}^n \mathbb{I}(c_i^{(t)} = k)}$$

**K-Means++ Initialization (Arthur & Vassilvitskii, 2007):**
Random initialization frequently falls into poor local minima. K-Means++ ensures spread:
1. Choose first centroid $\boldsymbol{\mu}_1$ uniformly at random from dataset.
2. For each point $\mathbf{x}$, compute shortest squared Euclidean distance $D(\mathbf{x})^2 = \min_{j} \|\mathbf{x} - \boldsymbol{\mu}_j\|^2$ to existing centroids.
3. Select next centroid with probability proportional to $D(\mathbf{x})^2$:
   $$P(\mathbf{x}_i = \boldsymbol{\mu}_{\text{next}}) = \frac{D(\mathbf{x}_i)^2}{\sum_{j=1}^n D(\mathbf{x}_j)^2}$$
4. Repeat until $K$ centroids are chosen. Guarantees an $\mathcal{O}(\log K)$ approximation bound to the optimal clustering.

### 1.2 Cluster Evaluation Metrics
1. **Elbow Method:** Plot WCSS vs $K$; identify inflection point where marginal reduction diminishes.
2. **Silhouette Coefficient:** For observation $i \in S_A$:
   - $a(i) = \frac{1}{|S_A| - 1} \sum_{j \in S_A, j \ne i} \|\mathbf{x}_i - \mathbf{x}_j\|$ (mean intra-cluster distance)
   - $b(i) = \min_{C \ne A} \frac{1}{|S_C|} \sum_{j \in S_C} \|\mathbf{x}_i - \mathbf{x}_j\|$ (mean nearest-cluster distance)
   $$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}, \quad s(i) \in [-1, 1]$$
   - $s \to +1$: Well-clustered; $s \approx 0$: On cluster boundary; $s < 0$: Misclustered.
3. **Davies-Bouldin Index (DBI):** Lower is better. Measures ratio of within-cluster scatter to between-cluster separation.

---

### 1.3 Hierarchical Agglomerative Clustering
Bottom-up clustering building a tree (dendrogram) without pre-specifying $K$:
- **Single Linkage:** $D(A, B) = \min_{\mathbf{a} \in A, \mathbf{b} \in B} \|\mathbf{a} - \mathbf{b}\|$ (Prone to chaining).
- **Complete Linkage:** $D(A, B) = \max_{\mathbf{a} \in A, \mathbf{b} \in B} \|\mathbf{a} - \mathbf{b}\|$ (Produces compact, spherical clusters).
- **Average Linkage:** $D(A, B) = \frac{1}{|A||B|} \sum_{\mathbf{a} \in A} \sum_{\mathbf{b} \in B} \|\mathbf{a} - \mathbf{b}\|$.
- **Ward's Linkage:** Merges pair that minimizes the increase in total within-cluster variance.

---

### 1.4 DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
Overcomes K-Means limitations (arbitrary geometric shapes, automatic noise identification, no pre-set $K$):

**Core Parameters:**
- $\epsilon$ (eps): Neighborhood radius around point $\mathbf{x}$.
- `min_samples`: Minimum number of points within $\epsilon$-neighborhood to form a dense region.

**Point Classification:**
1. **Core Point:** $|N_\epsilon(\mathbf{x})| \ge \text{min\_samples}$.
2. **Border Point:** $|N_\epsilon(\mathbf{x})| < \text{min\_samples}$, but belongs to the $\epsilon$-neighborhood of a Core Point.
3. **Noise Point:** Neither Core nor Border (label = -1).

**Parameter Selection:**
- Set `min_samples` $\ge 2 \times \text{dimensions}$ (rule of thumb: 4 to 10).
- Plot sorted $k$-nearest neighbor distance curve ($k = \text{min\_samples}$); select $\epsilon$ at the sharp "elbow" point.

---

## 2. Dimensionality Reduction

### 2.1 Principal Component Analysis (PCA)
Orthogonal linear transformation that projects data onto directions of maximal variance.

**Mathematical Formulation:**
Given centered data $\mathbf{X} \in \mathbb{R}^{n \times d}$ ($\frac{1}{n}\sum \mathbf{x}_i = \mathbf{0}$):
Sample Covariance Matrix:
$$\mathbf{\Sigma} = \frac{1}{n} \mathbf{X}^T \mathbf{X} \in \mathbb{R}^{d \times d}$$

First principal component $\mathbf{w}_1$ maximizes projected variance subject to $\|\mathbf{w}\|_2 = 1$:
$$\max_{\mathbf{w}} \mathbf{w}^T \mathbf{\Sigma} \mathbf{w} \quad \text{s.t.} \quad \mathbf{w}^T \mathbf{w} = 1$$

Lagrangian:
$$\mathcal{L}(\mathbf{w}, \lambda) = \mathbf{w}^T \mathbf{\Sigma} \mathbf{w} - \lambda (\mathbf{w}^T \mathbf{w} - 1) \implies \nabla_\mathbf{w}\mathcal{L} = 2\mathbf{\Sigma}\mathbf{w} - 2\lambda\mathbf{w} = 0 \implies \mathbf{\Sigma}\mathbf{w} = \lambda \mathbf{w}$$
The principal components are the eigenvectors of $\mathbf{\Sigma}$, ordered by descending eigenvalue $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_d$.

**Singular Value Decomposition (SVD) Implementation:**
Instead of explicitly computing $\mathbf{X}^T\mathbf{X}$ ($\mathcal{O}(nd^2)$), compute economy SVD:
$$\mathbf{X} = \mathbf{U} \mathbf{S} \mathbf{V}^T$$
- $\mathbf{V} \in \mathbb{R}^{d \times d}$: Right singular vectors (Principal Component directions).
- $\mathbf{\Sigma} = \frac{1}{n} \mathbf{V} \mathbf{S}^2 \mathbf{V}^T \implies \lambda_i = \frac{s_i^2}{n}$.
- Low-dimensional projection: $\mathbf{Z} = \mathbf{X}\mathbf{V}_k = \mathbf{U}_k \mathbf{S}_k$.

**Explained Variance Ratio:**
$$\text{EVR}_k = \frac{\lambda_k}{\sum_{j=1}^d \lambda_j} = \frac{s_k^2}{\sum_{j=1}^d s_j^2}$$

---

### 2.2 Non-Linear Manifold Learning: t-SNE vs UMAP

| Dimension | t-SNE (van der Maaten & Hinton, 2008) | UMAP (McInnes et al., 2018) |
|---|---|---|
| **Underlying Theory** | Probability divergence (Kullback-Leibler) | Riemannian geometry and algebraic topology |
| **High-Dim Similarity** | Gaussian kernel $p_{j \mid i} = \frac{\exp(-\|\mathbf{x}_i - \mathbf{x}_j\|^2 / 2\sigma_i^2)}{\sum_{k \ne i}\dots}$ | Fuzzy simplicial sets / exponential graph weights |
| **Low-Dim Kernel** | Student-$t$ distribution (1 degree of freedom) | Non-linear curve $(1 + a y^{2b})^{-1}$ |
| **Preservation** | Strict local neighborhood preservation | Both local neighborhood and **global topology** |
| **Computational Speed** | Very slow ($\mathcal{O}(n^2)$ or Barnes-Hut $\mathcal{O}(n \log n)$) | Fast ($\mathcal{O}(n)$ using nearest-neighbor descent) |
| **Parametric Projection** | No (cannot transform out-of-sample points) | Yes (can embed new out-of-sample data points) |
