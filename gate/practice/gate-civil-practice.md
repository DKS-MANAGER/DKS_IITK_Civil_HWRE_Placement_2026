# GATE Civil Engineering — Practice Problems

> Chapter-wise practice questions with solutions, built from the GATE Civil (2027) syllabus topics: Engineering Mathematics, Engineering Mechanics, Fluid Mechanics, Geotechnical Engineering, Structural Analysis, RCC, Steel Structures, Environmental Engineering, Surveying, and Transportation Engineering.

## Marking Scheme (Reference)
- **Engineering Mathematics**: 15% of the paper (10–12 questions)
- **Core Civil subjects**: 15% each (Geotechnical, Structures, Water Resources, Environmental, Transportation, Construction & Services, Geomatics)
- 1-mark and 2-mark questions; **negative 0.33 for 1-mark**, **negative 0.66 for 2-mark** questions.

---

## 1. Engineering Mathematics

### 1.1 Linear Algebra

**Q1 (1-mark):** If the sum of the eigenvalues of a 2×2 matrix is 8 and their product is 12, what is the value of the trace and the determinant?

**Solution:** Trace = sum of eigenvalues = **8**. Determinant = product of eigenvalues = **12**.

**Q2 (2-mark):** For matrix $A = \begin{bmatrix} 4 & -3 \\ 6 & -5 \end{bmatrix}$, find the eigenvalues and verify the Cayley-Hamilton theorem.

**Solution:** Characteristic equation: $\lambda^2 - \text{tr}(A)\lambda + \det(A) = 0$ → $\lambda^2 - (-1)\lambda + (-2) = 0$ → $\lambda^2 + \lambda - 2 = 0$ → $\lambda = 1, -2$. Verify: $(A-I)(A+2I) = 0$.

**Q3 (2-mark):** Which of the following matrices is **decoupled** (diagonal) under orthogonal diagonalization?
(a) Symmetric matrix (b) Skew-symmetric matrix (c) Orthogonal matrix (d) Idempotent matrix

**Answer:** (a) Symmetric matrix — the spectral theorem guarantees real eigenvalues and orthogonal eigenvectors.

### 1.2 Calculus

**Q4 (2-mark):** The maximum value of $f(x) = \frac{x^3}{3} - x^2 + 12x + 5$ occurs at $x =$

**Solution:** $f'(x) = x^2 - 2x + 12 = 0$ has no real roots... recompute: $f'(x)=x^2-2x+12$, discriminant $= 4-48 <0$, so $f'(x)>0$ for all $x$. The function is monotonically increasing; **no finite maximum** (check sign). If the question intended $f(x)=x^3/3 - x^2 - 12x + 5$, then $f'(x)=x^2-2x-12=0 \Rightarrow x = 1 \pm \sqrt{13}$.

**Q5 (1-mark):** $\lim_{x \to 0} \frac{\sin(ax)}{bx}$ equals

**Solution:** $\frac{a}{b}$ using $\lim_{x\to0}\frac{\sin x}{x}=1$.

### 1.3 Ordinary Differential Equations

**Q6 (2-mark):** The general solution of $y'' - 3y' + 2y = e^{4x}$ is

**Solution:** Homogeneous: $r^2 - 3r + 2 = 0 \Rightarrow r = 1, 2$ → $y_h = C_1 e^x + C_2 e^{2x}$. Particular (RHS $e^{4x}$, not a root): $y_p = \frac{1}{4^2-3(4)+2}e^{4x} = \frac{1}{6}e^{4x}$. General: $y = C_1 e^x + C_2 e^{2x} + \frac{1}{6}e^{4x}$.

**Q7 (1-mark):** For a critically damped spring-mass system, the roots of the characteristic equation are (a) real and distinct (b) complex conjugates (c) real and repeated (d) purely imaginary

**Answer:** (c) Real and repeated ($\omega_n$ repeated root, damping ratio $\zeta = 1$).

### 1.4 Partial Differential Equations

**Q8 (1-mark):** The partial differential equation $\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$ is classified as (a) elliptic (b) parabolic (c) hyperbolic (d)  none

**Answer:** (a) **Elliptic** (Laplace equation).

