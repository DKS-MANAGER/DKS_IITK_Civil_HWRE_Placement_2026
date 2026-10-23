# Topic Master 04: Machine Learning, Generative AI, RAG & Agentic Systems

> **Consolidated Module**: TOPIC-04 (Artificial Intelligence & Machine Learning)  
> **Target Assessment**: AI Track Technical Interviews, System Design & Architecture Evaluation  
> **Structure**:
> - **SECTION A**: Classical Machine Learning, Regularization Geometry (L1 vs L2), Tree Ensembles (Random Forest vs GBDT), Imbalanced Classification (PR-AUC vs ROC-AUC), Time-Series (ADF, ARIMA) & CNNs
> - **SECTION B**: Generative AI & LLMs: Transformer Self-Attention ($Q, K, V$), Few-Shot JSON Prompting, Enterprise RAG Pipeline (Chunking, Vector Embeddings, Hybrid Search + Cross-Encoder Reranking) & Offline Python RAG Script
> - **SECTION C**: Agentic Workflows, Tool Calling, Multi-Agent Supervisors, Graph Analytics, Knowledge Graphs & Graph Neural Networks (GNNs)

---

# SECTION A: Classical Machine Learning, NLP & Time-Series Analytics

# Module 06: Applied Machine Learning, NLP, Time-Series, and Computer Vision

> **Module Code**: DEL-M06  
> **Priority**: P2 (Core Role Alignment)  
> **Target Assessment**: Technical Interview Modeling Defense & Applied Analytics Cases  
> **Standard**: Complete theoretical foundations, loss functions, evaluation proofs, imbalanced metrics, time-series stationarity, and runnable Python demonstrations.

---

## 1. End-to-End Machine Learning Workflow & Problem Framing

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                       ENTERPRISE ML DELIVERY PIPELINE                       │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. Business Problem Definition ──► Framing as Regression / Classification   │
│ 2. Data Audit & Leakage Check  ──► Temporal train/test split; PII scrubbing │
│ 3. Feature Engineering         ──► Missing imputation, scaling, encodings   │
│ 4. Baseline Model Selection    ──► Simple heuristic (mean or majority class)│
│ 5. Model Training & Validation ──► Ridge, Random Forest, XGBoost (K-Fold)   │
│ 6. Rigorous Evaluation         ──► PR-AUC, ROC-AUC, Cost-weighted matrix    │
│ 7. Model Explainability        ──► SHAP value feature attribution           │
│ 8. Deployment & Drift Monitor  ──► Concept drift & retraining trigger       │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Core Supervised Algorithms & Mathematical Intuition

### 2.1 Linear Regression & Regularization (Ridge vs. Lasso)

* **Ordinary Least Squares (OLS) Objective**:
  $$\min_{\mathbf{w}} \sum_{i=1}^N (y_i - \mathbf{w}^T \mathbf{x}_i)^2$$
* **Ridge Regression (L2 Regularization)**:
  $$\min_{\mathbf{w}} \left[ \sum_{i=1}^N (y_i - \mathbf{w}^T \mathbf{x}_i)^2 + \lambda \sum_{j=1}^D w_j^2 \right]$$
  *Shrinks weights continuously towards zero; handles multicollinearity; keeps all features.*
* **Lasso Regression (L1 Regularization)**:
  $$\min_{\mathbf{w}} \left[ \sum_{i=1}^N (y_i - \mathbf{w}^T \mathbf{x}_i)^2 + \lambda \sum_{j=1}^D |w_j| \right]$$
  *Drives coefficients to exactly zero due to the diamond-shaped geometry of the L1 ball; performs automatic feature selection.*

---

### 2.2 Logistic Regression & Cross-Entropy Loss

* Maps real linear combinations to probability interval $(0, 1)$ via Sigmoid function:
  $$P(Y = 1 \mid \mathbf{x}) = \sigma(\mathbf{w}^T \mathbf{x}) = \frac{1}{1 + e^{-\mathbf{w}^T \mathbf{x}}}$$
* **Binary Cross-Entropy (Log-Loss)**:
  $$\mathcal{L}(\mathbf{w}) = - \frac{1}{N} \sum_{i=1}^N \left[ y_i \ln(\hat{y}_i) + (1 - y_i) \ln(1 - \hat{y}_i) \right]$$

---

### 2.3 Tree Ensembles: Random Forest (Bagging) vs. Gradient Boosting (Boosting)

