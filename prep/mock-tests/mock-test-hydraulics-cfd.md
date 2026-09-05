# Mock Test — Hydraulics / CFD Engineer

> **Timed test:** 60 minutes · 3 sections · 50 marks. Simulates a hydraulics/CFD technical round (NHPC, WAPCOS, research labs, AgniKul).

---

## Section A — Technical MCQ (10 × 2 = 20 marks) · 15 min

1. The Reynolds number is the ratio of:
   - (a) Inertia to viscous forces
   - (b) Inertia to gravity forces
   - (c) Pressure to inertia forces
   - (d) Viscous to surface tension

2. In turbulent flow, the friction factor for a smooth pipe at high Re follows:
   - (a) Blasius correlation
   - (b) f = 64/Re
   - (c) f = constant
   - (d) f = 1/Re

3. The k-ε turbulence model solves transport equations for:
   - (a) Turbulent kinetic energy and dissipation rate
   - (b) Velocity and pressure
   - (c) Temperature and concentration
   - (d) Vorticity and streamfunction

4. The Kolmogorov scale represents:
   - (a) The smallest eddy scale where dissipation occurs
   - (b) The largest eddy scale
   - (c) The integral length scale
   - (d) The mesh size

5. NPSH available must be:
   - (a) Greater than NPSH required
   - (b) Less than NPSH required
   - (c) Equal to NPSH required
   - (d) Independent of NPSH required

6. In LES, the subgrid-scale model accounts for:
   - (a) Eddies smaller than the grid
   - (b) All eddies
   - (c) Only mean flow
   - (d) Boundary layers only

7. The Moody diagram plots:
   - (a) Friction factor vs Reynolds number
   - (b) Velocity vs depth
   - (c) Pressure vs flow
   - (d) Head vs discharge

8. The -5/3 law describes:
   - (a) The inertial subrange of the energy spectrum
   - (b) The dissipation range
   - (c) The integral scale
   - (d) The Kolmogorov scale

9. Wall functions are used in CFD to:
   - (a) Model the near-wall region without resolving it
   - (b) Resolve the full boundary layer
   - (c) Remove the boundary layer
   - (d) Increase mesh density everywhere

10. The specific speed of a pump is used to:
    - (a) Select the pump type for a given duty
    - (b) Measure pump efficiency
    - (c) Calculate NPSH
    - (d) Determine pipe diameter

---

## Section B — Numerical (3 × 8 = 24 marks) · 30 min

**Q1.** Water flows in a pipe (D = 0.2 m, L = 100 m) at Q = 0.05 m³/s. Using f = 0.02, find the head loss and the Reynolds number (ν = 10⁻⁶ m²/s).

**Q2.** A pump delivers 0.1 m³/s against a head of 30 m at 1450 rpm. Using the affinity laws, find the new head and flow if the speed is increased to 1750 rpm.

**Q3.** For a hydraulic jump in a rectangular channel, the upstream Froude number is 4 and upstream depth is 0.5 m. Find the conjugate depth.

---

## Section C — Behavioral / HR (2 × 3 = 6 marks) · 15 min

1. "Describe a CFD simulation you ran and how you validated it." (STAR)
2. "Why hydraulics/CFD, and what software are you proficient in?" (Motivation)

---

## Answer Key

**Section A:** 1-a, 2-a, 3-a, 4-a, 5-a, 6-a, 7-a, 8-a, 9-a, 10-a

**Section B:**
- Q1: V = Q/A = 0.05/(π×0.2²/4) = 1.59 m/s. Re = VD/ν = 1.59×0.2/1e-6 = 3.18×10⁵. h_f = f(L/D)(V²/2g) = 0.02×(100/0.2)×(1.59²/19.62) = 1.29 m.
- Q2: Affinity: Q ∝ N, H ∝ N². Q₂ = 0.1×(1750/1450) = 0.121 m³/s. H₂ = 30×(1750/1450)² = 43.7 m.
- Q3: y₂/y₁ = ½[√(1+8Fr₁²)−1] = ½[√(1+8×16)−1] = ½[√129−1] = ½[11.36−1] = 5.18. y₂ = 0.5×5.18 = 2.59 m.

**Section C:** Assess STAR structure, validation rigor, software proficiency, motivation.

---

## Scorecard

| Section | Max | Your Score |
|:--------|:---:|:----------:|
| A — Technical MCQ | 20 | |
| B — Numerical | 24 | |
| C — Behavioral | 6 | |
| **Total** | **50** | |

**Rating:** 40+ Excellent · 30–39 Good · 20–29 Needs Work · <20 Revisit fundamentals

---

## Related

- [Role Study Plan](../../core/hwre/hydraulics/role-study-plan.md)
- [Hydraulics](../../core/hwre/hydraulics/hydraulics.md)
- [Turbulence Modeling](../../core/hwre/hydraulics/turbulence-modeling.md)
- [Mock Test Hub](README.md)
