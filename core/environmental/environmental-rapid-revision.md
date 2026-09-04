# Environmental Engineer — Rapid Revision Sheet

> Last-minute cheat sheet for environmental engineering interviews (CPCB, SPCB, consulting).

---

## Framework 1: Water Quality Parameters

### IS 10500 Drinking Water Standards
| Parameter | Acceptable | Permissible |
|:----------|:----------:|:-----------:|
| pH | 6.5–8.5 | No relaxation |
| TDS | 500 mg/L | 2000 mg/L |
| Hardness | 200 mg/L | 600 mg/L |
| Chloride | 250 mg/L | 1000 mg/L |
| Sulphate | 200 mg/L | 400 mg/L |
| Fluoride | 0.6–1.2 mg/L | 1.5 mg/L |
| Iron | 0.3 mg/L | No relaxation |
| Coliforms | 0 MPN/100mL | 5 MPN/100mL (Rural) |

### CPCB Effluent Standards (Inland Surface Water)
| Parameter | Limit (mg/L) |
|:----------|:------------:|
| BOD₅ | 30 |
| COD | 250 |
| TSS | 100 |
| Oil & Grease | 10 |
| Total Coliforms | 5000 MPN/100mL |
| pH | 5.5–9.0 |

### Key Ratios
- **BOD/COD > 0.5:** Easily biodegradable
- **BOD/COD < 0.3:** Hardly biodegradable (needs advanced treatment)
- **COD ≥ BOD always** (COD includes non-biodegradable organics)

---

## Framework 2: BOD Kinetics

### First-Order BOD Reaction
- y_t = L₀(1 - e^{-k₁t}) — BOD exerted at time t
- L_t = L₀ × e^{-k₁t} — BOD remaining
- **BOD₅ (standard test):** 5 days at 20°C in dark

### Temperature Correction
- k_T = k₂₀ × θ^{(T-20)}
- θ = 1.047 for BOD
- θ = 1.024 for reaeration (k₂)

### Streeter-Phelps Oxygen Sag
- D = k₁L₀/(k₂-k₁) × (e^{-k₁t} - e^{-k₂t}) + D₀e^{-k₂t}
- **Critical time:** t_c = ln[(k₂/k₁)(1 - D₀(k₂-k₁)/(k₁L₀))] / (k₂-k₁)
- **Critical deficit:** D_c = k₁L₀/k₂ × e^{-k₁t_c}
- **Minimum DO:** DO_min = DO_sat - D_c

---

## Framework 3: Wastewater Treatment Process Train

```
Raw Wastewater
    ↓
Screening (remove large solids)
    ↓
Grit Chamber (remove sand/grit, v = 0.3 m/s)
    ↓
Primary Sedimentation (remove 50-65% SS, 25-35% BOD)
    ↓
Secondary Treatment:
    ├── Activated Sludge Process (F/M = 0.2-0.6, MLSS = 2000-4000 mg/L)
    ├── Trickling Filter (low energy, robust)
    ├── Oxidation Pond (low cost, land-intensive)
    └── Sequencing Batch Reactor (SBR)
    ↓
Tertiary Treatment:
    ├── Sand Filtration
    ├── Disinfection (chlorination, UV, ozonation)
    └── Nutrient Removal (N, P)
    ↓
Effluent Discharge (meets CPCB standards)
```

### Design Parameters
| Process | HRT | F/M | MLSS | BOD Removal |
|:--------|:----|:----|:-----|:------------|
| Primary sedimentation | 1.5–2.5 hr | — | — | 25–35% |
| Activated sludge | 4–8 hr | 0.2–0.6 | 2000–4000 mg/L | 85–95% |
| Trickling filter | — | — | — | 80–90% |
| Oxidation pond | 2–3 weeks | — | — | 70–85% |
| UASB reactor | 6–24 hr | — | — | 75–85% |

---

## Framework 4: Air Pollution Quick Reference

### NAAQS (National Ambient Air Quality Standards)
| Pollutant | Averaging Time | Standard |
|:----------|:---------------|:--------:|
| PM₂.₅ | Annual | 40 μg/m³ |
| PM₂.₅ | 24-hour | 60 μg/m³ |
| PM₁₀ | Annual | 60 μg/m³ |
| PM₁₀ | 24-hour | 100 μg/m³ |
| SO₂ | Annual | 50 μg/m³ |
| SO₂ | 24-hour | 80 μg/m³ |
| NOₓ | Annual | 40 μg/m³ |
| NOₓ | 24-hour | 80 μg/m³ |
| CO | 8-hour | 2 mg/m³ |
| CO | 24-hour | 4 mg/m³ |
| Ozone | 8-hour | 100 μg/m³ |

### Control Devices Comparison
| Device | Efficiency | Best For | Cost |
|:-------|:----------:|:---------|:----:|
| Cyclone | 70–85% | Coarse PM (> 10μm) | Low |
| ESP | 99%+ | Fine PM, large flows | High |
| Baghouse | 99%+ | Fine PM, moderate flows | Medium |
| Wet scrubber | 90–95% | Gases + PM, hot gases | Medium |
| Catalytic converter | 90%+ | Vehicle exhaust (CO, HC, NOₓ) | Medium |

### Gaussian Plume Model
- C(x,y,z) = Q/(2πuσ_yσ_z) × exp(-y²/2σ_y²) × [exp(-(z-H)²/2σ_z²) + exp(-(z+H)²/2σ_z²)]
- **Ground-level max:** occurs at x where σ_z = H/√2
- **Pasquill classes:** A (unstable) → F (stable); A has best dispersion, F worst

---

## Framework 5: Solid & Hazardous Waste

