# Turbulence Modeling

## Relevance to HWRE

Turbulence modeling is critical for computational fluid dynamics (CFD) applications in water resources, including sediment-laden flows, open channel hydraulics, and multiphase interfacial phenomena. Understanding model selection, near-wall treatment, and computational cost trade-offs is essential for HWRE roles involving OpenFOAM or similar solvers.

> **Related topics:** [`hydraulics.md`](hydraulics.md) · [`open-channel-flow.md`](../open_channel_flow/open-channel-flow.md) · [`sediment-transport.md`](../hydrology/sediment-transport.md)

---

## Turbulence Characteristics

### Energy Cascade
- Kinetic energy transfers from large eddies to progressively smaller eddies
- Kolmogorov scales: Smallest scales where viscosity dissipates kinetic energy into heat
- Universal equilibrium range: Statistics depend only on viscosity and dissipation rate
- Energy spectrum: $E(k) = C_K \varepsilon^{2/3} k^{-5/3}$ (Kolmogorov -5/3 law)

### Free Shear vs. Wall-Bounded Turbulence

| Type | Examples | Key Feature |
|------|----------|-------------|
| Free shear | Jets, wakes, mixing layers | Anisotropy persists across the flow |
| Wall-bounded | Boundary layers, channels, pipes | Strong anisotropy near the wall |

- **Log-law region:** Overlap region in turbulent boundary layers where velocity varies logarithmically with wall distance
  $$u^+ = \frac{1}{\kappa} \ln(y^+) + B$$
  where $\kappa = 0.41$ (von Kármán constant), $B = 5.0$, $u^+ = u/u_\tau$, $y^+ = y u_\tau/\nu$

---

## Reynolds-Averaged Navier-Stokes (RANS) Models

### Reynolds Decomposition
$$u_i = \bar{u}_i + u_i'$$

Where $\bar{u}_i$ is the time-averaged velocity and $u_i'$ is the fluctuating component.

### Reynolds-Averaged Momentum Equation
$$\rho \left(\frac{\partial \bar{u}_i}{\partial t} + \bar{u}_j \frac{\partial \bar{u}_i}{\partial x_j}\right) = -\frac{\partial \bar{p}}{\partial x_i} + \frac{\partial}{\partial x_j}\left(\mu \frac{\partial \bar{u}_i}{\partial x_j} - \rho \overline{u_i' u_j'}\right)$$

The term $-\rho \overline{u_i' u_j'}$ is the **Reynolds stress tensor** (6 unknowns for 3D flow) — this is the closure problem.

### Eddy-Viscosity Hypothesis (Boussinesq)
$$-\rho \overline{u_i' u_j'} = \mu_t \left(\frac{\partial \bar{u}_i}{\partial x_j} + \frac{\partial \bar{u}_j}{\partial x_i}\right) - \frac{2}{3} \rho k \delta_{ij}$$

Where $\mu_t$ = turbulent (eddy) viscosity, $k$ = turbulent kinetic energy.

---

### Two-Equation Models

#### k-epsilon (k-ε) Family

**Transport equations:**
$$\frac{\partial (\rho k)}{\partial t} + \nabla \cdot (\rho \bar{u} k) = \nabla \cdot \left[\left(\mu + \frac{\mu_t}{\sigma_k}\right) \nabla k\right] + P_k - \rho \varepsilon$$

$$\frac{\partial (\rho \varepsilon)}{\partial t} + \nabla \cdot (\rho \bar{u} \varepsilon) = \nabla \cdot \left[\left(\mu + \frac{\mu_t}{\sigma_\varepsilon}\right) \nabla \varepsilon\right] + C_{1\varepsilon} \frac{\varepsilon}{k} P_k - C_{2\varepsilon} \rho \frac{\varepsilon^2}{k}$$

$$\mu_t = \rho C_\mu \frac{k^2}{\varepsilon}$$

| Variant | Key Feature | Best For |
|---------|-------------|----------|
| **Standard k-ε** | Baseline; robust, widely validated | High-Re free shear flows, industrial applications |
| **RNG k-ε** | Renormalization group theory; $C_{1\varepsilon}$ varies with strain rate | Swirling flows, moderate curvature |
| **Realizable k-ε** | Non-negative normal stresses; variable $C_\mu$ | Jets, mixing layers, rotating flows |

**Limitations:**
- Requires wall functions or low-Re modification near walls
- Under-predicts separation in adverse pressure gradients
- Poor performance in strong streamline curvature

#### k-omega (k-ω) Family

**Transport equations:**
$$\frac{\partial (\rho k)}{\partial t} + \nabla \cdot (\rho \bar{u} k) = \nabla \cdot \left[\left(\mu + \frac{\mu_t}{\sigma_k}\right) \nabla k\right] + P_k - \beta^* \rho k \omega$$

$$\frac{\partial (\rho \omega)}{\partial t} + \nabla \cdot (\rho \bar{u} \omega) = \nabla \cdot \left[\left(\mu + \frac{\mu_t}{\sigma_\omega}\right) \nabla \omega\right] + \alpha \frac{\omega}{k} P_k - \beta \rho \omega^2$$

