# Sediment Transport

## Overview

Sediment transport describes the movement of solid particles by flowing water. It governs river morphology, reservoir siltation, coastal erosion, and scour around hydraulic structures. Accurate prediction requires understanding particle dynamics, turbulence-particle interactions, and bed evolution.

## Modes of Transport

### Bed Load
- Sediment rolls, slides, or hops (saltates) along the bed
- Dominated by larger, heavier particles
- Described by empirical formulas such as Meyer-Peter Müller and Engelund-Hansen

### Suspended Load
- Particles maintained in suspension by turbulence
- Concentration typically follows a Rouse profile: c/cₐ = (yₐ/y)^(Z)
  - Z = w / (κ u*)
  - w = fall velocity
  - κ = von Karman constant
  - u* = shear velocity

### Wash Load
- Very fine particles carried in suspension without deposition under normal flows
- Originates from upstream sources; not in equilibrium with local bed material

## Incipient Motion

### Shields Parameter
- τ* = τ / [(ρs - ρ)gd]
- Where:
  - τ = bed shear stress
  - ρs = sediment density
  - ρ = fluid density
  - d = grain diameter
- Critical Shields parameter (~0.047 for uniform grains in clear water) marks the onset of motion

### Critical Shear Stress
- τc = θc(ρs - ρ)gd
- Depends on grain size, density, and flow conditions

## Bed Forms

- **Ripples:** Small-scale, asymmetric; wavelengths < 0.3 m
- **Dunes:** Large-scale, asymmetric; wavelengths up to hundreds of meters
- **Plane bed:** Flat surface; occurs at high transport rates
- **Antidunes:** Symmetric, upstream-migrating; form at high Froude numbers
- **Wash loading:** No bedforms; fine sediment in suspension

## Scour Mechanics

### Clear-Water Scour
- Occurs when there is no sediment supply; maximum scour depth limited by equilibrium
- Live-bed scour: Sediment supply replenishes the scour hole; equilibrium scour depth depends on transport capacity

### Key Structures Affected
- Bridge piers: Local scour from flow contraction and vortex systems
- Abutments: Flow obstruction and lateral contraction
- Spillways and stilling basins: High-velocity jet impact and hydraulic jump scour

### Scour Depth Estimation
- HEC-18 and HEC-23 guidelines for bridge scour
- Laursen's theory for clear-water scour at piers
- Live-bed scour equations incorporating sediment transport capacity

## Computational Approaches

### Empirical Formulas
- Engelund-Hansen, Ackers-White, Yang for total load
- Van Rijn for bed load and suspended load separately

### Numerical Models
- **SRH-2D:** Two-dimensional sedimentation and river hydraulics (USBR)
- **FLOW-3D:** CFD for detailed local scour and turbulence-sediment interaction
- **SedFoam / sedInterFoam:** OpenFOAM-based solvers for sediment-laden flows and multiphase transport
- **Delft3D:** Morphodynamic modeling for coastal and estuarine environments

## Sediment Budget & Budget Analysis
- Sediment yield from a catchment
- Reservoir sedimentation rates and useful life estimation
- Channel aggradation and degradation trends

## Environmental Considerations
- Sediment as a vector for pollutants and nutrients
- Habitat maintenance flows and sediment pulses
- Dam removal and sediment release management

## Further expansion needed
- Detailed derivation of sediment transport equations
- Numerical schemes for morphodynamic modeling
- Scale effects in physical model studies
- Climate change impacts on sediment yield

## References

* [Civil_Placement_IITK](https://github.com/DKS-MANAGER/Civil_Placement_IITK)
* [awesome-civil-engineering](https://github.com/awesome-civil-engineering/awesome-civil-engineering)