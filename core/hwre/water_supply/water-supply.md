# Water Supply Engineering

## Overview

Water supply engineering encompasses the collection, treatment, transmission, and distribution of potable water to consumers. It integrates hydrology, hydraulics, chemistry, and public health.

> **Related topics:** [`groundwater.md`](groundwater.md) · [`wastewater-engineering.md`](../wastewater/wastewater-engineering.md) · [`water-resources-engineering.md`](../water_resources/water-resources-engineering.md)

---

## Water Demand

### Per Capita Demand (Indian Standards)

| Category | Demand (lpcd) |
|----------|--------------|
| Domestic (public standpipe) | 40 |
| Domestic (with individual connection) | 135–200 |
| Commercial | 20–30 |
| Industrial | 50–75 |
| Public use | 10 |
| Fire demand (100-yr) | 1000–1500 L/min |
| **Total** | 200–350 lpcd |
| **Design with UFW (20%)** | 250–450 lpcd |

### Population Forecasting

| Method | Formula | When to Use |
|--------|---------|-------------|
| Arithmetic | $P_n = P_0 + n\bar{x}$ | Stable, mature cities |
| Geometric | $P_n = P_0(1+r)^n$ | Growing cities |
| Incremental | $P_n = P_0 + n\bar{x} + n(n+1)d/2$ | Moderate growth |
| Logistic | $P = P_{sat}/(1+ae^{-bt})$ | S-shaped growth |

### Fire Demand (Kuichling)
$$Q = 3182\sqrt{P}$$ (L/min, P in thousands)

---

## Water Treatment

### Treatment Train
```
Raw Water → Aeration → Coagulation → Flocculation → Sedimentation → Filtration → Disinfection → Distribution
```

### Process Parameters

| Process | Purpose | Typical Value |
|---------|---------|---------------|
| Coagulation | Destabilize colloids | Alum: 20–60 mg/L, rapid mix 30–60s |
| Flocculation | Form settleable flocs | G = 20–70 s⁻¹, 15–30 min |
| Sedimentation | Remove flocs | HRT = 2–4 hrs, overflow 1–2 m³/m²·h |
| Rapid sand filtration | Remove fine particles | Rate 4–6 m/h, bed depth 0.6–0.7 m |
| Slow sand filtration | Biological treatment | Rate 0.1–0.3 m/h, bed depth 1–1.5 m |
| Chlorination | Kill pathogens | Residual 0.2–1.0 mg/L |

### Slow Sand vs Rapid Sand Filter

| Parameter | Slow Sand | Rapid Sand |
|-----------|-----------|------------|
| Rate | 0.1–0.3 m/h | 4–6 m/h |
| Media | Sand (0.2–0.3 mm) | Sand + anthracite |
| Biological layer | Schmutzdecke (critical) | Not essential |
| Cleaning | Scraping surface | Backwashing |
| Area required | 10–20× more | Less |
| Pre-treatment | Coagulation optional | Coagulation required |

---

## Distribution Systems

### Layout Types

| Type | Advantages | Disadvantages |
|------|-----------|---------------|
| **Dead-end** | Low cost, simple | Stagnation, no redundancy |
| **Gridiron** | Good reliability | Higher cost |
| **Ring (loop)** | Redundancy, equal pressure | Complex design |
| **Radial** | Balanced pressure | Needs elevated reservoir |

### Hydraulic Design

**Hazen-Williams equation:**
$$h_f = \frac{10.67 L Q^{1.85}}{C^{1.85} D^{4.87}}$$

Where $C$ = Hazen-Williams coefficient (100–140)

### Storage Requirements
- **Balancing storage:** For demand fluctuations (typically 1 day)
- **Break storage:** For pump failure (half-day supply)
- **Fire storage:** 1000–1500 L/min for 2–4 hours
- **Emergency storage:** 1–3 days

---

## Pumping

| Scheme | Description | Use |
|--------|-------------|-----|
| Direct | No storage, constant discharge | Small systems |
| Indirect | Pump to elevated reservoir, gravity distribution | Most common |
| High-lift | Booster pumps for high-rise | Urban areas |

### Pump Selection Criteria
- Head: Total dynamic head (static + friction + velocity)
- Discharge: Design flow rate
- Specific speed: $N_s = N\sqrt{Q}/H^{3/4}$
- NPSH: Ensure $NPSH_A > NPSH_R$

