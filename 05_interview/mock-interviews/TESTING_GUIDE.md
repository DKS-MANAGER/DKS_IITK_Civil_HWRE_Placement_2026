# Master Testing & Assessment Guide

> **Domain:** Complete Placement Examination & Simulation Ladder · **Target:** IIT Kanpur Postgraduate Placements 2026  
> **Testing Architecture:** 8-Level Progressive Evaluation from Granular Diagnostics to Full Live Simulations  
> **Repository Roots:** [`01_common/aptitude/mocks/section-tests/`](../../01_common/aptitude/mocks/section-tests/) · [`01_common/aptitude/mocks/section-tests/section/`](../../01_common/aptitude/mocks/section-tests/section/) · [`01_common/aptitude/mocks/`](../../01_common/aptitude/mocks/) · [`05_interview/mock-interviews/mock-tests/`](../../05_interview/mock-interviews/mock-tests/) · [`05_interview/mock-interviews/READINESS_SCORECARD.md`](../../05_interview/mock-interviews/READINESS_SCORECARD.md)

---

## 1. The 8-Level Placement Assessment Ladder

Placement testing is not a flat list of questions; it is a **multi-tiered cognitive diagnostic system** that builds from isolated formula mastery to high-pressure full interview simulations:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────┐
│                             THE 8-LEVEL PLACEMENT ASSESSMENT LADDER                            │
├───────┬──────────────────────────┬─────────────────────────────┬───────────────────────────────┤
│ Level │ Assessment Tier          │ Scope & Time                │ Primary Target & File Location│
├───────┼──────────────────────────┼─────────────────────────────┼───────────────────────────────┤
│ Level 1: Topic Tests     │ Isolated functional test │ 15 Qs · 20 min          │ Level 1: Diagnostic Baseline   │
│                          │                          │ Cat-8 Cognitive Hierarchy   │ 01_common/aptitude/mocks/section-tests/ (17 tests)    │
├───────┼──────────────────────────┼─────────────────────────────┼───────────────────────────────┤
│ L2    │ Sectional Speed Tests    │ 25–30 Qs · 30–40 min        │ Domain pacing & stamina       │
│       │                          │ Quant, Reasoning, DI, Verbal│ 01_common/aptitude/mocks/section-tests/section/ (5 tests)│
├───────┼──────────────────────────┼─────────────────────────────┼───────────────────────────────┤
│ L3    │ Full Placement Mocks     │ 50 Qs · 60 min              │ General multi-domain OA sim   │
│       │                          │ Baseline to Institutional   │ 01_common/aptitude/mocks/ (M01 to M05)  │
├───────┼──────────────────────────┼─────────────────────────────┼───────────────────────────────┤
│ L4    │ Hard & Expert Mocks      │ 50–60 Qs · 60–75 min        │ High-pressure & extreme cases │
│       │                          │ Day-1 High-Selectivity      │ 01_common/aptitude/mocks/ (H01, E01)    │
├───────┼──────────────────────────┼─────────────────────────────┼───────────────────────────────┤
│ L5    │ Role & Company OAs       │ 30–50 Qs · 45–60 min        │ Recruiter pattern screening   │
│       │                          │ Core Civil, PSUs, Analytics │ 05_interview/mock-interviews/mock-tests/ (25 tests)   │
├───────┼──────────────────────────┼─────────────────────────────┼───────────────────────────────┤
│ L6    │ Technical Interview Bank │ Branching Question Trees    │ Navier-Stokes, OpenFOAM, etc. │
│       │                          │ 5-Level Deep Probes         │ 01_common/interview-fundamentals/technical/     │
├───────┼──────────────────────────┼─────────────────────────────┼───────────────────────────────┤
│ L7    │ Case & Behavioral Sims   │ 30–45 min Dialogues         │ Consulting cases & STAR-L HR  │
│       │                          │ Exhibits & Pushback Trees   │ 05_interview/case-interview/case-interviews/     │
├───────┼──────────────────────────┼─────────────────────────────┼───────────────────────────────┤
│ L8    │ Full Live Simulation     │ 45 min End-to-End Interview │ 100-pt scorecard & PPP defense│
│       │                          │ 3-Layer Interrogation       │ 05_interview/mock-interviews/MOCK_INTERVIEW.md        │
└───────┴──────────────────────────┴─────────────────────────────┴───────────────────────────────┘
```

---

## 2. Directory Breakdown by Assessment Layer

### Level 1: Topic Diagnostic Tests ([`01_common/aptitude/mocks/section-tests/`](../../01_common/aptitude/mocks/section-tests/README.md))
- **Structure:** 14 Standardized Topic Tests (210 questions) covering Number Systems, Percentages, Profit & Loss, SI/CI, Ratios, Averages, Time & Work, Speed-Time-Distance, Permutations & Combinations, Probability, Series, Seating, DI, and Verbal.
- **Pedagogy:** Cat-8 progression from Level 1 Foundation to Level 6 Trap questions with complete distractor post-mortems.
- **Target:** $\ge 12.50 / 15.00\text{ Marks}$ under strict $+1.00 / -0.25$ negative marking.

### Level 2: Sectional Assessment Layer ([`01_common/aptitude/mocks/section-tests/section/`](../../01_common/aptitude/mocks/section-tests/section/README.md))
- **Structure:** 5 Pure-Domain Timed Tests (140 questions):
  - `sectional-quant-01.md` (30 Qs · 40 min: Arithmetic, Algebra, Geometry, Modern Math, Engineering Math)
  - `sectional-reasoning-01.md` (30 Qs · 40 min: Syllogisms, Coded Inequalities, Circular Seating, Verbal Logic)
  - `sectional-di-01.md` (25 Qs · 35 min: 5 independent non-recycled sets: EPC, Dam Hydrograph, SaaS, Ports, Fabs)
  - `sectional-verbal-01.md` (25 Qs · 30 min: Grammar, Cloze, Discourse Logic, Critical Reasoning, CFD Passage)
  - `sectional-civil-core-01.md` (25 Qs · 35 min: Dimensional analysis, Unit conversions, Discharge, Earthwork, Risk)
- **Pedagogy:** Isolates speed bottlenecks and domain-specific time pacing (~70–80 seconds per question).

### Level 3 & Level 4: Full Placement Mock Suite ([`01_common/aptitude/mocks/`](../../01_common/aptitude/mocks/README.md))
- **Inventory:** 7 Standardized Full Placement Mocks (360+ questions):
  - `full-placement-mock-01.md` — Baseline Diagnostic (50 Qs · 60 min)
  - `full-placement-mock-02.md` — Standard Corporate (50 Qs · 60 min)
  - `full-placement-mock-03.md` — Competitive Placement (50 Qs · 60 min)
  - `full-placement-mock-04.md` — IITK High-Bar Flagship (50 Qs · 60 min)
  - `full-placement-mock-05.md` — Expert Mixed Suite (50 Qs · 60 min)
  - `hard-placement-mock-01.md` — High-Pressure Selective (60 Qs · 75 min)
  - `expert-placement-mock-01.md` — Extreme Multi-Caselets (50 Qs · 60 min)
- **Rules:** Interleaved multi-domain format (no in-test difficulty labels), strict negative marking ($-0.25$ / $-0.33$).

### Level 5: Role-Specific Technical OAs ([`05_interview/mock-interviews/mock-tests/`](../../05_interview/mock-interviews/mock-tests/README.md))
- **Inventory:** 25 Role-specific screening tests covering Civil General, Construction Management, Hydrodynamics & CFD, Water Resources & Hydrology, Transportation, Geotechnical, Structural Analysis, Environmental, GIS, and Operations Research.

### Level 6: Technical Interview Question Trees ([`01_common/interview-fundamentals/technical/`](../technical/technical-interview-bank.md))
- **Inventory:** 10 Master Technical Question Trees spanning Navier-Stokes derivation, OpenFOAM PISO/SIMPLE algorithms, $y^+$ wall resolution, ASME GCI grid convergence, Theis groundwater diffusion, and bridge pier scour.
- **Protocol:** Primary Question $\to$ Derivation $\to$ Physical Application $\to$ Assumptions $\to$ Numerical Failure Modes.

### Level 7 & Level 8: Case Simulations & Full Mock Interview
- **Case Interviews:** [`05_interview/case-interview/case-interviews/case-simulation-suite.md`](../../05_interview/case-interview/case-interviews/case-simulation-suite.md) featuring full dialogues, exhibits, MECE issue trees, and interviewer pushback.
- **Full Live Sim:** [`05_interview/mock-interviews/MOCK_INTERVIEW.md`](../../05_interview/mock-interviews/MOCK_INTERVIEW.md) graded on the 100-point performance rubric in [`05_interview/mock-interviews/READINESS_SCORECARD.md`](../../05_interview/mock-interviews/READINESS_SCORECARD.md).

---

## 3. Recommended Testing Workflow: The Retest Loop

```
1. DIAGNOSE: Attempt a Level 1 Topic Test (15 Qs · 20 min)
      ↓
2. ANALYZE: Classify errors into Type C (Concept), A (Algebra/Calculation), T (Time/Pacing), M (Misread)
      ↓
3. REMEDIATE: Drill corresponding chapter in 01_common/aptitude/quantitative/, 01_common/aptitude/data-interpretation/, or 01_common/aptitude/verbal/
      ↓
4. SECTIONAL DRILL: Take a Level 2 Sectional Test (25–30 Qs) under 5-minute time clamp
      ↓
5. ESCALATE: Attempt Level 3/4 Full Placement Mocks under timed exam conditions
      ↓
6. LOG & AUDIT: Record scores in 05_interview/mock-interviews/READINESS_SCORECARD.md
```

---

> **Related Guides:** [ASSESSMENT_ARCHITECTURE.md](ASSESSMENT_ARCHITECTURE.md) · [MASTER_NAVIGATION.md](../../docs/MASTER_NAVIGATION.md) · [PREPARATION_WORKFLOW.md](../../docs/PREPARATION_WORKFLOW.md)