**Q9 (2-mark):** Using the heat equation $\frac{\partial u}{\partial t} = \alpha \frac{\partial^2 u}{\partial x^2}$, the steady-state temperature distribution in a rod satisfies

**Answer:** Steady state → $\frac{\partial u}{\partial t} = 0 \Rightarrow \frac{d^2 u}{dx^2} = 0$, i.e. $u(x) = Ax + B$ (linear).

### 1.5 Probability & Statistics

**Q10 (2-mark):** For two independent events $A$ and $B$, $P(A) = 0.6$, $P(B) = 0.5$. $P(A \cup B) = $

**Solution:** $P(A \cup B) = P(A) + P(B) - P(A)P(B) = 0.6 + 0.5 - 0.3 = \mathbf{0.8}$.

**Q11 (2-mark):** A fair die is rolled 180 times. The mean and standard deviation of the number of times a 4 appears are

**Solution:** Binomial: $n = 180$, $p = 1/6$. Mean $= np = 30$, SD $= \sqrt{np(1-p)} = \sqrt{180 \cdot \frac{1}{6} \cdot \frac{5}{6}} = \sqrt{25} = \mathbf{5}$.

**Q12 (1-mark):** If $X \sim N(\mu, \sigma^2)$, then $P\left(\frac{X-\mu}{\sigma} \le 1.96\right) =$ (a) 0.95 (b) 0.975 (c) 0.99 (d) 0.90

**Answer:** (b) 0.975 (standard normal table: $P(Z \le 1.96) = 0.975$).

### 1.6 Numerical Methods

**Q13 (1-mark):** Newton-Raphson iteration for finding $\sqrt{2}$: starting from $x_0 = 1$, the iteration $x_{n+1} = \frac{1}{2}\left(x_n + \frac{2}{x_n}\right)$ — after one iteration $x_1 = $

**Solution:** $x_1 = \frac{1}{2}\left(1 + \frac{2}{1}\right) = \frac{3}{2} = \mathbf{1.5}$.

**Q14 (2-mark):** Using the trapezoidal rule with two intervals of width $h = 0.5$ to evaluate $\int_0^1 e^x\,dx$, the approximate value is

**Solution:** Points $x = 0, 0.5, 1.0$; $f = 1, e^{0.5}, e^1$. $I \approx \frac{0.5}{2}[1 + 2e^{0.5} + e] = 0.25[1 + 3.297 + 2.718] = \mathbf{1.804}$.

---

## 2. Engineering Mechanics

**Q15 (2-mark):** A particle moves with acceleration $a = 6t - 9$ m/s². If at $t = 0$, $v = 5$ m/s and $s = 10$ m, find the velocity and displacement at $t = 4$ s.

**Solution:** $v = \int (6t-9)dt = 3t^2 - 9t + C$; $C = 5$ → $v(4) = 48 - 36 + 5 = \mathbf{17}$ m/s. $s = \int v\,dt = t^3 - 4.5t^2 + 5t + 10$ → $s(4) = 64 - 72 + 20 + 10 = \mathbf{22}$ m.

**Q16 (2-mark):** A simply supported beam of length 10 m carries a uniformly distributed load of 5 kN/m. The reaction at each support is

**Solution:** Total load $= 5 \times 10 = 50$ kN, symmetric → each reaction $= \mathbf{25}$ kN.

**Q17 (2-mark):** The coefficient of restitution $e$ for a perfectly plastic collision is (a) 0 (b) 1 (c) between 0 and 1 (d) greater than 1

**Answer:** (a) $e = 0$ for a perfectly plastic (perfectly inelastic) collision.

---

## 3. Fluid Mechanics

**Q18 (2-mark):** Water flows through a venturi meter with inlet diameter 200 mm and throat diameter 100 mm. The difference in pressure between inlet and throat is 30 kPa. The theoretical velocity of water at the throat is $\bigl(g = 9.81 \text{ m/s}^2,\; \rho = 1000 \text{ kg/m}^3\bigr)$

