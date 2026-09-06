# DOCS Audit State

> **Live tracking document for the `docs/` audit and rebuild.**
> Maintained by the repository maintainer. Update after every meaningful change to `docs/`.

---

## Audit Summary

| Field | Value |
|:------|:------|
| **Audit start** | 2026-09-06 |
| **Audit scope** | Entire `docs/` directory + root `README.md` integration |
| **Docs files inventoried** | 20 (10 top-level, 8 templates, 2 audit/source) |
| **Files classified** | KEEP: 8 · IMPROVE: 4 · CREATE: 17 |
| **Files created** | 17 (4 `_SYSTEM` + 13 user-facing guides) |
| **Files modified** | 4 (README, start-here, placement-control-panel, content-standards) |
| **Broken links found** | 0 (600 internal links verified) |
| **Status** | COMPLETE |

---

## Completed

- [x] **Inventory** — Recursively inspected every file under `docs/` (see [`DOCS_FILE_MAP.md`](DOCS_FILE_MAP.md))
- [x] **Classification** — Assigned KEEP / IMPROVE / MERGE / MOVE / DELETE / CREATE to every file
- [x] **Purpose definition** — Documented what `docs/` must answer (repository understanding, navigation, usage, system docs)
- [x] **Architecture design** — Final documentation architecture defined (see below)
- [x] **`_SYSTEM/DOCS_FILE_MAP.md`** — Created
- [x] **`_SYSTEM/DOCS_AUDIT_STATE.md`** — Created (this file)
- [x] **`_SYSTEM/DOCS_LINK_AUDIT.md`** — Created
- [x] **`_SYSTEM/DOCS_CONTENT_REGISTRY.md`** — Created
- [x] **`docs/README.md`** — Rebuilt as documentation hub
- [x] **`GETTING_STARTED.md`** — Created
- [x] **`MASTER_NAVIGATION.md`** — Created
- [x] **`TRACKS.md`** — Created
- [x] **`ROLES.md`** — Created
- [x] **`COMPANIES.md`** — Created
- [x] **`HOW_TO_USE.md`** — Created
- [x] **`INTERVIEW_GUIDE.md`** — Created
- [x] **`BEHAVIOURAL_HR_GUIDE.md`** — Created
- [x] **`TESTING_GUIDE.md`** — Created
- [x] **`RAPID_REVISION_GUIDE.md`** — Created
- [x] **`PREPARATION_WORKFLOW.md`** — Created
- [x] **`SOURCE_POLICY.md`** — Created
- [x] **`CONTENT_STANDARDS.md`** — Improved (source policy, naming, links, updates)
- [x] **`CONTRIBUTING.md`** — Created
- [x] **`start-here.md`** — Mojibake fixed + routed to GETTING_STARTED
- [x] **`placement-control-panel.md`** — Mojibake fixed
- [x] **Link validation** — Terminal-verified: 600 internal links, 0 broken
- [x] **README integration** — Root README routes into docs/ correctly (115 links, 0 missing)
- [x] **Mojibake fix** — start-here.md and placement-control-panel.md verified clean

---

## Modified

| File | Change |
|:-----|:-------|
| `README.md` | Rebuilt as documentation hub with START HERE flow |
| `start-here.md` | Fixed mojibake; added link to GETTING_STARTED |
| `placement-control-panel.md` | Fixed mojibake |
| `content-standards.md` | Added source/evidence policy, naming, link, update conventions |

---

## Remaining

- [ ] Continuous maintenance: keep `DOCS_FILE_MAP.md` and `DOCS_CONTENT_REGISTRY.md` in sync with new files
- [ ] Periodic link re-audit (run `python scripts/validate_index.py` + manual docs link check)
- [ ] User journey re-test after any future docs changes

---

## Next

1. Verify all new docs files render correctly on GitHub
2. Re-run link audit after any future edits
3. Update this file after every meaningful change

---

## Final Documentation Architecture

```
docs/
├── README.md                    ← Documentation hub (START HERE)
├── GETTING_STARTED.md           ← "I just cloned this repo. What do I do?"
├── HOW_TO_USE.md                ← Practical user manual (workflows by scenario)
├── MASTER_NAVIGATION.md         ← Single routing document (track/role/company)
├── TRACKS.md                    ← Track documentation (Core Civil, HWRE, CFD, Non-Core)
├── ROLES.md                     ← Role documentation (role → track → topics → links)
├── COMPANIES.md                 ← Company index (company → domain → role → prep)
├── INTERVIEW_GUIDE.md           ← Interview system (technical + behavioural)
├── BEHAVIOURAL_HR_GUIDE.md      ← Behavioural / HR preparation guide
├── TESTING_GUIDE.md             ← Testing system (topic → subject → mixed → role → mock)
├── RAPID_REVISION_GUIDE.md      ← Rapid revision (1-day / 3-day / 7-day)
├── PREPARATION_WORKFLOW.md      ← Full system workflow (visual)
├── CONTENT_STANDARDS.md         ← Content quality gates (improved)
├── SOURCE_POLICY.md             ← Source / evidence policy (VERIFIED / SOURCE-DERIVED / INFERRED / PREDICTED)
├── CONTRIBUTING.md              ← Practical contribution guide
├── start-here.md                ← Legacy onboarding (kept, fixed, routes to GETTING_STARTED)
├── architecture.md              ← Canonical information architecture (kept)
├── placement-control-panel.md   ← Command center (kept, fixed)
├── roadmap.md                   ← Phased timeline (kept)
├── setup.md                     ← GitHub setup checklist (kept)
├── deep-critical-audit.md       ← Repository audit report (kept)
├── templates/                   ← 8 canonical page templates (kept)
├── audit/                       ← GATE-O-Pedia analysis (kept)
├── sources/                     ← Source provenance (kept)
└── _SYSTEM/
    ├── DOCS_FILE_MAP.md         ← Complete file inventory
    ├── DOCS_AUDIT_STATE.md      ← Live audit state (this file)
    ├── DOCS_LINK_AUDIT.md       ← Link audit
    └── DOCS_CONTENT_REGISTRY.md ← Content registry (prevents sprawl)
```

---

> **Last Updated:** 2026-09-06
> **Maintained by:** DKS IITK Civil/HWRE Placement 2026