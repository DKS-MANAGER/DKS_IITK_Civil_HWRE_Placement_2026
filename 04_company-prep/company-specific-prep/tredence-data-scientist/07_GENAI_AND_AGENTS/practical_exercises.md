# 25 Solved GenAI & AI Agent Technical Exercises

**Target Role:** Data Scientist / Associate Data Scientist | Tredence Analytics  
**Context:** IIT Kanpur Placement Season 2026–27  
**Coverage:** Attention Mathematics, LoRA Derivations, Vector Search Complexity, RRF Fusion, RAG Triad, Tool Calling

---

### Q1. Transformer Self-Attention Memory Complexity
**Problem:** A transformer layer processes a sequence of length $L = 4,096$ with hidden dimension $d = 4,096$. Calculate the number of elements in the self-attention weight matrix $\mathbf{Q}\mathbf{K}^T$ and calculate the memory required to store this single matrix in 16-bit float (FP16).  
**Solution:**
- The attention matrix $\mathbf{A} = \mathbf{Q}\mathbf{K}^T$ has dimension $L \times L = 4,096 \times 4,096 = 16,777,216$ elements ($16.78\text{M}$ entries).
- FP16 stores each number in 2 bytes.
- $\text{Memory} = 16,777,216 \times 2 \text{ bytes} = 33,554,432 \text{ bytes} = 32 \text{ MB}$ per attention head.
- For $h = 32$ heads, the un-fused attention maps consume $32 \times 32 \text{ MB} = 1,024 \text{ MB} = 1.0 \text{ GB}$ per layer per sample. (FlashAttention solves this by tiling without materializing the $L \times L$ matrix in HBM).

---

### Q2. LoRA Trainable Parameter Reduction
**Problem:** A linear projection weight in a 7B LLM has dimensions $d_{\text{in}} = 4,096$ and $d_{\text{out}} = 4,096$. We apply LoRA with rank $r = 16$. Calculate the number of parameters in the original frozen layer, the number of trainable LoRA parameters, and the percentage reduction in trainable parameters.  
**Solution:**
- Original frozen weight $\mathbf{W}_0$: $4,096 \times 4,096 = 16,777,216$ parameters.
- LoRA low-rank decomposition: $\mathbf{B} \in \mathbb{R}^{4096 \times 16}$ and $\mathbf{A} \in \mathbb{R}^{16 \times 4096}$.
- Total LoRA parameters: $(4,096 \times 16) + (16 \times 4,096) = 65,536 + 65,536 = 131,072$ parameters.
- $\text{Reduction} = 1 - \frac{131,072}{16,777,216} = 1 - 0.0078125 = 99.22\%$ parameter reduction.

---

### Q3. Reciprocal Rank Fusion (RRF) Calculation
**Problem:** In an enterprise hybrid search engine ($k = 60$), Document $D_1$ is ranked #2 by BM25 and #8 by Dense Vector Search. Document $D_2$ is ranked #1 by BM25 and #25 by Dense Search. Document $D_3$ is ranked #4 by BM25 and #4 by Dense Search. Compute RRF scores and determine the final ranking.  
**Solution:**
$$\text{RRF}(D) = \frac{1}{60 + r_{\text{BM25}}} + \frac{1}{60 + r_{\text{Dense}}}$$
- $\text{RRF}(D_1) = \frac{1}{60 + 2} + \frac{1}{60 + 8} = \frac{1}{62} + \frac{1}{68} \approx 0.016129 + 0.014706 = 0.030835$.
- $\text{RRF}(D_2) = \frac{1}{60 + 1} + \frac{1}{60 + 25} = \frac{1}{61} + \frac{1}{85} \approx 0.016393 + 0.011765 = 0.028158$.
- $\text{RRF}(D_3) = \frac{1}{60 + 4} + \frac{1}{60 + 4} = \frac{1}{64} + \frac{1}{64} = \frac{2}{64} = 0.031250$.
**Final Ranking:**
1. **$D_3$ (Score: $0.03125$)** — Consistent high performance across both modalities wins.
2. **$D_1$ (Score: $0.03084$)**
3. **$D_2$ (Score: $0.02816$)**

