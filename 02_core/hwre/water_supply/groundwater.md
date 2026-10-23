# Groundwater Engineering

## Introduction

Groundwater is water stored beneath the Earth's surface in pore spaces and fractures of rock and soil. It provides approximately 50% of global drinking water and is essential for agriculture and industry.

> **Related topics:** [`water-supply.md`](water-supply.md) · [`hydrology.md`](../hydrology/hydrology.md) · [`water-resources-engineering.md`](../water_resources/water-resources-engineering.md)

---

## Darcy's Law & Velocity Terminology

### Statement
The macroscopic discharge rate of fluid through a porous medium is directly proportional to the hydraulic gradient and cross-sectional area perpendicular to flow.

### Governing Relations: Darcy Velocity vs. Seepage Velocity
$$Q = -K \cdot A \cdot \frac{dh}{dl} = K \cdot i \cdot A$$

$$\text{Darcy Velocity (Specific Discharge / Superficial Velocity): } v = \frac{Q}{A} = K \cdot i$$

$$\text{Actual Pore Seepage Velocity (Interstitial Velocity): } v_s = \frac{v}{n} = \frac{K \cdot i}{n}$$

Where:
- $Q$ = discharge ($\text{m}^3\text{/s}$)
- $K$ = hydraulic conductivity (m/s)
- $i = -\frac{dh}{dl}$ = hydraulic gradient (dimensionless)
- $A$ = total gross cross-sectional area (soil grains + voids) ($\text{m}^2$)
- $A_v = n \cdot A$ = area of interconnected pore voids ($\text{m}^2$)
- $n$ = effective porosity ($0 < n < 1$; typically $0.25\text{--}0.45$)
- $v$ = Darcy flux / superficial velocity (m/s) — fictitious velocity assuming flow through entire cross section
- $v_s$ = true seepage velocity (m/s) — actual interstitial velocity of water moving through pore channels ($v_s > v$)

### Validity
- Valid for laminar flow in saturated media
- Applicable when Reynolds number $Re < 1\text{ to }10$
- $Re = \frac{\rho v d_{10}}{\mu}$ where $d_{10}$ = effective grain diameter

---

## Aquifer Properties

### Transmissivity ($T$)
$$T = K \cdot b$$
Where $b$ = saturated thickness (m). Units: m²/day or m²/s

### Storativity ($S$) / Storage Coefficient
Volume of water released from or taken into storage per unit surface area per unit change in head.

| Aquifer Type | Storativity | Typical Range |
|--------------|-------------|---------------|
| Confined | $S = \rho g b (\alpha + n\beta)$ | $10^{-5}$ to $10^{-3}$ |
| Unconfined | $S \approx S_y$ (specific yield) | 0.01 to 0.30 |

### Specific Yield ($S_y$) vs Specific Retention ($S_r$)
- $S_y$: Gravity-drained water released from storage (effective porosity)
- $S_r$: Water held against gravity (adsorbed + capillary water)
- $S_y + S_r = n$ (total porosity)

---

## Types of Aquifers

| Type | Upper Boundary | Recharge | Pressure |
|------|---------------|----------|----------|
| **Unconfined** | Water table (phreatic) | Direct through vadose zone | Atmospheric |
| **Confined** | Aquitard (low-K layer) | Leakage or distant recharge | Artesian (potentiometric > ground) |
| **Leaky (Semi-confined)** | Semi-permeable layer | Leakage through aquitard | Between confined/unconfined |

---

## Well Hydraulics

### Steady-State Flow

#### Thiem Equation (Confined Aquifer)
$$Q = \frac{2\pi T (h_2 - h_1)}{\ln(r_2/r_1)}$$

Where $h_1, h_2$ = piezometric heads at distances $r_1, r_2$

#### Dupuit-Forchheimer (Unconfined Aquifer)
$$Q = \frac{\pi K (h_2^2 - h_1^2)}{\ln(r_2/r_1)}$$

---

### Unsteady-State Flow (Theis Solution)

$$s = \frac{Q}{4\pi T} W(u)$$

