# HWRE — Formula Sheet

> Canonical formula reference for HWRE placement preparation. Priority tags: `[P0]` Must Memorize · `[P1]` Frequently Used · `[P2]` Useful · `[P3]` Low Priority.

**Authoritative source**: GATE-O-PEDIA Civil Engineering Handbook (Physics Wallah) + standard texts (Streeter, Chow, Subramanya, Todd).

## Notation Convention

| Symbol | Meaning | Unit |
|--------|---------|------|
| Q | Discharge / flow rate | m³/s |
| V, v | Velocity | m/s |
| A | Cross-sectional area | m² |
| P | Wetted perimeter / pressure | m / Pa |
| R | Hydraulic radius | m |
| S₀ | Bed slope | — |
| S_f | Friction slope | — |
| y | Flow depth | m |
| y_c | Critical depth | m |
| y_n | Normal depth | m |
| g | Gravitational acceleration | 9.81 m/s² |
| γ | Specific weight | N/m³ |
| ρ | Density | kg/m³ |
| μ | Dynamic viscosity | Pa·s |
| ν | Kinematic viscosity | m²/s |
| K | Hydraulic conductivity | m/s |
| T | Transmissivity | m²/s |
| S | Storativity | — |
| h_f | Head loss | m |
| f | Darcy friction factor | — |
| n | Manning's roughness | — |
| Fr | Froude number | — |
| Re | Reynolds number | — |

---

## 1. Fluid Mechanics & Hydraulics

### 1.1 Fluid Properties `[P0]`
| Formula | Equation | Notes |
|---------|----------|-------|
| Specific weight | `γ = ρg` | Water: 9810 N/m³ |
| Bulk modulus | `K = −V(dP/dV)` | Compressibility |
| Surface tension | `σ = F/L` | Capillary rise `h = 2σcosθ/(γr)` |
| Capillary rise | `h = 2σcosθ/(γr)` | `[P2]` |

### 1.2 Hydrostatics `[P0]`
| Formula | Equation | Notes |
|---------|----------|-------|
| Pressure at depth | `P = γh` | Gauge pressure |
| Absolute pressure | `P_abs = P_atm + γh` | |
| Hydrostatic force (plane) | `F = γh̄A` | h̄ = depth of centroid |
| Center of pressure | `h_cp = h̄ + I_G/(Ah̄)` | `[P1]` |
| Buoyancy | `F_b = γV_displaced` | Archimedes |
| Metacentric height | `GM = BM − BG` | Stability `[P2]` |

### 1.3 Kinematics & Dynamics `[P0]`
| Formula | Equation | Notes |
|---------|----------|-------|
| Continuity | `Q = A₁V₁ = A₂V₂` | Incompressible |
| Bernoulli | `P/γ + V²/2g + z = const` | Along streamline |
| Momentum | `ΣF = ρQ(V₂ − V₁)` | Force on structures |
| Euler's equation | `dP/ρ + VdV + gdz = 0` | `[P2]` |
| Reynolds number | `Re = ρVD/μ = VD/ν` | Laminar < 2000, turbulent > 4000 |

### 1.4 Pipe Flow `[P0]`
| Formula | Equation | Notes |
|---------|----------|-------|
| Darcy-Weisbach | `h_f = f(L/D)(V²/2g)` | All pipe flows |
| Hagen-Poiseuille | `f = 64/Re` | Laminar, Re < 2000 |
| Colebrook-White | `1/√f = −2log(ε/D/3.7 + 2.51/(Re√f))` | Implicit `[P1]` |
| Swamee-Jain | `f = 0.25/[log(ε/D/3.7 + 5.74/Re^0.9)]²` | Explicit `[P1]` |
| Minor losses | `h_m = K(V²/2g)` | K from fittings table |
| Hazen-Williams | `V = 0.849CR^0.63S^0.54` | Water supply `[P1]` |
| Hazen-Williams (head loss) | `h_f = 10.67LQ^1.85/(C^1.85D^4.87)` | SI units `[P1]` |
| Manning (pipe) | `V = (1/n)R^(2/3)S^(1/2)` | Full flow `[P1]` |

### 1.5 Pumps & Turbines `[P1]`
| Formula | Equation | Notes |
|---------|----------|-------|
| Pump power | `P = γQH/η` | W |
| Turbine power | `P = γQHη` | W |
| Specific speed (pump) | `N_s = N√Q/H^(3/4)` | `[P2]` |
| Specific speed (turbine) | `N_s = N√P/H^(5/4)` | `[P2]` |
| NPSH available | `NPSH_A = P_atm/γ − P_v/γ − h_s − h_f` | Cavitation check |
| Affinity laws | `Q ∝ N`, `H ∝ N²`, `P ∝ N³` | `[P1]` |