---

### Q4. Cosine Similarity vs Dot Product on Normalized Vectors
**Problem:** Two embeddings are $\mathbf{u} = [0.6, 0.8]$ and $\mathbf{v} = [0.8, -0.6]$. Verify whether they are unit-normalized and compute their Cosine Similarity and Euclidean Distance.  
**Solution:**
- $\|\mathbf{u}\| = \sqrt{0.6^2 + 0.8^2} = \sqrt{0.36 + 0.64} = 1.0$.
- $\|\mathbf{v}\| = \sqrt{0.8^2 + (-0.6)^2} = \sqrt{0.64 + 0.36} = 1.0$. Both are unit-normalized.
- $\cos(\theta) = \mathbf{u} \cdot \mathbf{v} = (0.6 \times 0.8) + (0.8 \times -0.6) = 0.48 - 0.48 = 0.0$ (Orthogonal).
- $\|\mathbf{u} - \mathbf{v}\|_2 = \sqrt{2 - 2\cos(\theta)} = \sqrt{2 - 0} = \sqrt{2} \approx 1.4142$.

---

### Q5. RAG Triad Faithfulness Calculation
**Problem:** An LLM generates an answer containing 5 distinct factual claims in response to a customer query. An automated evaluator audits the retrieved context: 4 claims are directly supported by context text, while 1 claim mentions a warranty policy not present in the retrieved text. Calculate the Faithfulness score.  
**Solution:**
$$\text{Faithfulness} = \frac{\text{Grounded Claims}}{\text{Total Generated Claims}} = \frac{4}{5} = 0.80 \ (80\%)$$
Threshold for enterprise deployment is typically $\ge 0.95$. A score of $0.80$ triggers an automated hallucination guardrail block.

---

### Q6. HNSW Graph Search vs Flat Index Speedup
**Problem:** A corporate vector database holds $N = 1,000,000$ documents with dimension $d = 1,536$. A Flat index requires calculating distances against all $N$ vectors. An HNSW index searches $\approx M \cdot \log_2(N)$ nodes, where $M = 32$. Calculate the theoretical operation reduction factor.  
**Solution:**
- Flat Index distance computations: $1,000,000$.
- HNSW distance computations: $32 \times \log_2(1,000,000) \approx 32 \times 20 = 640$.
- $\text{Reduction Factor} = \frac{1,000,000}{640} = 1,562.5\times$ fewer vector comparisons.

---

### Q7. KV-Cache Memory Calculation in LLM Inference
**Problem:** In autoregressive decoding for a batch size $B = 4$, context sequence length $L = 2,048$, number of layers $N_{\text{layers}} = 32$, hidden dimension $d = 4,096$, in FP16 (2 bytes). How much GPU RAM is consumed by Key-Value (KV) caching?  
**Solution:**
For each token, layer, and batch item, we store Key vector ($d$) and Value vector ($d$):
$$\text{KV Cache Bytes} = 2 \times (\text{Key} + \text{Value}) \times B \times L \times N_{\text{layers}} \times d_{\text{layer}}$$
$$\text{KV Cache Bytes} = 2 \times 2 \times 4 \times 2,048 \times 32 \times 4,096 \text{ bytes} = 4,294,967,296 \text{ bytes} = 4.0 \text{ GB}$$

---

### Q8. Temperature and Top-p Sampling Distribution
**Problem:** An LLM outputs raw logits for 3 candidate tokens: $[2.0, 1.0, 0.0]$. Compute the softmax probability distribution under: (a) Temperature $T = 1.0$, and (b) Temperature $T = 0.5$.  
**Solution:**
- **(a) $T = 1.0$:** Logits remain $[2, 1, 0]$.
  $e^2 \approx 7.389, e^1 \approx 2.718, e^0 = 1.0 \implies \sum = 11.107$.
  $P = [7.389/11.107, 2.718/11.107, 1.0/11.107] = [0.665, 0.245, 0.090]$.
