# Hydrologist — Role Study Plan

## Role Overview

The Hydrologist role targets **water resources agencies** (CWC, CWRBM, NIH, NWDA), **PSUs** (NHPC, WAPCOS, Brahmaputra Board), **consulting firms** (AECOM, Mott MacDonald, WSP), and **research institutions** (IITs, NITs, CSIR-NIO). The role requires deep expertise in rainfall-runoff modeling, flood frequency analysis, watershed hydrology, and sediment transport — complementing the broader Water Resources Engineer role with specialized hydrological focus.

**Who targets this role:** M.Tech Hydrology/Water Resources, B.Tech civil with strong math/stats background, GATE qualified (Water Resources Engineering paper).

---

## 3–4 Highest-Value Preparation Blocks

### Topic 1: Rainfall-Runoff Analysis & Unit Hydrograph Theory

#### Why This Matters
Unit hydrograph (UH) theory is the most frequently tested hydrology topic in interviews. It connects rainfall to flood peaks — the fundamental problem of engineering hydrology.

#### What to Learn
- [ ] Hydrologic cycle and catchment response
- [ ] Rainfall excess (effective rainfall) computation
- [ ] S-curve method for UH derivation
- [ ] Unit hydrograph derivation from observed data
- [ ] S-curve lagging and UH of different durations
- [ ] Instantaneous Unit Hydrograph (IUH) — Snyder's, Snyder's modified
- [ ] Clark, Snyder, and SCS unit hydrograph methods
- [ ] Flood hydrograph analysis: base flow separation, lag time, time to peak

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`hydrology.md`](hydrology.md) | Full UH theory, Muskingum, groundwater | Full |
| [`sediment-transport.md`](sediment-transport.md) | Erosion and sediment yield | Reference |

#### Worked Example
**Problem:** A 4-hour storm produces the following excess rainfall and direct runoff: Time (hr): 0, 2, 4, 6, 8, 10, 12; Excess rainfall (cm): -, 2.5, -, 1.5, -, -, -; DRH (m³/s): 0, 50, 120, 80, 40, 10, 0. Derive the 2-hour unit hydrograph.

**Solution:**
1. **Total excess rainfall:** P₁ = 2.5 cm (0-4 hr), P₂ = 1.5 cm (4-8 hr)
2. **Use S-curve method:**
   - Construct S-curve by summing DRH contributions (shifted by storm duration)
   - Subtract S-curve shifted by 4 hr to get 4-hr UH
   - Lag S-curve by 2 hr to get 2-hr UH ordinates
3. **2-hr UH ordinates:** Divide S-curve increment by 2hr excess rainfall rate
4. **Verification:** Check that Σ(UH ordinates × duration) = 1 cm of excess rainfall over catchment area

#### Practice
**Basic (3–5):**
1. Given a rainfall hyetograph and infiltration capacity curve, compute excess rainfall.
2. Derive a 4-hr UH from observed rainfall and DRH data.
3. Convert a 6-hr UH to a 2-hr UH using the S-curve method.
4. What is the difference between a unit hydrograph and an instantaneous unit hydrograph?

**Intermediate (3–5):**
5. A catchment has a 2-hr UH with peak 150 m³/s at 3 hr. A storm produces 3 cm excess rain in first 2 hr and 2 cm in next 2 hr. Find the resulting flood hydrograph.
6. Use Snyder's method to derive a unit hydrograph for a catchment: L = 25 km, L_c = 10 km, C_p = 0.6, C_t = 1.8.
7. Explain the S-curve method step by step. Why is it needed?
8. A catchment area is 50 km². Find the peak of the 1-hr UH using the SCS method (CN = 75).

**Interview-Level (5+):**
9. Derive the SCS dimensionless unit hydrograph. What assumptions does it make?
10. What are the limitations of unit hydrograph theory? When does it fail?
11. Explain Clark's method for converting a lumped model to a UH.
12. How do you handle antecedent moisture conditions in SCS-CN method?
13. Compare rational method, UH method, and SCS-CN method for peak flow estimation.

#### Interview Questions (What Interviewer Tests)
| Question | What They're Testing |
|:---------|:---------------------|
| Derive a UH from this data. | Analytical skill, time management |
| What is the S-curve? Why is it needed? | Conceptual understanding |
| What are the limitations of UH theory? | Critical thinking |
| How do you handle multi-storm events? | Application to real problems |
| Compare Snyder and SCS methods. | Methodology comparison |

