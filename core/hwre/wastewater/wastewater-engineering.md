# Wastewater Engineering

## Overview

Wastewater engineering involves the collection, treatment, and disposal of domestic, industrial, and stormwater. It protects public health and the environment by removing contaminants before discharge or reuse.

> **Related topics:** [`water-supply.md`](../water_supply/water-supply.md) · [`irrigation-engineering.md`](../irrigation/irrigation-engineering.md) · [`../core/hwre/hydraulics/hydraulics.md`](../../core/hwre/hydraulics/hydraulics.md)

---

## Wastewater Characteristics

### Key Parameters

| Parameter | Typical Domestic WW | Significance |
|-----------|-------------------|-------------|
| BOD₅ | 200–300 mg/L | Organic pollution measure |
| COD | 400–600 mg/L | Total organic matter |
| TSS | 200–300 mg/L | Suspended solids |
| pH | 6.5–8.5 | Acidity/alkalinity |
| TN | 40–50 mg/L | Nitrogen content |
| TP | 8–12 mg/L | Phosphorus content |
| Coliforms | 10⁶–10⁸ MPN/100mL | Pathogen indicator |

### BOD vs COD
$$BOD_5 = L_0(1 - e^{-5k})$$

Where $L_0$ = ultimate BOD, $k$ = decay rate constant (day⁻¹)

**BOD/COD ratio:**
- Domestic WW: 0.5–0.6 (biodegradable)
- Industrial WW: varies; low ratio indicates refractory organics

---

## Treatment Train

### Treatment Stages

| Stage | Process | Removal | Typical Efficiency |
|-------|---------|---------|-------------------|
| **Preliminary** | Screening, grit removal | Large solids, grit | 10–15% BOD |
| **Primary** | Sedimentation | Settleable solids | 25–35% BOD, 50–70% TSS |
| **Secondary** | Biological (ASP, TF) | Dissolved organics | 85–95% BOD |
| **Tertiary** | N/P removal, filtration | Nutrients, remaining TSS | 90–99% BOD |
| **Disinfection** | Chlorination, UV, Ozone | Pathogens | 99.9% coliforms |

### Treatment Flow Diagram
```
Raw WW → Screen → Grit Chamber → Primary Clarifier → Aeration Tank → Secondary Clarifier
              ↓                                    ↓              ↓
         Grit disposal                      Return Sludge    Waste Sludge
                                                                     ↓
                                                              Thickener → Digester → Dewatering → Disposal
```

---

## Activated Sludge Process (ASP)

### Key Parameters

| Parameter | Definition | Typical Value |
|-----------|-----------|---------------|
| **F/M ratio** | $F/M = QS_0/(VX)$ | 0.2–0.5 kgBOD/kgMLSS·d |
| **MLSS** | Mixed liquor suspended solids | 1500–3000 mg/L |
| **SVI** | Sludge volume index (mL/g) | 50–150 |
| **SRT** | Solids retention time (days) | 5–15 days |
| **HRT** | Hydraulic retention time (hrs) | 4–8 hours |

### Design Equations
$$V = \frac{QS_0Y(SRT)}{X(1 + k_d \cdot SRT)}$$

Where $Y$ = yield coefficient (~0.5), $k_d$ = decay coefficient (~0.06 d⁻¹)

### Aeration Requirements
$$O_2 \text{ demand} = Q(S_0 - S)/f - 1.42\Delta X_{biomass}$$

---

## Trickling Filter

| Type | Depth | Organic Loading | Recirculation |
|------|-------|----------------|---------------|
| Low rate | 1.5–2 m | 0.08–0.32 kg/m³·d | None |
| High rate | 1.5–2 m | 0.32–1.0 kg/m³·d | 3:1–5:1 |
| Roughing | 1–2 m | 1.0–4.0+ kg/m³·d | 5:1–10:1 |

---

## Sludge Management

### Treatment Process
```
Raw Sludge → Thickening → Stabilization → Dewatering → Disposal
              (gravity/DAF)  (anaerobic/aerobic) (belt press/centrifuge)
```

### Anaerobic Digestion
$$CH_4 \text{ production} = 0.35 \times Q \times L_v \times \text{removed fraction}$$ (m³/kg COD removed)

