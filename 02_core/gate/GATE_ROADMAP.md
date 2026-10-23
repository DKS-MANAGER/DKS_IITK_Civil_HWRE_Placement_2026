# GATE Civil — Study Roadmap

> Complete preparation path: Syllabus → Learn → Practice → PYQ → Test → Revise.

## 1. Exam Structure & Official Mark Distribution (GATE Civil — 100 Marks Total)

Official GATE CE paper format (65 questions, 180 minutes, virtual calculator):
- **General Aptitude (GA):** Exactly **15 Marks** (10 questions: 5 of 1-mark, 5 of 2-mark)
- **Engineering Mathematics:** Exactly **13 Marks** (Section 1 of CE syllabus)
- **Core Civil Engineering:** Exactly **72 Marks** (Sections 2 through 7)
- **Total:** Exactly **100 Marks** (30 of 1-mark, 35 of 2-mark; MCQs, MSQs, NATs)

| Section / Core Subject | Official GATE Mark Allocation | Typical Range (Historical CE Papers) | Priority | Prerequisite |
| :--- | :---: | :---: | :---: | :--- |
| **General Aptitude (GA)** | **15 Marks** (Fixed) | **15%** | P0 | Verbal & Quantitative basics |
| **Engineering Mathematics** | **13 Marks** (Fixed) | **13%** | P0 | Calculus, Linear Algebra |
| **Geotechnical Engineering** (Soil Mech + Foundation) | Part of Core 72M | **13 – 15 Marks** | P0 | SOM, Fluid mechanics |
| **Environmental Engineering** (Water, WW, Air, MSW) | Part of Core 72M | **10 – 12 Marks** | P0 | Chemistry, fluid flow |
| **Water Resources & Hydraulics** (Fluids, OCF, Hydro, Irrig) | Part of Core 72M | **9 – 11 Marks** | P0 | Engineering Math, Fluids |
| **Structural Engineering** (Analysis, RCC, Steel) | Part of Core 72M | **11 – 13 Marks** | P0 | SOM, Matrix analysis |
| **Mechanics & Strength of Materials (SOM)** | Part of Core 72M | **7 – 9 Marks** | P0 | Statics, Math |
| **Transportation Engineering** (Highway, Traffic, Pavement) | Part of Core 72M | **8 – 10 Marks** | P1 | Geotechnical basics |
| **Geomatics Engineering (Surveying)** | Part of Core 72M | **4 – 6 Marks** | P1 | Basic trigonometry |
| **Construction Materials & Management** | Part of Core 72M | **3 – 5 Marks** | P1 | Concrete technology |
| **Total** | **100 Marks** | **100% (Sum of parts = 100M)** | — | — |

> *Source: Official GATE Information Brochure (IITs/IISc) and analysis of recent CE question papers.* Core subject marks fluctuate slightly from session to session, but GA (15M) and Engineering Mathematics (13M) are strictly standardized.

## 2. Six-Stage Progression

### Stage 1 — Foundation (Concepts)
- Read the subject notes: [`civil/gate-civil-notes.md`](civil/gate-civil-notes.md)
- For depth, use the linked `02_core/<subject>/` files.
- Goal: understand every concept, condition, and assumption.

### Stage 2 — Building (Formulas + Examples)
- Memorize the formula sheet: [`formulas/gate-civil-formulas.md`](formulas/gate-civil-formulas.md)
- Start with `[P0]` formulas, then `[P1]`.
- Solve the verified examples: [`practice/gate-civil-practice.md`](practice/gate-civil-practice.md)

### Stage 3 — Practice (Topic-wise)
- Solve topic-wise questions, Basic → GATE-level → Hard.
- Maintain the error log: [`ERROR_ANALYSIS.md`](ERROR_ANALYSIS.md)

### Stage 4 — PYQs
- Work through the topic-wise PYQ system: [`pyq/gate-civil-pyq.md`](pyq/gate-civil-pyq.md)
- Target: last 10–15 years, topic-wise.

### Stage 5 — Test (Timed)
- Take the full mock: [`mocks/gate-civil-mock-1.md`](mocks/gate-civil-mock-1.md)
- Simulate exam conditions: 3 hours, no calculator except GATE virtual calculator.

### Stage 6 — Revision
- Use [`RAPID_REVISION.md`](RAPID_REVISION.md) (30-min / 2-hr / 1-day).
- Use [`revision_notes/gate-civil-revision.md`](revision_notes/gate-civil-revision.md) for flashcards.
- Re-solve errors from [`ERROR_ANALYSIS.md`](ERROR_ANALYSIS.md).

## 3. Inter-Subject Dependency Map

```
Engineering Mathematics
   → Engineering Mechanics
      → Strength of Materials
         → Structural Analysis
            → RCC / Steel

Fluid Mechanics
   → Hydraulics (Open Channel)
      → Hydrology

Geotechnical (Soil Mechanics)
   → Foundation Engineering
```

Study in dependency order — never study RCC before SOM, or Hydrology before Fluid Mechanics.

## 4. Weekly Rhythm (During Full Preparation)

| Day | Focus |
| --- | ----- |
| Mon–Wed | Learn 1 subject + formulas + 10–15 practice questions |
| Thu | PYQs for that subject |
| Fri | Error analysis + reattempt |
| Sat | Timed topic test |
| Sun | Full mock (once per 2 weeks) + review |

## 5. GATE + Placement Connection

| GATE Subject | GATE Role | Placement Interview Role |
| ------------ | --------- | ------------------------ |
| Strength of Materials | Structural questions | Structural/Core interview |
| Fluid Mechanics | Hydraulics questions | HWRE/Hydraulics interview |
| Construction Management | CPM/PERT questions | Project Engineer interview |
| Geotechnical | Foundation questions | Geotech/Core interview |
| Environmental | Treatment questions | Environmental interview |

GATE preparation directly feeds core-company technical interviews. Do not mix unrelated placement content into GATE study.