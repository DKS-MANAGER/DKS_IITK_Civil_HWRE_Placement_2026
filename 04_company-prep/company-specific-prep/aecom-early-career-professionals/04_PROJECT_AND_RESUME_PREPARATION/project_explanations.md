# Academic & Research Projects: Technical Explanations & Defense
**Candidate Background:** M.Tech Civil Engineering (Hydraulics & Water Resources Engineering — HWRE), IIT Kanpur  
**Target Role:** Early Career Professionals (ECP) — Infrastructure / Water Resources Engineering  
**Company:** AECOM India (Bengaluru & Gurugram)  
**Standard:** Rigorous Project Defense & Value Demonstration Guide  

---

## Overview

In technical interviews at AECOM, interviewers probe beyond high-level buzzwords to examine the mathematical foundations, engineering trade-offs, data integrity, code compliance, and commercial applicability of your academic projects.

This module provides exhaustive, interview-ready defenses for the candidate's three major projects:
1. **Predictive Machine Learning for Bridge Scour & Hydraulic Failure Risk (XGBoost & TreeSHAP)**
2. **Streamflow Time-Series Modeling & Forecasting (SARIMAX & Machine Learning)**
3. **IDF Curve Derivation & FAO-56 Penman-Monteith Evapotranspiration Framework**

---

# PROJECT 1: Predictive Machine Learning for Bridge Scour & Hydraulic Failure Risk

### 1. Executive Summary
- **Domain:** Structural-Hydraulic Asset Risk Management, Extreme Value Modeling, Explainable AI.
- **Dataset:** Multi-variate bridge inspection records with geotechnical, hydraulic, structural, and environmental attributes.
- **Core Algorithms:** XGBoost (Extreme Gradient Boosting), LightGBM, Random Forest, SHAP (SHapley Additive exPlanations).
- **Key Metrics:** **ROC-AUC: 0.983**, **PR-AUC: 0.854**, **F1-Score: 0.891** on an extreme-class-imbalanced dataset ($< 5\%$ failure events).

---

### 2. Engineering Context & Motivation
Bridge scour and hydraulic instability account for over $55\%$ of all bridge failures worldwide. Traditional bridge risk management relies on periodic physical inspections (every 2 to 5 years), which:
1. Are qualitative and subjective.
2. Miss sudden scouring occurring during extreme unmonitored flood hydrographs.
3. Cannot continuously prioritize capital expenditure across large portfolios of aging infrastructure assets.

This project was conceived as an intelligent, data-driven decision-support tool to predict the probability of hydraulic failure and scour vulnerability for bridge portfolios, bridging physical hydraulic mechanics with scalable predictive analytics.

---

### 3. Data Pipeline & Feature Engineering
The dataset incorporated 28 engineered features categorized into four physical domains:
1. **Hydraulic Parameters:**
   - 100-year design flood discharge ($Q_{100}$).
   - Approach flow velocity ($V_0$).
   - Froude number ($Fr = V_0 / \sqrt{g y_0}$).
   - Channel contraction ratio ($B_{\text{bridge}} / B_{\text{channel}}$).
   - Angle of flow attack relative to pier longitudinal axis ($\theta$).
2. **Structural & Foundation Geometry:**
   - Pier shape factor (round nose, rectangular, sharp nose).
   - Pier width ($b$) and number of piers in waterway.
   - Foundation type (shallow spread footing, well foundation / caisson, deep drilled shaft / pile group).
   - Foundation embedment depth relative to historical Lacey scour depth ($D_f / R_{\text{scour}}$).
3. **Geotechnical & Bed Material Properties:**
   - Median sediment grain diameter ($d_{50}$).
   - Soil gradation coefficient ($\sigma_g = \sqrt{d_{84} / d_{16}}$).
   - Critical Shields shear stress ($\tau_c$).
   - Cohesive vs cohesionless bed categorization.
4. **Historical & Environmental Stressors:**
   - Age of structure (years in service).
   - Frequency of historical overtopping events.
   - Upstream watershed deforestation / urbanization index.

---

