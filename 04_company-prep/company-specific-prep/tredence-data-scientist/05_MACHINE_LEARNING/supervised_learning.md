# Supervised Learning Algorithms: Theory, Mathematics, and Optimization

**Target Role:** Data Scientist / Associate Data Scientist | Tredence Analytics  
**Context:** IIT Kanpur Placement Season 2026–27  
**Prerequisites:** Multivariable Calculus, Gradient Descent, Linear Algebra, Probability

---

## 1. Generalized Linear Models (GLMs)

### 1.1 Ordinary Least Squares (OLS) Regression
Given feature matrix $\mathbf{X} \in \mathbb{R}^{n \times p}$ and target $\mathbf{y} \in \mathbb{R}^n$:
$$\mathbf{y} = \mathbf{X}\mathbf{w} + \boldsymbol{\epsilon}, \quad \boldsymbol{\epsilon} \sim \mathcal{N}(0, \sigma^2 \mathbf{I})$$

**Closed-Form Normal Equation:**
$$J(\mathbf{w}) = \|\mathbf{y} - \mathbf{X}\mathbf{w}\|_2^2 \implies \nabla_\mathbf{w} J(\mathbf{w}) = -2\mathbf{X}^T(\mathbf{y} - \mathbf{X}\mathbf{w}) = 0 \implies \mathbf{w}^* = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$$

*Computational Complexity:* $(\mathbf{X}^T\mathbf{X})$ inversion takes $\mathcal{O}(p^3 + np^2)$. If $p > 10,000$, use iterative Gradient Descent ($\mathcal{O}(knp)$).

### 1.2 Regularization: Ridge vs Lasso vs ElasticNet
$$\mathcal{L}_{\text{ElasticNet}}(\mathbf{w}) = \frac{1}{2n}\|\mathbf{y} - \mathbf{X}\mathbf{w}\|_2^2 + \lambda \left[\alpha \|\mathbf{w}\|_1 + \frac{1 - \alpha}{2} \|\mathbf{w}\|_2^2\right]$$

| Regularizer | Penalty Term | Geometry | Sparsity | Closed-form Solution | Collinear Features |
|---|---|---|---|---|---|
| **Ridge ($L_2$)** | $\frac{\lambda}{2} \|\mathbf{w}\|_2^2$ | Hypersphere ($L_2$ ball) | No (shrinks to zero) | $\mathbf{w}^* = (\mathbf{X}^T\mathbf{X} + \lambda \mathbf{I})^{-1}\mathbf{X}^T\mathbf{y}$ | Shrinks correlated weights equally |
| **Lasso ($L_1$)** | $\lambda \|\mathbf{w}\|_1$ | Polyhedron (corners on axes) | Yes (exact zeros) | No (Subgradient / Coordinate Descent) | Arbitrarily picks one and zeros others |
| **ElasticNet** | $\lambda_1 \|\mathbf{w}\|_1 + \lambda_2 \|\mathbf{w}\|_2^2$ | Rounded diamond | Yes | No (Coordinate Descent) | Groups and retains correlated features |

### 1.3 Logistic Regression
Models the log-odds of a binary event $y \in \{0, 1\}$:
$$p(\mathbf{x}) = P(y = 1 \mid \mathbf{x}) = \sigma(\mathbf{w}^T\mathbf{x}) = \frac{1}{1 + e^{-\mathbf{w}^T\mathbf{x}}}$$
$$\ln\left(\frac{p(\mathbf{x})}{1 - p(\mathbf{x})}\right) = \mathbf{w}^T\mathbf{x}$$

**Binary Cross-Entropy (Log-Loss) Optimization:**
$$\mathcal{L}(\mathbf{w}) = -\frac{1}{n} \sum_{i=1}^n \left[y_i \ln p(\mathbf{x}_i) + (1 - y_i) \ln(1 - p(\mathbf{x}_i))\right]$$
**Gradient:**
$$\nabla_\mathbf{w} \mathcal{L}(\mathbf{w}) = \frac{1}{n} \mathbf{X}^T (\mathbf{p} - \mathbf{y})$$
**Hessian Matrix:**
$$\mathbf{H} = \nabla_\mathbf{w}^2 \mathcal{L}(\mathbf{w}) = \frac{1}{n} \mathbf{X}^T \mathbf{S} \mathbf{X}, \quad \text{where } \mathbf{S} = \text{diag}(p_i(1 - p_i))$$
Since $p_i(1 - p_i) > 0$, $\mathbf{H}$ is positive semi-definite $\implies$ Log-loss is strictly convex with a unique global minimum solved via Newton-Raphson (Iteratively Reweighted Least Squares - IRLS).

---

## 2. Tree-Based Ensembles

