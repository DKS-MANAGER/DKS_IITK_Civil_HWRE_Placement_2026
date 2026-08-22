# GATE Civil Engineering — Topic-Wise Revision Notes

> Concise, topic-wise revision summaries for GATE Civil 2027. Each topic lists key concepts, essential formulas, and typical question pointers, paraphrased from the free GATE Civil study material and the IITK Civil/HWRE placement repository.

---

## 1. Engineering Mathematics

### 1.1 Linear Algebra
- **Matrices**: symmetric, skew-symmetric, orthogonal; rank, inverse; eigenvalues/eigenvectors; Cayley-Hamilton theorem ($\mathbf{p(A)=0}$ for $p(\lambda)=\det(\lambda I-A)$); diagonalisation.
- **Systems**: Consistency condition $\rho(A) = \rho(A|B)$.
- **Key formulas**: $A\mathbf{v}=\lambda \mathbf{v}$; $|\det A| = \prod \lambda_i$; $\text{tr}(A) = \sum \lambda_i$.
- **Typical questions**: rank of $3\times3$ matrix, eigenvalues of $2\times2$ matrix, solution of simultaneous linear equations.

### 1.2 Calculus
- **Single variable**: limits, continuity, differentiability, mean value theorem, maxima/minima.
- **Multivariable**: partial derivatives, total derivative, chain rule, gradient $\nabla f$, divergence $\nabla\cdot\vec{v}$, curl $\nabla\times\vec{v}$.
- **Integrals**: double/triple integrals; Green's, Stokes', Gauss' theorems ($\int\!\!\int_S \nabla\cdot\vec{F}\,dS = \int\!\!\int\!\!\int_V \nabla\cdot\vec{F}\,dV$).
- **Common derivatives**: $\frac{d}{dx}(x^n)=nx^{n-1}$; $\frac{d}{dx}\ln x = 1/x$.

### 1.3 Ordinary Differential Equations
- **First order**: separable, linear $\left(\frac{dy}{dx}+Py=Q\right)$ with integrating factor $e^{\int P\,dx}$, exact, Bernoulli.
- **Higher order**: homogeneous with constant coefficients; complementary function + particular integral (variation of parameters).
- **Applications**: spring-mass-dashpot ($m\ddot x + c\dot x + kx = F$), RC/RL circuits.
- **Key**: Auxiliary equation roots → under/critically/over damped behaviour in mechanical vibrations.

### 1.4 Partial Differential Equations
- **Classification**:
  - Elliptic: $\frac{A\,G_{xx}+2B\,G_{xy}+C\,G_{yy}=0}$, $B^2-AC<0$ (e.g. Laplace: $\nabla^2 u=0$).
  - Parabolic: $B^2-AC=0$ (heat/diffusion: $\frac{\partial u}{\partial t}=\alpha\nabla^2 u$).
  - Hyperbolic: $B^2-AC>0$ (wave: $\frac{\partial^2 u}{\partial t^2}=c^2\nabla^2 u$).
- **Methods**: separation of variables, boundary value problems.

### 1.5 Probability & Statistics
- **Distributions**: Normal $\mathcal{N}(\mu,\sigma^2)$ with PDF $f(x)=\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}$; Binomial, Poisson, Exponential, Uniform.
- **Theorems**: Central Limit Theorem; Law of Large Numbers.
- **Bayes' theorem**: $P(A|B)=\frac{P(B|A)P(A)}{P(B)}$.
- **Measures**: $E[X]=\sum xP(x)$; $\text{Var}(X)=E[X^2]-(E[X])^2$.
- **Hypothesis testing**: Type I/II errors, p-value, significance level.

