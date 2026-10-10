# 07. Candidate & Project Defense — Technical Grounding

> **Target Role**: Spec Analytics Analyst — Business Analytics (SBS), Citi AIM  
> **Framework Focus**: Candidate-adaptable defense of quantitative engineering research and computational modeling projects across three archetypes.  
> **Evidence Policy**: No fabricated tools, languages, or personal claims. Defends verifiable quantitative modeling methods and outlines genuine transferable analytical skills.

---

## 1. Mapping Engineering Research to Banking Analytics

In an interview with a senior Citi AIM panel, you must articulate an honest, grounded bridge between quantitative engineering coursework and business analytics:

```
    QUANTITATIVE ENGINEERING RESEARCH               CITI AIM BUSINESS ANALYTICS
┌───────────────────────────────────────┐       ┌───────────────────────────────────────┐
│ • Extreme Value Statistics (Gumbel,   │       │ • Value-at-Risk (VaR) & Heavy-Tailed  │
│   Log-Pearson III, GEV)               │──────►│   Credit Loss Distributions           │
├───────────────────────────────────────┤       ├───────────────────────────────────────┤
│ • Decadal Sequential Time-Series      │       │ • High-Frequency Transaction Volumes, │
│   (Stationarity, ACF, PACF, ARIMA)    │──────►│   Portfolio Balances & Churn Trends   │
├───────────────────────────────────────┤       ├───────────────────────────────────────┤
│ • Multi-Gigabyte Sensor & Spatial     │       │ • Multi-Million Row Transactional     │
│   Data Cleaning (Missing Values, QA)  │──────►│   Data Warehouses & Feature Pipeline  │
├───────────────────────────────────────┤       ├───────────────────────────────────────┤
│ • Optimization & Sensitivity Analysis │       │ • Portfolio Risk vs Revenue Trade-Offs│
│   (Numerical Network Solvers)         │──────►│   (Credit Approval Cutoff Tuning)     │
└───────────────────────────────────────┘       └───────────────────────────────────────┘
```

### The Honest Transferable Skills Narrative
> *"I do not claim that hydrodynamic fluid modeling is identical to financial accounting. However, the underlying mathematical, statistical, and data manipulation toolkit is directly transferable.*
>
> *Both disciplines require extracting multi-variate data, diagnosing data quality flaws, testing for statistical stationarity, selecting and calibrating probability distributions, and making high-stakes decisions under uncertainty.*
>
> *In civil engineering systems, underestimating an extreme tail event causes a bridge or dam failure. In banking analytics, underestimating an extreme tail event causes severe credit defaults and insolvency. The mathematical discipline of respecting data integrity, validating model assumptions, and presenting risk trade-offs transparently is identical."*

---

## 2. In-Depth Project Defense Archetype 1: Time-Series & Predictive Analytics

* **Core Focus**: Forecasting continuous sequential variables under high variability and missing observations.
* **Relevant Project Scope**: Hydrologic streamflow, meteorological sequences, or demand forecasting.

### 11-Point Structured Project Defense:
1. **Research Problem**: Predicting seasonal streamflow volumes and peak discharge across multi-decadal gauge records to optimize reservoir storage allocations.
2. **Dataset & Source**: 30+ years of daily and monthly discharge observations from central river basin gauging stations.
3. **Data Quality Challenges**: Missing observation days during extreme flood events, sensor drift, and seasonal non-stationarity. Handled via local interpolation for short gaps ($<3$ days) and seasonal median imputation for extended sensor outages.
4. **Methods & Tools Actually Used**: Python (Pandas, NumPy, Statsmodels, SciPy). Autoregressive Integrated Moving Average (ARIMA), Seasonal ARIMA (SARIMA), and trend testing (Mann-Kendall test).
5. **Assumptions & Design Choices**: Assumed weak (covariance) stationarity after seasonal differencing ($d=1, D=1$). Verified via Augmented Dickey-Fuller (ADF) test ($p < 0.01$).
6. **Validation & Evaluation**: Chronological train-test split (first 25 years training, trailing 5 years out-of-time test). Evaluated using Root Mean Squared Error (RMSE), Mean Absolute Percentage Error (MAPE), and Nash-Sutcliffe Efficiency (NSE).
7. **Key Quantified Result**: SARIMA model achieved $\text{NSE} = 0.82$ and reduced forecasting MAPE from $28.4\%$ (baseline moving average) to $14.1\%$ on out-of-sample data.
8. **Limitations**: Linear autoregressive models struggle with extreme non-linear weather shocks (e.g., flash cloudbursts not present in autoregressive lags).
9. **Alternative Methods Considered**: Long Short-Term Memory (LSTM) recurrent neural networks; rejected for baseline deployment due to limited training sample length (monthly aggregates) and lack of interpretability.
10. **What Could Be Improved**: Coupling exogenous meteorological covariates (sea-surface temperature anomalies, ENSO indices) via SARIMAX or Gradient Boosted Decision Trees (XGBoost).
11. **Demonstration of Analytics Readiness**: Proves proficiency in Python data pipelines, time-series stationarity testing, diagnostic residual checks (Ljung-Box test), and preventing temporal data leakage.

---

## 3. In-Depth Project Defense Archetype 2: Parametric Risk Modeling & Optimization

* **Core Focus**: Fitting probabilistic distributions, extreme-value modeling, and multi-parameter optimization.
* **Relevant Project Scope**: Intensity-Duration-Frequency (IDF) curves, evapotranspiration, or tail-risk estimation.

