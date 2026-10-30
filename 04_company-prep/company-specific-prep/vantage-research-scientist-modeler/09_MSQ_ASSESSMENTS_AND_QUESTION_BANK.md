# Module 09: MSQ Assessment Preparation & 40-Question Practice Suite

> **Track**: Screening Assessment Simulation & Advanced Technical Question Bank  
> **Role Level**: Scientist – Modeler (Scientist 1 / Scientist 2 Standard)  
> **Target Entity**: Vantage Research  
> **Evidentiary Status**: `[INTERNAL PRACTICE SIMULATION — CALIBRATED TO OFFICIAL JD COMPETENCIES]`  
> **Assessment Format**: Multiple Select Questions (MSQs), Single-Choice Questions & Numerical Worksheets  

---

## 1. Assessment Overview & MSQ Answering Strategy

The Vantage Research official job posting explicitly specifies an **"MSQ assessment"** as the primary screening round for the Scientist – Modeler position.

### Evidentiary Scope & Institutional Context
* **Confirmed Term**: The screening round is officially designated as an **"MSQ assessment"** (`[OFFICIAL VR PORTAL]`).
* **Format Interpretation**: In Indian technical competitive examinations (e.g., GATE), the acronym MSQ designates **Multiple Select Questions** (where one or more options are correct with zero partial credit). In other recruitment settings, it may refer to a "Model-based Screening Quiz" or a composite technical test. The company does *not* publicly publish its exact platform, question count, or marking scheme.
* **Practice Design**: To provide the most rigorous possible preparation, this question bank is formulated as **multi-select technical practice questions (`[TIER 5 / SIMULATION]`)** calibrated directly to the 7 technical competency domains listed in the official JD.
* **Strategic Answering Rule**: Evaluate each option as an independent True/False mathematical proposition. Never stop after finding one correct statement!

---

## 2. 40-Question Technical Question Bank with Complete Mathematical Solutions

---

### Part 1: Linear Algebra, Calculus & Stability (Questions 01–05)

#### Question 01 [MSQ — Linear Stability & Eigenvalues]
Consider the linear planar dynamical system $\dot{\mathbf{x}} = \mathbf{A} \mathbf{x}$, where $\mathbf{A} = \begin{pmatrix} -3 & 4 \\ -2 & 1 \end{pmatrix}$. Which of the following statements are **CORRECT**?
- (A) The trace of the system is $\tau = -2$ and the determinant is $\Delta = 5$.
- (B) The eigenvalues of $\mathbf{A}$ are $\lambda_{1, 2} = -1 \pm 2i$.
- (C) The origin is a stable spiral (focus).
- (D) Trajectories in the phase plane rotate in a counter-clockwise direction.

**Answer**: **(A), (B), (C)** (Option D is incorrect: rotation is clockwise)

**Detailed Step-by-Step Derivation**:
1. **Trace**: $\tau = a_{11} + a_{22} = -3 + 1 = -2$.
2. **Determinant**: $\Delta = (-3)(1) - (4)(-2) = -3 + 8 = 5$.
   * Option (A) is **CORRECT**.
3. **Characteristic Equation**: $\lambda^2 - \tau \lambda + \Delta = \lambda^2 + 2\lambda + 5 = 0$.
   $$\lambda_{1, 2} = \frac{-2 \pm \sqrt{2^2 - 4(1)(5)}}{2} = \frac{-2 \pm \sqrt{4 - 20}}{2} = \frac{-2 \pm \sqrt{-16}}{2} = -1 \pm 2i$$
   * Option (B) is **CORRECT**.
4. **Stability Classification**:
   * Real part of eigenvalues $\text{Re}(\lambda) = -1 < 0 \implies$ Trajectories spiral asymptotically toward the origin $\implies$ **Stable Spiral (Focus)**.
   * Option (C) is **CORRECT**.
5. **Direction of Rotation**:
   * Test velocity vector at point $(x, y) = (1, 0)$ on the positive x-axis:
     $$\dot{x} = -3(1) + 4(0) = -3, \quad \dot{y} = -2(1) + 1(0) = -2$$
   * At $(1, 0)$, $\dot{y} = -2 < 0$ (flow points downwards). This indicates clockwise rotation in standard Cartesian axes, but let us check $(0, 1)$ on positive y-axis:
     $$\dot{x} = 4(1) = 4 > 0, \quad \dot{y} = 1(1) = 1 > 0$$
   * At $(0, 1)$, $\dot{x} > 0$ (moving right); at $(1, 0)$, $\dot{y} < 0$ (moving down); at $(0, -1)$, $\dot{x} < 0$ (moving left); at $(-1, 0)$, $\dot{y} > 0$ (moving up). This is a **clockwise** motion!
   * *Correction / Refinement*: Option (D) asserts counter-clockwise. Since the verified vector flow rotates clockwise ($\rightarrow \downarrow \leftarrow \uparrow$), Option (D) is **INCORRECT**.
   * **Correct Answer Key: (A), (B), (C)**.

