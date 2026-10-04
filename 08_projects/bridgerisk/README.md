# Project: Bridge Hydrodynamic Scour & Structural Risk Assessment

> **Project Code**: `bridgerisk`  
> **Domain**: Hydraulic Engineering, River Mechanics & Structural Safety  
> **Key Tools**: HEC-RAS (1D/2D Unsteady Flow), Python (NumPy/Pandas/Matplotlib), QGIS, OpenFOAM

---

## 1. Project Overview & Motivation

Bridge pier scour during high-magnitude flood events is the primary cause of hydraulic bridge failures globally. Conventional empirical equations (e.g., Richardson's CSU equation, Melville-Dongol) often either overpredict scour depths (leading to excessively expensive deep caisson foundations) or underpredict in complex compound channels with debris accumulation.

### Core Objectives:
1. Model hydrodynamic flow fields and shear stress distribution around complex pier geometries under 50-year and 100-year return period flood hydrographs.
2. Predict local and contraction scour depths using 2D shallow water hydrodynamic modeling coupled with sediment transport formulations.
3. Perform probabilistic bridge vulnerability classification and construct depth-damage fragility curves for risk advisory.

---

## 2. Technical Methodology & Workflow

```text
[Bathymetry & LiDAR Dem] ──► [Mesh Generation in QGIS/HEC-RAS] ──► [Unsteady Hydrodynamic 2D Run]
                                                                             │
[Vulnerability Index] ◄── [Scour Fragility Curves] ◄── [CSU / Melville Scour Models]
```

### 1. Hydrodynamic Modeling:
* Solved 2D Saint-Venant shallow water equations using finite volume discretization in HEC-RAS 2D.
* Implemented unsteady Manning's $n$ roughness calibration across main channel ($n=0.032$) and vegetated floodplains ($n=0.065$).

### 2. Pier Scour Formulation:
* Implemented CSU (FHWA HEC-18) equation:
  $$y_s = 2.0 \cdot y_1 \cdot K_1 K_2 K_3 \cdot \left(\frac{a}{y_1}\right)^{0.65} \cdot Fr_1^{0.43}$$
  Where $a$ is pier width, $y_1$ is approach flow depth, $Fr_1$ is approach Froude number, and $K_1, K_2, K_3$ are shape, alignment, and bed condition correction factors.

---

## 3. Key Quantified Outcomes & Findings

* **Scour Depth Prediction**: Identified a peak local scour depth of $4.85\text{ m}$ under the 100-year peak discharge ($2,450\text{ m}^3/\text{s}$), indicating pier foundation exposure risk.
* **Sensitivity Analysis**: Found that skew angle misalignment ($>15^\circ$) increased scour depth by $38\%$ compared to aligned flow.
* **Mitigation Recommendation**: Proposed riprap apron collar protection sizing ($d_{50} = 350\text{ mm}$) to arrest vortex shedding and reduce foundation risk by $60\%$.

---

## 4. Interview Defense & Technical Q&A

### Q1: "Why use 2D shallow water equations over 1D HEC-RAS for pier scour?"
* **Answer**: *"1D models assume one-dimensional flow along a single streamline and cannot resolve lateral velocity gradients, eddy circulation, or skew angle effects around bridge piers. 2D shallow water models compute depth-averaged transverse and longitudinal velocities at each computational cell, giving accurate local approach velocities for scour equations."*

### Q2: "How did you validate your model results without physical flume measurements?"
* **Answer**: *"I cross-validated the 2D hydrodynamic results against observed USGS/CWC gauge stage-discharge rating curves ($R^2 = 0.94$). For scour depth, I performed comparative sensitivity across three established formulations (CSU, Melville-Dongol, and Froehlich) to establish confidence bounds."*
