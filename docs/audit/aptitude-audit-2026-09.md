# Aptitude Folder — Independent Audit & One-Stop Rebuild Plan

**Target:** `aptitude/` in `DKS_IITK_Civil_HWRE_Placement_2026`
**Audience:** IIT Kanpur M.Tech Civil / HWRE (CFD/OpenFOAM) placement candidate
**Date:** 2026-09-11
**Method:** Full structural inspection of all 61 files across `aptitude/` + `_SYSTEM/APTITUDE_*`, plus close reading of every file type (all 8 meta files; representative deep reads of quant, reasoning, DI, verbal modules; all 14 topic tests' answer keys; the full mock). Company-pattern claims are checked against the repo's own `prep/company-profiles/` and general knowledge of Indian placement testing; nothing about specific companies is fabricated — items that need verification are flagged.

---

## 1. Executive Verdict

| Question | Answer |
|---|---|
| **Current status** | **Incomplete — major gaps.** A strong navigation/planning shell and solid *teaching* text for quant + verbal, sitting on top of a practice layer that is roughly 40% unanswered, ~6% broken, heavily duplicated, and missing several whole domains. |
| **Placement readiness it delivers** | **Basic.** Borderline Basic→Intermediate for a plain quant+verbal screen (TCS-style). **Beginner** for consulting / analytics / eLitmus / any test with non-verbal, analogy/classification, or statement-argument reasoning. |
| **Is it a "one-stop" system yet?** | No. It is a good *skeleton* of one. |
| **Repo's own self-assessment** | `_SYSTEM/APTITUDE_COMPLETENESS_MATRIX.md` scores every P0 topic 9/10 and declares "Target Met / PLACEMENT_READY". **This audit does not support that claim** — the matrix is self-graded and was not validated against the actual question content. Treat it as aspirational, not factual. |

**The three things that make it "not ready" regardless of topic coverage:**

1. **Unreliable answer keys.** 6 of 14 topic tests (`probability-test`, `si-ci-test`, `profit-loss-test`, `permutations-combinations-test`, `series-test`, `speed-time-distance-test`) have **every single answer = "A"** (verified: 15/15 each). A candidate who bubbles "A" throughout scores 100%. These tests cannot measure or build skill and actively train a wrong instinct.
2. **Broken questions shipped with visible AI scratchpad.** The flagship mock and several reasoning/DI modules contain questions whose own solutions say things like *"Options are wrong. Correct answer: 8."*, *"the puzzle is flawed. I'll present a corrected version."*, *"answer is likely 63 (common in such tests)."* See §4 and the Appendix.
3. **Whole domains absent:** non-verbal/abstract reasoning (0 files), analogy & classification (0), statement–assumption/argument/conclusion (0), company/platform test patterns (0), civil-core aptitude (0), engineering-mathematics screening (0), cloze test (0), sectional & high-difficulty mocks (0).

---

## 2. What Exists Today (inventory)

```
aptitude/                    61 files, ~4,900 lines
├── 8 meta files             README, ROADMAP, ROLE_MATRIX, 7_14_30_DAY_PLAN,
│                            DAILY_PLAN, FORMULA_SHEET, RAPID_REVISION, ERROR_LOG
├── quant/                    17 topic modules
├── reasoning/               10 topic modules
├── di/                       5 topic modules
├── verbal/                   6 topic modules
├── tests/                   14 topic tests (10–15 Q each)
└── mocks/                    1 full mock (50 Q / 60 min)
```

Plus three **other** overlapping aptitude corpora in the workspace that the repo's own audit already identified: `Aptitude/` (34 files, root sibling), `Aptitude-For-Placements/` (~60 solved examples), and `aptitude/` (20 condensed modules, still linked from the repo README role-navigation). Consolidation is unfinished.

**Approximate question count:** ~950–1,000 items total, but only ~55–60% have a worked answer. The ~255 "Practice — Basic/Intermediate/Advanced" questions inside the quant modules and the ~130 practice items inside the reasoning modules have **no answer key at all**.

### Meta layer — GOOD (keep, light edits)

`README`, `ROADMAP`, `ROLE_MATRIX`, `7_14_30_DAY_PLAN`, `DAILY_PLAN`, `RAPID_REVISION`, `ERROR_LOG` are genuinely well done: clear navigation, a sensible learn→time→test→analyse loop, role-weighted topic priorities, realistic day plans, a proper error-log workflow with spaced reattempts. This is the strongest part of the folder and needs only: (a) links to the new sections added below, (b) `FORMULA_SHEET` correction — see next.

### `FORMULA_SHEET.md` — one hard error

**Sphere volume is written as `¾πr³`. It is `4⁄3 πr³`.** The same wrong value is repeated in `quant/mensuration.md`. Hemisphere (`⅔πr³`) is correct, so only the full-sphere entry is wrong. Fix in both files. Otherwise the sheet is accurate but thin (no algebra identities beyond basics, no logarithms/surds, no geometry theorems, no coordinate geometry, no stats).

---

## 3. Domain-by-Domain Audit

Legend: **Have** = usable module with answers · **Partial** = module exists but thin / unanswered practice / quality issues · **Missing** = no coverage in `aptitude/` or the three sibling corpora.

### 3.1 Quantitative Aptitude

| Sub-topic | Status | Notes |
|---|---|---|
| Number system, HCF/LCM, simplification | Partial | Good text + 5 worked + 3 solved MCQ each; 15 practice Q **unanswered**. Remainders/modular arithmetic thin. |
| Percentages, ratio & proportion, averages, profit/loss/discount | Partial | Best-built quant modules. Same "15 unanswered practice" gap. `profit-loss.md` has a garbled trap-table entry (line 96). |
| SI & CI, mixtures & alligation, partnership, ages | Partial | Fine content; unanswered practice. |
| Time & work (incl. pipes & cisterns) | Partial | Pipes folded in adequately. Unanswered practice. |
| Time-speed-distance (incl. trains, boats & streams) | Partial | Trains/boats folded in but only 1–2 examples each; deserve their own drill sets. |
| Probability, permutations & combinations | Partial | Conditional probability, Bayes, circular/restricted arrangements under-covered. |
| Progressions (AP/GP/HP) | Partial | HP and AGP missing; only basic AP/GP. |
| Mensuration | Partial | **Sphere volume error.** No pure geometry (triangles, circles, similarity, polygons). P2 priority is too low for a Civil student. |
| **Algebra — linear & quadratic equations, identities, factorisation** | **Missing** | Only a 6-line formula block. No module, no practice. Appears in almost every test. |
| **Surds, indices, logarithms** | **Missing** | Standard in TCS NQT, GATE-adjacent screens. |
| **Geometry (lines/angles/triangles/circles/quadrilaterals, Pythagorean triples)** | **Missing** | Distinct from mensuration; high value for Civil. |
| **Coordinate geometry** | **Missing** | `_SYSTEM` matrix already flags this as 0/10. |
| **Set theory / Venn (numeric two- and three-set)** | **Missing** | Only appears implicitly in one percentages example. |
| **Inequalities, functions, basic trigonometry** | **Missing** | Low-frequency but expected in a "one-stop" claim. |
| Data sufficiency (quant style) | Partial | Lives in `di/data-sufficiency.md`; 3 worked + 2 solved, 15 unanswered; non-standard option lettering. |
| **Calculation-speed drills** (tables ×30, squares/cubes, fraction↔%↔decimal, reciprocals) | **Missing** | Only scattered in number-system. Deserves its own timed drill file. |

### 3.2 Logical Reasoning

| Sub-topic | Status | Notes |
|---|---|---|
| Number/letter series, wrong-term | Partial | Good text; 15 practice **unanswered**; letter/alphanumeric series thin. |
| Coding–decoding | **Broken** | Worked Example 1 premise is self-inconsistent ("CAT → DBT" under a "+1" rule; +1 gives DBU). Worked Example 4 (BRIGHT=54) ships a full failed-derivation scratchpad ending *"answer is likely 63"*. Example 2 answer (59) **contradicts** the mock's answer (58) for the identical question. |
| Blood relations, direction sense | Partial | Content OK; unanswered practice. |
| Order & ranking | **Broken** | Worked Example 3 and Placement Q3 contain "Let me recalculate / Hmm, let me recheck" scratchpad; Placement Q3's stated answer ("C) 9") is contradicted two lines later by "**Answer: B) 8**". |
| Seating arrangement (linear/circular/two-row) | Partial | Module text OK. The **test** (`tests/seating-arrangement-test.md`) has 4 non-questions ("Various clues", "multiple constraints" with no clues given) and Q1 answer-key ("D") contradicts its own explanation ("Answer: A"). |
| Puzzles & scheduling (floor/box/month) | **Broken** | Worked Example 2 openly states *"the puzzle is flawed. I'll present a corrected version."* The same flawed puzzle is repeated as Practice Q2. Hard practice Q6–Q10 are placeholders ("Seven people … with multiple constraints"). No practice answers. |
| Syllogism | Have (mostly) | 3 solid worked + 3 solved MCQ; propositions, either-or, possibility covered. 15 practice **unanswered**. |
| Input–output (machine) | Partial | Modern IBPS-style single module; unanswered practice. |
| Clocks & calendars | Partial | Basic; thin. |
| **Analogy (verbal / number / letter)** | **Missing** | Flagged 0/10 by `_SYSTEM` matrix. Near-universal in placement tests. |
| **Classification / odd-one-out** | **Missing** | Flagged 0/10. |
| **Statement & Assumptions / Arguments (strong-weak) / Conclusions / Course of Action** | **Missing** | Core of bank, PSU, and many IT tests. |
| **Cause & Effect, Assertion–Reason** | **Missing** | |
| **Logical Venn diagrams (reasoning, not numeric)** | **Missing** | |
| **Coded inequalities, symbol/notation substitution** | **Missing** | Mock Q22 tries this and is broken. |
| **Data sufficiency (reasoning), decision-making / eligibility** | **Missing** | |
| **Logical sequence of words, situation reaction** | **Missing** | |
| Data-arrangement + DI combined (analytical puzzles from data) | **Missing** | High value for consulting/analytics. |

### 3.3 Abstract / Non-Verbal Reasoning — **ENTIRELY ABSENT**

No `non_verbal/` folder; nothing in the three sibling corpora either. All of the following are missing: figure series, figure analogy, figure classification, pattern/rule detection, mirror & water images, paper folding & cutting, completion of incomplete pattern, embedded/hidden figures, cubes & dice, grouping of figures, dot situation. Non-verbal is less central to *IIT* placements than to mass recruiters, but **eLitmus, AMCAT, CoCubes, several PSUs, and some IT screens include it**, and a "one-stop" resource cannot omit it. Cubes & dice and figure series are the highest-value items here.

### 3.4 Verbal Ability — **strongest section, still has gaps**

| Sub-topic | Status | Notes |
|---|---|---|
| Reading comprehension | Have | 3 passages, 15 Q **all answered with explanations**. Good. But: only 3 passages, all ~150 words. Placement/consulting RC is 300–900 words. Passage 2 is duplicated verbatim in the mock. |
| Grammar & error spotting | Have | 20 Q all answered + explained. Solid. |
| Sentence completion / fill-in-the-blanks | Have | Answered. Single-blank only; double-blank thin. |
| Para jumbles | Have | 12 Q answered — but 6 of the "hard/very-hard" items resolve to the sentences **already in order** (A-B-C-D-E-F), so they are not real jumbles. |
| Vocabulary | Have | 20 Q answered + 8 themed word-groups (~50 words). Far too thin for placement — target 300–500 words with spaced-repetition sets. Typo "perillous" (line 72). |
| Critical reasoning | Partial | 3 worked + 2 solved; the 15 "practice" items are bare stubs with no options and no answers. |
| **Cloze test** | **Missing** | Standard in TCS, Accenture, Cognizant. |
| **Sentence correction / improvement (as a distinct drill)** | **Missing** | Different skill from error-spotting. |
| **Synonyms & antonyms (dedicated bulk sets)** | **Missing** | Only ~10 antonym pairs exist. |
| **One-word substitution, idioms & phrases, para-completion, spelling** | **Missing** | Idioms exist in root `Aptitude/` but were not carried into `aptitude/verbal/`. |
| **Verbal analogy** | **Missing** | (also missing from reasoning) |

### 3.5 Data / Analytical Skills

| Sub-topic | Status | Notes |
|---|---|---|
| Tables & caselets | **Broken** | `di/tables-caselets.md`: Q7 ("Answer: B) 73.3" → "**Answer corrected:** A) 72.5"), Q10 (→ "**Answer corrected:** A) Beena"), and Q13 (answer not among options, rationalised as "this tests whether you verify") shipped with scratchpad. Q14–Q15 then build on the broken Q13 value. |
| Bar/line graphs, pie charts, mixed graphs | Partial | Present; not deeply inspected line-by-line but same template. |
| Data sufficiency | Partial | See 3.1. |
| Approximation, mental calculation, numerical estimation | Partial | Mentioned as strategy; no dedicated drill sets. |
| **Caselet-heavy, missing-data DI, multi-graph, radar/bubble/stacked** | **Missing / thin** | Matrix flags missing-data DI as 0/10. |
| **Data-driven logical reasoning (DI + arrangement)** | **Missing** | Core consulting/analytics format. |
| **Volume of unique datasets** | **Critical gap** | The **entire folder recycles ~4 datasets**. The mock's DI section, `di-test.md`, and `di/tables-caselets.md` SET 1 are the **same sales table and the same water pie**, near-verbatim. Need 25–30 distinct sets. |

### 3.6 Placement-Specific Testing — **ENTIRELY ABSENT**

No `company_patterns/` folder. Nothing on: negative marking regimes, sectional cutoffs, adaptive testing (AMCAT and TCS NQT are adaptive), calculator-allowed vs not, per-platform structure. The repo's `prep/company-profiles/*` mention "online aptitude" in passing (e.g. `civil-lt.md` §7) but there is no consolidated, structured pattern reference. This is the single most valuable thing to add for an IITK candidate, because the test *format* often matters more than raw topic depth.

Platforms/among-companies to document (structure, #Q, time, negative marking, sectional cutoff, adaptive?, difficulty, calculator?): **TCS NQT / iON**, **CoCubes**, **AMCAT (Aspiring Minds)**, **eLitmus pH Test**, **Mercer|Mettl**, **HackerRank/HackerEarth aptitude**, **SHL / Aon cut-e (Verify, ADEPT-15)**, **Pearson/Versant**, **IBM Kenexa**, **Criteria (CCAT)**. Consulting: **McKinsey Solve (Imbellus)**, **BCG (Casey/online case + Pymetrics)**, **Bain (SOVA / Test)**, **Kearney**, **ZS Associates** (multi-round aptitude), analytics: **Axtria, Tiger Analytics, Fractal, Mu Sigma, Accenture (Cognitive + Analytical)**. Core/EPC: **L&T** (own online test: quant + LR + technical MCQ), **Tata Projects, Afcons, AECOM**. Every entry must be labelled with an evidence-confidence tag and "verify current pattern from the placement cell before relying on it."

### 3.7 Core-Civil / Engineering Aptitude — **ABSENT as an aptitude section**

Relevant material exists elsewhere (`core/gate/`, subject guides) but is not framed or drilled as *aptitude*. A Civil/HWRE-specific quantitative-aptitude set should cover: unit conversions & dimensional analysis (SI/FPS, cumec ↔ MLD ↔ lpcd), quantity-estimation arithmetic (BOQ %, wastage, bulking of sand, mix-design ratios like M20 = 1:1.5:3), percentages in compaction / moisture content / voids / efficiency, mensuration for earthwork (trapezoidal & prismoidal volume, area by coordinates, cross-sections), discharge `Q = A·V` and reservoir fill/empty time, slope/gradient/% grade/camber, weighted averages (CBR, SPT-N), interest & engineering economics (straight-line & WDV depreciation, EMI, benefit–cost ratio, simple NPV), probability & return period (`T = 1/p`, risk `= 1 − (1 − 1/T)ⁿ`), and interpretation of engineering plots (hydrographs, rating curves, stress–strain, S–N).

Keep **engineering mathematics / physics screening** strictly separate (the user asked for this): a short MCQ set on matrices/eigenvalues, calculus (maxima–minima, definite integrals), vector calculus (grad/div/curl — CFD), numerical methods (Newton–Raphson, trapezoidal/Simpson, Gauss elimination), probability distributions & regression, plus fluid-mechanics screening (Bernoulli, continuity, Reynolds number, Manning, pump power `P = ρgQH`, dimensional analysis / Buckingham π). Cross-link to `core/gate/` rather than duplicate the theory.

---

## 4. Systemic Quality Defects (with evidence)

| # | Defect | Evidence | Severity |
|---|---|---|---|
| Q1 | **Degenerate answer keys** — all answers "A" | `probability-test`, `si-ci-test`, `profit-loss-test`, `permutations-combinations-test`, `series-test`, `speed-time-distance-test`: 15/15 = A (verified). `time-work-test`, `averages-test`: 14/15 = A. | CRITICAL |
| Q2 | **Broken questions with visible AI scratchpad** | `mocks/full-placement-mock-1.md` Q14 ("Options are wrong. Correct answer: 8"), Q20 ("Closest is 58… approximately"), Q22 ("The options seem wrong. Let me just set the answer…"), Q29 ("Without drawing… Answer: A"), Q30 ("answer is likely 63"). `di/tables-caselets.md` Q7/Q10/Q13. `reasoning/coding-decoding.md` Ex.4. `reasoning/puzzles-scheduling.md` Ex.2. `reasoning/order-ranking.md` Ex.3 & Placement Q3. `tests/probability-test.md` Q13. | CRITICAL |
| Q3 | **Answer key contradicts its own explanation** | `tests/seating-arrangement-test.md` Q1 (key D, explanation "A"), Q6 (key A, explanation "D"). `mocks/…mock-1.md` Q27 (key A = "5 km", solution concludes "3 km" = B, twice). `reasoning/order-ranking.md` Placement Q3 (labelled C, working says B). | CRITICAL |
| Q4 | **Placeholder "non-questions"** | `tests/seating-arrangement-test.md` Q7–Q10; `reasoning/puzzles-scheduling.md` practice Q6–Q10 — no constraints supplied, unsolvable by construction. | HIGH |
| Q5 | **~40% of practice questions have no answer key** | Every `quant/*` "Practice — Basic/Intermediate/Advanced" block (17 modules × 15 Q ≈ 255). Every `reasoning/*` practice block. `verbal/critical-reasoning.md` practice. | HIGH |
| Q6 | **Heavy duplication** | Mock Section C = `tests/di-test.md` ≈ `di/tables-caselets.md` SET 1 (same 2 datasets). Mock Section D ≈ `verbal/reading-comprehension.md` Passage 2 + `tests/verbal-test.md`. `tests/verbal-test.md` Q1/Q2/Q5/Q8/Q14 duplicate `verbal/vocabulary.md` and the mock. | HIGH |
| Q7 | **Factual error** | Sphere volume `¾πr³` (should be `4⁄3 πr³`) in `FORMULA_SHEET.md` and `quant/mensuration.md`. | HIGH |
| Q8 | **Cross-file answer contradictions** | Coding "TIGER" = 59 (`reasoning/coding-decoding.md`) vs 58 (mock Q20). Series wrong-term item uses "…47, 94, 191" (mock Q28) vs "…47, 95" (`reasoning/series.md` practice Q14). | MEDIUM |
| Q9 | **Answer options not randomised** | Even where keys are correct, correct answer is disproportionately option A/B. Tests are not "blind." | MEDIUM |
| Q10 | **Four overlapping aptitude corpora** unconsolidated | `aptitude/`, `Aptitude/`, `Aptitude-For-Placements/`, `aptitude/` (last still linked from repo README). | MEDIUM |
| Q11 | **Trivial "jumbles"** | `verbal/para-jumbles.md` Q6, Q8, Q9, Q10, Q12 answer = sentences already in order. | LOW |
| Q12 | Typos | "perillous" (`verbal/vocabulary.md` L72); CJK stray text was fixed separately in the Sep-2026 accuracy review. | LOW |

---

## 5. File-by-File Evaluation

Rating: **Good** (keep, minor edits) · **Fix** (usable after correction) · **Rebuild** (structurally broken or degenerate) · **Add** (does not exist).

### Meta (8)
| File | Rating | Action |
|---|---|---|
| `README.md` | Good | Add links to new sections (§8). |
| `ROADMAP.md`, `7_14_30_DAY_PLAN.md`, `DAILY_PLAN.md`, `ERROR_LOG.md`, `RAPID_REVISION.md` | Good | Add non-verbal / company-pattern / civil-core rows to the plans. |
| `ROLE_MATRIX.md` | Good | Add rows for the new topics; add a "test platform by company" column or companion table. |
| `FORMULA_SHEET.md` | Fix | Correct sphere volume; add algebra identities, log/surd rules, geometry theorems, coordinate-geometry, stats, engineering-economics blocks. |

### quant/ (17)
| File | Rating | Action |
|---|---|---|
| `percentages`, `ratio-proportion`, `averages`, `profit-loss`, `number-system`, `time-work`, `speed-time-distance`, `simple-compound-interest`, `simplification`, `hcf-lcm`, `partnership`, `problems-on-ages`, `progressions`, `mixtures-alligation`, `permutations-combinations`, `probability` | Fix | Add a full **answer key + one-line solution** for every "Practice" question (15 each). Add 5–8 harder placement MCQs per file with randomised options. `profit-loss` L96 trap-table fix. Deepen: remainders (number-system), conditional probability & Bayes (probability), restricted/circular arrangements (P&C), HP & AGP (progressions), trains & boats as their own sub-sets (speed-time-distance). |
| `mensuration` | Fix | Sphere-volume error; add pure-geometry section or split; raise priority for Civil. |

### reasoning/ (10)
| File | Rating | Action |
|---|---|---|
| `syllogism`, `series`, `blood-relations`, `direction-sense`, `input-output`, `clocks-calendars` | Fix | Add practice answer keys; broaden `series` to alphanumeric; add real datasets to `input-output`. |
| `coding-decoding` | Rebuild | Ex.1 premise inconsistent; Ex.4 fabricated. Rewrite all worked examples with verified answers; reconcile "TIGER" with the mock; add answer keys. |
| `order-ranking` | Rebuild | Ex.3 & Placement Q3 broken/contradictory. Rewrite with clean worked solutions. |
| `puzzles-scheduling` | Rebuild | Broken worked example + placeholder practice. Replace with 8–10 fully-specified, fully-solved puzzles across floor/linear/circular/month/box/grouping. |
| `seating-arrangement` | Fix | Module text OK; the matching test is the problem (below). |

### di/ (5)
| File | Rating | Action |
|---|---|---|
| `tables-caselets` | Rebuild | Q7/Q10/Q13 broken. Rewrite with verified answers; every question's options must contain the correct value. |
| `bar-line-graphs`, `pie-charts`, `mixed-graphs`, `data-sufficiency` | Fix | Add fresh unique datasets (stop reusing the sales table); add practice answer keys; standard DS option lettering. |

### verbal/ (6)
| File | Rating | Action |
|---|---|---|
| `reading-comprehension` | Fix | Keep the 3 passages; add 12–15 more incl. 500–900-word passages (science, business, abstract, tech). De-duplicate from the mock. |
| `grammar-error-spotting`, `vocabulary`, `sentence-completion` | Good→Fix | Grammar is solid. Vocabulary: expand to 300–500 words + antonym/synonym bulk sets + spaced-repetition list. Fix "perillous". |
| `para-jumbles` | Fix | Replace the 5 "already-ordered" items with genuine jumbles (4- and 6-sentence, with anchor options). |
| `critical-reasoning` | Fix | Convert the 15 practice stubs into full items (stimulus + 4 options + answer + why-wrong). |

### tests/ (14)
| File | Rating | Action |
|---|---|---|
| `probability-test`, `si-ci-test`, `profit-loss-test`, `permutations-combinations-test`, `series-test`, `speed-time-distance-test`, `time-work-test`, `averages-test`, `ratio-proportion-test` | Rebuild | Degenerate/near-degenerate answer keys. Re-key with randomised option positions; add a full worked solution (not just a letter) for every question; expand to 15–20 Q. |
| `seating-arrangement-test` | Rebuild | 4 non-questions + 2 key/explanation contradictions. |
| `di-test` | Rebuild | 100% duplicate of the mock's DI section. New datasets. |
| `number-system-test`, `percentages-test`, `verbal-test` | Fix | Real answer distributions; de-duplicate `verbal-test` from the mock; add worked solutions. |

### mocks/ (1)
| File | Rating | Action |
|---|---|---|
| `full-placement-mock-1` | Rebuild | Fix Q14, Q20, Q22, Q27 (key vs solution), Q29, Q30; strip all "Hmm / let me recalculate" text; replace DI section with fresh data; randomise options. Then treat as the template for Mocks 2–8. |

---

## 6. Gap Analysis

Priority: **CRITICAL** = must have before placements · **HIGH** = strongly recommended · **MEDIUM** = useful · **LOW** = optional.
"Recommended questions" = new items to author (with answers), on top of fixing what exists.

| Topic | Current coverage | Missing content | Priority | Recommended new Qs | Difficulty mix |
|---|---|---|---|---|---|
| **Answer keys for existing practice** | ~40% of practice unanswered | Full key + 1-line solution for every practice Q in quant/ & reasoning/ | **CRITICAL** | ~400 solutions (no new Qs) | n/a |
| **Fix broken items** | ~15 broken/contradictory Qs | Corrected questions + verified answers; strip scratchpad | **CRITICAL** | ~15 rewrites | n/a |
| **Re-key degenerate tests** | 6–9 tests all-"A" | Randomised keys + worked solutions | **CRITICAL** | ~120 solutions + re-key | Easy→Hard |
| Algebra (linear/quadratic/identities) | Formula block only | Full module + drills | **CRITICAL** | 40–50 | 15E / 20M / 15H |
| Analogy (verbal/number/letter) | None | Full module | **CRITICAL** | 40 | 15E / 15M / 10H |
| Classification / odd-one-out | None | Full module | **CRITICAL** | 30 | 12E / 12M / 6H |
| Statement–Assumption / Argument / Conclusion / Course of Action | None | Module (4 sub-types) | **HIGH** | 50 | 10E / 25M / 15H |
| Non-verbal: figure series, analogy, classification | None | Module (SVG or described figures) | **HIGH** | 45 | 15E / 20M / 10H |
| Non-verbal: cubes & dice, mirror/water images, paper folding | None | Module | **HIGH** | 30 | 10E / 12M / 8H |
| Cloze test | None | Module | **HIGH** | 8 passages ×5 | M–H |
| Reading comprehension (long/varied) | 3 short passages | 12–15 passages, 300–900 words | **HIGH** | 15 passages ×5 = 75 | M–VH |
| Vocabulary (bulk) | ~50 words | 300–500 words + synonym/antonym sets + SRS list | **HIGH** | 300+ words, 120 MCQ | E–H |
| Data Interpretation datasets | ~4 datasets recycled | 25–30 distinct sets (table/bar/line/pie/caselet/mixed/missing-data) | **HIGH** | 25 sets ×5 = 125 | 30E / 60M / 35H |
| Data-driven logical reasoning (DI + arrangement) | None | Module (consulting/analytics format) | **HIGH** | 12 sets ×4 = 48 | M–VH |
| Geometry (plane) | None (mensuration only) | Module: triangles, circles, similarity, polygons | **HIGH** | 35 | 12E / 15M / 8H |
| Surds, indices, logarithms | None | Module | **HIGH** | 25 | 10E / 10M / 5H |
| Company / platform test patterns | None | 15–20 pattern briefs + reference | **HIGH** | reference doc + 6 pattern mocks | mixed |
| Civil-core aptitude | None (as aptitude) | Module + drills (units, estimation, earthwork, econ, return period) | **HIGH** | 50 | 15E / 25M / 10H |
| Sentence correction / improvement | Partial (error-spotting) | Distinct drill | MEDIUM | 30 | E–H |
| One-word substitution, idioms & phrases, para-completion | None (idioms in root `Aptitude/`) | Modules | MEDIUM | 60 + 40 | E–M |
| Coded inequalities, symbol substitution | None (mock item broken) | Module | MEDIUM | 25 | M–H |
| Cause & Effect, Assertion–Reason, decision-making, logical-Venn | None | Module | MEDIUM | 40 | M–H |
| Set theory / numeric Venn (2- & 3-set) | 1 example | Module | MEDIUM | 20 | E–M |
| Coordinate geometry | None (0/10) | Section in geometry module | MEDIUM | 20 | E–M |
| Calculation-speed drills | Scattered | Dedicated timed drill file | MEDIUM | 10 drill sheets | E |
| Engineering mathematics screening | None (in aptitude) | MCQ module, cross-linked to `core/gate/` | MEDIUM | 60 | M–H |
| Fluid-mechanics / physics screening | None | Short MCQ set | MEDIUM | 30 | M–H |
| Progressions: HP, AGP; conditional probability; circular P&C | Thin | Extend existing modules | MEDIUM | 30 | M–H |
| Trains / boats & streams as own sets | Folded into TSD | Dedicated drill sets | MEDIUM | 30 | E–M |
| Radar/bubble/stacked charts, spelling, active-passive | None | Small additions | LOW | 30 | E–M |

---

## 7. Question-Bank Quality Requirements

Every topic module, after rebuild, must contain:

| Component | Target per major topic |
|---|---|
| Concept + formula + shortcut text | 1 section (exists for most) |
| Worked examples (fully solved, step-by-step) | 6–8, verified, no scratchpad |
| Practice — Easy | 10, **with answer key + 1-line solution** |
| Practice — Medium | 12, with answers |
| Practice — Hard | 10, with answers |
| Placement-level mixed MCQ | 8–10, 4 options, **options randomised**, answer + why-each-wrong |
| Timed set | 1 (10–15 Q, target time, benchmark) |
| Common traps | 4–6 (exists for quant) |
| Rapid-revision block | 1 (exists) |

Rules:
- **Never** leave a practice question without a verified answer.
- **Never** ship a question whose correct value is absent from its options.
- **Never** leave model reasoning ("Hmm", "let me recalculate", "not in options") in a solution.
- Randomise correct-option position (~25% each of A/B/C/D across a set).
- Generated questions are labelled **"Practice (generated)"**. Reported company/platform patterns are labelled **"Reported pattern — representative, not actual recalled questions"** with an evidence-confidence tag. Do **not** label any generated question as a real past company question.
- Difficulty tag on every question; each module reports its own difficulty distribution.

---

## 8. Target Structure (with exact files)

```
aptitude/
├── README.md                         (update)
├── ROADMAP.md  ROLE_MATRIX.md  7_14_30_DAY_PLAN.md  DAILY_PLAN.md
├── FORMULA_SHEET.md  RAPID_REVISION.md  ERROR_LOG.md   (update)
├── MASTER_CHECKLIST.md               ← NEW (see §9)
│
├── quantitative/
│   ├── README.md
│   ├── number-system.md  hcf-lcm.md  simplification.md  surds-indices-logarithms.md   ← NEW
│   ├── percentages.md  ratio-proportion.md  averages.md  mixtures-alligation.md
│   ├── profit-loss-discount.md  simple-compound-interest.md  partnership.md
│   ├── time-work-pipes.md  speed-time-distance.md  trains.md  boats-streams.md         ← trains/boats NEW
│   ├── problems-on-ages.md  progressions.md  algebra-equations.md                       ← algebra NEW
│   ├── geometry.md  coordinate-geometry.md  mensuration.md                              ← geometry/coord NEW
│   ├── permutations-combinations.md  probability.md  set-theory-venn.md                 ← set-theory NEW
│   └── calculation-speed-drills.md                                                      ← NEW
│
├── logical_reasoning/
│   ├── README.md
│   ├── series.md  analogy.md  classification.md                                         ← analogy/classification NEW
│   ├── coding-decoding.md  coded-inequalities-symbols.md                                ← inequalities NEW
│   ├── blood-relations.md  direction-sense.md  order-ranking.md  clocks-calendars.md
│   ├── seating-arrangement.md  puzzles-scheduling.md  input-output.md
│   ├── syllogism.md  logical-venn.md                                                    ← venn NEW
│   ├── statement-assumption-argument-conclusion.md                                      ← NEW
│   ├── cause-effect-assertion-reason.md  decision-making-eligibility.md                 ← NEW
│   └── logical-sequence-situation-reaction.md                                           ← NEW
│
├── non_verbal/                        ← NEW FOLDER
│   ├── README.md
│   ├── figure-series-analogy-classification.md
│   ├── pattern-rule-detection.md
│   ├── mirror-water-images.md
│   ├── paper-folding-cutting.md
│   ├── cubes-and-dice.md
│   └── embedded-and-grouping-figures.md
│
├── verbal/
│   ├── README.md
│   ├── reading-comprehension.md  rc-passage-bank.md                                     ← bank NEW
│   ├── grammar-error-spotting.md  sentence-correction-improvement.md                    ← NEW
│   ├── sentence-completion-fill-blanks.md  cloze-test.md  para-completion.md            ← cloze/para NEW
│   ├── para-jumbles.md
│   ├── vocabulary.md  synonyms-antonyms-bank.md  one-word-substitution.md  idioms-phrases.md  ← 3 NEW
│   ├── verbal-analogy.md                                                                ← NEW
│   └── critical-reasoning.md
│
├── data_interpretation/
│   ├── README.md
│   ├── tables-caselets.md  bar-line-graphs.md  pie-charts.md  mixed-graphs.md
│   ├── missing-data-di.md  radar-bubble-stacked.md                                      ← NEW
│   ├── data-sufficiency.md
│   ├── data-driven-reasoning.md                                                         ← NEW (DI + arrangement)
│   ├── approximation-drills.md                                                          ← NEW
│   └── di-set-bank.md                                                                   ← 25–30 unique datasets
│
├── critical_reasoning/               (optional split from verbal; or keep in verbal/)
│
├── company_patterns/                 ← NEW FOLDER
│   ├── README.md
│   ├── platforms-tcs-nqt.md  amcat.md  cocubes.md  elitmus.md  mettl.md  hackerrank.md  shl-aon.md
│   ├── consulting-mckinsey-bcg-bain-zs.md
│   ├── analytics-accenture-axtria-fractal-tigeranalytics.md
│   ├── finance-barclays-bnymellon.md
│   ├── core-epc-lt-tataprojects-aecom.md
│   ├── psu-gate-and-own-exams.md
│   └── iitk-recruiter-notes.md        (consolidate from prep/company-profiles/*)
│
├── civil_core_aptitude/              ← NEW FOLDER
│   ├── README.md
│   ├── units-dimensional-analysis.md
│   ├── estimation-quantity-arithmetic.md
│   ├── earthwork-mensuration.md
│   ├── engineering-economics.md
│   ├── flow-discharge-reservoir.md
│   ├── return-period-risk-frequency.md
│   └── engineering-graph-interpretation.md
│
├── engineering_mathematics/          ← NEW FOLDER (screening MCQ, cross-linked to core/gate)
│   ├── README.md
│   ├── linear-algebra.md  calculus.md  vector-calculus.md  numerical-methods.md
│   ├── probability-statistics.md  differential-equations.md
│   └── fluid-mechanics-physics-screening.md
│
├── timed_tests/                      ← replaces/absorbs tests/
│   ├── README.md
│   ├── topic/  (one per topic, re-keyed, worked solutions, 15–20 Q)
│   ├── sectional-quant.md  sectional-reasoning.md  sectional-verbal.md  sectional-di.md
│   ├── 30-min-mixed.md  60-min-mixed.md  90-min-full.md
│   ├── high-difficulty-iit.md
│   └── core-engineering-aptitude.md
│
├── mixed_tests/
│   ├── full-placement-mock-1..8.md   (mock-1 rebuilt; 2–8 new)
│   └── pattern-mocks/  tcs-style.md  elitmus-style.md  amcat-style.md  consulting-numerical.md
│
├── previous_style_questions/         ← NEW FOLDER
│   ├── README.md   (disclaimer: representative of reported patterns, not recalled questions)
│   ├── tcs-style-set.md  elitmus-style-set.md  amcat-style-set.md
│   ├── consulting-style-set.md  core-epc-style-set.md
│   └── psu-style-set.md
│
└── resources/                        ← NEW FOLDER
    ├── README.md
    ├── book-list.md      (Arun Sharma, R.S. Aggarwal, Nishit Sinha, Sarvesh Verma …)
    ├── practice-sites.md (IndiaBix, PrepInsta, Faceprep, GfG, PrepLounge …)
    ├── formula-pdfs.md   (links + local one-pager)
    └── flashcards.md     (Anki/CSV: vocab, formulas, traps)
```

---

## 9. Placement Master Checklist

Save as `aptitude/MASTER_CHECKLIST.md`. Tick when you can do it **under time, at ≥80% accuracy**.

### A. Calculation fluency (do these first)
- [ ] Multiplication tables to 30; squares to 30; cubes to 15
- [ ] Fraction ↔ % ↔ decimal table (1/2 … 1/20) from memory
- [ ] Reciprocals to 20; √2, √3, √5, π, e approximations
- [ ] 2- and 3-digit multiplication/division mentally in < 15 s
- [ ] Percentage of a number, % change, successive % — mental

### B. Quantitative (each: solve E in 30 s, M in 60–90 s, H in ≤ 2 min)
- [ ] Number system: divisibility, unit digit, factors, remainders, trailing zeros
- [ ] HCF/LCM word problems; simplification / BODMAS / approximation
- [ ] Surds, indices, logarithms
- [ ] Percentages; ratio & proportion; averages; weighted average; alligation
- [ ] Profit/loss/discount; dishonest dealer; successive discount
- [ ] Simple & compound interest; CI–SI difference; instalments
- [ ] Time & work; efficiency; wages; pipes & cisterns
- [ ] Time-speed-distance; average speed; relative speed; trains; boats & streams
- [ ] Partnership; problems on ages; mixtures (repeated replacement)
- [ ] Algebra: linear & quadratic equations, identities, factorisation
- [ ] Progressions: AP, GP, HP, AGP; sum formulas
- [ ] Permutations & combinations: restrictions, circular, repetition
- [ ] Probability: classical, conditional, at-least-one, Bayes (basic)
- [ ] Set theory / Venn (2- and 3-set)
- [ ] Geometry: triangles, circles, similarity, polygons; Pythagorean triples
- [ ] Coordinate geometry: distance, section, slope, area
- [ ] Mensuration: all 2-D and 3-D (correct sphere volume 4⁄3 πr³), earthwork volumes

### C. Logical reasoning
- [ ] Number / letter / alphanumeric series; wrong-term
- [ ] Analogy (verbal, number, letter); classification / odd-one-out
- [ ] Coding–decoding (shift, reverse, position sum, substitution); coded inequalities; symbol substitution
- [ ] Blood relations (incl. coded); direction sense (incl. coded)
- [ ] Order & ranking (overlapping vs non-overlapping)
- [ ] Seating: linear, circular, two-row, facing in/out
- [ ] Puzzles: floor, box, month/day scheduling, selection, grouping
- [ ] Machine input–output
- [ ] Syllogism: A/E/I/O, either-or, possibility, 3+ statements
- [ ] Logical Venn diagrams
- [ ] Statement & assumptions / arguments (strong-weak) / conclusions / course of action
- [ ] Cause & effect; assertion–reason; decision-making / eligibility
- [ ] Clocks & calendars
- [ ] Data sufficiency (both quant and reasoning styles)

### D. Non-verbal / abstract
- [ ] Figure series, figure analogy, figure classification
- [ ] Pattern / rule detection (inductive)
- [ ] Mirror & water images; paper folding & cutting
- [ ] Cubes & dice; embedded & grouping of figures

### E. Verbal ability
- [ ] Reading comprehension: main idea, inference, tone, vocab-in-context, detail — 300–900-word passages
- [ ] Grammar: subject–verb, tense, pronoun, parallelism, modifiers, prepositions, articles
- [ ] Error spotting; sentence correction / improvement
- [ ] Sentence completion; single & double fill-in-the-blanks; para completion
- [ ] Cloze test
- [ ] Para jumbles (4- and 6-sentence, anchored)
- [ ] Vocabulary: 300–500 high-frequency words; synonyms/antonyms; one-word substitution; idioms & phrases
- [ ] Verbal analogy
- [ ] Critical reasoning: strengthen, weaken, assumption, conclusion, inference, flaw

### F. Data interpretation
- [ ] Table, bar, line, pie, mixed, caselet, missing-data
- [ ] Radar / bubble / stacked
- [ ] Approximation & elimination on DI
- [ ] Data-driven logical reasoning (DI + arrangement)
- [ ] Multi-set papers under 8–10 min/set

### G. Civil / HWRE core aptitude
- [ ] Unit conversions & dimensional analysis (cumec ↔ MLD ↔ lpcd, SI/FPS)
- [ ] Quantity-estimation arithmetic (BOQ %, wastage, bulking, mix ratios)
- [ ] Percentages in compaction, moisture, voids, efficiency
- [ ] Earthwork volumes (trapezoidal, prismoidal); area by coordinates
- [ ] Discharge Q = A·V; reservoir fill/empty time
- [ ] Slope / gradient / % grade / camber
- [ ] Engineering economics: depreciation (SL & WDV), EMI, B/C ratio, simple NPV
- [ ] Return period T = 1/p; risk = 1 − (1 − 1/T)ⁿ; exceedance probability
- [ ] Interpreting hydrographs, rating curves, stress–strain, S–N plots

### H. Engineering mathematics screening (keep separate from general aptitude)
- [ ] Matrices, determinants, eigenvalues
- [ ] Calculus: limits, derivatives, maxima–minima, definite integrals
- [ ] Vector calculus: gradient, divergence, curl (CFD)
- [ ] Numerical methods: Newton–Raphson, trapezoidal / Simpson, Gauss elimination
- [ ] Probability distributions, regression, hypothesis testing
- [ ] Fluid-mechanics screening: Bernoulli, continuity, Reynolds, Manning, pump power, Buckingham π

### I. Test-craft
- [ ] Know the pattern of every company you've applied to (sections, #Q, time, negative marking, sectional cutoff, adaptive?, calculator?)
- [ ] Question-selection: skip in ≤ 10 s anything you can't crack in 90 s
- [ ] Sectional time budgeting; when to guess (only if no negative marking)
- [ ] Error log maintained; wrong questions reattempted at 1 / 3 / 7 days
- [ ] ≥ 6 full mocks done under strict timing with analysis

### J. Score gates (from full-length mocks)
- [ ] Plain quant+verbal screen (TCS-style): ≥ 75%
- [ ] eLitmus / AMCAT style (with negative marking): ≥ 70th–80th percentile equivalent
- [ ] Consulting numerical + verbal: ≥ 80%
- [ ] High-difficulty IIT PPO-style: ≥ 60% (these are meant to be hard)

---

## 10. Test Specifications

All tests: no calculator unless the company allows one; maintain an error log; review every wrong + every guessed-right question. Benchmarks are for a prepared IITK candidate and assume no negative marking unless stated.

### 10.1 — 30-minute Aptitude Test
| Spec | Value |
|---|---|
| Questions | 25 |
| Distribution | Quant 10 · Reasoning 8 · DI 4 · Verbal 3 |
| Difficulty | 10 Easy · 11 Medium · 4 Hard |
| Time | 30 min (~72 s/Q) |
| Purpose | Daily warm-up / quick diagnostic |
| Benchmark | Strong ≥ 20/25 · Average 15–19 · Weak < 15 |

### 10.2 — 60-minute Aptitude Test
| Spec | Value |
|---|---|
| Questions | 50 |
| Distribution | Quant 18 · Reasoning 15 · DI 9 · Verbal 8 |
| Difficulty | 15 Easy · 22 Medium · 13 Hard |
| Time | 60 min (~72 s/Q) |
| Purpose | Standard mock (this is what the existing mock should become, fixed) |
| Benchmark | Placement-ready ≥ 40/50 · Strong 34–39 · Needs work < 30 |

### 10.3 — 90-minute Full Placement Test
| Spec | Value |
|---|---|
| Questions | 75 |
| Distribution | Quant 25 · Reasoning 20 · DI 15 · Verbal 15 |
| Difficulty | 20 Easy · 35 Medium · 20 Hard |
| Time | 90 min; **sectional soft limits** Q 32 / R 25 / DI 20 / V 13 min |
| Purpose | Full simulation incl. stamina & section switching |
| Benchmark | Comprehensive ≥ 60/75 · Strong 50–59 · Intermediate 40–49 |

### 10.4 — Quant-Only Test
| Spec | Value |
|---|---|
| Questions | 30 |
| Distribution | Arithmetic 14 · Algebra/Number 8 · Geometry/Mensuration 4 · P&C/Probability 4 |
| Difficulty | 9 Easy · 13 Medium · 8 Hard |
| Time | 35 min |
| Benchmark | Strong ≥ 24/30 · Average 18–23 |

### 10.5 — Reasoning-Only Test
| Spec | Value |
|---|---|
| Questions | 30 |
| Distribution | Series/Analogy/Classification 8 · Arrangements & puzzles 9 · Syllogism/Statements 7 · Coding/Blood/Direction/Ranking 6 |
| Difficulty | 8 Easy · 14 Medium · 8 Hard |
| Time | 35 min |
| Benchmark | Strong ≥ 24/30 · Average 18–23 |

### 10.6 — Verbal-Only Test
| Spec | Value |
|---|---|
| Questions | 30 |
| Distribution | RC 10 (2 passages) · Grammar/Error/Correction 8 · Vocab/Synonym/Antonym/One-word 6 · Jumbles/Cloze/Completion 6 |
| Difficulty | 9 Easy · 14 Medium · 7 Hard |
| Time | 30 min |
| Benchmark | Strong ≥ 24/30 · Average 18–23 |

### 10.7 — Data Interpretation Test
| Spec | Value |
|---|---|
| Questions | 20 (4 sets of 5: table, bar+line, pie, caselet/missing-data) |
| Difficulty | 5 Easy · 9 Medium · 6 Hard |
| Time | 25 min (~6 min/set) |
| Benchmark | Strong ≥ 16/20 · Average 11–15 |

### 10.8 — High-Difficulty IIT Placement Test
| Spec | Value |
|---|---|
| Questions | 40 |
| Distribution | Quant 16 · Reasoning 12 · DI 8 · Verbal (critical reasoning heavy) 4 |
| Difficulty | 0 Easy · 14 Medium · 26 Hard/Very-Hard |
| Time | 55 min (deliberately tight) · **negative marking −0.25** |
| Purpose | PPO shortlists, consulting/analytics/quant screens, eLitmus-tier |
| Benchmark | ≥ 24/40 is strong · ≥ 30/40 is excellent |

### 10.9 — Core-Engineering Placement Aptitude Test
| Spec | Value |
|---|---|
| Questions | 40 |
| Distribution | General quant 12 · Logical/DI 8 · **Civil-core aptitude 12** (units, estimation, earthwork, economics, return period) · **Engineering-maths/fluid screening 8** |
| Difficulty | 8 Easy · 20 Medium · 12 Hard |
| Time | 50 min |
| Purpose | L&T / Tata Projects / AECOM / PSU-style tests that mix aptitude with technical MCQ |
| Benchmark | Strong ≥ 30/40 · Average 22–29 |

---

## 11. Actionable Improvement Plan (prioritised)

### Phase 0 — Trust repair (do first; ~1–2 days, no new topics)
1. **Re-key the degenerate tests.** `probability-test`, `si-ci-test`, `profit-loss-test`, `permutations-combinations-test`, `series-test`, `speed-time-distance-test` (+ `time-work-test`, `averages-test`, `ratio-proportion-test`): re-solve every question, place the correct answer in a randomised position, add a worked solution line per question.
2. **Fix the broken items** listed in the Appendix — the mock (Q14, Q20, Q22, Q27, Q29, Q30), `di/tables-caselets.md` (Q7, Q10, Q13–15), `reasoning/coding-decoding.md` (Ex.1, Ex.4), `reasoning/puzzles-scheduling.md` (Ex.2, practice Q6–10), `reasoning/order-ranking.md` (Ex.3, Placement Q3), `tests/seating-arrangement-test.md` (Q1, Q6, Q7–10), `tests/probability-test.md` (Q13). Strip **all** "Hmm / let me recalculate / not in options" text.
3. **Fix the sphere-volume error** in `FORMULA_SHEET.md` and `quant/mensuration.md`.
4. Add a short "Known limitations / last verified" note to `aptitude/README.md` and correct `_SYSTEM/APTITUDE_COMPLETENESS_MATRIX.md` so it stops claiming 9/10 across the board.

### Phase 1 — Complete what's half-built (~1 week)
5. **Add answer keys + 1-line solutions to every unanswered practice block** in `quantitative/*` and `logical_reasoning/*` (~400 solutions). This alone moves the folder from "notes" to "practice."
6. Convert `verbal/critical-reasoning.md` practice stubs into full items; fix `verbal/para-jumbles.md` trivial jumbles; fix "perillous".
7. **De-duplicate DI:** author 10 new unique datasets; repoint the mock and `di-test` to fresh data.
8. Rename folders to the §8 scheme (`quant/`→`quantitative/`, `reasoning/`→`logical_reasoning/`, `di/`→`data_interpretation/`, `tests/`→`timed_tests/`, `mocks/`→`mixed_tests/`) and update links. Retire `aptitude/` (redirect its README to `aptitude/`).

### Phase 2 — Fill the CRITICAL / HIGH domain gaps (~2–3 weeks)
9. New quant modules: `algebra-equations`, `surds-indices-logarithms`, `geometry`, `coordinate-geometry` (section), `set-theory-venn`, `calculation-speed-drills`; split `trains` and `boats-streams`.
10. New reasoning modules: `analogy`, `classification`, `statement-assumption-argument-conclusion`, `logical-venn`, `coded-inequalities-symbols`, `cause-effect-assertion-reason`, `decision-making-eligibility`.
11. New `non_verbal/` folder (6 files).
12. New verbal: `cloze-test`, `sentence-correction-improvement`, `synonyms-antonyms-bank`, `one-word-substitution`, `idioms-phrases` (port from root `Aptitude/`), `verbal-analogy`, `rc-passage-bank` (12–15 passages), expand `vocabulary` to 300–500 words + SRS list.
13. New `data_interpretation/` additions: `missing-data-di`, `data-driven-reasoning`, `approximation-drills`, `di-set-bank` (25–30 sets).
14. New `company_patterns/` folder — start with the platforms/companies most relevant to this candidate: **L&T / core-EPC**, **TCS NQT**, **eLitmus**, **AMCAT**, **consulting (McKinsey/BCG/Bain/ZS)**, **analytics (Accenture/Axtria/Fractal)**, **PSU/GATE**. Consolidate the scattered "online aptitude" notes from `prep/company-profiles/*`. Label evidence confidence; add "verify with placement cell."

### Phase 3 — Civil-core, eng-maths, and the full test suite (~2 weeks)
15. New `civil_core_aptitude/` folder (7 files, ~50 drilled questions).
16. New `engineering_mathematics/` folder (MCQ screening, cross-linked to `core/gate/`; do not duplicate theory).
17. Build the 9 tests in §10 + `timed_tests/sectional-*` + rebuild `full-placement-mock-1` and author Mocks 2–8 + `mixed_tests/pattern-mocks/*`.
18. New `previous_style_questions/` folder (clearly disclaimered) and `resources/` folder (book list, sites, flashcards).

### Phase 4 — Polish
19. Extend `probability` (conditional/Bayes), `progressions` (HP/AGP), `permutations-combinations` (restricted/circular).
20. Add flashcard exports (`resources/flashcards.md`) for vocab, formulas, traps.
21. Add a `quality_check.py` rule that flags any test whose answer key is >60% one letter, and any solution block containing "let me recalculate / not in options / Hmm".

### Effort estimate
| Phase | Scope | Rough effort |
|---|---|---|
| 0 | Trust repair | 1–2 days |
| 1 | Complete half-built | ~1 week |
| 2 | CRITICAL/HIGH gaps | 2–3 weeks |
| 3 | Civil-core + eng-maths + tests | ~2 weeks |
| 4 | Polish | few days |

**If time is short, Phases 0 + 1 + item 14 (company patterns) deliver ~70% of the placement value.**

---

## Appendix — Broken-Item Triage List

| File | Item | Problem | Fix |
|---|---|---|---|
| `mocks/full-placement-mock-1.md` | Q14 | Correct answer (8) not in options; solution says so | Rewrite options to include 8; key = that option |
| " | Q20 | Coding "TIGER" — solution: "Closest is 58… approximately" | Set rule = position sum → 59; put 59 in options |
| " | Q22 | Symbol substitution — "options seem wrong… set answer as A" | Recompute (8×4 + 6÷3 − 2 = 32); fix options |
| " | Q27 | Key = A ("5 km"); solution concludes "3 km" (B) twice | Key = B; verify path |
| " | Q29 | "Without drawing… Answer: A" — no solution | Supply full constraints + solution or replace |
| " | Q30 | "answer is likely 63 (common in such tests)" | Define a real coding rule; solve it |
| `di/tables-caselets.md` | Q7 | "Answer: B) 73.3" → "Answer corrected: A) 72.5" | Keep 72.5; delete scratchpad |
| " | Q10 | "Answer: B) Farhan" → "corrected: A) Beena" | Keep Beena; delete scratchpad |
| " | Q13 | 106.5 not in options; rationalised as a feature | Fix options; Q14/Q15 depend on it — re-verify |
| `reasoning/coding-decoding.md` | Ex.1 | "CAT → DBT" inconsistent with stated "+1" rule | Use a consistent example (e.g. CAT→DBU) |
| " | Ex.4 | BRIGHT=54 — full failed-derivation, "likely 63" | Define rule (e.g. Σ positions − n); solve |
| " | Ex.2 | "TIGER = 59" contradicts mock's 58 | Reconcile to 59 |
| `reasoning/puzzles-scheduling.md` | Ex.2 | "the puzzle is flawed. I'll present a corrected version." | Replace with a clean, fully-specified puzzle |
| " | Practice Q6–Q10 | Placeholders ("… with multiple constraints") | Write full puzzles with constraints + answers |
| `reasoning/order-ranking.md` | Ex.3 | "Let me recalculate… Hmm" scratchpad | Clean solution |
| " | Placement Q3 | Labelled "C) 9", working ends "Answer: B) 8" | Verify; single consistent answer |
| `tests/seating-arrangement-test.md` | Q1 | Key "D", explanation "Answer: A" | Reconcile |
| " | Q6 | Key "A", explanation ends "D"; question under-specified (4 people, 5 seats) | Rewrite question + key |
| " | Q7–Q10 | "Various clues" / "multiple constraints" — none given | Write full questions |
| `tests/probability-test.md` | Q13 | "Not in options… Closest is 5/6… A (closest)" | Fix options (13/18); this is also an all-"A" test |
| All-"A" tests | whole key | 15/15 = A | Re-key with randomised positions + worked solutions |
| `FORMULA_SHEET.md`, `quant/mensuration.md` | Sphere volume | `¾πr³` written; correct is `4⁄3 πr³` | Correct both |
| `verbal/para-jumbles.md` | Q6, Q8, Q9, Q10, Q12 | "Jumble" answer = already-ordered A-B-C-D-E-F | Replace with genuine jumbles |
