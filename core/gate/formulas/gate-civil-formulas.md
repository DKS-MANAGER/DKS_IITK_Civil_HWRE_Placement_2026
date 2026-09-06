# GATE Civil Engineering — Formula Sheet

> Canonical GATE Civil formula reference. Priority tags: `[P0]` Must Memorize, `[P1]` Frequently Used, `[P2]` Useful, `[P3]` Low Priority.
> Use with [`civil/gate-civil-notes.md`](../civil/gate-civil-notes.md) (concepts) and [`practice/gate-civil-practice.md`](../practice/gate-civil-practice.md) (solved problems).
> **Authoritative source**: GATE-O-PEDIA Civil Engineering Handbook (Physics Wallah, 947 pp). All formulas verified against this handbook and standard codes (IS 456, IS 800, IRC).

## Notation Convention

| Symbol | Meaning | Symbol | Meaning |
| ------ | ------- | ------ | ------- |
| σ | normal stress | ε | normal strain |
| τ | shear stress | γ | shear strain / unit weight |
| E | Young's modulus | G | shear modulus |
| I | second moment of area | Q | first moment of area |
| ν | Poisson's ratio | K | bulk modulus |
| M | bending moment | V | shear force |
| EI | flexural rigidity | GJ | torsional rigidity |
| f_ck | characteristic concrete strength | f_y | yield strength of steel |
| γ_w | unit weight of water (9.81 kN/m³) | ρ | density |
| μ | dynamic viscosity | ν | kinematic viscosity |
| Q | discharge | q | discharge per unit width |
| h_f | friction head loss | S | slope / storage coefficient |
| T | transmissivity | c_v | coefficient of consolidation |
| u | pore water pressure | σ' | effective stress |

---

## 1. Engineering Mathematics

### 1.1 Linear Algebra

**Eigenvalues** `[P0]`
- Characteristic equation: `det(A − λI) = 0`
- For 2×2 `[[a,b],[c,d]]`: `λ² − (a+d)λ + (ad − bc) = 0`
- Trace = sum of eigenvalues; det = product of eigenvalues
- **GATE trap**: For symmetric matrix, eigenvalues are real; eigenvectors orthogonal.

**Cayley-Hamilton** `[P1]`
- Every square matrix satisfies its own characteristic equation: `p(A) = 0`

**Rank** `[P1]`
- Row rank = column rank = number of non-zero rows in row-echelon form
- For `n×n` matrix: rank = n ⟺ det ≠ 0 ⟺ invertible

**Inverse** `[P1]`
- `A⁻¹ = adj(A)/det(A)`, valid when `det(A) ≠ 0`

### 1.2 Calculus

**Taylor series** `[P0]`
- `f(x) = f(a) + f'(a)(x−a) + f''(a)(x−a)²/2! + f'''(a)(x−a)³/3! + ...`
- Maclaurin (a=0): `eˣ = 1 + x + x²/2! + x³/3! + ...`
- `sin x = x − x³/3! + x⁵/5! − ...`, `cos x = 1 − x²/2! + x⁴/4! − ...`
- `ln(1+x) = x − x²/2 + x³/3 − ...` (|x| < 1)

**Vector calculus** `[P1]`
- Gradient: `∇f = (∂f/∂x, ∂f/∂y, ∂f/∂z)`
- Divergence: `∇·F = ∂F_x/∂x + ∂F_y/∂y + ∂F_z/∂z`
- Curl: `∇×F = (∂F_z/∂y − ∂F_y/∂z, ∂F_x/∂z − ∂F_z/∂x, ∂F_y/∂x − ∂F_x/∂y)`
- Gauss: `∮∮ F·dS = ∭ (∇·F) dV`
- Stokes: `∮ F·dr = ∬ (∇×F)·dS`
- Green: `∮ (P dx + Q dy) = ∬ (∂Q/∂x − ∂P/∂y) dx dy`

### 1.3 Differential Equations

**First-order linear** `[P0]`
- `dy/dx + P(x)y = Q(x)` → integrating factor `IF = e^∫P dx`
- Solution: `y·IF = ∫ Q·IF dx + C`

**Second-order constant coefficients** `[P0]`
- `ay'' + by' + cy = 0`, auxiliary `am² + bm + c = 0`
- Distinct real roots: `y = C₁e^(m₁x) + C₂e^(m₂x)`
- Repeated roots: `y = (C₁ + C₂x)e^(mx)`
- Complex roots `m = α ± iβ`: `y = e^(αx)(C₁cos βx + C₂sin βx)`

**Cauchy-Euler** `[P1]`
- `x²y'' + axy' + by = 0` → try `y = x^m`

**Laplace transform** `[P1]`
- `L{f(t)} = ∫₀^∞ e^(−st) f(t) dt`
- `L{1} = 1/s`, `L{t} = 1/s²`, `L{e^(at)} = 1/(s−a)`, `L{sin at} = a/(s²+a²)`, `L{cos at} = s/(s²+a²)`

### 1.4 Probability & Statistics

**Bayes' theorem** `[P0]`
- `P(A|B) = P(B|A)·P(A)/P(B)`

**Distributions** `[P0]`
- Binomial: `P(X=k) = C(n,k) pᵏ (1−p)^(n−k)`, mean `np`, variance `np(1−p)`
- Poisson: `P(X=k) = e^(−λ) λᵏ/k!`, mean = variance = `λ`
- Normal: `f(x) = (1/√(2πσ²)) e^(−(x−μ)²/(2σ²))`
- Exponential: `f(x) = λe^(−λx)`, mean `1/λ`

**Statistics** `[P1]`
- `E[X] = Σ x P(x)`, `Var(X) = E[X²] − (E[X])²`
- Coefficient of variation = `σ/μ`

### 1.5 Numerical Methods

**Newton-Raphson** `[P0]`
- `x_{n+1} = x_n − f(x_n)/f'(x_n)`
- **GATE trap**: fails when `f'(x_n) = 0` (horizontal tangent).

