# 02 — Exploratory Data Analysis & Diagnostic Visualization
## Structured EDA Frameworks, Missingness Diagnostics, Outlier Treatment & Seaborn Visualizations

> **Document Status**: Technical Core Curriculum `[TIER 5 / PEDAGOGICAL MODULE]`

---

## 1. The 5-Step Production EDA Protocol

At Tredence, exploratory data analysis is not ad-hoc plotting; it is an auditable, reproducible diagnostic pipeline:

```python
import pandas as pd
import numpy as np

def comprehensive_eda_audit(df: pd.DataFrame) -> dict:
    """
    Executes a structured 5-step data quality and exploratory audit.
    Returns audit dictionary and prints formatted diagnostic summary.
    """
    print("=" * 80)
    print("TREDENCE ENTERPRISE DATA AUDIT & EDA REPORT")
    print("=" * 80)

    # Step 1: Shape and Memory
    n_rows, n_cols = df.shape
    mem_mb = df.memory_usage(deep=True).sum() / (1024**2)
    print(f"\n[1] DATASET DIMENSIONS: {n_rows:,} Rows | {n_cols} Columns | Memory Footprint: {mem_mb:.2f} MB")

    # Step 2: Column Types & Cardinality
    type_counts = df.dtypes.value_counts().to_dict()
    print(f"[2] DATA TYPES DISTRIBUTION: {type_counts}")

    # Step 3: Missingness Breakdown
    missing = df.isnull().sum()
    missing_pct = (missing / n_rows) * 100
    missing_df = pd.DataFrame({'Missing_Count': missing, 'Pct': missing_pct})
    missing_df = missing_df[missing_df['Missing_Count'] > 0].sort_values(by='Pct', ascending=False)
    print("\n[3] MISSING VALUE AUDIT:")
    if missing_df.empty:
        print("    No missing values detected across all columns.")
    else:
        print(missing_df.to_string())

    # Step 4: Duplicate Records
    n_duplicates = int(df.duplicated().sum())
    print(f"\n[4] DUPLICATE ROWS: {n_duplicates:,} ({n_duplicates/n_rows:.2%})")

    # Step 5: Numerical Statistics
    numeric_df = df.select_dtypes(include=[np.number])
    stats_df = None
    if not numeric_df.empty:
        stats_df = numeric_df.describe(percentiles=[0.01, 0.05, 0.25, 0.50, 0.75, 0.95, 0.99]).T
        stats_df['skewness'] = numeric_df.skew()
        stats_df['kurtosis'] = numeric_df.kurtosis()
        print("\n[5] NUMERICAL COLUMN SUMMARY:")
        print(stats_df[['mean', 'std', '50%', '99%', 'skewness']].to_string())

    print("=" * 80)
    return {
        'shape': (n_rows, n_cols),
        'missing': missing_df,
        'duplicates': n_duplicates,
        'numerical_stats': stats_df
    }
```

---

## 2. Missingness Mechanisms & Imputation Strategies

Data missingness is categorized into three mechanisms (Rubin's Taxonomy):
1. **Missing Completely at Random (MCAR)**: Missingness probability is entirely independent of observed and unobserved data. Imputation: Mean, median, or deletion if < 3%.
2. **Missing at Random (MAR)**: Missingness probability depends on observed features (e.g., younger customers less likely to report income). Imputation: Iterative Imputer (MICE) or MissForest.
3. **Missing Not at Random (MNAR)**: Missingness depends on the unobserved value itself (e.g., high-income earners refusing to disclose income). Imputation: Explicit missingness indicator flag + median imputation.

---

## 3. Outlier Detection & Treatment

```python
def treat_outliers_iqr(df: pd.DataFrame, col: str, multiplier: float = 1.5) -> pd.DataFrame:
    """
    Applies Tukey's fences using Interquartile Range (IQR).
    Clamps extreme values to upper and lower fences.
    """
    df = df.copy()
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_fence = Q1 - multiplier * IQR
    upper_fence = Q3 + multiplier * IQR

    outliers_count = ((df[col] < lower_fence) | (df[col] > upper_fence)).sum()
    df[col] = df[col].clip(lower=lower_fence, upper=upper_fence)
    print(f"Capped {outliers_count:,} outliers in '{col}' to bounds [{lower_fence:.2f}, {upper_fence:.2f}].")
    return df
```
