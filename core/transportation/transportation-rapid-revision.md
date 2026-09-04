# Transportation Engineering — Rapid Revision Sheet

> Last-minute cheat sheet for Transportation Engineering interviews and exams.

---

## Framework 1: Highway Geometric Design

### Minimum Radius

$$R_{min} = \frac{V^2}{127(e + f)}$$

| V (km/h) | f (IRC) | e_max (plain) | R_min (m) |
|:---------:|:-------:|:--------------:|:---------:|
| 30 | 0.17 | 0.07 | 35.2 |
| 50 | 0.16 | 0.07 | 91.7 |
| 80 | 0.15 | 0.07 | 217.6 |
| 100 | 0.13 | 0.06 | 356.3 |
| 120 | 0.12 | 0.06 | 518.8 |

### Sight Distance Formulas

**SSD (Stopping Sight Distance):**
$$SSD = 0.278 \cdot V \cdot t + \frac{V^2}{254(f \pm G)}$$

| V (km/h) | SSD (m) IRC |
|:---------:|:-----------:|
| 30 | 24 |
| 50 | 48 |
| 80 | 120 |
| 100 | 185 |
| 120 | 260 |

**OSD (Overtaking):** OSD = d₁ + d₂ + d₃

### Vertical Curves

**Summit:** L = N·V²/46.7

| Condition | Formula |
|:----------|:--------|
| SSD ≥ L | L = N·S²/4.4 |
| SSD < L | L = 2S - 4.4/N |

### Road Classification Standards

| Class | V_design (km/h) | Carriageway (m) | Gradient (ruling) |
|:------|:---------------:|:---------------:|:-----------------:|
| NH/Expressway | 100-120 | 7.0/14.0 | 3% |
| SH | 80 | 7.0 | 4% |
| MDR | 65 | 7.0 | 5% |
| ODR | 50 | 6.0 | 6% |
| VR | 30 | 3.75 | 7% |

---

## Framework 2: Traffic Engineering

### Fundamental Equation
$$q = k \cdot v$$

### Greenshields Model

| Parameter | Formula | At Capacity |
|:----------|:--------|:------------|
| Speed | v = v_f(1 - k/k_j) | v_opt = v_f/2 |
| Flow | q = k·v_f(1 - k/k_j) | q_max = v_f·k_j/4 |
| Capacity | q_max = v_f·k_j/4 | k_opt = k_j/2 |

### Webster's Signal Design

$$C_o = \frac{1.5L + 5}{1 - \sum Y_i}$$

| Symbol | Meaning |
|:-------|:--------|
| C_o | Optimal cycle length (s) |
| L | Total lost time per cycle (s) |
| Y_i | Flow ratio = q_i / s_i |
| g_i | Effective green = Y_i/ΣY_j × (C-L) |

**Saturation flow (Indian):** s = 525 · w_h (IRC SP:88)

**Degree of saturation:** X_i = q_i / [s_i × (g_i/C)] — target ≤ 0.85-0.90

### LOS Classification (Indian Conditions)

| LOS | v/c Ratio | Description |
|:----|:---------:|:------------|
| A | < 0.35 | Free flow |
| B | 0.35-0.55 | Stable, slight delay |
| C | 0.55-0.75 | Stable, acceptable delay |
| D | 0.75-0.90 | Approaching unstable |
| E | 0.90-1.00 | Unstable, significant delay |
| F | > 1.00 | Forced flow |

### Speed Measures

| Measure | Formula | Use |
|:--------|:--------|:----|
| Time mean speed | v̄_t = Σv_i/n | Arithmetic mean |
| Space mean speed | v̄_s = n/Σ(1/v_i) | Harmonic mean (use this!) |
| 85th percentile | From cumulative freq | Speed limit basis |

---

## Framework 3: Pavement Design

### Flexible Pavement Layers (Top → Bottom)

| Layer | Material | Thickness Coeff |
|:------|:---------|:---------------:|
| Surface | Bituminous Concrete (BC) | 0.35 |
| Binder | Dense Bituminous Macadam (DBM) | 0.25 |
| Base | Wet Mix Macadam (WMM) | 0.15 |
| Sub-base | Granular Sub-base (GSB) | 0.08 |
| Subgrade | Compacted soil | — |

**IRC:37 Quick Reference (Total Thickness, mm):**

| CBR (%) | 10 msa | 50 msa | 100 msa |
|:--------:|:------:|:------:|:-------:|
| 2 | 520 | 680 | 780 |
| 3 | 440 | 580 | 670 |
| 5 | 350 | 460 | 550 |
| 10 | 240 | 330 | 400 |
| 15 | 190 | 270 | 330 |

### Rigid vs Flexible Pavement

| Aspect | Flexible | Rigid |
|:-------|:---------|:------|
| Load distribution | Layer-by-layer | Slab action (spreads load) |
| Failure mode | Rutting, fatigue cracking | Pumping, faulting, corner cracking |
| Design method | CBR (IRC:37) | PCA / Westergaard (IRC:58) |
| Maintenance | Easier, overlays | Harder, full slab replacement |
| Cost | Lower initial | Higher initial, lower maintenance |
| Life | 15-20 years | 30-40 years |

---

## Framework 4: Railway & Airport

