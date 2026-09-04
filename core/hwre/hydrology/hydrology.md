# Hydrology

## Hydrologic Cycle

The hydrologic cycle describes the continuous movement of water on, above, and below the Earth's surface.

> **Related topics:** [`open-channel-flow.md`](../open_channel_flow/open-channel-flow.md) · [`sediment-transport.md`](sediment-transport.md) · [`water-resources-engineering.md`](../water_resources/water-resources-engineering.md) · [`flood-control.md`](../flood_control/flood-control.md)

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

## 🗺️ Subject Roadmap

```
Beginner                    Intermediate                   Advanced                      Interview
─────────────────────────────────────────────────────────────────────────────────────────────────────
Hydrologic cycle      →  Rainfall-runoff models     →  Probable Maximum Flood       →  Unit hydrograph assumptions
Precipitation         →  Unit hydrograph analysis    →  Real-time flood forecasting  →  Why return period ≠ risk
Infiltration (Horton) →  Flood frequency analysis    →  Climate change impacts       →  Muskingum K and X meaning
Runoff coefficient    →  Muskingum routing           →  Groundwater-surface coupling  →  Theis vs Cooper-Jacob
Groundwater basics    →  Theis/Cooper-Jacob          →  MODFLOW modeling              →  Darcy's law validity
Return period         →  Level-pool routing          →  Stochastic hydrology         →  Risk vs reliability
```

> **Priority:** `P0 — Must Know` · **Tags:** `CORE CIVIL` `HWRE`

---

## 📋 Formula Sheet

<details>
<summary><strong>Click to expand — Complete Hydrology Formula Sheet</strong></summary>

| Formula | Equation | Variables | Units | Conditions | Interview Importance |
|---------|----------|-----------|-------|------------|---------------------|
| Rainfall excess | $P_{eff} = P - I_a - F$ | $P$=rainfall, $I_a$=initial abstraction, $F$=infiltration | mm | Before runoff | ⭐⭐ |
| Rational Method | $Q_p = CiA$ | $C$=runoff coeff, $i$=intensity, $A$=area | m³/s | Small catchments <200 km² | ⭐⭐⭐ |
| SCS-CN | $Q = (P-0.2S)^2/(P+0.8S)$, $S = 25400/CN - 254$ | $CN$=curve number | mm | Watershed runoff | ⭐⭐⭐ |
| Horton | $f(t) = f_c + (f_0-f_c)e^{-kt}$ | $f_0$=initial, $f_c$=final, $k$=decay | mm/hr | Infiltration | ⭐⭐ |
| Unit Hydrograph | $DRH = UH \times P_{eff}$ | $UH$=unit hydrograph, $P_{eff}$=excess rainfall | m³/s | Linear response | ⭐⭐⭐ |
| Snyder's UH | $t_p = C_t(L\cdot L_c)^{0.3}$, $Q_p = 640C_pA/t_p$ | $C_t$,$C_p$=coefficients | hr, m³/s | Ungauged catchments | ⭐⭐ |
| Muskingum | $O_2 = C_0I_2 + C_1I_1 + C_2O_1$ | $K$=travel time, $X$=weighting (0–0.5) | m³/s | Channel routing | ⭐⭐⭐ |
| Level Pool | $2S/\Delta t + O = 2I + (2S/\Delta t - O)_{prev}$ | — | m³/s | Reservoir routing | ⭐⭐⭐ |
| Gumbel | $x_T = \bar{x} + (\sigma/\sigma_n)[0.7797y_T - 0.45005y_T + ...]$ | $y_T = -\ln(-\ln(1-1/T))$ | m³/s | Flood frequency | ⭐⭐ |
| Log-Pearson III | $\log x_T = \overline{\log x} + K_T \sigma_{\log x}$ | $K_T$=frequency factor | m³/s | Flood frequency (US standard) | ⭐⭐ |
| Darcy's Law | $Q = KiA$ | $K$=conductivity, $i$=gradient | m³/s | Groundwater flow | ⭐⭐⭐ |
| Theis | $s = (Q/4\pi T)W(u)$, $u = r^2S/4Tt$ | $W(u)$=well function | m | Transient well flow (confined) | ⭐⭐⭐ |
| Cooper-Jacob | $s = (2.3Q/4\pi T)\log(2.25Tt/r^2S)$ | Same as Theis | m | $u < 0.01$ | ⭐⭐⭐ |
| Thiem | $Q = 2\pi T(h_2-h_1)/\ln(r_2/r_1)$ | $T$=transmissivity | m³/s | Steady well flow (confined) | ⭐⭐ |
| Risk | $R = 1-(1-1/T)^n$ | $T$=return period, $n$=years | — | Probability of exceedance | ⭐⭐⭐ |

