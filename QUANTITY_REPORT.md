# Quantity Report — DKS IITK Civil / HWRE Placement 2026

**Generated:** 2026-08-21 · **Audited files:** 70 markdown files (excludes `index/`, `todo/`, and the 6 audit outputs).

## 1. Headline Metrics

| Metric | Value |
|--------|-------|
| Markdown files scanned | 70 |
| Files useful (non-empty, on-topic) | 70 (100%) |
| Topics defined in `master_index.md` | 46 |
| Topics mapped in `topic_map.md` | 43 |
| Unique destinations in `source_map.csv` | 68 |
| Destinations present on disk | 64 |
| Destinations with issues | 4 (1 missing, 2 typo, 1 skipped) |
| Files with a references section | 50 |
| Files without a references section | 20 |
| Files with empty placeholder sections | 1 |
| Files with naming deviation | 5 |
| Duplicate/merged topics (consolidated) | 28 |
| Explicit conflicts to verify | 3 |
| Unresolved items | 2 (missing file + expansion marker) |
| Missing topics (no file) | 1 |

## 2. Files per Category (Folder Coverage)

| Category | Files | With refs | Notes |
|----------|-------|-----------|-------|
| root | 3 | 1 | README, CHANGELOG lack refs |
| aptitude | 17 | 17 | fully cited |
| behavioral | 6 | 5 | guide uses bold `**Sources:**` |
| civil | 9 | 9 | fully cited |
| gate | 4 | 0 | **none cited** |
| hwre | 6 | 6 | fully cited |
| interviews | 15 | 12 | company-profiles, mock, technical-bank lack refs |
| resources | 6 | 0 | **none cited** |
| templates | 4 | 0 | templates (sources N/A) |

## 3. Notes per Category (by sub-topic)

- **civil (9):** foundations, hydraulics, turbulence-modeling, open-channel-flow, hydrology,
  sediment-transport, water-resources, geotechnical, structures.
- **hwre (6):** irrigation, groundwater, water-supply, wastewater, flood-control, exam-notes.
- **aptitude (17):** basics, averages, data-interpretation, number-system, partnership,
  percentages, permutations-combinations, probability, problems-on-ages, problems-on-train,
  profit-loss-discount, ratio-proportion, speed-time-distance, time-work, shortcuts,
  reasoning-practice, verbal-ability.
- **behavioral (6):** guide, self-introduction, teamwork, leadership, conflict-resolution, hr-questions-bank.
- **gate (4):** civil-notes, formulas, revision, practice.
- **interviews (15):** technical-bank, hr-guide, mock-questions, company-profiles,
  interview-experiences, + 10 company files (cei-american, darwinbox, deltax, expeditor,
  hiremi, hubstream, johnson-controls, mu-sigma, schneider-electric, tech-mahindra).
- **resources (6):** book_list, paper_list, links, non-core-prep, placement-data, technical-stack.
- **templates (4):** resume, self-intro, interview-answer, study-plan.

## 4. Source-Map Coverage

- `source_map.csv`: 95 mapping rows → 68 unique destinations. 64 resolve; 4 issues
  (2 hyphen typos `darwin-box.md`→`darwinbox.md`, `musigma.md`→`mu-sigma.md`; 1 truly
  missing `project-discussion.md`; 1 intentionally skipped binary `syllabus.pdf`).
- `master_index.md`: 46 topics. All have a destination file **except** topic #18
  "Project Discussion" → `interviews/technical/project-discussion.md` (missing).

## 5. Duplicates & Conflicts (summary; detail in DUPLICATE_CONFLICTS.md)

- **28 topics** consolidated from 2+ sources (2 from 3 sources, 1 from 4 sources).
- **3 conflicts** flagged for verification in `todo/agent_todo.md` (CFD tooling,
  Aptitude LaTeX vs plain-text, old vs recent interview experiences) — all resolved by
  "keep both / label clearly".
- **Unresolved:** `project-discussion.md` never created; `interview-experiences.md`
  carries a "Further expansion needed" marker.

## 6. Interpretation

Coverage is strong: 70 notes across 8 categories, 46/46 master-index topics realized (minus
the one missing project-discussion note). Weakest dimensions are **provenance** (20 notes
uncited, especially all 4 GATE and all 6 resources notes) and **a few stubs/placeholder
references**. No empty or orphaned files; encoding is uniform.
