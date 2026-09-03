# GATE Civil — Rapid Revision Cards

## Overview

One-page rapid revision cards for each major GATE Civil topic. Use for last-minute review. Each card: key formulas, concepts, and common question types.

---

## 📐 CARD 1: Engineering Mathematics

### Linear Algebra
| Concept | Formula/Key Point |
|---------|-------------------|
| Eigenvalues | det(A - λI) = 0 |
| Cayley-Hamilton | Every matrix satisfies its characteristic equation |
| Rank | Number of non-zero rows in echelon form |
| Inverse | A⁻¹ = adj(A)/det(A) |

### Calculus
| Concept | Formula |
|---------|---------|
| Taylor Series | f(x) = f(a) + f'(a)(x-a) + f''(a)(x-a)²/2! + ... |
| Gradient | ∇f = (∂f/∂x, ∂f/∂y, ∂f/∂z) |
| Divergence | ∇·F = ∂Fx/∂x + ∂Fy/∂y + ∂Fz/∂z |
| Curl | ∇×F = determinant |

### Differential Equations
| Type | Solution Approach |
|------|-------------------|
| dy/dx + P(x)y = Q(x) | IF = e^∫Pdx |
| d²y/dx² + ay = 0 | y = C₁cos(√ax) + C₂sin(√ax) |
| Cauchy-Euler | x²y'' + axy' + by = 0 → try y = x^m |

### Probability
| Concept | Formula |
|---------|---------|
| Bayes | P(A|B) = P(B|A)P(A)/P(B) |
| Binomial | P(X=k) = C(n,k)p^k(1-p)^(n-k) |
| Normal | f(x) = (1/√2πσ²)e^(-(x-μ)²/2σ²) |
| E[X] | ΣxP(x) |

### Numerical Methods
| Method | Formula |
|--------|---------|
| Newton-Raphson | x_{n+1} = x_n - f(x_n)/f'(x_n) |
| Trapezoidal | ∫f(x)dx ≈ h/2[f₀ + 2(f₁+...+f_{n-1}) + f_n] |
| Simpson 1/3 | ∫f(x)dx ≈ h/3[f₀ + 4f₁ + 2f₂ + 4f₃ + ... + f_n] |

---

## 🏗️ CARD 2: Structural Engineering

### Mechanics
| Concept | Formula |
|---------|---------|
| Bending Stress | σ = My/I |
| Shear Stress | τ = VQ/Ib |
| Torsion | T/J = τ/r = Gθ/L |
| Deflection | EI d²y/dx² = M(x) |

### Columns
| End Condition | K | P_cr |
|---------------|---|------|
| Fixed-Fixed | 0.5 | π²EI/(0.5L)² |
| Fixed-Pinned | 0.7 | π²EI/(0.7L)² |
| Pinned-Pinned | 1.0 | π²EI/L² |
| Fixed-Free | 2.0 | π²EI/(2L)² |

### IS 456 (RCC)
| Parameter | Value |
|-----------|-------|
| M_u,lim (Fe415) | 0.138f_ckbd² |
| M_u,lim (Fe500) | 0.133f_ckbd² |
| x_u,max/d (Fe415) | 0.48 |
| x_u,max/d (Fe500) | 0.46 |
| Min tension steel | 0.85bd/f_y |
| Load factors | 1.5(DL+LL), 1.2(DL+LL±WL) |

### IS 800 (Steel)
| Parameter | Value |
|-----------|-------|
| γ_M0 (yield) | 1.1 |
| γ_M1 (ultimate) | 1.25 |
| Tension (net) | 0.9A_nf_u/γ_M1 |
| Bolt shear | f_ub n_n A_nb/(√3γ_Mb) |

---

## 🪨 CARD 3: Geotechnical Engineering

### Soil Properties
| Property | Formula |
|----------|---------|
| Void ratio | e = V_v/V_s |
| Porosity | n = e/(1+e) |
| Saturation | S = V_w/V_v |
| Se = wG_s | |

### Permeability
| Test | Formula |
|------|---------|
| Constant head | k = QL/(Aht) |
| Falling head | k = (aL/At)ln(h₁/h₂) |

### Shear Strength
| Concept | Formula |
|---------|---------|
| Mohr-Coulomb | τ = c + σ'tanφ |
| Triaxial | σ₁ = σ₃N_φ + 2c√N_φ, N_φ = tan²(45+φ/2) |