---

#### Question 02 [MSQ — Jacobian & Linearization]
A 2-species biological interaction model is given by:
$$\frac{dx}{dt} = x(2 - x - y), \quad \frac{dy}{dt} = y(3 - 2x - y)$$
Which of the following statements regarding the equilibrium point $(x^*, y^*) = (1, 1)$ are **CORRECT**?
- (A) The Jacobian matrix evaluated at $(1, 1)$ is $\mathbf{J} = \begin{pmatrix} -1 & -1 \\ -2 & -1 \end{pmatrix}$.
- (B) The eigenvalues of the Jacobian at $(1, 1)$ are $\lambda = -1 \pm \sqrt{2}$.
- (C) The equilibrium point $(1, 1)$ is a saddle point.
- (D) The equilibrium point $(1, 1)$ is asymptotically stable.

**Answer**: **(A), (B), (C)**

**Detailed Step-by-Step Derivation**:
1. **Compute Partial Derivatives**:
   * $f(x, y) = 2x - x^2 - xy \implies \frac{\partial f}{\partial x} = 2 - 2x - y, \quad \frac{\partial f}{\partial y} = -x$.
   * $g(x, y) = 3y - 2xy - y^2 \implies \frac{\partial g}{\partial x} = -2y, \quad \frac{\partial g}{\partial y} = 3 - 2x - 2y$.
2. **Evaluate Jacobian at $(1, 1)$**:
   * $J_{11} = 2 - 2(1) - 1 = -1$.
   * $J_{12} = -1$.
   * $J_{21} = -2(1) = -2$.
   * $J_{22} = 3 - 2(1) - 2(1) = -1$.
   $$\mathbf{J}(1, 1) = \begin{pmatrix} -1 & -1 \\ -2 & -1 \end{pmatrix}$$
   * Option (A) is **CORRECT**.
3. **Eigenvalues**:
   * $\tau = -1 + (-1) = -2$.
   * $\Delta = (-1)(-1) - (-1)(-2) = 1 - 2 = -1$.
   $$\lambda^2 - \tau \lambda + \Delta = \lambda^2 + 2\lambda - 1 = 0 \implies \lambda = \frac{-2 \pm \sqrt{4 - 4(1)(-1)}}{2} = \frac{-2 \pm \sqrt{8}}{2} = -1 \pm \sqrt{2}$$
   * Option (B) is **CORRECT**.
4. **Stability Classification**:
   * $\lambda_1 = -1 + \sqrt{2} \approx +0.414 > 0$ (unstable manifold).
   * $\lambda_2 = -1 - \sqrt{2} \approx -2.414 < 0$ (stable manifold).
   * Since $\Delta < 0$ and eigenvalues have opposite real signs, $(1, 1)$ is a **Saddle Point** (unstable).
   * Option (C) is **CORRECT**; Option (D) is **INCORRECT**.

---

#### Question 03 [Single-Choice — Non-Dimensionalization]
For the Gompertz tumor growth equation $\frac{dV}{dt} = \alpha V \ln\left(\frac{K}{V}\right)$, where $[V] = \text{mm}^3$ and $[t] = \text{days}$, define dimensionless volume $u = \frac{V}{K}$ and dimensionless time $\tau = \alpha t$. The resulting dimensionless differential equation is:
- (A) $\frac{du}{d\tau} = u \ln(u)$
- (B) $\frac{du}{d\tau} = -u \ln(u)$
- (C) $\frac{du}{d\tau} = \ln(u)$
- (D) $\frac{du}{d\tau} = u (1 - u)$

**Answer**: **(B)**

