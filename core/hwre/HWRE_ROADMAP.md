# HWRE — Roadmap

> Complete preparation pathway for HWRE-focused placements (NHPC, CWC, WAPCOS, AECOM, L&T Water, Tata Projects, consulting firms).

## Syllabus Coverage

| # | Subject | Priority | Study Guide | Weight |
|---|---------|:--------:|-------------|:------:|
| 1 | Fluid Mechanics & Hydraulics | P0 | [hydraulics.md](hydraulics/hydraulics.md) | High |
| 2 | Open Channel Flow | P0 | [open-channel-flow.md](open_channel_flow/open-channel-flow.md) | High |
| 3 | Hydrology | P0 | [hydrology.md](hydrology/hydrology.md) | High |
| 4 | Groundwater | P1 | [groundwater.md](water_supply/groundwater.md) | Medium |
| 5 | Water Resources | P0 | [water-resources-engineering.md](water_resources/water-resources-engineering.md) | High |
| 6 | Sediment Transport | P0 | [sediment-transport.md](hydrology/sediment-transport.md) | Medium |
| 7 | Turbulence / CFD | P0 | [turbulence-modeling.md](hydraulics/turbulence-modeling.md) | Medium |
| 8 | Irrigation | P1 | [irrigation-engineering.md](irrigation/irrigation-engineering.md) | Medium |
| 9 | Flood Control | P1 | [flood-control.md](flood_control/flood-control.md) | Medium |
| 10 | Wastewater | P1 | [wastewater-engineering.md](wastewater/wastewater-engineering.md) | Low |
| 11 | Water Supply | P1 | [water-supply.md](water_supply/water-supply.md) | Low |

## 6-Stage Progression

```
STAGE 1: FOUNDATION      → Fluid mechanics + OCF fundamentals
STAGE 2: CORE HYDROLOGY  → Precipitation, runoff, UH, routing
STAGE 3: WATER RESOURCES → Reservoirs, canals, irrigation, groundwater
STAGE 4: APPLIED HWRE    → Flood control, wastewater, water supply
STAGE 5: MODELLING       → HEC-HMS → HEC-RAS → GIS pipeline
STAGE 6: INTERVIEW       → Q&A bank, mock tests, error analysis, revision
```

### Stage 1: Foundation (Week 1)
- [ ] Fluid properties, hydrostatics, Bernoulli, momentum
- [ ] Pipe flow: Darcy-Weisbach, Moody, minor losses
- [ ] Open channel: specific energy, critical depth, hydraulic jump
- [ ] GVF profiles (M/S/C/A/H profiles)
- **Resources**: [`hydraulics.md`](hydraulics/hydraulics.md) · [`open-channel-flow.md`](open_channel_flow/open-channel-flow.md) · [Formulas §1–2](formulas/hwre-formulas.md#1-fluid-mechanics--hydraulics)

### Stage 2: Core Hydrology (Week 2)
- [ ] Hydrologic cycle, precipitation, infiltration models
- [ ] Unit hydrograph: derivation, S-curve, Snyder
- [ ] Flood frequency: Gumbel, Log-Pearson III
- [ ] Flood routing: Muskingum, level-pool
- **Resources**: [`hydrology.md`](hydrology/hydrology.md) · [Formulas §3](formulas/hwre-formulas.md#3-hydrology)

### Stage 3: Water Resources (Week 3)
- [ ] Reservoir design: mass curve, yield, sedimentation
- [ ] Canal design: Lacey, Kennedy, Manning
- [ ] Groundwater: Darcy, Theis, Cooper-Jacob, Thiem
- [ ] Irrigation: duty-delta, efficiencies, crop water requirement
- **Resources**: [`water-resources-engineering.md`](water_resources/water-resources-engineering.md) · [`groundwater.md`](water_supply/groundwater.md) · [`irrigation-engineering.md`](irrigation/irrigation-engineering.md)

### Stage 4: Applied HWRE (Week 4)
- [ ] Flood control structures, levees, spillways
- [ ] Sediment transport: Shields, MPM, Rouse, scour
- [ ] Wastewater: BOD, ASP, treatment train
- [ ] Water supply: demand, treatment, distribution
- **Resources**: [`flood-control.md`](flood_control/flood-control.md) · [`sediment-transport.md`](hydrology/sediment-transport.md) · [`wastewater-engineering.md`](wastewater/wastewater-engineering.md) · [`water-supply.md`](water_supply/water-supply.md)

### Stage 5: Modelling (Week 5)
- [ ] HEC-HMS: watershed setup, loss methods, transform, routing
- [ ] HEC-RAS: geometry, steady/unsteady, bridges, dam breach
- [ ] GIS: RAS Mapper, terrain processing, flood mapping
- **Resources**: [`MODELLING.md`](MODELLING.md) · [HEC-HMS Tutorial](../../software-and-tech/deep-dives/hec-hms-tutorial.md) · [HEC-RAS Walkthrough](../../software-and-tech/deep-dives/hec-ras-walkthrough.md)

### Stage 6: Interview (Week 6)
- [ ] Review [`INTERVIEW.md`](INTERVIEW.md) Q&A bank
- [ ] Take [`mocks/hwre-mock-1.md`](mocks/hwre-mock-1.md) under timed conditions
- [ ] Log errors in [`ERROR_ANALYSIS.md`](ERROR_ANALYSIS.md)
- [ ] Review [`TRAPS.md`](TRAPS.md) before every mock
- [ ] Final revision via [`RAPID_REVISION.md`](RAPID_REVISION.md)

## Inter-Subject Dependencies

```
Fluid Mechanics ──→ Open Channel Flow ──→ Flood Routing
      │                    │                    │
      ↓                    ↓                    ↓
Hydrology ──────────→ Water Resources ──→ Flood Control
      │                    │
      ↓                    ↓
Groundwater ──────→ Irrigation ──→ Water Supply
      │
      ↓
Sediment Transport ←── Open Channel Flow
      │
      ↓
Turbulence / CFD ──→ Modelling (HEC-RAS, OpenFOAM)
```

## GATE + Placement Connection

| GATE Topic | Placement Relevance | Companies |
|------------|--------------------|-----------|
| Fluid Mechanics | Pipe networks, pumps | AECOM, L&T, Tata Projects |
| Open Channel Flow | River modeling, HEC-RAS | CWPRS, WAPCOS, NHPC |
| Hydrology | Flood estimation, HEC-HMS | CWC, NHPC, WAPCOS |
| Groundwater | Well design, MODFLOW | CGWB, consulting firms |
| Water Resources | Reservoir operation | NHPC, state water boards |
| Sediment Transport | Scour analysis | CWPRS, consulting firms |
| Turbulence / CFD | OpenFOAM, research | IITs, ANSYS, research labs |

> **Cross-reference**: GATE Civil formula sheet covers the same topics with P0–P3 tags — [`core/gate/formulas/gate-civil-formulas.md`](../gate/formulas/gate-civil-formulas.md)

## Related

- [MASTER_INDEX.md](MASTER_INDEX.md) · [30/60/90-Day Plan](HWRE_30_60_90_DAY_PLAN.md) · [Rapid Revision](RAPID_REVISION.md)