### Consolidation
| Parameter | Formula |
|-----------|---------|
| Settlement (NC) | S_c = [C_c/(1+e₀)]H log(σ'_f/σ'_i) |
| Time factor | T_v = c_vt/H²_dr |
| T_v (50%) | 0.197 |
| T_v (90%) | 0.848 |

### Bearing Capacity
| Theory | Formula |
|--------|---------|
| Terzaghi | q_u = cN_c + qN_q + 0.5γBN_γ |
| Net safe | q_s = (q_u - γD_f)/F + γD_f |

### Earth Pressure
| Theory | K_a | K_p |
|--------|-----|-----|
| Rankine | tan²(45-φ/2) | tan²(45+φ/2) |

---

## 💧 CARD 4: Water Resources Engineering

### Fluid Mechanics
| Concept | Formula |
|---------|---------|
| Bernoulli | P/γ + V²/2g + z = constant |
| Continuity | A₁V₁ = A₂V₂ |
| Reynolds | Re = VD/ν |
| Froude | Fr = V/√(gD) |

### Pipe Flow
| Equation | Formula |
|----------|---------|
| Darcy-Weisbach | h_f = f(L/D)(V²/2g) |
| Hazen-Williams | h_f = 10.67LQ^1.85/(C^1.85D^4.87) |
| Manning | V = (1/n)R^(2/3)S^(1/2) |

### Open Channel
| Concept | Formula |
|---------|---------|
| Critical depth (rect) | y_c = (q²/g)^(1/3) |
| Hydraulic jump | y₂/y₁ = ½[√(1+8Fr₁²)-1] |
| Energy loss | ΔE = (y₂-y₁)³/(4y₁y₂) |
| GVF | dy/dx = (S₀-S_f)/(1-Fr²) |

### Hydrology
| Method | Formula |
|--------|---------|
| Rational | Q = CiA |
| Muskingum | O₂ = C₀I₂ + C₁I₁ + C₂O₁ |
| Theis | s = (Q/4πT)W(u) |
| Thiem | Q = 2πT(h₂-h₁)/ln(r₂/r₁) |

---

## 🌍 CARD 5: Environmental Engineering

### Water Treatment
| Process | Key Parameter |
|---------|---------------|
| Coagulation | Alum 20-60 mg/L, G=300-1000 s⁻¹, 30-60s |
| Flocculation | G=20-70 s⁻¹, 15-30 min |
| Sedimentation | Overflow 1-2 m³/m²·h, HRT 2-4 hrs |
| Rapid sand filter | Rate 4-6 m/h, bed 0.6-0.7m |
| Chlorination | Residual 0.2-1.0 mg/L, CT ≥ 30 mg·min/L |

### Wastewater
| Parameter | Typical Value |
|-----------|---------------|
| BOD₅ (domestic) | 200-300 mg/L |
| COD/BOD ratio | 1.5-2.0 |
| ASP F/M ratio | 0.2-0.5 kgBOD/kgMLSS·d |
| MLSS | 1500-3000 mg/L |
| SRT | 5-15 days |
| SVI | 50-150 mL/g |

### Discharge Standards (CPCB)
| Parameter | Inland Surface | Land Disposal |
|-----------|---------------|---------------|
| BOD₅ | < 30 mg/L | < 100 mg/L |
| COD | < 250 mg/L | — |
| TSS | < 100 mg/L | — |
| pH | 5.5-9.0 | 6.0-8.5 |

---

## 🛣️ CARD 6: Transportation Engineering

### Geometric Design
| Parameter | Formula |
|-----------|---------|
| SSD | 0.278Vt_R + V²/(254f) |
| Superelevation | e + f = V²/(127R) |
| Transition curve | L = V³/(4RC), C=0.3 m/s³ |

### Traffic
| Concept | Formula |
|---------|---------|
| Flow-density | q = kv |
| Shockwave | w = (q₂-q₁)/(k₂-k₁) |
| Webster cycle | C = 1.5L/(1-ΣY_i) |

### Pavement
| Type | Design Method |
|------|---------------|
| Flexible | CBR method (IRC 37) |
| Rigid | Westergaard (IRC 58) |

---

## 📏 CARD 7: Surveying

### Traversing
| Concept | Formula |
|---------|---------|
| Latitude | L = l cosθ |
| Departure | D = l sinθ |
| Closing error | ΣL = 0, ΣD = 0 |
| Area (coordinates) | A = ½|Σ(x_i y_{i+1} - x_{i+1} y_i)| |