### Waste Hierarchy (Best → Worst)
1. **Prevention** — Reduce generation
2. **Minimization** — Reduce at source
3. **Reuse** — Use again for same purpose
4. **Recycling** — Process into new material
5. **Recovery** — Energy recovery (WtE)
6. **Disposal** — Landfilling (last resort)

### Sanitary Landfill Components
- **Liner system:** HDPE/clay liner (minimum 1.5m compacted clay + 1.5mm geomembrane)
- **Leachate collection:** Gravel drainage layer + perforated pipes
- **Gas management:** Landfill gas (45-60% CH₄, 40-55% CO₂) → energy recovery
- **Final cover:** Soil cover + vegetation

### Hazardous Waste Treatment
| Method | Application |
|:-------|:-----------|
| Stabilization/Solidification | Reduce leachability |
| Incineration | Destroy organics (850-1100°C) |
| Sanitary landfill | Non-treatable hazardous waste |
| Chemical treatment | Neutralization, precipitation |
| Biological treatment | Biodegradable hazardous waste |

---

## Framework 6: Environmental Regulations

### Key Indian Environmental Laws
| Law | Year | Purpose |
|:----|:----:|:--------|
| Water Act | 1974 | Prevention of water pollution |
| Air Act | 1981 | Prevention of air pollution |
| EPA | 1986 | Umbrella environmental protection |
| EIA Notification | 2006 (amended) | Environmental clearance for projects |
| Hazardous Waste Rules | 2008 | HCW management |
| MSW Rules | 2016 | Municipal solid waste management |
| Plastic Waste Rules | 2016 | Plastic waste management |
| E-Waste Rules | 2016 | Electronic waste management |
| CRZ Notification | 2019 | Coastal zone regulation |

### EIA Process Stages
1. **Screening** — Does the project need EIA?
2. **Scoping** — Which environmental aspects are important?
3. **Baseline study** — Current environmental conditions
4. **Impact prediction** — What will the project impact?
5. **Mitigation measures** — How to reduce impacts?
6. **Public hearing** — Stakeholder consultation
7. **Decision-making** — Environmental clearance (or rejection)
8. **EMP** — Environmental Management Plan (post-clearance)

### CPCB Consent Process
- **CTE (Consent to Establish):** Before construction/establishment
- **CTO (Consent to Operate):** Before commencing operations (renewed periodically)

---

## Framework 7: Quick-Fire Interview Answers

1. **"What is BOD?"** — Biochemical Oxygen Demand: the oxygen consumed by microorganisms while decomposing organic matter. Measured over 5 days at 20°C (BOD₅).

2. **"What is the difference between BOD and COD?"** — BOD measures biodegradable organic matter (microbial decomposition); COD measures ALL oxidizable matter (chemical oxidation). COD > BOD always.

3. **"What is an activated sludge process?"** — Biological treatment where microorganisms (activated sludge) in an aeration tank decompose organic matter. Mixed liquor (MLSS) is settled in a secondary clarifier, and settled sludge is returned (RAS).

4. **"What is the Streeter-Phelps equation?"** — Models DO sag in a river after wastewater discharge. It balances deoxygenation (BOD decay) against reaeration (atmospheric oxygen transfer).

5. **"What is the difference between primary and secondary treatment?"** — Primary removes solids by physical processes (sedimentation). Secondary removes dissolved organics by biological processes (activated sludge, trickling filter).

6. **"What is ESP?"** — Electrostatic Precipitator: removes fine particulate matter using electric field. Gas passes through corona discharge, particles acquire charge, collect on plates. Efficiency > 99%.

7. **"What is EIA?"** — Environmental Impact Assessment: systematic process to identify, predict, and evaluate environmental effects of a project before it is approved.

8. **"What is the difference between CTE and CTO?"** — CTE (Consent to Establish) is obtained before construction. CTO (Consent to Operate) is obtained before starting operations. Both from SPCB.

9. **"What is the BOD/COD ratio?"** — Indicates biodegradability. Ratio > 0.5 = easily biodegradable. Ratio < 0.3 = hardly biodegradable. Important for selecting treatment process.

10. **"What is anaerobic digestion?"** — Biological process where microorganisms break down organic matter WITHOUT oxygen. Produces biogas (60% CH₄ + 40% CO₂). Used for sludge treatment and high-strength wastewater.

---

## Last-Minute Checklist

- [ ] IS 10500 standards for 4+ parameters
- [ ] CPCB effluent discharge standards (BOD, COD, TSS)
- [ ] BOD kinetics formulas (y_t, temperature correction)
- [ ] Streeter-Phelps critical time and deficit formulas
- [ ] Wastewater treatment train (primary → secondary → tertiary)
- [ ] NAAQS for PM₂.₅, PM₁₀, SO₂, NOₓ
- [ ] Air pollution control device comparison (ESP vs baghouse vs scrubber)
- [ ] Waste hierarchy (prevention → disposal)
- [ ] EIA process steps
- [ ] Key Indian environmental laws (Water Act, Air Act, EPA)
- [ ] BOD/COD ratio meaning
- [ ] Difference between CTE and CTO

---

## Cross-Links

**Study:**
→ [Environmental Engineering Full Reference](environmental-engineering.md)
→ [Wastewater Engineering](../hwre/wastewater/wastewater-engineering.md)
→ [Role Study Plan](role-study-plan.md)

**Deeper:**
→ [Water Resources Engineering](../hwre/water_resources/water-resources-engineering.md)
→ [Water Supply](../hwre/water_supply/water-supply.md)
→ [Hydrology](../hwre/hydrology/hydrology.md)

**Interview:**
→ [Technical Interview Bank](../../prep/interview/technical/technical-interview-bank.md)
→ [Behavioral Guide](../../prep/behavioral/behavioral-interview-guide.md)

---

*Last updated: 2026-09-04*