**Commonly Confused Pairs:**
- **Return Period vs Risk:** Return period = average interval ($T=1/P$); Risk = probability of exceedance in $n$ years ($R=1-(1-1/T)^n$)
- **Muskingum K vs X:** $K$ = travel time through reach (hours); $X$ = wedge storage weight (0 = level pool, 0.5 = pure translation)
- **Unit Hydrograph vs S-Hydrograph:** UH = response to 1 unit of excess rain; S-curve = response to continuous unit rainfall intensity
- **Theis vs Cooper-Jacob:** Theis is exact (implicit integral); Cooper-Jacob is approximation valid for $u < 0.01$ (large time)
- **Confined vs Unconfined aquifer:** Confined = piezometric surface above top; Unconfined = water table = phreatic surface

</details>

---

## ❓ Question Bank

### A. Basic Concept Questions

1. What is a unit hydrograph? State its two key assumptions.
2. What is the difference between return period and risk?
3. Explain the Muskingum routing method. What do $K$ and $X$ represent?
4. What is Darcy's law and when is it valid?
5. What is the difference between the Theis and Cooper-Jacob equations?
6. What is the SCS-CN method?
7. What are the differences between confined and unconfined aquifers?
8. What is the Gumbel distribution used for in hydrology?
9. Explain the level-pool routing method.
10. What is the S-curve method used for?

### B. WHY Questions

1. **Why** is the unit hydrograph assumption of linearity valid for moderate rainfall events?
   - Because for moderate events, the catchment response (infiltration, storage, routing) is approximately proportional to input. For extreme events, nonlinear effects (saturated areas, overbank flow) break this assumption.

2. **Why** does Muskingum routing use both prism and wedge storage?
   - During the rising limb, wedge storage (additional volume above prism) exists because inflow > outflow. During the falling limb, wedge storage is negative. $X$ weights the relative importance of these storage components.

3. **Why** is the Cooper-Jacob approximation valid only for small $u$?
   - Because the approximation drops higher-order terms in the expansion of the well function $W(u)$, which are negligible when $u < 0.01$ (typically late time or near well).

4. **Why** does flood frequency analysis use logarithmic transformations?
   - Because flood data is typically positively skewed (log-normal or log-Pearson Type III distribution). Log transformation normalizes the distribution and stabilizes variance.

5. **Why** does increasing impervious area increase peak discharge?
   - Impervious surfaces reduce infiltration, increase runoff volume, reduce time of concentration, and increase peak discharge (higher $C$ in Rational Method, higher $CN$ in SCS-CN).

### C. WHAT-IF Questions

1. **What happens** if return period increases from 50 years to 100 years?
   - Design flood magnitude increases (typically 10–30%), but risk per year decreases from 2% to 1%. Risk over 50 years: 64% vs 39.5%.

2. **What happens** if Muskingum $X = 0$?
   - Level-pool routing (reservoir). Storage depends only on outflow. Prism storage only, no wedge.

3. **What happens** if aquifer storativity increases?
   - Drawdown spreads more slowly; Theis curve shows slower response; Cooper-Jacob plot has flatter slope for $T$.

4. **What happens** if rainfall intensity doubles but duration halves (same total depth)?
   - Peak discharge increases (higher intensity), but total volume is similar. Time of concentration may decrease.

5. **What happens** if the well is not fully penetrating?
   - Actual drawdown > Theis prediction (partial penetration increases flow resistance). Need correction factors or 3D models.

### D. Comparison Questions

| Concept A | Concept B | Key Difference | Application |
|-----------|-----------|----------------|-------------|
| Muskingum | Level-pool | Channel reach vs reservoir; prism+wedge vs prism only | Routing |
| Theis | Cooper-Jacob | Exact (implicit) vs approximation ($u<0.01$) | Aquifer testing |
| Gumbel | Log-Pearson III | GEV vs log-normal skew | Flood frequency |
| Return period | Risk | $T = 1/P$ vs $R = 1-(1-1/T)^n$ | Design & probability |
| Confined | Unconfined | $S \ll S_y$; piezometric vs water table | Well design |
| Horton | Green-Ampt | Empirical decay vs physics-based | Infiltration modeling |
| Unit hydrograph | S-curve | Single event vs continuous response | Duration conversion |
| Steady state | Transient | $ds/dt = 0$ vs $ds/dt \neq 0$ | Well testing |