### 11-Point Structured Project Defense:
1. **Research Problem**: Deriving Intensity-Duration-Frequency (IDF) design curves and computing daily reference evapotranspiration ($ET_0$) to evaluate catchment water deficits.
2. **Dataset & Source**: 40-year daily meteorological records (precipitation, max/min temperature, wind speed, relative humidity, solar radiation).
3. **Data Quality Challenges**: Missing humidity and solar radiation data on select historical dates; non-uniform observation timestamps. Handled by calibrating the Hargreaves-Samani temperature-based formulation against full FAO-56 Penman-Monteith baselines.
4. **Methods & Tools Actually Used**: Python (SciPy, Statsmodels), R (`evd`, `extRemes`), FAO-56 Penman-Monteith physical equations.
5. **Assumptions & Design Choices**: Evaluated Extreme Value Type I (Gumbel) and Log-Pearson Type III (LP3) distributions. Fitted empirical Sherman equation ($i = \frac{K \cdot T^m}{(D + b)^c}$) via non-linear least squares (Levenberg-Marquardt algorithm).
6. **Validation & Evaluation**: Goodness-of-fit evaluated via Kolmogorov-Smirnov (K-S) and Anderson-Darling tests, plus Akaike Information Criterion (AIC).
7. **Key Quantified Result**: LP3 distribution demonstrated superior heavy-tail fit over Gumbel ($\Delta\text{AIC} = -14.2$). Sherman IDF formulation achieved $R^2 = 0.988$ and $\text{RMSE} = 2.45\text{ mm/hr}$ across all 36 duration-frequency evaluation points.
8. **Limitations**: Assumed stationarity across the 40-year baseline; climate trend analysis revealed a $+21.8\%$ intensification in 1-hour 50-year return precipitation, indicating traditional static IDF curves underestimate modern extreme events.
9. **Alternative Methods Considered**: Generalized Extreme Value (GEV) distribution with non-stationary time-dependent location parameters ($\mu(t) = \mu_0 + \mu_1 t$).
10. **What Could Be Improved**: Integrating sub-hourly automated weather station (AWS) gauge data directly rather than relying on empirical IMD disaggregation formulas.
11. **Demonstration of Analytics Readiness**: Demonstrates deep mathematical mastery of statistical distributions, maximum likelihood estimation, non-linear curve fitting, and extreme tail risk analysis (directly analogous to financial credit loss distribution modeling).

---

## 4. In-Depth Project Defense Archetype 3: Physical Systems Modeling & Asset Risk

* **Core Focus**: 2D hydrodynamic flow simulation, scour vulnerability, and physical asset failure risk.
* **Relevant Project Scope**: Bridge pier scour, hydraulic network head loss, or infrastructure integrity.

### 11-Point Structured Project Defense:
1. **Engineering Problem**: Simulating 2D hydrodynamic flow and scour vulnerability around highway bridge piers across 10-year to 100-year flood discharge scenarios.
2. **Dataset & Source**: River cross-section bathymetry, SRTM digital elevation models, discharge gauge hydrographs.
3. **Data Quality Challenges**: Noisy bathymetric contours and irregular riverbank elevation steps. Interpolated via TIN surface generation in QGIS.
4. **Methods & Tools Actually Used**: HEC-RAS 2D (shallow water Saint-Venant equations), QGIS, Python data automation.
5. **Assumptions & Design Choices**: Solved depth-averaged 2D Saint-Venant equations on an unstructured mesh. Evaluated CSU (HEC-18), Melville, and Froehlich scour formulations.
6. **Validation & Evaluation**: Model calibrated against physical gauge water surface elevations ($R^2 = 0.94$). CSU equation predicted scour within $+5.4\%$ of historical flood mark data.
7. **Key Quantified Result**: Identified critical 4.85 m scour undermining risk under 100-year peak flow ($2,450\text{ m}^3/\text{s}$). Designed a 350 mm $d_{50}$ riprap collar countermeasure reducing bed shear stress by $64\%$.
8. **Limitations**: 2D depth-averaged models assume hydrostatic pressure distributions and cannot explicitly resolve the 3D downward jet vortex on the pier nose.
9. **Alternative Methods Considered**: 3D CFD in OpenFOAM; rejected due to prohibitive computational runtime across a 2.4 km river reach.
10. **What Could Be Improved**: Coupling reach-scale 2D shallow water models with localized 3D Large Eddy Simulation (LES) around vulnerable bridge piers.

---

## 5. Frequently Asked Technical Grilling Questions & Model Answers

### Q1: "You have not worked in banking. How do you plan to understand Citi's complex credit and trading products?"
* **Model Answer**:
  * *"Every quantitative field has domain-specific taxonomy. When I began my graduate research, I had to master fluid rheology, turbulence equations, and hydro-meteorology.*
  * *Banking products follow clear financial logic: balances, interest rates, probability of default, roll rates, and recovery values. I have already studied the fundamentals of retail banking, card portfolios (transactors vs revolvers), and credit risk metrics like the KS statistic.*
  * *My core strength is that I learn quantitative systems rapidly from first principles. With Citi's structured onboarding and AIM team mentoring, I will master internal schemas and product lines quickly while delivering immediate value on data manipulation and statistical analysis."*

### Q2: "In your time-series project, why did you use SARIMA instead of a modern deep learning model like LSTM?"
* **Model Answer**:
  * *"I chose SARIMA based on sample size, data grain, and interpretability:*
  * *First, we had monthly aggregate data ($\sim 360$ time steps). Deep learning architectures like LSTMs have hundreds of thousands of parameters and require massive datasets to avoid severe overfitting, whereas SARIMA has only 5 to 7 parsimonious parameters.*
  * *Second, SARIMA provides explicit statistical significance tests for each parameter ($p$-values), clear confidence intervals on forecasts, and straightforward residual diagnostics via ACF/PACF plots.*
  * *In an enterprise analytics and risk governance environment like Citi, interpretability, auditability, and parsimony are often far more valuable than a black-box model that achieves marginal training error reductions."*
