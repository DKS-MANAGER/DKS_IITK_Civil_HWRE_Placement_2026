# Hydrology & Water Resources Engineering: Analytical Foundations

**Target Role:** Early Career Professionals (ECP) | AECOM India  
**Context:** IIT Kanpur Placement Season 2026–27  
**Candidate Alignment:** M.Tech Civil (HWRE), IIT Kanpur — IDF Curve Derivation, Streamflow Modeling, FAO-56 PET

---

## 1. Catchment Hydrology & Precipitation Mechanics

### 1.1 Hydrologic Water Budget Equation
For a closed watershed boundary over time interval $\Delta t$:

$$P - R - ET - G - \Delta S = 0$$
Where $P$ is precipitation, $R$ is surface runoff, $ET$ is evapotranspiration, $G$ is net groundwater outflow, and $\Delta S$ is the change in total basin storage (soil moisture, groundwater, depression storage).

### 1.2 Areal Rainfall Estimation
1. **Thiessen Polygon Method:** Assigns weights $w_i = \frac{A_i}{A_{\text{total}}}$ based on perpendicular bisectors:
   $$\bar{P} = \sum_{i=1}^n w_i P_i$$
2. **Isohyetal Method:** Accounts for orographic topography by integrating contour bands:
   $$\bar{P} = \frac{1}{A_{\text{total}}} \sum_{j=1}^{m} A_j \left(\frac{P_j + P_{j+1}}{2}\right)$$

### 1.3 Intensity-Duration-Frequency (IDF) Curves
*(Candidate Project Anchor)*  
IDF relationships quantify the probability of extreme rainfall events:

$$I = \frac{K \cdot T^m}{(D + a)^n}$$
- $I$: Rainfall intensity (mm/hr).
- $D$: Rainfall duration (minutes or hours).
- $T$: Return period (years).
- $K, m, a, n$: Basin-calibrated empirical parameters.

---

## 2. Infiltration & Evapotranspiration

### 2.1 Infiltration Modeling
1. **Horton's Exponential Infiltration Equation:**
   $$f(t) = f_c + (f_0 - f_c) e^{-k t}$$
   Total cumulative infiltration: $F(t) = \int_0^t f(t) dt = f_c t + \frac{f_0 - f_c}{k} (1 - e^{-kt})$.
2. **The $\Phi$-Index:** The constant average infiltration rate above which rainfall volume equals direct surface runoff volume:
   $$R = \sum_{t=1}^N (P_t - \Phi \Delta t) \cdot \mathbb{I}(P_t > \Phi \Delta t)$$

### 2.2 Evapotranspiration: FAO-56 Penman-Monteith Formulation
*(Candidate Project Anchor)*  
The international gold standard (Allen et al., 1998) for reference evapotranspiration ($ET_0$):

$$ET_0 = \frac{0.408 \Delta (R_n - G) + \gamma \frac{900}{T + 273} u_2 (e_s - e_a)}{\Delta + \gamma (1 + 0.34 u_2)}$$
Where:
- $R_n$: Net radiation at the crop surface ($\text{MJ/m}^2/\text{day}$).
- $G$: Soil heat flux density ($\text{MJ/m}^2/\text{day}$).
- $T$: Mean daily air temperature at 2 m height ($^\circ\text{C}$).
- $u_2$: Wind speed at 2 m height ($\text{m/s}$).
- $e_s - e_a$: Saturation vapor pressure deficit ($\text{kPa}$).
- $\Delta$: Slope of the vapor pressure curve ($\text{kPa}/^\circ\text{C}$).
- $\gamma$: Psychrometric constant ($\text{kPa}/^\circ\text{C}$).

---

## 3. Hydrograph Analysis & Unit Hydrograph Theory

A Unit Hydrograph (UH) is the direct runoff hydrograph resulting from $1\text{ cm}$ (or $1\text{ mm}$) of effective rainfall occurring uniformly over a watershed at a constant rate for duration $D$.

### 3.1 Foundational Assumptions
1. **Linear Response (Proportionality):** If effective rainfall increases by factor $k$, direct runoff ordinates scale by $k$.
2. **Time Invariance:** Catchment response to a unit storm is invariant over time.
3. **Superposition:** Runoff from sequential rain blocks is obtained by summing lagged hydrographs.

### 3.2 The S-Curve Technique (Changing Duration $D_1 \to D_2$)
To convert a $D_1$-hour UH to a $D_2$-hour UH:
1. Construct the continuous $S$-curve by summing infinitely lagged $D_1$-hour unit hydrographs:
   $$S(t) = \sum_{k=0}^\infty UH(t - k D_1)$$
   The $S$-curve reaches an equilibrium discharge $Q_e = 2.778 \frac{A}{D_1} \text{ m}^3/\text{s}$.
2. Lag the $S$-curve by new duration $D_2$: $S(t - D_2)$.
3. Compute the new $D_2$-hour UH ordinates:
   $$UH_{D_2}(t) = \frac{D_1}{D_2} \left[ S(t) - S(t - D_2) \right]$$

---

## 4. Flood Estimation & Routing

### 4.1 Extreme Value Analysis: Gumbel Type I
For annual maximum flood series with sample mean $\bar{x}$ and sample standard deviation $s$:

