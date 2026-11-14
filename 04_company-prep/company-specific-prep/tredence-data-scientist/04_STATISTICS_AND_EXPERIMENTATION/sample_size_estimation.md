# Sample Size Estimation & Power Calculations

**Target Role:** Data Scientist / Associate Data Scientist | Tredence Analytics  
**Context:** IIT Kanpur Placement Season 2026–27  
**Prerequisites:** Central Limit Theorem, Hypothesis Testing ($\alpha, \beta$), Effect Sizes

---

## 1. Mathematical Derivation of Sample Size

### 1.1 Continuous Metrics (e.g., Average Order Value, Revenue per User)
Consider an independent two-sample test comparing Control ($C$) and Treatment ($T$):
$$H_0: \mu_T - \mu_C = 0 \quad \text{vs} \quad H_1: \mu_T - \mu_C = \delta \ (\delta \ne 0)$$
Assume equal sample size $n_C = n_T = n$ and common variance $\sigma^2$.

Under $H_0$, the difference in sample means $\bar{X}_T - \bar{X}_C$ follows:
$$\bar{X}_T - \bar{X}_C \sim \mathcal{N}\left(0, \frac{2\sigma^2}{n}\right)$$
Critical threshold for significance level $\alpha$ (two-tailed):
$$\text{Threshold} = Z_{1 - \alpha/2} \sqrt{\frac{2\sigma^2}{n}}$$

Under $H_1$, the distribution is centered at true effect $\delta$:
$$\bar{X}_T - \bar{X}_C \sim \mathcal{N}\left(\delta, \frac{2\sigma^2}{n}\right)$$
To detect this difference with power $1 - \beta$, the critical threshold must lie $Z_{1 - \beta}$ standard errors below $\delta$:
$$\delta - Z_{1 - \beta} \sqrt{\frac{2\sigma^2}{n}} = Z_{1 - \alpha/2} \sqrt{\frac{2\sigma^2}{n}}$$

Equating and factoring out standard error:
$$\delta = \left(Z_{1 - \alpha/2} + Z_{1 - \beta}\right) \sqrt{\frac{2\sigma^2}{n}}$$

Squaring both sides and solving for sample size per variant $n$:

$$n = \frac{2 \sigma^2 \left(Z_{1 - \alpha/2} + Z_{1 - \beta}\right)^2}{\delta^2} = \frac{2 \left(Z_{1 - \alpha/2} + Z_{1 - \beta}\right)^2}{\left(\frac{\delta}{\sigma}\right)^2}$$

Where:
- $\delta / \sigma$: Cohen's $d$ (Standardized Effect Size).
- For $\alpha = 0.05$ (two-tailed), $Z_{1 - \alpha/2} = 1.96$.
- For Power $= 0.80$, $\beta = 0.20 \implies Z_{1 - \beta} = 0.8416$.
- Numerator factor: $(1.96 + 0.8416)^2 = (2.8016)^2 \approx 7.85 \implies n \approx \frac{15.7 \sigma^2}{\delta^2}$.

---

### 1.2 Binary Metrics (e.g., Conversion Rate, Click-Through Rate)
For baseline conversion rate $p_1$ and expected treatment conversion rate $p_2 = p_1 + \delta$:
Pooled variance under $H_0$: $\bar{p} = \frac{p_1 + p_2}{2}, \quad \sigma_0^2 = 2\bar{p}(1 - \bar{p})$.  
Variance under $H_1$: $\sigma_1^2 = p_1(1 - p_1) + p_2(1 - p_2)$.

**Standard Normal Approximation Formula (Evan Miller Formulation):**
$$n = \frac{\left(Z_{1 - \alpha/2}\sqrt{2\bar{p}(1 - \bar{p})} + Z_{1 - \beta}\sqrt{p_1(1 - p_1) + p_2(1 - p_2)}\right)^2}{\delta^2}$$

*Simplified Operational Rule of Thumb:*
$$n \approx \frac{16 \cdot p_1(1 - p_1)}{\delta^2}$$

---

## 2. Minimum Detectable Effect (MDE)

The **Minimum Detectable Effect (MDE)** is the smallest true lift that an experiment has an $80\%$ probability of confirming at $\alpha = 0.05$.

- **Absolute MDE:** $\delta = p_2 - p_1$.
- **Relative MDE:** $\delta_{\text{rel}} = \frac{p_2 - p_1}{p_1} \implies \delta = p_1 \cdot \delta_{\text{rel}}$.

**Inverse Scaling Law:**
$$\text{Sample Size } n \propto \frac{1}{\text{MDE}^2}$$
*Impact:* If business leadership demands detecting a 1% relative lift instead of a 5% relative lift, the required sample size does not increase by $5\times$; it increases by $5^2 = 25\times$.

---

## 3. Practical Enterprise Experimentation Adjustments

1. **Test Duration Rules:**
   - **Never run for fewer than 7 days** regardless of traffic velocity. Customer purchase patterns exhibit severe day-of-week seasonality (e.g., Friday paydays, weekend mobile browsing).
   - Recommended horizon: 14 to 28 days (captures 2 to 4 full business cycles).
   - Running beyond 4 weeks introduces cookie churn, browser storage clearance, and market contamination.

2. **Cluster / Unequal Traffic Splitting ($k = n_T / n_C \ne 1$):**
   If business risk restricts treatment exposure to 10% traffic ($k = 0.1$):
   $$n_{\text{total}} = n_{\text{equal\_total}} \times \frac{(k + 1)^2}{4k}$$
   For $k = 0.1$, $\frac{1.1^2}{0.4} = 3.025 \implies$ requires **$3\times$ total user sample size** compared to a 50/50 balanced split.

---

## 4. Production Python Power Calculation Implementation

```python
import numpy as np
from scipy import stats
from statsmodels.stats.power import NormalIndPower, TTestIndPower

def calculate_proportions_sample_size(p1: float, mde_rel: float, alpha: float = 0.05, power: float = 0.80) -> dict:
    """
    Computes required sample size per variant for a binary proportion test.
    """
    p2 = p1 * (1 + mde_rel)
    delta = abs(p2 - p1)
    
    # Standard Cohen's h effect size for proportions
    h = 2 * (np.arcsin(np.sqrt(p1)) - np.arcsin(np.sqrt(p2)))
    
    power_analysis = NormalIndPower()
    n_per_variant = power_analysis.solve_power(effect_size=abs(h), alpha=alpha, power=power, alternative='two-sided')
    n_required = int(np.ceil(n_per_variant))
    
    return {
        "baseline_rate": p1,
        "treatment_rate": p2,
        "relative_mde": f"{mde_rel:.1%}",
        "sample_size_per_variant": n_required,
        "total_sample_size": n_required * 2
    }

# Example: Baseline conversion 5%, want to detect 5% relative lift (from 5.0% to 5.25%)
res = calculate_proportions_sample_size(p1=0.05, mde_rel=0.05)
print(res)
# {'baseline_rate': 0.05, 'treatment_rate': 0.0525, 'relative_mde': '5.0%', 
#  'sample_size_per_variant': 122134, 'total_sample_size': 244268}
```
