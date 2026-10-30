# Module 01: Mathematical Foundations & Dynamical Systems

> **Track**: Core Mathematical Foundations for Quantitative Systems Pharmacology (QSP)  
> **Role Level**: Scientist – Modeler (Scientist 1 / Scientist 2 Standard)  
> **Target Entity**: Vantage Research  
> **Evidentiary Standard**: `[PEER-REVIEWED MATHEMATICAL & DYNAMICAL SYSTEMS STANDARDS]`  

---

## 1. Executive Summary & Syllabus Overview

At Vantage Research, mathematical modeling is not treated as abstract curve fitting; it is the fundamental language used to describe multi-scale physiological processes. Whether modeling enzyme-substrate complexes, antibody-receptor dynamics, or cytokine cascades, the modeler must translate physical and biochemical hypotheses into well-posed dynamical systems.

This module establishes the foundational mathematical apparatus required for the **Scientist 2** benchmark:
1. **Linear Algebra & Matrix Stability**: Eigenvalues, eigenvectors, characteristic polynomials, similarity transformations, and the trace-determinant classification of fixed points.
2. **Calculus & Multivariable Analysis**: Directional derivatives, gradients, Jacobians, Hessians, Taylor series in $\mathbb{R}^n$, and implicit differentiation.
3. **Dynamical Systems Theory**: Autonomous vs non-autonomous systems, equilibrium points, Hartman-Grobman theorem, phase-plane portraits, nullclines, limit cycles (Poincaré-Bendixson theorem), and local bifurcations (saddle-node, transcritical, pitchfork, Hopf).
4. **Conservation Laws & Rate Formulations**: Macroscopic conservation of mass, compartmental continuity, translating verbal kinetic rules into formal rate equations.
5. **Dimensional Analysis & Non-Dimensionalization**: Buckingham Pi theorem, characteristic scales, scaling biological equations, and asymptotic limits.

---

## 2. Linear Algebra & Stability of Linear Dynamical Systems

### 2.1 The General Linear Autonomous System
Consider the $n$-dimensional linear system of ordinary differential equations:
$$\frac{d\mathbf{x}}{dt} = \mathbf{A} \mathbf{x}, \quad \mathbf{x}(0) = \mathbf{x}_0$$
where $\mathbf{x} \in \mathbb{R}^n$ is the state vector and $\mathbf{A} \in \mathbb{R}^{n \times n}$ is a constant real matrix.

The analytical solution is given by the matrix exponential:
$$\mathbf{x}(t) = e^{\mathbf{A}t} \mathbf{x}_0 = \left( \sum_{k=0}^{\infty} \frac{(\mathbf{A}t)^k}{k!} \right) \mathbf{x}_0$$

If $\mathbf{A}$ is diagonalizable ($\mathbf{A} = \mathbf{P} \mathbf{\Lambda} \mathbf{P}^{-1}$, where $\mathbf{\Lambda} = \text{diag}(\lambda_1, \dots, \lambda_n)$ and the columns of $\mathbf{P}$ are the linearly independent eigenvectors $\mathbf{v}_i$):
$$\mathbf{x}(t) = \mathbf{P} e^{\mathbf{\Lambda}t} \mathbf{P}^{-1} \mathbf{x}_0 = \sum_{i=1}^n c_i e^{\lambda_i t} \mathbf{v}_i$$
where the constants $c_i$ satisfy $\mathbf{P} \mathbf{c} = \mathbf{x}_0$.

### 2.2 Asymptotic Stability Criteria
* **Theorem (Linear Stability)**:
  1. The origin $\mathbf{x}^* = \mathbf{0}$ is **asymptotically stable** if and only if **all** eigenvalues of $\mathbf{A}$ have strictly negative real parts:
     $$\text{Re}(\lambda_i) < 0 \quad \forall i \in \{1, 2, \dots, n\}$$
     In this case, $\lim_{t \to \infty} \mathbf{x}(t) = \mathbf{0}$ for all $\mathbf{x}_0$.
  2. The origin is **neutrally (marginally) stable** if all eigenvalues have $\text{Re}(\lambda_i) \le 0$, and those with $\text{Re}(\lambda_i) = 0$ have equal algebraic and geometric multiplicities (non-defective).
  3. The origin is **unstable** if at least one eigenvalue has $\text{Re}(\lambda_i) > 0$, or if an eigenvalue with $\text{Re}(\lambda_i) = 0$ has geometric multiplicity strictly less than its algebraic multiplicity.

