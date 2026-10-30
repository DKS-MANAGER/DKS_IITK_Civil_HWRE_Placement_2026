# Module 03: Parameter Estimation, Optimization & Sensitivity Analysis

> **Track**: Model Calibration, Identifiability & Sensitivity in Drug Development  
> **Role Level**: Scientist – Modeler (Scientist 1 / Scientist 2 Standard)  
> **Target Entity**: Vantage Research  
> **Evidentiary Standard**: `[PEER-REVIEWED PHARMACOMETRICS & GLOBAL SENSITIVITY STANDARDS]`  

---

## 1. Executive Summary & Core Modeling Principles

In Quantitative Systems Pharmacology (QSP), constructing differential equations is only the first step. A model becomes a reliable drug development tool only when its parameters are calibrated against experimental data, its parameter identifiability is proven, and its sensitivities are mapped.

This module details:
1. **Model Governance**: The rigorous distinction between Model Verification, Model Calibration, and Model Validation.
2. **Parameter Identifiability**: Structural identifiability (Laplace transforms, Lie derivatives) vs Practical identifiability (Fisher Information Matrix, Profile Likelihood).
3. **Objective Functions & Optimization**: Ordinary Least Squares (OLS), Weighted Least Squares (WLS), Maximum Likelihood Estimation (MLE), Gauss-Newton, and Levenberg-Marquardt algorithms.
4. **Global Optimization**: Multi-start L-BFGS-B, Differential Evolution, and handling rugged multimodal objective landscapes.
5. **Local Sensitivity Analysis (LSA)**: Normalized sensitivity coefficients and the forward sensitivity differential equations.
6. **Global Sensitivity Analysis (GSA)**: Morris elementary effects screening, Sobol variance decomposition (first-order $S_i$ vs total-order $S_{Ti}$), and detecting non-linear parameter interactions.

---

## 2. Model Calibration, Verification & Validation

