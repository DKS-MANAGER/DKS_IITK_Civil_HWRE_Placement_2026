# Accenture Japan Digital Consultant — Master Study Guide

> **Target Role**: Digital Consultant (Analyst Entry Level), Accenture Japan Ltd.  
> **Target Audience**: IIT Kanpur Civil / HWRE Graduate transitioning to Digital Consulting in Tokyo  
> **Core Objective**: A rigorous, end-to-end curriculum detailing exactly what to study, in what sequence, and the required mastery depth for every domain.

---

## 🏛️ Executive Philosophy: The Digital Consultant Mindset

A **Digital Consultant** operates at the intersection of **Business Strategy** and **Technology Architecture**. Unlike pure software engineering (writing specific production code) or pure management consulting (strategy without execution oversight), your mission is:
1. **Diagnose**: Identify operational bottlenecks and quantify financial impact.
2. **Architect**: Design scalable, vendor-agnostic technology solutions (Cloud, AI, IoT, Enterprise Systems).
3. **Execute**: Guide implementation roadmaps, manage organizational change, and realize measurable business KPIs.

---

## 🗺️ Master Curriculum Architecture

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                   DIGITAL CONSULTANT CURRICULUM ARCHITECTURE                │
├──────────────────────────────┬──────────────────────────────┬───────────────┤
│ DOMAIN A: Company & Role     │ DOMAIN B: Consulting & MECE  │ DOMAIN C: Tech│
│ Mastery (Accenture Japan)    │ Structuring (Cases & Math)   │ Test (Py/SQL) │
├──────────────────────────────┼──────────────────────────────┼───────────────┤
│ DOMAIN D: Digital Tech       │ DOMAIN E: AI, GenAI &        │ DOMAIN F: IoT │
│ Architecture (Cloud, ERP)    │ Enterprise RAG Pipelines     │ & Industry X  │
├──────────────────────────────┼──────────────────────────────┼───────────────┤
│ DOMAIN G: Project & Resume   │ DOMAIN H: Japan Readiness,   │ DOMAIN I: Mock│
│ Defense (Civil/HWRE Bridge)  │ STAR Stories & Executive Fit │ Simulations   │
└──────────────────────────────┴──────────────────────────────┴───────────────┘
```

---

## 📚 Detailed Domain Breakdown & Preparation Protocol

### Domain A: Company & Role Understanding (`[P0]` — Mastery Target: L4)
* **What to Study**:
  * **Accenture Business Model**: Global scale (750k+ employees), multi-service integration (Strategy & Consulting, Technology, Operations, Song, Industry X).
  * **Technology-Agnostic Philosophy (`[JD VERIFIED]`)**: Why Accenture does not sell proprietary software, but selects the best fit across AWS, Azure, GCP, SAP, Salesforce, or custom open-source stacks.
  * **Analyst Responsibilities**: Requirements engineering, functional specifications, data pipeline analysis, stakeholder alignment, user story creation.
  * **3 Career Progression Tracks (`[JD VERIFIED]`)**:
    1. *Business × Technology Path*: Upstream requirements, IT strategy, enterprise architecture.
    2. *Project Management Path*: Leading multidisciplinary teams, large transformation programs.
    3. *Technology Specialist Path*: Deep technical expertise in Cloud, AI, Cybersecurity, or Industry X.
* **Practice Requirement**:
  * Deliver a crisp 60-second role definition and 90-second "Why Accenture Japan" without notes.
* **Canonical Resources**: [`ROLE.md`](ROLE.md) · [`PLACEMENT_FACTS.md`](PLACEMENT_FACTS.md).

---

### Domain B: Consulting Problem Solving & Business Mathematics (`[P0]` — Mastery Target: L4)
* **What to Study**:
  * **MECE Structuring**: Mutually Exclusive, Collectively Exhaustive deconstruction across Mathematical (Revenue = P × Q), Value Chain (Inbound -> Ops -> Outbound -> Sales), and Internal vs External trees.
  * **Hypothesis-Driven Synthesis**: Leading with the answer using the Pyramid Principle (Recommendation -> 3 Supporting Pillars -> Quantified Risks).
  * **Case Archetypes**:
    * *Profitability & Cost Reduction*: Diagnosing unit economics, fixed vs variable cost inflation, customer mix shift.
    * *Market Entry & Growth*: Sizing TAM/SAM/SOM, evaluating build vs buy vs partner.
    * *Digital Transformation (DX)*: Diagnosing legacy IT bottlenecks, cloud migration roadmaps, user adoption.
  * **Business Mathematics**:
    * Gross Margin = $(	ext{Revenue} - 	ext{COGS}) / 	ext{Revenue}$
    * EBITDA Margin = $	ext{EBITDA} / 	ext{Revenue}$
    * Break-even Volume = $	ext{Fixed Costs} / (	ext{Price} - 	ext{Variable Cost per unit})$
    * Customer Lifetime Value: $LTV = (	ext{ARPU} 	imes 	ext{Gross Margin}) / 	ext{Churn Rate}$
    * $LTV / CAC$ Ratio (Target: $>3.0x$, Payback $<12$ months).
    * Rule of 72: Years to double $pprox 72 / 	ext{Growth Rate \%}$.
* **Practice Requirement**:
  * 15 timed issue-tree drills (90s each).
  * 10 consulting math mental calculations (zero paper errors).
  * 8 business cases in [`CONSULTING_CASES.md`](CONSULTING_CASES.md).
* **Canonical Resources**: [`03_non_core/consulting/02_problem-solving.md`](../../../03_non_core/consulting/02_problem-solving.md) · [`01_common/placement-math/`](../../../01_common/placement-math/).

---

### Domain C: Technical Test Preparation (Python & SQL) (`[P0]` — Mastery Target: L3)
* **What to Study**:
  * **Python Algorithmic Logic**:
    * Arrays, Hash Maps (Dictionaries), Strings, Two-Pointer technique, Sliding Window, Prefix Sums.
    * Time Complexity $O(1), O(N), O(N \log N)$ and Space Complexity trade-offs.
  * **SQL & Data Analytics**:
    * Multi-table JOINs (`INNER`, `LEFT`, `FULL`, `CROSS`).
    * Aggregations & Grouping (`GROUP BY`, `HAVING`, `SUM`, `AVG`, `COUNT(DISTINCT)`).
    * Subqueries, CTEs (`WITH` clauses), CASE WHEN logic, COALESCE.
    * Window Functions: `ROW_NUMBER() OVER()`, `RANK()`, `DENSE_RANK()`, `LAG()`, `LEAD()`, running totals.
    * Business Scenarios: Daily Active Users (DAU), Monthly Active Users (MAU), Customer Retention, Top-N per Department.
* **Practice Requirement**:
  * Solve 30 Python problems and 40 SQL queries in [`TECHNICAL_TEST.md`](TECHNICAL_TEST.md).
* **Canonical Resources**: [`TECHNICAL_TEST.md`](TECHNICAL_TEST.md) · [`03_non_core/software-engineering/programming/python.md`](../../../03_non_core/software-engineering/programming/python.md) · [`03_non_core/analytics/analytics/04_tools-and-technical-stack.md`](../../../03_non_core/analytics/analytics/04_tools-and-technical-stack.md).

---

### Domain D: Digital Technology & Cloud Architecture (`[P0]` — Mastery Target: L3)
* **What to Study**:
  * **Cloud Computing Fundamentals**:
    * Public vs Private vs Hybrid vs Multi-Cloud.
    * Service Models: IaaS (EC2/VMs), PaaS (App Service/Elastic Beanstalk), SaaS (Salesforce/Workday).
    * Modern Infrastructure: Microservices, Docker Containers, Kubernetes orchestration, Serverless (AWS Lambda / Azure Functions).
    * Disaster Recovery: Recovery Time Objective (RTO) vs Recovery Point Objective (RPO), multi-region active-active vs active-passive.
  * **Technology Selection Framework**:
    * How to objectively compare AWS vs Azure vs GCP based on existing client landscape, enterprise licensing, data residency laws in Japan, and TCO.
  * **Enterprise Systems**:
    * ERP (SAP S/4HANA core ledger & logistics), CRM (Salesforce customer 360), Supply Chain (Blue Yonder/SAP SCM).
    * Integration Architecture: REST APIs, JSON, API Gateways (Kong/Apigee), Event-Driven Architecture (Kafka / RabbitMQ message queues).
* **Practice Requirement**:
  * Architect 3 enterprise cloud migration blueprints with trade-off matrices.
* **Canonical Resources**: [`WHAT_TO_STUDY.md`](WHAT_TO_STUDY.md) · [`03_non_core/software-engineering/04_tools-and-technical.md`](../../../03_non_core/software-engineering/04_tools-and-technical.md).

---

### Domain E: AI, Machine Learning & Enterprise Generative AI (`[P0]` — Mastery Target: L3)
* **What to Study**:
  * **Classical ML Fundamentals**: Supervised vs Unsupervised, Regression vs Classification, Train/Val/Test split, Overfitting/Underfitting, Precision/Recall/F1-score, ROC-AUC.
  * **Enterprise Generative AI & LLMs**:
    * Tokens, Embeddings, Context Window limits, Hallucination risks.
    * **RAG (Retrieval-Augmented Generation) Architecture**:
      $$	ext{User Query} \longrightarrow 	ext{Embedding Model} \longrightarrow 	ext{Vector Search (Cosine Similarity)} \longrightarrow 	ext{Context Ingestion} \longrightarrow 	ext{LLM Output}$$
    * When to use Prompt Engineering vs RAG vs Fine-Tuning.
    * **Responsible AI & Security**: Enterprise data privacy, preventing PII leakage, Role-Based Access Control (RBAC), toxicity guardrails.
* **Practice Requirement**:
  * Walk through the Enterprise Insurance Policy Retrieval case in [`CONSULTING_CASES.md`](CONSULTING_CASES.md).
* **Canonical Resources**: [`CONSULTING_CASES.md`](CONSULTING_CASES.md) · [`WHAT_TO_STUDY.md`](WHAT_TO_STUDY.md).

---

### Domain F: Industry X & Smart Factory IoT (`[P0]` — Mastery Target: L3)
* **What to Study**:
  * **IoT Ecosystem**: Physical Sensors (Vibration, Temperature, Acoustic) $\longrightarrow$ Edge Gateways $\longrightarrow$ MQTT/HTTPS Telemetry Ingestion $\longrightarrow$ Cloud Data Lake.
  * **Manufacturing Systems**: SCADA (Supervisory Control), MES (Manufacturing Execution Systems), ERP integration.
  * **Key Operational Concepts**:
    * **OEE (Overall Equipment Effectiveness)**:
      $$	ext{OEE} = 	ext{Availability} 	imes 	ext{Performance} 	imes 	ext{Quality}$$
    * Predictive Maintenance: Anomaly detection on telemetry streams to prevent unplanned downtime.
    * Digital Twins: Virtual replica of physical plant equipment for real-time stress simulation.
* **Practice Requirement**:
  * Solve the Robotics Smart Factory Case in [`CONSULTING_CASES.md`](CONSULTING_CASES.md).
* **Canonical Resources**: [`CONSULTING_CASES.md`](CONSULTING_CASES.md) · [`03_non_core/operations/`](../../../03_non_core/operations/).

---

### Domain G: Civil/HWRE Project & Resume Defense (`[P0]` — Mastery Target: L4)
* **What to Study**:
  * **The 4-Step Technical Defense**:
    1. *Problem Context (30s)*: Physical / engineering bottleneck (e.g. pier scour failure, flood lead time).
    2. *Methodology & Stack (45s)*: Governing physics, Python automation, OpenFOAM CFD, statistical time-series.
    3. *Key Technical Bottleneck (45s)*: Data sparsity, numerical instability, memory optimization.
    4. *Quantified Outcome & Value (30s)*: % error reduction, NSE score, runtime speedup.
  * **Engineering-to-Consulting Transfer Matrix**:
    * Numerical simulation $\longrightarrow$ Computational modeling & systems thinking.
    * Hydrological forecasting $\longrightarrow$ Predictive analytics under high uncertainty.
    * Complex physical networks $\longrightarrow$ Enterprise supply chain and workflow architecture.
* **Practice Requirement**:
  * Rehearse 30s, 60s, and 2-minute project pitches for M.Tech research and key coursework.
* **Canonical Resources**: [`PROJECT_STRATEGY.md`](PROJECT_STRATEGY.md) · [`08_projects/`](../../../08_projects/) · [`RESUME_STRATEGY.md`](RESUME_STRATEGY.md).

---

### Domain H: Japan Readiness, Cross-Cultural Fit & HR (`[P0]` — Mastery Target: L4)
* **What to Study**:
  * **Japanese Business Culture**:
    * *Nemawashi (根回し)*: Informal consensus building before formal decision-making.
    * *Kaizen (改善)*: Continuous incremental operational improvement.
    * *Omotenashi (おもてなし)*: High standard of customer service and stakeholder care.
    * *Attention to Detail*: Meticulous validation of data, slides, and executive memos.
  * **Japanese Language Strategy (`[JD VERIFIED]`)**:
    * Verified fact: Japanese is NOT required at hiring, but mandatory after joining.
    * Concrete action plan: Dedicating 1 hour/day pre-joining, leveraging Accenture's sponsored JPY 664,658 training program, targeting conversational fluency within 12 months.
  * **Core Behavioral Stories**:
    * Adaptability & grit in unfamiliar environments.
    * Overcoming technical project failures.
    * Resolving cross-disciplinary team conflicts.
    * Passion for continuous learning in emerging tech.
* **Practice Requirement**:
  * Practice all 5 STAR stories in [`BEHAVIOURAL_HR.md`](BEHAVIOURAL_HR.md) and mock interviews in [`INTERVIEW.md`](INTERVIEW.md).
* **Canonical Resources**: [`BEHAVIOURAL_HR.md`](BEHAVIOURAL_HR.md) · [`INTERVIEW.md`](INTERVIEW.md) · [`01_common/behavioral/`](../../../01_common/behavioral/).

---

## 📅 Timed Study Roadmaps

### 30-Day Comprehensive Master Plan
* **Days 01–05**: Role Mastery, Accenture Tech-Agnostic Model, Aptitude Section Tests.
* **Days 06–12**: Consulting Problem Solving, MECE Issue Trees, Business Math Drills.
* **Days 13–18**: Technical Test Drills (Python 30 questions, SQL 40 questions).
* **Days 19–24**: Digital Technology Deep Dive (Cloud, AI/RAG, IoT/Industry X Cases).
* **Days 25–28**: Project Defense Walkthroughs, STAR Stories, Japanese Motivation.
* **Days 29–30**: Full Timed Mock Interviews & Readiness Scorecard review.

### 14-Day High-ROI Accelerated Plan
* **Days 01–03**: Role Alignment, MECE Structuring & 4 Core Business Cases.
* **Days 04–07**: Python & SQL Technical Test Practice (High-Yield Questions).
* **Days 08–10**: Cloud, AI/RAG, and Smart Factory Cases in [`CONSULTING_CASES.md`](CONSULTING_CASES.md).
* **Days 11–13**: Project Defense (Civil/HWRE Bridge) & Director Fit QA.
* **Day 14**: Rapid Revision ([`RAPID_REVISION.md`](RAPID_REVISION.md)).

### 7-Day Sprint Plan
* **Day 01**: Role pitch & 5 Issue-Tree drills.
* **Day 02**: SQL Window Functions & Python Algorithms.
* **Day 03**: Cloud Architecture & Enterprise RAG Case.
* **Day 04**: Smart Factory Industry X Case & Business Math.
* **Day 05**: Project Defense (4-Step Answer Framework).
* **Day 06**: HR & Japan Readiness ("Why Japan?", "Why Accenture?").
* **Day 07**: Timed Mock Test & Emergency Revision.

### Emergency Plans (3-Day / 1-Day / 3-Hour / 60-Minute)
* Refer to [`RAPID_REVISION.md`](RAPID_REVISION.md) for hyper-condensed flashcard checklists.