| Dimension | Random Forest (Bagging) | Gradient Boosted Decision Trees (Boosting) |
| :--- | :--- | :--- |
| **Core Principle** | Parallel independent trees trained on bootstrap samples with random feature subsets. | Sequential trees; each tree fits the negative gradient (residual errors) of the prior ensemble. |
| **Primary Error Reduced** | **Variance** (averaging deep, high-variance trees). | **Bias** (combining shallow, weak learners into a strong learner). |
| **Parallelization** | Fully parallelizable across CPU cores. | Inherently sequential (though histogram split finding is parallelized in XGBoost/LightGBM). |
| **Sensitivity to Outliers**| Robust to noise and outliers. | More sensitive to label noise as it continually tries to correct hard outliers. |

---

## 3. Evaluation Metrics for Imbalanced Enterprise Data

In real consulting engagements (fraud detection, churn prediction, equipment failure), the positive class is rare (1% or less). **Accuracy is completely misleading**.

```text
CONFUSION MATRIX:
                  Predicted Negative    Predicted Positive
Actual Negative │ True Negative (TN)  │ False Positive (FP) │  Type I Error
Actual Positive │ False Negative (FN) │ True Positive (TP)  │  Type II Error
```

### Metrics Defined
* **Precision**: $\frac{\text{TP}}{\text{TP} + \text{FP}}$ — Out of all predicted positives, how many are actually positive? (Crucial when false alarms are expensive).
* **Recall (Sensitivity)**: $\frac{\text{TP}}{\text{TP} + \text{FN}}$ — Out of all actual positives, how many did we catch? (Crucial in medical diagnosis and fraud).
* **F1-Score**: Harmonic mean of Precision and Recall:
  $$\text{F1} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$
* **ROC-AUC vs. PR-AUC Rule**:
  * **ROC-AUC**: Plots True Positive Rate vs. False Positive Rate. Inflated on highly imbalanced data because huge numbers of True Negatives suppress the False Positive Rate.
  * **PR-AUC (Precision-Recall AUC)**: Focuses exclusively on the minority positive class. The gold standard for evaluating imbalanced enterprise models.

---

## 4. Time-Series Analysis & Forecasting

### 4.1 Classical Time-Series Decomposition
$$Y_t = T_t + S_t + C_t + I_t \quad (\text{Additive}) \quad \text{or} \quad Y_t = T_t \times S_t \times C_t \times I_t \quad (\text{Multiplicative})$$

### 4.2 Stationarity & The Augmented Dickey-Fuller (ADF) Test
* **Stationarity**: Constant mean, constant variance, and autocovariance dependent only on time lag $k$, not on absolute time $t$.
* **ADF Test**: Tests null hypothesis $H_0$: Series possesses a unit root (non-stationary). If $p < 0.05$, reject $H_0$ and conclude the series is stationary. If non-stationary, apply first-order differencing: $\Delta Y_t = Y_t - Y_{t-1}$.

---

## 5. Natural Language Processing (NLP) & Computer Vision

### 5.1 Text Representations: TF-IDF to Dense Embeddings
* **Term Frequency-Inverse Document Frequency (TF-IDF)**:
  $$\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \ln\left(\frac{N}{1 + |\{d \in D : t \in d\}|}\right)$$
  *Captures lexical importance but lacks semantic understanding (synonyms have zero overlap).*
* **Dense Embeddings (Sentence Transformers)**: Maps variable-length text to a fixed-dimensional dense vector space (e.g., 768 dimensions) where semantic similarity corresponds to vector cosine similarity:
  $$\cos(\mathbf{u}, \mathbf{v}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|}$$

### 5.2 Computer Vision Basics (CNN Architecture)
* **Convolution Operation**: Sliding a learnable weight kernel (e.g., $3 \times 3$) across an image matrix to produce feature maps capturing edges, textures, and spatial hierarchies.
* **Pooling**: Max pooling reduces spatial dimensionality while preserving dominant activations, providing translational invariance.

---

## 6. Runnable Python Demonstration: Model Training & Evaluation

```python
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, average_precision_score, roc_auc_score

# 1. Generate Synthetic Imbalanced Dataset (95% Negative, 5% Positive)
X, y = make_classification(
    n_samples=2000, 
    n_features=10, 
    weights=[0.95, 0.05], 
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)

# 2. Train Model with Class Weight Balancing
clf = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
clf.fit(X_train, y_train)

# 3. Predict Probabilities & Labels
y_pred_proba = clf.predict_proba(X_test)[:, 1]
y_pred = clf.predict(X_test)

# 4. Evaluation Outputs
print("ROC-AUC Score:", round(roc_auc_score(y_test, y_pred_proba), 4))
print("PR-AUC Score:", round(average_precision_score(y_test, y_pred_proba), 4))
print("
Classification Report:
", classification_report(y_test, y_pred))
```

