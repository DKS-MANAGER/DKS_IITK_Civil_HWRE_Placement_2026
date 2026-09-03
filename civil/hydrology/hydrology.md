# Hydrology

## Hydrologic Cycle

The hydrologic cycle describes the continuous movement of water on, above, and below the Earth's surface.

> **Related topics:** [`open-channel-flow.md`](../open_channel_flow/open-channel-flow.md) · [`sediment-transport.md`](sediment-transport.md) · [`water-resources-engineering.md`](../water_resources/water-resources-engineering.md) · [`../hwre/flood_control/flood-control.md`](../../hwre/flood_control/flood-control.md)

---

## Rainfall-Runoff Relationships

### Catchment Response
- Rainfall excess = Precipitation − infiltration losses − interception losses
- **Time of concentration ($t_c$):** Time for water to travel from the most distant point to the outlet
- **Lag time ($t_L$):** Delay between centroid of rainfall excess and peak discharge
- **Relationship:** $t_L \approx 0.6 \, t_c$ (typical)

### Infiltration Models

| Model | Equation | Parameters |
|-------|----------|------------|
| **Horton** | $f(t) = f_c + (f_0 - f_c)e^{-kt}$ | $f_0$: initial rate, $f_c$: final rate, $k$: decay constant |
| **Philip** | $F(t) = St^{1/2} + At$ | $S$: sorptivity, $A$: transmissivity term |
| **Green-Ampt** | $f = K\left(1 + \frac{\psi \Delta\theta}{F}\right)$ | $K$: hydraulic conductivity, $\psi$: wetting front suction |

---

## Hydrograph Analysis

### Unit Hydrograph (UH)

**Definition:** Direct runoff hydrograph resulting from 1 unit (e.g., 1 cm) of effective rainfall distributed uniformly over the catchment for a specified duration.

**Key principles:**
- **Linearity:** Runoff is proportional to effective rainfall depth
- **Time-invariance:** The UH response is the same regardless of when rainfall occurs

