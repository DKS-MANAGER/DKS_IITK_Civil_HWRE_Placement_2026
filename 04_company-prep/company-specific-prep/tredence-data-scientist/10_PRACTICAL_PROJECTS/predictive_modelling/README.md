# Project 1: Predictive Customer Churn & TreeSHAP Explainability

**Domain:** Omnichannel Enterprise Subscription / Retail Loyalty  
**Stack:** Python, Pandas, Scikit-Learn, LightGBM, TreeSHAP  
**Focus:** Class Imbalance, Leak-Free Pipelines, Probability Calibration, XAI

---

## 1. Project Overview

This project develops an end-to-end customer churn prediction pipeline designed for enterprise decision support.

### Key Technical Pillars:
1. **Leak-Free Preprocessing:** Encloses all imputation and one-hot encoding inside a Scikit-Learn `ColumnTransformer` fit strictly on the training partition.
2. **Handling Class Imbalance:** Employs LightGBM with calibrated `scale_pos_weight` and threshold optimization.
3. **Model Interpretability:** Computes exact local Shapley values using `shap.TreeExplainer` to generate reason codes for every individual high-risk customer.
4. **Business ROI Modeling:** Formulates a net profit matrix translating statistical precision/recall into saved EBITDA dollars.

---

## 2. File Structure

- `train_and_explain.py`: Fully reproducible Python script generating synthetic customer data, training LightGBM, performing evaluation (ROC-AUC, PR-AUC, Brier score), and generating TreeSHAP attributions.
- `interview_defense.md`: Comprehensive defense guide addressing likely interviewer challenges.
