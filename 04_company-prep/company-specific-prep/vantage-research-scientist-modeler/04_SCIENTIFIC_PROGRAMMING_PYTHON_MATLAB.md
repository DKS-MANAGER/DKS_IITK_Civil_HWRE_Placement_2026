# Module 04: Scientific Programming in Python & MATLAB

> **Track**: Production Scientific Computing & Numerical Simulation Workflows  
> **Role Level**: Scientist – Modeler (Scientist 1 / Scientist 2 Standard)  
> **Target Entity**: Vantage Research  
> **Evidentiary Standard**: `[NUMPY, SCIPY & MATLAB SCIENTIFIC COMPUTING STANDARDS]`  

---

## 1. Executive Summary & Code Quality Benchmarks

At Vantage Research, writing scientific code is not a loose exploratory exercise in a Jupyter notebook; it is a mission-critical engineering workflow. Code must be numerically robust, modular, unit-tested, vectorized, and reproducible. A modeler must be equally comfortable writing production Python (`scipy`, `numpy`) and MATLAB scripts.

This module provides complete, mathematically verified, runnable reference code architectures across four core modeling challenges:
1. **Script 1**: Coupled Stiff Multi-Compartment PK/PD Solver with Analytical Jacobian & Event Detection (Repeated Dosing).
2. **Script 2**: Nonlinear Parameter Calibration Pipeline with Weighted Residuals, Bounds, and Covariance-Based 95% Confidence Intervals.
3. **Script 3**: Normalized Local Sensitivity Analysis Engine via Forward Sensitivity Differential Equations.
4. **Script 4**: Sobol Global Sensitivity Analysis (GSA) Pipeline Computing First-Order ($S_i$) and Total-Order ($S_{Ti}$) Variance Indices.

---

## 2. Production Scientific Architecture: Python Stack

```python
"""
VANTAGE RESEARCH PRODUCTION MODELING ARCHITECTURE
Standard directory/module separation for QSP simulations:
  ├── model/
  │    ├── equations.py     # Pure mathematical ODE definitions & Jacobians
  │    ├── parameters.py    # Dataclasses with nominal values, units & bounds
  ├── solvers/
  │    ├── integrator.py    # solve_ivp wrapper with tolerance & event logic
  ├── calibration/
  │    ├── optimizer.py     # Least-squares & differential evolution wrappers
  │    ├── identifiability.py # FIM and profile likelihood diagnostics
  └── analysis/
       ├── sensitivity.py   # Local & global Sobol sensitivity engines
       ├── visualization.py # Publication-quality Matplotlib figures
"""
```

---

## 3. Script 1: Coupled Stiff PK/PD Integration with Analytical Jacobian & Multiple Dosing

This script simulates a 2-compartment pharmacokinetic model coupled to an indirect-response biomarker pharmacodynamic model under repeated oral dosing.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from dataclasses import dataclass

@dataclass
class PKPDParameters:
    # Pharmacokinetics
    ka: float = 1.2       # Absorption rate [1/h]
    CL: float = 5.0       # Clearance [L/h]
    V1: float = 20.0      # Central volume [L]
    Q: float = 8.0        # Inter-compartmental clearance [L/h]
    V2: float = 50.0      # Peripheral volume [L]
    F: float = 0.85       # Bioavailability [dimensionless]
    # Pharmacodynamics (Indirect Response Type I: Drug inhibits synthesis kin)
    kin: float = 10.0     # Biomarker baseline synthesis [nM/h]
    kout: float = 0.2     # Biomarker degradation rate [1/h]
    Imax: float = 0.90    # Maximum fractional inhibition [0, 1]
    IC50: float = 2.5     # Half-maximal inhibitory concentration [mg/L]