$$\mu_t = \rho \frac{k}{\omega}$$

| Variant | Key Feature | Best For |
|---------|-------------|----------|
| **Standard k-ω** | Superior near-wall behavior | Wall-bounded flows, boundary layers |
| **SST k-ω** | Blends k-ω near walls with k-ε in free stream | Adverse pressure gradients, separation |

**SST blending function:**
$$F_1 = \tanh\left(\arg_1^4\right), \quad \arg_1 = \min\left(\max\left(\frac{\sqrt{k}}{\beta^* \omega y}, \frac{500 \nu}{y^2 \omega}\right), \frac{4 \rho \sigma_{\omega 2} k}{CD_{k\omega} y^2}\right)$$

---

### Near-Wall Treatment

| $y^+$ Range | Treatment | Mesh Requirement |
|-------------|-----------|------------------|
| $y^+ < 5$ | Viscous sublayer resolved | Very fine mesh (10–20 cells across BL) |
| $y^+ \approx 30$–$300$ | Wall functions | Coarser mesh acceptable |
| $y^+ > 300$ | Log-law region | May miss important near-wall physics |

**y+ calculation:**
$$y^+ = \frac{y \cdot u_\tau}{\nu}, \quad u_\tau = \sqrt{\frac{\tau_w}{\rho}}$$

**Practical guideline for OpenFOAM:**
- For wall functions: first cell center at $y^+ \approx 30$–$150$
- For low-Re models: $y^+ \approx 1$ (first cell center in viscous sublayer)
- Target: 10–20 cells across the boundary layer for LES

---

## Large Eddy Simulation (LES) vs. DNS vs. RANS

| Method | Resolution | Cost | Fidelity | Typical Use |
|--------|-----------|------|----------|-------------|
| DNS | All scales | Extremely high | Highest | Fundamental research, low Re |
| LES | Large scales | High | High | Complex separated flows, aeroacoustics |
| RANS | Time-averaged | Low | Moderate | Design iterations, industrial applications |

### LES Subgrid-Scale Models
- **Smagorinsky:** $\mu_{sgs} = \rho (C_s \Delta)^2 |\bar{S}|$ — requires $C_s$ tuning
- **Dynamic Smagorinsky:** $C_s$ computed from resolved scales — more accurate
- **WALE:** Wall-Adapting Local Eddy-viscosity — better near-wall behavior without wall functions

### Computational Cost Comparison

| Method | Relative Cost | Grid Points | Time Steps |
|--------|--------------|-------------|------------|
| RANS | 1× | $10^5$–$10^6$ | 1 (steady) |
| LES | 100–1000× | $10^7$–$10^9$ | $10^4$–$10^6$ |
| DNS | $10^4$–$10^6$× | $Re^{9/4}$ | $Re^{3/2}$ |

---

## Multiphase Turbulence

### Volume of Fluid (VOF)
- Tracks interface between immiscible fluids using a phase-fraction function $\alpha$
- $\alpha = 0$ (phase 1), $\alpha = 1$ (phase 2), $0 < \alpha < 1$ (interface)
- Suitable for free-surface flows, waves, and droplet dynamics
- Turbulence: typically RANS (k-ω SST) or LES

### Euler-Euler Approaches
- Treats phases as interpenetrating continua
- Each phase has its own momentum, continuity, and turbulence equations
- Coupling via drag, lift, and virtual mass forces
- Suitable for sediment-laden flows and bubbly flows

### Sediment-Laden Flows
- Turbulence modulation by suspended particles
- Two-way coupling between fluid and sediment phases
- Rouse profile for suspended sediment concentration:
  $$\frac{c}{c_a} = \left(\frac{y_a}{y}\right)^Z, \quad Z = \frac{w_s}{\kappa u_\tau}$$

---

## 🎤 OpenFOAM Case Setup Guide

### RANS Case (k-ω SST)

```
// 0/U — Boundary conditions
inlet       { type fixedValue; value uniform (1 0 0); }
outlet      { type zeroGradient; }
walls       { type noSlip; }
frontAndBack { type empty; }

// 0/k
inlet       { type fixedValue; value uniform 0.01; }
outlet      { type zeroGradient; }
walls       { type kLowReWallFunction; value uniform 0; }

// 0/omega
inlet       { type fixedValue; value uniform 10; }
outlet      { type zeroGradient; }
walls       { type omegaWallFunction; value uniform 0; }
```

**Key dictionary settings (turbulenceProperties):**
```
simulationType RAS;
RAS
{
    model          kOmegaSST;
    turbulence     on;
    printCoeffs    on;
}
```

**Mesh requirements:**
- First cell center: $y^+ \approx 1$ for low-Re SST, $y^+ \approx 30$–$100$ for wall functions
- Boundary layer: 15–20 inflation layers with growth ratio 1.1–1.2
- $y^+$ monitor: `wallFunction` entries in `0/nut` or use `yPlus` function object

### LES Case

```
// turbulenceProperties
simulationType LES;
LES
{
    model          dynSmagorinsky;
    turbulence     on;
    printCoeffs    on;
}
```