### Railway Superelevation

$$e = \frac{G \cdot V^2}{127 \cdot R}$$

| Gauge | Width (mm) | Common Use |
|:------|:----------:|:-----------|
| BG (Broad Gauge) | 1676 | Indian Railways mainline |
| MG (Meter Gauge) | 1000 | Legacy routes (converting to BG) |
| NG (Narrow Gauge) | 762/610 | Hill railways (Shimla, Darjeeling) |

**Cant deficiency limits:** BG = 76 mm (Indian Railways)

### Airport Runway

**Key factors for runway length:**
1. Elevation (higher = longer, +7% per 300 m)
2. Temperature (+1% per 1°C above standard)
3. Gradient (+10% per 1% upward gradient)
4. Aircraft weight (heavier = longer)

**ICAO Aircraft Categories:**
- A: Wingspan < 15m (Cessna, etc.)
- B: 15m ≤ Wingspan < 24m (ATR-72)
- C: 24m ≤ Wingspan < 36m (A320, B737)
- D: 36m ≤ Wingspan < 52m (A330, B777)
- E: 52m ≤ Wingspan < 65m (A380)

---

## Quick-Fire Interview Answers

**Q1: What is the fundamental equation of traffic flow?**
A: q = k × v, where q = flow (veh/hr), k = density (veh/km), v = space mean speed (km/hr). This is the basic identity of traffic flow theory.

**Q2: What is the difference between SSD and OSD?**
A: SSD is the minimum distance to see an obstacle and stop safely. OSD is the minimum distance to safely complete an overtaking maneuver. OSD is always larger than SSD because it accounts for the overtaking vehicle's acceleration, the overtaken vehicle's travel, and the oncoming vehicle's approach.

**Q3: Why is Webster's method used for signal design?**
A: Webster's method minimizes total intersection delay by finding the optimal cycle length C_o = (1.5L+5)/(1-ΣY). It balances between too short (frequent lost time) and too long (excessive delay in red phases).

**Q4: What are PCU factors and why do they matter?**
A: PCU (Passenger Car Unit) converts mixed traffic into equivalent car units. A bus = 3.0 PCU, two-wheeler = 0.5 PCU, etc. This allows capacity analysis of roads with heterogeneous Indian traffic.

**Q5: When would you choose rigid over flexible pavement?**
A: Rigid pavement for: high-traffic (>100 msa), long design life needed, heavy axle loads (industrial areas), low maintenance budget over time. Flexible pavement for: moderate traffic, shorter design life acceptable, easier future widening, lower initial budget.

**Q6: What is cant deficiency in railways?**
A: Cant deficiency is the difference between the required superelevation for a given speed and the actual superelevation provided. It exists because trains run at different speeds on the same track. Excessive cant deficiency causes passenger discomfort and track wear. Indian Railways limit: 76 mm for BG.

**Q7: How does elevation affect runway length?**
A: Higher elevation = lower air density = less lift = longer runway needed. ICAO recommends +7% increase in runway length per 300 m above MSL. A runway at 600 m elevation needs ~14% longer than at sea level.

**Q8: What is LOS in traffic engineering?**
A: Level of Service (LOS) is a qualitative measure of traffic conditions, graded A (free flow) to F (forced flow). It's based on speed, delay, and volume-to-capacity ratio. LOS C is typically the design target for urban roads.

**Q9: What is the 100% rule in WBS?**
A: The sum of child elements at any WBS level must equal 100% of the parent element's scope. This ensures no work is missing or duplicated. It's a fundamental principle of scope management.

**Q10: Name 3 recent transportation infrastructure projects in India.**
A: (1) Delhi-Mumbai Expressway (1,386 km, India's longest), (2) Bharatmala Pariyojana (65,000 km highway development), (3) Mumbai-Ahmedabad Bullet Train (508 km, Shinkansen technology).

---

## Last-Minute Checklist

- [ ] R_min formula and IRC friction values
- [ ] SSD formula with gradient correction
- [ ] Summit/valley curve formulas and conditions
- [ ] Greenshields model and q_max derivation
- [ ] Webster's signal design (complete method)
- [ ] LOS A-F with v/c ratios
- [ ] Flexible pavement layers and thickness table
- [ ] Rigid vs flexible comparison
- [ ] Railway superelevation formula and cant deficiency limits
- [ ] Airport runway length factors (elevation, temp, gradient)
- [ ] PCU factors for Indian vehicles
- [ ] IRC road classification standards

---

## Cross-Links

- [`transportation-engineering.md`](transportation-engineering.md) — Full subject reference
- [`transportation-software.md`](transportation-software.md) — Software tools
- [`role-study-plan.md`](role-study-plan.md) — Detailed study plan with worked examples
- [`geotechnical.md`](../geotechnical/geotechnical.md) — Subgrade design
- [`civil-rapid-revision.md`](../fundamentals/civil-rapid-revision.md) — Cross-subject formulas

---

## References

- IRC:73, IRC:78, IRC:37-2018, IRC:58-2015, IRC SP:88, IRC:102
- MoRTH Specifications
- ICAO Annex 14
* [awesome-civil-engineering](https://github.com/awesome-civil-engineering/awesome-civil-engineering)
