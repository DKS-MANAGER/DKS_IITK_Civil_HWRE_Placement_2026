# 02 — Python Fundamentals for Data Scientists
## Object-Oriented Programming, Generators, Decorators, Exception Handling & Memory Management

> **Document Status**: Technical Core Curriculum `[TIER 5 / PEDAGOGICAL MODULE]`  
> **Target Role**: Data Scientist / Associate Data Scientist | Tredence Analytics

---

## 1. Object-Oriented Programming (OOP) in Data Science

In production enterprise analytics at Tredence, data scientists cannot rely on monolithic, one-off scripts. Machine learning components, feature transformers, and evaluation engines must be encapsulated as reusable, stateful classes compatible with Scikit-learn or PySpark architectures.

### 1.1 Custom Transformer Architecture
A production-grade feature engineering class implementing the Scikit-learn `BaseEstimator` and `TransformerMixin` interface:

```python
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class OutlierCapper(BaseEstimator, TransformerMixin):
    """
    Clamps numerical feature values between lower and upper quantile thresholds.
    Fits thresholds on training data to prevent out-of-sample data leakage.
    """
    def __init__(self, lower_quantile: float = 0.01, upper_quantile: float = 0.99):
        self.lower_quantile = lower_quantile
        self.upper_quantile = upper_quantile
        self.bounds_ = {}

    def fit(self, X: pd.DataFrame, y=None):
        X_df = pd.DataFrame(X)
        for col in X_df.select_dtypes(include=[np.number]).columns:
            q_low = X_df[col].quantile(self.lower_quantile)
            q_high = X_df[col].quantile(self.upper_quantile)
            self.bounds_[col] = (q_low, q_high)
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X_out = pd.DataFrame(X).copy()
        for col, (q_low, q_high) in self.bounds_.items():
            if col in X_out.columns:
                X_out[col] = X_out[col].clip(lower=q_low, upper=q_high)
        return X_out
```

---

## 2. Iterators, Generators & Memory-Efficient Processing

When processing multi-gigabyte transaction logs (e.g., retail POS receipts or telecom call detail records), loading an entire CSV into memory causes `MemoryError` crashes. Generators provide lazy evaluation:

```python
from typing import Generator, Dict, Any
import csv

def stream_large_transaction_csv(file_path: str, chunk_filter_col: str, filter_val: str) -> Generator[Dict[str, Any], None, None]:
    """
    Streams a large CSV line-by-line without loading the full file into RAM.
    Yields parsed records matching specific filter criteria.
    """
    with open(file_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get(chunk_filter_col) == filter_val:
                yield {
                    'transaction_id': int(row['transaction_id']),
                    'customer_id': int(row['customer_id']),
                    'amount': float(row['amount']),
                    'store_id': row['store_id']
                }

# Usage: Process 50GB file in O(1) memory
# for record in stream_large_transaction_csv('raw_pos.csv', 'store_id', 'STR_104'):
#     process_transaction(record)
```

---

## 3. Function Decorators in MLOps & Production Pipelines

Decorators enable non-invasive logging, execution latency profiling, and exception handling across production analytical pipelines:

```python
import time
import functools
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def timer_and_audit(func):
    """
    Decorator that measures execution time and logs input argument dimensions.
    Essential for monitoring latency in real-time inference endpoints.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        logging.info(f"Executing '{func.__name__}' with {len(args)} positional args and {list(kwargs.keys())}.")
        try:
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - start_time
            logging.info(f"Finished '{func.__name__}' in {elapsed:.4f}s.")
            return result
        except Exception as e:
            logging.error(f"Error in '{func.__name__}': {str(e)}")
            raise e
    return wrapper

@timer_and_audit
def train_baseline_model(X_train: np.ndarray, y_train: np.ndarray):
    # Simulated model fitting
    time.sleep(0.15)
    return "Model Trained Successfully"
```

---

## 4. Python Memory Management & Mutability Pitfalls

### 4.1 Shallow vs Deep Copying
```python
import copy

# Mutable default argument trap
def append_prediction(score: float, registry: list = None) -> list:
    if registry is None:
        registry = []  # Correct pattern: avoids shared list mutation across calls
    registry.append(score)
    return registry

# Deep copying nested data structures
original_config = {'model': 'LightGBM', 'params': {'learning_rate': 0.05, 'max_depth': 6}}
shallow_copy = original_config.copy()
deep_copy = copy.deepcopy(original_config)

shallow_copy['params']['max_depth'] = 8
# Notice: original_config['params']['max_depth'] is now 8!
assert original_config['params']['max_depth'] == 8
assert deep_copy['params']['max_depth'] == 6  # Deep copy remains unmutated
```
