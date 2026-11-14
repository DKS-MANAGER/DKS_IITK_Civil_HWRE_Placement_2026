# Tredence — Data Scientist / Associate Data Scientist Preparation Hub
## IIT Kanpur Placement Season 2026–27 | Phase 1

> **Document Status**: Authoritative Company-Specific Placement Preparation Suite `[TIER 1 / PROFORMA & EMPIRICAL AUDIT]`  
> **Corporate Legal Entity**: Tredence Analytics Solutions Private Limited / Tredence Inc.  
> **Role Designation (Proforma)**: **Data Scientist** `[TIER 1 / PROFORMA FACT]`  
> **Role Designation (JD)**: **Associate Data Scientist** `[TIER 1 / JD FACT]`  
> **Target Candidate Profile**: M.Tech Civil Engineering (Hydraulics and Water Resources Engineering — HWRE), IIT Kanpur · B.Tech Civil Engineering  
> **Posting Locations**: Bengaluru, Hyderabad, Chennai, Gurugram, Pune, Kolkata `[TIER 1 / PROFORMA FACT]`  
> **Compensation Profile**: ₹14.5 LPA (Proforma & Main Slide) vs. ₹12.5 LPA (Secondary Slide) — *See Compensation Audit*  
> **Core Mandate**: Decision Intelligence, Last-Mile AI Adoption, Predictive & Prescriptive Analytics, Enterprise GenAI, and Vertical-Specific Delivery (Retail, CPG, Industrials, Telecom, Healthcare).

---

## 1. Executive Summary & The Tredence Decision Intelligence Paradigm

**Tredence Inc.** is a global data science and AI solutions firm founded in 2013 by **Shub Bhowmick**, **Sumit Mehra**, and **Shashank Dubey**, headquartered in San Jose, California, with global delivery operations anchored in Bengaluru, Chennai, Gurugram, Hyderabad, Kolkata, and Pune.

