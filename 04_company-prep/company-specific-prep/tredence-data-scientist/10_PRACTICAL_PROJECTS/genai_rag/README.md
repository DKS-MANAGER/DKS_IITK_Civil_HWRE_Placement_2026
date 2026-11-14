# Project 4: Enterprise Hybrid Search RAG Pipeline & Evaluation

**Domain:** Enterprise Generative AI & Knowledge Retrieval  
**Stack:** Python, NumPy, BM25, Reciprocal Rank Fusion, Cross-Encoder Re-Ranking  
**Focus:** Lexical vs Semantic Search, Hybrid RRF, Cross-Attention Re-Ranking, RAG Triad

---

## 1. Project Overview

This project implements a multi-stage production Retrieval-Augmented Generation (RAG) pipeline designed for technical enterprise document querying (e.g., retail SOPs, vendor contracts, procurement policies).

### Key Technical Pillars:
1. **Hybrid Retrieval:** Blends sparse lexical matching (BM25 for exact SKU/policy codes) with dense semantic vector retrieval (capturing semantic intent).
2. **Reciprocal Rank Fusion (RRF):** Merges ranked candidate lists without requiring score normalization.
3. **Cross-Encoder Neural Re-Ranking:** Simulates deep all-to-all cross-attention scoring on the top-50 candidates to select the top-5 most relevant context passages.
4. **RAG Triad Faithfulness Audit:** Automatically parses generated claims and scores factual consistency against retrieved context to prevent hallucinations.

---

## 2. File Structure

- `rag_pipeline.py`: Fully reproducible Python script implementing chunking, BM25, vector search, RRF, cross-encoder re-ranking, and automated faithfulness evaluation.
- `interview_defense.md`: Technical defense explaining hybrid search trade-offs, chunking strategies, and hallucination guardrail architectures.