#### Common Mistakes
- **Not checking** that the UH ordinates sum to 1 cm over the catchment area
- **Confusing** effective rainfall with total rainfall
- **Forgetting** to separate base flow before deriving UH
- **Applying** UH to very small catchments (< 5 km²) where assumptions break down
- **Not shifting** the S-curve correctly when deriving UH for different durations

#### Completion Criterion
✅ Can derive a UH of any duration from observed data in under 10 minutes
✅ Can explain the S-curve method completely
✅ Can compare 3+ UH methods and choose appropriately
✅ Can handle multi-storm events using superposition

---

### Topic 2: Flood Frequency Analysis & Statistical Hydrology

#### Why This Matters
Flood frequency analysis determines the design discharge for bridges, culverts, dams, and floodplain mapping. Every hydrology interview will include this topic.

#### What to Learn
- [ ] Return period, probability of exceedance: T = 1/P
- [ ] Gumbel (EV1) distribution for flood frequency
- [ ] Log-Pearson Type III distribution (USGS/CWC standard)
- [ ] Weibull plotting position formula: P = m/(n+1)
- [ ] Parameter estimation: method of moments, L-moments
- [ ] Confidence intervals for estimated quantiles
- [ ] Regional flood frequency analysis basics

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`hydrology.md`](hydrology.md) | Flood frequency, statistical methods | Full |
| [`water-resources-engineering.md`](../water_resources/water-resources-engineering.md) | Design floods, reservoir design | Reference |

#### Worked Example
**Problem:** Annual maximum flood data (m³/s): 120, 180, 250, 320, 150, 200, 280, 160, 350, 140. Estimate the 100-year flood using Gumbel's method.

**Solution:**
1. **Compute statistics:** x̄ = 215 m³/s, σ = 77.3 m³/s
2. **Gumbel parameters:**
   - α = π/(σ√6) = π/(77.3×2.449) = 0.0166
   - β = x̄ - 0.5772/α = 215 - 34.8 = 180.2
3. **For T = 100 years:** y_T = -ln(-ln(1-1/T)) = -ln(-ln(0.99)) = 4.600
4. **x_T = β + y_T/α** = 180.2 + 4.600/0.0166 = 180.2 + 277.1 = **457.3 m³/s**

#### Practice
**Basic (3–5):**
1. What is the return period of a flood with 2% annual exceedance probability?
2. Given 15 annual maximum flood values, rank them and compute Weibull plotting positions.
3. Fit a Gumbel distribution to a dataset. Estimate the 50-year flood.
4. What is the difference between an extreme value distribution and a normal distribution?

**Intermediate (3–5):**
5. Compute the 100-year, 50-year, and 10-year floods using Log-Pearson Type III.
6. Create a flood frequency curve (probability paper plot).
7. What is the 90% confidence interval for the 100-year flood estimate?
8. Explain regional flood frequency analysis. When is it used?

**Interview-Level (5+):**
9. Why is Log-Pearson Type III preferred over Gumbel for flood frequency?
10. What are the limitations of using only 30 years of data for a 100-year flood estimate?
11. How does climate change affect flood frequency analysis?
12. Explain L-moments and why they are preferred over method of moments.
13. What is the difference between at-site and regional frequency analysis?

#### Common Mistakes
- **Confusing** return period with frequency (T = 100 means 1% chance per year, NOT "once in 100 years")
- **Using** the wrong plotting position formula (Weibull: m/(n+1), not m/n)
- **Not checking** for outliers before fitting distributions
- **Applying** normal distribution to flood data (floods are typically skewed)

#### Completion Criterion
✅ Can compute flood quantiles using Gumbel and Log-Pearson III methods
✅ Can construct flood frequency curves
✅ Can explain confidence intervals and their meaning
✅ Can discuss limitations and regional approaches

---

### Topic 3: Watershed Modeling & Hydrologic Software

#### Why This Matters
Modern hydrology relies on computational tools. Knowing HEC-HMS, HEC-RAS, SWAT, MIKE, and GIS-based watershed analysis is essential for consulting and research roles.

