# Accenture Japan Digital Consultant — Master Study Guide

> **Target Role**: Digital Consultant (Analyst Entry Level), Accenture Japan Ltd. (`[JD VERIFIED]`)  
> **Target Audience**: IIT Kanpur Postgraduate Engineering Candidates (`[JD VERIFIED]`)  
> **Core Objective**: Comprehensive, end-to-end preparation curriculum covering conceptual foundations, practical practice, and interview mastery across all eight essential digital consulting domains.

---

## 1. Executive Philosophy: The Digital Consultant Mindset

A **Digital Consultant** operates directly at the intersection of **Enterprise Business Strategy** and **Technology Architecture** (`[JD VERIFIED]`):

```text
┌─────────────────────────────────┐           ┌─────────────────────────────────┐
│     BUSINESS STRATEGY & VALUE   │           │   TECHNOLOGY ARCHITECTURE & AI  │
│ • Diagnosing Operating Pains    │ ◄───────► │ • Cloud, AI/Data Analytics      │
│ • Quantifying Financial Impact  │           │ • Industry X (Smart Factory/IoT)│
│ • Business Process Optimization │           │ • Enterprise Core (ERP/APIs)    │
└─────────────────────────────────┘           └─────────────────────────────────┘
                 ▲                                             ▲
                 └──────────────────────┬──────────────────────┘
                                        │
                          ┌───────────────────────────┐
                          │    DIGITAL CONSULTANT     │
                          │   (Accenture Japan Ltd.)  │
                          └───────────────────────────┘
```

> **The Technology-Agnostic Core (`[JD VERIFIED]`)**:  
> Accenture does not sell proprietary software. We evaluate clients' needs objectively across AWS, Azure, GCP, SAP, Salesforce, or open-source solutions to deliver maximum measurable business ROI.

---

