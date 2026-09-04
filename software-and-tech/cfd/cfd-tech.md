# 🌊 CFD / Computational Engineering Technology Roadmap

> **Branch:** CFD / Computational Engineering
> **Particularly strong for M.Tech/research candidates. Covers the full CFD workflow and toolchain.**

---

## Decision Tree

```
CFD student → what tools?

1. Python first         → Data processing, scripting (MUST)
2. Linux + Bash         → HPC environment (MUST)
3. OpenFOAM             → Open-source CFD (MUST)
4. ParaView             → Visualization (MUST)
5. MATLAB               → Numerical methods (HIGH ROI)
6. Git                  → Version control (HIGH ROI)
7. C/C++               → Solver modification (SPECIALIZED)
8. HPC / SLURM         → Large-scale simulations (SPECIALIZED)
```

---

## Full CFD Workflow

```
1. Physical Problem
   → Define what you're solving (flow, heat, sediment, multiphase)

2. Governing Equations
   → Navier-Stokes, RANS, LES, turbulence closure
   → Discretization: FVM (finite volume method)

3. Geometry
   → Define in CAD or blockMesh/snappyHexMesh
   → Simplify: remove unnecessary details

4. Mesh
   → Structured (blockMesh) or unstructured (snappyHexMesh)
   → Quality checks: skewness, orthogonality, aspect ratio, y+

5. Numerical Scheme
   → Divergence, gradient, Laplacian terms
   → Time stepping: steady (simpleFoam) vs unsteady (pimpleFoam)

6. Boundary Conditions
   → Inlet: velocity, turbulence intensity
   → Outlet: pressure, zero gradient
   → Wall: no-slip, wall functions

7. Solver Selection
   → Incompressible: simpleFoam, pimpleFoam
   → Multiphase: interFoam, multiphaseInterFoam
   → Compressible: rhoSimpleFoam, rhoPimpleFoam

8. Convergence
   → Monitor residuals (1e-4 for engineering, 1e-6 for research)
   → Check physical quantities (mass balance, forces)
   → Adjust under-relaxation, time step

9. Verification
   → Mesh independence study (3+ meshes)
   → Code verification (manufactured solutions)
   → Time step sensitivity

10. Validation
    → Compare with experimental data
    → Quantify error (L2 norm, relative error)

11. Post-Processing
    → ParaView: contours, streamlines, vectors
    → Python: quantitative extraction, statistics
    → LaTeX: include in thesis/paper
```

---

## Tool Details

### OpenFOAM

| Property | Value |
|:---------|:------|
| **What** | Open-source CFD toolbox |
| **Developer** | OpenFOAM Foundation / ESI-OpenCFD |
| **License** | Open-source (GPL) |
| **Platform** | Linux (primary) |
| **Key solvers** | simpleFoam, pimpleFoam, interFoam, sedFoam |
| **Learning time to L2** | 20–30 hours |
| **Learning time to L3** | 60–100 hours |
| **Learning time to L4** | 200+ hours |
| **Alternative** | ANSYS Fluent/CFX (commercial) |

### Case Structure

```
case/
├── 0/                    # Initial and boundary conditions
│   ├── U                 # Velocity field
│   ├── p                 # Pressure field
│   ├── nut               # Turbulent viscosity
│   └── k, epsilon/omega  # Turbulence quantities
├── constant/
│   ├── polyMesh/         # Mesh files
│   ├── turbulenceProperties
│   └── transportProperties
├── system/
│   ├── controlDict       # Solver settings, time control
│   ├── fvSchemes         # Numerical schemes
│   ├── fvSolution        # Solver algorithms
│   └── blockMeshDict     # Mesh generation (if using blockMesh)
└── 0.5/, 1.0/, ...      # Time directories (unsteady output)
```

### ParaView

| Property | Value |
|:---------|:------|
| **What** | Open-source 3D visualization |
| **Developer** | Kitware |
| **License** | Open-source (BSD) |
| **Key features** | Slice, clip, contour, streamline, glyph, animation |
| **Learning time to L2** | 10–15 hours |
| **Learning time to L3** | 20–30 hours |
| **Alternative** | EnSight (commercial), FieldView (commercial) |

---

## Mesh Quality Checklist

```
☐ Maximum skewness < 0.85
☐ Minimum orthogonality > 0.1
☐ Aspect ratio < 100 (ideally < 20 for near-wall)
☐ y+ appropriate for wall treatment:
    - y+ < 1 (low-Re, resolved boundary layer)
    - 30 < y+ < 300 (wall functions)
☐ Sufficient cells in boundary layer (10+ cells)
☐ No negative volumes
☐ Adequate resolution in region of interest
☐ Cells refined around geometric features
```

---

## Linux/HPC Skills for CFD

```
Essential:
    → cd, ls, mkdir, cp, mv, rm, cat, less
    → grep, sed, awk (basic text processing)
    → SSH for remote connection
    → File permissions (chmod)
    → Environment variables (export, .bashrc)
    → Package management (apt/yum)
    → Compilation basics (make, wmake)

HPC:
    → SLURM job submission (sbatch, srun)
    → Module system (module load)
    → MPI basics (mpirun, -np)
    → File systems on HPC (/scratch, /home)
    → Batch job scripts
```

---

## Interview Questions

### Basic (101)
- What is CFD? What are its main steps?
- What is the finite volume method?
- Explain the difference between RANS and LES.

### Practical (201)
- Walk me through setting up a simple channel flow in OpenFOAM.
- How do you select the right turbulence model?
- What is y+? How does it affect your simulation?

### Technical (301)
- Explain the SIMPLE algorithm.
- How do you perform a mesh independence study?
- What are the sources of error in a CFD simulation?

### Troubleshooting
- Your simulation diverges after 100 iterations. What do you check?
- Residuals are flat but results look wrong. What's happening?
- How do you handle a complex geometry that won't mesh?

### Project Defense
- Explain your CFD project from problem to results.
- How did you validate your simulation?
- What mesh did you use and why?
- What convergence criteria did you apply?

---

## 🔬 Deep-Dive Walkthroughs

> **"I know I need OpenFOAM. Now how do I actually build a case?"**

Follow the hands-on step-by-step guide to build a complete CFD case end-to-end:

| Tool | Deep-Dive Guide |
|:-----|:----------------|
| OpenFOAM | [`deep-dives/openfoam-case-study.md`](../deep-dives/openfoam-case-study.md) |

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| Sediment Transport | [`sediment/`](../sediment/sediment-tech.md) |
| HWRE Technology | [`hwre/`](../hwre/hwre-tech-roadmap.md) |
| Research Technology | [`research/`](../research/research-tech.md) |
| Linux/Developer Tools | [`developer-tools/`](../developer-tools/linux-dev-tools.md) |
| Cloud/HPC | [`computing/`](../computing/cloud-hpc.md) |
| Core Hydraulics | [`core/hwre/hydraulics/`](../../core/hwre/hydraulics/hydraulics.md) |
| Turbulence Modeling | [`core/hwre/hydraulics/turbulence-modeling.md`](../../core/hwre/hydraulics/turbulence-modeling.md) |

---

*See also: [`sediment-tech.md`](../sediment/sediment-tech.md) for sediment-specific CFD, [`research-tech.md`](../research/research-tech.md) for the research technology stack.*
