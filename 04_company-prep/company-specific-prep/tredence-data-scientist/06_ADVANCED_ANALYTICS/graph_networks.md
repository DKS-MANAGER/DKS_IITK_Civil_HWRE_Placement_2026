# Graph Analytics, Network Science, and Graph Neural Networks (GNNs)

**Target Role:** Data Scientist / Associate Data Scientist | Tredence Analytics  
**Context:** IIT Kanpur Placement Season 2026–27  
**Prerequisites:** Linear Algebra, Spectral Graph Theory, Deep Learning Foundations

---

## 1. Graph Representations & Matrix Formulations

A graph $G = (V, E)$ consists of vertices (nodes) $V$ with $|V| = N$ and edges $E$ with $|E| = M$.

### 1.1 Structural Matrices
1. **Adjacency Matrix $\mathbf{A} \in \mathbb{R}^{N \times N}$:**
   $$A_{ij} = \begin{cases} w_{ij} & \text{if } (i, j) \in E \\ 0 & \text{otherwise} \end{cases}$$
2. **Degree Matrix $\mathbf{D} \in \mathbb{R}^{N \times N}$:** Diagonal matrix where $D_{ii} = \sum_j A_{ij}$.
3. **Graph Laplacian Matrix $\mathbf{L} \in \mathbb{R}^{N \times N}$:**
   $$\mathbf{L} = \mathbf{D} - \mathbf{A}$$
4. **Symmetric Normalized Laplacian $\mathbf{L}_{\text{sym}}$:**
   $$\mathbf{L}_{\text{sym}} = \mathbf{D}^{-1/2} \mathbf{L} \mathbf{D}^{-1/2} = \mathbf{I} - \mathbf{D}^{-1/2} \mathbf{A} \mathbf{D}^{-1/2}$$
   *Spectral Property:* $\mathbf{L}_{\text{sym}}$ is positive semi-definite; its eigenvalues $0 = \lambda_1 \le \lambda_2 \le \dots \le \lambda_N \le 2$ govern graph diffusion, heat flow, and spectral graph convolutions.

---

## 2. Centrality Metrics & Topological Importance

| Centrality Metric | Mathematical Formula | Analytical Intuition | Enterprise / Retail Use Case |
|---|---|---|---|
| **Degree Centrality** | $C_D(v) = \frac{\text{deg}(v)}{N - 1}$ | Direct connectivity volume | High-frequency retail hub or distribution cross-dock |
| **Closeness Centrality** | $C_C(v) = \frac{N - 1}{\sum_{u \ne v} d(v, u)}$ | Average shortest path distance to all nodes | Optimal central fulfillment warehouse placement |
| **Betweenness Centrality** | $C_B(v) = \sum_{s \ne v \ne t} \frac{\sigma_{st}(v)}{\sigma_{st}}$ | Fraction of all shortest paths passing through $v$ | Critical single point of failure in supply chain or fraud router |
| **PageRank** | $\mathbf{r} = d \mathbf{P}^T \mathbf{r} + \frac{1-d}{N}\mathbf{1}$ | Recursive prestige from high-scoring neighbors ($d = 0.85$) | Influence ranking of B2B client accounts or product virality |

---

## 3. Community Detection: Modularity & The Louvain Algorithm

Communities are subgraphs with dense internal edges and sparse external connections.

### 3.1 Newman-Girvan Modularity ($Q$)
$$Q = \frac{1}{2M} \sum_{i, j} \left[ A_{ij} - \frac{k_i k_j}{2M} \right] \delta(c_i, c_j)$$
Where $M$ is total edges, $k_i$ is degree of node $i$, $c_i$ is community of node $i$, and $\delta(c_i, c_j) = 1$ if $c_i = c_j$.
- $Q \in [-0.5, 1]$. Values above $0.3 - 0.7$ indicate strong community structure.

### 3.2 The Louvain Algorithm (Blondel et al.)
1. **Phase 1 (Local Modularity Optimization):** Each node starts in its own community. For each node $i$, compute modularity gain $\Delta Q$ of moving $i$ into neighbor $j$'s community. Move $i$ to the community maximizing positive $\Delta Q$. Repeat until local convergence.
2. **Phase 2 (Community Aggregation):** Aggregate communities into super-nodes; weight edges by the sum of inter-community link weights.
3. Iterate Phase 1 and 2 hierarchically until modularity cannot increase. Extremely fast ($\mathcal{O}(N \log N)$), scaling to tens of millions of enterprise nodes.

---