### 1.6 Numerical Methods
- **Root finding**: Bisection; **Newton–Raphson**: $x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}$.
- **Linear systems**: Gauss elimination (forward elimination + back substitution); Gauss-Seidel iteration.
- **Interpolation**: Lagrange; Newton forward/backward difference.
- **Integration**: **Trapezoidal**: $\frac{h}{2}[f_0+2(f_1+\cdots+f_{n-1})+f_n]$; **Simpson's 1/3**: $\frac{h}{3}[f_0+4f_1+2f_2+\cdots]$.
- **ODE**: Euler; **Runge–Kutta 4th order** (most common in GATE).

---

## 2. Engineering Mechanics

### 2.1 Statics
- **Equilibrium**: $\sum F_x=0,\ \sum F_y=0,\ \sum M=0$.
- **Trusses**: Method of joints; method of sections.
- **Friction**: Limiting friction $F=\mu N$; cone of friction; wedges, screw threads.
- **Centroids & centres of mass** (composite bodies).

### 2.2 Dynamics
- **Kinematics**: Rectilinear/curvilinear; relative motion; projectile motion.
- **Kinetics**: Newton's second law $\sum F = ma$; work-energy theorem ($W=\Delta KE$); impulse-momentum ($\sum F \Delta t = \Delta p$).
- **Vibrations**: Free vibration $x=A\cos\omega_n t + B\sin\omega_n t$; natural frequency $\omega_n=\sqrt{k/m}$; damping ratio $\zeta$; critical damping $\zeta=1$.

### 2.3 Virtual Work
- Principle: $\delta W = 0$ for equilibrium; applied to beams, frames, and mechanisms.

---

## 3. Fluid Mechanics

### 3.1 Fluid Properties
- Density $\rho$, specific weight $\gamma=\rho g$, specific gravity, viscosity $\mu$ (Newtons law of viscosity $\tau=\mu\frac{du}{dy}$), surface tension, capillarity.

### 3.2 Fluid Statics
- Hydrostatic pressure $p=\gamma h$; centre of pressure; buoyancy $F_B = \rho g V_{displaced}$; stability: metacentre $M$, $GM = \frac{I_{xx}}{V} - CG$ (stable if $GM>0$).

### 3.3 Kinematics & Dynamics
- **Bernoulli** (along streamline): $\frac{p}{\gamma}+\frac{v^2}{2g}+z=\text{const}$; assumptions: inviscid, incompressible, steady, along streamline.
- **Continuity**: $A_1v_1=A_2v_2$ (steady, incompressible).
- **Momentum**: $\sum F_x = \rho Q(v_2\cos\theta_2 - v_1\cos\theta_1)$.
- **Energy equation** with head loss $h_L$.

### 3.4 Dimensional Analysis
- Buckingham π theorem → dimensionless groups: **Reynolds** $Re=\frac{\rho v L}{\mu}$, **Froude** $Fr=\frac{v}{\sqrt{gL}}$, **Weber** $We=\frac{\rho v^2 L}{\sigma}$, **Euler** $Eu=\frac{p}{\rho v^2}$, **Mach** $Ma=\frac{v}{c}$.
- Model analysis, scale ratios.

### 3.5 Viscous & Turbulent Flow
- **Laminar** (pipe): parabolic profile, $Hagen$–$Poiseuille$ $\Delta p = \frac{32\mu L v}{\rho g D^2}$; $Re < 2000$.
- **Turbulent**: Prandtl mixing length; logarithmic profile.
- **Head loss**: **Darcy–Weisbach** $h_f = f\frac{L}{D}\frac{v^2}{2g}$; **Hazen–Williams** $h_f=10.67 L Q^{1.85}/(C^{1.85} D^{4.87})$; **Manning** $v=\frac{1}{n}R^{2/3}S^{1/2}$.
- **Boundary layer**: $\delta$, displacement & momentum thickness; $Re_x = \frac{\rho vx}{\mu}$; transition at $Re_x \approx 5\times10^5$.

