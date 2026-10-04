# Technical Summary — Bridge Hydrodynamic Scour & Structural Risk

> **Project Code**: `bridgerisk`  
> **Domain**: Hydraulic Engineering, River Mechanics & Computational Fluid Dynamics  
> **Software & Tools**: HEC-RAS 2D, OpenFOAM (interFoam), QGIS, Python (NumPy, SciPy, Matplotlib)

---

## 1. Governing Hydrodynamic Equations

The hydrodynamic flow field is governed by the 2D depth-averaged Shallow Water (Saint-Venant) equations derived from the Reynolds-Averaged Navier-Stokes (RANS) equations:

### Continuity Equation:
$$\frac{\partial h}{\partial t} + \frac{\partial (h u)}{\partial x} + \frac{\partial (h v)}{\partial y} = q$$

### Momentum Equations:
$$\frac{\partial (h u)}{\partial t} + \frac{\partial (h u^2)}{\partial x} + \frac{\partial (h u v)}{\partial y} = -g h \frac{\partial z_s}{\partial x} - \frac{\tau_{bx}}{\rho} + \frac{\tau_{xx}}{\rho} + \frac{\tau_{xy}}{\rho}$$

$$\frac{\partial (h v)}{\partial t} + \frac{\partial (h u v)}{\partial x} + \frac{\partial (h v^2)}{\partial y} = -g h \frac{\partial z_s}{\partial y} - \frac{\tau_{by}}{\rho} + \frac{\tau_{yx}}{\rho} + \frac{\tau_{yy}}{\rho}$$

Where $h$ is flow depth, $u, v$ are depth-averaged velocity components in $x, y$, $z_s$ is water surface elevation ($z_s = z_b + h$), and $\tau_{bx}, \tau_{by}$ are bottom shear stresses defined by Manning's formulation:
$$\tau_{bx} = \frac{\rho g n^2 u \sqrt{u^2 + v^2}}{h^{1/3}}$$

---

## 2. Pier Scour Mathematical Formulations

### Federal Highway Administration (FHWA HEC-18 / CSU Equation):
$$y_s = 2.0 \cdot y_1 \cdot K_1 K_2 K_3 K_4 \cdot \left(\frac{a}{y_1}\right)^{0.65} \cdot Fr_1^{0.43}$$
Where:
* $y_s$: Scour depth ($\text{m}$).
* $y_1$: Flow depth directly upstream of pier ($\text{m}$).
* $a$: Pier width ($\text{m}$).
* $Fr_1$: Approach Froude number ($Fr_1 = \frac{V_1}{\sqrt{g y_1}}$).
* $K_1$: Pier nose shape factor ($1.0$ for semicircular, $1.1$ for square nose, $0.9$ for sharp nose).
* $K_2$: Angle of attack correction factor: $K_2 = \left(\cos \theta + \frac{L}{a}\sin \theta\right)^{0.65}$.
* $K_3$: Bed condition factor ($1.1$ for clear-water scour and plane bed).
* $K_4$: Armoring factor for coarse bed materials ($D_{50} \ge 2\text{ mm}$).

---

## 3. Computational Mesh & Boundary Conditions

* **Computational Domain**: $2.4\text{ km}$ river reach upstream and downstream of bridge alignment.
* **Mesh Resolution**: Variable unstructured mesh with cell size $15\text{ m} \times 15\text{ m}$ in floodplains, refined down to $1.5\text{ m} \times 1.5\text{ m}$ around bridge piers and abutments.
* **Upstream Boundary**: Unsteady discharge hydrograph with peak flow $Q_{100} = 2,450\text{ m}^3/\text{s}$.
* **Downstream Boundary**: Normal depth friction slope $S_0 = 0.00085$.
* **Manning's Roughness**: Calibrated $n = 0.032$ (main sandy channel) and $n = 0.065$ (densely vegetated overbanks).
