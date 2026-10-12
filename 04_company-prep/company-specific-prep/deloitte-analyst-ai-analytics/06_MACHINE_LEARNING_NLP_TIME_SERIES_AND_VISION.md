# Module 06: Applied Machine Learning, NLP, Time-Series, and Computer Vision

> **Module Code**: DEL-M06  
> **Priority**: P2 (Core Role Alignment)  
> **Target Assessment**: Technical Interview Modeling Defense & Applied Analytics Cases  
> **Standard**: Complete theoretical foundations, loss functions, evaluation proofs, imbalanced metrics, time-series stationarity, and runnable Python demonstrations.

---

## 1. End-to-End Machine Learning Workflow & Problem Framing

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                       ENTERPRISE ML DELIVERY PIPELINE                       │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. Business Problem Definition ──► Framing as Regression / Classification   │
│ 2. Data Audit & Leakage Check  ──► Temporal train/test split; PII scrubbing │
│ 3. Feature Engineering         ──► Missing imputation, scaling, encodings   │
│ 4. Baseline Model Selection    ──► Simple heuristic (mean or majority class)│
│ 5. Model Training & Validation ──► Ridge, Random Forest, XGBoost (K-Fold)   │
│ 6. Rigorous Evaluation         ──► PR-AUC, ROC-AUC, Cost-weighted matrix    │
│ 7. Model Explainability        ──► SHAP value feature attribution           │
│ 8. Deployment & Drift Monitor  ──► Concept drift & retraining trigger       │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Core Supervised Algorithms & Mathematical Intuition

### 2.1 Linear Regression & Regularization (Ridge vs. Lasso)

* **Ordinary Least Squares (OLS) Objective**:
  $$\min_{\mathbf{w}} \sum_{i=1}^N (y_i - \mathbf{w}^T \mathbf{x}_i)^2$$
* **Ridge Regression (L2 Regularization)**:
  $$\min_{\mathbf{w}} \left[ \sum_{i=1}^N (y_i - \mathbf{w}^T \mathbf{x}_i)^2 + \lambda \sum_{j=1}^D w_j^2 \right]$$
  *Shrinks weights continuously towards zero; handles multicollinearity; keeps all features.*
* **Lasso Regression (L1 Regularization)**:
  $$\min_{\mathbf{w}} \left[ \sum_{i=1}^N (y_i - \mathbf{w}^T \mathbf{x}_i)^2 + \lambda \sum_{j=1}^D |w_j| \right]$$
  *Drives coefficients to exactly zero due to the diamond-shaped geometry of the L1 ball; performs automatic feature selection.*

---

### 2.2 Logistic Regression & Cross-Entropy Loss

* Maps real linear combinations to probability interval $(0, 1)$ via Sigmoid function:
  $$P(Y = 1 \mid \mathbf{x}) = \sigma(\mathbf{w}^T \mathbf{x}) = \frac{1}{1 + e^{-\mathbf{w}^T \mathbf{x}}}$$
* **Binary Cross-Entropy (Log-Loss)**:
  $$\mathcal{L}(\mathbf{w}) = - \frac{1}{N} \sum_{i=1}^N \left[ y_i \ln(\hat{y}_i) + (1 - y_i) \ln(1 - \hat{y}_i) \right]$$

---

### 2.3 Tree Ensembles: Random Forest (Bagging) vs. Gradient Boosting (Boosting)

| Dimension | Random Forest (Bagging) | Gradient Boosted Decision Trees (Boosting) |
| :--- | :--- | :--- |
| **Core Principle** | Parallel independent trees trained on bootstrap samples with random feature subsets. | Sequential trees; each tree fits the negative gradient (residual errors) of the prior ensemble. |
| **Primary Error Reduced** | **Variance** (averaging deep, high-variance trees). | **Bias** (combining shallow, weak learners into a strong learner). |
| **Parallelization** | Fully parallelizable across CPU cores. | Inherently sequential (though histogram split finding is parallelized in XGBoost/LightGBM). |
| **Sensitivity to Outliers**| Robust to noise and outliers. | More sensitive to label noise as it continually tries to correct hard outliers. |

---

## 3. Evaluation Metrics for Imbalanced Enterprise Data

In real consulting engagements (fraud detection, churn prediction, equipment failure), the positive class is rare (1% or less). **Accuracy is completely misleading**.

