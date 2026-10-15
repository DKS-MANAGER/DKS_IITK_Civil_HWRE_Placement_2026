# Citi AIM Analytics — Preparation Schedules & Readiness Scorecard

> **Target Role**: Spec Analytics Analyst — Business Analytics (SBS), Citi AIM  
> **Purpose**: Structured preparation roadmaps (30, 14, 7, 3, and 1-day) and an objective self-assessment rubric.  
> **Important Disclaimer**: All scores, target benchmarks, and timelines in this document are **internal study-planning heuristics** (`[PREPARATION RECOMMENDATION]`), NOT official company-mandated cutoffs.

---

## 1. Structured Preparation Roadmaps

### 1.1 The 30-Day Comprehensive Mastery Plan
*Target Audience: Candidates starting preparation 1 month before Phase 1 tests.*

| Phase & Days | Focus Area | Specific Topics & Resources | Practice Target | Tangible Completion Criterion |
| :--- | :--- | :--- | :--- | :--- |
| **Week 1 (Days 1–7)** | **Probability & Basic Statistics** | Axioms, conditional probability, Bayes' Theorem, Discrete & Continuous distributions, CLT, sampling errors. Study [`01_STATISTICS_PROBABILITY.md`](01_STATISTICS_PROBABILITY.md). | Solve 20 probability and distribution numericals. Practice mental math in [`01_common/aptitude/quantitative/`](../../../01_common/aptitude/quantitative/). | $100\%$ accuracy on Bayes conditional updates and CLT confidence interval derivations. |
| **Week 2 (Days 8–14)** | **SQL & Data Manipulation** | Execution order, Joins, NULL semantics, CTEs, Window functions (`ROW_NUMBER`, `DENSE_RANK`, `LAG`, `LEAD`, cumulative frames). Study [`02_SQL_DATA_MANIPULATION.md`](02_SQL_DATA_MANIPULATION.md). | Solve all 30 SQL problems. Verify queries on paper or a local PostgreSQL instance. | Able to write complex CTEs with window functions without referencing documentation. |
| **Week 3 (Days 15–21)**| **Hypothesis Testing & Predictive Modeling** | $Z$, $t$, Welch's $t$, ANOVA, $\chi^2$, Linear & Logistic regression, KS statistic, K-Means, RFM segmentation. Study [`03_PREDICTIVE_MODELING_ML.md`](03_PREDICTIVE_MODELING_ML.md). | Solve 15 hypothesis testing scenarios and 10 modeling metric evaluation exercises. | Clearly explain odds ratios, p-value definitions, confusion matrix trade-offs, and KS decile tables. |
| **Week 4 (Days 22–27)**| **Cases, Visualization & Project Defense** | 10 Banking Cases in [`04_INTERVIEW_AND_CASES.md`](04_INTERVIEW_AND_CASES.md), Visualization rules in [`05_DATA_VISUALIZATION_AND_BUSINESS_COMMUNICATION.md`](05_DATA_VISUALIZATION_AND_BUSINESS_COMMUNICATION.md), Project defense in [`07_PROJECT_AND_RESUME_DEFENCE.md`](07_PROJECT_AND_RESUME_DEFENCE.md). | Work through all 10 business cases using the 10-point framework. Rehearse 2-minute elevator pitch. | Articulate defensible business recommendations and defend M.Tech engineering research quantitatively. |
| **Final (Days 28–30)**| **Mock Testing & Rapid Revision** | Timed mocks in [`01_common/aptitude/mocks/`](../../../01_common/aptitude/mocks/). Behavioural prep in [`06_BEHAVIOURAL_STAKEHOLDERS_COMPLIANCE.md`](06_BEHAVIOURAL_STAKEHOLDERS_COMPLIANCE.md). Quick review via [`RAPID_REVISION.md`](RAPID_REVISION.md). | Complete 2 full-length timed mocks. Rehearse 5 STAR behavioural answers. | Complete all 9 scorecard areas at "Interview-Ready" or "Strong" level. |

---

### 1.2 The 14-Day Accelerated Plan
*Target Audience: Candidates with a 2-week preparation window.*

