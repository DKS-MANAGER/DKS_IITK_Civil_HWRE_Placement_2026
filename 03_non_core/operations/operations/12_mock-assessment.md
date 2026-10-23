# 12. Operations Management: Comprehensive Technical Mock Assessment

> **Exam Focus**: Operations Research, Queueing Theory, Inventory Optimization & Six Sigma  
> **Target Audience**: IIT Kanpur candidates targeting plant operations, logistics management, and manufacturing leadership profiles.  
> **Duration**: 60 Minutes  
> **Total Marks**: 50 Marks (+2 for correct MCQ, -0.66 for incorrect; Full stepwise credit for analytical derivations).  
> **Calculators**: Scientific calculator permitted.

---

## Section A: Conceptual & Quantitative Operations MCQs (10 Marks)

### Q1. Bottleneck Identification & Line Capacity
A manufacturing process consists of five sequential workstations:
- Station 1: $12\text{ units/hour}$
- Station 2: $18\text{ units/hour}$
- Station 3: $9\text{ units/hour}$
- Station 4: $14\text{ units/hour}$
- Station 5: $16\text{ units/hour}$
If management invests $₹50\text{ Lakhs}$ to double the capacity of Station 3 to $18\text{ units/hour}$, what is the new overall maximum output capacity of the entire line?
- **(a)** $18\text{ units/hour}$
- **(b)** $14\text{ units/hour}$
- **(c)** $12\text{ units/hour}$
- **(d)** $16\text{ units/hour}$

### Q2. Economic Order Quantity (EOQ) Sensitivity
If annual demand for an industrial component quadruples ($4\times$) while the unit holding cost doubles ($2\times$) and the order placement cost remains unchanged, the new Economic Order Quantity ($Q^*_{\text{new}}$) will:
- **(a)** Remain completely unchanged.
- **(b)** Increase by a factor of $\sqrt{2} \approx 1.414$ ($41.4\%$ increase).
- **(c)** Double ($100\%$ increase).
- **(d)** Quadruple ($300\%$ increase).

### Q3. Single-Server Queueing Delay (M/M/1)
Trucks arrive at an unloading dock following a Poisson distribution at an average rate of $\lambda = 6\text{ trucks/hour}$. A single crew unloads trucks exponentially at an average rate of $\mu = 8\text{ trucks/hour}$. What is the average total time a truck spends at the dock (waiting in line + being unloaded)?
- **(a)** $15\text{ minutes}$
- **(b)** $30\text{ minutes}$
- **(c)** $45\text{ minutes}$
- **(d)** $60\text{ minutes}$

### Q4. Little's Law in Semiconductor Fabrication
A semiconductor cleanroom maintains an average Work-in-Progress (WIP) of $1,200\text{ silicon wafers}$. The mean cycle time for a wafer to complete all lithography and etching steps is $24\text{ days}$. What is the average daily throughput rate ($\lambda$) of the cleanroom at steady state?
- **(a)** $25\text{ wafers/day}$
- **(b)** $50\text{ wafers/day}$
- **(c)** $75\text{ wafers/day}$
- **(d)** $100\text{ wafers/day}$

### Q5. Process Capability ($C_{pk}$) Interpretation
A process has $\text{USL} = 105\text{ mm}$, $\text{LSL} = 95\text{ mm}$, process mean $\mu = 98\text{ mm}$, and process standard deviation $\sigma = 1.0\text{ mm}$. What is the value of $C_{pk}$?
- **(a)** $1.00$
- **(b)** $1.67$
- **(c)** $2.33$
- **(d)** $3.00$

---

## Section B: Analytical Problems & Derivations (25 Marks)

### Problem 6: Line Balancing & Station Assignment (15 Marks)
A consumer electronics manufacturer operates an assembly line with $C = 50\text{ seconds}$ cycle time. The line contains the following 7 elemental tasks:
- Task 1 ($30\text{ s}$), no predecessor.
- Task 2 ($20\text{ s}$), pred: 1.
- Task 3 ($25\text{ s}$), pred: 1.
- Task 4 ($15\text{ s}$), pred: 2.
- Task 5 ($30\text{ s}$), pred: 2.
- Task 6 ($20\text{ s}$), pred: 3, 4.
- Task 7 ($25\text{ s}$), pred: 5, 6.
1. Determine the theoretical minimum number of workstations ($N_{\min}$).
2. Assign tasks to workstations using the Ranked Positional Weight (RPW) or Longest Task Time heuristic.
3. Compute the line balancing efficiency and total idle time per unit.

