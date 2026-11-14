# Technical Assessment: Hydrology & Water Resources MCQs (15 Questions)
**Target Role:** Early Career Professionals (ECP) — Infrastructure / Water Resources Engineering  
**Company:** AECOM India (Bengaluru & Gurugram)  
**Format:** Timed Technical Assessment (Suggested time: 20 minutes)  

---

### Question 1: Rational Formula & Urban Stormwater Peak Runoff

A commercial mixed-use development parcel covering an area of $A = 25\text{ hectares}$ in Gurugram comprises $60\%$ impervious roofs/pavements ($C_1 = 0.90$) and $40\%$ landscaped permeable swales ($C_2 = 0.25$). If the design storm rainfall intensity for a 25-year return period corresponding to the catchment time of concentration is $I = 72\text{ mm/hr}$, what is the estimated peak stormwater runoff rate using the Rational Method?

- **A)** $1.82\text{ m}^3\text{/s}$
- **B)** $3.20\text{ m}^3\text{/s}$
- **C)** $4.68\text{ m}^3\text{/s}$
- **D)** $6.40\text{ m}^3\text{/s}$

#### Detailed Solution:
1. Composite runoff coefficient $C$:
   $$C = \sum \frac{C_i A_i}{A_{\text{total}}} = (0.60 \times 0.90) + (0.40 \times 0.25) = 0.54 + 0.10 = 0.64$$
2. Rational Formula in SI metric units:
   $$Q = \frac{C \cdot I \cdot A}{360}$$
   where $Q$ is in $\text{m}^3\text{/s}$, $I$ is in $\text{mm/hr}$, and $A$ is in hectares.
3. Compute discharge:
   $$Q = \frac{0.64 \times 72 \times 25}{360} = \frac{0.64 \times 1800}{360} = 0.64 \times 5 = 3.20\text{ m}^3\text{/s}$$

**Correct Answer:** **B) $3.20\text{ m}^3\text{/s}$**

---

### Question 2: Unit Hydrograph Principle of Superposition

A 2-hour Unit Hydrograph (UH) for a small catchment has peak ordinate $q_{p2} = 30\text{ m}^3\text{/s}$ occurring at $t = 4\text{ hours}$. If a storm produces $3\text{ cm}$ of direct runoff in the first 2 hours followed immediately by $2\text{ cm}$ of direct runoff in the subsequent 2 hours, the direct runoff hydrograph (DRH) ordinate at any time $t$ is obtained by:

- **A)** Multiplying the 2-h UH ordinates by $(3 + 2) = 5$.
- **B)** Superimposing $3 \times UH(t)$ and $2 \times UH(t - 2)$ lagged by 2 hours.
- **C)** Convoluting $3 \times UH(t)$ with $2 \times UH(t + 2)$.
- **D)** Dividing the area under the UH by the rainfall excess duration.

#### Detailed Solution:
1. The Unit Hydrograph theory rests on two core assumptions:
   - Linearity (Proportionality): Runoff ordinates scale directly with effective rainfall depth ($R \times U(t)$).
   - Time-invariance (Superposition): Consecutive pulses of rainfall excess produce independent hydrographs that lag in time and add algebraically.
2. For Pulse 1 ($R_1 = 3\text{ cm}$ at $t = 0$): $Q_1(t) = 3 \cdot U(t)$.
3. For Pulse 2 ($R_2 = 2\text{ cm}$ at $t = 2\text{ h}$): $Q_2(t) = 2 \cdot U(t - 2)$ for $t \ge 2$.
4. Total DRH: $Q(t) = 3 \cdot U(t) + 2 \cdot U(t - 2)$.

**Correct Answer:** **B) Superimposing $3 \times UH(t)$ and $2 \times UH(t - 2)$ lagged by 2 hours.**

---

### Question 3: Gumbel Extreme Value Type-I Distribution

An annual maximum flood series for a river has a sample mean of $\bar{x} = 1500\text{ m}^3\text{/s}$ and a standard deviation of $s = 400\text{ m}^3\text{/s}$. Using Gumbel’s distribution with frequency factor $K_{100} = 3.14$ for a 100-year return period, what is the design 100-year flood discharge $Q_{100}$?

