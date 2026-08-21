# Flood Control

## Overview

Flood control encompasses structural and non-structural measures to reduce flood damage and protect life, property, and infrastructure. It draws on hydrology, hydraulics, and hydraulic structure design.

## Flood Causes & Classification

### Meteorological Causes
- Intense rainfall exceeding infiltration and channel capacity
- Cyclonic storms and hurricanes
- Snowmelt combined with rainfall
- Dam and levee failures

### Hydrologic Causes
- Saturated soils reducing infiltration
- Frozen ground or impervious surfaces increasing runoff
- Rapid snowmelt

### Classification by Source
- Riverine floods: Overflow of river banks
- Flash floods: Rapid onset in small catchments (< 500 km²)
- Urban floods: Storm drainage inadequacy
- Coastal floods: Storm surge, tsunamis, high tides

## Flood Estimation

### Design Flood
- Standard Project Flood (SPF): Hypothetical flood from most severe meteorologic/hydrologic combination
- Probable Maximum Flood (PMF): Flood from PMP (Probable Maximum Precipitation)
- Return period selection based on consequence class (e.g., 100-year, 500-year)

### Rainfall-Runoff Methods
- Rational method: Q = CiA (small catchments < 200 km²)
- SCS-CN method: Curve number for rainfall excess
- Unit hydrograph and S-hydrograph methods
- Flood frequency analysis: Gumbel, Log-Pearson Type III

## Flood Routing

### Concept
- Determination of outflow hydrograph from a channel reach or reservoir given the inflow hydrograph

### Hydraulic (Dynamic Wave) Routing
- Full Saint-Venant equations
- Most accurate; requires detailed cross-section data
- Used for HEC-RAS unsteady flow simulations

### Hydrologic (Lumped) Routing
- **Muskingum method:**
  - Oₖ = C₀Iₖ + C₁Iₖ₋₁ + C₂Oₖ₋₁
  - C₀ + C₁ + C₂ = 1
  - Parameters K (storage time constant) and x (weighting factor)
- Kinematic wave: Balances inertial and gravitational forces; suitable for steep channels
- Diffusion wave: Includes pressure gradient effects; balances diffusion and gravity

## Flood Control Structures

### Dams & Reservoirs
- Multi-purpose: Flood control storage, hydropower, irrigation, water supply
- Surplus weirs and emergency spillways for flood routing
- Dam break analysis: Inflow design flood (IDF), breach parameters, wave propagation

### Levees & Floodwalls
- Height and crest width design
- Seepage and piping considerations
- Stability against overtopping, seepage, and slope failure

### Diversion Channels & Bypasses
- Divert excess floodwater away from vulnerable areas
- Design capacity and alignment considerations

### Detention/Retention Basins
- Detention basin: Temporary storage, controlled release
- Retention basin: Permanent pool with flood surcharge
- Peak discharge reduction and downstream erosion protection

## Floodplain Management

### Zoning & Land Use
- Floodway and flood fringe delineation
- Encroachment restrictions in floodplains
- Flood-proofing: Dry flood-proofing, wet flood-proofing

### Warning Systems
- Real-time gauging stations and telemetry
- Flood forecasting models and early warning dissemination

### Non-Structural Measures
- Flood insurance programs
- Relocation of vulnerable infrastructure
- Wetland preservation for natural flood attenuation

## Software Tools

| Tool | Application |
|------|-------------|
| HEC-RAS | 1D/2D river and floodplain hydraulic modeling |
| HEC-HMS | Watershed runoff modeling and flood hydrograph generation |
| MIKE FLOOD | Integrated 1D/2D flood modeling |
| TUFLOW | Hydrodynamic and hydraulic modeling for floodplain management |
| Flood Modeller | 1D/2D hydraulic modeling for rivers, floodplains, and drainage |
| OpenFlows Flood | Coastal, riverine, and urban flood modeling |
| InfoWorks ICM | Integrated catchment and sewer flooding modeling |

## Design Standards
- IS 12094: Guidelines for preparation of flood management plans
- Central Water Commission (CWC) guidelines for flood estimation
- National Disaster Management Authority (NDMA) flood guidelines

## Further expansion needed
- Dam break modeling with HEC-RAS and FLO-2D
- Coastal flood modeling with storm surge
- Urban flood resilience and green infrastructure
- Risk-based flood management and probabilistic approaches

## Sources
- `F:\2k26Placement\Civil_Placement_IITK\README.md`
- `F:\2k26Placement\awesome-civil-engineering\README.md`