## 2. Master Curriculum Architecture (Eight Core Domains)

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                   DIGITAL CONSULTANT CURRICULUM ARCHITECTURE                │
├──────────────────────────────┬──────────────────────────────┬───────────────┤
│ DOMAIN 1: Company & Role     │ DOMAIN 2: Structured Problem │ DOMAIN 3:     │
│ Understanding                │ Solving & Business Cases     │ Aptitude &    │
│ (Accenture Model & Tracks)   │ (MECE, Issue Trees, Cases)   │ Consulting Math│
├──────────────────────────────┼──────────────────────────────┼───────────────┤
│ DOMAIN 4: SQL & Data         │ DOMAIN 5: Python Coding &    │ DOMAIN 6:     │
│ Manipulation                 │ Algorithmic Problem Solving  │ Cloud & System│
│ (30 Enterprise Queries)      │ (20 Python Algorithms)       │ Architecture  │
├──────────────────────────────┼──────────────────────────────┼───────────────┤
│ DOMAIN 7: AI, Machine        │ DOMAIN 8: Project Defense,   │ DOMAIN 9:     │
│ Learning & Enterprise GenAI  │ Japan Cultural Fit & HR      │ Mock Practice │
│ (RAG, Governance, Ethics)    │ (STAR Narratives, Japanese)  │ & Scorecards  │
└──────────────────────────────┴──────────────────────────────┴───────────────┘
```

---

## 3. In-Depth Domain Study Protocol

### Domain 1: Company, Role & Career Progression (`[P1]` — Target Depth: L4)
* **What to Master**:
  * **Accenture Scale**: 800,000+ professionals globally; deep ecosystem partnerships with all major tech vendors.
  * **Technology-Agnostic Philosophy**: Unconstrained by proprietary products; focus on delivering measurable client transformation.
  * **Five Core Responsibilities (`[JD VERIFIED]`)**: Problem diagnosis, technology selection, strategy translation, defining what to build with AI/automation, full consulting lifecycle.
  * **Three Career Progression Tracks (`[JD VERIFIED]`)**:
    1. *Business × Technology Path*: Upstream strategy, requirements engineering, enterprise solutions.
    2. *Project Management Path*: Leading large transformation programs, budgets, cross-border teams.
    3. *Technology Specialist Path*: Deep technical expertise in Cloud, AI, Cybersecurity, or Industry X.
* **Practice Requirement**: Rehearse a crisp 60-second role pitch and 90-second "Why Accenture Japan" answer.
* **Core File**: [`ROLE.md`](ROLE.md) · [`PLACEMENT_FACTS.md`](PLACEMENT_FACTS.md).

---

### Domain 2: Structured Problem Solving & Digital Cases (`[P1]` — Target Depth: L4)
* **What to Master**:
  * **MECE Deconstruction**: Mutually Exclusive, Collectively Exhaustive breaking down of complex problems into mathematical driver trees, value-chain trees, and process trees.
  * **The 10-Point Digital Case Structure**: Problem statement, clarifying questions, structure, data required, tech plan, calculations, interpretation, recommendations, risks, and executive follow-ups.
  * **Digital Transformation (DX) Archetypes**: Cloud migration, smart factory Industry X, enterprise GenAI/RAG, omnichannel inventory management, and digital customer experience.
* **Practice Requirement**: Solve all 15 cases and 15 issue-tree drills in [`CONSULTING_CASES.md`](CONSULTING_CASES.md).
* **Canonical Links**: [`CONSULTING_CASES.md`](CONSULTING_CASES.md) · [`03_non_core/consulting/02_problem-solving.md`](../../../03_non_core/consulting/02_problem-solving.md).

---

### Domain 3: Quantitative Aptitude & Consulting Mathematics (`[P1]` — Target Depth: L3)
* **What to Master**:
  * **Business Margins**: Gross Margin $= (\text{Rev} - \text{COGS}) / \text{Rev}$; Operating Margin $= \text{EBIT} / \text{Rev}$.
  * **Unit Economics**: Customer Lifetime Value ($LTV = (\text{ARPU} \times \text{Margin}) / \text{Churn}$); $LTV / CAC > 3.0x$; Payback Period $< 12$ months.
  * **Break-Even Volume**: Fixed Costs divided by Contribution Margin per unit.
  * **Rule of 72 & CAGR**: Years to double $\approx 72 / \text{Rate \%}$.
  * **Market Sizing**: Population-based and supply-side estimation frameworks.
* **Practice Requirement**: Complete all 20 quantitative problems and 10 market sizing guesstimates.
* **Core Files**: [`TECHNICAL_TEST.md`](TECHNICAL_TEST.md) · [`01_common/placement-math/`](../../../01_common/placement-math/).

---

### Domain 4: SQL & Enterprise Data Manipulation (`[P2]` — Target Depth: L3)
* **What to Master**:
  * **Relational Schema Understanding**: Table grain, primary/foreign keys, handling NULLs with `COALESCE` and `NULLIF`.
  * **Advanced Aggregations & Joins**: `GROUP BY`, `HAVING`, multi-table `INNER`, `LEFT`, and `CROSS` joins.
  * **Subqueries & CTEs**: Modular query design using `WITH` statements.
  * **Window Functions**: `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `LAG()`, `LEAD()`, moving averages, and running totals.
* **Practice Requirement**: Execute and verify all 30 SQL challenges in [`TECHNICAL_TEST.md`](TECHNICAL_TEST.md).
* **Core Files**: [`TECHNICAL_TEST.md`](TECHNICAL_TEST.md) · [`03_non_core/analytics/analytics/04_tools-and-technical-stack.md`](../../../03_non_core/analytics/analytics/04_tools-and-technical-stack.md).

---

### Domain 5: Python & Algorithmic Problem Solving (`[P2]` — Target Depth: L3)
* **What to Master**:
  * **Core Algorithms**: Two pointers, sliding window, prefix sums, hash maps, heaps, binary search, and intervals.
  * **Complexity Analysis**: Time complexity $O(N)$ vs $O(N \log N)$ and auxiliary space bounds.
  * **System Problem Context**: Telemetry parsing, sliding-window session monitoring, log anomaly detection, and task dependency graphs (DAG).