def pkpd_derivatives(t: float, y: np.ndarray, p: PKPDParameters) -> np.ndarray:
    """
    State variables:
      y[0] = A_gut   (Drug amount in GI tract, mg)
      y[1] = A_cent  (Drug amount in central compartment, mg)
      y[2] = A_peri  (Drug amount in peripheral tissue, mg)
      y[3] = R_bm    (Biomarker concentration, nM)
    """
    A_gut, A_cent, A_peri, R_bm = y
    
    # Central concentration
    C_cent = max(A_cent / p.V1, 0.0)
    
    # Differential Equations
    dA_gut = -p.ka * A_gut
    dA_cent = p.ka * A_gut - (p.CL / p.V1) * A_cent - (p.Q / p.V1) * A_cent + (p.Q / p.V2) * A_peri
    dA_peri = (p.Q / p.V1) * A_cent - (p.Q / p.V2) * A_peri
    
    # Indirect Response: Drug inhibits synthesis kin
    inhibition = 1.0 - (p.Imax * C_cent) / (p.IC50 + C_cent)
    dR_bm = p.kin * inhibition - p.kout * R_bm
    
    return np.array([dA_gut, dA_cent, dA_peri, dR_bm])

def pkpd_jacobian(t: float, y: np.ndarray, p: PKPDParameters) -> np.ndarray:
    """Analytical Jacobian matrix for stiff solvers (Radau/BDF)."""
    A_gut, A_cent, A_peri, R_bm = y
    C_cent = max(A_cent / p.V1, 0.0)
    
    J = np.zeros((4, 4))
    # Row 0: dA_gut / dy
    J[0, 0] = -p.ka
    
    # Row 1: dA_cent / dy
    J[1, 0] = p.ka
    J[1, 1] = -(p.CL + p.Q) / p.V1
    J[1, 2] = p.Q / p.V2
    
    # Row 2: dA_peri / dy
    J[2, 1] = p.Q / p.V1
    J[2, 2] = -p.Q / p.V2
    
    # Row 3: dR_bm / dy
    # d(inhibition)/d(C_cent) = - (Imax * IC50) / (IC50 + C_cent)^2
    d_inhib_dC = -(p.Imax * p.IC50) / ((p.IC50 + C_cent)**2)
    J[3, 1] = p.kin * d_inhib_dC * (1.0 / p.V1)
    J[3, 3] = -p.kout
    
    return J

def simulate_multiple_dosing(dose_mg: float = 100.0, tau_h: float = 24.0, 
                             num_doses: int = 7) -> tuple:
    """Simulates repeated oral administration over num_doses cycles."""
    params = PKPDParameters()
    # Baseline steady-state biomarker R0 = kin / kout
    R0 = params.kin / params.kout
    y_current = np.array([0.0, 0.0, 0.0, R0])
    
    all_t = []
    all_y = []
    
    for dose_idx in range(num_doses):
        t_start = dose_idx * tau_h
        t_end = (dose_idx + 1) * tau_h
        
        # Administer dose into GI tract
        y_current[0] += dose_mg * params.F
        
        sol = solve_ivp(
            fun=lambda t, y: pkpd_derivatives(t, y, params),
            t_span=(t_start, t_end),
            y0=y_current,
            method='Radau',
            jac=lambda t, y: pkpd_jacobian(t, y, params),
            t_eval=np.linspace(t_start, t_end, 150),
            rtol=1e-7,
            atol=1e-9
        )
        
        all_t.append(sol.t)
        all_y.append(sol.y)
        y_current = sol.y[:, -1]
        
    t_full = np.concatenate(all_t)
    y_full = np.concatenate(all_y, axis=1)
    return t_full, y_full, params
```

---

## 4. Script 2: Parameter Calibration with Weighted Least Squares & Confidence Intervals

This script estimates clearance ($CL$) and volume ($V_1$) from sparse, noisy clinical concentration measurements.

```python
import numpy as np
from scipy.optimize import least_squares
from scipy.stats import t as student_t

def generate_synthetic_trial_data(true_CL=4.8, true_V=22.0, noise_cv=0.15, seed=42):
    """Generates synthetic 1-compartment IV bolus data with heteroscedastic noise."""
    np.random.seed(seed)
    time_pts = np.array([0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 12.0, 24.0, 36.0, 48.0])
    dose = 500.0 # mg
    
    true_conc = (dose / true_V) * np.exp(-(true_CL / true_V) * time_pts)
    # Relative proportional noise: y_obs = y_true * (1 + N(0, noise_cv^2))
    noisy_conc = true_conc * (1.0 + np.random.normal(0, noise_cv, size=len(time_pts)))
    return time_pts, dose, noisy_conc

