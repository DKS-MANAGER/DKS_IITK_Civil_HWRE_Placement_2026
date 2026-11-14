# Project 1: Interview Defense & Technical Q&A

**Candidate Defense Readiness:** Predictive Modeling & Explainability  
**Role:** Data Scientist / Associate Data Scientist | Tredence Analytics

---

### Q1. Why did you choose LightGBM over Random Forest or XGBoost for this churn model?
**Defense:**  
- LightGBM uses **Histogram-based binning** and **Leaf-wise (best-first) tree growth**, which reduces training latency by up to $8\times$ compared to XGBoost while achieving equivalent or superior PR-AUC.
- In production churn scoring across millions of enterprise subscribers, inference latency and memory footprint are critical; LightGBM's integer-binned representations allow efficient memory scaling.
- It also natively accommodates `scale_pos_weight` directly in its gradient/Hessian computation, properly handling class imbalance.

---

### Q2. How did you ensure zero data leakage in your pipeline?
**Defense:**  
- Data leakage typically occurs when statistics computed on the entire dataset (like mean/median imputation or categorical encoding) bleed into the validation or test splits.
- I strictly applied Scikit-Learn's `ColumnTransformer` inside an isolated training step. The `.fit()` method was called **exclusively on the training partition (`X_train`)**, and `.transform()` was applied downstream on `X_test`.
- Furthermore, features were strictly audited for temporal validity to ensure no post-churn artifacts (e.g., cancellation feedback codes) were used.

---

### Q3. Why did you use PR-AUC alongside ROC-AUC?
**Defense:**  
- In churn datasets with $\sim 12\%$ prevalence (and especially lower, like 2–5%), ROC-AUC can be deceptively optimistic.
- The denominator for the False Positive Rate includes all True Negatives ($\frac{\text{FP}}{\text{FP} + \text{TN}}$). When non-churners dominate, even a large volume of False Positives yields a small FPR, artificially inflating ROC-AUC.
- PR-AUC evaluates Precision against Recall directly, completely excluding True Negatives, making it the mathematically rigorous metric for imbalanced commercial retention models.

---

### Q4. How do you convert TreeSHAP outputs into frontline operational actions?
**Defense:**  
- TreeSHAP provides the exact marginal contribution $\phi_i$ of each feature to the model's log-odds output for an individual customer.
- For each flagged account, our pipeline extracts the top positive SHAP driver and maps it to a pre-authorized CRM intervention:
  - If driven by `contract_type_Month-to-month` $\implies$ Route to sales rep with an incentive to lock a discounted 1-year contract.
  - If driven by `customer_service_calls` $\implies$ Trigger a proactive outreach from a Senior Customer Success Manager.
  - If driven by `monthly_charges` $\implies$ Offer a customized plan downgrade or temporary rebate.
- This closes the Tredence "Last-Mile" adoption loop by transforming raw probabilities into specific prescriptive actions.