Unlike traditional IT consultancies that deliver passive dashboards or pure academic AI labs that build isolated models, Tredence differentiates itself by addressing the **"Last-Mile Adoption Problem"** in enterprise AI.

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              THE TREDENCE LAST-MILE ADOPTION PARADIGM                                 │
├───────────────────────────────────┬───────────────────────────────────┬────────────────────────────────┤
│      1. Business Problem          │       2. Algorithmic Core         │     3. Last-Mile Adoption      │
├───────────────────────────────────┼───────────────────────────────────┼────────────────────────────────┤
│ • Retail Out-of-Stock Loss        │ • Tree-Based Ensembles (LightGBM) │ • Automated Store Reorder APIs │
│ • CPG Trade Promotion Leakage     │ • Hierarchical Bayesian MMM       │ • Field Sales Mobile Workflows │
│ • Telecom Subscriber Churn        │ • Survival Analysis & Uplift Trees│ • Next-Best-Action Call Prompts│
│ • Industrial Asset Downtime       │ • Physics-Informed ML & Extremes  │ • Predictive Maintenance Flags │
│ • Supply Chain Volatility         │ • Mixed-Integer Linear Prog (MILP)│ • Dynamic Safety Stock Buffers │
└───────────────────────────────────┴───────────────────────────────────┴────────────────────────────────┘
```

The role of an **Associate Data Scientist / Data Scientist** at Tredence is not simply fitting an algorithm on clean data. It requires:
1. **Translating Business Ambiguity into a Structured Analytical Problem**: Defining objective functions, constraints, and measurable business KPIs.
2. **Developing Scalable, Interpretable Models**: Choosing models that balance accuracy with latency, governance, and business explainability (SHAP, feature attributions).
3. **Answering the "Now What?"**: Delivering concrete prescriptive interventions, operational workflows, and executive narratives that drive client revenue or EBITDA impact.

---

## 2. Master Directory Architecture

This preparation hub is organized into 14 specialized modules covering institutional research, technical disciplines, practical implementations, and behavioral readiness:

```text
tredence-data-scientist/
│
├── README.md                                  # Master navigation hub, executive overview & curriculum map
│
├── 00_COMPANY_AND_ROLE_RESEARCH/              # Institutional Intelligence & Recruitment Audit
│   ├── company_overview.md                    # Business model, "Last-Mile" philosophy, proprietary platforms
│   ├── india_operations.md                    # Delivery hubs (BLR, HYD, MAA, GGN, PNQ, CCU), work culture
│   ├── role_analysis.md                       # Associate Data Scientist responsibilities translated to rubrics
│   ├── jd_skill_mapping.md                    # 18-dimension JD competency taxonomy & priority tiers
│   ├── recruitment_process.md                 # 6-stage campus pipeline (PPT, Test, Tech Interviews, HR)
│   ├── compensation_verification.md           # Deep audit: ₹14.5 LPA vs ₹12.5 LPA slide discrepancy
│   └── source_registry.md                     # Provenance ledger with 5-tier evidence hierarchy
│
├── 01_PREPARATION_ROADMAP/                    # Strategic Execution Plans
│   ├── preparation_strategy.md                # 3-tier study methodology & allocation
│   ├── topic_priority_matrix.md               # P0 (Core) vs P1 (High Yield) vs P2 (Breadth)
│   ├── 7_day_plan.md                          # Emergency 7-day sprint plan
│   ├── 14_day_plan.md                         # Comprehensive 14-day mastery roadmap
│   └── final_revision_checklist.md            # 24-hour pre-interview exit checklist
│
├── 02_PYTHON_AND_DATA_ANALYSIS/               # Core Scientific Python Stack
│   ├── python_fundamentals.md                 # OOP, generators, decorators, memory management
│   ├── numpy.md                               # Vectorization, broadcasting, linear algebra, striding
│   ├── pandas.md                              # Advanced indexing, aggregation, windowing, memory downcasting
│   ├── eda_and_visualization.md               # Structured EDA pipelines, Seaborn, outlier handling
│   └── coding_questions.md                    # 50 production-grade Python coding problems & solutions
│
├── 03_SQL/                                    # Enterprise Analytical Database Analytics
│   ├── sql_notes.md                           # Processing order, relational algebra, indexing
│   ├── advanced_sql.md                        # Window functions (DENSE_RANK, LAG), CTEs, self-joins
│   ├── sql_question_bank.md                   # 50 real-world business analytical SQL queries
│   └── practice_datasets/                     # Synthetic schema & data files
│       └── mock_retail_cpg_schema.sql         # Retail / CPG multi-table schema with edge-case tests
│
├── 04_STATISTICS_AND_EXPERIMENTATION/         # Statistical Foundations & Business A/B Testing
│   ├── probability_and_statistics.md          # Distributions, CLT, Bayes' Theorem, estimators
│   ├── hypothesis_testing.md                  # Parametric vs non-parametric tests, p-values, power
│   ├── sample_size_estimation.md              # MDE, alpha, beta, variance sizing derivations
│   ├── ab_testing.md                          # Online experimentation, CUPED, network interference
│   └── numerical_problems.md                  # 50 solved statistical & experimental design questions
│
├── 05_MACHINE_LEARNING/                       # Predictive Modeling & Interpretability
│   ├── supervised_learning.md                 # OLS, Regularization, Logistic, Trees, Ensembles (LightGBM)
│   ├── unsupervised_learning.md               # K-Means, Hierarchical, DBSCAN, PCA, GMMs
│   ├── feature_engineering.md                 # Target encoding, WoE, cyclical encoding, imputation
│   ├── model_evaluation.md                    # ROC-AUC, PR-AUC, LogLoss, calibration curves, drift
│   ├── interpretability.md                    # TreeSHAP, Integrated Gradients, adverse action reasons
│   └── interview_questions.md                 # 60 technical ML interview deep-dives
│
├── 06_ADVANCED_ANALYTICS/                     # Advanced Vertical Methodologies
│   ├── time_series.md                         # Stationarity, ARIMA/SARIMA, rolling validation, intermittent
│   ├── graph_networks.md                      # Network analytics, Node2Vec, GNN foundations
│   ├── recommender_systems.md                 # Collaborative filtering, matrix factorization, cold start
│   ├── deep_learning.md                       # MLP, CNNs, LSTMs, Transformers, attention mechanisms
│   ├── computer_vision.md                     # Convolutions, architectures (ResNet), object detection
│   ├── nlp_nlu.md                             # TF-IDF, embeddings (Word2Vec), Transformer tokenization
│   └── reinforcement_learning.md              # MDP, Q-learning, exploration vs exploitation in business
│
├── 07_GENAI_AND_AGENTS/                       # Enterprise GenAI & Agentic AI Systems
│   ├── llm_fundamentals.md                    # Tokenization, self-attention, context windows, quantization
│   ├── embeddings_and_vector_search.md        # Cosine similarity, HNSW index, vector DBs (Chroma/FAISS)
│   ├── rag.md                                 # Chunking, hybrid search, cross-encoder reranking, RAG Triad
│   ├── agent_based_systems.md                 # ReAct loop, tool calling, multi-agent coordination
│   ├── evaluation_and_safety.md               # Hallucination metrics (Ragas, TruLens), guardrails
│   └── practical_exercises.md                 # 25 GenAI conceptual & design questions with code
│
├── 08_ASSESSMENT_PREPARATION/                 # Practice Banks & Timed Simulations
│   ├── python_assessment.md                   # 50 Python test questions with test cases
│   ├── sql_assessment.md                      # 50 SQL assessment queries across business cases
│   ├── statistics_assessment.md               # 50 Statistics & probability MCQs with derivations
│   ├── machine_learning_assessment.md         # 60 Machine learning MCQs with explanations
│   ├── genai_assessment.md                    # 25 GenAI & agent-based systems assessment items
│   └── mock_tests/                            # Timed Diagnostic Mock Assessments
│       ├── diagnostic_test_1.md               # 25-question cross-discipline diagnostic test
│       └── full_length_timed_mock.md          # 50-question 60-minute full-length simulation
│
├── 09_BUSINESS_CASES_AND_COMMUNICATION/       # The "Now What?" & Executive Delivery
│   ├── business_problem_framing.md            # MECE issue trees, translating ambiguity to math
│   ├── industry_cases.md                      # 20 full analytics cases across Retail, CPG, Telecom, Health
│   ├── executive_storytelling.md              # Pyramid Principle, slide design, communicating to CXOs
│   └── presentation_frameworks.md             # 8-step executive delivery presentation deck template
│
├── 10_PRACTICAL_PROJECTS/                     # 5 Standalone End-to-End Implementation Projects
│   ├── predictive_modelling/                  # Project 1: LightGBM / XGBoost customer churn + SHAP
│   ├── time_series_forecasting/               # Project 2: Multi-step SARIMA retail demand forecasting
│   ├── sql_business_analytics/                # Project 3: Production ANSI SQL retail analytics suite
│   ├── genai_rag/                             # Project 4: Production-grade RAG with hybrid search & rerank
│   └── prescriptive_analytics/                # Project 5: Scipy/PuLP promotion budget allocation optimizer
│
├── 11_INTERVIEW_PREPARATION/                  # Technical & Behavioral Interview Master Bank
│   ├── technical_interview.md                 # 100 deep-dive questions across all technical tracks
│   ├── project_deep_dive.md                   # Verbatim project defense frameworks (CFD, ML, Time-Series)
│   ├── business_interview.md                  # Live caselet solving & commercial troubleshooting
│   ├── behavioural_interview.md               # STAR responses mapped to Tredence Core Values (SPEED)
│   └── hr_questions.md                        # "Why Tredence?", compensation alignment, location choice
│
├── 12_CANDIDATE_FIT_AND_CV/                   # The Quantitative Engineering Pivot
│   ├── skill_gap_analysis.md                  # Transparent audit: demonstrated vs unpracticed skills
│   ├── project_mapping.md                     # Mapping HWRE engineering research to enterprise analytics
│   ├── resume_recommendations.md              # Data science resume bullet points with quantified metrics
│   ├── introduction_and_pitch.md              # 30-second and 3-minute interview introduction scripts
│   └── project_explanation_frameworks.md     # 5-stage project defense formula (Problem, Math, Code, Value)
│
└── 13_TRACKING_AND_REVISION/                  # Candidate Progress & Diagnostic Scorecards
    ├── preparation_tracker.md                 # Topic completion tracker and readiness percentage
    ├── mock_test_scores.md                    # Diagnostic assessment error log & score history
    ├── weak_topics.md                         # Targeted remediation registry for identified weak spots
    └── revision_log.md                        # Daily revision timestamp log