* **Practice Requirement**: Solve and verify all 20 Python coding problems in [`TECHNICAL_TEST.md`](TECHNICAL_TEST.md).
* **Core Files**: [`TECHNICAL_TEST.md`](TECHNICAL_TEST.md) · [`03_non_core/software-engineering/programming/python.md`](../../../03_non_core/software-engineering/programming/python.md).

---

### Domain 6: Cloud Computing & Enterprise Architecture (`[P2]` — Target Depth: L3)
* **What to Master**:
  * **Cloud Fundamentals**: IaaS vs PaaS vs SaaS; Public vs Private vs Hybrid vs Multi-Cloud.
  * **Microservices & Containers**: Docker containerization, Kubernetes orchestration, Serverless (AWS Lambda / Azure Functions).
  * **Enterprise Core Systems**: ERP (SAP S/4HANA), CRM (Salesforce), API Gateways, REST APIs, and Kafka event streaming.
  * **High Availability & Security**: RPO/RTO disaster recovery, Zero Trust architecture, RBAC, and data encryption.
* **Practice Requirement**: Review the 20 Cloud & Architecture questions in [`QUESTION_BANK.md`](QUESTION_BANK.md).
* **Core Files**: [`QUESTION_BANK.md`](QUESTION_BANK.md) · [`03_non_core/software-engineering/04_tools-and-technical.md`](../../../03_non_core/software-engineering/04_tools-and-technical.md).

---

### Domain 7: AI, Machine Learning & Enterprise Generative AI (`[P2]` — Target Depth: L3)
* **What to Master**:
  * **Classical ML Concepts**: Supervised vs unsupervised, classification vs regression, precision, recall, F1, ROC-AUC, and class imbalance.
  * **Enterprise GenAI & RAG**: Vector embeddings, chunking strategies, hybrid search (BM25 + vector cosine similarity), and grounded citations.
  * **AI Governance & ROI**: Mitigating hallucination, prompt injection guardrails, PII masking, and human-in-the-loop validation.
* **Practice Requirement**: Review the 20 AI/ML/GenAI questions in [`QUESTION_BANK.md`](QUESTION_BANK.md) and RAG cases in [`CONSULTING_CASES.md`](CONSULTING_CASES.md).
* **Core Files**: [`QUESTION_BANK.md`](QUESTION_BANK.md) · [`CONSULTING_CASES.md`](CONSULTING_CASES.md).

---

### Domain 8: Project Defense, Japan Readiness & Behavioral HR (`[P1]` — Target Depth: L4)
* **What to Master**:
  * **Civil/HWRE Project Defense**: Defending real IIT Kanpur projects ([`streamflow-time-series`](../../../08_projects/streamflow-time-series/), [`idf-pet`](../../../08_projects/idf-pet/), [`bridgerisk`](../../../08_projects/bridgerisk/)) using the 4-step framework without fabrication.
  * **Five Master STAR Stories**: Overcoming technical failure, cross-disciplinary conflict, independent continuous learning, pressure delivery, and cultural adaptability.
  * **Japanese Language & Relocation Strategy**: Communicating clear motivation for living in Tokyo, respecting *Ho-Ren-So*, *Nemawashi*, and *Kaizen*, and presenting a concrete pre-joining language plan utilizing Accenture's JPY 664,658 training program.
* **Practice Requirement**: Rehearse all 10 project-defense question sets in [`PROJECT_STRATEGY.md`](PROJECT_STRATEGY.md) and mock interviews in [`INTERVIEW.md`](INTERVIEW.md).
* **Core Files**: [`PROJECT_STRATEGY.md`](PROJECT_STRATEGY.md) · [`BEHAVIOURAL_HR.md`](BEHAVIOURAL_HR.md) · [`JAPAN_RELOCATION_AND_LANGUAGE.md`](JAPAN_RELOCATION_AND_LANGUAGE.md).
