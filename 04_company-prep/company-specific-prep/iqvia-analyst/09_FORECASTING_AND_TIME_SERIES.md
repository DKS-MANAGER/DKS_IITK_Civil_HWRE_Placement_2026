# Module 09: Forecasting & Time-Series Analytics in Biopharma

> **Document Status**: High-Yield Theoretical & Practical Reference `[TIER 4 / ECONOMETRIC & TIME-SERIES STANDARDS]`  
> **Core Focus**: Time-Series Decomposition, Stationarity, ARIMA/SARIMAX, Holt-Winters, Bass Diffusion Launch Curves, and Patent Cliff Modeling  
> **Target Role**: Analyst (IQVIA India)  

---

## 1. Time-Series Anatomy & Commercial Decomposition

Pharmaceutical demand time-series exhibit distinct structural behaviors driven by chronic patient maintenance, acute seasonal illness (e.g., flu season), and life-cycle events:

$$Y_t = f(T_t, S_t, C_t, I_t)$$

* **Additive Decomposition**: Used when seasonal fluctuations remain constant in magnitude regardless of overall sales level:
  $$Y_t = T_t + S_t + I_t$$
* **Multiplicative Decomposition**: Used when seasonal swings scale proportionally with sales volume (standard in growing brand launches):
  $$Y_t = T_t \times S_t \times I_t \iff \ln(Y_t) = \ln(T_t) + \ln(S_t) + \ln(I_t)$$

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 PHARMACEUTICAL DEMAND TIME-SERIES TAXONOMY                  │
├──────────────────────┬──────────────────────┬───────────────────────────────┤
│ Metric               │ Clinical Nature      │ Forecasting Behavior          │
├──────────────────────┼──────────────────────┼───────────────────────────────┤
│ **New-to-Brand (NRx)**│ Patients starting a  │ Volatile, highly responsive to│
│                      │ new therapy          │ sales detailing, marketing mix│
├──────────────────────┼──────────────────────┼───────────────────────────────┤
│ **Total Rx (TRx)**   │ NRx + Refills/Repeats│ Inertial, stable, driven by   │
│                      │ (Chronic adherence)  │ patient persistence & history │
└──────────────────────┴──────────────────────┴───────────────────────────────┘
```

---

## 2. Stationarity, Autocorrelation & Order Identification

### 2.1 Covariance Stationarity
A time series $\{Y_t\}$ is weakly stationary iff:
1. $\mathbb{E}[Y_t] = \mu$ (Constant mean for all $t$).
2. $\text{Var}(Y_t) = \sigma^2 < \infty$ (Constant finite variance).
3. $\text{Cov}(Y_t, Y_{t-k}) = \gamma_k$ (Autocovariance depends only on lag $k$, not time $t$).

### 2.2 Testing Stationarity: Augmented Dickey-Fuller (ADF) Test
$$\Delta Y_t = \alpha + \beta t + \gamma Y_{t-1} + \sum_{i=1}^{p} \delta_i \Delta Y_{t-i} + \varepsilon_t$$
* $H_0: \gamma = 0$ (Unit root present; Series is non-stationary).
* $H_1: \gamma < 0$ (Stationary; reject $H_0$ if $p < 0.05$).
* If non-stationary, apply first-order differencing: $\Delta Y_t = Y_t - Y_{t-1}$ ($d = 1$).

### 2.3 Order Identification via ACF and PACF
```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       ACF & PACF SIGNATURE PATTERNS                         │
├───────────────┬─────────────────────────────┬───────────────────────────────┤
│ Process       │ Autocorrelation (ACF)       │ Partial Autocorrelation (PACF)│
├───────────────┼─────────────────────────────┼───────────────────────────────┤
│ **AR($p$)**   │ Exponential or damped decay │ Cuts off sharply after lag $p$│
│ **MA($q$)**   │ Cuts off sharply after lag $q$│ Exponential or damped decay   │
│ **ARMA($p,q$)**│ Damped sine wave / decay    │ Damped decay                  │
└───────────────┴─────────────────────────────┴───────────────────────────────┘
```

---

## 3. Mathematical Formulation: ARIMA & SARIMAX

### 3.1 Seasonal ARIMA (SARIMA) Model
$$\Phi_P(B^s)\phi_p(B)(1 - B)^d (1 - B^s)^D Y_t = \Theta_Q(B^s)\theta_q(B)\varepsilon_t$$
where:
* $B$ is the backshift operator ($B^k Y_t = Y_{t-k}$).
* $\phi_p(B) = 1 - \phi_1 B - \dots - \phi_p B^p$ (Non-seasonal AR).
* $\theta_q(B) = 1 + \theta_1 B + \dots + \theta_q B^q$ (Non-seasonal MA).
* $\Phi_P(B^s)$ and $\Theta_Q(B^s)$ are seasonal polynomial operators with periodicity $s$ (e.g., $s = 12$ for monthly, $s = 52$ for weekly).

### 3.2 SARIMAX (Dynamic Regression with Exogenous Drivers)
In commercial analytics, baseline ARIMA is augmented with exogenous marketing variables $\mathbf{X}_t$ (e.g., promotional spend, price cuts, competitor launch flags):
$$Y_t = \mathbf{X}_t \boldsymbol{\beta} + \eta_t, \qquad \Phi(B)\Delta^d \eta_t = \Theta(B)\varepsilon_t$$

---

## 4. Exponential Smoothing Models (Holt-Winters)

When data exhibits local trend and seasonality, **Holt-Winters Multiplicative** smoothing adapts dynamically:
1. **Level ($L_t$)**: $L_t = \alpha \left(\frac{Y_t}{S_{t-m}}\right) + (1 - \alpha)(L_{t-1} + b_{t-1})$
2. **Trend ($b_t$)**: $b_t = \beta (L_t - L_{t-1}) + (1 - \beta)b_{t-1}$
3. **Seasonal Index ($S_t$)**: $S_t = \gamma \left(\frac{Y_t}{L_t}\right) + (1 - \gamma)S_{t-m}$
4. **$h$-step Forecast ($\hat{Y}_{t+h}$)**: $\hat{Y}_{t+h} = (L_t + h b_t) \times S_{t-m+h_m^+}$

---

## 5. Pharmaceutical Product Lifecycle Dynamics

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 PHARMACEUTICAL BRAND VOLUME LIFECYCLE (TRx)                 │
│                                                                             │
│ Volume ▲                     Peak Sales Plateau                             │
│        │                       ┌───────────┐                                │
│        │                      /             \                               │
│        │    Bass Adoption    /               \  Patent Expiration           │
│        │      Launch Curve  /                 \ (The Patent Cliff)          │
│        │          ┌────────┘                   \═════════════►              │
│        │         /                              Generic Erosion             │
│        │        /                                                           │
│        └───────┴──────────────┴───────────────┴─────────────────► Time      │
│            Pre-Launch      Launch & Growth   Maturity      Loss of Exclus.  │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.1 Bass Diffusion Launch Forecasting
Before historical sales exist, new drug adoption is modeled using Frank Bass's diffusion equation:
$$\frac{dN(t)}{dt} = \left[ p + \frac{q}{M} N(t) \right] [M - N(t)]$$
* $M$: Total market carrying capacity (addressable patient population).
* $p$: Coefficient of innovation (early adopting physicians who prescribe based on clinical trial publications).
* $q$: Coefficient of imitation (physicians influenced by Key Opinion Leaders, peer networks, and sales detailing).

### 5.2 Loss of Exclusivity (LOE) & Generic Erosion Curves
When a small-molecule blockbuster patent expires, generic entrants enter at $70\text{–}90\%$ discounts. Volume erodes exponentially:
$$\text{TRx}_{\text{originator}}(t) = \text{TRx}_{\text{peak}} \times e^{-k \cdot t}$$
where $k$ is the decay rate calibrated by therapeutic substitution ease ($k \approx 0.15\text{–}0.30\text{ per month}$, resulting in $> 80\%$ volume loss within 6–12 months).

---

## 6. Forecast Accuracy Metrics & Out-of-Sample Validation

```python
import numpy as np

