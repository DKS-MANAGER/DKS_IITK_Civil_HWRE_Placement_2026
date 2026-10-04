# SOFTWARE_CONTENT_REGISTRY.md — Canonical Source Registry

> **Purpose:** Prevent duplication. Every tool has ONE canonical source. All other pages link to it.
> If a tool is used by multiple tracks, do NOT create multiple versions — link to the canonical source.

---

## Canonical Source Table

| Tool | Canonical Source | Track(s) That Link Here | Status |
|:-----|:-----------------|:------------------------|:-------|
| **AutoCAD** | `tools/AutoCAD.md` (EXISTS) | structural, construction, geotech, transportation | P0 |
| **Excel** | `tools/Excel.md` (EXISTS) | ALL tracks | P0 |
| **STAAD.Pro** | `tools/STAAD.md` (EXISTS) | structural, construction | P0 |
| **ETABS** | `tools/ETABS.md` (EXISTS) | structural | P0 |
| **SAP2000** | `tools/SAP2000.md` (EXISTS) | structural, geotech | P1 |
| **HEC-RAS** | `deep-dives/hec-ras-walkthrough.md` (EXISTS) | hwre, hydrology, sediment, gis | P0 |
| **HEC-HMS** | `deep-dives/hec-hms-tutorial.md` (EXISTS) | hydrology, hwre | P1 |
| **EPANET** | `deep-dives/epanet-walkthrough.md` (EXISTS) | environmental, hwre | P1 |
| **SWMM** | `deep-dives/swmm-guide.md` (EXISTS) | environmental, hwre | P1 |
| **PLAXIS 2D** | `deep-dives/plaxis-2d-tutorial.md` (EXISTS) | geotechnical | P1 |
| **GeoStudio SLOPE/W** | `deep-dives/geostudio-slopew-tutorial.md` (EXISTS) | geotechnical | P1 |
| **OpenFOAM** | `deep-dives/openfoam-case-study.md` (EXISTS) | cfd, sediment, research | P1 |
| **QGIS / ArcGIS** | `tools/QGIS.md` (EXISTS) | gis, hwre, hydrology, environmental | P0 |
| **Primavera P6 / MS Project** | `tools/Primavera.md` (EXISTS) | construction, operations | P0 |
| **Revit / Navisworks** | `tools/Revit.md` (EXISTS) | bim, structural, construction | P1 |
| **Python** | `programming/python.md` (EXISTS) | ALL tracks | P0 |
| **MATLAB** | `programming/matlab.md` (EXISTS) | research, cfd | P1 |
| **SQL** | `programming/sql.md` (EXISTS) | data, product, operations, consulting | P1 |
| **Git** | `programming/git.md` (EXISTS) | research, tech | P2 |
| **C/C++** | `programming/c-cpp.md` (EXISTS) | tech | P2 |
| **Power BI** | `data/data-analytics-stack.md` (EXISTS) | data, operations | P2 |
| **ANSYS / Abaqus** | `cfd/cfd-tech.md` (EXISTS) | cfd, structural, geotech | P2 |
| **Civil 3D** | `transportation/transportation-tech.md` (EXISTS) | transportation | P2 |
| **Navisworks** | `tools/Revit.md` (EXISTS, includes Navisworks) | bim | P1 |

---

## Duplication Rules

1. **One canonical source per tool.** No tool page is duplicated across tracks.
2. **Branch roadmaps** (`structural-tech.md`, `hwre-tech-roadmap.md`, etc.) remain as **decision/overview** pages — they map tools to roles and link to canonical sources.
3. **Deep-dives** are the canonical **hands-on study material** for their tool.
4. **`software-interview-questions.md`** is the canonical **question bank**; tool pages link to it rather than re-listing all questions.
5. **New tool pages** must be registered here BEFORE creation.

---

## Registration Log

| Date | Tool | File | Action |
|:-----|:-----|:-----|:-------|
| 2026-09-06 | AutoCAD | `tools/AutoCAD.md` | REGISTERED (P0) |
| 2026-09-06 | Excel | `tools/Excel.md` | REGISTERED (P0) |
| 2026-09-06 | STAAD.Pro | `tools/STAAD.md` | REGISTERED (P0) |
| 2026-09-06 | ETABS | `tools/ETABS.md` | REGISTERED (P0) |
| 2026-09-06 | SAP2000 | `tools/SAP2000.md` | REGISTERED (P1) |
| 2026-09-06 | QGIS / ArcGIS | `tools/QGIS.md` | REGISTERED (P0) |
| 2026-09-06 | Primavera P6 / MS Project | `tools/Primavera.md` | REGISTERED (P0) |
| 2026-09-06 | Revit / Navisworks | `tools/Revit.md` | REGISTERED (P1) |
| 2026-09-06 | Folder queue | `_SYSTEM/FOLDER_QUEUE.md` | REGISTERED (system) |
| 2026-09-06 | Folder process state | `_SYSTEM/FOLDER_PROCESS_STATE.md` | REGISTERED (system) |
| 2026-09-06 | Link audit tool | `scripts/validate_software_links.py` | REGISTERED (tooling) |

---

> **Last Updated:** 2026-09-06