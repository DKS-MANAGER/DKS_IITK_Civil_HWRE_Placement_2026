# Module 09: Hydraulic Model Studies — Similitude, Scaling & Instrumentation

> **Document Focus**: Physical Scale Modeling, Similitude Laws (Froude, Reynolds, Weber), Scale Effects, Distorted River Models, and Laboratory Instrumentation  
> **Target Role**: Hydraulics Engineer (AFRY India)  
> **Evidentiary Status**: `[TIER 4 / STATUTORY & ENGINEERING CODES — ASCE MANUAL 97, USBR, CWPRS GUIDELINES, KOBUS]`  

---

## 1. Role of Physical Scale Models in Hydraulic Engineering

While numerical simulations (1D HEC-RAS, 2D hydrodynamic solvers, and 3D CFD in OpenFOAM) have advanced dramatically, **physical hydraulic scale models** remain a mandatory statutory requirement for major civil water infrastructure. Complex three-dimensional, highly turbulent phenomena cannot yet be modeled with 100% numerical certainty. These include:
* Vortices and air ingestion at deep hydropower intakes.
* Air entrainment, bulking, and cavitation on steep spillway chutes.
* Dynamic turbulent pressure fluctuations on stilling basin baffle piers and end sills.
* Scour hole geometries in three-dimensional plunge pools and around complex bridge pier groups.

Consulting firms like AFRY routinely draft tender specifications, oversee model fabrication, and interpret physical laboratory test results conducted at national hydraulic research institutions (e.g., Central Water and Power Research Station — CWPRS Pune, or specialized academic flumes at IITs).

---

## 2. The Three Pillars of Hydraulic Similitude

Similitude is the science of establishing dynamic equivalence between a scaled laboratory model (subscript $m$) and a full-size field prototype (subscript $p$). Complete similarity requires satisfying three geometric and physical conditions:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       THE THREE PILLARS OF SIMILITUDE                       │
├─────────────────────┬───────────────────────────────────────────────────────┤
│ 1. GEOMETRIC        │ Exact spatial scaling of all linear dimensions.       │
│    SIMILARITY       │ Length ratio $L_r = L_p / L_m = \text{Constant}$.     │
│                     │ Area ratio $A_r = L_r^2$; Volume ratio $V_r = L_r^3$. │
├─────────────────────┼───────────────────────────────────────────────────────┤
│ 2. KINEMATIC        │ Exact scaling of velocity vectors and acceleration.   │
│    SIMILARITY       │ Flow streamlines in model are geometrically identical │
│                     │ to prototype. Velocity ratio $v_r = v_p / v_m$;       │
│                     │ Time ratio $T_r = T_p / T_m = L_r / v_r$.             │
├─────────────────────┼───────────────────────────────────────────────────────┤
│ 3. DYNAMIC          │ Exact scaling of all active forces acting on fluid.   │
│    SIMILARITY       │ Force ratio $F_r = F_p / F_m = \text{Constant}$.      │
│                     │ Requires identical dimensionless force ratios.        │
└─────────────────────┴───────────────────────────────────────────────────────┘
```

---

## 3. Dimensionless Governing Numbers in Hydraulic Modeling

Dynamic similarity requires the ratio of inertial force ($F_i = \rho L^2 v^2$) to other active forces to be identical in model and prototype:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DIMENSIONLESS FORCE RATIOS IN FLUIDS                     │
├─────────────┬───────────────────────────┬───────────────────────────────────┤
│ NUMBER      │ MATHEMATICAL DEFINITION   │ DOMINANT HYDRAULIC PHENOMENON     │
├─────────────┼───────────────────────────┼───────────────────────────--------┤
│ **Froude**  │ $Fr = \frac{v}{\sqrt{g L}}$│ Free-surface gravity flows:       │
│ ($Fr$)      │ (Inertia / Gravity)       │ Spillways, weirs, open channels,  │
│             │                           │ hydraulic jumps, stilling basins  │
├─────────────┼───────────────────────────┼───────────────────────────────────┤
│ **Reynolds**│ $Re = \frac{v L}{\nu}$     │ Viscous resistance & pipe flow:   │
│ ($Re$)      │ (Inertia / Viscosity)     │ Closed conduits, boundary layers, │
│             │                           │ sediment fall velocity            │
├─────────────┼───────────────────────────┼───────────────────────────────────┤
│ **Weber**   │ $We = \frac{v}{\sqrt{\sigma / (\rho L)}}$│ Surface tension & capillary:      │
│ ($We$)      │ (Inertia / Surface Tension)│ Droplet formation, spray, thin    │
│             │                           │ nappe aeration, air entrainment   │
├─────────────┼───────────────────────────┼───────────────────────────────────┤
│ **Euler**   │ $Eu = \frac{\Delta p}{\frac{1}{2}\rho v^2}$│ Pressure drop & cavitation:       │
│ ($Eu / \sigma$)│ (Inertia / Pressure Force)│ High-head sluice gates, turbines, │
│             │                           │ cavitation index $\sigma$         │
└─────────────┴───────────────────────────┴───────────────────────────────────┘
```