### 2.1 Decision Trees (CART)
Recursively partitions feature space into orthogonal hyper-rectangles:
- **Regression:** Minimizes Mean Squared Error (Variance Reduction):
  $$\text{Split Gain} = \text{Var}(D) - \frac{|D_L|}{|D|}\text{Var}(D_L) - \frac{|D_R|}{|D|}\text{Var}(D_R)$$
- **Classification:** Minimizes Gini Impurity $I_G = 1 - \sum_{k=1}^K p_k^2$ or Entropy $H = -\sum_{k=1}^K p_k \log_2 p_k$.

### 2.2 Random Forest (Bagging + Feature Subsampling)
- **Bootstrap Aggregation:** Trains $B$ independent trees on bootstrap samples ($n$ rows sampled with replacement).
- **Random Subspace:** At each split, selects a random subset of $m = \sqrt{p}$ features (classification) or $m = p/3$ (regression).
- **Variance Reduction Formula:**
  $$\text{Var}(\bar{X}) = \rho \sigma^2 + \frac{1 - \rho}{B}\sigma^2$$
  Feature subsampling reduces the inter-tree correlation $\rho$, driving total variance toward $\rho \sigma^2$.

---

## 3. Gradient Boosting Framework

### 3.1 Mathematical Derivation (Friedman, 2001)
Given objective $\mathcal{L}(y, F_m(x))$:
1. Initialize $F_0(x) = \arg\min_\gamma \sum_{i=1}^n \mathcal{L}(y_i, \gamma)$.
2. For $m = 1$ to $M$:
   - Compute pseudo-residuals (negative gradients in function space):
     $$r_{im} = -\left[\frac{\partial \mathcal{L}(y_i, F(x_i))}{\partial F(x_i)}\right]_{F(x) = F_{m-1}(x)}$$
   - Fit base learner $h_m(x)$ to pseudo-residuals $\{x_i, r_{im}\}$.
   - Update model with shrinkage learning rate $\eta \in (0, 1]$:
     $$F_m(x) = F_{m-1}(x) + \eta \cdot h_m(x)$$

---

## 4. Modern GBDT Implementations: LightGBM vs XGBoost vs CatBoost

| Mechanism / Feature | XGBoost (Chen & Guestrin, 2016) | LightGBM (Ke et al., Microsoft 2017) | CatBoost (Prokhorenkova et al., Yandex 2018) |
|---|---|---|---|
| **Tree Growth Policy** | Level-wise (Depth-wise) | Leaf-wise (Best-first) | Symmetric / Oblivious trees |
| **Split Finding Algorithm** | Pre-sorted / Exact greedy or Weighted Quantile Sketch | **Histogram-based** (bins continuous features into 256 bins) | Ordered boosting / Minimal variance split |
| **Categorical Handling** | One-Hot or Integer encoding required | Native Fisher optimal split ($O(k \log k)$) | **Target Encoding with Ordered TS** (prevents target leakage) |
| **Speed Acceleration** | Exact histogram computation | **GOSS** (Gradient-based One-Side Sampling) + **EFB** (Exclusive Feature Bundling) | GPU optimized vectorization |
| **Memory Consumption** | High | Low ($8\times$ lower than XGBoost) | Moderate |
| **Missing Value Handling** | Learns default branch direction based on gain | Learns default branch direction | Treats as min/max value or separate category |

### 4.1 Second-Order Taylor Expansion in XGBoost
XGBoost optimizes a second-order approximation of the loss:
$$\mathcal{L}^{(t)} \approx \sum_{i=1}^n \left[ \mathcal{L}(y_i, \hat{y}^{(t-1)}) + g_i f_t(x_i) + \frac{1}{2} h_i f_t^2(x_i) \right] + \Omega(f_t)$$
Where $g_i = \partial_{\hat{y}^{(t-1)}} \mathcal{L}(y_i, \hat{y}^{(t-1)})$ and $h_i = \partial_{\hat{y}^{(t-1)}}^2 \mathcal{L}(y_i, \hat{y}^{(t-1)})$.
**Optimal Leaf Weight $w_j^*$ and Optimal Tree Split Gain:**
$$w_j^* = -\frac{\sum_{i \in I_j} g_i}{\sum_{i \in I_j} h_i + \lambda}$$
$$\text{Gain} = \frac{1}{2} \left[ \frac{\left(\sum_{i \in I_L} g_i\right)^2}{\sum_{i \in I_L} h_i + \lambda} + \frac{\left(\sum_{i \in I_R} g_i\right)^2}{\sum_{i \in I_R} h_i + \lambda} - \frac{\left(\sum_{i \in I} g_i\right)^2}{\sum_{i \in I} h_i + \lambda} \right] - \gamma$$
Where $\lambda$ controls $L_2$ leaf regularization and $\gamma$ is the minimum gain required to make a further partition (pruning penalty).
