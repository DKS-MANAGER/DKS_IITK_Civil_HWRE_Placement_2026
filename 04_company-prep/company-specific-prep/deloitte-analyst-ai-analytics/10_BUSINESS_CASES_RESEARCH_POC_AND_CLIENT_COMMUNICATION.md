# Module 10: Business Cases, PoC Engineering, and Executive Communication

> **Module Code**: DEL-M10  
> **Priority**: P2 (Core Role Alignment — High Interview Weight)  
> **Target Assessment**: Case Interviews, Technology Consulting Scenarios & Partner Round  
> **Standard**: Complete MECE problem decomposition, issue trees, PoC frameworks, executive slide architecture, and 7 detailed worked enterprise business cases.

---

## 1. Structured Consulting Problem-Solving Frameworks

### 1.1 The MECE Principle & Issue Trees

* **MECE (Mutually Exclusive, Collectively Exhaustive)**:
  * *Mutually Exclusive*: No overlapping branches or double-counted root causes.
  * *Collectively Exhaustive*: All plausible root causes or solution pathways are covered.
* **The Hypothesis-Driven Issue Tree**:
  1. State the central business problem as a clear decision question.
  2. Decompose the question into 2 to 4 MECE branches.
  3. Formulate falsifiable hypotheses for each branch.
  4. Identify specific data required to validate or refute each hypothesis.

```text
Problem: "Why did Client Operating Profit decline by 15% in Q3?"
  ├── Branch 1: Revenue Decline? (P * Q)
  │     ├── Hypothesis 1A: Volume dropped due to competitor product launch.
  │     └── Hypothesis 1B: Realized price dropped due to heavy promotional discounts.
  └── Branch 2: Cost Increase? (Fixed + Variable)
        ├── Hypothesis 2A: Cloud infrastructure spend spiked from unoptimized workloads.
        └── Hypothesis 2B: Supply chain procurement costs surged due to raw material tariffs.
```

---

### 1.2 The Minto Pyramid Principle for Executive Communication

Senior executive clients process information top-down:
1. **Core Recommendation First (The Answer)**: Lead with the conclusion and quantified action.
2. **Key Supporting Arguments (The Pillars)**: Group 3 strategic reasons supporting the answer.
3. **Underlying Data & Technical Evidence**: Detailed charts, calculations, and methodology reserved for the appendix or follow-up questions.

---

## 2. Seven Detailed Enterprise Consulting Business Cases

---

### Case 1: Data Pipeline Failure with Inconsistent Customer Records

* **Client Context**: A global retail banking client discovers that daily marketing attribution reports show conflicting revenue totals between the CRM system and core transaction logs ($1.4M discrepancy).
* **Clarifying Questions**:
  1. What is the source of truth table grain (transaction ID vs. customer session ID)?
  2. Has the data schema or ingestion cadence changed recently?
* **Analysis & Diagnosis**:
  1. *Schema Audit*: Found that an upstream POS system introduced micro-batch updates without idempotent deduplication keys, causing transactions with multiple card authorizations to be counted 3 times in the lakehouse Bronze layer.
  2. *Reconciliation Calculation*: Total raw rows logged = 1,420,000; distinct transaction keys = 1,180,000 (240,000 duplicate events accounting for the $1.4M discrepancy).
* **Technical Remediation**:
  1. Implement an idempotent `MERGE INTO` (Upsert) operation in the Silver layer using `(transaction_id, timestamp)` composite keys.
  2. Introduce automated Great Expectations data contracts checking for primary key uniqueness before promoting data to the Gold reporting mart.
* **Client-Ready Executive Communication**:
  > *"We diagnosed the $1.4M reporting variance to un-deduplicated POS authorization events in the ingestion layer. We implemented idempotent merge contracts and automated anomaly alerts in the Silver data pipeline. Historical data has been reconciled, and automated quality gates now guarantee 100% unique transaction grain moving forward."*

---

### Case 2: ML Model with Misleading High Accuracy on Loan Defaults

* **Client Context**: A non-banking financial company deploys an underwriting model boasting 97.5% classification accuracy, yet unpredicted loan defaults cause a $12M credit loss in Q2.
* **Diagnosis**:
  1. *Class Imbalance*: The historical default base rate is only 2.5% ($P(\text{Default}) = 0.025$). A naive dummy classifier predicting "No Default" for every applicant achieves 97.5% accuracy while catching zero defaults!
  2. *Evaluation Failure*: The internal team optimized raw accuracy rather than Recall on the default class.
* **Technical Remediation**:
  1. Recalibrate objective to **Cost-Weighted Utility Matrix**: Set False Negative penalty (unpredicted default = $50,000 loss) significantly higher than False Positive penalty (extra manual verification = $200 cost).
  2. Re-train XGBoost with `scale_pos_weight = 39` and tune decision classification threshold using **Precision-Recall AUC (PR-AUC)**.
* **Client-Ready Executive Communication**:
  > *"The 97.5% accuracy metric masked zero recall on default events due to extreme class imbalance. By switching to a cost-calibrated PR-AUC objective, our revised model captures 84% of high-risk defaults, mitigating an estimated $9.6M in annual credit write-offs at the cost of modest additional underwriting reviews."*

---

### Case 3: Enterprise RAG Assistant Producing Unsupported Hallucinations