**Numerical integration** `[P0]`
- Trapezoidal: `∫f dx ≈ (h/2)[f₀ + 2(f₁+...+f_{n−1}) + f_n]`, error `O(h²)`
- Simpson 1/3: `∫f dx ≈ (h/3)[f₀ + 4f₁ + 2f₂ + 4f₃ + ... + f_n]`, error `O(h⁴)`, **n must be even**
- Simpson 3/8: `∫f dx ≈ (3h/8)[f₀ + 3f₁ + 3f₂ + 2f₃ + ... + f_n]`, **n multiple of 3**

**Runge-Kutta 4th order** `[P1]`
- `y_{n+1} = y_n + (h/6)(k₁ + 2k₂ + 2k₃ + k₄)`
- `k₁ = f(x_n, y_n)`, `k₂ = f(x_n + h/2, y_n + hk₁/2)`, `k₃ = f(x_n + h/2, y_n + hk₂/2)`, `k₄ = f(x_n + h, y_n + hk₃)`

---

## 2. Engineering Mechanics

### 2.1 Equilibrium & Friction

**Equilibrium** `[P0]`
- `ΣF_x = 0`, `ΣF_y = 0`, `ΣM = 0`
- Lami's theorem (3 concurrent forces): `F₁/sin α = F₂/sin β = F₃/sin γ`

**Friction** `[P0]`
- `F_max = μN` (limiting friction)
- Angle of repose: `tan φ = μ`
- **GATE trap**: friction force is `≤ μN`, only equal at impending motion.

### 2.2 Centroid & Moment of Inertia

**Centroid** `[P0]`
- `x̄ = ∫x dA/∫dA`, `ȳ = ∫y dA/∫dA`
- Triangle (from base): `h/3`; semicircle (from diameter): `4r/3π`; quarter circle: `4r/3π`

**Moment of inertia** `[P0]`
- Rectangle `b×h` about centroidal axis: `I = bh³/12`
- Circle: `I = πd⁴/64 = πr⁴/4`
- Parallel axis: `I = I_c + Ad²`
- Radius of gyration: `r = √(I/A)`

### 2.3 Kinematics & Dynamics

**Projectile** `[P1]`
- Range: `R = u²sin 2θ/g`; max height: `H = u²sin²θ/(2g)`; time of flight: `T = 2u sin θ/g`

**Circular motion** `[P1]`
- Centripetal force: `F = mv²/r = mω²r`

---

## 3. Strength of Materials

### 3.1 Stress, Strain & Elastic Constants

**Definitions** `[P0]`
- `σ = P/A`, `ε = ΔL/L`, Hooke's law: `σ = Eε`
- Shear: `τ = V/A`, `γ = τ/G`
- Poisson's ratio: `ν = −ε_lateral/ε_axial`

**Elastic constants relation** `[P0]`
- `E = 2G(1 + ν) = 3K(1 − 2ν)`
- **GATE trap**: `ν` range for isotropic material: `−1 < ν < 0.5`; for most metals `ν ≈ 0.3`.

**Axial deformation** `[P0]`
- `δ = PL/(AE)`
- Composite bars: `δ = Σ P_i L_i/(A_i E_i)`

**Thermal stress** `[P1]`
- `σ = EαΔT` (when restrained)
- Free expansion: `δ = αLΔT`

### 3.2 Shear Force & Bending Moment

**Relations** `[P0]`
- `dM/dx = V`, `dV/dx = −w`
- **GATE trap**: point load → jump in SF; point moment → jump in BM.

### 3.3 Bending & Shear Stress

**Bending stress** `[P0]`
- `σ = My/I`, max at extreme fibre: `σ_max = M/Z`, section modulus `Z = I/y_max`
- Rectangle: `Z = bh²/6`; circle: `Z = πd³/32`

**Shear stress** `[P0]`
- `τ = VQ/(Ib)`
- Rectangle (max at NA): `τ_max = 3V/(2bh)` = 1.5 × average
- Circle (max at NA): `τ_max = 4V/(3A)` = 4/3 × average
- I-section: max at web (near NA)

### 3.4 Deflection

**Standard cases** `[P0]` (all for prismatic beam, EI constant)

| Beam | Loading | Max deflection |
| ---- | ------- | -------------- |
| Cantilever | Point load P at free end | `PL³/3EI` |
| Cantilever | UDL w | `wL⁴/8EI` |
| Simply supported | Point load P at centre | `PL³/48EI` |
| Simply supported | UDL w | `5wL⁴/384EI` |
| Fixed-fixed | UDL w | `wL⁴/384EI` |
| Fixed-fixed | Point load P at centre | `PL³/192EI` |

**Methods** `[P1]`
- Double integration: `EI d²y/dx² = M(x)`
- Moment-area: `θ_AB = ∫(M/EI)dx`, `Δ = ∫(M/EI)x dx`
- Conjugate beam: slope = shear, deflection = moment of conjugate beam
- Castigliano: `δ_i = ∂U/∂P_i`

### 3.5 Torsion

**Circular shaft** `[P0]`
- `T/J = τ/r = Gθ/L`
- Solid shaft: `J = πd⁴/32`; hollow: `J = π(D⁴−d⁴)/32`
- Power: `P = 2πNT/60` (N in rpm, T in N·m)

### 3.6 Principal Stresses & Mohr's Circle

**Principal stresses** `[P0]`
- `σ₁,₂ = (σ_x + σ_y)/2 ± √[((σ_x − σ_y)/2)² + τ_xy²]`
- Max shear: `τ_max = √[((σ_x − σ_y)/2)² + τ_xy²] = (σ₁ − σ₂)/2`
- Plane stress: `σ₃ = 0`; plane strain: `ε₃ = 0`

**Mohr's circle** `[P1]`
- Centre: `((σ_x+σ_y)/2, 0)`, radius: `√[((σ_x−σ_y)/2)² + τ_xy²]`