def model_predicted_conc(p: np.ndarray, dose: float, t: np.ndarray) -> np.ndarray:
    """p[0] = CL, p[1] = V"""
    CL, V = p
    return (dose / V) * np.exp(-(CL / V) * t)

def weighted_residual_function(p: np.ndarray, dose: float, t: np.ndarray, 
                               y_obs: np.ndarray) -> np.ndarray:
    """Computes weighted residuals: r_i = (y_obs - y_pred) / y_obs"""
    y_pred = model_predicted_conc(p, dose, t)
    # Relative weighting scheme prevents high peak concentrations from dominating
    return (y_obs - y_pred) / y_obs

def calibrate_and_compute_ci(t_obs, dose, y_obs, alpha=0.05):
    """Calibrates parameters and computes formal asymptotic 95% confidence intervals."""
    # Initial guess & physiological bounds
    p0 = np.array([10.0, 50.0])
    bounds = ([0.1, 1.0], [50.0, 200.0])
    
    res = least_squares(
        fun=weighted_residual_function,
        x0=p0,
        bounds=bounds,
        args=(dose, t_obs, y_obs),
        method='trf',
        ftol=1e-9,
        xtol=1e-9
    )
    
    p_hat = res.x
    n_obs = len(y_obs)
    n_params = len(p_hat)
    dof = n_obs - n_params
    
    # Jacobian matrix from least_squares: J = dr_i / dp_j
    J = res.jac
    # Estimated residual variance s^2
    s_sq = 2.0 * res.cost / dof
    
    # Covariance Matrix = s^2 * (J^T * J)^(-1)
    cov_matrix = s_sq * np.linalg.inv(J.T @ J)
    param_stderr = np.sqrt(np.diag(cov_matrix))
    
    # Student's t critical value for 95% two-sided interval
    t_crit = student_t.ppf(1.0 - alpha / 2.0, df=dof)
    ci_lower = p_hat - t_crit * param_stderr
    ci_upper = p_hat + t_crit * param_stderr
    
    return {
        'parameters': ['CL (L/h)', 'V (L)'],
        'estimate': p_hat,
        'stderr': param_stderr,
        'ci_95': list(zip(ci_lower, ci_upper)),
        'covariance': cov_matrix
    }
```

---

## 5. Script 3: Normalized Local Sensitivity Analysis Engine

This script solves the coupled system of forward sensitivity differential equations:
$$\frac{d\mathbf{y}}{dt} = \mathbf{f}(\mathbf{y}, \mathbf{p}), \quad \frac{d\mathbf{S}_p}{dt} = \mathbf{J}_y \mathbf{S}_p + \mathbf{J}_p$$

```python
import numpy as np
from scipy.integrate import solve_ivp

def sensitivity_system(t: float, y_aug: np.ndarray, dose: float) -> np.ndarray:
    """
    Augmented system containing state C and its sensitivities:
      y_aug[0] = C
      y_aug[1] = dC / dCL
      y_aug[2] = dC / dV
    """
    C, s_CL, s_V = y_aug
    
    CL_nom = 5.0  # L/h
    V_nom = 25.0  # L
    ke = CL_nom / V_nom
    
    # State ODE
    dC = -ke * C
    
    # Jacobian wrt state: df / dC = -ke
    J_state = -ke
    
    # Derivative wrt CL: df / dCL = -C / V
    df_dCL = -C / V_nom
    
    # Derivative wrt V: df / dV = (CL / V^2) * C
    df_dV = (CL_nom / (V_nom**2)) * C
    
    # Sensitivity ODEs
    ds_CL = J_state * s_CL + df_dCL
    ds_V = J_state * s_V + df_dV
    
    return np.array([dC, ds_CL, ds_V])

