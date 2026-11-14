# Mechanical Engineering & Mechanics of Materials: Theoretical Foundations
**Target Role:** Graduate Engineer Trainee (GET) — Product Engineering & Advanced Manufacturing  
**Company:** Ola Electric Mobility Limited  
**Standard:** First-Principles Mechanics & Structural Analysis  

---

## 1. Engineering Mechanics: Statics, Dynamics & Free-Body Diagrams (FBD)

### 1.1 Equilibrium of Rigid Bodies
For any vehicle component (chassis tube, suspension swingarm, motor bracket) in static equilibrium:
$$\sum \mathbf{F}_x = 0, \quad \sum \mathbf{F}_y = 0, \quad \sum \mathbf{F}_z = 0$$
$$\sum \mathbf{M}_x = 0, \quad \sum \mathbf{M}_y = 0, \quad \sum \mathbf{M}_z = 0$$

### 1.2 Free-Body Diagram (FBD) Methodology for EV Chassis
When analyzing an electric scooter frame under static and dynamic wheel bump loads:
1. **Isolate the Subsystem:** Cut imaginary boundaries separating the tubular frame from the front fork, rear swingarm pivot, and battery pack mounting bolts.
2. **Apply Active Loads:**
   - Rider + pillion weight: $W_{\text{payload}} = (75 + 75)\text{ kg} \times 9.81\text{ m/s}^2 \approx 1472\text{ N}$ applied at seat rails.
   - Battery pack dead weight: $W_{\text{battery}} \approx 25 - 35\text{ kg} \times 9.81 \approx 245 - 343\text{ N}$ distributed across under-floor mounting lugs.
   - Motor torque reaction: $T_{\text{motor}} \approx 60 - 100\text{ Nm}$ reacted at the mid-drive stator plate.
3. **Apply Dynamic Road Shock Factor:**
   - In 2W automotive design, road potholes and curb strikes impart vertical accelerations of $2.5g$ to $3.5g$.
   - Design dynamic load: $F_{\text{dynamic}} = m \cdot (g + a_{\text{bump}}) \approx 3.0 \cdot W_{\text{static}}$.

---

## 2. Stress, Strain & Continuum Mechanics

### 2.1 The Cauchy Stress Tensor
At any internal material point, the 3D stress state is represented by the symmetric second-order Cauchy stress tensor:
$$\boldsymbol{\sigma} = \begin{bmatrix} \sigma_x & \tau_{xy} & \tau_{xz} \\ \tau_{yx} & \sigma_y & \tau_{yz} \\ \tau_{zx} & \tau_{zy} & \sigma_z \end{bmatrix}, \quad \text{where } \tau_{ij} = \tau_{ji}$$

### 2.2 Generalized Hooke’s Law (Isotropic Linear Elasticity)
For an isotropic material with Young’s modulus $E$, shear modulus $G$, and Poisson’s ratio $\nu$:
$$\varepsilon_x = \frac{1}{E}\left[\sigma_x - \nu(\sigma_y + \sigma_z)\right]$$
$$\varepsilon_y = \frac{1}{E}\left[\sigma_y - \nu(\sigma_x + \sigma_z)\right]$$
$$\varepsilon_z = \frac{1}{E}\left[\sigma_z - \nu(\sigma_x + \sigma_y)\right]$$
$$\gamma_{xy} = \frac{\tau_{xy}}{G}, \quad \gamma_{yz} = \frac{\tau_{yz}}{G}, \quad \gamma_{zx} = \frac{\tau_{zx}}{G}$$
Relationship between elastic constants:
$$G = \frac{E}{2(1 + \nu)}, \quad K = \frac{E}{3(1 - 2\nu)}$$

### 2.3 Plane Stress vs Plane Strain
- **Plane Stress ($\sigma_z = \tau_{xz} = \tau_{yz} = 0$):**  
  Applies to thin sheet-metal components, chassis tube walls, and battery enclosure panels. Stress through the thickness is zero, but out-of-plane normal strain $\varepsilon_z = -\frac{\nu}{E}(\sigma_x + \sigma_y) \ne 0$.
- **Plane Strain ($\varepsilon_z = \gamma_{xz} = \gamma_{yz} = 0$):**  
  Applies to thick, heavily constrained solid sections (e.g., massive die-cast swingarm pivot bosses). Normal stress out-of-plane is non-zero: $\sigma_z = \nu(\sigma_x + \sigma_y)$.

---

## 3. Mohr's Circle & Principal Stresses (Analytical Derivation)

