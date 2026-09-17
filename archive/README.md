# Historical & Archived Assets

> **Archive Subsystem** — Stores deprecated, superseded, historical migration artifacts, and prior-generation documents.
> Active placement preparation must NOT reference files in this directory.

---

## 1. Directory Structure & Inventory

```
archive/
├── README.md                          # Archive registry & explanation (This file)
└── legacy-non-core-aptitude/          # Pre-September 2026 condensed aptitude files
    ├── README.md                      # Deprecated aptitude index
    ├── quantitative/                  # 14 basic quantitative modules (superseded by aptitude/quant/)
    ├── logical_reasoning/             # Single reasoning practice file (superseded by aptitude/reasoning/)
    ├── verbal/                        # Basic verbal file (superseded by aptitude/verbal/)
    └── shortcuts/                     # Basic shortcuts file (superseded by aptitude/FORMULA_SHEET.md)
```

---

## 2. Archival Rationale & Canonical Mappings

| Archived Asset | Rationale for Archival | Canonical Replacement in Active Repository |
|:---------------|:-----------------------|:-------------------------------------------|
| `legacy-non-core-aptitude/quantitative/*` | Condensed early draft with 10 problems per topic; lacked rigorous Cat-8 cognitive taxonomy, master answer keys, and verification standards. | [`aptitude/quant/`](../aptitude/quant/README.md) (18 chapters, 720 questions, 100% verified keys) |
| `legacy-non-core-aptitude/logical_reasoning/*` | Single generic practice file with limited coverage. | [`aptitude/reasoning/`](../aptitude/reasoning/README.md) (10 modules, 400 questions, complete analytical derivations) |
| `legacy-non-core-aptitude/verbal/*` | Introductory verbal notes without placement-level RC passages. | [`aptitude/verbal/`](../aptitude/verbal/README.md) (9 modules, 372 questions) |
| `legacy-non-core-aptitude/shortcuts/*` | Basic arithmetic shortcuts. | [`aptitude/FORMULA_SHEET.md`](../aptitude/FORMULA_SHEET.md) and [`aptitude/RAPID_REVISION.md`](../aptitude/RAPID_REVISION.md) |

---

## 3. Governance Policy

- Archived content is preserved for historical provenance, audit trails, and version continuity.
- No active preparation guide, workflow, or assessment engine should route candidates to `archive/`.
- Links in active documentation should point to the canonical hubs: [`aptitude/`](../aptitude/README.md), [`core/`](../core/README.md), [`non-core/`](../non-core/README.md), [`prep/`](../prep/README.md), and [`software-and-tech/`](../software-and-tech/README.md).
