# 🪨 Geotechnical Engineering Technology Roadmap

> **Branch:** Geotechnical Engineering
> **Tools mapped to FEM, slope stability, seepage, consolidation, foundations, and retaining structures.**

---

## Decision Tree

```
Geotechnical student → what tools?

1. PLAXIS first         → Geotechnical FEM (MUST)
2. GeoStudio (SLOPE/W) → Slope stability (MUST)
3. Excel                → Calculations, data processing (MUST)
4. GIS (QGIS)          → Site mapping, spatial data (HIGH ROI)
5. AutoCAD              → Cross-sections, drawings (HIGH ROI)
6. Python / MATLAB      → Analysis, optimization (ROLE DEPENDENT)
7. PLAXIS 3D            → 3D geotechnical modeling (SPECIALIZED)
```

---

## Tool Roadmap

### Essential

| Tool | Tag | Level | Problem Solved |
|:-----|:----|:------|:---------------|
| PLAXIS 2D | `[MUST LEARN]` | L2–L3 | FEM for geotechnical problems |
| GeoStudio (SLOPE/W + SEEP/W) | `[MUST LEARN]` | L2–L3 | Slope stability, seepage |
| Excel | `[MUST LEARN]` | L3 | Design calculations, data processing |

### Important

| Tool | Tag | Level | Problem Solved |
|:-----|:----|:------|:---------------|
| AutoCAD | `[HIGH ROI]` | L2 | Cross-sections, geometry definition |
| GIS (QGIS) | `[HIGH ROI]` | L2 | Site mapping, terrain analysis |
| Python | `[ROLE DEPENDENT]` | L2 | Data analysis, post-processing |
| MATLAB | `[ROLE DEPENDENT]` | L2 | Numerical methods, optimization |

### Advanced

| Tool | Tag | Level | Problem Solved |
|:-----|:----|:------|:---------------|
| PLAXIS 3D | `[SPECIALIZED]` | L3 | Complex 3D geometries |
| FLAC / FLAC3D | `[SPECIALIZED]` | L2–L3 | Large deformation, dynamic analysis |
| LPile | `[SPECIALIZED]` | L2 | Laterally loaded pile analysis |
| Settle3 | `[SPECIALIZED]` | L2 | 3D settlement analysis |
| Python + OpenSeesPy | `[SPECIALIZED]` | L2–L3 | Custom FEM, research |

---

## PLAXIS Workflow

The key to PLAXIS is understanding the **full workflow**, not just button-clicking.

```
1. Geometry
   → Define soil layers, structures, water table
   → Use built-in geometry tools or import from CAD

2. Mesh
   → Generate finite element mesh
   → Refine in areas of high gradient (near structures, slip surfaces)
   → Check mesh quality

3. Material Model
   → Select constitutive model:
     - Mohr-Coulomb (basic, first analysis)
     - Hardening Soil (for settlement, excavation)
     - Soft Soil (for soft clays, consolidation)
     - Cam Clay (research)
   → Assign parameters from lab/field tests

4. Boundary Conditions
   → Fix displacements at boundaries
   → Set water pressure conditions
   → Apply groundwater flow if needed

5. Loading
   → Construction stages (excavation, fill, structural loading)
   → Water level changes
   → Dynamic loading (seismic)

6. Solver
   → Plastic, drained, undrained analysis types
   → Set convergence criteria
   → Monitor convergence

7. Results
   → Displacement fields, stress fields
   → Safety factor (phi-c reduction)
   → Consolidation settlement
   → Structural forces in walls/piles

8. Validation
   → Compare with hand calculations
   → Check mesh convergence
   → Review stress paths
```

---

## GeoStudio Workflow

### SLOPE/W (Slope Stability)

```
1. Define → geometry, soil layers, water table
2. Assign → soil properties (c, φ, γ)
3. Define → slip surface search method (auto, circular, non-circular)
4. Run → factor of safety calculation
5. Results → critical slip surface, FoS, sensitivity analysis
```

### SEEP/W (Seepage Analysis)

```
1. Define → geometry, soil layers, boundary conditions
2. Assign → hydraulic properties (k, van Genuchten parameters)
3. Set → steady-state or transient analysis
4. Run → seepage analysis
5. Results → pore pressure distribution, flow nets, seepage quantity
```

---

## Material Models Selection Guide

| Model | When to Use | Complexity |
|:------|:------------|:-----------|
| Mohr-Coulomb | First-pass analysis, simple problems | Low |
| Hardening Soil | Excavation, settlement, cyclic loading | Medium |
| Soft Soil | Soft clays, consolidation | Medium |
| Soft Soil Creep | Time-dependent settlement (creep) | Medium-High |
| Modified Cam Clay | Research, advanced soil behavior | High |

---

## Example Projects

### For Resume

```
Project 1: Excavation Analysis
    Tools: PLAXIS 2D
    Workflow: Define geometry → soil model → excavation stages → results
    Output: Wall displacement, ground settlement, factor of safety
    Resume value: High

Project 2: Slope Stability Assessment
    Tools: SLOPE/W + SEEP/W
    Workflow: Geometry → soil properties → steady-state seepage → slope stability
    Output: Critical slip surface, FoS, sensitivity to water table
    Resume value: High

Project 3: Foundation Settlement
    Tools: PLAXIS 2D + Excel
    Workflow: Foundation geometry → consolidation analysis → settlement prediction
    Output: Settlement vs time, bearing capacity
    Resume value: Medium-High
```

---

## Interview Questions

### Basic (101)
- What is the difference between PLAXIS and GeoStudio?
- What constitutive model would you use for a first-pass analysis?
- What is the factor of safety in phi-c reduction?

### Practical (201)
- Walk me through a PLAXIS excavation analysis.
- How do you determine soil parameters from lab data?
- When would you use PLAXIS 2D vs 3D?
- How do you model groundwater in PLAXIS?

### Technical (301)
- Explain the hardening soil model. What makes it different from Mohr-Coulomb?
- How does PLAXIS handle soil-structure interaction?
- What is mesh sensitivity? How do you perform a mesh convergence study?

### Validation
- How do you validate your PLAXIS results?
- What hand calculations would you compare against?
- How do you handle uncertainty in soil parameters?

---

## Key Formulas for Quick Reference

```
Factor of Safety (Taylor):    FoS = c'/(γ·H·N_s)
Bearing Capacity (Terzaghi):  q_ult = c'N_c + γDN_q + 0.5γBN_γ
Settlement (Consolidation):   S = C_c·H/(1+e_0) · log(σ'_f/σ'_0)
Earth Pressure (Rankine):     K_a = tan²(45°-φ/2)
                              K_p = tan²(45°+φ/2)
Seepage Force:                j = i·γ_w
```

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| Core Geotechnical | [`core/geotechnical/`](../../core/geotechnical/geotechnical.md) |
| Python for Engineering | [`programming/python.md`](../programming/python.md) |
| GIS Technology | [`gis/`](../gis/gis-tech.md) |
| Research Technology | [`research/`](../research/research-tech.md) |

---

*See also: [`branch-roadmaps.md`](../branch-roadmaps.md) for full branch comparison.*
