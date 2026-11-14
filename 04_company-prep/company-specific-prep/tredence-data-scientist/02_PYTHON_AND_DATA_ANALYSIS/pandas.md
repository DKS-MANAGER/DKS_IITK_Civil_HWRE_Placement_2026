# 02 — Pandas: Advanced Data Wrangling & Memory Optimization
## Production Grouping, Window Transformations, Missingness & Pipeline Design

> **Document Status**: Technical Core Curriculum `[TIER 5 / PEDAGOGICAL MODULE]`

---

## 1. Memory Optimization & Type Downcasting

Loading multi-million-row enterprise tables with default `int64` and `float64` types exhausts RAM. Downcasting to appropriate integer/float widths and converting repetitive string columns to `category` achieves an **80–90% reduction in memory footprint**:

```python
import pandas as pd
import numpy as np

def optimize_dataframe_memory(df: pd.DataFrame, verbose: bool = True) -> pd.DataFrame:
    """
    Iterates through all columns and downcasts numeric types to minimum memory-safe width.
    Converts low-cardinality object columns to categorical dtype.
    """
    start_mem = df.memory_usage().sum() / 1024**2
    df = df.copy()

    for col in df.columns:
        col_type = df[col].dtype

        if col_type != object and not pd.api.types.is_categorical_dtype(df[col]):
            c_min = df[col].min()
            c_max = df[col].max()

            if str(col_type)[:3] == 'int':
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
            elif str(col_type)[:5] == 'float':
                if c_min > np.finfo(np.float32).min and c_max < np.finfo(np.float32).max:
                    df[col] = df[col].astype(np.float32)
        elif col_type == 'object':
            num_unique = len(df[col].unique())
            num_total = len(df[col])
            # If unique ratio < 50%, convert to category
            if num_unique / num_total < 0.5:
                df[col] = df[col].astype('category')

    end_mem = df.memory_usage().sum() / 1024**2
    if verbose:
        print(f"Memory decreased from {start_mem:.2f} MB to {end_mem:.2f} MB ({100 * (start_mem - end_mem) / start_mem:.1f}% reduction)")
    return df
```

---

## 2. Advanced GroupBy: `agg()` vs `transform()` vs `apply()`

```python
# Create sample retail dataset
data = {
    'store_id': ['S1', 'S1', 'S1', 'S2', 'S2', 'S2'],
    'category': ['Grocery', 'Electronics', 'Grocery', 'Grocery', 'Electronics', 'Electronics'],
    'sales': [120.0, 450.0, 180.0, 95.0, 520.0, 610.0]
}
df = pd.DataFrame(data)

# 1. agg(): Reduces each group to summary statistics (changes output shape)
summary = df.groupby('store_id')['sales'].agg(['mean', 'std', 'max'])

# 2. transform(): Returns an array of identical shape to the original dataframe!
# Essential for feature engineering: computing deviation from store average
df['store_mean_sales'] = df.groupby('store_id')['sales'].transform('mean')
df['sales_pct_of_store_mean'] = (df['sales'] / df['store_mean_sales']) * 100

# 3. Time-series rolling within group
# df['store_rolling_7d'] = df.groupby('store_id')['sales'].rolling(window=7, min_periods=1).mean().reset_index(0, drop=True)
```

---

## 3. High-Performance Multi-Table Merging & Join Integrity

In analytics consulting, joining large tables without validating cardinality leads to silent Cartesian explosions.

```python
# Strict merge validation: ensures 1-to-many or 1-to-1 relationships
orders = pd.DataFrame({'order_id': [1, 2, 3], 'customer_id': [101, 102, 103], 'amount': [50, 120, 80]})
customers = pd.DataFrame({'customer_id': [101, 102, 103], 'segment': ['Retail', 'Wholesale', 'Retail']})

# Validate validate='many_to_one' raises MergeError if customer_id is duplicated in customers table!
merged = pd.merge(orders, customers, on='customer_id', how='left', validate='many_to_one')
assert len(merged) == len(orders), "Merge created unintended duplicate rows!"
```
