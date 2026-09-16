# Data Interpretation: Radar & Stacked Area Graphs

> **Priority:** P2 · **Role relevance:** High (Power & Energy Infrastructure, Management Consulting, ESG Benchmarking, Product Analytics, Supply Chain & Quant Trading)  
> **Difficulty range:** Foundation → Multi-Axis Radial Geometry & Power Grid Merit-Order Dispatch · **Target speed:** 45–60 sec (Direct Spoke / Layer Read) – 110–160 sec (Radial Polygon Area / Stacked Dynamic Merit-Order Caselet)

---

## 1. Mathematical & Theoretical Framework

### 1.1 Radar (Spider / Kiviat) Geometry & Interpretation
A Radar chart projects $n$ quantitative variables onto equiangular radial spokes originating from a shared central origin ($O$).

```
+-----------------------------------------------------------------------------------+
|                        RADAR CHART GEOMETRIC PRINCIPLES                           |
+-----------------------------------------------------------------------------------+
| Metric / Feature       | Mathematical Formulation         | Analytical Caveat     |
|------------------------+----------------------------------+-----------------------|
| Central Angle          | \theta = 2\pi / n = 360^\circ / n| Uniform angular spacing|
| Spoke Coordinate       | (r_i \cos(i\theta), r_i \sin(i\theta)) | Radial distance r_i |
| Radial Polygon Area    | A = 0.5 \sin(\theta) \sum_{i=1}^n r_i r_{i+1} | Sequence-dependent!   |
| Metric Score Sum       | S = \sum_{i=1}^n r_i            | Order-invariant       |
| Euclidean Distance     | D = \sqrt{\sum_{i=1}^n (r_i - r_{\text{target}, i})^2} | Proximity to target   |
+-----------------------------------------------------------------------------------+
*(Note: In the polygon area formula, r_{n+1} \equiv r_1. The visual area is sensitive to the permutation of radial spokes, whereas the arithmetic sum of scores is invariant).*
```

---

### 1.2 Stacked Area & Cumulative Envelope Dynamics
Stacked area charts depict multi-variable time-series where each successive layer represents an additive component of the aggregate envelope:

$$\text{Cumulative Total at time } t: \quad Y(t) = \sum_{k=1}^m y_k(t)$$

$$\text{Marginal Value of Layer } k: \quad y_k(t) = S_k(t) - S_{k-1}(t)$$

Where $S_k(t)$ is the top boundary coordinate of layer $k$, and $S_0(t) \equiv 0$.

```
+-----------------------------------------------------------------------------------+
|                     STACKED AREA DYNAMICS & OPTICAL PITFALLS                      |
+-----------------------------------------------------------------------------------+
| Pitfall / Feature      | Mathematical Cause               | Correct Analytical Fix|
|------------------------+----------------------------------+-----------------------|
| Baseline Illusion      | Layer k's lower edge is S_{k-1}(t),| Measure vertical distance|
|                        | which fluctuates with prior layers| S_k(t) - S_{k-1}(t), not |
|                        |                                  | distance from zero!   |
| 100% Stacked Share     | w_k(t) = y_k(t) / Y(t)          | Expanding share can   |
|                        |                                  | accompany falling abs!|
| Negative Displacements | Stacked areas cannot handle y_k < 0| Switch to net bar or  |
|                        | without overlapping visual chaos | multi-line chart      |
+-----------------------------------------------------------------------------------+
```

---

## 2. Master Answer Key (Q1–Q40)

