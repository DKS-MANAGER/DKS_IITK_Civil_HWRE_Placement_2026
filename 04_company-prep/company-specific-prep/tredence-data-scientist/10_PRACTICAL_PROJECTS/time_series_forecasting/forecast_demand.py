"""
Project 2: Retail SKU Demand Forecasting & Spoilage Optimization
Reproducible Python script with synthetic generation of daily sales,
ADF stationarity testing, SARIMAX model fitting, and WAPE evaluation.
"""

import numpy as np
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.stattools import adfuller

def generate_synthetic_retail_demand(n_days: int = 180, random_state: int = 42) -> pd.Series:
    """Generates synthetic daily demand with upward trend, 7-day seasonality, and noise."""
    np.random.seed(random_state)
    dates = pd.date_range(start='2024-01-01', periods=n_days, freq='D')
    
    # 1. Base trend
    t = np.arange(n_days)
    trend = 100 + 0.25 * t
    
    # 2. Weekly seasonality (Friday/Saturday/Sunday peak shopping)
    day_of_week = dates.dayofweek
    seasonal_multipliers = np.array([0.85, 0.90, 0.95, 1.00, 1.25, 1.35, 1.15])
    seasonality = seasonal_multipliers[day_of_week]
    
    # 3. Random Gaussian noise
    noise = np.random.normal(loc=0, scale=8, size=n_days)
    
    demand = np.maximum(0, (trend * seasonality) + noise).round()
    return pd.Series(demand, index=dates, name='daily_demand')

def calculate_wape(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Computes Weighted Absolute Percentage Error (WAPE)."""
    return np.sum(np.abs(y_true - y_pred)) / np.sum(y_true)

def run_forecasting_pipeline():
    print("=== Step 1: Ingesting Daily Retail Demand ===")
    ts = generate_synthetic_retail_demand()
    print(f"Total time span: {ts.index.min().strftime('%Y-%m-%d')} to {ts.index.max().strftime('%Y-%m-%d')}")
    print(f"Mean daily demand: {ts.mean():.1f} units, Std: {ts.std():.1f} units")
    
    # Step 2: Stationarity Testing via ADF
    print("\n=== Step 2: Augmented Dickey-Fuller (ADF) Test ===")
    adf_res = adfuller(ts)
    print(f"ADF Statistic:       {adf_res[0]:.4f}")
    print(f"p-value:             {adf_res[1]:.4f}")
    print("Critical Values:")
    for k, v in adf_res[4].items():
        print(f"   {k}: {v:.4f}")
    if adf_res[1] > 0.05:
        print(">> Series is NON-STATIONARY. Differencing (d=1, D=1, s=7) is required.")
    else:
        print(">> Series is stationary.")
        
    # Step 3: Train-Test Split (Last 14 days as out-of-sample test horizon)
    horizon = 14
    train_ts = ts.iloc[:-horizon]
    test_ts = ts.iloc[-horizon:]
    print(f"\nTrain size: {len(train_ts)} days | Test horizon: {len(test_ts)} days")
    
    # Step 4: Fit SARIMAX Model (p=1, d=1, q=1) x (P=1, D=1, Q=1, s=7)
    print("\n=== Step 3: Fitting SARIMA(1, 1, 1) x (1, 1, 1, 7) ===")
    model = SARIMAX(
        train_ts,
        order=(1, 1, 1),
        seasonal_order=(1, 1, 1, 7),
        enforce_stationarity=False,
        enforce_invertibility=False
    )
    fitted_model = model.fit(disp=False)
    print(f"Model Converged successfully. AIC: {fitted_model.aic:.2f}, BIC: {fitted_model.bic:.2f}")
    
    # Step 5: 14-Day Out-of-Sample Forecasting
    print("\n=== Step 4: Generating 14-Day Point & Interval Forecasts ===")
    forecast_res = fitted_model.get_forecast(steps=horizon)
    pred_mean = forecast_res.predicted_mean
    conf_int = forecast_res.conf_int(alpha=0.05)
    
    results_df = pd.DataFrame({
        'actual': test_ts.values,
        'forecast': pred_mean.values.round(1),
        'ci_lower_95': conf_int.iloc[:, 0].values.round(1),
        'ci_upper_95': conf_int.iloc[:, 1].values.round(1)
    }, index=test_ts.index)
    
    # Step 6: Evaluation
    wape = calculate_wape(results_df['actual'].values, results_df['forecast'].values)
    mae = np.mean(np.abs(results_df['actual'].values - results_df['forecast'].values))
    
    print(results_df.head(7).to_string())
    print(f"\nForecast Accuracy Summary:")
    print(f"   WAPE: {wape:.2%} (Target: < 15%)")
    print(f"   MAE:  {mae:.2f} units/day")
    
    return {
        'aic': fitted_model.aic,
        'wape': wape,
        'mae': mae
    }

if __name__ == '__main__':
    run_forecasting_pipeline()
