# Repository Setup Checklist

This file documents the one-time manual steps required to bring the repository to production-grade status on GitHub.

## 1. Default Branch

The local default branch has been renamed to `main`. On GitHub:

1. Go to **Settings → Branches → Default branch**.
2. Change the default from `master` to `main`.
3. Delete the old `master` branch from the remote after confirming `main` is live.

## 2. Repository Metadata

Populate the GitHub "About" section and topics:

- **Description:** Curated placement-prep knowledge base for IITK Civil/HWRE DEEC 2026. Synthesizes 10 repositories and 1 gist into structured, cross-referenced notes with full source attribution.
- **Topics:** `civil-engineering`, `placements-2026`, `iit-kanpur`, `interview-prep`, `fluid-mechanics`, `gate-ce`, `openfoam`, `study-notes`

## 3. Badges

The README now uses live shields.io badges. If you add CI workflows, update the badge URLs to match the new workflow filenames.

## 4. Pre-commit Hook

Install the local validation hook:

```bash
pip install pre-commit
pre-commit install
```

This ensures `index/master_index.md` references are validated and `index/file_inventory.csv` is regenerated on every commit.

## 5. Community Files

The following files have been added and are ready to commit:

- `CONTRIBUTING.md` — contribution standards and code of conduct
- `.github/ISSUE_TEMPLATE/material-request.md`
- `.github/ISSUE_TEMPLATE/bug-report.md`
- `.github/ISSUE_TEMPLATE/feature-request.md`
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/workflows/markdown-lint.yml`
- `.github/workflows/latex-python-check.yml`
- `.github/workflows/content-audit.yml`

## 6. Directory Parity

The `cfd-cases/` directory has been added with a placeholder README. Populate it with OpenFOAM cases as needed.

## 7. Roadmap Deduplication

The inline roadmap in README.md has been replaced with a link to `placement-roadmap.md`. Keep the detailed timeline in the standalone file.

## 8. Root Standards

- `.gitignore` — excludes OS, editor, LaTeX, Python, OpenFOAM, and Git artifacts
- `.editorconfig` — enforces LF line endings, UTF-8, and consistent indentation

## Commit Convention

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add turbulence modeling notes
fix: correct broken link in hydraulics
docs: update README quick start
chore: regenerate file inventory
```

Avoid bulk-dump commits. Keep changes atomic and reviewable.