* **Days 1–3: Probability & Distribution Fundamentals**: Study [`01_STATISTICS_PROBABILITY.md`](01_STATISTICS_PROBABILITY.md). Solve Questions 1–15. Focus on Bayes, Binomial, Poisson, Normal, and CLT.
* **Days 4–7: SQL Mastery**: Work through [`02_SQL_DATA_MANIPULATION.md`](02_SQL_DATA_MANIPULATION.md). Write out solutions for Exercises 1–20. Master `DENSE_RANK`, `LAG`, and rolling aggregations.
* **Days 8–10: Hypothesis Testing & Modeling**: Study [`03_PREDICTIVE_MODELING_ML.md`](03_PREDICTIVE_MODELING_ML.md). Master Logistic regression, Precision/Recall trade-offs, ROC-AUC, and the KS statistic.
* **Days 11–12: Banking Cases & Data Communication**: Study [`04_INTERVIEW_AND_CASES.md`](04_INTERVIEW_AND_CASES.md) (Cases 1–5) and [`05_DATA_VISUALIZATION_AND_BUSINESS_COMMUNICATION.md`](05_DATA_VISUALIZATION_AND_BUSINESS_COMMUNICATION.md).
* **Days 13–14: Resume Defense & Behavioural Mock**: Review [`07_PROJECT_AND_RESUME_DEFENCE.md`](07_PROJECT_AND_RESUME_DEFENCE.md) and [`06_BEHAVIOURAL_STAKEHOLDERS_COMPLIANCE.md`](06_BEHAVIOURAL_STAKEHOLDERS_COMPLIANCE.md). Review formula sheets in [`RAPID_REVISION.md`](RAPID_REVISION.md).

---

### 1.3 The 7-Day High-Yield Sprint
*Target Audience: Candidates shortlisted for an assessment scheduled in one week.*

* **Day 1**: Probability & Bayes: Review Section 1–2 in [`01_STATISTICS_PROBABILITY.md`](01_STATISTICS_PROBABILITY.md); solve 10 numericals.
* **Day 2**: Sampling, CLT & Hypothesis Tests: Review Section 3–5 in [`01_STATISTICS_PROBABILITY.md`](01_STATISTICS_PROBABILITY.md); master $Z$, $t$, $\chi^2$, and p-value interpretation.
* **Day 3**: Core SQL: Review Section 1–3 in [`02_SQL_DATA_MANIPULATION.md`](02_SQL_DATA_MANIPULATION.md); solve Problems 1–15 (Joins, aggregations, basic window functions).
* **Day 4**: Advanced SQL & Aggregations: Solve Problems 16–30 in [`02_SQL_DATA_MANIPULATION.md`](02_SQL_DATA_MANIPULATION.md) (fraud velocity, churn, consecutive drops).
* **Day 5**: Predictive Modeling & Evaluation: Study [`03_PREDICTIVE_MODELING_ML.md`](03_PREDICTIVE_MODELING_ML.md); focus on Logistic regression, Precision vs Recall, and KS statistic.
* **Day 6**: Business Cases & Visualization: Work through Cases 1–4 in [`04_INTERVIEW_AND_CASES.md`](04_INTERVIEW_AND_CASES.md); read [`05_DATA_VISUALIZATION_AND_BUSINESS_COMMUNICATION.md`](05_DATA_VISUALIZATION_AND_BUSINESS_COMMUNICATION.md).
* **Day 7**: Project Defense & Behavioural Fit: Rehearse Civil-to-Citi pitch in [`07_PROJECT_AND_RESUME_DEFENCE.md`](07_PROJECT_AND_RESUME_DEFENCE.md); review Citi compliance culture in [`06_BEHAVIOURAL_STAKEHOLDERS_COMPLIANCE.md`](06_BEHAVIOURAL_STAKEHOLDERS_COMPLIANCE.md); run through [`RAPID_REVISION.md`](RAPID_REVISION.md).

---

### 1.4 The 3-Day Emergency Sequence
*Target Audience: Intensive review 72 hours prior to interview.*

