# GATE Civil Engineering — Topic-wise Notes

> Study notes for GATE Civil preparation. Each subject: key concepts, conditions, and links to detailed theory + formulas.
> **Primary source**: GATE-O-PEDIA Civil Engineering Handbook (Physics Wallah). Detailed theory lives in `core/<subject>/` files.

## How to Use These Notes

1. Read the concept summary below for each subject.
2. For depth, open the linked `core/<subject>/` file.
3. Memorize formulas from [`formulas/gate-civil-formulas.md`](../formulas/gate-civil-formulas.md).
4. Solve [`practice/gate-civil-practice.md`](../practice/gate-civil-practice.md) problems.
5. Track errors in [`ERROR_ANALYSIS.md`](../ERROR_ANALYSIS.md).

---

## 1. Engineering Mathematics

### 1.1 Linear Algebra
- **Matrix operations**: addition, multiplication, transpose, inverse (`A⁻¹ = adj(A)/det(A)`)
- **Determinants**: properties, Cramer's rule, rank
- **Eigenvalues/eigenvectors**: characteristic equation `det(A − λI) = 0`, Cayley-Hamilton theorem
- **Systems of equations**: consistency, Gaussian elimination
- **GATE focus**: eigenvalues of 2×2/3×3, rank, inverse, consistency of systems

### 1.2 Calculus
- **Limits & continuity**: L'Hôpital's rule, series expansions
- **Differentiation**: partial derivatives, total derivative, maxima/minima
- **Integration**: definite/improper integrals, Beta/Gamma functions
- **Vector calculus**: gradient, divergence, curl, Green's/Stokes/Gauss theorems
- **GATE focus**: Taylor/Maclaurin series, vector identities, double integrals

### 1.3 Differential Equations
- **First order**: variable separable, homogeneous, exact, linear (integrating factor)
- **Higher order**: linear with constant coefficients, Cauchy-Euler
- **PDE**: classification, separation of variables, wave/heat/Laplace equations
- **GATE focus**: first-order linear, second-order constant-coefficient, Laplace transforms

### 1.4 Probability & Statistics
- **Probability**: axioms, Bayes' theorem, random variables
- **Distributions**: Binomial, Poisson, Normal, Exponential
- **Statistics**: mean, median, mode, standard deviation, correlation, regression
- **GATE focus**: Bayes, binomial/Poisson/normal, expected value, variance

### 1.5 Numerical Methods
- **Root finding**: Bisection, Newton-Raphson, Secant
- **Interpolation**: Lagrange, Newton forward/backward
- **Integration**: Trapezoidal, Simpson's 1/3, 3/8 rules
- **ODE**: Euler, Runge-Kutta (2nd, 4th order)
- **GATE focus**: Newton-Raphson, Simpson's rule, RK-4

