# 🧰 TOOLS_INDEX.md — Complete Software & Technology Index

> **Every tool in the repository, one row each.** Canonical source + priority + level + role.
> This is the single entry point for "which tool, where to learn it."

---

## Civil Engineering Software (Category A)

| Tool | Priority | Target Level | Canonical Source | Used For | Roles |
|:-----|:--------:|:------------:|:-----------------|:---------|:------|
| **AutoCAD** | P0 | L3 | [`tools/AutoCAD.md`](tools/AutoCAD.md) | 2D drafting, structural drawings | Structural, Construction, Geotech |
| **Civil 3D** | P2 | L2 | [`transportation/transportation-tech.md`](transportation/transportation-tech.md) | Road/highway design | Transportation |
| **STAAD.Pro** | P0 | L3 | [`tools/STAAD.md`](tools/STAAD.md) | Frame analysis, steel/concrete design | Structural, Construction |
| **ETABS** | P0 | L3 | [`tools/ETABS.md`](tools/ETABS.md) | Building analysis, seismic design | Structural |
| **SAP2000** | P1 | L2–L3 | [`tools/SAP2000.md`](tools/SAP2000.md) | General FEA, bridges | Structural, Geotech |
| **SAFE** | P2 | L2 | [`structural/structural-tech.md`](structural/structural-tech.md) | Foundation/slab design | Structural |
| **Revit** | P1 | L2–L3 | [`tools/Revit.md`](tools/Revit.md) | BIM authoring | BIM, Structural, Construction |
| **Navisworks** | P1 | L2–L3 | [`tools/Revit.md`](tools/Revit.md) | Clash detection, coordination | BIM |
| **Primavera P6** | P0 | L2–L3 | [`tools/Primavera.md`](tools/Primavera.md) | Project scheduling, CPM | Construction, PM |
| **MS Project** | P0 | L2–L3 | [`tools/Primavera.md`](tools/Primavera.md) | Gantt, scheduling | Construction, PM |
| **HEC-RAS** | P0 | L3 | [`deep-dives/hec-ras-walkthrough.md`](deep-dives/hec-ras-walkthrough.md) | River hydraulics, flood modeling | Water Resources, Hydrology |
| **HEC-HMS** | P1 | L2–L3 | [`deep-dives/hec-hms-tutorial.md`](deep-dives/hec-hms-tutorial.md) | Rainfall-runoff modeling | Hydrology, Water Resources |
| **EPANET** | P1 | L2–L3 | [`deep-dives/epanet-walkthrough.md`](deep-dives/epanet-walkthrough.md) | Water distribution networks | Water Resources, Environmental |
| **SWMM** | P1 | L2 | [`deep-dives/swmm-guide.md`](deep-dives/swmm-guide.md) | Urban drainage, stormwater | Environmental, Water Resources |
| **PLAXIS 2D** | P0 | L2–L3 | [`deep-dives/plaxis-2d-tutorial.md`](deep-dives/plaxis-2d-tutorial.md) | Geotechnical FEM | Geotech |
| **GeoStudio SLOPE/W** | P1 | L2 | [`deep-dives/geostudio-slopew-tutorial.md`](deep-dives/geostudio-slopew-tutorial.md) | Slope stability | Geotech |
| **ArcGIS / QGIS** | P0 | L2–L3 | [`tools/QGIS.md`](tools/QGIS.md) | GIS, spatial analysis, mapping | GIS, Water Resources, Hydrology |
| **Google Earth Engine** | P2 | L2 | [`gis/gis-tech.md`](gis/gis-tech.md) | Satellite analysis | GIS, Hydrology |

---

## CFD / Engineering Simulation (Category B)

| Tool | Priority | Target Level | Canonical Source | Used For | Roles |
|:-----|:--------:|:------------:|:-----------------|:---------|:------|
| **OpenFOAM** | P0 | L3 | [`deep-dives/openfoam-case-study.md`](deep-dives/openfoam-case-study.md) | CFD simulation | CFD, Research |
| **ParaView** | P1 | L2–L3 | [`cfd/cfd-tech.md`](cfd/cfd-tech.md) | CFD post-processing | CFD |
| **ANSYS / Abaqus** | P1 | L2 | [`cfd/cfd-tech.md`](cfd/cfd-tech.md) | Commercial FEA/CFD | CFD, Structural, Geotech |
| **MATLAB** | P1 | L2–L3 | [`programming/matlab.md`](programming/matlab.md) | Numerical computing | Research, CFD |

---

## Programming / Data (Category C)

| Tool | Priority | Target Level | Canonical Source | Used For | Roles |
|:-----|:--------:|:------------:|:-----------------|:---------|:------|
| **Python** | P0 | L3 | [`programming/python.md`](programming/python.md) | Automation, data, analysis | ALL |
| **SQL** | P1 | L2–L3 | [`programming/sql.md`](programming/sql.md) | Databases, querying | DA, BA, PM, GIS |
| **Excel** | P0 | L3 | [`tools/Excel.md`](tools/Excel.md) | Calculations, BOQ, analysis | ALL |
| **Power BI** | P2 | L2 | [`data/data-analytics-stack.md`](data/data-analytics-stack.md) | Dashboards, BI | DA, BA, Ops |
| **Git / GitHub** | P2 | L2 | [`programming/git.md`](programming/git.md) | Version control | Research, Tech |
| **Linux / Shell** | P2 | L2 | [`developer-tools/linux-dev-tools.md`](developer-tools/linux-dev-tools.md) | HPC, command line | CFD, Research |
| **C / C++** | P3 | L2 | [`programming/c-cpp.md`](programming/c-cpp.md) | Performance, DSA | Tech |

---

## Non-Core Technology (Category D — only where roles exist)

| Tool | Priority | Target Level | Canonical Source | Used For | Roles |
|:-----|:--------:|:------------:|:-----------------|:---------|:------|
| **DSA** | P0 | L3 | [`technology-careers/tech-careers.md`](technology-careers/tech-careers.md) | Coding interviews | SWE-adjacent |
| **APIs / REST** | P2 | L2 | [`product/product-tech.md`](product/product-tech.md) | Product/tech | PM, Tech |
| **Databases** | P1 | L2–L3 | [`programming/sql.md`](programming/sql.md) | Data storage | DA, BA, Tech |
| **Cloud / HPC** | P2 | L2 | [`computing/cloud-hpc.md`](computing/cloud-hpc.md) | Large-scale compute | Research, CFD |

---

## How to Use This Index

1. Find your **role** in [`SOFTWARE_ROLE_MATRIX.md`](SOFTWARE_ROLE_MATRIX.md)
2. Identify your **P0 tools** (must-learn)
3. Open the **canonical source** for each tool
4. Follow the **study → practice → project → test → interview** flow in each page
5. Track your progress in [`SOFTWARE_COMPLETENESS_MATRIX.md`](SOFTWARE_COMPLETENESS_MATRIX.md)

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| Role → Tool Mapping | [`SOFTWARE_ROLE_MATRIX.md`](SOFTWARE_ROLE_MATRIX.md) |
| Learning Roadmap | [`SOFTWARE_ROADMAP.md`](SOFTWARE_ROADMAP.md) |
| Priority System | [`priority-system.md`](priority-system.md) |
| Content Registry | [`_SYSTEM/SOFTWARE_CONTENT_REGISTRY.md`](_SYSTEM/SOFTWARE_CONTENT_REGISTRY.md) |

---

*One canonical source per tool. Update the registry when adding tools.*