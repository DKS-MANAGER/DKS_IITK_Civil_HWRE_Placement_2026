# 12 — Machine Learning, XGBoost & Explainability (SHAP) in Credit Risk

## IIT Kanpur Placement Preparation — Barclays Quantitative Analytics (QA Model Monitoring)

---

### Executive Overview & The Regulated ML Landscape

In recent years, the adoption of machine learning (ML) — particularly Gradient Boosted Decision Trees (GBDT) such as **XGBoost** and **LightGBM** — has expanded across banking. In consumer lending, fraud detection, and credit underwriting, ensemble models routinely achieve **3 to 7 percentage point improvements in Gini / AUC** over traditional logistic scorecards by capturing complex non-linearities and high-order feature interactions.

However, in Tier 1 regulated banking (Barclays Risk QA, under **PRA SS1/23**, **Fed SR 11-7**, and **FCRA / ECOA**), the deployment of machine learning is constrained by two critical requirements:
1. **Mathematical Explainability & Adverse Action Reporting:** Banks cannot deploy an uninterpretable "black box". If a retail applicant is denied credit or assigned a high risk rating, regulations legally mandate providing the applicant with the **top 4 principal reasons** driving that decision.
2. **Domain Soundness & Monotonic Constraints:** Credit risk physics must not be violated (e.g., an increase in missed debt payments must *never* decrease predicted default risk, even if localized noise in the training sample suggests otherwise).

