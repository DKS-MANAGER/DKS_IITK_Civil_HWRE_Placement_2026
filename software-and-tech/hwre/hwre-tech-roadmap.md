# 🌊 Hydraulics / HWRE Technology Roadmap

> **Branch:** Hydraulics / Water Resources Engineering
> **This roadmap maps technologies to your HWRE specialization and target job role.**

---

## Decision Tree

```
I am an HWRE student. What should I learn?

1. HEC-RAS first           → River hydraulic modeling (MUST for all HWRE)
2. EPANET if water dist.   → Pressurized pipe network modeling
3. SWMM if urban drainage  → Stormwater / urban hydrology
4. Python or MATLAB        → Data analysis and automation
5. GIS (QGIS/ArcGIS)      → Spatial water problems
6. OpenFOAM if CFD/research → Advanced flow simulation
7. ParaView for visualization → CFD post-processing
```

**Not every HWRE student needs every tool.** Choose based on your specialization and role.

---

## Tool Roadmap by Specialization

### General HWRE (All students)

| Tool | Tag | Level | Why |
|:-----|:----|:------|:----|
| HEC-RAS | `[MUST LEARN]` | L2–L3 | Industry-standard river modeling |
| Excel | `[MUST LEARN]` | L2–L3 | Data processing, calculations |
| Python | `[HIGH ROI]` | L2–L3 | Automation, analysis, plotting |
| GIS (QGIS) | `[HIGH ROI]` | L2 | Spatial data, watershed mapping |

### River Engineering / Hydraulics

| Tool | Tag | Level | Why |
|:-----|:----|:------|:----|
| HEC-RAS | `[MUST LEARN]` | L3 | 1D/2D river modeling, flood mapping |
| HEC-RAS Mapper | `[MUST LEARN]` | L2 | Geospatial results visualization |
| Python | `[HIGH ROI]` | L2–L3 | Post-processing HEC-RAS output |
| QGIS / ArcGIS | `[HIGH ROI]` | L2 | Terrain, floodplain delineation |
| MATLAB | `[ROLE DEPENDENT]` | L2 | Numerical methods, ODE solving |
| SWMM | `[ROLE DEPENDENT]` | L2 | If urban drainage is relevant |

### Water Distribution / Supply

| Tool | Tag | Level | Why |
|:-----|:----|:------|:----|
| EPANET | `[MUST LEARN]` | L3 | Water distribution network modeling |
| WaterGEMS | `[ROLE DEPENDENT]` | L2 | Commercial WDN software (Bentley) |
| Python | `[HIGH ROI]` | L2–L3 | EPANET output analysis |
| GIS | `[HIGH ROI]` | L2 | Network mapping, spatial analysis |

### Urban Drainage / Stormwater

| Tool | Tag | Level | Why |
|:-----|:----|:------|:----|
| EPA SWMM | `[MUST LEARN]` | L3 | Urban drainage, stormwater management |
| HEC-RAS | `[HIGH ROI]` | L2 | For receiving water body modeling |
| Python | `[HIGH ROI]` | L2–L3 | SWMM output processing |
| GIS | `[HIGH ROI]` | L2 | Catchment delineation, LID planning |

### Irrigation Engineering

| Tool | Tag | Level | Why |
|:-----|:----|:------|:----|
| Excel | `[MUST LEARN]` | L3 | Irrigation calculations, duty-delta |
| HEC-RAS | `[ROLE DEPENDENT]` | L2 | Canal hydraulics |
| Python | `[HIGH ROI]` | L2 | Data analysis, optimization |
| GIS | `[ROLE DEPENDENT]` | L2 | Command area mapping |

### Groundwater

| Tool | Tag | Level | Why |
|:-----|:----|:------|:----|
| MODFLOW 6 | `[MUST LEARN]` | L2–L3 | Groundwater flow modeling |
| GIS | `[HIGH ROI]` | L2 | Well location, aquifer mapping |
| Python | `[HIGH ROI]` | L2 | MODFLOW post-processing |

### Flood Risk / Flood Management