Where:
- $s$ = drawdown (m)
- $W(u)$ = well function (exponential integral)
- $u = \frac{r^2 S}{4Tt}$

**Well function approximation:**
$$W(u) = -0.5772 - \ln u + u - \frac{u^2}{4} + \frac{u^3}{18} - \ldots$$

---

### Cooper-Jacob Approximation (Late Time, $u < 0.01$)

$$s = \frac{2.3Q}{4\pi T} \log\left(\frac{2.25Tt}{r^2 S}\right)$$

**Straight-line method:**
- Plot $s$ vs $\log t$ → straight line
- Slope = $2.3Q/(4\pi T)$ → gives $T$
- Intercept at $s=0$ → gives $S$

---

### Recovery Test (Theis Recovery)

$$s' = \frac{2.3Q}{4\pi T} \log\left(\frac{t}{t'}\right)$$

Where $t$ = time since pumping started, $t'$ = time since pumping stopped

---

## Pumping Test Analysis

### Step-Drawdown Test
$$s = BQ + CQ^2$$

Where:
- $B$ = aquifer loss coefficient (laminar)
- $C$ = well loss coefficient (turbulent)
- Well efficiency = $BQ/(BQ + CQ^2) \times 100\%$

### Specific Capacity
$$S_c = \frac{Q}{s}$$
- Indicator of aquifer productivity
- Declines with time due to aquifer dewatering

---

## Groundwater Flow Equations

### Confined Aquifer (2D)
$$\frac{\partial^2 h}{\partial x^2} + \frac{\partial^2 h}{\partial y^2} = \frac{S}{T} \frac{\partial h}{\partial t}$$

### Unconfined Aquifer (Boussinesq)
$$\frac{\partial}{\partial x}\left(Kh\frac{\partial h}{\partial x}\right) + \frac{\partial}{\partial y}\left(Kh\frac{\partial h}{\partial y}\right) = S_y \frac{\partial h}{\partial t}$$

---

## Groundwater Contamination & Transport

### Advection-Dispersion Equation
$$\frac{\partial C}{\partial t} = D_L \frac{\partial^2 C}{\partial x^2} - v \frac{\partial C}{\partial x} - \lambda C$$

Where:
- $D_L$ = longitudinal dispersivity (m²/s)
- $v$ = seepage velocity (m/s)
- $\lambda$ = decay constant

### Retardation Factor
$$R = 1 + \frac{\rho_b K_d}{n}$$

Where $K_d$ = distribution coefficient, $\rho_b$ = bulk density

---

## Worked Examples

### Example 1: Theis Solution
**Problem:** Pumping well at $Q = 0.01$ m³/s in confined aquifer. $T = 0.001$ m²/s, $S = 0.0001$. Find drawdown at $r = 50$ m after $t = 1$ day.

**Solution:**
1. $u = r^2 S / (4Tt) = 50^2 \times 0.0001 / (4 \times 0.001 \times 86400) = 0.00723$
2. $W(u) \approx -0.5772 - \ln(0.00723) = -0.5772 + 4.93 = 4.35$
3. $s = (0.01 / (4\pi \times 0.001)) \times 4.35 = 0.796 \times 4.35 = 3.46$ m

### Example 2: Cooper-Jacob Straight-Line Analysis
**Problem:** Pumping test data: $Q = 0.02$ m³/s, observation distance $r = 100$ m. Drawdown at $t = 1000$ min is $2.5$ m, at $t = 10000$ min is $3.2$ m. Find $T$ and $S$.

**Solution:**
1. Drawdown difference per log cycle of time:
   $$\Delta s = 3.2 - 2.5 = 0.70\text{ m/log cycle}$$
2. Transmissivity $T$:
   $$T = \frac{2.303 Q}{4\pi \, \Delta s} = \frac{2.303 \times 0.02}{4\pi \times 0.70} = \frac{0.04606}{8.796} = \mathbf{0.00523\text{ m}^2\text{/s}}$$