### E. Numerical Questions

**Easy:**
**Problem:** A 100 km² catchment has CN=75. Find runoff for P=80mm.
- **Given:** $CN=75$, $P=80$ mm
- **Find:** $Q$
- **Approach:** SCS-CN: $S = 25400/75 - 254 = 74.67$ mm, $I_a = 0.2S = 14.93$ mm
- **Solution:** $Q = (80-14.93)^2/(80+0.8\times74.67) = 65.07^2/139.74 = 30.3$ mm
- **Final Answer:** $Q = 30.3$ mm
- **Concept Tested:** SCS-CN method
- **Common Trap:** Forgetting $I_a = 0.2S$

**Medium:**
**Problem:** Muskingum routing: $K=8$h, $X=0.25$, $\Delta t=4$h. Inflow: 50, 120, 200, 180, 100 m³/s at 4-hr intervals. Find peak outflow.
- **Given:** $K=8$, $X=0.25$, $\Delta t=4$
- **Find:** Peak outflow
- **Approach:** Compute $C_0, C_1, C_2$, iterate
- **Solution:**
  - $C_0 = (-8\times0.25+2)/(8\times0.75+2) = 0/8 = 0$
  - $C_1 = (8\times0.25+2)/8 = 4/8 = 0.5$
  - $C_2 = 1-0-0.5 = 0.5$
  - $O_1=50$, $O_2=0.5(120)+0.5(50)=85$, $O_3=0.5(200)+0.5(85)=142.5$, $O_4=0.5(180)+0.5(142.5)=161.25$, $O_5=0.5(100)+0.5(161.25)=130.6$
- **Final Answer:** Peak outflow $\approx 161$ m³/s (attenuated from 200 m³/s inflow peak)
- **Concept Tested:** Muskingum routing
- **Common Trap:** $C_0=0$ when $0.5\Delta t = KX$

**Hard:**
**Problem:** Confined aquifer pumping test: Q=0.02 m³/s. Drawdown data: at r=30m, s=2.1m after 100min; s=3.8m after 400min. Find T and S.
- **Given:** $Q=0.02$ m³/s, $r=30$ m, $s_1=2.1$m at $t_1=100$min, $s_2=3.8$m at $t_2=400$min
- **Find:** $T$, $S$
- **Approach:** Cooper-Jacob: $\Delta s = 2.3Q/(4\pi T)$; $S = 2.25Tt_0/r^2$
- **Solution:**
  - $\Delta s = s_2 - s_1 = 1.7$ m, $\Delta\log t = \log(400/100) = 0.602$
  - Slope $= 1.7/0.602 = 2.824$ m/cycle
  - $T = 2.3Q/(4\pi \times 2.824) = 0.046/(35.49) = 0.0013$ m²/s
  - Extrapolate to $s=0$: $t_0 = 100 \times 10^{(-2.1/2.824)} = 100 \times 10^{-0.744} = 18.0$ min = 1080 s
  - $S = 2.25 \times 0.0013 \times 1080/30^2 = 3.159 \times 10^{-3}/900 = 0.0000035$
- **Final Answer:** $T \approx 0.0013$ m²/s, $S \approx 3.5 \times 10^{-6}$
- **Concept Tested:** Cooper-Jacob analysis
- **Common Trap:** Unit conversion (minutes to seconds)

### F. Rapid-Fire Questions (30+)

Q: What is the hydrologic cycle?
A: Continuous movement of water: evaporation → condensation → precipitation → runoff/infiltration → evaporation.

Q: What is time of concentration ($t_c$)?
A: Time for water to travel from the most hydraulically distant point to the catchment outlet.

Q: What is lag time?
A: Delay between centroid of rainfall excess and peak discharge; $t_L \approx 0.6t_c$.

Q: What is the Rational Method?
A: $Q_p = CiA$; valid for small catchments (<200 km²), short-duration storms.

Q: What does CN=100 mean?
A: 100% runoff (impervious surface); no infiltration.

Q: What is the S-curve?
A: Hydrograph from continuous unit-intensity rainfall; sum of UH ordinates shifted by duration $D$.

Q: What is Snyder's method?
A: Empirical UH for ungauged catchments using basin length, area, and coefficients $C_t$, $C_p$.

Q: What is the Muskingum $K$?
A: Travel time of flood wave through a channel reach (hours).

Q: What is Muskingum $X$?
A: Weighting factor (0–0.5) for wedge storage; $X=0$ is level pool, $X=0.5$ is pure translation.

