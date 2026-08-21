# Groundwater

## Introduction

Groundwater is water stored beneath the Earth's surface in pore spaces and fractures of rock and soil. It provides approximately 50% of global drinking water and is essential for agriculture and industry.

## Darcy's Law

### Statement
The discharge velocity (seepage velocity) through a porous medium is directly proportional to the hydraulic gradient.

### Equation
- Q = K × i × A
- v = Q / A = K × i
  - Q = discharge (m³/s)
  - K = hydraulic conductivity (m/s)
  - i = hydraulic gradient (dimensionless)
  - A = cross-sectional area (m²)
  - v = seepage velocity (m/s)

### Validity
- Valid for laminar flow in saturated media
- Applicable for Reynolds numbers < 1 to 10 depending on media

## Aquifer Properties

### Transmissivity (T)
- Capacity of an aquifer to transmit water
- T = K × b (b = saturated thickness)
- Units: m²/day

### Storativity (S) or Storage Coefficient
- Volume of water released from or taken into storage per unit surface area per unit change in head
- Confined aquifer: S = ρg × b × α (compressibility of water and matrix)
- Unconfined aquifer: S ≈ Sy (specific yield, typically 0.01–0.30)

### Specific Yield (Sy) vs. Specific Retention (Sr)
- Sy: Gravity-drained water released from storage (effective porosity)
- Sr: Water held against gravity (adsorbed water + capillary water)
- Sy + Sr = n (total porosity)

## Types of Aquifers

### Unconfined Aquifer
- Water table as the upper boundary
- Phreatic surface at atmospheric pressure
- Recharge occurs directly through the vadose zone

### Confined Aquifer
- Bounded by aquitards (low-permeability layers)
- Artesian pressure when potentiometric surface is above ground
- No direct recharge; relies on leakage or distant recharge zones

### Leaky Aquifer
- Semi-confined with leakage through overlying/underlying beds
- Hantush-Jacob solution for leaky confined aquifers

## Well Hydraulics

### Steady-State Flow to a Well
- **Thiem equation (confined):**
  - (h₁² - h₂²) / ln(r₂/r₁) = Q / (2πT)
- **Dupuit-Forchheimer (unconfined):**
  - (h₁² - h₂²) / ln(r₂/r₁) = Q / (πK)

### Unsteady-State Flow (Theis Solution)
- s = (Q / 4πT) × W(u)
- Where:
  - s = drawdown
  - W(u) = well function (exponential integral)
  - u = r²S / 4Tt

### Cooper-Jacob Approximation
- For large u (u > 0.01):
  - s = (Q / 4πT) × [-0.5772 - ln(u)]
- Allows determination of T and S from straight-line analysis of drawdown vs. log time

### Specific Capacity
- Sc = Q / s
- Indicator of aquifer productivity; declines with time due to aquifer dewatering

## Groundwater Flow Software

| Tool | Application |
|------|-------------|
| MODFLOW 6 | Modular, multi-model groundwater simulation |
| SEEP/W | Seepage and groundwater flow analysis |
| ICPR | Hydraulic and groundwater modeling |

## Groundwater Exploration

### Methods
- Surface geological and geophysical surveys
- Test drilling and aquifer testing (pumping tests, slug tests)
- Remote sensing for lineament mapping and recharge zone identification

### Pumping Test Analysis
- Constant-rate test: Step-drawdown and constant-rate phases
- Recovery test: Aquifer properties from post-pumping recovery
- Interpretation: Theis, Jacob, Theis recovery, Hantush-Bierschenk

## Contamination & Remediation

### Transport Processes
- Advection, dispersion (mechanical and hydrodynamic), diffusion, adsorption, decay
- Advection-dispersion equation for solute transport

### Remediation Strategies
- Pump-and-treat systems
- In-situ bioremediation and chemical oxidation
- Permeable reactive barriers

## Further expansion needed
- Groundwater modeling with MODFLOW packages
- Vadose zone flow and transport
- Coastal aquifer management and seawater intrusion
- Isotope hydrology for recharge estimation

## Sources
- `F:\2k26Placement\Civil_Placement_IITK\README.md`
- `F:\2k26Placement\awesome-civil-engineering\README.md`