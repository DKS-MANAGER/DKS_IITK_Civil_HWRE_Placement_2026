# Quantitative Aptitude Preparation: 15 Fully Solved Numerical Problems
**Target Role:** Early Career Professionals (ECP) — Infrastructure / Water Resources Engineering  
**Company:** AECOM India (Bengaluru & Gurugram)  
**Standard:** Graduate Engineering Online Assessment (OA) Pattern  

---

## Overview

In corporate online screening assessments for infrastructure engineering firms (such as AECOM, Arup, WSP, Jacobs, and Larsen & Toubro), quantitative aptitude tests evaluate candidate speed, numerical reasoning, mental arithmetic, and multi-step algebraic competence.

This module provides **15 fully solved numerical problems** representative of OA benchmarks, with complete algebraic proofs, speed shortcuts, and error trap analyses.

---

### Question 1: Pipes and Cisterns (Hydraulic Discharge & Inflow)

**Problem:**  
A municipal raw water balancing reservoir at a water treatment plant has two inlet pumps, Pump A and Pump B, and one gravity outlet sluice, Sluice C. Pump A running alone can fill the reservoir in 12 hours. Pump B running alone can fill the reservoir in 15 hours. The gravity outlet Sluice C, when fully open, can empty the completely filled reservoir in 20 hours.  
At 06:00 AM, the reservoir is completely empty. Pump A and Pump B are switched ON simultaneously. At 09:00 AM, Sluice C is inadvertently opened by the operations crew and remains open. At what time will the reservoir be completely full?

- **A)** 12:45 PM
- **B)** 01:15 PM
- **C)** 01:40 PM
- **D)** 02:00 PM

#### Detailed Mathematical Solution:
1. **Define Reservoir Capacity as LCM of Time Intervals:**  
   $\text{LCM}(12, 15, 20) = 60\text{ units}$.
2. **Determine Individual Rates of Flow:**
   - Inflow rate of Pump A: $R_A = \frac{60}{12} = +5\text{ units/hour}$.
   - Inflow rate of Pump B: $R_B = \frac{60}{15} = +4\text{ units/hour}$.
   - Outflow rate of Sluice C: $R_C = -\frac{60}{20} = -3\text{ units/hour}$.
3. **Phase 1: 06:00 AM to 09:00 AM (Duration $\Delta t_1 = 3\text{ hours}$):**
   - Active components: Pump A + Pump B.
   - Combined rate: $R_1 = R_A + R_B = 5 + 4 = +9\text{ units/hour}$.
   - Volume filled in Phase 1:
     $$V_1 = 9 \times 3 = 27\text{ units}$$
   - Remaining volume to be filled:
     $$V_{\text{rem}} = 60 - 27 = 33\text{ units}$$
4. **Phase 2: From 09:00 AM onwards (Pump A + Pump B + Sluice C):**
   - Net rate: $R_{\text{net}} = R_A + R_B + R_C = 5 + 4 - 3 = +6\text{ units/hour}$.
   - Time required to fill remaining 33 units:
     $$t_2 = \frac{V_{\text{rem}}}{R_{\text{net}}} = \frac{33}{6} = 5.5\text{ hours} = 5\text{ hours and } 30\text{ minutes}$$
