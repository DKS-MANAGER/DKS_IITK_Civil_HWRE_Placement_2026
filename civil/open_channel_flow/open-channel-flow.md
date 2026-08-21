# Open Channel Flow

## Definition & Scope

Open channel flow occurs when a fluid flows with a free surface exposed to atmospheric pressure. It is distinguished from pipe flow by the presence of this free surface, which introduces additional complexity in terms of varying depth, width, and velocity distribution.

## Classification by Flow Regime

### Steady vs. Unsteady
- **Steady flow:** Depth and velocity do not change with time at a given location
- **Unsteady flow:** Depth and velocity vary with time; governs flood wave propagation

### Uniform vs. Varied
- **Uniform flow:** Depth, velocity, and cross-section remain constant along the channel (normal depth)
- **Gradually Varied Flow (GVF):** Depth changes slowly over a long distance; surface slope ≈ bed slope
- **Rapidly Varied Flow (RVF):** Depth changes abruptly over a short distance; examples include hydraulic jumps and drops

## Fundamental Equations

### Continuity Equation
- For unsteady flow: ∂Q/∂x + ∂A/∂t = 0
- For steady flow: Q = constant along the channel

### Momentum Equation
- Saint-Venant equations form the foundation for unsteady open channel analysis
- Includes terms for local acceleration, convective acceleration, pressure, gravity, and friction

### Energy Equation
- Specific energy: E = y + V²/(2g)
- Alternate depth: Two possible depths for a given specific energy (subcritical and supercritical)

## Key Phenomena

### Hydraulic Jump
- Sudden transition from supercritical to subcritical flow
- Energy dissipation mechanism; used in stilling basins
- Conjugate depth relationship:
  - y₂/y₁ = (1/2) × [√(1 + 8Fr₁²) - 1]
  - Where Fr₁ = upstream Froude number
- Sequency depth: Depth at which specific energy is minimum; critical depth

### Critical Flow
- Froude number Fr = V/√(gD) = 1
- Minimum specific energy for a given discharge
- Controls flow measurement in flumes and weirs

### Flow Profiles (GVF)
- Classified by bed slope (mild, steep, critical, horizontal, adverse)
- M1, M2, M3 profiles for mild slopes
- S1, S2, S3 profiles for steep slopes
- Backwater curves: Profile upstream of a dam or obstruction
- Drawdown curves: Profile downstream of a free overfall

## Manning's Equation
- Empirical formula for uniform flow velocity: V = (1/n) × R^(2/3) × S^(1/2)
- Where:
  - n = Manning's roughness coefficient
  - R = hydraulic radius = A/P
  - S = energy slope (≈ bed slope for uniform flow)
- Applicable to both natural channels and engineered conduits

## Weirs & Flumes
- Sharp-crested weirs: Rectangular, triangular (V-notch), Cipolletti
- Broad-crested weirs: Critical flow control over a raised crest
- Flumes: Constricted sections designed to force critical depth for measurement

## Sediment Transport in Open Channels
- Bed load and suspended load mechanisms
- Critical tractive force (Shields parameter) for incipient motion
- Bed form evolution: Ripples, dunes, antidunes, plane bed

## Software Tools

| Tool | Application |
|------|-------------|
| HEC-RAS | 1D/2D river and open channel hydraulic modeling |
| MIKE FLOOD | Integrated 1D/2D flood modeling |
| TUFLOW | Hydrodynamic modeling for floodplain management |
| Flood Modeller | 1D/2D river, floodplain, and drainage modeling |
| SRH-2D | Two-dimensional sedimentation and river hydraulics |
| OpenFlows Flood | Coastal, riverine, and urban flood modeling |

## Design Applications
- Canal design for irrigation and drainage
- Culvert sizing and inlet/outlet control analysis
- Bridge scour assessment
- Floodplain delineation and zoning

## Further expansion needed
- Detailed derivation of Saint-Venant equations
- Numerical methods for GVF profile computation (direct step, standard step)
- Unsteady flow routing methods (Muskingum, kinematic wave, dynamic wave)
- Bridge hydraulics and scour depth calculations

## Sources
- `F:\2k26Placement\Civil_Placement_IITK\README.md`
- `F:\2k26Placement\awesome-civil-engineering\README.md`