---

## 7. Self-Assessment Checklist

- [ ] Can explain Ridge vs. Lasso regularization and why L1 produces sparse weights.
- [ ] Understand why Random Forest reduces variance while Gradient Boosting reduces bias.
- [ ] Confident explaining why PR-AUC is preferred over ROC-AUC for imbalanced business datasets.
- [ ] Understand Augmented Dickey-Fuller (ADF) testing for time-series stationarity.
- [ ] Able to explain the transition from TF-IDF sparse vectors to dense semantic embeddings.


---

# SECTION B: Generative AI, Prompt Engineering & Production RAG Architectures

# Module 07: Generative AI, Large Language Models, Prompt Engineering, and RAG

> **Module Code**: DEL-M07  
> **Priority**: P2 (Core Role Alignment — Major Interview Topic)  
> **Target Assessment**: Technical Screening & Applied AI Architecture Interviews  
> **Standard**: Complete theoretical foundations, Transformer mechanics, RAG design, hallucination mitigations, security guardrails, and a runnable pure-Python RAG pipeline.

---

## 1. Generative AI Foundations & Transformer Mechanics

### 1.1 Predictive ML versus Generative AI

* **Predictive ML**: Learns a mapping $f(X) \to Y$ or conditional probability $P(Y \mid X)$. Outputs a single label, numerical prediction, or probability distribution across predefined classes.
* **Generative AI (Autoregressive LLMs)**: Models the joint probability distribution of token sequences $P(w_1, w_2, \dots, w_T)$. Predicts the next token given preceding context:
  $$P(w_t \mid w_1, w_2, \dots, w_{t-1})$$
  Samples iteratively from this distribution to generate novel natural language, code, or structured JSON.

---

### 1.2 The Transformer Architecture (Self-Attention Explained)

The foundational breakthrough of the Transformer (Vaswani et al., 2017) is the **Self-Attention Mechanism**, which computes dynamic contextual relationships between all pairs of tokens in parallel, replacing sequential recurrence (RNNs).

```text
Input Tokens ──► Token Embeddings + Positional Encodings
                        │
                        ▼
            Linear Projections: Query (Q), Key (K), Value (V)
                        │
                        ▼
             Scaled Dot-Product Attention:
             Attention(Q, K, V) = softmax( (Q * K^T) / sqrt(d_k) ) * V
                        │
                        ▼
            Multi-Head Attention ──► Add & Norm (Residual)
                        │
                        ▼
            Feed-Forward Network ──► Add & Norm ──► Next Token Logits
```

#### The Query-Key-Value Analogy
* **Query ($Q$)**: What the current token is looking for (e.g., token "river" looking for related descriptors).
* **Key ($K$)**: What other tokens advertise about themselves (e.g., token "bank" advertising financial vs. geographical identity).
* **Value ($V$)**: The actual semantic information transferred if Query and Key match.
* **Scale Factor $\frac{1}{\sqrt{d_k}}$**: Prevents the dot product from exploding into regions of extremely small gradients during softmax.

---

## 2. Prompt Engineering & Structured Enterprise Output

### 2.1 Core Prompt Engineering Principles