### Problem 7: Safety Stock & Reorder Point Optimization (10 Marks)
A medical device distributor faces normally distributed daily demand with mean $\bar{d} = 120\text{ units/day}$ and standard deviation $\sigma_d = 20\text{ units/day}$. Replenishment lead time is constant at $L = 16\text{ days}$. 
1. Compute the safety stock required to achieve a $99\%$ cycle service level ($Z = 2.326$).
2. Determine the Reorder Point ($ROP$).
3. If the supplier introduces variable lead times ($\bar{L} = 16\text{ days}, \sigma_L = 3\text{ days}$), calculate the new safety stock and explain why it increases so dramatically.

---

## Section C: Operational Strategy & Executive Case (15 Marks)

### Case: Bottleneck Elevation in an E-Commerce Fulfillment Center
A fulfillment center experiences severe packing backlogs during festival sales. The warehouse manager proposes spending $₹80\text{ Lakhs}$ to add 10 automated packing machines.
1. As an Operations Specialist, outline the step-by-step diagnostic audit you must conduct *before* approving this capital expenditure.
2. How would you apply Goldratt’s "Subordinate" principle to ensure that upstream picking does not overwhelm the packing station and create chaotic floor congestion?
3. What KPIs would you track to confirm that total throughput increased rather than simply shifting the bottleneck to dispatch staging?

---

# Comprehensive Solutions & Marking Rubric

---

### Solution Q1: Bottleneck Identification
- **Correct Option: (c)** $12\text{ units/hour}$
- **Stepwise Explanation**:
  - Initial bottleneck was Station 3 ($9\text{ units/hour}$).
  - When Station 3 is upgraded from $9$ to $18\text{ units/hour}$, the capacities become:
    - Station 1: $12\text{ units/hour}$
    - Station 2: $18\text{ units/hour}$
    - Station 3: $18\text{ units/hour}$
    - Station 4: $14\text{ units/hour}$
    - Station 5: $16\text{ units/hour}$
  - The new minimum capacity is Station 1 ($12\text{ units/hour}$).
  - Therefore, the line throughput is capped at **$12\text{ units/hour}$**.
- **Distractor Analysis**:
  - *(a) is wrong*: Mistakenly assumed Station 2 or 3 dictated capacity.
  - *(b) is wrong*: Overlooked Station 1.

---

### Solution Q2: EOQ Sensitivity
- **Correct Option: (b)** Increase by a factor of $\sqrt{2} \approx 1.414$
- **Stepwise Derivation**:
  $$\text{EOQ} = \sqrt{\frac{2 D S}{H}}$$
  $$Q^*_{\text{new}} = \sqrt{\frac{2 (4D) S}{(2H)}} = \sqrt{\frac{4}{2}} \times \sqrt{\frac{2 D S}{H}} = \sqrt{2} \times Q^* \approx 1.414 \cdot Q^*$$

---

### Solution Q3: Single-Server Queueing Delay
- **Correct Option: (b)** $30\text{ minutes}$
- **Stepwise Derivation**:
  - $\lambda = 6\text{ trucks/hour}$, $\mu = 8\text{ trucks/hour}$.
  - System utilization: $\rho = \frac{\lambda}{\mu} = \frac{6}{8} = 0.75$.
  - Average total time in system ($W$):
    $$W = \frac{1}{\mu - \lambda} = \frac{1}{8 - 6} = \frac{1}{2} \text{ hours} = \mathbf{30 \text{ minutes}}$$
- **Distractor Analysis**:
  - *(a) is wrong*: Calculated average waiting time in queue $W_q = \frac{\rho}{\mu(1-\rho)} = \frac{0.75}{8(0.25)} = \frac{0.75}{2} = 0.375\text{ hours} = 22.5\text{ min}$, not total time.
  - *(c) is wrong*: Arithmetic confusion.

