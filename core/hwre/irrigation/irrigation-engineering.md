# Irrigation Engineering

## Scope

Irrigation engineering deals with the planning, design, and management of water supply systems for agricultural crops. It bridges hydrology, soil science, crop physiology, and water resources engineering.

> **Related topics:** [`water-resources-engineering.md`](../water_resources/water-resources-engineering.md) · [`groundwater.md`](../water_supply/groundwater.md) · [`flood-control.md`](../flood_control/flood-control.md)

---

## Crop Water Requirements

### Consumptive Use
- Consumptive use ($C_u$): Water used by vegetation through transpiration and evaporation from soil
- Penman equation for reference crop evapotranspiration ($ET_0$)
- **Crop coefficients ($K_c$):** $ET_c = K_c \times ET_0$

### Water Requirements

| Requirement | Formula | Description |
|------------|---------|-------------|
| **Net irrigation** | $NIR = ET_c - P_{eff}$ | Water needed at field |
| **Field irrigation** | $FIR = NIR / E_a$ | Plus application losses |
| **Canal irrigation** | $CIR = FIR / E_c$ | Plus conveyance losses |

Where $E_a$ = application efficiency, $E_c$ = conveyance efficiency

---

## Soil-Water Relationships

### Key Parameters
- **Field Capacity (FC):** Water content after gravitational drainage ceases (~20%)
- **Permanent Wilting Point (PWP):** Water content at which plants permanently wilt (~12%)
- **Available Moisture:** $AM = FC - PWP$ (~8%)
- **Readily Available Moisture (RAM):** 50–75% of AM

### Depth of Irrigation
$$d = (FC - \theta_{existing}) \times \gamma_b \times D_r$$

Where $D_r$ = root zone depth, $\gamma_b$ = bulk density

---

## Irrigation Methods

| Method | Water Use Efficiency | Best For |
|--------|---------------------|----------|
| **Furrow** | 40–60% | Row crops |
| **Border strip** | 50–70% | Cereals, fodder |
| **Basin** | 50–70% | Orchard, rice |
| **Sprinkler** | 70–85% | Uneven terrain, all crops |
| **Drip** | 85–95% | High-value crops, saline water |

---

## Canal Design

### Kennedy's Theory (Regime Channel)
$$V_0 = 0.55 m y^{0.64}$$

Where $m$ = silt factor = $1.76\sqrt{d_{mm}}$, $y$ = normal depth

### Lacey's Regime Theory
$$V = \left(\frac{Qf^2}{140}\right)^{1/6}$$

$$P = 2.67\sqrt{Q}$$

$$R = 5V^2/(2f)$$

Where $f$ = silt factor = $1.76\sqrt{d_{mm}}$

### Design Comparison

| Parameter | Kennedy | Lacey |
|-----------|---------|-------|
| Based on | Silt support | Regime conditions |
| Uses | Critical velocity ratio $m$ | Silt factor $f$ |
| Limitation | No width/depth relation | Assumes regime fully developed |

### Canal Types & Discharge

| Type | Capacity | Source |
|------|----------|--------|
| Main canal | > 50 m³/s | Headworks |
| Branch canal | 10–50 m³/s | Main canal off-take |
| Distributary | 2–10 m³/s | Branch canal |
| Minor | 0.1–2 m³/s | Distributary |
| Watercourse | < 0.1 m³/s | Minor |

---

## Irrigation Efficiencies

| Type | Definition | Typical Range |
|------|-----------|---------------|
| **Conveyance ($E_c$)** | (Delivered - seepage) / Diverted | 70–90% |
| **Application ($E_a$)** | (Stored in root zone) / Delivered | 50–85% |
| **Overall ($E_o$)** | $E_c \times E_a$ | 40–75% |
| **Cultural ($E_{cul}$)** | $ET_c$ / Water stored | 60–80% |

**Relationship:** $E_o = E_c \times E_a$

---

## Duty and Delta

### Duty ($D$)
$$D = \frac{\text{Area served}}{\text{Water supplied}} = \frac{A}{Q \times T}$$

- $D$ = hectares per cumec for $T$ days (cusec-days)

### Delta ($\Delta$)
$$\Delta = \frac{\text{Water required}}{\text{Area}} = \frac{8.64B}{D}$$ (metres)

Where $B$ = base period in days

