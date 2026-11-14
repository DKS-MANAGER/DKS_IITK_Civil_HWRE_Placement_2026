# Project 2: Retail SKU Demand Forecasting & Spoilage Optimization

**Domain:** Retail Supply Chain & Inventory Replenishment  
**Stack:** Python, Pandas, Statsmodels, SciPy, NumPy  
**Focus:** SARIMAX, Stationarity Diagnostics, Seasonality, WAPE Evaluation

---

## 1. Project Overview

This project builds an automated stochastic time-series demand forecasting pipeline for fast-moving retail SKUs subject to day-of-week seasonality, trend, and intermittent demand volatility.

### Key Technical Pillars:
1. **Statistical Diagnostics:** Augmented Dickey-Fuller (ADF) unit root testing to verify stationarity and guide differencing orders $(d, D)$.
2. **Seasonal Autoregressive Integrated Moving Average:** Fits $\text{SARIMA}(p, d, q) \times (P, D, Q)_7$ to capture weekly consumer shopping cycles.
3. **Probabilistic Uncertainty Estimation:** Generates 95% confidence intervals to size dynamic safety stock buffers.
4. **Volume-Weighted Evaluation:** Benchmarks forecast accuracy using Weighted Absolute Percentage Error (WAPE), eliminating the zero-division failure of MAPE.
5. **Candidate Synergy Anchor:** Direct mathematical transference from hydrological streamflow stochastic time-series and extreme flood recurrence modeling to retail demand volatility.

---

## 2. File Structure

- `forecast_demand.py`: Fully reproducible Python script simulating retail daily demand, checking stationarity, fitting SARIMAX, and computing 14-day forecasts.
- `interview_defense.md`: Interview defense guide detailing model selection, diagnostic tests, and business P&L alignment.