### 3.7 Buckling

**Euler buckling** `[P0]`
- `P_cr = π²EI/(KL)²`

| End condition | K | P_cr |
| ------------- | - | ---- |
| Both fixed | 0.5 | `4π²EI/L²` |
| One fixed, one pinned | 0.7 | `π²EI/(0.7L)²` |
| Both pinned | 1.0 | `π²EI/L²` |
| One fixed, one free | 2.0 | `π²EI/(2L)²` |

- Slenderness ratio: `λ = KL/r`; Euler valid for long columns (`λ > λ_critical`)
- **GATE trap**: Euler formula overestimates for short columns — use Rankine-Gordon: `1/P = 1/P_cr + 1/P_crush`

---

## 4. Structural Analysis

### 4.1 Determinacy

**Static indeterminacy** `[P0]`
- Beams: `D_s = r − 3` (r = reactions)
- Trusses: `D_s = m + r − 2j` (m = members, j = joints)
- Frames: `D_s = 3m + r − 3j − e_c` (e_c = internal hinges)
- **GATE trap**: original sheet incorrectly used `m + r = 2j` for beams — that condition is for trusses only.

**Kinematic indeterminacy** `[P1]`
- `D_k = 3j − r − e_c` (frames, no axial deformation)
- `D_k = 2j − r` (trusses)

### 4.2 Deflection Methods

**Slope-deflection** `[P1]`
- `M_AB = M_FAB + (2EI/L)(2θ_A + θ_B − 3Δ/L)`
- `M_BA = M_FBA + (2EI/L)(2θ_B + θ_A − 3Δ/L)`

**Moment distribution** `[P1]`
- Stiffness: `K = 4EI/L` (far end fixed), `K = 3EI/L` (far end pinned)
- Distribution factor: `DF = K/ΣK`
- Carry-over factor: `1/2` (fixed far end)

**Fixed-end moments** `[P0]`
- SS beam UDL w: `M_F = wL²/12` (both ends)
- SS beam point load P at centre: `M_F = PL/8`

### 4.3 Influence Lines & Energy Methods

**Muller-Breslau** `[P1]`
- Influence line for a reaction/force = deflected shape due to unit displacement in that direction.

**Virtual work** `[P1]`
- `Δ = ∫(M·m/EI)dx` (bending), `Δ = ∫(n·N/EA)dx` (axial)

### 4.4 Matrix Methods

**Stiffness method** `[P2]`
- `{F} = [K]{Δ}`; member stiffness `k = EA/L` (axial), `k = 4EI/L` (bending)
- **Flexibility method**: `{Δ} = [f]{F}`

---

## 5. Reinforced Concrete Structures (IS 456:2000)

### 5.1 Limit State Design

**Partial safety factors** `[P0]`
- Loads: `γ_f = 1.5` (DL+LL), `1.2` (DL+LL+WL/EL), `0.9` (DL+WL stabilizing)
- Materials: `γ_m = 1.5` (concrete), `1.15` (steel)

**Limiting moment** `[P0]`
- `M_u,lim = 0.138 f_ck b d²` (Fe415), `0.133 f_ck b d²` (Fe500)
- `x_u,max/d = 0.48` (Fe415), `0.46` (Fe500)
- `x_u,max/d = 0.53` (Fe250)

**Flexure (singly reinforced)** `[P0]`
- `M_u = 0.87 f_y A_st d (1 − A_st f_y/(b d f_ck))`
- Balanced steel: `A_st,bal = 0.36 f_ck b x_u,max/f_y`

**Shear** `[P0]`
- Nominal shear: `τ_v = V_u/(b d)`
- Design shear strength of concrete: `τ_c` (from IS 456 Table 19)
- Shear reinforcement: `V_us = 0.87 f_y A_sv d/s_v`
- Max shear stress: `τ_c,max = 2.5 MPa` (M20), `2.8 MPa` (M25), `3.1 MPa` (M30)

**Development length** `[P0]`
- `L_d = φ σ_s/(4 τ_bd)`
- `τ_bd` (M20): 1.2 MPa; (M25): 1.4 MPa; (M30): 1.5 MPa (plain bars); deformed bars: 1.6× these values

**Steel limits** `[P0]`
- Min tension steel: `0.85 bd/f_y`
- Max tension steel: `0.04 bD`
- Min shear steel: `0.4%` of gross area (for beams)

### 5.2 Columns

**Short column** `[P0]`
- `P_u = 0.4 f_ck A_c + 0.67 f_y A_sc` (with ties)
- `P_u = 0.45 f_ck A_c + 0.75 f_y A_sc` (with helical reinforcement)
- Min eccentricity: `e_min = l/500 + D/30`
- Slenderness: `l_eff/b ≤ 12` (short); `> 12` (long)

### 5.3 Slabs

**One-way vs two-way** `[P0]`
- One-way: `l_y/l_x > 2`; two-way: `l_y/l_x ≤ 2`
- **GATE trap**: original sheet had this reversed (`≤ 2` for one-way).

**Two-way slab coefficients** `[P1]`
- `M = α w l_x²` (α from IS 456 Table 26)

### 5.4 Serviceability

**Deflection** `[P1]`
- Span/depth limits: cantilever `1/7`, simply supported `1/20`, continuous `1/26`
- Modification factors for steel %, span, etc.

---

## 6. Steel Structures (IS 800:2007)

### 6.1 Partial Safety Factors

**Material factors** `[P0]`
- `γ_M0 = 1.1` (yield), `γ_M1 = 1.25` (ultimate), `γ_Mw = 1.25` (weld), `γ_Mb = 1.25` (bolt)

### 6.2 Tension Members

**Design strength** `[P0]`
- Gross yielding: `T_dg = A_g f_y/γ_M0`
- Net rupture: `T_dn = 0.9 A_n f_u/γ_M1`
- Block shear: `T_db` (from IS 800 Cl. 6.4)

### 6.3 Compression Members