def calculate_forecast_metrics(y_true, y_pred):
    """Calculates MAE, RMSE, MAPE, and Forecast Bias."""
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    errors = y_true - y_pred
    
    mae = np.mean(np.abs(errors))
    rmse = np.sqrt(np.mean(errors**2))
    mape = np.mean(np.abs(errors / y_true)) * 100
    bias = np.mean(errors)  # Positive = under-forecasting; Negative = over-forecasting
    
    return {'MAE': mae, 'RMSE': rmse, 'MAPE_pct': mape, 'Bias': bias}
```

---

## 7. Python Implementation: End-to-End SARIMAX Brand Forecasting

```python
"""
Module 09: Pharmaceutical Sales SARIMAX Forecasting Pipeline
Fits an auto-regressive seasonal model on weekly brand sales with detailing spend.
"""
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.statespace.sarimax import SARIMAX

# 1. Synthesize 104 Weeks of Brand TRx with Seasonality & Detailing
np.random.seed(42)
dates = pd.date_range(start='2024-01-01', periods=104, freq='W-MON')
trend = np.linspace(2000, 4500, 104)
seasonality = 400 * np.sin(2 * np.pi * np.arange(104) / 52)  # Annual cycle
detailing_calls = np.random.poisson(lam=80, size=104)
promo_impact = 15.0 * detailing_calls
noise = np.random.normal(0, 150, size=104)

weekly_trx = trend + seasonality + promo_impact + noise
df = pd.DataFrame({'TRx': weekly_trx, 'Detailing': detailing_calls}, index=dates)

# 2. Train / Test Split (Strict Out-of-Sample Split: Last 12 Weeks)
train = df.iloc[:-12]
test = df.iloc[-12:]

# 3. Fit SARIMAX(1, 1, 1) x (1, 0, 0, 52) with Exogenous Detailing
model = SARIMAX(
    train['TRx'],
    exog=train[['Detailing']],
    order=(1, 1, 1),
    seasonal_order=(1, 0, 0, 52),
    enforce_stationarity=False,
    enforce_invertibility=False
).fit(disp=False)

# 4. Generate 12-Week Out-of-Sample Forecast
forecast = model.forecast(steps=12, exog=test[['Detailing']])
test_mape = np.mean(np.abs((test['TRx'] - forecast) / test['TRx'])) * 100

print(f"12-Week Out-of-Sample SARIMAX MAPE: {test_mape:.2f}%")
print(model.summary().tables[1])
```