5. **Total Completion Time:**  
   $$\text{Final Time} = 09:00\text{ AM} + 5\text{ hr } 30\text{ min} = 02:30\text{ PM}\dots \text{Wait, verify arithmetic}$$
   Let's check options: 12:45, 01:15, 01:40, 02:00 PM.
   Let's re-verify:
   If Sluice C empty time was 10 hours: rate = -6.
   Let's re-calculate:
   If options are centered around 01:40 PM:
   Suppose reservoir capacity = 60 units.
   At 06:00 AM, A and B open. At 09:00 AM, 3 hours have passed: $9 \times 3 = 27$ units.
   If $t_2 = 33 / 6 = 5.5\text{ hrs} \to 2:30\text{ PM}$.
   Let's adjust question parameters so option C (01:40 PM) is exact:
   Suppose Sluice C empties in 10 hours ($R_C = -6$)? Then net rate = $5 + 4 - 6 = 3$ units/hr $\implies 33/3 = 11$ hrs.
   Suppose Phase 1 was 2 hours (06:00 to 08:00 AM): $V_1 = 18$ units. $V_{\text{rem}} = 42$. $42/6 = 7$ hrs.
   Suppose Pump A fills in 6 hours ($+10$), B in 10 hours ($+6$), C empties in 15 hours ($-4$). Total = 60 units.
   Phase 1 (06:00 to 09:00 AM, 3 hrs): $(10 + 6) \times 3 = 48$ units.
   Remaining: $60 - 48 = 12$ units.
   Net rate: $10 + 6 - 4 = 12$ units/hour.
   Time = $12 / 12 = 1$ hour.
   Time = 10:00 AM.
   Let's set clean numbers where the result matches **01:40 PM**:
   Let total capacity = 60 units.
   Pump A fills in 10 hrs ($+6$ units/hr).
   Pump B fills in 15 hrs ($+4$ units/hr).
   Sluice C empties in 12 hrs ($-5$ units/hr).
   Phase 1: 06:00 AM to 09:00 AM (3 hrs) with A and B: $(6 + 4) \times 3 = 30$ units.
   Remaining volume = $60 - 30 = 30$ units.
   At 09:00 AM, Sluice C opens. Net rate = $6 + 4 - 5 = +5$ units/hr.
   Time to fill = $30 / 5 = 6$ hours. $09:00\text{ AM} + 6\text{ hours} = 03:00\text{ PM}$.
   Let's make: Remaining volume = 28 units, rate = 6 units/hr $\implies 4\text{ hr } 40\text{ min} \implies 09:00 + 4:40 = 01:40\text{ PM}$!
   To get remaining volume = 28 units out of 60:
   Phase 1 filled = 32 units. If A and B rate = $10$ units/hr for 3.2 hrs?
   Let's construct the numbers cleanly:
   Let Pump A fill in 8 hours ($+7.5$), B in 12 hours ($+5$), C empty in 24 hours ($-2.5$). Total = 60 units.
   Rate of A + B = $12.5$ units/hr. Phase 1 (2 hours, 07:00 to 09:00): $25$ units. Remaining = 35 units.
   Net rate with C = $12.5 - 2.5 = 10$ units/hr.
   Time = $3.5$ hrs $\implies 09:00 + 3.5 = 12:30\text{ PM}$.

Let's fix the question statement to have exact, crisp numbers:
- Pump A fills in **8 hours**
- Pump B fills in **12 hours**
- Sluice C empties in **16 hours**
- Total capacity = $\text{LCM}(8, 12, 16) = 48\text{ units}$.
- Rate A = $6\text{ units/hr}$, Rate B = $4\text{ units/hr}$, Rate C = $-3\text{ units/hr}$.
- Start at 07:00 AM with A and B. Rate = $10\text{ units/hr}$.
- At 09:00 AM (2 hours elapsed), Volume filled = $2 \times 10 = 20\text{ units}$.
- Remaining volume = $48 - 20 = 28\text{ units}$.
- At 09:00 AM, Sluice C is opened.
- Combined net rate = $6 + 4 - 3 = 7\text{ units/hr}$.
- Time required = $\frac{28}{7} = 4\text{ hours}$.
- Time of completion = $09:00\text{ AM} + 4\text{ hours} = \mathbf{01:00\text{ PM}}$.

**Updated Options:**
- **A)** 12:00 PM
- **B)** 12:30 PM
- **C)** 01:00 PM
- **D)** 01:30 PM

**Correct Answer:** **C) 01:00 PM**

#### Shortcut Method:
Total units = 48.
Work done in first 2 hrs = $(6 + 4) \times 2 = 20$.
Remaining work = $48 - 20 = 28$.
Net efficiency = $6 + 4 - 3 = 7$.
Time = $28 / 7 = 4$ hours after 09:00 AM $\to 01:00$ PM.

#### Trap to Avoid:
Forgetting to add the initial 2 hours to the start time or applying Sluice C's emptying rate from 07:00 AM instead of 09:00 AM.

---

### Question 2: Time, Speed, and Distance (Relative Speed & Headwind)

**Problem:**  
An inspection drone flies from AECOM's Gurugram site office to a regional bridge construction site located $120\text{ km}$ away along a straight corridor against a steady headwind. The return flight from the bridge site to the office is along the exact same path with the same wind acting as a tailwind. The return flight takes $40\text{ minutes}$ less than the outward flight. If the drone's cruising speed in still air is $50\text{ km/h}$, find the velocity of the wind.

- **A)** $8\text{ km/h}$
- **B)** $10\text{ km/h}$
- **C)** $12\text{ km/h}$
- **D)** $15\text{ km/h}$

#### Detailed Mathematical Solution:
1. Let the velocity of the wind be $w\text{ km/h}$.
2. Speed during outward flight (against headwind): $v_{\text{out}} = (50 - w)\text{ km/h}$.
3. Speed during return flight (with tailwind): $v_{\text{ret}} = (50 + w)\text{ km/h}$.
4. Distance $D = 120\text{ km}$.
5. Time difference $\Delta t = 40\text{ minutes} = \frac{40}{60} = \frac{2}{3}\text{ hours}$.
6. Equation:
   $$\frac{120}{50 - w} - \frac{120}{50 + w} = \frac{2}{3}$$
