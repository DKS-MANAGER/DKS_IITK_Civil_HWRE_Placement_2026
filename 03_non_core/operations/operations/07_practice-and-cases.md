# 07. Operations Management: Practice Problems & Deep Cases

> **Track**: Operations Management & Process Engineering  
> **Target Audience**: IIT Kanpur candidates preparing for core operations, supply chain, and manufacturing excellence technical interviews.  
> **Content Structure**: Fully worked mathematical numericals, assembly line balancing, queueing derivations, and realistic industrial turnarounds.

---

## Problem 1: Assembly Line Balancing & Efficiency Optimization

### Problem Statement
An automotive sub-assembly line operates for $8\text{ hours}$ per day with an intended production quota of $480\text{ units/day}$. The manufacturing process consists of six sequential tasks whose elemental times and precedence relationships are detailed below:

| Task | Work Element Description | Immediate Predecessors | Task Time ($t_i$, seconds) |
| :---: | :--- | :---: | :---: |
| **A** | Insert Base Frame & Pins | None | 35 |
| **B** | Mount Drive Motor Assembly | A | 45 |
| **C** | Connect Electronic Wiring Harness | A | 25 |
| **D** | Install Gearbox Housing | B | 50 |
| **E** | Fasten Outer Casing & Seals | C, D | 40 |
| **F** | Final Calibration & Testing | E | 25 |

### Candidate Requirements:
1. Calculate the required cycle time ($C$) in seconds to meet the daily production quota.
2. Determine the theoretical minimum number of workstations ($N_{\min}$).
3. Group tasks into workstations using the Longest Task Time heuristic (ensuring precedence constraints are strictly honored).
4. Compute the actual Line Balancing Efficiency ($\eta$) and the Balance Delay (Idle Time Percentage).

---

### Step-by-Step Solution & Calculations

#### 1. Required Cycle Time ($C$)
The cycle time represents the maximum allowable time a unit may spend at any single workstation:
$$\text{Available Operating Time} = 8 \text{ hours} \times 3600 \text{ s/hour} = 28,800 \text{ seconds}$$
$$\text{Cycle Time } (C) = \frac{\text{Operating Time}}{\text{Production Volume}} = \frac{28,800 \text{ s}}{480 \text{ units}} = \mathbf{60.0 \text{ seconds/unit}}$$

#### 2. Theoretical Minimum Workstations ($N_{\min}$)
$$\sum t_i = 35 + 45 + 25 + 50 + 40 + 25 = 220 \text{ seconds}$$
$$N_{\min} = \left\lceil \frac{\sum t_i}{C} \right\rceil = \left\lceil \frac{220}{60} \right\rceil = \lceil 3.667 \rceil = \mathbf{4 \text{ workstations}}$$

#### 3. Line Balancing Assignment (Longest Task Time Heuristic)
Each workstation cannot exceed the maximum cycle time $C = 60\text{ seconds}$:

- **Workstation 1**:
  - Eligible tasks: A ($35\text{ s}$). Assign Task A.
  - Remaining time: $60 - 35 = 25\text{ s}$.
  - Eligible tasks with predecessors met: C ($25\text{ s}$) and B ($45\text{ s}$).
  - Only Task C fits ($25\text{ s} \le 25\text{ s}$). Assign Task C.
  - Workstation 1 contains: **Task A + Task C** $\implies \text{Total Time} = 35 + 25 = \mathbf{60\text{ s}}$ (Idle $= 0\text{ s}$).
- **Workstation 2**:
  - Eligible tasks: B ($45\text{ s}$). Assign Task B.
  - Remaining time: $60 - 45 = 15\text{ s}$. No eligible task fits in $15\text{ s}$.
  - Workstation 2 contains: **Task B** $\implies \text{Total Time} = \mathbf{45\text{ s}}$ (Idle $= 15\text{ s}$).
- **Workstation 3**:
  - Task B is complete; Task D is now eligible ($50\text{ s}$). Assign Task D.
  - Remaining time: $60 - 50 = 10\text{ s}$. No eligible task fits in $10\text{ s}$.
  - Workstation 3 contains: **Task D** $\implies \text{Total Time} = \mathbf{50\text{ s}}$ (Idle $= 10\text{ s}$).