---

## 2. Open Channel Flow

### 2.1 Basic Relations `[P0]`
| Formula | Equation | Notes |
|---------|----------|-------|
| Continuity | `Q = AV` | |
| Hydraulic radius | `R = A/P` | |
| Froude number | `Fr = V/√(gD_h)` | D_h = A/T (hydraulic depth) |
| Chezy | `V = C√(RS)` | C = Chezy coefficient |
| Manning | `V = (1/n)R^(2/3)S^(1/2)` | SI units |
| Chezy-Manning | `C = R^(1/6)/n` | `[P1]` |

### 2.2 Specific Energy & Critical Flow `[P0]`
| Formula | Equation | Notes |
|---------|----------|-------|
| Specific energy | `E = y + V²/2g = y + Q²/(2gA²)` | |
| Critical depth (rect) | `y_c = (q²/g)^(1/3)` | q = Q/b |
| Critical depth (triangular) | `y_c = (2q²/g)^(1/5)` | `[P2]` |
| Minimum specific energy | `E_min = 1.5y_c` | At critical flow |
| Critical velocity | `V_c = √(gy_c)` | Rectangular |
| Critical slope | `S_c = (gn²)/(R_c^(1/3))` | `[P2]` |

### 2.3 Hydraulic Jump `[P0]`
| Formula | Equation | Notes |
|---------|----------|-------|
| Conjugate depth | `y₂/y₁ = 0.5(√(1+8Fr₁²) − 1)` | Rectangular |
| Energy loss | `ΔE = (y₂−y₁)³/(4y₁y₂)` | |
| Jump length | `L_j ≈ 6.9(y₂−y₁)` | `[P2]` |
| Sequent force | `F = γQ(V₁−V₂)/g` | `[P2]` |

### 2.4 Gradually Varied Flow `[P1]`
| Formula | Equation | Notes |
|---------|----------|-------|
| GVF equation | `dy/dx = (S₀−S_f)/(1−Fr²)` | |
| Water surface profiles | M1/M2/M3, S1/S2/S3, C1/C2/C3, A2/A3, H2/H3 | See classification |

**Profile classification:** Draw y_n and y_c lines. Zone 1: y > both; Zone 2: between; Zone 3: below both.

---

## 3. Hydrology

### 3.1 Precipitation & Infiltration `[P0]`
| Formula | Equation | Notes |
|---------|----------|-------|
| Rainfall excess | `P_e = P − losses` | |
| Horton infiltration | `f = f_c + (f₀−f_c)e^(−kt)` | |
| Philip infiltration | `F = St^(1/2) + At` | `[P1]` |
| Green-Ampt | `f = K(1 + ψΔθ/F)` | `[P1]` |
| Thiessen polygon | `P̄ = ΣPᵢAᵢ/ΣAᵢ` | Areal rainfall |
| Arithmetic mean | `P̄ = ΣPᵢ/n` | |
| Isohyetal | `P̄ = ΣP̄ᵢAᵢ/ΣAᵢ` | `[P2]` |

### 3.2 Runoff `[P0]`
| Formula | Equation | Notes |
|---------|----------|-------|
| Rational method | `Q = CiA/360` | A in ha, i in mm/hr |
| Rational (km²) | `Q = CiA/3.6` | A in km² |
| Runoff coefficient | `C = runoff/rainfall` | 0.1 forest – 0.95 urban |
| SCS-CN | `Q = (P−0.2S)²/(P+0.8S)` | P > 0.2S |
| SCS-CN storage | `S = 25400/CN − 254` | S in mm |

### 3.3 Unit Hydrograph `[P0]`
| Formula | Equation | Notes |
|---------|----------|-------|
| UH definition | DRH = P_e × UH ordinates | Linearity + time-invariance |
| S-curve | Sum UH ordinates shifted by D | Duration conversion |
| Snyder t_p | `t_p = C_t(LL_c)^0.3` | Ungauged catchments |
| Snyder Q_p | `Q_p = 640C_pA/t_p` | A in km², t_p in hr |
| Lag time | `t_L ≈ 0.6t_c` | Typical |

