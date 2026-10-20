# ExxonMobil Engineer Recruitment: Master Roadmap & Curriculum Matrix

> **Company:** ExxonMobil Services & Technology Private Limited (EMSTPL), Bengaluru  
> **Profile:** Engineer (Campus Recruitment Drive, IIT Kanpur)  
> **Audience:** Civil Engineering (B.Tech / M.Tech / Dual Degree) with Hydraulics & Water Resources Engineering (HWRE) Specialization  
> **Document Role:** Primary landing page, curriculum matrix, topic dependency mapping, timed revision pathways, and mistake tracking framework.

---

## 1. Curriculum Architecture & Time Allocations

This curriculum is structured around the student's primary academic strength—**Civil Engineering & HWRE**—while bridging the technical competencies required for energy-sector industrial operations, general placement assessments, and company culture interviews.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        CURRICULUM TIME ALLOCATION (100% TOTAL)                         │
├──────────────────────────┬──────────────────────────┬──────────────────────────────────┤
│ Track                    │ Provisional Allocation   │ Core Learning Objective          │
├──────────────────────────┼──────────────────────────┼──────────────────────────────────┤
│ Track A: Civil & HWRE    │ 50% Time Budget          │ First-principles mastery, fluid  │
│                          │                          │ transport, open channel, CFD     │
│ Track B: Common Engg     │ 25% Time Budget          │ Thermodynamics, heat transfer,   │
│ & Aptitude               │                          │ materials, speed aptitude drills │
│ Track C: Oil/Gas, Safety │ 15% Time Budget          │ Upstream/downstream systems,     │
│ & Energy Operations      │                          │ flow assurance, OIMS, HAZOP/PSM  │
│ Track D: Interview Prep  │ 10% Time Budget          │ Thesis/project defense, STAR     │
│ & Behavioral             │                          │ safety stories, oral numericals  │
└──────────────────────────┴──────────────────────────┴──────────────────────────────────┘
```

---

## 2. Directory Structure & File Map

All resources are self-contained within this dedicated directory:

```
04_company-prep/company-specific-prep/exxonmobil-engineer/
├── README.md                          ◄── THIS MASTER ROADMAP
├── AUDIT_AND_RESEARCH_REPORT.md       ◄── Fact verification, recruitment proforma analysis, standards
├── STUDY_GUIDE.md                     ◄── Complete conceptual textbook (First principles to advanced)
├── TECHNICAL_WORKBOOK_CIVIL_HWRE.md   ◄── Graded multi-step numerical problems with full derivations
├── COMMON_ENGINEERING_AND_APTITUDE.md ◄── Thermo, Heat Transfer, Materials & Quantitative Aptitude drills
├── OIL_GAS_SAFETY_OPERATIONS.md       ◄── Industrial facilities, flow assurance, OIMS & process safety
├── QUESTION_BANK.md                   ◄── Graded question sets (Levels 1-3) with separated answer keys
├── MOCK_ASSESSMENTS.md                ◄── 4 Full-length timed mock tests with benchmark cutoffs
├── FORMULA_AND_RAPID_REVISION.md      ◄── High-density cheat sheets, unit trap checks, 5-min prep
└── INTERVIEW_AND_BEHAVIORAL.md        ◄── Project defense (CFD/OpenFOAM), STAR safety stories, HR
```

---

## 3. Pedagogical Three-Tier Progression

Every technical module in this course adheres strictly to a three-tier learning progression:

```
   Level 1: Foundation
   ┌───────────────────────────────────────────────────────────────────────┐
   │ Physical intuition, formal definitions, governing laws, dimensional    │
   │ homogeneity, and elementary single-concept worked examples.          │
   └───────────────────────────────────┬───────────────────────────────────┘
                                       │
                                       ▼
   Level 2: Application
   ┌───────────────────────────────────────────────────────────────────────┐
   │ Numerical problem solving, multi-equation coupling, non-ideal effects,│
   │ system curves, Moody charts, and engineering balance checks.          │
   └───────────────────────────────────┬───────────────────────────────────┘
                                       │
                                       ▼
   Level 3: Assessment & Interview Readiness
   ┌───────────────────────────────────────────────────────────────────────┐
   │ Troubleshooting non-convergent systems, transient surge, scour risk,  │
   │ identifying invalid physical assumptions, and defending CFD models.   │
   └───────────────────────────────────────────────────────────────────────┘