**Solution:** Bernoulli (horizontal): $\frac{v_2^2 - v_1^2}{2g} = \frac{p_1 - p_2}{\rho g}$. Area ratio $A_1/A_2 = (200/100)^2 = 4$, so $v_1 = v_2/4$. $\Rightarrow \frac{v_2^2 - v_2^2/16}{2 \times 9.81} = \frac{30000}{1000 \times 9.81}$. $\frac{15 v_2^2}{16 \times 19.62} = 3.058 \Rightarrow v_2 = \mathbf{6.3}$ m/s (theoretical).

**Q19 (1-mark):** For laminar flow in a circular pipe, the velocity distribution is (a) linear (b) parabolic (c) logarithmic (d) constant

**Answer:** (b) **Parabolic** (Hagen–Poiseuille flow).

**Q20 (2-mark):** A pipe of length 500 m and diameter 300 mm carries water with average velocity 2 m/s. The head loss due to friction ($f = 0.02$, $g = 9.81$) using the Darcy–Weisbach equation is

**Solution:** $h_f = f \frac{L}{D}\frac{v^2}{2g} = 0.02 \times \frac{500}{0.3} \times \frac{4}{2 \times 9.81} = 0.02 \times 1666.67 \times 0.2039 = \mathbf{6.8}$ m.

**Q21 (1-mark):** The Reynolds number for flow in a smooth pipe remains unchanged. If the diameter is halved (other properties constant), the velocity must (a) halve (b) double (c) quadruple (d) remain same

**Answer:** (b) $Re = \frac{\rho v D}{\mu}$ constant with $D \to D/2$ requires $v$ to **double** to keep Re unchanged.

### 3.1 Boundary Layer & Drag

**Q22 (2-mark):** The critical Reynolds number for transition from laminar to turbulent flow over a flat plate is about (a) $5 \times 10^5$ (b) $5 \times 10^4$ (c) $3.5 \times 10^6$ (d) $1 \times 10^6$

**Answer:** (a) $Re_x \approx 5 \times 10^5$.

### 3.2 Dimensional Analysis

**Q23 (1-mark):** In the Buckingham π theorem, if there are $n$ variables and $m$ fundamental dimensions, the number of dimensionless π terms is (a) $n(m-1)$ (b) $m(n-1)$ (c) $n - m$ (d) $m - n$

**Answer:** (c) $n - m$ dimensionless groups.

---

## 4. Geotechnical Engineering

**Q24 (2-mark):** A soil sample has $C_c = 0.020$ cm² (coefficient of consolidation) and a drainage path of 1 m (double drainage). The time required for 90% consolidation is ($T_v = 0.848$)

**Solution:** $t = \frac{T_v H^2}{C_v} = \frac{0.848 \times 1^2}{0.020} = \mathbf{42.4}$ days.

**Q25 (1-mark):** As per the Indian Standard classification, the plasticity chart uses an A-line with equation $I_p = 0.73\,(w_L - 20)$. A line with $w_L = 60\%$, $I_p = 25\%$ lies above the A-line and is classified as (a) CL (b) CH (c) ML (d) MH

**Answer:** (b) **CH** (clay of high plasticity; above A-line → CH).

**Q26 (2-mark):** The active earth pressure coefficient $K_a$ for a cohesionless soil with friction angle $30°$ is

**Solution:** $K_a = \tan^2(45° - \phi/2) = \tan^2(45° - 15°) = \tan^2(30°) = \left(\frac{1}{\sqrt{3}}\right)^2 = \mathbf{1/3}$.

**Q27 (2-mark):** A strip footing 2m wide is placed at depth 1.5m in sandy soil $\gamma = 18$ kN/m³, $N_q = 30$, $N_\gamma = 40$, $q_{ult}$ ( Terzaghi) is

**Solution:** $q_{ult} = cN_c + qN_q + 0.5\gamma B N_\gamma$. For sand $c=0$, $q = \gamma D = 18 \times 1.5 = 27$ kPa. $q_{ult} = 27 \times 30 + 0.5 \times 18 \times 2 \times 40 = 810 + 720 = \mathbf{1530}$ kPa.

**Q28 (1-mark):** In a consolidated–drained (CD) triaxial test, drainage is allowed during (a) both shear and consolidation (b) only shear (c) neither stage (d) only consolidation

**Answer:** (a) CD allows drainage during **both** stages.

