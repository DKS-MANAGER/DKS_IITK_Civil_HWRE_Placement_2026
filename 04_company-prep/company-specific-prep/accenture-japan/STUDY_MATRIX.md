# Accenture Japan Digital Consultant — Master Study Matrix

> **Target Role**: Digital Consultant (Analyst Entry Level), Accenture Japan Ltd.  
> **Target Candidate**: IIT Kanpur Civil / HWRE Graduate transitioning to Digital Consulting  
> **Matrix Standard**: Topic-by-topic placement roadmap mapping priorities, required depth, canonical repo modules, and mastery benchmarks.

---

## 🏛️ Priority & Depth Taxonomy
* **Priority**:
  * `[P0]`: Essential / Mandatory screening & interview barrier.
  * `[P1]`: High-Yield / Core differentiator during Manager & Director rounds.
  * `[P2]`: Secondary / Useful contextual depth.
  * `[P3]`: Optional / Supplementary background.
* **Required Depth (Mastery Level)**:
  * **L1 (Awareness)**: Define concept, business purpose, and high-level relevance.
  * **L2 (Working)**: Understand mechanics, architecture, and solve standard problems.
  * **L3 (Interview Ready)**: Defend architectural choices, trade-offs, and solve live cases/queries under time pressure.
  * **L4 (Strong Candidate)**: Synthesize ambiguous business-tech challenges, handle partner pushback, and lead executive recommendations.

---

## 📊 Comprehensive Topic-by-Topic Study Matrix

