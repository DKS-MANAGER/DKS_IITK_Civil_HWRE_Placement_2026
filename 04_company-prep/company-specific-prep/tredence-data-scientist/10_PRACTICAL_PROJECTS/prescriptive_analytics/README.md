# Project 5: Prescriptive Marketing Budget Allocation & Constrained Optimization

**Domain:** Enterprise Marketing Analytics & Prescriptive Decision Intelligence  
**Stack:** Python, NumPy, SciPy (`scipy.optimize.linprog`), Pandas  
**Focus:** Linear Programming (LP), Simplex / Interior-Point, Shadow Prices, Sensitivity Analysis

---

## 1. Project Overview

Predictive models forecast outcomes (e.g., predicting customer conversion probability or demand); **prescriptive models decide the optimal commercial action** under finite operational constraints.

This project formulates and solves an omnichannel marketing budget allocation problem for a CPG brand allocating a $\$1,000,000$ quarterly promotional budget across 5 channels.

### Mathematical Formulation:
$$\max_{\mathbf{x}} \sum_{i=1}^5 R_i \cdot x_i$$
Subject to:
1. **Total Budget:** $\sum_{i=1}^5 x_i \le \$1,000,000$
2. **Digital Mandate:** $x_{\text{Search}} + x_{\text{Social}} + x_{\text{Email}} \ge 0.60 \times \sum x_i$
3. **Channel Guardrails:** $L_i \le x_i \le U_i \quad \forall i$
4. **Non-negativity:** $x_i \ge 0$

---

## 2. File Structure

- `optimize_marketing_budget.py`: Fully reproducible Python script formulating and solving the LP using `scipy.optimize.linprog`, extracting optimal allocations and shadow prices (dual values).
- `interview_defense.md`: Technical defense explaining linear programming, interior-point methods, shadow prices, and the Tredence "Last-Mile" adoption loop.