### 3.4 Flood Frequency `[P1]`
| Formula | Equation | Notes |
|---------|----------|-------|
| Gumbel | `x_T = x̄ + K_Tσ` | |
| Gumbel K_T | `K_T = −(√6/π)[0.5772 + ln(ln(T/(T−1)))]` | `[P2]` |
| Log-Pearson III | `log x_T = log x̄ + K_Tσ_logx` | |
| Return period | `T = 1/P` | P = exceedance probability |
| Risk | `R = 1 − (1 − 1/T)^n` | n = design life |
| Reliability | `Rel = (1 − 1/T)^n` | |

### 3.5 Flood Routing `[P0]`
| Formula | Equation | Notes |
|---------|----------|-------|
| Muskingum storage | `S = K[XI + (1−X)O]` | |
| Muskingum routing | `O₂ = C₀I₂ + C₁I₁ + C₂O₁` | |
| C₀ | `(−KX + 0.5Δt)/(K(1−X) + 0.5Δt)` | |
| C₁ | `(KX + 0.5Δt)/(K(1−X) + 0.5Δt)` | |
| C₂ | `(K(1−X) − 0.5Δt)/(K(1−X) + 0.5Δt)` | |
| Check | `C₀ + C₁ + C₂ = 1` | Always verify |
| Level-pool | `2S/Δt + O = 2I + (2S/Δt − O)_prev` | Reservoir routing |

---

## 4. Groundwater

### 4.1 Darcy's Law & Properties `[P0]`
| Formula | Equation | Notes |
|---------|----------|-------|
| Darcy's law | `Q = KiA` | Laminar flow |
| Darcy velocity | `v = Ki` | |
| Seepage velocity | `v_s = Ki/n` | n = porosity |
| Transmissivity | `T = Kb` | m²/s |
| Storativity (confined) | `S = ρgb(α + nβ)` | 10⁻⁵–10⁻³ |
| Specific yield | `S_y = V_drained/V_total` | Unconfined |
| Porosity relation | `S_y + S_r = n` | |

### 4.2 Well Hydraulics `[P0]`
| Formula | Equation | Notes |
|---------|----------|-------|
| Thiem (confined) | `Q = 2πT(h₂−h₁)/ln(r₂/r₁)` | Steady |
| Dupuit (unconfined) | `Q = πK(h₂²−h₁²)/ln(r₂/r₁)` | Steady |
| Theis (unsteady) | `s = (Q/4πT)W(u)` | |
| Theis u | `u = r²S/(4Tt)` | |
| Well function | `W(u) = −0.5772 − ln u + u − u²/4 + ...` | `[P1]` |
| Cooper-Jacob | `s = (2.3Q/4πT)log(2.25Tt/(r²S))` | u < 0.01 |
| Recovery | `s' = (2.3Q/4πT)log(t/t')` | `[P1]` |
| Step-drawdown | `s = BQ + CQ²` | B laminar, C turbulent |
| Well efficiency | `η = BQ/(BQ + CQ²) × 100%` | `[P1]` |

---

## 5. Water Resources

### 5.1 Reservoir Design `[P1]`
| Formula | Equation | Notes |
|---------|----------|-------|
| Mass curve storage | Max vertical departure between cumulative inflow and demand line | Rippl method |
| Trap efficiency | `TE = 1 − 1/(1 + 0.0003·Cap/Y)` | Brune's curve |
| Firm yield | Minimum dependable flow | 75–95% dependability |
| Water balance | `P = E + R + ΔS` | Basin scale |

### 5.2 Canal Design `[P1]`
| Formula | Equation | Notes |
|---------|----------|-------|
| Lacey velocity | `V = (Qf²/140)^(1/6)` | |
| Lacey perimeter | `P = 2.67√Q` | |
| Lacey hydraulic radius | `R = 5V²/(2f)` | `[P2]` |
| Silt factor | `f = 1.76√d_mm` | d in mm |
| Kennedy velocity | `V₀ = 0.55my^0.64` | m = critical velocity ratio |
| Most efficient trapezoid | `b = 2y(√(1+z²) − z)`, `R = y/2` | `[P1]` |

---

## 6. Sediment Transport

### 6.1 Incipient Motion `[P0]`
| Formula | Equation | Notes |
|---------|----------|-------|
| Shields parameter | `τ* = τ₀/((ρ_s−ρ)gd)` | |
| Bed shear stress | `τ₀ = ρgRS` | |
| Critical Shields | `τ_c* ≈ 0.047` | Uniform grains |
| Critical shear stress | `τ_c = θ_c(ρ_s−ρ)gd` | |
| HEC-18 critical velocity | `V_c = 6.19y^0.141 d₅₀^0.357` | SI, m/s `[P2]` |

