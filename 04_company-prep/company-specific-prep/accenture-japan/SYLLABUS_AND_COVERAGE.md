# Accenture Japan Digital Consultant — Master Syllabus & Coverage Architecture

> **Document Status**: Authoritative Placement Curriculum & Verification Index  
> **Target Role**: Digital Consultant (Analyst Entry Level) (`[JD VERIFIED]`)  
> **Employing Entity**: Accenture Japan Ltd. (`[JD VERIFIED]`)  
> **Target Audience**: IIT Kanpur Undergraduate & Postgraduate Students (`[JD VERIFIED]`)  
> **Curriculum Standard**: Comprehensive, self-contained textbook-style course covering digital consulting foundations, consulting mathematics, Python, SQL, cloud & enterprise architecture, enterprise AI/RAG, case interviews, behavioral competencies, and Japan relocation readiness.

---

## 1. Syllabus Classification Hierarchy

To ensure students prioritize high-yield preparation while mastering necessary technical depth, topics are organized into three clear priority tiers:

1. **Tier 1: Core Proforma & JD Requirements (`[CORE — JD/PROFORMA]`)**:
   - Explicitly listed in the official Accenture Japan Job Description PDF (`Accenture Japan 2026- Digital Consultant Job Description.pdf`) or IIT Kanpur Phase 1 Placement Proforma.
   - Includes: Diagnosing business challenges, technology selection (Cloud, AI/Data, Industry X, IoT), translating tech into business strategies, defining what should be built, full consulting lifecycle, programming/technical test, and native-level English with openness to learn Japanese.
2. **Tier 2: Supporting Consulting & Analytical Pillars (`[SUPPORTING]`)**:
   - Technical and consulting competencies essential for performing effectively in technical tests and case interviews.
   - Includes: MECE issue trees, digital transformation case frameworks, consulting math (unit economics, margins, break-even, LTV/CAC), Python algorithmic problem solving (sliding window, two-pointer, hash maps), SQL window functions and CTEs, enterprise integration (REST APIs vs Kafka), and cloud migration patterns.
3. **Tier 3: Supplementary Advanced Material (`[SUPPLEMENTARY]`)**:
   - Advanced technical and domain-specific specializations that distinguish top candidates in Director-level interviews but should not displace core preparation.
   - Includes: Microservices design trade-offs, vector database indexing algorithms (HNSW), fine-tuning vs RAG, distributed transaction patterns (Saga), and Industry X IoT sensor edge computing.

---

## 2. Master Curriculum & Verification Concordance Table