### 3.1 Stress Transformation Equations
Consider an element rotated by angle $\theta$ counter-clockwise:
$$\sigma_{x'} = \frac{\sigma_x + \sigma_y}{2} + \frac{\sigma_x - \sigma_y}{2}\cos 2\theta + \tau_{xy}\sin 2\theta$$
$$\tau_{x'y'} = -\frac{\sigma_x - \sigma_y}{2}\sin 2\theta + \tau_{xy}\cos 2\theta$$

### 3.2 Circle Invariant & Principal Stresses
Squaring and summing eliminating $\theta$:
$$\left(\sigma_{x'} - \frac{\sigma_x + \sigma_y}{2}\right)^2 + \tau_{x'y'}^2 = \left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2 = R^2$$
This is the equation of a circle with center $C = \left(\frac{\sigma_x + \sigma_y}{2}, 0\right)$ and radius $R = \sqrt{\left(\frac{\sigma_x - \sigma_y}{2}\right)^2 + \tau_{xy}^2}$.
- **Major Principal Stress ($\sigma_1$):**
  $$\sigma_1 = \frac{\sigma_x + \sigma_y}{2} + R$$
- **Minor Principal Stress ($\sigma_2$):**
  $$\sigma_2 = \frac{\sigma_x + \sigma_y}{2} - R$$
- **Maximum In-Plane Shear Stress ($\tau_{\max}$):**
  $$\tau_{\max} = R = \frac{\sigma_1 - \sigma_2}{2}$$

---

## 4. Theories of Failure for Vehicle Design

Automotive components fail under different mechanisms depending on material ductility:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        FAILURE THEORIES SELECTION MATRIX                               │
├─────────────────────┬──────────────────────────┬───────────────────────────────────────┤
│ Theory              │ Material Suitability     │ Design Criterion                      │
├─────────────────────┼──────────────────────────┼───────────────────────────────────────┤
│ Von Mises           │ Ductile Metals           │ $\sigma_v \le S_y / FOS$              │
│ (Distortion Energy) │ (Steel Frame, Al 6061)   │ Most accurate; accounts for shear yield│
├─────────────────────┼──────────────────────────┼───────────────────────────────────────┤
│ Tresca              │ Ductile Metals           │ $\tau_{\max} \le S_y / (2 \cdot FOS)$ │
│ (Max Shear Stress)  │ (Conservative baseline)  │ Conservative envelope; polygon in 2D  │
├─────────────────────┼──────────────────────────┼───────────────────────────────────────┤
│ Rankine             │ Brittle Materials        │ $\sigma_1 \le S_{ut} / FOS$           │
│ (Max Normal Stress) │ (Die-Cast Al A380, Glass)│ Governed by tensile fracture plane    │
├─────────────────────┼──────────────────────────┼───────────────────────────────────────┤
│ Mohr-Coulomb        │ Asymmetric Strength      │ Compressive strength $S_{uc} \gg S_{ut}$│
│ (Frictional/Soils)  │ (Ceramics, Cast Irons)   │ Combines shear and normal friction    │
└─────────────────────┴──────────────────────────┴───────────────────────────────────────┘
```

### 4.1 Von Mises (Distortion Energy Theory) Detailed Derivation
Total strain energy $U$ is decomposed into volumetric dilation energy $U_v$ and shape distortion energy $U_d$:
$$U = U_v + U_d$$
- Hydrostatic mean stress: $\sigma_m = \frac{\sigma_1 + \sigma_2 + \sigma_3}{3}$.
- Dilatational energy: $U_v = \frac{3(1 - 2\nu)}{2E} \sigma_m^2$.
- Distortion energy (responsible for shear slip and dislocation movement):
  $$U_d = \frac{1 + \nu}{3E} \left[ \frac{(\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2}{2} \right]$$
In a uniaxial tensile test at yielding: $\sigma_1 = S_y, \sigma_2 = \sigma_3 = 0$:
$$U_{d,\text{yield}} = \frac{1 + \nu}{3E} S_y^2$$
Equating $U_d = U_{d,\text{yield}}$ yields the **Von Mises Equivalent Stress**:
$$\sigma_v = \sqrt{\frac{1}{2}\left[(\sigma_1 - \sigma_2)^2 + (\sigma_2 - \sigma_3)^2 + (\sigma_3 - \sigma_1)^2\right]} \le S_y$$

---

## 5. Strength of Materials in Vehicle Subsystems

### 5.1 Beam Bending & Section Modulus Optimization
For a tubular chassis rail subjected to bending moment $M$:
$$\sigma = \frac{M y}{I} = \frac{M}{Z}$$
where $Z = I / y_{\max}$ is the section modulus.
- For a circular tube (outer diameter $D$, wall thickness $t$):
  $$I = \frac{\pi}{64}(D^4 - d^4) \approx \frac{\pi}{8} D^3 t \quad (\text{for thin walls } t \ll D)$$
  $$Z \approx \frac{\pi}{4} D^2 t$$
- **Engineering Trade-off:** Doubling tube diameter $D$ while halving thickness $t$ maintains the same cross-sectional area (and weight), but **doubles the section modulus $Z$ and bending strength**! However, local thin-wall wrinkling/buckling sets a minimum wall thickness ($t \ge 1.5 - 2.0\text{ mm}$).

### 5.2 Torsion of Vehicle Shafts & Tubular Swingarms
When motor torque $T$ is transmitted:
$$\tau = \frac{T r}{J}, \quad \theta = \frac{T L}{G J}$$
- Solid circular shaft: $J = \frac{\pi D^4}{32}$.
- Thin-walled hollow tube (mean radius $r_m$, thickness $t$):
  $$J \approx 2\pi r_m^3 t$$
- Non-circular closed thin-walled sections (Bredt-Batho shear flow theory):
  $$q = \tau \cdot t = \frac{T}{2 A_m}$$
  where $A_m$ is the area enclosed by the median line of the wall.

### 5.3 Euler Column Buckling & Chassis Struts
Suspension linkages and front fork tubes subjected to compressive axial force $P$ risk catastrophic elastic buckling:
$$P_{cr} = \frac{\pi^2 E I}{L_e^2} = \frac{\pi^2 E A}{(L_e / r_g)^2}$$
where $\lambda = L_e / r_g$ is the slenderness ratio and $r_g = \sqrt{I/A}$ is the radius of gyration.
- When $\lambda < \lambda_c = \sqrt{\frac{2\pi^2 E}{S_y}}$, inelastic buckling governs (Johnson’s parabolic formula).

---

## 6. Fatigue Analysis & Dynamic Road Durability

EV two-wheelers operate under continuous cyclic vibratory stress. Static yield strength is insufficient; components fail via **fatigue fracture** at stresses well below $S_y$.

### 6.1 S-N Curve (Wöhler Curve) & Endurance Limit
- Steels exhibit a true **Endurance Limit ($S_e' \approx 0.50 S_{ut}$)** at $10^6 - 10^7$ cycles.
- Aluminum alloys (used in swingarms and battery enclosures) **do not have a true endurance limit**; their fatigue strength continues to decay indefinitely with cycle count ($S_f$ quoted at $5 \times 10^8$ cycles).

### 6.2 Marin Surface & Environmental Modification Factors
The laboratory endurance limit $S_e'$ is degraded to the operational component endurance limit $S_e$:
$$S_e = k_a \cdot k_b \cdot k_c \cdot k_d \cdot k_e \cdot S_e'$$
- $k_a$: Surface condition factor (machined, ground, as-cast, forged).
- $k_b$: Size factor (larger shafts exhibit higher probability of internal flaws).
- $k_c$: Reliability factor ($99.9\%$ reliability $\implies k_c = 0.753$).
- $k_d$: Temperature factor.
- $k_e$: Stress concentration factor ($k_e = 1 / K_f$, where $K_f = 1 + q(K_t - 1)$).

### 6.3 Mean Stress Corrections (Goodman vs Soderberg vs Gerber)
When cyclic stress consists of both an alternating stress amplitude $\sigma_a = \frac{\sigma_{\max} - \sigma_{\min}}{2}$ and a non-zero mean stress $\sigma_m = \frac{\sigma_{\max} + \sigma_{\min}}{2}$:
- **Modified Goodman Relation (Industry Standard for Brittle/Castings & General Design):**
  $$\frac{\sigma_a}{S_e} + \frac{\sigma_m}{S_{ut}} = \frac{1}{FOS}$$
- **Soderberg Relation (Most Conservative — Anchored to Yield Strength):**
  $$\frac{\sigma_a}{S_e} + \frac{\sigma_m}{S_y} = \frac{1}{FOS}$$
- **Gerber Parabolic Relation (Good fit for ductile steel data):**
  $$\frac{\sigma_a}{S_e} + \left(\frac{\sigma_m}{S_{ut}}\right)^2 = \frac{1}{FOS}$$

---
*End of Mechanical Engineering & Mechanics of Materials.*
