# Civil Engineering Foundations — Quick Revision Sheet

## Overview

This file serves as a **one-page quick revision** covering all core civil engineering domains. Use it for rapid recall before interviews and GATE.

> **Detailed topics:** [`hydraulics.md`](../hydraulics/hydraulics.md) · [`structures.md`](../structures/structures.md) · [`geotechnical.md`](../geotechnical/geotechnical.md) · [`open-channel-flow.md`](../open_channel_flow/open-channel-flow.md) · [`hydrology.md`](../hydrology/hydrology.md)

---

## 🔢 Fluid Mechanics & Hydraulics — Key Formulas

| Formula | Equation | When to Use |
|---------|----------|-------------|
| Continuity | $A_1V_1 = A_2V_2$ | Mass conservation in pipes |
| Bernoulli | $\frac{P}{\gamma} + \frac{V^2}{2g} + z = \text{const}$ | Energy along streamline |
| Darcy-Weisbach | $h_f = f\frac{L}{D}\frac{V^2}{2g}$ | Pipe friction loss |
| Manning | $V = \frac{1}{n}R^{2/3}S^{1/2}$ | Open channel velocity |
| Reynolds | $Re = \rho VD/\mu$ | Flow regime (laminar/turbulent) |
| Froude | $Fr = V/\sqrt{gD}$ | Subcritical/supercritical |
| Euler | $P_{cr} = \pi^2EI/(KL)^2$ | Column buckling |

**Critical y+ values:**
- $y^+ < 5$: Viscous sublayer (resolve fully)
- $y^+ \approx 30$–$300$: Wall functions
- $y^+ > 300$: Log-law region

**Moody diagram regions:**
- Laminar: $f = 64/Re$
- Transition: Colebrook-White
- Fully turbulent: $f$ depends only on $\epsilon/D$

---

## 🌊 Open Channel Flow — Key Formulas

| Formula | Equation |
|---------|----------|
| Specific Energy | $E = y + V^2/(2g)$ |
| Critical Depth (rect.) | $y_c = (q^2/g)^{1/3}$ |
| Froude Number | $Fr = V/\sqrt{gD_h}$ |
| Conjugate Depth | $y_2/y_1 = 0.5(\sqrt{1+8Fr_1^2}-1)$ |
| Energy Loss (jump) | $\Delta E = (y_2-y_1)^3/(4y_1y_2)$ |
| GVF Equation | $dy/dx = (S_0-S_f)/(1-Fr^2)$ |
| Manning | $Q = (1/n)AR^{2/3}S^{1/2}$ |

**Flow profile types:** M1 (backwater), M2 (drawdown), M3 (rising), S1, S2, S3

---

## 💧 Hydrology — Key Formulas

| Formula | Equation |
|---------|----------|
| Darcy's Law | $Q = KiA$ |
| Horton Infiltration | $f = f_c + (f_0-f_c)e^{-kt}$ |
| Muskingum Routing | $O_2 = C_0I_2 + C_1I_1 + C_2O_1$ |
| Theis (confined) | $s = (Q/4\pi T)W(u)$ |
| Cooper-Jacob | $s = (2.3Q/4\pi T)\log(2.25Tt/r^2S)$ |
| Thiem (steady) | $Q = 2\pi T(h_2-h_1)/\ln(r_2/r_1)$ |
| Gumbel Flood | $x_T = \bar{x} + K\sigma$ |
| Risk | $R = 1-(1-1/T)^n$ |

---

## 🏗️ Structural Mechanics — Key Formulas

| Formula | Equation |
|---------|----------|
| Flexure | $\sigma = My/I$ |
| Shear | $\tau = VQ/Ib$ |
| Torsion | $T/J = \tau/r = G\theta/L$ |
| Euler Buckling | $P_{cr} = \pi^2EI/(KL)^2$ |
| Strain Energy | $U = \int \sigma^2/(2E) dV$ |
| Castigliano | $\delta_i = \partial U/\partial P_i$ |

**IS 456 Key Values:**
- $M_{u,lim} = 0.138 f_{ck} b d^2$ (Fe415)
- $x_{u,max}/d = 0.48$ (Fe415), $0.46$ (Fe500)
- Min steel: $0.85bd/f_y$
- Min shear: $0.4\%$ gross area
- Load factor: $1.5(DL+LL)$

**IS 800 Key Values:**
- $\gamma_{M0} = 1.1$ (yield), $\gamma_{M1} = 1.25$ (ultimate)
- Tension: $T_{dn} = 0.9A_n f_u/\gamma_{M1}$
- Bolt shear: $V_{dsb} = f_{ub} n_n A_{nb}/(\sqrt{3}\gamma_{Mb})$

