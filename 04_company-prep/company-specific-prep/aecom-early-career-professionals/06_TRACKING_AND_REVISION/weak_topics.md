# Weak Topics & Error Analysis Log
**Target Role:** Early Career Professionals (ECP) — Infrastructure / Water Resources Engineering  
**Company:** AECOM India (Bengaluru & Gurugram)  
**Standard:** Root-Cause Error Remediation Framework  

---

## 1. Error Taxonomy & Classification Framework

Every incorrect answer or skipped question during mock practice stems from one of four root causes. Log each mistake under its exact category:

```
                               ROOT CAUSE TAXONOMY
                                       │
        ┌───────────────────┬──────────┴─────────┬───────────────────┐
        ▼                   ▼                    ▼                   ▼
    TYPE A:             TYPE B:              TYPE C:             TYPE D:
FORMULA RECALL SLIP   ARITHMETIC SLIP     CONCEPT GAP        CODE UNAWARENESS
Forgotten constant,   Sign error, unit    Physical flaw in   Unknown IS / IRC /
exponent, or factor   conversion error    mechanics logic    Eurocode clause
```

- **Type A (Formula Recall Slip):** You understood the concept, but forgot a specific coefficient (e.g., forgetting the $1.76$ in $f = 1.76\sqrt{d_{50}}$ or the $1.5$ in $E_{\min} = 1.5 y_c$).
- **Type B (Arithmetic & Unit Conversion Slip):** You used the correct formula, but stumbled on units (e.g., using area in $\text{km}^2$ instead of hectares in the Rational formula, or forgetting to convert minutes to seconds in Joukowsky reflection time).
- **Type C (Conceptual Gap):** You fundamentally misunderstood the physical phenomenon (e.g., confusing Inlet Control with Outlet Control in culverts, or applying Kinematic Wave when backwater effects dominated).
- **Type D (Code & Standard Unawareness):** You did not know the codified threshold or limit state mandate (e.g., crack width limits under IS 3370 or Lacey pier shape factor under IRC:78).

---

## 2. Active Error Remediation Journal

Log every mock test mistake in this tracking table and review it 24 hours prior to your placement test.

| # | Test & Q# | Topic Domain | Root Cause Type | Description of Error Committed | Correct Physical Principle / Formula | Action Taken & File Reference |
|---|---|---|---|---|---|---|
| 1 | Diag Q2 | Speed & Distance | Type B | Used arithmetic mean instead of harmonic mean for round-trip speed. | Average speed over equal distances is the harmonic mean: $\frac{2 v_1 v_2}{v_1 + v_2}$. | Reviewed `03_ASSESSMENT_PREPARATION/aptitude/quantitative_aptitude.md` Q2. |
| 2 | Diag Q5 | Mensuration | Type B | Multiplied diameter by width instead of subtracting inner circle from outer circle area. | Ring Area $= \pi(R_{\text{outer}}^2 - R_{\text{inner}}^2)$. | Practiced geometric cross-sections in `quantitative_aptitude.md` Q10. |
| 3 | Tech Q4 | Hydraulic Jump | Type A | Misremembered Belanger formula sign inside parentheses ($+1$ instead of $-1$). | $\frac{y_2}{y_1} = \frac{1}{2}\left(\sqrt{1 + 8Fr_1^2} - 1\right)$. | Wrote out derivation 3 times; see `05_INTERVIEW_PREPARATION/technical_interview.md`. |
| 4 | Tech Q5 | Water Hammer | Type C | Treated $1.8\text{ s}$ as slow closure because pipe was long. | Checked $T_r = \frac{2L}{a} = 2.4\text{ s}$. Since $t_c < T_r$, it is rapid closure $\implies \Delta H = a V_0 / g$. | Re-read Joukowsky surge notes in `02_TECHNICAL_PREPARATION/hydraulics_and_fluid_mechanics.md`. |
| 5 | Mock Q7 | Mixtures | Type B | Set denominator as $60$ instead of $(60 + x)$ when adding pure water. | Adding water increases total solution volume: $\frac{V_{\text{solute}}}{V_{\text{initial}} + V_{\text{added}}} = C_{\text{target}}$. | Re-solved alligation drill problems. |
| 6 | Mock Q19 | OCF Slopes | Type C | Confused steep slope ($S$) with adverse slope ($A$). | Steep slope has $y_n < y_c$ ($S_0 > S_c$); Adverse slope rises in direction of flow ($S_0 < 0$). | Reviewed GVF profiles table in `01_PREPARATION_ROADMAP/revision_checklist.md`. |
| 7 | Mock Q35 | Triaxial Tests | Type C | Assumed pore pressure increases effective stress. | $\sigma' = \sigma - u$. Positive pore pressure *decreases* effective stress, reducing shear resistance. | Reviewed Terzaghi effective stress derivation in `technical_interview.md`. |
| 8 | Mock Q44 | Lacey Regime | Type A | Used $P = 4.75 Q^{1/2}$ instead of $P = 4.83 \sqrt{Q}$ (minor code variation). | Lacey wetted perimeter is $P = 4.75\sqrt{Q}$ (metric base) or $4.83$ in some state manuals. | Coded reference checked against IRC:78. |

---

## 3. High-Frequency Trap Avoidance Checklist

Before entering your online assessment or technical interview, mentally review these top 10 classical pitfalls:

1. **Rational Formula Units:** In $Q = \frac{C I A}{360}$, $A$ must be in **hectares** and $I$ in **mm/hr** to output $\text{m}^3\text{/s}$. If $A$ is in $\text{km}^2$, divide by **3.6**.
2. **Belanger Sequent Depth:** Remember the minus sign outside the radical: $\frac{1}{2}(\sqrt{1 + 8Fr_1^2} \mathbf{- 1})$.
3. **Double Drainage vs Single Drainage in Consolidation:** For double drainage, drainage path $d = H / 2$. If bounded by rock on one side, $d = H$. Squaring $d$ in $t = \frac{T_v d^2}{c_v}$ means single drainage takes **4 times longer**!
4. **Water Hammer Closure Classification:** Never judge rapid vs slow closure based on time $t_c$ alone; always compute the reflection period $T_r = \frac{2L}{a}$. If $t_c < T_r$, it is rapid.
5. **Effective Stress with Water Table at Ground Surface:** Submerged unit weight is $\gamma_{\text{sub}} = \gamma_{\text{sat}} - \gamma_w \approx 20 - 9.81 \approx 10.2\text{ kN/m}^3$ (roughly half of total unit weight).
6. **Shields Parameter vs Critical Velocity:** Scour is governed by bed shear stress ($\tau_b$), not mean velocity alone. A deep slow river can scour more than a shallow fast flume.
7. **Pipes and Cisterns Negative Signs:** Emptying pipes have a **negative rate of work**.
8. **Relative Speed:** Traveling in the **same direction** $\implies$ subtract speeds ($v_1 - v_2$). Traveling in **opposite directions** $\implies$ add speeds ($v_1 + v_2$).
9. **IS 456 Maximum Concrete Strain:** Extreme bending compression fiber strain is **0.0035**; axial compression strain is **0.0020**.
10. **Lacey Regime Silt Factor:** $f = 1.76\sqrt{d_{50}}$ where $d_{50}$ is in **millimeters**, not meters!

---
*End of Weak Topics & Error Analysis Log.*