* **Day 1 (Morning & Afternoon)**: Complete [`01_STATISTICS_PROBABILITY.md`](01_STATISTICS_PROBABILITY.md) (Formulas, Bayes, distributions, hypothesis tests, solve Questions 1–12).
* **Day 2 (Full Day)**: Write out SQL queries 1–15 in [`02_SQL_DATA_MANIPULATION.md`](02_SQL_DATA_MANIPULATION.md). Study Logistic Regression and KS deciles in [`03_PREDICTIVE_MODELING_ML.md`](03_PREDICTIVE_MODELING_ML.md).
* **Day 3 (Full Day)**: Read Cases 1–3 in [`04_INTERVIEW_AND_CASES.md`](04_INTERVIEW_AND_CASES.md). Rehearse your elevator pitch in [`07_PROJECT_AND_RESUME_DEFENCE.md`](07_PROJECT_AND_RESUME_DEFENCE.md). Memorize the formula sheet in [`RAPID_REVISION.md`](RAPID_REVISION.md).

---

### 1.5 The 1-Day Emergency Revision Sequence
*Target Audience: Last-minute checklist 24 hours before interview.*

* **Hour 1–2**: Probability & Stats: Review probability formulas, Bayes equation, p-value definition, and Type I/II errors in [`RAPID_REVISION.md`](RAPID_REVISION.md).
* **Hour 3–4**: SQL Drills: Review the 10 core SQL patterns in [`RAPID_REVISION.md`](RAPID_REVISION.md); mentally write `DENSE_RANK` and `LAG` CTEs.
* **Hour 5**: Modeling & Evaluation: Review confusion matrix, ROC-AUC, and KS decile interpretation.
* **Hour 6**: Business Case Mechanics: Skim Case 1 (Credit cut-off) and Case 2 (Deposit decline) in [`04_INTERVIEW_AND_CASES.md`](04_INTERVIEW_AND_CASES.md).
* **Hour 7**: Project Defense: Practice the 2-minute pitch explaining why engineering modeling transfers to financial analytics ([`07_PROJECT_AND_RESUME_DEFENCE.md`](07_PROJECT_AND_RESUME_DEFENCE.md)).
* **Hour 8**: Behavioural & Ethics: Review compliance escalation and stakeholder management frameworks in [`06_BEHAVIOURAL_STAKEHOLDERS_COMPLIANCE.md`](06_BEHAVIOURAL_STAKEHOLDERS_COMPLIANCE.md).

---

## 2. Objective Readiness Scorecard

Evaluate your readiness across the 9 core competency areas using this 4-tier rubric:

### The 4-Tier Assessment Scale
* **Level 1 — Awareness (Score: 1)**: Recognizes terms and concepts, but unable to solve numerical problems or write queries without external reference material.
* **Level 2 — Developing (Score: 2)**: Solves straightforward problems with hints; understands theory but makes syntax or logical errors in edge cases.
* **Level 3 — Interview-Ready (Score: 3)**: Solves standard problems accurately and explains trade-offs clearly under timed conditions; writes valid SQL and calculates statistics from memory.
* **Level 4 — Strong (Score: 4)**: Demonstrates first-principles mastery; identifies hidden assumptions and edge cases; connects statistical outputs directly to commercial banking decisions and risk governance.

---

### Candidate Self-Assessment Matrix

