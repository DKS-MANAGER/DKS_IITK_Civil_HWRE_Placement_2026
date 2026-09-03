# HWRE Exam Notes — Consolidated Cheat Sheet

> **One-stop rapid revision for IITK Civil/HWRE Placement 2026**
> Covers all core topics with formulas, key concepts, and interview Q&A

---

## 📋 Quick Navigation

| Section | Page | Key Topics |
|---------|------|------------|
| [Fluid Mechanics & Hydraulics](#-fluid-mechanics--hydraulics) | 1 | Bernoulli, Darcy-Weisbach, pumps, boundary layer |
| [Open Channel Flow](#-open-channel-flow) | 2 | GVF, hydraulic jump, Manning, critical depth |
| [Hydrology & Groundwater](#-hydrology--groundwater) | 3 | UH, Muskingum, Theis, Darcy, well hydraulics |
| [Sediment Transport & Scour](#-sediment-transport--scour) | 4 | Shields, MPM, Rouse, HEC-18 scour |
| [Turbulence & CFD](#-turbulence--cfd) | 5 | RANS, k-ε, k-ω SST, LES, y+, OpenFOAM |
| [Structures & Geotech](#-structures--geotech) | 6 | IS 456/800, bearing capacity, consolidation |
| [Irrigation & Water Resources](#-irrigation--water-resources) | 7 | Duty-delta, canal design, reservoir routing |
| [Water Supply & Wastewater](#-water-supply--wastewater) | 8 | Treatment train, BOD/COD, distribution |
| [Flood Control](#-flood-control) | 9 | Muskingum, level-pool, PMF, levees |
| [Aptitude Shortcuts](#-aptitude-shortcuts) | 10 | 55 speed math tricks |
| [Behavioral STAR](#-behavioral-star) | 11 | 30 STAR stories framework |

---

## 🌊 Fluid Mechanics & Hydraulics

### Key Formulas

| Formula | Equation | Use |
|---------|----------|-----|
| Continuity | $A_1V_1 = A_2V_2$ | Mass conservation |
| Bernoulli | $\frac{P}{\gamma} + \frac{V^2}{2g} + z = \text{const}$ | Energy along streamline |
| Darcy-Weisbach | $h_f = f\frac{L}{D}\frac{V^2}{2g}$ | Pipe friction loss |
| Moody/Reynolds | $Re = \frac{VD}{\nu}$ | Flow regime |
| Pump power | $P = \frac{\gamma QH}{\eta}$ | Pump sizing |
| NPSH | $NPSH_A = \frac{P_{atm}}{\gamma} - \frac{P_v}{\gamma} - h_s - h_f$ | Cavitation check |

### Critical Values
- **Laminar:** $Re < 2000$, $f = 64/Re$
- **Transition:** $2000 < Re < 4000$
- **Turbulent:** $Re > 4000$, Moody diagram
- **y+ ranges:** < 5 (resolve), 30–300 (wall functions)

### Interview Q&A
1. **Bernoulli assumptions?** Steady, incompressible, frictionless, along streamline
2. **Reynolds significance?** Inertial/viscous forces ratio
3. **Moody diagram?** $f$ vs $Re$ for various $\epsilon/D$
4. **Cavitation prevention?** $NPSH_A > NPSH_R$, lower pump, larger suction pipe

---

## 🌊 Open Channel Flow

### Key Formulas

| Formula | Equation |
|---------|----------|
| Specific Energy | $E = y + \frac{V^2}{2g}$ |
| Critical Depth (rect.) | $y_c = \left(\frac{q^2}{g}\right)^{1/3}$ |
| Froude Number | $Fr = \frac{V}{\sqrt{gD_h}}$ |
| Manning | $V = \frac{1}{n}R^{2/3}S^{1/2}$ |
| Conjugate Depth | $\frac{y_2}{y_1} = \frac{1}{2}\left(\sqrt{1+8Fr_1^2}-1\right)$ |
| Energy Loss (jump) | $\Delta E = \frac{(y_2-y_1)^3}{4y_1y_2}$ |
| GVF Equation | $\frac{dy}{dx} = \frac{S_0-S_f}{1-Fr^2}$ |

### GVF Profiles
| Slope | Zone 1 | Zone 2 | Zone 3 |
|-------|--------|--------|--------|
| Mild (M) | M1 (backwater) | M2 (drawdown) | M3 (rising) |
| Steep (S) | S1 (rising) | S2 (drawdown) | S3 (backwater) |

### Interview Q&A
1. **Critical depth significance?** Minimum specific energy, $Fr=1$, controls flow
2. **Hydraulic jump?** Supercritical → subcritical, energy dissipation, stilling basins
3. **M1 vs M2?** M1: depth increases downstream (dam); M2: depth decreases (overfall)

---

## 💧 Hydrology & Groundwater

### Key Formulas

| Formula | Equation |
|---------|----------|
| Darcy's Law | $Q = KiA$ |
| Horton Infiltration | $f = f_c + (f_0-f_c)e^{-kt}$ |
| Muskingum | $O_2 = C_0I_2 + C_1I_1 + C_2O_1$ |
| Theis (confined) | $s = \frac{Q}{4\pi T}W(u)$ |
| Cooper-Jacob | $s = \frac{2.3Q}{4\pi T}\log\left(\frac{2.25Tt}{r^2S}\right)$ |
| Thiem (steady) | $Q = \frac{2\pi T(h_2-h_1)}{\ln(r_2/r_1)}$ |
| Gumbel Flood | $x_T = \bar{x} + K\sigma$ |
| Risk | $R = 1-(1-1/T)^n$ |

### Unit Hydrograph
- **Assumptions:** Linearity + Time-invariance
- **S-curve method** for duration conversion
- **Snyder:** $t_p = C_t(LL_c)^{0.3}$, $Q_p = 640C_pA/t_p$

### Interview Q&A
1. **UH assumptions?** Linearity, time-invariance, uniform rainfall
2. **Muskingum vs Level-pool?** Channel (wedge+prism) vs Reservoir (horizontal)
3. **Theis assumptions?** Infinite, homogeneous, isotropic, fully penetrating, constant Q
3. **Cooper-Jacob validity?** $u < 0.01$ (late time/small distance)

---

## 🏔️ Sediment Transport & Scour

### Key Formulas

| Formula | Equation |
|---------|----------|
| Shields | $\tau^* = \frac{\tau_0}{(\rho_s-\rho)gd}$, $\tau_c^* \approx 0.047$ |
| MPM (bed load) | $q_b^* = 8(\tau^*-\tau_c^*)^{3/2}$ |
| Rouse Profile | $\frac{c}{c_a} = \left(\frac{y_a}{y}\right)^Z$, $Z = \frac{w_s}{\kappa u_\tau}$ |
| Strickler | $n = \frac{d_{50}^{1/6}}{21.1}$ |
| HEC-18 Scour | $\frac{y_s}{y_1} = 2.0K_1K_2K_3K_4\left(\frac{a}{y_1}\right)^{0.35}Fr^{0.43}$ |
| Exner | $\frac{\partial z_b}{\partial t} + \frac{1}{1-p}\nabla\cdot\vec{q}_b = 0$ |

### Bed Forms Sequence
Ripples → Dunes → Plane bed → Antidunes → Chutes/pools (increasing Fr)

### Interview Q&A
1. **Shields parameter?** Ratio of bed shear to submerged particle weight
2. **Bed load vs suspended?** Bed: rolls/saltates; Suspended: turbulence-supported, Rouse profile
3. **HEC-18 factors?** $K_1$ (angle), $K_2$ (nose), $K_3$ (bed), $K_4$ (sediment size)
4. **Clear-water vs live-bed?** No supply vs supply replenishes scour hole

---

## 🌀 Turbulence & CFD

### Model Selection

| Application | Recommended | Why |
|-------------|-------------|-----|
| Steady pipe flow | k-ε or SST | Cost-effective |
| Hydraulic jump | LES + VOF | Unsteady, interface |
| Bridge pier scour | SST or LES | Near-wall accuracy |
| Reservoir | k-ε | Large domain, steady OK |
| Sediment transport | SST + Euler-Euler | Multiphase, modulation |

### Key Concepts
- **Boussinesq:** $-\rho\overline{u_i'u_j'} = \mu_t(\partial\bar{u}_i/\partial x_j + \partial\bar{u}_j/\partial x_i) - \frac{2}{3}\rho k\delta_{ij}$
- **k-ε:** Robust, high-Re, poor near walls
- **k-ω SST:** Best for separation, blends k-ω (wall) + k-ε (free stream)
- **LES:** Resolves large eddies, models subgrid
- **DNS:** Resolves all scales, research only

### y+ Guidelines
| Model | Target y+ | Cells in BL |
|-------|-----------|-------------|
| Wall functions | 30–100 | 5–10 |
| Low-Re SST | 1 | 15–20 |
| LES | 1 | 10–20 |

### OpenFOAM Case Structure
```
case/
├── 0/          # Initial & boundary conditions (U, p, k, omega, nut)
├── constant/   # Mesh, turbulenceProperties, transportProperties
├── system/     # controlDict, fvSchemes, fvSolution
```

### Interview Q&A
1. **RANS vs LES vs DNS?** RANS: models all, cheap; LES: resolves large, moderate; DNS: resolves all, expensive
2. **When SST over k-ε?** Adverse pressure gradients, separation, curved flows
3. **y+ importance?** Determines wall treatment; wrong y+ = wrong $\tau_w$
4. **Validation steps?** Grid independence, experimental comparison, y+ check, residuals < 1e-4, mass balance

---

## 🏗️ Structures & Geotech (Breadth)

### IS 456 Key Values
| Parameter | Value |
|-----------|-------|
| $M_{u,lim}$ (Fe415) | $0.138f_{ck}bd^2$ |
| $x_{u,max}/d$ (Fe415) | 0.48 |
| Min tension steel | $0.85bd/f_y$ |
| Load factor (DL+LL) | 1.5 |

### IS 800 Key Values
| Parameter | Value |
|-----------|-------|
| $\gamma_{M0}$ (yield) | 1.1 |
| $\gamma_{M1}$ (ultimate) | 1.25 |
| Tension (net) | $0.9A_nf_u/\gamma_{M1}$ |

### Geotech Key Formulas
| Formula | Equation |
|---------|----------|
| Mohr-Coulomb | $\tau_f = c + \sigma'\tan\phi$ |
| Terzaghi Bearing | $q_u = cN_c + qN_q + 0.5\gamma BN_\gamma$ |
| Rankine $K_a$ | $\tan^2(45-\phi/2)$ |
| Consolidation | $S = \frac{C_cH}{1+e_0}\log\frac{\sigma'_f}{\sigma'_i}$ |
| Time factor | $T_v = c_vt/H_{dr}^2$ |

---

## 🌾 Irrigation & Water Resources

### Duty-Delta
$$D \times \Delta = 8.64B$$
- $D$ = duty (ha/cumec), $\Delta$ = delta (m), $B$ = base period (days)

### Canal Design
| Theory | Formula |
|--------|---------|
| Kennedy | $V_0 = 0.55my^{0.64}$ |
| Lacey | $V = (Qf^2/140)^{1/6}$, $P = 2.67\sqrt{Q}$ |

### Irrigation Efficiencies
- $E_c$ (conveyance) = 70–90%
- $E_a$ (application) = 50–85%
- $E_o = E_c \times E_a$ = 40–75%

### Reservoir Routing
- **Level-pool:** $2S/\Delta t + O = 2I + (2S/\Delta t - O)_{prev}$
- **Muskingum:** $O_2 = C_0I_2 + C_1I_1 + C_2O_1$

---

## 💧 Water Supply & Wastewater

### Water Treatment Train
```
Aeration → Coagulation → Flocculation → Sedimentation → Filtration → Disinfection
```

### Key Parameters
| Process | Parameter | Value |
|---------|-----------|-------|
| Coagulation | Alum dose | 20–60 mg/L |
| Flocculation | G, time | 20–70 s⁻¹, 15–30 min |
| Sedimentation | Overflow rate | 1–2 m³/m²·h |
| Rapid sand filter | Rate | 4–6 m/h |
| Chlorination | Residual | 0.2–1.0 mg/L |

### Wastewater (ASP)
| Parameter | Value |
|-----------|-------|
| F/M ratio | 0.2–0.5 kgBOD/kgMLSS·d |
| MLSS | 1500–3000 mg/L |
| SRT | 5–15 days |
| HRT | 4–8 hours |
| SVI | 50–150 mL/g |

### BOD/COD
- $BOD_5 = L_0(1-e^{-5k})$
- BOD/COD > 0.5 = biodegradable

---

## 🌊 Flood Control

### Design Floods
| Structure | Return Period |
|-----------|--------------|
| Small culverts | 25–50 yr |
| Major bridges | 100 yr |
| High-hazard dams | PMF |

### Routing Methods
| Method | Application | Equation |
|--------|-------------|----------|
| Muskingum | Channel reach | $O_2 = C_0I_2 + C_1I_1 + C_2O_1$ |
| Level-pool | Reservoir | $2S/\Delta t + O = 2I + (2S/\Delta t - O)_{prev}$ |
| Kinematic wave | Steep channels | $Q = \alpha A^m$ |

### SCS-CN
$$Q = \frac{(P-0.2S)^2}{P+0.8S}, \quad S = \frac{25400}{CN} - 254$$

---

## ⚡ Aptitude Shortcuts (Top 10)

| # | Trick | Formula |
|---|-------|---------|
| 1 | Successive % | $a + b + ab/100$ |
| 2 | Product stability | $-x/(1+x/100)$ |
| 3 | Average speed | $2V_1V_2/(V_1+V_2)$ |
| 4 | Train crossing | $(L_1+L_2)/(V_1+V_2)$ |
| 5 | LCM work | $ab/(a+b)$ |
| 6 | Alligation | $(d-m):(m-c)$ |
| 7 | Successive discount | $d_1+d_2-d_1d_2/100$ |
| 8 | Rule of 72 | $72/r$ (doubling time) |
| 9 | CI-SI (2yr) | $SI \times r/100$ |
| 10 | Square near 50 | $2500 \pm 100x + x^2$ |

---

## 🎤 Behavioral STAR Framework

**STAR = Situation → Task → Action → Result**

### 30 STAR Categories
1. **Leadership** (4): Project lead, mentoring, influence without authority, initiative
2. **Problem-Solving** (4): Complex technical, incomplete info, creative, prevention
3. **Adaptability** (4): Change, persistence, competing priorities, quick learning
4. **Communication** (3): Complex explanation, difficult feedback, prevention
5. **Integrity** (2): Ethical decision, challenge status quo
6. **Project-Specific** (3): CFD achievement, bridge scour, OpenFOAM template
7. **Teamwork** (2): Cross-functional, supporting teammate
8. **Additional** (8): Time mgmt, conflict resolution, initiative, pressure, research, QA, self-improvement, knowledge sharing

### Key Questions
| Question | Framework |
|----------|-----------|
| Tell me about yourself | Present-Past-Future |
| Why this company? | Research + Connect |
| Why civil → analytics? | Transferable skills |
| Failure | Failure → Learning → Growth |
| Conflict | Listen → Collaborate → Resolve |
| Difficult decision | Analyze → Decide → Execute |

---

## 📚 Key References

| Topic | Source |
|-------|--------|
| Fluid Mechanics | Munson, White, Fox |
| Open Channel Flow | Chaudhry, Henderson |
| Hydrology | Chow, Viessman, Subramanya |
| Groundwater | Freeze & Cherry, Todd |
| Sediment Transport | Van Rijn, Julien |
| Turbulence | Pope, Wilcox |
| OpenFOAM | User Guide, OpenFOAM Wiki |
| Structures | IS 456, IS 800, Pillai & Menon |
| Geotech | Terzaghi & Peck, Das |
| Irrigation | Michael, Garg |
| Water Supply | CPHEEO Manual, Hammer |
| Wastewater | Metcalf & Eddy, CPHEEO |

---

## 🎯 Final Week Strategy

| Day | Focus |
|-----|-------|
| Mon | Fluid Mechanics + Hydraulics formulas |
| Tue | Open Channel Flow + Hydrology |
| Wed | Sediment + Turbulence/CFD |
| Thu | Structures + Geotech (breadth) |
| Fri | Irrigation + Water Resources |
| Sat | Water Supply + Wastewater + Flood |
| Sun | Aptitude shortcuts + Behavioral STAR |

**Daily:** 20 aptitude problems, 5 flashcards, 1 STAR story aloud

---

> **Last Updated:** 2026-09-03
> **Version:** 2.0 — Complete Consolidated Cheat Sheet
> **Maintained by:** DKS IITK Civil/HWRE Placement 2026