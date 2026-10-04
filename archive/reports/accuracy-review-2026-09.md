# Content Accuracy Review — September 2026

> Scope: factual accuracy of placement data and technical content across the repo
> (~554 Markdown files). Ground truth for company/CTC data is
> [`placement_data.csv`](../../Civil_Placement_IITK/placement_data.csv) — the IITK
> 2025-26 placement export (516 postings, 276 unique companies).
> This is a spot-check, not an exhaustive line-by-line audit.

## Summary

| Severity | Finding | Status |
|---|---|---|
| HIGH | `resources/placement-data.md` was a stale, partly-hallucinated aggregate | **Fixed** — rebuilt from CSV, civil-scoped |
| HIGH | Stray Chinese text (machine-translation artifact) in 7 files | **Fixed** — replaced with English; added `quality_check.py` guard |
| MEDIUM | L&T CTC stated three different ways across the repo | **Fixed** — reconciled to CSV (MT ₹7.0L / PGET ₹6.25L) |
| MEDIUM | Company count drifted between "25", "25+" | **Fixed** — standardised on 25 civil companies |
| LOW | Per-company profiles spot-check | Clean — no change |
| LOW | Core technical content spot-check | Clean — no change |
| NOTE | Links to the sibling `Civil_Placement_IITK` repo break on a standalone clone | Open — see recommendation |

## HIGH — `resources/placement-data.md`

The previous version claimed "20+ companies tracked" while listing ~50 rows, and its
content was the **all-branch** IITK pool (Abacus.AI ₹60L, Barclays, BNY Mellon, Cadence,
CapitalOne, Baya Systems…) rather than the civil/HWRE subset the rest of the repo curates.

- It listed **"L&T | Engineer | ₹10-12L"** — a role and figure that do not exist in the
  CSV. The CSV shows L&T Management Trainee ₹7,00,000 and PGET ₹6,25,000, which
  [`civil-lt.md`](../prep/company-profiles/civil-lt.md) and the README already stated
  correctly.
- The "Company Category Breakdown" percentages were incoherent (IT 70%, Core 70%,
  Finance 45%… on a base of 20).
- The `## References` section was truncated to empty.

**Action taken:** rebuilt the file from the CSV, scoped to the 25 civil-relevant
companies, using the Tier 1/2/3 grading and CTCs already established in
[`company-profiles.md`](../prep/company-profiles/company-profiles.md). No estimated
figures; PSU CTCs are explicitly left unquoted because they move with DA/IDA revisions.

## HIGH — CJK (Chinese) text contamination

Machine-translation fragments were left embedded in otherwise-English lines — a
generation artifact. Found and corrected in:

| File | Was | Now |
|---|---|---|
| `core/fundamentals/civil-rapid-revision.md` | "time不确定 / time已知" | "activity times uncertain / known" |
| `core/hwre/hydraulics/hydraulics.md` | "Manning适用于open channel…" | "Manning applies to open channel…" |
| `core/infrastructure/infrastructure-engineering-management.md` | "Q = CiA/360;适用于…" | "Q = CiA/360; applies to…" |
| `prep/behavioral/civil-hwre-behavioral.md` | "可持续抽水" | "Sustainable pumping" |
| `prep/company-profiles/civil-lt.md` | "design计算" | "design calculations" |
| `_SYSTEM/CONTENT_MATRIX.md` | "Structures (综合)" | "Structures (combined)" |
| `_SYSTEM/REQUIRED_FILE_MATRIX.md` | "Structures (综合)" | "Structures (combined)" |

**Guard added:** `scripts/quality_check.py` now has a `check_cjk_contamination` pass that
fails the build on any `[　-鿿]` / Hangul / kana character in a `.md` file.
Verified: current count is 0.

## MEDIUM — cross-document consistency

- **L&T CTC** was "₹6.25–7L" (README, correct), "MT ₹7,00,000 / PGET ₹6,25,000"
  (civil-lt.md, correct) and "₹10-12L" (placement-data.md and the top table of
  company-profiles.md, wrong). The two wrong instances are now corrected to the CSV
  figure.
- **Company count** appeared as "25", "25+", and "25 civil-relevant companies". The
  README badge and directory-tree comment now both say 25. The canonical list is the
  "Civil Engineering — Company-Specific Placement Strategies" section of
  `company-profiles.md`; a note was added to that file steering readers there and
  flagging the Analytics/Tech tables above it as all-branch context.
- README's "276 companies (516 postings)" matches the CSV exactly — kept as the anchor.

## LOW — spot-checks that passed

- **Company profiles vs CSV:** Godrej Properties AM ₹18L, Thornton Tomasetti ₹7.5L,
  Hilti ₹17L, ITC AUT ₹31.25L, L&T — all match. The `civil-*.md` files use
  `[CSV]/[INFERRED]/[PREDICTED]` evidence tags with a source-row citation; this is the
  right pattern and should be the model for any new profile.
- **Core technical content:** `core/hwre/hydraulics/hydraulics.md` fundamentals
  (continuity, Bernoulli derivation from Euler, momentum equation, Reynolds thresholds
  Re < 2000 / 2000–4000) are correct. A full technical pass of all ten ~30 KB subject
  guides was **not** performed and is the recommended next audit.

## NOTE — external links

Several profiles cite `../../../Civil_Placement_IITK/placement_data.csv`, which lives in a
sibling repo. The file resolves on the author's machine but the link breaks for anyone
who clones only this repo. Recommendation: vendor a civil-scoped copy of the CSV into
`resources/` and repoint the links, or convert the citations to plain text.

## Verification performed

- `Import-Csv placement_data.csv` → 516 rows, 276 unique companies; compared L&T, Godrej,
  Thornton, Hilti, ITC rows against the profiles and README.
- Regex sweep `[　-鿿가-힣]` across all `.md` files — 0 hits after fixes.
- `python scripts/quality_check.py` — CJK pass green; pre-existing "broken link" reports
  from that script's naive resolver are unrelated to this review (`linkcheck_report.txt`
  reports 207 checked / 0 missing with the stricter checker).
