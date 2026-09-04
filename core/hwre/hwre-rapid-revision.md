# Water Resources Engineer — Rapid Revision Sheet

> Last-minute revision for HWRE interviews. Core formulas, concepts, and key values in 15 minutes.

---

## Essential Formulas

### Hydraulics
| Formula | Equation | Use |
|:--------|:---------|:----|
| Continuity | Q = A × V | Mass conservation |
| Bernoulli | P/γ + V²/2g + z = const | Energy equation |
| Darcy-Weisbach | h_f = f(L/D)(V²/2g) | Pipe friction loss |
| Manning's | V = (1/n)R^(2/3)S₀^(1/2) | Open channel flow |
| Hazen-Williams | V = 0.849 × C × R^0.63 × S^0.54 | Water supply pipes |

### Open Channel Flow
| Formula | Equation |
|:--------|:---------|
| Specific Energy | E = y + V²/2g |
| Critical Depth (rectangular) | y_c = (q²/g)^(1/3) |
| Hydraulic Jump | y₂/y₁ = 0.5(√(1+8Fr₁²) − 1) |
| Energy Loss (jump) | ΔE = (y₂−y₁)³ / (4y₁y₂) |
| Froude Number | Fr = V/√(gy) |

### Hydrology
| Formula | Equation |
|:--------|:---------|
| Rational Method | Q = C × i × A |
| Unit Hydrograph | DR = Rainfall Excess × UH Ordinates |
| Muskingum | O₂ = C₀I₂ + C₁I₁ + C₂O₁ |
| C₀ = (−Kx+0.5Δt) / (K(1−x)+0.5Δt) |
| C₁ = (Kx+0.5Δt) / (K(1−x)+0.5Δt) |
| C₂ = (K(1−x)−0.5Δt) / (K(1−x)+0.5Δt) |
| Thiessen Weight | A_i / A_total |

### Groundwater
| Formula | Equation |
|:--------|:---------|
| Darcy's Law | Q = K × A × (dh/dl) |
| Transmissivity | T = K × b |
| Storage Coefficient | S = S_s × b (confined) |
| Theis Equation | s = (Q/4πT) × W(u) |

### Sediment Transport
| Formula | Equation |
|:--------|:---------|
| Shields Parameter | τ* = τ / ((ρ_s − ρ)gd) |
| HEC-RAS | Standard step method for GVF |
| Meyer-Peter & Müller | q_b ∝ (τ* − τ*_c)^1.5 |

---

## Key Dimensionless Numbers

| Number | Formula | Value/Range | Significance |
|:-------|:--------|:------------|:-------------|
| Reynolds (pipe) | Re = VD/ν | <2300 laminar, >4000 turbulent | Flow regime |
| Froude | Fr = V/√(gy) | <1 subcritical, >1 supercritical | Flow classification |
| Manning's n | Roughness | 0.012–0.050 | Channel resistance |
| Chezy C | C = R^(1/6)/n | 30–100 | Channel conveyance |

---

## Key Values to Memorize

### Water Properties
| Property | Value |
|:---------|:------|
| Density of water | 1000 kg/m³ |
| Specific weight (γ) | 9810 N/m³ |
| Kinematic viscosity (ν) at 20°C | 1.0 × 10⁻⁶ m²/s |
| Dynamic viscosity (μ) at 20°C | 1.0 × 10⁻³ Pa·s |

### Manning's n (Typical)
| Channel Type | n |
|:-------------|:--|
| Clean, straight natural channel | 0.025–0.033 |
| Gravel bed, straight | 0.030–0.040 |
| Earth, straight, clean | 0.017–0.025 |
| Concrete, trowel finish | 0.011–0.013 |
| Earth, natural, minor streams | 0.025–0.050 |

### Typical Values
| Parameter | Typical Range |
|:----------|:-------------|
| Porosity (sands) | 0.25–0.50 |
| Permeability (sands) | 10⁻⁵ to 10⁻³ m/s |
| Infiltration rate (grass) | 5–25 mm/hr |
| Runoff coefficient (urban) | 0.70–0.95 |
| Runoff coefficient (forest) | 0.10–0.30 |

---

## Classification Quick Reference

### Flow Classification
| Criterion | Subcritical | Critical | Supercritical |
|:----------|:------------|:---------|:--------------|
| Froude number | Fr < 1 | Fr = 1 | Fr > 1 |
| Depth | y > y_c | y = y_c | y < y_c |
| Velocity | Low | Critical | High |
| Control | Downstream | — | Upstream |

### GVF Profiles (Mild Slope)
| Profile | Condition | Description |
|:--------|:----------|:------------|
| M1 | y > y_c > y_n | Backwater (dam) |
| M2 | y_c > y > y_n | Drawdown (weir) |
| M3 | y_n > y > 0 | Hydraulic jump |

### GVF Profiles (Steep Slope)
| Profile | Condition | Description |
|:--------|:----------|:------------|
| S1 | y > y_c > y_n | Dam on steep slope |
| S2 | y_c > y > y_n | Drawdown |
| S3 | y_n > y > 0 | Chute flow |

---

## Last-Minute Checklist

- [ ] Reviewed Manning's equation and solved 1 problem
- [ ] Reviewed Bernoulli's equation with losses
- [ ] Reviewed hydraulic jump equations
- [ ] Reviewed UH concept and Muskingum routing
- [ ] Reviewed Darcy's law and well hydraulics
- [ ] Reviewed Froude number classification
- [ ] Prepared 3-minute thesis pitch
- [ ] Reviewed 5 key formulas from each subject
- [ ] Researched [company] recent water projects

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| Full Study Plan | [role-study-plan.md](role-study-plan.md) |
| Hydraulics | [hydraulics/hydraulics.md](hydraulics/hydraulics.md) |
| Open Channel Flow | [open_channel_flow/open-channel-flow.md](open_channel_flow/open-channel-flow.md) |
| Hydrology | [hydrology/hydrology.md](hydrology/hydrology.md) |
| Water Resources | [water_resources/water-resources-engineering.md](water_resources/water-resources-engineering.md) |
| Technical Interview Bank | [../../prep/interview/technical/technical-interview-bank.md](../../prep/interview/technical/technical-interview-bank.md) |

---

*Print this sheet 1 hour before your HWRE interview.*
