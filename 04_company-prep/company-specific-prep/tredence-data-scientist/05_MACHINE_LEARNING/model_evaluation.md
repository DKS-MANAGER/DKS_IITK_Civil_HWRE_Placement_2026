# Model Evaluation, Calibration, and Monitoring

**Target Role:** Data Scientist / Associate Data Scientist | Tredence Analytics  
**Context:** IIT Kanpur Placement Season 2026–27  
**Prerequisites:** Probability Theory, Confusion Matrix, Optimization

---

## 1. Classification Metrics & Decision Thresholds

### 1.1 The Confusion Matrix & Derived Metrics

$$\begin{array}{c|cc}
& \text{Predicted Negative } (\hat{y}=0) & \text{Predicted Positive } (\hat{y}=1) \\
\hline
\text{Actual Negative } (y=0) & \text{True Negative (TN)} & \text{False Positive (FP)} \\
\text{Actual Positive } (y=1) & \text{False Negative (FN)} & \text{True Positive (TP)}
\end{array}$$

- **Accuracy:** $\frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}}$ *(Deceptive under class imbalance; e.g., 99% accuracy by predicting all zeros).*
- **Precision (Positive Predictive Value):** $\frac{\text{TP}}{\text{TP} + \text{FP}}$ *(Cost of False Positives: spam flag, customer insult).*
- **Recall (Sensitivity / True Positive Rate):** $\frac{\text{TP}}{\text{TP} + \text{FN}}$ *(Cost of False Negatives: missed cancer, undetected fraud, unmitigated churn).*
- **Specificity (True Negative Rate):** $\frac{\text{TN}}{\text{TN} + \text{FP}}$.
- **$F_1$-Score:** Harmonic mean of Precision and Recall:
  $$F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}} = \frac{2\text{TP}}{2\text{TP} + \text{FP} + \text{FN}}$$
- **$F_\beta$-Score:** Weights Recall $\beta$ times as much as Precision:
  $$F_\beta = (1 + \beta^2) \frac{\text{Precision} \times \text{Recall}}{\beta^2 \text{Precision} + \text{Recall}}$$
  *(Use $\beta = 2$ in churn retention or medical diagnosis where missing a true positive is far more costly than a false alarm).*

---

### 1.2 ROC-AUC vs PR-AUC: The Imbalance Imperative

```
            ROC-AUC Curve                                     PR-AUC Curve
  1.0 ┌─────────────────────┐                   1.0 ┌──────────\──────────┐
      │          /          │                       │           \         │
  TPR │        /            │             Precision │            \        │
      │      /              │                       │             \_______│
  0.0 └─────────────────────┘                   0.0 └─────────────────────┘
      0.0       FPR       1.0                       0.0      Recall     1.0
  (Baseline = 0.5 diagonal)                     (Baseline = Positive prevalence P(y=1))
```

#### Why ROC-AUC is Misleading for Rare Events
- **Definition of FPR:** $\text{FPR} = \frac{\text{FP}}{\text{FP} + \text{TN}}$.
- If negative class is massive (e.g., $1,000,000$ non-fraud transactions) and positive class is tiny ($1,000$ fraud transactions):
  - Suppose a model generates $10,000$ False Positives.
  - $\text{FPR} = \frac{10,000}{10,000 + 990,000} = \frac{10,000}{1,000,000} = 0.01 \ (1\%)$.
  - The ROC curve appears outstanding ($\text{FPR} = 1\%$ at high TPR), yielding an inflated ROC-AUC of $\sim 0.95$.
  - However, Precision $= \frac{1,000}{1,000 + 10,000} \approx 9\%$. 91 out of 100 alerts are false alarms!
- **Rule:** For imbalanced datasets ($< 5\%$ minority class), **PR-AUC (Precision-Recall AUC / Average Precision)** is the mandatory primary evaluation metric.

---

## 2. Probability Calibration & Scoring