### Tacheometry
| Formula | D = ks + C (k=100, C=0 for anallactic) |

### Corrections
| Correction | Formula |
|------------|---------|
| Curvature | -0.0785D² (D in km) |
| Refraction | +0.0112D² (D in km) |

---

## 🎯 CARD 8: General Aptitude (Quick)

### Percentages
- Successive change: a + b + ab/100
- Product stability: -x/(1+x/100)
- 12.5% = 1/8, 16.67% = 1/6, 33.33% = 1/3

### Speed/Time/Distance
- Avg speed (equal dist): 2xy/(x+y)
- Relative speed: same dir = x-y, opp = x+y
- Train + platform: (L_train + L_platform)/V

### Time & Work
- LCM method: Total work = LCM(times)
- Together: xy/(x+y)
- Pipes: 1/x - 1/y = 1/t

### Profit/Loss
- SP = CP(100±P%)/100
- Successive discount: d₁+d₂-d₁d₂/100
- False weight: Gain% = Error/(True-Error)×100

### Probability
- P(A∪B) = P(A)+P(B)-P(A∩B)
- Independent: P(A∩B) = P(A)P(B)
- Bayes: P(A|B) = P(B|A)P(A)/P(B)

---

## 🎯 CARD 9: Key GATE Formulas (One Page)

### Structural
- M_u,lim = 0.138f_ckbd² (Fe415)
- x_u,max/d = 0.48 (Fe415)
- P_cr = π²EI/(KL)²
- σ = My/I, τ = VQ/Ib

### Geotech
- τ = c + σ'tanφ
- q_u = cN_c + qN_q + 0.5γBN_γ
- S_c = C_cH/(1+e₀) log(σ'_f/σ'_i)
- T_v = c_vt/H²_dr

### Water Resources
- h_f = f(L/D)(V²/2g)
- y_c = (q²/g)^(1/3)
- y₂/y₁ = ½[√(1+8Fr₁²)-1]
- Q = CiA
- s = (Q/4πT)W(u)

### Environmental
- BOD_t = L₀(1-e^{-kt})
- F/M = QS₀/(VX)
- SRT = VX/(Q_wX_w + Q_eX_e)

---

## 📋 Last Week Revision Plan

| Day | Morning (2hr) | Evening (1hr) |
|-----|---------------|---------------|
| Mon | Math + Aptitude formulas | PYQs Math |
| Tue | Structural formulas | PYQs Structural |
| Wed | Geotech formulas | PYQs Geotech |
| Thu | Water Resources formulas | PYQs Water |
| Fri | Environmental formulas | PYQs Env |
| Sat | Transportation + Survey | PYQs Trans/Survey |
| Sun | **Full Mock Test** (3hr) | **Analyze mistakes** |

---

## 🚫 Common GATE Traps

| Trap | Avoid By |
|------|----------|
| Unit mismatch | Always convert to consistent units |
| Sign convention | Define +ve direction clearly |
| Partial factor confusion | γ_f for loads, γ_m for materials |
| Effective vs total stress | σ' = σ - u |
| Critical depth vs normal depth | y_c from energy, y_n from Manning |
| BOD vs COD | BOD < COD, ratio ~0.5-0.6 |
| SSD vs OSD | SSD = stopping, OSD = overtaking |
| Curvature vs refraction | Curvature -ve, Refraction +ve |

---

## 📝 Last Minute Checklist

- [ ] All formula sheets memorized
- [ ] 15 years PYQs solved (topic-wise)
- [ ] 5 full mock tests completed
- [ ] Virtual calculator practiced
- [ ] Admit card, ID, stationery ready
- [ ] Exam center location confirmed
- [ ] Sleep 7+ hrs before exam
- [ ] Light breakfast, water bottle

---

## References

* [GATE_Civil_Study_Material_2027](https://github.com/DKS-MANAGER/GATE_Civil_Study_Material_2027)
* [Civil_Placement_IITK](https://github.com/DKS-MANAGER/Civil_Placement_IITK)
* [`../formulas/gate-civil-formulas.md`](../formulas/gate-civil-formulas.md) — Complete formula sheet
* [`../civil/gate-civil-notes.md`](../civil/gate-civil-notes.md) — Detailed topic-wise notes
* [`../practice/gate-civil-practice.md`](../practice/gate-civil-practice.md) — Practice problems
