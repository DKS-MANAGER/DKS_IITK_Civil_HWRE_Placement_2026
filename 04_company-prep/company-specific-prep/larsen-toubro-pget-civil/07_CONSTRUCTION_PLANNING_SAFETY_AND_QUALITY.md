# Module 07: Construction Planning, Site Safety & Quality Management

`[CORE TECHNICAL SYLLABUS — L&T CONSTRUCTION EPC PROJECT CONTROLS]`
`[KEY INDIAN CODES: IS 15883, IS 3764, IS 2750, IS 456 TABLE 11, ISO 9001/45001]`
`[CONTENT: CPM/PERT NETWORKS, FLOATS, CRASHING, HIRA SAFETY & QUALITY ASSURANCE]`

---

## 1. Executive Summary & Syllabus Overview

At L&T Construction, modern mega-projects operate under rigorous Project Management Controls (PMC), Environment Health & Safety (EHS), and Quality Assurance/Quality Control (QA/QC) regimes:
1. **Network Analysis & Critical Path Method (CPM):** Activity-on-Node (AON) and Activity-on-Arrow (AOA) logic, forward and backward pass, early/late event times, Total Float ($TF$), Free Float ($FF$), Independent Float ($IF$), and critical path identification.
2. **Project Crashing & Cost Optimization:** Normal vs crash durations, direct vs indirect costs, cost slope ($\text{Cost Slope} = \frac{\Delta C}{\Delta T}$), and optimum project duration.
3. **PERT (Program Evaluation and Review Technique):** 3-time estimates (optimistic $t_o$, most likely $t_m$, pessimistic $t_p$), expected time ($t_e$), variance ($\sigma^2$), standard normal deviate ($Z$), and probability of project completion by target date.
4. **Site Safety Management (EHS):** Hazard Identification and Risk Assessment (HIRA), Permit-to-Work (PTW) protocols (Hot Work, Confined Space, Height Work >1.8m, Deep Excavation), excavation shoring/benching per IS 3764, scaffolding safety per IS 2750 / IS 3696, and Zero Accident policy.
5. **Quality Assurance & Testing Frequencies:** Inspection & Test Plans (ITP), Non-Conformance Reports (NCR), concrete sampling frequencies per IS 456 Table 11, core cutting criteria, and ISO 9001 quality audit trails.

---

## 2. Construction Planning Calculations & Solved Problems

### Problem 7.01: CPM Network Analysis & Float Calculations
**Question:** A project network consists of activities A through G. Determine the Early Start (ES), Early Finish (EF), Late Start (LS), Late Finish (LF), Total Float ($TF$), Free Float ($FF$), and Independent Float ($IF$) for each activity, and identify the Critical Path.
* Activities and Durations:
  * A (1–2): 5 days
  * B (1–3): 4 days
  * C (2–4): 6 days
  * D (3–4): 7 days
  * E (2–5): 8 days
  * F (4–5): 4 days
  * G (5–6): 3 days

**Solution:**
1. Event Times (Forward Pass — Early Times):
   - $E_1 = 0$
   - $E_2 = E_1 + t_{12} = 0 + 5 = 5$
   - $E_3 = E_1 + t_{13} = 0 + 4 = 4$
   - $E_4 = \max(E_2 + t_{24}, \, E_3 + t_{34}) = \max(5 + 6, \, 4 + 7) = \max(11, 11) = 11$
   - $E_5 = \max(E_2 + t_{25}, \, E_4 + t_{45}) = \max(5 + 8, \, 11 + 4) = \max(13, 15) = 15$
   - $E_6 = E_5 + t_{56} = 15 + 3 = 18\text{ days}$ (Project Duration).
2. Event Times (Backward Pass — Late Times):
   - $L_6 = 18$
   - $L_5 = L_6 - t_{56} = 18 - 3 = 15$
   - $L_4 = L_5 - t_{45} = 15 - 4 = 11$
   - $L_3 = L_4 - t_{34} = 11 - 7 = 4$
   - $L_2 = \min(L_4 - t_{24}, \, L_5 - t_{25}) = \min(11 - 6, \, 15 - 8) = \min(5, 7) = 5$
   - $L_1 = \min(L_2 - t_{12}, \, L_3 - t_{13}) = \min(5 - 5, \, 4 - 4) = \min(0, 0) = 0$.