Q: What is the level-pool routing method?
A: Storage depends only on outflow (horizontal water surface); used for reservoirs.

Q: What is Darcy's law?
A: $Q = KiA$; discharge proportional to hydraulic conductivity and gradient; valid for laminar flow in porous media.

Q: What is transmissivity?
A: $T = Kb$; ability of the full aquifer thickness to transmit water; units: m²/s.

Q: What is storativity?
A: Volume of water released from storage per unit surface area per unit head change; confined: $10^{-5}$ to $10^{-3}$.

Q: What is specific yield?
A: Drainable porosity (unconfined aquifer); fraction of volume that drains by gravity; 0.01–0.40.

Q: What is the Theis well function $W(u)$?
A: $W(u) = \int_u^\infty e^{-x}/x \, dx$; describes transient drawdown in a confined aquifer.

Q: When is Cooper-Jacob valid?
A: When $u = r^2S/(4Tt) < 0.01$; typically at large time or small radial distance.

Q: What is the Thiem equation used for?
A: Steady-state analysis of confined aquifer pumping test; determines $T$ from two observation wells.

Q: What is a flood frequency curve?
A: Plot of discharge vs return period (often on log-probability paper); used for design flood selection.

Q: What is the 100-year flood?
A: Flood magnitude with 1% annual exceedance probability; NOT a guaranteed interval.

Q: What is the Gumbel distribution?
A: Extreme value distribution (Type I) used for annual maximum flood series.

Q: What is the probable maximum flood (PMF)?
A: Theoretically greatest flood for a catchment; used for dam safety design.

Q: What is baseflow separation?
A: Dividing a hydrograph into direct runoff and baseflow (groundwater contribution).

Q: What are the straight-line and variable-discharge methods?
A: Straight-line: connect start/end of direct runoff. Variable-discharge: baseflow decreases then increases (more realistic).

Q: What is the infiltration capacity?
A: Maximum rate at which soil can absorb water; decreases from initial rate to equilibrium.

Q: What is the Phi index?
A: Constant infiltration rate such that rainfall excess volume = actual runoff volume.

Q: What is a hydrograph?
A: Plot of discharge vs time at a point in a channel; shows response to a storm event.

Q: What is the peak discharge?
A: Maximum flow rate during a storm; depends on rainfall intensity, catchment area, and antecedent conditions.

Q: What is a recession curve?
A: Falling limb of hydrograph after peak; represents drainage of storage; $Q_t = Q_0 e^{-t/\tau}$.

Q: What is the constant for baseflow recession?
A: Typical $\tau$ = 10–30 days for groundwater recession; depends on aquifer properties.

Q: What is the Rational Method runoff coefficient $C$?
A: Fraction of rainfall that becomes runoff; depends on land use, soil, slope; 0.1 (forest) to 0.95 (asphalt).

Q: What is antecedent moisture condition (AMC)?
A: Soil moisture state before a storm; AMC-A (dry), AMC-B (average), AMC-C (wet); affects CN value.

### G. Deep Technical Questions (IITK M.Tech / PG Level)

1. **Derive the Muskingum routing coefficients from the storage equation.**
   - Start with $S = K[XI + (1-X)O]$, assume linear variation of $I$ and $O$ over $\Delta t$, integrate $\Delta S = \bar{I}\Delta t - \bar{O}\Delta t$, solve for $O_2$ in terms of $I_1$, $I_2$, $O_1$. Result: $C_0+C_1+C_2=1$.

2. **What are the limitations of the unit hydrograph concept?**
   - Linearity fails for extreme events (saturation, overbank flow). Time-invariance fails when antecedent conditions vary. Spatial uniformity assumption ignores storm movement. Not applicable to snowmelt-dominated catchments.

3. **How would you calibrate a distributed hydrologic model?**
   - Use split-sample testing (calibration period vs validation period). Objective functions: NSE, KGE, volume bias. Parameter estimation: GA, PSO, or Markov Chain Monte Carlo (MCMC). Validate against independent events and multiple catchments.

4. **Explain the physical basis of the Green-Ampt infiltration model.**
   - Based on Darcy's law with a sharp wetting front: $f = K(1 + \psi\Delta\theta/F)$. Assumes: piston-flow displacement, constant suction head $\psi$ at wetting front, uniform initial moisture. More physically realistic than Horton's empirical model.

5. **How does climate change affect flood frequency analysis?**
   - Non-stationarity violates the assumption of IID data. Need: trend analysis, non-stationary frequency models (time-varying parameters), regional frequency analysis, climate model downscaling (GCM → RCM → local).

