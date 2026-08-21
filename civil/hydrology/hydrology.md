# Hydrology

## Hydrologic Cycle

The hydrologic cycle describes the continuous movement of water on, above, and below the Earth's surface. Key processes include:
- **Precipitation:** Rain, snow, hail, and other forms of atmospheric moisture reaching the ground
- **Evaporation:** Liquid-to-vapor phase change from water bodies and soil
- **Transpiration:** Water vapor release from vegetation
- **Infiltration:** Entry of surface water into the subsurface
- **Interception:** Capture of precipitation by vegetation and structures
- **Runoff:** Overland and channel flow returning to oceans and lakes

## Rainfall-Runoff Relationships

### Catchment Response
- Rainfall excess = Precipitation - infiltration losses - interception losses
- Time of concentration: Time for water to travel from the most distant point to the outlet
- Lag time: Delay between centroid of rainfall excess and peak discharge

### Infiltration
- Horton's equation: Exponential decay of infiltration capacity with time
- Philip's equation: Two-term infiltration model
- Green-Ampt model: Sharp wetting front approximation

## Hydrograph Analysis

### Unit Hydrograph
- Direct runoff hydrograph resulting from 1 unit (e.g., 1 cm) of effective rainfall distributed uniformly over the catchment
- Assumes linearity and time-invariance of the catchment response
- Application: Synthesis of runoff hydrographs for any storm duration and excess rainfall

### Flood Frequency Analysis
- Fitting probability distributions (Gumbel, Log-Pearson Type III, etc.) to annual maximum series
- Return period and exceedance probability relationships
- Risk and reliability concepts in hydrologic design

### Hydrograph Separation
- Baseflow separation methods: Straight-line, fixed-discharge, variable-discharge
- Filters such as Lyne-Hollick and Eckhardt for continuous streamflow separation

## Flood Routing

### Concept
- Determination of the outflow hydrograph from a reservoir or reach given the inflow hydrograph and storage characteristics

### Methods
- **Muskingum method:** Lumped conceptual model using storage and weighting coefficients
- **Kinematic wave:** Balances inertial and gravitational forces; ignores pressure and local acceleration
- **Dynamic wave:** Full Saint-Venant equations; most accurate but computationally intensive

### Reservoir Routing
- Level-pool routing: Assumes horizontal water surface
- Storage indication method: Uses storage-outflow relationship

## Groundwater Hydrology

### Darcy's Law
- Q = K × i × A
- Where:
  - Q = discharge
  - K = hydraulic conductivity
  - i = hydraulic gradient
  - A = cross-sectional area

### Aquifer Properties
- Transmissivity (T) = K × b (b = aquifer thickness)
- Storativity (S) = Volume of water released/added per unit surface area per unit change in head
- Specific yield (Sy) vs. specific storage (Ss)

### Well Hydraulics
- Steady radial flow to a well in a confined aquifer (Theis non-equilibrium equation)
- Unsteady flow: Theis solution using the well function W(u)
- Cooper-Jacob approximation for large values of u
- Thiem equilibrium equation for steady-state cone of depression

### Theis Solution
- s = (Q / 4πT) × W(u)
- Where:
  - s = drawdown
  - Q = pumping rate
  - T = transmissivity
  - u = r²S / 4Tt
  - W(u) = exponential integral (well function)

## Groundwater Modeling Software

| Tool | Application |
|------|-------------|
| MODFLOW 6 | Modular groundwater flow and surface-water interaction modeling |
| SEEP/W | Seepage and groundwater flow analysis |
| ICPR | Integrated hydraulic and groundwater modeling |

## Further expansion needed
- Detailed derivation of unit hydrograph theory
- Rainfall-runoff model calibration techniques
- Advanced groundwater flow numerical methods
- Remote sensing applications in hydrology

## Sources
- `F:\2k26Placement\Civil_Placement_IITK\README.md`
- `F:\2k26Placement\awesome-civil-engineering\README.md`