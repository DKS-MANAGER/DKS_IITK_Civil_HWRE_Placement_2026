# Mock Test — Structural Engineer

> **Timed test:** 60 minutes · 3 sections · 50 marks. Simulates a core structural design technical round (L&T, Thornton Tomasetti, SPECTRUM, Hilti).

---

## Section A — Technical MCQ (10 × 2 = 20 marks) · 15 min

1. In limit state design, the partial safety factor for dead load (DL) in the ultimate limit state is:
   - (a) 1.0
   - (b) 1.5
   - (c) 1.2
   - (d) 2.0

2. The critical load for a column (Euler) is proportional to:
   - (a) 1/L²
   - (b) L²
   - (c) 1/L
   - (d) L

3. In a singly reinforced beam, the neutral axis depth at balanced section (IS 456, Fe415) is approximately:
   - (a) 0.48d
   - (b) 0.53d
   - (c) 0.36d
   - (d) 0.87d

4. The moment distribution method is best suited for:
   - (a) Indeterminate frames without sway
   - (b) Trusses
   - (c) Cables
   - (d) Plastic analysis

5. Development length in IS 456 depends on:
   - (a) Bond stress and bar diameter
   - (b) Only bar diameter
   - (c) Only concrete grade
   - (d) Span length

6. The shear strength of concrete (IS 456) increases with:
   - (a) Higher grade of concrete
   - (b) Higher steel percentage
   - (c) Both (a) and (b)
   - (d) Neither

7. A statically indeterminate structure has:
   - (a) More unknown reactions than equilibrium equations
   - (b) Fewer unknowns than equations
   - (c) No redundant reactions
   - (d) Only axial forces

8. The influence line for a reaction at a support is:
   - (a) A straight line
   - (b) A parabola
   - (c) A cubic
   - (d) A circle

9. In steel design (IS 800), the partial safety factor for material is:
   - (a) 1.1
   - (b) 1.5
   - (c) 1.25
   - (d) 2.0

10. The slenderness ratio of a column is:
    - (a) Effective length / least radius of gyration
    - (b) Radius of gyration / length
    - (c) Width / depth
    - (d) Height / width

---

## Section B — Numerical (3 × 8 = 24 marks) · 30 min

**Q1.** Design a singly reinforced rectangular beam (b = 300 mm, effective depth d = 500 mm) to resist a factored moment of 150 kN·m. Use M25 concrete and Fe415 steel. (Assume xu,max/d = 0.48.)

**Q2.** A column of effective length 3 m has a rectangular section 300 × 400 mm. Using Euler's formula with E = 200 GPa, estimate the critical buckling load about the weaker axis.

**Q3.** A simply supported beam of span 6 m carries a UDL of 20 kN/m (factored). Design the shear reinforcement using M25 concrete and Fe415 steel. (τc = 0.36 N/mm².)

---

## Section C — Behavioral / HR (2 × 3 = 6 marks) · 15 min

1. "Tell me about a structural design project where you had to balance safety and economy." (STAR)
2. "Why structural engineering, and how do you stay current with IS codes?" (Motivation)

---

## Answer Key

**Section A:** 1-b, 2-a, 3-a, 4-a, 5-a, 6-c, 7-a, 8-a, 9-a, 10-a

**Section B:**
- Q1: Mu = 0.87 fy Ast d (1 − Ast fy/(b d fck)). Try Ast = 900 mm² → Mu ≈ 0.87×415×900×500×(1 − 900×415/(300×500×25))×10⁻⁶ ≈ 150 kN·m. Provide 4-16mm (≈804) or 3-20mm (≈942) bars.
- Q2: I_min = bd³/12 = 300×400³/12 = 1.6×10⁹ mm⁴. P_cr = π²EI/L² = π²×200000×1.6e9/3000² = 3.51×10⁸ N ≈ 351 MN.
- Q3: Vu = wL/2 = 20×6/2 = 60 kN. τv = Vu/(bd) = 60000/(300×500) = 0.4 N/mm² > τc = 0.36. Vus = Vu − τc bd = 60 − 0.36×300×500/1000 = 6 kN. Provide nominal 2-legged 8mm @ 300 c/c.

**Section C:** Assess STAR structure, code awareness, safety-economy balance, quantified results.

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

- [Role Study Plan](../../core/structures/role-study-plan.md)
- [Structures](../../core/structures/structures.md)
- [RCC Design](../../core/rcc/rcc-design.md)
- [Mock Test Hub](README.md)