- **Workstation 4**:
  - Tasks C and D are complete; Task E ($40\text{ s}$) is eligible. Assign Task E.
  - Remaining time: $60 - 40 = 20\text{ s}$. Task F requires $25\text{ s}$ ($> 20\text{ s}$), so Task F cannot fit into Workstation 4!
  - Workstation 4 contains: **Task E** $\implies \text{Total Time} = \mathbf{40\text{ s}}$ (Idle $= 20\text{ s}$).
- **Workstation 5**:
  - Assign Task F ($25\text{ s}$).
  - Workstation 5 contains: **Task F** $\implies \text{Total Time} = \mathbf{25\text{ s}}$ (Idle $= 35\text{ s}$).

*Actual Number of Workstations Assigned ($N_{\text{actual}}$)*: **5 workstations**.

#### 4. Line Balancing Efficiency & Balance Delay
$$\text{Line Efficiency } (\eta) = \frac{\sum t_i}{N_{\text{actual}} \times C} \times 100\% = \frac{220}{5 \times 60} \times 100\% = \frac{220}{300} \times 100\% = \mathbf{73.33\%}$$
$$\text{Balance Delay } (\text{Idle \%}) = 100\% - 73.33\% = \mathbf{26.67\%}$$

---

## Problem 2: Stochastic Inventory Management with Lead-Time Uncertainty

### Problem Statement
A regional distribution center distributes commercial industrial pumps. 
- Mean daily demand ($\bar{d}$): $50\text{ pumps/day}$ with standard deviation $\sigma_d = 10\text{ pumps/day}$.
- Supplier replenishment lead time ($\bar{L}$): $9\text{ days}$ with standard deviation $\sigma_L = 2\text{ days}$.
- Unit procurement cost ($C$): $₹8,000$ per pump.
- Fixed order placement & transit inspection cost ($S$): $₹3,600$ per order.
- Annual inventory carrying cost rate ($i$): $20\%$ of unit value per year ($H = 0.20 \times 8000 = ₹1,600/\text{unit/year}$).
- Operating days per year: $300\text{ days/year}$ (Annual Demand $D = 50 \times 300 = 15,000\text{ units/year}$).
- Target cycle service level: $98\%$ ($Z = 2.054$).

### Calculate:
1. The Economic Order Quantity ($Q^*$).
2. The Required Safety Stock ($SS$) considering joint demand and lead-time variability.
3. The Reorder Point ($ROP$).
4. Total Annual Inventory Cost (Ordering cost + Cycle stock holding cost + Safety stock holding cost).

---

### Step-by-Step Solution

#### 1. Economic Order Quantity ($Q^*$)
$$\text{EOQ } (Q^*) = \sqrt{\frac{2 D S}{H}} = \sqrt{\frac{2 \times 15,000 \times 3,600}{1,600}} = \sqrt{\frac{108,000,000}{1,600}} = \sqrt{67,500} \approx \mathbf{259.8 \implies 260 \text{ pumps}}$$

#### 2. Safety Stock ($SS$) with Joint Variability
The variance of demand during lead time when both demand and lead time are stochastic random variables is:
$$\sigma_{DL}^2 = \bar{L} \cdot \sigma_d^2 + \bar{d}^2 \cdot \sigma_L^2$$
$$\sigma_{DL}^2 = (9 \times 10^2) + (50^2 \times 2^2) = (9 \times 100) + (2500 \times 4) = 900 + 10,000 = 10,900$$
$$\sigma_{DL} = \sqrt{10,900} \approx 104.403 \text{ pumps}$$
$$\text{Safety Stock } (SS) = Z \times \sigma_{DL} = 2.054 \times 104.403 \approx \mathbf{214.4 \implies 215 \text{ pumps}}$$

> **Engineering Note**: Notice that lead-time uncertainty ($\bar{d}^2 \sigma_L^2 = 10,000$) contributes **over $91\%$** of the total variance, while daily demand uncertainty contributes only $900$ ($9\%$). In operations, stabilizing supplier lead times generates drastically higher inventory reductions than demand forecasting tweaks!