### 6.2 Transport Formulas `[P1]`
| Formula | Equation | Notes |
|---------|----------|-------|
| Meyer-Peter Müller | `q_b* = 8(τ*−τ_c*)^(3/2)` | Bed load |
| MPM dimensionless | `q_b* = q_b/√(Δgd³)` | Δ = (ρ_s−ρ)/ρ |
| Rouse profile | `c/c_a = (y_a/y)^Z` | Suspended load |
| Rouse number | `Z = w_s/(κu_τ)` | κ = 0.41 |
| Strickler | `n = d₅₀^(1/6)/21.1` | SI units |
| Van Rijn bed load | `q_b = 0.053√(Δgd³)·T^1.5` | `[P2]` |
| Transport stage | `T = (τ₀−τ_c)/τ_c` | `[P2]` |

### 6.3 Scour `[P1]`
| Formula | Equation | Notes |
|---------|----------|-------|
| HEC-18 pier scour | `y_s/y₁ = 2.0K₁K₂K₃K₄(a/y₁)^0.35 Fr^0.43` | `[P2]` |
| Clear-water scour | Occurs when V < V_c | No sediment supply |
| Live-bed scour | Occurs when V > V_c | Sediment supply present |

---

## 7. Turbulence & CFD

### 7.1 Turbulence Fundamentals `[P1]`
| Formula | Equation | Notes |
|---------|----------|-------|
| Kolmogorov spectrum | `E(k) = C_Kε^(2/3)k^(−5/3)` | −5/3 law |
| Log-law | `u⁺ = (1/κ)ln(y⁺) + B` | B = 5.0, κ = 0.41 |
| Wall units | `u⁺ = u/u_τ`, `y⁺ = yu_τ/ν` | |
| Friction velocity | `u_τ = √(τ_w/ρ)` | |

### 7.2 RANS Models `[P1]`
| Formula | Equation | Notes |
|---------|----------|-------|
| Reynolds decomposition | `uᵢ = ūᵢ + uᵢ'` | |
| Boussinesq | `−ρuᵢ'uⱼ' = μ_t(∂ūᵢ/∂xⱼ + ∂ūⱼ/∂xᵢ) − (2/3)ρkδᵢⱼ` | |
| k-ε eddy viscosity | `μ_t = ρC_μk²/ε` | |
| k-ω eddy viscosity | `μ_t = ρk/ω` | |
| SST blending | `F₁ = tanh(arg₁⁴)` | Blends k-ω/k-ε |

### 7.3 Near-Wall Treatment `[P1]`
| y⁺ Range | Treatment |
|:--------:|-----------|
| y⁺ < 5 | Viscous sublayer resolved |
| 30–300 | Wall functions |
| > 300 | Log-law region |

---

## 8. Irrigation

### 8.1 Crop Water Requirements `[P1]`
| Formula | Equation | Notes |
|---------|----------|-------|
| Crop ET | `ET_c = K_c × ET₀` | |
| Net irrigation | `NIR = ET_c − P_eff` | |
| Field irrigation | `FIR = NIR/E_a` | |
| Canal irrigation | `CIR = FIR/E_c` | |
| Available moisture | `AM = FC − PWP` | |
| Depth of irrigation | `d = (FC − θ)γ_bD_r` | `[P2]` |

### 8.2 Duty & Delta `[P0]`
| Formula | Equation | Notes |
|---------|----------|-------|
| Duty | `D = A/(Q×T)` | hectares/cumec |
| Delta | `Δ = 8.64B/D` | metres |
| Relationship | `D × Δ = 8.64 × B` | B in days |

### 8.3 Efficiencies `[P1]`
| Efficiency | Formula | Typical |
|------------|---------|---------|
| Conveyance | `E_c = delivered/diverted` | 70–90% |
| Application | `E_a = stored/delivered` | 50–85% |
| Overall | `E_o = E_c × E_a` | 40–75% |

---

## 9. Flood Control

### 9.1 Flood Estimation `[P1]`
| Formula | Equation | Notes |
|---------|----------|-------|
| Rational method | `Q = CiA/360` | Small catchments |
| SCS-CN | `Q = (P−0.2S)²/(P+0.8S)` | |
| Gumbel | `x_T = x̄ + K_Tσ` | |
| Risk | `R = 1 − (1−1/T)^n` | |