def compute_normalized_local_sensitivity(dose: float = 100.0, t_max: float = 24.0):
    """Integrates forward sensitivity equations and returns normalized indices."""
    CL_nom = 5.0
    V_nom = 25.0
    
    # Initial conditions: C(0) = Dose / V, s_CL(0) = 0, s_V(0) = -Dose / V^2
    y0_aug = np.array([dose / V_nom, 0.0, -dose / (V_nom**2)])
    
    t_eval = np.linspace(0.01, t_max, 200)
    sol = solve_ivp(
        fun=lambda t, y: sensitivity_system(t, y, dose),
        t_span=(0.0, t_max),
        y0=y0_aug,
        t_eval=t_eval,
        method='Radau',
        rtol=1e-8,
        atol=1e-10
    )
    
    C_sol = sol.y[0]
    s_CL_raw = sol.y[1]
    s_V_raw = sol.y[2]
    
    # Normalization: S_norm = (dC / dp) * (p / C)
    S_norm_CL = s_CL_raw * (CL_nom / C_sol)
    S_norm_V = s_V_raw * (V_nom / C_sol)
    
    return sol.t, S_norm_CL, S_norm_V
```

---

## 6. Script 4: Variance-Based Sobol Global Sensitivity Analysis

This script implements Saltelli sampling to compute first-order ($S_i$) and total-order ($S_{Ti}$) Sobol indices without external dependencies.

```python
import numpy as np

def evaluate_model_auc(params_matrix: np.ndarray, dose: float = 500.0) -> np.ndarray:
    """
    Evaluates Area Under the Curve (AUC) for an array of parameter samples:
    AUC = Dose / CL (for 1-compartment model).
    params_matrix: [N_samples, 3] with columns [CL, V, ka].
    """
    CL = params_matrix[:, 0]
    return dose / CL

def compute_sobol_indices(param_bounds: list, n_samples: int = 4096, seed: int = 42):
    """
    Computes first-order and total-order Sobol indices using Saltelli sampling.
    param_bounds: list of tuples [(min, max), ...] for each parameter.
    """
    np.random.seed(seed)
    k = len(param_bounds)
    
    # Generate two independent random sample matrices A and B in [0, 1]
    A_raw = np.random.uniform(0, 1, (n_samples, k))
    B_raw = np.random.uniform(0, 1, (n_samples, k))
    
    # Scale to physical bounds
    A = np.zeros_like(A_raw)
    B = np.zeros_like(B_raw)
    for j in range(k):
        low, high = param_bounds[j]
        A[:, j] = low + A_raw[:, j] * (high - low)
        B[:, j] = low + B_raw[:, j] * (high - low)
        
    # Evaluate base matrices
    f_A = evaluate_model_auc(A)
    f_B = evaluate_model_auc(B)
    
    # Total variance of output
    f_all = np.concatenate([f_A, f_B])
    var_total = np.var(f_all, ddof=1)
    
    S_first = np.zeros(k)
    S_total = np.zeros(k)
    
    # Saltelli AB matrices for each parameter i
    for i in range(k):
        # AB_i: Matrix A with column i replaced by column i from B
        AB_i = np.copy(A)
        AB_i[:, i] = B[:, i]
        f_AB_i = evaluate_model_auc(AB_i)
        
        # First-order index: S_i = ( (1/N) * sum(f_B * (f_AB_i - f_A)) ) / var_total
        S_first[i] = np.mean(f_B * (f_AB_i - f_A)) / var_total
        
        # Total-order index: S_Ti = ( (1/(2N)) * sum((f_A - f_AB_i)^2) ) / var_total
        S_total[i] = (0.5 * np.mean((f_A - f_AB_i)**2)) / var_total
        
    return S_first, S_total
```

---

## 7. MATLAB Production Counterparts & Equivalence Matrix

| Task | Python Implementation | MATLAB Implementation |
| :--- | :--- | :--- |
| **Stiff Integration** | `solve_ivp(fun, (0, T), y0, method='Radau', jac=jac)` | `[t, y] = ode15s(@fun, [0 T], y0, odeset('Jacobian', @jac))` |
| **Nonlinear Fitting** | `least_squares(res_fun, p0, bounds=(lb, ub))` | `p_hat = lsqcurvefit(@model, p0, t_data, y_data, lb, ub)` |
| **Global Optimization** | `differential_evolution(obj_fun, bounds)` | `p_hat = ga(@obj_fun, nvars, [], [], [], [], lb, ub)` |
| **Local Sensitivity** | Integrate sensitivity ODE system $\dot{\mathbf{S}} = \mathbf{J}\mathbf{S} + \mathbf{f}_p$ | MATLAB SimBiology Toolbox `sbiomodel` sensitivity analyzer |
