# Quantified Results & Comparative Model Metrics — `streamflow-time-series`

> **Project Code**: `streamflow-time-series`  
> **Key Metrics**: Nash-Sutcliffe Efficiency (NSE), Kling-Gupta Efficiency (KGE), Percent Bias (PBIAS), Peak Discharge Relative Error (%).

---

## 1. 1-Day Lead Time Comparative Performance (Test Set)

| Model Name | Training Architecture | Test NSE | Test KGE | PBIAS (%) | RMSE ($\text{m}^3/\text{s}$) | Peak Timing Error |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Persistence (Naïve)** | $Q_t = Q_{t-1}$ | 0.52 | 0.48 | +2.1% | 48.2 | +1 Day Lag |
| **ARIMA (2,1,2)** | Unvariate autoregressive | 0.61 | 0.58 | -8.4% | 41.5 | +1 Day Lag |
| **SARIMAX** | Exogenous daily rainfall | 0.71 | 0.68 | -6.2% | 34.8 | 0 Day |
| **Conceptual (HEC-HMS)** | SCS-CN & Clark Hydrograph | 0.78 | 0.75 | -4.8% | 29.4 | 0 Day |
| **Vanilla GRU** | 64 units, 14-day window | 0.84 | 0.82 | -3.5% | 24.1 | 0 Day |
| **Stacked LSTM (2-Layer)**| 64 units, 14-day window | **0.88** | **0.87** | **-2.1%** | **20.8** | **0 Day** |

---

## 2. Multi-Day Lead Time Forecasting Degradation

| Forecasting Horizon | LSTM Test NSE | LSTM Test KGE | Peak Discharge Error (%) |
| :---: | :---: | :---: | :---: |
| **1-Day Ahead** | **0.88** | **0.87** | -5.4% |
| **2-Day Ahead** | 0.83 | 0.81 | -8.9% |
| **3-Day Ahead** | 0.79 | 0.76 | -11.8% |
| **5-Day Ahead** | 0.71 | 0.67 | -18.2% |
| **7-Day Ahead** | 0.64 | 0.60 | -25.6% |

---

## 3. Key Engineering Findings

1. **Recession Curve Tracking**: The LSTM model achieved near-perfect hydrograph recession limb tracking ($R^2 = 0.93$), demonstrating that recurrent memory cells effectively replicate groundwater baseflow release dynamics.
2. **Computational Speedup**: Once trained, the deep learning inference engine generated a 7-day river forecast in under $0.5\text{ seconds}$ compared to $4\text{ minutes}$ for a distributed physical model run, enabling real-time automated reservoir rule-curve management.