#### 3. Reorder Point ($ROP$)
$$\text{Expected Lead Time Demand} = \bar{d} \times \bar{L} = 50 \times 9 = 450\text{ pumps}$$
$$\text{ROP} = (\bar{d} \times \bar{L}) + SS = 450 + 215 = \mathbf{665 \text{ pumps}}$$

#### 4. Total Annual Inventory Cost ($TC$)
$$\text{Annual Ordering Cost} = \left(\frac{D}{Q^*}\right) S = \left(\frac{15,000}{260}\right) \times 3,600 = 57.69 \times 3,600 = ₹2,07,684$$
$$\text{Annual Cycle Stock Holding Cost} = \left(\frac{Q^*}{2}\right) H = \left(\frac{260}{2}\right) \times 1,600 = 130 \times 1,600 = ₹2,08,000$$
$$\text{Annual Safety Stock Holding Cost} = SS \times H = 215 \times 1,600 = ₹3,44,000$$
$$\text{Total Annual Cost } (TC) = 2,07,684 + 2,08,000 + 3,44,000 = \mathbf{₹7,59,684}$$

---

## Case Study: Six Sigma $C_{pk}$ Quality Turnaround in Precision Valves

### Situation
A precision hydraulics valve manufacturer experiences an alarming $8.2\%$ rejection rate on high-pressure piston diameters during customer incoming inspections. The design specification is $50.00\text{ mm} \pm 0.06\text{ mm}$ ($\text{LSL} = 49.94\text{ mm}, \text{USL} = 50.06\text{ mm}$). 
A statistical sample of 200 parts reveals:
- Current Process Mean ($\mu$): $50.025\text{ mm}$ (Mean has shifted upwards towards USL).
- Process Standard Deviation ($\sigma$): $0.020\text{ mm}$.

### 1. Process Capability Diagnostic
$$C_p = \frac{\text{USL} - \text{LSL}}{6\sigma} = \frac{50.06 - 49.94}{6 \times 0.020} = \frac{0.12}{0.12} = \mathbf{1.00}$$
$$C_{pk} = \min \left[ \frac{\text{USL} - \mu}{3\sigma}, \, \frac{\mu - \text{LSL}}{3\sigma} \right] = \min \left[ \frac{50.06 - 50.025}{0.06}, \, \frac{50.025 - 49.94}{0.06} \right] = \min [0.583, \, 1.417] = \mathbf{0.583}$$

**Finding**: While the process width is theoretically capable of achieving 3-sigma if perfectly centered ($C_p = 1.0$), the substantial mean shift ($\mu = 50.025$) produces a dismal $C_{pk} = 0.583$, causing heavy out-of-spec defects on the upper specification limit ($Z_{\text{upper}} = (50.06 - 50.025)/0.02 = 1.75\sigma \implies 4.01\%$ one-tail defect rate).

### 2. DMAIC Corrective Action Plan
1. **Define**: Target reducing valve diameter variance to achieve $C_{pk} \ge 1.50$ and zero customer rejections.
2. **Measure**: Instrument real-time CNC spindle temperature sensors and laser micrometers.
3. **Analyze**: Thermal expansion of the cutting tool during morning warmup caused the $0.025\text{ mm}$ upward mean drift.
4. **Improve**: Implement closed-loop coolant temperature regulation ($21^\circ\text{C} \pm 0.5^\circ\text{C}$) and re-center tool offset. Retrain machine to reduce vibration, lowering $\sigma$ from $0.020$ to $0.012\text{ mm}$.
5. **Control**: Post-intervention metrics: $\mu = 50.002\text{ mm}$, $\sigma = 0.012\text{ mm}$.
   $$C_{pk,\text{new}} = \min \left[ \frac{50.06 - 50.002}{0.036}, \, \frac{50.002 - 49.94}{0.036} \right] = \min [1.611, \, 1.722] = \mathbf{1.611} \quad (\text{Compliant})$$