7. Factor out 120 and find common denominator:
   $$120 \left[ \frac{(50 + w) - (50 - w)}{(50 - w)(50 + w)} \right] = \frac{2}{3}$$
   $$120 \left[ \frac{2w}{2500 - w^2} \right] = \frac{2}{3}$$
   $$\frac{240w}{2500 - w^2} = \frac{2}{3}$$
   $$3 \times 240w = 2 \times (2500 - w^2)$$
   $$720w = 5000 - 2w^2$$
   $$2w^2 + 720w - 5000 = 0 \implies w^2 + 360w - 2500 = 0$$
   Let's check roots:
   If $w = 10$: $10^2 + 360(10) - 2500 = 100 + 3600 - 2500 = 1200 \ne 0$.
   Wait! Let's re-check the distance and time:
   If $w = 10\text{ km/h}$:
   $t_{\text{out}} = \frac{120}{50 - 10} = \frac{120}{40} = 3\text{ hours}$.
   $t_{\text{ret}} = \frac{120}{50 + 10} = \frac{120}{60} = 2\text{ hours}$.
   Difference = $3 - 2 = 1\text{ hour} = 60\text{ minutes}$!
   Therefore, if the time difference is **1 hour (60 minutes)**, $w = 10\text{ km/h}$ exactly!
   Let's update the question statement to "takes $1\text{ hour}$ less" so that $w = 10\text{ km/h}$ is exact and clean.

**Updated Problem Statement:**  
"...The return flight takes **$1\text{ hour}$ less** than the outward flight. If the drone's speed in still air is $50\text{ km/h}$, find the velocity of the wind."

- **A)** $5\text{ km/h}$
- **B)** $10\text{ km/h}$
- **C)** $12.5\text{ km/h}$
- **D)** $15\text{ km/h}$

**Correct Answer:** **B) $10\text{ km/h}$**

#### Shortcut / Option Plugging:
Test Option B ($w = 10$):
- Outward speed = $50 - 10 = 40\text{ km/h} \implies t_1 = 120/40 = 3\text{ hrs}$.
- Return speed = $50 + 10 = 60\text{ km/h} \implies t_2 = 120/60 = 2\text{ hrs}$.
- Difference = $3 - 2 = 1\text{ hr}$. Matches instantly without solving quadratic equation.

---

### Question 3: Mixtures and Alligation (Concrete Mortar Batching)

**Problem:**  
A site materials engineer needs to prepare a high-early-strength grout mix with a cement-to-aggregate ratio of $40\%$ cement by mass. The site has two silos of pre-blended mixes:
- Mix X contains $25\%$ cement by mass.
- Mix Y contains $65\%$ cement by mass.
How many kilograms of Mix X must be blended with Mix Y to produce exactly $800\text{ kg}$ of the desired $40\%$ cement grout?

- **A)** $300\text{ kg}$
- **B)** $480\text{ kg}$
- **C)** $500\text{ kg}$
- **D)** $520\text{ kg}$

#### Detailed Mathematical Solution:
1. **Rule of Alligation:**
   $$\frac{\text{Mass of Mix X}}{\text{Mass of Mix Y}} = \frac{\%_Y - \%_{\text{target}}}{\%_{\text{target}} - \%_X} = \frac{65 - 40}{40 - 25} = \frac{25}{15} = \frac{5}{3}$$
2. The ratio of Mix X to Mix Y is $5 : 3$.
3. Total parts = $5 + 3 = 8\text{ parts}$.
4. Total mass required = $800\text{ kg}$.
5. Mass of Mix X:
   $$M_X = \left(\frac{5}{8}\right) \times 800 = 500\text{ kg}$$
6. Mass of Mix Y:
   $$M_Y = \left(\frac{3}{8}\right) \times 800 = 300\text{ kg}$$

**Correct Answer:** **C) $500\text{ kg}$**

#### Verification:
Total cement mass = $0.25(500) + 0.65(300) = 125 + 195 = 320\text{ kg}$.
Percentage = $\frac{320}{800} \times 100\% = 40\%$. (Exact).

---

### Question 4: Work and Wages (Project Engineering Labor)

**Problem:**  
Three design engineers—A, B, and C—are assigned to complete a highway drainage design package for AECOM.
- Engineer A and B together can complete the package in $10\text{ days}$.
- Engineer B and C together can complete it in $15\text{ days}$.
- Engineer A and C together can complete it in $12\text{ days}$.
If the total consultancy fee allocated for drafting this package is ₹$1,44,000$, and payments are distributed strictly in proportion to their daily individual work output, what is Engineer A's individual share?

- **A)** ₹$48,000$
- **B)** ₹$64,000$
- **C)** ₹$72,000$
- **D)** ₹$84,000$

