# Project 5: Interview Defense & Technical Q&A

**Candidate Defense Readiness:** Constrained Optimization & Prescriptive Intelligence  
**Role:** Data Scientist / Associate Data Scientist | Tredence Analytics

---

### Q1. What is the fundamental difference between Predictive Analytics and Prescriptive Analytics?
**Defense:**  
- **Predictive Analytics:** Answers *"What will happen?"* It forecasts consumer demand, customer churn probabilities, or equipment failure times given historical patterns.
- **Prescriptive Analytics:** Answers *"What should we do?"* It ingests the predictions from machine learning models and optimizes decision variables (e.g., promotional discounts, marketing spend, inventory orders) to maximize a business objective (EBITDA, revenue) subject to real-world operational constraints (budget limits, warehouse capacity, regulatory guardrails).
- Prescriptive analytics represents the ultimate milestone in Tredence's "Last-Mile Adoption" methodology.

---

### Q2. What is a "Shadow Price" (Dual Value) in linear programming, and why is it valuable to business executives?
**Defense:**  
- Mathematically, the shadow price $\lambda_i$ of constraint $i$ is the rate of change in the optimal objective value with respect to a unit relaxation of the constraint boundary $b_i$:
  $$\lambda_i = \frac{\partial z^*}{\partial b_i}$$
- **Executive Value:** For the total marketing budget constraint, our model calculated a shadow price of $\$3.80$. This tells the Chief Marketing Officer (CMO) that if leadership allocates an additional $\$100,000$ to the marketing budget, the portfolio will generate exactly $\$380,000$ in incremental revenue before hitting channel saturation caps. It provides direct quantitative justification for capital requests.

---

### Q3. How do you handle non-linear diminishing returns in marketing spend?
**Defense:**  
- Pure linear models assume constant marginal ROI (e.g., spending \$1M in Email continues to yield \$5.50 per dollar). In reality, marketing channels exhibit **diminishing marginal returns** (saturation curves modeled via Michaelis-Menten or Hill equations $R(x) = \frac{V_{\max} x^n}{K^n + x^n}$).
- **Techniques to handle non-linearity:**
  1. **Piecewise Linear Approximation:** Discretize the concave saturation curve into linear segments with decreasing slopes, solvable via Mixed-Integer Linear Programming (MILP).
  2. **Non-Linear Programming (NLP):** Use Sequential Least Squares Programming (SLSQP) or interior-point non-linear solvers with concave objective functions.
  3. **Channel Upper Bounds:** In our LP, we enforced conservative channel caps ($U_i$) to prevent allocating funds beyond the known linear threshold.
