# Duplicate & Conflict Report — DKS IITK Civil / HWRE Placement 2026

This report documents repeated topics across the 10 source repos + 1 gist, how they were
consolidated, explicit conflicts, and unresolved items. Source of truth: `index/topic_map.md`,
`index/master_index.md`, `index/source_map.csv`, `todo/agent_todo.md`.

## 1. Consolidated Duplicates (28 topics merged from 2+ sources)

Per `topic_map.md`, 43 mapped topics were produced; **28 were merged** from multiple sources
and **15 were directly extracted** from a single source.

### Merged from 2 sources (25)
- `civil/fundamentals/civil-engineering-foundations.md` (Civil_Placement_IITK + awesome-civil-engineering)
- `civil/hydraulics/hydraulics.md` (Civil_Placement_IITK + awesome-civil-engineering)
- `civil/hydrology/hydrology.md`
- `civil/water_resources/water-resources-engineering.md`
- `civil/geotechnical/geotechnical.md`
- `civil/structures/structures.md`
- `hwre/irrigation/irrigation-engineering.md`
- `hwre/water_supply/groundwater.md`
- `hwre/wastewater/wastewater-engineering.md`
- `hwre/flood_control/flood-control.md`
- `aptitude/quantitative/aptitude-basics.md` (Aptitude + Aptitude-For-Placements)
- `aptitude/logical_reasoning/reasoning-practice.md`
- `behavioral/self_intro/self-introduction.md`
- `behavioral/teamwork/teamwork.md`
- `behavioral/leadership/leadership.md`
- `behavioral/conflict_resolution/conflict-resolution.md`
- `behavioral/hr_questions/hr-questions-bank.md`
- `interviews/hr/hr-interview-guide.md`
- `interviews/technical/technical-interview-bank.md`
- `interviews/mock_questions/mock-interview-questions.md`
- `gate/formulas/gate-civil-formulas.md`
- `gate/practice/gate-civil-practice.md`
- `resources/book_list.md`
- `resources/technical-stack.md`
- `templates/resume-template.md`

### Merged from 3 sources (2)
- `behavioral/behavioral-interview-guide.md`
  (awesome-behavioral-interviews + behavioral-interview-list-of-questions + interview-handbook-2026)
- `interviews/mock_questions/mock-interview-questions.md`
  (interview-handbook-2026 + awesome-interview-questions + behavioral-interview-list-of-questions)

### Merged from 4 sources (1)
- `resources/links.md`
  (awesome-civil-engineering + Civil_Placement_IITK + campus-placement-prep + GATE_Civil_Study_Material_2027)

## 2. Repeated-Topics Resolution Table (`topic_map.md`)

| Topic | Repos | Resolution |
|-------|-------|------------|
| Behavioral Interview Tips | awesome-behavioral-interviews, behavioral-interview-list-of-questions, interview-handbook-2026 | → `behavioral/behavioral-interview-guide.md` |
| Technical Questions | Civil_Placement_IITK, interview-handbook-2026, campus-placement-prep | → `interviews/technical/technical-interview-bank.md` |
| Aptitude Basics | Aptitude, Aptitude-For-Placements, campus-placement-prep | → `aptitude/quantitative/aptitude-basics.md` |
| Hydraulics/Water Resources | Civil_Placement_IITK, awesome-civil-engineering | → `civil/hydraulics/hydraulics.md` |
| Resume Tips | Civil_Placement_IITK, campus-placement-prep | → `templates/resume-template.md` |

## 3. Conflicts to Verify (`todo/agent_todo.md`)

| # | Conflict | Disposition |
|---|----------|-------------|
| 1 | CFD tooling: OpenFOAM/SedFoam (Civil_Placement_IITK) vs FLOW-3D/OpenFOAM (awesome-civil-engineering) | **Kept both**, differences noted |
| 2 | Aptitude: LaTeX-heavy (Aptitude repo) vs plain-text (Aptitude-For-Placements) | **Merged concepts**, problem sets kept separate |
| 3 | Interview experiences: old (2011+, Placement_Preparation) vs recent (Civil_Placement_IITK profiles) | **Kept both**, clearly labeled by source/date |

No contradictory technical claims were found in the merged notes; the conflicts above were
handled by parallel inclusion rather than choosing one side.

## 4. Unresolved Items

- **`interviews/technical/project-discussion.md`** — planned/merged destination but the file
  was never created (see MISSING_CONTENT.md §1.1). The duplicate of "Project Discussion" from
  Civil_Placement_IITK + campus-placement-prep has no consolidated home.
- **`interviews/company_specific/interview-experiences.md`** — carries a
  "Further expansion needed" marker (Tech Mahindra post-2020 detail).

## 5. Map Inaccuracies Affecting Duplicate Tracking

- `source_map.csv` lists `darwin-box.md` / `musigma.md` as destinations; real files are
  `darwinbox.md` / `mu-sigma.md` (hyphen typos). Not duplicates — naming mismatches.
- `source_map.csv` "Not read yet" notes for 8 company files are stale (files exist).

## 6. Recommendations

1. Create `project-discussion.md` to close the one open duplicate merge.
2. Expand the flagged Tech Mahindra section.
3. Correct the 2 `source_map.csv` hyphen typos so duplicate→destination tracking is exact.