| Question | Level | Archetype / Domain | Correct Answer | Core Mathematical Principle |
|:---:|:---:|:---|:---:|:---|
| **Q1** | Level 1 | Radar Spoke Value Read | **C** | Direct radial coordinate read on Spoke 4 ($75.0$) |
| **Q2** | Level 1 | Radar Deficit Identification | **B** | Target ($80$) minus actual ($60$) $= 20\text{ points}$ |
| **Q3** | Level 1 | Stacked Area Total Read | **A** | Total aggregate envelope height $= 450\text{ MW}$ |
| **Q4** | Level 1 | Stacked Layer Subtraction | **D** | Layer thickness $= 320 - 180 = 140\text{ MW}$ |
| **Q5** | Level 1 | 100% Stacked Proportions | **B** | Relative percentage share $= (140 / 450) \times 100\% = 31.11\%$ |
| **Q6** | Level 2 | Aggregate Radar Score | **C** | $\sum_{i=1}^5 r_i = 70 + 85 + 60 + 75 + 90 = 380$ |
| **Q7** | Level 2 | Weighted Radar Composite | **B** | $\sum (w_i r_i) = 0.3(70) + 0.25(85) + 0.2(60) + 0.15(75) + 0.1(90) = 74.5$ |
| **Q8** | Level 2 | Marginal Layer Expansion | **A** | Layer expands from $140$ to $186.67 \implies +33.33\%$ |
| **Q9** | Level 2 | Cross-Layer Peak Identification | **C** | New aggregate envelope height $= 180 + 190 + 80 = 450\text{ MW}$ |
| **Q10** | Level 2 | Multi-Category Stacked Sum | **D** | Sum of bottom two layers $= 180 + 140 = 320\text{ MW}$ |
| **Q11** | Level 3 | Radar Euclidean Discrepancy | **B** | $\sqrt{\sum (r_i - 100)^2} = \sqrt{900 + 225 + 1600 + 625 + 100} = 58.74$ |
| **Q12** | Level 3 | Rate of Band Thickness Shift | **C** | $\Delta y / \Delta t = (150 - 100) / 4 = 12.5\text{ MW/hr}$ |
| **Q13** | Level 3 | Share Compression Paradox | **A** | Layer volume grows $+20\%$ but total grows $+50\% \implies$ share shrinks from $25\%$ to $20\%$ |
| **Q14** | Level 3 | Radar Variance / Uniformity | **D** | Population standard deviation of radial spoke values $= 10.68$ |
| **Q15** | Level 3 | Stacked Area Integral (MWh) | **B** | Trapezoidal integration under layer $= 1,440\text{ MWh}$ |
| **Q16** | Level 4 | Pentagonal Radar Area | **C** | $A = \frac{1}{2} \sin(72^\circ) \sum r_i r_{i+1} = 0.475528 \times 28,600 \approx 13,600.1$ |
| **Q17** | Level 4 | Merit-Order Base vs Peak | **A** | Baseload runs continuously; peaker gas turbines absorb volatile peak swing |
| **Q18** | Level 4 | Stacked Layer Cannibalization | **D** | Solar surge depresses net thermal generation from $400$ to $120\text{ MW}$ (drop of $280\text{ MW}$) |
| **Q19** | Level 4 | Multi-Entity Radar Dominance | **B** | Hub A strictly outperforms Hub B on 3 out of 5 axes |
| **Q20** | Level 4 | Ramp Rate Constraint in Area | **C** | Maximum steepness slope $= (590 - 500) / 2 = 45.0\text{ MW/hr}$ |
| **Q21** | Level 5 | 6-Axis Hexagonal Kiviat Area | **B** | $A = \frac{\sqrt{3}}{4} \sum r_i r_{i+1} = 0.4330127 \times 35,100 \approx 15,198.7$ |
| **Q22** | Level 5 | Duck Curve Net Load Peak | **A** | Evening ramp rate $= (420 - 150) / 3 = 90.0\text{ MW/hr}$ |
| **Q23** | Level 5 | Capacity Factor from Area | **C** | $\text{CF} = 7,800\text{ MWh} / (500\text{ MW} \times 24\text{ hr}) = 65.0\%$ |
| **Q24** | Level 5 | Radar Iso-Performance Curve | **D** | Trade-off: $+15$ pts on Speed and $-10$ pts on Cost yields $+5$ net points |
| **Q25** | Level 5 | Curtailment Energy Volume | **B** | Excess generation above transmission + storage cap $= 100\text{ MW} \times 4\text{ hr} = 400\text{ MWh}$ |
| **Q26** | Level 6 | Radar Axis Order Sensitivity | **C** | Permuting adjacent spokes inflates enclosed area purely due to spoke re-ordering |
| **Q27** | Level 6 | 7-Axis Defense Capability | **A** | Penalized composite score sum $= 560.0 - 20.0 = 540.0$ |
| **Q28** | Level 6 | Dual-Axis Stacked Dynamic | **C** | Annual spend rate of CapEx alone $= 120t - 50t = 70\text{ crore/year}$ |
| **Q29** | Level 6 | Dynamic Merit Dispatch Optimization | **B** | Effective marginal costs under carbon tax: Coal $= \text{₹}4.30$, Gas $= \text{₹}5.30$ |
| **Q30** | Level 6 | Multi-Spectral Sensor Kiviat | **C** | Maximum flawless hexagonal area $= 15,000 \times \sqrt{3} \approx 25,980.8$ |
| **Q31** | Level 7 | Spoke Order Optical Illusion | **B** | Rearranging adjacent spokes inflates perceived polygon area by maximizing cross-products |
| **Q32** | Level 7 | Wavy Baseline Misattribution | **C** | Middle layer's apparent plunge is an optical artifact caused by base layer's collapse |
| **Q33** | Level 7 | Non-Linear Radial Scale Trap | **A** | Visual area scales quadratically ($r^2$), making a $2\times$ score look $4\times$ larger |
| **Q34** | Level 7 | 100% Stacked Inflation Trap | **A** | Total market volume contracted from $100,000$ to $30,000$ units, shrinking absolute sales |
| **Q35** | Level 7 | Equal-Spoke Weighting Bias | **B** | Conjunctive constraint: single-source raw material failure halts $100\%$ of production |
| **Q36** | Level 8 | Clean Energy Generation Share | **C** | Total clean energy $= 2,800 / 4,500 \approx 62.22\%$ of 2030 generation |
| **Q37** | Level 8 | BESS Storage Round-Trip Loss | **B** | Energy consumed in charging ($500\text{ GWh}$) minus discharge ($400\text{ GWh}$) $= 100\text{ GWh}$ |
| **Q38** | Level 8 | Grid Carbon Intensity Abatement | **A** | Emissions decline from $2,205,000\text{ t}$ to $985,000\text{ t} (-55.33\%)$ |
| **Q39** | Level 8 | Grid Reliability Radar Index | **C** | 5-axis resilience index achieves equal-weighted score of $80.0$ |
| **Q40** | Level 8 | Levelized Cost & Curtailment | **B** | $200\text{ GWh}$ curtailed renewable power costs $\text{₹}36\text{ crore}$ at $\text{₹}1.80/\text{kWh}$ |

---

## 3. Comprehensive Practice Set (40 Placement Questions)

### Level 1: Foundation (Q1–Q5)

**Dataset Reference (Corporate Operations Radar & Hourly Plant Dispatch):**  
A technology firm evaluates its regional delivery hubs across 5 operational dimensions on a 0–100 scale:
- **Spoke 1 (Delivery Speed):** Hub A = $70$, Hub B = $65$, Target = $85$
- **Spoke 2 (Order Accuracy):** Hub A = $85$, Hub B = $80$, Target = $95$
- **Spoke 3 (Fleet Fuel Efficiency):** Hub A = $60$, Hub B = $70$, Target = $80$
- **Spoke 4 (Customer Satisfaction):** Hub A = $75$, Hub B = $80$, Target = $90$
- **Spoke 5 (Cost Efficiency):** Hub A = $90$, Hub B = $60$, Target = $85$

Simultaneously, an industrial captive power plant monitors its power generation stack at 12:00 PM:
- Layer 1 (Baseload Biomass): Top boundary = $180\text{ MW}$ (Origin = $0\text{ MW}$)
- Layer 2 (Waste Heat Recovery): Top boundary = $320\text{ MW}$
- Layer 3 (Grid Import): Top boundary = $450\text{ MW}$

#### Q1
On Spoke 4 (Customer Satisfaction), what is the exact rating achieved by Hub A?
- (A) $65.0$
- (B) $70.0$
- (C) $75.0$
- (D) $80.0$

#### Q2
On Spoke 3 (Fleet Fuel Efficiency), what is the deficit between Hub A's actual performance and the company target?
- (A) $10.0\text{ points}$
- (B) $20.0\text{ points}$
- (C) $25.0\text{ points}$
- (D) $30.0\text{ points}$

#### Q3
At 12:00 PM, what is the total aggregate power output generated across all three layers of the captive power plant?
- (A) $450\text{ MW}$
- (B) $500\text{ MW}$
- (C) $950\text{ MW}$
- (D) $320\text{ MW}$

#### Q4
What is the individual power generation contributed specifically by Layer 2 (Waste Heat Recovery)?
- (A) $320\text{ MW}$
- (B) $180\text{ MW}$
- (C) $160\text{ MW}$
- (D) $140\text{ MW}$

#### Q5
In a 100% stacked area visualization of the 12:00 PM generation mix, what percentage share does Layer 2 (Waste Heat Recovery) represent of total plant power?
- (A) $28.50\%$
- (B) $31.11\%$
- (C) $35.00\%$
- (D) $40.00\%$

---

### Level 2: Intermediate (Q6–Q10)

#### Q6
What is the unweighted arithmetic sum of Hub A's ratings across all 5 operational spokes?
- (A) $360.0$
- (B) $370.0$
- (C) $380.0$
- (D) $385.0$

