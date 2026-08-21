# QC Report — DKS IITK Civil / HWRE Placement 2026

**Scope:** All markdown files in the repository **except** `index/`, `todo/`, and the 6 audit
output files produced by this review (`QC_REPORT.md`, `QA_REPORT.md`, `QUANTITY_REPORT.md`,
`MISSING_CONTENT.md`, `DUPLICATE_CONFLICTS.md`, `index/file_inventory.csv`).
**Files audited:** 70. `LICENSE` is intentionally exempt (binary/non-markdown).

## 1. Summary of Checks

| Check | Result | Count / Detail |
|-------|--------|----------------|
| File existence | PASS | 70/70 present |
| File type (`.md`, except `LICENSE`) | PASS | all audited files are `.md` |
| Empty file (< 50 bytes) | PASS | smallest is `hubstream.md` (602 bytes) |
| Encoding / mojibake | PASS | UTF-8, no BOM, LF line endings, no mojibake |
| References section (`## Sources`/`## References`) | WARN | 50 PASS / **20 FAIL** |
| Empty placeholder sections | WARN | **1 FAIL** (`resources/non-core-prep.md`) |
| Naming (lowercase-with-hyphens) | WARN | **5 FAIL** (underscores in filename) |
| Topic ↔ folder match | PASS* | primary topic matches folder in all 70 (1 content note, see §6) |
| `source_map.csv` destination accuracy | WARN | 64/68 destinations resolve; 4 issues (§7) |

## 2. References Section (20 FAIL)

The following 20 files have **no** `## Sources` / `## References` heading. Per the build
convention (todo `Phase 7`), every generated note should cite its source at the bottom.

**High severity (content notes that should cite sources):**
- `gate/civil/gate-civil-notes.md`
- `gate/formulas/gate-civil-formulas.md`
- `gate/practice/gate-civil-practice.md`
- `gate/revision_notes/gate-civil-revision.md`
- `interviews/company_specific/company-profiles.md`
- `interviews/mock_questions/mock-interview-questions.md`
- `interviews/technical/technical-interview-bank.md`
- `resources/book_list.md`
- `resources/links.md`
- `resources/non-core-prep.md`
- `resources/paper_list.md`
- `resources/placement-data.md`
- `resources/technical-stack.md`

**Lower severity (docs / templates where sources are N/A or repo-internal):**
- `README.md`
- `CHANGELOG.md`
- `behavioral/behavioral-interview-guide.md` (uses bold `**Sources:**`, not a heading)
- `templates/interview_answer_template.md`
- `templates/resume-template.md`
- `templates/self_intro_template.md`
- `templates/study_plan_template.md`

Note: `behavioral/behavioral-interview-guide.md` does contain a bold `**Sources:**` line
but not a proper Markdown heading, so it fails the automated heading check.

## 3. Empty Placeholder Sections (1 FAIL)

- `resources/non-core-prep.md` — contains skeleton headings with no body:
  `# Problem:`, `# Solution approach:`, `# 1. [Step]`, `# 2. [Step]`, `# Key learnings:`.
  This is a stub; it needs real content or should be marked explicitly as a template.

## 4. Naming Convention (5 FAIL)

5 files use underscores in the filename instead of hyphens:

- `resources/book_list.md` → suggest `book-list.md`
- `resources/paper_list.md` → suggest `paper-list.md`
- `templates/interview_answer_template.md` → suggest `interview-answer-template.md`
- `templates/self_intro_template.md` → suggest `self-intro-template.md`
- `templates/study_plan_template.md` → suggest `study-plan-template.md`

Sub-folder names also use underscores (e.g. `self_intro/`, `conflict_resolution/`,
`hr_questions/`, `logical_reasoning/`, `verbal/`, `quantitative/`, `water_supply/`,
`exam_notes/`). These are not flagged as file failures but deviate from the
lowercase-with-hyphens convention and are worth a consistent rename pass.

## 5. Encoding & Integrity

All 70 files are UTF-8 without BOM, use LF line endings, and contain no mojibake or
stray control characters. LaTeX fragments (`$...$`, `$$...$$`) render as plain text and
are preserved intact in the civil / hwre / aptitude / gate notes.

## 6. Topic ↔ Folder Match

Every file's primary subject matches its directory (e.g. `civil/hydraulics/hydraulics.md`
under `civil/`, `hwre/wastewater/wastewater-engineering.md` under `hwre/`). One
**content** caveat: `civil/water_resources/water-resources-engineering.md` also absorbs
"Transportation Software" (PTV Vissim, SUMO) and "GIS Tools" (ArcGIS, QGIS) per
`source_map.csv` rows 25 & 27 — arguably mis-filed under Water Resources. Consider moving
those bullets to a dedicated `civil/transportation/` or `resources/tools/` note.

## 7. `source_map.csv` Destination Accuracy

`source_map.csv` declares 68 unique destination paths. 64 resolve on disk. 4 issues:

| Destination in source_map | Status | Reality |
|---------------------------|--------|---------|
| `interviews/company_specific/darwin-box.md` | merged | actual file is `darwinbox.md` (hyphen typo in map) |
| `interviews/company_specific/musigma.md` | merged | actual file is `mu-sigma.md` (hyphen typo in map) |
| `interviews/technical/project-discussion.md` | merged | **file does not exist** (see MISSING_CONTENT.md) |
| `resources/syllabus.pdf` | skipped | binary PDF never extracted (intentional) |

The two hyphen typos mean the map does not point at the real filenames and would break any
automated path resolver.

## 8. Recommendations

1. Add `## Sources` sections to the 13 high-severity notes (esp. the 4 GATE files and the
   3 interview guides).
2. Fill or clearly stub `resources/non-core-prep.md`.
3. Rename the 5 underscore files (and ideally the underscore folders) to hyphens.
4. Fix the 2 `source_map.csv` hyphen typos and create `project-discussion.md`.
5. Split the Transportation/GIS content out of `water-resources-engineering.md`.