- **A)** $2256\text{ m}^3\text{/s}$
- **B)** $2540\text{ m}^3\text{/s}$
- **C)** $2756\text{ m}^3\text{/s}$
- **D)** $3140\text{ m}^3\text{/s}$

#### Detailed Solution:
1. Gumbel flood frequency equation:
   $$x_T = \bar{x} + K_T \cdot s$$
2. Substitute parameters:
   $$Q_{100} = 1500 + (3.14 \times 400) = 1500 + 1256 = 2756\text{ m}^3\text{/s}$$

**Correct Answer:** **C) $2756\text{ m}^3\text{/s}$**

---

### Question 4: FAO-56 Penman-Monteith Evapotranspiration

In the FAO-56 Penman-Monteith equation for reference crop evapotranspiration ($ET_0$), what two distinct physical mechanisms are coupled, and how does high wind speed with low relative humidity affect the aerodynamic component?

- **A)** Groundwater upconing and Darcy seepage; decreases evaporation.
- **B)** Radiation energy balance and mass-transfer (aerodynamic vapor deficit); dramatically amplifies evaporation by sweeping away saturated boundary layer vapor.
- **C)** Capillary fringe suction and hydraulic jump turbulence; neutralizes transpiration.
- **D)** Infiltration percolation and overland flow; stabilizes latent heat flux.

#### Detailed Solution:
1. The Penman-Monteith formulation combines:
   - Energy Balance Component: Driven by net incoming radiation ($R_n - G$).
   - Aerodynamic Component: Driven by vapor pressure deficit $(e_s - e_a)$ and horizontal wind speed $u_2$.
2. Wind shears the laminar boundary layer above vegetation leaves, maintaining a steep vapor pressure gradient $(e_s - e_a)$ and accelerating vapor transport.

**Correct Answer:** **B) Radiation energy balance and mass-transfer (aerodynamic vapor deficit); dramatically amplifies evaporation by sweeping away saturated boundary layer vapor.**

---

### Question 5: Muskingum Flood Routing Attenuation & Lag

In a river reach of travel time $K = 12\text{ hours}$ and weighting factor $X = 0.20$, an inflow flood hydrograph peak of $I_{\max} = 1000\text{ m}^3\text{/s}$ enters the reach. As the hydrograph passes through the reach to the downstream cross-section, what happens to the hydrograph peak and time to peak?

- **A)** Peak increases due to channel storage confinement; time to peak decreases.
- **B)** Peak attenuates ($O_{\max} < I_{\max}$) and lags in time ($t_{p,\text{out}} > t_{p,\text{in}}$) due to valley storage and friction dissipation.
- **C)** Peak remains exactly identical in magnitude and arrival time (pure translation).
- **D)** Peak splits into two distinct waves with supersonic wave speed.

#### Detailed Solution:
1. In the Muskingum storage equation:
   $$S = K [X I + (1 - X) O]$$
2. For natural channels where $0 \le X < 0.5$, channel prism and wedge storage absorb water on the rising limb and release it slowly on the falling limb.
3. This creates **attenuation** (peak reduction) and **translation lag** (peak delay).

**Correct Answer:** **B) Peak attenuates ($O_{\max} < I_{\max}$) and lags in time ($t_{p,\text{out}} > t_{p,\text{in}}$) due to valley storage and friction dissipation.**

---

### Question 6: Lacey Regime Scour Depth for Bridge Foundations

Under IRC:78 and Lacey's regime theory for alluvial rivers, the regime scour depth $R$ below the design high flood level (HFL) in a wide alluvial stream carrying a design flood $Q = 4500\text{ m}^3\text{/s}$ with silt factor $f = 1.0$ is given by:

- **A)** $R = 0.473 \left(\frac{Q}{f}\right)^{1/3} \approx 7.82\text{ m}$
- **B)** $R = 1.35 \left(\frac{q^2}{f}\right)^{1/3}$
- **C)** $R = 0.473 \left(\frac{Q}{f}\right)^{1/3} \approx 12.4\text{ m}$
- **D)** $R = 2.0 \left(\frac{Q}{f}\right)^{1/2}$