#### Q7
Management implements a weighted operational composite score: Speed ($30\%$), Accuracy ($25\%$), Fuel Efficiency ($20\%$), Customer Satisfaction ($15\%$), and Cost Efficiency ($10\%$). What is Hub A's weighted composite score?
- (A) $72.25$
- (B) $74.50$
- (C) $76.00$
- (D) $78.20$

#### Q8
Between 12:00 PM and 4:00 PM, Layer 2 generation expands from $140\text{ MW}$ to $186.67\text{ MW}$. What is the relative percentage expansion of Layer 2's output?
- (A) $33.33\%$
- (B) $30.00\%$
- (C) $25.00\%$
- (D) $20.00\%$

#### Q9
If Layer 1 output remains flat at $180\text{ MW}$, Layer 2 increases to $190\text{ MW}$, and Layer 3 (Grid Import) drops to $80\text{ MW}$ at 6:00 PM, what is the new total envelope height at 6:00 PM?
- (A) $420\text{ MW}$
- (B) $435\text{ MW}$
- (C) $450\text{ MW}$
- (D) $460\text{ MW}$

#### Q10
What is the combined power contributed by the internally generated sources (Layer 1 + Layer 2) at 12:00 PM?
- (A) $280\text{ MW}$
- (B) $300\text{ MW}$
- (C) $310\text{ MW}$
- (D) $320\text{ MW}$

---

### Level 3: Hard (Q11–Q15)

#### Q11
A benchmark perfection profile has a score of $100$ on all 5 spokes. What is the Euclidean distance in 5-dimensional metric space between Hub A's performance vector $(70, 85, 60, 75, 90)$ and the perfection vector $(100, 100, 100, 100, 100)$?
- (A) $48.20$
- (B) $58.74$
- (C) $62.45$
- (D) $68.10$

#### Q12
From $t = 8:00\text{ AM}$ (thickness = $100\text{ MW}$) to $t = 12:00\text{ PM}$ (thickness = $150\text{ MW}$), Layer 2 experiences linear capacity ramping. What is its linear ramp rate per hour?
- (A) $10.0\text{ MW/hr}$
- (B) $11.5\text{ MW/hr}$
- (C) $12.5\text{ MW/hr}$
- (D) $15.0\text{ MW/hr}$

#### Q13
Between 2021 and 2024, a corporate SaaS division's annual revenue grew from $100\text{ M USD}$ to $120\text{ M USD}$ ($+20\%$). In the same period, total conglomerate revenue expanded from $400\text{ M USD}$ to $600\text{ M USD}$ ($+50\%$). What happened to the SaaS division's share in the conglomerate's 100% stacked area chart?
- (A) Its share compressed from $25.0\%$ to $20.0\%$ ($-5.0\text{ percentage points}$) despite growing in absolute terms
- (B) Its share expanded from $20.0\%$ to $25.0\%$
- (C) Its share remained unchanged at $25.0\%$
- (D) Its share compressed by $10.0\text{ percentage points}$

#### Q14
What is the population standard deviation ($\sigma$) of Hub A's 5 radial spoke scores $(70, 85, 60, 75, 90)$?
- (A) $8.45$
- (B) $9.82$
- (C) $10.25$
- (D) $10.68$

#### Q15
If Layer 1 (Baseload Biomass) generates a constant $180\text{ MW}$ continuously for an 8-hour shift, what is the total cumulative electrical energy produced by this layer?
- (A) $1,280\text{ MWh}$
- (B) $1,440\text{ MWh}$
- (C) $1,600\text{ MWh}$
- (D) $1,800\text{ MWh}$

---

### Level 4: Very Hard (Q16–Q20)

**Dataset Reference (Regular Pentagonal Radar Geometry & Solar-Thermal Dispatch):**  
A 5-axis radar chart has spokes spaced equiangularly at $\theta = 72^\circ$ ($2\pi / 5\text{ radians}$). The radial ratings of Enterprise X in sequence along the perimeter are:
$$r_1 = 70, \quad r_2 = 85, \quad r_3 = 60, \quad r_4 = 75, \quad r_5 = 90$$
*(Recall: Area $= \frac{1}{2} \sin(72^\circ) [r_1 r_2 + r_2 r_3 + r_3 r_4 + r_4 r_5 + r_5 r_1]$, with $\sin(72^\circ) \approx 0.9510565$).*

#### Q16
What is the geometric polygon surface area enclosed by Enterprise X's profile on this 5-axis radar chart?
- (A) $12,450.5\text{ sq units}$
- (B) $13,120.0\text{ sq units}$
- (C) $13,600.1\text{ sq units}$
- (D) $14,250.8\text{ sq units}$

#### Q17
In an electric utility's stacked area dispatch curve, Baseload Nuclear forms Layer 1 ($0$ to $400\text{ MW}$), Combined Cycle Gas Turbines (CCGT) form Layer 2 ($400$ to $750\text{ MW}$), and Open Cycle Peakers form Layer 3 ($750$ to $950\text{ MW}$). Why are peakers placed at the very top of the stack?
- (A) Peakers have the highest marginal fuel operating cost, so they are dispatched last and fluctuate most with peak demand
- (B) Peakers cannot operate at high temperatures
- (C) Nuclear reactors cannot ramp down at night
- (D) Peakers produce zero carbon emissions

#### Q18
During a solar noon surge, solar generation expands from $0\text{ MW}$ to $280\text{ MW}$ in Layer 2, while total system load remains fixed at $600\text{ MW}$. If nuclear baseload in Layer 1 is inflexible at $200\text{ MW}$, by how much must thermal generation in Layer 3 contract?
- (A) From $400\text{ MW}$ to $220\text{ MW}$ (contract by $180\text{ MW}$)
- (B) From $400\text{ MW}$ to $180\text{ MW}$ (contract by $220\text{ MW}$)
- (C) From $400\text{ MW}$ to $150\text{ MW}$ (contract by $250\text{ MW}$)
- (D) From $400\text{ MW}$ to $120\text{ MW}$ (contract by $280\text{ MW}$)

#### Q19
Hub A has radial vector $(70, 85, 60, 75, 90)$ and Hub B has radial vector $(65, 80, 70, 80, 60)$. Across how many of the 5 operational spokes does Hub A strictly outperform Hub B?
- (A) 2 axes
- (B) 3 axes
- (C) 4 axes
- (D) 5 axes

#### Q20
Between 5:00 PM (load = $500\text{ MW}$) and 7:00 PM (load = $590\text{ MW}$), total electricity demand surges steeply. What is the required system-wide average hourly ramping rate?
- (A) $35.0\text{ MW/hr}$
- (B) $40.0\text{ MW/hr}$
- (C) $45.0\text{ MW/hr}$
- (D) $50.0\text{ MW/hr}$

---

### Level 5: Expert (Q21–Q25)

