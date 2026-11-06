# Module 05: Python for Commercial Healthcare Analytics

> **Document Status**: Production-Grade Applied Reference `[TIER 4 / SCIENTIFIC PYTHON & ANSI STANDARDS]`  
> **Core Focus**: Core Python, Vectorized NumPy, High-Performance Pandas, Time-Series Feature Engineering, and Scikit-Learn Pipelines for Healthcare Datasets  
> **Target Role**: Analyst (IQVIA India)  

---

## 1. High-Performance Core Python & Memory-Efficient Data Structures

In commercial analytics, datasets such as patient-level claims or retail prescription audits (NPA) can span tens of millions of records. Writing clean, memory-efficient Python is a primary technical interview evaluation criterion.

### 1.1 List & Dictionary Comprehensions
Avoid slow `for` loops by utilizing comprehensions compiled directly in CPython bytecode:
```python
# Filtering and transforming physician detailing records
physicians = [
    {'npi': '1049283741', 'specialty': 'Oncology', 'calls': 14, 'converted': True},
    {'npi': '1928374650', 'specialty': 'Cardiology', 'calls': 4, 'converted': False},
    {'npi': '1837465920', 'specialty': 'Oncology', 'calls': 22, 'converted': True}
]

# Fast dictionary comprehension: NPI mapped to call intensity for converted Oncologists
oncology_call_map = {
    doc['npi']: doc['calls'] 
    for doc in physicians 
    if doc['specialty'] == 'Oncology' and doc['converted']
}
```

### 1.2 Iterators & Generators for Multi-Gigabyte Data Streaming
When reading a 5 GB prescription log file, loading the entire file into RAM triggers an `OutOfMemory` (OOM) exception. Python generators stream records lazily one line at a time:

```python
def stream_prescription_records(file_path):
    """Generator streaming large text files line-by-line without memory spikes."""
    with open(file_path, 'r', encoding='utf-8') as f:
        header = f.readline().strip().split(',')
        for line in f:
            fields = line.strip().split(',')
            yield dict(zip(header, fields))

# Usage: Processing records lazily
# for record in stream_prescription_records("national_prescription_audit_10M.csv"):
#     process_record(record)
```

---

## 2. Vectorized NumPy Operations & Broadcasting

NumPy replaces Python interpreter overhead with vectorized SIMD (Single Instruction, Multiple Data) execution in compiled C:

### 2.1 Broadcasting Rules
NumPy compares shapes element-wise from trailing dimensions backwards:
Two dimensions are compatible if:
1. They are equal, or
2. One of them is 1.

```python
import numpy as np

# Weekly promotional spends across 3 channels (104 weeks x 3 channels)
spend_matrix = np.random.uniform(5000, 25000, size=(104, 3))

# Channel-specific return multipliers (1 x 3)
channel_efficiency = np.array([1.25, 0.85, 1.40])

# Broadcasting: (104, 3) * (3,) -> (104, 3) element-wise multiplication
projected_sales = spend_matrix * channel_efficiency
```

### 2.2 Conditional Logic via `np.where` and `np.select`
```python
# Categorizing physician prescribing volume into Deciles without slow apply()
trx_volume = np.array([12, 45, 120, 8, 250, 65, 0])

conditions = [
    trx_volume == 0,
    (trx_volume > 0) & (trx_volume <= 20),
    (trx_volume > 20) & (trx_volume <= 80),
    trx_volume > 80
]
tier_labels = ['Non-Prescriber', 'Low Prescriber', 'Medium Prescriber', 'High Decile Key Target']

physician_tier = np.select(conditions, tier_labels, default='Unclassified')
```

---

## 3. High-Performance Pandas for Commercial Datasets

### 3.1 Memory Optimization: Categorical Dtypes & Downcasting
By default, Pandas assigns `int64` and `float64` to numeric columns and `object` to strings. For large datasets, downcasting memory usage by 70–85%:

```python
import pandas as pd

def optimize_commercial_df(df: pd.DataFrame) -> pd.DataFrame:
    """Downcasts float/int types and converts repetitive strings to categoricals."""
    start_mem = df.memory_usage().sum() / 1024**2
    for col in df.columns:
        col_type = df[col].dtype
        if col_type == 'object':
            num_unique = df[col].nunique()
            num_total = len(df[col])
            if num_unique / num_total < 0.2:  # High repetition (e.g., Specialty, Region)
                df[col] = df[col].astype('category')
        elif str(col_type).startswith('int'):
            df[col] = pd.to_numeric(df[col], downcast='integer')
        elif str(col_type).startswith('float'):
            df[col] = pd.to_numeric(df[col], downcast='float')
    end_mem = df.memory_usage().sum() / 1024**2
    print(f"Memory reduced from {start_mem:.2f} MB to {end_mem:.2f} MB ({(start_mem-end_mem)/start_mem*100:.1f}% reduction)")
    return df
```

### 3.2 Advanced GroupBy, Aggregations & Pivot Tables
```python
# Synthetic physician sales data
np.random.seed(42)
n_records = 1000
hcp_df = pd.DataFrame({
    'Territory_ID': np.random.choice(['East', 'West', 'North', 'South'], size=n_records),
    'Specialty': np.random.choice(['Cardiology', 'Oncology', 'Neurology'], size=n_records),
    'Brand_TRx': np.random.poisson(lam=35, size=n_records),
    'Market_TRx': np.random.poisson(lam=120, size=n_records),
    'Details_Delivered': np.random.randint(0, 15, size=n_records)
})

# Multi-level aggregation with named outputs
summary_table = hcp_df.groupby(['Territory_ID', 'Specialty']).agg(
    Total_Brand_TRx=('Brand_TRx', 'sum'),
    Mean_Market_TRx=('Market_TRx', 'mean'),
    Total_Details=('Details_Delivered', 'sum'),
    HCP_Count=('Brand_TRx', 'count')
).reset_index()

# Calculate brand market share
summary_table['Brand_Market_Share'] = summary_table['Total_Brand_TRx'] / (summary_table['Mean_Market_Rx'] * summary_table['HCP_Count'])
```