$$x_T = \bar{x} + K_T \cdot s$$
Frequency factor $K_T$:
$$K_T = -\frac{\sqrt{6}}{\pi} \left[ 0.5772 + \ln\left( \ln\left( \frac{T}{T - 1} \right) \right) \right]$$
Where $T$ is the design return period.
- Exceedance Probability: $P = 1/T$.
- Risk over project design life of $N$ years: $R = 1 - (1 - P)^N = 1 - \left(1 - \frac{1}{T}\right)^N$.

### 4.2 Muskingum Hydrologic Channel Routing
Relates storage to weighted inflow and outflow:
$$S = K \left[ X I + (1 - X) Q \right]$$
- $K$: Storage time constant ($\sim$ travel time through reach).
- $X$: Weighting factor ($0 \le X \le 0.5$; $X = 0$ for reservoir storage, $X \approx 0.2$ for natural rivers).

**Routing Formulation:**
$$Q_{j+1} = C_0 I_{j+1} + C_1 I_j + C_2 Q_j$$
Where:
$$C_0 = \frac{\Delta t - 2KX}{2K(1-X) + \Delta t}, \quad C_1 = \frac{\Delta t + 2KX}{2K(1-X) + \Delta t}, \quad C_2 = \frac{2K(1-X) - \Delta t}{2K(1-X) + \Delta t}$$
*Numerical Stability Constraint:* $2KX < \Delta t < 2K(1-X)$.

---

## 5. Urban Stormwater Drainage & Culvert Hydraulics

### 5.1 The Rational Method
For urban catchments where catchment area $A \le 50\text{ hectares}$:

$$Q_p = \frac{1}{360} C \cdot I(t_c) \cdot A$$
- $Q_p$: Peak discharge ($\text{m}^3/\text{s}$).
- $C$: Composite runoff coefficient ($\sum C_i A_i / A_{\text{total}}$).
- $I(t_c)$: Rainfall intensity for duration equal to time of concentration $t_c$ (from IDF curve).
- **Kirpich Formula for Time of Concentration ($t_c$):**
  $$t_c = 0.01947 \cdot L^{0.77} \cdot S^{-0.385} \quad (t_c \text{ in mins, } L \text{ in meters, } S \text{ in m/m})$$

### 5.2 Culvert Hydraulics: Inlet vs Outlet Control
Highway culverts (IRC:SP:13 / FHWA HEC-5) operate under two regimes:
1. **Inlet Control:** Discharge capacity is governed solely by culvert entrance geometry (area, shape, edge type) and headwater depth $HW$. Barrel roughness and tailwater have zero effect. Flow inside barrel is supercritical.
2. **Outlet Control:** Discharge capacity is governed by headwater, barrel friction, tailwater level $TW$, and barrel length. Flow inside barrel is subcritical or full-flowing pressurized pipe flow:
   $$H = H_e + H_f + H_o = \left( K_e + \frac{29.16 n^2 L}{R_h^{4/3}} + 1.0 \right) \frac{V^2}{2g}$$

---

## 6. River Engineering & Sediment Transport Mechanics

### 6.1 Incipient Motion & The Shields Diagram
Sediment grain motion initiates when hydrodynamic drag and lift forces exceed submerged submerged gravitational resistance.

**Dimensionless Shear Stress (Shields Parameter $\theta$):**
$$\theta = \frac{\tau_0}{(\gamma_s - \gamma) d_{50}} = \frac{u_*^2}{(s - 1) g d_{50}}$$
- Shear velocity: $u_* = \sqrt{\frac{\tau_0}{\rho}} = \sqrt{g R_h S_0}$.
- Specific gravity of sediment: $s = \frac{\rho_s}{\rho} \approx 2.65$.
- Motion initiates when $\theta > \theta_c \approx 0.03 - 0.06$ (Shields curve).

### 6.2 Vertical Suspended Sediment Profile: Rouse Equation
Equating downward gravitational settling ($C \cdot w_s$) with upward turbulent diffusion ($\epsilon_s \frac{dC}{dy}$):

$$\frac{C(y)}{C_a} = \left( \frac{h - y}{y} \frac{a}{h - a} \right)^{Z_*}$$
Where $Z_* = \frac{w_s}{\kappa u_*}$ is the **Rouse Number**:
- $w_s$: Particle settling velocity (Stokes' Law for fine particles).
- $\kappa$: von Kármán constant ($\approx 0.40$).
- $a$: Reference level above bed; $C_a$: Reference sediment concentration.
- $Z_* > 2.5$: Bedload dominates; $Z_* < 0.8$: Fully suspended wash load.

### 6.3 Bridge Foundation Scour Mechanics
Scour at bridge piers and abutments consists of three components:
$$\text{Total Scour} = \text{Long-Term Degradation} + \text{Contraction Scour} + \text{Local Scour}$$

1. **Lacey’s Regime Scour Depth (Indian Standard IRC:78):**
   $$R = 1.35 \left(\frac{q^2}{f}\right)^{1/3}, \quad f = 1.76 \sqrt{d_{50}} \text{ (Silt factor, } d_{50} \text{ in mm)}$$
   - Pier maximum scour depth: $d_s = 2.0 R$ below design High Flood Level (HFL).
   - Abutment maximum scour depth: $d_s = 1.27 R$ to $1.50 R$.
2. **Hydrodynamic Horseshoe & Wake Vortices:**
   Impinging flow decelerates at the upstream pier face, creating a strong downward vertical jet that rolls into a 3D **horseshoe vortex** at the bed. Downstream, boundary layer separation sheds **wake vortices** that vacuum sediment into the main current.