### 2.3 The Two-Dimensional Phase-Plane Classification
For a 2D planar system $\dot{\mathbf{x}} = \mathbf{A}\mathbf{x}$ with:
$$\mathbf{A} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$

The characteristic equation is:
$$\det(\mathbf{A} - \lambda \mathbf{I}) = \lambda^2 - \tau \lambda + \Delta = 0$$
where:
* $\tau = \text{tr}(\mathbf{A}) = a + d$ (Trace)
* $\Delta = \det(\mathbf{A}) = ad - bc$ (Determinant)
* Discriminant: $D = \tau^2 - 4\Delta$

The eigenvalues are:
$$\lambda_{1, 2} = \frac{\tau \pm \sqrt{\tau^2 - 4\Delta}}{2}$$

```
                          ▲ Trace (τ)
                          │         Unstable Spirals
             Unstable     │         (τ > 0, D < 0)
              Nodes       │
             (τ > 0, D>0) │
                          │                  Parabola: Δ = τ²/4
    ──────────────────────┼─────────────────────────► Determinant (Δ)
        Saddles (Δ < 0)   │    Centers (τ = 0, Δ > 0)
                          │
             Stable       │          Stable Spirals
              Nodes       │          (τ < 0, D < 0)
             (τ < 0, D>0) │
                          │
```

#### Detailed Stability Rules:
1. **$\Delta < 0$ (Saddle Point)**:
   - Eigenvalues are real with opposite signs ($\lambda_1 < 0 < \lambda_2$).
   - Always **unstable**. Trajectories approach along the stable eigenspace ($E^s$) and diverge along the unstable eigenspace ($E^u$).
2. **$\Delta > 0, \tau < 0$ (Stable Equilibrium)**:
   - If $\tau^2 - 4\Delta > 0$: **Stable Node** (two distinct real negative eigenvalues).
   - If $\tau^2 - 4\Delta = 0$: **Degenerate / Star Node** ($\lambda_1 = \lambda_2 < 0$).
   - If $\tau^2 - 4\Delta < 0$: **Stable Spiral / Focus** (complex conjugates $\alpha \pm i\beta$ with $\alpha < 0$).
3. **$\Delta > 0, \tau > 0$ (Unstable Equilibrium)**:
   - If $\tau^2 - 4\Delta > 0$: **Unstable Node** (two real positive eigenvalues).
   - If $\tau^2 - 4\Delta < 0$: **Unstable Spiral / Focus** ($\alpha \pm i\beta$ with $\alpha > 0$).
4. **$\tau = 0, \Delta > 0$ (Center / Vortex)**:
   - Pure imaginary eigenvalues $\lambda = \pm i \sqrt{\Delta}$.
   - Neutrally stable concentric closed trajectories (conservative system).

---

## 3. Nonlinear Dynamical Systems & Linearization

### 3.1 Autonomous Systems & Fixed Points
Consider the general autonomous nonlinear system:
$$\frac{d\mathbf{x}}{dt} = \mathbf{f}(\mathbf{x}), \quad \mathbf{x} \in \mathbb{R}^n, \quad \mathbf{f}: \mathbb{R}^n \to \mathbb{R}^n$$

A point $\mathbf{x}^* \in \mathbb{R}^n$ is an **equilibrium point (fixed point / steady state)** if:
$$\mathbf{f}(\mathbf{x}^*) = \mathbf{0}$$

### 3.2 The Jacobian Matrix and Hartman-Grobman Theorem
Let $\mathbf{u}(t) = \mathbf{x}(t) - \mathbf{x}^*$ represent a small perturbation away from the equilibrium point. Expanding $\mathbf{f}(\mathbf{x})$ via Taylor series about $\mathbf{x}^*$:
$$\mathbf{f}(\mathbf{x}^* + \mathbf{u}) = \mathbf{f}(\mathbf{x}^*) + \mathbf{J}(\mathbf{x}^*) \mathbf{u} + \mathcal{O}(\|\mathbf{u}\|^2)$$

