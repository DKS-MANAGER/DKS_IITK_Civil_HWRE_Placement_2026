# Practical Engineering Scenarios: 10 Consulting Case Studies
**Target Role:** Early Career Professionals (ECP) — Infrastructure / Water Resources Engineering  
**Company:** AECOM India (Bengaluru & Gurugram)  
**Standard:** Real-World Engineering Consultancy Project Delivery  

---

## Overview

In technical interviews and assessment center group exercises at AECOM, candidates are frequently presented with open-ended engineering scenarios. These scenarios test:
1. **First-Principles Application:** Applying hydraulics, hydrology, geotechnics, and structural mechanics to solve unconstrained site challenges.
2. **Regulatory & Design Code Compliance:** Applying IRC, IS, CIRIA, Eurocodes, or AASHTO standards appropriately.
3. **Multi-Disciplinary Synthesis:** Balancing hydraulic conveyance against geotechnical stability, cost, constructability, and environmental sustainability.
4. **Client Communication:** Delivering defensible, value-engineered recommendations.

This module provides **10 comprehensive real-world engineering scenarios**.

---

### Scenario 1: Highway Cross-Drainage Box Culvert Hydraulic Sizing (IRC:SP:13)

#### 1. Client Context & Background
AECOM has been awarded the detailed design consultancy for a 45 km, 6-lane access-controlled greenfield expressway package in Haryana. At Chainage km 28+450, the expressway alignment intersects a natural ephemeral seasonal drainage swale draining an upstream agricultural watershed of area $A = 4.2\text{ km}^2$.

#### 2. Problem Statement
Size an appropriate reinforced concrete box culvert (RCC) crossing that safely passes the 50-year return period design flood while satisfying the following constraints:
- Maximum permissible afflux (headwater rise above normal high flood level, HFL) = $0.30\text{ m}$ to prevent flooding of adjacent fertile farmland.
- Embankment finished road level (FRL) = $218.50\text{ m}$.
- Natural stream bed invert elevation = $212.00\text{ m}$.
- Natural 50-year HFL = $214.20\text{ m}$ (normal flow depth $y_n = 2.20\text{ m}$).
- Minimum required pavement crust + subgrade thickness above culvert top slab soffit = $1.20\text{ m}$.

#### 3. Engineering Methodology & Calculations
1. **Hydrological Peak Runoff Estimation:**
   - Time of concentration ($t_c$) using Kirpich's formula:
     $$t_c = 0.01947 \cdot L^{0.77} S^{-0.385}$$
     For $L = 3200\text{ m}$, $S = 0.0035 \implies t_c \approx 42\text{ minutes}$.
   - From regional Haryana IDF curves, 50-year intensity $I_{50} = 65\text{ mm/hr}$.
   - Composite runoff coefficient $C = 0.45$ (cultivated alluvial plain).
   - Peak discharge using Rational Method:
     $$Q = \frac{C \cdot I \cdot A}{3.6} = \frac{0.45 \times 65 \times 4.2}{3.6} = 34.125\text{ m}^3\text{/s}$$
   - Adding $10\%$ climate resilience factor under AECOM Sustainable Legacies: $Q_{\text{design}} \approx 37.5\text{ m}^3\text{/s}$.
2. **Vertical Geometric Envelope Clearance:**
   - Road FRL = $218.50\text{ m}$.
   - Minimum pavement cushion + slab thickness = $1.20 + 0.40\text{ m} = 1.60\text{ m}$.
   - Maximum allowable culvert top soffit elevation = $218.50 - 1.60 = 216.90\text{ m}$.
   - Maximum available internal clear height:
     $$H_{\text{clear}} \le 216.90 - 212.00 = 4.90\text{ m}$$
   - To match natural bank depth ($2.20\text{ m}$) and maintain self-cleansing velocity, adopt an internal clear height $H = 2.50\text{ m}$.
