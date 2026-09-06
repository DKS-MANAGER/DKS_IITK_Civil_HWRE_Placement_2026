# PREP FOLDER QUEUE

> Processing order for `prep/` folder-by-folder audit + rebuild.

---

## Queue

| # | Folder | Purpose | Files Found | Status | Notes |
|---|--------|---------|-------------|--------|-------|
| 1 | `behavioral/` | Behavioral/HR/STAR preparation | 30 | COMPLETE | PLACEMENT_READY — 198-line README, 200+ questions, 60+ stories, frameworks, strategies |
| 2 | `interview/` | Interview-round preparation (technical, HR, mock, revision) | 12 | COMPLETE | PLACEMENT_READY — interview-day-survival 248 lines, quick-revision 227 lines |
| 3 | `mock-tests/` | Role-specific timed mock tests | 26 | COMPLETE | PLACEMENT_READY — 25 role-specific tests, scorecards, answer keys |
| 4 | `company-profiles/` | Company-specific strategies + interview experiences | 36 | COMPLETE | GOOD — individual profiles are substantial; README is thin navigation |
| 5 | `templates/` | Reusable templates (resume, study plan, self-intro) | 6 | COMPLETE | GOOD — resume-template 214 lines, study-plan-template, self-intro-template |
| 6 | `technical/` | Technical interview resources (redirect) | 1 | COMPLETE | DEAD REDIRECT — 34-line README links to `interview/technical/`. Will be removed. |

## Top-Level Files (Created During Audit)

| # | File | Purpose | Status | Notes |
|---|------|---------|--------|-------|
| 7 | `_SYSTEM/` | Audit infrastructure (state, queue, matrix) | COMPLETE | 4 files |
| 8 | `MASTER_PREP_PLAN.md` | Master execution plan — the central hub | CREATED | Links to all prep systems |
| 9 | `30_14_7_DAY_PLAN.md` | Placement-specific 30/14/7 day plans | CREATED | Execution layer, distinct from `aptitude/7_14_30_DAY_PLAN.md` |
| 10 | `PLACEMENT_CHECKLIST.md` | Document + logistics checklist | CREATED | CV, docs, certificates, clothing, tech |
| 11 | `INTERVIEW_TOMORROW.md` | Interview-tomorrow mode (1-2 click path) | CREATED | Company → Role → Technical → Projects → HR → Revision |
| 12 | `SELECTION_STAGE_MAP.md` | Selection process stages documented | CREATED | Application → Screening → Aptitude → Technical → Case/GD → HR |
| 13 | `PLACEMENT_COMMUNICATION.md` | Recruiter comms, etiquette, emails | CREATED | Professional email, follow-up, scheduling |
| 14 | `CASE_GD.md` | Case interview + GD preparation | CREATED | For consulting/product/management roles only |
| 15 | `PROJECT_DEFENCE.md` | Canonical project defence system | CREATED | Consolidates interview/technical/ + behavioral/ approaches |
| 16 | `MOCK_INTERVIEW.md` | Canonical mock interview system | CREATED | 5-round structure with scoring rubric |
| 17 | `RAPID_REVISION.md` | Canonical rapid revision system | CREATED | 1-day, 3-day, 7-day plans |
| 18 | `RESUME/README.md` | Resume audit + resume→interview defense | CREATED | Audit checklist + claim→question→preparation |
| 19 | `APTITUDE/README.md` | Aptitude navigation layer → root `aptitude/` | CREATED | Links to root; no content duplication |
| 20 | `README.md` | Master prep navigation hub (overhauled) | UPDATED | Complete navigation overhaul |

## Processing Rules

1. Process folders in queue order (1 → 6)
2. Never partially fix multiple folders simultaneously
3. Mark folder COMPLETE only after: inventory → audit → fix → verify → score
4. Create `_SYSTEM/PREP_PROCESS_STATE.md` to track progress
5. Do not re-read completed folders
