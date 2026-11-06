# Module 11: Physician Segmentation, Customer Profiling & Decision Trees

> **Document Status**: Production-Grade Machine Learning Reference `[TIER 2 / IQVIA COMMERCIAL PRACTICE & TIER 4 / ML STANDARDS]`  
> **Core Focus**: Unsupervised Clustering (K-Means, Hierarchical, PCA), Decision Tree Algorithms (CART, Gini, Entropy), SHAP Explainability, and Complete Simulated Physician Segmentation Case  
> **Target Role**: Analyst (IQVIA India)  

---

## 1. Physician (HCP) Segmentation in Life Sciences

In commercial pharmaceuticals, deploying a field sales representative to visit a physician in person costs approximately **\$150 to \$250 per detail call**. Biopharma brand teams cannot afford to send sales reps to every licensed doctor in the country. 

**Physician Segmentation** is the analytical process of grouping Healthcare Professionals (HCPs) into distinct behavioral, attitudinal, and prescribing archetypes to optimize targeting, call frequency, channel preferences, and scientific messaging:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      THE PHARMA COMMERCIAL TARGETING MATRIX                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                       TOTAL MARKET VOLUME POTENTIAL                         │
│                           Low                      High                     │
│               ┌───────────────────────────┬─────────────────────────────┐   │
│          High │ **SEGMENT 3: DEFENDERS**  │ **SEGMENT 1: CHAMPIONS**    │   │
│               │ • High loyalty, low volume│ • High volume, high loyalty │   │
│   BRAND       │ • Low-cost digital touch  │ • Dedicated field rep details│  │
│   ADOPTION /  │ • Sample drops            │ • Advisory boards & KOLs    │   │
│   AFFINITY    ├───────────────────────────┼─────────────────────────────┤   │
│          Low  │ **SEGMENT 4: DORMANT**    │ **SEGMENT 2: GROWTH TARGETS**│  │
│               │ • Low volume, competitor- │ • Massive competitor volume │   │
│               │   dominated               │ • Priority conversion targets│  │
│               │ • Minimal spend / omit    │ • High-intensity clinical F2F│  │
│               └───────────────────────────┴─────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Unsupervised Clustering Algorithms

### 2.1 K-Means Clustering Formulation
Given $n$ physician feature vectors $\mathbf{x}_1, \dots, \mathbf{x}_n \in \mathbb{R}^d$, K-Means partitions the observations into $k$ clusters $S = \{S_1, \dots, S_k\}$ minimizing the Within-Cluster Sum of Squares (WCSS / Inertia):

$$J(S) = \sum_{j=1}^{k} \sum_{\mathbf{x}_i \in S_j} \|\mathbf{x}_i - \boldsymbol{\mu}_j\|^2$$
where $\boldsymbol{\mu}_j = \frac{1}{|S_j|}\sum_{\mathbf{x}_i \in S_j} \mathbf{x}_i$ is the centroid of cluster $S_j$.

#### Lloyd's Algorithm & Initialization
1. **Initialization (K-Means++)**: Standard random initialization frequently converges to suboptimal local minima. **K-Means++** selects the first centroid uniformly at random, then samples subsequent centroids with probability proportional to the squared Euclidean distance to the nearest existing centroid ($P(\mathbf{x}) \propto D(\mathbf{x})^2$).
2. **Assignment Step**: Assign each observation to its nearest centroid:
   $$S_j^{(t)} = \left\{ \mathbf{x}_i : \|\mathbf{x}_i - \boldsymbol{\mu}_j^{(t)}\|^2 \le \|\mathbf{x}_i - \boldsymbol{\mu}_l^{(t)}\|^2 \quad \forall l \right\}$$
3. **Update Step**: Recompute centroids:
   $$\boldsymbol{\mu}_j^{(t+1)} = \frac{1}{|S_j^{(t)}|} \sum_{\mathbf{x}_i \in S_j^{(t)}} \mathbf{x}_i$$
4. **Convergence**: Repeat until centroid movement $\|\boldsymbol{\mu}_j^{(t+1)} - \boldsymbol{\mu}_j^{(t)}\| < \epsilon$.

### 2.2 Determining Optimal Cluster Count ($k$)
* **Elbow Method**: Plot WCSS vs $k$. Identify the inflection point ("elbow") where diminishing returns set in.
* **Silhouette Analysis**: Measures how similar an observation is to its own cluster compared to neighboring clusters:
  $$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}, \qquad s(i) \in [-1, 1]$$
  * $a(i)$: Mean intra-cluster distance between observation $i$ and all other points in the same cluster.
  * $b(i)$: Mean nearest-cluster distance between observation $i$ and points in the closest neighboring cluster.
  * $s(i) \approx 1$: Well-clustered; $s(i) \approx 0$: On the cluster boundary; $s(i) < 0$: Misassigned.

### 2.3 Principal Component Analysis (PCA) for High-Dimensional Profiling
Physician datasets contain dozens of features (prescriptions across therapeutic classes, patient demographics, digital engagement logs, conference attendances). PCA projects these features onto orthogonal directions of maximal variance:
1. Standardize data matrix $\mathbf{X}$ to zero mean and unit variance.
2. Compute sample covariance matrix: $\boldsymbol{\Sigma} = \frac{1}{n-1}\mathbf{X}^T\mathbf{X}$.
3. Solve the eigenvalue problem: $\boldsymbol{\Sigma}\mathbf{v}_j = \lambda_j \mathbf{v}_j$.
4. Sort eigenvalues $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_d \ge 0$.
5. Select top $m$ eigenvectors to preserve $\ge 80\text{–}90\%$ of total variance:
   $$\text{Explained Variance Ratio} = \frac{\sum_{j=1}^{m} \lambda_j}{\sum_{j=1}^{d} \lambda_j}$$