```

---

## 3. The Quantitative Engineering-to-Data Science Pivot

The candidate holds an **M.Tech in Civil Engineering (Hydraulics and Water Resources Engineering — HWRE) from IIT Kanpur** with an advanced engineering mathematics and computational modeling foundation.

Rather than treating the civil/environmental engineering background as a barrier, this preparation strategy frames it as a **commanding mathematical, physical, and algorithmic advantage**:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                        CANDIDATE'S ENGINEERING-TO-DATA SCIENCE PIVOT MATRIX                            │
├──────────────────────────────────────────┬─────────────────────────────────────────────────────────────┤
│   CANDIDATE'S ENGINEERING FOUNDATION     │                 TREDENCE DATA SCIENCE EQUIVALENCE           │
├──────────────────────────────────────────┼─────────────────────────────────────────────────────────────┤
│ • Machine Learning & Explainability      │ • Predictive Modeling & Customer Risk (Retail/CPG/Telecom)  │
│   (XGBoost, ROC-AUC 0.983, TreeSHAP)     │   (Class-imbalance weighting, PR-AUC, SHAP attribution)     │
├──────────────────────────────────────────┼─────────────────────────────────────────────────────────────┤
│ • Hydrological Time-Series & ARMA        │ • Retail Demand Forecasting & Inventory Planning            │
│   (Stationarity, ACF/PACF, seasonality)  │   (Rolling-window validation, promotional spikes, MAE/WAPE) │
├──────────────────────────────────────────┼─────────────────────────────────────────────────────────────┤
│ • Extreme Value Theory (Gumbel / GEV)    │ • Tail-Risk Modeling & Anomaly Detection                    │
│   (Return periods, MLE fitting)          │   (Supply chain stockouts, industrial failure probabilities)│
├──────────────────────────────────────────┼─────────────────────────────────────────────────────────────┤
│ • Numerical PDEs & Finite Volume Methods │ • Algorithm Optimization & Numerical Convergence            │
│   (Discretization, Courant stability)    │   (Gradient descent, loss surfaces, mathematical modeling)  │
├──────────────────────────────────────────┼─────────────────────────────────────────────────────────────┤
│ • Rigorous Research Thesis Ownership     │ • Structured Analytical Consulting & Business Storytelling  │
│   (Hypothesis formulation, benchmarking) │   (Translating ambiguous problems into measurable solutions)│
└──────────────────────────────────────────┴─────────────────────────────────────────────────────────────┘
```

