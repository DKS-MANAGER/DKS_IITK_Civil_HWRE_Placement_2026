# Engineering Project Mapping Matrix: Civil/Fluids/Data to EV Engineering

## Overview
This document provides direct, one-to-one engineering translations between foundational engineering and computational project archetypes and the core technical demands of **Ola Electric's Product Engineering & Advanced Manufacturing** divisions.

---

## Project Archetype 1: Multi-Phase Computational Fluid Dynamics & Hydrodynamic Modeling (OpenFOAM CFD)

### Technical Profile Details:
- **Tools:** OpenFOAM (Linux HPC cluster), snappyHexMesh, ParaView, Python.
- **Physics Modeled:** Multiphase volume-of-fluid (VOF), incompressible Navier-Stokes, Reynolds-Averaged Navier-Stokes (RANS) closure using $k-\omega$ SST model.
- **Mesh & Boundary Resolution:** Viscous sublayer resolution ($y^+ \le 1$), boundary layer inflation layers, Courant number ($Co \le 0.8$) dynamic time-step control.
- **Validation:** Correlated numerical shear stress and vortex circulation against physical acoustic Doppler velocimetry (ADV) flume benchmark experiments.

### Direct Automotive Translation for Ola Electric:
| Computational Capability | Direct Ola EV Engineering Application | Technical Talking Point for Interview |
|:---|:---|:---|
| **Boundary Layer $y^+ \le 1$ Resolution** | **Conjugate Heat Transfer (CHT) in Battery Cold Plates** | *"In battery liquid cooling plates, resolving near-wall conductive boundary layer resistance without unphysical wall functions is critical to predicting peak cell temperatures. OpenFOAM low-Reynolds mesh generation skills transfer directly to battery thermal CAE."* |
| **Multiphase VOF Free-Surface Tracking** | **Battery Thermal Runaway Venting & Gas-Liquid Dynamics** | *"During thermal runaway, cells vent mixed high-pressure gases ($CO, HF, H_2$) and liquid droplet aerosols. Modeling multiphase interface tracking and directional blast pressure relief mirrors VOF free-surface simulations."* |
| **Separated Flow & Vortex Shedding ($k-\omega$ SST)** | **Scooter Underbody & Handlebar Aerodynamic Drag** | *"Adverse pressure gradient separation beneath submerged bluff bodies shares the identical Navier-Stokes physics as airflow separation around scooter wheel arches and underbody battery casings, directly impacting highway range."* |
| **HPC Cluster Linux Automation** | **Automated CAE Batch Meshing & Parametric Optimization** | *"Custom Bash and Python automation pipelines across multi-node HPC clusters enable automated parametric sweep studies that accelerate vehicle design cycles."* |

---

## Project Archetype 2: Predictive Machine Learning & Reliability Modeling (XGBoost & TreeSHAP)

### Technical Profile Details:
- **Dataset:** Benchmark multi-variate infrastructure inspection & asset telemetry records.
- **Algorithm:** Extreme Gradient Boosting (XGBoost) classifier with Bayesian hyperparameter tuning.
- **Explainability:** TreeSHAP (SHapley Additive exPlanations) for global feature importance and local instance-level decision trees.
- **Performance:** ROC-AUC of 0.89+, Precision-Recall optimization for high-cost false negative minimization.

### Direct Automotive Translation for Ola Electric:
| Machine Learning Capability | Direct Ola EV Engineering Application | Technical Talking Point for Interview |
|:---|:---|:---|
| **Imbalanced Class Classification (Rare Failures)** | **Automated In-Line Defect Detection in Cell Calendering / Welding** | *"In high-volume manufacturing, defects are rare ($< 0.1\%$). Handling extreme class imbalance using scale-pos-weight and focal loss provides the exact technique needed to train computer vision models detecting micro-pinholes in coated electrodes."* |
| **TreeSHAP Explainable AI** | **Root-Cause Analysis (D4) in Manufacturing Escapes** | *"Black-box neural networks cannot be audited in an automotive plant. Using TreeSHAP to attribute exact mathematical weights to failure features can be applied to sensor telemetry to identify which robotic weld parameter (current, voltage, travel speed) caused a joint failure."* |
| **Feature Engineering on Noisy Sensor Data** | **Predictive Maintenance for 5,000+ Industrial Robots at Futurefactory** | *"By transforming raw multi-axial vibration and motor current draw time-series into frequency-domain spectral features, engineers can predict robotic gearhead backlash and bearing failure before line stoppages occur."* |

---

## Project Archetype 3: Stochastic Time-Series & Extreme Value Modeling (SARIMAX & GEV Distributions)

### Technical Profile Details:
- **Methods:** Seasonal Autoregressive Integrated Moving Average with Exogenous Regressors (SARIMAX), Extreme Value Distributions (Gumbel, Generalized Extreme Value - GEV, Pearson Type III).
- **Domain:** Time-series forecasting, probabilistic return-period risk calculations, signal processing.

### Direct Automotive Translation for Ola Electric:
| Statistical Time-Series Capability | Direct Ola EV Engineering Application | Technical Talking Point for Interview |
|:---|:---|:---|
| **Stochastic Time-Series Forecasting (SARIMAX)** | **BMS State of Charge (SoC) & State of Health (SoH) Trajectory Prediction** | *"Vehicle battery voltage and current profiles are dynamic, non-stationary time-series. Utilizing SARIMAX and Kalman filtering allows engineers to develop robust state estimators that decouple ambient temperature fluctuations from electrochemical degradation."* |
| **Extreme Value Distribution Modeling (GEV / Gumbel)** | **Automotive Accelerated Fatigue Life Testing ($3\sigma / 6\sigma$ Extremes)** | *"In vehicle durability testing, failure is driven not by average road loads, but by the extreme tail-probability shock events ($5g$ pothole impacts). Mathematical mastery of extreme value theory enables statistically sound accelerated durability life predictions."* |
