# Structural Analysis — Rapid Revision Sheet

> Last-minute revision for structural analysis interviews. Core formulas, key concepts, and quick values in 15 minutes.

---

## Essential Formulas

| Formula | Equation | Use |
|:--------|:---------|:----|
| Static indeterminacy (plane truss) | $D_s = (m + R) - 2j$ | Determinacy |
| Static indeterminacy (rigid frame) | $D_s = (3m + R) - 3j$ | Determinacy |
| Kinematic indeterminacy | $D_k = NJ - C$ | DOF |
| Fixed-end moment (UDL) | $FEM = wL^2/12$ | Moment distribution |
| Fixed-end moment (central point) | $FEM = PL/8$ | Moment distribution |
| Stiffness (fixed far end) | $S = 4EI/L$ | Moment distribution |
| Stiffness (hinged far end) | $S = 3EI/L$ | Moment distribution |
| Distribution factor | $DF = K/\sum K$ | Moment distribution |
| Slope-deflection | $M_{AB} = M^F_{AB} + \frac{2EI}{L}(2\theta_A + \theta_B - 3\Delta/L)$ | Frame analysis |
| Stiffness method | $[K][D] = [P]$ | Matrix analysis |
| Shape factor | $SF = Z_p/Z_e$ | Plastic analysis |
| Plastic hinges for collapse | $N = D_s + 1$ | Plastic analysis |
| Arch thrust (3-hinged, UDL) | $H = wl^2/8h$ | Arch analysis |
| ILD value | $\sum(P \times \text{ord}) + \sum(w \times \text{area})$ | Influence lines |

---

## Key Values

| Parameter | Value |
|:----------|:------|
| Carry-over factor (fixed far end) | +1/2 |
| Carry-over factor (hinged far end) | 0 |
| Carry-over factor (cantilever) | -1 |
| Shape factor — rectangle | 1.5 |
| Shape factor — circle | 1.7 |
| Shape factor — I-section | 1.14 |
| Shape factor — diamond | 2.0 |
| Shape factor — triangle | 2.34 |
| Load factor — rectangle | 2.26 |
| Load factor — I-section | 1.70 |
| $D_s$ — 3-hinged arch | 0 |
| $D_s$ — 2-hinged arch | 1 |
| $D_s$ — fixed arch | 3 |
| Cable under UDL | Parabola |
| Cable under self-weight | Catenary |

---

## Support Reactions

| Support | Reactions |
|:--------|:----------|
| Free end | 0 |
| Roller | 1 |
| Hinged | 2 |
| Fixed | 3 |

---

## Collapse Mechanisms

| Mechanism | Description |
|:----------|:-------------|
| Beam | Simply supported, continuous, fixed beams |
| Sway | Frames (column top joints drift) |
| Joint | Where > 2 members meet |
| Gable | Gable frames (columns spread at top) |

---

## Plastic Analysis Theorems

| Theorem | Type | Condition | Result |
|:--------|:-----|:----------|:-------|
| Static | Lower bound | Equilibrium + Yield | $W \le W_u$ |
| Kinematic | Upper bound | Equilibrium + Mechanism | $W \ge W_u$ |

---

## Last-Minute Checklist

- [ ] Reviewed determinacy ($D_s$, $D_k$)
- [ ] Reviewed moment distribution (Hardy Cross)
- [ ] Reviewed influence lines (Müller-Breslau)
- [ ] Reviewed slope-deflection method
- [ ] Reviewed plastic analysis (shape factor, collapse)
- [ ] Reviewed arches and cables
- [ ] Reviewed stiffness method ($[K][D] = [P]$)

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| Full Study | [`structural-analysis.md`](structural-analysis.md) |
| Practice | [`PRACTICE.md`](PRACTICE.md) |
| Topic Test | [`TEST.md`](TEST.md) |
| Interview | [`INTERVIEW.md`](INTERVIEW.md) |
| RCC Design | [`../rcc/rcc-design.md`](../rcc/rcc-design.md) |
| Steel Design | [`../steel/steel-design.md`](../steel/steel-design.md) |

---

*Print this sheet 1 hour before your structural analysis interview.*