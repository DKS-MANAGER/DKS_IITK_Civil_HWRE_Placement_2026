# GATE Civil Formulas — Complete Quick Reference

> **One-page formula sheet for GATE Civil + PSU interviews.**
> Print this for daily revision. Target: recall any formula in < 10 seconds.

---

## 📐 Engineering Mathematics

### Linear Algebra
| Formula | Equation |
|---------|----------|
| Determinant | $\|AB\| = \|A\|\cdot\|B\|$, $\|A^T\| = \|A\|$ |
| Eigenvalue | $A\mathbf{v} = \lambda\mathbf{v}$ |
| Cayley-Hamilton | $p(A) = 0$ where $p(\lambda) = \det(\lambda I - A)$ |
| Rank | Row rank = Column rank |

### Calculus
| Formula | Equation |
|---------|----------|
| Taylor series | $f(x) = f(a) + f'(a)(x-a)/1! + f''(a)(x-a)^2/2! + \ldots$ |
| Gradient | $\nabla f = (\partial f/\partial x, \partial f/\partial y, \partial f/\partial z)$ |
| Divergence | $\nabla\cdot\mathbf{F} = \partial F_x/\partial x + \partial F_y/\partial y + \partial F_z/\partial z$ |
| Curl | $\nabla\times\mathbf{F}$ |

### ODE & PDE
| Formula | Equation |
|---------|----------|
| Linear ODE | $dy/dx + P(x)y = Q(x)$ → IF = $e^{\int P(x)dx}$ |
| Homogeneous | $y = C_1e^{m_1x} + C_2e^{m_2x}$ |
| Laplace | $\mathcal{L}\{f(t)\} = \int_0^\infty e^{-st}f(t)dt$ |

### Probability & Statistics
| Formula | Equation |
|---------|----------|
| Bayes | $P(A\|B) = P(B\|A)P(A)/P(B)$ |
| Normal PDF | $f(x) = (1/\sqrt{2\pi\sigma^2})e^{-(x-\mu)^2/2\sigma^2}$ |
| Expected value | $E[X] = \sum xP(x)$ |
| Variance | $\text{Var}(X) = E[X^2] - (E[X])^2$ |
| Binomial | $P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}$ |

### Numerical Methods
| Formula | Equation |
|---------|----------|
| Newton-Raphson | $x_{n+1} = x_n - f(x_n)/f'(x_n)$ |
| Trapezoidal | $\int f(x)dx \approx h/2[f_0 + 2(f_1+\ldots+f_{n-1}) + f_n]$ |
| Simpson's 1/3 | $\int f(x)dx \approx h/3[f_0 + 4f_1 + 2f_2 + 4f_3 + \ldots + f_n]$ |

---

## 🏗️ Structural Engineering

### Static Determinacy
| Structure | Condition |
|-----------|-----------|
| Beam | $m + r = 2j$ (determinate) |
| Truss | $m + r = 2j$ |
| Frame | $3m + r = 3j + e_c$ |

### Deflection Formulas

| Beam Type | Max Deflection | Location |
|-----------|---------------|----------|
| Cantilever (PL at free end) | $PL^3/3EI$ | Free end |
| Simply supported (PL at center) | $PL^3/48EI$ | Center |
| Simply supported (UDL w) | $5wL^4/384EI$ | Center |
| Fixed-fixed (UDL w) | $wL^4/384EI$ | Center |
| Cantilever (UDL w) | $wL^4/8EI$ | Free end |

### Methods
| Method | Key Equation |
|--------|-------------|
| Double integration | $EI\cdot d^2y/dx^2 = M(x)$ |
| Moment-area | $\theta_{AB} = (1/EI)\int M\,dx$ |
| Virtual work | $\Delta = \int(M\cdot m)/(EI)\,dx$ |
| Castigliano | $\delta_i = \partial U/\partial P_i$ |

### Concrete (IS 456:2000)

| Parameter | Formula/Value |
|-----------|--------------|
| Limiting moment (Fe415) | $M_{u,lim} = 0.138f_{ck}bd^2$ |
| Limiting moment (Fe500) | $M_{u,lim} = 0.133f_{ck}bd^2$ |
| $x_{u,max}/d$ (Fe415) | 0.48 |
| $x_{u,max}/d$ (Fe500) | 0.46 |
| Development length | $L_d = \phi\sigma_s/(4\tau_{bd})$ |
| Min tension steel | $0.85bd/f_y$ |
| Max tension steel | $0.04bD$ |
| Min shear steel | $0.4\%$ of gross area |
| One-way slab | $l_y/l_x \leq 2$ |

### Steel (IS 800:2007)

| Parameter | Formula/Value |
|-----------|--------------|
| Column buckling | $\sigma_{cr} = \pi^2E/\lambda^2$, $\lambda = l/r$ |
| Effective length | $L_{eff} = \alpha L$ |
| Tension (net) | $T_{dn} = 0.9A_nf_u/\gamma_{M1}$ |
| Tension (gross) | $T_{dg} = A_gf_y/\gamma_{M0}$ |
| Bolt shear | $V_{dsb} = f_{ub}n_nA_{nb}/(\sqrt{3}\gamma_{Mb})$ |
| Weld strength | $f_{wd} = f_u/(\sqrt{3}\gamma_{Mw})$ |
| $\gamma_{M0}$ | 1.1 (yield) |
| $\gamma_{M1}$ | 1.25 (ultimate) |