#### Detailed Mathematical Solution:
1. Let total work = $\text{LCM}(10, 15, 12) = 60\text{ units}$.
2. Pairwise work rates:
   - $R_A + R_B = \frac{60}{10} = 6\text{ units/day}$
   - $R_B + R_C = \frac{60}{15} = 4\text{ units/day}$
   - $R_A + R_C = \frac{60}{12} = 5\text{ units/day}$
3. Summing all three equations:
   $$2(R_A + R_B + R_C) = 6 + 4 + 5 = 15 \implies R_A + R_B + R_C = 7.5\text{ units/day}$$
4. Calculate individual efficiencies:
   - $R_A = (R_A + R_B + R_C) - (R_B + R_C) = 7.5 - 4 = 3.5\text{ units/day}$
   - $R_B = (R_A + R_B + R_C) - (R_A + R_C) = 7.5 - 5 = 2.5\text{ units/day}$
   - $R_C = (R_A + R_B + R_C) - (R_A + R_B) = 7.5 - 6 = 1.5\text{ units/day}$
5. Ratio of efficiencies:
   $$R_A : R_B : R_C = 3.5 : 2.5 : 1.5 = 7 : 5 : 3$$
6. Total parts = $7 + 5 + 3 = 15\text{ parts}$.
7. Engineer A's share:
   $$\text{Share}_A = \frac{7}{15} \times 1,44,000 = 7 \times 9,600 = \text{₹}67,200\dots \text{Wait, let's check options: 48k, 64k, 72k, 84k}$$
   Let's check if total fee is ₹$1,20,000$ or if $R_A$ share is different:
   $\frac{7}{15} \times 1,80,000 = 7 \times 12,000 = \text{₹}84,000$!
   If the fee is ₹$1,80,000$, then $\text{Share}_A = \text{₹}84,000$.
   Let's set total fee to **₹$1,80,000$** so that **Option D (₹84,000)** is exact!

**Updated Problem Statement:**  
"...If the total consultancy fee allocated for drafting this package is **₹$1,80,000$**, what is Engineer A's individual share?"

- **A)** ₹$48,000$
- **B)** ₹$60,000$
- **C)** ₹$72,000$
- **D)** ₹$84,000$

**Correct Answer:** **D) ₹$84,000$**

---

### Question 5: Percentage and Depreciation (Heavy Earthmoving Equipment)

**Problem:**  
A hydraulic excavator procured for the Dholera Industrial City project cost ₹$80,00,000$ new. Its value depreciates at a constant compound annual rate of $15\%$ for the first two years, and then at a rate of $10\%$ per annum for subsequent years due to salvage stabilization. What is the book value of the excavator at the end of 3 years?

- **A)** ₹$50,40,000$
- **B)** ₹$52,02,000$
- **C)** ₹$54,20,000$
- **D)** ₹$55,08,000$

#### Detailed Mathematical Solution:
1. Initial cost $V_0 = \text{₹}80,00,000$.
2. Depreciation factor for Year 1: $(1 - 0.15) = 0.85$.
3. Depreciation factor for Year 2: $(1 - 0.15) = 0.85$.
4. Depreciation factor for Year 3: $(1 - 0.10) = 0.90$.
5. Value at end of Year 3:
   $$V_3 = V_0 \times (0.85)^2 \times 0.90$$
6. Step-by-step arithmetic:
   - $(0.85)^2 = 0.7225$
   - $V_2 = 80,00,000 \times 0.7225 = 57,80,000$
   - $V_3 = 57,80,000 \times 0.90 = 57,80,000 - 5,78,000 = \text{₹}52,02,000$

**Correct Answer:** **B) ₹$52,02,000$**

---

### Question 6: Probability (Bridge Inspection Sensor Reliability)

**Problem:**  
To monitor structural health on a high-speed rail viaduct, an array of three independent piezoresistive strain sensors is installed at a critical pier-girder interface. For any anomalous displacement event exceeding $5\text{ mm}$, the probabilities of Sensor 1, Sensor 2, and Sensor 3 independently triggering an alarm are $0.90$, $0.80$, and $0.70$ respectively.  
What is the probability that **at least two** sensors will trigger the alarm during an anomalous event?

- **A)** $0.784$
- **B)** $0.856$
- **C)** $0.898$
- **D)** $0.924$

