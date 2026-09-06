# HWRE — Modelling Workflow

> End-to-end hydrologic + hydraulic modelling pipeline: HEC-HMS → HEC-RAS → GIS. The canonical workflow reference for HWRE modelling roles.

## Pipeline Overview

```
TERRAIN/GIS → HEC-HMS (rainfall-runoff) → HYDROGRAPH → HEC-RAS (hydraulics) → RAS Mapper (flood map)
     │                │                              │                          │
  DEM, land use   loss + transform + routing     steady/unsteady flow      inundation, depth, velocity
```

## Step 1: HEC-HMS (Hydrologic Modeling)

### 1.1 Basin Model Setup
1. Create a new project → Basin Model
2. Import watershed delineation (from GIS or HEC-GeoHMS)
3. Add subbasins, reaches, junctions, reservoirs
4. Connect elements to form the drainage network

### 1.2 Loss Methods
| Method | Parameters | Use |
|--------|-----------|-----|
| SCS-CN | CN, initial abstraction I_a | Small catchments, land-use based |
| Green-Ampt | K, ψ, Δθ | Physically based, infiltration |
| Deficit-Constant | Initial deficit, max rate | Continuous simulation |
| Initial-Constant | Initial loss, constant rate | Simple |

### 1.3 Transform Methods
| Method | Parameters | Use |
|--------|-----------|-----|
| SCS UH | Lag time | Small catchments |
| Snyder UH | t_p, C_p | Ungauged catchments |
| Clark UH | t_c, R | Distributed rainfall |
| Kinematic Wave | Slope, length, roughness | Overland flow |

### 1.4 Routing Methods
| Method | Parameters | Use |
|--------|-----------|-----|
| Muskingum | K, X | Channel routing |
| Lag | Lag time | Simple |
| Kinematic Wave | Reach properties | Steep channels |
| Modified Puls | Storage-discharge | Reservoir routing |

### 1.5 Meteorologic Model
1. Create Meteorologic Model
2. Assign precipitation (gauge weights, Thiessen, or gridded)
3. Set time window and time interval
4. Apply evapotranspiration if continuous simulation

### 1.6 Control Specifications
- Start/end time
- Time interval (e.g., 1 hr)
- Run → view hydrographs at junctions/outlets

## Step 2: HEC-RAS (Hydraulic Modeling)

### 2.1 Geometry
1. Create new project → Geometric Data
2. Draw river reach (centerline)
3. Add cross-sections (perpendicular to flow)
4. Assign bank stations, Manning's n, ineffective flow areas
5. Add structures: bridges, culverts, weirs, inline structures

### 2.2 Steady Flow Analysis
1. Steady Flow Data: enter flow at upstream boundary
2. Boundary conditions: normal depth, known WS, critical depth
3. Run steady analysis (standard step method)
4. View water surface profiles, velocity, shear stress

### 2.3 Unsteady Flow Analysis
1. Unsteady Flow Data: enter hydrograph at upstream boundary
2. Boundary conditions: stage hydrograph, Q-hydrograph, rating curve
3. Initial conditions: from steady run or specified
4. Run unsteady analysis (Saint-Venant equations)
5. View time-series at cross-sections

### 2.4 Dam Breach Analysis
1. Add breach parameters (bottom width, side slopes, failure time)
2. Run unsteady with breach
3. Route breach hydrograph downstream
4. Map inundation in RAS Mapper

## Step 3: GIS / RAS Mapper

### 3.1 Terrain Processing
1. Import DEM into RAS Mapper
2. Create terrain layer
3. Extract cross-sections from terrain
4. Compute floodplain extents

### 3.2 Flood Inundation Mapping
1. Run HEC-RAS → Results → RAS Mapper
2. Create floodplain layer from water surface
3. Map depth, velocity, shear stress
4. Export to GIS (shapefile/GeoTIFF)

### 3.3 HEC-GeoHMS / HEC-GeoRAS
| Tool | Purpose |
|------|---------|
| HEC-GeoHMS | Watershed delineation → HEC-HMS basin model |
| HEC-GeoRAS | Cross-section extraction → HEC-RAS geometry |

## Step 4: Other Tools

| Tool | Use Case | Workflow |
|------|----------|----------|
| EPANET | Water distribution | Network → demands → run → pressure/quality |
| SWMM | Urban drainage | Subcatchments → conduits → run → flooding |
| MODFLOW 6 | Groundwater | Grid → layers → BCs → run → heads |
| OpenFOAM | CFD | Mesh → solver → post-process |

## Common Pitfalls in Modelling

| Pitfall | Fix |
|---------|-----|
| Cross-sections not perpendicular to flow | Redraw perpendicular to centerline |
| Inconsistent Manning's n | Use field data or standard tables |
| Boundary condition too close to structure | Extend reach upstream/downstream |
| Unsteady model unstable | Reduce time step, check Courant condition |
| HMS/RAS units mismatch | Keep consistent (SI or imperial) throughout |
| DEM resolution too coarse | Use ≤ 30 m for small catchments |

## Interview Talking Points

1. **"Describe your modelling workflow."** — HEC-HMS for rainfall-runoff → export hydrograph → HEC-RAS for hydraulics → RAS Mapper for flood mapping.
2. **"Steady vs unsteady HEC-RAS?"** — Steady: constant flow, standard step; unsteady: time-varying, Saint-Venant, for routing/breach.
3. **"How do you calibrate a model?"** — Adjust loss/transform parameters to match observed hydrographs; validate on independent events.
4. **"What is the Courant condition?"** — `C = VΔt/Δx ≤ 1` for numerical stability in unsteady flow.

## Related

- [HEC-HMS Tutorial](../../software-and-tech/deep-dives/hec-hms-tutorial.md)
- [HEC-RAS Walkthrough](../../software-and-tech/deep-dives/hec-ras-walkthrough.md)
- [EPANET Walkthrough](../../software-and-tech/deep-dives/epanet-walkthrough.md)
- [SWMM Guide](../../software-and-tech/deep-dives/swmm-guide.md)
- [OpenFOAM Case Study](../../software-and-tech/deep-dives/openfoam-case-study.md)
- [HWRE Tech Roadmap](../../software-and-tech/hwre/hwre-tech-roadmap.md)
- [MASTER_INDEX.md](MASTER_INDEX.md)