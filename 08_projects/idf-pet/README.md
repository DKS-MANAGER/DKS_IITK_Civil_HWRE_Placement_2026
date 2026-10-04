# Project: IDF Rainfall Frequency & Potential Evapotranspiration Modeling

> **Project Code**: `idf-pet`  
> **Domain**: Urban Hydrology, Statistical Hydro-Meteorology & Water Balance  
> **Key Tools**: Python (SciPy, Matplotlib), R (evd / extRemes), FAO-56 Penman-Monteith, IMD Gridded Data

---

## 1. Project Overview & Motivation

Intensity-Duration-Frequency (IDF) relationships are fundamental design standards for urban storm sewer networks, culverts, and flood retention basins. Under accelerating climate change, historical static IDF curves increasingly lead to urban drainage under-capacity and severe waterlogging. Coupled with this, accurate Reference Crop Evapotranspiration ($ET_0$) modeling is critical for regional irrigation scheduling and water budget modeling.

### Core Objectives:
1. Extract and process sub-daily and daily extreme precipitation series across 40 years from Indian Meteorological Department (IMD) gridded datasets.
2. Fit theoretical extreme value distributions (Gumbel EV-I, Generalized Extreme Value / GEV, Log-Pearson Type III).
3. Derive updated empirical IDF equations (Sherman and Bernard parameterizations) for 2, 5, 10, 25, 50, and 100-year return periods.
4. Model daily Reference Evapotranspiration ($ET_0$) using the FAO-56 Penman-Monteith method and analyze seasonal irrigation deficits.

---

## 2. Mathematical Formulations

### 1. Bernard IDF Equation:
$$i = \frac{K \cdot T^m}{D^n}$$
Where $i$ is rainfall intensity ($\text{mm/hr}$), $T$ is return period (years), $D$ is duration (minutes or hours), and $K, m, n$ are regional empirical fitting parameters derived via non-linear regression.

### 2. FAO-56 Penman-Monteith Formulation:
$$ET_0 = \frac{0.408 \Delta (R_n - G) + \gamma \frac{900}{T + 273} u_2 (e_s - e_a)}{\Delta + \gamma (1 + 0.34 u_2)}$$
Where $R_n$ is net solar radiation, $G$ is soil heat flux density, $T$ is mean air temperature, $u_2$ is wind speed at $2\text{ m}$ height, and $(e_s - e_a)$ is vapor pressure deficit.

---

## 3. Results & Design Implications

* **Extreme Rainfall Shift**: Identified a $22\%$ increase in short-duration (< 2-hour) rainfall intensities for 10-year and 25-year return periods over the recent 2000–2020 epoch compared to the 1980–2000 baseline.
* **Urban Drainage Sizing**: Traditional storm drainage designed under legacy CPHEEO curves was found to be undersized by $18\text{--}25\%$, explaining recurrent urban street inundation.
* **Annual Water Deficit**: Quantified peak summer $ET_0$ at $7.8\text{ mm/day}$ in May, highlighting an annual crop water deficit of $680\text{ mm}$ requiring supplemental groundwater extraction.

---

## 4. Interview Defense & Technical Q&A

### Q1: "Why prefer Log-Pearson Type III or GEV over simple Gumbel distribution for extreme rainfall?"
* **Answer**: *"The Gumbel (EV-I) distribution has a fixed skewness coefficient ($1.14$) and exponential tails, which often underestimates extreme precipitation tails. GEV and Log-Pearson Type III incorporate a shape parameter (allowing heavy Frechet-type tails), providing a statistically superior fit to severe convective rainfall events ($p < 0.05$ on Anderson-Darling and Kolmogorov-Smirnov tests)."*

### Q2: "How did you estimate sub-daily rainfall intensities when only 24-hour daily rainfall records were available?"
* **Answer**: *"I applied the Indian Meteorological Department (IMD) empirical disaggregation formula: $P_t = P_{24} \cdot \left(\frac{t}{24}\right)^{0.333}$, as well as synthetic storm hyetograph temporal disaggregation methods (e.g., NRCS Type-II and alternating block methods)."*
