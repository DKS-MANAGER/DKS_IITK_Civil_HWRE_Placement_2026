# 🎯 SOFTWARE_ROLE_MATRIX.md — Role → Tool Mapping

> **Which software should I learn for my target role?**
> Every mapping below is grounded in **actual company evidence** from [`prep/company-profiles/`](../prep/company-profiles/) and the [`placement_data.csv`](../../Civil_Placement_IITK/placement_data.csv).
> Priority: **P0** = Required · **P1** = High-value · **P2** = Useful · **P3** = Optional.

---

## How to Read This Matrix

```
Role → Must Know (P0) → Useful (P1) → Optional (P2/P3)
Each tool links to its canonical study source.
```

---

## Core Civil Roles

### Structural Engineer

| Priority | Tool | Level | Canonical Source | Company Evidence |
|:--------:|:-----|:-----:|:-----------------|:-----------------|
| **P0** | AutoCAD | L3 | [`tools/AutoCAD.md`](tools/AutoCAD.md) | L&T, SPECTRUM, TT, Hilti, ASC |
| **P0** | STAAD.Pro | L3 | [`tools/STAAD.md`](tools/STAAD.md) | L&T, SPECTRUM, ASC, BPCL |
| **P0** | ETABS | L3 | [`tools/ETABS.md`](tools/ETABS.md) | TT, SPECTRUM, Hilti, Smarttrak |
| **P0** | Excel | L3 | [`tools/Excel.md`](tools/Excel.md) | Universal |
| **P1** | SAP2000 | L2–L3 | [`tools/SAP2000.md`](tools/SAP2000.md) | TT, Hilti, L&T |
| **P1** | Revit | L2 | [`tools/Revit.md`](tools/Revit.md) | TT, Godrej |
| **P2** | Python | L2 | [`programming/python.md`](programming/python.md) | Automation |

### Geotechnical Engineer

| Priority | Tool | Level | Canonical Source | Company Evidence |
|:--------:|:-----|:-----:|:-----------------|:-----------------|
| **P0** | PLAXIS 2D | L2–L3 | [`deep-dives/plaxis-2d-tutorial.md`](deep-dives/plaxis-2d-tutorial.md) | Reliance New Energy |
| **P0** | Excel | L3 | [`tools/Excel.md`](tools/Excel.md) | Universal |
| **P1** | GeoStudio SLOPE/W | L2 | [`deep-dives/geostudio-slopew-tutorial.md`](deep-dives/geostudio-slopew-tutorial.md) | Reliance New Energy |
| **P1** | AutoCAD | L2 | [`tools/AutoCAD.md`](tools/AutoCAD.md) | Foundation plans |
| **P2** | GIS | L2 | [`tools/QGIS.md`](tools/QGIS.md) | Site mapping |

### Transportation Engineer

| Priority | Tool | Level | Canonical Source | Company Evidence |
|:--------:|:-----|:-----:|:-----------------|:-----------------|
| **P0** | AutoCAD | L2–L3 | [`tools/AutoCAD.md`](tools/AutoCAD.md) | ASC Infratech |
| **P0** | Excel | L3 | [`tools/Excel.md`](tools/Excel.md) | Universal |
| **P1** | Civil 3D | L2 | [`transportation/transportation-tech.md`](transportation/transportation-tech.md) | ASC Infratech |
| **P1** | GIS | L2 | [`tools/QGIS.md`](tools/QGIS.md) | Road alignment |
| **P2** | STAAD.Pro | L2 | [`tools/STAAD.md`](tools/STAAD.md) | Bridge components |

### Water Resources Engineer

| Priority | Tool | Level | Canonical Source | Company Evidence |
|:--------:|:-----|:-----:|:-----------------|:-----------------|
| **P0** | HEC-RAS | L3 | [`deep-dives/hec-ras-walkthrough.md`](deep-dives/hec-ras-walkthrough.md) | Vassarlabs (explicit) |
| **P0** | Excel | L3 | [`tools/Excel.md`](tools/Excel.md) | Universal |
| **P1** | HEC-HMS | L2–L3 | [`deep-dives/hec-hms-tutorial.md`](deep-dives/hec-hms-tutorial.md) | Vassarlabs |
| **P1** | QGIS / ArcGIS | L2–L3 | [`tools/QGIS.md`](tools/QGIS.md) | Vassarlabs, GIST |
| **P1** | Python | L2–L3 | [`programming/python.md`](programming/python.md) | Vassarlabs |
| **P2** | EPANET | L2 | [`deep-dives/epanet-walkthrough.md`](deep-dives/epanet-walkthrough.md) | Rodic |

### Environmental Engineer

