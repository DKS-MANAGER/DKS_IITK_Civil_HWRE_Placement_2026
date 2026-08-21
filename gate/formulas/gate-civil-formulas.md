# GATE Civil Formulas & Quick Reference

## Engineering Mathematics

**Linear Algebra**
- Determinant properties: |AB| = |A|·|B|, |A^T| = |A|
- Eigenvalue equation: A·v = λ·v
- Cayley-Hamilton theorem: p(A) = 0 where p(λ) = det(λI − A)

**Calculus**
- Taylor series: f(x) = f(a) + f'(a)(x−a)/1! + f''(a)(x−a)²/2! + ...
- Partial derivative: ∂f/∂x with y held constant
- Gradient: ∇f = (∂f/∂x, ∂f/∂y, ∂f/∂z)

**ODE & PDE**
- First-order linear ODE: dy/dx + P(x)y = Q(x) → integrating factor e∫P(x)dx
- Separation of variables for PDEs

**Probability & Statistics**
- Bayes' theorem: P(A|B) = P(B|A)·P(A) / P(B)
- Normal distribution PDF: f(x) = (1/√(2πσ²)) e^−(x−μ)²/2σ²
- Expected value: E[X] = Σ x·P(x)

**Numerical Methods**
- Newton-Raphson: x_{n+1} = x_n − f(x_n)/f'(x_n)
- Trapezoidal rule: ∫f(x)dx ≈ h/2 [f₀ + 2(f₁+...+f_{n-1}) + f_n]

## Structural Engineering

**Static Determinacy**
- Beam: m + r = 2j (statically determinate)
- Truss: m + r = 2j where m = members, r = reactions, j = joints

**Deflection**
- Double integration: EI·d²y/dx² = M(x)
- Moment-area theorem: θ_AB = (1/EI)∫M dx, Δ = (1/EI)∫M·x̄ dx
- Macaulay's method for discontinuities
- Virtual work: Δ = ∫(M·m)/(EI) dx

**Concrete (IS 456)**
- Limit state of collapse: μ = 0.36·f_ck·b·x_u·(d−0.416·x_u) / b·d²
- One-way slab: l_y/l_x ≤ 2 → design as one-way
- Development length: L_d = (φ·σ_s)/(4·τ_bd)
- Shear: V_u = 0.36·f_ck^(1/2)·b·d (beam shear)

**Steel (IS 800)**
- Plastic section modulus: Z_p = A·(ȳ_p)
- Effective length: L_eff = α·L (α depends on end conditions)
- Column buckling: σ_cr = π²E/(λ²) where λ = l/r
- Fillet weld strength: F_u·t·(a/√3)

## Geotechnical Engineering

**Soil Classification**
- Unified soil classification: Coarse-grained = GW, GP, GM, GC; Fine-grained = CL, CH, ML, MH
- A-line: liquid limit = 0.73·(plasticity index) + 3

**Permeability**
- Darcy's law: Q = k·i·A where i = hydraulic gradient
- Coefficient of permeability: k = C·D²·γ_w/μ (in m/s)

**Effective Stress**
- σ' = σ − u (total stress minus pore water pressure)
- Critical void ratio concepts

**Shear Strength**
- Mohr-Coulomb: τ = c + σ'·tan(φ)
- Triaxial compression: σ₁ = σ₃·N_φ + 2c·√N_φ where N_φ = tan²(45+φ/2)

**Consolidation**
- Coefficient of volume compressibility: m_v = Δe/(1+e₀)·Δσ'
- Time factor: T_v = c_v·t/H²
- Primary consolidation settlement: S_c = (C_c/(1+e₀))·H·log(σ'_f/σ'_i)

**Earth Pressure**
- Rankine active: P_a = ½·K_a·γ·H² where K_a = tan²(45−φ/2)
- Rankine passive: P_p = ½·K_p·γ·H² where K_p = tan²(45+φ/2)
- Coulomb's wedge theory for inclined walls

## Water Resources Engineering

**Fluid Mechanics**
- Bernoulli (with losses): P₁/γ + α₁·v₁²/2g + z₁ = P₂/γ + α₂·v₂²/2g + z₂ + h_L
- Continuity: A₁·v₁ = A₂·v₂ (steady, incompressible)

**Flow Measurement**
- Venturi meter: Q = C_d·A₁A₂√(2gΔh)/(√(A₁²−A₂²))
- Orifice meter: Q = C_d·A·√(2ΔP/ρ)
- Weir (suppressed): Q = 1.84·(L−0.2H)·H^(3/2)

**Pipe Flow**
- Darcy-Weisbach: h_f = f·(L/D)·(v²/2g)
- Hazen-Williams: h_f = 10.67·L·Q^1.85/(C^1.85·D^4.87)
- Manning's equation: v = (1/n)·R^(2/3)·S^(1/2)

**Pumps & Turbines**
- Pump head: H = (P₂−P₁)/(ρg) + (v₂²−v₁²)/(2g) + (z₂−z₁)
- Specific speed: N_s = N√P/(H^(5/4)) (for pumps)

**Open Channel Flow**
- Normal depth ( Manning ): Q = (1/n)·A·R^(2/3)·S^(1/2)
- Critical depth: Q²T/(gA³) = 1
- Hydraulic jump: y₂/y₁ = ½[√(1+8·F₁²)−1]
- Specific energy: E = y + v²/(2g), minimum at critical depth

**Hydrology**
- Rational method: Q = C·i·A (peak runoff)
- Unit hydrograph: Q = Σ(PDHE)·UH
- Muskingum routing: S = K·O + K·X·I, O_{t+Δt} = C₀·I_{t+Δt} + C₁·I_t + C₂·O_t
- Hazen's formula: v ∝ R^0.6 (for small natural streams)

## Transportation Engineering

**Highway Capacity**
- Fundamental relationship: q = k·v (flow = density × speed)
- Shockwave: w = (q₂−q₁)/(k₂−k₁)

**Geometric Design**
- Stopping sight distance: SSD = 0.278·V·t_R + V²/(254·f)
- Superelevation: e + f = V²/(127·R)
- Transition curve: L = V³/(4·R·C) where C = 0.3 m/s³ (typical)

**Traffic Signal**
- Webster's method: t_L = (1.5·L + 5)/(1−ΣY_i)
- Cycle length: C = 1.5·t_L/(1−ΣY_i) where Y_i = q_i/s_i (critical flow ratio)

## Environmental Engineering

**Water Treatment**
- Filtration rate: q = K·(h/L) (for rapid sand filters)
- BOD removal: L_t = L₀·e^(-k·t)
- Log mean driving force: LMDF = (ΔC₁−ΔC₂)/ln(ΔC₁/ΔC₂)

**Wastewater**
- Sludge volume: V_s = (Q·X·t)/(1+XT_v·t) (activated sludge)
- F/M ratio: F/M = (Q·S₀)/(X·V) where S₀ = influent substrate
- Henry's law: C = k_H·P (gas solubility)

## Surveying & Geomatics

**Traversing**
- Latitude: L = l·cos(θ), Departure: D = l·sin(θ)
- Closing error: ΣL = 0, ΣD = 0 for closed traverse
- Area by coordinates: A = ½|Σ(x_i·y_{i+1} − x_{i+1}·y_i)|

**Tacheometric Survey**
- Stadia formula: D = k·s + C where s = staff intercept
- For anallactic telescope: k = 100, C = 0

---

## Sources
- `F:\2k26Placement\GATE_Civil_Study_Material_2027.md`
- `F:\2k26Placement\Civil_Placement_IITK\README.md`