In Barclays Risk QA, machine learning algorithms are utilized in two primary capacities:
- **Primary Production Models:** In non-capital retail credit scoring, early delinquency warning, and transaction fraud monitoring, accompanied by rigorous explainability engines.
- **Challenger / Benchmark Models:** In Model Validation and Monitoring, QA builds champion-challenger machine learning models to benchmark legacy logistic scorecards, quantifying whether traditional linear models are missing substantial non-linear signals.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        The Credit Risk Modeling Trade-Off                              │
├────────────────────────────────┬───────────────────────────────────────────────────────┤
│ Traditional Logistic Scorecard │ Modern Gradient Boosted Trees (XGBoost)               │
├────────────────────────────────┼───────────────────────────────────────────────────────┤
│ • Moderate Gini (~0.55 - 0.65) │ • High Gini (~0.62 - 0.72)                            │
│ • Fully linear, transparent    │ • Captures complex non-linear feature interactions    │
│ • Easily auditable scorecard   │ • Requires algorithmic explainability (TreeSHAP)      │
│ • Directly monotonic by binning│ • Requires explicit monotonic constraints enforcement │
│ • Regulatory standard since    │ • Highly sensitive to out-of-time population drift    │
│   1970s (FICO architecture)    │   and extreme tail calibration overfitting            │
└────────────────────────────────┴───────────────────────────────────────────────────────┘
```

---

### 1. Tree-Based Ensemble Algorithms in Credit Risk

#### 1.1 Decision Trees (CART)
A Classification and Regression Tree partitions the $p$-dimensional feature space into $M$ orthogonal hyper-rectangles $\{R_1, R_2, \dots, R_M\}$. At each internal node, the algorithm evaluates all candidate features $j$ and split thresholds $s$ to maximize the reduction in node impurity (e.g., Gini Impurity for binary default classification):

$$I_G(Q) = 1 - \sum_{k=0}^{1} p_k^2 = 2 p (1 - p)$$
$$\Delta I_G(Q, j, s) = I_G(Q) - \left( \frac{|Q_{\text{left}} Sachs|}{|Q|} I_G(Q_{\text{left}}) + \frac{|Q_{\text{right}}|}{|Q|} I_G(Q_{\text{right}}) \right)$$

While single decision trees are interpretable, they exhibit high variance and poor generalizability on out-of-time banking data.

#### 1.2 Extreme Gradient Boosting (XGBoost)
XGBoost builds an additive ensemble of $K$ regression trees:
$$\hat{y}_i = \sum_{k=1}^{K} f_k(\mathbf{x}_i), \quad f_k \in \mathcal{F}$$

At boosting step $t$, the objective function minimized is:
$$\mathcal{L}^{(t)} = \sum_{i=1}^{N} l(y_i, \; \hat{y}_i^{(t-1)} + f_t(\mathbf{x}_i)) + \Omega(f_t)$$

where the regularization term penalizes tree complexity to prevent out-of-sample overfitting:
$$\Omega(f_t) = \gamma T + \frac{1}{2} \lambda \sum_{j=1}^{T} w_j^2$$
with $T$ being the number of terminal leaves, $w_j$ the leaf weight scores, $\gamma$ the leaf creation cost, and $\lambda$ the $L_2$ ridge regularization coefficient.

##### Second-Order Taylor Expansion
XGBoost approximates the loss function using a second-order Taylor expansion around the previous prediction $\hat{y}_i^{(t-1)}$:
$$\mathcal{L}^{(t)} \approx \sum_{i=1}^{N} \left[ l(y_i, \hat{y}_i^{(t-1)}) + g_i f_t(\mathbf{x}_i) + \frac{1}{2} h_i f_t^2(\mathbf{x}_i) \right] + \gamma T + \frac{1}{2} \lambda \sum_{j=1}^{T} w_j^2$$

where the first and second order gradients for logistic loss ($l(y, \hat{y}) = y \ln(1 + e^{-\hat{y}}) + (1 - y) \ln(1 + e^{\hat{y}})$) are:
$$g_i = \frac{\partial l(y_i, \hat{y}_i^{(t-1)})}{\partial \hat{y}_i^{(t-1)}} = p_i - y_i$$
$$h_i = \frac{\partial^2 l(y_i, \hat{y}_i^{(t-1)})}{\partial (\hat{y}_i^{(t-1)})^2} = p_i (1 - p_i)$$

For a fixed tree structure with instance sets $I_j = \{i \mid q(\mathbf{x}_i) = j\}$ assigned to leaf $j$, the optimal leaf weight $w_j^*$ and minimum objective value $\tilde{\mathcal{L}}^{(t)}$ have exact analytical solutions:

$$w_j^* = -\frac{\sum_{i \in I_j} g_i}{\sum_{i \in I_j} h_i + \lambda} = -\frac{G_j}{H_j + \lambda}$$
$$\tilde{\mathcal{L}}^{(t)} = -\frac{1}{2} \sum_{j=1}^{T} \frac{G_j^2}{H_j + \lambda} + \gamma T$$

The quality of a candidate node split into left and right children is evaluated via the **Gain score**:
$$\text{Gain} = \frac{1}{2} \left[ \frac{G_L^2}{H_L + \lambda} + \frac{G_R^2}{H_R + \lambda} - \frac{(G_L + G_R)^2}{H_L + H_R + \lambda} \right] - \gamma$$

---

### 2. Class Imbalance in Credit Risk Modeling

In retail and wholesale credit portfolios, default is a rare event. Empirical 12-month default rates typically range from **0.5% (Prime mortgages)** to **3.5% (Unsecured credit cards)**. A naive model predicting "Non-Default" for every borrower achieves 96.5% to 99.5% accuracy while possessing zero risk discrimination.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        Class Imbalance Strategies in Risk QA                           │
├───────────────────────────────┬────────────────────────────────┬───────────────────────┤
│ Algorithmic Cost-Weighting    │ Resampling Techniques          │ Evaluation Metrics    │
├───────────────────────────────┼────────────────────────────────┼───────────────────────┤
│ • scale_pos_weight = N_0 / N_1│ • Random Undersampling (RUS)   │ • Reject Raw Accuracy │
│ • Penalizes false negatives   │ • SMOTE (Synthetic Minority)   │ • Prioritize ROC-AUC, │
│   (missed defaults) more      │ • CAUTION: SMOTE distorts      │   Gini, PR-AUC, and   │
│   heavily than false positives│   natural portfolio empirical  │   Precision at fixed  │
│ • Preserves raw feature space │   calibration and O/E ratios!  │   acceptance cutoffs  │
└───────────────────────────────┴────────────────────────────────┴───────────────────────┘
```

