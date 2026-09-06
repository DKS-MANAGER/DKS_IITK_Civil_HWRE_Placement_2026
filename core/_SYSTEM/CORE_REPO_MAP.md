# Core Repository Map — Complete Inventory

> **Purpose:** Complete file inventory of `core/` with status classification. Part of the master `core/` audit.
> **Status legend:** `GOOD` = placement-ready · `PARTIAL` = studyable but missing practice/test/interview · `INDEX_ONLY` = headings/links only · `EMPTY` = no content · `DUPLICATE` = overlaps canonical source · `MISPLACED` = wrong folder · `OBSOLETE` = superseded · `BROKEN` = dead link

---

## 1. Track Summary

| Track | Files | Study Material | Role Plan | Practice | Test | Interview | Revision | Overall |
|-------|:-----:|:--------------:|:---------:|:--------:|:----:|:---------:|:--------:|:-------:|
| `gate/` | 14 | ✅ | ✅ (via roadmap) | ✅ | ✅ | ✅ (in notes) | ✅ | **GOOD** |
| `hwre/` | 34 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | **GOOD** |
| `fundamentals/` | 5 | ✅ | ✅ | △ (in role plan) | ✗ | △ (in role plan) | ✅ | **PARTIAL** |
| `structures/` | 4 | ✅ | ✅ | △ | ✗ | △ | ✅ | **PARTIAL** |
| `rcc/` | 1 | ✅ | ✗ | ✗ | ✗ | ✗ | ✗ | **PARTIAL** |
| `steel/` | 1 | ✅ | ✗ | ✗ | ✗ | ✗ | ✗ | **PARTIAL** |
| `structural-analysis/` | 1 | ✅ | ✗ | ✗ | ✗ | ✗ | ✗ | **PARTIAL** |
| `geotechnical/` | 4 | ✅ | ✅ | △ | ✗ | △ | ✅ | **PARTIAL** |
| `environmental/` | 4 | ✅ | ✅ | △ | ✗ | △ | ✅ | **PARTIAL** |
| `transportation/` | 5 | ✅ | ✅ | △ | ✗ | △ | ✅ | **PARTIAL** |
| `geoinformatics/` | 4 | ✅ | ✅ | △ | ✗ | △ | ✅ | **PARTIAL** |
| `infrastructure/` | 7 | ✅ | ✅ | △ | ✗ | △ | ✅ | **PARTIAL** |

---

## 2. Full File Inventory

### `core/gate/` — GATE Civil Subsystem (REBUILT — GOOD)

| Path | Type | Purpose | Status |
|------|------|---------|--------|
| `gate/README.md` | Hub | GATE entry point | GOOD |
| `gate/MASTER_INDEX.md` | Navigation | 1–2 click navigation | GOOD |
| `gate/GATE_ROADMAP.md` | Roadmap | Syllabus → progression | GOOD |
| `gate/GATE_30_60_90_DAY_PLAN.md` | Plan | 3-phase prep plan | GOOD |
| `gate/RAPID_REVISION.md` | Revision | Rapid recall | GOOD |
| `gate/ERROR_ANALYSIS.md` | Meta | Error catalog | GOOD |
| `gate/civil/gate-civil-notes.md` | Study | Topic-wise notes | GOOD |
| `gate/formulas/gate-civil-formulas.md` | Formulas | Canonical formula sheet | GOOD |
| `gate/practice/gate-civil-practice.md` | Practice | 21 solved problems | GOOD |
| `gate/mocks/gate-civil-mock-1.md` | Test | Full mock test | GOOD |
| `gate/pyq/gate-civil-pyq.md` | PYQ | Previous questions | GOOD |
| `gate/revision_notes/gate-civil-revision.md` | Revision | Flash cards | GOOD |
| `gate/_SYSTEM/*` (4) | Tracking | Audit state, repo map, inventory, matrix | GOOD |

### `core/hwre/` — HWRE Subsystem (REBUILT — GOOD)

