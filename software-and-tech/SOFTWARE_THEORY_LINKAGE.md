# 🔗 SOFTWARE_THEORY_LINKAGE.md — Software ↔ Engineering Theory

> **A software page is never isolated from the engineering theory it implements.**
> For every tool: which fundamentals it applies, and where to revise them.

---

## Why This Matters

Interviewers don't ask "which button do you click" — they ask **"why did you choose this setting?"** and **"what does this result mean?"** Both require linking the tool to the underlying engineering theory.

---

## Structural Tools

### ETABS / STAAD.Pro / SAP2000

```
ETABS → Structural Analysis → stiffness method, FEM
      → Loads → IS 875 (DL/LL/WL), IS 1893 (seismic)
      → Boundary conditions → supports, diaphragms
      → Design → IS 456 (concrete), IS 800 (steel)
      → Dynamics → modal, response spectrum, time-history
```

| Theory Topic | Where to Revise |
|:-------------|:----------------|
| Structural Analysis | [`core/structural-analysis/structural-analysis.md`](../core/structural-analysis/structural-analysis.md) |
| RCC Design | [`core/rcc/rcc-design.md`](../core/rcc/rcc-design.md) |
| Steel Design | [`core/steel/steel-design.md`](../core/steel/steel-design.md) |
| Structures | [`core/structures/structures.md`](../core/structures/structures.md) |

### AutoCAD

```
AutoCAD → Engineering Drawing → IS 962 (drawing conventions)
        → Structural Detailing → IS 456 (rebar detailing)
        → Construction → drawing interpretation on site
```

### Revit / Navisworks

```
Revit → BIM → parametric modeling, LOD
      → Construction → coordination, quantity takeoff
      → Structural → 3D structural modeling
```

---

## Water Resources Tools

### HEC-RAS

```
HEC-RAS → Fluid Mechanics → open channel flow, energy equation
        → Open Channel Flow → Manning's, specific energy, GVF
        → Hydraulic Structures → bridges, culverts, weirs
        → Flood Modelling → floodplain hydraulics
```

| Theory Topic | Where to Revise |
|:-------------|:----------------|
| Open Channel Flow | [`core/hwre/open_channel_flow/open-channel-flow.md`](../core/hwre/open_channel_flow/open-channel-flow.md) |
| Hydraulics | [`core/hwre/hydraulics/hydraulics.md`](../core/hwre/hydraulics/hydraulics.md) |
| Water Resources | [`core/hwre/water_resources/water-resources-engineering.md`](../core/hwre/water_resources/water-resources-engineering.md) |

### HEC-HMS

```
HEC-HMS → Hydrology → rainfall-runoff, unit hydrograph
        → Watershed → catchment delineation, routing
        → Flood Forecasting → Muskingum routing
```

### EPANET / SWMM

```
EPANET → Water Supply → pipe networks, HGL, demand
SWMM   → Urban Drainage → stormwater, runoff, LID
```

### QGIS / ArcGIS

```
QGIS → Surveying → coordinate systems, projections
     → GIS → spatial analysis, cartography
     → Hydrology → watershed, DEM, flow direction
     → Remote Sensing → satellite imagery, classification
```

---

## Geotechnical Tools

### PLAXIS 2D / GeoStudio SLOPE/W

```
PLAXIS → Geotechnical → soil mechanics, FEM
       → Slope Stability → FoS, phi-c reduction
       → Groundwater → seepage, consolidation
```

| Theory Topic | Where to Revise |
|:-------------|:----------------|
| Geotechnical | [`core/geotechnical/geotechnical.md`](../core/geotechnical/geotechnical.md) |

---

## CFD Tools

### OpenFOAM / ANSYS

```
OpenFOAM → Fluid Mechanics → Navier-Stokes, turbulence
         → Numerical Methods → FVM, discretization
         → CFD → RANS/LES, y+, mesh independence
```

| Theory Topic | Where to Revise |
|:-------------|:----------------|
| Hydraulics (CFD) | [`core/hwre/hydraulics/hydraulics.md`](../core/hwre/hydraulics/hydraulics.md) |
| Turbulence Modeling | [`core/hwre/hydraulics/turbulence-modeling.md`](../core/hwre/hydraulics/turbulence-modeling.md) |

---

## Programming / Data Tools

### Python / MATLAB

```
Python → Numerical Methods → linear algebra, ODE, optimization
       → Data Analysis → statistics, visualization
       → Automation → engineering calculation workflows
```

### SQL

```
SQL → Data Management → relational databases, querying
    → Analytics → aggregation, window functions
```

### Excel

```
Excel → Quantity Surveying → IS 1200 (measurement)
      → RCC Design → IS 456 (design checks)
      → Construction Management → BOQ, billing, cost control
```

---

## Interview Defense Pattern

For any tool, connect: **Tool → Theory → Setting → Result → Interpretation**

```
Example (HEC-RAS):
    Tool: HEC-RAS
    Theory: Energy equation, Manning's equation
    Setting: Manning's n = 0.035 (main channel)
    Result: Water surface = 102.4 m at section 3
    Interpretation: "The water surface rises 0.8m above normal depth due to
                    bridge constriction — consistent with backwater theory"
```

```
Example (ETABS):
    Tool: ETABS
    Theory: Response spectrum analysis (IS 1893)
    Setting: Zone III, R=5, I=1
    Result: Inter-story drift = 0.0035
    Interpretation: "Drift is below the 0.004 limit — the lateral system is adequate"
```

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| Core Subjects | [`../core/README.md`](../core/README.md) |
| Role Matrix | [`SOFTWARE_ROLE_MATRIX.md`](SOFTWARE_ROLE_MATRIX.md) |
| Interview Questions | [`software-interview-questions.md`](software-interview-questions.md) |

---

*Tool knowledge without theory is not interview-defensible.*