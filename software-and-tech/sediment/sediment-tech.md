# 🏔️ Sediment Transport & River Engineering — Technology Roadmap

> **Branch:** Sediment Transport / River Engineering / CFD
> **Dedicated technology section for numerical modelling, CFD, data processing, and visualization.**

---

## Decision Tree

```
Sediment / River Engineering student → what tools?

1. Python first         → Data processing, analysis, plotting (MUST)
2. MATLAB               → Numerical methods, ODE/PDE (HIGH ROI)
3. HEC-RAS              → River morphology, sediment routing (MUST)
4. GIS (QGIS/ArcGIS)   → Spatial river analysis (HIGH ROI)
5. OpenFOAM             → CFD for sediment-laden flows (SPECIALIZED)
6. ParaView             → CFD visualization (SPECIALIZED)
7. C/C++                → Solver modification (SPECIALIZED)
```

---

## Tool Roadmap

### Essential

| Tool | Tag | Level | Problem Solved |
|:-----|:----|:------|:---------------|
| Python | `[MUST LEARN]` | L3 | Data processing, numerical methods, plotting |
| HEC-RAS | `[MUST LEARN]` | L2–L3 | River morphology, sediment routing (1D) |
| MATLAB | `[HIGH ROI]` | L2–L3 | Numerical methods, matrix operations |
| Excel | `[MUST LEARN]` | L3 | Quick calculations, data organization |

### Important

| Tool | Tag | Level | Problem Solved |
|:-----|:----|:------|:---------------|
| GIS (QGIS) | `[HIGH ROI]` | L2 | Spatial analysis, channel morphology mapping |
| ParaView | `[HIGH ROI]` | L2 | CFD post-processing, visualization |
| Git | `[HIGH ROI]` | L2 | Version control for codes and data |

### Advanced / CFD-Specific

| Tool | Tag | Level | Problem Solved |
|:-----|:----|:------|:---------------|
| OpenFOAM | `[SPECIALIZED]` | L3–L4 | CFD — turbulent sediment-laden flows |
| C/C++ | `[SPECIALIZED]` | L2–L3 | Custom solver development |
| Linux / Bash | `[SPECIALIZED]` | L2 | HPC workflows, batch processing |
| HPC / SLURM | `[SPECIALIZED]` | L2 | Large-scale simulations |
| ParaView (advanced) | `[SPECIALIZED]` | L3 | Custom visualization, Python scripting |

---

## Tool → Problem → Workflow

### Python for Sediment Transport

| Property | Value |
|:---------|:------|
| **Problem solved** | Process field/lab data, implement numerical methods, post-process CFD |
| **Key libraries** | NumPy, Pandas, Matplotlib, SciPy, SymPy |
| **Input data** | Grain size distributions, velocity profiles, concentration measurements |
| **Output** | Transport rate curves, grain size analysis, velocity-concentration plots |
| **Portfolio project** | Implement Meyer-Peter Müller bedload equation in Python, validate against lab data |

### HEC-RAS for Sediment

| Property | Value |
|:---------|:------|
| **Problem solved** | 1D sediment transport, channel morphology changes |
| **Key features** | Sediment transport functions (MPM, Yang, etc.), armoring,gradation |
| **Input data** | Channel geometry, flow, grain size distribution |
| **Output** | Bed change, sediment transport rates, armoring |
| **Portfolio project** | Model sediment transport in a river reach, predict aggradation/degradation |

### OpenFOAM for Sediment

| Property | Value |
|:---------|:------|
| **Problem solved** | CFD of sediment-laden flows, scour, multiphase transport |
| **Key solvers** | `sedFoam`, `interFoam`, `pimpleFoam` with custom UDFs |
| **Input data** | Geometry, mesh, boundary conditions, sediment properties |
| **Output** | Velocity field, concentration field, bed evolution |
| **Typical workflow** | Physical problem → equations → geometry → mesh → solver → convergence → validation → visualization |
| **Portfolio project** | Simulate scour around a bridge pier, validate against experimental data |

### ParaView

| Property | Value |
|:---------|:------|
| **Problem solved** | Visualization of CFD results (3D fields, streamlines, contours) |
| **Key features** | Slice, clip, streamline, contour, animation, Python scripting |
| **Input data** | OpenFOAM results (VTK format), any structured/unstructured data |
| **Output** | Publication-quality figures, animations, quantitative extracts |
| **Portfolio project** | Create visualization gallery of CFD sediment transport results |

---

## Full CFD Workflow for Sediment Transport