3. Float Calculations Table:
   * **Activity A (1–2):** $ES=0, EF=5, LS=0, LF=5 \implies TF = 5 - 0 - 5 = \mathbf{0}, FF = 5 - 0 - 5 = \mathbf{0}, IF = \mathbf{0}$.
   * **Activity B (1–3):** $ES=0, EF=4, LS=0, LF=4 \implies TF = 4 - 0 - 4 = \mathbf{0}, FF = 4 - 0 - 4 = \mathbf{0}, IF = \mathbf{0}$.
   * **Activity C (2–4):** $ES=5, EF=11, LS=5, LF=11 \implies TF = 11 - 5 - 6 = \mathbf{0}, FF = 11 - 5 - 6 = \mathbf{0}, IF = \mathbf{0}$.
   * **Activity D (3–4):** $ES=4, EF=11, LS=4, LF=11 \implies TF = 11 - 4 - 7 = \mathbf{0}, FF = 11 - 4 - 7 = \mathbf{0}, IF = \mathbf{0}$.
   * **Activity E (2–5):** $ES=5, EF=13, LS=7, LF=15 \implies TF = 15 - 5 - 8 = \mathbf{2}, FF = 15 - 5 - 8 = \mathbf{2}, IF = 15 - 5 - 8 = \mathbf{2}$.
   * **Activity F (4–5):** $ES=11, EF=15, LS=11, LF=15 \implies TF = 15 - 11 - 4 = \mathbf{0}, FF = 15 - 11 - 4 = \mathbf{0}, IF = \mathbf{0}$.
   * **Activity G (5–6):** $ES=15, EF=18, LS=15, LF=18 \implies TF = 18 - 15 - 3 = \mathbf{0}, FF = 18 - 15 - 3 = \mathbf{0}, IF = \mathbf{0}$.
4. Critical Paths: Two parallel critical paths exist:
   - **Path 1:** $1 \to 2 \to 4 \to 5 \to 6$ (A-C-F-G) $= 5 + 6 + 4 + 3 = \mathbf{18\text{ days}}$.
   - **Path 2:** $1 \to 3 \to 4 \to 5 \to 6$ (B-D-F-G) $= 4 + 7 + 4 + 3 = \mathbf{18\text{ days}}$.

### Problem 7.02: PERT Project Completion Probability
**Question:** The critical path of a water transmission project has three activities with $(t_o, t_m, t_p)$ in weeks:
- Activity A: $(4, 7, 10)$
- Activity B: $(8, 12, 16)$
- Activity C: $(6, 9, 18)$
Determine: (a) Expected project duration $T_e$, (b) Project standard deviation $\sigma_p$, and (c) Probability of completing the project within 30 weeks. ($Z = 0.816 \implies P \approx 79.3\%$).  
**Solution:**
1. Expected time ($t_e = \frac{t_o + 4 t_m + t_p}{6}$) and variance ($\sigma^2 = [ (t_p - t_o) / 6 ]^2$):
   - Activity A: $t_e = \frac{4 + 4(7) + 10}{6} = \frac{42}{6} = 7.0\text{ weeks}$; $\sigma_A^2 = \left(\frac{10 - 4}{6}\right)^2 = (1.0)^2 = 1.0$.
   - Activity B: $t_e = \frac{8 + 4(12) + 16}{6} = \frac{72}{6} = 12.0\text{ weeks}$; $\sigma_B^2 = \left(\frac{16 - 8}{6}\right)^2 = \left(\frac{8}{6}\right)^2 = 1.778$.
   - Activity C: $t_e = \frac{6 + 4(9) + 18}{6} = \frac{60}{6} = 10.0\text{ weeks}$; $\sigma_C^2 = \left(\frac{18 - 6}{6}\right)^2 = (2.0)^2 = 4.0$.
2. Expected total duration:
   $$T_e = 7.0 + 12.0 + 10.0 = \mathbf{29.0\text{ weeks}}$$
