# GATE Civil — Repository Map

> Dependency and navigation map for the GATE Civil preparation system. Shows how the GATE layer connects to the detailed `02_02_core/` subject files.

## GATE System Flow

```
SYLLABUS (GATE_ROADMAP.md)
   ↓
MASTER_INDEX.md  ← 1–2 click entry to everything
   ↓
LEARN   → civil/gate-civil-notes.md  +  02_02_core/<subject>/*.md (detailed theory)
   ↓
FORMULAS → formulas/gate-civil-formulas.md  (canonical, P0–P3 tagged)
   ↓
EXAMPLES → practice/gate-civil-practice.md  (solved, verified)
   ↓
PYQs    → pyq/gate-civil-pyq.md
   ↓
TESTS   → mocks/gate-civil-mock-1.md  (+ topic tests in practice/)
   ↓
ERRORS  → ERROR_ANALYSIS.md
   ↓
REVISE  → RAPID_REVISION.md  +  revision_notes/gate-civil-revision.md
```

## Subject → Source Map

| GATE Subject | GATE Layer (this dir) | Detailed Theory (02_02_core/) |
| ------------ | --------------------- | ----------------------- |
| Engineering Mathematics | `civil/gate-civil-notes.md` §1, `formulas/` §1 | — (self-contained) |
| Engineering Mechanics | `formulas/` §2 | [`02_02_02_core/civil-engineering/fundamentals/engineering-mechanics.md`](../../fundamentals/engineering-mechanics.md) |
| Strength of Materials | `formulas/` §3 | [`02_02_02_core/civil-engineering/fundamentals/strength-of-materials.md`](../../fundamentals/strength-of-materials.md) |
| Structural Analysis | `formulas/` §4 | [`02_02_02_core/civil-engineering/structural-analysis/structural-analysis.md`](../../structural-analysis/structural-analysis.md) |
| RCC | `formulas/` §5 | [`02_02_02_core/civil-engineering/rcc/rcc-design.md`](../../rcc/rcc-design.md) |
| Steel | `formulas/` §6 | [`02_02_02_core/civil-engineering/steel/steel-design.md`](../../steel/steel-design.md) |
| Geotechnical | `formulas/` §7 | [`02_02_02_core/civil-engineering/geotechnical/geotechnical.md`](../../geotechnical/geotechnical.md) |
| Fluid Mechanics | `formulas/` §8 | [`02_02_02_02_02_02_core/hwre/hydraulics/hydraulics.md`](../../hwre/hydraulics/hydraulics.md) |
| Hydraulics / Open Channel | `formulas/` §9 | [`02_02_02_02_02_02_core/hwre/hydraulics/hydraulics.md`](../../hwre/hydraulics/hydraulics.md) |
| Hydrology | `formulas/` §10 | [`02_02_02_02_02_02_core/hwre/hydrology/hydrology.md`](../../hwre/hydrology/hydrology.md) |
| Environmental | `formulas/` §11 | [`02_02_02_core/civil-engineering/environmental/environmental-engineering.md`](../../environmental/environmental-engineering.md) |
| Transportation | `formulas/` §12 | [`02_02_02_core/civil-engineering/transportation/transportation-engineering.md`](../../transportation/transportation-engineering.md) |
| Geomatics / Surveying | `formulas/` §13 | [`02_02_02_core/civil-engineering/geoinformatics/geoinformatics.md`](../../geoinformatics/geoinformatics.md) |
| Construction Management | `formulas/` §14 | [`02_02_02_core/civil-engineering/infrastructure/infrastructure-engineering-management.md`](../../infrastructure/infrastructure-engineering-management.md) |

## Inter-Subject Dependencies

```
Engineering Mechanics
   → Strength of Materials
      → Structural Analysis
         → RCC / Steel

Fluid Mechanics
   → Hydraulics (Open Channel)
      → Hydrology

Engineering Mathematics
   → Numerical Methods (used across all subjects)

Geotechnical (Soil Mechanics)
   → Foundation Engineering
```

## Canonical Source Principle

- **One canonical source per formula**: the formula sheet is the single GATE formula reference; subject files link to it rather than re-deriving conflicting variants.
- **One canonical source per concept**: detailed theory lives in `02_02_core/<subject>/`; the GATE layer links to it.
- **PYQs**: only in `pyq/gate-civil-pyq.md` — no duplicate question banks elsewhere.