#### Why SMOTE is Restricted in Regulated Banking:
Synthetic Minority Over-sampling Technique (SMOTE) generates artificial synthetic default examples by interpolating between nearest minority-class neighbors. In regulated banking (Barclays Risk QA), SMOTE is frequently challenged by 2LoD and regulators because:
1. It manufactures synthetic borrower profiles that may violate real-world business constraints (e.g., fractional number of dependents or incompatible bureau trade-lines).
2. It distorts the natural prior probability $P(Y = 1)$, destroying model calibration. A model trained on a 50:50 SMOTE-balanced sample produces severely inflated predicted probabilities that require complex post-hoc Platt scaling or isotonic recalibration.
3. **Preferred Regulatory Practice:** Use the natural un-resampled empirical portfolio distribution combined with cost-sensitive objective weights (`scale_pos_weight`) or tune decision cutoffs directly on predicted probability outputs.

---

### 3. Model Explainability via Cooperative Game Theory (SHAP)

To deploy machine learning models in credit underwriting, institutions must explain individual predictions to both supervisory authorities and rejected loan applicants. The gold standard for model explainability is **SHAP (SHapley Additive exPlanations)**, rooted in cooperative game theory (Lloyd Shapley, 1953; Lundberg & Lee, 2017).

#### 3.1 Mathematical Formulation of Shapley Values
Let $F$ be the set of all $M$ input features. We treat the prediction of a model for a specific applicant as a cooperative game where each feature is a "player", and the model prediction $f(x)$ is the total payout.

The **Shapley value** $\phi_i$ represents the unique fair marginal contribution of feature $i$ across all possible feature coalitions $S \subseteq F \setminus \{i\}$:

$$\phi_i(x) = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|! \, (|F| - |S| - 1)!}{|F|!} \left[ f(S \cup \{i\}) - f(S) \right]$$

where:
- $|S|$ is the number of features in coalition $S$.
- $|F|!$ is the total number of feature permutations.
- $\frac{|S|! \, (|F| - |S| - 1)!}{|F|!}$ is the combinatorial probability of forming coalition $S$.
- $f(S \cup \{i\}) - f(S)$ is the marginal difference in prediction when feature $i$ joins coalition $S$.

#### 3.2 Four Fundamental Axioms Satisfied by Shapley Values
SHAP is the *only* feature attribution method that simultaneously satisfies four essential mathematical properties:
1. **Efficiency (Additivity):**
   $$\sum_{i=1}^{M} \phi_i(x) = f(x) - \mathbb{E}[f(X)]$$
   The sum of feature Shapley values equals the difference between the model's prediction for this specific borrower and the baseline expected prediction across the portfolio.
2. **Symmetry:** If two features $i$ and $j$ contribute equally to all possible coalitions ($f(S \cup \{i\}) = f(S \cup \{j\})$ for all $S$), their attributions are identical: $\phi_i = \phi_j$.
3. **Dummy / Null Player:** If feature $i$ adds zero marginal value to any coalition ($f(S \cup \{i\}) = f(S)$ for all $S$), its attribution is strictly zero: $\phi_i = 0$.
4. **Monotonicity (Additivity across models):** If a model change increases the marginal contribution of feature $i$ for all coalitions, its attributed value cannot decrease.

#### 3.3 TreeSHAP for High-Speed Ensembles
While calculating exact Shapley values requires exponential time $\mathcal{O}(M \cdot 2^{|F|})$, Lundberg et al. (2020) developed **TreeSHAP**, an algorithm that computes exact Shapley values on tree-based models in polynomial time $\mathcal{O}(T \cdot L \cdot D^2)$ (where $T$ is trees, $L$ is leaves, and $D$ is maximum tree depth). This enables instant batch generation of explanations across millions of banking accounts.