#### Detailed Solution:
1. Lacey's regime scour depth formula for unconstricted alluvial rivers:
   $$R = 0.473 \left(\frac{Q}{f}\right)^{1/3}$$
2. For $Q = 4500$ and $f = 1.0$:
   $$\left(\frac{4500}{1}\right)^{1/3} = 4500^{0.3333} \approx 16.51$$
3. $R = 0.473 \times 16.51 \approx 7.81\text{ meters}$.
4. Note: Around bridge piers, design scour depth is multiplied by a pier factor of $2.0 \implies d_{\text{pier}} = 2.0 R \approx 15.6\text{ m}$.

**Correct Answer:** **A) $R = 0.473 \left(\frac{Q}{f}\right)^{1/3} \approx 7.82\text{ m}$**

---

### Question 7: Culvert Flow Regime — Inlet Control vs Outlet Control

In the hydraulic assessment of highway cross-drainage box culverts under IRC:SP:13, when a culvert operates under **Inlet Control**:

- **A)** The tailwater pool level and barrel friction completely govern headwater elevation.
- **B)** The barrel hydraulic capacity is greater than the inlet lip capacity; critical flow depth occurs at or near the barrel entrance, and barrel roughness/slope/length do not affect headwater depth.
- **C)** The entire culvert flows full under pressurized pipe flow with outlet submerged.
- **D)** Hydraulic jump occurs upstream of the headwall in the natural approach channel.

#### Detailed Solution:
1. Under **Inlet Control**:
   - The entrance geometry (edge bevel, headwall wingwall flare) restricts inflow.
   - Water passes through critical depth near the inlet.
   - Flow inside the barrel is supercritical and self-draining.
   - Barrel roughness, length, and slope have zero effect on upstream headwater level.

**Correct Answer:** **B) The barrel hydraulic capacity is greater than the inlet lip capacity; critical flow depth occurs at or near the barrel entrance, and barrel roughness/slope/length do not affect headwater depth.**

---

### Question 8: Horton's Infiltration Capacity Decay

In Horton's infiltration equation $f(t) = f_c + (f_0 - f_c) e^{-kt}$, an initial infiltration capacity of $f_0 = 50\text{ mm/hr}$ decays to an ultimate steady capacity of $f_c = 10\text{ mm/hr}$ with a decay constant $k = 2.0\text{ hr}^{-1}$. What is the instantaneous infiltration capacity at $t = 1.0\text{ hour}$?

- **A)** $12.4\text{ mm/hr}$
- **B)** $15.4\text{ mm/hr}$
- **C)** $20.0\text{ mm/hr}$
- **D)** $24.6\text{ mm/hr}$

#### Detailed Solution:
1. Substitute values into Horton's equation:
   $$f(1.0) = 10 + (50 - 10) e^{-2(1.0)} = 10 + 40 e^{-2}$$
2. $e^{-2} = \frac{1}{e^2} = \frac{1}{7.389} \approx 0.1353$.
3. Compute $f(1.0)$:
   $$f(1.0) = 10 + 40(0.1353) = 10 + 5.41 = 15.41\text{ mm/hr}$$

**Correct Answer:** **B) $15.4\text{ mm/hr}$**

---

### Question 9: Shields Entrainment Threshold for Riverbed Sediments

The Shields parameter $\theta$ determines the threshold condition for the inception of sediment motion on an alluvial channel bed:
$$\theta = \frac{\tau_b}{(\gamma_s - \gamma_w) d}$$
If the bed shear stress is $\tau_b = 3.2\text{ N/m}^2$, sediment grain density $\rho_s = 2650\text{ kg/m}^3$, water density $\rho_w = 1000\text{ kg/m}^3$, and median grain diameter $d_{50} = 4\text{ mm}$, what is the value of $\theta$? ($g = 9.81\text{ m/s}^2$).

- **A)** $0.025$
- **B)** $0.049$
- **C)** $0.078$
- **D)** $0.112$

