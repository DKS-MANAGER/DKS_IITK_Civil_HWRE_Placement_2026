# Module 02 — Role Specification, Recruitment Process & Evidentiary Ledger

## 1. Recruitment Pipeline Evidence Ledger

This table audits the selection process for the **Barclays Quantitative Analytics Graduate Analyst (BA4)** role at IIT Kanpur, comparing official proforma facts with verified candidate debriefs from premier Indian engineering campuses:

```
┌────────────────────────┬───────────────────┬──────────────────────────────────────────┬───────────────────────┬────────────┐
│         Stage          │  Proforma Status  │         Publicly Reported Reality        │        Source         │ Confidence │
├────────────────────────┼───────────────────┼──────────────────────────────────────────┼───────────────────────┼────────────┤
│ 1. Resume Shortlisting │ Explicitly Listed │ Filters for quantitative GPA, programming│ Campus Placement      │ High       │
│                        │                   │ fluency (Python/C++), and math rigor.    │ Debriefs (IIT/NIT)    │            │
├────────────────────────┼───────────────────┼──────────────────────────────────────────┼───────────────────────┼────────────┤
│ 2. Technical / Quant   │ Implied in hiring │ 60–90 min online assessment covering     │ GeeksforGeeks,        │ High       │
│    Screening Test      │ pipeline          │ probability, statistics, Python & SQL.   │ PrepLounge Debriefs   │            │
├────────────────────────┼───────────────────┼──────────────────────────────────────────┼───────────────────────┼────────────┤
│ 3. Technical Interview │ Explicitly Listed │ 45–60 min deep dive into credit risk,    │ Verified Candidate    │ High       │
│    (Round 1: Risk QA)  │                   │ metrics (ROC/Gini/KS/PSI), and ML stats. │ Interview Reports     │            │
├────────────────────────┼───────────────────┼──────────────────────────────────────────┼───────────────────────┼────────────┤
│ 4. Quantitative & Case │ Explicitly Listed │ Practical model monitoring scenarios,    │ Senior Quant Debriefs │ High       │
│    Triage (Round 2)    │                   │ IFRS 9 ECL mechanics, portfolio MIS.     │ (Noida Hub)           │            │
├────────────────────────┼───────────────────┼──────────────────────────────────────────┼───────────────────────┼────────────┤
│ 5. Leadership & Values │ Explicitly Listed │ 30–45 min round: Behavioral fit, Barclays│ Glassdoor India,      │ High       │
│    (HR / Director)     │                   │ RISES Values, cross-border stakeholders. │ AmbitionBox           │            │
└────────────────────────┴───────────────────┴──────────────────────────────────────────┴───────────────────────┴────────────┘
```

---

## 2. Technical Screening Test Architecture

