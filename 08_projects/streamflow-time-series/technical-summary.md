# Technical Summary — Streamflow Time-Series Modeling & Forecasting

> **Project Code**: `streamflow-time-series`  
> **Domain**: Surface Water Hydrology, Hydroinformatics & Deep Learning  
> **Software & Tools**: Python (PyTorch, Pandas, Scikit-Learn, Statsmodels), HEC-HMS

---

## 1. Mathematical Formulations & Architectures

### 1. Statistical Baseline: SARIMAX($p, d, q$) $\times$ ($P, D, Q$)$_s$
$$\Phi_P(B^s) \phi_p(B) (1 - B)^d (1 - B^s)^D Y_t = \Theta_Q(B^s) \theta_q(B) \epsilon_t + \sum_{k=1}^m \beta_k X_{k,t}$$
Where $B$ is the backshift operator ($B^k Y_t = Y_{t-k}$), $s = 365$ (annual seasonality), and $X_{k,t}$ is exogenous rainfall depth at time $t$.
* Order identification: Analyzed Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF) plots. Augmented Dickey-Fuller (ADF) test confirmed first-order stationarity ($p < 0.01$).

### 2. Recurrent Neural Network: Stacked LSTM
LSTMs resolve vanishing/exploding gradients in standard RNNs using memory cell states ($c_t$) and gating mechanisms:

$$\text{Forget Gate}: f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$$
$$\text{Input Gate}: i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i)$$
$$\text{Candidate Cell State}: \tilde{c}_t = \tanh(W_c \cdot [h_{t-1}, x_t] + b_c)$$
$$\text{Cell State Update}: c_t = f_t \odot c_{t-1} + i_t \odot \tilde{c}_t$$
$$\text{Output Gate}: o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o)$$
$$\text{Hidden State Output}: h_t = o_t \odot \tanh(c_t)$$

---

## 2. Feature Engineering & Temporal Processing

1. **Exogenous Features**: Daily precipitation ($P_t$), rolling rainfall sums ($P_{t-3}, P_{t-7}, P_{t-14}$), maximum daily temperature ($T_{max}$), and Day-of-Year cyclical encodings ($\sin(2\pi d / 365), \cos(2\pi d / 365)$).
2. **Lag Selection**: PACF analysis showed strong runoff auto-dependence up to 7 antecedent days, representing channel transit and soil detention storage.
3. **Loss Function**: Custom hydrological loss blending Mean Squared Error (MSE) and Nash-Sutcliffe Efficiency (NSE) to penalize peak discharge underestimation:
   $$\mathcal{L} = \text{MSE} + \lambda (1 - \text{NSE})$$