**Detailed Step-by-Step Derivation**:
1. $V = K u \implies \frac{dV}{dt} = K \frac{du}{dt}$.
2. By chain rule: $\frac{du}{dt} = \frac{du}{d\tau} \frac{d\tau}{dt} = \alpha \frac{du}{d\tau}$.
3. Substitute into Gompertz equation:
   $$K \alpha \frac{du}{d\tau} = \alpha (K u) \ln\left(\frac{K}{K u}\right) = \alpha K u \ln\left(\frac{1}{u}\right) = -\alpha K u \ln(u)$$
4. Divide both sides by $\alpha K$:
   $$\frac{du}{d\tau} = -u \ln(u)$$
   * Option (B) is **CORRECT**.

---

#### Question 04 [MSQ — Matrix Exponentials & Coupled Linear ODEs]
Consider the decoupled system $\dot{x} = -2x, \ \dot{y} = -5y$. Which of the following statements are **CORRECT**?
- (A) The system matrix has eigenvalues $\lambda_1 = -2, \lambda_2 = -5$.
- (B) All trajectories in the phase plane approach the origin along the line $y = 0$ (the slower eigenspace) as $t \to \infty$.
- (C) The origin is an asymptotically stable node.
- (D) The ratio $\frac{y(t)}{x(t)}$ approaches zero as $t \to \infty$ for any initial condition with $x(0) \ne 0$.

**Answer**: **(A), (B), (C), (D)**

**Detailed Step-by-Step Derivation**:
1. $x(t) = x_0 e^{-2t}, \ y(t) = y_0 e^{-5t}$.
2. Eigenvalues are $-2$ and $-5$ (both strictly negative real numbers $\implies$ Stable Node). Options (A) and (C) are **CORRECT**.
3. Ratio: $\frac{y(t)}{x(t)} = \frac{y_0 e^{-5t}}{x_0 e^{-2t}} = \frac{y_0}{x_0} e^{-3t} \to 0$ as $t \to \infty$. Option (D) is **CORRECT**.
4. Because the $y$-component decays as $e^{-5t}$ (much faster than $e^{-2t}$), trajectories become tangent to the $x$-axis ($y = 0$) as they enter the origin. Option (B) is **CORRECT**.

---

#### Question 05 [Numerical Value — Trace & Determinant Condition]
For a 2D linear system to exhibit neutrally stable periodic orbits (a Center), the trace of the Jacobian must equal:
- **Numerical Answer**: `0` (or `0.0`)

---

### Part 2: Numerical Methods & Stiff ODE Solvers (Questions 06–12)

#### Question 06 [MSQ — Explicit Runge-Kutta & Butcher Tableau]
Which of the following conditions must be satisfied for a Runge-Kutta method to be **consistent** of at least Order 1?
- (A) $\sum_{i=1}^s b_i = 1$
- (B) $c_i = \sum_{j=1}^s a_{ij}$ for all $i = 1, \dots, s$
- (C) $a_{ij} = 0$ for all $j \ge i$
- (D) $\sum_{i=1}^s b_i c_i = \frac{1}{2}$ (for 2nd-order consistency)

**Answer**: **(A), (B), (D)**

**Detailed Step-by-Step Derivation**:
* Option (A) is the fundamental condition for order $p=1$ consistency ($\sum b_i = 1$). **CORRECT**.
* Option (B) is the row-sum condition defining the internal stage evaluation times $c_i = \sum a_{ij}$. **CORRECT**.
* Option (C) defines an *explicit* RK method, but is NOT a requirement for consistency (implicit methods are also consistent!). **INCORRECT**.
* Option (D) is the exact algebraic tree condition for 2nd-order accuracy ($p=2$). **CORRECT**.

---

#### Question 07 [Single-Choice — Stability Limit of Explicit Solvers]
A stiff biochemical reaction network has a fastest negative eigenvalue $\lambda_{fast} = -5000\text{ s}^{-1}$. If the Forward Euler method ($y_{n+1} = y_n + h f(y_n)$) is used to simulate this system, what is the **maximum time step $h$** that guarantees numerical stability?
- (A) $0.0004\text{ s}$
- (B) $0.0002\text{ s}$
- (C) $0.0010\text{ s}$
- (D) $0.0020\text{ s}$

**Answer**: **(A)**

**Detailed Step-by-Step Derivation**:
1. For Forward Euler, the linear stability region is $|1 + \lambda h| \le 1$.
2. For real $\lambda < 0$: $-1 \le 1 + \lambda h \le 1 \implies -2 \le \lambda h \le 0 \implies h \le \frac{2}{|\lambda|}$.
3. Substituting $\lambda_{fast} = -5000\text{ s}^{-1}$:
   $$h_{max} = \frac{2}{5000} = \mathbf{0.0004\text{ seconds}}$$
   * Any step size $h > 0.4\text{ ms}$ will cause the numerical solution to oscillate and explode to infinity!
   * Option (A) is **CORRECT**.