```text
CONFUSION MATRIX:
                  Predicted Negative    Predicted Positive
Actual Negative │ True Negative (TN)  │ False Positive (FP) │  Type I Error
Actual Positive │ False Negative (FN) │ True Positive (TP)  │  Type II Error
```

### Metrics Defined
* **Precision**: $\frac{\text{TP}}{\text{TP} + \text{FP}}$ — Out of all predicted positives, how many are actually positive? (Crucial when false alarms are expensive).
* **Recall (Sensitivity)**: $\frac{\text{TP}}{\text{TP} + \text{FN}}$ — Out of all actual positives, how many did we catch? (Crucial in medical diagnosis and fraud).
* **F1-Score**: Harmonic mean of Precision and Recall:
  $$\text{F1} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$
* **ROC-AUC vs. PR-AUC Rule**:
  * **ROC-AUC**: Plots True Positive Rate vs. False Positive Rate. Inflated on highly imbalanced data because huge numbers of True Negatives suppress the False Positive Rate.
  * **PR-AUC (Precision-Recall AUC)**: Focuses exclusively on the minority positive class. The gold standard for evaluating imbalanced enterprise models.

---

## 4. Time-Series Analysis & Forecasting

### 4.1 Classical Time-Series Decomposition
$$Y_t = T_t + S_t + C_t + I_t \quad (\text{Additive}) \quad \text{or} \quad Y_t = T_t \times S_t \times C_t \times I_t \quad (\text{Multiplicative})$$

### 4.2 Stationarity & The Augmented Dickey-Fuller (ADF) Test
* **Stationarity**: Constant mean, constant variance, and autocovariance dependent only on time lag $k$, not on absolute time $t$.
* **ADF Test**: Tests null hypothesis $H_0$: Series possesses a unit root (non-stationary). If $p < 0.05$, reject $H_0$ and conclude the series is stationary. If non-stationary, apply first-order differencing: $\Delta Y_t = Y_t - Y_{t-1}$.

---

## 5. Natural Language Processing (NLP) & Computer Vision

### 5.1 Text Representations: TF-IDF to Dense Embeddings
* **Term Frequency-Inverse Document Frequency (TF-IDF)**:
  $$\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \ln\left(\frac{N}{1 + |\{d \in D : t \in d\}|}\right)$$
  *Captures lexical importance but lacks semantic understanding (synonyms have zero overlap).*
* **Dense Embeddings (Sentence Transformers)**: Maps variable-length text to a fixed-dimensional dense vector space (e.g., 768 dimensions) where semantic similarity corresponds to vector cosine similarity:
  $$\cos(\mathbf{u}, \mathbf{v}) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|}$$

### 5.2 Computer Vision Basics (CNN Architecture)
* **Convolution Operation**: Sliding a learnable weight kernel (e.g., $3 \times 3$) across an image matrix to produce feature maps capturing edges, textures, and spatial hierarchies.
* **Pooling**: Max pooling reduces spatial dimensionality while preserving dominant activations, providing translational invariance.

---

## 6. Runnable Python Demonstration: Model Training & Evaluation

```python
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, average_precision_score, roc_auc_score

# 1. Generate Synthetic Imbalanced Dataset (95% Negative, 5% Positive)
X, y = make_classification(
    n_samples=2000, 
    n_features=10, 
    weights=[0.95, 0.05], 
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)

# 2. Train Model with Class Weight Balancing
clf = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
clf.fit(X_train, y_train)

# 3. Predict Probabilities & Labels
y_pred_proba = clf.predict_proba(X_test)[:, 1]
y_pred = clf.predict(X_test)

# 4. Evaluation Outputs
print("ROC-AUC Score:", round(roc_auc_score(y_test, y_pred_proba), 4))
print("PR-AUC Score:", round(average_precision_score(y_test, y_pred_proba), 4))
print("
Classification Report:
", classification_report(y_test, y_pred))
```

---

## 7. Self-Assessment Checklist

- [ ] Can explain Ridge vs. Lasso regularization and why L1 produces sparse weights.
- [ ] Understand why Random Forest reduces variance while Gradient Boosting reduces bias.
- [ ] Confident explaining why PR-AUC is preferred over ROC-AUC for imbalanced business datasets.
- [ ] Understand Augmented Dickey-Fuller (ADF) testing for time-series stationarity.
- [ ] Able to explain the transition from TF-IDF sparse vectors to dense semantic embeddings.