```
Individual Account SHAP Waterfall Breakdown
Base Expected Default Probability: E[f(X)] = 2.50%
------------------------------------------------------------------------
Feature Name                Value    SHAP Contribution    Current Logit
------------------------------------------------------------------------
Base Log-Odds                           --                 -3.66 (2.50%)
+ Delinquency Count (24M)     2      +0.85                 -2.81 (5.68%)
+ Debt-to-Income (DTI)      48%      +0.42                 -2.39 (8.39%)
- Bureau Score              740      -0.55                 -2.94 (5.01%)
+ Credit Inquiries (6M)       5      +0.38                 -2.56 (7.19%)
------------------------------------------------------------------------
Final Model Output: f(x) = -2.56 (Predicted PD = 7.19%) -> REJECTED
```

#### Generating Regulatory Adverse Action Notice Codes
Under the US Equal Credit Opportunity Act (ECOA) and UK Consumer Duty guidelines, an applicant rejected by an automated model must be given the specific adverse reasons. Risk QA configures production pipelines to extract the **top 4 features with the highest positive SHAP values** (features pushing predicted default probability upward most severely):
1. Number of past delinquencies in the last 24 months ($\phi_1 = +0.85$).
2. High Debt-to-Income ratio ($\phi_2 = +0.42$).
3. Number of recent credit bureau inquiries ($\phi_3 = +0.38$).
4. Length of credit history shorter than benchmark.

---

### 4. Regulatory Constraints & Monotonicity Enforcement

In unconstrained machine learning, algorithms can discover spurious correlations in training data. For example, in an unconstrained XGBoost model, an applicant with 8 missed payments might randomly show a slightly lower predicted default rate than an applicant with 7 missed payments due to sample sparsity in the extreme tail.

Such behavior is strictly prohibited under banking regulations. A credit model must be **monotonically sound**.

```
Default Risk
    ▲
    │         Unconstrained ML (Regulatory Failure: Dip at high debt)
    │             . - - .
    │            /        \
    │           /          ' - . _
    │          /                   \
    │         /                     ' - -
    │        /
    │       /  Monotonically Constrained XGBoost (Regulator Approved)
    │      /   ──────────────────────────────────────────────────►
    │     /
    │    /
    │   /
    └──┴──────────────────────────────────────────────────────►
       0%                    50%                  100%   Debt-to-Income
```

#### Enforcing Monotonic Constraints in XGBoost
XGBoost supports exact mathematical monotonicity enforcement during node splitting. During tree growth, the algorithm restricts candidate splits such that leaf weights satisfy:
$$w_{\text{left}} \le w_{\text{right}} \quad (\text{for positive monotonic constraint } +1)$$
$$w_{\text{left}} \ge w_{\text{right}} \quad (\text{for negative monotonic constraint } -1)$$

In Python:
```python
params = {
    'objective': 'binary:logistic',
    'eval_metric': 'auc',
    # 1: Monotonically increasing risk (higher feature -> higher PD)
    # -1: Monotonically decreasing risk (higher feature -> lower PD)
    # 0: Unconstrained
    # Features: [DTI, Bureau_Score, Delinquency_Count, Annual_Income]
    'monotone_constraints': (1, -1, 1, -1)
}
```

Enforcing monotonicity provides mathematical certainty that:
- Higher Debt-to-Income will never lower risk.
- Higher Bureau Score will never increase risk.
- Higher Delinquencies will never lower risk.
- Higher Income will never increase risk.

This transforms XGBoost from an uninterpretable black box into a compliant, regulator-ready risk engine.

---

### 5. Step-by-Step Numerical Example: 3-Feature Shapley Calculation

Consider a simplified credit model with $M = 3$ binary features:
- Feature 1 ($x_1$): Delinquency History ($1 = \text{Yes}, 0 = \text{No}$)
- Feature 2 ($x_2$): High Utilization $> 80\%$ ($1 = \text{Yes}, 0 = \text{No}$)
- Feature 3 ($x_3$): Low Bureau Score $< 650$ ($1 = \text{Yes}, 0 = \text{No}$)