3. Zero-drawdown intercept time $t_0$:
   $$s = \Delta s \cdot \log_{10}\left(\frac{t}{t_0}\right) \implies 2.5 = 0.70 \cdot \log_{10}\left(\frac{1000}{t_0}\right)$$
   $$\log_{10}\left(\frac{1000}{t_0}\right) = \frac{2.5}{0.70} = 3.571 \implies \frac{1000}{t_0} = 3727.6 \implies t_0 = 0.2683\text{ min}$$
4. Storativity $S$ (converting $t_0$ to seconds: $t_0 = 0.2683 \times 60 = 16.10\text{ s}$):
   $$S = \frac{2.25 T t_0}{r^2} = \frac{2.25 \times 0.00523 \times 16.10}{100^2} = \frac{0.1894}{10000} = \mathbf{1.89 \times 10^{-5}}$$
   *(Note: Forgetting to convert $t_0$ from minutes to seconds is a severe error that underestimates $S$ by a factor of 60).*

### Example 3: Thiem Equation
**Problem:** Confined aquifer, $T = 0.005$ m²/s. Observation wells at $r_1 = 10$ m ($h_1 = 95$ m) and $r_2 = 100$ m ($h_2 = 99$ m). Find $Q$.

**Solution:**
1. $Q = 2\pi T (h_2 - h_1) / \ln(r_2/r_1)$
2. $Q = 2\pi \times 0.005 \times (99 - 95) / \ln(100/10)$
3. $Q = 0.1257 / 2.303 = 0.0546$ m³/s = 54.6 L/s

### Example 4: Unconfined Aquifer (Dupuit)
**Problem:** Unconfined aquifer, $K = 0.0001$ m/s. Observation wells at $r_1 = 20$ m ($h_1 = 15$ m) and $r_2 = 200$ m ($h_2 = 20$ m). Find $Q$.

**Solution:**
1. $Q = \pi K (h_2^2 - h_1^2) / \ln(r_2/r_1)$
2. $Q = \pi \times 0.0001 \times (400 - 225) / \ln(10)$
3. $Q = 0.000314 \times 175 / 2.303 = 0.0238$ m³/s = 23.8 L/s

### Example 5: Well Efficiency
**Problem:** Step-drawdown test: $Q_1 = 10$ L/s, $s_1 = 2$ m; $Q_2 = 20$ L/s, $s_2 = 5$ m. Find well efficiency at $Q_2$.

**Solution:**
1. $s = BQ + CQ^2$
2. $2 = 10B + 100C$
3. $5 = 20B + 400C$
4. Solving: $B = 0.15$, $C = 0.005$
5. At $Q_2 = 20$: Aquifer loss = $0.15 \times 20 = 3$ m, Well loss = $0.005 \times 400 = 2$ m
6. Efficiency = $3/(3+2) \times 100\% = 60\%$

---

## 🎤 Interview Q&A

### Q1: What is the difference between confined and unconfined aquifers?
**A:** Confined: bounded by aquitards, under artesian pressure, storativity $10^{-5}$–$10^{-3}$, Theis equation applies. Unconfined: water table is upper boundary, storativity ≈ specific yield (0.01–0.30), Dupuit-Forchheimer equation applies. Confined aquifers have much smaller storativity, so drawdown propagates faster.

### Q2: Explain the Theis equation and its assumptions.
**A:** Theis equation $s = (Q/4\pi T)W(u)$ describes transient drawdown in a confined aquifer. Assumptions: (1) infinite, homogeneous, isotropic aquifer, (2) fully penetrating well, (3) instantaneous release from storage, (4) constant pumping rate, (5) no recharge. $W(u)$ is the well function, $u = r^2S/4Tt$.

### Q3: When do you use Cooper-Jacob vs Theis?
**A:** Cooper-Jacob is an approximation of Theis for $u < 0.01$ (large time or small distance). It gives a straight-line plot of $s$ vs $\log t$, making it easier to determine $T$ and $S$ from field data. Use Theis for early time data or when $u > 0.01$.