```

---

## 4. Module Matrix & Cross-Track Mapping

| Module ID | Module Title | Track | Depth Tier | Primary File Reference |
| :--- | :--- | :--- | :--- | :--- |
| **A1** | Engineering Mathematics & Numerical Foundations | Track A | Level 1 - 2 | [STUDY_GUIDE.md](STUDY_GUIDE.md#module-a1) |
| **A2** | Engineering Mechanics & Strength of Materials | Track A | Level 1 - 2 | [STUDY_GUIDE.md](STUDY_GUIDE.md#module-a2) |
| **A3** | Fluid Mechanics & Pipeline Transport | Track A | Level 1 - 3 | [STUDY_GUIDE.md](STUDY_GUIDE.md#module-a3) |
| **A4** | Open-Channel Flow & Hydraulic Structures | Track A | Level 1 - 3 | [STUDY_GUIDE.md](STUDY_GUIDE.md#module-a4) |
| **A5** | Hydrology & Water Resources Engineering | Track A | Level 1 - 2 | [STUDY_GUIDE.md](STUDY_GUIDE.md#module-a5) |
| **A6** | Sediment Transport, River Mechanics & Scour | Track A | Level 1 - 3 | [STUDY_GUIDE.md](STUDY_GUIDE.md#module-a6) |
| **A7** | Environmental Engineering & Water Quality | Track A | Level 1 - 2 | [STUDY_GUIDE.md](STUDY_GUIDE.md#module-a7) |
| **A8** | Numerical Methods, FVM & Computational Fluid Dynamics | Track A | Level 2 - 3 | [STUDY_GUIDE.md](STUDY_GUIDE.md#module-a8) |
| **B1** | Thermodynamics & Energy Systems | Track B | Level 1 - 2 | [COMMON_ENGINEERING_AND_APTITUDE.md](COMMON_ENGINEERING_AND_APTITUDE.md#module-b1) |
| **B2** | Heat Transfer & Heat Exchanger Design | Track B | Level 1 - 2 | [COMMON_ENGINEERING_AND_APTITUDE.md](COMMON_ENGINEERING_AND_APTITUDE.md#module-b2) |
| **B3** | Materials, Corrosion & Failure Mechanics | Track B | Level 1 - 2 | [COMMON_ENGINEERING_AND_APTITUDE.md](COMMON_ENGINEERING_AND_APTITUDE.md#module-b3) |
| **B4** | Instrumentation, Process Controls & Maintenance | Track B | Level 1 - 2 | [COMMON_ENGINEERING_AND_APTITUDE.md](COMMON_ENGINEERING_AND_APTITUDE.md#module-b4) |
| **B5** | Quantitative Aptitude, Logic & Data Interpretation | Track B | Level 1 - 3 | [COMMON_ENGINEERING_AND_APTITUDE.md](COMMON_ENGINEERING_AND_APTITUDE.md#quantitative-aptitude) |
| **C1** | Energy Operations, Upstream/Downstream & Flow Assurance | Track C | Level 1 - 2 | [OIL_GAS_SAFETY_OPERATIONS.md](OIL_GAS_SAFETY_OPERATIONS.md#section-1) |
| **C2** | Process Safety Management, OIMS, HAZOP & Controls | Track C | Level 1 - 3 | [OIL_GAS_SAFETY_OPERATIONS.md](OIL_GAS_SAFETY_OPERATIONS.md#section-2) |
| **D1** | Project & Thesis Defense (OpenFOAM / Hydrodynamics) | Track D | Level 3 | [INTERVIEW_AND_BEHAVIORAL.md](INTERVIEW_AND_BEHAVIORAL.md#project-defense) |
| **D2** | Behavioral Competencies, OIMS & STAR Methodology | Track D | Level 3 | [INTERVIEW_AND_BEHAVIORAL.md](INTERVIEW_AND_BEHAVIORAL.md#behavioral-star) |

---

## 5. Suggested Timed Study Pathways

Depending on your preparation timeline before the ExxonMobil campus selection drive, execute one of the following structured routes:

### Route 1: 30-Minute Emergency Pre-Test Refresher
* **Target:** Rapid mental priming directly before logging into the Online Assessment.
* **00:00 - 10:00:** Review [FORMULA_AND_RAPID_REVISION.md](FORMULA_AND_RAPID_REVISION.md) (Darcy vs Fanning friction factors, Reynolds number, Bernoulli head equations, speed of sound in pipe elasticity).
* **10:00 - 20:00:** Review Common Traps section in [FORMULA_AND_RAPID_REVISION.md](FORMULA_AND_RAPID_REVISION.md) (gauge vs absolute pressure, pump NPSH available vs required, Manning's roughness unit dependencies).
* **20:00 - 30:00:** Speed review of aptitude quick-conversion mental shortcuts in [COMMON_ENGINEERING_AND_APTITUDE.md](COMMON_ENGINEERING_AND_APTITUDE.md).

### Route 2: 60-Minute High-Priority Technical Refresher
* **Target:** Pre-interview technical alignment.
* **00:00 - 25:00:** Fluid Mechanics & Pipeline Hydraulics ([STUDY_GUIDE.md Module A3](STUDY_GUIDE.md#module-a3)): Navier-Stokes assumptions, boundary layer separation, Darcy-Weisbach head loss, cavitation mechanics.
* **25:00 - 45:00:** Open-Channel Flow & Scour ([STUDY_GUIDE.md Modules A4 & A6](STUDY_GUIDE.md#module-a4)): Specific energy curve, critical depth, hydraulic jump conjugate depths, Shields diagram for sediment incipient motion.
* **45:00 - 60:00:** Process Safety & OIMS core principles in [OIL_GAS_SAFETY_OPERATIONS.md](OIL_GAS_SAFETY_OPERATIONS.md).

### Route 3: 90-Minute Core & Problem-Solving Sprint
* **Target:** Focused numerical readiness before the written/technical screening exam.
* **00:00 - 45:00:** Work through 4 core problems in [TECHNICAL_WORKBOOK_CIVIL_HWRE.md](TECHNICAL_WORKBOOK_CIVIL_HWRE.md): Pipe network head loss, Joukowsky water hammer pressure, hydraulic jump energy dissipation, and HEC-18 pier scour.
* **45:00 - 70:00:** Solve 15 speed aptitude problems in [COMMON_ENGINEERING_AND_APTITUDE.md](COMMON_ENGINEERING_AND_APTITUDE.md) (work-rate, mixture alligation, data interpretation).
* **70:00 - 90:00:** Complete Mock Test 1 (Civil/HWRE Technical Core) in [MOCK_ASSESSMENTS.md](MOCK_ASSESSMENTS.md).

### Route 4: 1-Day Intensive Preparation Camp
* **Morning (08:30 - 12:30):** Full read of [STUDY_GUIDE.md](STUDY_GUIDE.md) Modules A1 through A8; solve Level 1 & Level 2 practice questions.
* **Afternoon (13:30 - 16:30):** Solve all 12 problems in [TECHNICAL_WORKBOOK_CIVIL_HWRE.md](TECHNICAL_WORKBOOK_CIVIL_HWRE.md); review Thermodynamics & Heat Transfer in [COMMON_ENGINEERING_AND_APTITUDE.md](COMMON_ENGINEERING_AND_APTITUDE.md).
* **Evening (17:30 - 20:00):** Study [OIL_GAS_SAFETY_OPERATIONS.md](OIL_GAS_SAFETY_OPERATIONS.md) and prepare STAR behavioral stories in [INTERVIEW_AND_BEHAVIORAL.md](INTERVIEW_AND_BEHAVIORAL.md).
* **Night (20:30 - 22:30):** Attempt Mock Tests 1 & 4 in [MOCK_ASSESSMENTS.md](MOCK_ASSESSMENTS.md); log errors in the Mistake Log.

---

## 6. Personal Mistake Log Framework

To achieve active retention and eliminate recurring errors, use this standardized template to document every mistake made during practice sessions:

```markdown
### Mistake Entry Template