```
1. Physical Problem
   → Define what you're modeling (scour, transport, deposition)

2. Governing Equations
   → RANS + sediment transport equation (MPM, Van Rijn, etc.)
   → Reynolds decomposition, turbulence closure

3. Assumptions
   → Steady/unsteady, 2D/3D, single-phase/two-phase

4. Geometry
   → Channel, pier, pipeline — define in CAD or blockMesh

5. Mesh
   → blockMesh (structured) or snappyHexMesh (complex geometry)
   → Check quality: aspect ratio, skewness, y+

6. Numerical Scheme
   → Divergence, gradient, Laplacian terms
   → Time stepping: Euler, CrankNicolson, backward

7. Boundary Conditions
   → Inlet (velocity, concentration), outlet (pressure), wall (no-slip)

8. Solver
   → Select appropriate solver (interFoam, sedFoam, pimpleFoam)

9. Convergence
   → Monitor residuals, check physical quantities
   → Adjust under-relaxation, time step if needed

10. Verification
    → Mesh independence study
    → Code verification (manufactured solutions)

11. Validation
    → Compare with experimental data
    → Quantify error

12. Post-Processing
    → ParaView: contours, streamlines, profiles
    → Python: quantitative extraction, statistics
```

---

## Mesh Generation Tips

| Tool | Use Case | When to Use |
|:-----|:---------|:------------|
| `blockMesh` | Simple geometries (channels, pipes) | Rectangular or mapped meshes |
| `snappyHexMesh` | Complex geometries (piers, bridges) | Non-rectangular boundaries |
| `cfMesh` | Automatic meshing | Quick prototyping |
| `snappyHexMesh` + STL | Bodies from CAD | 3D objects in flow |

### Mesh Quality Checklist

```
☐ Maximum skewness < 0.85
☐ Minimum orthogonality > 0.1 (or quality > 0.01 in snappyHexMesh)
☐ Aspect ratio < 100 (ideally < 20)
☐ y+ appropriate for wall treatment (y+ < 1 for low-Re, 30-300 for wall functions)
☐ Sufficient cells in boundary layer
☐ No negative volumes
☐ Adequate resolution in region of interest
```

---

## Data Processing Workflow

```
Raw CFD output (VTK/OpenFOAM)
    ↓
ParaView — extract profiles, planes, streamlines
    ↓
Python (NumPy/Pandas) — read extracted data
    ↓
Statistical analysis — mean, RMS, profiles, budgets
    ↓
Matplotlib — publication-quality plots
    ↓
LaTeX — include in thesis/paper
```

---

## Interview Questions

### Basic (101)
- What is the Shields parameter? When is it used?
- Explain the difference between bed load and suspended load.
- What is the Rouse profile?

### Practical (201)
- How would you set up a sediment transport simulation in OpenFOAM?
- Walk me through a mesh independence study.
- How do you determine the critical shear stress for a given sediment?

### Technical (301)
- Explain the two-phase vs. one-phase approach for sediment transport modeling.
- How does armoring affect sediment transport?
- What turbulence model would you use and why?

### Validation
- How do you validate your CFD results?
- What experimental data would you compare against?
- How do you estimate uncertainty in your predictions?

### Project Defense
- Walk me through your project from problem definition to results.
- What was the biggest challenge in your simulation?
- How did you handle convergence issues?
- What would you do differently with unlimited time?

---

## Study Material

| Tool | Canonical Study Page |
|:-----|:---------------------|
| OpenFOAM | [`deep-dives/openfoam-case-study.md`](../deep-dives/openfoam-case-study.md) |
| HEC-RAS | [`deep-dives/hec-ras-walkthrough.md`](../deep-dives/hec-ras-walkthrough.md) |
| Python | [`programming/python.md`](../programming/python.md) |
| MATLAB | [`programming/matlab.md`](../programming/matlab.md) |

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| Core Sediment Transport | [`core/hwre/hydrology/sediment-transport.md`](../../core/hwre/hydrology/sediment-transport.md) |
| CFD Technology | [`cfd/`](../cfd/cfd-tech.md) |
| HWRE Tech Roadmap | [`hwre/`](../hwre/hwre-tech-roadmap.md) |
| Hydrology Technology | [`hydrology/`](../hydrology/hydrology-tech.md) |
| Python for Engineering | [`programming/python.md`](../programming/python.md) |
| Research Technology | [`research/`](../research/research-tech.md) |

---

*See also: [`cfd-tech.md`](../cfd/cfd-tech.md) for the full CFD technology overview, [`hwre-tech-roadmap.md`](../hwre/hwre-tech-roadmap.md) for general HWRE tools.*
