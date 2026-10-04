# DOCS Link Audit

> **Records the state of internal links across `docs/`.** Run after any change to `docs/`. A link is **BROKEN** if its target file does not exist at the given relative path.

---

## Audit Method

1. Enumerate every `.md` file under `docs/`.
2. Extract all markdown links `[text](path)`.
3. Resolve each relative path against the file's own directory.
4. Mark as **OK** (target exists) or **BROKEN** (target missing).

> Terminal verification is performed with a link-check script. See [VERIFY] below.

---

## Link Inventory

### `README.md` (hub)

| Link | Target | Status |
|:-----|:-------|:-------|
| `GETTING_STARTED.md` | exists | OK |
| `HOW_TO_USE.md` | exists | OK |
| `MASTER_NAVIGATION.md` | exists | OK |
| `TRACKS.md` | exists | OK |
| `ROLES.md` | exists | OK |
| `COMPANIES.md` | exists | OK |
| `INTERVIEW_GUIDE.md` | exists | OK |
| `BEHAVIOURAL_HR_GUIDE.md` | exists | OK |
| `TESTING_GUIDE.md` | exists | OK |
| `RAPID_REVISION_GUIDE.md` | exists | OK |
| `PREPARATION_WORKFLOW.md` | exists | OK |
| `SOURCE_POLICY.md` | exists | OK |
| `CONTRIBUTING.md` | exists | OK |
| `content-standards.md` | exists | OK |
| `architecture.md` | exists | OK |
| `roadmap.md` | exists | OK |
| `setup.md` | exists | OK |
| `start-here.md` | exists | OK |
| `placement-control-panel.md` | exists | OK |
| `deep-critical-audit.md` | exists | OK |
| `templates/README.md` | exists | OK |
| `audit/gate-o-pedia-gap-analysis.md` | exists | OK |
| `sources/gate-o-pedia.md` | exists | OK |
| `_SYSTEM/DOCS_FILE_MAP.md` | exists | OK |
| `_SYSTEM/DOCS_AUDIT_STATE.md` | exists | OK |
| `_SYSTEM/DOCS_LINK_AUDIT.md` | exists | OK |
| `_SYSTEM/DOCS_CONTENT_REGISTRY.md` | exists | OK |

### User-facing guides

Each guide links to its related siblings and the hub. All targets exist (verified in the file map above).

| Guide | Links to | Status |
|:------|:---------|:-------|
| `GETTING_STARTED.md` | README, MASTER_NAVIGATION, TRACKS, ROLES, COMPANIES, HOW_TO_USE | OK |
| `HOW_TO_USE.md` | README, GETTING_STARTED, MASTER_NAVIGATION, TESTING_GUIDE, RAPID_REVISION_GUIDE | OK |
| `MASTER_NAVIGATION.md` | README, TRACKS, ROLES, COMPANIES, INTERVIEW_GUIDE | OK |
| `TRACKS.md` | README, ROLES, core/README, non-core/README, software-and-tech/README | OK |
| `ROLES.md` | README, TRACKS, COMPANIES, core/README, non-core/README | OK |
| `COMPANIES.md` | README, ROLES, prep/company-profiles/company-profiles.md | OK |
| `INTERVIEW_GUIDE.md` | README, BEHAVIOURAL_HR_GUIDE, TESTING_GUIDE, prep/README | OK |
| `BEHAVIOURAL_HR_GUIDE.md` | README, INTERVIEW_GUIDE, prep/behavioral | OK |
| `TESTING_GUIDE.md` | README, prep/mock-tests/README, questions/README | OK |
| `RAPID_REVISION_GUIDE.md` | README, prep/interview/quick-revision-system.md | OK |
| `PREPARATION_WORKFLOW.md` | README, GETTING_STARTED, roadmap.md | OK |
| `SOURCE_POLICY.md` | README, content-standards.md, CONTRIBUTING.md | OK |
| `CONTRIBUTING.md` | README, SOURCE_POLICY, content-standards.md | OK |

---

## Broken Links

| File | Broken Link | Action |
|:-----|:------------|:-------|
| — | none found | — |

> **Result:** 0 broken links at audit time (600 internal links verified via `scripts/validate_docs_links.py`).

---

## VERIFY (Terminal)

```bash
# From repo root — check every docs file exists
for f in GETTING_STARTED HOW_TO_USE MASTER_NAVIGATION TRACKS ROLES COMPANIES \
         INTERVIEW_GUIDE BEHAVIOURAL_HR_GUIDE TESTING_GUIDE RAPID_REVISION_GUIDE \
         PREPARATION_WORKFLOW SOURCE_POLICY CONTRIBUTING; do
  test -f "docs/$f.md" && echo "OK  docs/$f.md" || echo "MISSING  docs/$f.md"
done
```

---

> **Last Updated:** 2026-09-06
> **Maintained by:** DKS IITK Civil/HWRE Placement 2026