### 3.6 Flow Measurement & Pumps
- **Venturi/Orifice meter**: $Q=C_d A_1 A_2\sqrt{2g\Delta h}/\sqrt{A_1^2-A_2^2}$.
- **Weirs**: rectangular $Q=1.84(L-0.2H)H^{3/2}$.
- **Pumps**: System curve + pump curve; BEP; $NPSH_{req}$, $NPSH_{avail}$.
- **Turbines**: Specific speed $N_s=N\sqrt{P}/H^{5/4}$; Pelton (impulse), Francis & Kaplan (reaction).

---

## 4. Geotechnical Engineering

### 4.1 Soil Classification & Index Properties
- IS classification: coarse-grained (GW/GP/GM/GC by sieve analysis); fine-grained (CL/CH via plasticity chart: $I_p = 0.73(w_L-20)$ A-line).
- Index properties: moisture content $w$, specific gravity $G_s$, Atterberg limits ($LL$, $PL$, $PI=LL-PL$, $IL$).
- Clay minerals: kaolinite (flocculated, low shrink-swell), montmorillonite (dispersed, high shrink-swell), illite.

### 4.2 Permeability & Seepage
- **Darcy's law**: $q = kiA$; $k = \frac{C D^2 \gamma_w}{\mu}$.
- **Flow nets**: Laplace equation $\frac{\partial^2 h}{\partial x^2}+\frac{\partial^2 h}{\partial z^2}=0$; $Q = k_f \cdot N_f \cdot \frac{b}{N_d}$.
- Effective stress principle: $\sigma' = \sigma - u$.

### 4.3 Compaction & Consolidation
- **Compaction**: OMC & MDD; Proctor test (standard/impact).
- **Terzaghi 1D consolidation**: $C_v = \frac{k(1+e_0)}{a_v\gamma_w}$; time factor $T_v=\frac{C_v t}{\bar{H}^2}$; $T_v = \frac{\pi}{4}U^2$ (for $U<60\%$), $T_v=1.781(\ln(100/U)-0.999\times10^{-3})$ for higher.
- **Settlement**: $S_c = \frac{C_c}{1+e_0}H\log_{10}\frac{\sigma'_f}{\sigma'_i}$; immediate & secondary compression.

### 4.4 Shear Strength
- **Mohr–Coulomb**: $\tau = c + \sigma'\tan\phi$.
- **Triaxial tests**: CU, UU, CD; effective vs total stress parameters.
- $\sigma_1=\sigma_3 N_\phi + 2c\sqrt{N_\phi}$, where $N_\phi=\tan^2(45+\phi/2)$.

### 4.5 Earth Pressure & Stability
- **Rankine active/passive**: $K_a = \tan^2(45-\phi/2)$; $K_p=\tan^2(45+\phi/2)$.
- **Coulomb**: incl. wall friction, surcharge, inclined backfill.
- **Slope stability**: Swedish circle (ordinary), **Bishop's simplified** method, Janbu's method; critical slip surface.