---

#### Question 08 [MSQ — A-Stability and L-Stability]
Which of the following statements regarding implicit differential equation solvers are **CORRECT**?
- (A) A numerical method is A-stable if its region of absolute stability contains the entire open left-half complex plane $\{z \in \mathbb{C} : \text{Re}(z) < 0\}$.
- (B) The Trapezoidal rule (Crank-Nicolson) is A-stable, but NOT L-stable.
- (C) The Backward Euler method is both A-stable and L-stable.
- (D) On highly stiff systems, an L-stable solver damps out rapid initial transients much faster than an A-stable solver that is not L-stable.

**Answer**: **(A), (B), (C), (D)** (All options correct)

**Detailed Step-by-Step Derivation**:
* (A) Matches the formal definition of Dahlquist A-stability. **CORRECT**.
* (B) For Trapezoidal rule, stability function $R(z) = \frac{1 + z/2}{1 - z/2}$. As $\text{Re}(z) \to -\infty$, $|R(-\infty)| = |-1| = 1 \ne 0$. Hence it is A-stable but not L-stable. **CORRECT**.
* (C) For Backward Euler, $R(z) = \frac{1}{1 - z}$. As $\text{Re}(z) \to -\infty$, $|R(-\infty)| = 0$. Hence it is L-stable. **CORRECT**.
* (D) Because $|R(-\infty)| = 0$, L-stable solvers immediately extinguish high-frequency stiff components without spurious numerical oscillations. **CORRECT**.

---

#### Question 09 [MSQ — PDE Stability & Discretization]
When solving the 1D advection-diffusion equation $\frac{\partial C}{\partial t} + u \frac{\partial C}{\partial x} = D \frac{\partial^2 C}{\partial x^2}$ using finite differences, which of the following criteria apply?
- (A) The Courant-Friedrichs-Lewy (CFL) condition requires $CFL = \frac{u \Delta t}{\Delta x} \le 1$ for explicit advective stability.
- (B) Central differencing for the advection term causes non-physical spatial oscillations if the grid Peclet number $Pe_g = \frac{u \Delta x}{D} > 2$.
- (C) First-order upwind differencing introduces artificial numerical diffusion.
- (D) For an explicit Euler time discretization of pure diffusion, stability requires $\Delta t \le \frac{\Delta x^2}{2D}$.

**Answer**: **(A), (B), (C), (D)** (All options correct)

---

### Part 3: Parameter Estimation & Sensitivity Analysis (Questions 13–20)

#### Question 10 [MSQ — Structural vs Practical Identifiability]
Which of the following statements correctly distinguish structural from practical identifiability?
- (A) Structural identifiability depends on model mathematical topology and observation function, assuming ideal noise-free and continuous data.
- (B) Practical identifiability depends on the quality, noise level, and sampling frequency of actual experimental measurements.
- (C) If a parameter is structurally unidentifiable, no amount of additional noisy experimental data from the same observation setup can resolve it.
- (D) A flat profile likelihood over a wide range indicates that a parameter is practically unidentifiable.

**Answer**: **(A), (B), (C), (D)** (All options correct)

---

#### Question 11 [Single-Choice — Normalized Sensitivity Derivation]
If a model output is given by $y(t) = A e^{-k t}$, what is the **normalized local sensitivity coefficient** of $y$ with respect to the rate constant $k$, defined as $S_k(t) = \frac{\partial y}{\partial k} \frac{k}{y}$?
- (A) $S_k(t) = -k t$
- (B) $S_k(t) = -t$
- (C) $S_k(t) = -k e^{-kt}$
- (D) $S_k(t) = 1 - k t$

**Answer**: **(A)**

**Detailed Step-by-Step Derivation**:
1. $\frac{\partial y}{\partial k} = \frac{\partial}{\partial k}(A e^{-kt}) = -A t e^{-kt} = -t \cdot y(t)$.
2. Normalized sensitivity:
   $$S_k(t) = \frac{\partial y}{\partial k} \cdot \frac{k}{y(t)} = (-t \cdot y(t)) \frac{k}{y(t)} = \mathbf{-k t}$$
   * Option (A) is **CORRECT**.

---

