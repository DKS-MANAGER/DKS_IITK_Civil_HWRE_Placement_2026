# Module 10: HEC-RAS Preparation — 1D River Modeling & Hydraulic Analysis

> **Document Focus**: HEC-RAS Architecture, 1D Steady/Unsteady Algorithms, Geometric Data, Boundary Conditions, Bridge Hydraulics, Warning Diagnostics, and Step-by-Step Case Study  
> **Target Role**: Hydraulics Engineer (AFRY India)  
> **Evidentiary Status**: `[TIER 4 / STATUTORY & ENGINEERING CODES — USACE HEC-RAS HYDRAULIC REFERENCE MANUAL CPD-69, BARKER]`  

---

## 1. Overview of HEC-RAS & Consulting Relevance

**HEC-RAS** (Hydrologic Engineering Center's River Analysis System), developed by the U.S. Army Corps of Engineers (USACE), is the worldwide industry-standard software for 1D and 2D river hydrodynamic modeling, floodplain delineation, bridge/culvert hydraulics, and dam-break inundation studies.

In AFRY's water and hydropower consulting practice in Noida, HEC-RAS is utilized daily to:
1. Estimate 1D river water surface profiles (WSPs) under design flood discharges ($Q_{100}, Q_{1000}, Q_{PMF}$).
2. Establish downstream **Tailwater Rating Curves (TRCs)** to set turbine centerline elevations, tailrace tunnel outlet levels, and powerhouse flood protection walls.
3. Compute backwater profiles caused by dams, weirs, and bridge crossings.
4. Model unsteady dam-break hydrograph attenuation and emergency action plans (EAP).

---

## 2. HEC-RAS Architecture & File Management

A complete HEC-RAS project consists of four decoupled primary files linked by a master project file:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          HEC-RAS FILE STRUCTURE                             │
├─────────────────────┬──────────────┬────────────────────────────────────────┤
│ COMPONENT           │ FILE EXT.    │ STORED INFORMATION                     │
├─────────────────────┼──────────────┼────────────────────────────────────────┤
│ **Project File**    │ `.prj`       │ Master manager linking geometry, plans,│
│                     │              │ flow files, and output settings.       │
├─────────────────────┼──────────────┼────────────────────────────────────────┤
│ **Plan File**       │ `.p01, .p02` │ Associates a specific geometry file    │
│                     │              │ with a specific flow file; sets run.   │
├─────────────────────┼──────────────┼────────────────────────────────────────┤
│ **Geometry File**   │ `.g01, .g02` │ Cross-sections, reach lengths, Manning │
│                     │              │ n values, bridges, culverts, weirs.    │
├─────────────────────┼──────────────┼────────────────────────────────────────┤
│ **Steady Flow**     │ `.f01, .f02` │ Profile discharges ($Q_i$) and boundary│
│                     │              │ conditions (Normal depth, rating curve)│
├─────────────────────┼──────────────┼────────────────────────────────────────┤
│ **Unsteady Flow**   │ `.u01, .u02` │ Time series hydrographs ($Q(t), h(t)$),│
│                     │              │ stage hydrographs, initial conditions. │
├─────────────────────┼──────────────┼────────────────────────────────────────┤
│ **Output Files**    │ `.r01, .O01` │ Computed water levels, velocities, HDF5│
│                     │              │ spatial results for RAS Mapper.        │
└─────────────────────┴──────────────┴────────────────────────────────────────┘
```

---

## 3. Geometric Data Input & Cross-Section Formulation

A river reach in HEC-RAS is discretized into a sequence of cross-sections oriented **perpendicular to the flow streamlines**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      HEC-RAS CROSS-SECTION CONVENTIONS                      │
│                                                                             │
│          Left Overbank (LOB)       Main Channel       Right Overbank (ROB)  │
│          Roughness: n_LOB          Roughness: n_CH    Roughness: n_ROB      │
│          ──────────────────┐       │~~~~~~~~~~~~~│    ┌──────────────────   │
│                            │       │Water Surface│    │                     │
│                            │ Left  │             │Right                     │
│                            │ Bank  \             / Bank                     │
│                            └───────┐\___________/┌────┘                     │
│          Station: 0.0              Station: 45.0  Station: 85.0             │
│          ◄──────────────── Reach Length: L_LOB ────────────────────────►    │
│          ◄──────────────── Reach Length: L_CH ─────────────────────────►    │
│          ◄──────────────── Reach Length: L_ROB ────────────────────────►    │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.1 Five Mandatory Elements per Cross-Section
1. **Station–Elevation Points ($X_i, Z_i$)**: A coordinate table describing the ground surface from extreme left to extreme right looking downstream.
2. **Main Channel Bank Stations**: Two station numbers dividing the cross-section into three distinct flow zones:
   * Left Overbank (LOB) / Floodplain.
   * Main Channel (carrying primary bedload and dry-season discharge).
   * Right Overbank (ROB) / Floodplain.
3. **Downstream Reach Lengths ($\Delta x$)**: The physical distances between the current cross-section and the next downstream section:
   * Main channel distance ($L_{CH}$).
   * Left overbank distance ($L_{LOB}$) — along the overbank flow path.
   * Right overbank distance ($L_{ROB}$) — along the overbank flow path.
   *(In curving river bends, overbank reach lengths differ significantly from main channel length!)*
4. **Manning Roughness Coefficients ($n$)**: Assigned separately across LOB, Main Channel, and ROB (e.g., $n_{LOB} = 0.055, n_{CH} = 0.035, n_{ROB} = 0.060$).
5. **Contraction and Expansion Coefficients ($C_{\text{cont}}, C_{\text{exp}}$)**:
   * Gradual natural river reaches: $C_{\text{cont}} = 0.10, C_{\text{exp}} = 0.30$.
   * Bridge approach transitions: $C_{\text{cont}} = 0.30, C_{\text{exp}} = 0.50$.
   * Abrupt changes (e.g., flumes, abutments): $C_{\text{cont}} = 0.60, C_{\text{exp}} = 0.80$.

### 3.2 Ineffective Flow Areas
Areas of the floodplain that store water but do not convey downstream discharge (e.g., dead zones upstream and downstream of bridge approach embankments) are designated as **Ineffective Flow Areas**:
* Ineffective flow is defined by a station and a trigger elevation.
* Below the trigger elevation, water is ponded; area is included in storage calculations, but conveyance ($K = 0$) and velocity ($v = 0$).
* When water rises above the trigger elevation, the area becomes active conveyance.

---

## 4. The 1D Standard Step Solution Engine

HEC-RAS solves 1D steady gradually varied flow via the **Standard-Step Energy Method**:
$$z_2 + y_2 + \alpha_2 \frac{v_2^2}{2g} = z_1 + y_1 + \alpha_1 \frac{v_1^2}{2g} + h_e$$
where head loss $h_e$ is:
$$h_e = \bar{S}_f L_{CH} + C \left| \alpha_2 \frac{v_2^2}{2g} - \alpha_1 \frac{v_1^2}{2g} \right|$$

### 4.1 Subdivided Conveyance & Kinetic Energy Correction ($\alpha$)
Because velocity in the deep main channel is much higher than in the shallow, heavily vegetated overbanks, evaluating total cross-section conveyance using a single hydraulic radius introduces massive errors. HEC-RAS subdivides the cross-section into subdivisions ($j = LOB, CH, ROB$):
$$K_j = \frac{1}{n_j} A_j R_j^{2/3}, \quad K_{\text{total}} = \sum K_j$$
Friction slope is calculated using total conveyance:
$$S_f = \left(\frac{Q}{K_{\text{total}}}\right)^2$$
The velocity head weighting coefficient $\alpha$ (Coriolis coefficient) is computed dynamically:
$$\alpha = \frac{\sum (v_j^2 A_j)}{\bar{v}^2 A_{\text{total}}} = \frac{\left(\sum \frac{K_j^3}{A_j^2}\right)}{\frac{K_{\text{total}}^3}{A_{\text{total}}^2}}$$
In wide natural floodplains, $\alpha$ typically ranges between **$1.15 \text{ and } 1.50$**!

---

## 5. Boundary Conditions in HEC-RAS

Selecting appropriate boundary conditions is critical to prevent non-convergence:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    HEC-RAS BOUNDARY CONDITION RULES                         │
├─────────────────────┬───────────────────────────────────────────────────────┤
│ FLOW REGIME         │ MANDATORY BOUNDARY CONDITION REQUIREMENTS             │
├─────────────────────┼───────────────────────────────────────────────────────┤
│ **Subcritical**     │ DOWNSTREAM Boundary Condition ONLY.                   │
│ ($Fr < 1$)          │ Disturbances travel upstream; computations proceed    │
│                     │ in the UPSTREAM direction.                            │
├─────────────────────┼───────────────────────────────────────────────────────┤
│ **Supercritical**   │ UPSTREAM Boundary Condition ONLY.                     │
│ ($Fr > 1$)          │ Disturbances swept downstream; computations proceed   │
│                     │ in the DOWNSTREAM direction.                          │
├─────────────────────┼───────────────────────────────────────────────────────┤
│ **Mixed Flow**      │ BOTH Upstream AND Downstream Boundary Conditions.     │
│ ($Fr < 1$ & $Fr > 1$)│ Engine runs subcritical upstream pass and supercritical│
│                     │ downstream pass; locates hydraulic jumps where        │
│                     │ momentum force $M_1 = M_2$.                           │
└─────────────────────┴───────────────────────────────────────────────────────┘
```

### 5.1 The Four Downstream Boundary Options
1. **Normal Depth ($S_0$)**: The user specifies the energy slope (typically approximating the channel bed slope $S_0$). HEC-RAS computes uniform depth via Manning's equation. *(Most common in consulting when downstream data is sparse)*.
2. **Known Water Surface Elevation**: User inputs a fixed measured stage (e.g., lake or reservoir pool level).
3. **Rating Curve**: User inputs a stage-discharge table ($h$ vs. $Q$) derived from a downstream gauging station.
4. **Critical Depth**: Program defaults to critical depth ($Fr = 1$). Used at waterfalls, free overfalls, or steep drop structures.

---

## 6. Bridge & Culvert Hydraulic Modeling Algorithms

Bridge structures constrict flow, creating backwater upstream. HEC-RAS models bridges using a four-cross-section system:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    FOUR CROSS-SECTION BRIDGE SYSTEM                         │
│                                                                             │
│       Section 4 (Upstream River Reach: Flow fully expanded)                 │
│       ═══════════════════════════════════════════════════════════════════   │
│                 ◄──────── Expansion Reach L_e ────────►                     │
│       Section 3 (Upstream Approach Section: Contraction begins)             │
│       ═══════════════════════════════════════════════════════════════════   │
│                 ◄──────── Short Distance (1–2 × Pier Width) ──►             │
│       Section 2 (Bridge Deck & Piers: Inside Constriction)                  │
│       ══════════[=== Pier ===]══════[=== Pier ===]═══════════════════════   │
│                 ◄──────── Short Distance ─────────────────────►             │
│       Section 1 (Downstream Exit Section)                                   │
│       ═══════════════════════════════════════════════════════════════════   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 6.1 Low Flow versus High Flow Methods
* **Low Flow (Water surface below low chord of deck)**:
  1. *Energy Method (Standard Step)*: Friction loss through opening plus pier drag using contracted cross-section.
  2. *Momentum Method*: Balances pressure forces, pier drag force, and momentum flux. Recommended when piers are skewed to flow.
  3. *Yarnell Equation*: Empirical pier loss formula:
     $$H_L = 2 K_p (K_p + 5) (Fr^2 + 0.6) \alpha \frac{v_2^2}{2g}$$
* **High Flow (Water surface touches or submerges deck)**:
  1. *Energy Method*: Treats entire bridge as a regular section with reduced conveyance and friction.
  2. *Pressure and Weir Flow*:
     * Sluice/Orifice pressure flow beneath the deck: $Q = C_d A \sqrt{2 g H}$.
     * Broad-crested weir flow overtopping the roadway: $Q = C b H^{3/2}$.

---

## 7. Troubleshooting Common HEC-RAS Errors & Warnings

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    HEC-RAS COMMON WARNINGS & ROOT CAUSES                    │
├────────────────────────────────────────┬────────────────────────────────────┤
│ WARNING MESSAGE IN LOG                 │ CAUSE & CORRECTIVE ACTION          │
├────────────────────────────────────────┼────────────────────────────────────┤
│ "The energy equation could not be      │ Cross-sections are spaced too far  │
│ balanced within specified iterations.  │ apart ($\Delta x$ too large).      │
│ Program defaulted to critical depth."  │ **Action**: Interpolate intermed-  │
│                                        │ iate cross-sections ($\Delta x/2$).│
├────────────────────────────────────────┼────────────────────────────────────┤
│ "Froude number exceeds 1.0 during      │ Flow choked; a hydraulic jump is   │
│ subcritical pass."                     │ imminent.                          │
│                                        │ **Action**: Switch simulation from │
│                                        │ Subcritical to Mixed Flow mode.    │
├────────────────────────────────────────┼────────────────────────────────────┤
│ "The energy loss between current and   │ Energy slope is too steep or reach │
│ previous section is too large."        │ length is excessive.               │
│                                        │ **Action**: Insert interpolated XS.│
├────────────────────────────────────────┼────────────────────────────────────┤
│ "Divided flow occurred."               │ Flow is split across islands or    │
│                                        │ overbank levees into two troughs.  │
│                                        │ **Action**: Check levee settings.  │
└────────────────────────────────────────┴────────────────────────────────────┘
```

---

## 8. Step-by-Step Practical River Modeling Case Study

**Objective**: Model a $1.2\text{ km}$ mountain river reach carrying a design discharge of $Q = 450\text{ m}^3\text{/s}$ to establish the tailwater rating curve and check bridge clearance.

### Step 1: Create Project & Geometry
1. Launch HEC-RAS $\rightarrow$ `File` $\rightarrow$ `New Project` $\rightarrow$ Enter title `Beas_River_Study.prj`. Set units to **System International (SI)**.
2. Open Geometric Data Editor $\rightarrow$ Draw River Reach from Upstream to Downstream $\rightarrow$ River name: `Beas`, Reach name: `Reach_1`.

### Step 2: Enter Cross-Section Geometry
Create 4 cross-sections ($RS = 1200, 800, 400, 0$):
* **Cross-Section RS 400 (Bridge Approach Section)**:
  * Station-Elevation coordinates:
    $$(0, 108.0), (20, 104.0), (40, 100.0), (55, 96.0), (70, 96.0), (85, 100.0), (105, 105.0), (130, 109.0)$$
  * Bank Stations: Left Bank $= 40.0\text{ m}$, Right Bank $= 85.0\text{ m}$.
  * Reach lengths to downstream ($RS = 0$): $L_{LOB} = 410\text{ m}, L_{CH} = 400\text{ m}, L_{ROB} = 415\text{ m}$.
  * Manning's $n$: $n_{LOB} = 0.055, n_{CH} = 0.038, n_{ROB} = 0.050$.
  * Contraction/Expansion: $C_{\text{cont}} = 0.10, C_{\text{exp}} = 0.30$.

### Step 3: Enter Steady Flow & Boundary Conditions
1. Open Steady Flow Data Editor $\rightarrow$ Enter 3 Profiles:
   * Profile 1 ($Q_{10} = 200\text{ m}^3\text{/s}$)
   * Profile 2 ($Q_{50} = 350\text{ m}^3\text{/s}$)
   * Profile 3 ($Q_{100} = 450\text{ m}^3\text{/s}$)
2. Click `Reach Boundary Conditions` $\rightarrow$ Select Downstream Reach $\rightarrow$ Set **Normal Depth** with energy slope $S_0 = 0.0018$.

### Step 4: Run Simulation & Extract Water Surface Profile
1. Open Steady Flow Analysis $\rightarrow$ Select **Subcritical Flow** $\rightarrow$ Click `COMPUTE`.
2. Open Cross-Section Profile Plot and Table.
3. *Simulated Results at RS 400*:
   * For $Q = 450\text{ m}^3\text{/s}$: Computed Water Surface Elevation $= 102.48\text{ m}$.
   * Maximum channel velocity: $v_{CH} = 2.84\text{ m/s}$.
   * Velocity head: $\alpha v^2 / 2g = 0.49\text{ m}$.
   * Total Energy Elevation: $EGL = 102.97\text{ m}$.
   * Froude number: $Fr = 0.42 < 1.0$ (Tranquil subcritical flow confirmed).
4. *Tailwater Rating Curve Export*:
   * $Q = 200\text{ m}^3\text{/s} \implies WSE = 100.82\text{ m}$
   * $Q = 350\text{ m}^3\text{/s} \implies WSE = 101.95\text{ m}$
   * $Q = 450\text{ m}^3\text{/s} \implies WSE = 102.48\text{ m}$
   This rating table is directly transferred to Module 11 (Bentley HAMMER) to define boundary tailrace reservoir elevations!