- Biogas: 60–65% CH₄, 35–40% CO₂
- Temperature: mesophilic (35°C) or thermophilic (55°C)

---

## Worked Examples

### Example 1: BOD Calculation
**Problem:** Wastewater has $L_0 = 250$ mg/L, $k = 0.23$ d⁻¹. Find BOD₅.

**Solution:**
1. $BOD_5 = L_0(1-e^{-5k}) = 250(1-e^{-5 \times 0.23}) = 250(1-e^{-1.15})$
2. $BOD_5 = 250(1-0.317) = 250 \times 0.683 = 170.7$ mg/L

### Example 2: Aeration Tank Volume
**Problem:** Design an ASP for $Q = 10$ ML/d, $S_0 = 250$ mg/L, $S = 20$ mg/L, $X = 2500$ mg/L, $Y = 0.5$, $k_d = 0.06$ d⁻¹, $SRT = 10$ days.

**Solution:**
1. $V = QS_0 Y(SRT) / [X(1+k_d \cdot SRT)]$
2. $V = (10000 \times 0.250 \times 0.5 \times 10) / (2.5(1+0.6))$
3. $V = 12500 / 4.0 = 3125$ m³
4. $HRT = V/Q = 3125/10000 = 0.3125$ days = 7.5 hours ✓

### Example 3: F/M Ratio
**Problem:** $Q = 5$ ML/d, $S_0 = 300$ mg/L, $V = 2000$ m³, $X = 2000$ mg/L. Find F/M.

**Solution:**
1. $F/M = QS_0/(VX) = (5000 \times 0.300)/(2000 \times 2.000) = 1500/4000 = 0.375$ kgBOD/kgMLSS·d ✓ (range: 0.2–0.5)

### Example 4: Chlorination Dose
**Problem:** Plant effluent has 10⁶ coliforms/100mL. Target: < 1000 coliforms/100mL. 3-log removal needed.

**Solution:**
1. CT = 3 (for 3-log inactivation at pH 7, 20°C, Cl₂)
2. Contact time $t = 30$ min (minimum)
3. $C = CT/t = 3/0.5 = 6$ mg/L
4. Residual Cl₂ needed: 0.5 mg/L
5. Total dose = 6 + 0.5 = 6.5 mg/L

### Example 5: Sludge Production
**Problem:** ASP with $Q = 10$ ML/d, $S_0 = 250$ mg/L, $S = 20$ mg/L, $Y = 0.5$, $k_d = 0.06$ d⁻¹. Find daily sludge production.

**Solution:**
1. $\Delta X = YQ(S_0-S)/1000 - k_d V X / 1000$
2. Biomass produced = $0.5 \times 10000 \times (0.250-0.020) = 1150$ kg/d
3. Decay = $0.06 \times 3125 \times 2.5 = 469$ kg/d
4. Net sludge = $1150 - 469 = 681$ kg/d (volatile SS)
5. Total TSS = $681/0.7 = 973$ kg/d (assuming 70% volatile)

---

## 🎤 Interview Q&A

### Q1: What is the difference between BOD and COD?
**A:** BOD measures biodegradable organic matter (5-day test, 20°C, biological oxidation). COD measures total organic matter (chemical oxidation, 2–3 hours). BOD/COD ratio indicates biodegradability: > 0.5 = biodegradable, < 0.3 = refractory. COD is always ≥ BOD.

### Q2: Explain the activated sludge process.
**A:** ASP uses aerobic microorganisms to degrade organics: (1) Primary effluent enters aeration tank with MLSS (1500–3000 mg/L), (2) Microorganisms consume BOD, (3) Mixed liquor flows to secondary clarifier, (4) Settled sludge returned (RAS) to maintain biomass, (5) Excess sludge wasted (WAS). Key parameters: F/M (0.2–0.5), SRT (5–15 days), HRT (4–8 hrs).

### Q3: What is SVI and what does it indicate?
**A:** Sludge Volume Index: SVI = (Settled sludge volume in 30 min × 1000) / MLSS (mg/L). Units: mL/g. SVI < 100: good settling, 100–200: moderate, > 200: bulking sludge (poor settling). Causes of bulking: filamentous bacteria, low DO, high F/M.

