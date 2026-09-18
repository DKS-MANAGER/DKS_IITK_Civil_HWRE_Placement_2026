# Selection Stage Map & Recruiter Process Blueprint

> **The institutional selection progression for campus recruitment.**
> Maps the standard recruitment funnel from initial resume shortlisting to final panel rounds.
> All factual statements carry authoritative provenance tags: `[VERIFIED]`, `[SOURCE-DERIVED]`, `[INFERRED]`, `[PREPARATION HEURISTIC]`, or `[SELF-REPORTED]`.

---

## 1. Universal Selection Funnel

```
STAGE 1: RESUME & ELIGIBILITY SCREENING  (SPO Portal CGPA & Branch criteria)
                   ↓
STAGE 2: SPEED APTITUDE & OA SCREENING   (60-min timed OA: Quant, DI, Logic, Verbal)
                   ↓
STAGE 3: CORE TECHNICAL / CODING TEST   (Domain MCQs, GATE-level checks, or SQL/DSA)
                   ↓
STAGE 4: TECHNICAL ORAL INTERVIEW       (M.Tech thesis defense & branching theory trees)
                   ↓
STAGE 5: CASE INTERVIEW / GROUP TASK     (Consulting cases, guesstimates, EPC site dilemmas)
                   ↓
STAGE 6: HR & BEHAVIORAL PROBES          (STAR stories, culture fit, relocation, compensation)
```

---

## 2. Detailed Stage Breakdown

### Stage 1: Application & Eligibility Screening

- **Focus:** Minimum CGPA cutoff (typically $\ge 6.5$ or $\ge 7.0$ for Day 1 firms `[VERIFIED]`), zero active backlogs, M.Tech specialization eligibility.
- **Evidentiary Standard:** `[SOURCE-DERIVED]` from IITK SPO recruiter job notification forms (JNF).
- **Preparation Anchor:** [`PLACEMENT_CHECKLIST.md`](PLACEMENT_CHECKLIST.md) · [`RESUME/RESUME_AUDIT.md`](RESUME/RESUME_AUDIT.md).

---

### Stage 2: Aptitude & Online Assessment (OA)

- **Focus:** High-speed quantitative calculation, multi-table data interpretation, logical reasoning, and reading comprehension under negative marking ($+1 / -0.25$).
- **Benchmarking `[PREPARATION HEURISTIC]`:** Target composite score $\ge 75\%$ with median time per question $\le 75\text{ s}$.
- **Preparation Ladder:**
  - Granular topic diagnostic tests: [`aptitude/tests/`](../aptitude/tests/)
  - Timed sectional drills (30–40 min): [`aptitude/tests/section/`](../aptitude/tests/section/)
  - Full campus OA simulations: [`aptitude/mocks/`](../aptitude/mocks/)
  - Testing guide & pacing rules: [`../docs/ASSESSMENT_ARCHITECTURE.md`](../docs/ASSESSMENT_ARCHITECTURE.md)

---

### Stage 3: Domain Technical Screening

- **Focus:** Core civil and computational MCQs (Open channel flow, fluid mechanics, soil mechanics, structural analysis, concrete/steel design, or SQL/Python queries).
- **Format:** 25–40 MCQs in 30–45 minutes, administered immediately following the general aptitude section.
- **Preparation Anchor:**
  - Civil core aptitude test: [`aptitude/tests/section/sectional-civil-core-01.md`](../aptitude/tests/section/sectional-civil-core-01.md)
  - Role-specific mock tests (25 tests): [`mock-tests/`](mock-tests/)
  - Formula review: [`../core/gate/formulas/gate-civil-formulas.md`](../core/gate/formulas/gate-civil-formulas.md)

---

### Stage 4: Technical Oral Interview & Thesis Defense

- **Focus:** Rigorous oral inquiry into fundamental engineering physics, mathematical derivations, boundary conditions, software settings, and M.Tech thesis research.
- **Methodology:** Branching oral inquiry trees testing Level 1 recall up to Level 5 edge-case judgment.
- **Preparation Anchor:**
  - Branching technical question trees: [`interview/technical/technical-interview-bank.md`](interview/technical/technical-interview-bank.md)
  - 3-Minute thesis pitch (P-A-R-I-C) & project defense: [`interview/technical/project-defense-guide.md`](interview/technical/project-defense-guide.md)
  - Software theory linkage: [`../software-and-tech/SOFTWARE_THEORY_LINKAGE.md`](../software-and-tech/SOFTWARE_THEORY_LINKAGE.md)

---

### Stage 5: Case Interview & Group Interaction (Where Applicable)

- **Focus:**
  - *Consulting / Analytics:* Structured problem decomposition (MECE issue trees, market sizing, profit diagnostics, cost reduction).
  - *Construction & EPC Giants (L&T, Godrej):* Group task on project resource constraints, safety vs deadline dilemmas, material substitution.