In pharmaceutical consulting and regulatory submissions (FDA/EMA MIDD), mixing up these three terms is a major red flag:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    THE MODEL CREDIBILITY TRIAD (ASME V&V 40)                │
├────────────────────┬────────────────────────────────────────────────────────┤
│ 1. MODEL           │ "Are we solving the equations right?"                  │
│    VERIFICATION    │ • Numerical error estimation (grid/time-step convergence)│
│                    │ • Benchmarking against analytical solutions             │
│                    │ • Checking code syntax, mass/charge conservation       │
├────────────────────┼────────────────────────────────────────────────────────┤
│ 2. MODEL           │ "Can we find parameter values that fit training data?" │
│    CALIBRATION     │ • Estimating unknown kinetic parameters from in vitro, │
│                    │   pre-clinical, or clinical trial measurements         │
│                    │ • Minimizing residual objective functions with bounds   │
├────────────────────┼────────────────────────────────────────────────────────┤
│ 3. MODEL           │ "Are we solving the right real-world equations?"       │
│    VALIDATION      │ • Testing calibrated model predictions against         │
│                    │   INDEPENDENT, UNSEEN datasets (e.g., higher doses,   │
│                    │   different patient cohorts, combination therapy)     │
│                    │ • Never validate on the same data used for calibration! │
└────────────────────┴────────────────────────────────────────────────────────┘
```

---

## 3. Parameter Identifiability Theory

Before launching an optimization algorithm, a modeler must ask: *Can these parameters be uniquely recovered from the available measurements?*

### 3.1 Structural (A Priori) Identifiability
A parameter vector $\mathbf{p}$ is **structurally identifiable** if, under the ideal assumption of infinite, continuous, noise-free observation data, distinct parameter values yield distinct model outputs:
$$\mathbf{y}(t, \mathbf{p}_1) = \mathbf{y}(t, \mathbf{p}_2) \ \forall t \ge 0 \implies \mathbf{p}_1 = \mathbf{p}_2$$

#### The Laplace Transform Method for Linear Systems:
Consider a 1-compartment IV bolus model:
$$\frac{dC}{dt} = -k_e C, \quad C(0) = \frac{\text{Dose}}{V_d}$$
where the measured output is plasma concentration $y(t) = C(t)$.

Taking the Laplace transform:
$$s \hat{C}(s) - C(0) = -k_e \hat{C}(s) \implies \hat{C}(s) = \frac{C(0)}{s + k_e} = \frac{\text{Dose} / V_d}{s + k_e}$$

The observed transfer function is characterized by:
* Coefficient of $s^0$ in denominator: $\phi_1 = k_e$
* Coefficient in numerator: $\phi_2 = \frac{\text{Dose}}{V_d} \implies V_d = \frac{\text{Dose}}{\phi_2}$

Since $k_e$ and $V_d$ can be solved uniquely from $\phi_1$ and $\phi_2$, both parameters are **structurally identifiable**.

*Counter-Example (Unidentifiable Model)*:
If only the total amount in the body $A(t)$ is measured, but $C(t) = A(t)/V_d$ is observed without knowing $\text{Dose}$, then $V_d$ cannot be disentangled from the input, causing a structural identifiability failure.

### 3.2 Practical (A Posteriori) Identifiability
A parameter is **practically unidentifiable** if, despite being structurally identifiable, the available experimental data is too noisy, sparse, or poorly sampled to constrain the parameter to a finite confidence interval.

#### Diagnostics for Practical Identifiability:
1. **Fisher Information Matrix (FIM)**:
   $$\mathbf{FIM} = \mathbf{J}^T \mathbf{W} \mathbf{J}$$
   where $\mathbf{J}_{ij} = \frac{\partial y(t_i)}{\partial p_j}$ is the sensitivity matrix and $\mathbf{W}$ is the measurement weighting matrix.
   * If $\det(\mathbf{FIM}) \approx 0$ or condition number $\kappa(\mathbf{FIM}) > 10^8$, strong collinearity exists between parameters!
2. **Profile Likelihood Analysis (Raue et al.)**:
   To profile parameter $p_j$, fix $p_j$ over a grid of values and re-optimize all other parameters $\mathbf{p}_{\sim j}$:
   $$\chi^2_{PL}(p_j) = \min_{\mathbf{p}_{\sim j}} \chi^2(p_j, \mathbf{p}_{\sim j})$$
   * **Practically Identifiable**: $\chi^2_{PL}(p_j)$ forms a steep convex parabola exceeding the $\chi^2_{\alpha, 1}$ threshold on both sides.
   * **Practically Unidentifiable**: $\chi^2_{PL}(p_j)$ is flat or fails to cross the threshold in one direction (infinite confidence interval!).

---

## 4. Parameter Estimation & Nonlinear Optimization

### 4.1 Objective Functions
Let $y_i^{exp}$ be experimental observations at timepoints $t_i$ ($i = 1, \dots, N$), and $y(t_i, \mathbf{p})$ be the model prediction.

1. **Ordinary Least Squares (OLS)**:
   $$\Phi(\mathbf{p}) = \sum_{i=1}^N \left( y_i^{exp} - y(t_i, \mathbf{p}) \right)^2$$
   *Valid only when measurement noise is independent, normally distributed, and homoscedastic (constant variance $\sigma^2$ across all concentrations).*
2. **Weighted Least Squares (WLS)**:
   In biological pharmacokinetic data, concentrations span orders of magnitude ($1000\text{ mg/L}$ at peak down to $1\text{ mg/L}$ at trough). OLS completely ignores the trough points!
   $$\Phi_{WLS}(\mathbf{p}) = \sum_{i=1}^N w_i \left( y_i^{exp} - y(t_i, \mathbf{p}) \right)^2$$
   *Standard Weighting Schemes*:
   * Relative weighting: $w_i = \frac{1}{(y_i^{exp})^2}$ (constant coefficient of variation).
   * Model-based weighting: $w_i = \frac{1}{(y(t_i, \mathbf{p}))^2}$.

### 4.2 The Levenberg-Marquardt (LM) Algorithm
The Levenberg-Marquardt algorithm interpolates between the **Gauss-Newton method** and the method of **Gradient Descent**:
$$(\mathbf{J}^T \mathbf{W} \mathbf{J} + \lambda \mathbf{I}) \Delta \mathbf{p} = \mathbf{J}^T \mathbf{W} \mathbf{r}$$
where $\mathbf{r} = \mathbf{y}^{exp} - \mathbf{y}(\mathbf{p})$ is the residual vector and $\lambda \ge 0$ is the damping parameter.
* When $\lambda$ is large: $\Delta \mathbf{p} \approx \frac{1}{\lambda} \mathbf{J}^T \mathbf{W} \mathbf{r}$ (steepest descent; guaranteed descent step when far from the minimum).
* When $\lambda$ is small: $\Delta \mathbf{p} \approx (\mathbf{J}^T \mathbf{W} \mathbf{J})^{-1} \mathbf{J}^T \mathbf{W} \mathbf{r}$ (quadratic Gauss-Newton; rapid second-order convergence near the minimum).

### 4.3 Residual Diagnostics
After calibration, a Scientist 2 modeler must inspect the residuals $r_i = y_i^{exp} - y(t_i, \hat{\mathbf{p}})$:
1. **Normality**: Quantile-Quantile (Q-Q) plot should lie on a 45-degree straight line.
2. **Homoscedasticity**: Standardized residuals plotted against predicted values must show an even band centered at zero, without funnel shapes.
3. **Autocorrelation (Runs Test)**: Residuals must not exhibit consecutive runs of positive or negative signs, which indicates structural model misspecification!

---

## 5. Local Sensitivity Analysis (LSA)

### 5.1 Normalized Sensitivity Coefficients
Local sensitivity evaluates how small perturbations in parameter $p_j$ affect output $y_i(t)$ around a baseline parameter set $\mathbf{p}_0$:
$$S_{ij}(t) = \frac{\partial y_i(t)}{\partial p_j} \cdot \frac{p_j}{y_i(t)} = \frac{\partial \ln y_i(t)}{\partial \ln p_j}$$
* *Interpretation*: An $S_{ij} = +1.5$ means that a **1% increase** in parameter $p_j$ causes a **1.5% increase** in state $y_i(t)$ at time $t$.
* *Invariance*: Because it is normalized by nominal values, $S_{ij}$ is dimensionless, allowing direct ranking between parameters with different physical units (e.g., comparing clearance $CL$ in $\text{L/h}$ against volume $V_d$ in $\text{L}$).

### 5.2 The Forward Sensitivity Differential Equations
Rather than using noisy finite differences, exact sensitivities are computed by differentiating the ODE system $\dot{\mathbf{y}} = \mathbf{f}(t, \mathbf{y}, \mathbf{p})$ with respect to parameter $p_j$:
$$\frac{d}{dt}\left(\frac{\partial \mathbf{y}}{\partial p_j}\right) = \mathbf{J}_y(t) \left(\frac{\partial \mathbf{y}}{\partial p_j}\right) + \frac{\partial \mathbf{f}}{\partial p_j}, \quad \frac{\partial \mathbf{y}}{\partial p_j}(0) = \frac{\partial \mathbf{y}_0}{\partial p_j}$$
where $\mathbf{J}_y = \frac{\partial \mathbf{f}}{\partial \mathbf{y}}$ is the system Jacobian. This coupled system of $n \times m$ sensitivity ODEs is integrated concurrently with the model state equations.

---

## 6. Global Sensitivity Analysis (GSA)

### 6.1 Why Local Sensitivity Fails in Biology
Local sensitivity evaluates derivatives at a single point $\mathbf{p}_0$. However, biological parameters vary across patients by 100% to 500%! In nonlinear systems, derivatives change dramatically across the physiological parameter space.

### 6.2 Morris Screening (Elementary Effects Method)
Morris screening is an efficient qualitative GSA method to classify parameters into:
1. Non-influential parameters.
2. Parameters with large linear effects without interactions.
3. Parameters with high non-linear effects and/or extensive interactions.

For parameter $i$, the elementary effect along a trajectory is:
$$EE_i(\mathbf{p}) = \frac{Y(p_1, \dots, p_i + \Delta, \dots, p_k) - Y(\mathbf{p})}{\Delta}$$

Over $R$ trajectories:
* **Absolute Mean**: $\mu_i^* = \frac{1}{R} \sum_{r=1}^R |EE_i^r|$ (Overall importance / influence).
* **Standard Deviation**: $\sigma_i = \sqrt{\frac{1}{R-1} \sum_{r=1}^R (EE_i^r - \mu_i)^2}$ (Degree of nonlinearity and parameter interactions).

### 6.3 Sobol Variance-Based Sensitivity Decomposition
Sobol analysis decomposes the total variance of model output $Y$ into fractions attributed to individual parameters and parameter combinations:
$$\text{Var}(Y) = \sum_{i=1}^k V_i + \sum_{i < j}^k V_{ij} + \dots + V_{1, \dots, k}$$

1. **First-Order Sensitivity Index ($S_i$, Main Effect)**:
   $$S_i = \frac{V_i}{\text{Var}(Y)} = \frac{\text{Var}_{p_i}\left(\mathbb{E}_{\mathbf{p}_{\sim i}}[Y \mid p_i]\right)}{\text{Var}(Y)}$$
   *Represents the expected percentage reduction in output variance if parameter $p_i$ were fixed to its true value.*
2. **Total-Order Sensitivity Index ($S_{Ti}$, Total Effect)**:
   $$S_{Ti} = 1 - \frac{\text{Var}_{\mathbf{p}_{\sim i}}\left(\mathbb{E}_{p_i}[Y \mid \mathbf{p}_{\sim i}]\right)}{\text{Var}(Y)}$$
   *Represents the fraction of output variance caused by parameter $p_i$, including its main effect and ALL interactions with other parameters!*
3. **Quantifying Parameter Interactions**:
   $$\text{Interaction Index} = S_{Ti} - S_i$$
   * If $S_{Ti} \approx S_i$: The parameter acts purely additively without interacting with others.
   * If $S_{Ti} \gg S_i$: The parameter is involved in strong non-linear coupling (e.g., feedback loops, complex formation).

---

## 7. Worked Mathematical Problems

### Problem 3.1: Analytical Derivation of Normalized Sensitivity for a 1-Compartment PK Model
**Question**: Plasma concentration following an IV bolus injection of dose $D$ is given by:
$$C(t) = \frac{D}{V_d} e^{-\frac{CL}{V_d} t}$$
1. Analytically derive the normalized local sensitivity coefficients with respect to clearance ($S_{CL}(t)$) and volume of distribution ($S_{V_d}(t)$).
2. Plot/interpret their values at $t = 0$ and $t = t_{1/2} = \frac{V_d \ln 2}{CL}$.

#### Solution:
**Step 1: Sensitivity with respect to Clearance ($CL$)**
$$\frac{\partial C}{\partial CL} = \frac{D}{V_d} \left( -\frac{t}{V_d} \right) e^{-\frac{CL}{V_d} t} = -\frac{t}{V_d} C(t)$$

Normalize by multiplying by $\frac{CL}{C(t)}$:
$$S_{CL}(t) = \frac{\partial C}{\partial CL} \cdot \frac{CL}{C(t)} = \left( -\frac{t}{V_d} C(t) \right) \frac{CL}{C(t)} = \mathbf{-\frac{CL}{V_d} t = -k_e t}$$

**Step 2: Sensitivity with respect to Volume of Distribution ($V_d$)**
$$C(t) = D V_d^{-1} e^{-CL V_d^{-1} t}$$
Using the product rule:
$$\frac{\partial C}{\partial V_d} = -D V_d^{-2} e^{-\frac{CL}{V_d} t} + \frac{D}{V_d} e^{-\frac{CL}{V_d} t} \left( \frac{CL t}{V_d^2} \right) = -\frac{1}{V_d} C(t) + \frac{CL t}{V_d^2} C(t) = \frac{C(t)}{V_d} \left( \frac{CL t}{V_d} - 1 \right)$$

Normalize by multiplying by $\frac{V_d}{C(t)}$:
$$S_{V_d}(t) = \frac{\partial C}{\partial V_d} \cdot \frac{V_d}{C(t)} = \mathbf{\frac{CL}{V_d} t - 1 = k_e t - 1}$$

**Step 3: Biological Interpretation at Key Timepoints**
* **At $t = 0$ (Peak / Dose administration)**:
  * $S_{CL}(0) = 0.0$. *(Clearance has zero effect on peak concentration $C_0 = D/V_d$)*.
  * $S_{V_d}(0) = -1.0$. *(A 1% increase in volume of distribution causes exactly a 1% reduction in $C_0$)*.
* **At $t = t_{1/2} = \frac{\ln 2}{k_e} \approx 0.693 / k_e$**:
  * $S_{CL}(t_{1/2}) = -\ln 2 \approx \mathbf{-0.693}$. *(A 1% increase in clearance reduces half-life concentration by 0.693%)*.
  * $S_{V_d}(t_{1/2}) = \ln 2 - 1 \approx 0.693 - 1 = \mathbf{-0.307}$.
* **At $t = \frac{1}{k_e}$ ($t = \text{mean residence time}$)**:
  * $S_{V_d}(1/k_e) = 1 - 1 = \mathbf{0.0}$!
  * *Critical Scientist 2 Finding*: At $t = 1/k_e$, plasma concentration is completely **insensitive** to volume of distribution! Sampling blood at this exact point isolates clearance from volume!

---

### Problem 3.2: Parameter Identifiability Failure in Two-Step Metabolic Cascades
**Question**: An intracellular metabolite cascade is modeled as:
$$\frac{dx_1}{dt} = -k_1 x_1, \quad x_1(0) = x_{10}$$
$$\frac{dx_2}{dt} = k_1 x_1 - k_2 x_2, \quad x_2(0) = 0$$
Only the downstream metabolite $y(t) = x_2(t)$ is measured. Show whether parameters $k_1$ and $k_2$ are structurally identifiable.

#### Solution:
Take Laplace transforms:
$$s \hat{x}_1(s) - x_{10} = -k_1 \hat{x}_1(s) \implies \hat{x}_1(s) = \frac{x_{10}}{s + k_1}$$
$$s \hat{x}_2(s) - 0 = k_1 \hat{x}_1(s) - k_2 \hat{x}_2(s) \implies (s + k_2) \hat{x}_2(s) = k_1 \left(\frac{x_{10}}{s + k_1}\right)$$
$$\hat{y}(s) = \hat{x}_2(s) = \frac{k_1 x_{10}}{(s + k_1)(s + k_2)} = \frac{k_1 x_{10}}{s^2 + (k_1 + k_2) s + k_1 k_2}$$

The observable transfer function coefficients are:
1. Numerator: $\phi_1 = k_1 x_{10}$
2. Denominator $s^1$ coefficient: $\phi_2 = k_1 + k_2$
3. Denominator $s^0$ coefficient: $\phi_3 = k_1 k_2$

If $x_{10}$ is known:
From $\phi_1$, $k_1 = \phi_1 / x_{10}$. Then $k_2 = \phi_2 - k_1$. Both parameters are **globally identifiable**.

**The Identifiability Failure (Unknown $x_{10}$)**:
If initial concentration $x_{10}$ is unknown, we only have $\phi_2 = k_1 + k_2$ and $\phi_3 = k_1 k_2$.
By Vieta's formulas, $k_1$ and $k_2$ are the roots of the symmetric quadratic polynomial:
$$\lambda^2 - \phi_2 \lambda + \phi_3 = 0$$
$$\{k_1, k_2\} = \frac{\phi_2 \pm \sqrt{\phi_2^2 - 4\phi_3}}{2}$$

*Scientist 2 Diagnostic*:
Because of the mathematical symmetry between $k_1$ and $k_2$, the model output $x_2(t)$ is identical whether $(k_1=0.1, k_2=1.0)$ or $(k_1=1.0, k_2=0.1)$!
This is a **two-fold discrete structural unidentifiability (flip-flop phenomenon)**. It can only be resolved by independently measuring $x_1(t)$ or measuring the initial dose $x_{10}$.
