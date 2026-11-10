# 23 — Study Roadmap & 100-Point Readiness Diagnostic Tracker

## IIT Kanpur Placement Preparation — Barclays Quantitative Analytics (QA Model Monitoring)

---

### Executive Overview & Preparation Strategy

Securing the **Barclays Quantitative Analytics Graduate Analyst (BA4) — QA Model Monitoring** role requires mastering a multi-disciplinary curriculum spanning mathematical statistics, credit risk modeling, regulatory frameworks, production programming, and institutional governance.

This roadmap provides three calibrated preparation tracks:
1. **Track A (30-Day Comprehensive Mastery):** Complete, ground-up theoretical and operational mastery.
2. **Track B (14-Day Intensive Sprint):** Focused execution for candidates with solid mathematical fundamentals.
3. **Track C (7-Day Emergency Crash Course):** High-yield triage targeting core interview questions and project defense.

---

### 1. Preparation Roadmaps

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                 Preparation Architecture                               │
├───────────────────────────────┬────────────────────────────────┬───────────────────────┤
│ Phase 1: Quant Core (Days 1-7)│ Phase 2: Risk & Models (8-16)  │ Phase 3: Polish (17-30│
├───────────────────────────────┼────────────────────────────────┼───────────────────────┤
│ • Probability distributions   │ • Credit scorecards & WoE      │ • Mock technical viva │
│ • Hypothesis testing & Z-tests│ • Basel Vasicek capital derivation│ • Candidate project defense│
│ • GLMs & Logistic regression  │ • IFRS 9 staging & multi-scenario│ • RISES behavioral prep │
│ • Vectorized Python & ANSI SQL│ • Discrimination, Calibration, │ • 100-point diagnostic│
│   pipelines                   │   and PSI / CSI mechanics      │   verification        │
└───────────────────────────────┴────────────────────────────────┴───────────────────────┘
```

---

#### Track A: 30-Day Comprehensive Mastery Roadmap

| Day Range | Core Focus Area | Primary Modules & Activities | Target Milestone |
| :--- | :--- | :--- | :--- |
| **Days 01–03** | Barclays Profile & Quant Pivot | Read `01`, `02`, `03`, `PLACEMENT_FACTS`. Memorize RISES values. Formulate 30-sec and 3-min candidate engineering pivot pitches. | Flawless role awareness and intro pitch. |
| **Days 04–07** | Statistics & Probability Core | Study `11`. Work through Q01–Q30 in `18`. Derive MLE for logistic regression, Binomial tests, and Gumbel EVT math. | 100% on probability and hypothesis tests. |
| **Days 08–11** | Credit Risk Fundamentals & Models | Master `04` and `05`. Derive $EL = PD \times LGD \times EAD$. Understand PIT vs TTC, WoE, IV, and downturn LGD floors. | Solve portfolio loss cases with speed. |
| **Days 12–15** | Model Monitoring Metrics & Math | Deep-dive `06` and `07`. Re-derive ROC-AUC, Gini ($2\times\text{AUC}-1$), KS decile decoupling, and Jeffreys symmetrized PSI. | Calculate KS and PSI by hand without error. |
| **Days 16–18** | Regulatory Capital & Stress Testing | Study `09`. Master Vasicek 1-factor model, 99.9% VaR, $RWA = K \times 12.5 \times EAD$, and CCAR/PRA satellite modeling. | Derive Basel capital requirement formula. |
| **Days 19–21** | IFRS 9 ECL & Staging Waterfall | Master `08`. Work through 3-stage ECL, SICR dual thresholds, discounting via EIR, and multi-scenario probability weighting. | Explain staging cliff-effect and Jensen's inequality. |
| **Days 22–24** | Production Python & SQL Mastery | Execute code in `13`, `14`, and `15`. Build automated monitoring pipeline, vectorized PSI, and SQL 12M outcome windows. | Run bug-free Python monitoring script. |
| **Days 25–26** | Machine Learning & Explainability | Study `12`. Master XGBoost math, second-order Taylor expansion, class imbalance weighting, monotonicity, and TreeSHAP. | Re-derive 3-player Shapley attribution by hand. |
| **Days 27–28** | Practical Projects & Governance | Review `10`, `16`, `17`, and `20`. Understand SR 11-7, PRA SS1/23, PMAs, and portfolio MIS vintage curves. | Defend all 6 practical projects in `20`. |
| **Days 29–30** | Candidate Project Defence & Vivas | Rehearse `19`, `21`, and `22`. Conduct 2 full mock interviews. Audit against 100-point diagnostic scorecard. | Score $\ge 85$ on diagnostic scorecard. |

---

#### Track B: 14-Day Intensive Sprint Roadmap

- **Day 01–02:** Role research, candidate pivot (`01`, `03`, `22`), and core banking parameters ($PD, LGD, EAD$ in `04`).
- **Day 03–04:** Statistical distributions, hypothesis testing, and logistic regression derivations (`11`, Q01–Q30 in `18`).
- **Day 05–06:** Discrimination (Gini, AUC, KS) and Stability (PSI, CSI) mechanics (`06`, `07`).
- **Day 07–08:** Regulatory Capital (Vasicek in `09`) and IFRS 9 ECL Staging (`08`).
- **Day 09–10:** Vectorized Python monitoring script (`13`) and SQL windowing queries (`14`).
- **Day 11–12:** Machine learning in credit risk, monotonicity, and SHAP explainability (`12`).
- **Day 13:** PRA SS1/23 governance, PMAs, and portfolio vintage curves (`10`, `17`, `20`).
- **Day 14:** Full review of 60 technical questions (`19`), RISES behavioral stories (`21`), and final mock interview.

---

#### Track C: 7-Day Emergency Crash Course

- **Day 01:** Memorize candidate pivot scripts (`03`, `22`) and core credit risk concepts ($PD, LGD, EAD$, PIT vs TTC in `04`, `05`).
- **Day 02:** Master Gini ($2\times\text{AUC}-1$), KS decile decoupling, and hand calculation of PSI (`07`).
- **Day 03:** Master Vasicek 99.9% VaR formula (`09`) and IFRS 9 3-stage ECL discounting (`08`).
- **Day 04:** Review vectorized Python monitoring engine (`13`) and SQL 12-month default windowing (`14`).
- **Day 05:** Master TreeSHAP explainability axioms and monotonicity constraints (`12`).
- **Day 06:** Memorize PRA SS1/23 principles, PMA sunset rules (`10`), and review Questions 01–40 in `19`.
- **Day 07:** Rehearse STAR behavioral scenarios with Barclays RISES values (`21`) and review Questions 41–60 in `19`.

---

### 2. The 100-Point Quantitative Readiness Diagnostic Scorecard

Use this auditable self-assessment before entering the Barclays technical interview. Each dimension carries 20 points.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                    Barclays Risk QA 100-Point Diagnostic Scorecard                     │
├──────────────────────────────────────────────────────┬─────────────┬───────────────────┤
│ Evaluation Dimension                                 │ Max Score   │ Self Score (0-20) │
├──────────────────────────────────────────────────────┼─────────────┼───────────────────┤
│ Dimension 1: Mathematical Statistics & Probability   │ 20 Points   │ [   / 20 ]        │
│ Dimension 2: Credit Risk Parameters & Modeling       │ 20 Points   │ [   / 20 ]        │
│ Dimension 3: Model Monitoring & Stability Metrics    │ 20 Points   │ [   / 20 ]        │
│ Dimension 4: Regulatory Capital & Impairment         │ 20 Points   │ [   / 20 ]        │
│ Dimension 5: Programming, Projects & Behavioral DNA  │ 20 Points   │ [   / 20 ]        │
├──────────────────────────────────────────────────────┼─────────────┼───────────────────┤
│ TOTAL READINESS SCORE                                │ 100 Points  │ [   / 100]        │
└──────────────────────────────────────────────────────┴─────────────┴───────────────────┘
```

#### Detailed Scoring Rubric:

##### Dimension 1: Mathematical Statistics & Probability (20 Points)
- [ ] (4 pts) Can derive Maximum Likelihood Estimation (MLE) for logistic regression from scratch.
- [ ] (4 pts) Can calculate mean, variance, and shape parameters for Beta, Binomial, and Poisson distributions.
- [ ] (4 pts) Can execute two-sided Binomial calibration $Z$-tests and interpret $p$-values.
- [ ] (4 pts) Understands weak covariance stationarity, unit roots (ADF test), and cointegration.
- [ ] (4 pts) Can explain extreme value distributions (Gumbel/GEV) and map them to tail loss modeling.

##### Dimension 2: Credit Risk Parameters & Modeling (20 Points)
- [ ] (4 pts) Can define $PD, LGD, EAD$, and differentiate between Expected Loss and Unexpected Loss.
- [ ] (4 pts) Can explain Weight of Evidence (WoE) and Information Value (IV) mathematically.
- [ ] (4 pts) Can articulate the exact difference between Point-in-Time (PIT) and Through-The-Cycle (TTC) PD.
- [ ] (4 pts) Understands Workout LGD discounting via Effective Interest Rate (EIR) vs Market LGD.
- [ ] (4 pts) Knows how Credit Conversion Factors (CCF) are applied to revolving lines.

##### Dimension 3: Model Monitoring & Stability Metrics (20 Points)
- [ ] (4 pts) Can prove that $\text{Gini} = 2 \times \text{AUC} - 1$ and Somers' $D$ rank correlation.
- [ ] (4 pts) Can calculate Kolmogorov-Smirnov (KS) across 10 deciles and state regulatory thresholds.
- [ ] (4 pts) Can derive Population Stability Index (PSI) from symmetrized Kullback-Leibler divergence.
- [ ] (4 pts) Knows exact regulatory traffic-light triggers for PSI ($<0.10, 0.10-0.25, \ge 0.25$).
- [ ] (4 pts) Can explain Characteristic Stability Index (CSI) and Hosmer-Lemeshow calibration caveats.

##### Dimension 4: Regulatory Capital & Impairment (20 Points)
- [ ] (4 pts) Can write and explain every term in the Vasicek Basel IRB capital requirement ($K$) formula.
- [ ] (4 pts) Understands why $RWA = K \times 12.5 \times EAD$ and the Basel 3.1 72.5% output floor.
- [ ] (4 pts) Can explain IFRS 9 3-stage classification, quantitative/qualitative SICR, and 30 DPD backstop.
- [ ] (4 pts) Explains why multi-scenario ECL is required via Jensen's Inequality convexity.
- [ ] (4 pts) Understands PRA SS1/23 principles, Model Tiers, and Post-Model Adjustment (PMA) sunset rules.

##### Dimension 5: Programming, Projects & Behavioral DNA (20 Points)
- [ ] (4 pts) Can write vectorized Python code to compute Gini, KS, and PSI with zero-division safeguards.
- [ ] (4 pts) Can write performant ANSI SQL queries using window functions (`ROWS BETWEEN`, `LAG`, `NTILE`).
- [ ] (4 pts) Understands TreeSHAP explainability axioms and monotonicity constraints in XGBoost.
- [ ] (4 pts) Has memorized and rehearsed the 90-second technical bridge for all 3 candidate projects.
- [ ] (4 pts) Has 10 STAR behavioral stories aligned with Barclays RISES values (especially Stewardship).

---

### 3. Diagnostic Readiness Benchmarking

```
┌─────────────────┬──────────────────┬────────────────────────────────────────────────────────┐
│ Total Score     │ Readiness Tier   │ Candidate Action Plan                                  │
├─────────────────┼──────────────────┼────────────────────────────────────────────────────────┤
│ 90 – 100 Points │ EXCELLENT        │ Placement Ready. Refine executive presence and speed.   │
├─────────────────┼──────────────────┼────────────────────────────────────────────────────────┤
│ 80 – 89 Points  │ COMPETITIVE      │ Strong Contender. Review weak technical sub-topics.    │
├─────────────────┼──────────────────┼────────────────────────────────────────────────────────┤
│ 65 – 79 Points  │ MARGINAL         │ Moderate Risk. Execute Track B sprint immediately.     │
├─────────────────┼──────────────────┼────────────────────────────────────────────────────────┤
│ < 65 Points     │ UNPREPARED       │ High Risk. Triage core modules (04, 07, 08, 09, 22).    │
└─────────────────┴──────────────────┴────────────────────────────────────────────────────────┘
```

---

### 4. Pre-Interview 24-Hour Checklist

#### Morning (T minus 24 hours):
- [ ] Review the **Executive 30-Second Master Pitch** in `22_CANDIDATE_PROJECT_DEFENCE.md`.
- [ ] Re-derive the **Vasicek capital formula ($K$)** and **Gini formula ($2\times\text{AUC}-1$)** on a blank sheet of paper.
- [ ] Review the **PSI formula and traffic lights** ($< 0.10, 0.10-0.25, \ge 0.25$).

#### Afternoon (T minus 12 hours):
- [ ] Review the **Top 20 Technical Traps** in `19_TECHNICAL_INTERVIEW_QUESTION_BANK.md`.
- [ ] Rehearse your **STAR responses for Integrity and Stewardship** in `21_STAKEHOLDER_AND_HR_INTERVIEW.md`.
- [ ] Review the **5 high-caliber questions** to ask the Barclays interview panel.

#### Evening (T minus 4 hours):
- [ ] Verify internet connection, webcam, microphone, and quiet interview space.
- [ ] Prepare clean notepad and pen for live mathematical derivations.
- [ ] Ensure proper professional formal business attire.
- [ ] Discontinue intense technical reading by 9:00 PM to ensure cognitive freshness.

---

*Authoritative cross-reference: Barclays Graduate Recruitment Guidelines; Bank of England PRA SS1/23; IIT Kanpur Placement Office Protocols 2026–27.*