### 9.2 Design Flood Selection `[P1]`
| Structure | Return Period |
|-----------|---------------|
| Small bridges/culverts | 25–50 yr |
| Major bridges | 50–100 yr |
| Dams (high hazard) | PMF |
| Levees/floodwalls | 100–500 yr |

---

## 10. Wastewater

### 10.1 BOD & Characteristics `[P0]`
| Formula | Equation | Notes |
|---------|----------|-------|
| BOD₅ | `BOD₅ = L₀(1 − e^(−5k))` | k in day⁻¹ |
| Ultimate BOD | `L₀ = BOD₅/(1 − e^(−5k))` | |
| BOD remaining | `L_t = L₀e^(−kt)` | `[P1]` |
| BOD/COD ratio | 0.5–0.6 domestic | Biodegradability |

### 10.2 Activated Sludge Process `[P1]`
| Formula | Equation | Notes |
|---------|----------|-------|
| Tank volume | `V = QS₀Y(SRT)/(X(1 + k_d·SRT))` | |
| F/M ratio | `F/M = QS₀/(VX)` | 0.2–0.5 |
| HRT | `HRT = V/Q` | 4–8 hr |
| SRT | `SRT = VX/(Q_wX_r)` | 5–15 days |
| Oxygen demand | `O₂ = Q(S₀−S)/f − 1.42ΔX` | `[P2]` |
| Methane production | `CH₄ = 0.35 × Q × L_v × removed` | m³/kg COD `[P2]` |

---

## 11. Water Supply

### 11.1 Demand & Population `[P1]`
| Formula | Equation | Notes |
|---------|----------|-------|
| Arithmetic growth | `P_n = P₀ + nx̄` | |
| Geometric growth | `P_n = P₀(1+r)^n` | |
| Incremental growth | `P_n = P₀ + nx̄ + n(n+1)d/2` | `[P2]` |
| Logistic | `P = P_sat/(1 + ae^(−bt))` | `[P2]` |
| Fire demand (Kuichling) | `Q = 3182√P` | L/min, P in thousands |

### 11.2 Treatment & Distribution `[P1]`
| Formula | Equation | Notes |
|---------|----------|-------|
| Hazen-Williams | `h_f = 10.67LQ^1.85/(C^1.85D^4.87)` | SI |
| Overflow rate | `v₀ = Q/A` | Sedimentation |
| Filter rate | `v = Q/A` | RSF 4–6 m/h |
| Pump specific speed | `N_s = N√Q/H^(3/4)` | |

---

## 12. Constants & Conversions

### Physical Constants
| Constant | Value |
|----------|-------|
| g | 9.81 m/s² |
| ρ_water | 1000 kg/m³ |
| γ_water | 9810 N/m³ |
| ν_water (20°C) | 1.0 × 10⁻⁶ m²/s |
| μ_water (20°C) | 1.0 × 10⁻³ Pa·s |
| P_atm | 101.3 kPa |
| ρ_sediment (quartz) | 2650 kg/m³ |
| von Kármán κ | 0.41 |
| Critical Shields | 0.047 |

### Unit Conversions
| Conversion | Factor |
|-----------|--------|
| 1 cumec | 1 m³/s |
| 1 m³/s | 86.4 MLD |
| 1 ha-m | 10,000 m³ |
| 1 cusec | 0.0283 m³/s |
| 1 acre-ft | 1233.5 m³ |
| 1 km² | 100 ha |
| 1 mm/hr over 1 ha | 0.00278 m³/s |

### Manning's n (Typical)
| Channel | n |
|---------|---|
| Concrete (trowel) | 0.011–0.013 |
| Earth (straight, clean) | 0.017–0.025 |
| Natural channel | 0.025–0.050 |
| Gravel bed | 0.030–0.040 |

---

## Rapid Revision Path

- **30 min**: P0 formulas only → [`RAPID_REVISION.md`](../RAPID_REVISION.md)
- **2 hr**: P0 + P1 → [`RAPID_REVISION.md`](../RAPID_REVISION.md)
- **1 day**: Complete → [`RAPID_REVISION.md`](../RAPID_REVISION.md)

## References

- GATE-O-PEDIA Civil Engineering Handbook (Physics Wallah)
- Subramanya, *Engineering Hydrology*
- Chow, *Open-Channel Hydraulics*
- Todd & Mays, *Groundwater Hydrology*
- Streeter & Wylie, *Fluid Mechanics*