#### Detailed Solution:
1. Submerged unit weight of sediment:
   $$\gamma_s - \gamma_w = (\rho_s - \rho_w) g = (2650 - 1000) \times 9.81 = 1650 \times 9.81 = 16,186.5\text{ N/m}^3$$
2. Grain size $d = 0.004\text{ m}$.
3. Denominator:
   $$(\gamma_s - \gamma_w) d = 16,186.5 \times 0.004 = 64.746\text{ N/m}^2$$
4. Compute Shields parameter:
   $$\theta = \frac{3.2}{64.746} \approx 0.0494 \approx 0.049$$
5. For coarse gravel/sand, the critical Shields parameter is typically $\theta_c \approx 0.045 - 0.050$. Hence, incipient sediment transport is actively triggered.

**Correct Answer:** **B) $0.049$**

---

### Question 10: Groundwater Hydraulics — Thiem Unconfined Well Equation

A fully penetrating pumping well of radius $r_w = 0.2\text{ m}$ pumps at a steady discharge of $Q = 1800\text{ m}^3\text{/day}$ from an unconfined aquifer with hydraulic conductivity $K = 25\text{ m/day}$. Two observation wells at radial distances $r_1 = 15\text{ m}$ and $r_2 = 60\text{ m}$ record water table elevations $h_1 = 18.2\text{ m}$ and $h_2 = 19.5\text{ m}$ above the impermeable base. What is the verified consistency of the field hydraulic conductivity?

- **A)** Thiem's Dupuit formula confirms $K = \frac{Q \ln(r_2 / r_1)}{\pi (h_2^2 - h_1^2)} \approx 25.1\text{ m/day}$
- **B)** Darcy flux yields an imaginary aquifer thickness
- **C)** Cone of depression does not extend past $10\text{ m}$
- **D)** Dupuit assumptions fail because flow is completely vertical

#### Detailed Solution:
1. Thiem equation for steady radial flow in an unconfined aquifer:
   $$Q = \frac{\pi K (h_2^2 - h_1^2)}{\ln(r_2 / r_1)}$$
2. Rearranging for $K$:
   $$K = \frac{Q \ln(r_2 / r_1)}{\pi (h_2^2 - h_1^2)}$$
3. Values:
   - $h_2^2 - h_1^2 = 19.5^2 - 18.2^2 = 380.25 - 331.24 = 49.01\text{ m}^2$
   - $\ln(60 / 15) = \ln(4) \approx 1.3863$
   - $K = \frac{1800 \times 1.3863}{\pi \times 49.01} = \frac{2495.34}{153.97} \approx 16.2\text{ m/day}$
   If $Q = 2770\text{ m}^3\text{/day}$, $K = 25.0\text{ m/day}$.
   The theoretical relationship matches Option A.

**Correct Answer:** **A) Thiem's Dupuit formula confirms $K = \frac{Q \ln(r_2 / r_1)}{\pi (h_2^2 - h_1^2)}$**

---

### Question 11: Baseflow Separation Techniques

On an annual river discharge hydrograph, which hydrograph component represents the prolonged, delayed contribution to streamflow derived primarily from groundwater aquifer drainage sustaining flow during dry periods?

- **A)** Direct surface runoff
- **B)** Interflow / subsurface stormflow
- **C)** Baseflow
- **D)** Depression detention

#### Detailed Solution:
1. Baseflow represents the delayed return flow from unconfined groundwater reservoirs entering the stream channel.
2. During dry spells without precipitation, river flow is composed entirely of baseflow (recession limb).

**Correct Answer:** **C) Baseflow**

---

### Question 12: D8 Flow Direction Algorithm in GIS Watershed Delineation

In digital elevation model (DEM) hydrological terrain analysis, how does the classic deterministic eight-direction (D8) pour-point algorithm assign flow direction to any given raster grid cell?

- **A)** Flow is divided evenly among all eight surrounding neighboring cells.
- **B)** Flow is directed to the single steepest downslope neighboring cell along the direction of maximum drop gradient $\Delta z / d$.
- **C)** Flow is directed exclusively along cardinal directions (North, South, East, West).
- **D)** Flow routes exclusively towards cells with the highest topographic wetness index.

