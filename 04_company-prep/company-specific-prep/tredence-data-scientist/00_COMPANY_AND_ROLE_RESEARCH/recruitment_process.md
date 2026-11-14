# 00 — Recruitment Process, Selection Workflow & Evidence Ledger
## Tredence Campus Hiring Stages, Evaluator Expectations, Preparation Guidelines & Verification Status

> **Document Status**: Recruitment Pipeline Evidence Audit `[TIER 1 / PROFORMA & CAMPUS AUDIT]`  
> **Source Material**: Official IIT Kanpur Placement Proforma, Company PPT Disclosures, Verified Historical Campus Debriefs.  
> **Evidentiary Constraint**: Confirmed proforma facts are distinguished from candidate debrief patterns. Test durations, platforms, question counts, or cutoff ratios are explicitly labeled where unconfirmed.

---

## 1. 6-Stage Selection Workflow Overview

The official IIT Kanpur Placement Proforma lists the following six stages for the Tredence Data Scientist recruitment drive:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              TREDENCE RECRUITMENT PIPELINE AUDIT                                       │
├───────────────────────┬───────────────────┬──────────────────────────────────────────┬─────────────────┤
│ Stage                 │ Proforma Status   │ Verified Campus Evidence                 │ Evidence Level  │
├───────────────────────┼───────────────────┼──────────────────────────────────────────┼─────────────────┤
│ 1. Application        │ Explicitly Listed │ Submission of formal campus CV via SPO   │ Confirmed Fact  │
├───────────────────────┼───────────────────┼──────────────────────────────────────────┼─────────────────┤
│ 2. Pre-Placement Talk │ Explicitly Listed │ 45–60 min presentation by Tredence       │ Confirmed Fact  │
│    (PPT)              │                   │ leadership covering Decision Intel, SPEED│                 │
├───────────────────────┼───────────────────┼──────────────────────────────────────────┼─────────────────┤
│ 3. Resume Shortlist   │ Explicitly Listed │ Filter for quantitative degree, Python/  │ Confirmed Fact  │
│                       │                   │ SQL coursework, ML/data science projects │                 │
├───────────────────────┼───────────────────┼──────────────────────────────────────────┼─────────────────┤
│ 4. Technical Test     │ Explicitly Listed │ Online screening test covering aptitude, │ Confirmed Fact  │
│                       │                   │ programming (Python), SQL, ML/stats      │ Platform Unstated│
├───────────────────────┼───────────────────┼──────────────────────────────────────────┼─────────────────┤
│ 5. Technical Interview│ Explicitly Listed │ Deep-dive technical round(s): live code, │ Confirmed Fact  │
│                       │                   │ ML math, time-series, project defense    │ Format Flexible │
├───────────────────────┼───────────────────┼──────────────────────────────────────────┼─────────────────┤
│ 6. HR Interview       │ Explicitly Listed │ Behavioral fit, communication, SPEED     │ Confirmed Fact  │
│                       │                   │ core values, location preferences        │ Final Round     │
└───────────────────────┴───────────────────┴──────────────────────────────────────────┴─────────────────┘
```

---

## 2. Granular Stage-by-Stage Analysis

### Stage 1: Application Submission
- **What it Evaluates**: Academic eligibility, basic degree alignment (M.Tech / B.Tech from premier university), branch eligibility.
- **Evidence Status**: `[TIER 1 / PROFORMA FACT]`. Proforma confirms M.Tech and B.Tech Civil Engineering candidates are eligible.
- **Recommended Preparation**: Ensure CV highlights Python, SQL, statistical modeling, machine learning, and time-series projects prominently in the upper third.
- **Common Mistakes**: Submitting a generic structural or construction management CV without prominent quantitative and computational programming sections.
- **Checklist**:
  - [ ] GitHub profile linked and clean.
  - [ ] Machine learning and time-series projects feature quantified metrics (ROC-AUC, RMSE, runtime improvements).
  - [ ] Python and SQL explicitly listed in technical skills section.

---

### Stage 2: Pre-Placement Talk (PPT)
- **What it Evaluates**: Candidate engagement, active listening, company awareness.
- **Evidence Status**: `[TIER 1 / PROFORMA FACT]`.
- **Observed Dynamic**: Tredence leadership typically discusses their retail/CPG client successes, proprietary platforms (MLWorks, Tredence Studio, Sancus), and the "Last-Mile Adoption" paradigm.
- **Recommended Preparation**: Take notes on specific client case studies mentioned by the speakers. Reference these in the technical and HR interviews to demonstrate genuine interest.
- **Common Mistakes**: Passive attendance without noting key executive names, platforms, or recent awards (e.g., Databricks Retail Partner of the Year).
- **Checklist**:
  - [ ] Note the speaker's name, practice vertical, and current strategic focus.
  - [ ] Prepare 1–2 intelligent questions regarding Tredence's agentic AI deployments or MLOps frameworks.

---

### Stage 3: Resume Shortlisting
- **What it Evaluates**: Quantitative rigor, project complexity, demonstrable programming capability.
- **Evidence Status**: `[TIER 1 / PROFORMA FACT]`.
- **Evaluator Expectations**: For non-CS/Data Science branches (such as M.Tech Civil HWRE), evaluators look for proof that the candidate writes real, production-style scientific code rather than just basic coursework scripts.
- **Recommended Preparation**: Frame engineering research around *computational modeling*, *stochastic differential equations*, *extreme-value probability distributions*, and *machine learning explainability*.
- **Common Mistakes**: Over-emphasizing civil engineering domain terminology (e.g., "scour depth", "concrete slump") instead of quantitative methodology (e.g., "non-linear Navier-Stokes PDE discretization", "tree-based ensemble learning with TreeSHAP").
- **Checklist**:
  - [ ] Verify that every project bullet follows the Action-Context-Metric formula.
  - [ ] Ensure SQL and advanced data libraries (Pandas, Scikit-learn, Statsmodels) are immediately visible.

---

### Stage 4: Technical Test (Online Assessment)
- **What it Evaluates**: Core quantitative problem solving, speed, accuracy, foundational programming, and database querying.
- **Evidence Status & Unverified Parameters**:
  - *Proforma Confirmation*: "Technical Test" is explicitly listed `[TIER 1]`.
  - *Unstated Parameters*: The proforma does **NOT** specify the testing platform (HackerEarth / Mettl / CoCubes / SHL), exact test duration (commonly 60–90 min in past campus drives), section counts, or negative marking rules `[UNVERIFIED]`.
- **Reported Campus Pattern (Past IIT/NIT Drives)**:
  - Section A: Quantitative Aptitude & Data Interpretation (15–20 MCQs).
  - Section B: Machine Learning, Statistics & Probability (15–20 MCQs).
  - Section C: SQL Analytical Queries (1–2 live query writing tasks or MCQs).
  - Section D: Python Programming / Data Manipulation (1–2 coding problems).
- **Recommended Preparation**: Complete the practice banks in Module 08 covering 50 Python questions, 50 SQL queries, 50 Statistics questions, and 60 ML questions.
- **Common Mistakes**: Getting stuck on a complex quantitative aptitude puzzle and running out of time for the high-yield SQL/Python coding problems.
- **Checklist**:
  - [ ] Practice timed window-function queries (DENSE_RANK, LAG, rolling sum).
  - [ ] Review binary search, two-pointer, and array manipulation algorithms in Python.
  - [ ] Review Bayes' theorem, conditional probability, and normal/binomial distribution math.

---

### Stage 5: Technical Interview Round(s)
- **What it Evaluates**: Mathematical foundations of ML algorithms, live problem-solving, code cleanliness, project authenticity, and commercial thinking ("Now What?").
- **Evidence Status**: `[TIER 1 / PROFORMA FACT]`. May be conducted as 1 or 2 sequential technical discussions depending on interviewer availability.
- **Typical Round Architecture**:
  1. *Candidate Introduction & Quantitative Pivot (5–7 min)*: Brief overview of background, why data science, and technical strengths.
  2. *Project Deep-Dive & Methodological Challenge (15–20 min)*: Explaining candidate's machine learning and time-series projects. Interviewer checks for genuine authorship by probing hyperparameters, data leakage prevention, feature engineering choices, and metric selection (why PR-AUC over ROC-AUC?).
  3. *Live Coding / SQL Exercise (15–20 min)*: Writing an analytical SQL query (e.g., second highest salary per department, customer retention cohort) or Python data processing logic on a shared screen.
  4. *Business Caselet / Problem Framing (10–15 min)*: A realistic client scenario (e.g., "A retail client is experiencing declining sales in Category X. How would you diagnose the problem and build a predictive model?").
  5. *Candidate Questions for Interviewer (3–5 min)*: Intelligent reverse questions regarding Tredence's decision intelligence accelerators.
- **Common Mistakes**:
  - Memorizing definitions without understanding mathematical mechanics (e.g., cannot write the logistic loss function or explain how a split is chosen in a gradient-boosted tree).
  - Failing to connect modeling results to business recommendations.
- **Checklist**:
  - [ ] Be ready to derive OLS, logistic sigmoid, Gini impurity, and MSE loss on a whiteboard.
  - [ ] Master the 5-stage project defense script (Problem $\to$ Math $\to$ Pipeline $\to$ Validation $\to$ Impact).
  - [ ] Practice articulating business trade-offs clearly without mathematical hand-waving.

---

### Stage 6: HR & Cultural Fit Interview
- **What it Evaluates**: Interpersonal communication, alignment with Tredence Core Values (SPEED), location flexibility, salary expectations, career ambition.
- **Evidence Status**: `[TIER 1 / PROFORMA FACT]`.
- **Core Topics**:
  - "Why Tredence over other analytics firms or product companies?"
  - Handling conflicting deadlines, client pressure, and working with cross-functional teams.
  - Location preference across Bengaluru, Hyderabad, Chennai, Gurugram, Pune, Kolkata.
- **Recommended Preparation**: Prepare 4–5 structured STAR behavioral stories demonstrating initiative, resolving technical disagreements, and managing tight timelines.
- **Common Mistakes**: Saying "I will work anywhere" without a thoughtful location rationale, or showing hesitation about client-facing consulting demands.
- **Checklist**:
  - [ ] Prepare an articulate answer for "Why consulting and decision intelligence?"
  - [ ] Align responses with the SPEED framework (Sense of Urgency, Partnership, Excellence, Entrepreneurial Spirit, Diversity).
