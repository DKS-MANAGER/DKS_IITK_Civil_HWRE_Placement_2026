# QA Report — DKS IITK Civil / HWRE Placement 2026

**Scope:** Content-quality assessment of the 70 audited markdown files (see QC_REPORT.md for
scope). Focus: paraphrase quality, formatting consistency, technical accuracy, completeness,
and reference completeness.

## 1. Overall Assessment

The knowledge base is in **good technical shape**. Core engineering, aptitude, and GATE
notes are well paraphrased (no long verbatim copying), use consistent headings, and preserve
formulas and definitions accurately. Remaining issues are concentrated in (a) template/
resource files that reference non-existent placeholder paths, (b) a few stubs, and
(c) missing source citations on generated notes (tracked in QC_REPORT.md).

## 2. Paraphrase Quality — PASS

- Source repos were synthesized rather than copied. No large verbatim passages detected.
- Aptitude notes consolidate 34 topics / 340 problems into concise, formula-led notes.
- Behavioral and interview guides are rewritten into STAR/CAR frameworks with examples.

## 3. Formatting Consistency — WARN

### 3.1 Broken internal references (placeholder paths)
Three files point readers to repo-relative paths that do not exist as markdown links or as
real folders:

- `placement-roadmap.md` → references `/resumes`, `/company-profiles`
- `hwre/exam_notes/hwre-exam-notes.md` → references `/core`, `/company-profiles`
- `templates/study_plan_template.md` → references `/core`, `/resumes`, `/company-profiles`

These appear as plain text (`Resume templates in /resumes/`), not Markdown links, so they
are not caught by a link checker but are still dead cross-references. Either create the
target folders/notes or rewrite as relative links (e.g. `interviews/company_specific/company-profiles.md`).

### 3.2 Checkbox markup
Earlier suspicion of broken `- [ ]` checkboxes in templates was **not confirmed** — the
checklist sections in all four templates use valid GitHub-flavored task lists.

### 3.3 Minor typo
- `templates/interview_answer_template.md` contains a duplicated `Task/Task` label (one
  occurrence). Should read `Task:`.

### 3.4 Self-referential "sources"
The four template files cite the repository's own files under a bold `**Sources:**` line
(e.g. `templates/resume-template.md` cites `templates/...`). These are internal pointers,
not external provenance, and are also why they fail the references-heading check in QC.

## 4. Technical Accuracy — PASS

- LaTeX formulas in hydraulics, open-channel flow, hydrology, sediment transport, GATE
  formulas/notes, and quantitative aptitude are syntactically intact.
- `gate/civil/gate-civil-notes.md` (12.9 KB) and `gate/practice/gate-civil-practice.md`
  (19.3 KB) are the largest and most formula-dense notes and render cleanly.
- Company experience files (e.g. `schneider-electric.md`, `tech-mahindra.md`) preserve
  round structures, tables, and package figures accurately.

## 5. Completeness — WARN

- `resources/non-core-prep.md` is a skeleton (empty `# Problem:` / `# Solution approach:`
  placeholders) — not yet usable.
- `interviews/company_specific/interview-experiences.md` carries an explicit
  **"Further expansion needed"** marker on the Tech Mahindra section (post-2020 process
  changes, exact coding sets not documented).

## 6. Reference Completeness — WARN

20 files lack a `## Sources` / `## References` heading (full list in QC_REPORT.md §2). The
4 GATE notes and 3 interview guides are the most important to backfill with provenance.
Company-experience files do cite sources, but as **absolute Windows paths**
(`F:\2k26Placement\Placement_Preparation\INTERVIEW EXPERIENCES\...`) — valid as provenance
but not portable/reproducible; a few also include external URLs (Hubstream, MuSigma,
Schneider). `source_map.csv` still carries stale `Not read yet` notes for 8 company
experiences (Musigma, Johnson Controls, Hubstream, Hiremi, Expeditor, Deltax, Darwinbox,
CEI American) even though those files were in fact created — the map was not updated.

## 7. Recommendations

1. Rewrite the 3 placeholder-path references as real relative links or create the targets.
2. Fix the `Task/Task` typo in `interview_answer_template.md`.
3. Backfill `## Sources` on GATE + interview-guide notes.
4. Complete `non-core-prep.md` or label it explicitly as a template.
5. Refresh `source_map.csv` "Not read yet" notes to reflect the created company files.