3. **Hydraulic Sizing under IRC:SP:13:**
   - Try a twin-cell box culvert: $2 \text{ cells} \times B\text{ m wide} \times 2.5\text{ m high}$.
   - Adopting $B = 3.5\text{ m}$ per cell: Total waterway clear width $= 2 \times 3.5 = 7.0\text{ m}$.
   - Total cross-sectional area $A = 7.0 \times 2.5 = 17.5\text{ m}^2$.
   - Flow velocity through barrel:
     $$V_{\text{barrel}} = \frac{Q}{A} = \frac{37.5}{17.5} \approx 2.14\text{ m/s}$$
     (Permissible velocity range under IRC:SP:13 is $1.5\text{ m/s}$ to $3.0\text{ m/s}$ to prevent sedimentation and scour).
4. **Inlet/Outlet Control Check:**
   - Headwater depth $HW$ calculated using orifice flow formula:
     $$Q = C_d \cdot A \cdot \sqrt{2g \Delta H}$$
   - With flared wingwalls ($C_d = 0.85$):
     $$\Delta H = \frac{Q^2}{2g (C_d A)^2} = \frac{37.5^2}{19.62 \times (0.85 \times 17.5)^2} = \frac{1406.25}{19.62 \times 221.27} = \frac{1406.25}{4341.3} \approx 0.32\text{ m}$$
   - Since $\Delta H = 0.32\text{ m} > 0.30\text{ m}$ (slight excess afflux), expand to a **triple-cell box culvert ($3 \times 3.0\text{ m} \times 2.5\text{ m}$)**:
     - Clear waterway $= 9.0\text{ m}$, Area $= 22.5\text{ m}^2$, $V = 1.67\text{ m/s}$.
     - Afflux $\Delta H = 0.18\text{ m} < 0.30\text{ m}$ (Safe).

#### 4. Consultancy Deliverables
- Structural general arrangement drawing (GAD) for a 3-cell $3.0\text{ m} \times 2.5\text{ m}$ box culvert.
- Stone pitching and flexible apron upstream ($3.0\text{ m}$) and downstream ($6.0\text{ m}$) to prevent exit jet scouring.
- Flared wingwalls at $45^\circ$ to minimize entrance energy losses.

---

### Scenario 2: Bridge Pier Scour Protection & Riprap Sizing (IRC:78 / HEC-18)

#### 1. Client Context & Background
During a bridge health monitoring audit for the National Highways Authority of India (NHAI), an AECOM structural-hydraulic inspection team discovers severe bed degradation around the central circular piers of a major bridge across an alluvial river in Uttar Pradesh.

#### 2. Problem Statement
Design an engineered rock riprap protection blanket around an existing circular bridge pier of diameter $D = 2.4\text{ m}$ subjected to an extreme design flood velocity $V_{\text{approach}} = 3.6\text{ m/s}$ and approach flow depth $y_0 = 5.8\text{ m}$.