### 3.3 Time-Series Feature Engineering for Forecasting
In pharmaceutical demand forecasting, temporal dependencies are captured using rolling windows, lag features, and exponential smoothing:

```python
# Assuming a weekly brand sales dataframe with DatetimeIndex
dates = pd.date_range(start='2024-01-01', periods=104, freq='W-MON')
sales_series = pd.DataFrame({
    'Week': dates,
    'Weekly_TRx': np.random.normal(5000, 400, size=104).cumsum() + 10000
}).set_index('Week')

# 1. Autoregressive Lags (Sales 1, 2, 4 weeks prior)
sales_series['Lag_1_TRx'] = sales_series['Weekly_TRx'].shift(1)
sales_series['Lag_2_TRx'] = sales_series['Weekly_TRx'].shift(2)
sales_series['Lag_4_TRx'] = sales_series['Weekly_TRx'].shift(4)

# 2. Rolling Moving Average & Volatility (4-week and 12-week smoothing)
sales_series['Rolling_4W_Mean'] = sales_series['Weekly_TRx'].rolling(window=4).mean()
sales_series['Rolling_4W_Std'] = sales_series['Weekly_TRx'].rolling(window=4).std()

# 3. Growth Velocity (4-week percentage change)
sales_series['TRx_Growth_4W'] = sales_series['Weekly_TRx'].pct_change(periods=4)
```

---

## 4. Scikit-Learn Pipelines & Time-Series Validation (Leakage Prevention)

### 4.1 Strict Time-Series Cross-Validation vs Random K-Fold
In commercial forecasting and Marketing Mix Modeling, **never use standard random `KFold` cross-validation**. Random K-Fold introduces severe **lookahead data leakage** by using future data to predict the past:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 TIME-SERIES CROSS-VALIDATION (FORWARD CHAINING)             │
│ Fold 1: [Train: Weeks 1–26 ] ---> [Test: Weeks 27–39]                      │
│ Fold 2: [Train: Weeks 1–39 ] ---> [Test: Weeks 40–52]                      │
│ Fold 3: [Train: Weeks 1–52 ] ---> [Test: Weeks 53–65]                      │
│ Fold 4: [Train: Weeks 1–65 ] ---> [Test: Weeks 66–78]                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.2 End-to-End Scikit-Learn Production Pipeline
```python
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.model_selection import TimeSeriesSplit, GridSearchCV

# Define column types
numeric_features = ['Details_Count', 'Digital_Impressions', 'Lag_1_Sales']
categorical_features = ['Region', 'Therapeutic_Class']

# Numeric pipeline: Impute missing medians + Z-score scaling
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# Categorical pipeline: Impute most frequent + One-Hot Encoding
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', drop='first'))
])

# Combine via ColumnTransformer
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)

# Full Model Pipeline
full_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', Ridge())
])

# Hyperparameter optimization using TimeSeriesSplit
param_grid = {'regressor__alpha': [0.1, 1.0, 10.0, 100.0]}
tscv = TimeSeriesSplit(n_splits=5)

grid_search = GridSearchCV(
    full_pipeline, 
    param_grid, 
    cv=tscv, 
    scoring='neg_mean_absolute_percentage_error',
    n_jobs=-1
)
```

---

## 5. Live Interview Coding Challenges & Solutions

### Challenge 1: Prescriber Deciling & Pareto Analysis
* **Task**: Given a DataFrame of 50,000 physicians and their annual brand prescription counts, compute the cumulative market volume share, assign physicians to deciles (1 to 10, where Decile 10 represents the highest prescribers), and verify whether the Pareto 80/20 rule holds.

```python
def assign_physician_deciles(df: pd.DataFrame, trx_col: str = 'Brand_TRx') -> pd.DataFrame:
    """Sorts physicians, calculates cumulative market share, and assigns deciles."""
    # 1. Sort descending by volume
    df_sorted = df.sort_values(by=trx_col, ascending=False).reset_index(drop=True)
    
    # 2. Calculate cumulative prescription volume and percentage
    total_trx = df_sorted[trx_col].sum()
    df_sorted['Cumulative_TRx'] = df_sorted[trx_col].cumsum()
    df_sorted['Cumulative_Share'] = df_sorted['Cumulative_TRx'] / total_trx
    
    # 3. Assign 10 Decile bins (Decile 10 = Top 10% high-volume prescribers)
    # Using pd.qcut on rank or explicit percentiles
    df_sorted['Decile'] = pd.qcut(
        df_sorted.index, 
        q=10, 
        labels=range(10, 0, -1)  # 10 is highest, 1 is lowest
    )
    
    # Check 80/20 Pareto principle
    top_20_pct_count = int(0.20 * len(df_sorted))
    share_top_20 = df_sorted.loc[top_20_pct_count, 'Cumulative_Share'] * 100
    print(f"Top 20% of physicians generate {share_top_20:.2f}% of total brand volume.")
    
    return df_sorted
```