**Buckling** `[P0]`
- `f_cd = f_y/γ_M0 / (φ + √(φ² − λ²))` where `φ = 0.5[1 + α(λ − 0.2) + λ²]`
- Non-dimensional slenderness: `λ = √(f_y/f_cr)`, `f_cr = π²E/(KL/r)²`
- **GATE trap**: use `KL/r`, not `L/r`.

### 6.4 Beams

**Bending** `[P1]`
- `M_d = β_b Z_p f_y/γ_M0` (plastic), `M_d = Z_e f_y/γ_M0` (elastic)
- Lateral torsional buckling: `M_cr` from IS 800 Cl. 8.2.2

### 6.5 Connections

**Bolts** `[P0]`
- Shear: `V_dsb = f_ub n_n A_nb/(√3 γ_Mb)` (n_n = shear planes)
- Bearing: `V_dpb = 2.5 k_b d t f_u/γ_Mb`
- Tension: `T_db = 0.9 f_ub A_nb/γ_Mb`

**Welds** `[P0]`
- `f_wd = f_u/(√3 γ_Mw)`
- Fillet weld strength: `P = f_wd × l_eff × t_t` (t_t = throat thickness = 0.7s)

---

## 7. Geotechnical Engineering

### 7.1 Phase Relationships

**Basic relations** `[P0]`
- Void ratio: `e = V_v/V_s`; porosity: `n = V_v/V = e/(1+e)`
- Degree of saturation: `S = V_w/V_v`
- **Key relation**: `Se = wG_s`
- Water content: `w = W_w/W_s`

**Densities** `[P0]`
- Bulk: `γ = (G_s + Se)γ_w/(1+e)`
- Dry: `γ_d = G_s γ_w/(1+e)`
- Submerged: `γ' = (G_s − 1)γ_w/(1+e)`
- Saturated: `γ_sat = (G_s + e)γ_w/(1+e)`
- **GATE trap**: `γ_d = γ/(1+w)`, `γ' = γ_sat − γ_w`

**Relative density** `[P1]`
- `D_r = (e_max − e)/(e_max − e_min)`

### 7.2 Index Properties & Classification

**Consistency** `[P1]`
- Plasticity index: `I_p = w_L − w_P`
- Liquidity index: `I_L = (w − w_P)/I_p`
- Consistency index: `I_c = (w_L − w)/I_p`

**A-line** `[P1]`
- `PI = 0.73(LL − 20)` (clay); `PI = 0.73(LL − 20) ± 4` (silt/clay boundary)

**Group index** `[P2]`
- `GI = 0.2a + 0.005ac + 0.01bd`
- `a = P200 − 35` (0–40), `b = P200 − 15` (0–40), `c = LL − 40` (0–20), `d = PI − 10` (0–20)

### 7.3 Compaction

**Proctor** `[P1]`
- `γ_d = γ/(1+w)`; zero-air-voids curve: `γ_d = G_s γ_w/(1 + wG_s/S)`
- OMC typically 12–18%, max dry density 1.6–1.9 g/cc

### 7.4 Permeability & Seepage

**Darcy's law** `[P0]`
- `v = ki`, `Q = kiA`; `k` = hydraulic conductivity (m/s)
- Constant head: `k = QL/(Aht)`
- Falling head: `k = (aL/At) ln(h₁/h₂)`
- Flow net: `q = kH(N_f/N_d)`
- Critical hydraulic gradient: `i_c = (G_s − 1)/(1+e) = γ'/γ_w`
- **GATE trap**: `i_c` for quick sand condition; boiling when `i ≥ i_c`.

### 7.5 Effective Stress

**Effective stress** `[P0]`
- `σ' = σ − u`
- Capillary rise: `h_c = 4T/(γ_w d)` (T = surface tension)

### 7.6 Consolidation

**Settlement** `[P0]`
- Normally consolidated: `S_c = [C_c/(1+e₀)] H log(σ'_f/σ'_i)`
- Over-consolidated (σ'_f < σ'_c): `S_c = [C_r/(1+e₀)] H log(σ'_f/σ'_i)`
- Over-consolidated (σ'_f > σ'_c): `S_c = [C_r/(1+e₀)] H log(σ'_c/σ'_i) + [C_c/(1+e₀)] H log(σ'_f/σ'_c)`

**Time rate** `[P0]`
- `T_v = c_v t/H_dr²`; `c_v = k/(m_v γ_w)`
- `T_v = (π/4)(U/100)²` for U < 60%; `T_v = 1.781 − 0.933 log(100 − U)` for U > 60%
- `T_v(50%) = 0.197`, `T_v(90%) = 0.848`
- **GATE trap**: `H_dr` = half thickness for double drainage, full thickness for single drainage.

### 7.7 Shear Strength

**Mohr-Coulomb** `[P0]`
- `τ_f = c + σ' tanφ`
- Triaxial: `σ₁ = σ₃ N_φ + 2c√N_φ`, `N_φ = tan²(45° + φ/2)`
- Unconfined compression: `q_u = 2c_u` (φ = 0)
- Vane shear: `c_u = T/[πD²(H/2 + D/6)]`

**Drained vs undrained** `[P1]`
- Drained (c', φ'): use effective stresses
- Undrained (c_u, φ_u = 0): use total stresses

### 7.8 Earth Pressure

**Rankine** `[P0]`
- `K_a = tan²(45° − φ/2)`, `K_p = tan²(45° + φ/2)`
- Active (cohesive): `p_a = K_a σ_v − 2c√K_a`
- Passive (cohesive): `p_p = K_p σ_v + 2c√K_p`
- **GATE trap**: tension crack depth `z_c = 2c/(γ√K_a)`; active pressure zero above this.

**Coulomb** `[P1]`
- `K_a = sin²(α+φ)/[sin²α sin(α−δ) (1 + √(sin(φ+δ)sin(φ−β)/(sin(α−δ)sin(α+β))))²]`