| # | Competency Area | Primary Evaluation Criterion | Level 1: Awareness | Level 2: Developing | Level 3: Interview-Ready | Level 4: Strong | Target Level | Current Score |
| :-: | :--- | :--- | :--- | :--- | :--- | :--- | :---: | :---: |
| **1** | **Probability & Statistics** | Accuracy on Bayes' theorem, distributions, expectations, and CLT. | Knows basic formulas; struggles with multi-step Bayes or Poisson. | Solves single-step problems; makes algebra errors under pressure. | Solves Bayes, Binomial, Normal, and CLT problems accurately within 3 mins each. | Derives distributions from first principles; explains failure modes and approximations. | **Level 3** | ___ / 4 |
| **2** | **Quantitative & Logical Reasoning** | Speed, estimation, and logical deductions on test puzzles and graphs. | Misses key deduction clues; slow mental arithmetic. | Solves standard questions; struggles with multi-constraint puzzles. | Solves speed math, estimation, and classic puzzles (25 horses, hats) with clear logic. | Explains general solution bounds; performs rapid order-of-magnitude estimation flawlessly. | **Level 3** | ___ / 4 |
| **3** | **SQL & Data Manipulation** | Syntax, logical order, Joins, NULLs, CTEs, and Window functions. | Writes basic `SELECT` and `WHERE`; confused by Joins and NULLs. | Writes basic Joins and `GROUP BY`; struggles with Window functions and frame clauses. | Writes clean CTEs with `DENSE_RANK`, `LAG`, and rolling frames without an IDE. | Writes optimized queries, identifies indexing implications, and handles tricky NULL edge cases. | **Level 3** | ___ / 4 |
| **4** | **Statistical Testing & Inference** | $Z$, $t$, Welch's $t$, ANOVA, $\chi^2$, p-values, and error trade-offs. | Confuses Type I and Type II errors; misstates p-value definition. | Selects correct test; makes errors calculating standard error or degrees of freedom. | Formulates $H_0/H_1$, computes test statistics, and interprets p-values correctly. | Identifies violation of assumptions (homoscedasticity, normality); recommends robust non-parametric tests. | **Level 3** | ___ / 4 |
| **5** | **Predictive Modeling & ML** | Linear/Logistic regression, segmentation, metrics, and KS statistic. | Treats models as black boxes; knows only accuracy. | Understands log-odds; confuses precision vs recall trade-offs. | Explains odds ratios, ROC-AUC, confusion matrix, K-Means, and KS decile separation. | Discusses data leakage, probability calibration, class imbalance techniques (SMOTE, weighting), and PSI drift. | **Level 3** | ___ / 4 |
| **6** | **Visualization & Communication** | Chart selection, dashboard layout, Minto Pyramid synthesis. | Produces cluttered, poorly labeled charts; explains methods rather than findings. | Picks standard charts; includes redundant information or confusing dual axes. | Selects clean visual encodings; structures executive summaries (Finding $\rightarrow$ Implication $\rightarrow$ Action). | Anticipates stakeholder objections; frames statistical results in dollars and risk mitigation. | **Level 3** | ___ / 4 |
| **7** | **Business Case Solving** | Problem structuring, issue trees, data identification, trade-offs. | Jumps directly to solutions without structured problem breakdown. | Builds partial issue trees; misses key cost or revenue drivers. | Structures MECE issue trees; identifies required data; calculates break-even and ROI. | Synthesizes commercial impact with risk trade-offs, operational constraints, and follow-up KPIs. | **Level 3** | ___ / 4 |
| **8** | **Project & Resume Defense** | Explaining actual engineering projects quantitatively without exaggeration. | Memorized descriptions; unable to defend methodology or data choices. | Explains what was done; struggles to connect engineering tools to analytics competencies. | Defends data sources, modeling choices, and results with quantitative precision; connects to analytics. | Candidly discusses research limitations, alternative models, and what could be improved with more data. | **Level 3** | ___ / 4 |
| **9** | **Stakeholder & Compliance Mindset**| Handling conflicting demands, ethical risk, and matrix teamwork. | Gives superficial answers; treats ethics as purely theoretical. | Gives generic teamwork examples; weak on regulatory risk culture. | Articulates structured STAR stories on conflict resolution, error escalation, and compliance adherence. | Demonstrates mature professional judgment balancing business growth with regulatory safety and ethics. | **Level 3** | ___ / 4 |

---

### 3. Readiness Scoring Benchmark (Internal Study Heuristic)

Sum your ratings across the 9 areas (Total Possible Score: 36 points):

* **Score: 30–36 (Strong / Interview-Ready)**: High likelihood of clearing technical and analytical grilling. Focus on mock interview polish and stamina.
* **Score: 23–29 (Developing / Targeted Review Needed)**: Good foundational knowledge with specific weak spots (typically Window SQL, advanced hypothesis testing, or case structuring). Allocate 80% of remaining study time to areas rated Level 1 or 2.
* **Score: < 23 (Critical Gaps)**: Risk of failing technical assessment or early interview grilling. Immediately execute the high-yield topics in the 7-day sprint plan.
