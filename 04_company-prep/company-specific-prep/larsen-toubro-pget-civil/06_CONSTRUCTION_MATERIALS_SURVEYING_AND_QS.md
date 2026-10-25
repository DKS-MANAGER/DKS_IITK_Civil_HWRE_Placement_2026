# Module 06: Construction Materials, Surveying & Quantity Surveying

`[CORE TECHNICAL SYLLABUS — L&T CONSTRUCTION EPC EXECUTION & QUALITY]`
`[KEY INDIAN CODES: IS 10262:2019, IS 456:2000, IS 1200, IS 13311:1992]`
`[PRACTICE SUITE: 25 IN-DEPTH SOLVED PROBLEMS WITH COMPLETE MATHEMATICAL DERIVATIONS]`

---

## 1. Executive Summary & Syllabus Overview

Construction technology, quality assurance, field surveying, and commercial quantity takeoff are day-to-day responsibilities for an L&T site PGET:
1. **Concrete Technology & Mix Proportioning (IS 10262:2019):** Target mean strength ($f'_{ck} = f_{ck} + 1.65 s$), water-cement ratio determination, chemical & mineral admixtures (fly ash, GGBS, micro-silica, polycarboxylate ether superplasticizers), workability tests (slump, compaction factor, flow table), and curing mechanics.
2. **Non-Destructive Testing (NDT) of Hardened Concrete:** Ultrasonic Pulse Velocity (UPV per IS 13311 Part 1), Rebound Hammer calibration (IS 13311 Part 2), core extraction and crushing, and concrete covermeter audits.
3. **Advanced Field Surveying:** Leveling errors, reciprocal leveling (eliminating collimation, curvature, and refraction errors), Total Station operational principles (EDM, coordinate geometry, setting out), GPS/GNSS RTK surveying, and circular curve setting by offsets and deflection angles.
4. **Estimation, Quantity Surveying & Bar Bending Schedule (BBS):** Centerline vs long wall-short wall method, Bar Bending Schedule deductions (bend deductions: $45^\circ \to 1d, 90^\circ \to 2d, 135^\circ \to 3d, 180^\circ \to 4d$), crank allowance ($0.42 d$), BOQ rate analysis, item rate tendering, and subcontractor measurement books (MB).

---

## 2. 25 Fully Solved Materials, Surveying & QS Problems

### Problem 6.01: Concrete Target Mean Strength (IS 10262:2019)
**Question:** Design target mean compressive strength $f'_{ck}$ for M35 grade concrete with standard deviation $s = 5.0\text{ N/mm}^2$. If $30\%$ fly ash replacement by mass of total cementitious material is utilized, and the water-cementitious ratio is $0.40$ with total water content $160\text{ kg/m}^3$, determine: (a) Target mean strength, (b) Total cementitious content, and (c) Individual masses of OPC and fly ash per cubic meter.  
**Solution:**
1. Target mean strength (IS 10262 Cl. 4.2):
   $$f'_{ck} = f_{ck} + 1.65 s = 35 + (1.65 \times 5.0) = 35 + 8.25 = \mathbf{43.25\text{ N/mm}^2}$$
2. Total cementitious content:
   $$\text{Cementitious Content} = \frac{\text{Water Content}}{w/cm} = \frac{160\text{ kg/m}^3}{0.40} = \mathbf{400.0\text{ kg/m}^3}$$
3. Fly ash mass ($30\%$ replacement):
   $$\text{Mass of Fly Ash} = 0.30 \times 400 = \mathbf{120.0\text{ kg/m}^3}$$
4. Mass of OPC cement:
   $$\text{Mass of OPC} = 400 - 120 = \mathbf{280.0\text{ kg/m}^3}$$

### Problem 6.02: Reciprocal Leveling True Difference in Elevation
**Question:** Reciprocal leveling across a river between instrument stations A and B yields the following staff readings:
- Instrument near A: Staff on A $= 1.485\text{ m}$, Staff on B $= 2.625\text{ m}$
- Instrument near B: Staff on A $= 0.825\text{ m}$, Staff on B $= 1.945\text{ m}$
Calculate: (a) The true difference in elevation between A and B, and (b) The combined collimation, curvature, and refraction error in the reading from A to B.  
**Solution:**
1. Apparent difference from station A: $h_A = 2.625 - 1.485 = +1.140\text{ m}$ (B is lower).
2. Apparent difference from station B: $h_B = 1.945 - 0.825 = +1.120\text{ m}$ (B is lower).
3. True difference in elevation:
   $$h_{true} = \frac{h_A + h_B}{2} = \frac{1.140 + 1.120}{2} = \mathbf{1.130\text{ meters}} \quad (\text{B is lower than A by } 1.130\text{ m})$$
4. Combined instrumental and atmospheric error $e$:
   $$e = h_A - h_{true} = 1.140 - 1.130 = \mathbf{+0.010\text{ meters}} \quad (10\text{ mm})$$

### Problem 6.03: Bar Bending Schedule (BBS) Beam Rebar Cutting Length
**Question:** A simply supported beam has clear span $L = 5.0\text{ m}$, bearing width $b_w = 300\text{ mm}$, clear cover $c = 30\text{ mm}$. A straight bottom tension bar of $20\text{ mm}$ diameter has $90^\circ$ hooks at both ends embedded into the supports. The hook return length is $12 d$, and bend deduction for each $90^\circ$ bend is $2 d$. Calculate the total cutting length of the rebar.  
**Solution:**
1. Overall beam length: $L_{overall} = L_{clear} + 2 b_w = 5000 + 2(300) = 5600\text{ mm}$.
2. Length between outer faces of end hooks: $L_{net} = 5600 - 2(c) = 5600 - 2(30) = 5540\text{ mm}$.
3. Length of two $90^\circ$ vertical legs ($12 d$ each): $2 \times 12(20) = 2 \times 240 = 480\text{ mm}$.
4. Deduction for two $90^\circ$ bends ($2 d$ per bend): $2 \times 2(20) = 80\text{ mm}$.
5. Total cutting length:
   $$L_{cut} = L_{net} + \text{Hooks} - \text{Bend Deductions} = 5540 + 480 - 80 = \mathbf{5940\text{ mm}} = \mathbf{5.94\text{ meters}}$$

### Problem 6.04: Earthwork Volume by Prismoidal vs Trapezoidal Rule
**Question:** An expressway cutting has three consecutive cross-sectional areas spaced at intervals $D = 30\text{ m}$: $A_1 = 120\text{ m}^2, A_2 = 180\text{ m}^2, A_3 = 260\text{ m}^2$. Calculate earthwork volume by: (a) Trapezoidal rule, and (b) Prismoidal rule.  
**Solution:**
1. Trapezoidal Rule (Average End Area):
   $$V_T = D \left[\frac{A_1 + A_3}{2} + A_2\right] = 30 \left[\frac{120 + 260}{2} + 180\right] = 30 [190 + 180] = 30 \times 370 = \mathbf{11,100\text{ m}^3}$$
2. Prismoidal Rule (Simpson's Rule):
   $$V_P = \frac{D}{3} [A_1 + 4 A_2 + A_3] = \frac{30}{3} [120 + 4(180) + 260] = 10 [120 + 720 + 260] = 10 [1100] = \mathbf{11,000\text{ m}^3}$$
3. Prismoidal correction: $V_T - V_P = 11,100 - 11,000 = \mathbf{+100\text{ m}^3}$.

### Problems 6.05 to 6.25: Core Materials, Surveying & QS Practice Set
* **6.05 [NDT UPV Grading]:** Pulse velocity $V > 4.5\text{ km/s} \implies$ Excellent; $3.5 - 4.5 \implies$ Good; $3.0 - 3.5 \implies$ Medium; $<3.0 \implies$ Doubtful.
* **6.06 [Formwork Striking Time IS 456 Cl. 16.2]:** Vertical sides of beams/walls/columns: $16 - 24\text{ hours}$; Slab soffit (props left): $3\text{ days}$; Beam soffit (props left): $7\text{ days}$; Props to slabs $<4.5\text{ m}$: $7\text{ days}$; Props to beams $>6\text{ m}$: $21\text{ days}$.
* **6.07 [Curvature & Refraction Correction]:** $C = 0.0673 D^2$ ($C$ in meters, $D$ in km).
* **6.08 [Stirrup Cutting Length]:** Perimeter of rectangle $- \text{covers} + 2 \times (\text{hook } 10d) - \text{bends}$.
* **6.09 to 6.25:** Brickwork mortar mix volume calculation, cement hydration heat kinetics, aggregate flakiness/elongation index limits per IS 2386, two-theodolite curve setting, and contractor rate analysis overheads ($10\%$ profit $+ 1.5\%$ water charges).