### Relationship
$$D \times \Delta = 8.64 \times B$$ (D in hectare/cumec, $\Delta$ in metres, $B$ in days)

### Kor watering
- First watering after sowing; highest water requirement
- Kor depth × Kor period = constant for a crop

---

## Drainage & Waterlogging

### Waterlogging
- Water table rises within root zone → reduces soil aeration
- Causes: Over-irrigation, poor drainage, canal seepage
- **Critical depth:** $D_c = \gamma_b/\gamma_w \times D_r$ (safe depth of water table)

### Drainage Methods
- **Surface:** Open ditches, graded land
- **Subsurface:** Tile drains, pipe drains, drainage wells
- **Drain spacing (Hooghoudt's):**
  $$L^2 = \frac{4Kd^2}{q}$$ (simplified form)

---

## Worked Examples

### Example 1: Duty-Delta Calculation
**Problem:** Crop A has base period 120 days, duty 900 hectares/cumec. Find delta.

**Solution:**
1. $\Delta = 8.64B/D = 8.64 \times 120 / 900 = 1.152$ m = 1152 mm
2. For rice (base period 150 days), $\Delta = 1500$ mm → $D = 8.64 \times 150 / 1.5 = 864$ ha/cumec

### Example 2: Irrigation Efficiency
**Problem:** Canal diverts 10 m³/s for 10 days to irrigate 5000 hectares. Find conveyance efficiency if 20% is lost.

**Solution:**
1. Water diverted = $10 \times 10 \times 86400 = 8640$ ha-m
2. Seepage loss = 20% → Water delivered = $0.80 \times 8640 = 6912$ ha-m
3. $E_c = 6912/8640 = 80\%$

---

## 🎤 Interview Q&A

### Q1: What is the difference between duty and delta?
**A:** Duty is the area served per unit of water supplied (ha/cumec). Delta is the depth of water applied per unit area (m). They are inversely related: $D \times \Delta = 8.64B$. High duty means efficient water use.

### Q2: Compare Kennedy's and Lacey's theories.
**A:** Kennedy uses critical velocity ratio $m$ to ensure silt support but doesn't give width/depth relations. Lacey uses regime conditions with silt factor $f$ and provides complete geometry ($P$, $R$, $V$). Lacey is more comprehensive but assumes fully developed regime.

### Q3: What are the causes of waterlogging and how do you prevent it?
**A:** Causes: over-irrigation, poor drainage, canal seepage, high water table. Prevention: (1) Efficient irrigation scheduling, (2) Proper canal lining, (3) Subsurface drainage (tile drains), (4) Vertical drainage (pumping wells), (5) Crop selection for drainage conditions.

### Q4: Why is drip irrigation the most efficient?
**A:** Drip delivers water directly to the root zone, minimizing evaporation, runoff, and deep percolation losses. Efficiency: 85–95% vs 50–70% for surface methods. Benefits: water savings, salt management, fertigation capability, suitable for saline water.

---

## Quick Reference Formulas

| Formula | Equation |
|---------|----------|
| Duty-Delta | $D \times \Delta = 8.64B$ |
| Delta | $\Delta = 8.64B/D$ |
| Duty | $D = A/(Q \times T)$ |
| Kennedy | $V_0 = 0.55my^{0.64}$ |
| Lacey Velocity | $V = (Qf^2/140)^{1/6}$ |
| Lacey Perimeter | $P = 2.67\sqrt{Q}$ |
| Overall efficiency | $E_o = E_c \times E_a$ |
| Depth of irrigation | $d = (FC-\theta)\gamma_b D_r$ |
| Hooghoudt | $L^2 = 4Kd^2/q$ |

---

## 🗺️ Subject Roadmap

```
Beginner                    Intermediate                   Advanced                      Interview
─────────────────────────────────────────────────────────────────────────────────────────────────────
Crop water needs       →  Duty, delta, base period   →  Command area development    →  Duty-delta relationship
Irrigation methods     →  Canal design (Kennedy/      →  Waterlogging & drainage     →  Kennedy vs Lacey
Soil-water basics          Lacey)                     →  Irrigation scheduling       →  Why drip is most efficient
Efficiency concepts    →  Canal lining & losses       →  Remote sensing for          →  Efficiency chain (Ec,Ea,Eo)
Water requirements     →  Flow measurement in canals      irrigation management       →  Crop coefficient Kc
```

> **Priority:** `P1 — High Priority` · **Tags:** `HWRE` `CORE CIVIL`

---

## 📋 Formula Sheet

<details>
<summary><strong>Click to expand — Complete Irrigation Formula Sheet</strong></summary>

| Formula | Equation | Variables | Units | Conditions | Interview Importance |
|---------|----------|-----------|-------|------------|---------------------|
| Duty-Delta | $D \times \Delta = 8.64B$ | $D$=duty (ha/cumec), $\Delta$=delta (m), $B$=base period (days) | — | Water distribution | ⭐⭐⭐ |
| Net Irrigation | $NIR = ET_c - P_{eff}$ | $ET_c$=crop ET, $P_{eff}$=effective rainfall | mm | Field water need | ⭐⭐ |
| Field Irrigation | $FIR = NIR / E_a$ | $E_a$=application efficiency | mm | Including application losses | ⭐⭐ |
| Canal Irrigation | $CIR = FIR / E_c$ | $E_c$=conveyance efficiency | mm | Including conveyance losses | ⭐⭐ |
| Overall Efficiency | $E_o = E_c \times E_a$ | — | — | Total system efficiency | ⭐⭐ |
| Kennedy | $V_0 = 0.55my^{0.64}$ | $m$=CVR, $y$=depth | m/s | Critical velocity | ⭐⭐ |
| Lacey Velocity | $V = (Qf^2/140)^{1/6}$ | $f$=silt factor, $Q$=discharge | m/s | Regime channel | ⭐⭐ |
| Lacey Perimeter | $P = 2.67\sqrt{Q}$ | $Q$=discharge | m | Regime channel | ⭐⭐ |
| Lacey Silt Factor | $f = 1.76\sqrt{d_{mm}}$ | $d_{mm}$=median grain size | — | Regime theory | ⭐⭐ |
| Depth of Irrigation | $d = (FC - \theta_{existing}) \gamma_b D_r$ | $FC$=field capacity, $\theta$=existing, $D_r$=root zone depth | m | Irrigation scheduling | ⭐⭐ |
| Hooghoudt | $L^2 = 4Kd^2/q$ | $L$=drain spacing, $K$=hydraulic conductivity, $d$=depth to barrier | m | Drainage design | ⭐⭐ |

**Commonly Confused Pairs:**
- **Duty vs Delta:** Duty = area per unit discharge (ha/cumec); Delta = depth of water applied (m). Inversely related.
- **Kennedy vs Lacey:** Kennedy gives velocity only (needs CVR); Lacey gives complete regime geometry (P, R, V).
- **Conveyance vs Application efficiency:** Conveyance = water reaching field / water diverted; Application = water used by crop / water delivered to field.
- **Base period vs Cropping period:** Base period = time from first watering to last irrigation; Cropping period = entire growing season.

</details>

---

## ❓ Question Bank

### A. Basic Concept Questions

1. Define duty, delta, and base period. How are they related?
2. What are the types of irrigation methods and their efficiencies?
3. Explain Kennedy's and Lacey's theories for regime channel design.
4. What is waterlogging and how does it affect agriculture?
5. What is the difference between conveyance and application efficiency?
6. What is the command area of a canal?
7. What are the factors affecting crop water requirement?
8. What is the Penman equation for evapotranspiration?
9. What is the difference between furrow and border strip irrigation?
10. What is the role of drainage in irrigation?

### B. WHY Questions

1. **Why** is drip irrigation the most efficient method?
   - Delivers water directly to root zone, minimizing evaporation, runoff, and deep percolation. Efficiency 85–95% vs 40–60% for surface methods.

2. **Why** does Kennedy's theory need a critical velocity ratio $m$?
   - Because the theory assumes the channel maintains a constant depth (no silting, no scouring). The CVR $m$ depends on silt characteristics and adjusts the critical velocity accordingly.

3. **Why** is Lacey's theory considered more comprehensive than Kennedy's?
   - Lacey provides complete regime geometry (width, depth, slope, perimeter) from a single silt factor $f$. Kennedy only gives velocity and requires additional assumptions for dimensions.

4. **Why** does canal seepage cause waterlogging?
   - Seepage raises the water table. When the water table reaches the root zone, soil becomes saturated, reducing aeration and crop growth.

5. **Why** is the base period used instead of the cropping period in the duty-delta relationship?
   - Because the base period represents the actual water application period, while the cropping period may include rainfed periods with no irrigation.

### C. WHAT-IF Questions

1. **What happens** if canal seepage losses are not controlled?
   - Waterlogging, salinization, reduced downstream availability, inefficient irrigation.

2. **What happens** if irrigation is applied at field capacity?
   - No need for irrigation; field is already at optimal moisture. Over-irrigation wastes water and causes waterlogging.

3. **What happens** if duty increases (more area per cumec)?
   - Delta decreases for same base period; less water per unit area but more area served.

4. **What happens** if drainage is inadequate?
   - Water table rises, root zone becomes saturated, crop yield decreases, soil salinity increases.

5. **What happens** if drip irrigation emitters clog?
   - Non-uniform water distribution, reduced efficiency, crop stress in under-irrigated zones.

### D. Comparison Questions

| Concept A | Concept B | Key Difference | Application |
|-----------|-----------|----------------|-------------|
| Duty | Delta | Area/discharge vs depth applied | Canal design |
| Kennedy | Lacey | Velocity only vs complete regime | Channel design |
| Furrow | Border strip | Narrow channels vs wide strips | Row vs row crops |
| Drip | Sprinkler | Localized vs overhead | Efficiency vs coverage |
| Conveyance eff. | Application eff. | Delivery vs crop use | System efficiency |
| Base period | Cropping period | Irrigation time vs full season | Duty-delta |
| Net irrigation | Gross irrigation | Field need vs total applied | Water accounting |

### E. Numerical Questions

**Easy:**
**Problem:** A canal serves 8000 hectares with discharge 10 m³/s. Base period is 120 days. Find duty and delta.
- **Given:** $A=8000$ ha, $Q=10$ m³/s, $B=120$ days
- **Find:** $D$, $\Delta$
- **Approach:** $D = A/Q = 8000/10 = 800$ ha/cumec; $\Delta = 8.64B/D = 8.64 \times 120/800 = 1.296$ m
- **Solution:** $D = 800$ ha/cumec, $\Delta = 1.30$ m
- **Final Answer:** $D = 800$ ha/cumec, $\Delta = 1.30$ m
- **Concept Tested:** Duty-delta relationship
- **Common Trap:** Forgetting the 8.64 conversion factor

**Medium:**
**Problem:** A canal diverts 20 m³/s. Conveyance efficiency is 80%, application efficiency is 65%. Command area = 15,000 ha. Base period = 150 days. Find delta and overall efficiency.
- **Given:** $Q=20$, $E_c=0.80$, $E_a=0.65$, $A=15000$ ha, $B=150$
- **Find:** $\Delta$, $E_o$
- **Approach:** $E_o = E_c \times E_a = 0.52$. Duty = $A/Q = 750$ ha/cumec. $\Delta = 8.64B/D = 8.64 \times 150/750 = 1.728$ m.
- **Solution:** $E_o = 52\%$, $\Delta = 1.73$ m
- **Final Answer:** $E_o = 52\%$, $\Delta = 1.73$ m
- **Concept Tested:** Overall efficiency and duty-delta
- **Common Trap:** Not chaining efficiencies

**Hard:**
**Problem:** Design a regime channel for Q=50 m³/s, f=1.2. Also find the Kennedy critical depth if m=1.0.
- **Given:** $Q=50$ m³/s, $f=1.2$, $m=1.0$
- **Find:** Lacey geometry ($P, R, V, y, b$) and Kennedy $y$
- **Approach:** Lacey: $V = (Qf^2/140)^{1/6}$, $P = 2.67\sqrt{Q}$, $R = 5V^2/(2g)$, $A = Q/V$, $b = P - 2y\sqrt{1+z^2}$. Kennedy: $V_0 = 0.55my^{0.64}$, equate to Lacey $V$.
- **Solution:**
  - $V = (50 \times 1.44/140)^{1/6} = (0.514)^{1/6} = 0.914$ m/s
  - $P = 2.67\sqrt{50} = 18.88$ m
  - $R = 5 \times 0.914^2/(2 \times 9.81) = 0.213$ m
  - $A = 50/0.914 = 54.7$ m²
  - $y = R \times 1.75 \approx 0.373$ m (approximate for regime)
  - Kennedy: $0.914 = 0.55 \times 1.0 \times y^{0.64}$ → $y^{0.64} = 1.662$ → $y = 2.27$ m
- **Final Answer:** Lacey: $V=0.91$ m/s, $P=18.9$ m, $R=0.21$ m; Kennedy: $y \approx 2.3$ m
- **Concept Tested:** Kennedy vs Lacey regime design
- **Common Trap:** Mixing up Lacey and Kennedy formulas

### F. Rapid-Fire Questions (20+)

Q: What is duty?
A: Area irrigated per unit discharge (ha/cumec).

Q: What is delta?
A: Depth of water applied to the crop (m).

Q: What is base period?
A: Time from first irrigation to last irrigation before harvest (days).

Q: What is the duty-delta relationship?
A: $D \times \Delta = 8.64B$.

Q: What is conveyance efficiency?
A: Water delivered to field / water diverted from source.

Q: What is application efficiency?
A: Water used by crop / water delivered to field.

Q: What is overall irrigation efficiency?
A: $E_o = E_c \times E_a$.

Q: What is Kennedy's critical velocity?
A: $V_0 = 0.55my^{0.64}$ — velocity at which neither silting nor scouring occurs.

Q: What is Lacey's silt factor?
A: $f = 1.76\sqrt{d_{mm}}$ — relates sediment size to regime dimensions.

Q: What is the most efficient irrigation method?
A: Drip irrigation (85–95% efficiency).

Q: What is waterlogging?
A: Saturation of root zone due to high water table, reducing crop growth.

Q: What is the Penman equation?
A: Combines energy balance and aerodynamic methods for evapotranspiration estimation.

Q: What is a cropping pattern?
A: Sequence and proportion of crops grown in a season on the same land.

Q: What is a Kharif crop?
A: Monsoon season crop (June–October): rice, cotton, sugarcane.

Q: What is a Rabi crop?
A: Winter season crop (October–March): wheat, mustard, gram.

Q: What is supplemental irrigation?
A: Irrigation applied during dry spells in rainfed agriculture to supplement rainfall.

Q: What is surface irrigation?
A: Water flows over the soil surface by gravity (furrow, border, basin methods).

Q: What is a watercourse?
A: The smallest distributary channel that delivers water to individual farm fields.

### G. Deep Technical Questions

1. **How would you optimize canal scheduling for a large command area?**
   - Use linear programming or genetic algorithms to minimize losses, balance supply-demand across blocks, account for travel time in canal system, and consider crop calendar constraints.

2. **Compare Kennedy's and Lacey's theories for alluvial channel design.**
   - Kennedy: only gives velocity; needs CVR (varies with silt). Lacey: gives complete geometry from silt factor; assumes regime conditions. Lacey is more comprehensive but both fail for non-alluvial or transitional channels.

3. **How does climate change affect irrigation water demand?**
   - Increased temperature → higher ET → more irrigation. Changed monsoon patterns → more supplemental irrigation needed. Need: crop modeling (CROPWAT), climate projections, adaptive management.

---

## 🎤 Interview Answer Format

### High-Value Q1: "Explain the duty-delta relationship."

**30-second answer:**
"Duty is the area served per unit discharge (ha/cumec), delta is the depth of water applied (m), and base period is the irrigation duration (days). They are related by $D \times \Delta = 8.64B$, where 8.64 converts units."

**If interviewer asks deeper:**
"The relationship comes from volume balance: volume supplied = $Q \times B \times 86400$ m³, volume needed = $A \times \Delta \times 10^4$ m³. Equating gives $D \times \Delta = 8.64B$. A higher duty means less water per unit area — indicating better water use efficiency."

**Key equation:**
$D \times \Delta = 8.64B$

---

## 🔗 Cross-Links

- [`water-resources-engineering.md`](../water_resources/water-resources-engineering.md) — Reservoir, canal systems
- [`hydrology.md`](../hydrology/hydrology.md) — Rainfall-runoff, infiltration
- [`groundwater.md`](../water_supply/groundwater.md) — Conjunctive use
- [`environmental-engineering.md`](../../environmental/environmental-engineering.md) — Water quality for irrigation
- [`geotechnical.md`](../../geotechnical/geotechnical.md) — Soil mechanics, drainage

---

## References