**Mesh requirements:**
- Isotropic cells in the bulk region
- Near-wall: $y^+ \approx 1$, 10–20 cells across boundary layer
- Grid resolution: $\Delta < 0.1 L_{integral}$ for energy-containing eddies

### Function Objects for Monitoring

```
functions
{
    yPlus
    {
        type            yPlus;
        libs            ("libfieldFunctionObjects.so");
        writeControl    writeTime;
        fields          (yPlus);
    }
    fieldAverage
    {
        type            fieldAverage;
        libs            ("libfieldFunctionObjects.so");
        writeControl    timeStep;
        writeInterval   100;
        writeFields     true;
        fields
        {
            U           { mean on; prime2Mean on; base (0 0 0); }
            p           { mean on; base (0 0 0); }
            k           { mean on; base 0; }
        }
    }
}
```

---

## 🎤 Interview Q&A

### Q1: When would you choose k-ω SST over standard k-ε?
**A:** SST is preferred for flows with adverse pressure gradients, boundary layer separation, or curved streamlines. The k-ω formulation handles near-wall physics better, and the SST blending switches to k-ε in the free stream to avoid sensitivity to free-stream values. Standard k-ε is fine for high-Re free shear flows without significant separation.

### Q2: What is y+ and why does it matter?
**A:** y+ is the dimensionless wall distance $y^+ = y u_\tau/\nu$. It determines which near-wall region a computational cell resolves. For wall functions, $y^+ \approx 30$–$300$ (log-law region). For low-Re models that resolve the viscous sublayer, $y^+ < 5$. Using the wrong y+ leads to incorrect wall shear stress and velocity profiles.

### Q3: Explain the difference between RANS, LES, and DNS.
**A:** RANS models all turbulent scales using time-averaged equations — cheapest, lowest fidelity. LES resolves large energy-containing eddies and models small subgrid scales — moderate cost, high fidelity. DNS resolves all scales down to the Kolmogorov scale — most expensive, highest fidelity. For HWRE applications, RANS is used for design iterations, LES for detailed scour/hydraulic jump studies, and DNS only for fundamental research.

### Q4: What is the Boussinesq hypothesis and what are its limitations?
**A:** The Boussinesq hypothesis relates Reynolds stresses to mean strain rates through an eddy viscosity: $-\rho \overline{u_i' u_j'} = \mu_t (\partial \bar{u}_i/\partial x_j + \partial \bar{u}_j/\partial x_i) - \frac{2}{3}\rho k \delta_{ij}$. Limitations: (1) assumes isotropic turbulence in the normal stresses, (2) eddy viscosity is a scalar (can't capture anisotropy), (3) fails in strong streamline curvature, rotation, and buoyancy.

### Q5: How do you validate a turbulence model for an OpenFOAM case?
**A:** (1) Grid independence study — refine mesh until results converge. (2) Compare with experimental data (velocity profiles, pressure coefficients, skin friction). (3) Monitor y+ values to ensure appropriate wall treatment. (4) Check residuals converge below $10^{-4}$ for all equations. (5) Verify mass conservation (inlet Q = outlet Q). (6) Use function objects to monitor forces, y+, and field averages.

### Q6: What is the -5/3 law and how is it used?
**A:** Kolmogorov's -5/3 law states that in the inertial subrange, the energy spectrum follows $E(k) = C_K \varepsilon^{2/3} k^{-5/3}$. In practice, it's used to: (1) verify LES grid resolution is adequate (resolved energy should follow this slope), (2) estimate dissipation rate from measured spectra, (3) determine if the computational domain is large enough to capture energy-containing eddies.

---

## Practical Considerations for HWRE

### Solver Selection

| Application | Recommended Model | Rationale |
|-------------|-------------------|-----------|
| Steady pipe flow | RANS k-ε or SST | Cost-effective, well-validated |
| Hydraulic jump | LES + VOF | Unsteady, strong turbulence- Interface interaction |
| Scour around pier | RANS SST or LES | Near-wall accuracy critical |
| Reservoir modeling | RANS k-ε | Large domain, steady-state OK |
| Open channel with sediment | RANS SST + Euler-Euler | Multiphase, turbulence modulation |
| Wave interaction | LES + VOF | Unsteady free surface |

### Mesh Sensitivity
- y+ monitoring is critical for wall-bounded hydraulic simulations
- Boundary layer mesh refinement: 10–20 cells across the boundary layer for LES
- Aspect ratio control in highly anisotropic boundary layer regions
- Run grid convergence index (GCI) study with at least 3 mesh levels

### Model Limitations
- k-epsilon may under-predict separation in adverse pressure gradients
- SST can over-predict separation in some free-shear configurations
- Wall functions become unreliable in strong pressure gradients or massive separation
- RANS cannot capture vortex shedding or unsteady coherent structures

---

## Key Resources

- Pope, *Turbulent Flows* (canonical reference for turbulence theory)
- OpenFOAM documentation for solver selection and case setup
- [`hydraulics.md`](hydraulics.md) — Fundamental hydraulics and pipe flow
- [`../hydrology/sediment-transport.md`](../hydrology/sediment-transport.md) — Sediment-turbulence interaction