---

## Worked Examples

### Example 1: Population Forecast
**Problem:** Population data: 1981: 50,000; 1991: 65,000; 2001: 85,000. Forecast for 2021 using geometric increase.

**Solution:**
1. Growth rate 1981–1991: $r_1 = (65/50)^{1/10} - 1 = 2.65\%$
2. Growth rate 1991–2001: $r_2 = (85/65)^{1/10} - 1 = 2.71\%$
3. Average $r = 2.68\%$
4. $P_{2021} = 85000(1.0268)^{20} = 85000 \times 1.704 = 144,840$

### Example 2: Water Demand
**Problem:** City population 150,000. Domestic 150 lpcd, commercial 30 lpcd, public 10 lpcd, industrial 50 lpcd. UFW = 20%. Find total design demand.

**Solution:**
1. Net demand = $(150 + 30 + 10 + 50) = 240$ lpcd
2. With UFW: $240/0.8 = 300$ lpcd
3. Total = $150000 \times 300 = 45$ ML/d
4. Fire demand: $3182\sqrt{150} = 38,973$ L/min ≈ 56.1 ML/d (separate pipe system)

### Example 3: Sedimentation Tank
**Problem:** Design a primary clarifier for $Q = 10$ ML/d, overflow rate = 30 m³/m²·d.

**Solution:**
1. Area $A = Q/overflow = 10000/30 = 333.3$ m²
2. Diameter (circular): $D = \sqrt{4A/\pi} = \sqrt{4 \times 333.3/\pi} = 20.6$ m → Use 21 m
3. HRT: $V/Q = (A \times \text{depth})/Q = 333.3 \times 3/416.7 = 2.4$ hrs ✓

### Example 4: Hazen-Williams Head Loss
**Problem:** Find head loss in 500 m pipe, $D = 300$ mm, $Q = 50$ L/s, $C = 120$.

**Solution:**
1. $h_f = 10.67 \times 500 \times 0.05^{1.85} / (120^{1.85} \times 0.3^{4.87})$
2. $h_f = 10.67 \times 500 \times 0.00386 / (7322 \times 0.00264)$
3. $h_f = 20.6 / 19.33 = 1.066$ m

### Example 5: Fire Demand
**Problem:** City population 200,000. Find fire demand using Kuichling and National Board of Fire Underwriters formulas.

**Solution:**
1. Kuichling: $Q = 3182\sqrt{200} = 44,997$ L/min ≈ 750 L/s
2. NBFU: $Q = 4637\sqrt{P}(1-0.001\sqrt{P})$ = 4637√200(1-0.001√200) = 65,549 × 0.986 = 64,631 L/min ≈ 1077 L/s

---

## 🎤 Interview Q&A

### Q1: What is the difference between slow sand and rapid sand filters?
**A:** Slow sand: biological filtration via Schmutzdecke, low rate (0.1–0.3 m/h), large area, no pre-treatment needed. Rapid sand: physical filtration, high rate (4–6 m/h), small area, requires coagulation pre-treatment, backwashing needed. Slow sand suits small communities with clean source; rapid sand suits large cities.

### Q2: How do you design a water distribution system?
**A:** (1) Estimate demand (per capita × population × UFW factor), (2) Select layout (gridiron/ring), (3) Size pipes using Hardy Cross or Hazen-Williams, (4) Determine pump size (TDH + friction), (5) Size elevated storage (balancing + fire + emergency), (6) Check pressure at critical nodes (min 15–20 m head).

### Q3: What is the role of coagulation in water treatment?
**A:** Coagulants (alum, PAC) neutralize negative charges on colloidal particles, destabilizing them so they can form flocs via flocculation. Alum + alkalinity → Al(OH)₃ floc + CO₂. Dose determined by jar test. Rapid mix (G = 300–1000 s⁻¹, 30s) followed by slow mix (G = 20–70 s⁻¹, 15–30 min).

### Q4: What are the design criteria for a water treatment plant?
**A:** Coagulation: G = 300–1000 s⁻¹, 30–60s. Flocculation: G = 20–70 s⁻¹, 15–30 min. Sedimentation: overflow 1–2 m³/m²·h, HRT 2–4 hrs. Rapid sand: rate 4–6 m/h, bed 0.6–0.7 m. Disinfection: residual 0.2–1.0 mg/L, contact time ≥ 30 min.

