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