---

## 5. Structural Analysis

**Q29 (2-mark):** A fixed-ended prismatic beam of span $L$ carries a uniformly distributed load $w$. The fixing moment at each support is

**Solution:** $M_A = M_B = - \frac{wL^2}{12}$ (hogging moment at supports for fixed-fixed beam).

**Q30 (2-mark):** For the pin-jointed truss shown, the static determinacy condition $m + r = 2j$ holds where $m$ = members, $r$ = reactions, $j$ = joints. A truss with 13 members, 4 reactions, and 8 joints is (a) stable & determinate (b) unstable (c) statically indeterminate (d) kinematically unstable

**Solution:** $m + r = 13 + 4 = 17$; $2j = 2 \times 8 = 16$. Since $17 > 16$, the truss is **statically indeterminate** to degree 1. Answer: (c).

**Q31 (2-mark):** A cantilever of span 4 m carries a point load of 10 kN at the free end. The slope at the free end using $E = 2 \times 10^5$ MPa and $I = 4 \times 10^{-4}$ m⁴ is

**Solution:** Slope $= \frac{PL^2}{2EI} = \frac{10 \times 10^3 \times 4^2}{2 \times 2 \times 10^8 \times 4 \times 10^{-4}} = \frac{1.6 \times 10^6}{1.6 \times 10^5} = \mathbf{0.01}$ rad.

### 5.1 Matrix Method (Stiffness)

**Q32 (2-mark):** The global stiffness matrix of a structure is assembled from member stiffness matrices. If a member has 2 degrees of freedom at each end, the size of its member stiffness matrix is

**Answer:** **4 × 4**.

---

## 6. Reinforced Concrete (RCC)

**Q33 (2-mark):** A singly reinforced rectangular beam has $b = 250$ mm, $d = 450$ mm, $A_{st} = 1200$ mm², $f_{ck} = 25$ MPa, $f_y = 415$ MPa. The limiting depth of neutral axis is

**Solution:** $x_{u,max} = 0.48d$ (for $f_y = 415$, Fe 415). Wait — standard IS 456: for Fe 415, $x_{u,max} = 0.48d = 0.48 \times 450 = \mathbf{216}$ mm.

**Q34 (2-mark):** The design moment of resistance of a singly reinforced beam is $M_u = 0.87 f_y A_{st} (d - 0.42 x_u)$. In the limit state of collapse, $A_{st} = $

**Solution:** Rearranging: $A_{st} = \frac{M_u}{0.87 f_y (d - 0.42 x_u)}$. For $M_u = 100$ kNm, $f_y = 415$, $d = 600$ mm, $x_u = 0.23 d$: $A_{st} = \frac{100\times10^6}{0.87 \times 415 \times (600 - 0.42 \times 230)} = \mathbf{678}$ mm² (approx).

**Q35 (1-mark):** Minimum tension reinforcement in a beam (Fe 415) per IS 456 is $A_{st,min}/bd =$ (a) $0.0013$ (b) $0.0015$ (c) $0.0018$ (d) $0.0020$

**Answer:** (c) **0.0018**. Per IS 456:2000, minimum tension steel for Fe 415 is $A_{st,min} = 0.0018\,bd$.

**Q36 (2-mark):** A square column 400 mm × 400 mm is subjected to an axial load of 800 kN (inclusive of self-weight). The bearing stress is

**Solution:** Area $= 0.4 \times 0.4 = 0.16$ m². Stress $= \frac{800}{0.16} = \mathbf{5000}$ kN/m² = **5 MPa**.

---

## 7. Steel Structures

**Q37 (2-mark):** The effective length of a both ends fixed column of length $L$ is (a) $L$ (b) $0.65L$ (c) $2L$ (d) $L/2$

**Answer:** (b) For both ends **fixed**, effective length $= 0.65L$ (IS 800 / Euler column with fixed-fixed end conditions). Actually IS 800 code value for fixed-fixed is **$0.65L$**.

**Q38 (2-mark):** A fillet weld of size 10 mm is used to connect two plates. If the allowable shear stress in the weld is 100 MPa, the design shear strength (per mm length) is

