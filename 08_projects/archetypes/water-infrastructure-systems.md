# Archetype 3: Hydro-Meteorological Frequency & Water Network Systems

> **Domain**: Water Resources Engineering / Municipal Infrastructure / Geospatial Analysis  
> **Status**: [HYPOTHETICAL ENGINEERING CASE ARCHETYPE — SAMPLE FOR INTERVIEW PRACTICE]  
> **Purpose**: Demonstrates core engineering calculations across frequency analysis, evapotranspiration modeling, pipe network pressure optimization, and geospatial catchment processing.

---

## 1. Executive Summary & Problem Formulation

* **Engineering Challenge**: Municipal water security and stormwater drainage systems require integrated hydrological and hydraulic design. Design rainfall intensities must be derived for extreme event return periods, while pipe distribution networks must maintain residual pressure within statutory limits under diurnal peak demands.
* **Objective**: Establish an end-to-end infrastructure pipeline integrating rainfall Intensity-Duration-Frequency (IDF) curves, FAO-56 reference evapotranspiration, and EPANET hydraulic network pressure head calibration.
* **Target Roles**: Core Civil Engineering, Urban Infrastructure Consulting, Environmental Systems Management.

---

## 2. Engineering Formulations & Methods

### 2.1 Rainfall Frequency Analysis (IDF Curves)
Extreme value distributions fitted to annual maximum rainfall series across multiple durations (15 min to 24 hr):

* **Gumbel Extreme Value Type I (EV-I)**:
  $$x_T = \bar{x} + K_T \cdot s, \quad K_T = -\frac{\sqrt{6}}{\pi} \left[0.5772 + \ln\left(\ln\left(\frac{T}{T-1}\right)\right)\right]$$

* **Log-Pearson Type III (LP3)**:
  $$y_T = \bar{y} + K_T(\gamma_y) \cdot s_y, \quad y = \log_{10}(x)$$

* **Sherman Empirical IDF Equation**:
  $$i = \frac{c \cdot T^m}{(t + d)^n}$$

### 2.2 FAO-56 Penman-Monteith Evapotranspiration
Standard physical model for reference crop evapotranspiration $ET_0$:

$$ET_0 = \frac{0.408 \Delta (R_n - G) + \gamma \frac{900}{T + 273} u_2 (e_s - e_a)}{\Delta + \gamma (1 + 0.34 u_2)}$$

where $R_n$ is net radiation, $G$ is soil heat flux, $T$ is mean air temperature, $u_2$ is wind speed at 2 m height, and $(e_s - e_a)$ is vapor pressure deficit.

### 2.3 Pipe Network Hydraulics (EPANET / Hazen-Williams)
For steady-state pressurized pipe networks:

$$h_f = 10.67 \cdot L \cdot Q^{1.852} \cdot C^{-1.852} \cdot D^{-4.87}$$

where $h_f$ is head loss, $L$ is pipe length, $D$ is pipe diameter, $Q$ is flow rate, and $C$ is Hazen-Williams roughness coefficient.

---

## 3. Illustrative Defense & Sample Interview Questions

### Q1: "How do you select between Gumbel EV-I and Log-Pearson Type III distributions?"
> **Model Response**: "We evaluate goodness-of-fit using the Chi-Square ($\chi^2$) and Kolmogorov-Smirnov (K-S) tests alongside sample skewness $\gamma$. When the skewness coefficient of the log-transformed data is near zero, Gumbel provides a parsimonious two-parameter fit. When sample skewness deviates significantly from zero ($|\gamma_y| > 0.4$), the three-parameter Log-Pearson Type III distribution better accounts for tail thickness and avoids underestimating extreme return-period rainfall depths."

### Q2: "In water distribution networks, how do you handle diurnal demand variation?"
> **Model Response**: "In EPANET, base nodal demands are modulated by time-varying demand multipliers representing morning and evening consumption peaks (typically $1.5\times$ to $2.2\times$ average day demand). The hydraulic simulation ensures residual pressure heads remain between statutory boundaries (minimum 12 m head to prevent backflow and contamination, and maximum 45 m head to limit pipe joint leakage and burst risk)."

### Q3: "How does geospatial catchment analysis integrate with design discharge estimation?"
> **Model Response**: "Using digital elevation models (DEM) in QGIS or Python (WhiteboxTools), we delineate stream networks and compute flow accumulation. Key geomorphological parameters—including catchment area $A$, mainstream length $L$, centroidal length $L_c$, and basin slope $S$—directly calibrate the Kirpich time-of-concentration formula ($t_c = 0.01947 L^{0.77} S^{-0.385}$), which defines the critical design storm duration for peak runoff estimation."