---

### Solution Q4: Little's Law in Semiconductor Fabrication
- **Correct Option: (b)** $50\text{ wafers/day}$
- **Calculation**:
  $$L = \lambda \times W \implies \lambda = \frac{L}{W} = \frac{1200\text{ wafers}}{24\text{ days}} = \mathbf{50 \text{ wafers/day}}$$

---

### Solution Q5: Process Capability ($C_{pk}$)
- **Correct Option: (a)** $1.00$
- **Calculation**:
  $$C_{pk} = \min \left[ \frac{\text{USL} - \mu}{3\sigma}, \, \frac{\mu - \text{LSL}}{3\sigma} \right] = \min \left[ \frac{105 - 98}{3(1.0)}, \, \frac{98 - 95}{3(1.0)} \right] = \min \left[ \frac{7}{3}, \, \frac{3}{3} \right] = \min [2.33, \, 1.00] = \mathbf{1.00}$$

---

### Solution Problem 6: Line Balancing & Station Assignment
1. **Total Task Time**: $\sum t_i = 30 + 20 + 25 + 15 + 30 + 20 + 25 = 165\text{ seconds}$.
   $$N_{\min} = \left\lceil \frac{165}{50} \right\rceil = \lceil 3.3 \rceil = \mathbf{4 \text{ workstations}}$$
2. **Workstation Assignments ($C = 50\text{ s}$)**:
   - *Station 1*: Task 1 ($30\text{ s}$) + Task 2 ($20\text{ s}$) $= \mathbf{50\text{ s}}$ (Idle $= 0\text{ s}$).
   - *Station 2*: Task 3 ($25\text{ s}$) + Task 4 ($15\text{ s}$) $= \mathbf{40\text{ s}}$ (Idle $= 10\text{ s}$).
   - *Station 3*: Task 5 ($30\text{ s}$) + Task 6 ($20\text{ s}$) $= \mathbf{50\text{ s}}$ (Idle $= 0\text{ s}$). (Predecessors for 6: Task 3, 4 completed in Station 2; Predecessor for 5: Task 2 completed in Station 1).
   - *Station 4*: Task 7 ($25\text{ s}$) $= \mathbf{25\text{ s}}$ (Idle $= 25\text{ s}$).
3. **Efficiency & Delay**:
   - Total Stations $= 4$ (Achieved theoretical minimum!).
   $$\text{Efficiency } (\eta) = \frac{165}{4 \times 50} \times 100\% = \frac{165}{200} \times 100\% = \mathbf{82.5\%}$$
   $$\text{Balance Delay} = 100\% - 82.5\% = \mathbf{17.5\%}$$

---

### Solution Problem 7: Safety Stock & Reorder Point Optimization
1. **Constant Lead Time Safety Stock**:
   $$SS = Z \times (\sigma_d \sqrt{L}) = 2.326 \times (20 \times \sqrt{16}) = 2.326 \times (20 \times 4) = 2.326 \times 80 = \mathbf{186.08 \implies 187 \text{ units}}$$
2. **Reorder Point**:
   $$\text{Expected Lead Time Demand} = \bar{d} \times L = 120 \times 16 = 1920\text{ units}$$
   $$\text{ROP} = 1920 + 187 = \mathbf{2,107 \text{ units}}$$
3. **Variable Lead Time Safety Stock**:
   $$\sigma_{DL} = \sqrt{L \cdot \sigma_d^2 + \bar{d}^2 \cdot \sigma_L^2} = \sqrt{(16 \times 20^2) + (120^2 \times 3^2)} = \sqrt{(16 \times 400) + (14400 \times 9)} = \sqrt{6400 + 129600} = \sqrt{136000} \approx 368.78$$
   $$SS_{\text{new}} = 2.326 \times 368.78 \approx \mathbf{857.8 \implies 858 \text{ units}}$$
   *Explanation*: Safety stock quadruples from $187$ to $858$ units because the uncertainty in supplier lead time is multiplied by the square of average demand ($\bar{d}^2 \sigma_L^2$), demonstrating why supplier reliability is paramount.