| Priority | Tool | Level | Canonical Source | Company Evidence |
|:--------:|:-----|:-----:|:-----------------|:-----------------|
| **P0** | Excel | L3 | [`tools/Excel.md`](tools/Excel.md) | Universal |
| **P1** | EPANET | L2–L3 | [`deep-dives/epanet-walkthrough.md`](deep-dives/epanet-walkthrough.md) | Rodic |
| **P1** | SWMM | L2 | [`deep-dives/swmm-guide.md`](deep-dives/swmm-guide.md) | Urban drainage |
| **P1** | AutoCAD | L2 | [`tools/AutoCAD.md`](tools/AutoCAD.md) | Rodic (process flow) |
| **P2** | GIS | L2 | [`tools/QGIS.md`](tools/QGIS.md) | EIA mapping |

### Construction / Project Engineer

| Priority | Tool | Level | Canonical Source | Company Evidence |
|:--------:|:-----|:-----:|:-----------------|:-----------------|
| **P0** | AutoCAD | L3 | [`tools/AutoCAD.md`](tools/AutoCAD.md) | L&T, Godrej, BPCL |
| **P0** | Excel | L3 | [`tools/Excel.md`](tools/Excel.md) | Universal |
| **P0** | Primavera P6 / MS Project | L2–L3 | [`tools/Primavera.md`](tools/Primavera.md) | L&T, Godrej, ITC, BPCL, HPCL |
| **P1** | STAAD.Pro | L2 | [`tools/STAAD.md`](tools/STAAD.md) | L&T, BPCL |
| **P1** | Revit | L2 | [`tools/Revit.md`](tools/Revit.md) | Godrej |

### BIM Engineer

| Priority | Tool | Level | Canonical Source | Company Evidence |
|:--------:|:-----|:-----:|:-----------------|:-----------------|
| **P0** | Revit | L3 | [`tools/Revit.md`](tools/Revit.md) | TT, Godrej |
| **P0** | Navisworks | L2–L3 | [`tools/Revit.md`](tools/Revit.md) | BIM coordination |
| **P1** | AutoCAD | L2 | [`tools/AutoCAD.md`](tools/AutoCAD.md) | 2D extraction |
| **P2** | Dynamo | L2 | [`bim/bim-tech.md`](bim/bim-tech.md) | Automation |

### Hydrologist

| Priority | Tool | Level | Canonical Source | Company Evidence |
|:--------:|:-----|:-----:|:-----------------|:-----------------|
| **P0** | HEC-HMS | L3 | [`deep-dives/hec-hms-tutorial.md`](deep-dives/hec-hms-tutorial.md) | Vassarlabs |
| **P0** | HEC-RAS | L2–L3 | [`deep-dives/hec-ras-walkthrough.md`](deep-dives/hec-ras-walkthrough.md) | Vassarlabs |
| **P1** | QGIS / ArcGIS | L2–L3 | [`tools/QGIS.md`](tools/QGIS.md) | Vassarlabs, GIST |
| **P1** | Python | L2 | [`programming/python.md`](programming/python.md) | Data analysis |
| **P2** | Google Earth Engine | L2 | [`gis/gis-tech.md`](gis/gis-tech.md) | Satellite flood mapping |

### GIS / Survey Engineer

| Priority | Tool | Level | Canonical Source | Company Evidence |
|:--------:|:-----|:-----:|:-----------------|:-----------------|
| **P0** | QGIS / ArcGIS | L3 | [`tools/QGIS.md`](tools/QGIS.md) | Vassarlabs, GIST |
| **P0** | SQL / PostGIS | L2–L3 | [`programming/sql.md`](programming/sql.md) | GIST |
| **P1** | Python (GeoPandas) | L2–L3 | [`programming/python.md`](programming/python.md) | GIST |
| **P2** | Google Earth Engine | L2 | [`gis/gis-tech.md`](gis/gis-tech.md) | GIST |

### CFD / Simulation Engineer

| Priority | Tool | Level | Canonical Source | Company Evidence |
|:--------:|:-----|:-----:|:-----------------|:-----------------|
| **P0** | OpenFOAM | L3 | [`deep-dives/openfoam-case-study.md`](deep-dives/openfoam-case-study.md) | AgniKul Cosmos |
| **P0** | Python | L3 | [`programming/python.md`](programming/python.md) | AgniKul |
| **P0** | Linux / ParaView | L2–L3 | [`developer-tools/linux-dev-tools.md`](developer-tools/linux-dev-tools.md) | CFD workflow |
| **P1** | ANSYS / Abaqus | L2 | [`cfd/cfd-tech.md`](cfd/cfd-tech.md) | Smarttrak, TuTr |
| **P2** | MATLAB | L2 | [`programming/matlab.md`](programming/matlab.md) | Numerical methods |

---

## Non-Core / Tech-Adjacent Roles

### Data Analyst

