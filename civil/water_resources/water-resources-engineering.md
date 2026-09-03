# Water Resources Engineering

## Scope

Water resources engineering encompasses the planning, development, distribution, and management of water for human and environmental needs. It integrates hydrology, hydraulics, groundwater, and irrigation into systems-level design.

> **Related topics:** [`hydrology.md`](../hydrology/hydrology.md) · [`open-channel-flow.md`](../open_channel_flow/open-channel-flow.md) · [`../hwre/irrigation/irrigation-engineering.md`](../../hwre/irrigation/irrigation-engineering.md) · [`../hwre/water_supply/water-supply.md`](../../hwre/water_supply/water-supply.md)

---

## Surface Water Systems

### Reservoir Design

**Storage capacity determination:**
- Mass curve (Rippl curve): Cumulative inflow vs time
- Maximum demand line drawn from mass curve
- Vertical difference = required storage

**Yield estimation:**
- **Firm yield:** Minimum dependable flow (usually at 75–95% dependability)
- **Secondary yield:** Additional water available during average years
- **Design flood:** Probable Maximum Flood (PMF) for dam safety

**Sedimentation:**
- Trap efficiency: $TE = 1 - 1/(1 + 0.0003 \cdot Cap/Y)$ (Brune's curve)
- Dead storage = sediment volume over design life
- Useful life: when live storage is depleted by sediment

**Reservoir operation rules:**
- Conservation rule curve: Guide storage allocation across seasons
- Flood control pool: Empty space for flood absorption
- Multi-purpose optimization: Irrigation + hydropower + flood control + environmental flows

### Canal Distribution Systems

**Canal classification:**

| Type | Purpose | Typical Capacity |
|------|---------|-----------------|
| Main canal | Headworks to distributaries | > 50 m³/s |
| Branch canal | Offtakes from main | 10–50 m³/s |
| Distributary | Area service | 2–10 m³/s |
| Minors | Field supply | 0.1–2 m³/s |
| Watercourses | Final delivery | < 0.1 m³/s |

**Lining comparison:**

| Parameter | Unlined | Concrete Lined | Brick Lined |
|-----------|---------|---------------|-------------|
| Seepage loss | High (30–50%) | Low (5–10%) | Medium (15–25%) |
| Cost | Low | High | Medium |
| Maintenance | High | Low | Medium |
| Velocity | Limited | Higher | Medium |

**Design velocity (Lacey's regime):**
$$V = \left(\frac{Q f^2}{140}\right)^{1/6}$$

**Wetted perimeter (Lacey):**
$$P = 2.67\sqrt{Q}$$

**Normal depth (Manning):**
$$Q = \frac{1}{n} A R^{2/3} S^{1/2}$$

### Stage-Discharge Relationships

**Rating curve:** $Q = C(H - a)^b$
- $H$ = gauge height, $a$ = gauge zero correction
- $C$, $b$ = empirical constants from current-meter measurements

**Afflux at bridges:**
$$h_2 - h_1 = \frac{V_2^2 - V_1^2}{2g} + h_f$$

---

## Groundwater Systems

### Aquifer Properties

| Type | Conditions | Properties |
|------|-----------|------------|
| Confined | Piezometric surface above top | $T = Kb$, storativity $S$ (10⁻⁵–10⁻³) |
| Unconfined | Water table = phreatic surface | $T = Kb$, specific yield $S_y$ (0.01–0.40) |
| Leaky | Semi-confining layer | Leakance $K'/b'$ |

### Well Hydraulics — Key Equations

**Thiem (steady, confined):**
$$Q = \frac{2\pi T(h_2 - h_1)}{\ln(r_2/r_1)}$$

**Theis (unsteady, confined):**
$$s = \frac{Q}{4\pi T} W(u), \quad u = \frac{r^2 S}{4Tt}$$

**Cooper-Jacob ($u < 0.01$):**
$$s = \frac{2.3Q}{4\pi T}\log\left(\frac{2.25Tt}{r^2S}\right)$$

**Dupuit (unsteady, unconfined):**
$$h_1^2 - h_2^2 = \frac{Q}{\pi K}\ln\frac{r_2}{r_1}$$

### Groundwater Contamination

**Advection-dispersion equation:**
$$\frac{\partial C}{\partial t} = D_L\frac{\partial^2 C}{\partial x^2} - v\frac{\partial C}{\partial x}$$

Where $D_L$ = longitudinal dispersity, $v$ = seepage velocity

---

## Integrated Water Resources Management (IWRM)

### System Optimization
- **Linear programming:** Reservoir operation, water allocation
- **Dynamic programming:** Sequential decision-making under uncertainty
- **Simulation-optimization:** Combine physical models with optimization algorithms
- **Multi-objective trade-offs:** Pareto frontiers for competing demands

### Climate Adaptation
- Changing precipitation patterns and extreme event frequency
- Drought planning and water allocation during scarcity
- Demand management and water conservation strategies
- Green infrastructure and sustainable urban drainage

---

## Decision Support Tools

| Software | Application |
|----------|-------------|
| HEC-HMS | Hydrologic modeling for watershed runoff |
| HEC-RAS | River hydraulic modeling, dam breach, bridge scour |
| MODFLOW 6 | Regional and local groundwater flow simulation |
| InfoWorks ICM | Integrated catchment modeling |
| MIKE FLOOD | 1D/2D coupled flood modeling |
| WaterGEMS | Water distribution network design |
| EPANET | Pipe network analysis and water quality |
| SWMM | Stormwater management |

---

## Infrastructure Assessment

### Dam Safety
- Hazard potential classification (High, Significant, Low)
- Inflow design flood: PMF for high-hazard dams
- Breach wave analysis: dam-break flood routing downstream
- Emergency action planning: warning systems, evacuation routes

### River Basin Planning
- Water balance at basin scale: Precipitation = Evaporation + Runoff + Storage change
- Inter-basin transfer feasibility: cost-benefit, environmental impact
- Environmental flow requirements: minimum flow for ecosystem health

---

## Worked Examples

### Example 1: Reservoir Storage (Mass Curve)
**Problem:** Monthly inflows (m³/s): 50, 80, 120, 90, 60, 40, 30, 35, 45, 70, 100, 80. Demand = 65 m³/s. Find required storage.

**Solution:**
1. Compute cumulative inflow and cumulative demand
2. Plot mass curve (cumulative inflow vs time)
3. Draw demand line from peak of mass curve with slope = 65 m³/s
4. Maximum vertical departure = required storage
5. Result: ~3 months of deficit at 65 m³/s → storage ≈ 3 × 30 × 86400 × (65-40) = ~65 Mm³

### Example 2: Canal Design (Manning)
**Problem:** Design a trapezoidal canal for $Q = 15$ m³/s, $S = 0.0005$, $n = 0.022$, $z = 1.5$.

**Solution:**
1. Most efficient section: $A/P = R = y/2$ for trapezoidal
2. $b = 2y(\sqrt{1+z^2} - z) = 2y(\sqrt{3.25} - 1.5) = 0.606y$
3. $A = (b+zy)y = (0.606y+1.5y)y = 2.106y^2$
4. $P = b+2y\sqrt{1+z^2} = 0.606y+3.606y = 4.212y$
5. $R = A/P = 0.5y$
6. Manning: $15 = (1/0.022)(2.106y^2)(0.5y)^{2/3}(0.0005)^{1/2}$
7. $15 = 45.45 \times 2.106y^2 \times 0.63y^{2/3} \times 0.0224$
8. $15 = 1.352 y^{8/3}$
9. $y^{8/3} = 11.09$ → $y = 2.44$ m → $b = 1.48$ m

---

## 🎤 Interview Q&A

### Q1: How do you determine reservoir storage capacity?
**A:** (1) Plot mass curve (cumulative inflow vs time). (2) Draw maximum demand line from peak. (3) Maximum vertical departure = required storage. For flood control, use routing (level-pool method) with design inflow hydrograph to determine required flood pool.

### Q2: What is the difference between firm yield and secondary yield?
**A:** Firm yield: minimum dependable water supply, available in 95% of years (conservative). Secondary yield: additional water available in average/good years, not guaranteed. Firm yield determines reservoir size for water supply; secondary yield is bonus for hydropower or irrigation in wet years.

### Q3: Explain the Theis equation and its practical use.
**A:** Theis equation describes transient drawdown in a confined aquifer due to pumping. $s = (Q/4\pi T)W(u)$ where $W(u)$ is the well function. Practical use: (1) Determine aquifer properties $T$ and $S$ from pumping test data, (2) Predict drawdown at observation wells, (3) Design well spacing to prevent interference. The Cooper-Jacob simplification is used for large time/small distance.

### Q4: What are environmental flows and why are they important?
**A:** Environmental flows (E-flows) are the minimum flow regimes needed to sustain riverine ecosystems. They include: baseflow for aquatic habitat, flood pulses for sediment transport and floodplain connectivity, seasonal flow patterns for fish spawning. E-flows are determined through hydrological, hydraulic, or holistic methods and are critical for sustainable water resource management.

---

## Quick Reference Formulas

| Formula | Equation | Use |
|---------|----------|-----|
| Manning | $Q = (1/n)AR^{2/3}S^{1/2}$ | Channel flow |
| Lacey | $V = (Qf^2/140)^{1/6}$ | Regime channel design |
| Thiem | $Q = 2\pi T(h_2-h_1)/\ln(r_2/r_1)$ | Steady well flow |
| Theis | $s = (Q/4\pi T)W(u)$ | Transient well flow |
| Dupuit | $h_1^2-h_2^2 = Q\ln(r_2/r_1)/(\pi K)$ | Unconfined flow |
| Brune trap eff. | $TE = 1-1/(1+0.0003\cdot Cap/Y)$ | Reservoir sedimentation |
| Rating curve | $Q = C(H-a)^b$ | Stage-discharge |

---

## References

* [Civil_Placement_IITK](https://github.com/DKS-MANAGER/Civil_Placement_IITK)
* [awesome-civil-engineering](https://github.com/awesome-civil-engineering/awesome-civil-engineering)
* [GATE_Civil_Study_Material_2027](https://github.com/DKS-MANAGER/GATE_Civil_Study_Material_2027)