| Tool | Tag | Level | Why |
|:-----|:----|:------|:----|
| HEC-RAS | `[MUST LEARN]` | L3 | 1D/2D flood simulation |
| HEC-HMS | `[MUST LEARN]` | L2–L3 | Rainfall-runoff modeling |
| GIS | `[MUST LEARN]` | L2–L3 | Floodplain mapping, risk assessment |
| Python | `[HIGH ROI]` | L2 | Flood data analysis |
| Google Earth Engine | `[ROLE DEPENDENT]` | L2 | Satellite-based flood mapping |

### CFD / Research (M.Tech)

| Tool | Tag | Level | Why |
|:-----|:----|:------|:----|
| OpenFOAM | `[MUST LEARN]` | L3–L4 | CFD simulation |
| ParaView | `[MUST LEARN]` | L2–L3 | CFD visualization |
| Python | `[MUST LEARN]` | L3 | Post-processing, automation |
| Linux / Bash | `[MUST LEARN]` | L2 | HPC, command-line workflows |
| Git | `[HIGH ROI]` | L2 | Version control for code |
| MATLAB | `[ROLE DEPENDENT]` | L2 | Numerical methods |
| HPC / SLURM | `[ROLE DEPENDENT]` | L2 | Large-scale simulations |

---

## Learning Paths by Career Goal

### Path A: Water Resources Industry (PSU / Core Company)

```
Priority 1: HEC-RAS (L3) + Excel (L3)
Priority 2: HEC-HMS (L2) + GIS (L2)
Priority 3: Python (L2) for data analysis
Optional:   EPANET or SWMM (L1-L2)

Timeline: 30 days
    Week 1: HEC-RAS basics + tutorials
    Week 2: HEC-RAS real project + Excel
    Week 3: HEC-HMS + GIS basics
    Week 4: Python post-processing + interview prep
```

### Path B: Technical Consulting / CFD

```
Priority 1: OpenFOAM (L3) + Linux (L2) + Python (L3)
Priority 2: ParaView (L2) + Git (L2)
Priority 3: MATLAB (L2) + HEC-RAS (L2)
Optional:   HPC / SLURM (L2)

Timeline: 90 days
    Month 1: Linux + OpenFOAM basics + tutorials
    Month 2: OpenFOAM intermediate + ParaView + Python
    Month 3: Custom project + portfolio + interview prep
```

### Path C: Data / Analytics (Non-Core)

```
Priority 1: Python (L3) + SQL (L3)
Priority 2: Excel (L3) + Power BI (L2)
Priority 3: Statistics + HEC-RAS (L1-L2)
Optional:   GIS (L2)

Timeline: 45 days
    Weeks 1-2: Python + Pandas fundamentals
    Weeks 3-4: SQL fundamentals + practice
    Weeks 5-6: Excel advanced + statistics
    Weeks 7: Power BI basics + project
    Week 8: Resume + interview prep
```

### Path D: Product / Business Analyst (Non-Core)

```
Priority 1: SQL (L3) + Excel (L3)
Priority 2: Python (L2) for analytics
Priority 3: Power BI (L2) + metrics frameworks
Optional:   HEC-RAS (L1)

Timeline: 30 days
    Week 1: Excel advanced (pivot, lookup, charts)
    Week 2: SQL fundamentals + practice
    Week 3: SQL advanced + Python basics
    Week 4: Power BI + metrics + interview prep
```

---

## Tool Details

### HEC-RAS

| Property | Value |
|:---------|:------|
| **What** | River Analysis System — 1D/2D hydraulic modeling |
| **Developer** | US Army Corps of Engineers (USACE) |
| **License** | Free (public domain) |
| **Platform** | Windows |
| **Primary use** | Steady/unsteady flow, flood mapping, dam breach |
| **Learning time to L2** | 15–20 hours |
| **Learning time to L3** | 30–40 hours |
| **Alternative** | MIKE 11/21 (commercial), HEC-RAS is industry standard for government |

### EPANET

| Property | Value |
|:---------|:------|
| **What** | Water distribution system modeling |
| **Developer** | US EPA |
| **License** | Free (public domain) |
| **Platform** | Windows (standalone) |
| **Primary use** | Pressurized pipe network, water quality |
| **Learning time to L2** | 10–15 hours |
| **Learning time to L3** | 20–30 hours |
| **Alternative** | WaterGEMS (commercial, Bentley) |

### EPA SWMM