**Dataset Reference (6-Axis Hexagonal Kiviat Diagram):**  
A financial institution benchmarks two quantitative trading algorithms on a 6-axis Kiviat diagram with equiangular spacing $\theta = 60^\circ$ ($\sin 60^\circ = \frac{\sqrt{3}}{2} \approx 0.866025$):
- Spoke 1 (Sharpe Ratio): Algo Alpha = $90$, Algo Beta = $70$
- Spoke 2 (Sortino Ratio): Algo Alpha = $85$, Algo Beta = $80$
- Spoke 3 (Max Drawdown Defense): Algo Alpha = $60$, Algo Beta = $95$
- Spoke 4 (Execution Latency): Algo Alpha = $80$, Algo Beta = $65$
- Spoke 5 (Hit Rate %): Algo Alpha = $75$, Algo Beta = $70$
- Spoke 6 (Capacity Scalability): Algo Alpha = $70$, Algo Beta = $85$

*(Formula: Hexagonal Area $= \frac{\sqrt{3}}{4} [r_1 r_2 + r_2 r_3 + r_3 r_4 + r_4 r_5 + r_5 r_6 + r_6 r_1]$).*

#### Q21
What is the exact polygon surface area enclosed by Algo Alpha on this 6-axis Kiviat chart?
- (A) $14,419.3\text{ sq units}$
- (B) $15,198.7\text{ sq units}$
- (C) $15,820.0\text{ sq units}$
- (D) $16,245.8\text{ sq units}$

#### Q22
In the "Duck Curve" power phenomenon, solar generation collapses rapidly between 4:00 PM and 7:00 PM while residential lighting and cooling demand surges. If net thermal dispatch must ramp from $150\text{ MW}$ at 4:00 PM to $420\text{ MW}$ at 7:00 PM, what is the required thermal ramp rate?
- (A) $90.0\text{ MW/hr}$
- (B) $85.0\text{ MW/hr}$
- (C) $80.0\text{ MW/hr}$
- (D) $75.0\text{ MW/hr}$

#### Q23
A $500\text{ MW}$ rated gas plant delivers power represented by a trapezoidal stacked area profile over a 24-hour day: $200\text{ MW}$ from 00:00 to 08:00 (8 hrs), ramping linearly to $450\text{ MW}$ at 16:00 (8 hrs), and running flat at $450\text{ MW}$ until 24:00 (8 hrs). What is the plant's 24-hour Capacity Factor?
- (A) $60.00\%$
- (B) $62.50\%$
- (C) $65.00\%$
- (D) $68.75\%$

#### Q24
On a radar chart with equal spoke weights, if an analyst establishes an iso-performance indifference threshold where $S = \sum_{i=1}^n r_i = 400$, and an engineering team improves Speed by $+15$ points while degrading Cost Efficiency by $-10$ points, how does the net score change?
- (A) Net score degrades by $-5$ points
- (B) Net score remains invariant
- (C) Net score improves by $+10$ points
- (D) Net score improves by $+5$ points

#### Q25
During hours of extreme solar overproduction, total renewable generation reaches $800\text{ MW}$ while maximum transmission evacuation capacity is strictly capped at $650\text{ MW}$ for a 4-hour window. If battery storage absorbs $50\text{ MW}$ continuously, what total volume of renewable energy must be curtailed (wasted) over the 4-hour period?
- (A) $300\text{ MWh}$
- (B) $400\text{ MWh}$
- (C) $450\text{ MWh}$
- (D) $600\text{ MWh}$

---

### Level 6: Extreme (Q26–Q30)

#### Q26 (The Spoke Ordering Distortion Theorem)
Consider Enterprise X's scores $(70, 85, 60, 75, 90)$. If the sequence of spokes around the 5-axis radar is permuted to place the highest scores adjacent to each other—$(90, 85, 75, 70, 60)$—what happens to the enclosed polygon area?
- (A) The area remains strictly invariant because the values are unchanged
- (B) The area contracts because adjacent peaks reduce polygon spread
- (C) The area expands significantly purely due to spoke re-ordering (maximizing adjacent cross-products)
- (D) Radar polygon area cannot be calculated for non-regular polygons

#### Q27
A 7-axis radar chart evaluates aerospace defense contractors with spokes spaced at $\theta = 360^\circ / 7 \approx 51.43^\circ$. A penalty rule states that any contractor with a score below $60$ on any spoke has their composite score reduced by $2.0\times$ the deficit. Contractor Gamma scores $(85, 90, 75, 50, 80, 85, 95)$. What is Gamma's penalized composite score sum?
- (A) $540.0$
- (B) $545.0$
- (C) $550.0$
- (D) $560.0$

#### Q28
A stacked area financial model tracks Cumulative R&D, Cumulative CapEx, and Cumulative SG&A over 5 years. If the top boundary curves are $S_1(t) = 50 t$, $S_2(t) = 120 t$, and $S_3(t) = 180 t$ (where $t$ is in years), what is the annual spend rate of CapEx (Layer 2) alone?
- (A) $50\text{ crore/year}$
- (B) $60\text{ crore/year}$
- (C) $70\text{ crore/year}$
- (D) $120\text{ crore/year}$

#### Q29
In a dynamic power grid, the marginal operating costs of three generation layers are:
- Baseload Coal: $\text{₹}2.50/\text{kWh}$
- Combined Cycle Gas: $\text{₹}4.50/\text{kWh}$
- Imported LNG Peaker: $\text{₹}9.00/\text{kWh}$
If a carbon tax of $\text{₹}2.00/\text{kg CO}_2$ is levied, and Coal emits $0.90\text{ kg CO}_2/\text{kWh}$ while Gas emits $0.40\text{ kg CO}_2/\text{kWh}$, what are the new effective marginal costs of Coal and Gas?
- (A) Coal = $\text{₹}3.50$, Gas = $\text{₹}4.90$
- (B) Coal = $\text{₹}4.30$, Gas = $\text{₹}5.30$
- (C) Coal = $\text{₹}4.50$, Gas = $\text{₹}5.00$
- (D) Coal = $\text{₹}5.20$, Gas = $\text{₹}6.10$

#### Q30
On a 6-axis benchmark Kiviat chart, what is the maximum possible polygon area achievable by a hypothetical "flawless" entity that scores $100$ on all 6 spokes?
- (A) $22,500.0\text{ sq units}$
- (B) $24,800.0\text{ sq units}$
- (C) $25,980.8\text{ sq units}$
- (D) $30,000.0\text{ sq units}$

---

### Level 7: Trap & Statistical Distortions (Q31–Q35)

