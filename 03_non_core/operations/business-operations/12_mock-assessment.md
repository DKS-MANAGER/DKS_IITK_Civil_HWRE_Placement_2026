# 12. Business Operations: Comprehensive Mock Assessment

> **Exam Focus**: Business Operations (BizOps) & Operational Excellence Assessment  
> **Target Audience**: IIT Kanpur students targeting non-core operations, BizOps, and marketplace strategy roles.  
> **Duration**: 60 Minutes  
> **Total Marks**: 50 Marks (Section A: 20 Marks, Section B: 20 Marks, Section C: 10 Marks)  
> **Rubric**: +2 for correct MCQ, -0.66 for incorrect; Stepwise evaluation for numericals and cases.

---

## Section A: Quantitative Process Modeling & Unit Economics (20 Marks)

### Q1. Flow Efficiency Calculation
A fintech platform processes merchant onboarding applications. The average application spends $4.5\text{ hours}$ in active document verification and background screening. However, due to queue wait times, batch approvals, and compliance review backlogs, the total elapsed time from merchant submission to account activation is $30.0\text{ hours}$. What is the flow efficiency of this onboarding process?
- **(a)** $12.5\%$
- **(b)** $15.0\%$
- **(c)** $22.5\%$
- **(d)** $85.0\%$

### Q2. Contribution Margin Waterfall
An on-demand grocery app reports the following monthly operational numbers:
- Gross Merchandise Value (GMV): $₹1,00,00,000$ (1 Crore) across $25,000\text{ orders}$ (AOV = $₹400$).
- Platform take rate / commission: $16\%$.
- Customer delivery fee collected: $₹20\text{ per order}$.
- Last-mile rider payout: $₹48\text{ per order}$.
- Payment gateway fee: $1.8\%$ of GMV.
- Packaging consumables: $₹5\text{ per order}$.
- Dark store variable labor: $₹12\text{ per order}$.
What is the net Contribution Margin 2 (CM2) per order?
- **(a)** $+₹10.80$
- **(b)** $+₹11.80$
- **(c)** $+₹21.80$
- **(d)** $-₹3.20$

### Q3. Little's Law in Customer Support Operations
A food delivery app's customer support chat operations has an arrival rate of $\lambda = 180\text{ tickets per hour}$. On average, each support ticket takes $W = 12\text{ minutes}$ to be resolved by an agent. Under steady-state conditions, what is the average number of active tickets ($L$) currently in the system (being handled or queued)?
- **(a)** $15\text{ tickets}$
- **(b)** $25\text{ tickets}$
- **(c)** $36\text{ tickets}$
- **(d)** $48\text{ tickets}$

### Q4. Takt Time Computation
A city sorting hub operates for two 8-hour shifts daily with 1 hour of total scheduled maintenance/breaks per shift ($14\text{ net productive hours per day}$). The hub is contracted to sort and dispatch $8,400\text{ parcels}$ every day to meet next-day delivery promises. What is the required Takt Time per parcel?
- **(a)** $4.0\text{ seconds}$
- **(b)** $6.0\text{ seconds}$
- **(c)** $8.5\text{ seconds}$
- **(d)** $12.0\text{ seconds}$

---

## Section B: Operational Case Diagnostics & Process Re-Engineering (20 Marks)

### Case Scenario: Ride-Hailing Driver Incentive & Cancellation Surge
In Metro City West, an online cab aggregator is experiencing a surge in driver cancellations. During morning peak hours ($08:00\text{ to }11:00$):
- Customer ride requests: $12,000\text{ requests/hour}$.
- Active drivers logged on: $8,000\text{ drivers}$.
- Match rate (rides accepted by a driver): $75\%$ ($9,000\text{ rides matched/hour}$).
- Driver cancellation rate after matching: $35\%$ ($3,150\text{ cancellations/hour}$).
- Customer cancellation rate due to ETA $> 12\text{ min}$: $20\%$ of remaining rides.
- Net fulfilled rides: $4,680\text{ rides/hour}$ (Fulfilled Demand Rate $= 39\%$).

### Candidate Tasks:
1. **Mathematical Breakdown (8 Marks)**: Calculate the revenue loss per hour during peak if the average fare is $₹300$ and the platform take rate is $22\%$.
2. **Root Cause Analysis (6 Marks)**: Present three distinct operational reasons why drivers cancel after accepting rides during peak hours.
3. **Operational Redesign (6 Marks)**: Propose a concrete BizOps intervention (combining dispatch algorithm tuning and incentive design) to increase the fulfilled demand rate to at least $60\%$.

---

## Section C: Service Level Agreement (SLA) & Incident Governance (10 Marks)

A 3PL logistics partner fails its On-Time In-Full (OTIF) delivery SLA of $98.0\%$, achieving only $91.5\%$ across 50,000 shipments in October.
1. Formulate a 3-tier escalation framework (Yellow, Orange, Red) with clear operational triggers and contractual penalty clauses.
2. Outline how you would establish automated daily tracking using SQL and dashboard alerts to detect SLA breaches within 2 hours of transit delays.

