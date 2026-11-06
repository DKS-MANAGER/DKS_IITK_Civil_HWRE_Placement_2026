# Module 13: Linear & Non-Linear Optimization Techniques

> **Document Status**: Production-Grade Applied Reference `[TIER 4 / MATHEMATICAL PROGRAMMING & INFORMS STANDARDS]`  
> **Core Focus**: Linear Programming (Simplex, Duality, Shadow Prices), Non-Linear Optimization (KKT Conditions, SLSQP), and Commercial Allocation Algorithms  
> **Target Role**: Analyst (IQVIA India)  

---

## 1. Mathematical Optimization in Commercial Strategy

Commercial decision-making at IQVIA is fundamentally constrained resource allocation: biopharma clients possess finite promotional budgets, a fixed headcount of sales representatives, and contractual channel boundaries, yet seek to maximize top-line prescription revenue.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    THE GENERAL OPTIMIZATION PROBLEM MATRIX                  │
│                                                                             │
│ Minimize or Maximize:   f(x)                   (Objective Function)         │
│ Subject to:             g_i(x) <= 0,  i=1..m   (Inequality Constraints)     │
│                         h_j(x)  = 0,  j=1..p   (Equality Constraints)       │
│                         l_k <= x_k <= u_k      (Decision Variable Bounds)   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Linear Programming (LP): Formulation, Simplex & Duality

### 2.1 Standard Primal Formulation
$$\max_{\mathbf{x}} \quad Z = \mathbf{c}^T \mathbf{x}$$
$$\text{subject to} \quad \mathbf{A}\mathbf{x} \le \mathbf{b}, \qquad \mathbf{x} \ge \mathbf{0}$$
where $\mathbf{x} \in \mathbb{R}^n$ represents decision variables (e.g., number of sales rep detailing calls allocated per region), $\mathbf{c} \in \mathbb{R}^n$ represents unit revenue contribution, and $\mathbf{A} \in \mathbb{R}^{m \times n}$ represents resource consumption across $m$ operational boundaries (e.g., total sales rep hours, travel capacity, budget limits).

### 2.2 The Simplex Method Mechanics
1. **Geometry**: The feasible region defined by $\mathbf{A}\mathbf{x} \le \mathbf{b}, \mathbf{x} \ge \mathbf{0}$ forms a convex polyhedron. The Fundamental Theorem of Linear Programming guarantees that if an optimal solution exists, it occurs at an **extreme point (vertex)** of the polyhedron.
2. **Algebraic Basis**: Simplex transforms inequalities into equalities via slack variables ($\mathbf{x}_s \ge \mathbf{0}$), partitions variables into basic ($\mathbf{x}_B$) and non-basic ($\mathbf{x}_N$), and pivots along adjacent edges where the reduced cost ($\bar{c}_j = c_j - \mathbf{c}_B^T \mathbf{B}^{-1}\mathbf{A}_j$) is strictly positive.

### 2.3 Duality Theory & Shadow Prices (Economic Interpretation)
Every primal linear program has an associated dual problem:
$$\min_{\mathbf{y}} \quad W = \mathbf{b}^T \mathbf{y} \qquad \text{subject to} \quad \mathbf{A}^T \mathbf{y} \ge \mathbf{c}, \quad \mathbf{y} \ge \mathbf{0}$$

* **Economic Meaning of Dual Variables ($y_i$) — Shadow Price**:
  $$y_i^* = \frac{\partial Z^*}{\partial b_i}$$
  $y_i^*$ represents the exact marginal increase in total brand revenue achieved by increasing resource capacity $b_i$ by one unit.
  * *Commercial Example*: If the shadow price for the Q3 digital marketing budget constraint is $\$3.40$, spending one additional dollar on digital promotion will yield $\$3.40$ in incremental brand revenue. If the shadow price is $\$0.00$, that budget constraint is non-binding (surplus slack exists; additional spend would be wasted).

---

## 3. Non-Linear Optimization & Karush-Kuhn-Tucker (KKT) Conditions

Because marketing returns saturate via concave S-curves (Hill function / logarithmic decay), commercial budget optimization problems are intrinsically non-linear.

### 3.1 Convexity & Hessian Matrix
A twice-differentiable function $f(\mathbf{x})$ is convex on a convex set iff its Hessian matrix $\mathbf{H} = \nabla^2 f(\mathbf{x})$ is **positive semi-definite** ($\mathbf{v}^T \mathbf{H} \mathbf{v} \ge 0$ for all $\mathbf{v} \neq \mathbf{0}$):
$$\mathbf{H}_{ij} = \frac{\partial^2 f}{\partial x_i \partial x_j}$$
* For concave revenue maximization ($\max R(\mathbf{x}) \iff \min -R(\mathbf{x})$), negative revenue is strictly convex, guaranteeing that any local optimum is the unique **global optimum**.