- **Preparation Anchor:**
  - Management consulting case simulations: [`../non-core/01_roles/consulting/case-bank.md`](../non-core/01_roles/consulting/case-bank.md)
  - Group task & GD frameworks: [`CASE_GD.md`](CASE_GD.md) · [`behavioral/group-discussion-mastery.md`](behavioral/group-discussion-mastery.md)

---

### Stage 6: HR, Behavioral & Cultural Alignment

- **Focus:** Leadership under pressure, handling peer conflict, explaining weaknesses, career longevity, relocation flexibility.
- **Methodology:** Structured behavioral STAR-L format (Situation, Task, Action, Result, Learning) with aggressive pushback probes.
- **Preparation Anchor:**
  - HR interview master database: [`behavioral/question-master-database.md`](behavioral/question-master-database.md)
  - Behavioral guide: [`../docs/BEHAVIOURAL_HR_GUIDE.md`](../docs/BEHAVIOURAL_HR_GUIDE.md)

---

## 3. Verified Company Selection Workflows

The following recruitment workflows are confirmed from verified campus candidate interview experiences (`[VERIFIED]` / `[SELF-REPORTED]`):

| Company | Sector | Verified Selection Stages | Primary Profile Dossier |
|:---|:---|:---|:---|
| **Larsen & Toubro (L&T)** | EPC / Construction | Online OA (Aptitude + Technical) $\to$ Group Task $\to$ Tech/HR Panel | [`company-profiles/civil-lt.md`](company-profiles/civil-lt.md) |
| **Godrej Properties** | Real Estate EPC | Aptitude Screening $\to$ Technical Evaluation $\to$ Case Presentation $\to$ Final HR | [`company-profiles/civil-godrej-properties.md`](company-profiles/civil-godrej-properties.md) |
| **Vassar Labs** | HWRE / Infratech | Technical OA (Water/GIS) $\to$ Technical Round 1 $\to$ Project Defense $\to$ Leadership | [`company-profiles/civil-vassarlabs.md`](company-profiles/civil-vassarlabs.md) |
| **Thornton Tomasetti** | Structural R&D | Structural Technical Screening $\to$ ETABS/SAP2000 Modeling Test $\to$ Director Interview | [`company-profiles/civil-thornton-tomasetti.md`](company-profiles/civil-thornton-tomasetti.md) |
| **BPCL / HPCL** | Energy PSU | CBT Technical OA (100 Qs) $\to$ Group Discussion $\to$ Senior Chief Engineer Panel | [`company-profiles/civil-bpcl.md`](company-profiles/civil-bpcl.md) · [`civil-hpcl.md`](company-profiles/civil-hpcl.md) |
| **Rodic Consultants** | Infrastructure PM | Screening Test $\to$ Water Network Technical Interview $\to$ HR Round | [`company-profiles/civil-rodic.md`](company-profiles/civil-rodic.md) |
| **TuTr Hyperloop** | Aerospace / R&D | Aerodynamics / CFD Screening $\to$ OpenFOAM/ANSYS Technical Interview $\to$ Founder Round | [`company-profiles/civil-tutr-hyperloop.md`](company-profiles/civil-tutr-hyperloop.md) |
| **Schneider Electric** | Energy Automation | Online Aptitude Test $\to$ Group Discussion $\to$ Technical Panel Interview | [`company-profiles/schneider-electric.md`](company-profiles/schneider-electric.md) |
| **Mu Sigma** | Decision Sciences | Mu Sigma Aptitude Test $\to$ Video Synthesis / Case Round $\to$ Personal Interview | [`company-profiles/mu-sigma.md`](company-profiles/mu-sigma.md) |
| **Tech Mahindra** | Tech Consulting | 5-Round Funnel: General Aptitude $\to$ Essay $\to$ Technical $\to$ Management $\to$ HR | [`company-profiles/tech-mahindra.md`](company-profiles/tech-mahindra.md) |

---

## 4. Tactical Execution Protocol

1. **Target Identification**: Check specific company profiles in [`company-profiles/`](company-profiles/) to see exact past stage structures.
2. **Eliminate Non-Tested Preparation**: If a company does not hold a group task or coding round, skip that module and concentrate 100% on their primary filter.
3. **Log Progress**: Track performance and calibration status in [`READINESS_SCORECARD.md`](READINESS_SCORECARD.md).

---

> **Related Navigation:**
> [MASTER_PREP_PLAN.md](MASTER_PREP_PLAN.md) · [READINESS_SCORECARD.md](READINESS_SCORECARD.md) · [../docs/IITK_PLACEMENT_MAP.md](../docs/IITK_PLACEMENT_MAP.md) · [README.md](README.md)