- **(b) $T = 0.5$:** Scaled logits $[2/0.5, 1/0.5, 0/0.5] = [4, 2, 0]$.
  $e^4 \approx 54.598, e^2 \approx 7.389, e^0 = 1.0 \implies \sum = 62.987$.
  $P = [54.598/62.987, 7.389/62.987, 1.0/62.987] = [0.867, 0.117, 0.016]$.
*Conclusion:* Lower temperature sharpens the distribution, making the top token much more likely (less creative, more deterministic).

---

### Q9. BM25 Term Frequency Saturation
**Problem:** In BM25, the TF component is $\frac{f(q, D) \cdot (k_1 + 1)}{f(q, D) + k_1 \cdot (1 - b + b \frac{|D|}{\text{avgdl}})}$. If $k_1 = 1.5, b = 0.75, |D| = \text{avgdl}$, compare the score contribution when term frequency $f = 1$ vs $f = 10$ vs $f = 100$.  
**Solution:**
When $|D| = \text{avgdl}$, the denominator simplifies to $f + k_1 = f + 1.5$.
Numerator factor is $f \times (1.5 + 1) = 2.5f$.
- $f = 1$: $\frac{2.5(1)}{1 + 1.5} = \frac{2.5}{2.5} = 1.0$.
- $f = 10$: $\frac{2.5(10)}{10 + 1.5} = \frac{25}{11.5} \approx 2.174$.
- $f = 100$: $\frac{2.5(100)}{100 + 1.5} = \frac{250}{101.5} \approx 2.463$.
*Asymptotic limit:* $\lim_{f \to \infty} \frac{2.5f}{f + 1.5} = 2.5$. Unlike standard TF which grows linearly or logarithmically without bound, BM25 saturates cleanly at $k_1 + 1 = 2.5$.

---

### Q10. Token Chunk Overlap Redundancy Ratio
**Problem:** A 10,000-token enterprise document is chunked with chunk size $C = 500$ tokens and overlap $O = 100$ tokens. Calculate the total number of chunks created and the total number of tokens stored across all chunks.  
**Solution:**
- Stride $S = C - O = 500 - 100 = 400$ tokens.
- Number of chunks $N = \left\lceil \frac{10,000 - 500}{400} \right\rceil + 1 = \left\lceil \frac{9,500}{400} \right\rceil + 1 = 24 + 1 = 25$ chunks.
- Total tokens stored $= 25 \times 500 = 12,500$ tokens ($25\%$ storage expansion due to overlap).

---

### Q11. Direct Preference Optimization (DPO) Loss Calculation
**Problem:** In a DPO training step with $\beta = 0.1$, for a prompt $x$, candidate winner $y_w$ has log-ratio $\ln \frac{\pi_\theta(y_w \mid x)}{\pi_{\text{ref}}(y_w \mid x)} = 1.5$, and loser $y_l$ has log-ratio $\ln \frac{\pi_\theta(y_l \mid x)}{\pi_{\text{ref}}(y_l \mid x)} = -0.5$. Calculate the implicit reward difference and the DPO loss $\mathcal{L}_{\text{DPO}}$.  
**Solution:**
$$\Delta r = \beta \left( \ln \frac{\pi_\theta(y_w \mid x)}{\pi_{\text{ref}}(y_w \mid x)} - \ln \frac{\pi_\theta(y_l \mid x)}{\pi_{\text{ref}}(y_l \mid x)} \right) = 0.1 \times [1.5 - (-0.5)] = 0.1 \times 2.0 = 0.20$$
$$\mathcal{L}_{\text{DPO}} = -\ln \sigma(\Delta r) = -\ln \sigma(0.20)$$
$$\sigma(0.20) = \frac{1}{1 + e^{-0.20}} = \frac{1}{1 + 0.8187} = \frac{1}{1.8187} \approx 0.5498$$
$$\mathcal{L}_{\text{DPO}} = -\ln(0.5498) \approx 0.598$$

---

