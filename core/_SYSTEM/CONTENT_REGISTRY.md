# Content Registry — Canonical Source Tracking

> **Purpose:** Track duplication across `core/`. One canonical source per concept; all other files link to it.
> **Action:** `KEEP` = canonical · `LINK` = link to canonical · `MERGE` = merge into canonical · `REMOVE` = delete

---

## Canonical Sources

| Concept | Canonical File | Used By | Duplicate Files | Action |
|---------|---------------|---------|-----------------|--------|
| Fluid Mechanics | `hwre/hydraulics/hydraulics.md` | GATE, HWRE, Fundamentals | `fundamentals/civil-engineering-foundations.md` (§Fluid) | LINK |
| Open Channel Flow | `hwre/open_channel_flow/open-channel-flow.md` | GATE, HWRE | `fundamentals/civil-engineering-foundations.md` (§OCF) | LINK |
| Hydrology | `hwre/hydrology/hydrology.md` | GATE, HWRE | `fundamentals/civil-engineering-foundations.md` (§Hydrology) | LINK |
| Groundwater | `hwre/water_supply/groundwater.md` | GATE, HWRE | `fundamentals/civil-engineering-foundations.md` (§GW) | LINK |
| Water Resources | `hwre/water_resources/water-resources-engineering.md` | GATE, HWRE | `fundamentals/civil-engineering-foundations.md` (§WRE) | LINK |
| Wastewater | `hwre/wastewater/wastewater-engineering.md` | HWRE, Environmental | `environmental/environmental-engineering.md` (§Wastewater) | LINK |
| Water Supply | `hwre/water_supply/water-supply.md` | HWRE, Environmental | `environmental/environmental-engineering.md` (§Water) | LINK |
| Engineering Mechanics | `fundamentals/engineering-mechanics.md` | GATE, Structures | `structures/structures.md` (§SOM) | LINK |
| Strength of Materials | `fundamentals/strength-of-materials.md` | GATE, Structures | `structures/structures.md` (§SOM) | LINK |
| Structural Analysis | `structural-analysis/structural-analysis.md` | GATE, Structures | `structures/structures.md` (§Analysis) | LINK |
| RCC Design | `rcc/rcc-design.md` | GATE, Structures | `structures/structures.md` (§RCC) | LINK |
| Steel Design | `steel/steel-design.md` | GATE, Structures | `structures/structures.md` (§Steel) | LINK |
| Geotechnical | `geotechnical/geotechnical.md` | GATE, Structures | `structures/structures.md` (§Geotech) | LINK |
| Transportation | `transportation/transportation-engineering.md` | GATE, Infrastructure | — | KEEP |
| Geoinformatics | `geoinformatics/geoinformatics.md` | GATE, Infrastructure | — | KEEP |
| Infrastructure Mgmt | `infrastructure/infrastructure-engineering-management.md` | GATE, Fundamentals | — | KEEP |
| Environmental | `environmental/environmental-engineering.md` | GATE, HWRE | — | KEEP |
| GATE Formulas | `gate/formulas/gate-civil-formulas.md` | All tracks | `fundamentals/civil-engineering-foundations.md` | LINK |
| HWRE Formulas | `hwre/formulas/hwre-formulas.md` | HWRE | `fundamentals/civil-engineering-foundations.md` | LINK |

---

## Duplicate Analysis

| Duplicate | Canonical | Overlap | Action |
|-----------|-----------|---------|--------|
| `structures/structures.md` §RCC | `rcc/rcc-design.md` | High — IS 456 provisions, beam/column design | **LINK** — replace RCC section with link to canonical |
| `structures/structures.md` §Steel | `steel/steel-design.md` | High — IS 800 provisions, connections | **LINK** — replace Steel section with link to canonical |
| `structures/structures.md` §SOM | `fundamentals/strength-of-materials.md` | High — stress/strain, bending | **LINK** — replace SOM section with link to canonical |
| `fundamentals/civil-engineering-foundations.md` | `gate/formulas/gate-civil-formulas.md` + `hwre/formulas/hwre-formulas.md` | Medium — formula summary | **LINK** — keep as revision, add canonical links |
| `environmental/environmental-engineering.md` §Wastewater | `hwre/wastewater/wastewater-engineering.md` | Medium — ASP, BOD | **LINK** — keep summary, link to canonical |

---

## Key Principle

> **One source per concept.** Subject guides link to the canonical formula sheet. Revision sheets summarize + link back. No file should be the sole source of a concept that exists elsewhere.