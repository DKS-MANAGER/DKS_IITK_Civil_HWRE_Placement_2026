# Interview Grilling Questions — Streamflow Forecasting (`streamflow-time-series`)

> **Focus**: Questions on machine learning vs hydrological physics, data quality, over-fitting, and operational deployment.

---

## 1. Technical Grilling Questions & Answers

### Q1: "Deep learning models are often called 'black boxes'. If an extreme flood exceeds historical training records, why should an engineer trust an LSTM?"
* **Answer**: *"Pure data-driven models cannot extrapolate beyond the convex hull of their training distribution. When discharge exceeds historical bounds, an unconstrained LSTM may violate conservation of mass. To address this, I implemented physics-guided bounds: predicted total runoff volume cannot exceed total catchment precipitation over the concentration window ($\int Q dt \le \int P dt \cdot A$). For extreme safety-critical spillway operations, deep learning should be coupled with a physical conceptual model (HEC-HMS/SWAT) as an ensemble."*

### Q2: "Why use Nash-Sutcliffe Efficiency (NSE) and Kling-Gupta Efficiency (KGE) instead of standard $R^2$ or MSE?"
* **Answer**:
  * $R^2$ measures only linear correlation; a model that consistently predicts $2 \times \text{observed discharge}$ still yields $R^2 = 1.0$ despite a 100% volume error.
  * Standard MSE squares errors, disproportionately penalizing single peak outliers while ignoring cumulative water balance volume errors.
  * **NSE** measures predictive skill relative to the mean observed hydrograph ($NSE = 1$ is perfect; $NSE < 0$ means the mean is a better predictor than the model).
  * **KGE** explicitly balances correlation ($r$), variability bias ($\alpha = \sigma_{sim}/\sigma_{obs}$), and volume bias ($\beta = \mu_{sim}/\mu_{obs}$).

### Q3: "How did you optimize LSTM hyperparameters and prevent overfitting?"
* **Answer**: *"I used a 3-way chronological split (70% train, 15% validation, 15% holdout test). I tuned hidden layer dimensions (32, 64, 128 units), sequence window length (7, 14, 30 days), and learning rate ($10^{-3}$ to $10^{-4}$) using Bayesian optimization. Overfitting was controlled via Dropout (0.2), $L_2$ weight decay ($10^{-5}$), and Early Stopping monitored strictly on validation KGE."*