#### Q31 (The Spoke-Ordering Optical Mirage)
Two vendor evaluation reports present radar charts of the identical Vendor V. Report 1 arranges axes as (Quality, Speed, Cost, Support, Scalability) with alternating high and low scores ($90, 40, 85, 35, 80$). Report 2 clusters high scores together: (Quality, Cost, Scalability, Speed, Support) ($90, 85, 80, 40, 35$). Why does Vendor V appear far more impressive in Report 2?
- (A) Report 2 used logarithmic radial scaling
- (B) Clustering high values creates larger adjacent vector cross-products ($r_i r_{i+1}$), visually bloating the enclosed polygon area by over $+25\%$ without changing a single underlying score
- (C) Report 2 omitted the low scores
- (D) The perimeter remains identical in both reports

#### Q32 (The Wavy Baseline Illusion)
In a stacked area chart showing three software product revenues, Product 1 (bottom) drops sharply by $80\%$. Product 2 (middle) has completely steady sales of exactly $50\text{ M USD}$ every quarter. Why do unsophisticated viewers mistakenly conclude that Product 2 is crashing?
- (A) Product 2's price dropped
- (B) Product 2's volume was miscounted
- (C) Because Product 2's lower baseline is the upper boundary of Product 1, Product 1's collapse pulls down Product 2's entire spatial band, even though its vertical thickness is constant
- (D) Stacked area charts normalize all layers to percentages

#### Q33 (The Radial Quadratic Area Inflation Bias)
On a radar chart, Hub Alpha's score is $50$ and Hub Beta's score is $100$ on all spokes. A viewer perceives Hub Beta as being 4 times as competent as Hub Alpha. What is the psychological / mathematical root of this distortion?
- (A) Polygon visual surface area scales quadratically ($r^2$), so doubling the linear score quadruples the visual ink/area ($\{100/50\}^2 = 4.0$)
- (B) Linear scales invert proportions
- (C) Human perception cannot evaluate radial angles
- (D) Hub Beta's perimeter doubled

#### Q34 (The 100% Stacked Share Mirage)
A clean tech startup's market share in a 100% stacked area graph of European electric scooters expands from $10\%$ in 2022 to $25\%$ in 2023. The CEO claims revenue grew $2.5\times$. What additional information proves the CEO wrong?
- (A) Total market volume contracted from $100,000$ to $30,000$ units (absolute units fell from $10,000$ to $7,500$)
- (B) Product prices dropped by $5\%$
- (C) The number of competitors doubled
- (D) Share cannot exceed $20\%$

#### Q35 (The Equal-Spoke Weighting Fallacy)
A company evaluates supplier resilience on a 5-spoke radar: Cybersecurity ($80$), Geopolitical Diversification ($80$), Financial Solvency ($80$), Labor Safety ($80$), and Single-Source Raw Material Risk ($10$). The average score is $66.0$ ("Moderate Risk"). Why is this radar representation fatally misleading?
- (A) Average calculation was incorrect
- (B) Single-source raw material dependency is a catastrophic single-point-of-failure (conjunctive constraint) that halts $100\%$ of manufacturing regardless of cybersecurity or labor safety
- (C) Cybersecurity should have higher weight
- (D) The axes are correlated

---

### Level 8: Hybrid Infrastructure & Grid Transition Caselet (Q36–Q40)

**Dataset Reference (National Electric Grid 2020–2030 Transition):**  
A national transmission operator models the 24-hour aggregate generation stack transitioning from 2020 to 2030 (measured in Gigawatt-hours, GWh per typical summer day):

```
+-----------------------------------------------------------------------------------+
|               SUMMER DAY 24-HOUR GENERATION ENVELOPE (GWh/day)                    |
+-----------------------------------------------------------------------------------+
| Generation Source         | 2020 Output (GWh) | 2030 Projected (GWh)| Marginal Cost |
|---------------------------+-------------------+---------------------+---------------|
| Baseload Coal (Layer 1)   | 1,800             | 800                 | ₹2.80 / kWh   |
| Nuclear Power (Layer 2)   | 400               | 600                 | ₹1.50 / kWh   |
| Combined Cycle Gas (L3)   | 600               | 400                 | ₹5.20 / kWh   |
| Solar Photovoltaic (L4)   | 300               | 1,200               | ₹1.80 / kWh   |
| Onshore/Offshore Wind (L5)| 400               | 1,000               | ₹2.20 / kWh   |
| Battery Storage BESS (L6) | 0                 | 400 (Discharge)     | ₹6.50 / kWh   |
| Open Peaker Gas (L7)      | 500               | 100                 | ₹11.00 / kWh  |
|---------------------------+-------------------+---------------------+---------------|
| Total Grid Generation     | 4,000 GWh         | 4,500 GWh           |               |
+-----------------------------------------------------------------------------------+
```

*Grid Resilience Radar Scorecard (5 Dimensions on 0–100 Scale):*
- **Grid Inertia & Frequency Stability:** $2020 = 90$, $2030 = 60$
- **Decarbonization Index:** $2020 = 35$, $2030 = 85$
- **Ramping Flexibility:** $2020 = 50$, $2030 = 90$
- **System Operating Cost Efficiency:** $2020 = 70$, $2030 = 80$
- **Fuel Import Security:** $2020 = 45$, $2030 = 85$

*(Additional Operational Parameters: BESS Round-trip efficiency $= 80.0\%$, meaning charging BESS requires $1.25\times$ the discharge energy. During peak solar hours in 2030, $1,850\text{ GWh}$ of renewable generation is generated, but local transmission line thermal constraints cap maximum simultaneous renewable injection to $1,500\text{ GWh}$, with surplus absorbed by battery or curtailed).*

#### Q36
What percentage of the total 2030 daily electricity generation is contributed by zero-carbon clean energy sources (Nuclear + Solar + Wind)?
- (A) $55.56\%$
- (B) $58.20\%$
- (C) $62.22\%$
- (D) $65.00\%$

#### Q37
To discharge $400\text{ GWh}$ of electricity during the evening peak via BESS (Layer 6) at $80.0\%$ round-trip efficiency, how much solar energy must be dedicated to charging BESS during midday, and how many GWh are lost as round-trip thermal dissipation?
- (A) $480\text{ GWh}$ charged, $80\text{ GWh}$ lost
- (B) $500\text{ GWh}$ charged, $100\text{ GWh}$ lost
- (C) $520\text{ GWh}$ charged, $120\text{ GWh}$ lost
- (D) $550\text{ GWh}$ charged, $150\text{ GWh}$ lost

