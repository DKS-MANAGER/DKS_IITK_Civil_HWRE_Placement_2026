# 05 — Dimensional Analysis, Similitude & Model Laws

> **Discipline**: Fundamental Fluid Mechanics & Hydraulic Scale Modeling  
> **Key Exam / Interview Topics**: Rayleigh's method, Buckingham $\pi$-theorem, Repeating variables selection, Dimensionless numbers (Reynolds, Froude, Weber, Euler, Mach), Model laws, Distorted hydraulic models.

---

## 1. Buckingham $\pi$-Theorem

If a physical phenomenon involves $n$ physical variables which can be expressed in terms of $m$ fundamental dimensions ($M, L, T$ or $F, L, T$), the relation can be grouped into $(n - m)$ independent dimensionless $\pi$-terms:
$$f(\pi_1, \pi_2, \dots, \pi_{n-m}) = 0$$

### Rules for Selecting Repeating Variables ($m$ variables):
1. Must not form a dimensionless group by themselves.
2. Must collectively contain all fundamental dimensions ($M, L, T$).
3. Standard convention:
   * 1 Geometric property (e.g., Length $L$ or Diameter $D$).
   * 1 Kinematic / Flow property (e.g., Velocity $V$).
   * 1 Dynamic / Fluid property (e.g., Density $\rho$ or Viscosity $\mu$).

---

## 2. Dimensionless Numbers in Fluid Mechanics

| Number | Mathematical Definition | Physical Force Ratio | Primary Application Domain |
| :--- | :--- | :--- | :--- |
| **Reynolds Number ($Re$)** | $Re = \frac{\rho V L}{\mu} = \frac{V L}{\nu}$ | $\frac{\text{Inertia Force}}{\text{Viscous Force}}$ | Submerged pipe flow, aircraft wings, submarines, laminar-turbulent transition. |
| **Froude Number ($Fr$)** | $Fr = \frac{V}{\sqrt{g L}}$ | $\sqrt{\frac{\text{Inertia Force}}{\text{Gravity Force}}}$ | Free-surface flows, rivers, spillways, ship bow waves, hydraulic jumps. |
| **Euler Number ($Eu$)** | $Eu = \frac{V}{\sqrt{\Delta P / \rho}} = \frac{\Delta P}{\rho V^2}$ | $\frac{\text{Pressure Force}}{\text{Inertia Force}}$ | Cavitation phenomena, valve throttling, pressure drop in conduits. |
| **Weber Number ($We$)** | $We = \frac{\rho V^2 L}{\sigma}$ | $\frac{\text{Inertia Force}}{\text{Surface Tension Force}}$ | Droplet breakup, atomization, liquid sprays, very small scale weirs. |
| **Mach Number ($M$)** | $M = \frac{V}{c} = \frac{V}{\sqrt{K/\rho}}$ | $\sqrt{\frac{\text{Inertia Force}}{\text{Elastic Force}}}$ | High-speed compressible aerodynamics, water hammer pressure wave propagation. |

---

## 3. Model Laws & Scale Ratios

### 1. Froude Model Law (Gravity Dominant — Rivers, Spillways, Channels):
Condition: $Fr_m = Fr_p \implies \frac{V_m}{\sqrt{g_m L_m}} = \frac{V_p}{\sqrt{g_p L_p}}$.
Assuming $g_m = g_p$:
* **Velocity Scale Ratio**: $V_r = \sqrt{L_r}$.
* **Time Scale Ratio**: $T_r = \frac{L_r}{V_r} = \sqrt{L_r}$.
* **Discharge Scale Ratio**: $Q_r = A_r V_r = L_r^2 \cdot L_r^{1/2} = L_r^{2.5} = L_r^{5/2}$.
* **Force Scale Ratio**: $F_r = m_r a_r = \rho_r L_r^3 \cdot g_r = \rho_r L_r^3$.
* **Power Scale Ratio**: $P_r = F_r V_r = \rho_r L_r^3 \cdot L_r^{1/2} = \rho_r L_r^{3.5}$.

### 2. Reynolds Model Law (Viscosity Dominant — Pipe Networks, Deep Submarines):
Condition: $Re_m = Re_p \implies \frac{\rho_m V_m L_m}{\mu_m} = \frac{\rho_p V_p L_p}{\mu_p}$.
* **Velocity Scale Ratio**: $V_r = \frac{\nu_r}{L_r}$.
* **Discharge Scale Ratio**: $Q_r = A_r V_r = L_r^2 \cdot \frac{\nu_r}{L_r} = L_r \nu_r$.
* **Force Scale Ratio**: $F_r = \rho_r L_r^2 V_r^2 = \mu_r V_r L_r$.

---

## 4. Distorted Hydraulic Models

In river and harbor modeling, if vertical scale were made equal to horizontal scale ($L_r = 1:1,000$), water depths in the model would be just a few millimeters, where surface tension and laminar effects would introduce gross errors.
* **Horizontal Scale Ratio**: $L_{rh} = \frac{L_m}{L_p}$.
* **Vertical Scale Ratio**: $L_{rv} = \frac{H_m}{H_p}$ (where $L_{rv} > L_{rh}$, typically $5\text{--}10\times$ exaggerated vertically).
* **Discharge Ratio in Distorted Model**:
  $$Q_r = A_r V_r = (L_{rh} \cdot L_{rv}) \cdot \sqrt{L_{rv}} = L_{rh} \cdot L_{rv}^{3/2}$$
* **Manning's $n$ Roughness Ratio**:
  $$n_r = \frac{L_{rv}^{2/3}}{L_{rh}^{1/2}}$$
