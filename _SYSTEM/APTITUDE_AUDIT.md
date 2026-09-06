# Aptitude System Audit

> Full audit of all aptitude-related content across the repository.
> Classification: `EMPTY` · `HEADINGS_ONLY` · `RESOURCE_ONLY` · `PARTIAL` · `GOOD` · `PLACEMENT_READY`
> Audit date: 2026-09-05

---

## 1. Audit Scope

Three aptitude sources exist in the workspace. This audit covers all of them and establishes the **canonical** source for the rebuild.

| Source | Path | Role |
|:-------|:-----|:-----|
| **Aptitude/** (root) | `Aptitude/` | 34-topic study kit (richest per-topic content) |
| **Aptitude-For-Placements/** | `Aptitude-For-Placements/` | ~60 single solved problems (no `.md` ext) |
| **Canonical repo** | `DKS_IITK_Civil_HWRE_Placement_2026/non-core/aptitude/` | Condensed topic modules + shortcuts + reasoning/verbal |

**Canonical decision:** The rebuild lives in `DKS_IITK_Civil_HWRE_Placement_2026/aptitude/` (new canonical hub). The root `Aptitude/` files are treated as a **reference source** for high-quality per-topic content. `Aptitude-For-Placements/` is a **practice bank** of solved examples.

---

## 2. File-by-File Audit

### 2.1 Root `Aptitude/` — Quantitative Aptitude

| Path | Purpose | Topic | Study? | Practice? | Solutions? | Difficulty? | Timed? | Quality | Duplicate | Missing Content | Required Fix |
|:-----|:--------|:------|:------:|:---------:|:----------:|:-----------:|:------:|:-------:|:---------|:----------------|:-------------|
| `Aptitude/Number_System.md` | Study + 10 Q | Number System | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | Duplicates non-core number-system | Difficulty labels, timed set, traps, revision | Upgrade to 12-section template |
| `Aptitude/HCF_LCM_Divisibility.md` | Study + 10 Q | HCF/LCM | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Difficulty, traps, revision | Upgrade |
| `Aptitude/Simplification.md` | Study + 10 Q | Simplification | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Difficulty, traps | Upgrade |
| `Aptitude/Averages_Mixtures.md` | Study + 10 Q | Averages/Mixtures | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | Duplicates non-core averages | Difficulty, traps, revision | Upgrade |
| `Aptitude/Percentages.md` | Study + 10 Q | Percentages | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | Duplicates non-core percentages | Difficulty, traps, revision | Upgrade |
| `Aptitude/Ratio_Proportion.md` | Study + 10 Q | Ratio/Proportion | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | Duplicates non-core ratio | Difficulty, traps | Upgrade |
| `Aptitude/Profit_Loss_Discount.md` | Study + 10 Q | Profit/Loss | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | Duplicates non-core P&L | Difficulty, traps | Upgrade |
| `Aptitude/Simple_Compound_Interest.md` | Study + 10 Q | SI/CI | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Difficulty, traps | Upgrade |
| `Aptitude/Time_Work.md` | Study + 10 Q | Time & Work | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | Duplicates non-core time-work | Difficulty, traps | Upgrade |
| `Aptitude/Speed_Time_Distance.md` | Study + 10 Q | TSD | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | Duplicates non-core TSD | Difficulty, traps | Upgrade |
| `Aptitude/Problems_on_Ages.md` | Study + 10 Q | Ages | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | Duplicates non-core ages | Difficulty, traps | Upgrade |
| `Aptitude/Progressions.md` | Study + 10 Q | Progressions | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Difficulty, traps | Upgrade |
| `Aptitude/Permutations_Combinations.md` | Study + 10 Q | P&C | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | Duplicates non-core P&C | Difficulty, traps | Upgrade |
| `Aptitude/Probability.md` | Study + 10 Q | Probability | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | Duplicates non-core probability | Difficulty, traps | Upgrade |
| `Aptitude/Mensuration.md` | Study + 10 Q | Mensuration | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Difficulty, traps | Upgrade |

### 2.2 Root `Aptitude/` — Logical Reasoning

| Path | Purpose | Topic | Study? | Practice? | Solutions? | Difficulty? | Timed? | Quality | Duplicate | Missing Content | Required Fix |
|:-----|:--------|:------|:------:|:---------:|:----------:|:-----------:|:------:|:-------:|:---------|:----------------|:-------------|
| `Aptitude/Blood_Relations.md` | Study + 10 Q | Blood Relations | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Difficulty, traps | Upgrade |
| `Aptitude/Direction_Sense.md` | Study + 10 Q | Direction Sense | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Difficulty, traps | Upgrade |
| `Aptitude/Coding_Decoding.md` | Study + 10 Q | Coding-Decoding | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Difficulty, traps | Upgrade |
| `Aptitude/Order_Ranking.md` | Study + 10 Q | Order/Ranking | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Difficulty, traps | Upgrade |
| `Aptitude/Seating_Arrangement.md` | Study + 10 Q | Seating | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Difficulty, traps | Upgrade |
| `Aptitude/Puzzles_Scheduling.md` | Study + 10 Q | Puzzles | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Difficulty, traps | Upgrade |
| `Aptitude/Syllogism.md` | Study + 10 Q | Syllogism | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Difficulty, traps | Upgrade |
| `Aptitude/Input_Output.md` | Study + 10 Q | Input/Output | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Difficulty, traps | Upgrade |
| `Aptitude/Clocks_Calendars.md` | Study + 10 Q | Clocks/Calendars | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Difficulty, traps | Upgrade |

### 2.3 Root `Aptitude/` — Data Interpretation & Verbal

| Path | Purpose | Topic | Study? | Practice? | Solutions? | Difficulty? | Timed? | Quality | Duplicate | Missing Content | Required Fix |
|:-----|:--------|:------|:------:|:---------:|:----------:|:-----------:|:------:|:-------:|:---------|:----------------|:-------------|
| `Aptitude/Tables_Caselets.md` | Study + 10 Q | Tables/Caselets | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Set-based DI, difficulty | Upgrade to DI sets |
| `Aptitude/Bar_Line_Graphs.md` | Study + 10 Q | Bar/Line | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Set-based DI, difficulty | Upgrade to DI sets |
| `Aptitude/Pie_Charts.md` | Study + 10 Q | Pie Charts | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Set-based DI, difficulty | Upgrade to DI sets |
| `Aptitude/Data_Sufficiency.md` | Study + 10 Q | Data Sufficiency | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Difficulty, traps | Upgrade |
| `Aptitude/Grammar_Error_Spotting.md` | Study + 10 Q | Grammar | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Difficulty, traps | Upgrade |
| `Aptitude/Idioms_Phrases.md` | Study + 10 Q | Idioms | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Difficulty, traps | Upgrade |
| `Aptitude/Para_Jumbles.md` | Study + 10 Q | Para Jumbles | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Difficulty, traps | Upgrade |
| `Aptitude/Reading_Comprehension.md` | Study + 10 Q | RC | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Difficulty, traps | Upgrade |
| `Aptitude/Sentence_Completion.md` | Study + 10 Q | Sentence Completion | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Difficulty, traps | Upgrade |
| `Aptitude/Vocabulary.md` | Study + 10 Q | Vocabulary | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Difficulty, traps | Upgrade |
| `Aptitude/README.md` | Index | All | ✅ | — | — | — | — | GOOD | — | No roadmap/role matrix links | Link to new system |

### 2.4 `Aptitude-For-Placements/` — Practice Bank

| Path | Purpose | Topic | Study? | Practice? | Solutions? | Difficulty? | Timed? | Quality | Duplicate | Missing Content | Required Fix |
|:-----|:--------|:------|:------:|:---------:|:----------:|:-----------:|:------:|:-------:|:---------|:----------------|:-------------|
| `Aptitude-For-Placements/Averages/Averages-1..7` | 7 solved examples | Averages | ❌ | ✅ | ✅ | ❌ | ❌ | PARTIAL | Duplicates Aptitude/Averages | No study material, no difficulty | Reference bank only |
| `Aptitude-For-Placements/Number System/Number System-1..6` | 6 solved examples | Number System | ❌ | ✅ | ✅ | ❌ | ❌ | PARTIAL | Duplicates Aptitude/Number_System | No study material | Reference bank only |
| `Aptitude-For-Placements/Partnership/Partnership-1..8` | 8 solved examples | Partnership | ❌ | ✅ | ✅ | ❌ | ❌ | PARTIAL | — | No study material | Reference bank only |
| `Aptitude-For-Placements/Percentage/Percentage-1..7` | 7 solved examples | Percentage | ❌ | ✅ | ✅ | ❌ | ❌ | PARTIAL | Duplicates Aptitude/Percentages | No study material | Reference bank only |
| `Aptitude-For-Placements/Probability/Probability-1..7` | 7 solved examples | Probability | ❌ | ✅ | ✅ | ❌ | ❌ | PARTIAL | Duplicates Aptitude/Probability | No study material | Reference bank only |
| `Aptitude-For-Placements/Problem on Ages/...-1..6` | 6 solved examples | Ages | ❌ | ✅ | ✅ | ❌ | ❌ | PARTIAL | Duplicates Aptitude/Problems_on_Ages | No study material | Reference bank only |
| `Aptitude-For-Placements/Problems on Train/...-1..7` | 7 solved examples | Trains | ❌ | ✅ | ✅ | ❌ | ❌ | PARTIAL | Duplicates Aptitude/Speed_Time_Distance | No study material | Reference bank only |
| `Aptitude-For-Placements/Profit & Loss/...-1..7` | 7 solved examples | P&L | ❌ | ✅ | ✅ | ❌ | ❌ | PARTIAL | Duplicates Aptitude/Profit_Loss | No study material | Reference bank only |
| `Aptitude-For-Placements/Ratio and Proportion/...-1..5` | 5 solved examples | Ratio | ❌ | ✅ | ✅ | ❌ | ❌ | PARTIAL | Duplicates Aptitude/Ratio | No study material | Reference bank only |
| `Aptitude-For-Placements/Time and Work/...-1..4` | 4 solved examples | Time & Work | ❌ | ✅ | ✅ | ❌ | ❌ | PARTIAL | Duplicates Aptitude/Time_Work | No study material | Reference bank only |
| `Aptitude-For-Placements/Time, Speed and Distance/...-1..7` | 7 solved examples | TSD | ❌ | ✅ | ✅ | ❌ | ❌ | PARTIAL | Duplicates Aptitude/Speed_Time_Distance | No study material | Reference bank only |
| `Aptitude-For-Placements/README.md` | Index | All | — | — | — | — | — | RESOURCE_ONLY | — | No navigation to system | Link to canonical hub |

### 2.5 Canonical `non-core/aptitude/` — Condensed Modules

| Path | Purpose | Topic | Study? | Practice? | Solutions? | Difficulty? | Timed? | Quality | Duplicate | Missing Content | Required Fix |
|:-----|:--------|:------|:------:|:---------:|:----------:|:-----------:|:------:|:-------:|:---------|:----------------|:-------------|
| `non-core/aptitude/README.md` | Index | All | — | — | — | — | — | GOOD | — | No roadmap/role matrix | Link to new system |
| `non-core/aptitude/quantitative/aptitude-basics.md` | Overview + 15 examples | All | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Difficulty, traps | Keep as overview |
| `non-core/aptitude/quantitative/number-system.md` | Study + 10 Q | Number System | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | Duplicates Aptitude/Number_System | Difficulty, traps | Upgrade |
| `non-core/aptitude/quantitative/percentages.md` | Study + 15 Q | Percentages | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | Duplicates Aptitude/Percentages | Difficulty, traps | Upgrade |
| `non-core/aptitude/quantitative/ratio-proportion.md` | Study + 10 Q | Ratio | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | Duplicates Aptitude/Ratio | Difficulty, traps | Upgrade |
| `non-core/aptitude/quantitative/profit-loss-discount.md` | Study + 10 Q | P&L | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | Duplicates Aptitude/Profit_Loss | Difficulty, traps | Upgrade |
| `non-core/aptitude/quantitative/time-work.md` | Study + 10 Q | Time & Work | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | Duplicates Aptitude/Time_Work | Difficulty, traps | Upgrade |
| `non-core/aptitude/quantitative/speed-time-distance.md` | Study + 10 Q | TSD | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | Duplicates Aptitude/Speed_Time_Distance | Difficulty, traps | Upgrade |
| `non-core/aptitude/quantitative/averages.md` | Study + 10 Q | Averages | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | Duplicates Aptitude/Averages | Difficulty, traps | Upgrade |
| `non-core/aptitude/quantitative/partnership.md` | Study + 10 Q | Partnership | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Difficulty, traps | Upgrade |
| `non-core/aptitude/quantitative/permutations-combinations.md` | Study + 10 Q | P&C | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | Duplicates Aptitude/P&C | Difficulty, traps | Upgrade |
| `non-core/aptitude/quantitative/probability.md` | Study + 10 Q | Probability | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | Duplicates Aptitude/Probability | Difficulty, traps | Upgrade |
| `non-core/aptitude/quantitative/problems-on-ages.md` | Study + 10 Q | Ages | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | Duplicates Aptitude/Ages | Difficulty, traps | Upgrade |
| `non-core/aptitude/quantitative/problems-on-train.md` | Study + 10 Q | Trains | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | Duplicates Aptitude/TSD | Difficulty, traps | Upgrade |
| `non-core/aptitude/quantitative/data-interpretation.md` | Study + 10 Q | DI | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Set-based DI | Upgrade to DI sets |
| `non-core/aptitude/logical_reasoning/reasoning-practice.md` | Practice | Reasoning | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Difficulty, traps | Upgrade |
| `non-core/aptitude/verbal/verbal-ability.md` | Practice | Verbal | ✅ | ✅ | ✅ | ❌ | ❌ | GOOD | — | Difficulty, traps | Upgrade |
| `non-core/aptitude/shortcuts/aptitude-shortcuts.md` | 50+ shortcuts | All | ✅ | — | — | — | — | GOOD | — | Derived explanations | Keep as shortcut reference |

---

## 3. Classification Summary

| Classification | Count | Files |
|:---------------|:-----:|:------|
| EMPTY | 0 | — |
| HEADINGS_ONLY | 0 | — |
| RESOURCE_ONLY | 1 | `Aptitude-For-Placements/README.md` |
| PARTIAL | 11 | All `Aptitude-For-Placements/*` topic folders |
| GOOD | 55 | All `Aptitude/*.md` + `non-core/aptitude/*` |
| PLACEMENT_READY | 0 | — |

**No file is currently PLACEMENT_READY.** Every topic lacks the full system layer (difficulty, timed tests, traps, revision, role matrix).

---

## 4. System-Level Gaps (Across All Sources)

| # | Gap | Requirement | Severity |
|:--|:----|:------------|:--------:|
| G1 | No `_SYSTEM/APTITUDE_AUDIT.md` | §2 | P0 |
| G2 | No `_SYSTEM/APTITUDE_STATE.md` | §32 | P0 |
| G3 | No `_SYSTEM/APTITUDE_COMPLETENESS_MATRIX.md` | §30 | P0 |
| G4 | No `APTITUDE_ROADMAP.md` | §23 | P0 |
| G5 | No `APTITUDE_ROLE_MATRIX.md` | §22 | P0 |
| G6 | No `APTITUDE_7_14_30_DAY_PLAN.md` | §24 | P0 |
| G7 | No `DAILY_APTITUDE_PLAN.md` | §25 | P0 |
| G8 | No `APTITUDE_FORMULA_SHEET.md` | §18 | P0 |
| G9 | No `APTITUDE_RAPID_REVISION.md` | §19 | P0 |
| G10 | No `APTITUDE_ERROR_LOG.md` | §16 | P0 |
| G11 | No timed topic tests | §13 | P0 |
| G12 | No full mock tests | §14 | P0 |
| G13 | No difficulty system on questions | §9 | P0 |
| G14 | No common traps section per topic | §7 | P1 |
| G15 | No role-universality navigation | §22/§29 | P1 |
| G16 | Duplication across 3 sources | §28 | P1 |
| G17 | No canonical navigation hub (≤2 clicks) | §29 | P0 |

---

## 5. Priority Fix Plan

**P0 (build now):** G1–G13, G17 — the entire system layer + difficulty + tests + mocks.

**P1 (build after P0):** G14–G16 — traps per topic, role matrix navigation, deduplication via canonical hub.

**P2 (defer):** Advanced/rare placement topics (coordinate geometry, boats & streams deep-dive, etc.) — only if placement data supports.

---

## 6. Canonical Structure (Target)

```
aptitude/                          ← NEW canonical hub
├── README.md                      ← Navigation (≤2 clicks)
├── ROADMAP.md
├── ROLE_MATRIX.md
├── 7_14_30_DAY_PLAN.md
├── DAILY_PLAN.md
├── FORMULA_SHEET.md
├── RAPID_REVISION.md
├── ERROR_LOG.md
├── quant/                         ← P0 topics upgraded to 12-section template
├── reasoning/
├── di/
├── verbal/
├── tests/                         ← Topic tests
└── mocks/                         ← Full mock tests
```

---

*Audit complete. See `_SYSTEM/APTITUDE_STATE.md` for build progress tracking.*
