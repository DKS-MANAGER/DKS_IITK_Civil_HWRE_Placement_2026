# SOFTWARE_REQUIRED_FILES.md — Required-File Audit

> For each role/tool: what exists, what is required, current quality, and action.
> Actions: `KEEP` · `EXTEND` · `CREATE` · `MERGE` · `MOVE` · `DELETE`

---

## P0 Tools (Placement-Critical)

| Role | Tool | Existing File | Required File | Current Quality | Action |
|:-----|:-----|:--------------|:--------------|:----------------|:-------|
| Structural / Construction | AutoCAD | `tools/AutoCAD.md` | Same (canonical) | PLACEMENT_READY | **KEEP** |
| All roles | Excel | `tools/Excel.md` | Same (canonical) | PLACEMENT_READY | **KEEP** |
| Structural | STAAD.Pro | `tools/STAAD.md` | Same (canonical) | PLACEMENT_READY | **KEEP** |
| Structural | ETABS | `tools/ETABS.md` | Same (canonical) | PLACEMENT_READY | **KEEP** |
| Water Resources | HEC-RAS | `deep-dives/hec-ras-walkthrough.md` | Same (canonical) | PLACEMENT_READY | **KEEP** |
| GIS / Water Resources | QGIS / ArcGIS | `tools/QGIS.md` | Same (canonical) | PLACEMENT_READY | **KEEP** |
| Construction / PM | Primavera P6 / MS Project | `tools/Primavera.md` | Same (canonical) | PLACEMENT_READY | **KEEP** |
| All roles | Python | `programming/python.md` | Same (canonical) | GOOD | **KEEP** (practice+tests in `practice/`+`tests/`) |
| Structural | SAP2000 | `tools/SAP2000.md` | Same (canonical) | PLACEMENT_READY | **KEEP** |

## P1 Tools (High-Value)

| Role | Tool | Existing File | Required File | Current Quality | Action |
|:-----|:-----|:--------------|:--------------|:----------------|:-------|
| BIM | Revit / Navisworks | `tools/Revit.md` | Same (canonical) | PLACEMENT_READY | **KEEP** |
| Hydrology | HEC-HMS | `deep-dives/hec-hms-tutorial.md` | Same | PLACEMENT_READY | **KEEP** |
| Water Supply | EPANET | `deep-dives/epanet-walkthrough.md` | Same | PLACEMENT_READY | **KEEP** |
| Urban Drainage | SWMM | `deep-dives/swmm-guide.md` | Same | PLACEMENT_READY | **KEEP** |
| Geotech | PLAXIS 2D | `deep-dives/plaxis-2d-tutorial.md` | Same | PLACEMENT_READY | **KEEP** |
| Geotech | GeoStudio SLOPE/W | `deep-dives/geostudio-slopew-tutorial.md` | Same | PLACEMENT_READY | **KEEP** |
| CFD | OpenFOAM | `deep-dives/openfoam-case-study.md` | Same | PLACEMENT_READY | **KEEP** |
| Data / BA / PM | SQL | `programming/sql.md` | Same | GOOD | **KEEP** |
| Research | MATLAB | `programming/matlab.md` | Same | GOOD | **KEEP** |

## P2/P3 Tools (Useful / Optional)

| Role | Tool | Existing File | Required File | Current Quality | Action |
|:-----|:-----|:--------------|:--------------|:----------------|:-------|
| Transportation | Civil 3D | `transportation/transportation-tech.md` | Same | PARTIAL | **KEEP** |
| CFD | ANSYS / Abaqus | `cfd/cfd-tech.md` | Same | PARTIAL | **KEEP** |
| Data | Power BI | `data/data-analytics-stack.md` | Same | PARTIAL | **KEEP** |
| Research | Git | `programming/git.md` | Same | PARTIAL | **KEEP** |
| Tech | C/C++ | `programming/c-cpp.md` | Same | PARTIAL | **KEEP** |

## System / Navigation Files

| File | Required File | Current Quality | Action |
|:-----|:--------------|:----------------|:-------|
| `_SYSTEM/SOFTWARE_AUDIT_STATE.md` | Same | GOOD | **KEEP** |
| `_SYSTEM/SOFTWARE_REPO_MAP.md` | Same | GOOD | **KEEP** |
| `_SYSTEM/SOFTWARE_CONTENT_REGISTRY.md` | Same | GOOD | **KEEP** |
| `_SYSTEM/SOFTWARE_REQUIRED_FILES.md` | Same | GOOD | **KEEP** |
| `_SYSTEM/FOLDER_QUEUE.md` | Same | GOOD | **KEEP** |
| `_SYSTEM/FOLDER_PROCESS_STATE.md` | Same | GOOD | **KEEP** |
| `SOFTWARE_ROLE_MATRIX.md` | Same | GOOD | **KEEP** |
| `SOFTWARE_ROADMAP.md` | Same | GOOD | **KEEP** |
| `TOOLS_INDEX.md` | Same | GOOD | **KEEP** |
| `SOFTWARE_COMPLETENESS_MATRIX.md` | Same | GOOD | **KEEP** |
| `SOFTWARE_RESUME_STRATEGY.md` | Same | GOOD | **KEEP** |

---

## Build Order (P0 → P1 → P2) — ALL COMPLETE

```
Phase 1: _SYSTEM infrastructure (DONE)
Phase 2: SOFTWARE_ROLE_MATRIX.md, TOOLS_INDEX.md, SOFTWARE_ROADMAP.md (DONE)
Phase 3: SOFTWARE_COMPLETENESS_MATRIX.md (DONE)
Phase 4: P0 tool pages (AutoCAD, Excel, STAAD, ETABS, QGIS, Primavera, SAP2000) (DONE)
Phase 5: P1 tool pages (Revit) + extend Python/SQL/MATLAB (DONE)
Phase 6: Practice system + test bank (DONE)
Phase 7: Company + theory linkage (DONE)
Phase 8: Verification + review (DONE — 825 links, 5/5 journeys)
```

---

> **Last Updated:** 2026-09-06