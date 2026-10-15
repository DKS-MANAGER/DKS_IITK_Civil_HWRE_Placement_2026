# Syllabus and Topic Coverage Matrix — Deloitte USI Analyst

> **Document Type**: Master Syllabus & Coverage Specification  
> **Target Role**: Analyst (AI, Analytics & Technology Consulting)  
> **Status**: Comprehensive Curriculum Mapped to Job Description  

---

## 1. Curriculum Priority Framework

* **P1 — Core Foundations**: Essential prerequisites tested in Round 1 Online Assessments and technical screening. Zero tolerance for weak fundamentals.
* **P2 — Core Role Alignment**: Technologies and consulting capabilities explicitly central to day-to-day delivery in data, analytics, cloud, and modern AI.
* **P3 — Specialized Breadth**: Advanced AI, graph architectures, research methods, and domain enterprise workflows explicitly present in the job description.

---

## 2. Complete Syllabus Map

| Module Code | Topic & Subtopics | Priority | Prerequisites | Required Depth | Relevant JD Requirement | Teaching File & Section | Mastery Test |
| :--- | :--- | :---: | :--- | :--- | :--- | :--- | :--- |
| **M01-A** | Quantitative Aptitude (Percentages, Ratios, Time-Work, Speed, P&C, Probability) | **P1** | High school mathematics | Speed calculation & conceptual mastery | Analytical thinking, logical reasoning | [`01_APTITUDE...md#1`](01_APTITUDE_LOGICAL_REASONING_AND_VERBAL.md) | 25-question timed drill (< 30 mins) |
| **M01-B** | Logical Reasoning & Data Interpretation (Syllogisms, Puzzles, Charts) | **P1** | Basic deductive logic | Error-free constraint satisfaction | Problem-solving, analytical deduction | [`01_APTITUDE...md#2`](01_APTITUDE_LOGICAL_REASONING_AND_VERBAL.md) | Complex puzzle deduction in < 4 mins |
| **M01-C** | Verbal Ability & Business English | **P1** | English grammar & vocabulary | Professional business writing & comprehension | Spoken & written communication | [`01_APTITUDE...md#3`](01_APTITUDE_LOGICAL_REASONING_AND_VERBAL.md) | Error detection & comprehension drills |
| **M02-A** | Python Fundamentals & Data Structures (Strings, Lists, Dicts, Sets) | **P1** | None | Idiomatic coding & time complexity | Programming fundamentals | [`02_PYTHON...md#1`](02_PYTHON_PROGRAMMING_AND_DSA.md) | Clean code passing edge cases |
| **M02-B** | Algorithms & Problem Solving (Sliding Window, Two Pointers, Hashing, Binary Search, DP) | **P1** | Python syntax | Optimal Big-O implementation | Algorithmic problem-solving | [`02_PYTHON...md#2`](02_PYTHON_PROGRAMMING_AND_DSA.md) | Medium LeetCode-style problems |
| **M03-A** | SQL Relational Foundations (Keys, Normalization, NULL logic) | **P1** | Relational concepts | Strict understanding of 3-valued logic | Data manipulation & databases | [`03_SQL_DATABASES...md#1`](03_SQL_DATABASES_AND_DATA_MANIPULATION.md) | Schema design & normalization |
| **M03-B** | Advanced SQL (Joins, CTEs, Window Functions, Performance Tuning) | **P1** | Basic SQL | Writing multi-table analytical queries | Data integration & analytics | [`03_SQL_DATABASES...md#2`](03_SQL_DATABASES_AND_DATA_MANIPULATION.md) | Complex reporting queries |
| **M04-A** | Descriptive & Inferential Statistics (Distributions, CLT, Hypothesis Testing) | **P1** | Probability basics | P-value interpretation & significance testing | Analytics & interpretation | [`04_STATISTICS...md#1`](04_STATISTICS_ANALYTICS_AND_VISUALIZATION.md) | A/B test evaluation calculation |
| **M04-B** | Exploratory Data Analysis & Visualization (Dashboards, Matplotlib/Seaborn, KPIs) | **P1** | Statistics & Python | Chart selection & stakeholder storytelling | Analytics & communication | [`04_STATISTICS...md#2`](04_STATISTICS_ANALYTICS_AND_VISUALIZATION.md) | Dashboard mockups & insight synthesis |
| **M05-A** | Data Engineering Architecture (ETL/ELT, Lakehouses, Warehouses) | **P2** | SQL & databases | Modern data ecosystem design | Cloud-based data ecosystems | [`05_DATA_ENGINEERING...md#1`](05_DATA_ENGINEERING_CLOUD_AND_GOVERNANCE.md) | Pipeline architectural trade-offs |
| **M05-B** | Cloud Fundamentals (AWS, Azure, GCP comparison, Storage, Compute) | **P2** | General computing | Service mapping & cost trade-offs | Cloud ecosystems | [`05_DATA_ENGINEERING...md#2`](05_DATA_ENGINEERING_CLOUD_AND_GOVERNANCE.md) | Cloud migration case defense |
| **M05-C** | Data Quality, Governance & Security (Lineage, Access Control, GDPR) | **P2** | Enterprise data concepts | Governance framework construction | Governance, standards & security | [`05_DATA_ENGINEERING...md#3`](05_DATA_ENGINEERING_CLOUD_AND_GOVERNANCE.md) | Data audit protocol design |
| **M06-A** | Supervised & Unsupervised Machine Learning (Linear, Trees, Boosting, Clustering) | **P2** | Statistics & Python | End-to-end pipeline & metric selection | AI/ML technologies | [`06_MACHINE_LEARNING...md#1`](06_MACHINE_LEARNING_NLP_TIME_SERIES_AND_VISION.md) | Metric selection for imbalanced data |
| **M06-B** | Time-Series Forecasting (ARIMA, Seasonality, Stationarity, Lag Features) | **P3** | Statistics | Stationarity testing & lag feature design | Time-series analysis | [`06_MACHINE_LEARNING...md#2`](06_MACHINE_LEARNING_NLP_TIME_SERIES_AND_VISION.md) | Demand forecasting model pipeline |
| **M06-C** | NLP & Computer Vision Fundamentals (Embeddings, Classification, CNNs) | **P3** | Linear algebra basics | Representation learning intuition | NLP & Image recognition | [`06_MACHINE_LEARNING...md#3`](06_MACHINE_LEARNING_NLP_TIME_SERIES_AND_VISION.md) | Vector embedding search |
| **M07-A** | Transformer Architectures, LLM Mechanics & Prompt Engineering | **P2** | Deep learning intuition | Attention mechanism, tokenomics, prompt design | Generative AI & LLMs | [`07_GENERATIVE_AI...md#1`](07_GENERATIVE_AI_LLM_PROMPT_ENGINEERING_RAG.md) | Few-shot JSON prompt engineering |
| **M07-B** | Retrieval-Augmented Generation (RAG) Architecture & Failure Modes | **P2** | Vector embeddings | Chunking, hybrid search, hallucination guards | RAG & Cognitive tech | [`07_GENERATIVE_AI...md#2`](07_GENERATIVE_AI_LLM_PROMPT_ENGINEERING_RAG.md) | End-to-end RAG script validation |
| **M08-A** | Agentic AI Systems & Multi-Agent Workflows | **P3** | LLM APIs & Python | Tool use, state loops, guardrails, human-in-loop | Agentic AI & workflows | [`08_AGENTIC_AI...md#1`](08_AGENTIC_AI_GRAPH_ANALYTICS_AND_KNOWLEDGE_GRAPHS.md) | Agent stopping conditions & safety |
| **M08-B** | Graph Analytics, Knowledge Graphs & Graph Neural Networks | **P3** | Graph data structures | Entity resolution, Cypher queries, GNN intuition | Graph analytics & KG | [`08_AGENTIC_AI...md#2`](08_AGENTIC_AI_GRAPH_ANALYTICS_AND_KNOWLEDGE_GRAPHS.md) | Knowledge graph schema design |
| **M09-A** | Enterprise Platforms & ERP Workflows (S2P, O2C, Inventory) | **P3** | Business fundamentals | Process mapping & master data integration | Packaged enterprise platforms | [`09_ENTERPRISE_PLATFORMS...md#1`](09_ENTERPRISE_PLATFORMS_ERP_AND_PROCESS_IMPROVEMENT.md) | As-Is vs To-Be process mapping |
| **M09-B** | Business Process Improvement, Root Cause & Build vs. Buy | **P2** | Enterprise concepts | KPI bottleneck diagnosis & ROI calculation | Business-process improvement | [`09_ENTERPRISE_PLATFORMS...md#2`](09_ENTERPRISE_PLATFORMS_ERP_AND_PROCESS_IMPROVEMENT.md) | Process optimization case solution |
| **M10-A** | Structured Consulting Problem-Solving (Issue Trees, MECE, Hypotheses) | **P2** | Analytical logic | Hypothesis-driven problem decomposition | Analytical problem-solving | [`10_BUSINESS_CASES...md#1`](10_BUSINESS_CASES_RESEARCH_POC_AND_CLIENT_COMMUNICATION.md) | Structuring ambiguous business briefs |
| **M10-B** | 7 Detailed Enterprise Business Cases with Worked Solutions | **P2** | Cross-functional skills | Multi-step calculation & recommendation | Analytics & business cases | [`10_BUSINESS_CASES...md#2`](10_BUSINESS_CASES_RESEARCH_POC_AND_CLIENT_COMMUNICATION.md) | End-to-end case interviews |
| **M10-C** | Research, PoCs, Experimentation & Client Storytelling | **P2** | Communication | Designing PoC success criteria & executive decks | PoCs & client communication | [`10_BUSINESS_CASES...md#3`](10_BUSINESS_CASES_RESEARCH_POC_AND_CLIENT_COMMUNICATION.md) | Executive briefing slide outline |
| **M11-A** | Consulting Behavioral Scenarios & "Why Deloitte USI?" | **P1** | Introspection | STAR method storytelling & firm alignment | Client presentation, teamwork | [`11_INTERVIEW_BEHAVIOURAL...md#1`](11_INTERVIEW_BEHAVIOURAL_AND_SCENARIOS.md) | Confident verbal pitch delivery |
| **M11-B** | Shift Flexibility, Client Conflict, Ethics & Mock Client Meeting | **P1** | Professional conduct | De-escalation & operational resilience | Shifting requirements, client site | [`11_INTERVIEW_BEHAVIOURAL...md#2`](11_INTERVIEW_BEHAVIOURAL_AND_SCENARIOS.md) | Mock meeting defense |
