# Missing Content Report — DKS IITK Civil / HWRE Placement 2026

This report lists content that is **expected but absent**, plus mapping inaccuracies that
make intended content look missing. Scope: 70 audited markdown files.

## 1. Truly Missing Topics (no file on disk)

### 1.1 `interviews/technical/project-discussion.md`  ❗
- Referenced by `master_index.md` row 18 ("Project Discussion — How to present projects in
  interviews") and `source_map.csv` row 61 (`campus-placement-prep/README.md` →
  `interviews/technical/project-discussion.md`, status `merged`).
- **Not present** in the repo and **not listed** in `todo/agent_todo.md`'s P0/P1 checklists,
  so it was never queued for generation. This is the single genuine content gap versus the
  planned index.

## 2. Intentionally Skipped / Un-extracted Sources

### 2.1 `resources/syllabus.pdf`
- `source_map.csv` row 20 maps `Civil_Placement_IITK/placeemnt_iitksyllabus.pdf` →
  `resources/syllabus.pdf` with status `skipped` (binary PDF; the model lacked PDF input).
- No markdown equivalent was produced. Syllabus coverage is noted as deferred to
  `GATE_Civil_Study_Material_2027.md`.

## 3. Source-Map Path Inaccuracies (files exist under a different name)

These destinations in `source_map.csv` do not resolve verbatim, but the content **does**
exist — the map has hyphenation typos:

| source_map destination | Actual file |
|-------------------------|-------------|
| `interviews/company_specific/darwin-box.md` | `interviews/company_specific/darwinbox.md` |
| `interviews/company_specific/musigma.md` | `interviews/company_specific/mu-sigma.md` |

Any tool that resolves `source_map.csv` paths will falsely report these as missing.

## 4. Stale Map Notes (content exists, map says otherwise)

`source_map.csv` rows 66–73 carry `notes = "Not read yet"` for 8 company experiences:
Musigma, Johnson Controls, Hubstream, Hiremi, Expeditor, Deltax, Darwinbox, CEI American.
All 8 corresponding files **were created** (e.g. `musigma.md`, `johnson-controls.md`). The
notes were never updated after generation — a documentation inconsistency, not missing content.

## 5. Partially Complete Content

- `resources/non-core-prep.md` — skeleton with empty `# Problem:` / `# Solution approach:`
  placeholders (stub, not yet filled).
- `interviews/company_specific/interview-experiences.md` — explicit
  **"Further expansion needed"** marker on the Tech Mahindra section (post-2020 process and
  exact coding problem sets undocumented in source).

## 6. Expected-but-Absent (negative check)

- All 46 `master_index.md` topics have a file **except** Project Discussion (§1.1).
- All `topic_map.md` destinations exist except none additional (the 2 hyphen typos resolve
  to real files; the 1 missing file is `project-discussion.md`).
- No empty directories remain; `todo/agent_todo.md` cleanup tasks are otherwise satisfied.

## 7. Recommended Additions

1. Create `interviews/technical/project-discussion.md` (or remove its index entries).
2. Fix the 2 `source_map.csv` hyphen typos.
3. Clear the stale `Not read yet` notes.
4. Complete `non-core-prep.md` and expand the Tech Mahindra section of `interview-experiences.md`.
