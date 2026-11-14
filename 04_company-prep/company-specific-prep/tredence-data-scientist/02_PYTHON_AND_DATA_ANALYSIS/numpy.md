# 02 — NumPy: Vectorization, Broadcasting & Numerical Computing
## High-Performance Matrix Operations, Memory Strides & Numerical Stability

> **Document Status**: Technical Core Curriculum `[TIER 5 / PEDAGOGICAL MODULE]`

---

## 1. Array Memory Architecture & Vectorization

Python lists store arrays of pointers to individual boxed integer/float objects, creating pointer indirection overhead and cache thrashing. In contrast, a NumPy `ndarray` represents a contiguous block of homogeneous memory in C order (row-major) or Fortran order (column-major).

```
Python List:  [Ptr] ──> [Int Object (28 bytes)]
              [Ptr] ──> [Int Object (28 bytes)]
              [Ptr] ──> [Int Object (28 bytes)]

NumPy Array:  [Int32 | Int32 | Int32 | Int32] (Contiguous 16 bytes in CPU L1 Cache)
```

### 1.1 Vectorized Calculation vs Python Loop Benchmark
```python
import numpy as np
import time

n_elements = 1_000_000
python_list = list(range(n_elements))
numpy_array = np.arange(n_elements, dtype=np.float64)

# Native Python Loop: ~65ms
start = time.perf_counter()
res_list = [x**2 + 2*x + 1 for x in python_list]
loop_time = time.perf_counter() - start

# Vectorized NumPy (SIMD vector instructions): ~2ms (30x faster)
start = time.perf_counter()
res_np = numpy_array**2 + 2*numpy_array + 1
vector_time = time.perf_counter() - start

print(f"Loop Time: {loop_time:.4f}s | Vector Time: {vector_time:.4f}s | Speedup: {loop_time/vector_time:.1f}x")
```

---

## 2. The Strict Rules of NumPy Broadcasting

Two dimensions are compatible for broadcasting if:
1. They are equal, OR
2. One of them is 1.

If arrays have different numbers of dimensions, prepend dimensions of size 1 to the smaller array's shape until shapes match.

```python
# Example: Normalizing a feature matrix X by feature means
X = np.array([
    [10.0, 200.0, 3000.0],
    [20.0, 400.0, 5000.0],
    [30.0, 600.0, 7000.0]
]) # Shape (3, 3)

feature_means = np.array([20.0, 400.0, 5000.0]) # Shape (3,) -> Broadcasts to (1, 3) -> (3, 3)
X_centered = X - feature_means

# Column-wise normalization (subtract mean of each row across time)
row_means = X.mean(axis=1, keepdims=True) # Shape (3, 1) -> Broadcasts across columns (3, 3)
X_row_normalized = X - row_means
```

---

## 3. Numerical Stability in Machine Learning: The Log-Sum-Exp Trick

When computing softmax probabilities in multiclass classification or logistic regression, evaluating $e^{z_i}$ for large logits causes arithmetic overflow (`inf`), while large negative values cause underflow to zero.

$$\text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_{j=1}^K e^{z_j}} = \frac{e^{z_i - c}}{\sum_{j=1}^K e^{z_j - c}}, \quad \text{where } c = \max(z)$$

```python
def stable_softmax(logits: np.ndarray) -> np.ndarray:
    """
    Computes numerically stable softmax along the last dimension.
    Prevents floating point overflow by subtracting max logit.
    """
    c = np.max(logits, axis=-1, keepdims=True)
    exp_shifted = np.exp(logits - c)
    sum_exp = np.sum(exp_shifted, axis=-1, keepdims=True)
    return exp_shifted / sum_exp

# Test extreme values
large_logits = np.array([1000.0, 1005.0, 1010.0])
# Naive np.exp(large_logits) -> [inf, inf, inf] -> [nan, nan, nan]
probs = stable_softmax(large_logits)
assert np.allclose(probs.sum(), 1.0)
print("Stable Softmax Probabilities:", np.round(probs, 4)) # [0.0001, 0.0067, 0.9932]
```