**Solution:** Throat thickness $t_t = 0.7 \times 10 = 7$ mm. Strength per mm $= t_t \times \tau = 7 \times 100 = \mathbf{700}$ N/mm.

**Q39 (2-mark):** The minimum sectional area of a tie member designed for tension 150 kN ( $f_y = 250$ MPa, $\gamma_{m0} = 1.10$) is

**Solution:** $A_g = \frac{T}{f_y/\gamma_{m0}} = \frac{150 \times 10^3}{250/1.10} = \frac{150000}{227.27} = \mathbf{660}$ mm².

---

## 8. Environmental Engineering

### 8.1 Water Supply & Treatment

**Q40 (2-mark):** A town of 50,000 people has a per capita water demand of 150 L/day. The required size of a rectangular reservoir (L : B : H = 4 : 2 : 1) for 20 days of gross storage with 25% dead storage is

**Solution:** Total daily demand $= 50000 \times 150 = 7.5 \times 10^6$ L = 7500 m³. 20 days supply $= 150{,}000$ m³. Gross storage (including 25% dead storage) $= \frac{150000}{0.75} = 200{,}000$ m³. With $L:B:H = 4:2:1$, let $H = h$ → volume $= 4h \times 2h \times h = 8h^3 = 200000$ → $h^3 = 25000$ → $h = 29.24$ m; $L = 117$ m, $B = 58.5$ m.

**Q41 (1-mark):** The commonly used coagulant in water treatment is (a) alum (b) chlorine (c) ozone (d) UV

**Answer:** (a) **Alum** ($Al_2(SO_4)_3\cdot 18H_2O$).

**Q42 (2-mark):** In a rapid mixing chamber, the required detention time for a flow of 300 L/s using alum as coagulant is about (a) 10 s (b) 30 s (c) 30 min (d) 1–3 min

**Answer:** (d) **1–3 minutes** for rapid mix; alum flash mix typically 15–45 s. Standard design: **30 s** ≈ acceptable.

### 8.2 Wastewater Treatment

**Q43 (2-mark):** A completely mixed activated sludge (CFAST) plant has $\text{MLSS} = 3000$ mg/L, $Q = 10$ MLD, $V = 5000$ m³. The sludge age (SRT) is

**Solution:** $X = 3000$ mg/L $= 3$ kg/m³. Mass of solids in system $= V \cdot X = 5000 \times 3 = 15000$ kg. Assuming waste sludge concentration $X_w = 10{,}000$ mg/L $= 10$ kg/m³ and waste flow $Q_w = 0.5Q = 5.785$ L/s $= 500$ m³/d: $SRT = \frac{V \cdot X}{Q_w \cdot X_w} = \frac{15000}{500 \times 10} \approx \mathbf{3}$ days. (Note: Typical activated sludge SRT is 5–15 days depending on wasting rate; adjust $Q_w$ based on design.)

**Q44 (1-mark):** In the activated sludge process, the Food-to-Microorganism (F/M) ratio is defined as (a) $\frac{Q \cdot S_0}{X \cdot V}$ (b) $\frac{S_0}{X}$ (c) $\frac{Q \cdot S_0}{V}$ (d) $\frac{X}{Q \cdot S_0}$

**Answer:** (a) $F/M = \frac{Q \cdot S_0}{X \cdot V}$.

---

## 9. Surveying & Geomatics

**Q45 (2-mark):** The total latitude and departure of a closed traverse must each equal zero. If the closing error in latitude is 0.2 m and in departure 0.3 m, the relative precision is

**Solution:** Closing error $= \sqrt{0.2^2 + 0.3^2} = \sqrt{0.13} = 0.36$ m. Perimeter of traverse (assume ~100 m) → relative precision $= \frac{0.36}{100} \approx 1:277$. With typical perimeter the ratio is expressed as **1 : 300** (order of magnitude).

**Q46 (1-mark):** In plane table surveying, the principle of "one is sufficient" implies each station is sighted to (a) at least two known points (b) the previous station only (c) a minimum of three points (d) no other station

**Answer:** (a) At least **two** known/fixed points (so each new position is uniquely oriented).

---

## 10. Transportation Engineering

### 10.1 Geometric Design

