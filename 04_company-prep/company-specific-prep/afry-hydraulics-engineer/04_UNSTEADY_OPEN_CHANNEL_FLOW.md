# Module 04: Unsteady Open-Channel Flow & The Saint-Venant Equations

> **Document Focus**: 1D Saint-Venant Governing Equations, Shallow-Water Wave Approximations, Numerical Stability (CFL), and Flood Routing Mechanics  
> **Target Role**: Hydraulics Engineer (AFRY India)  
> **Evidentiary Status**: `[TIER 4 / STATUTORY & ENGINEERING CODES — USACE HEC-RAS, CUNGE, CHOW]`  

---

## 1. Fundamentals of Unsteady Open-Channel Flow

Unsteady flow occurs whenever flow parameters (depth $y$, velocity $v$, discharge $Q$) vary with time at a given cross-section ($\partial y / \partial t \ne 0, \partial Q / \partial t \ne 0$). Typical engineering instances encountered by AFRY include:
* Natural flood wave propagation following extreme rainfall events.
* Dam-break and levee-breach surge dynamics.
* Hydroelectric power plant load rejection or rapid turbine startup, generating positive and negative surges in headrace/tailrace channels.
* Operation of spillway control gates.

---

## 2. Derivation of the 1D Saint-Venant Equations

The 1D Saint-Venant equations (first published by Adhémar Jean-Claude Barré de Saint-Venant in 1871) represent the depth-averaged Navier-Stokes equations under the shallow-water hypothesis:
1. The channel is approximately straight and prismatic.
2. The water depth is small compared to the wavelength, ensuring hydrostatic pressure distribution ($\cos\theta \approx 1$, vertical accelerations negligible).
3. The bed slope is small ($S_0 \ll 1$).
4. Frictional resistance is evaluated using steady-state formulas (Manning or Chezy).
5. The fluid is incompressible and of uniform density.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SAINT-VENANT CONTROL VOLUME BALANCE                      │
│                                                                             │
│                  Water Surface                                              │
│               ───────────────────.                                          │
│              /                    \                                         │
│   Inflow    │                      │   Outflow                              │
│   Q         │      Control         │   Q + (∂Q/∂x)dx                        │
│  ──────────►│      Volume          │──────────►                             │
│             │                      │                                        │
│   Bed       └──────────────────────┘                                        │
│             ◄──────── dx ──────────►                                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.1 Derivation of Continuity Equation
Consider a control volume of length $dx$ between sections 1 and 2. The conservation of mass dictates:
$$\text{Net mass inflow rate} = \text{Rate of mass accumulation inside control volume}$$
$$\rho Q - \left[\rho Q + \frac{\partial(\rho Q)}{\partial x}dx\right] + \rho q_L dx = \frac{\partial(\rho A dx)}{\partial t}$$
where $q_L$ is lateral inflow per unit length ($\text{m}^2\text{/s}$). Dividing by constant density $\rho$ and length $dx$:
$$\boxed{\frac{\partial A}{\partial t} + \frac{\partial Q}{\partial x} - q_L = 0}$$
Since flow area $A$ changes only due to depth $y$ ($dA = T dy$):
$$T \frac{\partial y}{\partial t} + \frac{\partial Q}{\partial x} - q_L = 0$$
Expanding $Q = A v$:
$$T \frac{\partial y}{\partial t} + A \frac{\partial v}{\partial x} + v T \frac{\partial y}{\partial x} - q_L = 0$$

### 2.2 Derivation of Momentum Equation
Newton's second law states that the net external force acting on the fluid element equals the time rate of change of linear momentum:
$$\sum F_x = \frac{\partial}{\partial t}(\rho A v dx) + \frac{\partial}{\partial x}(\rho A v^2 dx)$$
The net external forces acting along the flow direction are:
1. **Hydrostatic pressure force gradient**:
   $$F_{p1} - F_{p2} = -\frac{\partial F_p}{\partial x}dx = -\rho g A \frac{\partial y}{\partial x}dx$$
2. **Gravity body force component along bed slope**:
   $$W_x = \rho g A dx \sin\theta \approx \rho g A S_0 dx$$
3. **Boundary shear resistance (friction force)**:
   $$F_f = -\tau_0 P dx = -\rho g A S_f dx$$
4. **Lateral inflow momentum**:
   $$M_L = \rho q_L v_x dx$$
Summing the forces and equating to momentum flux:
$$-\rho g A \frac{\partial y}{\partial x}dx + \rho g A S_0 dx - \rho g A S_f dx = \frac{\partial}{\partial t}(\rho Q dx) + \frac{\partial}{\partial x}\left(\rho \frac{\beta Q^2}{A}dx\right)$$
Dividing by $\rho g A dx$:
$$\boxed{\frac{1}{g A}\frac{\partial Q}{\partial t} + \frac{1}{g A}\frac{\partial}{\partial x}\left(\frac{\beta Q^2}{A}\right) + \frac{\partial y}{\partial x} - S_0 + S_f = 0}$$

