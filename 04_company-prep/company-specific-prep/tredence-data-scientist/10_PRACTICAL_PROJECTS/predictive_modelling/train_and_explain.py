"""
Project 1: Enterprise Predictive Customer Churn & TreeSHAP Pipeline
Reproducible Python script with synthetic generation, leak-free pipeline,
evaluation metrics (PR-AUC, ROC-AUC, Brier score), and TreeSHAP explainability.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import roc_auc_score, average_precision_score, brier_score_loss, classification_report
import lightgbm as lgb
import shap

def generate_synthetic_churn_data(n_samples: int = 5000, random_state: int = 42) -> pd.DataFrame:
    """Generates a realistic enterprise customer churn dataset with class imbalance (~12% churn)."""
    np.random.seed(random_state)
    
    tenure_months = np.random.exponential(scale=24, size=n_samples).clip(1, 72)
    monthly_charges = np.random.normal(loc=70, scale=30, size=n_samples).clip(20, 150)
    customer_service_calls = np.random.poisson(lam=1.5, size=n_samples)
    contract_type = np.random.choice(['Month-to-month', 'One-year', 'Two-year'], size=n_samples, p=[0.55, 0.25, 0.20])
    payment_method = np.random.choice(['Electronic check', 'Mailed check', 'Bank transfer', 'Credit card'], size=n_samples)
    tech_support = np.random.choice(['Yes', 'No'], size=n_samples, p=[0.4, 0.6])
    
    # Latent churn probability
    z = (
        - 0.05 * tenure_months
        + 0.02 * monthly_charges
        + 0.60 * customer_service_calls
        + 1.20 * (contract_type == 'Month-to-month')
        - 0.80 * (tech_support == 'Yes')
        - 2.5
    )
    p = 1 / (1 + np.exp(-z))
    churn = np.random.binomial(n=1, p=p)
    
    df = pd.DataFrame({
        'tenure_months': tenure_months,
        'monthly_charges': monthly_charges,
        'customer_service_calls': customer_service_calls,
        'contract_type': contract_type,
        'payment_method': payment_method,
        'tech_support': tech_support,
        'churn': churn
    })
    
    # Inject missingness (MAR)
    mask_missing = np.random.binomial(1, 0.05, size=n_samples).astype(bool)
    df.loc[mask_missing, 'monthly_charges'] = np.nan
    
    return df

def run_pipeline():
    print("=== Step 1: Ingesting Data ===")
    df = generate_synthetic_churn_data()
    print(f"Dataset shape: {df.shape}, Churn rate: {df['churn'].mean():.2%}")
    
    X = df.drop(columns=['churn'])
    y = df['churn']
    
    # Step 2: Leak-Free Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42, stratify=y)
    
    num_cols = ['tenure_months', 'monthly_charges', 'customer_service_calls']
    cat_cols = ['contract_type', 'payment_method', 'tech_support']
    
    # Step 3: Preprocessing Transformer
    preprocessor = ColumnTransformer(transformers=[
        ('num', Pipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
        ]), num_cols),
        ('cat', Pipeline([
            ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
            ('ohe', OneHotEncoder(drop='first', sparse_output=False))
        ]), cat_cols)
    ])
    
    # Fit preprocessor strictly on X_train
    X_train_proc = preprocessor.fit_transform(X_train)
    X_test_proc = preprocessor.transform(X_test)
    
    # Extract feature names
    cat_feature_names = preprocessor.named_transformers_['cat']['ohe'].get_feature_names_out(cat_cols)
    all_feature_names = list(num_cols) + list(cat_feature_names)
    
    # Step 4: Model Training with LightGBM
    scale_pos_weight = (len(y_train) - sum(y_train)) / sum(y_train)
    model = lgb.LGBMClassifier(
        n_estimators=100,
        learning_rate=0.05,
        max_depth=4,
        num_leaves=15,
        scale_pos_weight=scale_pos_weight,
        random_state=42,
        verbosity=-1
    )
    model.fit(X_train_proc, y_train)
    
    # Step 5: Evaluation
    y_pred_proba = model.predict_proba(X_test_proc)[:, 1]
    y_pred = (y_pred_proba >= 0.50).astype(int)
    
    roc_auc = roc_auc_score(y_test, y_pred_proba)
    pr_auc = average_precision_score(y_test, y_pred_proba)
    brier = brier_score_loss(y_test, y_pred_proba)
    
    print("\n=== Model Performance Evaluation ===")
    print(f"ROC-AUC Score:      {roc_auc:.4f}")
    print(f"PR-AUC (Avg Prec):  {pr_auc:.4f} (Baseline: {y_test.mean():.4f})")
    print(f"Brier Score Loss:   {brier:.4f}")
    print("\nClassification Report (Threshold 0.50):")
    print(classification_report(y_test, y_pred))
    
    # Step 6: TreeSHAP Attribution
    print("\n=== TreeSHAP Attribution Analysis ===")
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X_test_proc)
    
    # In binary LightGBM, shap_values can be list of 2 arrays or 1 array
    if isinstance(shap_values, list):
        shap_matrix = shap_values[1]
    else:
        shap_matrix = shap_values
        
    mean_abs_shap = np.abs(shap_matrix).mean(axis=0)
    shap_importance_df = pd.DataFrame({
        'feature': all_feature_names,
        'mean_abs_shap': mean_abs_shap
    }).sort_values('mean_abs_shap', ascending=False)
    
    print("Top 5 Global Drivers of Churn:")
    print(shap_importance_df.head(5).to_string(index=False))
    
    # Single Customer Reason Code Example
    cust_idx = 0
    cust_score = y_pred_proba[cust_idx]
    cust_shap = shap_matrix[cust_idx]
    top_driver_idx = np.argmax(cust_shap)
    print(f"\nSample Customer #0 Predicted Churn Probability: {cust_score:.2%}")
    print(f"Primary Churn Driver: {all_feature_names[top_driver_idx]} (SHAP impact: {cust_shap[top_driver_idx]:+.3f})")
    
    return {
        'roc_auc': roc_auc,
        'pr_auc': pr_auc,
        'brier': brier,
        'top_features': shap_importance_df.head(5)['feature'].tolist()
    }

if __name__ == '__main__':
    run_pipeline()