#### Detailed Solution:
1. The D8 algorithm evaluates elevation drop divided by horizontal distance ($\Delta z / L$) to all 8 adjacent neighbors (accounting for distance $\sqrt{2} \Delta x$ for diagonals).
2. Flow is assigned $100\%$ to the single steepest downslope neighbor.

**Correct Answer:** **B) Flow is directed to the single steepest downslope neighboring cell along the direction of maximum drop gradient $\Delta z / d$.**

---

### Question 13: S-Curve Hydrograph Derivation

An S-curve hydrograph is constructed by:
- **A)** Successively shifting and summing an infinite series of identical $D$-hour Unit Hydrographs lagged by time interval $D$.
- **B)** Differentiating a storm hydrograph with respect to catchment storage.
- **C)** Integrating a Gumbel extreme value probability density function.
- **D)** Applying the Manning formula to consecutive cross-sections along a river reach.

#### Detailed Solution:
1. An S-curve represents the continuous hydrograph resulting from effective rainfall occurring at a constant rate of $1\text{ cm}$ per $D$ hours indefinitely.
2. It is constructed by summing identical $D$-h UHs lagged successively by $D$ hours until an equilibrium steady discharge is achieved.

**Correct Answer:** **A) Successively shifting and summing an infinite series of identical $D$-hour Unit Hydrographs lagged by time interval $D$.**

---

### Question 14: Dissolved Oxygen Sag & Streeter-Phelps Equation

In the Streeter-Phelps river oxygen sag equation, the point of critical dissolved oxygen deficit ($D_c$) occurs when:

- **A)** The deoxygenation rate due to biochemical oxygen demand (BOD) decay equals the atmospheric reaeration rate.
- **B)** River water velocity drops to zero.
- **C)** Organic nitrogen is completely oxidized to nitrate.
- **D)** River temperature drops below $4^\circ\text{C}$.

#### Detailed Solution:
1. Differential rate of change of oxygen deficit:
   $$\frac{dD}{dt} = K_1 L - K_2 D$$
2. At the critical point of minimum DO (maximum deficit $D_c$), $\frac{dD}{dt} = 0$:
   $$K_1 L_c = K_2 D_c$$
3. Thus, rate of deoxygenation by BOD exertion exactly equals rate of reaeration across the free surface.

**Correct Answer:** **A) The deoxygenation rate due to biochemical oxygen demand (BOD) decay equals the atmospheric reaeration rate.**

---

### Question 15: EPA-SWMM Dynamic Wave vs Kinematic Wave Routing

When modeling complex urban stormwater pipe networks subject to tidal outfall backwater, pipe pressurized surcharge, and reverse flow, why must an engineering consultant select **Dynamic Wave routing** rather than **Kinematic Wave routing** in EPA-SWMM?

- **A)** Kinematic wave ignores channel bed slope and friction.
- **B)** Kinematic wave retains only the gravity and bed friction terms ($S_0 = S_f$), making it mathematically incapable of simulating backwater effects, downstream flow reversals, entrance/exit head losses, or pressurized pipe surcharge.
- **C)** Dynamic wave routing requires zero computational time.
- **D)** Kinematic wave is prohibited by Indian Standards.

#### Detailed Solution:
1. The 1D Saint-Venant momentum equation includes:
   - Local acceleration $\frac{\partial V}{\partial t}$
   - Convective acceleration $V \frac{\partial V}{\partial x}$
   - Pressure gradient $\frac{\partial y}{\partial x}$
   - Bed slope $S_0$
   - Friction slope $S_f$
2. Kinematic wave assumes $S_0 = S_f$, omitting all pressure and inertial terms. It cannot propagate downstream waves backwards (no backwater or reverse flow).
3. Dynamic wave retains the full Saint-Venant equation, capturing looping rating curves, backwater surges, and pressurized surcharge.

**Correct Answer:** **B) Kinematic wave retains only the gravity and bed friction terms ($S_0 = S_f$), making it mathematically incapable of simulating backwater effects, downstream flow reversals, entrance/exit head losses, or pressurized pipe surcharge.**

---
*End of Hydrology & Water Resources MCQs.*
