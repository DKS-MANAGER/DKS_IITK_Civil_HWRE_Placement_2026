# Technical Summary — IDF Rainfall Frequency & Potential Evapotranspiration

> **Project Code**: `idf-pet`  
> **Domain**: Hydro-Meteorology, Urban Drainage Design & Statistical Modeling  
> **Software & Tools**: Python (SciPy, Statsmodels, Pandas), R (evd, extRemes), FAO-56 Standard

---

## 1. Mathematical Formulations & Statistical Distributions

### 1. Extreme Value Type I (Gumbel Distribution):
Cumulative distribution function:
$$F(x) = \exp\left(-\exp\left(-\frac{x - u}{\alpha}\right)\right)$$
Rainfall depth for return period $T$:
$$x_T = \bar{x} + K_T \cdot s$$
Where frequency factor:
$$K_T = -\frac{\sqrt{6}}{\pi} \left[ 0.5772 + \ln\left(\ln\left(\frac{T}{T - 1}\right)\right) \right]$$

### 2. Log-Pearson Type III (LP3) Distribution:
Applies Pearson Type III formulation to logarithmic transformed data $y = \log_{10}(x)$:
$$y_T = \bar{y} + K_{LP3}(T, C_s) \cdot s_y$$
Where $C_s$ is the coefficient of skewness:
$$C_s = \frac{N \sum (y - \bar{y})^3}{(N - 1)(N - 2) s_y^3}$$

### 3. Empirical Sherman & Bernard IDF Parameterization:
$$\text{Sherman}: i = \frac{a}{(D + b)^c} \quad \text{where } a = K \cdot T^m$$
$$\text{Bernard}: i = \frac{K \cdot T^m}{D^n}$$
Non-linear least squares optimization was used to minimize Root Mean Square Error (RMSE) across return periods $T \in \{2, 5, 10, 25, 50, 100\text{ years}\}$ and durations $D \in \{15, 30, 60, 120, 360, 720, 1440\text{ minutes}\}$.

---

## 2. FAO-56 Penman-Monteith Evapotranspiration Formulation

$$ET_0 = \frac{0.408 \Delta (R_n - G) + \gamma \frac{900}{T_{mean} + 273} u_2 (e_s - e_a)}{\Delta + \gamma (1 + 0.34 u_2)}$$
Where:
* $ET_0$: Reference evapotranspiration ($\text{mm/day}$).
* $R_n$: Net radiation at the crop surface ($\text{MJ/m}^2/\text{day}$).
* $G$: Soil heat flux density ($\approx 0$ for daily calculations).
* $\Delta$: Slope of saturation vapor pressure-temperature curve ($\text{kPa/}^\circ\text{C}$):
  $$\Delta = \frac{4098 [0.6108 \exp(\frac{17.27 T}{T + 237.3})]}{(T + 237.3)^2}$$
* $\gamma$: Psychrometric constant ($\approx 0.067\text{ kPa/}^\circ\text{C}$).
* $(e_s - e_a)$: Vapor pressure deficit ($\text{kPa}$).
