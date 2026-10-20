# 07. Business Operations: Realistic Practice Cases & Solutions

> **Track**: Business Operations (BizOps) & Operational Excellence  
> **Target Audience**: IIT Kanpur candidates preparing for BizOps case interviews, take-home operational assignments, and problem-solving rounds.  
> **Structure**: Detailed business context, structured diagnostics, step-by-step mathematical calculations, and executive interview defenses.

---

## Case 1: Quick-Commerce Dark Store Hub Turnaround

### Business Situation
You are the BizOps Manager for a rapid delivery platform in Bengaluru. "Hub South-4" is missing its 10-minute delivery promise, with median order fulfillment times escalating to $16.4\text{ minutes}$. Customer churn in the catchment area has risen by $22\%$ month-over-month.

### Provided Hub Data
- Daily order volume ($D$): $2,400\text{ orders/day}$ over a 16-hour operating window ($06:00\text{ to }22:00$).
- Peak hours ($18:00\text{ to }22:00$): $40\%$ of daily orders ($960\text{ orders}$ over 4 hours $= 240\text{ orders/hour}$).
- Current hub layout: 2,500 sq.ft facility; 8 picking aisles; 4 packing stations.
- Active staff during peak hours: 6 Pickers and 4 Packers.
- Measured task benchmarks during peak:
  - Average picking time per order: $2.5\text{ minutes}$ ($0.0417\text{ hours}$).
  - Average packing, bagging & barcode scan time per order: $1.2\text{ minutes}$ ($0.020\text{ hours}$).
  - Average rider wait time outside hub: $6.8\text{ minutes}$.
  - Average rider transit time to customer doorstep: $5.5\text{ minutes}$.

---

### Step-by-Step Diagnostic & Mathematical Solution

#### 1. Capacity Bottleneck Identification
Let us calculate the theoretical hourly processing capacity of each operational stage during peak hours:

1. **Picking Capacity**:
   $$\text{Capacity}_{\text{pick}} = \frac{6 \text{ pickers} \times 60 \text{ min/hour}}{2.5 \text{ min/order}} = \frac{360}{2.5} = \mathbf{144 \text{ orders/hour}}$$
2. **Packing Capacity**:
   $$\text{Capacity}_{\text{pack}} = \frac{4 \text{ packers} \times 60 \text{ min/hour}}{1.2 \text{ min/order}} = \frac{240}{1.2} = \mathbf{200 \text{ orders/hour}}$$
3. **Incoming Peak Demand**:
   $$\text{Peak Demand} = \mathbf{240 \text{ orders/hour}}$$

**Diagnostic Finding**:
- The picking station is the **critical bottleneck**, capable of handling only $144\text{ orders/hour}$ against an arrival rate of $240\text{ orders/hour}$.
- Deficit rate: $240 - 144 = 96\text{ orders/hour}$. Over the 4-hour peak, a massive backlog of $384\text{ orders}$ accumulates, leading to escalating queues, rider idle wait times, and delayed deliveries.

#### 2. Process Optimization & Staff Rebalancing
To process $240\text{ orders/hour}$ without increasing head count:
1. **Batch Picking Implementation**:
   Currently, pickers execute single-order routing. Implement multi-order wave picking (2 orders per wave):
   - Walking time reduces by $40\%$.
   - New pick time per order $= 1.5\text{ minutes}$.
   - New picking capacity per worker $= 60 / 1.5 = 40\text{ orders/hour}$.
   - Number of pickers needed for 240 orders/hour $= 240 / 40 = \mathbf{6\text{ pickers}}$.
2. **Packing Streamlining**:
   - Automated barcode verification and pre-opened thermal delivery bags reduce packing time to $0.9\text{ minutes/order}$.
   - Capacity per packer $= 60 / 0.9 = 66.7\text{ orders/hour}$.
   - Number of packers needed for 240 orders/hour $= 240 / 66.7 = 3.6 \implies \mathbf{4\text{ packers}}$.
3. **Total Turnaround Impact**:
   - Picking time: $1.5\text{ min}$
   - Packing time: $0.9\text{ min}$
   - Rider dispatch staging: $0.8\text{ min}$
   - In-hub fulfillment time drops from $10.9\text{ min}$ to $\mathbf{3.2\text{ min}}$.
   - Adding transit time ($5.5\text{ min}$), total customer delivery time $= 3.2 + 5.5 = \mathbf{8.7\text{ minutes}}$ (Compliant with $<10\text{ min}$ SLA).