#### What to Learn
- [ ] HEC-HMS: basin model, meteorological model, control specifications
- [ ] Loss methods: SCS-CN, Green-Ampt, initial/constant
- [ ] Transform methods: SCS UH, Clark UH, ModClark
- [ ] Routing: Muskingum, kinematic wave
- [ ] HEC-RAS: steady/unsteady flow, floodplain mapping
- [ ] GIS for hydrology: watershed delineation, DEM processing, slope/aspect
- [ ] ArcSWAT basics: watershed delineation, HRU definition, model calibration
- [ ] Google Earth Engine for large-scale hydrologic analysis

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`hydrology.md`](hydrology.md) | Muskingum, routing methods | Full |
| *GATE Civil Notes — Hydrology section* | Exam-oriented fundamentals | Reference |

#### Worked Example
**HEC-HMS Setup for a Small Catchment:**
1. **Create basin model:** Define subbasins, reaches, junctions
2. **Define subbasin properties:** Area, centroid, longest flow path, slope
3. **Select loss method:** SCS-CN (CN = 75 for good forest cover)
4. **Select transform method:** SCS Unit Hydrograph (T_p = D/2 + 0.6T_lag)
5. **Select routing method:** Muskingum (K = 1.5 hr, X = 0.25)
6. **Meteorological model:** Standard gage method with rainfall input
7. **Control specifications:** Start/end time, time step = 15 min
8. **Run and analyze:** Peak flow, time to peak, runoff volume

#### Practice (Software-Oriented)
1. Describe the complete HEC-HMS workflow for a 100 km² catchment.
2. What are the differences between SCS-CN and Green-Ampt loss methods?
3. In HEC-RAS, explain the difference between 1D and 2D flow simulation.
4. How would you delineate a watershed using DEM data in QGIS?
5. What is HRU in SWAT? How is it defined?
6. Describe the process of calibrating an HEC-HMS model.
7. What are the key inputs for a flood forecasting model?

#### Common Mistakes
- **Using default parameters** without local calibration
- **Not validating** model results against observed data
- **Choosing wrong time step** (too coarse misses peak, too fine causes noise)
- **Ignoring** model uncertainty
- **Not documenting** model assumptions and limitations

#### Completion Criterion
✅ Can set up an HEC-HMS model from scratch
✅ Can delineate a watershed from DEM
✅ Can compare and select appropriate loss/transform/routing methods
✅ Can calibrate and validate a hydrologic model

---

### Topic 4: Sediment Transport & River Engineering

#### Why This Matters
Sediment transport is critical for river engineering, dam design, bridge scour, and environmental flows. It's a specialized topic that distinguishes hydrologists from general water resources engineers.

#### What to Learn
- [ ] Sediment transport modes: bed load, suspended load, wash load
- [ ] HEC-RAS sediment transport: empirical formulas (Meyer-Peter & Müller, Einstein)
- [ ] Shields diagram and critical shear stress
- [ ] Bed forms: ripples, dunes, plane bed, antidunes
- [ ] Scour at bridge piers: contraction, local, long-term
- [ ] Sediment yield estimation: USLE, RUSLE
- [ ] Reservoir sedimentation and sediment management
- [ ] Environmental sediment flows

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`sediment-transport.md`](sediment-transport.md) | Bed load, suspended load, scour | Full |
| [`hydrology.md`](hydrology.md) | Watershed erosion context | Reference |

#### Worked Example
**Problem:** A rectangular channel (width = 10m, depth = 2m) has bed material with d₅₀ = 0.5 mm. The shear velocity is 0.08 m/s. Determine if the bed material will move using the Shields diagram.

**Solution:**
1. **Compute dimensionless shear stress (Shields parameter):**
   - τ* = τ₀ / ((ρ_s - ρ)gd₅₀)
   - τ₀ = ρu²*_f = 1000 × 0.08² = 6.4 Pa
   - τ* = 6.4 / ((2650 - 1000) × 9.81 × 0.0005) = 6.4 / 8.09 = **0.791**

2. **Check Shields diagram:** For d₅₀ = 0.5mm and Re* = u*_f × d₅₀ / ν = 0.08 × 0.0005 / 10⁻⁶ = 40
   - Critical Shields parameter ≈ 0.05–0.06 for this Re*
   - Since τ* = 0.791 >> 0.06, **bed material will definitely move** (active transport)

