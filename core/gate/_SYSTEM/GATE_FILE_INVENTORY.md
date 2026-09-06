# GATE Civil — File Inventory

> Canonical inventory of every file under `core/gate/` plus the `core/` subject files that serve as detailed concept sources. Statuses: `EMPTY`, `INDEX_ONLY`, `PARTIAL`, `GOOD`, `COMPLETE`, `DUPLICATE`, `MISPLACED`.

## core/gate/ Files

| File | Purpose | Subject | Actual Content? | Questions? | Solutions? | Status |
| ---- | ------- | ------- | --------------- | ---------- | ---------- | ------ |
| [`README.md`](../README.md) | Navigation hub | All | Yes (links) | No | No | `PARTIAL` |
| [`MASTER_INDEX.md`](../MASTER_INDEX.md) | 1–2 click navigation | All | Yes (links) | No | No | `GOOD` |
| [`GATE_ROADMAP.md`](../GATE_ROADMAP.md) | Study roadmap | All | Yes | No | No | `GOOD` |
| [`GATE_30_60_90_DAY_PLAN.md`](../GATE_30_60_90_DAY_PLAN.md) | Time-boxed plan | All | Yes | No | No | `GOOD` |
| [`ERROR_ANALYSIS.md`](../ERROR_ANALYSIS.md) | Error tracking | All | Yes | No | No | `GOOD` |
| [`RAPID_REVISION.md`](../RAPID_REVISION.md) | Rapid revision | All | Yes | No | No | `GOOD` |
| [`civil/gate-civil-notes.md`](../civil/gate-civil-notes.md) | Topic-wise study | All | Partial (topic lists) | No | No | `PARTIAL` |
| [`formulas/gate-civil-formulas.md`](../formulas/gate-civil-formulas.md) | Formula reference | All | Yes | No | No | `GOOD` |
| [`practice/gate-civil-practice.md`](../practice/gate-civil-practice.md) | Solved problems | All | Yes | Yes | Yes | `PARTIAL` |
| [`revision_notes/gate-civil-revision.md`](../revision_notes/gate-civil-revision.md) | Revision cards | All | Yes | No | No | `GOOD` |
| [`pyq/gate-civil-pyq.md`](../pyq/gate-civil-pyq.md) | PYQ system | All | Yes | Yes | Yes | `GOOD` |
| [`mocks/gate-civil-mock-1.md`](../mocks/gate-civil-mock-1.md) | Full mock test | All | Yes | Yes | Yes | `GOOD` |
| [`_SYSTEM/GATE_FILE_INVENTORY.md`](GATE_FILE_INVENTORY.md) | This file | All | Yes | No | No | `GOOD` |
| [`_SYSTEM/GATE_REPO_MAP.md`](GATE_REPO_MAP.md) | Repo map | All | Yes | No | No | `GOOD` |
| [`_SYSTEM/GATE_AUDIT_STATE.md`](GATE_AUDIT_STATE.md) | Audit state | All | Yes | No | No | `GOOD` |
| [`_SYSTEM/GATE_COMPLETENESS_MATRIX.md`](GATE_COMPLETENESS_MATRIX.md) | Completeness scores | All | Yes | No | No | `GOOD` |

## core/ Subject Files (Detailed Concept Sources)

These files hold the detailed theory. The GATE layer links to them instead of duplicating content.

| File | Subject | Lines | Role in GATE System |
| ---- | ------- | ----: | ------------------- |
| [`core/fundamentals/engineering-mechanics.md`](../../fundamentals/engineering-mechanics.md) | Engineering Mechanics | 615 | EM theory + examples |
| [`core/fundamentals/strength-of-materials.md`](../../fundamentals/strength-of-materials.md) | Strength of Materials | 703 | SOM theory + examples |
| [`core/structural-analysis/structural-analysis.md`](../../structural-analysis/structural-analysis.md) | Structural Analysis | 678 | Analysis methods |
| [`core/rcc/rcc-design.md`](../../rcc/rcc-design.md) | RCC Design | 885 | IS 456 design |
| [`core/steel/steel-design.md`](../../steel/steel-design.md) | Steel Design | 852 | IS 800 design |
| [`core/structures/structures.md`](../../structures/structures.md) | Structures overview | 317 | Structures hub |
| [`core/geotechnical/geotechnical.md`](../../geotechnical/geotechnical.md) | Geotechnical | 276 | Soil mechanics + foundations |
| [`core/hwre/hydraulics/hydraulics.md`](../../hwre/hydraulics/hydraulics.md) | Hydraulics | 670 | Pipe + open channel |
| [`core/hwre/hydrology/hydrology.md`](../../hwre/hydrology/hydrology.md) | Hydrology | 586 | Hydrology + groundwater |
| [`core/hwre/water_resources/water-resources-engineering.md`](../../hwre/water_resources/water-resources-engineering.md) | Water Resources | 556 | Water resources |
| [`core/environmental/environmental-engineering.md`](../../environmental/environmental-engineering.md) | Environmental | 619 | Water/wastewater/air/solid |
| [`core/transportation/transportation-engineering.md`](../../transportation/transportation-engineering.md) | Transportation | 641 | Highway + traffic |
| [`core/geoinformatics/geoinformatics.md`](../../geoinformatics/geoinformatics.md) | Geomatics | 778 | Surveying + GIS/RS |
| [`core/infrastructure/infrastructure-engineering-management.md`](../../infrastructure/infrastructure-engineering-management.md) | Construction Mgmt | 810 | CPM/PERT + estimation |

## Audit Notes

- **Duplicates**: `gate/formulas/gate-civil-formulas.md` overlaps with subject files' formula sections — resolved by making the formula sheet the canonical GATE formula reference and linking subject files to it.
- **Misplaced**: none.
- **Empty**: none after rebuild.
- **Integrity**: all internal links verified by `scripts/quality_check.py` (0 broken links, 0 orphans).