### 4. Machine Learning Architecture & Handling Class Imbalance
1. **Class Imbalance Mitigation:**
   - In real-world bridge infrastructure, catastrophic failure is rare ($< 5\%$ of records).
   - Standard accuracy metrics are deceptive (a naive classifier predicting "No Failure" achieves $95\%$ accuracy).
   - Mitigated via:
     - Synthetic Minority Over-sampling Technique (**SMOTE-NC** for mixed continuous-categorical variables).
     - Scale Pos Weight tuning in XGBoost: $\text{scale\_pos\_weight} = \frac{N_{\text{negative}}}{N_{\text{positive}}} \approx 19.0$.
     - Evaluating primarily via **Precision-Recall AUC (PR-AUC)** rather than ROC-AUC alone.
2. **Model Training & Hyperparameter Tuning:**
   - 5-fold Stratified Cross-Validation.
   - Bayesian Hyperparameter Optimization with `Optuna` tuning:
     - `max_depth` $\in [3, 7]$ (preventing overfitting on noisy inspection logs).
     - `learning_rate` $\eta \in [0.01, 0.05]$.
     - `subsample` $\in [0.7, 0.9]$ and `colsample_bytree` $\in [0.6, 0.8]$.
     - `gamma` / minimum loss reduction $\in [0.1, 1.0]$.
3. **Loss Function (Binary Logistic Regression with Hessian Regularization):**
   $$\mathcal{L}(\theta) = \sum_{i=1}^n \left[ y_i \ln(1 + e^{-\hat{y}_i}) + (1 - y_i) \ln(1 + e^{\hat{y}_i}) \right] + \sum_{k=1}^K \left( \gamma T_k + \frac{1}{2} \lambda \|w_k\|^2 \right)$$

---

### 5. Explainable AI (SHAP) & Physical Validation
In engineering consultancy, "black-box" models cannot be certified for public infrastructure safety. We deployed **TreeSHAP** (Shapley Additive exPlanations based on cooperative game theory) to ensure model predictions obeyed first-principles hydraulic mechanics:
1. **Global Feature Importance:**
   - Top 1: Foundation Embedment Ratio ($D_f / R_{\text{scour}}$) — Negative SHAP value when $D_f / R > 1.5$ (protective effect).
   - Top 2: Angle of Flow Attack ($\theta$) — Acute positive SHAP spikes when $\theta > 15^\circ$, accurately reflecting the tripling of effective pier width and horseshoe vortex intensification.
   - Top 3: Channel Contraction Ratio ($B_{\text{bridge}} / B_{\text{channel}}$).
   - Top 4: Approach Froude Number ($Fr$).
2. **Local Explainability:**
   - Provided individual bridge "waterfall plots" detailing why a specific bridge was flagged as high risk (e.g., shallow foundation depth contributing $+42\%$ risk, skewed flow attack contributing $+28\%$).

---

### 6. AECOM Commercial Alignment
- **Enterprise Asset Management:** Enables AECOM's asset management advisory teams to prioritize bridge maintenance and scour countermeasure investments (e.g., riprap armoring, sheet piling) across national or state transport corridors.
- **Client Pitch:** Direct translation into digital twin solutions for NHAI, Indian Railways, or state highway departments.

---

# PROJECT 2: Streamflow Time-Series Modeling & Forecasting (SARIMAX)

### 1. Executive Summary
- **Domain:** Hydro-Informatics, Statistical Hydrology, Catchment Inflow Forecasting.
- **Dataset:** 35 years of daily and monthly discharge observations coupled with gridded satellite precipitation (IMD / TRMM) and temperature reanalysis data.
- **Core Models:** SARIMAX (Seasonal Autoregressive Integrated Moving Average with eXogenous variables), Prophet, LSTM (Long Short-Term Memory Neural Networks).
- **Key Metrics:** **Nash-Sutcliffe Efficiency (NSE) = 0.88**, **Kling-Gupta Efficiency (KGE) = 0.91**, Root Mean Square Error (RMSE) reduction by $34\%$ over baseline AR(1).

---

### 2. Theoretical Formulation & Methodology

#### 2.1 Stationarity & Transformative Pre-Processing
Hydrological time series exhibit non-stationarity due to annual monsoonal seasonality, multi-decadal climate cycles, and long-term land-use changes:
1. **Variance Stabilization:** Box-Cox power transformation:
   $$y^{(\lambda)} = \begin{cases} \frac{y^\lambda - 1}{\lambda}, & \lambda \ne 0 \\ \ln(y), & \lambda = 0 \end{cases}$$
   $\lambda \approx 0.22$ was optimal for converting skewed daily flood discharges to an approximately Gaussian distribution.