| Domain | Topic & Subtopics | Priority | Evidence | Prerequisites | Teaching Resource | Worked Examples | Questions & Answers | Practical Exercises | Mastery Criteria | Verification Status |
| :--- | :--- | :---: | :--- | :--- | :--- | :---: | :---: | :---: | :--- | :---: |
| **Digital Consulting Foundations** | What digital consulting is; contrast with strategy, SE, IT ops; problem diagnosis; business-to-tech translation; stakeholder alignment; feasibility, security, TCO | `[CORE — JD/PROFORMA]` | Explicitly named in JD: "Diagnose client challenges & design enterprise solutions" | Basic business awareness | [`ROLE.md#1-executive-summary-what-is-a-digital-consultant`](ROLE.md#1-executive-summary-what-is-a-digital-consultant) · [`ROLE.md#4-end-to-end-teaching-case-manufacturing-predictive-maintenance`](ROLE.md#4-end-to-end-teaching-case-manufacturing-predictive-maintenance) | 2 complete end-to-end models | 10 Q&As in `QUESTION_BANK.md` | 3 architecture drills | Explain digital consulting value, 5 JD duties, and 3 career paths without buzzwords in $< 90\text{s}$. | `[VERIFIED]` |
| **Structured Problem Solving & Cases** | MECE issue trees, hypothesis-driven solving, root-cause analysis, process mapping, bottleneck analysis, 14-step case structure | `[CORE — JD/PROFORMA]` | Required in Round 1 & Round 2 interviews (`[JD VERIFIED]`) | Logic fundamentals | [`CONSULTING_CASES.md#1-the-14-point-digital-case-interview-architecture`](CONSULTING_CASES.md#1-the-14-point-digital-case-interview-architecture) | 15 full cases | 15 follow-up Q&A sets | 15 timed issue-tree drills | Decompose ambiguous business problem into 3-level MECE tree in $< 90\text{s}$; deliver structured case recommendation in $< 10\text{m}$. | `[VERIFIED]` |
| **Consulting Mathematics & Quant** | Margins (Gross/EBITDA), unit economics, LTV/CAC, break-even volume, Rule of 72, CAGR, NPV, payback period, market sizing | `[SUPPORTING]` | "Deliver measurable outcomes" (`[JD VERIFIED]`) | High school algebra | [`TECHNICAL_TEST.md#4-section-3-consulting-mathematics--unit-economics`](TECHNICAL_TEST.md#4-section-3-consulting-mathematics--unit-economics) · [`CONSULTING_CASES.md#3-structured-market-sizing-and-guesstimates`](CONSULTING_CASES.md#3-structured-market-sizing-and-guesstimates) | 20 math problems + 10 guesstimates | 20 worked solutions | 10 independent drills | Calculate margins, break-even, and payback mentally with zero arithmetic errors; size Tokyo markets in $< 5\text{m}$. | `[VERIFIED]` |
| **Python Fundamentals & Algorithms** | Syntax, data structures, strings, dicts, two-pointer, sliding window, binary search, stacks, prefix sums, Big-O complexity | `[CORE — JD/PROFORMA]` | Online Technical / Coding Test (`[JD VERIFIED]`) | Basic programming syntax | [`TECHNICAL_TEST.md#3-section-2-python-coding--algorithmic-logic`](TECHNICAL_TEST.md#3-section-2-python-coding--algorithmic-logic) | 20 complete 12-component problems | 20 dry runs & complexity analyses | 20 runnable test suites | Implement clean, runnable Python solution with optimal time/space complexity and dry run in $< 10\text{m}$. | `[VERIFIED]` |
| **SQL & Enterprise Data Manipulation** | Relational schemas, table grains, PK/FK, logical processing order, joins, NULL semantics, CTEs, window functions (`ROW_NUMBER`, `DENSE_RANK`, `LAG`, `LEAD`, moving averages) | `[SUPPORTING]` | Data retrieval & manipulation in technical assessment | Relational algebra basics | [`TECHNICAL_TEST.md#2-section-1-sql--data-analytics`](TECHNICAL_TEST.md#2-section-1-sql--data-analytics) | 30 complete enterprise queries | 30 explanations & edge-case audits | 30 synthetic schema drills | Formulate error-free ANSI SQL queries with CTEs and window functions on synthetic schemas in $< 4\text{m}$. | `[VERIFIED]` |
| **Cloud Computing & Architecture** | IaaS/PaaS/SaaS, public/private/hybrid, AWS/Azure/GCP, HA/DR (RTO/RPO), shared responsibility, 6 Rs migration, Strangler Fig pattern, retail inventory migration scenario | `[CORE — JD/PROFORMA]` | Named in JD cutting-edge tech: "Cloud, enterprise architecture" | Operating systems & networks | [`QUESTION_BANK.md#3-cloud-computing--enterprise-architecture-deep-dive`](QUESTION_BANK.md#3-cloud-computing--enterprise-architecture-deep-dive) · [`STUDY_GUIDE.md#domain-6-cloud-computing--system-architecture`](STUDY_GUIDE.md#domain-6-cloud-computing--system-architecture) | 4 architecture design models | 20 conceptual & trade-off Q&As | 4 migration case studies | Evaluate AWS vs Azure vs on-prem objectively; diagram Strangler Fig cloud migration with SLA and RTO/RPO targets. | `[VERIFIED]` |
| **Enterprise AI, ML & GenAI** | AI vs ML vs DL, supervised/unsupervised, overfitting, metrics vs business ROI, LLMs, embeddings, RAG vs fine-tuning, vector search, hallucinations, data privacy/governance | `[CORE — JD/PROFORMA]` | Named in JD cutting-edge tech: "AI/Data Analytics, GenAI & automation" | Python & linear algebra | [`QUESTION_BANK.md#4-ai-machine-learning--enterprise-genai`](QUESTION_BANK.md#4-ai-machine-learning--enterprise-genai) · [`CONSULTING_CASES.md#case-2-enterprise-genai--rag--policy-search-for-a-japanese-life-insurer`](CONSULTING_CASES.md#case-2-enterprise-genai--rag--policy-search-for-a-japanese-life-insurer) | 3 complete RAG & ML pipelines | 20 AI/GenAI Q&As | 3 AI business case studies | Diagram end-to-end RAG architecture with vector retrieval, embeddings, citations, and privacy guardrails. | `[VERIFIED]` |
| **Digital Transformation Strategy** | Digitization vs transformation, build vs buy vs partner, ERP modernization, data platforms, TCO & value realization, change management, pilot design | `[CORE — JD/PROFORMA]` | "Translate technology into actionable business strategies" (`[JD VERIFIED]`) | Enterprise systems | [`ROLE.md#2-five-explicit-job-responsibilities`](ROLE.md#2-five-explicit-job-responsibilities) · [`CONSULTING_CASES.md`](CONSULTING_CASES.md) | 5 strategy decision matrices | 15 strategy Q&As | 5 pilot design drills | Build structured decision matrix comparing custom build vs SaaS package with 5-year TCO and change risks. | `[VERIFIED]` |
| **Japanese Readiness & Relocation** | Language roadmap (JLPT N5 $\to$ N2), workplace culture (*Ho-Ren-So*, *Nemawashi*), relocation budgeting, housing, ward office registration, bank accounts | `[CORE — JD/PROFORMA]` | "Mindset open to learning Japanese essential; Tokyo affiliation" (`[JD VERIFIED]`) | Open mindset | [`JAPAN_RELOCATION_AND_LANGUAGE.md`](JAPAN_RELOCATION_AND_LANGUAGE.md) | 1 comprehensive relocation plan | 10 cultural interview Q&As | 1 Tokyo cost-of-living budget | Articulate 18-month Japanese learning plan and professional cultural adaptation (*Ho-Ren-So*) convincingly. | `[VERIFIED]` |
| **Behavioural Interviews & Fit** | STAR storytelling, conflict resolution, ambiguity handling, failure recovery, persuading stakeholders, cross-border teams | `[CORE — JD/PROFORMA]` | Evaluated in Manager (R1) and Director (R2) interviews (`[JD VERIFIED]`) | Genuine candidate experience | [`BEHAVIOURAL_HR.md`](BEHAVIOURAL_HR.md) · [`INTERVIEW.md`](INTERVIEW.md) | 10 authentic STAR frameworks | 30 behavioural scenarios | 10 delivery drills | Deliver structured STAR narrative in $< 90\text{s}$ with quantifiable business/technical impact and zero fabrication. | `[VERIFIED]` |
| **Project & Resume Technical Defense** | Grounded defense of engineering research (CFD, hydrology, extreme tail risk, numerical modeling) mapped to consulting competencies | `[CORE — JD/PROFORMA]` | Candidate degree requirement (`[JD VERIFIED]`) | Academic research thesis | [`PROJECT_STRATEGY.md`](PROJECT_STRATEGY.md) · [`RESUME_STRATEGY.md`](RESUME_STRATEGY.md) | 3 engineering project archetypes | 15 technical grilling Q&As | 3 project translation drills | Defend modeling assumptions, validation metrics, and limitations; articulate engineering-to-consulting transfer smoothly. | `[VERIFIED]` |

---

## 3. Course Navigation & Sequential Study Path

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                   CANONICAL ACCENTURE JAPAN STUDY ROADMAP                              │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Step 01: Role & Facts Architecture  ──► PLACEMENT_FACTS.md · ROLE.md                  │
│ Step 02: Structured Problem Solving ──► CONSULTING_CASES.md (14-Point Framework)       │
│ Step 03: Consulting Math & Aptitude ──► TECHNICAL_TEST.md (Section 3) · Cases          │
│ Step 04: Python Coding & Algorithms ──► TECHNICAL_TEST.md (Section 2 - 20 Problems)   │
│ Step 05: SQL & Data Manipulation    ──► TECHNICAL_TEST.md (Section 1 - 30 Queries)     │
│ Step 06: Cloud & Architecture       ──► QUESTION_BANK.md (Section 3)                   │
│ Step 07: Enterprise AI & GenAI      ──► QUESTION_BANK.md (Section 4) · Cases           │
│ Step 08: Japan Culture & Relocation ──► JAPAN_RELOCATION_AND_LANGUAGE.md               │
│ Step 09: Behavioral & Fit (STAR)    ──► BEHAVIOURAL_HR.md · INTERVIEW.md               │
│ Step 10: Engineering Project Defense──► PROJECT_STRATEGY.md · RESUME_STRATEGY.md       │
│ Step 11: Master Question Bank Drills──► QUESTION_BANK.md                               │
│ Step 12: Readiness Benchmark        ──► READINESS_SCORECARD.md · RAPID_REVISION.md     │
└────────────────────────────────────────────────────────────────────────────────────────┘
```