### 7.9 Bearing Capacity

**Terzaghi** `[P0]`
- Strip: `q_u = cN_c + qN_q + 0.5γBN_γ`
- Square: `q_u = 1.3cN_c + qN_q + 0.4γBN_γ`
- Circular: `q_u = 1.3cN_c + qN_q + 0.3γBN_γ`
- `N_q = e^(πtanφ) tan²(45°+φ/2)`, `N_c = (N_q − 1)cotφ`, `N_γ` (from table)

**Net safe pressure** `[P0]`
- `q_ns = (q_u − γD_f)/FOS + γD_f` (FOS typically 2.5–3)

### 7.10 Settlement & Foundations

**Immediate settlement** `[P1]`
- `S_i = qB(1−ν²)I_f/E`

**Pile capacity** `[P0]`
- `Q_u = q_b A_b + Σ f_s A_s` (end bearing + skin friction)
- In clay: `Q_u = N_c c_u A_b + α c_u A_s`

### 7.11 Slope Stability

**Infinite slope** `[P1]`
- Dry: `F_s = tanφ/tanβ`
- Seepage parallel to slope: `F_s = (γ'/γ_sat)(tanφ/tanβ)`
- **GATE trap**: seepage case reduces F_s by factor `γ'/γ_sat ≈ 0.5`.

**Finite slope** `[P2]`
- Fellenius (φ=0): `F_s = c_u R²θ/(W d)`
- Bishop's simplified: iterative slice method

---

## 8. Fluid Mechanics

### 8.1 Properties

**Viscosity** `[P0]`
- Newton's law: `τ = μ du/dy`
- Kinematic: `ν = μ/ρ`
- **GATE trap**: `μ` (Pa·s) vs `ν` (m²/s); water `μ ≈ 10⁻³ Pa·s`, `ν ≈ 10⁻⁶ m²/s`.

**Surface tension** `[P1]`
- Pressure inside droplet: `Δp = 4T/d`; inside bubble: `Δp = 8T/d`; jet: `Δp = 2T/d`

**Compressibility** `[P1]`
- Bulk modulus: `K = −dp/(dV/V)`

### 8.2 Hydrostatics

**Pressure** `[P0]`
- `p = γh` (gauge); `p_abs = p_gauge + p_atm`
- **GATE trap**: gauge vs absolute — always check.

**Hydrostatic force** `[P0]`
- Plane surface: `F = γA h̄` (h̄ = depth of centroid)
- Centre of pressure: `y_p = ȳ + I_c/(A ȳ)`
- **GATE trap**: `I_c` about centroidal axis, not about water surface.

**Buoyancy** `[P1]`
- `F_b = γ_w V_displaced`; metacentric height `GM = BM − BG`, `BM = I/V`

### 8.3 Kinematics & Dynamics

**Continuity** `[P0]`
- `A₁v₁ = A₂v₂` (incompressible); `ρ₁A₁v₁ = ρ₂A₂v₂` (compressible)

**Bernoulli** `[P0]`
- `p/γ + v²/2g + z = constant` (along streamline, steady, inviscid, incompressible)
- With losses: `p₁/γ + v₁²/2g + z₁ = p₂/γ + v₂²/2g + z₂ + h_L`

**Momentum** `[P0]`
- `ΣF = ρQ(V₂ − V₁)` (vector)
- Force on plate: normal `F = ρAV²`; inclined `F = ρAV² sinθ`

### 8.4 Dimensional Analysis

**Dimensionless numbers** `[P0]`
- Reynolds: `Re = ρVD/μ = VD/ν` (laminar pipe flow: Re < 2000)
- Froude: `Fr = V/√(gL)` (open channel: < 1 subcritical, = 1 critical, > 1 supercritical)
- Euler: `Eu = Δp/(ρV²)`
- Mach: `M = V/c`

**Buckingham π** `[P1]`
- Number of π terms = n − m (n = variables, m = fundamental dimensions)

### 8.5 Pipe Flow

**Darcy-Weisbach** `[P0]`
- `h_f = f(L/D)(v²/2g)`
- **GATE trap**: `D` is pipe diameter; for non-circular use hydraulic diameter `D_h = 4A/P`.

**Hagen-Poiseuille (laminar)** `[P0]`
- `f = 64/Re` (Re < 2000)
- `h_f = 32μVL/(γD²)` (direct form)
- **GATE trap**: valid ONLY for laminar flow (Re < 2000). For turbulent use Colebrook/Swamee-Jain.

**Hazen-Williams** `[P1]`
- `h_f = 10.67 L Q^1.85/(C^1.85 D^4.87)` (Q in m³/s, D in m)
- `C ≈ 100–140` for new pipes

**Manning (pipe)** `[P1]`
- `v = (1/n) R^(2/3) S^(1/2)` (R = A/P)

**Colebrook-White** `[P2]`
- `1/√f = −2 log₁₀(ε/(3.7D) + 2.51/(Re√f))`

**Swamee-Jain** `[P2]`
- `f = 0.25/[log₁₀(ε/(3.7D) + 5.74/Re^0.9)]²`

**Minor losses** `[P1]`
- `h_m = K v²/2g`; sudden expansion: `h_m = (v₁−v₂)²/2g`; sudden contraction: `h_m = 0.5v₂²/2g`

### 8.6 Boundary Layer

**Thickness** `[P2]`
- Laminar (Blasius): `δ = 5x/√Re_x`; displacement `δ* = 1.72x/√Re_x`
- Turbulent: `δ = 0.37x/Re_x^(1/5)`
- Drag: `F_D = C_D (1/2)ρAV²`

---

## 9. Hydraulics / Open Channel Flow

### 9.1 Uniform Flow

**Manning** `[P0]`
- `Q = (1/n) A R^(2/3) S^(1/2)`
- **GATE trap**: `R = A/P` (hydraulic radius), NOT pipe radius. For full pipe `R = D/4`.

