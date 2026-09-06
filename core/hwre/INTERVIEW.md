# HWRE — Interview Q&A Bank

> Dedicated HWRE interview questions with model answers. Complements the general [`technical-interview-bank.md`](../../prep/interview/technical/technical-interview-bank.md).

## Section 1: Fluid Mechanics & Hydraulics

### Q1. State Bernoulli's equation and its assumptions.
**A:** `P/γ + V²/2g + z = const` along a streamline. Assumptions: (1) steady flow, (2) incompressible fluid, (3) frictionless (inviscid) flow, (4) along a streamline. With losses: add `h_L` on the downstream side.

### Q2. What is the Reynolds number and why does it matter?
**A:** `Re = ρVD/μ = VD/ν` — ratio of inertial to viscous forces. Laminar: Re < 2000; transition: 2000–4000; turbulent: > 4000. It determines friction factor, mixing, and heat/mass transfer.

### Q3. Explain the Darcy-Weisbach equation and the Moody diagram.
**A:** `h_f = f(L/D)(V²/2g)`. The friction factor f depends on Re and relative roughness ε/D. Moody diagram plots f vs Re for various ε/D: laminar `f = 64/Re`, transition, and fully turbulent zones.

### Q4. What is NPSH and why does it matter?
**A:** Net Positive Suction Head — the head available at the pump suction to prevent cavitation. `NPSH_A = P_atm/γ − P_v/γ − h_s − h_f`. Cavitation occurs when `NPSH_A < NPSH_R`. Prevention: lower pump, larger suction pipe, reduce suction losses.

### Q5. What is the difference between a pump and a turbine?
**A:** Pump adds energy to fluid (`P = γQH/η`); turbine extracts energy from fluid (`P = γQHη`). Pump specific speed: `N_s = N√Q/H^(3/4)`; turbine: `N_s = N√P/H^(5/4)`.

## Section 2: Open Channel Flow

### Q6. What is specific energy and critical depth?
**A:** Specific energy `E = y + V²/2g` — energy per unit weight relative to the channel bed. Critical depth is where E is minimum (`E_min = 1.5y_c`), at `Fr = 1`. For rectangular: `y_c = (q²/g)^(1/3)`.

### Q7. Explain the hydraulic jump and its applications.
**A:** Sudden transition from supercritical to subcritical flow. Conjugate depth: `y₂/y₁ = 0.5(√(1+8Fr₁²) − 1)`. Energy loss: `ΔE = (y₂−y₁)³/(4y₁y₂)`. Applications: stilling basins, energy dissipation, flow measurement.

### Q8. What are GVF profiles and how do you classify them?
**A:** Gradually varied flow profiles classified by bed slope (M/S/C/A/H) and zone (1/2/3). Draw y_n and y_c lines. Zone 1: y above both; Zone 2: between; Zone 3: below both. E.g., M1 (backwater, dam), M2 (drawdown, weir), M3 (below normal depth).

### Q9. What is the difference between Chezy and Manning equations?
**A:** Chezy: `V = C√(RS)`; Manning: `V = (1/n)R^(2/3)S^(1/2)`. Manning is empirical, more accurate for natural channels. Relation: `C = R^(1/6)/n`.

### Q10. What is the Froude number and its significance?
**A:** `Fr = V/√(gD_h)` — ratio of inertial to gravitational forces. Fr < 1: subcritical (downstream control); Fr = 1: critical; Fr > 1: supercritical (upstream control). Governs wave propagation and controls.

## Section 3: Hydrology

### Q11. Explain the unit hydrograph concept and its assumptions.
**A:** DRH from 1 unit (e.g., 1 cm) of effective rainfall over a catchment for a specified duration. Assumptions: (1) linearity (runoff ∝ rainfall excess), (2) time-invariance (same response regardless of when rainfall occurs), (3) uniform rainfall distribution.