**Formulas:** [`§1 Engineering Mathematics`](../formulas/gate-civil-formulas.md#1-engineering-mathematics)

---

## 2. Engineering Mechanics

### 2.1 Force Systems & Equilibrium
- Force is characterized by magnitude, direction, point of application, line of action
- **Equilibrium**: `ΣF_x = 0`, `ΣF_y = 0`, `ΣM = 0`
- **Lami's theorem**: three concurrent coplanar forces in equilibrium — each force proportional to sine of angle between the other two
- **Free body diagrams**: isolate the body, show all external forces

### 2.2 Friction
- Limiting friction: `F_max = μN`
- Angle of repose: `tanφ = μ`
- Friction force ≤ μN; only equal at impending motion

### 2.3 Trusses
- **Method of joints**: equilibrium at each joint (2 equations per joint)
- **Method of sections**: cut through ≤3 members, moment equilibrium
- Zero-force members: identify by inspection

### 2.4 Centroid & Moment of Inertia
- Centroid: `x̄ = ∫x dA/∫dA`
- Standard shapes: triangle h/3 from base, semicircle 4r/3π, quarter circle 4r/3π
- MOI: rectangle `bh³/12`, circle `πd⁴/64`
- Parallel axis: `I = I_c + Ad²`

**Formulas:** [`§2 Engineering Mechanics`](../formulas/gate-civil-formulas.md#2-engineering-mechanics)
**Detailed theory:** [`core/fundamentals/engineering-mechanics.md`](../../fundamentals/engineering-mechanics.md)

---

## 3. Strength of Materials

### 3.1 Stress, Strain & Elastic Constants
- `σ = P/A`, `ε = ΔL/L`, Hooke's law `σ = Eε`
- Shear: `τ = V/A`, `γ = τ/G`
- Poisson's ratio: `ν = −ε_lateral/ε_axial`
- **Elastic constants**: `E = 2G(1+ν) = 3K(1−2ν)`
- Axial deformation: `δ = PL/(AE)`
- Thermal stress: `σ = EαΔT` (restrained)

### 3.2 Bending & Shear
- Bending stress: `σ = My/I`, section modulus `Z = I/y_max`
- Shear stress: `τ = VQ/(Ib)`; rectangle max `3V/2bh`, circle max `4V/3A`
- Relations: `dM/dx = V`, `dV/dx = −w`

### 3.3 Deflection
- Double integration: `EI d²y/dx² = M(x)`
- Standard cases: cantilever `PL³/3EI`, `wL⁴/8EI`; SS `PL³/48EI`, `5wL⁴/384EI`; fixed `wL⁴/384EI`
- Moment-area, conjugate beam, Castigliano methods

### 3.4 Torsion
- `T/J = τ/r = Gθ/L`; solid `J = πd⁴/32`, hollow `J = π(D⁴−d⁴)/32`

### 3.5 Principal Stresses & Mohr's Circle
- `σ₁,₂ = (σ_x+σ_y)/2 ± √[((σ_x−σ_y)/2)² + τ_xy²]`
- Max shear `= (σ₁−σ₂)/2`
- Mohr's circle: centre `((σ_x+σ_y)/2, 0)`, radius `√[((σ_x−σ_y)/2)² + τ_xy²]`

### 3.6 Buckling
- Euler: `P_cr = π²EI/(KL)²`; K = 0.5/0.7/1.0/2.0
- Rankine-Gordon for short columns

**Formulas:** [`§3 Strength of Materials`](../formulas/gate-civil-formulas.md#3-strength-of-materials)
**Detailed theory:** [`core/fundamentals/strength-of-materials.md`](../../fundamentals/strength-of-materials.md)

---

## 4. Structural Analysis

### 4.1 Determinacy
- Beams: `D_s = r − 3`
- Trusses: `D_s = m + r − 2j`
- Frames: `D_s = 3m + r − 3j − e_c`
- Kinematic: `D_k = 3j − r − e_c` (frames), `2j − r` (trusses)

### 4.2 Deflection Methods
- **Slope-deflection**: `M_AB = M_FAB + (2EI/L)(2θ_A + θ_B − 3Δ/L)`
- **Moment distribution**: stiffness `4EI/L` (fixed far end), `3EI/L` (pinned); DF = K/ΣK; carry-over 1/2
- Fixed-end moments: UDL `wL²/12`, centre point load `PL/8`

### 4.3 Influence Lines & Energy Methods
- Muller-Breslau principle
- Virtual work: `Δ = ∫(M·m/EI)dx`
- Castigliano: `δ_i = ∂U/∂P_i`

### 4.4 Matrix Methods
- Stiffness: `{F} = [K]{Δ}`; flexibility: `{Δ} = [f]{F}`

**Formulas:** [`§4 Structural Analysis`](../formulas/gate-civil-formulas.md#4-structural-analysis)
**Detailed theory:** [`core/structural-analysis/structural-analysis.md`](../../structural-analysis/structural-analysis.md)

---

## 5. Reinforced Concrete Structures

### 5.1 Limit State Design (IS 456:2000)
- Partial safety factors: loads `γ_f = 1.5`, materials `γ_m = 1.5` (concrete), `1.15` (steel)
- Limiting moment: `M_u,lim = 0.138f_ckbd²` (Fe415), `0.133f_ckbd²` (Fe500)
- `x_u,max/d = 0.48` (Fe415), `0.46` (Fe500), `0.53` (Fe250)

### 5.2 Flexure, Shear, Bond
- Flexure: `M_u = 0.87f_yA_st d(1 − A_stf_y/(bdf_ck))`
- Shear: `τ_v = V_u/(bd)`, `V_us = 0.87f_yA_sv d/s_v`
- Development length: `L_d = φσ_s/(4τ_bd)`
- Steel limits: min `0.85bd/f_y`, max `0.04bD`

### 5.3 Columns & Slabs
- Short column: `P_u = 0.4f_ckA_c + 0.67f_yA_sc`
- One-way slab: `l_y/l_x > 2`; two-way: `l_y/l_x ≤ 2`
- Span/depth: cantilever 1/7, SS 1/20, continuous 1/26

**Formulas:** [`§5 RCC`](../formulas/gate-civil-formulas.md#5-reinforced-concrete-structures)
**Detailed theory:** [`core/rcc/rcc-design.md`](../../rcc/rcc-design.md)

---

## 6. Steel Structures

### 6.1 IS 800:2007
- Partial safety factors: `γ_M0 = 1.1`, `γ_M1 = 1.25`, `γ_Mw = 1.25`, `γ_Mb = 1.25`

### 6.2 Tension & Compression
- Tension: gross `T_dg = A_gf_y/γ_M0`, net `T_dn = 0.9A_nf_u/γ_M1`
- Compression: `f_cd` from buckling curve, `λ = √(f_y/f_cr)`

### 6.3 Beams & Connections
- Bending: `M_d = β_bZ_pf_y/γ_M0` (plastic)
- Bolts: shear `V_dsb = f_ubn_nA_nb/(√3γ_Mb)`
- Welds: `f_wd = f_u/(√3γ_Mw)`, throat `t_t = 0.7s`

**Formulas:** [`§6 Steel`](../formulas/gate-civil-formulas.md#6-steel-structures)
**Detailed theory:** [`core/steel/steel-design.md`](../../steel/steel-design.md)

---

## 7. Geotechnical Engineering

### 7.1 Phase Relationships
- `e = V_v/V_s`, `n = e/(1+e)`, `S = V_w/V_v`, `Se = wG_s`
- `γ = (G_s+Se)γ_w/(1+e)`, `γ_d = G_sγ_w/(1+e)`, `γ' = (G_s−1)γ_w/(1+e)`

### 7.2 Permeability & Seepage
- Darcy: `v = ki`, `Q = kiA`
- Constant/falling head tests
- Flow net: `q = kH(N_f/N_d)`
- Critical gradient: `i_c = (G_s−1)/(1+e)`

### 7.3 Consolidation
- Settlement: `S_c = [C_c/(1+e₀)]H log(σ'_f/σ'_i)`
- Time: `T_v = c_vt/H_dr²`; `T_v(50%) = 0.197`, `T_v(90%) = 0.848`

### 7.4 Shear Strength
- Mohr-Coulomb: `τ_f = c + σ'tanφ`
- Triaxial: `σ₁ = σ₃N_φ + 2c√N_φ`

### 7.5 Earth Pressure & Bearing Capacity
- Rankine: `K_a = tan²(45−φ/2)`, `K_p = tan²(45+φ/2)`
- Terzaghi: `q_u = cN_c + qN_q + 0.5γBN_γ` (strip)

### 7.6 Slope Stability
- Infinite slope: `F_s = tanφ/tanβ` (dry); `(γ'/γ_sat)(tanφ/tanβ)` (seepage)

**Formulas:** [`§7 Geotechnical`](../formulas/gate-civil-formulas.md#7-geotechnical-engineering)
**Detailed theory:** [`core/geotechnical/geotechnical.md`](../../geotechnical/geotechnical.md)

---

## 8. Fluid Mechanics

### 8.1 Properties
- Viscosity: `τ = μ du/dy`; `ν = μ/ρ`
- Surface tension: droplet `4T/d`, bubble `8T/d`, jet `2T/d`

### 8.2 Hydrostatics
- `p = γh`; `F = γAh̄`; centre of pressure `y_p = ȳ + I_c/(Aȳ)`
- Buoyancy: `F_b = γ_wV_displaced`

### 8.3 Dynamics
- Continuity: `A₁v₁ = A₂v₂`
- Bernoulli: `p/γ + v²/2g + z = constant`
- Momentum: `ΣF = ρQ(V₂−V₁)`

### 8.4 Dimensional Analysis
- Re, Fr, Eu, M numbers
- Buckingham π: n−m terms

### 8.5 Pipe Flow
- Darcy-Weisbach: `h_f = f(L/D)(v²/2g)`
- Hagen-Poiseuille: `f = 64/Re` (laminar)
- Minor losses: `h_m = Kv²/2g`

**Formulas:** [`§8 Fluid Mechanics`](../formulas/gate-civil-formulas.md#8-fluid-mechanics)
**Detailed theory:** [`core/hwre/hydraulics/hydraulics.md`](../../hwre/hydraulics/hydraulics.md)

---

## 9. Hydraulics / Open Channel Flow

### 9.1 Uniform Flow
- Manning: `Q = (1/n)AR^(2/3)S^(1/2)`
- Chezy: `v = C√(RS)`
- Most efficient: rectangular `b = 2y`, trapezoidal half-hexagon

### 9.2 Critical Flow
- `y_c = (q²/g)^(1/3)` (rectangular)
- Specific energy: `E = y + v²/2g`, `E_min = 1.5y_c`
- Froude: `Fr = v/√(gy)`

### 9.3 Hydraulic Jump
- `y₂/y₁ = ½[√(1+8Fr₁²)−1]`
- Energy loss: `ΔE = (y₂−y₁)³/(4y₁y₂)`
- Forms only when `Fr₁ > 1`

### 9.4 GVF
- `dy/dx = (S₀−S_f)/(1−Fr²)`
- M, S, C, H, A profiles

### 9.5 Pumps & Turbines
- Power: `P = γQH/η`
- Specific speed: `N_s = N√Q/H^(3/4)`
- Affinity: `Q∝N`, `H∝N²`, `P∝N³`

**Formulas:** [`§9 Hydraulics`](../formulas/gate-civil-formulas.md#9-hydraulics--open-channel-flow)
**Detailed theory:** [`core/hwre/hydraulics/hydraulics.md`](../../hwre/hydraulics/hydraulics.md)

---

## 10. Hydrology

### 10.1 Precipitation & Infiltration
- Average rainfall: arithmetic, Thiessen, isohyetal
- Horton: `f = f_c + (f₀−f_c)e^(−kt)`

### 10.2 Runoff
- Rational: `Q = CiA/360` (A in ha, i in mm/hr); `Q = CiA/3.6` (A in km², i in mm/hr)
- SCS-CN: `Q = (P−0.2S)²/(P+0.8S)`

### 10.3 Hydrographs
- Unit hydrograph: DRH = UH × excess rainfall (convolution)
- S-curve technique for duration change

### 10.4 Flood Frequency
- Gumbel: `x_T = x̄ + Kσ`
- Risk: `R = 1−(1−1/T)^n`

### 10.5 Groundwater
- Theis: `s = (Q/4πT)W(u)`
- Cooper-Jacob: `s = (2.3Q/4πT)log₁₀(2.25Tt/r²S)` (u < 0.01)
- Thiem: `Q = 2πT(h₂−h₁)/ln(r₂/r₁)`

**Formulas:** [`§10 Hydrology`](../formulas/gate-civil-formulas.md#10-hydrology)
**Detailed theory:** [`core/hwre/hydrology/hydrology.md`](../../hwre/hydrology/hydrology.md)

---

## 11. Environmental Engineering

### 11.1 Water Supply
- Population forecasting: arithmetic, geometric, incremental
- Per capita demand: 135–200 LPCD
- Hardness: `(Ca²⁺/20 + Mg²⁺/12.15) × 50`

### 11.2 Water Treatment
- Sedimentation: Stokes `v_s = (g/18)(ρ_s−ρ_w)d²/μ`
- Coagulation/flocculation: `G = √(P/(μV))`
- Filtration: rapid 4–6 m/h, slow 0.1–0.2 m/h
- Disinfection: Chick's law, CT concept

### 11.3 Wastewater
- BOD: `BOD_t = L₀(1−e^(−kt))`, `BOD₅ ≈ 0.68L₀`
- ASP: `F/M = QS₀/(VX)`, `SRT = VX/(Q_wX_w + Q_eX_e)`
- Sewer: min velocity 0.6 m/s, min diameter 200 mm

### 11.4 Air & Solid Waste
- Gaussian plume dispersion
- ESP: Deutsch `η = 1−e^(−wA/Q)`
- Solid waste: 0.3–0.6 kg/capita/day

**Formulas:** [`§11 Environmental`](../formulas/gate-civil-formulas.md#11-environmental-engineering)
**Detailed theory:** [`core/environmental/environmental-engineering.md`](../../environmental/environmental-engineering.md)

---

## 12. Transportation Engineering

### 12.1 Geometric Design
- SSD: `0.278Vt_R + V²/(254f)`
- Superelevation: `e + f = V²/(127R)`, `e_max = 0.07`
- Transition: `L = V³/(4RC)`
- Vertical curves: crest `L = NS²/4.4`, valley comfort `L = NV³/360`

### 12.2 Traffic Engineering
- Fundamental: `q = kv`
- Greenshields: `v = v_f(1−k/k_j)`
- Shockwave: `w = (q₂−q₁)/(k₂−k₁)`
- Webster: `C₀ = (1.5L+5)/(1−ΣY)`

### 12.3 Pavements
- Flexible: CBR method (IRC 37)
- Rigid: Westergaard (IRC 58)

**Formulas:** [`§12 Transportation`](../formulas/gate-civil-formulas.md#12-transportation-engineering)
**Detailed theory:** [`core/transportation/transportation-engineering.md`](../../transportation/transportation-engineering.md)

---

## 13. Geomatics / Surveying

### 13.1 Errors & Levelling
- Curvature: `−0.0785D²`, refraction: `+0.0112D²`, combined `−0.0673D²`
- `H = BS − FS`; `ΣBS − ΣFS = last RL − first RL`

### 13.2 Traversing
- Latitude `L = l cosθ`, departure `D = l sinθ`
- Closing error: `e = √((ΣL)² + (ΣD)²)`
- Area: `A = ½|Σ(x_i y_{i+1} − x_{i+1} y_i)|`

### 13.3 Tacheometry & Curves
- `D = ks + C` (k=100, C=0 anallactic)
- Simple curve: `T = R tan(Δ/2)`, `L = RΔ`

### 13.4 RS/GIS
- NDVI = `(NIR−Red)/(NIR+Red)`
- Raster vs vector

**Formulas:** [`§13 Geomatics`](../formulas/gate-civil-formulas.md#13-geomatics--surveying)
**Detailed theory:** [`core/geoinformatics/geoinformatics.md`](../../geoinformatics/geoinformatics.md)

---

## 14. Construction Management

### 14.1 CPM
- `TF = LS − ES = LF − EF`; critical activities `TF = 0`
- Project duration = longest path

### 14.2 PERT
- `t_e = (t₀ + 4t_m + t_p)/6`
- Variance: `σ² = ((t_p−t₀)/6)²`
- Probability: `Z = (T_s−T_e)/σ`

### 14.3 Cost & Contracts
- Cost slope = (crash − normal)/(normal time − crash time)
- Earned value: `CPI = EV/AC`, `SPI = EV/PV`

**Formulas:** [`§14 Construction Mgmt`](../formulas/gate-civil-formulas.md#14-construction-management)
**Detailed theory:** [`core/infrastructure/infrastructure-engineering-management.md`](../../infrastructure/infrastructure-engineering-management.md)

---

## References

- [`../formulas/gate-civil-formulas.md`](../formulas/gate-civil-formulas.md) — Complete formula sheet
- [`../revision_notes/gate-civil-revision.md`](../revision_notes/gate-civil-revision.md) — Rapid revision cards
- [`../practice/gate-civil-practice.md`](../practice/gate-civil-practice.md) — Practice problems
- [`../pyq/gate-civil-pyq.md`](../pyq/gate-civil-pyq.md) — PYQ system
- **GATE-O-PEDIA Civil Engineering Handbook** (Physics Wallah) — primary source