---

## 🪨 Geotechnical Engineering

### Soil Classification
| Parameter | Formula |
|-----------|---------|
| A-line | $PI = 0.73(LL - 20)$ |
| Group index | $GI = 0.2a + 0.005ac + 0.01bd$ |
| Relative density | $D_r = (e_{max} - e)/(e_{max} - e_{min})$ |

### Phase Relationships
| Formula | Equation |
|---------|----------|
| Void ratio | $e = V_v/V_s$ |
| Porosity | $n = V_v/V = e/(1+e)$ |
| Saturation | $S = V_w/V_v$ |
| Relation | $Se = wG_s$ |
| Bulk density | $\gamma = (G_s + Se)\gamma_w/(1+e)$ |
| Dry density | $\gamma_d = G_s\gamma_w/(1+e)$ |
| Submerged | $\gamma' = (G_s - 1)\gamma_w/(1+e)$ |

### Permeability & Seepage
| Formula | Equation |
|---------|----------|
| Darcy's law | $Q = kiA$, $v = ki$ |
| Constant head | $k = QL/(Aht)$ |
| Falling head | $k = (aL/At)\ln(h_1/h_2)$ |
| Flow net | $q = kH(N_f/N_d)$ |
| Critical gradient | $i_c = (G_s - 1)/(1+e)$ |

### Effective Stress & Shear Strength
| Formula | Equation |
|---------|----------|
| Effective stress | $\sigma' = \sigma - u$ |
| Mohr-Coulomb | $\tau_f = c + \sigma'\tan\phi$ |
| Triaxial | $\sigma_1 = \sigma_3N_\phi + 2c\sqrt{N_\phi}$, $N_\phi = \tan^2(45+\phi/2)$ |
| Unconfined | $q_u = 2c_u$ (for $\phi = 0$) |
| Vane shear | $c_u = T/[\pi D^2(H/2 + D/6)]$ |

### Consolidation
| Formula | Equation |
|---------|----------|
| Settlement (NC) | $S_c = [C_c/(1+e_0)]H\log(\sigma'_f/\sigma'_i)$ |
| Settlement (OC) | $S_c = [C_r/(1+e_0)]H\log(\sigma'_c/\sigma'_i) + [C_c/(1+e_0)]H\log(\sigma'_f/\sigma'_c)$ |
| Time factor | $T_v = c_vt/H_{dr}^2$ |
| $T_v$ (50%) | 0.197 |
| $T_v$ (90%) | 0.848 |
| $c_v$ | $c_v = k/(m_v\gamma_w)$ |

### Earth Pressure & Bearing Capacity
| Formula | Equation |
|---------|----------|
| Rankine $K_a$ | $\tan^2(45-\phi/2)$ |
| Rankine $K_p$ | $\tan^2(45+\phi/2)$ |
| Active (cohesive) | $p_a = K_a\sigma_v - 2c\sqrt{K_a}$ |
| Passive (cohesive) | $p_p = K_p\sigma_v + 2c\sqrt{K_p}$ |
| Terzaghi $q_u$ | $cN_c + qN_q + 0.5\gamma BN_\gamma$ |
| Net safe | $q_{safe} = (q_u - \gamma D_f)/F + \gamma D_f$ |
| Pile $Q_u$ | $q_bA_b + \sum f_sA_s$ |

---

## 💧 Water Resources Engineering

### Fluid Mechanics
| Formula | Equation |
|---------|----------|
| Bernoulli (with losses) | $P_1/\gamma + \alpha_1v_1^2/2g + z_1 = P_2/\gamma + \alpha_2v_2^2/2g + z_2 + h_L$ |
| Continuity | $A_1v_1 = A_2v_2$ |
| Momentum | $\sum F = \rho Q(V_2 - V_1)$ |
| Reynolds | $Re = \rho VD/\mu = VD/\nu$ |
| Froude | $Fr = V/\sqrt{gD}$ |

### Flow Measurement
| Formula | Equation |
|---------|----------|
| Venturi | $Q = C_dA_1A_2\sqrt{2g\Delta h}/\sqrt{A_1^2-A_2^2}$ |
| Orifice | $Q = C_dA\sqrt{2\Delta P/\rho}$ |
| Weir (suppressed) | $Q = 1.84(L-0.2H)H^{3/2}$ |
| V-notch | $Q = 1.38\tan(\theta/2)H^{5/2}$ |
| Pitot tube | $V = \sqrt{2(P_0-P)/\rho}$ |