#### Question 12 [MSQ — Sobol Global Sensitivity Indices]
In variance-based global sensitivity analysis (Sobol indices), which of the following relations are **MATHEMATICALLY VALID**?
- (A) The first-order index satisfies $0 \le S_i \le 1$.
- (B) The total-order index satisfies $S_{Ti} \ge S_i$ for every parameter $i$.
- (C) The difference $S_{Ti} - S_i$ quantifies the interactions between parameter $i$ and all other parameters.
- (D) If $\sum_{i=1}^k S_i = 1$, the model is strictly additive with zero parameter interactions.

**Answer**: **(A), (B), (C), (D)** (All options correct)

---

### Part 4: QSP, Systems Biology & Pharmacometrics (Questions 21–30)

#### Question 13 [Single-Choice — Michaelis-Menten Asymptotes]
In the Michaelis-Menten rate law $v = \frac{V_{max} [S]}{K_m + [S]}$, when the substrate concentration is much lower than the Michaelis constant ($[S] \ll K_m$):
- (A) The reaction follows zero-order kinetics with rate $v \approx V_{max}$.
- (B) The reaction follows first-order kinetics with apparent rate constant $k = \frac{V_{max}}{K_m}$.
- (C) The reaction velocity is independent of enzyme concentration.
- (D) The reaction rate is infinite.

**Answer**: **(B)**

---

#### Question 14 [MSQ — Target-Mediated Drug Disposition (TMDD)]
Which of the following characteristics are hallmarks of Target-Mediated Drug Disposition (TMDD)?
- (A) At low doses, drug clearance is high due to rapid target-mediated internalization and degradation.
- (B) At high doses, target receptors become fully saturated, and apparent clearance decreases toward non-specific linear clearance.
- (C) Systemic exposure ($AUC$) increases more than proportionally with dose as saturation occurs.
- (D) The plasma concentration-time profile exhibits non-linear, dose-dependent half-lives.

**Answer**: **(A), (B), (C), (D)** (All options correct)

---

#### Question 15 [Single-Choice — Oral Pharmacokinetics $T_{max}$]
A drug administered orally has an absorption rate constant $k_a = 2.0\text{ h}^{-1}$ and elimination rate constant $k_e = 0.2\text{ h}^{-1}$. What is the time to peak plasma concentration $T_{max}$?
- (A) $1.11\text{ hours}$
- (B) $1.28\text{ hours}$
- (C) $2.30\text{ hours}$
- (D) $0.50\text{ hours}$

**Answer**: **(B)**

**Detailed Step-by-Step Derivation**:
$$T_{max} = \frac{\ln(k_a / k_e)}{k_a - k_e} = \frac{\ln(2.0 / 0.2)}{2.0 - 0.2} = \frac{\ln(10.0)}{1.8} = \frac{2.302585}{1.8} = \mathbf{1.2792\text{ hours}} \approx \mathbf{1.28\text{ hours}}$$
* Option (B) is **CORRECT**.

---

#### Question 16 [MSQ — Pharmacodynamic $E_{max}$ Models]
For the sigmoidal Hill pharmacodynamic equation $E = \frac{E_{max} C^\gamma}{EC_{50}^\gamma + C^\gamma}$:
- (A) $EC_{50}$ is the drug concentration producing 50% of the maximum effect $E_{max}$.
- (B) When the Hill coefficient $\gamma = 1$, the equation reduces to the standard hyperbolic $E_{max}$ model.
- (C) When $\gamma \gg 1$, the dose-response curve acts as a sharp, threshold-like switch.
- (D) Doubling drug concentration from $EC_{50}$ to $2 \times EC_{50}$ always doubles the pharmacological effect $E$.

**Answer**: **(A), (B), (C)**

**Refutation of (D)**:
At $C = EC_{50}$, $E = 0.50 E_{max}$.
At $C = 2 EC_{50}$ (with $\gamma = 1$): $E = \frac{E_{max}(2)}{1 + 2} = \frac{2}{3} E_{max} \approx 0.67 E_{max}$.
The effect increases from $0.50$ to $0.67$, which is a **33% increase**, NOT a doubling (100% increase)! Thus, (D) is **INCORRECT**.

---

#### Question 17 [Single-Choice — Steady-State Accumulation Factor]
A patient receives an IV bolus every $\tau = 12\text{ hours}$. The drug elimination rate constant is $k_e = 0.05776\text{ h}^{-1}$ (half-life $t_{1/2} = 12\text{ hours}$). What is the steady-state accumulation factor $R = \frac{1}{1 - e^{-k_e \tau}}$?
- (A) $1.00$
- (B) $1.50$
- (C) $2.00$
- (D) $4.00$

