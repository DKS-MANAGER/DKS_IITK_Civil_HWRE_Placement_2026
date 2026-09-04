# Hydrologist — Rapid Revision Sheet

> Last-minute cheat sheet for hydrology and flood analysis interviews.

---

## Framework 1: Rainfall-Runoff Quick Reference

### Key Definitions
| Term | Meaning |
|:-----|:--------|
| Rainfall excess | Total rainfall minus losses (infiltration, interception, depression storage) |
| Effective rainfall | Rainfall that contributes to direct runoff |
| Base flow | Groundwater contribution to streamflow (slow, steady) |
| DRH | Direct Runoff Hydrograph (total hydrograph minus base flow) |
| UH | Unit Hydrograph: DRH from 1 cm of excess rainfall |

### Rational Method
- Q = CIA/360 (Q in m³/s, C dimensionless, I in mm/hr, A in km²)
- Use for small catchments (< 5 km²)
- C depends on land use: 0.1 (forest) to 0.9 (paved)

### SCS-CN Method
- **CN (Curve Number):** 0-100, higher = more runoff
- **Runoff depth:** Q = (P - 0.2S)² / (P + 0.8S) when P > 0.2S
- **S = 25400/CN - 254** (S in mm)
- **Antecedent Moisture Conditions:**
  - AMC-I (dry): CN₁ = 4.2CN/(10 - 0.058CN)
  - AMC-II (normal): CN
  - AMC-III (wet): CN₃ = 23CN/(10 + 0.13CN)

### Unit Hydrograph Methods
| Method | Parameters | When Used |
|:-------|:-----------|:----------|
| SCS UH | T_p, Q_p | Simple, standard |
| Snyder | C_p, C_t | Regional, ungauged |
| Clark | T_c, R | Lumped model |
| ModClark | Gridded | Distributed model |

### S-Curve Method
1. Sum UH ordinates cumulatively → S-curve
2. Lag S-curve by T (desired duration) → S_t curve
3. Subtract: S - S_t → T-hr UH ordinates
4. Divide by T to get per-hour ordinates

### UH Quick Formulas (SCS)
- **Lag time:** T_lag = 0.6T_c (T_c in hours)
- **Time to peak:** T_p = D/2 + T_lag (D = excess rain duration)
- **Peak discharge:** Q_p = 2.08A/T_p (A in km², T_p in hours, Q_p in m³/s)

---

## Framework 2: Flood Frequency Quick Reference

### Key Formulas
| Distribution | Parameters | Formula |
|:-------------|:-----------|:--------|
| Gumbel (EV1) | α, β | x_T = β - (1/α)ln(-ln(1-1/T)) |
| Log-Pearson III | μ_log, σ_log, K | log(x_T) = μ_log + K·σ_log |
| Weibull (plotting) | m, n | P = m/(n+1) |

### Gumbel Distribution
- α = π/(σ√6) ≈ 1.2825/σ
- β = x̄ - 0.5772/α = x̄ - 0.45σ
- **Gumbel reduced variate:** y_T = -ln(-ln(1-1/T))
  - T=10: y=2.250; T=50: y=3.902; T=100: y=4.600; T=500: y=6.215

### Return Period Conversion
- P(exceedance in n years) = 1 - (1 - 1/T)^n
- 100-year flood in 30 years: P = 1 - (0.99)^30 = 26%

### Common Mistakes to Remember
- **T = 100** means 1% chance EACH year, not "happens once in 100 years"
- **Always use** m/(n+1) for plotting position (not m/n)
- **Floods are skewed** — don't assume normal distribution
- **Short records** (< 30 years) have large uncertainty for long return periods

---

## Framework 3: Muskingum Routing Quick Reference

### Basic Equations
- **Storage:** S = K[xI + (1-x)O]
- **K** = travel time through reach (hours)
- **x** = weighting factor (0-0.5, typically 0.1-0.3)
- **Outflow:** O₂ = C₀I₂ + C₁I₁ + C₂O₁

### Muskingum Coefficients
| Coefficient | Formula |
|:------------|:--------|
| C₀ | (-Kx + 0.5Δt) / (K(1-x) + 0.5Δt) |
| C₁ | (Kx + 0.5Δt) / (K(1-x) + 0.5Δt) |
| C₂ | (K(1-x) - 0.5Δt) / (K(1-x) + 0.5Δt) |

**Check:** C₀ + C₁ + C₂ = 1.0

### Typical Values
- Natural channel: K = 1-5 hr, x = 0.1-0.3
- Reservoir: K = large, x = 0 (level pool)
- Check: Δt should be ≈ K to 3K for stability

---

## Framework 4: Sediment Transport Quick Reference

### Shields Diagram
- **Shields parameter:** τ* = τ₀ / ((ρ_s - ρ)gd)
- **Critical shear stress** (mobility begins): τ*_cr ≈ 0.03-0.06 for sand
- **Reynolds number (grain):** Re* = u*_f d / ν
- Bed movement when τ* > τ*_cr

### Bed Load Formulas
| Formula | Applicability |
|:--------|:-------------|
| Meyer-Peter & Müller | Coarse bed material |
| Einstein | Graded sediment |
| Engelund-Hansen | Total load, sand-bed streams |
| Van Rijn | Sand transport, partial transport |