Since $\mathbf{f}(\mathbf{x}^*) = \mathbf{0}$, the linearized perturbation dynamics are governed by:
$$\frac{d\mathbf{u}}{dt} \approx \mathbf{J}(\mathbf{x}^*) \mathbf{u}$$
where $\mathbf{J}(\mathbf{x}^*)$ is the **Jacobian matrix** evaluated at $\mathbf{x}^*$:
$$\mathbf{J}(\mathbf{x}^*) = \begin{pmatrix}
\frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \dots & \frac{\partial f_1}{\partial x_n} \\
\frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & \dots & \frac{\partial f_2}{\partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial f_n}{\partial x_1} & \frac{\partial f_n}{\partial x_2} & \dots & \frac{\partial f_n}{\partial x_n}
\end{pmatrix}_{\mathbf{x} = \mathbf{x}^*}$$

* **Theorem (Hartman-Grobman)**:
  If the equilibrium point $\mathbf{x}^*$ is **hyperbolic** (i.e., no eigenvalue of $\mathbf{J}(\mathbf{x}^*)$ has zero real part, $\text{Re}(\lambda_i) \ne 0 \ \forall i$), then there exists a local homeomorphism mapping the trajectories of the nonlinear system $\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x})$ in a neighborhood of $\mathbf{x}^*$ to the trajectories of the linearized system $\dot{\mathbf{u}} = \mathbf{J}(\mathbf{x}^*)\mathbf{u}$.
  * *Scientist 2 Insight*: If an eigenvalue has $\text{Re}(\lambda) = 0$ (e.g., center or bifurcation point), linearization is inconclusive, and nonlinear higher-order terms or Lyapunov functions must be evaluated.

---

## 4. Phase-Plane Analysis & Nullclines

For a 2-variable biological system:
$$\frac{dx}{dt} = f(x, y), \quad \frac{dy}{dt} = g(x, y)$$

### 4.1 Nullclines
* **$x$-nullcline**: The set of points where $\frac{dx}{dt} = 0 \implies f(x, y) = 0$. On this curve, flow is purely vertical ($\uparrow$ or $\downarrow$).
* **$y$-nullcline**: The set of points where $\frac{dy}{dt} = 0 \implies g(x, y) = 0$. On this curve, flow is purely horizontal ($\rightarrow$ or $\leftarrow$).
* **Equilibrium Points**: Intersections of the $x$-nullcline and $y$-nullcline ($f(x, y) = 0 \cap g(x, y) = 0$).

### 4.2 Step-by-Step Phase-Plane Construction Protocol
1. Find all algebraic intersections of $f(x, y) = 0$ and $g(x, y) = 0$.
2. Compute the analytical Jacobian $\mathbf{J}(x, y) = \begin{pmatrix} f_x & f_y \\ g_x & g_y \end{pmatrix}$.
3. For each fixed point $(x^*, y^*)$, evaluate $\mathbf{J}(x^*, y^*)$, find $\tau$ and $\Delta$, and determine local stability.
4. Partition the phase space into regions bounded by nullclines and assign vector arrows $(\text{sign}(f), \text{sign}(g))$.
5. Sketch representative trajectories connecting regions.

---

## 5. Non-Dimensionalization & Characteristic Scales

### 5.1 Why Non-Dimensionalization is Vital in Biological Modeling
Biological models often involve parameters differing by 6 to 12 orders of magnitude (e.g., fast sub-second receptor binding vs slow multi-week tumor growth). Non-dimensionalization:
1. Minimizes the total number of free parameters (Buckingham Pi theorem).
2. Identifies the dominant biological timescales and small perturbation parameters ($\epsilon \ll 1$).
3. Eliminates unit ambiguity and prevents floating-point numerical overflow/underflow during simulation.

### 5.2 Worked Derivation: Non-Dimensionalizing a Damped Biological Feedback Oscillator
Consider a cytokine-receptor negative feedback loop governed by:
$$\frac{dx}{dt} = \frac{V_m y^n}{K^n + y^n} - k_d x$$
$$\frac{dy}{dt} = k_s x - \gamma y$$
where $[x]$ and $[y]$ are cytokine and inhibitor concentrations in $\text{nM}$, and $t$ is time in hours.

#### Step 1: Define Characteristic Scales
Let:
$$\tilde{x} = \frac{x}{x_c}, \quad \tilde{y} = \frac{y}{y_c}, \quad \tilde{t} = \frac{t}{t_c}$$
where $x_c, y_c, t_c$ are constant reference scales to be determined.

