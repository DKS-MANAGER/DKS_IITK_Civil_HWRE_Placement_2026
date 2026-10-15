# Archetype 2: Catchment Streamflow & Hydrological Time-Series Forecasting

> **Domain**: Hydrology / Time-Series Analysis / Statistical & Machine Learning  
> **Status**: [HYPOTHETICAL ENGINEERING CASE ARCHETYPE — SAMPLE FOR INTERVIEW PRACTICE]  
> **Purpose**: Demonstrates systematic time-series methodology, statistical stationarity testing, model comparison, and rigorous evaluation metrics without referencing personal research data or proprietary streams.

---

## 1. Executive Summary & Problem Formulation

* **Engineering Challenge**: Catchment runoff exhibits complex nonlinear dynamics driven by seasonal rainfall patterns, antecedent soil moisture, evapotranspiration, and basin geomorphology. Accurate multi-day lead-time streamflow forecasting is essential for reservoir dispatch, flood early warning, and drought management.
* **Objective**: Build a comparative modeling framework comparing classical statistical time-series methods (ARIMA/SARIMAX), gradient boosting (XGBoost/LightGBM), and recurrent neural networks (LSTM) for daily river discharge prediction.
* **Target Roles**: Data Science, Business Analytics, Hydrological Engineering, Risk Analytics.

---

## 2. Statistical Methodology & Modeling Pipeline

### 2.1 Exploratory Analysis & Stationarity Testing
* **Augmented Dickey-Fuller (ADF) Test**: Tests null hypothesis $H_0$ of a unit root (non-stationarity). First-order differencing $d=1$ applied if $p > 0.05$.
* **Seasonal Decomposition**: Decomposing flow $Y_t = T_t + S_t + I_t$ into trend, seasonal (annual monsoon cycle), and irregular residual components.
* **Autocorrelation (ACF) & Partial Autocorrelation (PACF)**: Guides initial autoregressive order $p$ and moving average order $q$.

### 2.2 Model Formulations

#### 1. SARIMAX $(p, d, q) \times (P, D, Q)_s$
$$\Phi_P(B^s) \phi_p(B) (1-B)^d (1-B^s)^D Y_t = \Theta_Q(B^s) \theta_q(B) \epsilon_t + \beta X_t$$
where $X_t$ incorporates exogenous hydro-meteorological features (basin-averaged rainfall $P_t$, temperature).

#### 2. Long Short-Term Memory (LSTM) Networks
Gated recurrent architecture with memory cell $c_t$, forget gate $f_t$, input gate $i_t$, and output gate $o_t$ to capture multi-week hydrological lag memory.

---

## 3. Evaluation Metrics

Model performance is evaluated using standard hydrology and statistical metrics:

1. **Nash-Sutcliffe Efficiency (NSE)**:
   $$\mathrm{NSE} = 1 - \frac{\sum_{t=1}^T (Q_{obs,t} - Q_{sim,t})^2}{\sum_{t=1}^T (Q_{obs,t} - \bar{Q}_{obs})^2}$$
   ($\mathrm{NSE} = 1$ is perfect model; $\mathrm{NSE} > 0.75$ indicates very good hydrological performance).

2. **Kling-Gupta Efficiency (KGE)**:
   $$\mathrm{KGE} = 1 - \sqrt{(r - 1)^2 + (\alpha - 1)^2 + (\beta - 1)^2}$$
   decomposing error into linear correlation $r$, relative variability $\alpha = \sigma_{sim}/\sigma_{obs}$, and bias ratio $\beta = \mu_{sim}/\mu_{obs}$.

---

## 4. Illustrative Defense & Sample Interview Questions

### Q1: "Why would an LSTM outperform SARIMAX during peak monsoon hydrographs?"
> **Model Response**: "SARIMAX assumes linear relationships between exogenous rainfall lags and discharge, whereas runoff generation is inherently threshold-dependent. Infiltration excess and saturation excess runoff only occur after antecedent soil storage capacity is exceeded. LSTMs with nonlinear activation functions and continuous cell state memory effectively learn this nonlinear storage threshold, yielding significantly higher peak capture efficiency during high-discharge events."

### Q2: "How did you prevent data leakage during time-series feature engineering?"
> **Model Response**: "We strictly maintained causal temporal partitioning. The dataset was split chronologically into training (60%), validation (20%), and test (20%) windows without shuffling. All rolling lag statistics, cumulative precipitation sums, and normalization scalers were fitted exclusively on the training window and applied transform-only to subsequent validation and test intervals."

### Q3: "What were the limitations of your approach?"
> **Model Response**: "Pure data-driven models can violate mass balance during unprecedented rainfall events that exceed training-distribution extremes. Integrating a hybrid approach—such as using a lumped conceptual hydrologic model (e.g., GR4J or HBV) to provide physics-constrained baseflow priors—improves out-of-distribution robustness."