* **Client Context**: A wealth management advisory firm piloted an internal GenAI assistant to query 500-page regulatory compliance PDFs. The bot cited non-existent compliance exemptions, risking statutory fines.
* **Root-Cause Analysis**:
  1. *Chunking Flaw*: Fixed 300-token chunks arbitrarily severed regulatory tables and conditional policy clauses.
  2. *Retrieval Noise*: Pure dense vector search retrieved semantically similar but legally outdated 2018 policy documents.
  3. *Prompt Weakness*: Model was prompted to "be helpful" without strict abstention instructions.
* **Technical Remediation**:
  1. Implement **Hybrid Search**: Combine BM25 keyword matching for exact regulatory statute codes with dense semantic embeddings, followed by a Cross-Encoder reranker.
  2. Enforce strict **Negative Constraint & Citation Grounding**: "If the answer cannot be established with 100% certainty from the provided context, state 'INSUFFICIENT CONTEXT'. Every claim must append `[DocID, Page]`.
* **Client-Ready Executive Communication**:
  > *"We eliminated regulatory hallucinations by upgrading the ingestion pipeline to document-aware semantic chunking, implementing hybrid keyword-vector retrieval, and enforcing strict citation-grounded prompts. The assistant now achieves 98.4% grounded faithfulness on audit benchmarks and reliably abstains on out-of-scope queries."*

---

### Case 4: Process Bottleneck in Procurement (Source-to-Pay Invoice Backlog)

* **Client Context**: A manufacturing client suffers from a 28-day invoice payment cycle time, accumulating late payment penalties from tier-1 suppliers.
* **Process Mapping & 5 Whys**:
  1. 42% of supplier invoices fail the automated 3-Way Match in the ERP system.
  2. Root Cause: Loading dock personnel scan paper Goods Receipts (GR) with a 6-day lag, while suppliers transmit digital EDI invoices instantly. The system triggers a false "Missing Goods Receipt" payment hold.
* **Remediation**:
  1. Deploy mobile barcode scanning at physical loading docks, creating instantaneous ERP Goods Receipts upon pallet unloading.
  2. Automate tolerance auto-approval for price variances under $50.
* **Quantified ROI**:
  * Reduces invoice processing cycle from 28 days to 4.2 days.
  * Recovers $850,000 annually in early-payment supplier discounts (2/10 Net 30).

---

### Case 5: Knowledge Graph for Synthetic Financial Fraud Ring Detection

* **Client Context**: A fintech lender experiences serial defaults from seemingly unrelated applicant identities across separate online loan applications.
* **Graph Methodology**:
  1. Constructed a Property Knowledge Graph in Neo4j with entity nodes: `(:Applicant)`, `(:BankAccount)`, `(:DeviceFingerprint)`, `(:Phone)`, `(:Address)`.
  2. Ran **Weakly Connected Components (WCC)** and community detection to isolate densely connected clusters.
* **Discovery**: Uncovered 14 distinct applicant accounts sharing 2 burner mobile numbers and a single device MAC address, siphoning $3.8M in coordinated loans.
* **Client-Ready Recommendation**: Integrate real-time 2-hop graph neighborhood expansion into the loan origination API before automated disbursement.

---

### Case 6: Retail Supply Chain Time-Series Demand Forecasting

* **Client Context**: A national retailer suffers from recurring stockouts on high-velocity SKUs during seasonal promotional campaigns, alongside high carrying costs on stagnant inventory.
* **Solution Architecture**:
  1. Replaced simple moving-average baselines with a hierarchical **SARIMAX model** incorporating exogenous promotional calendar flags, price markdown percentage, and local holiday indicators.
  2. Tested stationarity via ADF test ($p = 0.002$ after first differencing).
* **Outcome**:
  * Reduced Mean Absolute Percentage Error (MAPE) from 34% to 14.2%.
  * Decreased stockouts by 45%, unlocking $4.2M in previously lost seasonal sales.

---

### Case 7: Evaluating an Enterprise AI Proof-of-Concept (Go / No-Go Decision)

* **Client Context**: A healthcare provider wants to invest $600,000 into an autonomous AI agent to automatically triage and respond to patient portal clinical inquiries.
* **Feasibility & Risk Evaluation**:
  1. *Data Readiness*: Patient clinical notes are 70% unstructured text with inconsistent medical acronyms; high liability risk.
  2. *Regulatory Liability*: Autonomous medical responses carry severe malpractice liability if advice deviates from clinical standards.
* **Consulting Recommendation (No-Go for Autonomous; Go for Copilot)**:
  > *"We recommend against a fully autonomous patient-facing agent due to acute medical liability and unstandardized clinical data. Instead, we propose a lower-cost $180,000 'Physician Copilot' PoC. The system drafts preliminary triage responses for mandatory physician review and sign-off, cutting clinician documentation time by 40% while preserving zero-defect patient safety."*

---

## 3. Self-Assessment Checklist

- [ ] Can structure ambiguous client questions into MECE issue trees in real time.
- [ ] Understand the Minto Pyramid Principle and how to deliver top-down executive communication.
- [ ] Able to identify class imbalance traps and defend PR-AUC in credit/fraud cases.
- [ ] Can trace root causes of RAG hallucinations and explain hybrid search fixes.
- [ ] Mastered PoC feasibility analysis, risk assessment, and Go / No-Go business framing.