### Q4: What is well efficiency and how do you determine it?
**A:** Well efficiency = aquifer loss / total drawdown = $BQ/(BQ + CQ^2)$. Determined from step-drawdown test: plot $s/Q$ vs $Q$, slope = $C$, intercept = $B$. Efficiency typically 60–80% for well-designed wells. Low efficiency indicates well losses (turbulent flow near screen).

### Q5: How does groundwater contamination transport differ from surface water?
**A:** Groundwater: advection + dispersion + diffusion + adsorption + decay. Much slower (m/day vs m/s), longer residence times, harder to remediate. Retardation factor $R = 1 + \rho_b K_d/n$ slows contaminant velocity. Pump-and-treat is common but slow; in-situ methods (bioremediation, PRBs) increasingly used.

---

## Quick Reference

| Formula | Equation |
|---------|----------|
| Darcy's Law | $Q = KiA$ |
| Transmissivity | $T = Kb$ |
| Theis | $s = (Q/4\pi T)W(u)$ |
| Cooper-Jacob | $s = (2.3Q/4\pi T)\log(2.25Tt/r^2S)$ |
| Thiem (confined) | $Q = 2\pi T(h_2-h_1)/\ln(r_2/r_1)$ |
| Dupuit (unconfined) | $Q = \pi K(h_2^2-h_1^2)/\ln(r_2/r_1)$ |
| Recovery | $s' = (2.3Q/4\pi T)\log(t/t')$ |
| Step-drawdown | $s = BQ + CQ^2$ |
| Well efficiency | $\eta = BQ/(BQ+CQ^2)$ |
| Specific capacity | $S_c = Q/s$ |

---

## 🗺️ Subject Roadmap

```
Beginner                    Intermediate                   Advanced                      Interview
─────────────────────────────────────────────────────────────────────────────────────────────────────
Darcy's law           →  Aquifer properties (T,S,Sy) →  MODFLOW modeling             →  When Darcy's law fails
Confined vs unconfined→  Theis/Cooper-Jacob analysis  →  Contaminant transport        →  Theis vs Cooper-Jacob
Well basics           →  Pumping test interpretation  →  Managed aquifer recharge     →  Step-drawdown test
Groundwater flow      →  Flow nets,Dupuit            →  Saltwater intrusion models   →  Well efficiency calculation
```

> **Priority:** `P0 — Must Know` · **Tags:** `HWRE` `CORE CIVIL`

---

## ❓ Question Bank (Selected)

### A. Basic Concept
1. What is Darcy's law and when is it valid?
2. What is the difference between transmissivity and storativity?
3. What are confined and unconfined aquifers?

### B. WHY Questions
1. **Why** does storativity differ so much between confined and unconfined aquifers?
   - Confined: water released by compression of aquifer and expansion of water ($S \sim 10^{-5}$). Unconfined: water drains by gravity ($S_y \sim 0.01-0.30$).

2. **Why** is the Cooper-Jacob plot linear?
   - Because the well function approximation $W(u) \approx -0.5772 - \ln(u)$ makes $s$ proportional to $\log(t)$, giving a straight line on semi-log paper.

3. **Why** does well efficiency decrease with pumping rate?
   - Higher Q → higher velocity near well → turbulent losses ($CQ^2$ term) → increased drawdown beyond Darcy prediction.

---

## 🎤 Interview Answer Format

### High-Value Q: "How do you interpret a pumping test?"

**30-second answer:**
"Plot drawdown vs log-time on semi-log paper. For confined aquifers, the Cooper-Jacob straight line gives: slope = $2.3Q/(4\pi T)$ for transmissivity, and $T = 2.3Q/(4\pi \times \text{slope})$. The intercept at zero drawdown gives $S = 2.25Tt_0/r^2$."

---

## 🔗 Cross-Links

- [`hydrology.md`](../hydrology/hydrology.md) — Groundwater hydrology overview
- [`water-resources-engineering.md`](../water_resources/water-resources-engineering.md) — Well hydraulics
- [`water-supply.md`](water-supply.md) — Water supply from groundwater

---

## References

* [awesome-civil-engineering](https://github.com/awesome-civil-engineering/awesome-civil-engineering)