---

## 4. Froude Similitude Laws (Open-Channel & Dam Models)

Because gravity is the overwhelmingly dominant driving force in open-channel and spillway flows, model testing is governed by **Froude Model Law**:
$$Fr_m = Fr_p \implies \frac{v_m}{\sqrt{g_m L_m}} = \frac{v_p}{\sqrt{g_p L_p}}$$
Since models operate on Earth in the same gravitational field ($g_m = g_p$):
$$\frac{v_p}{v_m} = \sqrt{\frac{L_p}{L_m}} \implies \boxed{v_r = \sqrt{L_r} = L_r^{1/2}}$$

### 4.1 Derivation of Standard Froude Scale Ratios
Let the geometric scale ratio be $L_r = L_p / L_m$ (e.g., for a 1:40 scale model, $L_r = 40$).
1. **Length Ratio**: $L_r = \frac{L_p}{L_m}$
2. **Area Ratio**: $A_r = \frac{A_p}{A_m} = L_r^2$
3. **Volume Ratio**: $V_r = \frac{V_p}{V_m} = L_r^3$
4. **Velocity Ratio**: $v_r = \frac{v_p}{v_m} = \sqrt{L_r} = L_r^{1/2}$
5. **Time Scale Ratio**:
   $$T_r = \frac{L_r}{v_r} = \frac{L_r}{L_r^{1/2}} = \boxed{L_r^{1/2} = \sqrt{L_r}}$$
6. **Discharge Scale Ratio**:
   $$Q_r = \frac{Q_p}{Q_m} = A_r v_r = (L_r^2)(L_r^{1/2}) = \boxed{L_r^{5/2} = L_r^{2.5}}$$
7. **Force Scale Ratio**:
   $$F_r = m_r a_r = (\rho_r L_r^3)\left(\frac{L_r}{T_r^2}\right) = \rho_r L_r^3 \left(\frac{L_r}{L_r}\right) = \boxed{\rho_r L_r^3}$$
   When freshwater is used in both model and prototype ($\rho_r = 1.0$):
   $$F_r = \boxed{L_r^3}$$
8. **Pressure Head Ratio**:
   $$H_r = \frac{H_p}{H_m} = \boxed{L_r}$$
9. **Power Scale Ratio**:
   $$P_r = F_r v_r = (L_r^3)(L_r^{1/2}) = \boxed{L_r^{7/2} = L_r^{3.5}}$$
10. **Manning Roughness Scale Ratio**:
    From Manning's equation $v = \frac{1}{n} R^{2/3} S^{1/2}$:
    $$v_r = \frac{1}{n_r} R_r^{2/3} S_r^{1/2} \implies L_r^{1/2} = \frac{1}{n_r} (L_r)^{2/3} (1)^{1/2}$$
    $$\boxed{n_r = \frac{L_r^{2/3}}{L_r^{1/2}} = L_r^{1/6}}$$

---

## 5. Scale Effects & Physical Modeling Boundaries

### 5.1 The Impossibility of Dual Froude–Reynolds Similitude
To achieve simultaneous Froude and Reynolds similitude:
$$v_r = \sqrt{L_r} \quad (\text{Froude}) \quad \text{and} \quad v_r = \frac{\nu_r}{L_r} \quad (\text{Reynolds})$$
Equating both:
$$\sqrt{L_r} = \frac{\nu_r}{L_r} \implies \nu_r = L_r^{3/2}$$
For a 1:40 scale model ($L_r = 40$), the required model kinematic viscosity would be:
$$\nu_m = \frac{\nu_p}{40^{1.5}} = \frac{\nu_p}{253}$$
No non-hazardous fluid exists with a viscosity 250 times less viscous than water! Therefore, **water must be used in both model and prototype**, meaning Reynolds numbers in the model are inevitably much smaller than in the prototype:
$$Re_r = \frac{v_r L_r}{\nu_r} = \frac{(L_r^{1/2})(L_r)}{1} = L_r^{3/2} = 40^{1.5} \approx 253$$
The model Reynolds number is 250 times smaller than prototype!