### Bed Form Sequence (Increasing Velocity)
1. **Static bed** (no movement)
2. **Ripples** (small, triangular, Re* < ~5)
3. **Dunes** (larger, triangular, flow separation)
4. **Plane bed** (dunes washed out, upper regime)
5. **Antidunes** (in phase with surface waves, supercritical)

### Bridge Scour
| Type | Cause | Formula (HEC-18) |
|:-----|:------|:-----------------|
| Contraction | Channel narrows | y₂ from continuity |
| Local (pier) | Vortex at pier | y_s = 2.0K₁K₂K₃(K_w)^(0.65)·y₁·(V₁/V_c)^0.43 |
| Long-term | General degradation | Requires sediment balance |
| Overbank | Floodplain flow | Compare with main channel |

---

## Framework 5: Hydrologic Modeling Software

### HEC-HMS Components
| Component | What It Defines |
|:----------|:----------------|
| Basin Model | Subbasins, reaches, junctions, diversions |
| Meteorological Model | Rainfall input, gridded or gage-based |
| Control Specifications | Start/end time, time step |
| **Loss Methods** | SCS-CN, Green-Ampt, initial/constant |
| **Transform Methods** | SCS UH, Clark UH, ModClark |
| **Routing Methods** | Muskingum, kinematic wave, lag |

### HEC-RAS Quick Reference
| Feature | Description |
|:--------|:-----------|
| 1D Steady | Gradually varied flow (M1, M2, S2, etc.) |
| 1D Unsteady | Full Saint-Venant equations |
| 2D Flow | Diffusion wave or shallow water equations |
| Sediment | Empirical transport + bed evolution |
| **Critical output:** | Water surface profile, velocity, shear stress |

### GIS for Hydrology
| Task | Tool |
|:-----|:-----|
| Watershed delineation | ArcGIS/QGIS + DEM |
| Flow accumulation/length | Hydrology toolbox |
| Slope/aspect | Spatial Analyst |
| Land use classification | Remote sensing |
| Rainfall interpolation | IDW, Kriging |

---

## Framework 6: Quick-Fire Interview Answers

1. **"What is a unit hydrograph?"** — The direct runoff hydrograph resulting from 1 cm of excess rainfall uniformly distributed over the catchment for a specified duration.

2. **"What is the difference between rational method and UH method?"** — Rational method gives peak flow only (Q=CIA); UH gives the entire hydrograph shape. Rational method is for small catchments (< 5 km²).

3. **"What is Muskingum routing?"** — A storage-based routing method using S = K[xI + (1-x)O] to route a flood wave through a river reach. K = travel time, x = weighting factor.

4. **"What is the 100-year flood?"** — A flood magnitude that has a 1% probability of being equaled or exceeded in any given year. NOT "once in 100 years."

5. **"What is CN in SCS method?"** — Curve Number. A dimensionless parameter (0-100) reflecting the runoff potential of a catchment based on soil type, land use, and antecedent moisture.

6. **"What is the difference between bed load and suspended load?"** — Bed load rolls/slides along the bed (heavier particles). Suspended load is carried within the flow by turbulence (finer particles).

7. **"What is bridge scour?"** — Removal of sediment from around bridge foundations due to increased flow velocity and vortex action. Types: contraction, local (pier), and long-term degradation.

8. **"What is the S-curve?"** — A hydrograph of infinite duration rainfall at a constant intensity. Used to convert a UH of one duration to another.

9. **"What are the assumptions of unit hydrograph theory?"** — (a) Rainfall is uniform over catchment, (b) Rainfall excess duration is constant, (c) Direct runoff is proportional to rainfall excess (linearity), (d) Time base of DRH is constant.

10. **"Why is Log-Pearson Type III preferred for flood frequency?"** — It handles skewed flood data well, is recommended by USGS/CWC, and uses logarithmic transformation which better represents the multiplicative nature of flood processes.

---

## Last-Minute Checklist

- [ ] UH definition and S-curve method memorized
- [ ] SCS-CN formulas (Q, S, AMC adjustments) known
- [ ] Gumbel distribution steps clear
- [ ] Muskingum coefficients formulas memorized (C₀, C₁, C₂)
- [ ] Return period concept crisp (NOT "once in X years")
- [ ] Shields diagram concept clear
- [ ] HEC-HMS workflow steps known
- [ ] Bridge scour types and formula known
- [ ] Difference between bed load and suspended load clear
- [ ] At least 3 interview answers rehearsed

---

## Cross-Links

**Study:**
→ [Hydrology Full Reference](hydrology.md)
→ [Sediment Transport](sediment-transport.md)
→ [Role Study Plan](role-study-plan.md)

**Deeper:**
→ [Water Resources Engineering](../water_resources/water-resources-engineering.md)
→ [Open Channel Flow](../open_channel_flow/open-channel-flow.md)
→ [Hydraulics](../hydraulics/hydraulics.md)

**Interview:**
→ [Technical Interview Bank](../../../prep/interview/technical/technical-interview-bank.md)
→ [Behavioral Guide](../../../prep/behavioral/behavioral-interview-guide.md)

---

*Last updated: 2026-09-04*