---

## Case 2: E-Commerce Marketplace Return-to-Origin (RTO) Reduction

### Business Context
An online fashion and lifestyle marketplace processes $50,000\text{ shipments/day}$. Cash-on-Delivery (COD) orders represent $60\%$ of total volume ($30,000\text{ orders/day}$). However, the Return-to-Origin (RTO) rate on COD orders is $28\%$ ($8,400\text{ returned orders/day}$), compared to only $6\%$ on prepaid orders ($1,200\text{ orders/day}$).

### Financial Parameters
- Average Order Value (AOV): $₹1,200$.
- Gross Margin on sold goods: $35\%$.
- Forward logistics cost per shipment: $₹65$.
- Reverse logistics & restocking cost per returned shipment: $₹75$.
- Packaging and transit damage loss per returned shipment: $₹40$.

---

### Quantitative Impact & Action Plan

#### 1. Baseline Financial Drain from COD RTO
Every returned order incurs logistics loss, reverse processing loss, and packaging write-offs without generating net revenue:
$$\text{Cost per RTO Shipment} = \text{Forward Shipping } (₹65) + \text{Reverse Shipping } (₹75) + \text{Damage & Repackaging } (₹40) = \mathbf{₹180 \text{ per RTO}}$$
$$\text{Daily RTO Cost} = 8,400 \text{ orders} \times ₹180 = \mathbf{₹15,12,000 \text{ per day}} \quad (\approx \mathbf{₹55.2 \text{ Crore/year}})$$

#### 2. Root Cause Segmentation
A Pareto audit of 1,000 failed COD deliveries reveals three primary causes:
1. **Customer Rejection at Doorstep / Impulsive Buyer Remorse**: $45\%$
2. **Incorrect / Incomplete Delivery Address & Geolocation Failure**: $35\%$
3. **Late Delivery Beyond Promised Date**: $20\%$

#### 3. Strategic Recommendations & Sensitivity
1. **Address Verification & WhatsApp Confirmation Engine**:
   - Automatically ping COD orders with high fraud risk scores using an address-cleansing API.
   - Require customer 1-click confirmation on WhatsApp before dispatch.
   - Expected reduction in address failure: $60\% \implies 0.35 \times 0.60 = 21\%$ total RTO reduction.
2. **Prepaid Conversion Incentives**:
   - Offer an instant ₹50 discount or UPI cashback if the user flips from COD to prepaid at checkout.
   - Cost of incentive $= ₹50$. Saved RTO cost $= ₹180$.
   - Net saving per converted order $= 180 - 50 = \mathbf{+₹130}$.
3. **RTO Target**:
   - Reducing COD RTO from $28\%$ to $18\%$ saves $3,000\text{ RTO orders/day}$.
   - Net daily cost savings $= 3,000 \times ₹180 = \mathbf{₹5,40,000 \text{ per day}}$ ($\mathbf{₹19.7 \text{ Cr annually}}$).

---

## Interview Defense & Follow-Up Questions

> **Q1**: *"If you add WhatsApp confirmation for COD orders, won't it add friction and reduce overall checkout conversion?"*  
> **Model Answer**: "Yes, introducing blanket friction lowers top-of-funnel conversion. Therefore, we do not apply WhatsApp verification universally. Instead, we deploy a machine-learning fraud scoring model based on user history, pincode risk, and order value. For trusted repeat customers (risk score $< 0.15$), the order bypasses verification instantly. Friction is directed selectively to unverified accounts, guest checkouts, and high-risk pincodes where the financial loss of RTO outweighs the small conversion drop."

> **Q2**: *"How would you measure whether driver incentive changes actually improved delivery times or just increased platform costs?"*  
> **Model Answer**: "We would run a geographically separated A/B test (cluster randomized trial across distinct delivery zones with comparable order density). In the test zones, we implement dynamic surge incentives tied strictly to SLA adherence during peak hours; the control zones maintain flat payouts. We evaluate the Difference-in-Differences (DiD) on three metrics: (1) Median Click-to-Deliver time, (2) Platform Delivery Cost per Order, and (3) Driver Churn/Retention rate."
