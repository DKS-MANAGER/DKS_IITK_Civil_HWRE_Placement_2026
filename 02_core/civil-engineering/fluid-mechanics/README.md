# Fluid Mechanics — Fundamental Theory & Governing Principles

> **Canonical Ownership**: Fundamental Fluid Mechanics (Properties, Statics, Kinematics, Dynamics, Pipe Flow, Boundary Layer, Dimensional Analysis).  
> **Cross-Discipline Boundaries**:  
> * **Fundamental Fluid Mechanics** $\rightarrow$ [`02_core/civil-engineering/fluid-mechanics/`](README.md) (This section)  
> * **Hydraulics, Open Channel Flow & Hydrology** $\rightarrow$ [`02_core/hwre/`](../../hwre/README.md)  
> * **Numerical CFD, Turbulence Modeling & OpenFOAM** $\rightarrow$ [`02_core/cfd/`](../../cfd/cfd-tech.md)  
> * **Technical Interview Questions** $\rightarrow$ [`05_interview/technical/civil/`](../../../05_interview/technical/civil/README.md) & [`05_interview/technical/hwre/`](../../../05_interview/technical/hwre/README.md)

---

## 1. Topic Architecture & Module Index

```text
fluid-mechanics/
├── README.md                                  # Canonical map & cross-discipline routing
├── 01_fluid-properties-and-statics.md         # Viscosity, hydrostatic pressure, buoyancy & floatation
├── 02_fluid-kinematics-and-dynamics.md        # Continuity, Euler, Bernoulli & momentum principles
├── 03_pipe-flow-and-losses.md                 # Hagen-Poiseuille, Darcy-Weisbach, Moody chart & minor losses
├── 04_boundary-layer-and-drag.md              # Prandtl boundary layer, separation, drag & lift
└── 05_dimensional-analysis-and-similitude.md  # Buckingham Pi theorem & model scaling laws
```

---

## 2. Topic Details & Key Formulas

| Module | Core Topics | Key Governing Equations | Link to Next Level |
| :--- | :--- | :--- | :--- |
| **01. Properties & Statics** | Viscosity (Newtonian vs non-Newtonian), Surface tension, Hydrostatic force on curved gates, Metacentric height. | $\tau = \mu \frac{du}{dy}$, $F = \rho g \bar{h} A$, $h^* = \bar{h} + \frac{I_{xx}}{\bar{h} A}$, $GM = \frac{I}{V} - BG$ | Applied in dam & gate design: [`hwre/`](../../hwre/README.md) |
| **02. Kinematics & Dynamics** | Streamlines, Velocity potential $\phi$ & Stream function $\psi$, Continuity, Euler equation, Bernoulli with head loss. | $\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = 0$, $\frac{p}{\rho g} + \frac{V^2}{2g} + z = \text{const}$ | Extended to Navier-Stokes: [`cfd/`](../../cfd/cfd-tech.md) |
| **03. Pipe Flow & Losses** | Laminar flow, Hagen-Poiseuille, Darcy-Weisbach friction factor, Equivalent pipe, Water hammer. | $h_f = \frac{f L V^2}{2 g D}$, $f_{lam} = \frac{64}{Re}$, $\Delta P = \frac{32 \mu V L}{D^2}$, $c = \sqrt{\frac{K/\rho}{1 + (K D / E t)}}$ | Extended to pipe networks: [`hwre/software-deep-dives/epanet-walkthrough.md`](../../hwre/software-deep-dives/epanet-walkthrough.md) |
| **04. Boundary Layer** | Displacement thickness $\delta^*$, Momentum thickness $\theta$, Shape factor $H$, Boundary separation control. | $\delta^* = \int_0^\delta \left(1 - \frac{u}{U}\right) dy$, $\theta = \int_0^\delta \frac{u}{U}\left(1 - \frac{u}{U}\right) dy$, $\left.\frac{\partial u}{\partial y}\right|_{y=0} = 0$ (separation) | Extended to wall functions ($y^+$): [`cfd/`](../../cfd/cfd-tech.md) |
| **05. Dimensional Analysis**| Buckingham Pi theorem, Reynolds & Froude similitude, Distorted hydraulic models. | $Re = \frac{\rho V L}{\mu}$, $Fr = \frac{V}{\sqrt{g L}}$, $We = \frac{\rho V^2 L}{\sigma}$, $Eu = \frac{\Delta p}{\rho V^2}$ | Applied in spillway flume modeling: [`hwre/`](../../hwre/README.md) |