### Q5: What is non-revenue water and how do you reduce it?
**A:** Non-revenue water (NRW) = water produced but not billed (leaks, theft, metering errors). Typical in India: 30–50%. Reduction: (1) Leak detection (acoustic, satellite), (2) Meter replacement, (3) Pressure management, (4) DMA (district metered areas), (5) Pipe replacement programs. Target: < 20%.

---

## Quick Reference

| Formula | Equation |
|---------|----------|
| Per capita demand | $Q = P \times q \times 1.2$ (with UFW) |
| Population (geometric) | $P_n = P_0(1+r)^n$ |
| Fire demand (Kuichling) | $Q = 3182\sqrt{P}$ (L/min) |
| Hazen-Williams | $h_f = 10.67LQ^{1.85}/(C^{1.85}D^{4.87})$ |
| Alum dose | $Al_2(SO_4)_3 \cdot 18H_2O + Ca(HCO_3)_2 → 2Al(OH)_3 + 3CaSO_4 + 6CO_2$ |

---

## Standards

| Parameter | IS 10500 Limit |
|-----------|---------------|
| pH | 6.5–8.5 |
| TDS | < 500 mg/L (acceptable), < 2000 (limiting) |
| Hardness | < 200 mg/L (acceptable) |
| Chlorides | < 250 mg/L |
| Fluoride | < 1.0 mg/L |
| Iron | < 0.3 mg/L |
| E. coli | Absent in 100 mL |

---

## 🗺️ Subject Roadmap

```
Beginner                    Intermediate                   Advanced                      Interview
─────────────────────────────────────────────────────────────────────────────────────────────────────
Water demand basics   →  Population forecasting       →  Real-time network modeling   →  Per capita demand estimation
Treatment train       →  Coagulation-flocculation     →  Advanced oxidation           →  Why coagulation is essential
Disinfection          →  Slow/Rapid sand filters      →  Membrane filtration          →  Chlorination vs UV
Distribution systems  →  Hardy Cross network analysis  →  SCADA & real-time control   →  Network analysis basics
Fire demand           →  Pipe sizing (Hazen-Williams) →  Water hammer analysis        →  Fire demand formula
IS 10500 standards    →  Water audit & NRW            →  Smart water systems          →  Non-revenue water
```

> **Priority:** `P1 — High Priority` · **Tags:** `HWRE` `ENVIRONMENTAL`

---

## ❓ Question Bank (Selected)

### A. Basic Concept
1. What are the steps in a water treatment plant?
2. What is non-revenue water and how do you reduce it?
3. What are the IS 10500 drinking water standards?

### B. WHY Questions
1. **Why** is coagulation necessary before sedimentation?
   - Colloidal particles (< 1 μm) have negative surface charges that prevent settling. Coagulants neutralize these charges, allowing flocculation and gravity settling.

2. **Why** is slow sand filtration being replaced by rapid sand filtration?
   - Slow sand: low rate (0.1–0.4 m/h), large area, biological process. Rapid sand: higher rate (4–6 m/h), smaller footprint, requires pre-treatment (coagulation).

3. **Why** is residual chlorine maintained in distribution?
   - Prevents regrowth of bacteria in pipes; maintains water quality from treatment plant to consumer tap. Typical residual: 0.2–1.0 mg/L.

---

## 🎤 Interview Answer Format

### High-Value Q: "Describe the water treatment train."

**30-second answer:**
"Raw water → Aeration → Coagulation (rapid mix) → Flocculation (slow mix) → Sedimentation → Filtration (rapid sand) → Disinfection (chlorination) → Distribution. Each step removes progressively smaller contaminants."

**Key equation:**
Hazen-Williams: $h_f = 10.67LQ^{1.85}/(C^{1.85}D^{4.87})$

---

## 🔗 Cross-Links

- [`wastewater-engineering.md`](../wastewater/wastewater-engineering.md) — Wastewater treatment comparison
- [`water-resources-engineering.md`](../water_resources/water-resources-engineering.md) — Source water
- [`groundwater.md`](groundwater.md) — Groundwater as source
- [`environmental-engineering.md`](../../environmental/environmental-engineering.md) — Water quality engineering

---

## References

* [awesome-civil-engineering](https://github.com/awesome-civil-engineering/awesome-civil-engineering)
