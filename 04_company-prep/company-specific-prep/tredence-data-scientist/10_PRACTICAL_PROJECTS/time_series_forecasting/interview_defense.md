# Project 2: Interview Defense & Technical Q&A

**Candidate Defense Readiness:** Stochastic Time-Series & Demand Forecasting  
**Role:** Data Scientist / Associate Data Scientist | Tredence Analytics

---

### Q1. Why did you choose SARIMA over simple exponential smoothing or Prophet?
**Defense:**  
- **Mathematical Rigor & Grounding:** SARIMA provides a transparent, mathematically grounded likelihood framework $\Phi(B^s)\phi(B)(1-B)^d(1-B^s)^D Y_t = \Theta(B^s)\theta(B)\epsilon_t$ that explicitly models autoregressive dynamics and stochastic seasonal shocks.
- **Diagnostics:** Unlike black-box curve-fitting packages (such as Prophet), SARIMA yields verifiable statistical diagnostics (ADF unit root testing, ACF/PACF residual independence, Ljung-Box test) ensuring that all linear autocovariance structure is captured.
- **Candidate Domain Synergy:** My background in stochastic hydrological time-series modeling (streamflow forecasting and flood recurrence) translates directly to modeling seasonal volatility, cyclic shocks, and extreme demand spikes.

---

### Q2. Why is WAPE preferred over MAPE for retail SKU demand forecasting?
**Defense:**  
- $\text{MAPE} = \frac{1}{n} \sum \frac{|y_i - \hat{y}_i|}{y_i}$. When actual daily demand $y_i = 0$ (common in slow-moving retail SKUs), MAPE results in division by zero. Furthermore, if $y_i = 1$ and forecast is $5$, MAPE explodes to $400\%$, distorting aggregate reporting.
- $\text{WAPE} = \frac{\sum |y_i - \hat{y}_i|}{\sum y_i}$. WAPE aggregates absolute unit errors and divides by total actual sales volume. It never divides by zero and naturally weights high-velocity SKUs more heavily than trivial deviations on slow-moving inventory.

---

### Q3. How do you convert the forecast confidence intervals into inventory safety stock?
**Defense:**  
- A point forecast $\hat{y}_t$ provides the expected conditional mean demand. However, ordering exactly $\hat{y}_t$ results in stockouts $50\%$ of the time due to symmetric error distributions.
- The upper 95% confidence limit $\hat{y}_{\text{upper}}$ represents the 97.5th percentile demand under Gaussian error assumptions.
- **Safety Stock Buffer:**
  $$\text{Safety Stock} = \hat{y}_{\text{upper}} - \hat{y}_{\text{mean}} = Z_{\alpha} \times \sigma_{\text{forecast}}$$
- For perishable dairy/produce, we tune $Z_\alpha$ based on the cost ratio of stockout penalties vs spoilage write-offs (Critical Fractile / Newsvendor model), establishing an optimal, profitable inventory replenishment policy.