| Path | Type | Purpose | Status |
|------|------|---------|--------|
| `hwre/README.md` | Hub | HWRE entry point | GOOD |
| `hwre/MASTER_INDEX.md` | Navigation | 1–2 click navigation | GOOD |
| `hwre/HWRE_ROADMAP.md` | Roadmap | Syllabus → progression | GOOD |
| `hwre/HWRE_30_60_90_DAY_PLAN.md` | Plan | 3-phase prep plan | GOOD |
| `hwre/RAPID_REVISION.md` | Revision | Rapid recall | GOOD |
| `hwre/ERROR_ANALYSIS.md` | Meta | Error catalog | GOOD |
| `hwre/TRAPS.md` | Meta | Common traps | GOOD |
| `hwre/INTERVIEW.md` | Interview | 41 Q&A | GOOD |
| `hwre/MODELLING.md` | Study | HEC-HMS→RAS→GIS | GOOD |
| `hwre/role-study-plan.md` | Role plan | HWRE role | GOOD |
| `hwre/formulas/hwre-formulas.md` | Formulas | Canonical HWRE sheet | GOOD |
| `hwre/practice/hwre-practice.md` | Practice | 21 solved problems | GOOD |
| `hwre/mocks/hwre-mock-1.md` | Test | Full mock test | GOOD |
| `hwre/exam_notes/hwre-exam-notes.md` | Revision | Cheat sheet | GOOD |
| `hwre/hydraulics/hydraulics.md` | Study | Hydraulics | GOOD |
| `hwre/hydraulics/turbulence-modeling.md` | Study | Turbulence/CFD | GOOD |
| `hwre/hydraulics/hydraulics-rapid-revision.md` | Revision | Hydraulics revision | GOOD |
| `hwre/hydraulics/role-study-plan.md` | Role plan | Hydraulics role | GOOD |
| `hwre/hydrology/hydrology.md` | Study | Hydrology | GOOD |
| `hwre/hydrology/sediment-transport.md` | Study | Sediment | GOOD |
| `hwre/hydrology/hydrology-rapid-revision.md` | Revision | Hydrology revision | GOOD |
| `hwre/hydrology/role-study-plan.md` | Role plan | Hydrology role | GOOD |
| `hwre/open_channel_flow/open-channel-flow.md` | Study | OCF | GOOD |
| `hwre/water_resources/water-resources-engineering.md` | Study | WRE | GOOD |
| `hwre/water_supply/water-supply.md` | Study | Water supply | GOOD |
| `hwre/water_supply/groundwater.md` | Study | Groundwater | GOOD |
| `hwre/irrigation/irrigation-engineering.md` | Study | Irrigation | GOOD |
| `hwre/flood_control/flood-control.md` | Study | Flood control | GOOD |
| `hwre/wastewater/wastewater-engineering.md` | Study | Wastewater | GOOD |
| `hwre/hydraulics_notes/` | — | **EMPTY folder** | **EMPTY** |
| `hwre/_SYSTEM/*` (4) | Tracking | Audit state, repo map, inventory, matrix | GOOD |

### `core/fundamentals/` — Foundations (PARTIAL)

| Path | Type | Purpose | Status |
|------|------|---------|--------|
| `fundamentals/README.md` | Hub | Entry point | GOOD |
| `fundamentals/engineering-mechanics.md` | Study | Mechanics (616 lines) | GOOD |
| `fundamentals/strength-of-materials.md` | Study | SOM (704 lines) | GOOD |
| `fundamentals/civil-engineering-foundations.md` | Revision | Cross-domain formula sheet | GOOD |
| `fundamentals/civil-rapid-revision.md` | Revision | Rapid revision | GOOD |
| `fundamentals/role-study-plan.md` | Role plan | General Civil role (346 lines) | GOOD |

### `core/structures/` — Structures (PARTIAL)

| Path | Type | Purpose | Status |
|------|------|---------|--------|
| `structures/README.md` | Hub | Entry point | GOOD |
| `structures/structures.md` | Study | SOM+RCC+steel overview (318) | **DUPLICATE** (overlaps rcc/steel) |
| `structures/structural-rapid-revision.md` | Revision | Rapid revision | GOOD |
| `structures/role-study-plan.md` | Role plan | Structural role (187) | GOOD |

### `core/rcc/` — RCC Design (PARTIAL)

| Path | Type | Purpose | Status |
|------|------|---------|--------|
| `rcc/rcc-design.md` | Study | RCC design (886 lines) | GOOD |

### `core/steel/` — Steel Design (PARTIAL)

| Path | Type | Purpose | Status |
|------|------|---------|--------|
| `steel/steel-design.md` | Study | Steel design (853 lines) | GOOD |

### `core/structural-analysis/` — Structural Analysis (PARTIAL)

| Path | Type | Purpose | Status |
|------|------|---------|--------|
| `structural-analysis/structural-analysis.md` | Study | Structural analysis (679) | GOOD |

### `core/geotechnical/` — Geotechnical (PARTIAL)