#### Detailed Mathematical Solution:
1. Let $A, B, C$ denote the events that Sensors 1, 2, and 3 trigger.
   - $P(A) = 0.90 \implies P(A') = 0.10$
   - $P(B) = 0.80 \implies P(B') = 0.20$
   - $P(C) = 0.70 \implies P(C') = 0.30$
2. "At least two" means exactly two sensors trigger OR all three sensors trigger:
   $$P(\ge 2) = P(\text{all 3}) + P(A \cap B \cap C') + P(A \cap B' \cap C) + P(A' \cap B \cap C)$$
3. Compute individual joint probabilities:
   - All three: $0.90 \times 0.80 \times 0.70 = 0.504$
   - A and B, not C: $0.90 \times 0.80 \times 0.30 = 0.216$
   - A and C, not B: $0.90 \times 0.20 \times 0.70 = 0.126$
   - B and C, not A: $0.10 \times 0.80 \times 0.70 = 0.056$
4. Summing all mutually exclusive cases:
   $$P(\ge 2) = 0.504 + 0.216 + 0.126 + 0.056 = 0.902\dots \text{Wait: } 0.504 + 0.216 = 0.720; 0.720 + 0.126 = 0.846; 0.846 + 0.056 = 0.902$$
   Let's check options: if options are A) 0.856, B) 0.898, C) 0.902, D) 0.924.
   Let's make **C) 0.902** an option!

**Updated Options:**
- **A)** $0.856$
- **B)** $0.884$
- **C)** $0.902$
- **D)** $0.948$

**Correct Answer:** **C) $0.902$**

---

### Question 7: Permutations and Combinations (Inspection Team Dispatch)

**Problem:**  
AECOM's Delhi-NCR infrastructure inspection pool consists of 6 Geotechnical engineers, 5 Structural engineers, and 4 Hydraulic engineers. A specialized rapid-response forensic team of 5 engineers must be formed to investigate a canal embankment breach.  
The team must contain **at least 2 Geotechnical engineers** and **at least 1 Hydraulic engineer**. How many distinct team combinations can be selected?

- **A)** $1,248$
- **B)** $1,860$
- **C)** $2,142$
- **D)** $2,436$

#### Detailed Mathematical Solution:
1. Total engineers = $6\text{ Geo} + 5\text{ Struct} + 4\text{ Hyd} = 15\text{ engineers}$.
2. Team size = 5.
3. Constraints: $G \ge 2$, $H \ge 1$.
   Possible partitions $(G, H, S)$ where $G + H + S = 5$, $G \in [2, 4]$, $H \in [1, 3]$, $S \in [0, 2]$:
   - Case 1: $G = 2, H = 1, S = 2 \implies \binom{6}{2} \binom{4}{1} \binom{5}{2} = 15 \times 4 \times 10 = 600$
   - Case 2: $G = 2, H = 2, S = 1 \implies \binom{6}{2} \binom{4}{2} \binom{5}{1} = 15 \times 6 \times 5 = 450$
   - Case 3: $G = 2, H = 3, S = 0 \implies \binom{6}{2} \binom{4}{3} \binom{5}{0} = 15 \times 4 \times 1 = 60$
   - Case 4: $G = 3, H = 1, S = 1 \implies \binom{6}{3} \binom{4}{1} \binom{5}{1} = 20 \times 4 \times 5 = 400$
   - Case 5: $G = 3, H = 2, S = 0 \implies \binom{6}{3} \binom{4}{2} \binom{5}{0} = 20 \times 6 \times 1 = 120$
   - Case 6: $G = 4, H = 1, S = 0 \implies \binom{6}{4} \binom{4}{1} \binom{5}{0} = 15 \times 4 \times 1 = 60$
4. Total valid combinations:
   $$\text{Total} = 600 + 450 + 60 + 400 + 120 + 60 = 1,690$$
   Let's check options: if options are A) 1,540, B) 1,690, C) 1,820, D) 2,142.

**Updated Options:**
- **A)** $1,540$
- **B)** $1,690$
- **C)** $1,820$
- **D)** $2,142$

**Correct Answer:** **B) $1,690$**

---

### Question 8: Profit, Loss, and Commercial Bidding

**Problem:**  
In an engineering consultancy tender, AECOM estimates the baseline execution cost of an Environmental Impact Assessment (EIA) study at ₹$50,00,000$. The commercial team marks up the baseline cost by $40\%$ to arrive at the catalog list bid price. During client contract negotiations, the client demands a rebate. What maximum percentage discount can AECOM offer on the list bid price such that the firm still secures a net profit margin of $19\%$ over the baseline cost?

- **A)** $12\%$
- **B)** $15\%$
- **C)** $18\%$
- **D)** $21\%$

#### Detailed Mathematical Solution:
1. Baseline Cost $C = 100\text{ units}$.
2. List Bid Price $L = 100 \times 1.40 = 140\text{ units}$.
3. Desired Selling Price with $19\%$ profit: $S = 100 \times 1.19 = 119\text{ units}$.
4. Discount allowable = $L - S = 140 - 119 = 21\text{ units}$.
5. Percentage discount on List Price:
   $$\text{Discount \%} = \frac{L - S}{L} \times 100\% = \frac{21}{140} \times 100\% = \frac{3}{20} \times 100\% = 15\%$$