**S-Curve Method (for duration conversion):**
1. Derive S-curve by summing UH ordinates with time shift = duration $D$
2. Shift S-curve by new duration $D'$
3. Difference = $(D'/D) \times$ new UH ordinates

**Snyder's Method (for ungauged catchments):**
$$t_p = C_t (L \cdot L_c)^{0.3}$$
$$Q_p = \frac{640 \cdot C_p \cdot A}{t_p}$$

Where: $L$ = basin length, $L_c$ = length to centroid, $C_t$, $C_p$ = coefficients

### Flood Frequency Analysis

**Gumbel Distribution:**
$$x_T = \bar{x} + \frac{\sigma}{\sigma_n} \left[0.7797 \, y_T - 0.45005 \, y_T + 0.1291 \, y_T^2\right]$$

Where $y_T = -\ln(-\ln(1 - 1/T))$, $T$ = return period

**Log-Pearson Type III:**
$$\log x_T = \bar{\log x} + K_T \cdot \sigma_{\log x}$$

Where $K_T$ is the frequency factor from tables

### Hydrograph Separation
- **Straight-line method:** Connect start and end of direct runoff
- **Fixed-discharge method:** Baseflow = constant (minimum flow)
- **Variable-discharge method:** Baseflow decreases then increases
- **Filters:** Lyne-Hollick, Eckhardt for continuous separation

---

## Flood Routing

### Muskingum Method

**Storage equation:**
$$S = K[XI + (1-X)O]$$

Where $K$ = storage time constant, $X$ = weighting factor (0–0.5)

**Routing equation:**
$$O_2 = C_0 I_2 + C_1 I_1 + C_2 O_1$$

**Routing coefficients:**
$$C_0 = \frac{-KX + 0.5\Delta t}{K(1-X) + 0.5\Delta t}$$
$$C_1 = \frac{KX + 0.5\Delta t}{K(1-X) + 0.5\Delta t}$$
$$C_2 = \frac{K(1-X) - 0.5\Delta t}{K(1-X) + 0.5\Delta t}$$

**Check:** $C_0 + C_1 + C_2 = 1$

**Typical values:**
- $K$ = travel time through reach (hours)
- $X$ = 0.0–0.5 (typically 0.1–0.3 for natural channels)

### Level Pool (Reservoir) Routing

**Storage-indication method:**
$$\frac{2S}{\Delta t} + O = 2I + \left(\frac{2S}{\Delta t} - O\right)_{\text{previous}}$$

**Steps:**
1. Develop $S$ vs $O$ relationship from stage-storage-discharge curves
2. Compute $(2S/\Delta t + O)$ for each $O$
3. At each time step, compute RHS using known $I_1$, $I_2$, and previous $(2S/\Delta t - O)$
4. Find $O_2$ from the $(2S/\Delta t + O)$ vs $O$ curve

### Wave Routing Methods

| Method | Equation | Application |
|--------|----------|-------------|
| **Kinematic Wave** | $Q = \alpha A^m$ | Steep slopes, no backwater |
| **Diffusion Wave** | Adds pressure gradient term | Moderate complexity |
| **Dynamic Wave** | Full Saint-Venant | Most accurate, computationally expensive |

---

## Groundwater Hydrology

### Darcy's Law
$$Q = K \cdot i \cdot A = -KA\frac{dh}{dl}$$

Where:
- $Q$ = discharge (m³/s)
- $K$ = hydraulic conductivity (m/s)
- $i$ = hydraulic gradient ($dh/dl$)
- $A$ = cross-sectional area (m²)

### Aquifer Properties

| Property | Definition | Units |
|----------|------------|-------|
| Transmissivity $T$ | $T = K \cdot b$ (aquifer thickness) | m²/s |
| Storativity $S$ | Volume released per unit area per unit head change | dimensionless |
| Specific yield $S_y$ | Drainable porosity (unconfined) | dimensionless |
| Specific storage $S_s$ | Volume released per unit volume per unit head change | 1/m |

### Well Hydraulics

#### Thiem Equation (Steady State — Confined)
$$Q = \frac{2\pi T (h_2 - h_1)}{\ln(r_2/r_1)}$$

#### Theis Equation (Unsteady — Confined)
$$s = \frac{Q}{4\pi T} W(u)$$

Where $u = \frac{r^2 S}{4Tt}$ and $W(u) = \int_u^\infty \frac{e^{-x}}{x} dx$ (well function)

#### Cooper-Jacob Approximation ($u < 0.01$)
$$s = \frac{2.3Q}{4\pi T} \log\left(\frac{2.25Tt}{r^2 S}\right)$$

**Plot:** $s$ vs $\log t$ → straight line; slope gives $T$, intercept gives $S$

---

## Hydrologic Modeling Software

| Tool | Application |
|------|-------------|
| HEC-HMS | Precipitation-runoff modeling |
| MODFLOW 6 | Groundwater flow modeling |
| SEEP/W | Seepage and groundwater analysis |
| SWMM | Stormwater management |
| RAS Mapper | GIS-based hydraulic analysis |

---

## Worked Examples

### Example 1: Unit Hydrograph Synthesis
**Problem:** 1-hour UH for a catchment: $Q_p = 50$ m³/s, $t_p = 5$ h. Synthesize a 3-hour DRH for $P_{eff} = 5$ cm using S-curve.

**Solution:**
1. S-curve: Sum 1-h UH ordinates shifted by 1 h each
2. Shift S-curve by 3 h (new duration)
3. Difference = $(3/1) \times$ 3-h UH ordinates
4. 3-h UH peak: $Q_{p,3h} = Q_{p,1h} \times (1/3) = 16.7$ m³/s
5. For 5 cm excess: Multiply 3-h UH by 5 → DRH peak = 83.3 m³/s

### Example 2: Muskingum Routing
**Problem:** $K = 6$ h, $X = 0.2$, $\Delta t = 3$ h. Inflow: $I_1=100$, $I_2=150$, $I_3=200$, $I_4=180$, $I_5=120$ m³/s. Find $O_5$.

**Solution:**
1. Compute coefficients:
   - $C_0 = (-6 \times 0.2 + 1.5)/(6 \times 0.8 + 1.5) = 0.3/6.3 = 0.0476$
   - $C_1 = (6 \times 0.2 + 1.5)/6.3 = 2.7/6.3 = 0.4286$
   - $C_2 = 1 - 0.0476 - 0.4286 = 0.5238$
2. Assume $O_1 = I_1 = 100$ m³/s
3. $O_2 = 0.0476(150) + 0.4286(100) + 0.5238(100) = 7.14 + 42.86 + 52.38 = 102.38$ m³/s
4. $O_3 = 0.0476(200) + 0.4286(150) + 0.5238(102.38) = 9.52 + 64.29 + 53.63 = 127.44$ m³/s
5. $O_4 = 0.0476(180) + 0.4286(200) + 0.5238(127.44) = 8.57 + 85.72 + 66.75 = 161.04$ m³/s
6. $O_5 = 0.0476(120) + 0.4286(180) + 0.5238(161.04) = 5.71 + 77.15 + 84.35 = 167.21$ m³/s

### Example 3: Darcy's Law Application
**Problem:** Confined aquifer, $T = 0.01$ m²/s, pumping at $Q = 0.01$ m³/s. Observation wells at $r_1 = 10$ m ($h_1 = 95$ m) and $r_2 = 100$ m ($h_2 = 99$ m). Verify Thiem equation.

**Solution:**
1. $Q = 2\pi T(h_2 - h_1)/\ln(r_2/r_1)$
2. $Q = 2\pi(0.01)(99-95)/\ln(100/10) = 0.0628 \times 4 / 2.303 = 0.109$ m³/s
3. Given $Q = 0.01$ m³/s → check: actual drawdown differs from assumed
4. Solve for $K$: $K = Q\ln(r_2/r_1)/(2\pi b(h_2-h_1))$

---

## 🎤 Interview Q&A

### Q1: What is a unit hydrograph and what are its assumptions?
**A:** A unit hydrograph is the direct runoff hydrograph resulting from 1 unit (1 cm or 1 inch) of effective rainfall uniformly distributed over the catchment for a specified duration. Assumptions: (1) Linearity — runoff is proportional to rainfall depth, (2) Time-invariance — the catchment response is the same regardless of when rainfall occurs, (3) Uniform rainfall distribution over the catchment.

### Q2: How do you convert a UH of one duration to another?
**A:** Use the S-curve method. (1) Derive the S-curve by summing the original UH ordinates shifted by the original duration. (2) Shift the S-curve by the new duration. (3) The difference between the two S-curves, multiplied by the ratio of durations, gives the new UH. Alternatively, for simple scaling, use the assumption that peak discharge is inversely proportional to duration.

### Q3: Explain the Muskingum method and its parameters.
**A:** The Muskingum method routes flood waves through a channel reach using storage $S = K[XI + (1-X)O]$. $K$ is the travel time through the reach (hours), $X$ is a weighting factor (0–0.5) that accounts for the wedge-shaped storage during rising and falling limbs. $X = 0$ gives level-pool routing, $X = 0.5$ gives perfect translation. The routing equation $O_2 = C_0 I_2 + C_1 I_1 + C_2 O_1$ is computationally efficient.

### Q4: What is the difference between return period and risk?
**A:** Return period $T$ is the average interval between events of a given magnitude: $T = 1/P(X \geq x)$. Risk is the probability that the event will be exceeded at least once in $n$ years: $R = 1 - (1 - 1/T)^n$. For example, a 100-year flood has $T = 100$, and the risk of occurrence in 50 years is $R = 1 - (0.99)^{50} = 39.5\%$.

### Q5: Compare Muskingum routing with level-pool routing.
**A:** Muskingum routing is for channel reaches (prism + wedge storage), uses $K$ and $X$, and can handle translatory waves. Level-pool routing is for reservoirs (level water surface), uses storage-indication method, and assumes horizontal water surface. Muskingum is more general; level-pool is simpler for reservoir operations.

### Q6: What is the Theis equation and when is it applicable?
**A:** The Theis equation $s = (Q/4\pi T)W(u)$ describes unsteady radial flow to a well in a confined aquifer. Assumptions: (1) infinite, homogeneous, isotropic aquifer, (2) fully penetrating well, (3) instantaneous release of water from storage, (4) constant pumping rate. The Cooper-Jacob simplification applies when $u < 0.01$ (large time or small distance).

---

## Quick Reference Formulas

| Formula | Equation | Use |
|---------|----------|-----|
| Darcy's Law | $Q = KiA$ | Groundwater flow |
| Thiem (steady) | $Q = 2\pi T(h_2-h_1)/\ln(r_2/r_1)$ | Confined aquifer properties |
| Theis (unsteady) | $s = (Q/4\pi T)W(u)$ | Transient drawdown |
| Muskingum | $O_2 = C_0I_2 + C_1I_1 + C_2O_1$ | Channel routing |
| Gumbel | $x_T = \bar{x} + K\sigma$ | Flood frequency |
| Horton | $f = f_c + (f_0-f_c)e^{-kt}$ | Infiltration |

---

## References

* [Civil_Placement_IITK](https://github.com/DKS-MANAGER/Civil_Placement_IITK)
* [awesome-civil-engineering](https://github.com/awesome-civil-engineering/awesome-civil-engineering)
* [`../open_channel_flow/open-channel-flow.md`](../open_channel_flow/open-channel-flow.md) — Open channel hydraulics
* [`../water_resources/water-resources-engineering.md`](../water_resources/water-resources-engineering.md) — Reservoir design