6. **Compare the Muskingum-Cunge method with standard Muskingum.**
   - Muskingum-Cunge derives $K$ and $X$ from physical channel properties ($K = \Delta x/c$, $X = 0.5 - Q/(2cBT_0S_0)$) rather than calibration. It ensures numerical diffusion matches physical diffusion. More physically based but requires detailed channel geometry.

---

## 🎤 Interview Answer Format

### High-Value Q1: "What is a unit hydrograph?"

**30-second answer:**
"A unit hydrograph is the direct runoff hydrograph resulting from 1 unit of effective rainfall uniformly distributed over a catchment. It assumes linearity and time-invariance of the catchment response."

**If interviewer asks deeper:**
"The two key assumptions are: (1) linearity — if rainfall doubles, DRH ordinates double; (2) time-invariance — the response is the same regardless of when rainfall occurs. These assumptions break down for extreme events and varying antecedent conditions. The S-curve method converts UH of one duration to another."

**Key equation:**
$DRH = UH \times P_{eff}$

**Engineering interpretation:**
"Unit hydrographs are the basis for design storm hydrology. From a UH, we can compute the hydrograph for any rainfall event by superposition, which is essential for spillway design, flood plain mapping, and stormwater management."

---

### High-Value Q2: "Explain Muskingum routing."

**30-second answer:**
"Muskingum routing is a channel routing method that uses the storage equation $S = K[XI + (1-X)O]$, where $K$ is travel time and $X$ weights wedge storage. The routing equation $O_2 = C_0I_2 + C_1I_1 + C_2O_1$ is computationally efficient."

**If interviewer asks deeper:**
"$K$ has units of time and represents the average travel time of a flood wave through the reach. $X$ (0 to 0.5) represents the relative importance of inflow vs outflow on storage: $X=0$ gives level-pool (reservoir), $X=0.5$ gives pure translation with no attenuation. For natural channels, $X$ typically ranges from 0.1 to 0.3."

**Key equation:**
$O_2 = C_0I_2 + C_1I_1 + C_2O_1$, where $C_0+C_1+C_2=1$

**Engineering interpretation:**
"Muskingum routing predicts how a flood wave is attenuated and delayed as it travels downstream. This is critical for flood warning systems, dam operation, and designing channel capacity."

---

## 🔗 Interviewer Follow-up Chain

```
Q1: "What is a unit hydrograph?"
    ↓
Q2: "What are its assumptions and limitations?"
    ↓ (linearity, time-invariance; fails for extreme events)
Q3: "How do you convert a UH of one duration to another?"
    ↓ (S-curve method)
Q4: "How would you derive a UH from observed data?"
    ↓ (deconvolution, least squares, or transform methods)
Q5: "What if the catchment is ungauged?"
    ↓ (Snyder's method, regional UH, or CN-based approaches)
```

```
Q1: "What is Muskingum routing?"
    ↓
Q2: "What do K and X represent physically?"
    ↓ (travel time; wedge storage weight)
Q3: "What happens when X=0?"
    ↓ (level-pool routing; prism storage only)
Q4: "How do you determine K and X?"
    ↓ (trial-and-error fitting, or Muskingum-Cunge from physical properties)
Q5: "How does this differ from level-pool routing?"
    ↓ (channel vs reservoir; wedge storage vs horizontal surface)
```

---

## 🔗 Cross-Links

- [`open-channel-flow.md`](../open_channel_flow/open-channel-flow.md) — GVF, hydraulic jump
- [`water-resources-engineering.md`](../water_resources/water-resources-engineering.md) — Reservoir design, canal design
- [`flood-control.md`](../flood_control/flood-control.md) — Flood estimation, structural measures
- [`sediment-transport.md`](sediment-transport.md) — Sediment in rivers
- [`groundwater.md`](../water_supply/groundwater.md) — Detailed well hydraulics
- [`hydraulics.md`](../hydraulics/hydraulics.md) — Pipe flow fundamentals
- [`irrigation-engineering.md`](../irrigation/irrigation-engineering.md) — Crop water requirements

---

## References

* [awesome-civil-engineering](https://github.com/awesome-civil-engineering/awesome-civil-engineering)
* [`../open_channel_flow/open-channel-flow.md`](../open_channel_flow/open-channel-flow.md) — Open channel hydraulics
* [`../water_resources/water-resources-engineering.md`](../water_resources/water-resources-engineering.md) — Reservoir design