### Q4: What is tertiary treatment and when is it needed?
**A:** Tertiary treatment removes nutrients (N, P) and remaining TSS after secondary treatment. Needed when: (1) Discharge to sensitive water bodies (eutrophication risk), (2) Water reuse requirements, (3) Stricter regulatory standards. Processes: nitrification-denitrification (N), chemical/biological P removal, sand filtration, UV disinfection.

### Q5: Compare trickling filter and ASP.
**A:** Trickling filter: fixed-film, passive aeration, lower energy, robust to shock loads, lower efficiency (80–85% BOD), simpler operation. ASP: suspended growth, mechanical aeration, higher efficiency (90–95% BOD), more flexible, higher energy cost. Trickling filters suit small communities; ASP suits larger plants.

---

## Quick Reference

| Formula | Equation |
|---------|----------|
| BOD at time t | $BOD_t = L_0(1-e^{-kt})$ |
| F/M ratio | $F/M = QS_0/(VX)$ |
| SRT | $\theta_c = VX / (Q_w X_w + Q_e X_e)$ |
| HRT | $\theta = V/Q$ |
| Sludge production | $\Delta X = YQ(S_0-S) - k_dVX$ |
| CH₄ production | $0.35 \times Q \times L_v \times \text{removed}$ |
| Chlorination | $CT = C \times t$ |

---

## Discharge Standards (CPCB India)

| Parameter | Inland Surface | Land Disposal |
|-----------|---------------|---------------|
| BOD₅ | < 30 mg/L | < 100 mg/L |
| COD | < 250 mg/L | — |
| TSS | < 100 mg/L | — |
| pH | 5.5–9.0 | 6.0–8.5 |
| Fecal coliform | < 1000 MPN/100mL | — |

---

## 🗺️ Subject Roadmap

```
Beginner                    Intermediate                   Advanced                      Interview
─────────────────────────────────────────────────────────────────────────────────────────────────────
WW characteristics   →  BOD/COD kinetics            →  Nutrient removal (N,P)       →  BOD test interpretation
Treatment stages     →  Activated sludge process     →  Membrane bioreactors         →  F/M ratio and SRT
Sedimentation        →  Trickling filters             →  Resource recovery            →  Why secondary before tertiary
Disinfection         →  Sludge treatment              →  Energy-neutral plants       →  Chlorination vs UV vs Ozone
CPCB standards       →  Design of ASP/TF             →  Advanced oxidation           →  Discharge standards
```

> **Priority:** `P1 — High Priority` · **Tags:** `ENVIRONMENTAL` `HWRE`

---

## ❓ Question Bank (Selected)

### A. Basic Concept
1. What is BOD and how does it differ from COD?
2. What are the stages of wastewater treatment?
3. What is the Streeter-Phelps oxygen sag curve?

### B. WHY Questions
1. **Why** is secondary treatment needed after primary?
   - Primary removes only 25–35% BOD (settleable solids). Secondary uses biological processes to remove dissolved organics (85–95% BOD).

2. **Why** is SVI important for ASP operation?
   - SVI > 200 indicates bulking sludge (poor settling), which washes out of the secondary clarifier and degrades effluent quality.

3. **Why** is tertiary treatment needed for sensitive water bodies?
   - Secondary effluent still contains nutrients (N, P) that cause eutrophication. Tertiary removes these to protect receiving waters.

---

## 🎤 Interview Answer Format

### High-Value Q: "Explain the activated sludge process."

**30-second answer:**
"ASP is a suspended-growth biological process where microorganisms degrade organic matter in an aeration tank. Mixed liquor flows to a clarifier where sludge settles; part is returned as RAS, excess is wasted as WAS. Key parameters: F/M ratio, SRT, MLSS, DO."

**Key equations:**
$F/M = QS_0/(VX)$, $\theta_c = VX/(Q_wX_w + Q_eX_e)$

---

## 🔗 Cross-Links

- [`water-supply.md`](../water_supply/water-supply.md) — Water treatment
- [`environmental-engineering.md`](../../environmental/environmental-engineering.md) — BOD kinetics, DO sag
- [`hydrology.md`](../hydrology/hydrology.md) — Stormwater, urban hydrology

---

## References

* [awesome-civil-engineering](https://github.com/awesome-civil-engineering/awesome-civil-engineering)
