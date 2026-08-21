# Contributing to DKS_IITK_Civil_HWRE_Placement_2026

Thank you for contributing. This guide ensures consistency across all notes, interviews, and resources.

## Pre-commit Checks

Install the pre-commit hook to validate index references and update the file inventory automatically:

```bash
pip install pre-commit
pre-commit install
```

The `validate-index` hook runs on every commit and ensures `index/master_index.md` references stay in sync with the file tree.

## Before You Start

1. Search existing issues and notes to avoid duplicates.
2. For large additions, open an issue first to align with maintainers.
3. Fork the repo and create a feature branch: `add/<topic>` or `fix/<file>`.

## Content Standards

- **Paraphrase, don't copy-paste.** Rewrite source material in your own words.
- **Cite sources.** Every note must end with a `## Sources` section listing original repositories.
- **Use templates.** Interview experiences use `templates/interview-answer-template.md`. Resource additions use `templates/study-plan-template.md`.
- **Anonymize.** Remove names, roll numbers, company-specific confidential prompts, and panel details.
- **Validate facts.** Mark resources as ✅ only after verification by 2+ peers.

## Branching & PRs

- Keep PRs single-purpose. One topic or fix per PR.
- Write a clear title and description. Link related issues with `Fixes #123`.
- PRs are reviewed weekly (Sundays) by a rotating maintainer.

## Issue Labels

- `good-first-issue` — quick wins for new contributors
- `material-request` — missing notes, books, or question banks
- `bug` — broken links, typos, incorrect derivations
- `enhancement` — structure, formatting, or tooling improvements

## Code of Conduct

Be respectful. This is a peer learning resource. Disagreements are welcome; personal attacks are not.