Tree ensembles (LightGBM, Random Forest) output uncalibrated scores due to aggressive leaf bagging and margin-based optimization.

### 2.1 Calibration Metrics
- **Brier Score:** Mean squared difference between predicted probabilities and actual outcomes:
  $$\text{BS} = \frac{1}{N} \sum_{i=1}^N (\hat{p}_i - y_i)^2, \quad \text{BS} \in [0, 1]$$
- **Reliability Diagram:** Plot observed fraction of positives vs mean predicted probability across 10 bins. A perfectly calibrated model follows the $45^\circ$ line ($y = x$).

### 2.2 Calibration Methods
1. **Platt Scaling:** Fits a univariate logistic regression model on uncalibrated raw logits $f(x)$:
   $$\hat{p}(x) = \frac{1}{1 + \exp(A \cdot f(x) + B)}$$
   *Best for:* Small datasets; assumes sigmoid shape distortion.
2. **Isotonic Regression:** Non-parametric piecewise constant step-function minimizing squared error subject to monotonicity:
   $$\min_{m} \sum (y_i - m(f_i))^2 \quad \text{s.t.} \quad m(f_i) \le m(f_j) \text{ whenever } f_i \le f_j$$
   *Best for:* Large datasets ($N > 1,000$); can fit arbitrary monotonic distortions.

---

## 3. Regression & Demand Forecasting Metrics

| Metric | Mathematical Formula | Key Properties | Tredence / Industry Application |
|---|---|---|---|
| **MAE** | $\frac{1}{n} \sum \|y_i - \hat{y}_i\|$ | Robust to outliers; predicts median. Scale-dependent. | Logistics delivery time deviation |
| **RMSE** | $\sqrt{\frac{1}{n} \sum (y_i - \hat{y}_i)^2}$ | Heavily penalizes large errors; predicts conditional mean. | Energy load forecasting, Financial loss |
| **MAPE** | $\frac{100\%}{n} \sum \left\|\frac{y_i - \hat{y}_i}{y_i}\right\|$ | Intuitive percentage; breaks when $y_i = 0$ (division by zero); penalizes over-predictions more than under-predictions. | General managerial reporting |
| **WAPE** | $\frac{\sum \|y_i - \hat{y}_i\|}{\sum y_i}$ | Robust to zeros; volume-weighted. Does not blow up for zero-demand SKUs. | **Gold standard for Retail & CPG demand forecasting** |

---

## 4. Production Drift Monitoring: PSI & KS-Test

Production models degrade due to distribution shifts over time:
- **Covariate Drift:** Input distribution changes $P_t(X) \ne P_0(X)$, but relationship $P(Y \mid X)$ remains invariant.
- **Concept Drift:** Underlying relationship changes $P_t(Y \mid X) \ne P_0(Y \mid X)$ (e.g., consumer behavior shifts post-pandemic).

### 4.1 Population Stability Index (PSI)
Measures the shift between a baseline (training/validation) distribution $B$ and target (production) distribution $T$ across $K$ bins (deciles):

$$\text{PSI} = \sum_{k=1}^K \left(T_k - B_k\right) \times \ln\left(\frac{T_k}{B_k}\right)$$

Where $T_k$ and $B_k$ are proportions of observations falling in bin $k$.

**Industry Action Thresholds:**
- **$\text{PSI} < 0.10$:** No significant change; model is stable.
- **$0.10 \le \text{PSI} < 0.25$:** Moderate shift; flag for monitoring and review feature shifts.
- **$\text{PSI} \ge 0.25$:** Significant distribution change; **mandatory trigger to retrain model** on recent data.

### 4.2 Kolmogorov-Smirnov (KS) Drift Statistic
Two-sample non-parametric test comparing empirical CDFs:
$$D = \sup_x |F_{\text{baseline}}(x) - F_{\text{production}}(x)|$$
If $p\text{-value} < 0.05$, reject null hypothesis of identical distributions.
