# Module 22 — Candidate Project Defence & Consulting Translation

In an IQVIA Associate Consultant interview, interviewers will scrutinize your technical master's research to test whether you can **explain complex quantitative work to non-technical business stakeholders**, synthesize actionable conclusions, and defend analytical choices under pressure.

---

## Strategic Framing of Engineering Research for Consulting

```
┌─────────────────────────────────┐                 ┌─────────────────────────────────┐
│  Candidate Engineering Project  │                 │ Pharma Commercial Equivalency   │
├─────────────────────────────────┤                 ├─────────────────────────────────┤
│ • Machine Learning & SHAP       │ ──────────────► │ • Prescriber Response Scoring   │
│   (XGBoost, ROC-AUC 0.983)      │                 │   (HCP Targeting & Churn Risk)  │
├─────────────────────────────────┤                 ├─────────────────────────────────┤
│ • Hydrological Time-Series      │ ──────────────► │ • Biopharma Demand Forecasting  │
│   (ARMA, Trend, Seasonality)    │                 │   (TRx/NRx Launch & Patent Cliff│
├─────────────────────────────────┤                 ├─────────────────────────────────┤
│ • Hydrodynamic Transport        │ ──────────────► │ • Healthcare Funnel Dynamics    │
│   (Mass balance, Flow networks) │                 │   (Patient Journey & Leakage)   │
└─────────────────────────────────┘                 └─────────────────────────────────┘
```

---

## Project 1: Machine Learning Infrastructure Risk Prediction & SHAP Analysis

### 1.1 Technical Profile
- **Project Scope**: Large-scale predictive risk modeling of 2,500+ physical infrastructure assets using historical inspection registries, material degradation parameters, and climatic exposure metrics.
- **Methodology**: Gradient Boosting (XGBoost), Class Imbalance Resolution, ROC-AUC and PR-AUC calibration, and Explainable AI using SHAP (SHapley Additive exPlanations).
- **Core Results**: Achieved ROC-AUC of 0.983 and PR-AUC of 0.854; quantified non-linear threshold effects of environmental degradation on asset failure risk.

### 1.2 30-Second Elevator Pitch
> *"In this project, I built a predictive machine learning risk-scoring framework on 2,500+ asset records to solve a high-stakes resource allocation problem. By combining XGBoost with SHAP explainability, my model achieved a 0.983 ROC-AUC while identifying the exact structural inflection points that drive critical risk. This transformed an opaque technical model into a transparent decision-support dashboard for capital expenditure prioritization."*

### 1.3 3-Minute Consulting Case Walkthrough
> *"**The Business Problem**: Infrastructure asset management faces a classic commercial optimization dilemma: municipal budgets are severely constrained, while catastrophic asset failure carries immense human and financial costs. Asset managers historically relied on subjective periodic inspections that resulted in either premature capital replacement or reactive emergency repairs.
> 
> **Our Hypothesis**: We hypothesized that multi-variable interactions between asset age, material properties, and environmental stress follow identifiable non-linear degradation curves that can accurately forecast asset vulnerability years before physical failure occurs.
> 
> **Analytical Approach**: 
> 1. *Data Engineering*: We extracted and cleaned 2,500+ historical records, handling significant missingness and severe class imbalance (critical risk assets represented < 8% of total volume).
> 2. *Model Architecture*: We selected XGBoost for its superior performance on tabular non-linear interactions, tuning hyperparameters via 5-fold stratified cross-validation.
> 3. *Explainability*: Rather than leaving the model as a black box, we applied game-theoretic SHAP values to quantify the marginal contribution of every single variable to individual asset risk scores.
> 
> **Findings & Commercial Takeaway**: The model demonstrated that environmental stress factors act as dramatic non-linear risk accelerators once an asset passes 25 years of operational service. From an executive decision-making standpoint, this enabled leadership to shift 40% of maintenance budgets from uniform random inspections to proactive preventative maintenance on the top 10% highest-risk assets, reducing expected lifecycle risk costs by 32%.
> 
> **Pharma Consulting Equivalence**: This methodology translates directly to pharmaceutical commercial analytics—specifically in **physician targeting and patient churn prediction**. Just as we isolated the multi-variable drivers of asset risk, biopharma consultants use predictive scoring and SHAP feature attribution to determine which oncologists are most likely to switch brands or which patients face high therapy abandonment risk."*

### 1.4 Tough Cross-Examination Q&A
- **Interviewer**: *"With only 8% positive class representation, standard accuracy is useless. Why did you rely on PR-AUC rather than just ROC-AUC?"*
  - **Candidate**: *"Exactly. In severely imbalanced datasets, ROC-AUC can present an overly optimistic picture because the false positive rate is diluted by the massive negative class denominator. Precision-Recall AUC (PR-AUC) focuses strictly on the minority positive class. Achieving a PR-AUC of 0.854 confirmed that when our model flagged an asset as high-risk, the probability of it genuinely requiring intervention was exceptionally high, minimizing wasted capital expenditure on false alarms."*