3. Total variance:
   $$\sigma_p^2 = \sum \sigma_i^2 = 1.0 + 1.778 + 4.0 = 6.778$$
   $$\sigma_p = \sqrt{6.778} = \mathbf{2.603\text{ weeks}}$$
4. Standard Normal Deviate for Target $T_s = 30\text{ weeks}$:
   $$Z = \frac{T_s - T_e}{\sigma_p} = \frac{30.0 - 29.0}{2.603} = \frac{1.0}{2.603} = \mathbf{+0.384}$$
5. Cumulative Normal Probability:
   $$P(Z \le 0.384) = 0.50 + 0.1495 = \mathbf{0.6495} \quad (\approx 65\%)$$

### Problem 7.03: Project Crashing & Cost Optimization
**Question:** Activity A has a normal duration of 10 days at a normal cost of ₹50,000, and a crash duration of 6 days at a crash cost of ₹82,000. Indirect cost is ₹5,000 per day. Calculate the cost slope, and explain whether crashing Activity A by 2 days is economically viable.  
**Solution:**
1. Cost slope calculation:
   $$\text{Cost Slope} = \frac{\text{Crash Cost} - \text{Normal Cost}}{\text{Normal Time} - \text{Crash Time}} = \frac{82,000 - 50,000}{10 - 6} = \frac{32,000}{4} = \mathbf{\text{INR } 8,000\text{ per day}}$$
2. Economic Viability Analysis:
   - Direct cost increase per day crashed: $+ \text{INR } 8,000$.
   - Indirect cost saving per day shortened: $- \text{INR } 5,000$.
   - Net cost impact: $+8,000 - 5,000 = +\text{INR } 3,000/\text{day}$.
   - Crashing Activity A increases total project cost by ₹3,000/day. It is economically justified **ONLY** if:
     - Activity A lies on the critical path, and
     - Contractual liquidated damages (penalty) for delay exceed ₹3,000/day, or a milestone completion bonus is unlocked.

---

## 3. Site Safety Management & QA/QC Protocols

### 3.1 Permit to Work (PTW) System Matrix

| Work Category | Trigger Condition | Safety Mandates & Checkpoints | Key Hazards |
| :--- | :--- | :--- | :--- |
| **Working at Height** | Fall risk $>1.8\text{ meters}$ | Full body harness with double lanyard attached to static lifeline, inspected scaffolding with green tag, toe boards. | Fall from height, dropped objects. |
| **Deep Excavation** | Trench depth $>1.5\text{ meters}$ | Shoring, strutting or $1:1$ benching per IS 3764, access ladder every $15\text{ m}$, gas testing for toxic fumes. | Soil cave-in, asphyxiation. |
| **Hot Work** | Welding, gas cutting, grinding | Fire extinguisher on stand, fire blanket, removal of flammables within $10\text{ m}$, 30-min fire watch. | Fire, flash burn, explosion. |
| **Confined Space** | TBM tunnel, sewer, closed tank | Multi-gas detector ($O_2, CO, H_2S, LEL$), forced mechanical ventilation, standby rescue buddy. | Oxygen deficiency, toxic gas. |
| **Heavy Lifting** | Tandem lift or load $>10\text{ tons}$ | Third-party certified rigging gears, approved lifting plan, outrigger mat verification, no workers under boom. | Crane toppling, rigging failure. |

### 3.2 Concrete QA/QC Sampling Frequencies (IS 456 Table 11)

| Quantity of Concrete in Pour | Number of Test Samples (3 Cubes each) |
| :--- | :--- |
| $1 - 5\text{ m}^3$ | 1 sample |
| $6 - 15\text{ m}^3$ | 2 samples |
| $16 - 30\text{ m}^3$ | 3 samples |
| $31 - 50\text{ m}^3$ | 4 samples |
| $51\text{ m}^3$ and above | 4 samples $+ 1$ additional sample for each additional $50\text{ m}^3$ or part thereof |

> **Acceptance Criteria (IS 456 Cl. 16.1):**
> 1. Mean strength of 4 non-overlapping consecutive test results $\ge f_{ck} + 0.825 \times \text{established standard deviation}$ (or $f_{ck} + 3\text{ N/mm}^2$, whichever is greater).
> 2. Any individual test result $\ge f_{ck} - 3\text{ N/mm}^2$.