---

## 🪨 Geotechnical — Key Formulas

| Formula | Equation |
|---------|----------|
| Mohr-Coulomb | $\tau_f = c + \sigma'\tan\phi$ |
| Terzaghi Bearing | $q_u = cN_c + qN_q + 0.5\gamma BN_\gamma$ |
| Rankine Active | $K_a = \tan^2(45°-\phi/2)$ |
| Rankine Passive | $K_p = \tan^2(45°+\phi/2)$ |
| Consolidation | $S = C_cH\log(\sigma'/\sigma'_0)/(1+e_0)$ |
| Time Factor | $T_v = c_v t/H_{dr}^2$ |
| Pile Capacity | $Q_u = q_bA_b + \sum f_sA_s$ |
| Fellenius | $F_s = \sum(c'l+W\cos\alpha\tan\phi')/\sum W\sin\alpha$ |

**Phase Relationships:**
- $Se = wG_s$
- $\gamma_{bulk} = (G_s+Se)\gamma_w/(1+e)$
- $\gamma_{dry} = G_s\gamma_w/(1+e)$

---

## 🌍 HWRE Key Concepts

### Turbulence Models
- **k-ε:** Robust, high-Re; poor near walls
- **k-ω SST:** Best for separation, adverse pressure gradients
- **LES:** Large eddies resolved; high cost
- **DNS:** All scales; very high cost

### Sediment Transport
- **Shields:** $\tau^* = \tau_0/[(\rho_s-\rho)gd]$, $\tau_c^* \approx 0.047$
- **MPM:** $q_b^* = 8(\tau^*-\tau_c^*)^{3/2}$
- **Rouse:** $c/c_a = (y_a/y)^Z$, $Z = w_s/(\kappa u_\tau)$
- **HEC-18 Scour:** $y_s/y_1 = 2.0 K_1 K_2 K_3 K_4 (a/y_1)^{0.35} Fr^{0.43}$

### Water Resources
- **Duty-Delta-DWR:** $D = 864B/d$, $\Delta = 2.63 D \cdot CWR$ (cfs-day/ac-ft)
- **Reservoir Routing:** Level-pool method
- **Canal Design:** Regime theory, Lacey's formula

---

## 🧮 Aptitude Quick Tricks

| Trick | Application |
|-------|-------------|
| Successive % change | $a + b + ab/100$ |
| Product stability | If $A \times B = C$ and A changes by $x\%$, B must change by $-x/(1+x/100)\%$ to keep C constant |
| LCM method | For work problems: assign total work = LCM of times |
| % to fraction | $12.5\% = 1/8$, $16.67\% = 1/6$, $33.33\% = 1/3$ |
| Ratio scaling | $a:b = c:d \Rightarrow ad = bc$ |
| SI/CI | $CI = SI(1 + r/100)$; $CI - SI = SI \times r/100$ |
| Speed ratio | Opposite direction: add; Same direction: subtract |

---

## 🎤 Common Interview Questions — Quick Answers

| Question | Quick Answer |
|----------|-------------|
| Bernoulli assumptions? | Steady, incompressible, frictionless, along streamline |
| Reynolds number meaning? | Ratio of inertial to viscous forces |
| What is y+? | Dimensionless wall distance; determines near-wall treatment |
| Mohr-Coulomb? | $\tau_f = c + \sigma'\tan\phi$ — defines shear strength of soil |
| IS 456 load factor? | 1.5 for DL+LL |
| Euler vs Rankine for columns? | Euler for long (buckling), Rankine for intermediate |
| Darcy's law validity? | Laminar flow through porous media ($Re < 1$) |
| Unit hydrograph assumptions? | Linearity + time-invariance |
| Shields parameter? | Ratio of bed shear to submerged particle weight |
| k-ε vs k-ω SST? | SST better for separation; k-ε for free shear |

---

## Technical Stack for HWRE Roles

| Tool | Application |
|------|-------------|
| Python | Automation, plotting, ML, coding tests |
| MATLAB | Numerical methods, matrix FEM, ODE/PDE |
| OpenFOAM / SedFoam | CFD, RANS/LES, multiphase, scour |
| QGIS / ParaView | GIS workflows, CFD post-processing |
| LaTeX / Overleaf | Reports, formula sheets |
| Git / GitHub | Version control, collaborative tracking |
| HEC-RAS / HEC-HMS | River/hydrologic modeling |
| SAP2000 / ETABS | Structural analysis |

---

## References