#### Q38
If Coal emits $0.95\text{ kg CO}_2/\text{kWh}$, Nuclear emits $0$, Gas (CCGT + Peaker) emits $0.45\text{ kg CO}_2/\text{kWh}$, and Solar/Wind emit $0$, what is the reduction in total daily $\text{CO}_2$ emissions between 2020 and 2030?
- (A) From $2,205,000\text{ tonnes}$ to $985,000\text{ tonnes}$ (Reduction of $1,220,000\text{ tonnes}$, or $-55.33\%$)
- (B) From $2,500,000\text{ tonnes}$ to $1,100,000\text{ tonnes}$ (Reduction of $-56.00\%$)
- (C) From $2,100,000\text{ tonnes}$ to $1,200,000\text{ tonnes}$ (Reduction of $-42.86\%$)
- (D) From $1,900,000\text{ tonnes}$ to $850,000\text{ tonnes}$ (Reduction of $-55.26\%$)

#### Q39
What is the composite score of the 2030 Grid Resilience Radar Scorecard across the 5 dimensions using equal weighting?
- (A) $76.0$
- (B) $78.5$
- (C) $80.0$
- (D) $82.0$

#### Q40
If $1,850\text{ GWh}$ of solar/wind is generated during midday, transmission lines evacuate $1,500\text{ GWh}$, and BESS absorbs its full daily charging requirement of $500\text{ GWh}$ of which $350\text{ GWh}$ comes from this solar window (leaving $0\text{ GWh}$ unevacuated surplus during that window), what happens if transmission capacity drops unexpectedly to $1,300\text{ GWh}$ while BESS is fully charged?
- (A) Grid explodes
- (B) $200\text{ GWh}$ of renewable power must be curtailed, representing an economic loss of $\text{₹}36\text{ crore}$ at solar tariff $\text{₹}1.80/\text{kWh}$
- (C) Gas peakers ramp up
- (D) Nuclear output is reduced to zero

---

## 4. Rigorous Step-by-Step Solutions & Deductive Derivations

### Level 1 (Q1–Q5)

#### Q1
- **Target:** Rating achieved by Hub A on Spoke 4.
- **Reading:** Look at Spoke 4 (Customer Satisfaction): Hub A $= 75.0$.
- **Correct Answer:** **C**

#### Q2
- **Target:** Deficit between Hub A's actual performance and target on Spoke 3.
- **Calculation:**
  $$\text{Target} = 80, \quad \text{Actual} = 60$$
  $$\text{Deficit} = 80 - 60 = 20.0\text{ points}$$
- **Correct Answer:** **B**

#### Q3
- **Target:** Total aggregate envelope height at 12:00 PM.
- **Reading:** Top boundary of Layer 3 is $450\text{ MW}$. In a stacked area chart, the topmost boundary represents total aggregate generation.
- **Correct Answer:** **A**

#### Q4
- **Target:** Marginal generation contributed by Layer 2.
- **Calculation:**
  $$y_2(t) = S_2(t) - S_1(t) = 320 - 180 = 140\text{ MW}$$
- **Correct Answer:** **D**

#### Q5
- **Target:** Percentage share of Layer 2 in 100% stacked area.
- **Calculation:**
  $$w_2 = \frac{y_2}{Y} \times 100\% = \frac{140}{450} \times 100\% \approx 31.111\% \approx 31.11\%$$
- **Correct Answer:** **B**

---

### Level 2 (Q6–Q10)

#### Q6
- **Target:** Unweighted arithmetic sum of Hub A's ratings.
- **Calculation:**
  $$S = \sum r_i = 70 + 85 + 60 + 75 + 90 = 380.0$$
- **Correct Answer:** **C**

#### Q7
- **Target:** Weighted operational composite score for Hub A.
- **Calculation:**
  $$\bar{S} = 0.30(70) + 0.25(85) + 0.20(60) + 0.15(75) + 0.10(90)$$
  $$\bar{S} = 21.0 + 21.25 + 12.0 + 11.25 + 9.0 = 74.50$$
- **Correct Answer:** **B**

#### Q8
- **Target:** Relative percentage expansion of Layer 2.
- **Calculation:**
  $$\Delta_{\text{rel}} = \frac{186.67 - 140.0}{140.0} \times 100\% = \frac{46.67}{140.0} \times 100\% = 33.33\%$$
- **Correct Answer:** **A**

#### Q9
- **Target:** New total envelope height at 6:00 PM.
- **Calculation:**
  $$Y(6\text{ PM}) = y_1 + y_2 + y_3 = 180 + 190 + 80 = 450\text{ MW}$$
- **Correct Answer:** **C**

#### Q10
- **Target:** Combined power of Layer 1 + Layer 2 at 12:00 PM.
- **Calculation:**
  $$\text{Combined Output} = S_2(t) = 320\text{ MW}$$
  $$\text{Alternatively: } 180 + 140 = 320\text{ MW}$$
- **Correct Answer:** **D**

---

### Level 3 (Q11–Q15)

#### Q11
- **Target:** 5-dimensional Euclidean distance from Hub A $(70, 85, 60, 75, 90)$ to $(100, 100, 100, 100, 100)$.
- **Calculation:**
  $$\Delta = (30, 15, 40, 25, 10)$$
  $$\sum \Delta_i^2 = 30^2 + 15^2 + 40^2 + 25^2 + 10^2 = 900 + 225 + 1600 + 625 + 100 = 3,450$$
  $$D = \sqrt{3,450} \approx 58.7367 \approx 58.74$$
- **Correct Answer:** **B**

#### Q12
- **Target:** Hourly linear ramp rate of Layer 2.
- **Calculation:**
  $$\text{Ramp Rate} = \frac{150 - 100}{12 - 8} = \frac{50\text{ MW}}{4\text{ hours}} = 12.5\text{ MW/hr}$$
- **Correct Answer:** **C**

#### Q13
- **Target:** Impact on SaaS share in 100% stacked area.
- **Calculation:**
  $$\text{Share}_{2021} = \frac{100}{400} = 25.0\%$$
  $$\text{Share}_{2024} = \frac{120}{600} = 20.0\%$$
  $$\Delta \text{Share} = 20.0\% - 25.0\% = -5.0\text{ percentage points}$$
- **Correct Answer:** **A**

#### Q14
- **Target:** Population standard deviation ($\sigma$) of $(70, 85, 60, 75, 90)$.
- **Calculation:**
  $$\text{Mean } \mu = \frac{380}{5} = 76.0$$
  $$\sum (x_i - \mu)^2 = (-6)^2 + (9)^2 + (-16)^2 + (-1)^2 + (14)^2 = 36 + 81 + 256 + 1 + 196 = 570$$
  $$\sigma = \sqrt{\frac{570}{5}} = \sqrt{114} \approx 10.677 \approx 10.68$$
- **Correct Answer:** **D**

#### Q15
- **Target:** Cumulative electrical energy produced in MWh.
- **Calculation:**
  $$E = P \times t = 180\text{ MW} \times 8\text{ hours} = 1,440\text{ MWh}$$
- **Correct Answer:** **B**

---

### Level 4 (Q16–Q20)