#### Practice
**Basic (3–5):**
1. What are the three modes of sediment transport? Give an example of each.
2. Explain the Shields diagram. What is the critical shear stress?
3. What are bed forms? Describe the sequence as flow velocity increases.
4. What is bridge scour? Name 3 types.

**Intermediate (3–5):**
5. Estimate bed load transport using Meyer-Peter & Müller formula for given conditions.
6. Calculate the sediment yield of a catchment using USLE (provide R, K, C, P, LS values).
7. A reservoir receives 500,000 m³ of sediment annually. If the trap efficiency is 80%, how much sediment passes through?
8. Explain the difference between live-bed scour and clear-water scour at bridge piers.

**Interview-Level (5+):**
9. How does climate change affect sediment transport in rivers?
10. Explain sediment routing in reservoirs. What is the sediment rating curve?
11. What are the challenges in measuring suspended sediment concentration?
12. How would you design a sediment bypass tunnel for a dam?

#### Common Mistakes
- **Confusing** bed load with suspended load (bed load rolls/slides; suspended is carried in flow)
- **Not knowing** that bed forms increase roughness (and thus resistance to flow)
- **Ignoring** sediment in dam design (reservoir sedimentation reduces storage life)
- **Using** uniform sediment assumptions when real beds are graded

#### Completion Criterion
✅ Can determine if bed material moves using Shields criterion
✅ Can compute sediment transport rates
✅ Can explain bridge scour and mitigation methods
✅ Can describe sediment management in reservoirs

---

## Mock Test (45 Minutes)

| # | Question | Topic | Marks |
|---|:---------|:------|------:|
| 1 | A 6-hour storm produces: 0-2hr: 2cm, 2-4hr: 4cm, 4-6hr: 1cm excess rainfall. The 2-hr UH ordinates are [0, 20, 50, 35, 15, 5, 0] m³/s. Find the flood hydrograph. | UH | 20 |
| 2 | Annual max flows (m³/s): 150, 200, 350, 180, 450, 220, 300, 280, 400, 160, 250, 320. Compute the 50-year flood using Gumbel's method. | Flood Frequency | 20 |
| 3 | Describe the complete HEC-HMS setup for a 200 km² catchment including loss method, transform method, and routing. | Software | 15 |
| 4 | A bridge pier (width = 2m) in a river with flow depth = 3m, velocity = 2 m/s. Estimate the scour depth using HEC-18 formula. | Sediment/Scour | 15 |
| 5 | What is the difference between unit hydrograph and instantaneous unit hydrograph? Derive IUH from S-curve. | UH Theory | 15 |
| 6 | Explain the SCS-CN method. How do you account for antecedent moisture conditions? | Rainfall-Runoff | 15 |
| | | **Total** | **100** |

---

## Interview Strategy

### Technical Interview (15–20 minutes)
1. **Start with your strongest topic** — UH derivation, flood frequency, or software
2. **Show the math** — interviewers want to see your calculation process
3. **Draw the hydrograph** — always sketch the response curve
4. **Connect to practice** — mention real projects, datasets, software used

### Hydrology-Specific Tips
- Know the **return period** concept cold (not "once in 100 years")
- Be ready to **derive a UH on the board** (practice this 3+ times)
- Know **HEC-HMS** workflow step by step
- Understand **uncertainty** in hydrological estimates

---

## Cross-Links

**Next:**
→ [Hydrology Rapid Revision](hydrology-rapid-revision.md) — Last-minute formula cheat sheet

**Study:**
→ [Hydrology Full Reference](hydrology.md) — Complete hydrology theory
→ [Sediment Transport](sediment-transport.md) — Detailed sediment mechanics
→ [Water Resources Engineering](../water_resources/water-resources-engineering.md)
→ [Open Channel Flow](../open_channel_flow/open-channel-flow.md)

**Interview:**
→ [Technical Interview Bank](../../../prep/interview/technical/technical-interview-bank.md)
→ [Behavioral Guide](../../../prep/behavioral/behavioral-interview-guide.md)

**Related:**
→ [WRE Role Study Plan](../role-study-plan.md) — Broader water resources preparation

---

*This study plan follows the [Role Study Plan Template](../../../prep/templates/role-study-plan-template.md).*
*Last updated: 2026-09-04*