---

## Project 2: Hydrological Time-Series & Extreme Value Forecasting

### 2.1 Technical Profile
- **Project Scope**: Multi-decadal temporal flow forecasting, autoregressive modeling, and extreme event probability modeling using generalized extreme value distributions (Gumbel / Log-Pearson Type III).
- **Methodology**: Time-series decomposition (trend, seasonality, cyclic residuals), ARMA/ARIMA modeling, Maximum Likelihood Estimation (MLE) of distribution parameters.
- **Core Results**: Developed 25-year and 50-year recurrence interval risk curves; quantified forecast uncertainty bands for capacity design under climate variability.

### 2.2 30-Second Elevator Pitch
> *"My research in hydrological time-series modeling focused on forecasting extreme, low-probability, high-impact events across multi-decade horizons. By combining autoregressive time-series models with extreme-value statistical distributions, I developed probabilistic risk curves that enabled infrastructure planners to design resilient systems under deep future demand uncertainty."*

### 2.3 3-Minute Consulting Walkthrough
> *"**The Strategic Context**: Large-scale water resources infrastructure requires capital investments with 30-to-50-year operational horizons. Planners must size storage and conveyance capacity to balance two catastrophic risks: under-building, which causes devastating overflow failures, and over-building, which locks up hundreds of millions in unremunerative capital expenditure.
> 
> **The Analytical Framework**:
> 1. *Decomposition*: I decomposed 40 years of continuous daily streamflow data into long-term secular trends, multi-modal annual seasonality, and stochastic residual noise.
> 2. *Distributional Fitting*: Standard Gaussian distributions fail to capture heavy tail risks. I applied Gumbel and Generalized Extreme Value (GEV) distributions using Maximum Likelihood Estimation to model 99th-percentile tail events.
> 3. *Scenario Planning*: I generated probabilistic sensitivity bands across differing macroeconomic and climatic scenarios.
> 
> **Strategic "So-What"**: The analysis demonstrated that historical 50-year design benchmarks were under-estimating peak volume recurrence by 18% due to accelerating variance in annual cycles. This provided engineering leadership with the quantitative justification to adopt modular, scalable infrastructure expansion thresholds rather than a rigid single-build model.
> 
> **Pharma Consulting Equivalence**: In biopharma commercial strategy, this directly mirrors **Loss-of-Exclusivity (LOE) patent cliff forecasting and epidemic surge demand planning**. Just as extreme value statistics model the tail risks of hydrological events, pharmaceutical forecasters model the steep, non-linear demand drop-off when multiple generic competitors enter a market, allowing brand directors to optimize supply-chain inventory and contractual hedging."*

### 2.4 Tough Cross-Examination Q&A
- **Interviewer**: *"Historical time-series assumes stationarity. How did you handle non-stationary trends in your forecasting model?"*
  - **Candidate**: *"We conducted rigorous Augmented Dickey-Fuller (ADF) tests on the raw series, which confirmed non-stationarity. We addressed this through first-order differencing and seasonal detrending to achieve weak stationarity in the residual series before fitting the autoregressive parameters. Furthermore, for long-term forecasting, we incorporated a dynamic drift parameter to explicitly capture secular trend drift rather than assuming historical mean reversion."*

---

## Project 3: Computational Fluid & Solute Transport Numerical Simulation

### 3.1 Technical Profile
- **Project Scope**: Numerical modeling of multi-dimensional advection-dispersion and mass-transport dynamics through complex boundary geometries.
- **Methodology**: Finite Difference / Finite Volume discretizations, stability and convergence analysis (Courant-Friedrichs-Lewy condition), mass conservation balance.
- **Core Results**: Simulated dynamic solute concentration decay curves across downstream networks; established threshold limits for regulatory compliance.

### 3.2 Consulting Translation Pitch
> *"This project modeled how mass and volume propagate through complex, constrained physical networks over time. In consulting, I view this as the perfect structural analog for **Patient Journey Flow and Funnel Leakage Analytics**. 
> 
> In a patient journey, eligible individuals flow through multiple sequential clinical stages—symptom presentation, physician consultation, diagnostic testing, payer prior authorization, prescription fulfillment, and chronic persistence. Just as physical flow networks experience bottlenecks, resistance, and mass leakage, a pharmaceutical commercial funnel experiences diagnostic drop-offs, payer denial resistance, and retail abandonment. 
> 
> My background in analyzing fluid network flow allows me to immediately conceptualize pharmaceutical commercial bottlenecks as a **dynamic mass-balance equation**, identifying exactly which bottleneck remediation yields the highest return on investment."*