**Chezy** `[P1]`
- `v = C√(RS)`, `C = (1/n)R^(1/6)`

**Most efficient section** `[P1]`
- Rectangular: `b = 2y` (hydraulic radius `R = y/2`)
- Trapezoidal: half-hexagon, `R = y/2`

### 9.2 Critical Flow & Specific Energy

**Critical depth** `[P0]`
- General: `Q²T/(gA³) = 1`
- Rectangular: `y_c = (q²/g)^(1/3)`
- Critical velocity: `v_c = √(g y_c)`
- Specific energy: `E = y + v²/2g`; minimum at critical depth: `E_min = 1.5 y_c`

**Froude number** `[P0]`
- `Fr = v/√(g y)` (rectangular); `Fr = v/√(g A/T)` (general)
- Subcritical `Fr < 1`, critical `Fr = 1`, supercritical `Fr > 1`

### 9.3 Hydraulic Jump

**Sequent depth** `[P0]`
- `y₂/y₁ = ½[√(1 + 8Fr₁²) − 1]`
- Energy loss: `ΔE = (y₂ − y₁)³/(4y₁y₂)`
- Jump length: `L_j ≈ 6.9(y₂ − y₁)` (approx)
- **GATE trap**: jump forms only when `Fr₁ > 1` (supercritical upstream).

### 9.4 Gradually Varied Flow

**GVF equation** `[P1]`
- `dy/dx = (S₀ − S_f)/(1 − Fr²)`
- Profiles: M (mild, y > y_c), S (steep, y < y_c), C (critical), H (horizontal), A (adverse)

### 9.5 Pumps & Turbines

**Pump** `[P1]`
- Head: `H = (p₂−p₁)/γ + (v₂²−v₁²)/2g + (z₂−z₁) + h_L`
- Power: `P = γQH/η`
- Specific speed: `N_s = N√Q/H^(3/4)` (Q in m³/s, H in m)
- NPSH: `NPSH = p_atm/γ − h_s − h_fs − p_v/γ`

**Affinity laws** `[P1]`
- `Q ∝ N`, `H ∝ N²`, `P ∝ N³`

**Turbine** `[P2]`
- Specific speed: `N_s = N√P/H^(5/4)` (P in kW)

---

## 10. Hydrology

### 10.1 Precipitation & Infiltration

**Rainfall analysis** `[P1]`
- Average rainfall: arithmetic mean, Thiessen polygon, isohyetal method
- `P = Σ(A_i P_i)/ΣA_i` (Thiessen)

**Infiltration** `[P0]`
- Horton: `f = f_c + (f₀ − f_c)e^(−kt)`
- **GATE trap**: `f₀` = initial (max), `f_c` = final (constant/min).

**Evaporation** `[P1]`
- Dalton: `E = K(e_s − e_a)`
- Pan coefficient: `E_lake = C_p × E_pan` (C_p ≈ 0.7)

### 10.2 Runoff

**Rational method** `[P0]`
- `Q = CiA` (Q in m³/s)
- `Q = CiA/360` (A in ha, i in mm/hr)
- `Q = CiA/3.6` (A in km², i in mm/hr)
- **GATE trap**: unit conversion — the constant depends on units. For A in ha and i in mm/hr, divide by 360 (not 3.6).

**SCS-CN** `[P1]`
- `Q = (P − 0.2S)²/(P + 0.8S)`, `S = 25400/CN − 254` (mm)

### 10.3 Hydrographs

**Unit hydrograph** `[P0]`
- Direct runoff: `DRH = UH × excess rainfall (convolution)`
- `UH` = runoff from 1 cm (or 1 mm) excess rainfall over unit duration
- **GATE trap**: UH duration must match rainfall excess duration.

**Synthetic / S-curve** `[P2]`
- S-curve = summation of successive UHs; used to change UH duration.

### 10.4 Flood Frequency

**Gumbel** `[P1]`
- `x_T = x̄ + Kσ`; `K = (√6/π)[0.5772 + ln(ln(T/(T−1)))]`
- **GATE trap**: `K` is negative for T < 2.33 years.

**Return period & risk** `[P0]`
- `R = 1 − (1 − 1/T)^n` (risk of exceedance in n years)
- Reliability: `= (1 − 1/T)^n`

### 10.5 Groundwater

**Darcy (aquifer)** `[P0]`
- `Q = KiA`

**Theis** `[P1]`
- `s = (Q/4πT) W(u)`, `u = r²S/(4Tt)`
- Valid for confined, unsteady flow

**Cooper-Jacob** `[P1]`
- `s = (2.3Q/4πT) log₁₀(2.25Tt/(r²S))` (valid for `u < 0.01`)

**Thiem** `[P2]`
- `Q = 2πT(h₂ − h₁)/ln(r₂/r₁)` (steady confined)

---

## 11. Environmental Engineering

### 11.1 Water Demand & Quality

**Population forecasting** `[P0]`
- Arithmetic: `P_n = P₀ + n x̄`
- Geometric: `P_n = P₀(1 + r)^n`
- Incremental: `P_n = P₀ + n x̄ + n(n+1)/2 × ȳ`

**Water demand** `[P1]`
- Per capita demand: 135–200 LPCD (Indian standards)
- Max daily = 1.8 × avg; max hourly = 1.5 × max daily

**Hardness** `[P1]`
- `Hardness (mg/L as CaCO₃) = (Ca²⁺/20 + Mg²⁺/12.15) × 50`
- **GATE trap**: divide by equivalent weights (Ca=20, Mg=12.15), not molar masses.

**pH** `[P0]`
- `pH = −log[H⁺]`; `[H⁺][OH⁻] = 10⁻¹⁴` (25°C)

### 11.2 Water Treatment

**Sedimentation** `[P0]`
- Terminal settling: `v_s = (g/18)(ρ_s − ρ_w)d²/μ` (Stokes, laminar)
- Overflow rate: `v₀ = Q/A`; removal fraction `= v_s/v₀`
- **GATE trap**: Stokes valid for `Re < 1` (small particles).