#### Step 2: Substitute into Differential Equations
By chain rule, $\frac{dx}{dt} = \frac{x_c}{t_c} \frac{d\tilde{x}}{d\tilde{t}}$. Substituting:
$$\frac{x_c}{t_c} \frac{d\tilde{x}}{d\tilde{t}} = \frac{V_m y_c^n \tilde{y}^n}{K^n + y_c^n \tilde{y}^n} - k_d x_c \tilde{x}$$
$$\frac{y_c}{t_c} \frac{d\tilde{y}}{d\tilde{t}} = k_s x_c \tilde{x} - \gamma y_c \tilde{y}$$

#### Step 3: Choose Characteristic Scales to Balance Terms
* Choose $y_c = K$ (scales inhibitor concentration by its half-maximal activation constant).
* Choose $t_c = \frac{1}{k_d}$ (characteristic timescale set by cytokine degradation).
* Balance production in equation 1: Set $\frac{x_c}{t_c} = V_m \implies x_c = V_m t_c = \frac{V_m}{k_d}$.

#### Step 4: Formulate the Dimensionless System
Multiplying equation 1 by $\frac{t_c}{x_c} = \frac{1}{V_m}$:
$$\frac{d\tilde{x}}{d\tilde{t}} = \frac{\tilde{y}^n}{1 + \tilde{y}^n} - \tilde{x}$$

Multiplying equation 2 by $\frac{t_c}{y_c} = \frac{1}{K k_d}$:
$$\frac{d\tilde{y}}{d\tilde{t}} = \left( \frac{k_s x_c}{K k_d} \right) \tilde{x} - \left( \frac{\gamma}{k_d} \right) \tilde{y}$$
$$\frac{d\tilde{y}}{d\tilde{t}} = \alpha \tilde{x} - \beta \tilde{y}$$
where the dimensionless groups are:
$$\alpha = \frac{k_s V_m}{K k_d^2}, \quad \beta = \frac{\gamma}{k_d}$$

*Result*: The original 6 physical parameters ($V_m, K, n, k_d, k_s, \gamma$) are reduced to **2 dimensionless parameters** ($\alpha, \beta$) plus the exponent $n$.

---

## 6. Worked Mathematical Problems

### Problem 1.1: Complete Stability & Phase-Plane Analysis of a Receptor Activation Model
**Scenario**: In an oncology signaling pathway, the active receptor concentration $R$ and an intracellular negative regulator $P$ interact according to:
$$\frac{dR}{dt} = S_0 - k_1 R - k_2 R P$$
$$\frac{dP}{dt} = k_3 R - k_4 P$$
where $S_0 = 10\text{ nM/h}$, $k_1 = 1.0\text{ h}^{-1}$, $k_2 = 0.5\text{ nM}^{-1}\text{h}^{-1}$, $k_3 = 2.0\text{ h}^{-1}$, and $k_4 = 1.0\text{ h}^{-1}$.

**Tasks**:
1. Find all equilibrium points in the biologically relevant domain ($R \ge 0, P \ge 0$).
2. Evaluate the Jacobian matrix at the equilibrium point.
3. Determine the eigenvalues, trace, determinant, and classify the stability.

#### Solution:
**Step 1: Equilibrium Points**
Set $\frac{dP}{dt} = 0 \implies k_3 R - k_4 P = 0 \implies P = \frac{k_3}{k_4} R = \frac{2.0}{1.0} R = 2 R$.

Substitute into $\frac{dR}{dt} = 0$:
$$S_0 - k_1 R - k_2 R (2 R) = 0$$
$$10 - 1.0 R - 0.5 R (2 R) = 0 \implies 10 - R - R^2 = 0$$
$$R^2 + R - 10 = 0$$

Solving the quadratic equation:
$$R^* = \frac{-1 \pm \sqrt{1^2 - 4(1)(-10)}}{2} = \frac{-1 \pm \sqrt{41}}{2} \approx \frac{-1 + 6.4031}{2} = \mathbf{2.7016\text{ nM}}$$
(Reject negative root $R = -3.7016$ as biologically impossible).

The corresponding regulator level:
$$P^* = 2 R^* = 2(2.7016) = \mathbf{5.4031\text{ nM}}$$
Unique biological equilibrium: $(R^*, P^*) = (2.7016, 5.4031)$.