**Correct Answer:** **B) $15\%$**

---

### Question 9: Simple and Compound Interest (Capital Financing)

**Problem:**  
An infrastructure joint venture borrows ₹$10\text{ Crores}$ for project mobilization. A portion of the loan is borrowed from Bank 1 at an annual simple interest rate of $8\%$, while the remaining portion is borrowed from Bank 2 at an annual compound interest rate of $10\%$ compounded annually. If at the end of 2 years, the total interest paid to both banks combined is ₹$1,89,00,000$, how much principal was borrowed from Bank 2?

- **A)** ₹$3.5\text{ Crores}$
- **B)** ₹$4.0\text{ Crores}$
- **C)** ₹$4.5\text{ Crores}$
- **D)** ₹$5.0\text{ Crores}$

#### Detailed Mathematical Solution:
1. Let principal from Bank 2 be $P_2$ (in ₹ Crores).
2. Principal from Bank 1 is $P_1 = (10 - P_2)$ Crores.
3. Interest from Bank 1 (Simple Interest for 2 years at $8\%$):
   $$I_1 = P_1 \times 0.08 \times 2 = 0.16(10 - P_2) = 1.60 - 0.16 P_2$$
4. Interest from Bank 2 (Compound Interest for 2 years at $10\%$):
   $$I_2 = P_2 \times \left[(1 + 0.10)^2 - 1\right] = P_2 \times (1.21 - 1) = 0.21 P_2$$
5. Total Interest $I_{\text{total}} = 1.89\text{ Crores}$:
   $$(1.60 - 0.16 P_2) + 0.21 P_2 = 1.89$$
   $$1.60 + 0.05 P_2 = 1.89$$
   $$0.05 P_2 = 0.29 \implies P_2 = \frac{0.29}{0.05} = 5.8\text{ Crores}$$
   Let's check if $I_{\text{total}} = 1.85$ or $1.80$:
   If $P_2 = 5.0\text{ Crores}$:
   $I_1 = 5 \times 0.16 = 0.80$ Cr.
   $I_2 = 5 \times 0.21 = 1.05$ Cr.
   Total = $0.80 + 1.05 = 1.85\text{ Crores} = \text{₹}1,85,00,000$!
   Let's set total interest to **₹$1,85,00,000$** so that $P_2 = 5.0\text{ Crores}$ is exact!

**Updated Problem Statement:**  
"...If at the end of 2 years, the total interest paid to both banks combined is **₹$1,85,00,000$**, how much principal was borrowed from Bank 2?"

- **A)** ₹$3.5\text{ Crores}$
- **B)** ₹$4.0\text{ Crores}$
- **C)** ₹$4.5\text{ Crores}$
- **D)** ₹$5.0\text{ Crores}$

**Correct Answer:** **D) ₹$5.0\text{ Crores}$**

---

### Question 10: Mensuration and Geometry (Culvert Flow Area)

**Problem:**  
A horse-shoe tunnel arch cross-section consists of a semi-circular crown of radius $R = 3\text{ m}$ resting on vertical sidewalls of height $H = 2\text{ m}$, with a flat horizontal invert bed of width $2R = 6\text{ m}$. What is the total cross-sectional area and the wetted perimeter when the tunnel is running full (excluding the bed invert)?

- **A)** $\text{Area} = 26.14\text{ m}^2$, $\text{Perimeter} = 13.42\text{ m}$
- **B)** $\text{Area} = 22.14\text{ m}^2$, $\text{Perimeter} = 11.28\text{ m}$
- **C)** $\text{Area} = 28.56\text{ m}^2$, $\text{Perimeter} = 15.71\text{ m}$
- **D)** $\text{Area} = 24.32\text{ m}^2$, $\text{Perimeter} = 12.56\text{ m}$

#### Detailed Mathematical Solution:
1. Total cross-sectional area:
   $$\text{Area} = \text{Area of semi-circle} + \text{Area of rectangular lower section}$$
   $$\text{Area} = \frac{\pi R^2}{2} + (2R \times H)$$
   $$\text{Area} = \frac{\pi \times 3^2}{2} + (6 \times 2) = 4.5\pi + 12 \approx 4.5 \times 3.14159 + 12 = 14.137 + 12 = 26.137\text{ m}^2 \approx 26.14\text{ m}^2$$
2. Perimeter (semi-circular arch + 2 vertical side walls):
   $$\text{Perimeter} = \pi R + 2H = 3\pi + 2(2) = 3(3.14159) + 4 = 9.425 + 4 = 13.425\text{ m} \approx 13.42\text{ m}$$

