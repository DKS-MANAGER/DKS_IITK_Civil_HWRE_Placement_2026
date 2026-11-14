# Machine Learning Interpretability, XAI, and TreeSHAP

**Target Role:** Data Scientist / Associate Data Scientist | Tredence Analytics  
**Context:** IIT Kanpur Placement Season 2026–27  
**Prerequisites:** Game Theory, Tree Ensembles, Vector Calculus

---

## 1. The Explainability Imperative in Enterprise AI

In enterprise consulting (the core of Tredence's "Last-Mile Adoption" mission), high predictive performance ($\text{AUC} > 0.90$) is insufficient. Business leaders (e.g., Chief Commercial Officers, VP Supply Chain) reject black-box models because:
1. **Regulatory Compliance:** Fair lending, non-discriminatory hiring, GDPR "Right to Explanation".
2. **Actionability ("Now What?"):** Knowing an account will churn is useless unless the model explains *why* (e.g., price increase vs service outage) so the frontline account manager can choose the correct retention lever.
3. **Debugging & Model Trust:** Catching spurious correlations, leakage, or racial/geographic biases before deployment.

---

## 2. Global vs Local Interpretability

- **Global Interpretability:** Understanding overall model behavior across the entire population (e.g., "Which 5 features drive 80% of revenue predictions across all stores?").
- **Local Interpretability:** Explaining why the model made a specific prediction for a single individual record (e.g., "Why was Customer #48,201 flagged as high churn risk with probability 0.84?").

---

## 3. Cooperative Game Theory & Shapley Values

Developed by Lloyd Shapley (Nobel Memorial Prize, 1953), Shapley values allocate total payout among players in a coalitional game based on their marginal contributions.

### 3.1 The 4 Foundational Axioms
Any valid additive attribution method must satisfy:
1. **Efficiency (Local Accuracy):** Attributions sum to the difference between model output and expected baseline:
   $$\sum_{i=1}^M \phi_i(x) = f(x) - \mathbb{E}[f(X)]$$
2. **Symmetry:** If two features $i$ and $j$ contribute identically to all possible subsets $S$:
   $$f(S \cup \{i\}) = f(S \cup \{j\}) \implies \phi_i = \phi_j$$
3. **Dummy (Null Player):** If feature $i$ contributes nothing to any subset $S$:
   $$f(S \cup \{i\}) = f(S) \implies \phi_i = 0$$
4. **Additivity:** For an ensemble model $f(x) = g(x) + h(x)$, attributions add directly:
   $$\phi_i(f) = \phi_i(g) + \phi_i(h)$$

**The Classic Shapley Value Formulation:**
$$\phi_i(x) = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|!(|F| - |S| - 1)!}{|F|!} \left[f(S \cup \{i\}) - f(S)\right]$$
Where $F$ is the complete set of features, and $S$ is a subset excluding feature $i$.

---

## 4. TreeSHAP: Exact Fast Tree Attribution

Computing model-agnostic KernelSHAP requires evaluating $2^{|F|}$ feature subsets—computationally intractable for enterprise datasets ($M > 50$).

### 4.1 TreeSHAP Computational Breakthrough (Lundberg et al., 2020)
TreeSHAP exploits the internal tree structure of decision trees:
- It pushes conditional expectations down all leaves simultaneously in a single tree traversal.
- **Complexity Reduction:** Reduces computational time from exponential $\mathcal{O}(T \cdot 2^M)$ to low-order polynomial:
  $$\mathcal{O}(T \cdot L \cdot D^2)$$
  Where $T$ is the number of trees, $L$ is maximum leaves per tree, and $D$ is maximum tree depth ($D \le 6$ in standard GBDT).
- Computes **exact** Shapley values without sampling approximation.

---

## 5. SHAP Visualizations in Executive Delivery

```
                       SHAP Beeswarm Plot (Global Impact)
 Feature Name           Negative Impact <─── 0 ───> Positive Impact     Feature Value
 ───────────────────────────────────────────────────────────────────
 tenure_months         ●●●●●●●●●●●●●●●●●●│●●●●●●●●●●●●●●●●●●●          Low ── High
 monthly_charges                 ●●●●●●●●│●●●●●●●●●●●●●●●●●●●●●●●      Low ── High
 customer_tickets                        │●●●●●●●●●●●●●●●●●●●●●●●      Low ── High
 payment_auto_pay      ●●●●●●●●●●●●●●●●●●│●●●●                         Low ── High
```

1. **Beeswarm (Summary) Plot:** Combines feature importance with feature directionality. Each dot is an observation; color represents feature value (Blue = Low, Red = High); horizontal position is SHAP impact on prediction.
2. **Waterfall / Force Plot (Local):** Deconstructs an individual prediction starting from base value $\mathbb{E}[f(X)] \approx 0.15$ step-by-step to final score $0.84$. Red bars push score up; blue bars push score down.
3. **Dependence Plot (Non-linear & Interaction Effects):** Plots feature value on $x$-axis and SHAP value on $y$-axis, coloring points by an interacting secondary feature to reveal non-linear thresholds and synergy.

---

## 6. Production Python Implementation Template

```python
import shap
import lightgbm as lgb
import matplotlib.pyplot as plt

# 1. Train GBDT Model
model = lgb.LGBMClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(X_train, y_train)

# 2. Instantiate Fast TreeExplainer
explainer = shap.TreeExplainer(model)
shap_values = explainer(X_test)

# 3. Global Interpretability: Summary Beeswarm Plot
plt.figure(figsize=(10, 6))
shap.summary_plot(shap_values, X_test, show=False)
plt.title("TreeSHAP Global Feature Attributions", fontsize=14)
plt.tight_layout()
plt.savefig("shap_summary_plot.png", dpi=300)
plt.close()

# 4. Local Interpretability: Single Customer Waterfall
customer_idx = 0
plt.figure(figsize=(8, 5))
shap.plots.waterfall(shap_values[customer_idx], show=False)
plt.title(f"Local Churn Attribution: Customer #{customer_idx}", fontsize=14)
plt.tight_layout()
plt.savefig("shap_waterfall_cust0.png", dpi=300)
plt.close()
```