Let the model output function $f(S)$ represent predicted default rate (%) for any subset of active features:
- $f(\emptyset) = 2.0\%$ (Baseline portfolio average)
- $f(\{1\}) = 6.0\%$
- $f(\{2\}) = 4.0\%$
- $f(\{3\}) = 5.0\%$
- $f(\{1, 2\}) = 11.0\%$
- $f(\{1, 3\}) = 10.0\%$
- $f(\{2, 3\}) = 8.0\%$
- $f(\{1, 2, 3\}) = 18.0\%$

Let us compute the exact **Shapley Value for Feature 1 ($\phi_1$)**:
Total features $|F| = 3$. The possible coalitions $S \subseteq \{2, 3\}$ excluding Feature 1 are:
1. $S = \emptyset \quad (|S| = 0)$
2. $S = \{2\} \quad (|S| = 1)$
3. $S = \{3\} \quad (|S| = 1)$
4. $S = \{2, 3\} \quad (|S| = 2)$

#### Weight Formula:
$$W(|S|) = \frac{|S|! \, (|F| - |S| - 1)!}{|F|!} = \frac{|S|! \, (3 - |S| - 1)!}{3!} = \frac{|S|! \, (2 - |S|)!}{6}$$

| Coalition ($S$) | Coalition Size ($|S|$) | Weight $W(|S|)$ | $f(S)$ | $f(S \cup \{1\})$ | Marginal Contribution $f(S \cup \{1\}) - f(S)$ | Weighted Contribution |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| $\emptyset$ | 0 | $\frac{0! \, 2!}{6} = \frac{2}{6} = \frac{1}{3}$ | $2.0\%$ | $6.0\%$ | $6.0 - 2.0 = +4.0\%$ | $\frac{1}{3} \times 4.0\% = +1.333\%$ |
| $\{2\}$ | 1 | $\frac{1! \, 1!}{6} = \frac{1}{6}$ | $4.0\%$ | $11.0\%$ | $11.0 - 4.0 = +7.0\%$ | $\frac{1}{6} \times 7.0\% = +1.167\%$ |
| $\{3\}$ | 1 | $\frac{1! \, 1!}{6} = \frac{1}{6}$ | $5.0\%$ | $10.0\%$ | $10.0 - 5.0 = +5.0\%$ | $\frac{1}{6} \times 5.0\% = +0.833\%$ |
| $\{2, 3\}$ | 2 | $\frac{2! \, 0!}{6} = \frac{2}{6} = \frac{1}{3}$ | $8.0\%$ | $18.0\%$ | $18.0 - 8.0 = +10.0\%$ | $\frac{1}{3} \times 10.0\% = +3.333\%$ |
| **Sum** | — | **1.000** | — | — | — | **$\phi_1 = \mathbf{+6.667\%}$** |

#### Verification of Additivity:
Performing the identical calculation for Feature 2 and Feature 3 yields:
- $\phi_1 = +6.667\%$
- $\phi_2 = +4.667\%$
- $\phi_3 = +4.667\%$
- $\text{Total Attributions} = \phi_1 + \phi_2 + \phi_3 = 6.667\% + 4.667\% + 4.667\% = \mathbf{+16.0\%}$.
- Total Model Shift = $f(\{1, 2, 3\}) - f(\emptyset) = 18.0\% - 2.0\% = \mathbf{+16.0\%}$.

The efficiency axiom holds exactly: $\sum_{i=1}^3 \phi_i = f(x) - \mathbb{E}[f(X)]$. Feature 1 (Delinquency History) accounts for $+6.67\%$ of the $+16.0\%$ total risk increase, ranking as the primary reason code for adverse action.

---

*Authoritative cross-reference: Lundberg, S. M., & Lee, S. I. (2017), "A Unified Approach to Interpreting Model Predictions", NeurIPS; Chen, T., & Guestrin, C. (2016), "XGBoost: A Scalable Tree Boosting System", ACM KDD; Bank of England PRA SS1/23 ("Model Risk Management Principles for Banks").*