### 5.2 Limiting Scale Effects in Engineering Practice
To ensure viscous and surface-tension distortions (scale effects) do not invalidate physical model measurements:
1. **Viscous Scale Effect (Boundary Layer Distortion)**:
   * Chute and stilling basin models must be constructed at sufficiently large scales ($L_r \le 50$) so that the model flow remains fully turbulent:
     $$Re_m = \frac{v_m R_m}{\nu} > 10^5$$
2. **Surface Tension / Weber Scale Effect**:
   * If water depth over an ogee crest or weir drops below $30\text{ mm}$, capillary surface tension forces curl the nappe, altering the discharge coefficient.
   * *Mandate*: Model head on crest must always exceed $H_m \ge 30\text{ mm}$ (preferably $\ge 50\text{ mm}$).
3. **Air Entrainment Scale Effect**:
   * Self-aeration on spillway chutes occurs when turbulent kinetic energy overcomes surface tension ($\sigma$). Models cannot correctly scale air entrainment because $We$ is not preserved. Air entrainment is therefore evaluated numerically or via semi-empirical prototype transfer functions.

---

## 6. Distorted versus Undistorted Hydraulic Models

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    UNDISTORTED vs. DISTORTED SCALE MODELS                   │
├─────────────────────┬───────────────────────────┬───────────────────────────┤
│ FEATURE             │ UNDISTORTED MODEL         │ DISTORTED MODEL           │
├─────────────────────┼───────────────────────────┼───────────────────────────┤
│ Geometric Ratio     │ $L_{xr} = L_{zr} = L_r$   │ $L_{xr} \ne L_{zr}$       │
│                     │ Vertical and horizontal   │ Horizontal scale $L_{xr}$ │
│                     │ scales are identical.     │ differs from vertical     │
│                     │                           │ scale $L_{zr}$.           │
├─────────────────────┼───────────────────────────┼───────────────────────────┤
│ Primary Application │ Hydraulic structures:     │ Wide river channels,      │
│                     │ Spillways, stilling       │ floodplains, estuaries,   │
│                     │ basins, intake towers     │ reservoirs, sedimentation │
├─────────────────────┼───────────────────────────┼───────────────────────────┤
│ Why Distort?        │ Preserves streamline      │ A wide, shallow river     │
│                     │ curvature and true local  │ would have tiny depth in  │
│                     │ velocity profiles.        │ undistorted model ($2$ mm)│
│                     │                           │ leading to laminar flow.  │
└─────────────────────┴───────────────────────────┴───────────────────────────┘
```

### 6.1 Scaling Laws for Distorted River Models
Let horizontal scale be $L_{xr} = X_r$ and vertical scale be $L_{zr} = Z_r$:
* **Distortion Ratio**: $D = \frac{X_r}{Z_r} > 1$ (typically $D = 2 \text{ to } 5$).
* **Slope Exaggeration**: $S_r = \frac{Z_r}{X_r}$.
* **Velocity Ratio**: $v_r = \sqrt{Z_r}$.
* **Discharge Ratio**: $Q_r = A_r v_r = (X_r Z_r)\sqrt{Z_r} = \boxed{X_r Z_r^{3/2}}$.
* **Manning Roughness Ratio**:
  $$n_r = \frac{Z_r^{2/3}}{X_r^{1/2}}$$
  In distorted river models, the model bed must usually be made artificially rougher (using wire mesh, gravel strips, or roughness studs) to satisfy this criterion!

---

## 7. Laboratory Instrumentation & Measurement Techniques

Modern physical hydraulic models utilize high-precision electronic instrumentation:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 INSTRUMENTATION IN HYDRAULIC SCALE MODELS                   │
├────────────────────────┬───────────────────────────┬────────────────────────┤
│ MEASURED PARAMETER     │ SENSOR / INSTRUMENT       │ ACCURACY & FREQUENCY   │
├────────────────────────┼───────────────────────────┼────────────────────────┤
│ **3D Flow Velocity**   │ Acoustic Doppler          │ $\pm 0.5\%$, sampling  │
│                        │ Velocimeter (ADV)         │ up to 50–100 Hz        │
├────────────────────────┼───────────────────────────┼────────────────────────┤
│ **Water Surface**      │ Ultrasonic Level Sensors; │ $\pm 0.1$ mm accuracy; │
│ **Elevations**         │ Capacitance Wave Probes   │ dynamic wave tracking  │
├────────────────────────┼───────────────────────────┼────────────────────────┤
│ **Turbulent Pressure** │ Piezo-resistive dynamic   │ High frequency (1 kHz) │
│ **Fluctuations**       │ pressure transducers      │ for cavitation/impact  │
├────────────────────────┼───────────────────────────┼────────────────────────┤
│ **Surface Flow Field** │ Particle Image            │ High-speed camera,     │
│                        │ Velocimetry (PIV)         │ planar velocity field  │
├────────────────────────┼───────────────────────────┼────────────────────────┤
│ **Discharge Control**  │ Electromagnetic Flowmeters│ $\pm 0.2\%$ on intake  │
│                        │ (Magmeters) & V-notch weirs│ supply pipelines       │
└────────────────────────┴───────────────────────────┴────────────────────────┘
```

