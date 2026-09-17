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

For any engineering software, structure your interview defense using the five-step chain:
**Tool → Governing Theory → Setting / Input Choice → Analytical Result → Engineering Interpretation**

> [!NOTE]
> Numerical values below are **illustrative examples**. In actual interview defenses, always explicitly state your load combinations, code references, boundary assumptions, and project acceptance criteria.

```
Illustrative Example 1 (HEC-RAS — 1D Backwater Defense):
    Tool: HEC-RAS
    Governing Theory: 1D Standard Step Method, Energy Equation, Manning's Equation
    Illustrative Setting: Manning's n = 0.035 (calibrated for natural gravel bed with slight meander)
    Simulated Result: Water surface elevation = 102.40 m at River Station 3.00
    Engineering Interpretation:
    "The modeled water surface exhibits a 0.80 m backwater rise upstream of the pier
     contraction relative to uniform flow depth. This conforms to specific energy
     conservation through a constricted cross-section under subcritical regime (Fr < 1.0)."
```

```
Illustrative Example 2 (ETABS — Seismic Drift Check Defense):
    Tool: ETABS
    Governing Theory: Dynamic Response Spectrum Analysis (Modal Combination via CQC)
    Illustrative Setting: IS 1893:2016 Zone III (Z = 0.16), SMRF (R = 5), Medium Soil (Type II), I = 1.0
    Simulated Result: Maximum elastic inter-story drift ratio = 0.0032 under DL + 0.8LL + 1.2EQX
    Engineering Interpretation:
    "Under this illustrative load combination, the maximum computed elastic drift ratio of
     0.0032 satisfies the permissible limit of 0.0040 specified under IS 1893:2016 Cl 7.11.1.
     However, full lateral compliance also requires verifying P-Delta amplification,
     torsional irregularity limits (< 1.5), and soft-story stiffness criteria."
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