In non-conservative primitive velocity form ($v, y$):
$$\underbrace{\frac{1}{g}\frac{\partial v}{\partial t}}_{\text{Local Acceleration}} + \underbrace{\frac{v}{g}\frac{\partial v}{\partial x}}_{\text{Convective Acceleration}} + \underbrace{\frac{\partial y}{\partial x}}_{\text{Pressure Gradient}} + \underbrace{S_f}_{\text{Friction Slope}} - \underbrace{S_0}_{\text{Bed Slope}} = 0$$

---

## 3. Wave Approximations & Modeling Hierarchy

Depending on which terms in the momentum equation dominate, the Saint-Venant system simplifies into three operational modeling tiers:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SAINT-VENANT HIERARCHY COMPARISON                        │
├─────────────────────┬───────────────────────────────────────────────────────┤
│ APPROXIMATION       │ MOMENTUM EQUATION & PHYSICAL MEANING                  │
├─────────────────────┼───────────────────────────────────────────────────────┤
│ **Kinematic Wave**  │ $S_0 = S_f$                                           │
│                     │ Inflow translates downstream without wave peak        │
│                     │ attenuation. No backwater influence possible.         │
├─────────────────────┼───────────────────────────────────────────────────────┤
│ **Diffusion Wave**  │ $S_0 - \frac{\partial y}{\partial x} = S_f$           │
│                     │ Includes pressure gradient; models wave subsidence    │
│                     │ (attenuation) and mild backwater effects.             │
├─────────────────────┼───────────────────────────────────────────────────────┤
│ **Dynamic Wave**    │ All terms retained:                                   │
│ (Full 1D / HEC-RAS) │ $\frac{1}{g}\frac{\partial v}{\partial t} + \frac{v}{g}\frac{\partial v}{\partial x} + \frac{\partial y}{\partial x} - S_0 + S_f = 0$       │
│                     │ Accurately models tidal reversals, loop rating curves,│
│                     │ dam breaks, and rapidly surging hydro transients.     │
└─────────────────────┴───────────────────────────────────────────────────────┘
```

### 3.1 Kinematic Wave Mechanics
* **Governing Relation**: Discharge is a strict function of local flow depth: $Q = f(A) = \alpha A^m$.
* **Wave Celerity ($c_k$)**: Differentiating continuity:
  $$\frac{\partial A}{\partial t} + \frac{dQ}{dA}\frac{\partial A}{\partial x} = 0 \implies \frac{\partial A}{\partial t} + c_k \frac{\partial A}{\partial x} = 0$$
  where the kinematic celerity is:
  $$c_k = \frac{dQ}{dA}$$
* For a wide rectangular channel using Manning's equation ($Q = \frac{1}{n} b y^{5/3} S_0^{1/2} = \alpha A^{5/3}$):
  $$c_k = \frac{d}{dA}(\alpha A^{5/3}) = \frac{5}{3}\alpha A^{2/3} = \frac{5}{3}v$$
  **Key Rule**: The kinematic flood wave travels at **1.67 times the mean water velocity**!

### 3.2 Diffusion Wave Mechanics
By retaining the pressure gradient $\partial y / \partial x$, the governing momentum balance becomes:
$$Q = K \sqrt{S_0 - \frac{\partial y}{\partial x}}$$
where $K$ is channel conveyance ($K = \frac{1}{n} A R^{2/3}$). Differentiating and substituting into continuity yields the non-linear advection-diffusion equation:
$$\frac{\partial Q}{\partial t} + c_d \frac{\partial Q}{\partial x} = D_h \frac{\partial^2 Q}{\partial x^2}$$
where $D_h$ is the **hydraulic diffusion coefficient**:
$$D_h = \frac{Q}{2 B S_0}$$
* Physical Implication: As the flood wave travels down the river, $D_h$ causes the peak discharge to flatten (peak attenuation) while stretching the hydrograph time base.

---

## 4. Numerical Solution Schemes & The CFL Stability Criterion

### 4.1 Numerical Discretization in HEC-RAS (Preissmann 4-Point Implicit Scheme)
The USACE HEC-RAS 1D unsteady flow engine utilizes the **Preissmann Box Scheme**, an implicit finite-difference technique that evaluates spatial and temporal derivatives on a compact $2 \times 2$ grid:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       PREISSMANN 4-POINT IMPLICIT GRID                      │
│                                                                             │
│       Time (t)                                                              │
│          ▲                                                                  │
│    t+Δt  ┼──────────────●────────────────────────● (n+1)                    │
│          │             (i)                      (i+1)                       │
│          │                                                                  │
│     t    ┼──────────────●────────────────────────● (n)                      │
│          │             (i)                      (i+1)                       │
│          └──────────────┴────────────────────────┴────────► Distance (x)    │
│                        x_i                      x_{i+1}                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

The function $f(x, t)$ and its derivatives are approximated using weighting parameters $\theta$ (time weighting, typically $0.6 \le \theta \le 1.0$) and spatial midpoint:
$$\frac{\partial f}{\partial t} \approx \frac{(f_{i}^{n+1} + f_{i+1}^{n+1}) - (f_{i}^n + f_{i+1}^n)}{2 \Delta t}$$
$$\frac{\partial f}{\partial x} \approx \theta \frac{f_{i+1}^{n+1} - f_{i}^{n+1}}{\Delta x} + (1 - \theta)\frac{f_{i+1}^n - f_{i}^n}{\Delta x}$$
When $\theta = 0.5$, the scheme is second-order accurate in time (Crank-Nicolson) but marginally stable. In HEC-RAS, $\theta = 0.6 \text{ to } 1.0$ is utilized to introduce numerical damping that suppresses non-physical high-frequency oscillations.

### 4.2 The Courant-Friedrichs-Lewy (CFL) Condition
The CFL condition governs the relationship between computational space step $\Delta x$ and time step $\Delta t$. The **Courant Number ($Cr$)** is defined as:
$$Cr = \frac{(v + c)\Delta t}{\Delta x}$$
where $v$ is mean flow velocity and $c = \sqrt{g D_h}$ is gravity wave celerity.
* **Explicit Schemes**: Strictly require $Cr \le 1.0$ to prevent explosive mathematical instability.
* **Implicit Schemes (HEC-RAS)**: While unconditionally stable mathematically for any $Cr$, practical solution accuracy requires:
  $$Cr \le 1.0 \text{ to } 2.0 \quad (\text{Target: } Cr \approx 1.0 \text{ in flood routing reaches})$$
  If $Cr \gg 2.0$, numerical diffusion artificially attenuates the flood peak and delays arrival timing.

---

## 5. Solved Numerical Example: CFL Grid Sizing & Kinematic Wave Routing

**Statement**: An upstream mountain river reach of length $L = 12\text{ km}$ has a bed slope of $S_0 = 0.0025$, Manning's $n = 0.035$, and an approximately rectangular bed width of $b = 40\text{ m}$. During a design flood, the mean flow depth is $y = 3.5\text{ m}$.
1. Compute the steady mean velocity $v$, wave celerity $c$, and dynamic wave speed $(v + c)$.
2. Calculate the kinematic wave celerity $c_k$ and the estimated travel time of the flood peak across the 12 km reach.
3. If an engineer sets cross-section spacing at $\Delta x = 200\text{ m}$ in HEC-RAS, determine the maximum allowable time step $\Delta t$ to ensure $Cr \le 1.0$.

**Solution**:
1. **Flow Velocity & Wave Celerity**:
   $$A = b y = 40 \times 3.5 = 140\text{ m}^2$$
   $$P = b + 2y = 40 + 2(3.5) = 47.0\text{ m} \implies R = \frac{140}{47} = 2.9787\text{ m}$$
   Applying Manning's equation:
   $$v = \frac{1}{n} R^{2/3} S_0^{1/2} = \frac{1}{0.035} (2.9787)^{2/3} (0.0025)^{1/2} = \frac{1}{0.035} (2.0709) (0.05) = \mathbf{2.958\text{ m/s}}$$
   Discharge: $Q = 140 \times 2.958 = 414.12\text{ m}^3\text{/s}$.
   Gravity wave celerity ($c$):
   $$c = \sqrt{g D_h} = \sqrt{9.81 \times 3.5} = \sqrt{34.335} = \mathbf{5.860\text{ m/s}}$$
   Dynamic propagation speed:
   $$v + c = 2.958 + 5.860 = \mathbf{8.818\text{ m/s}}$$

2. **Kinematic Wave Celerity & Travel Time**:
   For a wide channel, kinematic wave celerity is:
   $$c_k = \frac{5}{3} v = \frac{5}{3}(2.958) = \mathbf{4.930\text{ m/s}}$$
   Travel time of the flood peak over $L = 12,000\text{ m}$:
   $$t_{\text{travel}} = \frac{L}{c_k} = \frac{12,000\text{ m}}{4.930\text{ m/s}} = 2434.1\text{ seconds} \approx \mathbf{40.57\text{ minutes}}$$

3. **CFL Time Step Requirement**:
   To satisfy $Cr = \frac{(v + c)\Delta t}{\Delta x} \le 1.0$:
   $$\Delta t \le \frac{\Delta x}{v + c} = \frac{200\text{ m}}{8.818\text{ m/s}} = 22.68\text{ seconds}$$
   **Engineering Recommendation**: Set HEC-RAS unsteady simulation computation interval to **$\Delta t = 20\text{ seconds}$** (or smaller integer divisor, e.g., 15 s) to maintain numerical stability and prevent artificial peak attenuation.