#### Q16
- **Target:** Geometric polygon area of regular pentagonal radar with scores $(70, 85, 60, 75, 90)$.
- **Calculation:**
  $$A = \frac{1}{2} \sin(72^\circ) [r_1 r_2 + r_2 r_3 + r_3 r_4 + r_4 r_5 + r_5 r_1]$$
  $$r_1 r_2 = 70 \times 85 = 5,950$$
  $$r_2 r_3 = 85 \times 60 = 5,100$$
  $$r_3 r_4 = 60 \times 75 = 4,500$$
  $$r_4 r_5 = 75 \times 90 = 6,750$$
  $$r_5 r_1 = 90 \times 70 = 6,300$$
  $$\sum r_i r_{i+1} = 5,950 + 5,100 + 4,500 + 6,750 + 6,300 = 28,600$$
  $$A = \frac{1}{2} \times 0.9510565 \times 28,600 = 0.475528 \times 28,600 \approx 13,600.1$$
- **Correct Answer:** **C**

#### Q17
- **Target:** Merit-order placement of peaker gas turbines.
- **Deduction:** Economic dispatch orders plants by ascending marginal operational cost. Peakers have the highest marginal cost per kWh and are dispatched strictly during peak net demand.
- **Correct Answer:** **A**

#### Q18
- **Target:** Contraction of thermal generation during solar surge.
- **Calculation:**
  $$\text{Total Load} = 600\text{ MW}$$
  $$\text{Baseline Nuclear (Layer 1)} = 200\text{ MW}$$
  $$\text{Solar (Layer 2)} = 280\text{ MW}$$
  $$\text{Required Thermal (Layer 3)} = 600 - (200 + 280) = 120\text{ MW}$$
  $$\text{Initial Thermal (zero solar)} = 600 - 200 = 400\text{ MW}$$
  $$\text{Contraction} = 400 - 120 = 280\text{ MW}$$
- **Correct Answer:** **D**

#### Q19
- **Target:** Number of axes where Hub A outperforms Hub B.
- **Comparison:**
  - Spoke 1: $70 > 65$ (Hub A wins)
  - Spoke 2: $85 > 80$ (Hub A wins)
  - Spoke 3: $60 < 70$ (Hub B wins)
  - Spoke 4: $75 < 80$ (Hub B wins)
  - Spoke 5: $90 > 60$ (Hub A wins)
  - Total Hub A wins $= 3\text{ axes}$.
- **Correct Answer:** **B**

#### Q20
- **Target:** System-wide hourly ramping rate from 5 PM to 7 PM.
- **Calculation:**
  $$\Delta P = 590 - 500 = 90\text{ MW}$$
  $$\Delta t = 2\text{ hours} \implies \text{Ramp Rate} = \frac{90}{2} = 45.0\text{ MW/hr}$$
- **Correct Answer:** **C**

---

### Level 5 (Q21–Q25)

#### Q21
- **Target:** Hexagonal Kiviat polygon area for Algo Alpha $(90, 85, 60, 80, 75, 70)$.
- **Calculation:**
  $$A = \frac{\sqrt{3}}{4} \sum_{i=1}^6 r_i r_{i+1}$$
  $$r_1 r_2 = 90 \times 85 = 7,650$$
  $$r_2 r_3 = 85 \times 60 = 5,100$$
  $$r_3 r_4 = 60 \times 80 = 4,800$$
  $$r_4 r_5 = 80 \times 75 = 6,000$$
  $$r_5 r_6 = 75 \times 70 = 5,250$$
  $$r_6 r_1 = 70 \times 90 = 6,300$$
  $$\sum = 7,650 + 5,100 + 4,800 + 6,000 + 5,250 + 6,300 = 35,100$$
  $$A = \frac{1.7320508}{4} \times 35,100 = 0.4330127 \times 35,100 \approx 15,198.7$$
- **Correct Answer:** **B**

#### Q22
- **Target:** Thermal ramp rate during evening duck curve ramp.
- **Calculation:**
  $$\text{Ramp} = \frac{420 - 150}{7 - 4} = \frac{270\text{ MW}}{3\text{ hours}} = 90.0\text{ MW/hr}$$
- **Correct Answer:** **A**

#### Q23
- **Target:** 24-hour Capacity Factor of gas plant.
- **Calculation:**
  - Rated Maximum Energy $= 500\text{ MW} \times 24\text{ hr} = 12,000\text{ MWh}$
  - Period 1 (0–8 hrs): $200\text{ MW} \times 8\text{ hr} = 1,600\text{ MWh}$
  - Period 2 (8–16 hrs, trapezoid): $\frac{200 + 450}{2} \times 8 = 325 \times 8 = 2,600\text{ MWh}$
  - Period 3 (16–24 hrs): $450\text{ MW} \times 8\text{ hr} = 3,600\text{ MWh}$
  - Total Actual Energy $= 1,600 + 2,600 + 3,600 = 7,800\text{ MWh}$
  - Capacity Factor $= \frac{7,800}{12,000} \times 100\% = 65.0\%$
- **Correct Answer:** **C**

#### Q24
- **Target:** Net score shift under iso-performance trade-off.
- **Calculation:**
  $$\Delta S = \Delta \text{Speed} + \Delta \text{Cost} = +15 + (-10) = +5\text{ points}$$
- **Correct Answer:** **D**

#### Q25
- **Target:** Volume of renewable energy curtailed over 4 hours.
- **Calculation:**
  $$\text{Renewable Generation Rate} = 800\text{ MW}$$
  $$\text{Transmission Evacuation Cap} = 650\text{ MW}$$
  $$\text{Battery Absorption Rate} = 50\text{ MW}$$
  $$\text{Total Evacuated/Stored Rate} = 650 + 50 = 700\text{ MW}$$
  $$\text{Curtailed Power Rate} = 800 - 700 = 100\text{ MW}$$
  $$\text{Curtailed Energy over 4 hrs} = 100\text{ MW} \times 4\text{ hrs} = 400\text{ MWh}$$
- **Correct Answer:** **B**

---

### Level 6 (Q26–Q30)

#### Q26
- **Target:** Mathematical impact of spoke re-ordering on enclosed polygon area.
- **Principle:** In $A = \frac{1}{2} \sin(\theta) \sum r_i r_{i+1}$, pairing large scores consecutively maximizes $\sum r_i r_{i+1}$ (Rearrangement Inequality). Hence, permuting axes expands visual area without any data change.
- **Correct Answer:** **C**

#### Q27
- **Target:** Penalized composite score sum for Contractor Gamma.
- **Calculation:**
  - Base Score Sum $= 85 + 90 + 75 + 50 + 80 + 85 + 95 = 560.0$
  - Deficit on Spoke 4 (Threshold $= 60$): $60 - 50 = 10\text{ points}$
  - Penalty $= 2.0 \times 10 = 20.0\text{ points}$
  - Penalized Score $= 560.0 - 20.0 = 540.0$