### Q12. Product Quantization Compression Ratio
**Problem:** Original embeddings have dimension $d = 1,024$ stored as 32-bit floats (4 bytes each). We apply Product Quantization (PQ) by dividing each vector into $m = 64$ subvectors of dimension 16, and quantizing each subvector to 256 cluster centroids (represented by an 8-bit unsigned integer). Calculate the compressed size per vector and the compression ratio.  
**Solution:**
- Original size: $1,024 \times 4 \text{ bytes} = 4,096 \text{ bytes}$.
- Compressed PQ size: $m = 64$ subvectors $\times 1 \text{ byte (8-bit index)} = 64 \text{ bytes}$.
- $\text{Compression Ratio} = \frac{4,096}{64} = 64\times$ smaller ($98.44\%$ RAM reduction).

---

### Q13. ReAct Loop Maximum Horizon Guard
**Problem:** An autonomous SQL data agent enters an infinite loop executing invalid SQL commands that throw runtime exceptions. Design the termination condition for the orchestrator.  
**Solution:**
Enforce a triple-guard termination policy:
1. `max_iterations = 5` (hard cut-off on ReAct cycles).
2. `error_history_dedup`: If the exact same SQL error message is encountered twice in succession, abort and trigger human-in-the-loop fallback.
3. `budget_timeout`: Maximum elapsed execution wall time $= 30\text{ seconds}$.

---

### Q14. Cross-Encoder Re-ranking Latency Budgeting
**Problem:** A customer service bot must maintain a total end-to-end response SLA of $\le 500\text{ ms}$. Network round-trip takes $80\text{ ms}$, Hybrid Retrieval takes $35\text{ ms}$, and LLM token generation takes $300\text{ ms}$. How much time remains for Cross-Encoder re-ranking, and how many candidate documents can be re-ranked if each candidate takes $1.5\text{ ms}$ on GPU?  
**Solution:**
- Allocated time $= 80 + 35 + 300 = 415\text{ ms}$.
- Available budget $= 500 - 415 = 85\text{ ms}$.
- Max re-rankable documents $= \left\lfloor \frac{85\text{ ms}}{1.5\text{ ms/doc}} \right\rfloor = 56$ documents. (Safe setting: Top 50 candidates).

---

### Q15. HyDE (Hypothetical Document Embedding) Failure Modes
**Problem:** When can HyDE perform worse than direct query embedding search?  
**Solution:**
1. **Highly obscure/niche domain jargon:** The LLM hallucinates incorrect domain entities in its hypothetical answer, steering vector search toward completely wrong document clusters.
2. **Fact verification / Counter-intuitive queries:** If the user asks *"Did Brand X file for bankruptcy in 2024?"*, an ungrounded LLM may author a confident hypothetical story detailing a fictitious bankruptcy, retrieving false documents.

---

### Q16. Semantic Chunking Cutoff Criterion
**Problem:** In semantic chunking, adjacent sentence cosine similarities are: $[0.92, 0.88, 0.85, 0.42, 0.89, 0.91]$. Where should the document be split?  
**Solution:**
Between sentence 3 and sentence 4, where similarity drops drastically to $0.42$. This indicates a major topical transition in the document text.

---

### Q17. Tool Calling Schema Validation Failure
**Problem:** An LLM generates a tool call for `calculate_safety_stock(sku="SKU102", service_level="95%")`. The Pydantic schema expects `service_level: float = Field(ge=0.0, le=1.0)`. How should the agent system handle this?  
**Solution:**
Catch the Pydantic `ValidationError`. Pass the error message back to the LLM as an environment observation: *"ValidationError: Value '95%' is not a valid float. Expected a float between 0.0 and 1.0 (e.g., 0.95)."* The LLM then re-generates the corrected tool call: `calculate_safety_stock(sku="SKU102", service_level=0.95)`.

---

### Q18. Multi-Head Attention Parameter Count
**Problem:** In an LLM with hidden dimension $d_{\text{model}} = 4,096$, how many parameters are in the Multi-Head Attention layer with projections $\mathbf{W}^Q, \mathbf{W}^K, \mathbf{W}^V, \mathbf{W}^O$ (ignoring biases)?  
**Solution:**
Each projection matrix is $\mathbb{R}^{d_{\text{model}} \times d_{\text{model}}} = 4,096 \times 4,096 = 16,777,216$ parameters.
$$\text{Total Parameters} = 4 \times (4,096 \times 4,096) = 67,108,864 \text{ parameters } (\approx 67.1\text{M parameters})$$

