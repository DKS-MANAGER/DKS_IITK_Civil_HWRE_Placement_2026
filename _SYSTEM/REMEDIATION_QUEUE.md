# REMEDIATION_QUEUE.md — Prioritized Gap Fixes

**Generated:** 2026-09-04
**Method:** CONTENT_MATRIX.md scoring + REPO_MAP.md depth analysis

## P0 — Critical (Score < 5, blocks student preparation)

| # | Priority | Unit | Problem | Required Fix | Status |
|---|----------|------|---------|--------------|--------|
| 1 | P0 | `core/transportation/transportation-software.md` | 245 words, no examples/MCQs/interview/revision | Enrich with civil software coverage (MS Project, Primavera, AutoCAD Civil, STAAD, etc.) + examples + interview Qs | PENDING |
| 2 | P0 | `prep/behavioral/self_intro/self-introduction.md` | 3.5/10, no conceptQ/MCQs/interview/revision/links | Add self-interview framework, role-specific variants, follow-ups, common mistakes | PENDING |
| 3 | P0 | `non-core/analytics/technical-stack.md` | 4.5/10, no examples/MCQs/interview/revision/links | Add interview-relevant Qs, tool comparison tables, project examples | PENDING |
| 4 | P0 | `non-core/consulting/case-frameworks.md` | 4.0/10, no examples/conceptQ/MCQs/interview/revision | Add worked case examples, framework application guides, interview prep | PENDING |
| 5 | P0 | `non-core/consulting/case-bank.md` | 4.0/10, no examples/conceptQ/MCQs/interview/revision | Add solved cases with frameworks, practice cases, interview format | PENDING |

## P1 — High Value (Score 5-6, significant gaps)

| # | Priority | Unit | Problem | Required Fix | Status |
|---|----------|------|---------|--------------|--------|
| 6 | P1 | `core/fundamentals/civil-engineering-foundations.md` | 5.0/10, no examples/conceptQ/MCQs/interview | Add solved examples, conceptual Qs, interview prep | PENDING |
| 7 | P1 | `prep/interview/quick-revision-system.md` | 5.0/10, thin on content | Enrich with actual revision content per subject | PENDING |
| 8 | P1 | `software-and-tech/deep-dives/hec-ras-walkthrough.md` | 5.0/10, needs examples/interview/revision | Add worked examples, interview Qs, quick reference | PENDING |
| 9 | P1 | `non-core/consulting/consulting-overview.md` | 5.5/10, needs examples/conceptQ/MCQs | Add more depth, case examples, test prep | PENDING |
| 10 | P1 | `non-core/product-management/pm-overview.md` | 5.5/10, needs conceptQ/MCQs/interview/revision | Add PM interview prep, metrics frameworks, cases | PENDING |
| 11 | P1 | `non-core/analytics/non-core-prep.md` | 6.0/10, needs conceptQ/MCQs/interview | Add practice questions, interview prep | PENDING |
| 12 | P1 | `non-core/aptitude/quantitative/aptitude-basics.md` | 6.0/10, needs conceptQ/MCQs/interview | Add more MCQs, speed tricks, test format | PENDING |
| 13 | P1 | `core/gate/civil/gate-civil-notes.md` | 6.5/10, needs conceptQ/interview | Add conceptual deep-dive questions, interview mapping | PENDING |

## P2 — Enhancement (Score 7-7.5, minor gaps)

| # | Priority | Unit | Problem | Required Fix | Status |
|---|----------|------|---------|--------------|--------|
| 14 | P2 | `core/gate/formulas/gate-civil-formulas.md` | 7.5/10, needs conceptQ/interview | Add application examples | PENDING |
| 15 | P2 | `core/gate/practice/gate-civil-practice.md` | 7.5/10, needs conceptQ/interview | Add explanation depth | PENDING |
| 16 | P2 | `core/gate/revision_notes/gate-civil-revision.md` | 7.5/10, needs conceptQ/interview | Add key insights | PENDING |
| 17 | P2 | `prep/behavioral/behavioral-interview-guide.md` | 7.0/10, needs examples/revision | Add more example answers, quick revision | PENDING |
| 18 | P2 | `non-core/consulting/case-frameworks.md` | 7.0/10 (if counted) | Add worked examples | PENDING |
| 19 | P2 | `software-and-tech/deep-dives/openfoam-case-study.md` | 6.0/10 | Add interview Qs, revision | PENDING |
| 20 | P2 | `non-core/product-management/pm-metrics-strategy.md` | Not yet scored | Audit & enrich | PENDING |
| 21 | P2 | `non-core/product-management/product-sense.md` | Not yet scored | Audit & enrich | PENDING |

## P3 — Systemic Gaps (Cross-cutting)

| # | Priority | Unit | Problem | Required Fix | Status |
|---|----------|------|---------|--------------|--------|
| 22 | P3 | `questions/` directory | Only 1 file (README.md) | Need per-subject question banks or link existing Qs | PENDING |
| 23 | P3 | Company profiles (18 files) | Many < 500 words | Enrich thin company profiles | PENDING |
| 24 | P3 | Subject-level rapid revision | Missing for most core subjects | Create RAPID_REVISION.md per core subject | PENDING |
| 25 | P3 | Subject-level formula sheets | Only GATE has dedicated formula file | Add formula quick-reference to each core subject | PENDING |
| 26 | P3 | Navigation rebuild | After content fixes, rebuild indexes | Update README, indexes, cross-links | PENDING |
| 27 | P3 | `_SYSTEM/MASTER_COMPLETENESS.md` | Does not exist | Create final completeness dashboard | PENDING |

## Execution Strategy

1. Fix P0 items (5 files) — estimated 5 implementations
2. Fix P1 items (8 files) — estimated 8 implementations
3. Fix P2 items (8 files) — estimated 5 implementations
4. Fix P3 items (6 systemic tasks) — estimated 6 implementations
5. Final navigation rebuild + link validation
6. Quality gate + completeness check

## Rules
- Read each file BEFORE modifying
- One logical unit at a time
- Update AUDIT_STATE.md after each unit
- Do not overwrite good content — extend it
- Never create empty placeholders
