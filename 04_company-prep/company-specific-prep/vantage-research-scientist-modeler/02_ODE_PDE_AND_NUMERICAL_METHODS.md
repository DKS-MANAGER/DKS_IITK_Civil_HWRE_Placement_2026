# Module 02: ODE/PDE Simulation & Numerical Methods

> **Track**: Numerical Methods & Computational Solvers for Multi-Scale QSP  
> **Role Level**: Scientist – Modeler (Scientist 1 / Scientist 2 Standard)  
> **Target Entity**: Vantage Research  
> **Evidentiary Standard**: `[PEER-REVIEWED COMPUTATIONAL MATHEMATICS & HAIRER-WANNER STANDARDS]`  

---

## 1. Executive Summary & Core Engineering Competencies

In Quantitative Systems Pharmacology (QSP) and physiological modeling, differential equation systems rarely admit closed-form analytical solutions. Modeler candidates must have a deep, operational command over numerical integration algorithms, stability boundaries, truncation error analysis, and solver selection.

This module details:
1. **Explicit One-Step Methods**: Forward Euler, Heun's method, classical 4th-Order Runge-Kutta (RK4), Butcher tableau formulation, and order of convergence ($\mathcal{O}(h^p)$).
2. **Adaptive Time-Stepping**: Embedded Runge-Kutta pairs (Dormand-Prince `RK45`, Cash-Karp), local truncation error estimation, and step-size adjustment formulas.
3. **The Challenge of Numerical Stiffness**: Physical origin of stiffness in multi-scale biological networks, linear stability domains in the complex plane ($z = \lambda h$), A-stability, and L-stability.
4. **Implicit Solvers for Stiff ODEs**: Backward Euler, Backward Differentiation Formulas (BDF / Gear's method), implicit Runge-Kutta (Radau IIA), and Newton-Raphson nonlinear iteration.
5. **Partial Differential Equations (PDEs) in Transport**: 1D Advection-Diffusion-Reaction models for tissue penetration, Finite Difference Method (FDM), Finite Volume Method (FVM), boundary conditions (Dirichlet, Neumann, Robin), and numerical stability criteria (CFL, Peclet).

---

## 2. Ordinary Differential Equation Solvers: Theory & Mechanics

Consider the initial value problem (IVP):
$$\frac{d\mathbf{y}}{dt} = \mathbf{f}(t, \mathbf{y}), \quad \mathbf{y}(t_0) = \mathbf{y}_0, \quad t \in [t_0, t_{end}]$$
where $\mathbf{y} \in \mathbb{R}^n$ is the state vector and $\mathbf{f}: \mathbb{R} \times \mathbb{R}^n \to \mathbb{R}^n$ is Lipschitz continuous in $\mathbf{y}$.

### 2.1 The General Runge-Kutta Framework & Butcher Tableau
An $s$-stage Runge-Kutta method computes the step from $t_n$ to $t_{n+1} = t_n + h$ via:
$$\mathbf{y}_{n+1} = \mathbf{y}_n + h \sum_{i=1}^s b_i \mathbf{k}_i$$
where the internal stage derivatives $\mathbf{k}_i$ are given by:
$$\mathbf{k}_i = \mathbf{f}\left(t_n + c_i h, \mathbf{y}_n + h \sum_{j=1}^s a_{ij} \mathbf{k}_j\right), \quad i = 1, \dots, s$$

The method's coefficients are compactly represented by the **Butcher Tableau**:
$$\begin{array}{c|c}
\mathbf{c} & \mathbf{A} \\
\hline
& \mathbf{b}^T
\end{array}
\quad = \quad
\begin{array}{c|cccc}
c_1 & a_{11} & a_{12} & \dots & a_{1s} \\
c_2 & a_{21} & a_{22} & \dots & a_{2s} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
c_s & a_{s1} & a_{s2} & \dots & a_{ss} \\
\hline
& b_1 & b_2 & \dots & b_s
\end{array}$$

* **Explicit RK Method (ERK)**: $a_{ij} = 0$ for all $j \ge i$. The matrix $\mathbf{A}$ is strictly lower triangular. Each stage $\mathbf{k}_i$ is computed explicitly using previously calculated stages $\mathbf{k}_1, \dots, \mathbf{k}_{i-1}$.
* **Implicit RK Method (IRK)**: $\mathbf{A}$ is not strictly lower triangular. Computing $\mathbf{k}_i$ requires solving a coupled system of $s \times n$ nonlinear algebraic equations at each time step!

### 2.2 Classical 4th-Order Runge-Kutta (RK4)
For classical RK4 ($s = 4$):
$$\mathbf{k}_1 = \mathbf{f}(t_n, \mathbf{y}_n)$$
$$\mathbf{k}_2 = \mathbf{f}\left(t_n + \frac{h}{2}, \mathbf{y}_n + \frac{h}{2} \mathbf{k}_1\right)$$
$$\mathbf{k}_3 = \mathbf{f}\left(t_n + \frac{h}{2}, \mathbf{y}_n + \frac{h}{2} \mathbf{k}_2\right)$$
$$\mathbf{k}_4 = \mathbf{f}(t_n + h, \mathbf{y}_n + h \mathbf{k}_3)$$
$$\mathbf{y}_{n+1} = \mathbf{y}_n + \frac{h}{6}(\mathbf{k}_1 + 2\mathbf{k}_2 + 2\mathbf{k}_3 + \mathbf{k}_4)$$

* **Local Truncation Error (LTE)**: $d_{n+1} = \mathcal{O}(h^5)$.
* **Global Truncation Error (GTE)**: $e_n = \mathcal{O}(h^4)$.

### 2.3 Adaptive Time-Stepping: Embedded Pairs (Dormand-Prince / RK45)
In practice, fixed-step RK4 is inefficient because smooth solution regions can tolerate large steps, while sharp biological transients (e.g., IV bolus injection or enzyme activation bursts) demand fine resolution.

An **embedded Runge-Kutta pair** computes two approximations of different orders ($p$ and $\hat{p} = p-1$) using the same stage evaluations:
$$\mathbf{y}_{n+1} = \mathbf{y}_n + h \sum_{i=1}^s b_i \mathbf{k}_i \quad (\text{Order } p)$$
$$\hat{\mathbf{y}}_{n+1} = \mathbf{y}_n + h \sum_{i=1}^s \hat{b}_i \mathbf{k}_i \quad (\text{Order } p-1)$$

The local error estimate $\mathbf{E}_n$ is obtained with zero extra function evaluations:
$$\mathbf{E}_n = \mathbf{y}_{n+1} - \hat{\mathbf{y}}_{n+1} = h \sum_{i=1}^s (b_i - \hat{b}_i) \mathbf{k}_i = \mathcal{O}(h^p)$$

#### Step-Size Control Algorithm:
Compute the scalar error norm scaled by user-defined tolerances:
$$\text{err} = \sqrt{\frac{1}{n} \sum_{i=1}^n \left( \frac{|E_{n, i}|}{\text{atol}_i + \text{rtol} |y_{n+1, i}|} \right)^2}$$

The optimal next time step $h_{new}$ is computed with safety factor $S \approx 0.85\text{–}0.90$:
$$h_{new} = h \cdot \min\left( \text{facmax}, \ \max\left( \text{facmin}, \ S \cdot \left(\frac{1}{\text{err}}\right)^{\frac{1}{p}} \right) \right)$$
* If $\text{err} \le 1.0$: Accept step $\mathbf{y}_{n+1}$ and advance with $h_{new}$.
* If $\text{err} > 1.0$: Reject step, discard $\mathbf{y}_{n+1}$, and recompute with $h_{new}$.

---

## 3. Numerical Stiffness & Implicit Methods

### 3.1 The Origin of Stiffness in QSP Models
Biological systems naturally span vast timescale disparities:
* *Fast processes*: Receptor-ligand association/dissociation ($k_{on} \approx 10^5\text{–}10^7 \ \text{M}^{-1}\text{s}^{-1}$, timescale milliseconds to seconds).
* *Intermediate processes*: Drug absorption and elimination ($t_{1/2} \approx \text{hours to days}$).
* *Slow processes*: Target synthesis/turnover, tumor growth, or autoimmune disease progression (timescale weeks to months).

Let $\mathbf{J} = \frac{\partial \mathbf{f}}{\partial \mathbf{y}}$ be the system Jacobian with eigenvalues $\lambda_1, \dots, \lambda_n$.
* **Definition of Stiffness Ratio (SR)**:
  $$SR = \frac{\max_i |\text{Re}(\lambda_i)|}{\min_i |\text{Re}(\lambda_i)|} \gg 1 \quad \text{with } \text{Re}(\lambda_i) < 0$$
When $SR > 10^3\text{–}10^6$, the system is **stiff**.

### 3.2 Linear Stability Analysis & Dahlquist Test Equation
Consider Dahlquist's test problem:
$$\frac{dy}{dt} = \lambda y, \quad \text{Re}(\lambda) < 0$$

Applying a numerical one-step method yields:
$$y_{n+1} = R(z) y_n, \quad z = \lambda h \in \mathbb{C}$$
where $R(z)$ is the **stability function**. The numerical solution remains bounded if and only if:
$$|R(z)| \le 1$$
The region $\mathcal{S} = \{z \in \mathbb{C} : |R(z)| \le 1\}$ is the **linear stability region**.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    STABILITY REGION COMPARISON IN COMPLEX PLANE             │
├──────────────────────────────────────┬──────────────────────────────────────┤
│ EXPLICIT METHODS (e.g., Forward Euler)│ IMPLICIT METHODS (e.g., Backward Euler)
│ R(z) = 1 + z                         │ R(z) = 1 / (1 - z)                   │
│ Stability Region: Disk of radius 1   │ Stability Region: Entire complex     │
│ centered at z = -1.                  │ plane EXCEPT a disk of radius 1 at +1│
│                                      │                                      │
│                Im(z)                 │                Im(z)                 │
│                  ▲                   │                  ▲                   │
│                  │                   │       STABLE     │    STABLE         │
│             ╭────┼────╮              │      ────────────┼─────────────      │
│     STABLE  │  ● │    │ UNSTABLE     │                  │  ╭───╮            │
│    ─────────┼────┼────┼────────►Re(z)│    ──────────────┼──┤ ● ├──► Re(z)    │
│      -2     │ -1 │  0 │              │                  │  ╰───╯  +1        │
│             ╰────┼────╯              │       STABLE     │  UNSTABLE         │
│                  │                   │                  │                   │
├──────────────────────────────────────┴──────────────────────────────────────┤
│ • Forward Euler requires: |1 + λh| ≤ 1 ⟹ h ≤ 2 / |λ|                        │
│ • If fast eigenvalue has λ = -10,000 s⁻¹, explicit solver MUST take         │
│   h ≤ 0.0002 s even when simulating 30 days of drug therapy!                │
│ • Backward Euler is stable for ANY h > 0 because Re(z) < 0 ⟹ |1 - z| > 1!   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.3 A-Stability and L-Stability
* **A-Stability**: A numerical method is A-stable if its stability region contains the entire left half of the complex plane:
  $$\mathbb{C}^- = \{z \in \mathbb{C} : \text{Re}(z) \le 0\} \subseteq \mathcal{S}$$
  *Backward Euler, Trapezoidal rule, and Radau IIA are A-stable.*
* **L-Stability**: A method is L-stable if it is A-stable AND:
  $$\lim_{\text{Re}(z) \to -\infty} |R(z)| = 0$$
  *Significance*: An L-stable solver instantly damps out high-frequency stiff transients without spurious oscillations. Backward Euler and Radau IIA are L-stable; the Trapezoidal rule (Crank-Nicolson) is A-stable but NOT L-stable ($|R(-\infty)| = 1$, causing ringing artifacts).

### 3.4 Key Implicit Solvers for Stiff QSP Models
1. **Backward Differentiation Formulas (BDF / Gear's Method)**:
   $$\sum_{j=0}^k \alpha_j \mathbf{y}_{n+1-j} = h \beta \mathbf{f}(t_{n+1}, \mathbf{y}_{n+1})$$
   BDF methods of order $k=1$ to $k=5$ are implemented in `scipy.integrate.solve_ivp(method='BDF')` and MATLAB's `ode15s`. Excellent for stiff kinetics.
2. **Radau IIA (Implicit Runge-Kutta)**:
   A 5th-order, 3-stage fully implicit Runge-Kutta method. A-stable and L-stable. Implemented in `scipy.integrate.solve_ivp(method='Radau')`. The gold-standard solver for stiff physiological models and differential algebraic equations (DAEs).

---

## 4. Partial Differential Equations (PDEs) in Biological Transport

### 4.1 1D Advection-Diffusion-Reaction Equation
When modeling drug transport across an endothelial barrier or through a solid tumor:
$$\frac{\partial C}{\partial t} + \underbrace{u \frac{\partial C}{\partial x}}_{\text{Advection}} = \underbrace{D \frac{\partial^2 C}{\partial x^2}}_{\text{Diffusion}} - \underbrace{R(C)}_{\text{Reaction / Clearance}}, \quad x \in [0, L]$$
where:
* $C(x, t)$ is drug concentration [$\text{mg/mL}$].
* $u$ is interstitial fluid velocity [$\text{cm/s}$].
* $D$ is Brownian diffusion coefficient in tissue [$\text{cm}^2/\text{s}$].
* $R(C) = \frac{V_{max} C}{K_m + C}$ represents cellular receptor uptake / clearance.

### 4.2 Boundary Conditions
1. **Dirichlet Boundary Condition (Fixed Concentration)**:
   $$C(0, t) = C_{plasma}(t)$$
   *(e.g., continuous intravenous blood supply at vessel wall).*
2. **Neumann Boundary Condition (Zero Flux / Impermeable Wall)**:
   $$-D \frac{\partial C}{\partial x}\Bigg|_{x = L} = 0 \implies \frac{\partial C}{\partial x}(L, t) = 0$$
   *(e.g., symmetrical tumor core or impermeable basement membrane).*
3. **Robin Boundary Condition (Mixed / Permeable Membrane Transport)**:
   $$-D \frac{\partial C}{\partial x}\Bigg|_{x = 0} = P_{perm} \left( C_{blood}(t) - C(0, t) \right)$$
   where $P_{perm}$ is vascular wall permeability [$\text{cm/s}$].

### 4.3 Spatial Discretization via Finite Difference Method (FDM)
Discretize spatial domain $[0, L]$ into $N$ intervals of width $\Delta x = L / N$, with grid points $x_j = j \Delta x$ ($j = 0, \dots, N$):
* **Diffusion Term (Central Difference, $\mathcal{O}(\Delta x^2)$)**:
  $$\frac{\partial^2 C}{\partial x^2}\Bigg|_{x_j} \approx \frac{C_{j+1} - 2C_j + C_{j-1}}{\Delta x^2}$$
* **Advection Term (Upwind Difference for $u > 0$, $\mathcal{O}(\Delta x)$)**:
  $$u \frac{\partial C}{\partial x}\Bigg|_{x_j} \approx u \frac{C_j - C_{j-1}}{\Delta x}$$
  *(Central difference for advection $\frac{C_{j+1}-C_{j-1}}{2\Delta x}$ produces non-physical numerical oscillations when grid Peclet number $Pe_g = \frac{u \Delta x}{D} > 2$!)*

### 4.4 Method of Lines (MOL)
Substituting spatial finite differences converts the PDE into a system of $N-1$ coupled ODEs in time:
$$\frac{dC_j}{dt} = -u \left(\frac{C_j - C_{j-1}}{\Delta x}\right) + D \left(\frac{C_{j+1} - 2C_j + C_{j-1}}{\Delta x^2}\right) - R(C_j), \quad j = 1, \dots, N-1$$
This coupled ODE system can then be integrated in Python using `scipy.integrate.solve_ivp(method='BDF')`.

### 4.5 Stability Criteria
* **Courant-Friedrichs-Lewy (CFL) Condition**:
  $$CFL = \frac{u \Delta t}{\Delta x} \le 1$$
* **Diffusion Number (von Neumann Stability for explicit Euler)**:
  $$r = \frac{D \Delta t}{\Delta x^2} \le \frac{1}{2}$$

---

## 5. Solver Selection Matrix for QSP & PK/PD Applications

| Problem Characteristic | Dominant Physics | Recommended Solver (Python) | Recommended Solver (MATLAB) | Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Non-stiff PK models** | 1- or 2-compartment linear clearance | `solve_ivp(method='RK45')` | `ode45` | Efficient, low memory overhead, adaptive step size. |
| **Enzyme & receptor networks** | Fast binding, slow synthesis ($SR > 10^4$) | `solve_ivp(method='Radau')` | `ode15s` | L-stable; damps fast transients without step-size collapse. |
| **Large metabolic networks** | Sparse Jacobian, $> 50$ ODEs | `solve_ivp(method='BDF')` | `ode15s` / `ode23t` | Backward differentiation handles large sparse Jacobian matrices efficiently. |
| **Spatial drug penetration** | Method-of-lines discretized 1D/2D PDE | `solve_ivp(method='Radau')` | `pdepe` / `ode15s` | Stiff diffusion spectrum ($\lambda \propto -4D/\Delta x^2$). |

---

## 6. Worked Numerical Problems

### Problem 2.1: Stiffness Detection & Stability Limit in a Two-Compartment Model
**Question**: An intravenous drug distributes between blood plasma ($y_1$) and tissue ($y_2$) governed by:
$$\frac{dy_1}{dt} = -1001 y_1 + 999 y_2$$
$$\frac{dy_2}{dt} = 999 y_1 - 1001 y_2$$
with initial conditions $y_1(0) = 2.0, y_2(0) = 0.0$.
1. Find the exact analytical solution.
2. Determine the eigenvalues and the stiffness ratio.
3. Compute the maximum stable time step $h_{max}$ if Forward Euler is used.
4. Explain what happens if $h = 0.0015\text{ s}$ is used with Forward Euler versus Backward Euler.

#### Solution:
**Step 1: Eigenvalues and Analytical Solution**
The system matrix is:
$$\mathbf{A} = \begin{pmatrix} -1001 & 999 \\ 999 & -1001 \end{pmatrix}$$
Trace $\tau = -2002$, Determinant $\Delta = (-1001)^2 - (999)^2 = (1001 - 999)(1001 + 999) = (2)(2000) = 4000$.

Characteristic equation:
$$\lambda^2 + 2002 \lambda + 4000 = 0 \implies (\lambda + 2)(\lambda + 2000) = 0$$
$$\lambda_1 = -2\text{ s}^{-1}, \quad \lambda_2 = -2000\text{ s}^{-1}$$

Eigenvectors:
* For $\lambda_1 = -2$: $(\mathbf{A} + 2\mathbf{I})\mathbf{v}_1 = \begin{pmatrix} -999 & 999 \\ 999 & -999 \end{pmatrix} \mathbf{v}_1 = \mathbf{0} \implies \mathbf{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$.
* For $\lambda_2 = -2000$: $(\mathbf{A} + 2000\mathbf{I})\mathbf{v}_2 = \begin{pmatrix} 999 & 999 \\ 999 & 999 \end{pmatrix} \mathbf{v}_2 = \mathbf{0} \implies \mathbf{v}_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$.

General solution:
$$\mathbf{y}(t) = c_1 e^{-2t} \begin{pmatrix} 1 \\ 1 \end{pmatrix} + c_2 e^{-2000t} \begin{pmatrix} 1 \\ -1 \end{pmatrix}$$

Applying initial conditions $\mathbf{y}(0) = \begin{pmatrix} 2 \\ 0 \end{pmatrix}$:
$$c_1 + c_2 = 2, \quad c_1 - c_2 = 0 \implies c_1 = 1, \ c_2 = 1$$

Exact Analytical Solution:
$$y_1(t) = e^{-2t} + e^{-2000t}$$
$$y_2(t) = e^{-2t} - e^{-2000t}$$

**Step 2: Stiffness Ratio**
$$SR = \frac{|\lambda_2|}{|\lambda_1|} = \frac{2000}{2} = \mathbf{1000}$$
The fast transient $e^{-2000t}$ decays within $t \approx \frac{5}{2000} = 0.0025\text{ s}$, after which both concentrations follow the slow decay $e^{-2t}$ over several seconds.

**Step 3: Forward Euler Stability Limit**
For Forward Euler, stability requires $|1 + \lambda_i h| \le 1$ for all eigenvalues.
For $\lambda_2 = -2000$:
$$-1 \le 1 - 2000 h \le 1 \implies -2 \le -2000 h \implies h \le \frac{2}{2000} = \mathbf{0.0010\text{ s}}$$
The maximum stable step size is $h_{max} = 1.0\text{ ms}$.

**Step 4: Comparison at $h = 0.0015\text{ s}$**
* **Forward Euler**: $h = 0.0015\text{ s} > h_{max}$.
  $$1 + \lambda_2 h = 1 - 2000(0.0015) = 1 - 3.0 = -2.0$$
  At each step, the error is multiplied by $(-2.0)$. After $n$ steps, error grows as $(-2.0)^n$. The numerical solution **explodes violently to infinity**, even though the exact component $e^{-2000t}$ is practically zero!
* **Backward Euler**:
  $$R(\lambda_2 h) = \frac{1}{1 - \lambda_2 h} = \frac{1}{1 - (-2000 \times 0.0015)} = \frac{1}{1 + 3.0} = \frac{1}{4.0} = 0.25 < 1$$
  The fast transient decays stably without explosion, allowing Backward Euler to take large steps ($h = 0.1\text{ s}$) once the fast transient has passed!

---

### Problem 2.2: Truncation Error Verification for Euler vs Midpoint vs RK4
**Question**: Derive the local truncation error of the Midpoint method (RK2) for $y' = f(t, y)$ and verify that it achieves $\mathcal{O}(h^3)$ local order.

#### Solution:
The Midpoint method evaluates:
$$k_1 = f(t_n, y_n)$$
$$y_{n+1} = y_n + h f\left(t_n + \frac{h}{2}, \ y_n + \frac{h}{2} k_1\right)$$

Expand $y(t_n + h)$ using Taylor series about $t_n$:
$$y(t_n + h) = y(t_n) + h y'(t_n) + \frac{h^2}{2} y''(t_n) + \frac{h^3}{6} y'''(t_n) + \mathcal{O}(h^4)$$
Since $y' = f$, $y'' = f_t + f_y f$. Thus:
$$y(t_n + h) = y_n + h f + \frac{h^2}{2} (f_t + f_y f) + \frac{h^3}{6} y'''(t_n) + \mathcal{O}(h^4)$$

Now expand the numerical increment $f\left(t_n + \frac{h}{2}, y_n + \frac{h}{2} f\right)$ via 2D Taylor series:
$$f\left(t_n + \frac{h}{2}, y_n + \frac{h}{2} f\right) = f + \frac{h}{2} f_t + \left(\frac{h}{2} f\right) f_y + \mathcal{O}(h^2) = f + \frac{h}{2} (f_t + f f_y) + \mathcal{O}(h^2)$$

Multiply by $h$:
$$y_{n+1} = y_n + h \left[ f + \frac{h}{2}(f_t + f f_y) + \mathcal{O}(h^2) \right] = y_n + h f + \frac{h^2}{2}(f_t + f f_y) + \mathcal{O}(h^3)$$

Subtracting $y_{n+1}$ from the exact Taylor expansion:
$$d_{n+1} = y(t_n + h) - y_{n+1} = \left[ y_n + h f + \frac{h^2}{2}(f_t + f f_y) + \frac{h^3}{6} y''' \right] - \left[ y_n + h f + \frac{h^2}{2}(f_t + f f_y) + \mathcal{O}(h^3) \right] = \mathbf{\mathcal{O}(h^3)}$$
The terms through $h^2$ cancel exactly. Thus, the Local Truncation Error is $\mathcal{O}(h^3)$, and the global convergence order is $\mathcal{O}(h^2)$ (Second Order).