### Pipe Flow
| Formula | Equation |
|---------|----------|
| Darcy-Weisbach | $h_f = f(L/D)(v^2/2g)$ |
| Hazen-Williams | $h_f = 10.67LQ^{1.85}/(C^{1.85}D^{4.87})$ |
| Manning | $v = (1/n)R^{2/3}S^{1/2}$ |
| Colebrook-White | $1/\sqrt{f} = -2\log(\epsilon/3.7D + 2.51/Re\sqrt{f})$ |
| Swamee-Jain | $f = 0.25/[\log(\epsilon/3.7D + 5.74/Re^{0.9})]^2$ |

### Open Channel Flow
| Formula | Equation |
|---------|----------|
| Manning | $Q = (1/n)AR^{2/3}S^{1/2}$ |
| Critical depth | $Q^2T/(gA^3) = 1$ |
| Critical (rect.) | $y_c = (q^2/g)^{1/3}$ |
| Hydraulic jump | $y_2/y_1 = 0.5[\sqrt{1+8F_1^2}-1]$ |
| Specific energy | $E = y + v^2/2g$ |
| GVF | $dy/dx = (S_0-S_f)/(1-Fr^2)$ |
| Energy loss (jump) | $\Delta E = (y_2-y_1)^3/(4y_1y_2)$ |

### Hydrology
| Formula | Equation |
|---------|----------|
| Rational | $Q = CiA$ |
| Horton's infiltration | $f = f_c + (f_0-f_c)e^{-kt}$ |
| Muskingum | $O_2 = C_0I_2 + C_1I_1 + C_2O_1$ |
| Darcy's law | $Q = KiA$ |
| Theis | $s = (Q/4\pi T)W(u)$, $u = r^2S/4Tt$ |
| Thiem | $Q = 2\pi T(h_2-h_1)/\ln(r_2/r_1)$ |
| Gumbel | $x_T = \bar{x} + K\sigma$ |
| Risk | $R = 1-(1-1/T)^n$ |

### Sediment Transport
| Formula | Equation |
|---------|----------|
| Shields | $\tau^* = \tau_0/[(\rho_s-\rho)gd]$, $\tau_c^* \approx 0.047$ |
| MPM | $q_b^* = 8(\tau^*-\tau_c^*)^{3/2}$ |
| Rouse | $c/c_a = (y_a/y)^Z$, $Z = w_s/(\kappa u_\tau)$ |
| Strickler | $n = d_{50}^{1/6}/21.1$ |
| HEC-18 scour | $y_s/y_1 = 2.0K_1K_2K_3K_4(a/y_1)^{0.35}Fr^{0.43}$ |

---

## 🛣️ Transportation Engineering

| Formula | Equation |
|---------|----------|
| Flow-density | $q = k\cdot v$ |
| Shockwave | $w = (q_2-q_1)/(k_2-k_1)$ |
| SSD | $SSD = 0.278Vt_R + V^2/(254f)$ |
| Superelevation | $e + f = V^2/(127R)$ |
| Transition curve | $L = V^3/(4RC)$, $C = 0.3$ m/s³ |
| Webster's cycle | $C = 1.5L/(1-\sum Y_i)$ |

---

## 🌍 Environmental Engineering

| Formula | Equation |
|---------|----------|
| BOD decay | $L_t = L_0e^{-kt}$ |
| Streeter-Phelps | $D = (k_1L_0/(k_2-k_1))(e^{-k_1t}-e^{-k_2t}) + D_0e^{-k_2t}$ |
| Population (arithmetic) | $P_n = P_0 + n\bar{x}$ |
| Population (geometric) | $P_n = P_0(1+r)^n$ |
| Hardness | Hardness (mg/L as CaCO₃) = $(Ca^{2+}/20 + Mg^{2+}/12.15)\times 50$ |
| pH | $pH = -\log[H^+]$ |

---

## 📏 Surveying & Geomatics

| Formula | Equation |
|---------|----------|
| Latitude | $L = l\cos\theta$ |
| Departure | $D = l\sin\theta$ |
| Closing error | $\sum L = 0$, $\sum D = 0$ (closed) |
| Area (coordinates) | $A = 0.5\|\sum(x_iy_{i+1} - x_{i+1}y_i)\|$ |
| Stadia | $D = ks + C$ ($k=100$, $C=0$ for anallactic) |
| Curvature correction | $-0.0785D^2$ (D in km) |
| Refraction correction | $+0.0112D^2$ (D in km) |

---

## 🎯 GATE Strategy

| Topic | Weight | Priority |
|-------|--------|----------|
| Geotechnical | 12–15% | P0 |
| Environmental | 10–12% | P0 |
| Transportation | 8–10% | P1 |
| Water Resources | 10–12% | P0 |
| Structures | 12–15% | P0 |
| Surveying | 5–7% | P1 |
| Mathematics | 12–15% | P0 |
| Aptitude | 15% | P0 |

**Daily revision:** Pick 1 topic, write all formulas from memory, check against this sheet.

---

## References

* [`../civil/gate-civil-notes.md`](../civil/gate-civil-notes.md) — Detailed GATE notes
* [`../civil/gate-civil-revision.md`](../revision_notes/gate-civil-revision.md) — Rapid revision cards