| Property | Value |
|:---------|:------|
| **What** | Storm Water Management Model |
| **Developer** | US EPA |
| **License** | Free (open-source) |
| **Platform** | Windows, Linux |
| **Primary use** | Urban drainage, stormwater, LID analysis |
| **Learning time to L2** | 12–18 hours |
| **Learning time to L3** | 25–35 hours |
| **Alternative** | MIKE URBAN (commercial) |

### HEC-HMS

| Property | Value |
|:---------|:------|
| **What** | Hydrologic Modeling System — rainfall-runoff |
| **Developer** | USACE |
| **License** | Free (public domain) |
| **Platform** | Windows |
| **Primary use** | Watershed modeling, flood forecasting |
| **Learning time to L2** | 10–15 hours |
| **Learning time to L3** | 20–25 hours |
| **Alternative** | MIKE SHE (commercial), SWMM (for urban) |

### OpenFOAM (for HWRE)

| Property | Value |
|:---------|:------|
| **What** | Open-source CFD toolbox |
| **Developer** | OpenFOAM Foundation / ESI-OpenCFD |
| **License** | Open-source (GPL) |
| **Platform** | Linux (primary), macOS |
| **Primary use** | Free-surface flow, turbulence, sediment transport |
| **Learning time to L2** | 20–30 hours |
| **Learning time to L3** | 60–100 hours |
| **Learning time to L4** | 200+ hours |
| **Alternative** | ANSYS Fluent/CFX (commercial) |

---

## Interview Questions for HWRE Tools

### HEC-RAS

**Basic:**
- What is HEC-RAS? What type of problems does it solve?
- What is the difference between 1D and 2D HEC-RAS?
- What data does HEC-RAS need for a steady flow analysis?

**Practical:**
- Walk me through a HEC-RAS project from data to results.
- How do you set up a 2D floodplain model?
- What boundary conditions are available and when do you use each?

**Troubleshooting:**
- Your model isn't converging in unsteady flow. What do you check?
- How do you validate HEC-RAS results against observations?

### EPANET

**Basic:**
- What is EPANET? What does it model?
- What is a hydraulic grade line (HGL)?
- What are demand-driven vs. pressure-driven models?

**Practical:**
- How do you model a water distribution network in EPANET?
- How do you analyze water quality in a pipe network?

### OpenFOAM (for HWRE roles)

**Basic:**
- What is OpenFOAM? Why is it used in HWRE?
- What is the case structure (0/, constant/, system/)?

**Practical:**
- How would you set up a simple channel flow simulation?
- What solver would you use for a free-surface flow problem?

---

## 🔬 Deep-Dive Walkthroughs

> **"I know I need HEC-RAS. Now how do I actually build a model?"**

Follow the hands-on step-by-step guides to build real models end-to-end:

| Tool | Deep-Dive Guide |
|:-----|:----------------|
| HEC-RAS | [`deep-dives/hec-ras-walkthrough.md`](../deep-dives/hec-ras-walkthrough.md) |
| HEC-HMS | [`deep-dives/hec-hms-tutorial.md`](../deep-dives/hec-hms-tutorial.md) |
| SWMM | [`deep-dives/swmm-guide.md`](../deep-dives/swmm-guide.md) |
| EPANET | [`deep-dives/epanet-walkthrough.md`](../deep-dives/epanet-walkthrough.md) |
| OpenFOAM | [`deep-dives/openfoam-case-study.md`](../deep-dives/openfoam-case-study.md) |

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| Core HWRE Hydraulics | [`core/hwre/hydraulics/`](../../core/hwre/hydraulics/hydraulics.md) |
| Open-Channel Flow | [`core/hwre/open_channel_flow/`](../../core/hwre/open_channel_flow/open-channel-flow.md) |
| Hydrology | [`hydrology/`](../hydrology/hydrology-tech.md) |
| CFD Technology | [`cfd/`](../cfd/cfd-tech.md) |
| GIS Technology | [`gis/`](../gis/gis-tech.md) |
| Branch Roadmaps | [`branch-roadmaps.md`](../branch-roadmaps.md) |
| Role Roadmaps | [`role-roadmaps.md`](../role-roadmaps.md) |

---

*See also: [`hydrology-tech.md`](../hydrology/hydrology-tech.md) for hydrology-specific tools, [`cfd-tech.md`](../cfd/cfd-tech.md) for advanced CFD.*