| Priority | Tool | Level | Canonical Source | Company Evidence |
|:--------:|:-----|:-----:|:-----------------|:-----------------|
| **P0** | Excel | L3 | [`tools/Excel.md`](tools/Excel.md) | Axis Bank, Mu Sigma |
| **P0** | SQL | L3 | [`programming/sql.md`](programming/sql.md) | Accenture, Blitz |
| **P0** | Python | L3 | [`programming/python.md`](programming/python.md) | Accenture, Barclays |
| **P1** | Power BI | L2–L3 | [`data/data-analytics-stack.md`](data/data-analytics-stack.md) | Axis Bank |

### Business Analyst

| Priority | Tool | Level | Canonical Source | Company Evidence |
|:--------:|:-----|:-----:|:-----------------|:-----------------|
| **P0** | Excel | L3 | [`tools/Excel.md`](tools/Excel.md) | Universal |
| **P0** | SQL | L2–L3 | [`programming/sql.md`](programming/sql.md) | Battery Smart |
| **P1** | Power BI | L2 | [`data/data-analytics-stack.md`](data/data-analytics-stack.md) | Axis Bank |
| **P2** | Python | L2 | [`programming/python.md`](programming/python.md) | Analytics |

### Product Manager / Product Analyst

| Priority | Tool | Level | Canonical Source | Company Evidence |
|:--------:|:-----|:-----:|:-----------------|:-----------------|
| **P0** | Excel | L3 | [`tools/Excel.md`](tools/Excel.md) | Universal |
| **P0** | SQL | L2–L3 | [`programming/sql.md`](programming/sql.md) | Product roles |
| **P1** | Analytics / Metrics | L2 | [`product/product-tech.md`](product/product-tech.md) | PM roles |
| **P2** | Python | L2 | [`programming/python.md`](programming/python.md) | Funnel analysis |

### Consultant / Strategy

| Priority | Tool | Level | Canonical Source | Company Evidence |
|:--------:|:-----|:-----:|:-----------------|:-----------------|
| **P0** | Excel | L3 | [`tools/Excel.md`](tools/Excel.md) | BCG, consulting |
| **P0** | PowerPoint | L3 | [`consulting/consulting-tech.md`](consulting/consulting-tech.md) | Consulting |
| **P1** | SQL | L1–L2 | [`programming/sql.md`](programming/sql.md) | Data-driven cases |

### Software Engineer (Tech-Adjacent)

| Priority | Tool | Level | Canonical Source | Company Evidence |
|:--------:|:-----|:-----:|:-----------------|:-----------------|
| **P0** | DSA / Coding | L3 | [`technology-careers/tech-careers.md`](technology-careers/tech-careers.md) | Hubstream, Deltax, Darwinbox |
| **P0** | SQL | L2–L3 | [`programming/sql.md`](programming/sql.md) | Expeditors, CEI |
| **P1** | OOP / Java / Python | L2–L3 | [`programming/c-cpp.md`](programming/c-cpp.md) | BNY, Cadence |
| **P2** | System Design | L2 | [`technology-careers/tech-careers.md`](technology-careers/tech-careers.md) | Product companies |

---

## Quick Reference Table

| Role | Must Know (P0) | Useful (P1) | Optional (P2/P3) |
|:-----|:---------------|:------------|:-----------------|
| Structural Engineer | AutoCAD, STAAD, ETABS, Excel | SAP2000, Revit | Python |
| Geotechnical Engineer | PLAXIS, Excel | GeoStudio, AutoCAD | GIS |
| Transportation Engineer | AutoCAD, Excel | Civil 3D, GIS | STAAD |
| Water Resources Engineer | HEC-RAS, Excel | HEC-HMS, QGIS, Python | EPANET |
| Environmental Engineer | Excel | EPANET, SWMM, AutoCAD | GIS |
| Construction / Project Eng | AutoCAD, Excel, Primavera | STAAD, Revit | Power BI |
| BIM Engineer | Revit, Navisworks | AutoCAD | Dynamo |
| Hydrologist | HEC-HMS, HEC-RAS | QGIS, Python | GEE |
| GIS / Survey Engineer | QGIS/ArcGIS, SQL | Python (GeoPandas) | GEE |
| CFD Engineer | OpenFOAM, Python, Linux | ANSYS, ParaView | MATLAB |
| Data Analyst | Excel, SQL, Python | Power BI | Tableau |
| Business Analyst | Excel, SQL | Power BI | Python |
| Product Manager | Excel, SQL | Analytics | Python |
| Consultant | Excel, PowerPoint | SQL | Power BI |
| Software Engineer | DSA, SQL | OOP/Java/Python | System Design |

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| Role Roadmaps | [`role-roadmaps.md`](role-roadmaps.md) |
| Branch Roadmaps | [`branch-roadmaps.md`](branch-roadmaps.md) |
| Priority System | [`priority-system.md`](priority-system.md) |
| Tool Index | [`TOOLS_INDEX.md`](TOOLS_INDEX.md) |
| Company Profiles | [`../prep/company-profiles/company-profiles.md`](../prep/company-profiles/company-profiles.md) |

---

*Grounded in company evidence from the repository. Update when new placement data arrives.*