---

## 4. Priority Tiers for Preparation

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                       TOPIC PRIORITY MATRIX                                            │
├────────────────────┬───────────────────────────────────────────┬───────────────────────────────────────┤
│    Priority Tier   │                 Disciplines               │             Primary Modules           │
├────────────────────┼───────────────────────────────────────────┼───────────────────────────────────────┤
│ Tier P0            │ • Advanced SQL (Windowing, CTEs, Joins)   │ Modules 02, 03, 04, 05, 08, 12        │
│ (Absolute Core)    │ • Vectorized Python (NumPy, Pandas, Scikit│                                       │
│                    │ • Core ML (Trees, Boosting, Regression)   │                                       │
│                    │ • Statistics & Hypothesis Testing         │                                       │
│                    │ • Candidate Project Deep-Dive Defense     │                                       │
├────────────────────┼───────────────────────────────────────────┼───────────────────────────────────────┤
│ Tier P1            │ • Time-Series Modeling (ARIMA, Rolling)   │ Modules 01, 04, 06, 09, 10, 11        │
│ (High Yield)       │ • Business A/B Testing & Sample Sizing    │                                       │
│                    │ • Model Interpretability (SHAP / Lime)    │                                       │
│                    │ • Business Case Framing ("Now What?")     │                                       │
│                    │ • Executive Storytelling (Pyramid Model)  │                                       │
├────────────────────┼───────────────────────────────────────────┼───────────────────────────────────────┤
│ Tier P2            │ • Enterprise GenAI & RAG Architecture     │ Modules 06, 07, 10                    │
│ (Differentiators)  │ • Recommender Systems & Graph Analytics   │                                       │
│                    │ • Deep Learning (CNNs, Transformers)      │                                       │
│                    │ • Prescriptive Optimization (MILP/LP)     │                                       │
└────────────────────┴───────────────────────────────────────────┴───────────────────────────────────────┘
```