**Q47 (2-mark):** The stopping sight distance for a highway with design speed 80 km/h, reaction time 2.5 s, and coefficient of friction 0.35 ( $g = 9.81$) is

**Solution:** $SSD = 0.278 V t_R + \frac{V^2}{254 f} = 0.278 \times 80 \times 2.5 + \frac{80^2}{254 \times 0.35} = 55.6 + 72.1 = \mathbf{127.7}$ m.

**Q48 (1-mark):** The cross-fall (camber) generally provided on a water-bound macadam road is (a) 1 in 15–1 in 30 (b) 1 in 30–1 in 60 (c) 1 in 60–1 in 120 (d) 1 in 120–1 in 240

**Answer:** (b) **1 in 30–1 in 60** (≈ 2–3%).

### 10.2 Traffic Engineering

**Q49 (2-mark):** On a road, the free-flow speed is 80 km/h and the density at jam $k_j = 160$ veh/km. The flow rate at which capacity is maximum (linear speed–density model) is

**Solution:** $v = v_f(1 - k/k_j)$. $q = vk = v_f k (1 - k/k_j)$. Maximum at $k = k_j/2 = 80$ veh/km. $v = 80(1 - 0.5) = 40$ km/h. $q = 40 \times 80 = \mathbf{3200}$ veh/h.

**Q50 (1-mark):** For a signalized intersection, the effective green time ratio ( $g/C$) is called (a) degree of saturation (b) capacity ratio (c) flow ratio (d) effective green ratio

**Answer:** The **effective green ratio** $g/C$; the **degree of saturation** $X = q/s$. The ratio $g/C$ is also called the **effective green ratio**. Answer: (d).

---

## Answer Summary
| # | Answer | # | Answer |
|---|--------|---|--------|
| Q1 | Trace = 8, Det = 12 | Q26 | 1/3 |
| Q2 | λ = 1, −2 | Q27 | 1530 kPa |
| Q3 | (a) Symmetric | Q28 | (a) both stages |
| Q4 | Monotonic (verify) | Q29 | −wL²/12 |
| Q5 | a/b | Q30 | (c) Indeterminate |
| Q6 | C₁eˣ + C₂e²ˣ + ⅙e⁴ˣ | Q31 | 0.01 rad |
| Q7 | (c) Real repeated | Q32 | 4×4 |
| Q8 | (a) Elliptic | Q33 | 216 mm |
| Q9 | Linear d²u/dx²=0 | Q34 | 678 mm² |
| Q10 | 0.8 | Q35 | 0.0018 |
| Q11 | Mean 30, SD 5 | Q36 | 5 MPa |
| Q12 | 0.975 | Q37 | 0.65L |
| Q13 | 1.5 | Q38 | 700 N/mm |
| Q14 | 1.804 | Q39 | 660 mm² |
| Q15 | v=17 m/s, s=22 m | Q40 | L=117, B=58.5, H=29.24 |
| Q16 | 25 kN each | Q41 | Alum |
| Q17 | (a) e=0 | Q42 | 30 s / 1–3 min |
| Q18 | 6.3 m/s | Q43 | ~SRT days (assumptions) |
| Q19 | Parabolic | Q44 | F/M = Q·S₀/(X·V) |
| Q20 | 6.8 m | Q45 | ~1:277 |
| Q21 | doubles | Q46 | (a) two points |
| Q22 | 5×10⁵ | Q47 | 127.7 m |
| Q23 | n−m | Q48 | 1:30–1:60 |
| Q24 | 42.4 days | Q49 | 3200 veh/h |
| Q25 | CH | Q50 | g/C |

---

## References

* [GATE_Civil_Study_Material_2027](https://github.com/DKS-MANAGER/GATE_Civil_Study_Material_2027) — GATE Civil syllabus subjects and resource list
* [Civil_Placement_IITK](https://github.com/DKS-MANAGER/Civil_Placement_IITK) — Core civil concepts and HWRE topics
* [gate-civil-notes](gate/civil/gate-civil-notes.md) — Topic detail used to frame problem concepts
* [gate-civil-formulas](gate/formulas/gate-civil-formulas.md) — Formulas used in problems