2. **Unit Root Testing:**
   - Augmented Dickey-Fuller (ADF) test: Null hypothesis of a unit root was rejected only after first-order non-seasonal differencing ($d = 1$) and seasonal differencing ($D = 1, s = 12$ months):
     $$\Delta \Delta_{12} y_t = (1 - B)(1 - B^{12}) y_t$$

#### 2.2 SARIMAX $(p, d, q) \times (P, D, Q)_s$ Model Architecture
The mathematical representation incorporating exogenous meteorological covariates:
$$\Phi_P(B^s) \phi_p(B) (1 - B)^d (1 - B^s)^D y_t = \sum_{j=1}^m \beta_j X_{j, t} + \Theta_Q(B^s) \theta_q(B) \varepsilon_t$$
where:
- $B$ is the backshift lag operator ($B^k y_t = y_{t-k}$).
- $\phi_p(B) = 1 - \sum_{i=1}^p \phi_i B^i$ (non-seasonal AR operator).
- $\theta_q(B) = 1 + \sum_{i=1}^q \theta_i B^i$ (non-seasonal MA operator).
- $\Phi_P(B^s)$ and $\Theta_Q(B^s)$ are the seasonal AR and MA polynomial operators for period $s = 12$.
- $X_{j, t}$ represents exogenous rainfall excess and mean temperature.
- $\varepsilon_t \sim \mathcal{N}(0, \sigma^2)$ is white noise.

#### 2.3 Parameter Estimation & Model Selection
1. Model identification via Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF) plots.
2. Grid search across parameter space: $p \in [1, 3], d = 1, q \in [1, 2], P \in [0, 2], D = 1, Q \in [0, 1]$.
3. Best model selected via Akaike Information Criterion (AIC) and Bayesian Information Criterion (BIC):
   $$AIC = 2k - 2\ln(\hat{L}), \quad BIC = k\ln(n) - 2\ln(\hat{L})$$
   Selected optimal model: **SARIMAX$(2, 1, 1) \times (1, 1, 1)_{12}$ with 3-day antecedent rainfall as exogenous predictor**.
4. **Residual Diagnostics:** Ljung-Box Q-test confirmed residuals were uncorrelated white noise ($p\text{-value} > 0.05$).

---

### 3. Hydrological Performance Metrics
Standard $R^2$ is inadequate for streamflow because high seasonal peaks distort variance. We evaluated using specialized hydrology metrics:
1. **Nash-Sutcliffe Efficiency (NSE):**
   $$NSE = 1 - \frac{\sum_{t=1}^T (Q_{\text{obs}, t} - Q_{\text{sim}, t})^2}{\sum_{t=1}^T (Q_{\text{obs}, t} - \overline{Q}_{\text{obs}})^2} = 0.88$$
   ($NSE = 1.0$ is perfect; $> 0.75$ represents very good hydrological predictive power).
2. **Kling-Gupta Efficiency (KGE):**
   $$KGE = 1 - \sqrt{(r - 1)^2 + (\alpha - 1)^2 + (\beta - 1)^2} = 0.91$$
   where $r$ is correlation, $\alpha = \sigma_{\text{sim}} / \sigma_{\text{obs}}$ (flow variability bias), and $\beta = \mu_{\text{sim}} / \mu_{\text{obs}}$ (water balance volume bias).

---

### 4. AECOM Consulting Relevance
- Reservoir rule-curve optimization for hydroelectric and irrigation schemes.
- Early warning flood forecasting and reservoir inflow management during monsoonal storm events.
- Water supply resilience planning under climate change scenarios.

---

# PROJECT 3: IDF Curve Derivation & FAO-56 Penman-Monteith Evapotranspiration Framework

### 1. Executive Summary
- **Domain:** Engineering Hydrology, Extreme Rainfall Statistics, Agricultural & Irrigation Water Demand.
- **Deliverables:** High-resolution Intensity-Duration-Frequency (IDF) equations for return periods $T \in [2, 100\text{ years}]$, and an automated Python computation pipeline for reference evapotranspiration ($ET_0$) complying with FAO Irrigation and Drainage Paper No. 56.

