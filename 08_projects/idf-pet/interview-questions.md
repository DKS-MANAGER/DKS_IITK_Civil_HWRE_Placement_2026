# Interview Grilling Questions — IDF Rainfall Frequency & PET (`idf-pet`)

> **Focus**: Extreme value theory, temporal rainfall disaggregation, evapotranspiration physics, climate change impacts, and statistical model validation.

---

## 1. Technical Grilling Questions & Answers

### Q1: "Why choose Log-Pearson Type III over Gumbel (EV-I) for extreme rainfall, and how do you test which distribution is superior?"
* **Answer**:
  * **Theoretical distinction**: Gumbel assumes a fixed skewness ($C_s = 1.1396$), meaning the tail behavior is strictly exponential and cannot adapt to heavier or lighter empirical skewness in the observed data. Log-Pearson Type III (LP3) incorporates sample skewness $C_s$ directly through a third parameter, providing superior flexibility for skewed hydrological extremes.
  * **Model selection tests**: We evaluate goodness-of-fit using the **Kolmogorov-Smirnov (K-S) test**, **Anderson-Darling test** (which gives more weight to the extreme tails than K-S), and **Akaike Information Criterion (AIC / BIC)**. In our analysis, LP3 achieved lower AIC ($\Delta \text{AIC} = -14.2$) and better tail fit for $T \ge 25\text{ years}$ where Gumbel systematically under-predicted peak 1-hour intensities by $12\%$.

### Q2: "How did you disaggregate daily rainfall totals into sub-hourly (15-min, 30-min, 1-hour) intervals without continuous autographic gauge records?"
* **Answer**: We implemented the **IMD (Indian Meteorological Department) Empirical Reduction Formulation** and verified it against synthetic storm generation (Modified Bartlett-Lewis Rectangular Pulse model):
  $$P_t = P_{24} \cdot \left(\frac{t}{24}\right)^{1/3}$$
  Where $P_t$ is rainfall depth in time $t$ (hours) and $P_{24}$ is daily rainfall. For sub-hourly resolution, we fitted local dimensionless cumulative rainfall curves (Huff Quartile curves / SCS Type-II distribution) to capture the peak burst intensity occurring within the first 30–40% of storm duration.

### Q3: "In the FAO-56 Penman-Monteith equation, which parameter is the most sensitive, and what happens if wind speed data is unavailable?"
* **Answer**:
  * **Sensitivity**: In semi-arid and sub-humid Indian catchments, the vapor pressure deficit $(e_s - e_a)$ and net solar radiation $R_n$ are the most sensitive drivers of $ET_0$. During hot pre-monsoon periods, aerodynamic demand dominates; during monsoon, radiation dominates.
  * **Missing wind data**: If $u_2$ is missing, FAO-56 allows defaulting to global average $u_2 \approx 2.0\text{ m/s}$, or calibrating against the **Hargreaves-Samani temperature-based method** ($ET_0 = 0.0023 \cdot R_a \cdot (T_{max} - T_{min})^{0.5} \cdot (T_{mean} + 17.8)$), adjusting the empirical coefficient using local historical humidity regimes.

### Q4: "How does non-stationarity due to climate change affect classic IDF curves, and how can engineers design for it?"
* **Answer**: Traditional IDF assumes **stationarity** (past statistical distributions predict future probabilities). Under climate change, convective storm intensity is increasing at roughly the Clausius-Clapeyron rate ($\approx 6–7\% \text{ per } ^\circ\text{C}$ of atmospheric warming). To address non-stationarity:
  1. We fit **Non-Stationary GEV models** where location ($\mu$) and scale ($\sigma$) parameters vary as functions of time or global mean temperature covariates: $\mu(t) = \mu_0 + \mu_1 t$.
  2. For engineering drainage design, we apply **Climate Change Scaling Factors (CCSF)** from CMIP6 ensemble projections, scaling baseline design intensities by $+15\%\text{ to }+25\%$ for 50-year design lifespans.
