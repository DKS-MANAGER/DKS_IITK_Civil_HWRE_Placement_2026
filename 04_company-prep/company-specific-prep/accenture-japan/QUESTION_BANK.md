# Master Question Bank — Technical, Behavioral & Enterprise Scenarios

> **Target Role**: Digital Consultant (Analyst Entry Level), Accenture Japan Ltd. (`[JD VERIFIED]`)  
> **Coverage**: 30 Technical Interview Questions with Answer Outlines, 30 Behavioural & Stakeholder Scenarios, 20 Cloud & Enterprise Architecture Questions, 20 AI/ML/GenAI Questions, and 10 Executive Synthesis Exercises.  
> **Classification**: All questions classified by relevance tag (`[JD VERIFIED]`, `[PREPARATION RECOMMENDATION]`, `[PRACTICE ASSUMPTION]`).

---

## 1. Thirty Technical Interview Questions with Answer Outlines

#### Q1: "Explain how you would architect a legacy mainframe data migration to AWS while ensuring zero downtime."
* **Answer Outline**: Use the **Strangler Fig pattern**. Implement Change Data Capture (CDC) via AWS DMS or Debezium streaming from mainframe DB2 logs to Kafka. Replicate read traffic to PostgreSQL on Amazon Aurora first. Validate data parity across 30 days before incrementally migrating write transactions via microservices behind an API Gateway.

#### Q2: "What is the difference between synchronous REST APIs and event-driven architectures with Kafka?"
* **Answer Outline**: REST is synchronous point-to-point (request-response); if the receiving service is down or slow, the caller blocks or times out. Kafka is asynchronous and decoupled; producers write events to persistent partitioned topics, and consumers read independently at their own pace, providing fault tolerance and peak traffic smoothing.

#### Q3: "How do you explain the trade-offs between AWS Lambda (Serverless) and Kubernetes (EKS) to a CFO?"
* **Answer Outline**: Serverless is 100% OpEx—pay only for exact milliseconds executed, zero cost when idle, ideal for unpredictable spiky traffic. Kubernetes requires maintaining cluster nodes (fixed baseline CapEx/OpEx), but is more cost-effective for continuous, high-volume predictable workloads and avoids vendor lock-in.

#### Q4: "What is the CAP theorem, and why can't a distributed database have all three?"
* **Answer Outline**: CAP states that a distributed system can only guarantee two of Consistency, Availability, and Partition Tolerance. Network partitions ($P$) are inevitable in distributed systems, so systems must choose between Consistency ($C$ - all nodes see same data at once, rejecting writes during partition) or Availability ($A$ - every request receives a response, but data may be stale).

#### Q5: "How does a vector database work, and why can't traditional relational databases handle semantic search efficiently?"
* **Answer Outline**: Relational databases index exact text (B-trees/inverted index). Vector databases store high-dimensional numerical embeddings ($d = 1536$) and search using approximate nearest neighbor (ANN) algorithms (e.g., HNSW) calculating cosine distance, finding semantically similar meanings (e.g., "automobile" and "car") rather than literal keyword matches.

#### Q6: "What is the difference between RAG and fine-tuning an LLM?"
* **Answer Outline**: Fine-tuning updates model weights to adapt tone, format, or specialized domain vocabulary, but cannot reliably memorize fast-changing internal documents and is prone to hallucination. RAG retrieves fresh, authoritative external documents at runtime and inserts them into the prompt, guaranteeing verifiable citations with zero model retraining cost.

#### Q7: "What is database indexing, and what is the trade-off of adding too many indexes?"
* **Answer Outline**: Indexes (typically B-Trees) drastically accelerate `SELECT` read queries from $O(N)$ table scans to $O(\log N)$ lookups. The trade-off is write degradation: every `INSERT`, `UPDATE`, and `DELETE` must synchronously update all indexes, consuming storage and slowing write throughput.

#### Q8: "How do you prevent SQL injection in enterprise applications?"
* **Answer Outline**: Never concatenate user input into raw SQL strings. Always use parameterized queries / prepared statements, Object-Relational Mappers (ORMs), stored procedures, and enforce least-privilege database user permissions.

#### Q9: "What is the difference between vertical scaling and horizontal scaling?"
* **Answer Outline**: Vertical scaling (scaling up) adds more CPU/RAM to an existing single machine (limited by hardware ceiling and single point of failure). Horizontal scaling (scaling out) adds more commodity instances behind a load balancer, providing virtually unlimited elasticity and high availability.

#### Q10: "Explain the concept of an API Gateway and three key features it provides."
* **Answer Outline**: A single entry point for all client requests before reaching internal microservices. Key features: 1) Authentication & Authorization (JWT validation), 2) Rate Limiting & Throttling (preventing DDoS), 3) Protocol translation & SSL termination.

