# Civil Infrastructure Engineering Fundamentals

**Target Role:** Early Career Professionals (ECP) | AECOM India  
**Context:** IIT Kanpur Placement Season 2026–27  
**Coverage:** Soil Mechanics, Foundation Engineering, Structural Analysis, RCC Design, Surveying, Project Management

---

## 1. Soil Mechanics & Foundation Engineering

### 1.1 Effective Stress Principle (Terzaghi, 1925)
Total vertical stress ($\sigma$) at depth $z$ is partitioned between the mineral skeleton and the pore water:

$$\sigma = \sigma' + u \implies \sigma' = \sigma - u$$
- All soil deformation, volume change, consolidation, and shear strength are strictly governed by **effective stress $\sigma'$**, never total stress $\sigma$.
- In submerged soils, upward seepage reduces effective stress: $\sigma' = z (\gamma_{\text{sat}} - \gamma_w) - i z \gamma_w$.
- **Quick Sand Condition:** Occurs when upward hydraulic gradient $i$ reaches the critical gradient $i_{\text{crit}}$, driving effective stress to zero:
  $$i_{\text{crit}} = \frac{\gamma'}{\gamma_w} = \frac{G_s - 1}{1 + e} \approx 1.0 \quad (\text{for } G_s = 2.65, e = 0.65)$$

### 1.2 Shear Strength & Mohr-Coulomb Failure Criterion
$$\tau_f = c' + \sigma' \tan\phi'$$
- $c'$: Effective cohesion (intercept on shear stress axis).
- $\phi'$: Effective angle of internal friction.
- **Triaxial Test Regimes:**
  - *Consolidated Drained (CD):* Measures drained effective parameters ($c', \phi'$) for long-term embankment stability.
  - *Consolidated Undrained (CU):* Measures pore pressure build-up during rapid loading (e.g., sudden reservoir drawdown).
  - *Unconsolidated Undrained (UU):* Measures short-term undrained shear strength $s_u = c_u$ ($\phi_u = 0$) during rapid construction.

### 1.3 Lateral Earth Pressure on Retaining Walls
1. **Rankine Theory (Smooth, Vertical Wall):**
   - Active Earth Pressure Coefficient:
     $$K_a = \frac{1 - \sin\phi}{1 + \sin\phi} = \tan^2\left(45^\circ - \frac{\phi}{2}\right)$$
     Active horizontal stress: $\sigma_a = K_a \sigma_v' - 2 c' \sqrt{K_a}$. Depth of tensile crack: $z_c = \frac{2 c'}{\gamma \sqrt{K_a}}$.
   - Passive Earth Pressure Coefficient:
     $$K_p = \frac{1 + \sin\phi}{1 - \sin\phi} = \tan^2\left(45^\circ + \frac{\phi}{2}\right) = \frac{1}{K_a}$$
     Passive horizontal stress: $\sigma_p = K_p \sigma_v' + 2 c' \sqrt{K_p}$.

### 1.4 Shallow Foundation Bearing Capacity (Terzaghi Formulation)
For a continuous strip footing of width $B$ at foundation depth $D_f$:

$$q_u = c' N_c + \gamma D_f N_q + \frac{1}{2} \gamma B N_\gamma$$
Where $N_c, N_q, N_\gamma$ are dimensionless bearing capacity factors depending solely on friction angle $\phi'$.
- Safe bearing capacity: $q_{\text{safe}} = \frac{q_u - \gamma D_f}{FOS} + \gamma D_f$, where $FOS = 2.5 \text{ to } 3.0$.
- Water Table Correction: If water table rises to ground level, the surcharge ($\gamma D_f$) and self-weight ($\gamma B$) terms are reduced by using submerged unit weight $\gamma' \approx 0.5 \gamma_{\text{bulk}}$, halving bearing capacity!

---

## 2. Structural Analysis & Reinforced Concrete (RCC)

### 2.1 Static Determinacy & Beam Mechanics
- **Degree of Static Indeterminacy:** $D_s = r - 3$ for 2D beams/frames (where $r$ is reaction components).
- **SFD and BMD Differential Relationships:**
  $$\frac{dV}{dx} = -w(x) \quad (\text{Slope of Shear Force Diagram equals negative distributed load})$$
  $$\frac{dM}{dx} = V(x) \quad (\text{Slope of Bending Moment Diagram equals Shear Force})$$
  *Rule:* Maximum or minimum bending moment occurs at points where shear force changes sign ($V = 0$).

### 2.2 Reinforced Concrete Design: Limit State Method (IS 456:2000)
1. **Limit State of Collapse (Flexure):**
   - Maximum compressive strain in concrete at extreme outer fiber: $\epsilon_{cu} = 0.0035$.
   - Idealized parabolic-rectangular stress block: compressive stress $= 0.446 f_{ck}$, depth of centroid $= 0.416 x_u$.
   - Total Compressive Force: $C = 0.36 f_{ck} b x_u$.
   - Total Tensile Force: $T = 0.87 f_y A_{st}$.
   - **Limiting Neutral Axis Depth:**
     $$\frac{x_{u, \text{lim}}}{d} = \frac{0.0035}{0.0055 + \frac{0.87 f_y}{E_s}} = \begin{cases} 0.53 & \text{for } \text{Fe 250} \\ 0.48 & \text{for } \text{Fe 415} \\ 0.46 & \text{for } \text{Fe 500} \end{cases}$$
   - **Limiting Moment of Resistance:**
     $$M_{u, \text{lim}} = 0.36 f_{ck} b x_{u, \text{lim}} (d - 0.416 x_{u, \text{lim}}) = \begin{cases} 0.148 f_{ck} b d^2 & (\text{Fe 250}) \\ 0.138 f_{ck} b d^2 & (\text{Fe 415}) \\ 0.133 f_{ck} b d^2 & (\text{Fe 500}) \end{cases}$$

### 2.3 Liquid Retaining Structures (IS 3370:2021)
For environmental, water, and wastewater tanks at AECOM:
- Designed to **prevent through-wall cracking** and water leakage.
- Direct tension and flexural tension checked against permissible uncracked tensile strength of concrete:
  $$\sigma_{ct} = \frac{T}{A_c + (m - 1) A_{st}} \le \sigma_{ct, \text{perm}}$$
- Mandatory crack width limitation: $w_{\text{max}} \le 0.1\text{ mm}$ for critical water retaining elements.

---

## 3. Surveying & Geomatics

### 3.1 Leveling & Atmospheric Corrections
- **Curvature Correction ($C_c$):** Due to Earth's spherical curvature, the horizontal line of sight diverges upward from the level surface:
  $$C_c = -\frac{d^2}{2R} \approx -0.0785 d^2 \quad (C_c \text{ in meters, } d \text{ in km})$$
- **Refraction Correction ($C_r$):** Atmospheric light rays bend downward:
  $$C_r = +\frac{1}{7} \frac{d^2}{2R} \approx +0.0112 d^2$$
- **Combined Curvature & Refraction Correction ($C$):**
  $$C = C_c + C_r = -0.0673 d^2 \quad (\text{Subtracted from staff reading})$$

### 3.2 Coordinate Reference Systems in Infrastructure BIM/GIS
- **WGS84 (EPSG:4326):** Geographic coordinate system (Latitude/Longitude in decimal degrees).
- **Universal Transverse Mercator (UTM):** Conformal cylindrical map projection dividing the globe into 60 zones of $6^\circ$ longitude each, providing planar coordinates in meters (Northing/Easting) essential for civil alignment modeling in Civil 3D.

---

## 4. Construction Project Management (CPM / PERT)

Infrastructure projects (highways, metros, dams) at AECOM utilize Network Scheduling:

```
 Node Representation: [ Earliest Start (ES) | Task Name | Earliest Finish (EF) ]
                      [ Latest Start (LS)   | Duration  | Latest Finish (LF)   ]
```

- **Critical Path:** The sequence of dependent activities that determines the shortest possible project completion time. An activity is on the critical path iff its **Total Float is zero ($TF = 0$)**:
  $$TF_i = LF_i - EF_i = LS_i - ES_i = 0$$
- **Free Float ($FF$):** Float available without delaying the early start of any immediate successor:
  $$FF_i = ES_{\text{successor}} - EF_i$$
- **PERT Expected Activity Duration (Beta Distribution):**
  $$t_e = \frac{t_o + 4 t_m + t_p}{6}, \quad \text{Variance } \sigma^2 = \left(\frac{t_p - t_o}{6}\right)^2$$
  Where $t_o$ is optimistic time, $t_m$ is most likely time, and $t_p$ is pessimistic time.