**Correct Answer:** **A) $\text{Area} = 26.14\text{ m}^2$, $\text{Perimeter} = 13.42\text{ m}$**

---

### Question 11: Averages and Weighted Quantities (Hydraulic Gradient Profiling)

**Problem:**  
Along a $150\text{ km}$ water pipeline alignment, the terrain slopes vary across three distinct geomorphic reaches:
- Reach 1 ($50\text{ km}$): Hydraulic gradient $S_1 = 1 \text{ in } 500 = 0.0020$
- Reach 2 ($60\text{ km}$): Hydraulic gradient $S_2 = 1 \text{ in } 1000 = 0.0010$
- Reach 3 ($40\text{ km}$): Hydraulic gradient $S_3 = 1 \text{ in } 250 = 0.0040$
What is the overall distance-weighted average hydraulic gradient across the entire $150\text{ km}$ alignment?

- **A)** $1 \text{ in } 469$ ($0.00213$)
- **B)** $1 \text{ in } 536$ ($0.00187$)
- **C)** $1 \text{ in } 625$ ($0.00160$)
- **D)** $1 \text{ in } 750$ ($0.00133$)

#### Detailed Mathematical Solution:
1. Distance-weighted average gradient $\bar{S}$:
   $$\bar{S} = \frac{\sum (L_i \times S_i)}{\sum L_i} = \frac{50(0.0020) + 60(0.0010) + 40(0.0040)}{150}$$
2. Numerator:
   - Reach 1 elevation drop: $50,000 \times 0.0020 = 100\text{ m}$ (or in km: $50 \times 0.002 = 0.100\text{ km}$)
   - Reach 2 elevation drop: $60 \times 0.001 = 0.060\text{ km}$
   - Reach 3 elevation drop: $40 \times 0.004 = 0.160\text{ km}$
   - Total drop = $0.100 + 0.060 + 0.160 = 0.320\text{ km} = 320\text{ m}$
3. Weighted average gradient:
   $$\bar{S} = \frac{0.320}{150} = \frac{32}{15000} = \frac{1}{468.75} \approx 1 \text{ in } 469 \text{ (or } 0.002133\text{)}$$

**Correct Answer:** **A) $1 \text{ in } 469$ ($0.00213$)**

---

### Question 12: Ratio and Proportion (Catchment Runoff Partitioning)

**Problem:**  
A river basin with an annual rainfall volume of $1,200\text{ million cubic meters (MCM)}$ discharges into three tributary sub-catchments A, B, and C such that:
- $3$ times the volume in Catchment A is equal to $4$ times the volume in Catchment B.
- $5$ times the volume in Catchment B is equal to $6$ times the volume in Catchment C.
Assuming zero initial storage changes, what is the allocated runoff volume in Catchment B?

- **A)** $320\text{ MCM}$
- **B)** $360\text{ MCM}$
- **C)** $400\text{ MCM}$
- **D)** $480\text{ MCM}$

#### Detailed Mathematical Solution:
1. $3A = 4B \implies \frac{A}{B} = \frac{4}{3} = \frac{20}{15}$.
2. $5B = 6C \implies \frac{B}{C} = \frac{6}{5} = \frac{15}{12.5}\dots$ Let's make integer ratios:
   $B$ is common to both:
   $\frac{A}{B} = \frac{4}{3} = \frac{8}{6}$.
   $\frac{B}{C} = \frac{6}{5}$.
   Therefore:
   $$A : B : C = 8 : 6 : 5$$
3. Sum of ratio parts = $8 + 6 + 5 = 19\text{ parts}$.
   $1200 / 19$ is not an integer.
   Let's check if total volume is $1,140\text{ MCM}$:
   $1140 / 19 = 60\text{ MCM}$.
   Then $B = 6 \times 60 = 360\text{ MCM}$!
   $A = 8 \times 60 = 480\text{ MCM}$.
   $C = 5 \times 60 = 300\text{ MCM}$.
   Total = $480 + 360 + 300 = 1,140\text{ MCM}$.

**Updated Problem Statement:**  
"...A river basin with an annual rainfall volume of **$1,140\text{ million cubic meters (MCM)}$** discharges into three tributary sub-catchments..."

- **A)** $300\text{ MCM}$
- **B)** $360\text{ MCM}$
- **C)** $420\text{ MCM}$
- **D)** $480\text{ MCM}$

**Correct Answer:** **B) $360\text{ MCM}$**

---

### Question 13: Time and Distance (Two Trains / Survey Vehicles Approaching)

**Problem:**  
Two railway track inspection trolleys leave Station P and Station Q simultaneously, traveling towards each other on parallel tracks along the Western Dedicated Freight Corridor. They cross each other after $4\text{ hours}$. If Trolley P takes $3\text{ hours and } 20\text{ minutes}$ less than Trolley Q to cover the entire distance between P and Q, what is the speed of Trolley P if the distance between P and Q is $240\text{ km}$?

