# KLA Corporation — 4-Week Strategic Study Guide
## Comprehensive Roadmap, Daily Milestones & Revision Strategy for IIT Kanpur Candidates

> **Document Status**: Structured Preparation Roadmap & Milestone Plan  
> **Target Role**: Applications Engineer `[OFFICIAL PROFORMA FACT]` (Functional CAE Benchmark)  
> **Target Candidate**: IIT Kanpur M.Tech Civil (Hydraulics & Water Resources Engineering)  
> **Placement Cycle**: IIT Kanpur Placement Season 2026–27 | Phase 1  

---

> [!NOTE]
> **PEDAGOGICAL PREPARATION FRAMEWORK (`[TIER 5]`):**
> This 4-week study roadmap is a structured pedagogical plan designed to systematically eliminate domain gaps, bridge computational fluid mechanics to semiconductor processes, and master SPC/Python requirements. It is a recommended preparation schedule developed for the candidate, not an official corporate recruitment timeline or mandated testing calendar.

---

## 1. Preparation Architecture & Phase Overview

To bridge the knowledge gap systematically without burning out, the preparation is organized into four sequential 7-day phases:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       4-WEEK PREPARATION TIMELINE                           │
├─────────────────────────────────────────────────────────────────────────────┤
│ WEEK 1: SEMICONDUCTOR FOUNDATIONS & MANUFACTURING FLOW                      │
│ • Focus: Silicon physics, FEOL/BEOL steps, litho/etch/CMP defect mechanisms.│
│ • Key Output: Master Rayleigh equations, Preston's law, and yield models.   │
├─────────────────────────────────────────────────────────────────────────────┤
│ WEEK 2: INSPECTION OPTICS, METROLOGY & STATISTICAL PROCESS CONTROL (SPC)    │
│ • Focus: Brightfield vs Darkfield, e-beam review, Shewhart charts, Cp/Cpk.  │
│ • Key Output: Solve all numerical SPC capability and limit problems.        │
├─────────────────────────────────────────────────────────────────────────────┤
│ WEEK 3: SCIENTIFIC PYTHON, KLARF PARSING, ML (ADC) & PERL BASICS            │
│ • Focus: Writing KLARF parsers, imbalanced XGBoost models, Perl regex.      │
│ • Key Output: Run and explain Projects 1, 2, and 3 codebases.               │
├─────────────────────────────────────────────────────────────────────────────┤
│ WEEK 4: THESIS DEFENSE, PIVOT SCRIPTS, FAB CASES & CUSTOMER DRILLS          │
│ • Focus: 3-minute pivot pitch, CFD transport analogy, 4 fab case studies.   │
│ • Key Output: Complete mock assessment and full-length simulated interview. │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Detailed Weekly Milestones & Daily Schedule

### Week 1: Semiconductor Foundations & Manufacturing Flow
* **Day 1**: Study [Module 01: Company and Role Research](01_COMPANY_AND_ROLE_RESEARCH.md). Understand KLA's ecosystem role (~50–55% market share in Process Diagnostics & Control), global customer context (SEC 10-K examples: TSMC, Samsung, Intel), and core Applications Engineer duties.
* **Day 2**: Read [Module 03: Semiconductor Fundamentals](03_SEMICONDUCTOR_FUNDAMENTALS_AND_YIELD.md) Section 1 & 2. Learn silicon ingot crystal growth (Czochralski), wafer slicing, and the complete FEOL vs. BEOL manufacturing sequence.
* **Day 3**: Deep dive into **Photolithography**. Master the Rayleigh resolution equation ($CD = k_1 \frac{\lambda}{NA}$) and Depth of Focus ($DOF$). Understand ArF immersion ($193\text{ nm}$) vs. EUV ($13.5\text{ nm}$).
* **Day 4**: Deep dive into **CMP & Etch**. Master Preston’s law ($MRR = k_p \cdot P \cdot V$), dishing, erosion, and micro-scratch formation. Understand plasma etch anisotropy and selectivity.
* **Day 5**: Study **Semiconductor Yield Modeling**. Derive the Poisson Yield Model ($Y = e^{-A D_0}$) and Negative Binomial Model ($Y = (1 + A D_0 / \alpha)^{-\alpha}$). Understand defect clustering physics.
* **Day 6**: Review killer vs. nuisance defect distinctions. Solve worked numerical problems in Module 03.
* **Day 7**: Weekly Self-Assessment. Write down the entire 7-step fab sequence from memory without referring to notes.

---

