# Master Sectional Assessment Suite & Speed Pacing Layer

> **Domain:** Timed Sectional Examination & Domain-Specific Speed Calibration · **Target:** IIT Kanpur Postgraduate Placements 2026  
> **Testing Level:** Layer 2 of the Three-Tier Placement Assessment System  
> **Sectional Battery:** 5 Standardized Tests across Quant, Reasoning, DI, Verbal, and Core Civil Screening (140 High-Yield Placement Questions)  
> **Scoring Discipline:** $+1.00$ Mark for Correct, $-0.25$ Mark for Incorrect, $0.00$ for Unattempted · Strict Negative Marking Applied

---

## 1. Pedagogical Architecture & Functional Purpose

While **Layer 1 Topic Tests** (`aptitude/tests/`) diagnose granular formula mastery in isolated chapters and **Layer 3 Full Mocks** (`aptitude/mocks/`) simulate 60-to-75-minute multi-domain cognitive endurance, **Layer 2 Sectional Tests** fulfill a critical diagnostic function:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────┐
│                           THE THREE-TIER PLACEMENT TESTING ENGINE                              │
├──────────────────────────┬──────────────────────────────────────┬──────────────────────────────┤
│ Assessment Layer         │ Structure & Timing                   │ Primary Pedagogical Function │
├──────────────────────────┼──────────────────────────────────────┼──────────────────────────────┤
│ Layer 1: Topic Tests     │ 15 Questions · 20 Minutes            │ Micro-diagnosis of formulaic │
│ (aptitude/tests/)        │ Cat-8 Cognitive Hierarchy            │ gaps & concept blindness.    │
├──────────────────────────┼──────────────────────────────────────┼──────────────────────────────┤
│ Layer 2: Sectional Tests │ 25–30 Questions · 30–40 Minutes      │ High-speed pacing, domain    │
│ (aptitude/tests/section/)│ Pure Domain Screening                │ stamina, constraint triage.  │
├──────────────────────────┼──────────────────────────────────────┼──────────────────────────────┤
│ Layer 3: Full Mocks      │ 50–60 Questions · 60–75 Minutes      │ Complete corporate recruitment│
│ (aptitude/mocks/)        │ Interleaved Multi-Domain Suites      │ OA simulation under pressure.│
└──────────────────────────┴──────────────────────────────────────┴──────────────────────────────┘
```

Sectional tests isolate speed bottlenecks. A candidate scoring $80\%$ overall on full mocks might conceal a severe speed deficit in Data Interpretation or Verbal inference that triggers sectional cutoff disqualification by top-tier recruiters.

---

## 2. Master Sectional Tests Directory

| Sectional Assessment File | Target Screening Domain | Total Questions & Time | Core Covered Competencies | Target Benchmark `[PREPARATION HEURISTIC]` |
|:---|:---|:---:|:---|:---:|
| [**Quantitative Sectional 01**](sectional-quant-01.md) | Quantitative Aptitude | 30 Qs · 40 min | Arithmetic, Algebra, Geometry, Modern Math, Engineering Screening | $\ge 22.50 / 30.00$ |
| [**Reasoning Sectional 01**](sectional-reasoning-01.md) | Logical & Analytical Reasoning | 30 Qs · 40 min | Syllogisms, Coded Inequalities, Circular Arrangement, Verbal Logic | $\ge 22.50 / 30.00$ |
| [**Data Interpretation Sectional 01**](sectional-di-01.md) | Data Interpretation & Analytics | 25 Qs · 35 min | 5 Independent Sets: EPC Overruns, Reservoir Hydrographs, SaaS, Logistics, Fabs | $\ge 18.75 / 25.00$ |
| [**Verbal Ability Sectional 01**](sectional-verbal-01.md) | Verbal & Reading Comprehension | 25 Qs · 30 min | Error Spotting, Cloze, Discourse Logic, Critical Reasoning, CFD Passage | $\ge 18.75 / 25.00$ |
| [**Civil Core Aptitude 01**](sectional-civil-core-01.md) | Civil Engineering Core Aptitude | 25 Qs · 35 min | Dimensional Analysis, Unit Conversions, Discharge, Earthwork, Risk, Economics | $\ge 18.75 / 25.00$ |

---

## 3. Standardized Sectional Timing & Scoring Rubric

All tests in this suite enforce standardized negative marking:
- **Correct Answer:** $+1.00$ Mark
- **Incorrect Answer:** $-0.25$ Mark
- **Unattempted Question:** $0.00$ Marks

### Sectional Target Score Translation Matrix `[PREPARATION HEURISTIC]`

> [!NOTE]
> **Methodological Note:** Score bands represent internal aspirational targets calibrated to past corporate shortlisting cutoffs, not empirical population percentiles.

```
+------------------------------------------------------------------------------------+
| SCALED SCORE (%)   | PERFORMANCE TIER       | RECOMMENDED ACTION PROTOCOL          |
+--------------------+------------------------+--------------------------------------+
| ≥ 80.0%            | 🟢 Tier 1 Target Met   | Proceed to Layer 3 Full Mocks        |
|                    | (Top Selectivity)      | (High-Speed Pacing Confirmed)        |
+--------------------+------------------------+--------------------------------------+
| 70.0% – 79.9%      | 🟡 Tier 2 Proficient   | Review unattempted & incorrect traps |
|                    | (Solid Shortlist)      | Re-attempt under 5-minute time clamp |
+--------------------+------------------------+--------------------------------------+
| 55.0% – 69.9%      | 🟠 Tier 3 Vulnerable   | Isolate question archetypes > 90s    |
|                    | (Baseline Pass)        | Drill Cat-8 Level 4–6 Topic Modules  |
+--------------------+------------------------+--------------------------------------+
| < 55.0%            | 🔴 Sectional Risk      | Immediate 48-Hour Remedial Protocol: |
|                    | (Cutoff Failure Risk)  | Retake Layer 1 Topic Diagnostic Test |
+--------------------+------------------------+--------------------------------------+
```

---

## 4. Post-Test Error Triage & Scorecard Integration

After completing any sectional assessment:
1. Count your raw score: $\text{Raw Score} = \text{Correct} - (0.25 \times \text{Incorrect})$.
2. Log your performance in [READINESS_SCORECARD.md](../../../prep/READINESS_SCORECARD.md).
3. Classify every lost mark into one of the four cognitive error buckets:
   - **Type C (Conceptual Gap):** Theoretical theorem, formula, or grammar rule forgotten.
   - **Type A (Calculation Slip):** Correct algebraic formulation, but arithmetic or sign mistake.
   - **Type T (Pacing Bottleneck):** Spent $> 90\text{ seconds}$ on a single problem, starving subsequent high-probability questions.
   - **Type M (Misread Trap):** Overlooked a critical boundary constraint or negative polarity word (*except, neither, never*).
4. Do not re-attempt the exact same test within 48 hours; instead, drill the underlying topic modules in `aptitude/quant/`, `aptitude/di/`, `aptitude/verbal/`, or `core/hwre/`.
