# Placement Assessment Architecture

> **The Authoritative 8-Level Testing, Evaluation, and Diagnostic Engine.**
> Governs all testing layers across Quantitative Aptitude, Logical Reasoning, Data Interpretation, Verbal Ability, Core Civil/HWRE Engineering, and Interview Simulations.

---

## 1. The 8-Level Assessment Ladder

The repository structures assessment as an integrated progressive ladder. Rather than treating mock tests as isolated question sets, each level isolates a distinct dimension of candidate performance:

```
                                  ┌─────────────────────────────────┐
                                  │ LEVEL 8: Full Live Simulation   │ (45m Board Panel)
                                  └────────────────┬────────────────┘
                                                   │
                                  ┌────────────────▼────────────────┐
                                  │ LEVEL 7: Case & HR Simulations  │ (Consulting & STAR)
                                  └────────────────┬────────────────┘
                                                   │
                                  ┌────────────────▼────────────────┐
                                  │ LEVEL 6: Technical Trees        │ (Branching Oral Bank)
                                  └────────────────┬────────────────┘
                                                   │
                                  ┌────────────────▼────────────────┐
                                  │ LEVEL 5: Role & Company OAs     │ (Company-Specific Tests)
                                  └────────────────┬────────────────┘
                                                   │
                                  ┌────────────────▼────────────────┐
                                  │ LEVEL 4: Hard & Expert Mocks    │ (High-Selectivity Drill)
                                  └────────────────┬────────────────┘
                                                   │
                                  ┌────────────────▼────────────────┐
                                  │ LEVEL 3: Full Placement Mocks   │ (50-Q Multi-Domain)
                                  └────────────────┬────────────────┘
                                                   │
                                  ┌────────────────▼────────────────┐
                                  │ LEVEL 2: Sectional Tests        │ (30-40m Section Timed)
                                  └────────────────┬────────────────┘
                                                   │
                                  ┌────────────────▼────────────────┐
                                  │ LEVEL 1: Topic Diagnostics      │ (15-Q Focus Check)
                                  └─────────────────────────────────┘
```

---

## 2. Assessment Level Specifications

| Level | Examination Unit | Scope & Structure | Target Time | Benchmark `[PREPARATION HEURISTIC]` | Primary Directory |
|:---|:---|:---|:---:|:---:|:---|
| **Level 1** | **Topic Diagnostics** | 15 MCQs focused on a single topic (e.g., Time & Work, Critical Flow, Syllogisms). | 15–20 min | $\ge 12/15$ ($\ge 80\%$) | [`aptitude/tests/`](../aptitude/tests/) |
| **Level 2** | **Sectional Tests** | 25–30 MCQs across an entire section (Quant, DI, Reasoning, Verbal, Civil Core). | 30–40 min | $\ge 75\%$ score, $\le 75\text{ s/Q}$ | [`aptitude/tests/section/`](../aptitude/tests/section/) |
| **Level 3** | **Full Placement Mocks** | 50 MCQs balanced across Quant (15), Reasoning (15), DI (10), Verbal (10). Standard campus OA simulation. | 60 min | $\ge 37.5 / 50$ ($\ge 75\%$) | [`aptitude/mocks/`](../aptitude/mocks/) |
| **Level 4** | **Hard & Expert Mocks** | 50–60 MCQs with complex multi-table DI caselets, multi-statement logic, and advanced algebra. | 60 min | $\ge 70\%$ composite score | [`aptitude/mocks/`](../aptitude/mocks/) |
| **Level 5** | **Role & Company OAs** | Company-calibrated technical + aptitude blend (L&T, Godrej, BPCL, Vassar Labs). | 45–90 min | Meets company cutoff tier | [`prep/mock-tests/`](../prep/mock-tests/) |
| **Level 6** | **Technical Branching Trees** | Multi-level oral inquiry (Core theory $\to$ Mathematical derivation $\to$ Edge case $\to$ Industrial application). | 30–45 min | Level 4+ defense on core thesis | [`prep/interview/technical/technical-interview-bank.md`](../prep/interview/technical/technical-interview-bank.md) |
| **Level 7** | **Case & Behavioral Sims** | Management consulting caselets, guesstimates, and structured STAR behavioral probes. | 30–40 min | Clear MECE structure, 0 contradictions | [`non-core/consulting/`](../non-core/consulting/) · [`prep/CASE_GD.md`](../prep/CASE_GD.md) |
| **Level 8** | **Full Live Simulation** | End-to-end 45-minute mock interview panel covering Resume, Core Thesis, Aptitude, Case, and HR. | 45 min | Composite Score $\ge 85/100$ | [`prep/MOCK_INTERVIEW.md`](../prep/MOCK_INTERVIEW.md) |

