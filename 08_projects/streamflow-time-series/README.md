# Project: Hydrological Streamflow Time-Series Modeling & Forecasting

> **Project Code**: `streamflow-time-series`  
> **Domain**: Surface Water Hydrology, Time-Series Analysis & Machine Learning  
> **Key Tools**: Python (Pandas, Scikit-Learn, PyTorch, Statsmodels), HEC-HMS, Hydroinformatics

---

## 1. Project Overview & Motivation

Accurate multi-day streamflow forecasting is essential for reservoir operation, hydropower generation scheduling, flood warning, and drought management. While physically based distributed hydrological models (e.g., SWAT, HEC-HMS) require extensive spatial meteorological and soil parameters, data-driven deep learning models (LSTM, GRU) can capture non-linear hydrological lag and catchment memory effects directly from hydro-meteorological time-series data.

### Core Objectives:
1. Process and decompose 20+ years of daily discharge, precipitation, and temperature time-series data.
2. Build and compare statistical benchmark models (ARIMA, SARIMAX) against Long Short-Term Memory (LSTM) recurrent neural networks.
3. Evaluate model generalizability during extreme monsoon flood peaks and low-flow dry seasons using hydrological metrics (NSE, KGE, RMSE).

---

## 2. Technical Methodology & Architecture

```text
[Daily Rainfall & Runoff Data] ──► [Feature Engineering: Lags & Rolling Averages]
                                                  │
                 ┌────────────────────────────────┴────────────────────────────────┐
                 ▼                                                                 ▼
      [Statistical Baseline: SARIMAX]                                   [Deep Learning: LSTM / GRU]
                 │                                                                 │
                 └────────────────────────────────┬────────────────────────────────┘
                                                  ▼
                         [Model Evaluation: NSE, KGE, PBIAS, RMSE]
```

### Key Performance Metrics:
* **Nash-Sutcliffe Efficiency (NSE)**:
  $$NSE = 1 - \frac{\sum_{t=1}^T (Q_o^t - Q_m^t)^2}{\sum_{t=1}^T (Q_o^t - \overline{Q_o})^2}$$
* **Kling-Gupta Efficiency (KGE)**: Decomposes correlation, bias, and variability ratio.

---

## 3. Results & Comparative Performance

| Model Architecture | Lead Time | NSE (Calibration) | NSE (Testing) | Peak Discharge Error (%) |
| :--- | :---: | :---: | :---: | :---: |
| **ARIMA (2,1,2)** | 1-Day | 0.68 | 0.61 | -24.5% |
| **SARIMAX (Rainfall exogenous)**| 1-Day | 0.76 | 0.71 | -16.2% |
| **Stacked LSTM (2-Layer)** | 1-Day | **0.91** | **0.88** | **-5.4%** |
| **Stacked LSTM (2-Layer)** | 3-Day | 0.82 | 0.79 | -11.8% |

* **Key Finding**: The LSTM model demonstrated superior ability to capture non-linear catchment storage release dynamics and hydrograph recession limbs compared to linear time-series methods.

---

## 4. Interview Defense & Technical Q&A

### Q1: "Why does LSTM outperform traditional physical models in streamflow forecasting?"
* **Answer**: *"LSTMs contain memory cells and forget gates that inherently retain past precipitation history over variable lag times (representing groundwater and soil moisture storage). Unlike conceptual lumped models that rely on simplified empirical infiltration parameters, LSTMs learn complex multi-temporal catchment memory without requiring explicit soil parameterization."*

### Q2: "How did you prevent data leakage in time-series train/test splitting?"
* **Answer**: *"I used strict chronological splitting (first 70% of years for training, 15% validation, final 15% testing) without random shuffling. All feature scalers (MinMaxScaler) were fitted strictly on the training set to prevent future information leakage into test splits."*