---

# Solutions, Worked Calculations & Scoring Rubric

---

### Solution Q1: Flow Efficiency Calculation
- **Correct Option: (b)** $15.0\%$
- **Calculation**:
  $$\text{Flow Efficiency} = \frac{\text{Value-Added Active Time}}{\text{Total Elapsed Lead Time}} \times 100\% = \frac{4.5\text{ hours}}{30.0\text{ hours}} \times 100\% = 0.15 \times 100\% = \mathbf{15.0\%}$$
- **Distractor Analysis**:
  - *(a) is wrong*: Took $(30 - 4.5)/30 = 85\%$ waste, then misapplied ratios.
  - *(d) is wrong*: $85.0\%$ is the non-value added waiting time percentage, not the flow efficiency.

---

### Solution Q2: Contribution Margin Waterfall
- **Correct Option: (b)** $+₹11.80$
- **Calculation**:
  - Commission revenue per order $= ₹400 \times 16\% = +₹64.00$
  - Customer delivery fee $= +₹20.00$
  - **Total Order Revenue** $= 64.00 + 20.00 = \mathbf{+₹84.00}$
  - Variable Costs per order:
    - Last-mile rider payout: $-₹48.00$
    - Payment gateway fee: $₹400 \times 1.8\% = -₹7.20$
    - Packaging: $-₹5.00$
    - Dark store labor: $-₹12.00$
  - **Total Variable Cost** $= 48.00 + 7.20 + 5.00 + 12.00 = \mathbf{₹72.20}$
  - **Net CM2 per order** $= 84.00 - 72.20 = \mathbf{+₹11.80}$
- **Distractor Analysis**:
  - *(a) is wrong*: Arithmetic error in subtracting payment gateway fee.
  - *(c) is wrong*: Forgot to deduct dark store labor.

---

### Solution Q3: Little's Law in Customer Support Operations
- **Correct Option: (c)** $36\text{ tickets}$
- **Calculation**:
  - Little's Law: $L = \lambda \times W$
  - Arrival rate: $\lambda = 180\text{ tickets/hour}$
  - Average time in system: $W = 12\text{ minutes} = \frac{12}{60}\text{ hours} = 0.20\text{ hours}$
  - Average inventory (active tickets):
    $$L = 180 \times 0.20 = \mathbf{36 \text{ tickets}}$$

---

### Solution Q4: Takt Time Computation
- **Correct Option: (b)** $6.0\text{ seconds}$
- **Calculation**:
  - Net operating time $= 14\text{ hours} = 14 \times 3600\text{ seconds} = 50,400\text{ seconds}$
  - Total customer demand $= 8,400\text{ parcels}$
  - Takt Time $= \frac{50,400\text{ seconds}}{8,400\text{ parcels}} = \mathbf{6.0 \text{ seconds/parcel}}$

---

### Solution Section B: Ride-Hailing Case Solution
1. **Financial Loss per Peak Hour**:
   - Total demand $= 12,000\text{ rides}$. Fulfilled demand $= 4,680\text{ rides}$.
   - Unfulfilled ride requests $= 12,000 - 4,680 = 7,320\text{ lost rides/hour}$.
   - Platform commission per ride $= ₹300 \times 22\% = ₹66.00$.
   - **Net Hourly Commission Loss** $= 7,320 \times ₹66 = \mathbf{₹4,83,120 \text{ per hour}}$.
   - Over a 3-hour peak, platform loses **₹14.49 Lakhs daily**.
2. **Root Cause Analysis**:
   - *Distance to Pickup*: Driver is matched to rider $3.5\text{ km}$ away without paid deadheading; driver calls rider, inquires destination, and cancels if unprofitable.
   - *Cash vs. Online Payment Preference*: High preference for cash fares due to daily fuel requirements.
   - *Traffic Gridlock at Pickup Point*: High wait time to reach customer exceeds initial estimated travel time.
3. **Operational Redesign**:
   - **Forward Dispatching**: Match drivers with customers who are within $1.0\text{ km}$ ($<4\text{ min}$ pickup ETA).
   - **Destination Transparency & Daily Goal Bonuses**: Show destination direction and reward drivers who maintain $<5\%$ cancellation with peak milestone incentives.
   - **Pickup Fee Allowance**: Compensate drivers $₹8/\text{km}$ for pickup distance beyond $1.5\text{ km}$ to eliminate reluctance to travel.

---

### Solution Section C: SLA Escalation Framework
- **Yellow Threshold ($95.0\%\text{--}97.9\%$ OTIF)**: Daily automated alert to 3PL operations lead; daily standup to reallocate line-haul trucks.
- **Orange Threshold ($92.0\%\text{--}94.9\%$ OTIF)**: Financial penalty of $2\%$ on monthly billing; platform reroutes $25\%$ of shipment volume to backup 3PL courier.
- **Red Threshold ($< 92.0\%$ OTIF)**: Immediate contractual breach; forfeiture of security deposit; platform freezes new shipment allocation until formal CAPA (Corrective and Preventive Action) review is cleared.