### 4.6 Foundation Engineering
- **Bearing capacity**: Terzaghi ($q_{ult}=cN_c+qN_q+0.5\gamma BN_\gamma$); Meyerhof; HAS.
- **Settlement**: immediate, primary consolidation, secondary.
- **Footing design**: isolated, combined, strap, raft; punching shear $\tau = Q/(4(b_1+b_2)\bar{d}$.

---

## 5. Structural Analysis

### 5.1 Statically Determinate Structures
- **Static determinacy**: beam $m+r=2j$; truss $m+r=2j$.
- **Diagrams**: Shear Force (SF) & Bending Moment (BM); relationship $dV/dx=-w$, $dM/dx=V$.

### 5.2 Statically Indeterminate
- **Force method**: flexibility matrix, consistent deformation.
- **Displacement method**: slope-deflection, **moment distribution** (Hardy Cross).
- **Influence lines** (Müller-Breslau principle).

### 5.3 Matrix/Computer Methods
- Member stiffness matrix; transformation; assembly; boundary conditions; static & kinematic indeterminacy ($D_k = 3m_r - r$; $D_s = m + r - 3j + r_r$).

### 5.4 Deflection
- **Double integration**: $EI\frac{d^2y}{dx^2}=M$; **moment-area**: $\theta_{AB}=\frac{1}{EI}\int M\,dx$.
- **Conjugate beam method**; **Castigliano's** / unit-load method ($\Delta = \int \frac{Mm}{EI}dx$); **Macaulay's** notation.

---

## 6. Reinforced Concrete (RCC)

- **Limit state**: $\gamma_{m0}=1.5$ (dead), $\gamma_{m0}=1.5$ (live), load factors 1.5.
- **Singly reinforced**: $x_u = \frac{0.87f_y A_{st}}{0.36f_{ck}b}$; $M_u=0.87f_yA_{st}(d-0.42x_u)$.
- **Limiting depth**: Fe 415 → $x_{u,max}=0.48d$; Fe 500 → $x_{u,max}=0.45d$.
- **Shear**: $\tau_v = V/(bd)$; $\tau_c$ from IS code tables; stirrups $V_{us}=0.87f_y A_{sv} j_d/s$.
- **Development length**: $L_d = \frac{\phi\sigma_s}{4\tau_{bd}}$ (anchorage = 8–12 $\phi$ hooks for stirrups).
- **Slabs**: one-way if $l_y/l_x \le 2$.
- **Columns**: minimum eccentricity $e_{min}=0.005D$ or 20 mm (whichever larger); interaction diagrams for biaxial bending.
- **Footing**: combine with steel/concrete design per IS 456.

---

## 7. Steel Structures

- **Connections**: riveted, **welded** (fillet $\rightarrow$ throat $=0.7\times$size; groove); **bolted** (bearing-type vs friction-grip).
- **Tension members**: net area $A_{net}=A_g - n\phi^2/4$ (n = number of bolts); shear lag factor $\alpha$.
- **Compression members**: $\lambda = l/r$ (radius of gyration $r=\sqrt{I/A}$); $P_{uz}=0.6f_u A_g$ (IS 800); lacing/battening.
- **Beams**: plastic moment $M_p=\phi_y Z_p$; shape factor $S=M_p/M_y$ (1.12–1.18 for rectangle).
- **Gantry girders**: dynamic factor for trolley/loads; combined stresses.

---

## 8. Structural Dynamics & Earthquake Engineering
- **SDOF**: $m\ddot x + c\dot x + kx = F(t)$; $\omega_n=\sqrt{k/m}$; $\zeta = c/(2\sqrt{km})$.
- **Response spectrum**: IS 1893 elastic spectrum; **SRSS & CQC** modal combination.
- **Seismic coefficient**: $V_B = \frac{Z}{2}\frac{I}{R}W$ (or $\alpha W$).

---

## 9. Geotechnical / Water Resources (Civil Depth)
- **Water resources planning**: mass diagram, reservoir capacity–yield relation; **Muskingum** flood routing: $O_{t+\Delta t}=C_0 I_{t+\Delta t}+C_1 I_t+C_2 O_t$.

---

## 10. Transportation Engineering

### 10.1 Highway Geometric Design
- **Sight distances**: SSD $= 0.278 V t_R + V^2/(254f)$; OSD; ISD.
- **Superelevation**: $e+f=V^2/(127R)$; minimum $R=V^2/(1125(f+C)$.
- **Vertical curves**: summit — $L=AI^2/(2a\times100)$; valley — $L=2y_m/(aC)$.
- **Transition curves**: spiral; $\Delta E$ and shift.

### 10.2 Pavement Design
- **Flexible**: **Boussinesq/Glassius** (2D); **Burmister** (3D); CBR method, Westergaard.
- **Rigid**: Westergaard; load equations; joint spacing; **critical load position**.

### 10.3 Traffic Engineering
- **Speed–density**: $q=kv$; shockwave $w=(q_2-q_1)/(k_2-k_1)$.
- **Signal design**: **Webster**: $C = \frac{1.5L}{1-Y}$ where $Y=\sum q_i/s_i$.
- **Highway capacity** (HCS), PCU values.

---

## 11. Railways & Airport Engineering
- **Railways**: gauge types; superelevation $e=G\tan\theta$; cant deficiency; grain flow.
- **Airports**: runway orientation (wind rose), basic runway length, thrust–length–gradient relation, gate capacity.

---

## 12. Environmental Engineering

### 12.1 Water Supply
- **Demand**: per capita consumption, peak factor ($1.5$ for daily max).
- **Population forecast**: arithmetic, geometric, incremental.
- **Intake, treatment train**: screening → grit → coagulation/flocculation → sedimentation → filtration → disinfection.
- **Coagulation**: alum dose; jar test.
- **Filtration**: rapid sand $q \approx 5–7.5$ m³/m²/day; backwash.

### 12.2 Sewerage / Stormwater
- **DWF**: $Q = \frac{5}{3}qiP$ (per capita, $i$=inflow).
- **Rational method**: $Q=CAi$ (storm).
- **Sewer appurtenances**: manholes, inverted siphon, catchbasin, flushing.

### 12.3 Wastewater Treatment
- **Activated sludge**: MLSS, MLVSS, sludge volume index $SVI=X/(V_{os}\cdot 1000)$; $F/M = \frac{QS_0}{XV}$.
- **BOD**: $L_t = L_0 e^{-kt}$; UASB, anaerobic digestion; biogas %CH₄.
- **Trickling filter**: recirculation ratio; removal %.
- **Oxidation pond**: HRT 5–10 days, depth 3–5 m.
- **Solid waste**: collection system design, MSW composition, landfill.

---

## 13. Surveying & Geomatics
- **Traversing**: $\Sigma L=0$, $\Sigma D=0$; Bowditch/Egyptian method for corrections.
- **Tacheometry**: stadia formula $D=ks+C$; anallactic ($k=100$, $C=0$).
- **Curves**: simple circular curve ($L_c = R\Delta$, $T=R\tan(\Delta/2)$); transition curve length $L=V^3/(4RC)$.
- **GNSS/ GPS**: positioning, DGPS corrections.
- **Photogrammetry**: parallax, scale; map projection basics.

---

## 14. Construction Management & Engineering Economy
- **CPM/PERT**: critical path (longest path); float (TF, FF, TF); **crashing**: minimum cost.
- **PERT**: $\beta = (\beta' - \beta)/\sigma$ activity variance; project variance.
- **EVA** (Earned value): PV, EV, AC; $CV=EV-AC$, $SV=EV-PV$, $CPI=EV/AC$, $SPI=EV/PV$.
- **Engineering economics**: Present worth $PW=F(P/F,i,n)$; Annual worth; $IRR = 0$; $Payback$ period.

---

## 15. Engineering Geology (if applicable to paper)
- **Minerals & rocks**: Igneous, Sedimentary, Metamorphic; structural features, unconformity.
- **Geohazards**: landslides, earthquakes; site investigation (SPT N-value, SCPT).

---

## Quick Memory Aids
- **Euler's formula** (column): $P_{cr}=\frac{\pi^2 EI}{(KL)^2}$.
- **Lacey's silt theory**: $f = 1.376\, s^{5/2}/\sqrt{3072}$ (silt factor relation), optimal depth & pitch.
- **Thiele's method**, **Lacey vs Kennedy** scour in HWRE.

---

## References

* [GATE_Civil_Study_Material_2027](https://github.com/DKS-MANAGER/GATE_Civil_Study_Material_2027) — GATE Civil syllabus topics, recommended books, papers, channels
* [Civil_Placement_IITK](https://github.com/DKS-MANAGER/Civil_Placement_IITK) — Core civil/HWRE concepts and company-relevant topics
* [gate-civil-notes](gate/civil/gate-civil-notes.md) — Topic detail
* [gate-civil-formulas](gate/formulas/gate-civil-formulas.md) — Key formulas