| Field | Description / Value |
| :--- | :--- |
| **Date & Time** | `YYYY-MM-DD HH:MM` |
| **Source File & Question ID**| e.g., `TECHNICAL_WORKBOOK_CIVIL_HWRE.md` / `Problem 04` |
| **Topic & Module** | e.g., Hydraulic Jump / Module A4 |
| **Error Classification** | `[Formula Selection]` / `[Unit Conversion]` / `[Algebraic]` / `[Physical Assumption]` |
| **What I Did (Incorrect)** | Used $y_2/y_1 = \frac{1}{2}(\sqrt{1+8Fr_1^2}-1)$ for a trapezoidal channel instead of rectangular. |
| **Correct Underlying Concept**| The Belanger equation strictly applies to horizontal rectangular channels. For non-rectangular cross-sections, the general momentum conservation equation $M_1 = M_2$ with hydrostatic force $F_p = \rho g \bar{y} A$ must be solved numerically. |
| **Corrective Action** | Re-derive Belanger equation from momentum balance; record channel geometry check in pre-solution steps. |
| **Scheduled Revision Date**| `+2 days from error` |
```

---

## 7. Quality Assurance Checklist

Every document in this preparation suite has undergone the following validation checks:
- [x] Governing equations verified against authoritative textbooks (Fox & McDonald, Chow, White, API standards).
- [x] Friction factor conventions explicitly distinguished ($f_{Darcy} = 4 \times f_{Fanning}$).
- [x] Dimension and unit homogeneity verified across all worked numerical calculations.
- [x] Answer keys physically separated from problem statements to enforce active recall.
- [x] Clear demarcation between verified recruitment facts `[JD VERIFIED]`, candidate reports `[CANDIDATE-REPORTED]`, and educational recommendations `[REPRESENTATIVE]`.