---

### 2. IDF Curve Derivation Methodology

#### 2.1 Annual Maximum Precipitation Series (AMS)
1. Extracted maximum rainfall depths for durations: $D \in [15\text{ min}, 30\text{ min}, 1\text{ hr}, 2\text{ hr}, 6\text{ hr}, 12\text{ hr}, 24\text{ hr}]$.
2. Fitted extreme value probability distributions:
   - Gumbel (Extreme Value Type I / EV-I).
   - Log-Pearson Type III (LP-III).
   - Generalized Extreme Value (GEV).
3. Goodness-of-fit evaluated using Kolmogorov-Smirnov (K-S) and Chi-Square tests.

#### 2.2 Sherman / Bernard IDF Empirical Parameter Fitting
The relationship between rainfall intensity $I$ (mm/hr), duration $D$ (hours), and return period $T$ (years) was parameterized into the generalized Sherman equation:
$$I = \frac{K \cdot T^m}{(D + a)^n}$$
where $K, m, a, n$ are empirical catchment parameters determined through non-linear least-squares optimization using Python's `scipy.optimize.curve_fit`.
- Catchment calibrated parameters: $K = 54.2$, $m = 0.218$, $a = 0.35\text{ hr}$, $n = 0.782$.
- Coefficient of determination: $R^2 = 0.992$ across all duration-frequency combinations.

---

### 3. FAO-56 Penman-Monteith Reference Evapotranspiration ($ET_0$)

#### 3.1 Thermodynamic Formulation
The standardized FAO-56 Penman-Monteith equation for an idealized grass reference crop ($h = 0.12\text{ m}$, albedo $\alpha = 0.23$, surface resistance $r_s = 70\text{ s/m}$):
$$ET_0 = \frac{0.408 \Delta (R_n - G) + \gamma \frac{900}{T + 273} u_2 (e_s - e_a)}{\Delta + \gamma (1 + 0.34 u_2)}$$
where:
- $ET_0$: Reference evapotranspiration ($\text{mm/day}$).
- $R_n$: Net radiation flux at crop surface ($\text{MJ/m}^2\cdot\text{day}$).
- $G$: Soil heat flux density ($\text{MJ/m}^2\cdot\text{day}$, negligible for daily steps: $G \approx 0$).
- $T$: Mean daily air temperature at $2\text{ m}$ height ($^\circ\text{C}$).
- $u_2$: Wind speed at $2\text{ m}$ height ($\text{m/s}$).
- $e_s$: Saturation vapor pressure ($\text{kPa}$).
- $e_a$: Actual vapor pressure ($\text{kPa}$).
- $e_s - e_a$: Vapor pressure deficit ($VPD$, $\text{kPa}$).
- $\Delta$: Slope of vapor pressure curve ($\text{kPa/}^\circ\text{C}$):
  $$\Delta = \frac{4098 \left[ 0.6108 \exp\left(\frac{17.27 T}{T + 237.3}\right) \right]}{(T + 237.3)^2}$$
- $\gamma$: Psychrometric constant ($\text{kPa/}^\circ\text{C}$):
  $$\gamma = \frac{c_p P}{\varepsilon \lambda} \approx 0.000665 P$$
  where $P$ is atmospheric pressure adjusted for site altitude.

#### 3.2 Computational Implementation
- Automated end-to-end Python script processing meteorological feeds: daily maximum/minimum temperature, solar radiation hours, relative humidity, and anemometer wind data.
- Built-in sanity filters for psychrometric consistency (e.g., ensuring $e_a \le e_s$ and solar radiation does not exceed extraterrestrial radiation $R_a$).

---

### 4. AECOM Consulting Relevance
- **Urban Drainage Sizing:** Direct input into EPA-SWMM and Civil 3D for sizing stormwater collection networks, retention basins, and culverts complying with municipal design criteria.
- **Irrigation & Water Allocation Master Planning:** Sizing canal delivery volumes and reservoir releases based on accurate crop water requirements ($ET_c = K_c \cdot ET_0$).

---
*End of Project Explanations & Defense.*