### Week 2: Inspection Optics, Metrology & Statistical Process Control (SPC)
* **Day 8**: Study [Module 04: Inspection, Metrology & Process Control](04_INSPECTION_METROLOGY_AND_PROCESS_CONTROL.md) Section 1. Contrast Brightfield (BF) normal specular illumination with Darkfield (DF) oblique scatterometry.
* **Day 9**: Study optical defect detection algorithms: Die-to-Die (D2D) and Die-to-Statistical-Image (D2SI) subtraction. Understand noise thresholding ($T = \mu + k\sigma$) and the Receiver Operating Characteristic (ROC) curve.
* **Day 10**: Study **Metrology Systems**: Overlay metrology (IBO vs. DBO) on KLA Archer, and Optical Critical Dimension (OCD) on SpectraShape. Understand overlay error budgets.
* **Day 11**: Study **Statistical Process Control (SPC)**. Master Shewhart $\bar{X}-R$ and $\bar{X}-S$ charts. Memorize the 4 Western Electric rules for detecting process drift.
* **Day 12**: Derive process capability indices: $C_p = \frac{USL - LSL}{6\sigma}$ and $C_{pk} = \min(\frac{USL - \mu}{3\sigma}, \frac{\mu - LSL}{3\sigma})$. Master the difference between process potential and centering.
* **Day 13**: Study Root-Cause Analysis (RCA) tools: Ishikawa (Fishbone 6M) diagrams, 5-Whys, and Failure Mode and Effects Analysis (FMEA).
* **Day 14**: Solve Questions 10 through 12 in [Module 09: Simulated Assessment](09_SIMULATED_ASSESSMENT_AND_QUESTION_BANK.md).

---

### Week 3: Python Data Analytics, ML (ADC) & Perl Automation
* **Day 15**: Study [Module 05: Statistics, Data Analytics & Scientific Python](05_STATISTICS_DATA_ANALYTICS_AND_PYTHON.md). Understand the structure of industry-standard **KLARF** text inspection files.
* **Day 16**: Run and examine the Python `KlarfParser` class in Module 05. Practice extracting die grid coordinates (`XINDEX`, `YINDEX`) and computing global millimeter locations (`X_GLOBAL`, `Y_GLOBAL`).
* **Day 17**: Study [Module 06: Machine Learning & Perl Scripting](06_MACHINE_LEARNING_AND_PERL_SCRIPTING.md). Understand Automated Defect Classification (ADC) feature engineering (Area, Aspect Ratio, Optical Contrast, Radial Distance).
* **Day 18**: Study imbalanced learning in fab analytics: why Accuracy fails under 95:5 class imbalance, tuning `scale_pos_weight` in XGBoost, and using PR-AUC over ROC-AUC.
* **Day 19**: Study **SHAP Explainable AI** for fab root-cause analysis. Connect it to your BridgeRisk deterioration project at IIT Kanpur.
* **Day 20**: Master **Perl Scripting Essentials**. Review scalars (`$`), arrays (`@`), hashes (`%`), and regex capturing (`$line =~ /LotID\s+"([^"]+)"/`). Run the 50-line Perl script in Module 06.
* **Day 21**: Run [Module 11 Projects 1 and 2](11_PRACTICE_PROJECTS_PORTFOLIO.md) locally; verify that you can walk an interviewer through every function.

---

### Week 4: Project Defense, Pivot Script, Fab Cases & Customer Scenarios
* **Day 22**: Study [Module 07: Engineering Problem-Solving & CFD Pivot](07_ENGINEERING_PROBLEM_SOLVING_AND_CFD_PIVOT.md). Master the transport phenomena bridge: mapping OpenFOAM Navier-Stokes fluid mechanics to CMP slurry lubrication and CVD gas transport.
* **Day 23**: Rehearse the **3-minute Civil-to-Semiconductor interview pivot script**. Practice delivering it aloud until it sounds natural, confident, and non-defensive.
* **Day 24**: Rehearse your M.Tech and B.Tech project defenses: OpenFOAM CFD sediment modeling, BridgeRisk XGBoost/SHAP, and IDF curve statistical derivation.
* **Day 25**: Study [Module 08: Customer-Facing Engineering & HR](08_CUSTOMER_FACING_SCENARIOS_AND_HR.md). Memorize the 5-phase customer escalation protocol and practice your confident >80% travel defense.
* **Day 26**: Study [Module 10: Technical Interview & Case Studies](10_TECHNICAL_INTERVIEW_AND_CASE_STUDIES.md). Thoroughly review all 4 fab engineering troubleshooting cases (Post-CMP scratches, optical nuisance explosion, overlay drift, and BKM node transfer failure).
* **Day 27**: Timed Practice Test: Complete all 15 questions in [Module 09: Simulated Assessment](09_SIMULATED_ASSESSMENT_AND_QUESTION_BANK.md) in 45 minutes under exam conditions. Check score against the answer key.
* **Day 28**: Final Verification Audit. Benchmark against the 10-point checklist in [READINESS_SCORECARD.md](READINESS_SCORECARD.md). Rest well before interview day.
