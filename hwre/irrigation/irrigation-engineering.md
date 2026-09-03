# Irrigation Engineering

## Scope

Irrigation engineering deals with the planning, design, and management of water supply systems for agricultural crops. It bridges hydrology, soil science, crop physiology, and water resources engineering.

> **Related topics:** [`water-resources-engineering.md`](../../civil/water_resources/water-resources-engineering.md) · [`groundwater.md`](../water_supply/groundwater.md) · [`flood-control.md`](../flood_control/flood-control.md)

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

## References

* [Civil_Placement_IITK](https://github.com/DKS-MANAGER/Civil_Placement_IITK)
* [GATE_Civil_Study_Material_2027](https://github.com/DKS-MANAGER/GATE_Civil_Study_Material_2027)