**Step 2: Analytical Jacobian**
$$\mathbf{J}(R, P) = \begin{pmatrix} \frac{\partial \dot{R}}{\partial R} & \frac{\partial \dot{R}}{\partial P} \\ \frac{\partial \dot{P}}{\partial R} & \frac{\partial \dot{P}}{\partial P} \end{pmatrix} = \begin{pmatrix} -(k_1 + k_2 P) & -k_2 R \\ k_3 & -k_4 \end{pmatrix}$$

Substitute the numerical parameters and steady-state values:
$$J_{11} = -(1.0 + 0.5 \times 5.4031) = -(1.0 + 2.7016) = -3.7016\text{ h}^{-1}$$
$$J_{12} = -(0.5 \times 2.7016) = -1.3508\text{ h}^{-1}$$
$$J_{21} = k_3 = 2.0\text{ h}^{-1}$$
$$J_{22} = -k_4 = -1.0\text{ h}^{-1}$$

$$\mathbf{J}(R^*, P^*) = \begin{pmatrix} -3.7016 & -1.3508 \\ 2.0 & -1.0 \end{pmatrix}$$

**Step 3: Stability Classification**
* **Trace**: $\tau = J_{11} + J_{22} = -3.7016 + (-1.0) = \mathbf{-4.7016} < 0$.
* **Determinant**:
  $$\Delta = J_{11} J_{22} - J_{12} J_{21} = (-3.7016)(-1.0) - (-1.3508)(2.0) = 3.7016 + 2.7016 = \mathbf{6.4032} > 0$$
* **Discriminant**:
  $$D = \tau^2 - 4\Delta = (-4.7016)^2 - 4(6.4032) = 22.105 - 25.613 = \mathbf{-3.508} < 0$$

* **Eigenvalues**:
  $$\lambda_{1, 2} = \frac{\tau \pm \sqrt{D}}{2} = \frac{-4.7016 \pm i \sqrt{3.508}}{2} = \mathbf{-2.3508 \pm 0.9365 i}$$

* **Conclusion**:
  Since $\tau < 0$, $\Delta > 0$, and $D < 0$, the equilibrium point is a **Stable Spiral (Focus)**. Perturbations around this steady state will undergo damped oscillations and decay exponentially to the baseline.

---

### Problem 1.2: Bifurcation Analysis in an Auto-Catalytic Gene Switch
**Question**: A synthetic gene expression switch satisfies the dimensionless model:
$$\frac{dx}{dt} = \mu + \frac{x^2}{1 + x^2} - x$$
where $\mu \ge 0$ is a basal transcription rate. Determine the critical bifurcation parameter $\mu_c$ where the system transitions between monostability and bistability.

#### Solution:
Equilibrium satisfies:
$$\mu + \frac{x^2}{1 + x^2} - x = 0 \implies \mu = x - \frac{x^2}{1 + x^2}$$

Define $g(x) = x - \frac{x^2}{1 + x^2}$. Saddle-node bifurcations occur where the function $g(x)$ has local extrema ($\frac{dg}{dx} = 0$):
$$\frac{dg}{dx} = 1 - \frac{d}{dx}\left(\frac{x^2}{1 + x^2}\right) = 1 - \frac{2x(1 + x^2) - x^2(2x)}{(1 + x^2)^2} = 1 - \frac{2x}{(1 + x^2)^2} = 0$$
$$(1 + x^2)^2 = 2x$$

Expanding:
$$(x^2 + 1)^2 - 2x = x^4 + 2x^2 - 2x + 1 = 0$$

Let us check roots:
For $x \ge 0$: At $x = 0.5$, $(1 + 0.25)^2 = 1.5625$, while $2(0.5) = 1.0$.
At $x = 1.0$, $(1 + 1)^2 = 4.0$, while $2(1) = 2.0$.
Notice that for all $x \ge 0$, $(1 + x^2)^2 \ge 1 + 2x^2 > 2x$ (since $2x^2 - 2x + 1 = 2(x - 0.5)^2 + 0.5 > 0$).
Therefore, $(1 + x^2)^2 = 2x$ has **no real roots**!
*Conclusion*: The function $g(x)$ is strictly monotonically increasing for all $x \ge 0$. Thus, for every $\mu \ge 0$, there exists **exactly one real steady state**! The system never undergoes a saddle-node bifurcation into bistability under this rate law.
*(Scientist 2 Demonstration: Catching the trap where candidates blindly assume an algebraic equation must have bifurcation points without verifying the discriminant!)*