---

### Q19. RoPE (Rotary Position Embedding) Mechanism
**Problem:** Why did RoPE replace absolute learnable position embeddings in modern LLMs?  
**Solution:**
- Absolute embeddings add a static position vector to the token embedding, which struggles to extrapolate to sequence lengths longer than seen during pretraining.
- RoPE encodes relative positional information by rotating the Query and Key vectors in 2D chunks of the complex plane:
  $$\langle \mathbf{R}_{\Theta, m}^d \mathbf{q}, \mathbf{R}_{\Theta, n}^d \mathbf{k} \rangle = g(\mathbf{q}, \mathbf{k}, m - n)$$
- The inner product depends strictly on relative token distance $m - n$, enabling natural length generalization and smooth decay with distance.

---

### Q20. LLM Judge Position Bias Experiment
**Problem:** An LLM-as-a-Judge evaluates Candidate A and Candidate B. When prompt presents $[A, B]$, it chooses $A$ with score 4.5 vs 3.5. When order is flipped to $[B, A]$, it chooses $B$ with score 4.2 vs 3.8. What should the system do?  
**Solution:**
The evaluator exhibits severe position bias (systematically picking the first candidate). The outcome is ambiguous. Treat as a **tie**, average the scores ($A: 4.15, B: 4.0$), or route to an independent secondary model (or human annotator) for tie-breaking.

---

### Q21. Prompt Injection Canary Tokens
**Problem:** How does a canary token detect direct system prompt leakage?  
**Solution:**
Inject a secret randomized UUID string into the hidden system prompt (e.g., `"Canary: 9f8b7a6c"`). Inspect every outgoing agent response. If the canary string appears in the response, trigger an immediate security kill-switch and log a prompt extraction jailbreak attempt.

---

### Q22. GPU VRAM Sizing for 70B Model in 4-Bit
**Problem:** How much VRAM is required to load a 70-billion parameter model quantized to 4-bit (NF4)?  
**Solution:**
- 70 billion parameters $\times 0.5 \text{ bytes per parameter (4 bits)} = 35 \text{ GB}$.
- Add $\sim 20\%$ overhead for quantization scales, metadata, and CUDA runtime context: $35 \times 1.20 = 42 \text{ GB}$.
- Fits comfortably inside a single 48GB GPU (e.g., NVIDIA A6000 or A100-80GB).

---

### Q23. Bounded Context Window Budgeting
**Problem:** An LLM has an 8,192-token context window. System prompt takes 500 tokens. The maximum generated answer is capped at 1,000 tokens. The user query takes 100 tokens. How many tokens remain for retrieved RAG context chunks?  
**Solution:**
$$\text{Remaining Context Budget} = 8,192 - (500 + 1,000 + 100) = 8,192 - 1,600 = 6,592 \text{ tokens}$$
Can safely inject up to 13 chunks of 500 tokens each.

---

### Q24. Quantization: INT8 vs FP16 Precision Loss
**Problem:** What is the primary difference between Uniform Quantization and NormalFloat4 (NF4) Quantization?  
**Solution:**
- Uniform INT8 splits the min-max range into equal intervals. However, neural network weights follow a bell-shaped Gaussian distribution; most weights cluster tightly around zero. Uniform quantization wastes discrete quantization buckets on empty outer tails.
- NF4 (NormalFloat4) constructs quantization bins based on the empirical quantiles of a standard normal distribution $\mathcal{N}(0, 1)$, ensuring equal information entropy per bucket and preserving model perplexity.

---

### Q25. Evaluator-Optimizer Convergence Criterion
**Problem:** In an automated business report generator, when should an Evaluator-Optimizer loop terminate?  
**Solution:**
Terminate when:
1. Critic rubric score $\ge 4.5 / 5.0$ (Quality threshold achieved), OR
2. Iteration count reaches $N_{\max} = 3$ (Cost and latency cap), OR
3. Score delta between consecutive iterations $\Delta \le 0.1$ (Marginal refinement plateau).