---

## 3. Timing, Scoring, and Examination Rules

### 3.1 Standard Scoring Protocol

Unless specified otherwise in a role-specific test:

$$\text{Total Score} = (\text{Correct Responses} \times 1.0) - (\text{Incorrect Responses} \times 0.25)$$

Unattempted questions score $0$.

### 3.2 Time-Allocation Budget

Strict time budgets must be enforced during timed runs:

```
┌──────────────────────────────────────┬─────────────────────────┐
│ Section                              │ Target Time per Question│
├──────────────────────────────────────┼─────────────────────────┤
│ Quantitative Aptitude                │ 60 – 75 seconds         │
│ Data Interpretation (per Question)   │ 75 – 90 seconds         │
│ Logical Reasoning                    │ 45 – 60 seconds         │
│ Verbal Ability / Comprehension       │ 35 – 50 seconds         │
│ Civil Engineering Core Technical     │ 45 – 60 seconds         │
└──────────────────────────────────────┴─────────────────────────┘
```

> **The 90-Second Rule**: In any Level 2–4 aptitude test, if an individual problem takes longer than 90 seconds without a visible path to the final solution, **mark for review and immediately skip**. Lingering on difficult questions destroys section-level composite scores.

---

## 4. Error Classification & Diagnostic Protocol

After completing any test at Level 1 through Level 5, every incorrect or skipped question must be classified into one of four error buckets:

```
                   ERROR CLASSIFICATION TAXONOMY
     ┌────────────────────────────────────────────────────────┐
     │  [C] CONCEPTUAL GAP                                    │
     │      Formula forgotten, theorem misapplied, or theory  │
     │      unfamiliar. Remediate via canonical topic guide.  │
     ├────────────────────────────────────────────────────────┤
     │  [A] ARITHMETIC / EXECUTION SLIP                       │
     │      Understood method, but made algebra, sign, or     │
     │      unit conversion error. Remediate with scratchpad  │
     │      discipline.                                       │
     ├────────────────────────────────────────────────────────┤
     │  [T] TRAP / MISINTERPRETATION                          │
     │      Misread question stem ("which is NOT true",       │
     │      radius vs diameter, percentage points vs percent).│
     ├────────────────────────────────────────────────────────┤
     │  [M] TIME / PACING BOTTLENECK                          │
     │      Question understood, but ran out of time or spent │
     │      >120s grinding algebraic calculations.            │
     └────────────────────────────────────────────────────────┘
```

---

## 5. The Closed-Loop Retest Engine

Diagnostic testing is useless without systematic remediation. The repository enforces a 6-step closed loop:

1. **Step 1: Baseline Test** — Take the designated diagnostic test under exam conditions.
2. **Step 2: Score & Classify** — Calculate net score using the $+1 / -0.25$ formula and classify every mistake ($C, A, T, M$).
3. **Step 3: Root-Cause Review** — Compare candidate solution step-by-step against the canonical full solution key.
4. **Step 4: Targeted Remediation**:
   - For $[C]$ errors: Read the canonical topic guide in `aptitude/` or `core/hwre/`.
   - For $[A]$ errors: Redo the numerical calculation twice by hand without a calculator.
   - For $[T]$ errors: Underline keywords in the question prompt.
   - For $[M]$ errors: Learn the alternative shortcut or approximation heuristic.
5. **Step 5: 48-Hour Quarantine** — Wait at least 48 hours to prevent short-term visual memorization.
6. **Step 6: Retest** — Attempt an alternate test or an unattempted sectional module to verify mastery.

---

## 6. Scorecard Integration

All test results should be logged in [`prep/READINESS_SCORECARD.md`](../prep/READINESS_SCORECARD.md). The candidate moves from **🟡 NEEDS CALIBRATION** to **🟢 READY** when composite benchmarks across all 5 active levels are verified under timed conditions.

---

> **Related Navigation**:
> [TESTING_GUIDE.md](TESTING_GUIDE.md) · [IITK_PLACEMENT_MAP.md](IITK_PLACEMENT_MAP.md) · [MASTER_NAVIGATION.md](MASTER_NAVIGATION.md) · [READINESS_SCORECARD.md](../prep/READINESS_SCORECARD.md)
