# Core Remediation Queue

> **Purpose:** Prioritized gap list for `core/`. Fix order: **P0 → P1 → P2 → P3**.
> **Priority:** P0 = no study material / broken path / missing critical interview · P1 = missing practice/tests/weak role strategy · P2 = missing revision/navigation · P3 = formatting/cleanup

---

## P0 — Critical (No study material / broken path / missing interview)

| # | Item | Track | Gap | Action | Status |
|---|------|-------|-----|--------|--------|
| 1 | `core/_SYSTEM/` layer | All | No tracking layer | Create CORE_REPO_MAP, TRACK_INVENTORY, ROLE_INVENTORY, CONTENT_MATRIX, REQUIRED_FILES, REMEDIATION_QUEUE, AUDIT_STATE | ✅ DONE |
| 2 | Design Engineer role | RCC/Steel | No role plan, practice, test, interview | Create `rcc/role-study-plan.md` + practice/test/interview | ✅ DONE |
| 3 | Structural Analysis practice | Structures | No practice file | Create `structural-analysis/PRACTICE.md` | ✅ DONE |
| 4 | RCC practice | RCC | No practice file | Create `rcc/PRACTICE.md` | ✅ DONE |
| 5 | Steel practice | Steel | No practice file | Create `steel/PRACTICE.md` | ✅ DONE |
| 6 | Structural Analysis test | Structures | No test file | Create `structural-analysis/TEST.md` | ✅ DONE |
| 7 | RCC test | RCC | No test file | Create `rcc/TEST.md` | ✅ DONE |
| 8 | Steel test | Steel | No test file | Create `steel/TEST.md` | ✅ DONE |
| 9 | Structural Analysis interview | Structures | No interview file | Create `structural-analysis/INTERVIEW.md` | ✅ DONE |
| 10 | RCC interview | RCC | No interview file | Create `rcc/INTERVIEW.md` | ✅ DONE |
| 11 | Steel interview | Steel | No interview file | Create `steel/INTERVIEW.md` | ✅ DONE |
| 12 | `core/MASTER_INDEX.md` | All | No unified navigation | Create unified role → track → topic map | ⏳ NEXT |

## P1 — Important (Missing practice/tests / weak role strategy)

| # | Item | Track | Gap | Action | Status |
|---|------|-------|-----|--------|--------|
| 13 | Geotech practice/test/interview | Geotech | Embedded in role plan only | Create standalone files | ✅ DONE |
| 14 | Environmental practice/test/interview | Environmental | Embedded in role plan only | Create standalone files | ✅ DONE |
| 15 | Transportation practice/test/interview | Transportation | Embedded in role plan only | Create standalone files | ✅ DONE |
| 16 | Geoinformatics practice/test/interview | Geoinformatics | Embedded in role plan only | Create standalone files | ✅ DONE |
| 17 | Infrastructure practice/test/interview | Infrastructure | Embedded in role plan only | Create standalone files | ✅ DONE |
| 18 | CONTENT_REGISTRY.md | All | No duplication tracking | Create canonical-source registry | ✅ DONE |

## P2 — Navigation / Revision

| # | Item | Track | Gap | Action | Status |
|---|------|-------|-----|--------|--------|
| 19 | `structures/structures.md` duplication | Structures | Duplicates RCC/steel content | Link to canonical `rcc-design.md`/`steel-design.md` | ✅ DONE |
| 20 | RCC/Steel/Structural Analysis rapid revision | RCC/Steel/SA | No rapid revision files | Create `RAPID_REVISION.md` for each | ✅ DONE |
| 21 | `core/README.md` upgrade | All | No unified navigation | Add role → track → topic map | ✅ DONE |

## P3 — Formatting / Cleanup

| # | Item | Track | Gap | Action | Status |
|---|------|-------|-----|--------|--------|
| 22 | `hwre/hydraulics_notes/` empty folder | HWRE | Empty directory | Remove folder | ✅ DONE (already absent) |
| 23 | `civil-engineering-foundations.md` links | Fundamentals | No canonical-source links | Add links to canonical formula sheets | ✅ DONE |

---

## Execution Order

```
PHASE D  →  P0 items 1–12 (system layer + structural practice/test/interview + MASTER_INDEX)
PHASE E  →  P0 study-material gaps (structural practice/test/interview)
PHASE F  →  P1 items 13–18 (B-tier practice/test/interview + CONTENT_REGISTRY)
PHASE G  →  Company mapping (link companies → roles → content)
PHASE H  →  P2 items 19–21 (revision + navigation)
PHASE I  →  Navigation (MASTER_INDEX + README upgrade)
PHASE J  →  P3 items 22–23 (cleanup)
PHASE K  →  Final QA (quality_check.py + user test A–E)