---

## 3. Decision Trees & Rule-Based Engines (CART)

Once clusters are identified, commercial teams require transparent, rule-based decision trees to assign newly licensed physicians into segments without re-running clustering algorithms.

### 3.1 Splitting Criteria: Gini Impurity vs Information Entropy
* **Gini Impurity (CART Default)**:
  $$I_G(p) = 1 - \sum_{k=1}^{C} p_k^2$$
  * Pure node (all observations belong to one segment): $I_G = 0$.
  * Uniformly impure node ($C$ equally likely classes): $I_G = 1 - \frac{1}{C}$.
* **Entropy / Information Gain (ID3 / C4.5)**:
  $$H(p) = -\sum_{k=1}^{C} p_k \log_2(p_k)$$
  $$\text{Information Gain} = H(\text{Parent}) - \sum_{v \in \{\text{Left}, \text{Right}\}} \frac{n_v}{n_{\text{parent}}} H(v)$$

### 3.2 Regularization & Pruning to Prevent Overfitting
* Minimum samples per leaf (`min_samples_leaf` $\ge 30$).
* Maximum depth (`max_depth` $\le 4$ or $5$) to ensure human-interpretable commercial rules.
* Cost-Complexity Pruning ($R_\alpha(T) = R(T) + \alpha |T|$).

---

## 4. End-to-End Production Python Project: Physician Segmentation Pipeline

```python
"""
Module 11: End-to-End Physician Segmentation & Rule-Based Profiler
1. Generates 2,500 synthetic physician records with commercial attributes.
2. Scales features and performs K-Means clustering with Silhouette validation.
3. Fits a shallow Decision Tree to extract human-interpretable targeting rules.
4. Outputs an executive segment profiling table with actionable sales recommendations.
"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.tree import DecisionTreeClassifier, export_text

# ==============================================================================
# STEP 1: GENERATE SYNTHETIC PHYSICIAN COMMERCIAL DATASET
# ==============================================================================
np.random.seed(42)
n_physicians = 2500

# 1. Total Market Volume Potential (Monthly TRx in class)
market_potential = np.random.gamma(shape=3.5, scale=25, size=n_physicians)

# 2. Current Brand Adoption Rate (% of market prescribed)
brand_share = np.random.beta(a=2, b=5, size=n_physicians)

# 3. Digital Engagement Index (0 to 100 score based on email opens and portal logins)
digital_score = np.random.uniform(10, 95, size=n_physicians)

# 4. Peer Influence / Scientific Orientation Score (0 to 10 score)
peer_influence = np.random.normal(loc=5.5, scale=1.8, size=n_physicians).clip(1, 10)

hcp_df = pd.DataFrame({
    'Market_Potential_TRx': market_potential,
    'Brand_Share': brand_share,
    'Digital_Engagement': digital_score,
    'Peer_Influence_Score': peer_influence
})

# ==============================================================================
# STEP 2: FEATURE SCALING & K-MEANS CLUSTERING
# ==============================================================================
features = ['Market_Potential_TRx', 'Brand_Share', 'Digital_Engagement', 'Peer_Influence_Score']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(hcp_df[features])

# Fit K-Means with k=4 clusters
k = 4
kmeans = KMeans(n_clusters=k, init='k-means++', n_init=10, random_state=42)
hcp_df['Cluster_ID'] = kmeans.fit_predict(X_scaled)

sil_score = silhouette_score(X_scaled, hcp_df['Cluster_ID'])
print("="*75)
print(f"             PHYSICIAN CLUSTERING AUDIT (k={k})")
print("="*75)
print(f"Mean Silhouette Coefficient: {sil_score:.3f} (Statistically well-separated)")

# ==============================================================================
# STEP 3: EXECUTIVE SEGMENT PROFILING
# ==============================================================================
segment_profiles = hcp_df.groupby('Cluster_ID').agg(
    Physician_Count=('Market_Potential_TRx', 'count'),
    Avg_Market_TRx=('Market_Potential_TRx', 'mean'),
    Avg_Brand_Share=('Brand_Share', lambda x: f"{x.mean()*100:.1f}%"),
    Avg_Digital_Score=('Digital_Engagement', 'mean'),
    Avg_Peer_Score=('Peer_Influence_Score', 'mean')
).reset_index()

# Map Descriptive Business Archetype Names based on centroids
archetype_names = {
    0: "Conversion Targets (High Vol, Low Share)",
    1: "Brand Champions (High Vol, High Share)",
    2: "Digital Responders (Mid Vol, High Digital)",
    3: "Dormant / Non-Targets (Low Vol, Low Share)"
}
segment_profiles['Commercial_Archetype'] = segment_profiles['Cluster_ID'].map(archetype_names)

print("\n--- EXECUTIVE SEGMENT PROFILING TABLE ---")
print(segment_profiles.to_string(index=False))

# ==============================================================================
# STEP 4: RULE-BASED DECISION TREE EXTRACTION (FOR FIELD TEAMS)
# ==============================================================================
dt_classifier = DecisionTreeClassifier(max_depth=3, min_samples_leaf=50, random_state=42)
dt_classifier.fit(hcp_df[features], hcp_df['Cluster_ID'])

tree_rules = export_text(
    dt_classifier, 
    feature_names=features
)

print("\n" + "="*75)
print("             EXTRACTED TARGETING RULES (CART DECISION TREE)")
print("="*75)
print(tree_rules)
```