- **A)** $30\text{ km/h}$
- **B)** $36\text{ km/h}$
- **C)** $40\text{ km/h}$
- **D)** $45\text{ km/h}$

#### Detailed Mathematical Solution:
1. Total distance $D = 240\text{ km}$.
2. Time to cross = $4\text{ hours} \implies v_P + v_Q = \frac{240}{4} = 60\text{ km/h}$.
3. Let $v_P = v \implies v_Q = 60 - v$.
4. Time difference: $t_Q - t_P = 3\text{ hr } 20\text{ min} = \frac{10}{3}\text{ hours}$.
   $$\frac{240}{60 - v} - \frac{240}{v} = \frac{10}{3}$$
5. Divide by 10:
   $$24 \left( \frac{v - (60 - v)}{v(60 - v)} \right) = \frac{1}{3}$$
   $$24 \left( \frac{2v - 60}{60v - v^2} \right) = \frac{1}{3} \implies 72(2v - 60) = 60v - v^2$$
   $$144v - 4320 = 60v - v^2 \implies v^2 + 84v - 4320 = 0$$
6. Factorizing:
   Find two numbers with product $-4320$ and sum $84$:
   $120 \times (-36) = -4320$, and $120 - 36 = 84$.
   $$(v + 120)(v - 36) = 0 \implies v = 36\text{ km/h}$$
7. Check:
   - $v_P = 36\text{ km/h} \implies t_P = \frac{240}{36} = \frac{20}{3}\text{ hrs} = 6\text{ hr } 40\text{ min}$.
   - $v_Q = 60 - 36 = 24\text{ km/h} \implies t_Q = \frac{240}{24} = 10\text{ hrs}$.
   - Difference = $10 - 6\frac{2}{3} = 3\frac{1}{3}\text{ hrs} = 3\text{ hr } 20\text{ min}$. Exactly matches!

**Correct Answer:** **B) $36\text{ km/h}$**

---

### Question 14: Quadratic Equations and Optimization (Channel Hydraulic Efficiency)

**Problem:**  
An open drainage channel of rectangular cross-section is to be designed with a fixed cross-sectional area of $A = 18\text{ m}^2$. The wetted perimeter is given by $P = B + 2y$, where $B$ is the bed width and $y$ is the water depth. For what value of depth $y$ is the wetted perimeter minimized (ensuring maximum hydraulic efficiency)?

- **A)** $1.5\text{ m}$
- **B)** $2.12\text{ m}$
- **C)** $3.0\text{ m}$
- **D)** $4.24\text{ m}$

#### Detailed Mathematical Solution:
1. $A = B \times y = 18 \implies B = \frac{18}{y}$.
2. Wetted perimeter:
   $$P(y) = \frac{18}{y} + 2y$$
3. To minimize $P(y)$, take the first derivative with respect to $y$ and set to zero:
   $$\frac{dP}{dy} = -\frac{18}{y^2} + 2 = 0 \implies 2y^2 = 18 \implies y^2 = 9 \implies y = 3\text{ m}$$
4. Second derivative check:
   $$\frac{d^2P}{dy^2} = \frac{36}{y^3} > 0 \quad (\text{for } y > 0 \implies \text{Strict Local Minimum})$$
5. Width $B = \frac{18}{3} = 6\text{ m} = 2y$ (classic most efficient rectangular hydraulic section: $B = 2y$).

**Correct Answer:** **C) $3.0\text{ m}$**

---

### Question 15: Logarithms and Scale Transformations (Earthquake Intensity / Decibel Attenuation)

**Problem:**  
In geotechnical seismic isolation design, ground vibration amplitude attenuates with radial distance $r$ from a blast according to:
$$A(r) = A_0 \cdot 10^{-0.04 r}$$
where $A_0$ is the source amplitude and $r$ is in meters. At what distance $r$ will the vibration amplitude be reduced to exactly $1\%$ of its initial value $A_0$?

- **A)** $25\text{ m}$
- **B)** $50\text{ m}$
- **C)** $75\text{ m}$
- **D)** $100\text{ m}$

#### Detailed Mathematical Solution:
1. We require $\frac{A(r)}{A_0} = 0.01 = 10^{-2}$.
2. Substitute into equation:
   $$10^{-0.04 r} = 10^{-2}$$
3. Equating exponents:
   $$-0.04 r = -2 \implies 0.04 r = 2$$
   $$r = \frac{2}{0.04} = \frac{200}{4} = 50\text{ meters}$$

**Correct Answer:** **B) $50\text{ m}$**

---
*End of Quantitative Aptitude Bank (15 Solved Problems).*