### 3.2 Karush-Kuhn-Tucker (KKT) First-Order Necessary Conditions
For the problem $\min f(\mathbf{x})$ subject to $g_i(\mathbf{x}) \le 0$ and $h_j(\mathbf{x}) = 0$:
1. **Stationarity**: $\nabla f(\mathbf{x}^*) + \sum_{i=1}^{m} \mu_i \nabla g_i(\mathbf{x}^*) + \sum_{j=1}^{p} \lambda_j \nabla h_j(\mathbf{x}^*) = \mathbf{0}$
2. **Primal Feasibility**: $g_i(\mathbf{x}^*) \le 0 \quad \forall i, \qquad h_j(\mathbf{x}^*) = 0 \quad \forall j$
3. **Dual Feasibility**: $\mu_i \ge 0 \quad \forall i$
4. **Complementary Slackness**: $\mu_i g_i(\mathbf{x}^*) = 0 \quad \forall i$ (Either the constraint is active $g_i(\mathbf{x}^*) = 0$, or its multiplier $\mu_i = 0$).

---

## 4. Python Implementation: Linear & Non-Linear Commercial Solvers

### 4.1 Part A: Linear Programming via `scipy.optimize.linprog`
* **Problem**: Allocate sales rep detailing capacity across 3 physician specialty segments (Cardiologists, Oncologists, Primary Care) to maximize revenue under total rep time and compliance call limits.

```python
"""
Part A: Linear Programming Allocation using High-Performance HiGHS Solver
"""
import numpy as np
from scipy.optimize import linprog

# Objective: Maximize Revenue = 450*x_cardio + 850*x_onco + 250*x_pce
# linprog minimizes by default, so invert signs
c = [-450, -850, -250]

# Constraints: A_ub * x <= b_ub
# 1. Total Sales Rep Hours: 2.0*x_cardio + 3.5*x_onco + 1.2*x_pce <= 10,000 hours
# 2. Maximum Budget for Samples/Collateral: 40*x_cardio + 90*x_onco + 20*x_pce <= $250,000
A_ub = [
    [2.0, 3.5, 1.2],
    [40.0, 90.0, 20.0]
]
b_ub = [10000, 250000]

# Bounds: Minimum detailing calls mandated by client contracts
bounds = [
    (500, 3000),   # Cardio calls
    (300, 2000),   # Onco calls
    (1000, 6000)   # Primary Care calls
]

# Solve using modern HiGHS simplex/interior-point engine
res_lp = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

print("="*65)
print("             LINEAR PROGRAMMING SFE ALLOCATION RESULT")
print("="*65)
print(f"Status: {res_lp.message}")
print(f"Optimal Calls - Cardiology   : {res_lp.x[0]:10.1f}")
print(f"Optimal Calls - Oncology     : {res_lp.x[1]:10.1f}")
print(f"Optimal Calls - Primary Care : {res_lp.x[2]:10.1f}")
print(f"Maximum Net Revenue Achieved : ${-res_lp.fun:10,.2f}")
```

### 4.2 Part B: Non-Linear Constrained Budget Optimization via `SLSQP`
* **Problem**: Allocate an \$8M brand marketing budget across 4 promotional channels with diminishing return Hill saturation curves.

```python
"""
Part B: Non-Linear Constrained Optimization via SLSQP
"""
import numpy as np
from scipy.optimize import minimize

total_budget = 8_000_000.0  # $8.0 Million Total Brand Spend

# Channel Parameters: Max Potential ($), Half-Saturation K ($), Slope S
channels = {
    'Field Detailing': {'max_rev': 14_000_000, 'K': 3_500_000, 'S': 1.1},
    'Digital Emails':  {'max_rev':  4_500_000, 'K':   800_000, 'S': 0.9},
    'Display Media':   {'max_rev':  3_000_000, 'K':   600_000, 'S': 0.8},
    'Congress Events': {'max_rev':  5_000_000, 'K': 1_200_000, 'S': 1.2}
}
channel_names = list(channels.keys())

def total_portfolio_revenue(spends):
    """Calculates total revenue across all 4 saturating channels."""
    rev = 0.0
    for i, name in enumerate(channel_names):
        p = channels[name]
        x = spends[i]
        # Hill Saturation Function
        channel_rev = p['max_rev'] * (x ** p['S']) / (p['K'] ** p['S'] + x ** p['S'])
        rev += channel_rev
    return rev

# Objective to minimize: Negative Revenue
objective = lambda s: -total_portfolio_revenue(s)

# Constraints & Bounds
budget_constraint = {'type': 'eq', 'fun': lambda s: np.sum(s) - total_budget}
# Each channel must receive between $200k and $5M
bounds = [(200_000, 5_000_000) for _ in range(4)]
initial_guess = [total_budget / 4.0] * 4

# Execute Sequential Least Squares Programming (SLSQP)
res_nlp = minimize(
    objective, 
    initial_guess, 
    method='SLSQP', 
    bounds=bounds, 
    constraints=budget_constraint,
    options={'ftol': 1e-6, 'disp': False}
)

print("\n" + "="*65)
print("             NON-LINEAR MARKETING ALLOCATION (SLSQP)")
print("="*65)
for i, name in enumerate(channel_names):
    allocated = res_nlp.x[i]
    share = (allocated / total_budget) * 100
    print(f"{name:18}: ${allocated:10,.2f} ({share:5.1f}% of total budget)")
print(f"\nTotal Budget Allocated: ${np.sum(res_nlp.x):10,.2f}")
print(f"Maximized Revenue     : ${-res_nlp.fun:10,.2f}")
```