**Coagulation-flocculation** `[P1]`
- Velocity gradient: `G = √(P/(μV))`; `Gt` typically 10⁴–10⁵

**Filtration** `[P1]`
- Rapid sand filter: rate 4–6 m/h, bed 0.6–0.7 m
- Slow sand filter: rate 0.1–0.2 m/h

**Disinfection** `[P1]`
- Chick's law: `N/N₀ = e^(−kt)`
- CT concept: `CT ≥ 30 mg·min/L` (typical)

### 11.3 Wastewater

**BOD** `[P0]`
- `BOD_t = L₀(1 − e^(−kt))`; `BOD₅ = L₀(1 − e^(−5k))`
- `k` (base e) ≈ 0.23/day at 20°C; `k_T = k₂₀ × 1.047^(T−20)`
- **GATE trap**: BOD < COD; COD/BOD ≈ 1.5–2.0 for domestic.

**Activated sludge** `[P0]`
- `F/M = QS₀/(VX)`
- `SRT = VX/(Q_w X_w + Q_e X_e)`
- `V = QS₀Y(SRT)/[X(1 + k_d·SRT)]`
- Sludge volume index: `SVI = V_settled(ml/L) × 1000/MLSS(mg/L)`

**Trickling filter** `[P1]`
- Recirculation ratio: `R = Q_r/Q`

**Sewer design** `[P1]`
- Min velocity: 0.6 m/s (self-cleansing); max: 3 m/s
- Min diameter: 200 mm (150 mm in some codes)

### 11.4 Air Pollution

**Dispersion** `[P2]`
- Gaussian plume: `C = (Q/2πuσ_yσ_z) exp(−y²/2σ_y²) [exp(−(z−H)²/2σ_z²) + exp(−(z+H)²/2σ_z²)]`

**Control** `[P2]`
- Cyclone efficiency, ESP (Deutsch): `η = 1 − e^(−wA/Q)`

### 11.5 Solid Waste

**Generation** `[P2]`
- Per capita: 0.3–0.6 kg/day (Indian urban)
- Landfill gas: methane from anaerobic decomposition

---

## 12. Transportation Engineering

### 12.1 Geometric Design

**Sight distance** `[P0]`
- SSD: `SSD = 0.278 V t_R + V²/(254f)` (V in km/h, SSD in m)
- OSD: `OSD = d₁ + d₂ + d₃` (reaction + overtaking + clearance)
- **GATE trap**: `0.278` converts km/h to m/s; `254 = 2g × 1000/3600²` factor.

**Superelevation** `[P0]`
- `e + f = V²/(127R)` (V in km/h, R in m)
- `e_max = 0.07` (IRC); `f` design ≤ 0.15
- **GATE trap**: if required `e > e_max`, reduce speed.

**Curves** `[P1]`
- Transition length: `L = V³/(4RC)` (C = rate of change of centrifugal accel, 0.5–0.8 m/s³)
- Setback distance, extra widening: `W_e = nl²/(2R) + V/(9.5√R)`

**Vertical curves** `[P1]`
- Length (SSD): `L = NS²/(4.4)` (crest, S < L); `L = NS²/(h₁+h₂)` general
- Valley curve: comfort criterion `L = NV³/360`

### 12.2 Traffic Engineering

**Fundamental diagram** `[P0]`
- `q = kv`; `k_j` = jam density, `v_f` = free-flow speed
- Max flow: `q_max = k_j v_f/4` (linear model)

**Shockwave** `[P1]`
- `w = (q₂ − q₁)/(k₂ − k₁)`

**Greenshields** `[P1]`
- `v = v_f(1 − k/k_j)`

**Signal design (Webster)** `[P0]`
- Optimum cycle: `C₀ = 1.5L + 5/(1 − ΣY)` (L = lost time, Y = flow/saturation)
- Green split: `g_i = (C₀ − L) × Y_i/ΣY`

### 12.3 Pavements

**Flexible (IRC 37)** `[P1]`
- Design based on CBR: `T = (914 + 914 log₁₀(N))/CBR^0.5` (approx, N = cumulative standard axles)

**Rigid (IRC 58)** `[P1]`
- Westergaard: `σ = 0.316P/h² [4 log₁₀(l/b) + 1.069]` (interior loading)
- Radius of relative stiffness: `l = [Eh³/(12(1−μ²)k)]^(1/4)`

---

## 13. Geomatics / Surveying

### 13.1 Errors & Adjustments

**Error types** `[P1]`
- Systematic (cumulative, same sign) vs accidental (random)
- Most probable value = arithmetic mean

### 13.2 Levelling

**Curvature & refraction** `[P0]`
- Curvature correction: `C_c = −0.0785 D²` (D in km, m)
- Refraction correction: `C_r = +0.0112 D²` (D in km, m)
- Combined: `C = −0.0673 D²`
- **GATE trap**: curvature −ve, refraction +ve; combined −0.0673D².

**Leveling equations** `[P1]`
- `H = BS − FS` (rise/fall); `ΣBS − ΣFS = last RL − first RL`

### 13.3 Traversing

**Latitude & departure** `[P0]`
- `L = l cosθ`, `D = l sinθ`
- Closing error: `e = √((ΣL)² + (ΣD)²)`
- Relative error: `e/Σl` (should be < 1/2000 for traverse)

**Area by coordinates** `[P0]`
- `A = ½|Σ(x_i y_{i+1} − x_{i+1} y_i)|`

### 13.4 Theodolite & Tacheometry

**Tacheometry** `[P1]`
- `D = ks + C` (k = 100, C = 0 for anallactic)
- Inclined: `D = ks cos²θ`, `V = ks sin2θ/2`

### 13.5 Curves

**Simple curve** `[P1]`
- `T = R tan(Δ/2)`, `L = RΔ` (Δ in radians), `E = R(sec(Δ/2) − 1)`
- Chainage of tangent points, deflection angle method