- **Correct Answer:** **A**

#### Q28
- **Target:** Annual spend rate of CapEx (Layer 2) alone.
- **Calculation:**
  $$y_2(t) = S_2(t) - S_1(t) = 120 t - 50 t = 70 t$$
  $$\frac{d y_2}{dt} = 70\text{ crore/year}$$
- **Correct Answer:** **C**

#### Q29
- **Target:** Effective marginal generation costs under carbon tax.
- **Calculation:**
  - Coal: $\text{Base} = \text{₹}2.50$, Tax $= 0.90\text{ kg} \times \text{₹}2.00/\text{kg} = \text{₹}1.80 \implies \text{Total} = 2.50 + 1.80 = \text{₹}4.30/\text{kWh}$
  - Gas: $\text{Base} = \text{₹}4.50$, Tax $= 0.40\text{ kg} \times \text{₹}2.00/\text{kg} = \text{₹}0.80 \implies \text{Total} = 4.50 + 0.80 = \text{₹}5.30/\text{kWh}$
- **Correct Answer:** **B**

#### Q30
- **Target:** Maximum possible area of regular hexagon with $r = 100$.
- **Calculation:**
  $$A_{\max} = 6 \times \left(\frac{\sqrt{3}}{4} \times 100^2\right) = \frac{3\sqrt{3}}{2} \times 10,000 = 15,000 \times 1.7320508 \approx 25,980.76\text{ sq units}$$
- **Correct Answer:** **C**

---

### Level 7 (Q31–Q35)

#### Q31
- **Target:** Cause of visual inflation in radar chart reports.
- **Explanation:** By clustering large coordinates adjacently, the pairwise cross-products $r_i r_{i+1}$ are maximized, creating a much larger colored polygon area (Rearrangement Inequality).
- **Correct Answer:** **B**

#### Q32
- **Target:** Explanation of the wavy baseline illusion in stacked area charts.
- **Explanation:** In a stacked area chart, the lower boundary of layer $k$ is $S_{k-1}(t)$. Any volatility or sharp plunge in layer 1 moves the physical position of all higher layers down, creating an optical illusion of a collapse in layer 2 even when layer 2's thickness is constant.
- **Correct Answer:** **C**

#### Q33
- **Target:** Root cause of quadratic visual area distortion in radar charts.
- **Explanation:** The visual area of a polygon scales with the square of linear spoke dimensions ($r^2$). A $2\times$ increase in scores leads to a $4\times$ increase in visual surface area ($2^2 = 4$).
- **Correct Answer:** **A**

#### Q34
- **Target:** Identifying why expanding percentage share can accompany falling sales.
- **Explanation:** If the total market volume collapses by more than the percentage gain, absolute unit sales fall: $10\%$ of $100,000 = 10,000$, whereas $25\%$ of $30,000 = 7,500$ (a $-25\%$ drop in volume).
- **Correct Answer:** **A**

#### Q35
- **Target:** Flaw of equal-weight averaging in radar resilience diagrams.
- **Explanation:** Real-world supply chains are governed by conjunctive constraints (weakest-link principles). A complete failure in single-source raw material supply halts the entire plant regardless of high scores in other areas.
- **Correct Answer:** **B**

---

### Level 8 (Q36–Q40)

#### Q36
- **Target:** Percentage of 2030 generation from clean sources (Nuclear + Solar + Wind).
- **Calculation:**
  $$\text{Clean Energy} = 600\text{ (Nuclear)} + 1,200\text{ (Solar)} + 1,000\text{ (Wind)} = 2,800\text{ GWh}$$
  $$\text{Total Generation} = 4,500\text{ GWh}$$
  $$\text{Clean Share} = \frac{2,800}{4,500} \times 100\% \approx 62.222\% \approx 62.22\%$$
- **Correct Answer:** **C**

#### Q37
- **Target:** Energy required to charge BESS and round-trip dissipation loss.
- **Calculation:**
  $$\text{Discharge Target} = 400\text{ GWh}, \quad \eta = 80.0\% = 0.80$$
  $$\text{Energy Input (Charged)} = \frac{400}{0.80} = 500\text{ GWh}$$
  $$\text{Dissipation Loss} = 500 - 400 = 100\text{ GWh}$$
- **Correct Answer:** **B**

#### Q38
- **Target:** Daily $\text{CO}_2$ emissions reduction between 2020 and 2030.
- **Calculation:**
  - **2020 Emissions:**
    - Coal: $1,800\text{ GWh} \times 10^6\text{ kWh/GWh} \times 0.95\text{ kg} = 1,710,000,000\text{ kg} = 1,710,000\text{ tonnes}$
    - Gas: $(600 + 500)\text{ GWh} = 1,100\text{ GWh} \times 10^6 \times 0.45\text{ kg} = 495,000\text{ tonnes}$
    - Total $2020 = 1,710,000 + 495,000 = 2,205,000\text{ tonnes}$
  - **2030 Emissions:**
    - Coal: $800\text{ GWh} \times 10^6 \times 0.95\text{ kg} = 760,000\text{ tonnes}$
    - Gas: $(400 + 100)\text{ GWh} = 500\text{ GWh} \times 10^6 \times 0.45\text{ kg} = 225,000\text{ tonnes}$
    - Total $2030 = 760,000 + 225,000 = 985,000\text{ tonnes}$
  - **Abatement:**
    $$\Delta = 2,205,000 - 985,000 = 1,220,000\text{ tonnes} \implies \frac{1,220,000}{2,205,000} \times 100\% \approx 55.33\%$$
- **Correct Answer:** **A**

#### Q39
- **Target:** Equal-weighted composite score of 2030 Grid Resilience Radar Scorecard.
- **Calculation:**
  $$\bar{S}_{2030} = \frac{60 + 85 + 90 + 80 + 85}{5} = \frac{400}{5} = 80.0$$
- **Correct Answer:** **C**

#### Q40
- **Target:** Renewable curtailment and financial loss when transmission drops to $1,300\text{ GWh}$.
- **Calculation:**
  - Surplus generation during midday $= 1,850\text{ GWh}$
  - Evacuated via lines $= 1,300\text{ GWh}$
  - Absorbed by BESS $= 350\text{ GWh}$
  - Total absorbed/evacuated $= 1,650\text{ GWh}$
  - Curtailed generation $= 1,850 - 1,650 = 200\text{ GWh} = 200,000,000\text{ kWh}$
  - Financial value at tariff $\text{₹}1.80/\text{kWh} = 200,000,000 \times 1.80 = \text{₹}360,000,000 = \text{₹}36\text{ crore}$
- **Correct Answer:** **B**