| ID | Domain | Topic | Priority | Target Depth | What to Know (Core Concepts) | Practice Required | Canonical Repo Source | Mastery Test / Benchmark |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- | :--- | :--- |
| **01** | **Company & Role** | Accenture Business Model & Tech-Agnostic DX | `[P0]` | **L4** | Technology-agnostic consulting vs pure SWE; 3 career paths (BizxTech, PM, Specialist); End-to-end transformation lifecycle. | 60-sec role pitch; 90-sec 'Why Accenture Japan' | [`ROLE.md`](ROLE.md) · [`PLACEMENT_FACTS.md`](PLACEMENT_FACTS.md) | Articulate role value proposition without hesitation in <90s. |
| **02** | **Consulting** | MECE Structuring & Issue Trees | `[P0]` | **L4** | Mutually Exclusive, Collectively Exhaustive deconstruction; mathematical vs process vs customer-journey trees. | 15 timed issue-tree drills (90s each) | [`03_non_core/consulting/02_problem-solving.md`](../../../03_non_core/consulting/02_problem-solving.md) | Build a 3-level MECE tree for an ambiguous business problem in 90 seconds. |
| **03** | **Consulting** | Digital Transformation (DX) Case Archetypes | `[P0]` | **L4** | Problem Diagnosis -> Tech Architecture -> Change Management -> Value Realization; Legacy modernization, Omnichannel. | 8 full DX cases with architecture blueprints | [`CONSULTING_CASES.md`](CONSULTING_CASES.md) | Diagnose operational bottleneck and architect a 3-tier digital solution with KPIs in 10 mins. |
| **04** | **Consulting** | Industry X & Smart Factory IoT | `[P0]` | **L3** | Sensors -> Gateways -> Edge -> Cloud Ingestion; Predictive maintenance, OEE calculation, Digital Twins, MES integration. | 5 Industry X factory cases | [`CONSULTING_CASES.md`](CONSULTING_CASES.md) · [`03_non_core/operations/`](../../../03_non_core/operations/) | Explain edge-to-cloud IoT pipeline for machine downtime reduction. |
| **05** | **Consulting Math** | Business Arithmetic & Unit Economics | `[P0]` | **L3** | CAGR, Rule of 72, Margins (Gross/EBITDA), Break-even, CAC, LTV, LTV/CAC, Payback period, Fast mental math. | 10 consulting math timed drills | [`01_common/placement-math/`](../../../01_common/placement-math/) · [`03_non_core/consulting/05_consulting-math.md`](../../../03_non_core/consulting/05_consulting-math.md) | Compute LTV/CAC and break-even capacity utilization mentally with zero paper errors. |
| **06** | **Aptitude** | Quantitative Speed Math & Data Interpretation | `[P0]` | **L3** | Percentages, Ratios, Time-Speed-Distance, Mixtures, Probability, Permutations, Multi-table DI. | Complete 3 Aptitude Section Tests | [`01_common/aptitude/quantitative/`](../../../01_common/aptitude/quantitative/) · [`mocks/`](../../../01_common/aptitude/mocks/) | Score >=85% on Aptitude Sectional Assessment. |
| **07** | **Aptitude** | Logical & Critical Reasoning | `[P0]` | **L3** | Coding-Decoding, Seating Arrangements, Syllogisms, Series, Flowcharts, Statement-Assumptions. | Complete 2 Logical Reasoning Mocks | [`01_common/aptitude/logical-reasoning/`](../../../01_common/aptitude/logical-reasoning/) | Solve 15 logic puzzles with 100% accuracy under 15 minutes. |
| **08** | **Digital Tech** | Cloud Computing & Modernization Strategy | `[P0]` | **L3** | IaaS/PaaS/SaaS, AWS vs Azure vs GCP selection criteria, Hybrid Cloud, Containers (Docker), Microservices, Serverless, RTO/RPO. | 5 Cloud Migration & Architecture cases | [`WHAT_TO_STUDY.md`](WHAT_TO_STUDY.md) · [`03_non_core/software-engineering/04_tools-and-technical.md`](../../../03_non_core/software-engineering/04_tools-and-technical.md) | Defend multi-cloud vs single-cloud strategy for a Japanese banking client. |
| **09** | **Digital Tech** | Enterprise Systems & Integration Architecture | `[P1]` | **L3** | ERP (SAP S/4HANA), CRM (Salesforce), SCM, REST APIs, JSON, API Gateways, Webhooks, Message Queues (Kafka/RabbitMQ). | 3 Enterprise System Integration scenarios | [`WHAT_TO_STUDY.md`](WHAT_TO_STUDY.md) | Explain API Gateway rate limiting and ERP-CRM data synchronization. |
| **10** | **AI & GenAI** | Enterprise Generative AI & RAG Architecture | `[P0]` | **L3** | LLMs, Embeddings, Vector Databases, RAG Pipeline (Query -> Embedding -> Retrieval -> LLM), Fine-Tuning vs RAG, Guardrails, AI ROI. | 5 Enterprise GenAI & RAG case studies | [`CONSULTING_CASES.md`](CONSULTING_CASES.md) · [`WHAT_TO_STUDY.md`](WHAT_TO_STUDY.md) | Diagram enterprise RAG architecture ensuring zero PII data leakage. |
| **11** | **Data & SQL** | Relational SQL & Analytical Querying | `[P0]` | **L3** | Multi-table JOINs, GROUP BY, HAVING, Subqueries, CTEs, Window Functions (`ROW_NUMBER`, `RANK`, `LAG`, `LEAD`), Cohort retention. | Solve 40 SQL Problems (15 Easy, 20 Med, 5 Hard) | [`TECHNICAL_TEST.md`](TECHNICAL_TEST.md) · [`03_non_core/analytics/analytics/04_tools-and-technical-stack.md`](../../../03_non_core/analytics/analytics/04_tools-and-technical-stack.md) | Write multi-table SQL query with window functions and CTEs in under 5 minutes. |
| **12** | **Coding Logic** | Python / Algorithmic Problem Solving | `[P0]` | **L3** | Arrays, Strings, Dictionaries, Two Pointers, Sliding Window, Prefix Sums, Time/Space Complexity O(N). | Solve 30 Technical Coding Questions | [`TECHNICAL_TEST.md`](TECHNICAL_TEST.md) · [`03_non_core/software-engineering/programming/python.md`](../../../03_non_core/software-engineering/programming/python.md) | Implement clean Python solution with O(N) complexity in under 8 minutes. |
| **13** | **Cybersecurity** | Enterprise Security & Governance Basics | `[P1]` | **L2** | CIA Triad, Zero Trust Architecture, MFA, RBAC, Least Privilege, TLS encryption, Data Privacy, Compliance. | 2 Security & Compliance Case Reviews | [`WHAT_TO_STUDY.md`](WHAT_TO_STUDY.md) | Explain Zero Trust security model for remote enterprise workforce. |
| **14** | **Project Defense** | IIT Civil / HWRE Technical Defense | `[P0]` | **L4** | Problem Statement -> Methodology (OpenFOAM/Python/HEC-RAS/ML) -> Key Bottleneck -> Quantified Result; Cloud scaling vision. | 30s, 60s, and 2-min pitch for thesis & projects | [`PROJECT_STRATEGY.md`](PROJECT_STRATEGY.md) · [`08_projects/`](../../../08_projects/) | Flawlessly defend technical choices, assumptions, and cloud scaling for thesis. |
| **15** | **Career Story** | Engineering to Digital Consulting Pivot | `[P0]` | **L4** | Translating numerical modeling/systems engineering into commercial digital transformation; 'Why not Civil?' 'Why not SWE?'. | Rehearse pivot pitch 10 times | [`ROLE.md`](ROLE.md) · [`BEHAVIOURAL_HR.md`](BEHAVIOURAL_HR.md) | Explain career transition convincingly with zero defensiveness. |
| **16** | **Japan Readiness** | Cross-Cultural & Language Commitment | `[P0]` | **L4** | Professional etiquette, Nemawashi (consensus building), attention to detail, commitment to Japanese language training. | Rehearse Japan motivation & learning plan | [`BEHAVIOURAL_HR.md`](BEHAVIOURAL_HR.md) · [`INTERVIEW.md`](INTERVIEW.md) | Articulate concrete 18-month Japanese language roadmap and Tokyo career goals. |
| **17** | **Behavioral** | STAR Story Bank & Leadership | `[P0]` | **L4** | 5 core STAR stories: Overcoming technical failure, cross-functional conflict, learning new tech, leadership under pressure. | Complete 5 detailed STAR story worksheets | [`BEHAVIOURAL_HR.md`](BEHAVIOURAL_HR.md) · [`01_common/behavioral/`](../../../01_common/behavioral/) | Deliver a crisp STAR story in under 90 seconds with clear business takeaways. |

---

## 🧭 How to Use This Matrix
1. **Initial Diagnostic**: Review each topic and check your starting depth level (L1 to L4).
2. **Execution Sprints**: Follow the [Study Guide](STUDY_GUIDE.md) and execute topic blocks in priority order (`[P0]` -> `[P1]`).
3. **Tracking & Quality**: Log all problem-solving mistakes in [ERROR_LOG.md](ERROR_LOG.md) and compute your weekly benchmark score using [READINESS_SCORECARD.md](READINESS_SCORECARD.md).