#### 3. Engineering Calculations & Code Compliance
1. **Local Scour Depth Estimation (IRC:78 & Lacey's Theory):**
   - Pier scour depth under Lacey's formula:
     $$d_s = 2.0 R - y_0$$
     Where $R = 0.473(Q/f)^{1/3}$.
   - For an alluvial sand bed with $d_{50} = 0.35\text{ mm}$, silt factor $f = 1.76\sqrt{d_{50}} = 1.76\sqrt{0.35} \approx 1.04$.
   - Lacey scour depth below HFL reaches $d_{\text{total}} \approx 14.2\text{ m}$, indicating that unreinforced natural bed sediment will be completely undermined during design floods.
2. **Riprap Stone Sizing using Isbash Formula (FHWA HEC-18 & IRC:78):**
   - The critical stone size to resist dislodgement by horseshoe vortices:
     $$d_{50,\text{riprap}} = \frac{0.692 (K_v V)^2}{2g (S_s - 1)}$$
   - Where:
     - $V = 3.6\text{ m/s}$ (approach velocity).
     - $K_v = 1.5$ (velocity multiplier for flow acceleration and vortex intensification around circular piers).
     - Local velocity at pier nose: $V_{\text{local}} = 1.5 \times 3.6 = 5.4\text{ m/s}$.
     - Specific gravity of rock riprap $S_s = 2.65$.
   - Compute required median rock diameter:
     $$d_{50} = \frac{0.692 \times (5.4)^2}{2 \times 9.81 \times (2.65 - 1)} = \frac{0.692 \times 29.16}{19.62 \times 1.65} = \frac{20.178}{32.373} \approx 0.623\text{ m} \approx 625\text{ mm}$$
3. **Riprap Layer Geometry & Layout:**
   - Riprap layer thickness:
     $$T_{\text{layer}} = \max(2.0 \cdot d_{50}, d_{100}) = 2.0 \times 0.625 = 1.25\text{ m}$$
   - Lateral extent of riprap apron:
     - Distance from pier face $= 2.0 D = 2.0 \times 2.4 = 4.8\text{ m}$ in all directions.
     - Total apron diameter $= D + 2(2D) = 5D = 12.0\text{ m}$.
4. **Geotextile Filter Layer Design:**
   - Direct placement of rock boulders on fine sand ($d_{50} = 0.35\text{ mm}$) will result in "winnowing" (sub-base sand sucking through boulder voids under fluctuating suction pressures).
   - Specify a non-woven needle-punched polypropylene geotextile filter fabric underneath the riprap, weighed down with an intermediate $150\text{ mm}$ gravel bedding layer ($d_{50,\text{gravel}} = 20\text{ mm}$) to prevent fabric puncture.

---

### Scenario 3: Urban Stormwater Attenuation Basin & SuDS Retrofit

#### 1. Client Context & Background
A multi-national tech campus in Whitefield, Bengaluru, is expanding its built-up footprint by $40,000\text{ m}^2$, converting open grass fields into asphalt parking lots and multi-story office blocks. The local municipal corporation (BBMP) mandates a "zero-runoff-increase" policy: the peak 10-year post-development discharge into the municipal drain must not exceed pre-development peak flow.

#### 2. Hydraulic Design & Calculations
1. **Pre-development Peak Discharge:**
   - Area $A = 4.0\text{ hectares}$.
   - Pre-development runoff coefficient $C_{\text{pre}} = 0.20$ (permeable soil/grassland).
   - Time of concentration $t_{c,\text{pre}} = 25\text{ minutes} \implies I_{10} = 60\text{ mm/hr}$.
   - Pre-development peak:
     $$Q_{\text{pre}} = \frac{0.20 \times 60 \times 4.0}{360} = 0.133\text{ m}^3\text{/s} = 133\text{ L/s}$$
2. **Post-development Peak Discharge (Unmitigated):**
   - Post-development runoff coefficient $C_{\text{post}} = 0.85$ (roofs, roads, paved plaza).
   - Post-development $t_{c,\text{post}} = 10\text{ minutes} \implies I_{10} = 110\text{ mm/hr}$.
   - Post-development unmitigated peak:
     $$Q_{\text{post}} = \frac{0.85 \times 110 \times 4.0}{360} = 1.039\text{ m}^3\text{/s} = 1,039\text{ L/s}$$
   - Discharge increase factor: $\approx 7.8\times$ pre-development runoff.
3. **Required Attenuation Storage Volume:**
   - The detention basin must store the differential hydrograph volume during the critical design storm duration.
   - Using the modified Rational / hydrograph routing trapezoidal approximation for a 2-hour storm ($P = 85\text{ mm}$):
     - Total post-development inflow volume:
       $$V_{\text{in}} = 10 \times C_{\text{post}} \times P \times A = 10 \times 0.85 \times 85 \times 4.0 = 2,890\text{ m}^3$$
     - Allowable outflow volume over 2 hours at constant $Q_{\text{pre}} = 0.133\text{ m}^3\text{/s}$:
       $$V_{\text{out}} = 0.133 \times 7200 = 958\text{ m}^3$$
     - Required active storage volume:
       $$V_{\text{storage}} = V_{\text{in}} - V_{\text{out}} = 2890 - 958 = 1,932\text{ m}^3$$
     - Add $15\%$ freeboard and sediment accumulation margin:
       $$V_{\text{design}} \approx 2,220\text{ m}^3$$
4. **Basin Geometry & Orifice Control:**
   - Basin footprint: $40\text{ m} \times 30\text{ m} = 1,200\text{ m}^2$ at bed level.
   - Maximum active water depth $h = 1.60\text{ m}$, freeboard $= 0.40\text{ m}$ (total depth $= 2.0\text{ m}$).
   - Flow throttle: circular orifice plate installed at the outlet headwall:
     $$Q_{\text{allowable}} = C_d A_o \sqrt{2gh} \implies A_o = \frac{0.133}{0.60 \times \sqrt{2 \times 9.81 \times 1.60}} = \frac{0.133}{0.60 \times 5.60} = \frac{0.133}{3.36} \approx 0.0396\text{ m}^2$$
     - Orifice diameter $d_o = \sqrt{\frac{4 \times 0.0396}{\pi}} = 0.224\text{ m} \approx 225\text{ mm}$.
   - High-level overflow weir: Broad-crested weir set at $1.60\text{ m}$ stage to safely bypass 100-year storms without overtopping basin bunds.

---

### Scenario 4: Water Transmission Pumping Station Surge Analysis & Air Vessel Sizing

#### 1. Context & Hydraulic Network
A raw water transmission main delivers $Q = 1.2\text{ m}^3\text{/s}$ ($4,320\text{ m}^3\text{/hr}$) from an intake river reservoir to a regional treatment facility located $8.5\text{ km}$ away.
- Pipe material: Mild Steel (MS) with internal cement mortar lining, internal diameter $D = 1000\text{ mm}$, wall thickness $t = 12\text{ mm}$.
- Static pumping head $H_s = 45\text{ m}$.
- Total friction head loss at steady state $h_f = 22\text{ m}$.
- Rated pump operating head $H_o = 67\text{ m}$.

#### 2. Hydraulic Transient (Water Hammer) Problem
In the event of an abrupt total power trip at the pump house, pump check valves slam shut within $0.5\text{ seconds}$ to prevent reverse rotation. An acoustic negative decompression wave races downstream at wave speed $a \approx 1020\text{ m/s}$. The minimum transient pressure drops below negative atmospheric pressure, risking column separation and subsequent violent cavitation rejoining shockwaves ($> 25\text{ bar}$), which would rupture the transmission main.

#### 3. Surge Suppression Solution (Compressed Air Vessel)
1. **Initial Flow Parameters:**
   - Flow velocity:
     $$V_0 = \frac{1.2}{\frac{\pi}{4}(1.0)^2} = 1.528\text{ m/s}$$
   - Pipeline acoustic reflection time:
     $$T_r = \frac{2L}{a} = \frac{2 \times 8500}{1020} = 16.67\text{ seconds}$$
2. **Air Vessel Sizing Principle (Graze & Horlacher / Parmakian Formulation):**
   - Upon pump power trip, the compressed air in the vessel expands polytropically ($P V^{1.2} = \text{constant}$), expelling water into the pipeline to prevent downsurge below atmospheric pressure:
     $$C_{\text{vessel}} = \frac{2 L A V_0}{a \Delta H_{\text{permissible}}}$$
   - Design criteria:
     - Minimum transient pressure along profile $\ge +2.0\text{ m}$ head (no sub-atmospheric pressure anywhere).
     - Maximum upsurge head $\le 1.33 \times \text{pipe rating} = 1.33 \times 100\text{ m} = 133\text{ m}$.
3. **Air Vessel Specifications:**
   - Total required vessel volume: $V_{\text{vessel}} \approx 28\text{ m}^3$.
   - Steady-state operating air-to-water ratio: $55\%$ compressed air ($15.4\text{ m}^3$) and $45\%$ water ($12.6\text{ m}^3$).
   - Asymmetric throttling orifice installed at vessel throat:
     - Outflow (during downsurge): Low headloss orifice coefficient ($C_{d,\text{out}} = 0.95$) for immediate water injection.
     - Inflow (during return upsurge): Constricted orifice ($C_{d,\text{in}} = 0.25$) to dissipate kinetic energy and damp the oscillation.

---

### Scenario 5: Dam Ogee Spillway Cavitation Risk Assessment & Aeration Ramp Design

#### 1. Context & Failure Mechanism
A $65\text{ m}$ high concrete gravity dam on a Himalayan river has an uncontrolled ogee spillway discharging a maximum unit discharge $q = 45\text{ m}^2\text{/s}$. Flow velocities down the spillway chute reach $V = 32\text{ m/s}$.
- When flow velocity exceeds $V \approx 25 - 30\text{ m/s}$, the Cavitation Index $\sigma$ falls below the critical threshold:
  $$\sigma = \frac{P_{\text{amb}} - P_v + \gamma y \cos \theta}{\frac{1}{2}\rho V^2} < \sigma_{\text{critical}} \approx 0.20$$
  Under these conditions, surface micro-irregularities (offset joints, concrete spalling $> 2\text{ mm}$) trigger cavitation bubble formation. The implosion of these bubbles produces micro-jets exceeding $1000\text{ MPa}$, eroding deep pits into the concrete chute and risking spillway failure.

#### 2. Hydraulic Design of Forced Aeration Ramps
1. **Cavitation Mitigation via Air Entrainment:**
   - Research demonstrates that an air concentration of just $c_{\text{air}} \ge 6 - 8\%$ adjacent to the invert bed acts as a compressible cushion, reducing cavitation impact shock pressures by up to $99\%$.
2. **Aerator Geometry (Deflector Ramp + Offset + Air Supply Duct):**
   - Ramp angle $\alpha = 8.5^\circ$, ramp height $t_r = 0.25\text{ m}$.
   - Downstream step offset $s_o = 0.50\text{ m}$.
   - Chute slope $\theta = 45^\circ$.
3. **Trajectory Jet Length Calculation:**
   - The ramp projects the high-velocity water sheet away from the concrete surface, creating a sub-atmospheric air cavity beneath the nappe:
     $$L_{\text{jet}} = \frac{V_0^2}{g} \cdot \frac{\sin 2(\alpha + \theta) + \dots}{1 + \dots} \approx 6.8\text{ m}$$
4. **Air Supply Ducts:**
   - Aeration ducts embedded in the spillway training walls must supply air to the under-nappe cavity at a rate of:
     $$Q_{\text{air}} = \beta \cdot Q_{\text{water}}$$
     where entrainment ratio $\beta \approx 0.08 - 0.12$.
   - Ducts sized for maximum air flow velocity $\le 40\text{ m/s}$ to minimize throttling losses and prevent cavity vacuum lock.

---

### Scenario 6: Water Distribution Network Pressure Deficit & DMA Leakage Remediation

#### 1. Problem Context
AECOM is tasked with optimizing a District Metered Area (DMA) serving 35,000 residents in an old urban sector.
- Total daily water supply into DMA = $5.2\text{ MLD}$ ($60.2\text{ L/s}$).
- Legitimate billed residential consumption = $3.1\text{ MLD}$ ($35.9\text{ L/s}$).
- Non-Revenue Water (NRW) / physical leakage = $2.1\text{ MLD}$ ($40.4\%$ of total supply).
- During peak morning hours (07:00–09:00), end-of-line multi-story residential blocks suffer complete pressure drop ($H < 4\text{ m}$, below mandated $12\text{ m}$).
- During night hours (01:00–04:00), low demand causes static pressures to surge to $48\text{ m}$, bursting old cast-iron joints and driving massive background leakage.

#### 2. Hydraulic Modeling & Engineering Solution
1. **Model Calibration in WaterGEMS / EPANET:**
   - Perform C-factor roughness testing on aging pipelines (aged cast-iron $C = 80$, modern DI $C = 130$).
   - Execute Minimum Night Flow (MNF) analysis at 03:00 AM. Legitimate night consumption $\approx 1.5\text{ L/conn/hr}$. Measured MNF is $32\text{ L/s}$, confirming large background pipe bursts.
2. **Pressure Management via Modulating Pressure Reducing Valves (PRVs):**
   - Install an automated flow-modulated PRV at the DMA inlet node.
   - Fixed-outlet PRV vs Time-Modulated PRV:
     - Set daylight operating pressure = $22\text{ m}$ (sufficient to maintain $12\text{ m}$ at the highest consumer tap).
     - Modulate night pressure down to $14\text{ m}$.
   - Hydraulic leakage reduction relation:
     $$\text{Leakage Rate } q_L \propto P^{N_1} \quad (N_1 \approx 1.15 \text{ for elastic pipe cracks})$$
     - Reducing average DMA pressure from $38\text{ m}$ to $20\text{ m}$ reduces physical leakage volume by:
       $$\text{Reduction} = 1 - \left(\frac{20}{38}\right)^{1.15} = 1 - (0.526)^{1.15} = 1 - 0.477 = 52.3\%$$
     - Daily water saved $= 2.1\text{ MLD} \times 0.523 \approx 1.10\text{ MLD}$.
3. **Pumping & Pipeline Debottlenecking:**
   - Upsize the $600\text{ m}$ bottleneck trunk feeder from $150\text{ mm}$ AC to $250\text{ mm}$ DI Class K9, eliminating $18\text{ m}$ of dynamic friction loss and restoring minimum peak morning pressures to $15.5\text{ m}$.

---

### Scenario 7: River Training Works & Guide Bund Layout for Alluvial Bridges

#### 1. Context & River Mechanics
A new $1.8\text{ km}$ four-lane bridge is to be constructed across an active, meandering, braided alluvial river in Bihar (Ganga basin).
- High Flood Level (HFL) design discharge $Q_{100} = 22,000\text{ m}^3\text{/s}$.
- Natural unconstrained khadir (floodplain) width between high banks $= 4.5\text{ km}$.
- If the bridge is spanned across the entire $4.5\text{ km}$ floodplain, project capital expenditure exceeds budget by ₹650 Crores, and multiple parallel channels will wander unpredictably beneath the bridge, producing acute oblique attack angles against bridge piers.

#### 2. Hydraulic Training Works Design under IRC:89 & IRC:5
1. **Waterway Constriction & Lacey's Regime Width:**
   - Constrict the active river channel to its stable regime width:
     $$W = 4.83 \cdot \sqrt{Q} = 4.83 \times \sqrt{22,000} = 4.83 \times 148.32 \approx 716\text{ meters}$$
   - Allowing for pier obstruction and a safety factor of $1.15$, provide a clear bridge waterway of $L_{\text{bridge}} = 850\text{ m}$ across 17 spans of $50\text{ m}$ each.
2. **Guide Bund Layout (Spring's Guide Bund System):**
   - Earthen embankments with armored slopes constructed upstream and downstream of bridge abutments to guide flow axially through the bridge waterway:
   - Upstream length of guide bund:
     $$L_{\text{up}} = 1.25 \times L_{\text{bridge}} = 1.25 \times 850 = 1,062.5\text{ m}$$
   - Downstream length of guide bund:
     $$L_{\text{down}} = 0.25 \times L_{\text{bridge}} = 0.25 \times 850 = 212.5\text{ m}$$
   - Curved upstream mole-head:
     - Radius of upstream curve $R_c = 0.45 \times L_{\text{bridge}} = 0.45 \times 850 = 382.5\text{ m}$ subtending a sweep angle of $120^\circ - 145^\circ$.
3. **Launching Apron (Flexible Stone Protection):**
   - During extreme scour, the riverbed at the toe of the guide bund undermines. The launching apron must roll down along the scoured slope to self-heal and armor the toe.
   - Lacey scour depth $R = 0.473(22000/1.0)^{1/3} \approx 13.2\text{ m}$.
   - Scour depth at guide bund nose $= 2.0 R \approx 26.4\text{ m}$ below HFL.
   - Thickness of pitching on slope: $1.0\text{ m}$ heavy hand-packed rock riprap over $150\text{ mm}$ graded gravel filter.
   - Apron width at toe $W_{\text{apron}} = 1.5 \times (\text{scour depth below bed}) \approx 24.0\text{ m}$.

---

### Scenario 8: Industrial Wastewater Effluent Treatment Plant (ETP) Biological Sizing

#### 1. Context & Influent Characteristics
A pharmaceutical and chemical processing zone in Gujarat generates $Q = 2,500\text{ m}^3\text{/day}$ of high-strength industrial effluent.
- Raw influent characteristics:
  - $BOD_5 = 1,200\text{ mg/L}$
  - $COD = 3,000\text{ mg/L}$
  - Total Suspended Solids ($TSS$) = $450\text{ mg/L}$
  - Ammoniacal Nitrogen ($NH_4\text{-N}$) = $65\text{ mg/L}$
- Central Pollution Control Board (CPCB) discharge standards to surface waters:
  - $BOD_5 \le 10\text{ mg/L}$ ($99.2\%$ removal)
  - $COD \le 50\text{ mg/L}$
  - $TSS \le 20\text{ mg/L}$
  - Total Nitrogen $\le 10\text{ mg/L}$

#### 2. Process Train & Biological Unit Sizing
1. **Primary Treatment:**
   - Screen chambers + equalization tank (24-hour retention $= 2,500\text{ m}^3$ with submerged air mixers to prevent anaerobic souring).
   - Coagulation-Flocculation with polyaluminium chloride (PAC) + Primary Clarifier: removes $70\%$ TSS and $30\%$ BOD.
   - Primary effluent entering biological stage:
     $$BOD_{\text{in}} = 1200 \times (1 - 0.30) = 840\text{ mg/L}$$
     $$\text{Daily BOD load} = 2,500\text{ m}^3 \times 0.840\text{ kg/m}^3 = 2,100\text{ kg BOD/day}$$
2. **Biological Stage: Moving Bed Biofilm Reactor (MBBR) + Activated Sludge:**
   - Target effluent $BOD_e = 10\text{ mg/L}$.
   - Total BOD removal required $= 2,100 - (2,500 \times 0.010) = 2,100 - 25 = 2,075\text{ kg/day}$.
   - Select MBBR with high surface area HDPE carriers ($A_{\text{carrier}} = 650\text{ m}^2\text{/m}^3$ at $55\%$ media filling fraction).
   - Surface Area Loading Rate (SALR) = $18\text{ g BOD/m}^2\cdot\text{day}$.
   - Required carrier surface area:
     $$A_{\text{total}} = \frac{2,075,000\text{ g/day}}{18\text{ g/m}^2\cdot\text{day}} = 115,278\text{ m}^2$$
   - Total carrier volume:
     $$V_{\text{media}} = \frac{115,278}{650} \approx 177.3\text{ m}^3$$
   - Total bioreactor tank volume at $55\%$ filling ratio:
     $$V_{\text{tank}} = \frac{177.3}{0.55} \approx 322.4\text{ m}^3 \to \text{Provide } 400\text{ m}^3 \text{ working volume}$$
3. **Tertiary Polishing & Zero Liquid Discharge (ZLD):**
   - Secondary Tube Settler $\to$ Dual Media Filter (Sand-Anthracite) $\to$ Ultrafiltration (UF) $\to$ Reverse Osmosis (RO, 2-stage $85\%$ recovery) $\to$ Multiple Effect Evaporator (MEE) for brine crystallization.

---

### Scenario 9: 2D Hydrodynamic Flood Inundation Modeling & Risk Evacuation Zoning

#### 1. Context & Objective
Following severe urban flooding in the Chennai coastal basin, AECOM is retained by the state disaster management authority to establish an operational, real-time 2D hydrodynamic flood forecasting model using HEC-RAS 2D.

#### 2. Technical Modeling Workflow & Methodological Rigor
1. **Terrain & Mesh Generation:**
   - Merge airborne LiDAR ($0.5\text{ m}$ vertical accuracy) with bathymetric sonar soundings along river channels.
   - Generate a hybrid 2D computational mesh:
     - Base cell size $= 20\text{ m} \times 20\text{ m}$ on floodplains.
     - Refinement zones $= 2\text{ m} \times 2\text{ m}$ along flood walls, highway embankments, bridge piers, and channel breaklines.
     - Enforce sub-grid bathymetry: extract detailed elevation-volume curves per cell to capture micro-topographic drainage ditches.
2. **Turbulence & Equation Selection:**
   - Shallow Water Equations (Full Momentum / Saint-Venant) vs Diffusion Wave:
     - Chute spillway outflows, bridge contractions, and sudden tidal surges possess high convective acceleration ($u \frac{\partial u}{\partial x}$) and wave dynamics.
     - **Full Saint-Venant (SWE) mode must be selected**, as Diffusion Wave artificially damps inertial sloshing and underestimates backwater crest levels around highway embankments.
3. **Boundary Conditions & Coupling:**
   - Upstream: Hydrograph inflow from HEC-HMS rainfall-runoff model.
   - Downstream: Dynamic astronomical tide hydrograph + $0.80\text{ m}$ sea-level rise storm surge.
4. **Flood Hazard Vulnerability Index Mapping:**
   - Compute hazard product $H \times V$ (Depth $\times$ Velocity in $\text{m}^2\text{/s}$):
     - Low Hazard ($D \cdot V < 0.375\text{ m}^2\text{/s}$): Safe for wading adults.
     - Extreme Hazard ($D \cdot V > 1.5\text{ m}^2\text{/s}$ or Depth $> 1.2\text{ m}$): Vehicles mobilized, masonry wall collapse.
   - Output geo-referenced raster heatmaps integrated into the city’s GIS portal to establish phased community evacuation corridors.

---

### Scenario 10: Transit-Oriented Development (TOD) Sustainable Drainage & Groundwater Recharge

#### 1. Context & Sustainable Legacies Mandate
At a major transit interchange hub along the Delhi-Meerut Regional Rapid Transit System (RRTS), a 15-hectare multi-modal depot and commercial hub is being master-planned. The regional aquifer in this part of Western UP is critically over-exploited, with the static water table declining at $> 1.2\text{ m/year}$.

#### 2. Integrated WSUD / SuDS Master Plan
1. **Source Control Interventions:**
   - Green Roofs on station concourses ($12,000\text{ m}^2$): $80\text{ mm}$ engineered growth substrate capturing the first $15\text{ mm}$ of rainfall via retention and evapotranspiration.
   - Permeable Interlocking Concrete Pavements (PICP) across all pedestrian plazas ($25,000\text{ m}^2$): open-graded crushed stone reservoir sub-base ($300\text{ mm}$ thick with $40\%$ void space), storing $3,000\text{ m}^3$ of stormwater before subterranean infiltration.
2. **Conveyance & Filtration Swales:**
   - Replace concrete road gutters with vegetated roadside bioretention swales ($4\text{ km}$ total length).
   - Filter media: engineered loamy sand with engineered organic compost filtering heavy metals, tire wear debris, and hydrocarbon grease.
3. **Managed Aquifer Recharge (MAR) Injection Wells:**
   - Harvested rooftop runoff routed through silt traps and oil-grit separators into 8 deep recharge shaft boreholes.
   - Recharge shafts penetrate into unsaturated quaternary coarse sand aquifers at $35\text{ m}$ depth below ground level.
   - Infiltration rate per recharge shaft $= 25\text{ L/s}$, yielding an annual artificial recharge volume of $\approx 220,000\text{ m}^3\text{/year}$, reversing localized water table depression and achieving net-positive water stewardship.

---
*End of Practical Engineering Scenarios (10 Case Studies).*