When an online screening assessment is administered, it typically features three core quantitative sections:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 ONLINE ASSESSMENT SECTIONAL BREAKDOWN                                  │
├──────────────────────┬─────────────┬───────────┬───────────────────────────────────────────────────────┤
│       Section        │  Questions  │ Time Alloc│                      Core Topics                      │
├──────────────────────┼─────────────┼───────────┼───────────────────────────────────────────────────────┤
│ Section 1: Probability│ 12–15 MCQs  │ 25–30 min │ • Conditional probability, Bayes' theorem,            │
│ & Applied Statistics │             │           │ • Distributions (Normal, Binomial, Poisson, Gumbel)   │
│                      │             │           │ • Hypothesis testing, p-values, central limit theorem │
├──────────────────────┼─────────────┼───────────┼───────────────────────────────────────────────────────┤
│ Section 2: Data &    │ 12–15 MCQs  │ 20–25 min │ • Logistic regression odds ratios, confusion matrices │
│ Risk Fundamentals    │             │           │ • Credit risk definitions (PD, LGD, EAD, Expected Loss│
│                      │             │           │ • ROC-AUC, Gini coefficient, KS statistic, and PSI    │
├──────────────────────┼─────────────┼───────────┼───────────────────────────────────────────────────────┤
│ Section 3: Hands-On  │ 2 Coding    │ 35–40 min │ • Python data manipulation (NumPy array operations,   │
│ Python / SQL Queries │ Problems    │           │   Pandas aggregation, vectorized metric calculation)  │
│                      │             │           │ • SQL window functions, CTEs, and loan default flags. │
└──────────────────────┴─────────────┴───────────┴───────────────────────────────────────────────────────┘
```

---

## 3. The Technical Interview Format (Rounds 1 & 2)

Conducted by Vice Presidents, Directors, or Lead Quantitative Analysts from the Noida QA team, the technical interviews assess mathematical depth, statistical intuition, and practical troubleshooting ability.

```
┌─────────────────────────────────┬─────────────────────────────────┬─────────────────────────────────┐
│  Segment 1: Theory (20 mins)    │   Segment 2: Triage (25 mins)   │  Segment 3: Coding (15 mins)    │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ • Credit risk definitions       │ • Live model deterioration case │ • Vectorized Python code        │
│ • Deriving Gini from ROC-AUC    │ • Investigating a Gini drop     │ • Writing SQL window query      │
│ • Explaining PSI formula        │ • Recommending PMA vs rebuild   │ • Pandas data cleaning check    │
│ • IFRS 9 3-stage ECL mechanics  │ • Macroeconomic stress impacts  │ • Edge case validation          │
└─────────────────────────────────┴─────────────────────────────────┴─────────────────────────────────┘
```

### 3.1 Live Troubleshooting Simulation Archetype
Interviewers frequently present a realistic operational scenario:
> *"Suppose you are monitoring the UK Residential Mortgage Probability of Default (PD) model for Q3. The historical development Gini was 0.72. Over the last two quarters, the monitored Gini dropped sharply to 0.54, while the Population Stability Index (PSI) jumped to 0.28. 
> 1. How do you interpret these two metrics together?
> 2. How do you isolate whether this is driven by an economic shock, borrower mix shift, or a broken data pipeline?
> 3. What concrete action do you recommend in the Model Monitoring Pack presented to the Model Governance Committee?"*

---

## 4. The Leadership & HR Fit Interview

Barclays evaluates candidates against its globally recognized **RISES Values**:

```
┌─────────────────────────────────┬────────────────────────────────────────────────────────────────────────┐
│         Barclays Value          │                     What It Means in Model Monitoring                  │
├─────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ 1. Respect                      │ Listening to portfolio risk teams; cross-cultural empathy when working │
│                                 │ with London and New York credit officers; valuing diverse perspectives.│
├─────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ 2. Integrity                    │ Absolute honesty in reporting model flaws; never suppressing a model   │
│                                 │ deterioration warning to please business lending targets.              │
├─────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ 3. Service                      │ Supporting portfolio teams with timely, automated, and accurate packs; │
│                                 │ helping business units understand regulatory capital implications.     │
├─────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ 4. Excellence                   │ Zero tolerance for flawed mathematical derivations or unverified code; │
│                                 │ continuous pursuit of monitoring automation and robust documentation.  │
├─────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ 5. Stewardship                  │ Protecting the bank’s long-term capital safety; ensuring models comply │
│                                 │ with PRA and Basel regulatory standards for future generations.        │
└─────────────────────────────────┴────────────────────────────────────────────────────────────────────────┘
```

### 4.1 Common Candidate Elimination Traps
1. **The "Front-Office Trader" Delusion**: Talking exclusively about Black-Scholes options pricing, stochastic volatility, or high-frequency trading. This demonstrates a complete failure to read the job description, which is explicitly focused on **credit risk model monitoring**.
2. **Confusing Discrimination with Calibration**: Claiming that a high ROC-AUC proves a model is accurate. (A model can have a perfect 0.90 AUC and still underestimate default rates by 500%!).
3. **Black-Box Machine Learning Bias**: Believing that an uninterpretable deep neural network is always superior to a well-calibrated logistic regression scorecard in regulated credit risk.

---

## 5. Official Barclays Selection & Assessment Framework (BA1–BA4)

Barclays evaluates candidates for Graduate Analyst (BA4) positions using its official **Selection and Assessment Framework**. Candidates are assessed against **3 to 5 competencies** selected from the framework:

```
┌─────────────────────────────────┬─────────────────────────────────┬──────────────────────────────────────────┐
│ Competency Area (BA1–BA4)       │ Underlying Capabilities         │ Behavioral Focus for BA4 Graduate Analyst│
├─────────────────────────────────┼─────────────────────────────────┼──────────────────────────────────────────┤
│ 1. Leadership Skills            │ • Developing Others             │ Provides constructive objective feedback;│
│                                 │ • Enabling High Performance     │ takes accountability for own development;│
│                                 │                                 │ embraces autonomy to deliver objectives. │
├─────────────────────────────────┼─────────────────────────────────┼──────────────────────────────────────────┤
│ 2. Business Skills              │ • Continuous Improvement & Inn. │ Applies systematic review methodologies; │
│                                 │ • Defining & Executing Change   │ embraces new ways of working; considers  │
│                                 │ • Commercial Decision Making    │ broad bank operational metrics & impact. │
├─────────────────────────────────┼─────────────────────────────────┼──────────────────────────────────────────┤
│ 3. Interpersonal Skills         │ • Building Self-Insight         │ Reflects on own strengths and weaknesses;│
│                                 │ • Building Relationships        │ establishes trust-based relationships;   │
│                                 │ • Working Collaboratively       │ integrates others' opinions into work.   │
├─────────────────────────────────┼─────────────────────────────────┼──────────────────────────────────────────┤
│ 4. Control Environment          │ • Building an Effective         │ Proactively identifies risk; understands │
│                                 │   Control Environment           │ personal responsibility for controls;    │
│                                 │                                 │ escalates risk events in line with policy│
├─────────────────────────────────┼─────────────────────────────────┼──────────────────────────────────────────┤
│ 5. Technical Skills             │ • Role-Specific Risk QA Skills  │ Mastery of model performance monitoring; │
│                                 │ • Planning & Organising (BA4)   │ prioritizes long-term outcomes; engages  │
│                                 │                                 │ colleagues to deliver strategic goals.   │
└─────────────────────────────────┴─────────────────────────────────┴──────────────────────────────────────────┘
```