---

## 8. Solved Engineering Problem: Spillway Scale-Model Study

**Statement**: A 1:40 scale undistorted physical model ($L_r = 40$) of an ogee spillway and USBR Type II stilling basin is tested in a hydraulic laboratory.
* The prototype design flood is $Q_p = 2,400\text{ m}^3\text{/s}$.
* Prototype spillway crest design head is $H_p = 8.0\text{ m}$.
* Prototype chute velocity at the stilling basin toe is $v_p = 32.0\text{ m/s}$.
* During the model test, the total hydrodynamic force measured on a single model chute block by a miniature load cell is $F_m = 0.420\text{ N}$.
* Time required for a dye tracer to clear the prototype plunge pool reach must be estimated if the model clearance time is $t_m = 18.5\text{ seconds}$.
1. Calculate the required model test discharge $Q_m$ in liters per second (L/s).
2. Calculate the corresponding water head $H_m$ over the model crest and verify that surface tension scale effects are avoided ($H_m \ge 50\text{ mm}$).
3. Calculate the model flow velocity $v_m$ entering the stilling basin.
4. Scale up the dynamic hydrodynamic impact force $F_p$ acting on the full-scale prototype chute block.
5. Determine the prototype plunge pool travel clearance time $t_p$.

**Solution**:
1. **Model Inflow Discharge ($Q_m$)**:
   The discharge scale ratio under Froude similitude is:
   $$Q_r = L_r^{5/2} = (40)^{2.5} = (40^2)\sqrt{40} = 1600 \times 6.32456 = \mathbf{10,119.29}$$
   $$Q_m = \frac{Q_p}{Q_r} = \frac{2,400\text{ m}^3\text{/s}}{10,119.29} = 0.23717\text{ m}^3\text{/s} = \mathbf{237.17\text{ L/s}}$$
   The laboratory pumping supply must deliver $237.2\text{ L/s}$.

2. **Model Crest Head ($H_m$) & Scale Effect Verification**:
   $$H_r = L_r = 40 \implies H_m = \frac{H_p}{L_r} = \frac{8.0\text{ m}}{40} = 0.200\text{ m} = \mathbf{200\text{ mm}}$$
   *Evaluation against Scale Effect Limit*:
   $$H_m = 200\text{ mm} \gg 50\text{ mm} \quad (\text{Safe})$$
   Surface tension and capillary scale effects are completely negligible.

3. **Model Chute Velocity ($v_m$)**:
   $$v_r = \sqrt{L_r} = \sqrt{40} = 6.3246$$
   $$v_m = \frac{v_p}{v_r} = \frac{32.0\text{ m/s}}{6.3246} = \mathbf{5.060\text{ m/s}}$$
   Check model Reynolds number with flow depth $y_m = y_p / 40 = 2.50\text{ m} / 40 = 0.0625\text{ m}$:
   $$Re_m = \frac{v_m y_m}{\nu} = \frac{5.060 \times 0.0625}{1.004 \times 10^{-6}} = \frac{0.31625}{1.004 \times 10^{-6}} = 3.15 \times 10^5 \gg 10^5 \quad (\text{Fully Turbulent})$$
   Viscous scale effects are avoided.

4. **Prototype Dynamic Hydrodynamic Force ($F_p$)**:
   The force scale ratio for water in both model and prototype is:
   $$F_r = L_r^3 = 40^3 = 64,000$$
   Prototype force on chute block:
   $$F_p = F_r \times F_m = 64,000 \times 0.420\text{ N} = 26,880\text{ N} = \mathbf{26.88\text{ kN}}$$
   Structural engineers will design the anchor reinforcement bars in the concrete chute block for a factored hydrodynamic drag of $\mathbf{26.9\text{ kN}}$.

5. **Prototype Tracer Travel Time ($t_p$)**:
   The time scale ratio is:
   $$T_r = \sqrt{L_r} = \sqrt{40} = 6.3246$$
   Prototype travel clearance time:
   $$t_p = T_r \times t_m = 6.3246 \times 18.5\text{ seconds} = 117.0\text{ seconds} = \mathbf{1.95\text{ minutes}}$$