### 13.6 Remote Sensing / GIS

**RS basics** `[P2]`
- Resolution: spatial, spectral, radiometric, temporal
- NDVI = `(NIR − Red)/(NIR + Red)`

**GIS** `[P2]`
- Raster vs vector; overlay, buffer, network analysis

---

## 14. Construction Management

### 14.1 CPM

**Critical path** `[P0]`
- `TF = LS − ES = LF − EF` (total float)
- `FF = ES_next − EF_current` (free float)
- Critical activities: `TF = 0`
- **GATE trap**: project duration = longest path, not sum of all activities.

### 14.2 PERT

**Three-point estimate** `[P0]`
- `t_e = (t₀ + 4t_m + t_p)/6`
- Variance: `σ² = ((t_p − t₀)/6)²`
- Project variance = sum of variances on critical path
- Probability of completion: `Z = (T_s − T_e)/σ`

### 14.3 Cost & Time

**Cost slope** `[P1]`
- `Cost slope = (Crash cost − Normal cost)/(Normal time − Crash time)`
- Crashing: reduce critical activities with lowest cost slope first

### 14.4 Estimation & Contracts

**Rate analysis** `[P1]`
- `Rate = (Material cost + Labour cost + Equipment cost) × (1 + contractor's profit%)`

**Contracts** `[P2]`
- Types: lump sum, item rate, cost plus, percentage rate
- Earned value: `EV = %complete × BAC`; `CPI = EV/AC`; `SPI = EV/PV`

---

## 15. Constants & Unit Conversions

### 15.1 Physical Constants

| Constant | Value |
| -------- | ----- |
| g | 9.81 m/s² |
| γ_w | 9.81 kN/m³ |
| ρ_w | 1000 kg/m³ |
| μ_w (20°C) | 1.002 × 10⁻³ Pa·s |
| ν_w (20°C) | 1.004 × 10⁻⁶ m²/s |
| 1 atm | 101.325 kPa = 10.33 m water |
| E_steel | 200 GPa |
| G_steel | 77 GPa |
| E_concrete | 5000√f_ck MPa (IS 456) |
| α_steel | 12 × 10⁻⁶ /°C |
| π | 3.1416 |
| e | 2.718 |

### 15.2 Unit Conversions

| Conversion | Factor |
| ---------- | ------ |
| 1 km/h → m/s | ÷ 3.6 |
| 1 m/s → km/h | × 3.6 |
| 1 kN/m³ → kg/m³ | × 101.97 |
| 1 MPa → kN/m² | × 1000 |
| 1 N/mm² | = 1 MPa |
| 1 m²/s → cm²/s | × 10⁴ |
| 1 Darcy | ≈ 10⁻¹² m² |
| 1 ha | = 10⁴ m² |
| 1 MLD | = 10³ m³/day = 0.01157 m³/s |
| 1 cusec | = 0.0283 m³/s |
| 1 acre-foot | = 1233.5 m³ |
| 1° | = 0.01745 rad |

### 15.3 Common Trigonometric Values

| Angle | sin | cos | tan |
| ----- | --- | --- | --- |
| 0° | 0 | 1 | 0 |
| 30° | 0.5 | 0.866 | 0.577 |
| 45° | 0.707 | 0.707 | 1 |
| 60° | 0.866 | 0.5 | 1.732 |
| 90° | 1 | 0 | ∞ |

### 15.4 Common Fraction-Percentage Conversions

| Fraction | % | Fraction | % |
| -------- | - | -------- | - |
| 1/2 | 50% | 1/7 | 14.28% |
| 1/3 | 33.33% | 1/8 | 12.5% |
| 1/4 | 25% | 1/9 | 11.11% |
| 1/5 | 20% | 1/10 | 10% |
| 1/6 | 16.67% | 1/12 | 8.33% |

---

## 16. Final Rapid Revision

### 30-Minute (P0 Only)

- `σ = My/I`, `τ = VQ/Ib`, `P_cr = π²EI/(KL)²`
- `M_u,lim = 0.138f_ckbd²` (Fe415), `0.133f_ckbd²` (Fe500)
- `Se = wG_s`, `σ' = σ − u`, `τ_f = c + σ'tanφ`
- `q_u = cN_c + qN_q + 0.5γBN_γ`
- `T_v = c_vt/H_dr²`, `T_v(50%) = 0.197`, `T_v(90%) = 0.848`
- `h_f = f(L/D)(v²/2g)`, `y_c = (q²/g)^(1/3)`
- `y₂/y₁ = ½[√(1+8Fr₁²) − 1]`
- `Q = CiA`, `s = (Q/4πT)W(u)`
- `BOD_t = L₀(1−e^(−kt))`, `F/M = QS₀/(VX)`
- `SSD = 0.278Vt_R + V²/(254f)`, `e + f = V²/(127R)`
- `q = kv`, `C₀ = (1.5L + 5)/(1 − ΣY)`
- `t_e = (t₀ + 4t_m + t_p)/6`

### 2-Hour (P0 + P1)

Full formula sheet above, sections 1–14. Skip `[P2]`/`[P3]` items.

### 1-Day (Complete)

Entire sheet + [`RAPID_REVISION.md`](../RAPID_REVISION.md) + [`revision_notes/gate-civil-revision.md`](../revision_notes/gate-civil-revision.md).

---

## References

- [`civil/gate-civil-notes.md`](../civil/gate-civil-notes.md) — Detailed topic-wise notes
- [`practice/gate-civil-practice.md`](../practice/gate-civil-practice.md) — Solved problems
- [`pyq/gate-civil-pyq.md`](../pyq/gate-civil-pyq.md) — PYQ system
- [`revision_notes/gate-civil-revision.md`](../revision_notes/gate-civil-revision.md) — Rapid revision cards
- [`../civil/gate-civil-notes.md`](../civil/gate-civil-notes.md) — GATE notes (legacy link)
