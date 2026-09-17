# Canonical Source & Evidentiary Provenance Policy

> **Universal Evidence and Provenance Governance.** Every data point, compensation figure, interview format, and preparation benchmark across the repository must be strictly classified under one of six canonical evidentiary labels.

---

## 1. The 6-Tier Canonical Evidentiary Taxonomy

To eliminate governance ambiguity across technical notes, placement statistics, and mock assessments, all content adheres to this unified taxonomy:

| Canonical Label | Evidentiary Standard & Criteria | Primary Application Areas |
|:---|:---|:---|
| **`[VERIFIED]`** | Directly supported by authoritative, primary sources (official institute placement CSV, published peer-reviewed journal papers, standard university textbooks, or corporate job notifications). | Placement compensation, governing differential equations, textbook theorems. |
| **`[SOURCE-DERIVED]`** | Faithfully extracted or adapted from named external educational repositories or engineering standards (e.g., Bureau of Indian Standards IS codes, GATE-O-Pedia). | IS 456 / IS 800 codal clauses, standard handbook formulas. |
| **`[INFERRED]`** | Rigorous mathematical derivations, geometric proofs, or logical deductions from established empirical premises. | Step-by-step mock solutions, P&L cascading, hydraulic jump head loss. |
| **`[PREPARATION HEURISTIC]`** | Repository pedagogical targets, pacing rules, aspirational score bands, and industry practitioner rules-of-thumb (not statutory laws). | 45s/Q time limits, mock target score bands, VC $LTV:CAC$ ranges. |
| **`[SELF-REPORTED]`** | Anecdotal debriefs, candidate interview testimonies, alumni feedback, or self-evaluated mock diagnostic scores. | Student interview experiences, timed mock run scores, CPI reports. |
| **`[PREDICTED]`** | Forward-looking estimates, macroeconomic projections, or anticipated company hiring volumes. | Next-season recruitment estimates, hiring quota forecasts. |

---

## 2. Core Governance Rules

1. **Mandatory Labeling:** Every statistical claim, compensation figure, and benchmark table must display its canonical tag inline or in section headers.
2. **No False Equivalence:** Never present an `[INFERRED]` derivation or `[PREPARATION HEURISTIC]` as a `[VERIFIED]` institutional fact.
3. **Citation Requirement:** For all `[VERIFIED]` and `[SOURCE-DERIVED]` claims, cite the exact source document, chapter, or dataset filename in the supporting text or central [Source Registry](../resources/source-registry.md).
4. **Heuristic Safeguards:** All percentile mappings, target OA cutoffs, and mock score bands must be explicitly labeled `[PREPARATION HEURISTIC]` to prevent misinterpreting self-study benchmarks as official population percentiles.
5. **Transparency in Reporting:** Personal interview performance logs and mock completion velocity must be tagged `[SELF-REPORTED]` or `[OBSERVED IN TIMED RUN]`.

---

## 3. Provenance Verification Workflow

```
When adding or updating content:
   1. Determine the evidentiary basis of the claim.
   2. Assign the appropriate canonical label from the 6-tier taxonomy.
   3. If [VERIFIED] or [SOURCE-DERIVED], record origin in resources/source-registry.md.
   4. If [PREPARATION HEURISTIC] or [PREDICTED], append an explanatory note.
   5. Run repository quality checks to ensure zero unlabeled claims in technical notes.
```

---

## 4. Cross-Reference Governance Documents

- [Content Standards](content-standards.md) — 8 quality gates & definition of done
- [Source Registry](../resources/source-registry.md) — central catalog of repository data sources
- [Contributing Guide](CONTRIBUTING.md) — instructions for external PRs and additions

---

> **Back to:** [README](README.md) · [Main README](../README.md)