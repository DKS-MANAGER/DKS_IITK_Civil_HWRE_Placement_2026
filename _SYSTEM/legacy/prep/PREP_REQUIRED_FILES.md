# PREP REQUIRED FILES

> Required file inventory for `prep/` — maps every file to its placement-execution purpose.

---

## Existing Folders (AUDITED)

| Area | Folder | Files | Quality | Status | Action |
|------|--------|-------|---------|--------|--------|
| Behavioral/HR | `behavioral/` | 30 | 9/10 | PLACEMENT_READY | KEEP |
| Interview Rounds | `interview/` | 12 | 9/10 | PLACEMENT_READY | KEEP |
| Mock Tests | `mock-tests/` | 26 | 9/10 | PLACEMENT_READY | KEEP |
| Company Intel | `company-profiles/` | 36 | 7/10 | GOOD | KEEP |
| Templates | `templates/` | 6 | 8/10 | GOOD | KEEP |
| Technical Redirect | `technical/` | 1 | N/A | DEAD REDIRECT | DELETE |

## Top-Level Files (EXISTING)

| Area | File | Quality | Status | Action |
|------|------|---------|--------|--------|
| Prep Index | `README.md` | 7/10 | PARTIAL | UPDATE — complete navigation overhaul |

## Top-Level Files (CREATED)

| Area | File | Purpose | Action |
|------|------|---------|--------|
| Master Plan | `MASTER_PREP_PLAN.md` | Central execution hub | CREATE |
| Timeline | `30_14_7_DAY_PLAN.md` | Placement execution timelines | CREATE |
| Checklist | `PLACEMENT_CHECKLIST.md` | Document + logistics checklist | CREATE |
| Interview Tomorrow | `INTERVIEW_TOMORROW.md` | Rapid 1-2 click interview prep | CREATE |
| Stage Map | `SELECTION_STAGE_MAP.md` | Selection process documentation | CREATE |
| Communication | `PLACEMENT_COMMUNICATION.md` | Professional comms + etiquette | CREATE |
| Case/GD | `CASE_GD.md` | Case interview + GD (non-core) | CREATE |
| Project Defence | `PROJECT_DEFENCE.md` | Canonical project defence system | CREATE |
| Mock Interview | `MOCK_INTERVIEW.md` | Canonical mock interview system | CREATE |
| Rapid Revision | `RAPID_REVISION.md` | Canonical rapid revision plans | CREATE |

## New Folders (CREATED)

| Area | Folder | Files | Purpose | Action |
|------|--------|-------|---------|--------|
| Resume | `RESUME/` | 3 | Audit + defense + template reference | CREATE |
| Aptitude Nav | `APTITUDE/` | 1 | Navigation layer → root `aptitude/` | CREATE |

## Canonical Source Mapping

| Component | Canonical Location | Also Present At | Action |
|-----------|-------------------|-----------------|--------|
| Aptitude Content | `../aptitude/` (root) | — | `prep/APTITUDE/` links to it |
| Behavioral Q&A | `behavioral/question-master-database.md` | — | Canonical |
| Self Introduction | `behavioral/self_intro/self-introduction-system.md` | — | Canonical |
| Story Bank | `behavioral/story-bank/` | — | Canonical |
| HR Questions | `behavioral/hr_questions/hr-questions-bank.md` | — | Canonical |
| Mock Interview | `MOCK_INTERVIEW.md` (prep-level) + `behavioral/mock-interviews/` | `interview/mock-tests/` | `MOCK_INTERVIEW.md` is the execution entry point |
| Project Defence | `PROJECT_DEFENCE.md` (prep-level) | `interview/technical/project-defense-guide.md` | `PROJECT_DEFENCE.md` consolidates |
| Quick Revision | `RAPID_REVISION.md` (prep-level) | `interview/quick-revision-system.md` + `behavioral/rapid-revision-cards.md` | `RAPID_REVISION.md` is the execution entry point |
| Company Profiles | `company-profiles/` | — | Canonical |
| Interview Day | `interview/interview-day-survival.md` | — | Canonical |
| Resume | `templates/resume-template.md` | — | Canonical |

## Build Order

```
1. _SYSTEM/ (infrastructure) ✅
2. MASTER_PREP_PLAN.md ✅
3. 30_14_7_DAY_PLAN.md ✅
4. PLACEMENT_CHECKLIST.md ✅
5. INTERVIEW_TOMORROW.md ✅
6. SELECTION_STAGE_MAP.md ✅
7. PLACEMENT_COMMUNICATION.md ✅
8. CASE_GD.md ✅
9. RESUME/ ✅
10. PROJECT_DEFENCE.md ✅
11. MOCK_INTERVIEW.md ✅
12. RAPID_REVISION.md ✅
13. APTITUDE/ ✅
14. README.md overhaul ✅
15. DELETE technical/README.md ✅
```

**ALL COMPLETE**