#### Q11–Q30 Rapid Question Outlines:
* **Q11 (Database Normalization)**: 1NF (atomic values), 2NF (no partial dependencies on composite key), 3NF (no transitive dependencies). Eliminates data redundancy.
* **Q12 (Denormalization in Data Warehouses)**: Star/Snowflake schemas intentionally introduce redundancy to eliminate expensive multi-table joins during OLAP analytical reporting.
* **Q13 (ACID Properties)**: Atomicity (all or nothing), Consistency (valid state rules), Isolation (concurrent transactions don't interfere), Durability (committed data survives crashes).
* **Q14 (JWT Tokens)**: Header, Payload, Signature. Stateless authentication where server verifies signature without database session lookup.
* **Q15 (Docker vs Virtual Machines)**: VMs virtualize hardware and run a full guest OS (heavy, gigabytes). Docker containers share host OS kernel and run isolated user spaces (lightweight, megabytes, starts in milliseconds).
* **Q16 (Microservices vs Monolith)**: Monolith is simple to deploy initially; microservices offer independent scalability, failure isolation, and autonomous team deployment at the cost of distributed system complexity.
* **Q17 (Latency vs Throughput)**: Latency is time taken for a single request roundtrip (ms). Throughput is the number of requests processed per second (RPS/TPS).
* **Q18 (Zero Trust Architecture)**: "Never trust, always verify." Requires identity authentication and encryption for every single request, even within internal corporate network.
* **Q19 (Edge Computing in IoT)**: Processing telemetry locally on factory gateways to achieve $< 5\text{ ms}$ response times for safety shutoffs without waiting for roundtrip cloud latency.
* **Q20 (Digital Twin)**: A real-time virtual simulation model of a physical asset updated continuously via IoT telemetry to simulate stress and predict component wear.
* **Q21 (Data Drift vs Concept Drift)**: Data drift is shift in input feature distribution ($P(X)$). Concept drift is shift in statistical relationship between inputs and target label ($P(Y|X)$).
* **Q22 (Precision vs Recall in Fraud)**: High Recall catches all frauds (misses few, but generates false alarms). High Precision ensures flagged cases are truly fraudulent. Fraud systems prioritize Recall.
* **Q23 (RPO vs RTO)**: Recovery Point Objective (acceptable data loss duration in time). Recovery Time Objective (acceptable downtime duration before system is restored).
* **Q24 (MQTT vs HTTP in IoT)**: MQTT is a lightweight, low-bandwidth publish-subscribe protocol ideal for battery-constrained sensors. HTTP is heavier with verbose headers.
* **Q25 (Cold Start in Serverless)**: Latency spike when a cloud provider spins up a new container instance from scratch to execute an idle function.
* **Q26 (OAuth 2.0 vs SAML)**: OAuth 2.0 is modern REST/JSON token authorization. SAML is XML-based federated enterprise SSO standard common in legacy enterprise systems.
* **Q27 (ETL vs ELT)**: ETL transforms data before loading (traditional data warehouse). ELT loads raw data into cloud data lakehouse (Snowflake/BigQuery) and transforms at scale using SQL.
* **Q28 (Multi-Cloud Strategy Trade-off)**: Prevents single-vendor lock-in and improves negotiating leverage, but increases engineering complexity to lowest-common-denominator services.
* **Q29 (Container Orchestration - Kubernetes)**: Automatically handles container scheduling, self-healing restarts, rolling zero-downtime updates, and horizontal auto-scaling.
* **Q30 (Data Governance & Lineage)**: Tracking data origin, transformations, and downstream dependencies across the enterprise to ensure auditability, compliance, and trust.

---

## 2. Thirty Behavioural & Stakeholder Scenarios (STAR Model Frameworks)

#### Scenario 1: Stakeholder Disagrees with Data Findings
* **Prompt**: *"What do you do if a client executive strongly disagrees with your analytical recommendation because it contradicts their intuition?"*
* **STAR Framework**:
  * **S**: In an engineering modeling review, senior reviewers challenged my anomaly threshold.
  * **T**: Defend the conclusion without becoming combative or dismissing their domain expertise.
  * **A**: Validated their intuitive scenarios by running sensitivity stress-tests live; showed the exact boundary conditions where their intuition applied vs where data revealed structural drift.
  * **R**: Reached consensus by adopting a phased rollout with intermediate review gates.

#### Scenario 2: Handling Incomplete or Missing Client Data
* **Prompt**: *"How do you proceed when a client provides dirty, incomplete datasets right before a deadline?"*
* **STAR Framework**: Highlight data audit, separating core usable data from imputed intervals, establishing explicit confidence intervals, and communicating risks transparently.

#### Scenario 3: Cross-Cultural Team Conflict (India vs Japan Team)
* **Prompt**: *"Describe a situation where cultural or communication differences caused friction in a project."*
* **STAR Framework**: Emphasize adopting *Ho-Ren-So* (structured reporting) and *Nemawashi* (informal alignment before meetings) to replace ad-hoc assumptions with written agreements.

#### Scenarios 4–30 Practical Outlines:
* **S4 (Overcoming Technical Failure)**: Pivot quickly, conduct root-cause analysis, document lessons learned.
* **S5 (Handling Ambiguous Requirements)**: Build rapid prototype / mock wireframe to elicit concrete feedback.
* **S6 (Ethical / Data Security Concern)**: Escalate transparently; refuse to bypass PII protection for convenience.
* **S7 (Learning a Technology Fast)**: 7-day deep-dive methodology: documentation, hands-on build, peer review.
* **S8 (Managing Competing Priorities)**: Eisenhower Matrix: triage urgent vs strategic tasks; communicate capacity early.
* **S9 (Leading Without Authority)**: Influence through data, clear shared metrics, and removing blockers for peers.
* **S10 (Admitting a Mistake to a Manager)**: Acknowledge error immediately, present 2 concrete remediation options.
* **S11 (Dealing with a Disengaged Team Member)**: 1-on-1 private discussion to uncover root cause (overwhelmed vs underutilized).
* **S12 (Unreasonable Client Deadline Push)**: Deconstruct scope into MVP vs Phase 2; negotiate features rather than quality.
* **S13 (Explaining Complex Tech to Non-Tech Audience)**: Use business analogies (e.g., comparing API Gateway to a hotel concierge).
* **S14 (Working Across Timezones)**: Asynchronous documentation, clean handover summaries, respecting working hours.
* **S15 (Adapting to Sudden Scope Change)**: Re-baseline roadmap, document budget/timeline impacts, adjust milestones.
* **S16 (Receiving Harsh Critical Feedback)**: Listen actively, separate emotion from content, ask for 1 specific behavior to change.
* **S17 (Giving Difficult Feedback to a Peer)**: Use Situation-Behavior-Impact (SBI) framework privately and constructively.
* **S18 (Persuading a Skeptical Client to Adopt Cloud)**: Present TCO calculation and security compliance audit certificates.
* **S19 (Handling Burnout Under High Pressure)**: Prioritize ruthlessly, take structured micro-breaks, communicate team load.
* **S20 (Balancing Perfectionism vs Speed)**: Adopt 80/20 rule: deliver working iterative MVP to gather real feedback.
* **S21 (Resolving Conflicting Client Stakeholder Demands)**: Map requirements back to the core sponsor business case.
* **S22 (Staying Calm During a Live Production Outage)**: Follow incident protocol: triage, isolate, restore, post-mortem.
* **S23 (Promoting Inclusive Teamwork)**: Actively solicit ideas from quieter team members in meetings.
* **S24 (Challenging Senior Management with Data)**: Frame challenge as risk mitigation supported by verifiable empirical data.
* **S25 (Maintaining Work Quality in Repetitive Tasks)**: Automate repetitive manual scripts using Python.
* **S26 (Negotiating Feature Scope with Developers)**: Focus on business user stories and agreed acceptance criteria.
* **S27 (Building Rapport with a New Client)**: Learn client industry terminology, demonstrate deep preparation in first meeting.
* **S28 (Managing Client Scope Creep)**: Welcome new ideas, but log them formally in change-request register with cost impact.
* **S29 (Presenting to C-Suite Executives)**: Lead with the recommendation (Pyramid Principle); keep details in appendix.
* **S30 (Championing Continuous Improvement - Kaizen)**: Conduct blameless retrospective at the end of every engagement milestone.

---

## 3. Twenty Cloud & Enterprise Architecture Questions

1. **Cloud Shared Responsibility Model**: AWS/Azure secures the cloud (physical data centers, hardware, hypervisors); the customer secures in the cloud (data, IAM credentials, OS patches, network rules).
2. **Multi-Region Disaster Recovery Strategies**: Backup & Restore (cheapest, high RPO/RTO) $\to$ Pilot Light $\to$ Warm Standby $\to$ Active-Active Multi-Region (zero downtime, high cost).
3. **Database Sharding vs Read Replicas**: Read replicas replicate read queries to slave nodes (scales read throughput). Sharding horizontally partitions table rows across separate database nodes (scales write capacity and storage).
4. **VPC Subnet Architecture**: Public subnet contains Load Balancers with internet gateways; private subnets contain application containers and databases with no direct inbound internet routes.
5. **Circuit Breaker Pattern in Microservices**: Prevents cascading system failure by temporarily tripping open when downstream service error rates breach thresholds, returning fallback cached responses.
6. **API Idempotency**: Ensuring repeated identical API requests (e.g., payment submission) produce the exact same result without duplicate charges using unique Idempotency Keys.
7. **Database Connection Pooling**: Reusing a cache of pre-established database connections to avoid the expensive TCP and SSL handshake latency of opening new connections per request.
8. **Asynchronous Messaging vs Webhooks**: Messaging uses queues with guaranteed delivery and consumer pull. Webhooks are HTTP push callbacks from one system to another, requiring receiver uptime.
9. **Eventual Consistency vs Strong Consistency**: Strong consistency ensures reads immediately reflect latest write (higher latency). Eventual consistency allows temporary replication lag across nodes before converging.
10. **Data Lake vs Data Warehouse vs Lakehouse**: Data Warehouse stores structured curated data for BI (Snowflake). Data Lake stores raw unstructured files (S3). Lakehouse combines ACID transactions on open object storage (Databricks).
11. **SaaS vs Custom Build Evaluation**: Build custom when capability is a core competitive differentiator; buy SaaS (Salesforce, SAP) for standardized commodity back-office processes.
12. **Content Delivery Network (CDN) Dynamics**: Caching static assets (images, JS) and edge-rendering dynamic API responses at edge points of presence close to users globally.
13. **Zero-Downtime Deployment Strategies**: Blue/Green (switch routing between two identical environments) vs Canary (route 5% of live traffic to new version, monitor errors before full rollout).
14. **Enterprise Service Bus (ESB) vs Event-Driven Mesh**: ESB centralizes transformation logic (legacy bottleneck). Event-driven mesh (Kafka) keeps core dumb and endpoints smart.
15. **Data Encryption: At Rest vs In Transit**: In transit uses TLS 1.3 encryption. At rest uses AES-256 with Customer-Managed Keys (AWS KMS / Azure Key Vault).
16. **Immutable Infrastructure**: Servers are never modified in place; updates require building new container/AMI images and replacing old instances completely.
17. **Micro-Frontends**: Decomposing monolithic web frontends into independently deployable user interface components owned by autonomous domain teams.
18. **Observability: Metrics vs Logs vs Traces**: Metrics track aggregated trends (CPU %). Logs record discrete event details (timestamped errors). Traces follow a single request's end-to-end journey across microservices.
19. **Cost Allocation & Cloud Tagging (FinOps)**: Enforcing mandatory tags (`CostCenter`, `ProjectID`, `Environment`) on every cloud resource to hold engineering teams accountable for cloud spend.
20. **Legacy Monolith Strangler Pattern**: Intercepting incoming traffic with an API Gateway and gradually routing traffic to newly built microservices until the monolith has zero traffic.

---

## 4. Twenty AI, Machine Learning & Generative AI Questions

1. **Hallucination Mitigation in Enterprise GenAI**: Use RAG with strict temperature (0.0), ground responses in retrieved documents, prompt LLM to say "I do not know" if context lacks evidence, and employ guardrails.
2. **Embedding Cosine Similarity vs Euclidean Distance**: Cosine similarity measures angle between normalized vector directions regardless of magnitude; standard metric for text semantic similarity.
3. **Chunking Strategies in RAG**: Fixed-size chunking with overlap (e.g., 500 tokens with 50-token overlap) vs semantic chunking based on document headings and markdown structure.
4. **Fine-Tuning vs RAG Cost Analysis**: RAG has near-zero training CapEx and continuous data freshness. Fine-tuning requires significant GPU training cost and must be re-run whenever base facts change.
5. **Class Imbalance in Fraud / Defect Detection**: Accuracy is misleading (99% baseline). Address via SMOTE oversampling, downsampling, and optimizing PR-AUC rather than ROC-AUC.
6. **Overfitting Detection**: Validation loss starts increasing while training loss continues decreasing; solve with regularization, dropout, pruning, and more diverse training data.
7. **Cross-Validation in Time-Series**: Must use rolling forward-chaining splits ($T_1 \to T_2 \to T_3$); random k-fold leaks future information into past predictions.
8. **Feature Engineering vs Deep Learning Representation**: Classical models (XGBoost) require manual feature domain creation. Deep learning learns latent representations automatically from raw high-dimensional inputs.
9. **Explainable AI (SHAP & LIME)**: Computing Shapley values to identify exactly which input features contributed positively or negatively to an individual prediction for regulatory compliance.
10. **Data Leakage Vectors**: Target leakage occurs when features unavailable at prediction time (e.g., future status flags) are accidentally included in training sets.
11. **Responsible AI & Toxicity Guardrails**: Input/output filters (e.g., Llama Guard, NeMo Guardrails) that block jailbreaks, toxic language, and confidential corporate data leakage.
12. **Vector Index HNSW vs Flat Search**: Flat search compares query against every vector ($O(N)$ exact, slow). Hierarchical Navigable Small World (HNSW) uses multi-layer graph navigation ($O(\log N)$ approximate, fast).
13. **Model Quantization**: Converting neural network weights from 32-bit floating point (FP32) to 8-bit or 4-bit integers (INT8/INT4), slashing GPU memory requirements with minimal accuracy loss.
14. **Small Language Models (SLMs) vs Massive LLMs**: Deploying 7B-14B parameter models (e.g., Mistral, Llama-3) on-premise for specific enterprise tasks at 1/10th the inference cost of GPT-4.
15. **Prompt Injection & Jailbreak Attacks**: Adversarial user inputs tricking LLM into ignoring system safety guardrails (e.g., *"Ignore all previous instructions"*). Mitigated via dual-model screening.
16. **Model Monitoring & Concept Drift**: Tracking production prediction distributions against training baselines using Population Stability Index (PSI) and Kolmogorov-Smirnov statistics.
17. **Agentic Workflows & Tool Use (ReAct Pattern)**: LLM reasons, determines which external API tool to invoke (SQL query, weather API), receives execution output, and synthesizes final answer.
18. **Evaluation Metrics: BLEU / ROUGE vs LLM-as-a-Judge**: ROUGE checks n-gram overlap. LLM-as-a-Judge uses a powerful LLM to evaluate factual consistency, relevance, and tone against rubrics.
19. **Cold-Start Problem in Recommender Systems**: New users or items with zero historical interaction data; mitigated using content-based metadata filtering until behavioral signals accumulate.
20. **AI Ethics & Privacy Regulations in Japan**: Aligning with Japan Ministry of Economy, Trade and Industry (METI) AI Governance Guidelines: transparency, non-discrimination, accountability, and privacy.

---

## 5. Ten Executive Synthesis Exercises (Minto Pyramid Principle)

For each scenario, the candidate must deliver an answer using the **Answer First $\longrightarrow$ Three Supporting Pillars $\longrightarrow$ Risk/Next Step** structure:

* **Exercise 1: Recommendation on Cloud Migration Strategy**:  
  *"We recommend adopting a phased Hybrid Cloud migration to AWS Tokyo over 24 months, delivering JPY 350M in annual IT savings. First, legacy mainframe batch processing costs will drop by 45%. Second, release velocity for mobile customer features will accelerate from bi-annual to bi-weekly. Third, disaster recovery RTO will improve from 24 hours to 15 minutes. The immediate next step is executing a 60-day migration pilot for the mobile statements read service."*
* **Exercise 2: Pitching AI Automation for Call Centers**: Lead with 30% operational cost reduction and 24/7 coverage, supported by deflection metrics and high customer satisfaction ratings.
* **Exercise 3: Advising Between AWS vs Azure for a Japanese Conglomerate**: Emphasize existing Microsoft enterprise licensing and Active Directory integration as primary cost driver favoring Azure.
* **Exercise 4: Executive Defense of IoT Predictive Maintenance in Manufacturing**: Quantify the 70% reduction in unplanned breakdown losses against a 4-month payback horizon.
* **Exercise 5: Recommending Strangler Fig Pattern over Big-Bang Core ERP Migration**: Frame as operational risk containment for critical continuous enterprise ledger availability.
* **Exercise 6: Presenting Enterprise RAG Adoption to C-Suite**: Highlight employee time reclamation (2.5 hrs/day) with zero customer confidential data exposure.
* **Exercise 7: Explaining Why Private 5G is Required Over Port Wi-Fi**: Cite physical radio wave attenuation around metal shipping containers and strict sub-10ms latency for autonomous vehicles.
* **Exercise 8: Synthesizing Fraud Detection Model Trade-Offs for a Risk Committee**: Defend accepting higher false positives to completely eliminate catastrophic undetected fraud losses.
* **Exercise 9: Justifying Investment in Data Governance & Lineage**: Connect data cleanliness to regulatory audit compliance and elimination of duplicate reporting errors.
* **Exercise 10: Presenting a Project Delay Recovery Plan**: State revised milestone delivery date upfront, explain root cause, and present resource re-allocation plan that recovers timeline within 60 days.