## 4. Graph Representation Learning: Node2Vec

Learns continuous low-dimensional feature representations $\mathbf{z}_v \in \mathbb{R}^d$ preserving network neighborhoods.

### 4.1 Biased Second-Order Random Walks (Grover & Leskovec, 2016)
Given a walk that traversed edge $(t, v)$ and is currently at node $v$, the unnormalized transition probability to neighbor $x$ is $\pi_{vx} = \alpha_{pq}(t, x) \cdot w_{vx}$:

$$\alpha_{pq}(t, x) = \begin{cases} 
\frac{1}{p} & \text{if } d_{tx} = 0 \text{ (Return back to } t\text{)} \\
1 & \text{if } d_{tx} = 1 \text{ (Traverse local triangle neighbor)} \\
\frac{1}{q} & \text{if } d_{tx} = 2 \text{ (Move outward to new node)}
\end{cases}$$

- **Parameter $p$ (Return Parameter):** High $p$ discourages returning, encouraging exploratory walks. Low $p$ keeps walks local (captures **Homophily / Micro-communities**).
- **Parameter $q$ (In-Out Parameter):** Low $q$ promotes DFS-like outward exploration (captures **Structural Roles**, e.g., hub vs bridge node). High $q$ promotes BFS-like local exploration.
- Generated walk sequences are fed into **Word2Vec Skip-gram with Negative Sampling** to optimize node embeddings.

---

## 5. Graph Neural Networks (GNNs)

### 5.1 The Message Passing Paradigm
At layer $k$, node $v$'s representation $\mathbf{h}_v^{(k)}$ is updated via aggregation over its local neighborhood $\mathcal{N}(v)$:

$$\mathbf{m}_v^{(k)} = \text{AGGREGATE}^{(k)}\left(\left\{ \mathbf{h}_u^{(k-1)} : u \in \mathcal{N}(v) \right\}\right)$$
$$\mathbf{h}_v^{(k)} = \text{UPDATE}^{(k)}\left(\mathbf{h}_v^{(k-1)}, \mathbf{m}_v^{(k)}\right)$$

### 5.2 Key Architectures

1. **Graph Convolutional Network (GCN - Kipf & Welling, 2017):**
   $$\mathbf{H}^{(k)} = \sigma\left( \tilde{\mathbf{D}}^{-1/2} \tilde{\mathbf{A}} \tilde{\mathbf{D}}^{-1/2} \mathbf{H}^{(k-1)} \mathbf{W}^{(k)} \right)$$
   Where $\tilde{\mathbf{A}} = \mathbf{A} + \mathbf{I}_N$ (adds self-loops) and $\tilde{\mathbf{D}}_{ii} = \sum_j \tilde{A}_{ij}$. First-order localized Chebyshev polynomial spectral approximation.

2. **Graph Attention Network (GAT - Veličković et al., 2018):**
   Replaces fixed degree-normalization with learnable self-attention coefficients:
   $$\alpha_{ij} = \frac{\exp\left(\text{LeakyReLU}\left(\mathbf{a}^T [\mathbf{W}\mathbf{h}_i \,\|\, \mathbf{W}\mathbf{h}_j]\right)\right)}{\sum_{k \in \mathcal{N}(i)} \exp\left(\text{LeakyReLU}\left(\mathbf{a}^T [\mathbf{W}\mathbf{h}_i \,\|\, \mathbf{W}\mathbf{h}_k]\right)\right)}$$
   $$\mathbf{h}_i^{(k)} = \sigma\left( \sum_{j \in \mathcal{N}(i)} \alpha_{ij} \mathbf{W} \mathbf{h}_j^{(k-1)} \right)$$

---

## 6. Enterprise Applications in Tredence Verticals

1. **Syndicate Fraud Ring Detection:**
   - Entities (Credit Cards, Phone Numbers, Device IDs, Physical Addresses, IP Addresses) modeled as a heterogeneous graph.
   - Fraud rings share intermediate identifiers. Betweenness centrality and Louvain community detection isolate tightly coupled fraudulent clusters with high precision.
2. **Supply Chain Disruption Propagation:**
   - Multi-tier supplier-factory-warehouse BOM (Bill of Materials) directed acyclic graph.
   - Simulates cascade failures: if Supplier $X$ shuts down, GNN propagates delay probabilities to downstream assembly plants.
3. **Bipartite Customer-Product Market Basket Analysis:**
   - Nodes: Customers and SKUs. Edges: Purchases.
   - Node embeddings derived from GNNs predict high-affinity cross-sell items.