| Path | Type | Purpose | Status |
|------|------|---------|--------|
| `geotechnical/README.md` | Hub | Entry point | GOOD |
| `geotechnical/geotechnical.md` | Study | Geotech (277 lines) | GOOD |
| `geotechnical/geotechnical-rapid-revision.md` | Revision | Rapid revision | GOOD |
| `geotechnical/role-study-plan.md` | Role plan | Geotech role (445) | GOOD |

### `core/environmental/` — Environmental (PARTIAL)

| Path | Type | Purpose | Status |
|------|------|---------|--------|
| `environmental/README.md` | Hub | Entry point | GOOD |
| `environmental/environmental-engineering.md` | Study | Environmental (620) | GOOD |
| `environmental/environmental-rapid-revision.md` | Revision | Rapid revision | GOOD |
| `environmental/role-study-plan.md` | Role plan | Enviro role (363) | GOOD |

### `core/transportation/` — Transportation (PARTIAL)

| Path | Type | Purpose | Status |
|------|------|---------|--------|
| `transportation/README.md` | Hub | Entry point | GOOD |
| `transportation/transportation-engineering.md` | Study | Transportation (642) | GOOD |
| `transportation/transportation-software.md` | Study | Software tools | GOOD |
| `transportation/transportation-rapid-revision.md` | Revision | Rapid revision | GOOD |
| `transportation/role-study-plan.md` | Role plan | Transport role (414) | GOOD |

### `core/geoinformatics/` — Geoinformatics (PARTIAL)

| Path | Type | Purpose | Status |
|------|------|---------|--------|
| `geoinformatics/README.md` | Hub | Entry point | GOOD |
| `geoinformatics/geoinformatics.md` | Study | GIS/RS (779 lines) | GOOD |
| `geoinformatics/geoinformatics-rapid-revision.md` | Revision | Rapid revision | GOOD |
| `geoinformatics/role-study-plan.md` | Role plan | GIS role (441) | GOOD |

### `core/infrastructure/` — Infrastructure Mgmt (PARTIAL)

| Path | Type | Purpose | Status |
|------|------|---------|--------|
| `infrastructure/README.md` | Hub | Entry point | GOOD |
| `infrastructure/infrastructure-engineering-management.md` | Study | Infra mgmt (811) | GOOD |
| `infrastructure/infrastructure-rapid-revision.md` | Revision | Rapid revision | GOOD |
| `infrastructure/construction-rapid-revision.md` | Revision | Construction revision | GOOD |
| `infrastructure/construction-role-study-plan.md` | Role plan | Construction role | GOOD |
| `infrastructure/role-study-plan.md` | Role plan | Infra/PM role (436) | GOOD |

### `core/README.md` — Root Hub

| Path | Type | Purpose | Status |
|------|------|---------|--------|
| `core/README.md` | Hub | Branch navigation | GOOD (needs MASTER_INDEX upgrade) |

---

## 3. Key Findings

1. **`gate/` and `hwre/` are complete subsystems** (Level 4–5). All other tracks are Level 3 (studyable) but **missing the practice → test → interview chain**.
2. **No `core/_SYSTEM/` tracking layer** exists (this file is the first).
3. **No `core/MASTER_INDEX.md`** — `core/README.md` is the only hub and lacks a unified role → track → topic map.
4. **`rcc/`, `steel/`, `structural-analysis/`** have strong study material but **no role plan, practice, test, or interview files**.
5. **`structures/structures.md`** duplicates RCC + steel content (should link to canonical `rcc-design.md`/`steel-design.md`).
6. **`hwre/hydraulics_notes/`** is an **empty folder** — should be removed.
7. **B-tier role plans** (geotech, enviro, transport, GIS, infra) embed practice questions but have **no standalone test or interview files**.
8. **`civil-engineering-foundations.md`** and **`civil-rapid-revision.md`** duplicate formulas across tracks — acceptable as revision, but must link to canonical sources.

---

## 4. Navigation Graph

```
core/README.md (root hub)
├── gate/MASTER_INDEX.md → notes → formulas → practice → mock → pyq → revision
├── hwre/MASTER_INDEX.md → 11 subjects → formulas → practice → mock → interview → modelling
├── fundamentals/README.md → mechanics → SOM → foundations → role plan
├── structures/README.md → structures.md → rcc-design → steel-design → structural-analysis
├── geotechnical/README.md → geotechnical.md → role plan
├── environmental/README.md → environmental-engineering.md → role plan
├── transportation/README.md → transportation-engineering.md → software → role plan
├── geoinformatics/README.md → geoinformatics.md → role plan
└── infrastructure/README.md → infrastructure-engineering-management.md → role plan