# 🚗 Transportation Engineering Technology Roadmap

> **Branch:** Transportation Engineering
> **Tools mapped to highway design, traffic simulation, transport modelling, pavement analysis, and GIS.**

---

## Decision Tree

```
Transportation student → what tools?

1. AutoCAD / Civil 3D  → Highway design, geometric design (MUST)
2. GIS (ArcGIS/QGIS)  → Spatial analysis, transport planning (MUST)
3. Traffic simulation   → VISSIM / Synchro / SUMO (ROLE DEPENDENT)
4. Excel               → Data analysis, capacity calculations (MUST)
5. Python              → Data analysis, traffic data processing (HIGH ROI)
6. TransCAD            → Transport demand modeling (ROLE DEPENDENT)
7. MATLAB              → Numerical methods (ROLE DEPENDENT)
```

---

## Tool → Role Mapping

### Highway Design Engineer

| Tool | Tag | Level | Purpose |
|:-----|:----|:------|:--------|
| AutoCAD | `[MUST LEARN]` | L3 | 2D drafting, cross-sections |
| Civil 3D | `[MUST LEARN]` | L2–L3 | Roadway design, profiles, corridors |
| Excel | `[MUST LEARN]` | L3 | Calculations, pavement design |
| OpenRoads | `[ROLE DEPENDENT]` | L2 | Roadway design (Bentley alternative) |
| GIS | `[HIGH ROI]` | L2 | Route alignment, terrain analysis |

### Traffic Engineer

| Tool | Tag | Level | Purpose |
|:-----|:----|:------|:--------|
| Synchro / SimTraffic | `[MUST LEARN]` | L2–L3 | Signal timing, intersection analysis |
| PTV Vissim | `[HIGH ROI]` | L2 | Microscopic traffic simulation |
| SIDRA | `[HIGH ROI]` | L2 | Intersection capacity |
| Excel | `[MUST LEARN]` | L3 | Traffic data analysis, HCM calculations |
| Python | `[HIGH ROI]` | L2 | Traffic data processing |
| GIS | `[HIGH ROI]` | L2 | Network analysis, mapping |

### Transport Planning / Demand

| Tool | Tag | Level | Purpose |
|:-----|:----|:------|:--------|
| TransCAD | `[MUST LEARN]` | L2–L3 | Transport demand modeling (4-step model) |
| GIS (ArcGIS) | `[MUST LEARN]` | L2–L3 | Spatial analysis, zoning |
| Excel | `[MUST LEARN]` | L3 | Data processing, model calibration |
| Python | `[HIGH ROI]` | L2 | Data analysis, automation |
| SUMO | `[ROLE DEPENDENT]` | L2 | Agent-based transport simulation |

### Pavement Engineer

| Tool | Tag | Level | Purpose |
|:-----|:----|:------|:--------|
| Excel | `[MUST LEARN]` | L3 | Pavement design calculations |
| AutoCAD | `[MUST LEARN]` | L2 | Pavement drawings |
| HCS | `[ROLE DEPENDENT]` | L2 | Highway Capacity Manual analysis |
| GIS | `[ROLE DEPENDENT]` | L2 | Pavement management, mapping |

---

## Tool Details

### PTV Vissim

| Property | Value |
|:---------|:------|
| **What** | Microscopic multimodal traffic simulation |
| **Developer** | PTV Group |
| **License** | Commercial (academic licenses available) |
| **Primary use** | Detailed traffic simulation, signal optimization |
| **Learning time to L2** | 15–25 hours |
| **Alternative** | Aimsun Next, SUMO (open-source) |

### Synchro

| Property | Value |
|:---------|:------|
| **What** | Traffic signal timing and intersection analysis |
| **Developer** | Trafficware (Cubic) |
| **License** | Commercial |
| **Primary use** | Signal timing, intersection level-of-service |
| **Learning time to L2** | 8–12 hours |
| **Alternative** | HCS, SIDRA |

### TransCAD

| Property | Value |
|:---------|:------|
| **What** | GIS-based transportation planning |
| **Developer** | Caliper Corporation |
| **License** | Commercial (academic available) |
| **Primary use** | 4-step demand model, network analysis |
| **Learning time to L2** | 20–30 hours |
| **Alternative** | EMME (commercial), Python custom |

### Civil 3D (Transportation)

| Property | Value |
|:---------|:------|
| **What** | Civil engineering design — roadway focus |
| **Developer** | Autodesk |
| **License** | Commercial (free for students) |
| **Primary use** | Horizontal/vertical alignment, profiles, corridors |
| **Learning time to L2** | 20–30 hours |
| **Alternative** | OpenRoads Designer (Bentley) |

---

## Typical Industry Workflow

### Highway Design

```
Step 1: Survey — Import terrain data (DEM, point cloud)
Step 2: Align — Define horizontal and vertical alignment
Step 3: Cross-section — Define typical cross-section
Step 4: Corridor — Generate corridor model
Step 5: Quantities — Compute earthwork, pavement quantities
Step 6: Drawings — Generate plan, profile, cross-section sheets
Step 7: Report — Design calculations, specifications
```

### Traffic Study

```
Step 1: Collect — Traffic counts, turning movements, speed data
Step 2: Analyze — Peak hour factors, growth rates, LOS
Step 3: Model — Build Synchro/Vissim model
Step 4: Simulate — Run traffic scenarios
Step 5: Optimize — Signal timing, geometry improvements
Step 6: Report — Findings, recommendations, exhibits
```

---

## Open-Source Alternatives

| Commercial | Open-Source Alternative | Notes |
|:-----------|:----------------------|:------|
| PTV Vissim | SUMO | Agent-based, good for research |
| TransCAD | QGIS + custom Python | Less automated, more flexible |
| Synchro | HCS (limited) | HCS is semi-commercial |
| Civil 3D | QGIS + GRASS GIS | Limited design capabilities |

---

## Interview Questions

### Basic (101)
- What is Level of Service (LOS)?
- Explain the four-step transport demand model.
- What is HCM? How is it used?

### Practical (201)
- How do you set up a traffic simulation in Vissim/Synchro?
- How do you compute the capacity of a signalized intersection?
- Walk me through a highway geometric design workflow.

### Technical (301)
- How do you calibrate a transport demand model?
- Explain the difference between microscopic and macroscopic simulation.
- What are the limitations of the HCM methodology?

---

## Study Material

| Tool | Canonical Study Page |
|:-----|:---------------------|
| Excel | [`tools/Excel.md`](../tools/Excel.md) |
| QGIS / GIS | [`tools/QGIS.md`](../tools/QGIS.md) |
| Python | [`programming/python.md`](../programming/python.md) |

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| Core Transportation | [`core/transportation/`](../../core/transportation/transportation-engineering.md) |
| Existing Transport Software | [`core/transportation/transportation-software.md`](../../core/transportation/transportation-software.md) |
| GIS Technology | [`gis/`](../gis/gis-tech.md) |
| Python for Engineering | [`programming/python.md`](../programming/python.md) |

---

*See also: [`branch-roadmaps.md`](../branch-roadmaps.md) for full branch comparison.*
