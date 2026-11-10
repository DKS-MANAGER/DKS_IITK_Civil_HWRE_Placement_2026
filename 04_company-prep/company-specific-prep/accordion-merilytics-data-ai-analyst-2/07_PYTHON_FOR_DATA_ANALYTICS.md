# Module 07 — Python for Data Analytics & Predictive Modeling

In private equity analytics at Accordion (Merilytics), Python is used for **scalable data cleaning, complex feature engineering, exploratory data analysis (EDA), and machine learning pipelines** that exceed Excel's processing capabilities.

---

## 1. High-Performance NumPy Vectorization

Python loops (`for`, `while`) are notoriously slow on large datasets because of dynamic type checking and interpreter overhead. NumPy arrays execute operations in compiled C:

```python
import numpy as np

# AVOID: Native Python loop (slow)
def calculate_markup_loop(costs, markup_rates):
    prices = []
    for c, m in zip(costs, markup_rates):
        prices.append(c * (1 + m))
    return prices

# PREFERRED: Vectorized NumPy array operation (100x faster)
def calculate_markup_vectorized(costs_arr, markup_arr):
    return costs_arr * (1.0 + markup_arr)
```

### 1.1 Array Broadcasting Rules
Broadcasting allows operations between arrays of different shapes without copying data in memory:
1. Two dimensions are compatible when:
   - They are equal, or
   - One of them is 1.
2. *Example*: Applying regional tax rates `(3,)` across a sales matrix `(100000, 3)`.

---

## 2. Advanced Pandas Workflows & Memory Optimization

When loading transactional extracts with millions of rows into a workstation, default Pandas types can easily exhaust RAM. Downcasting data types reduces memory footprint by up to 80%:

```python
import pandas as pd
import numpy as np

def optimize_dataframe_memory(df: pd.DataFrame) -> pd.DataFrame:
    """Downcasts numeric types and converts low-cardinality strings to categories."""
    initial_mem = df.memory_usage(deep=True).sum() / (1024 ** 2)
    
    for col in df.columns:
        col_type = df[col].dtype
        
        # Optimize integers
        if np.issubdtype(col_type, np.integer):
            c_min = df[col].min()
            c_max = df[col].max()
            if c_min >= 0:
                if c_max < 255:
                    df[col] = df[col].astype(np.uint8)
                elif c_max < 65535:
                    df[col] = df[col].astype(np.uint16)
                elif c_max < 4294967295:
                    df[col] = df[col].astype(np.uint32)
            else:
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                    
        # Optimize floats
        elif np.issubdtype(col_type, np.floating):
            df[col] = df[col].astype(np.float32)
            
        # Optimize string objects with low cardinality
        elif col_type == 'object':
            num_unique = df[col].nunique()
            num_total = len(df[col])
            if num_unique / num_total < 0.20:  # If unique values < 20%
                df[col] = df[col].astype('category')
                
    final_mem = df.memory_usage(deep=True).sum() / (1024 ** 2)
    print(f"Memory reduced from {initial_mem:.2f} MB to {final_mem:.2f} MB ({(1 - final_mem/initial_mem)*100:.1f}% savings)")
    return df
```

### 2.1 GroupBy: `agg()` vs. `transform()`
- `agg()`: Aggregates and collapses rows (returns 1 row per group).
- `transform()`: Computes group-level metrics but broadcasts back to original row shape (returns identical row count). Ideal for computing percentage contribution to parent category:

```python
# Compute customer order spend and its percentage of that customer's total spend
df['customer_total_spend'] = df.groupby('customer_id')['order_amount'].transform('sum')
df['pct_of_customer_spend'] = (df['order_amount'] / df['customer_total_spend']) * 100
```

---

## 3. End-to-End Predictive Machine Learning Pipeline

Below is a complete, production-grade churn prediction pipeline demonstrating feature engineering, cross-validation, XGBoost training, and SHAP explainability:

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, roc_auc_score, precision_recall_curve, auc
import xgboost as xgb
import shap

# 1. Load Simulated Portfolio Company Customer Dataset
# Columns: customer_id, tenure_months, monthly_charges, total_charges, 
#          support_tickets_last_90d, contract_type, payment_method, churn_flag
data = pd.read_csv("portco_saas_churn_sample.csv")

X = data.drop(columns=['customer_id', 'churn_flag'])
y = data['churn_flag']

# 2. Define Preprocessing Pipeline
numeric_features = ['tenure_months', 'monthly_charges', 'total_charges', 'support_tickets_last_90d']
categorical_features = ['contract_type', 'payment_method']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(drop='first', sparse_output=False), categorical_features)
    ]
)

# 3. Model Architecture with XGBoost (Handling Class Imbalance)
# Calculate scale_pos_weight = (count of negative class) / (count of positive class)
imbalance_ratio = (len(y) - y.sum()) / y.sum()

model = xgb.XGBClassifier(
    n_estimators=150,
    max_depth=4,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    scale_pos_weight=imbalance_ratio,
    eval_metric='logloss',
    random_state=42
)

# 4. Stratified Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, stratify=y, random_state=42
)

# Fit preprocessing and model
X_train_proc = preprocessor.fit_transform(X_train)
X_test_proc = preprocessor.transform(X_test)

model.fit(X_train_proc, y_train)

# 5. Model Evaluation (ROC-AUC & PR-AUC)
y_pred_proba = model.predict_proba(X_test_proc)[:, 1]
roc_auc = roc_auc_score(y_test, y_pred_proba)

precision, recall, _ = precision_recall_curve(y_test, y_pred_proba)
pr_auc = auc(recall, precision)

print(f"ROC-AUC: {roc_auc:.4f} | PR-AUC: {pr_auc:.4f}")

# 6. Explainable AI with SHAP
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test_proc)

# Feature Names Extraction
feature_names = numeric_features + list(
    preprocessor.named_transformers_['cat'].get_feature_names_out(categorical_features)
)

# Top Churn Drivers
mean_abs_shap = np.abs(shap_values).mean(axis=0)
shap_summary = pd.DataFrame({
    'Feature': feature_names,
    'Mean_SHAP_Impact': mean_abs_shap
}).sort_values('Mean_SHAP_Impact', ascending=False)

print("\n--- TOP CHURN DRIVERS (SHAP) ---")
print(shap_summary.head(5))
```

---

## 4. Translating Technical Machine Learning to Private Equity CFOs

When presenting predictive models to Accordion engagement leaders or portfolio company CFOs, never focus on loss functions or hyperparameter grids. **Translate predictions into EBITDA dollars**:

```
┌─────────────────────────────────┬────────────────────────────────────────────────────────────────────────┐
│          Technical Term         │                           Executive PE Translation                     │
├─────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ High Recall (85%)               │ "Our model catches 85 out of every 100 customers who are about to      │
│                                 │ cancel, allowing our Customer Success reps to intervene before churn." │
├─────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ High Precision (78%)            │ "When our model flags a customer as high-risk, there is a 78% certainty│
│                                 │ they will leave, meaning we avoid wasting discount offers on loyalists."│
├─────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ SHAP Feature: Support Tickets   │ "Customers with > 3 unresolved support tickets in 90 days face a 4.2x  │
│                                 │ higher churn risk. Fixing Tier-1 support directly protects $3.2M ARR." │
└─────────────────────────────────┴────────────────────────────────────────────────────────────────────────┘
```

