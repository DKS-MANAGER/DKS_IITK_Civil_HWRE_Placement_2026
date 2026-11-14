# Project 4: Interview Defense & Technical Q&A

**Candidate Defense Readiness:** GenAI, RAG Architectures & Evaluation  
**Role:** Data Scientist / Associate Data Scientist | Tredence Analytics

---

### Q1. Why did you choose Hybrid Search (BM25 + Dense) instead of pure vector search?
**Defense:**  
- **The Out-of-Distribution & Exact Code Failure:** Dense embeddings map queries into general semantic subspaces. In enterprise consulting (retail, supply chain, healthcare), queries frequently contain exact alphanumeric SKU identifiers (e.g., `SKU-DAIRY-101`), legal clause numbers (`FS-88`), or ICD-10 medical billing codes. Dense vector search frequently misses exact alphanumeric tokens because their semantic proximity is diluted.
- **Complementary Synergy:** Sparse BM25 guarantees $100\%$ precision on rare keywords and exact identifiers, while Dense Vector search captures paraphrasing and conceptual intent. Combining them via Reciprocal Rank Fusion (RRF) yields the highest empirical recall across technical corpora.

---

### Q2. How does Reciprocal Rank Fusion (RRF) handle differing score scales?
**Defense:**  
- BM25 outputs unbounded positive scores based on term frequency and document length, while cosine vector similarity outputs scores bounded in $[-1, 1]$. Normalizing both scores (e.g., via min-max or sigmoid scaling) is brittle because score distributions vary drastically across queries.
- RRF bypasses score calibration entirely by utilizing **rank positions**:
  $$\text{RRF}(d) = \sum_{m \in M} \frac{1}{k + r_m(d)}$$
- Using smoothing constant $k = 60$, an item ranked #1 in both modalities scores $\frac{1}{61} + \frac{1}{61} \approx 0.0328$, easily outranking documents that appear in only one list.

---

### Q3. How do you mitigate hallucinations in enterprise generative AI?
**Defense:**  
- **System Prompt Grounding:** Strict system prompt constraints instructing the model to rely *strictly and exclusively* on the retrieved context text and respond with *"I do not have sufficient information in the provided SOPs to answer this query"* if context is absent.
- **Citation Mandate:** Requiring direct source document and sentence citations for every assertion.
- **RAG Triad Faithfulness Guardrail:** Running an automated post-generation Natural Language Inference (NLI) entailment check: if the faithfulness score drops below $0.95$, the output is intercepted before reaching the user and routed to human review.