### Q12. How do you convert a UH of one duration to another?
**A:** S-curve method: (1) sum UH ordinates shifted by duration D to get S-curve; (2) shift S-curve by new duration D'; (3) difference = `(D'/D) ×` new UH ordinates.

### Q13. What is the Muskingum method for flood routing?
**A:** Channel routing using storage `S = K[XI + (1−X)O]`. Routing equation: `O₂ = C₀I₂ + C₁I₁ + C₂O₁`. K = travel time, X = weighting factor (0–0.5). Verify `C₀ + C₁ + C₂ = 1`.

### Q14. What is the difference between Muskingum and level-pool routing?
**A:** Muskingum: channel routing with wedge + prism storage (X ≠ 0). Level-pool: reservoir routing with horizontal water surface (X = 0), uses storage-indication method.

### Q15. How do you perform flood frequency analysis?
**A:** Fit a distribution (Gumbel EV1 or Log-Pearson III) to annual peak flows. Gumbel: `x_T = x̄ + K_Tσ`. Return period T = 1/P. Risk: `R = 1 − (1 − 1/T)^n`.

### Q16. What is the Rational method and its limitations?
**A:** `Q = CiA/360` (A in ha, i in mm/hr). Assumes uniform rainfall, constant intensity, small catchment (< 200 km²). Limitations: no storage, no routing, empirical C.

## Section 4: Groundwater

### Q17. State Darcy's law and its validity.
**A:** `Q = KiA` — discharge proportional to hydraulic gradient. Valid for laminar flow (Re < 1–10). Seepage velocity: `v_s = Ki/n`.

### Q18. What is the difference between confined and unconfined aquifers?
**A:** Confined: bounded by aquitards, artesian pressure, storativity 10⁻⁵–10⁻³ (elastic). Unconfined: water table surface, storativity = specific yield 0.01–0.30 (gravity drainage).

### Q19. Explain the Theis equation and its use.
**A:** `s = (Q/4πT)W(u)`, `u = r²S/(4Tt)`. Used for pumping test analysis to determine T and S, and to predict drawdown. Cooper-Jacob simplification valid when u < 0.01.

### Q20. What is the Thiem equation?
**A:** Steady-state confined flow: `Q = 2πT(h₂−h₁)/ln(r₂/r₁)`. Used to determine T from steady pumping test with two observation wells.

### Q21. What is specific capacity and well efficiency?
**A:** Specific capacity `S_c = Q/s` — productivity indicator. Well efficiency = aquifer loss / total loss × 100%. From step-drawdown: `s = BQ + CQ²`.

## Section 5: Water Resources

### Q22. How do you determine reservoir storage capacity?
**A:** Mass curve (Rippl) method: (1) plot cumulative inflow vs time; (2) draw maximum demand line from peak; (3) maximum vertical departure = required storage. For flood control, use level-pool routing with design inflow hydrograph.

### Q23. What is firm yield vs secondary yield?
**A:** Firm yield: minimum dependable supply (95% of years). Secondary yield: additional water in average/wet years. Firm yield determines reservoir size for water supply.

### Q24. What are environmental flows and why are they important?
**A:** Minimum flow regimes to sustain riverine ecosystems: baseflow for habitat, flood pulses for sediment transport and floodplain connectivity, seasonal patterns for spawning. Determined by hydrological, hydraulic, or holistic methods.

### Q25. What is the difference between Lacey and Kennedy canal theories?
**A:** Kennedy: critical velocity ratio m, no width-depth relation. Lacey: regime theory with silt factor f, gives velocity `V = (Qf²/140)^(1/6)` and perimeter `P = 2.67√Q`.

## Section 6: Sediment Transport

### Q26. What is the Shields parameter and critical shear stress?
**A:** `τ* = τ₀/((ρ_s−ρ)gd)` — dimensionless bed shear. Incipient motion at `τ_c* ≈ 0.047` for uniform grains. Critical shear stress: `τ_c = θ_c(ρ_s−ρ)gd`.

### Q27. What is the difference between bed load and suspended load?
**A:** Bed load: rolls/slides/saltates along bed (MPM formula). Suspended load: carried by turbulence (Rouse profile `c/c_a = (y_a/y)^Z`). Wash load: very fine, not in equilibrium with bed.

### Q28. What causes bridge pier scour?
**A:** Local acceleration and vortex formation around pier. HEC-18: `y_s/y₁ = 2.0K₁K₂K₃K₄(a/y₁)^0.35 Fr^0.43`. Clear-water (V < V_c) vs live-bed (V > V_c) scour.

## Section 7: Turbulence & CFD

### Q29. What is the difference between RANS, LES, and DNS?
**A:** RANS: time-averaged equations, all turbulence modeled, low cost. LES: large scales resolved, small scales modeled (subgrid), high cost. DNS: all scales resolved, extremely high cost, low Re only.

### Q30. What is the k-ε vs k-ω SST model?
**A:** k-ε: robust for high-Re free shear flows, poor near walls. k-ω: good near walls. SST blends k-ω near walls with k-ε in free stream — best for adverse pressure gradients and separation.

### Q31. What is y+ and why does it matter?
**A:** `y⁺ = yu_τ/ν` — dimensionless wall distance. y⁺ < 5: resolve viscous sublayer; 30–300: wall functions; > 300: log-law region. Determines mesh requirements and near-wall treatment.

## Section 8: Irrigation & Water Supply

### Q32. What is duty and delta?
**A:** Duty D: area irrigated per cumec (hectares/cumec). Delta Δ: total water depth required (m). Relationship: `D × Δ = 8.64 × B` (B = base period in days).

### Q33. What are the irrigation efficiencies?
**A:** Conveyance `E_c` (delivered/diverted, 70–90%), application `E_a` (stored/delivered, 50–85%), overall `E_o = E_c × E_a` (40–75%).

### Q34. How do you forecast population?
**A:** Arithmetic `P_n = P₀ + nx̄` (stable cities), geometric `P_n = P₀(1+r)^n` (growing), incremental (moderate growth), logistic (S-shaped, saturation).

### Q35. What is the difference between slow sand and rapid sand filters?
**A:** Slow sand: 0.1–0.3 m/h, biological (schmutzdecke), scraping cleaning, no coagulation needed. Rapid sand: 4–6 m/h, physical-chemical, backwashing, coagulation required.

## Section 9: Wastewater

### Q36. What is BOD and how is it measured?
**A:** Biochemical oxygen demand — oxygen consumed by microorganisms decomposing organics over 5 days at 20°C. `BOD₅ = L₀(1 − e^(−5k))`. BOD/COD ratio 0.5–0.6 indicates biodegradability.

### Q37. Explain the Activated Sludge Process.
**A:** Biological secondary treatment: aeration tank (microorganisms consume organics) + secondary clarifier (sludge settling) + return sludge. Key parameters: F/M ratio 0.2–0.5, MLSS 1500–3000 mg/L, SRT 5–15 days, HRT 4–8 hr.

### Q38. What is the difference between SRT and HRT?
**A:** SRT (solids retention time): average time solids stay in system = `VX/(Q_wX_r)`. HRT (hydraulic retention time): average time water stays = `V/Q`. SRT controls biological growth; HRT controls physical contact.

## Section 10: Modelling

### Q39. Describe the HEC-HMS → HEC-RAS workflow.
**A:** (1) HEC-HMS: build basin model, apply loss (SCS-CN/Green-Ampt), transform (UH/Snyder/Clark), route (Muskingum); (2) export hydrograph; (3) HEC-RAS: build geometry (cross-sections), import hydrograph as boundary condition, run steady/unsteady analysis; (4) RAS Mapper: map flood inundation.

### Q40. What is the difference between steady and unsteady HEC-RAS?
**A:** Steady: constant or gradually varied discharge, standard step method, simpler. Unsteady: time-varying hydrographs, solves Saint-Venant equations, needed for flood routing, dam breach, tidal flows.

### Q41. What is RAS Mapper used for?
**A:** GIS-based pre/post-processing: terrain processing, cross-section extraction, floodplain mapping, velocity/depth visualization, dam breach inundation.

## Quick Reference: Top 10 Most Likely Questions

1. State Bernoulli's equation and its assumptions.
2. What is the hydraulic jump and how do you compute conjugate depths?
3. Explain the unit hydrograph concept.
4. How do you route a flood (Muskingum vs level-pool)?
5. What is the Theis equation used for?
6. How do you determine reservoir storage capacity?
7. What is the difference between confined and unconfined aquifers?
8. What is the Shields parameter?
9. Describe the HEC-HMS → HEC-RAS workflow.
10. What is the difference between RANS, LES, and DNS?

## Related

- [MASTER_INDEX.md](MASTER_INDEX.md) · [TRAPS.md](TRAPS.md) · [General Interview Bank](../../prep/interview/technical/technical-interview-bank.md) · [Project Defense Guide](../../prep/interview/technical/project-defense-guide.md)