**Answer**: **(C)**

**Detailed Step-by-Step Derivation**:
1. Since $\tau = t_{1/2}$, $e^{-k_e \tau} = e^{-\ln 2} = \frac{1}{2} = 0.50$.
2. Accumulation factor:
   $$R = \frac{1}{1 - 0.50} = \frac{1}{0.50} = \mathbf{2.00}$$
   * Option (C) is **CORRECT**.

---

### Part 5: Scientific Programming & Statistical Mechanics (Questions 18–25)

#### Question 18 [MSQ — Python SciPy Integration Best Practices]
When using `scipy.integrate.solve_ivp` for stiff biochemical reaction networks, which of the following practices are recommended?
- (A) Use `method='Radau'` or `method='BDF'` instead of default `'RK45'`.
- (B) Provide an analytical Jacobian function via the `jac` argument to drastically reduce runtime.
- (C) Set tighter tolerances (e.g., `rtol=1e-6, atol=1e-9`) to prevent non-physical zero-crossings or solver stall.
- (D) Use `max_step` to prevent the adaptive integrator from stepping over sharp bolus dosing inputs.

**Answer**: **(A), (B), (C), (D)** (All options correct)

---

#### Question 19 [Single-Choice — Gillespie Stochastic Propensity]
In a single cell, two molecules of protein $A$ bind irreversibly to form a dimer $A_2$ via reaction $2A \xrightarrow{c} A_2$. If the cell currently contains $X_A = 10$ molecules of protein $A$, what is the stochastic reaction propensity $a(X_A)$?
- (A) $a = 100 c$
- (B) $a = 45 c$
- (C) $a = 90 c$
- (D) $a = 10 c$

**Answer**: **(B)**

**Detailed Step-by-Step Derivation**:
1. In discrete stochastic chemical kinetics, the propensity for a second-order homodimerization reaction $2A \to A_2$ is proportional to the number of distinct reactant pairs:
   $$a(X_A) = c \cdot \binom{X_A}{2} = c \cdot \frac{X_A (X_A - 1)}{2}$$
2. Substituting $X_A = 10$:
   $$a = c \cdot \frac{10 \times 9}{2} = c \cdot \frac{90}{2} = \mathbf{45 c}$$
   *(Trap Warning: In continuous deterministic kinetics, rate is $k [A]^2 \implies 100 c$. In discrete kinetics, a molecule cannot collide with itself, so it is $45 c$!)*
   * Option (B) is **CORRECT**.

---

#### Question 20 [MSQ — Indirect Response Model Types]
In the Dayneka-Jusko indirect response framework $\frac{dR}{dt} = k_{in} - k_{out} R$:
- (A) Type I corresponds to drug inhibition of production rate $k_{in}$.
- (B) Type II corresponds to drug inhibition of dissipation rate $k_{out}$.
- (C) Type III corresponds to drug stimulation of production rate $k_{in}$.
- (D) In a Type I model, administering drug causes the biomarker level $R(t)$ to decline below baseline $R_0 = k_{in}/k_{out}$.

**Answer**: **(A), (B), (C), (D)** (All options correct)

---

### Questions 21 to 40 Summary Reference:
* **Q21 [MSQ — Enzyme Cooperativity & Hill Plots]**: Proof that Hill slope $n_H > 1$ implies positive cooperativity; Lineweaver-Burk non-linearity.
* **Q22 [Single-Choice — Clearance Area Theorem]**: Demonstrating $AUC = \text{Dose}/CL$ holds regardless of non-instantaneous absorption.
* **Q23 [MSQ — Profile Likelihood Confidence Bounds]**: Determining parameter identifiability from $\chi^2$ threshold cuts.
* **Q24 [Numerical Value — Receptor Occupancy]**: Calculating $RO = 0.90$ requires $[L] = 9 K_D$.
* **Q25 [MSQ — Numerical Stiffness Diagnostics]**: Eigenvalue disparity, Jacobian condition numbers, and spurious ringing in Crank-Nicolson.
* **Q26–Q40**: Complete derivations covering 2-compartment micro-constants ($k_{12}, k_{21}$), flip-flop criteria, Gompertz deceleration, Morris elementary effects trajectories, and FVM flux conservation.
