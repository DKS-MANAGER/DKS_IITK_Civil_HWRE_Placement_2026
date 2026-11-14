# Natural Language Processing (NLP) & Sequence Modeling

**Target Role:** Data Scientist / Associate Data Scientist | Tredence Analytics  
**Context:** IIT Kanpur Placement Season 2026–27  
**Prerequisites:** Linear Algebra, Probability, Recurrent Neural Networks

---

## 1. Classical Text Processing & Vector Space Models

### 1.1 Tokenization & Subword Algorithms
- **Byte-Pair Encoding (BPE):** Iteratively merges the most frequent pair of adjacent bytes/characters. Handles Out-Of-Vocabulary (OOV) words by decomposing them into subword units (e.g., `["un", "afford", "able"]`). Standard in GPT models.
- **WordPiece:** Maximizes the language model likelihood of adding a candidate merge to the vocabulary. Standard in BERT models.

### 1.2 TF-IDF (Term Frequency - Inverse Document Frequency)
Measures the importance of term $t$ in document $d$ relative to corpus $D$:

$$\text{TF}(t, d) = \frac{f_{t, d}}{\sum_{t' \in d} f_{t', d}}$$
$$\text{IDF}(t, D) = \ln\left(\frac{1 + |D|}{1 + |\{d \in D : t \in d\}|}\right) + 1$$
$$\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \text{IDF}(t, D)$$
High TF-IDF terms are frequent within document $d$ but rare across the broader corpus, serving as distinctive topical signatures.

---

## 2. Distributed Word Embeddings

### 2.1 Word2Vec (Mikolov et al., 2013)
- **CBOW (Continuous Bag of Words):** Predicts target word $w_t$ given symmetric context words $w_{t-c}, \dots, w_{t+c}$. Faster to train; performs well on frequent words.
- **Skip-Gram with Negative Sampling (SGNS):** Predicts context words given target word $w_t$. Superior performance on rare words and specialized jargon:
  $$\mathcal{L}_{\text{SGNS}} = \ln \sigma(\mathbf{v}_{w_O}'^T \mathbf{v}_{w_I}) + \sum_{i=1}^k \mathbb{E}_{w_i \sim P_n(w)} \left[ \ln \sigma(-\mathbf{v}_{w_i}'^T \mathbf{v}_{w_I}) \right]$$

### 2.2 FastText (Bojanowski et al., Facebook 2017)
Extends Word2Vec by representing each word as a bag of character $n$-grams (e.g., `<wh`, `whe`, `her`, `ere`, `re>` for `where`).
- Computes embedding as the sum of character $n$-gram vectors.
- **Critical Capability:** Robustly generates meaningful embeddings for previously unseen Out-Of-Vocabulary (OOV) misspellings and technical domain product serial codes.

---

## 3. Recurrent Architectures: LSTM & GRU

Standard Recurrent Neural Networks (RNNs) suffer from severe vanishing gradients over long sequences due to repeated Jacobian multiplication during Backpropagation Through Time (BPTT).

```
          ┌────────────────────────────────────────────────────────┐
          │                    LSTM Cell State C_t                 │
C_{t-1} ──┴──> (X) ────────────────────────────── (+) ─────────────┴──> C_t
                ^                                  ^
                │ f_t (Forget)                     │ (i_t * ~C_t)
                │                                  │
          ┌─────┴──────┐                    ┌──────┴──────┐
          │  Sigmoid   │                    │    Tanh     │
          └─────┬──────┘                    └──────┬──────┘
                ^                                  ^
h_{t-1}, x_t ───┴──────────────────────────────────┴───────────────┴──> h_t
```

### 3.1 Long Short-Term Memory (LSTM) Equations
$$\begin{aligned}
\mathbf{f}_t &= \sigma(\mathbf{W}_f [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_f) && \text{(Forget Gate: what to erase from memory)} \\
\mathbf{i}_t &= \sigma(\mathbf{W}_i [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_i) && \text{(Input Gate: what new information to store)} \\
\tilde{\mathbf{C}}_t &= \tanh(\mathbf{W}_c [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_c) && \text{(Candidate Cell State: candidate new memories)} \\
\mathbf{C}_t &= \mathbf{f}_t \odot \mathbf{C}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{C}}_t && \text{(Cell State Update: linear additive highway)} \\
\mathbf{o}_t &= \sigma(\mathbf{W}_o [\mathbf{h}_{t-1}, \mathbf{x}_t] + \mathbf{b}_o) && \text{(Output Gate: what to expose)} \\
\mathbf{h}_t &= \mathbf{o}_t \odot \tanh(\mathbf{C}_t) && \text{(Hidden State)}
\end{aligned}$$

*Why LSTMs Solve Vanishing Gradients:* The cell state update $\mathbf{C}_t = \mathbf{f}_t \odot \mathbf{C}_{t-1} + \dots$ is linear and additive. When forget gate $\mathbf{f}_t \approx 1$, the error gradient flows back unchanged over hundreds of timesteps.

---

## 4. The Transformer Self-Attention Mechanism

Vaswani et al. (2017) eliminated recurrence entirely in favor of parallelized attention.

### 4.1 Scaled Dot-Product Attention
Given Query $\mathbf{Q}$, Key $\mathbf{K}$, and Value $\mathbf{V}$ matrices ($\mathbf{Q}, \mathbf{K} \in \mathbb{R}^{n \times d_k}, \mathbf{V} \in \mathbb{R}^{n \times d_v}$):

$$\text{Attention}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{softmax}\left(\frac{\mathbf{Q}\mathbf{K}^T}{\sqrt{d_k}}\right) \mathbf{V}$$

- **Scaling Factor $\frac{1}{\sqrt{d_k}}$:** For large $d_k$, dot products $\mathbf{q} \cdot \mathbf{k}$ grow large in magnitude, pushing the softmax function into regions with tiny gradients (gradient saturation). Dividing by $\sqrt{d_k}$ ensures variance of dot products remains $1$.

### 4.2 Multi-Head Attention (MHA)
Allows the model to jointly attend to information from different representation subspaces at different positions:

$$\text{MultiHead}(\mathbf{Q}, \mathbf{K}, \mathbf{V}) = \text{Concat}(\text{head}_1, \dots, \text{head}_h)\mathbf{W}^O$$
$$\text{where } \text{head}_i = \text{Attention}(\mathbf{Q}\mathbf{W}_i^Q, \mathbf{K}\mathbf{W}_i^K, \mathbf{V}\mathbf{W}_i^V)$$

---

## 5. Enterprise NLP in Tredence Verticals

1. **Customer Review Sentiment & Root-Cause Mining:**
   - Multi-label aspect-based sentiment extraction on e-commerce product reviews.
   - Categorizes negative reviews into supply chain drivers: "late delivery", "damaged packaging", or "sizing defect".
2. **Support Ticket Auto-Triage & Routing:**
   - Fine-tuned BERT / RoBERTa models classifying incoming B2B partner support tickets to proper resolution queues.
3. **Automated Procurement Invoice Extraction:**
   - LayoutLM and OCR models extracting structured tables, SKU descriptions, and tax totals from unstructured supplier invoices.