1. **Explicit Role & Constraint Framing**: Define system identity and strict boundaries.
2. **Delimited Context**: Use triple backticks (```) or XML tags (`<context>`) to separate reference data from user instructions, preventing prompt injection.
3. **Few-Shot Exemplars**: Provide 2–3 high-quality input/output pairs to anchor output formatting and tone.
4. **Chain-of-Thought (CoT)**: Instruct the model to "think step-by-step" before generating its final answer. Forces intermediate autoregressive tokens that improve logical accuracy on reasoning tasks.

#### Enterprise Few-Shot Extraction Prompt Template
```text
System: You are an enterprise data extractor. Extract information strictly from the provided document.
Output MUST be valid JSON adhering to the schema:
{"client_name": str, "project_status": str, "contract_value_usd": float}
If an entity is absent, set its value to null. Do not invent facts.

### Example 1
Input: "Global Retail completed the migration with a budget of $450,000."
Output: {"client_name": "Global Retail", "project_status": "completed", "contract_value_usd": 450000.0}

### Example 2
Input: "Apex Healthcare is evaluating cloud options with pending allocation."
Output: {"client_name": "Apex Healthcare", "project_status": "evaluating", "contract_value_usd": null}

### Task
Input: "<context>{client_input}</context>"
Output:
```

---

## 3. Retrieval-Augmented Generation (RAG) Architecture

### 3.1 Why RAG Over Fine-Tuning?

| Decision Dimension | Retrieval-Augmented Generation (RAG) | Model Fine-Tuning (PEFT / LoRA) |
| :--- | :--- | :--- |
| **Primary Goal** | Supplying dynamic, real-time proprietary factual knowledge. | Adapting writing style, tone, specialized syntax, or vocabulary. |
| **Data Freshness** | Instant (update vector database index in seconds). | Static (requires re-training job to update facts). |
| **Hallucination Risk**| Low (answers grounded in cited source chunks). | High (model can hallucinate unverifiable facts). |
| **Auditability** | High (exact document page and sentence cited). | Black box (cannot trace specific weights to facts). |
| **Cost & Compute** | Low infrastructure cost; standard API calls. | High GPU compute cost for training and serving custom weights. |

---

### 3.2 The End-to-End RAG Pipeline

```text
Phase 1: Ingestion Pipeline (Offline)
  PDFs / Docs ──► Text Cleaning ──► Recursive Chunking ──► Embedding Model ──► Vector Index (HNSW)

Phase 2: Retrieval & Inference Pipeline (Online / Real-Time)
  User Query ──► Query Embedding ──► Top-K Vector Search ──► Re-Ranker (Cross-Encoder)
                                                                    │
                                                                    ▼ Context Injection
                                           LLM Prompt Synthesis ──► Generation with Citations
```

### 3.3 Chunking Strategies & Trade-Offs
* **Fixed-Size Chunking (e.g., 500 tokens, 100 token overlap)**: Simple to implement. May sever a critical table or thought boundary mid-sentence.
* **Recursive Character Chunking**: Splits sequentially on double newlines (`

`), single newlines (`
`), and spaces (` `) to preserve paragraph and sentence cohesion.
* **Semantic Chunking**: Computes embedding distances between consecutive sentences; inserts split boundaries when the semantic similarity drops below a threshold.

---

## 4. Hallucinations, Guardrails, and RAG Evaluation

### 4.1 Root Causes of Hallucination in RAG
1. **Retrieval Failure**: The relevant chunk was not in the top-$K$ search results.
2. **Context Stuffing / Lost in the Middle**: LLMs attend heavily to the beginning and end of long prompts, sometimes ignoring chunks in the middle.
3. **Over-Confidence**: When context lacks an answer, the model relies on pre-trained parametric memory instead of abstaining.

### 4.2 The RAGAS Evaluation Framework
* **Faithfulness**: Are all claims in the generated response grounded in the retrieved context?
* **Answer Relevance**: Does the generated response directly address the user's prompt?
* **Context Precision**: Are the retrieved chunks actually relevant to the query, or is the context filled with noise?
* **Context Recall**: Did the retrieval pipeline capture all facts needed to answer the question?

---

## 5. Runnable Pure-Python RAG Pipeline (Offline Demonstration)

This self-contained implementation demonstrates document chunking, synthetic embedding projection, cosine similarity retrieval, and grounded answer synthesis without requiring external API keys.

```python
import math
from typing import List, Dict, Any

class SimpleVectorRAG:
    def __init__(self):
        self.documents: List[Dict[str, Any]] = []
        # Fixed vocabulary for a deterministic bag-of-words pseudo-embedding
        self.vocab = [
            "deloitte", "consulting", "cloud", "aws", "azure", "lakehouse",
            "snowflake", "pipeline", "etl", "governance", "security", "ai"
        ]
        
    def _embed(self, text: str) -> List[float]:
        """Deterministic normalized term-frequency embedding vector."""
        tokens = text.lower().split()
        vec = [tokens.count(w) for w in self.vocab]
        norm = math.sqrt(sum(x**2 for x in vec))
        return [x / norm if norm > 0 else 0.0 for x in vec]
        
    def _cosine_similarity(self, v1: List[float], v2: List[float]) -> float:
        return sum(a * b for a, b in zip(v1, v2))
        
    def add_document(self, doc_id: str, content: str):
        embedding = self._embed(content)
        self.documents.append({"id": doc_id, "content": content, "embedding": embedding})
        
    def retrieve(self, query: str, top_k: int = 2) -> List[Dict[str, Any]]:
        query_vec = self._embed(query)
        scored = []
        for doc in self.documents:
            sim = self._cosine_similarity(query_vec, doc["embedding"])
            scored.append((sim, doc))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [doc for sim, doc in scored[:top_k] if sim > 0.0]

    def answer_query(self, query: str) -> str:
        retrieved_docs = self.retrieve(query, top_k=2)
        if not retrieved_docs:
            return "Abstention: Insufficient relevant context in knowledge base to answer reliably."
            
        context_str = " | ".join([f"[{d['id']}]: {d['content']}" for d in retrieved_docs])
        return f"Synthesized Response grounded in Context: {context_str}"

# Execution Verification
rag = SimpleVectorRAG()
rag.add_document("DOC-1", "Deloitte USI delivers enterprise cloud migrations using AWS and Snowflake lakehouse pipelines.")
rag.add_document("DOC-2", "Healthcare compliance requires strict data security governance and patient record masking.")
rag.add_document("DOC-3", "Automated marketing campaigns leverage real-time analytics to drive customer engagement.")

print(rag.answer_query("How does Deloitte handle cloud lakehouse pipelines?"))
# Returns grounded context citing DOC-1

print(rag.answer_query("What is the capital of France?"))
# Returns Abstention response!
```

---

## 6. Self-Assessment Checklist

- [ ] Can explain the mathematical Query-Key-Value mechanism of Self-Attention.
- [ ] Understand few-shot prompting, chain-of-thought, and structured JSON extraction.
- [ ] Confident articulating the business and technical trade-offs between RAG and Fine-Tuning.
- [ ] Mastered chunking strategies, vector database indexing (HNSW), and hybrid search.
- [ ] Understand RAGAS evaluation metrics (Faithfulness, Context Precision, Answer Relevance).


---

# SECTION C: Agentic Workflows, Knowledge Graphs & Graph Analytics

# Module 08: Agentic AI, Graph Analytics, and Knowledge Graphs

> **Module Code**: DEL-M08  
> **Priority**: P3 (Specialized Breadth — Explicit JD Requirement)  
> **Target Assessment**: Advanced Technical Interviews & Technology Architecture Defense  
> **Standard**: Complete theoretical foundations, agent loop mechanics, graph algorithms, Cypher syntax, GNN message passing intuition, and enterprise fraud/relationship use cases.

---

## 1. Part A: Agentic AI & Autonomous Workflows

### 1.1 From LLM Calls to Autonomous Agents

```text
Level 1: Zero-Shot LLM Call
  User Prompt ──► LLM ──► Text Output
  • Fixed, single step. No real-time data, no external tools.

Level 2: Retrieval-Augmented Generation (RAG)
  User Prompt ──► Vector Search ──► LLM + Context ──► Grounded Text Output
  • Read-only access to external documents. Deterministic, single-hop retrieval.

Level 3: Autonomous Agent (The ReAct Loop)
  User Goal ──► LLM Reasoner (Thought)
                     │
                     ▼
                 Action (Tool Selection: SQL / API / Search)
                     │
                     ▼
                 Environment Execution (Observation)
                     │
                     ▼
                 Reflection / State Update ──► Loop until Goal or Stopping Criterion!
```

---

### 1.2 Tool Calling Mechanics & Function Schemas

Modern LLMs do not execute code directly; they output structured JSON calling signatures matching a predefined tool schema:

```json
{
  "name": "query_enterprise_erp",
  "description": "Fetches real-time inventory levels from SAP S/4HANA for a given SKU",
  "parameters": {
    "type": "object",
    "properties": {
      "sku_code": {"type": "string", "description": "Unique material master ID"},
      "plant_id": {"type": "string", "description": "Manufacturing facility code"}
    },
    "required": ["sku_code", "plant_id"]
  }
}
```

### 1.3 Agent Orchestration Architectures
* **Single-Agent System**: One LLM maintains thought history, calls tools sequentially, and decides completion. High risk of infinite loops or context degradation on complex multi-step tasks.
* **Hierarchical Multi-Agent System (Manager-Worker)**:
  * **Supervisor / Router Agent**: Decomposes high-level client brief into subtasks; delegates tasks to specialized subagents; aggregates results.
  * **Specialist Subagents**: Dedicated prompts and constrained tools (e.g., *SQL Agent*, *Code Interpreter Agent*, *Report Drafting Agent*).

### 1.4 Guardrails, Loop Detection, and When NOT to Use Agents
* **Loop Prevention**: Maintain a global step counter (e.g., `max_iterations = 8`); detect duplicate tool calls with identical parameters.
* **Human-in-the-Loop (HITL)**: Mandatory manual confirmation gates for destructive actions (database updates, email dispatch, financial trades).
* **Consulting Pragmatism Rule**: If a business process follows a deterministic sequence of steps (e.g., monthly payroll calculation), **do not use an autonomous agent**. Deterministic code (Python script / Airflow DAG) is 100x cheaper, 10x faster, and has zero probability of hallucinated drift.

---

## 2. Part B: Graph Analytics & Knowledge Graphs

### 2.1 Graph Foundations & Network Theory

A graph $G = (V, E)$ consists of vertices (nodes) $V$ and edges $E$.
* **Adjacency Matrix ($A$)**: $A_{ij} = 1$ if edge $(i, j) \in E$, else $0$. Space: $O(|V|^2)$. Efficient for dense graphs, wasteful for sparse graphs.
* **Adjacency List**: Maps each node to its immediate neighbors. Space: $O(|V| + |E|)$. Optimal for real-world sparse enterprise networks.

### 2.2 Network Centrality Metrics & Enterprise Meaning

| Centrality Metric | Mathematical Definition | Consulting & Enterprise Application |
| :--- | :--- | :--- |
| **Degree Centrality** | $C_D(v) = \text{deg}(v)$ | Identifying high-volume transaction hubs or active communication nodes. |
| **Betweenness Centrality** | $C_B(v) = \sum_{s \ne v \ne t} \frac{\sigma_{st}(v)}{\sigma_{st}}$ | Detecting critical bridge nodes or single-point-of-failure suppliers in supply chains. |
| **Closeness Centrality** | $C_C(v) = \frac{1}{\sum_{u \ne v} d(v, u)}$ | Finding central distribution warehouses that minimize transit latency across a network. |
| **PageRank** | $PR(v) = \frac{1-d}{|V|} + d \sum_{u \in M(v)} \frac{PR(u)}{L(u)}$ | Measuring systemic importance in interconnected banking or interbank counterparty networks. |

---

### 2.3 Knowledge Graphs & Property Graph Querying (Cypher)

* **Knowledge Graph**: A structured semantic network storing real-world entities (nodes) connected by typed relationships (edges) with explicit schema constraints and entity resolution.
* **Property Graph Example (Neo4j / Cypher)**:

```cypher
// Query: Identify potential synthetic fraud rings sharing accounts or phone numbers
MATCH (c1:Customer)-[:HAS_IDENTIFIER]->(id:PhoneNumber)<-[:HAS_IDENTIFIER]-(c2:Customer)
WHERE c1.customer_id <> c2.customer_id
MATCH (c1)-[t:TRANSFERRED_FUNDS]->(c2)
RETURN c1.customer_id, c2.customer_id, id.value, t.amount
ORDER BY t.amount DESC;
```

---

### 2.4 Graph Neural Networks (GNN) Intuition: Message Passing

Standard neural networks cannot handle non-Euclidean graph topologies with variable node degrees. **Graph Neural Networks (GNNs)** solve this via **Neighborhood Aggregation (Message Passing)**:

```text
Step 1: Aggregate messages from local neighbors
  a_v^(k) = AGGREGATE( { h_u^(k-1) : u ∈ N(v) } )   [e.g., Sum, Mean, Max]

Step 2: Update target node representation
  h_v^(k) = UPDATE( h_v^(k-1), a_v^(k) )            [e.g., Linear layer + ReLU]
```

At layer $k$, node $v$ incorporates information from its $k$-hop neighborhood. Enables high-accuracy node classification (fraud detection) and link prediction (recommendation engines).

---

## 3. Self-Assessment Checklist

- [ ] Can articulate the transition from Zero-Shot LLM calls to the ReAct autonomous loop.
- [ ] Understand why multi-agent systems use supervisor routers and when deterministic scripts are preferred.
- [ ] Mastered degree, betweenness, and PageRank centralities in business context.
- [ ] Can read and write basic Cypher pattern matching queries (`MATCH ... WHERE ... RETURN`).
- [ ] Understand the 2-step intuition of GNN message passing (Aggregate and Update).
