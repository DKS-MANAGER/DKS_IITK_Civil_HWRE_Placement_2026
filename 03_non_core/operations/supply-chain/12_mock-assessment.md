# 12. Supply Chain Management: Comprehensive Technical Mock Assessment

> **Exam Focus**: Supply Chain Strategy, Inventory Optimization, Multi-Echelon Logistics & Network Design  
> **Target Audience**: IIT Kanpur candidates preparing for supply chain consulting, corporate logistics, and FMCG operations assessments.  
> **Duration**: 60 Minutes  
> **Total Marks**: 50 Marks (+2 for correct MCQ, -0.66 for incorrect; Full stepwise credit for analytical derivations).  
> **Calculators**: Scientific calculator permitted.

---

## Section A: Conceptual & Quantitative SCM MCQs (10 Marks)

### Q1. Square Root Law of Inventory Consolidation
A company currently operates 9 regional warehouses with an aggregate total safety stock across all 9 locations of $₹18\text{ Crores}$. If the company consolidates all operations into a single central national distribution center, assuming independent and identical demand distributions across all territories, what will be the new total required safety stock?
- **(a)** $₹2.0\text{ Crores}$
- **(b)** $₹6.0\text{ Crores}$
- **(c)** $₹9.0\text{ Crores}$
- **(d)** $₹12.0\text{ Crores}$

### Q2. The Bullwhip Effect Variance Ratio
In a 2-stage supply chain where the retailer updates demand forecasts using a simple moving average over $p = 4\text{ periods}$ and the order replenishment lead time from the manufacturer is $L = 2\text{ periods}$, what is the theoretical lower bound of the Bullwhip variance ratio $\dfrac{\sigma^2_{\text{orders}}}{\sigma^2_{\text{demand}}}$?
- **(a)** $1.25$
- **(b)** $2.00$
- **(c)** $2.50$
- **(d)** $3.25$

### Q3. Newsvendor Critical Fractile
A retailer purchases a seasonal gift item for $C = ₹600$ and sells it during Diwali for $P = ₹1,000$. Any unsold units at the end of the festive season are liquidated to a discounter for a salvage value of $V = ₹200$. What is the critical fractile ($CR$) that determines the optimal stock level?
- **(a)** $0.40$
- **(b)** $0.50$
- **(c)** $0.60$
- **(d)** $0.67$

### Q4. FTL vs. LTL Break-Even Economics
A dedicated 16-ton truck charter costs a flat rate of $₹48,000$ per trip between Chennai and Kolkata. An LTL freight carrier charges $₹4.00\text{ per kg}$ for consolidated parcel cargo. Above what shipment consignment weight does it become financially cheaper to book the dedicated FTL truck?
- **(a)** $8,000\text{ kg}$
- **(b)** $10,000\text{ kg}$
- **(c)** $12,000\text{ kg}$
- **(d)** $16,000\text{ kg}$

### Q5. Vendor Managed Inventory (VMI) Core Mechanism
In a true Vendor Managed Inventory (VMI) partnership between a manufacturer and an enterprise retailer:
- **(a)** The retailer places daily purchase orders based on their internal MRP algorithm.
- **(b)** The manufacturer monitors retailer point-of-sale inventory and autonomously decides replenishment timing and order quantities within agreed min-max stock bands.
- **(c)** The retailer assumes full financial ownership of all goods the moment they leave the manufacturer's factory gate.
- **(d)** The manufacturer pays a fixed penalty for every day inventory remains in the retailer's backroom.

---

## Section B: Analytical Calculations & Derivations (25 Marks)

### Problem 6: Multi-Echelon Safety Stock & Lead-Time Variance (15 Marks)
A retail chain distributes imported smartwatches through its regional hub.
- Mean daily customer demand ($\bar{d}$): $80\text{ units/day}$ with $\sigma_d = 15\text{ units/day}$.
- Supplier shipping lead time from overseas factory ($\bar{L}$): $25\text{ days}$ with standard deviation $\sigma_L = 5\text{ days}$.
- Target cycle service level: $95\%$ ($Z = 1.645$).
- Unit cost of smartwatch: $₹4,000$.
- Annual inventory carrying cost: $25\%$ per year ($H = 0.25 \times 4000 = ₹1,000/\text{unit/year}$).

#### Tasks:
1. Calculate the safety stock required under joint demand and lead-time uncertainty.
2. Determine what percentage of the total safety stock variance is driven by lead-time uncertainty versus demand uncertainty.
3. If the supply chain team signs an SLA with a premium air-freight carrier guaranteeing deterministic lead time ($L = 10\text{ days}, \sigma_L = 0$), calculate the new safety stock and the annual inventory holding cost saved.

### Problem 7: Newsvendor Optimal Order Quantity & Expected Profit (10 Marks)
A fashion apparel manufacturer is producing a limited-edition winter jacket.
- Unit production cost: $C = ₹1,800$.
- Retail selling price: $P = ₹3,800$.
- Salvage clearance price for unsold inventory: $V = ₹800$.
- Winter season demand is normally distributed with mean $\mu = 5,000\text{ jackets}$ and standard deviation $\sigma = 1,200\text{ jackets}$.
1. Compute the critical fractile and determine the optimal production quantity $Q^*$.
2. If the manufacturer conservatively decides to produce only the mean demand ($Q = 5,000$), calculate the probability of stocking out.

---

## Section C: Logistics Strategy & Distribution Architecture Case (15 Marks)

### Case: Omnichannel Fulfillment Network Redesign
A national retail brand with 300 physical department stores is launching an online direct-to-consumer (D2C) channel promising 2-day delivery across India.
The executive committee is debating two fulfillment strategies:
- **Strategy A (Store Fulfillment)**: Pick and ship e-commerce orders directly from the backrooms of the 300 existing physical retail stores.
- **Strategy B (Dedicated E-Commerce Fulfillment Centers)**: Build 3 dedicated, highly automated dark fulfillment centers located in Delhi NCR, Mumbai, and Bengaluru exclusively for online orders.

#### Candidate Tasks:
1. Compare Strategy A and Strategy B across: (i) Inventory holding costs, (ii) Store associate labor efficiency, (iii) Inventory visibility/accuracy, and (iv) Shipping transit costs.
2. Formulate a hybrid operating model that leverages physical stores as click-and-collect / returns hubs while retaining centralized fulfillment for online orders.

---

# Comprehensive Solutions, Calculations & Scoring Rubric

---

### Solution Q1: Square Root Law of Inventory Consolidation
- **Correct Option: (b)** $₹6.0\text{ Crores}$
- **Calculation**:
  $$I_{\text{central}} = \frac{I_{\text{total, decentralized}}}{\sqrt{N}} = \frac{₹18\text{ Crores}}{\sqrt{9}} = \frac{18}{3} = \mathbf{₹6.0 \text{ Crores}}$$
- **Distractor Analysis**:
  - *(a) is wrong*: Divided by $N = 9$ linearly ($18/9 = 2$), which would be cycle stock allocation, not safety stock risk pooling.
  - *(c) is wrong*: Assumed a $50\%$ reduction without square root math.

---

### Solution Q2: Bullwhip Effect Variance Ratio
- **Correct Option: (c)** $2.50$
- **Stepwise Calculation**:
  $$\frac{\sigma^2_{\text{orders}}}{\sigma^2_{\text{demand}}} \ge 1 + \frac{2L}{p} + \frac{2L^2}{p^2}$$
  - $L = 2$, $p = 4$.
  - First term: $\frac{2(2)}{4} = \frac{4}{4} = 1.0$.
  - Second term: $\frac{2(2^2)}{4^2} = \frac{2(4)}{16} = \frac{8}{16} = 0.50$.
  - Bullwhip Ratio $= 1 + 1.0 + 0.50 = \mathbf{2.50}$.
- **Distractor Analysis**:
  - *(b) is wrong*: Forgot the squared term $\frac{2L^2}{p^2}$.

---

### Solution Q3: Newsvendor Critical Fractile
- **Correct Option: (b)** $0.50$
- **Calculation**:
  - Cost of Underage ($C_u$): $P - C = 1,000 - 600 = ₹400$.
  - Cost of Overage ($C_o$): $C - V = 600 - 200 = ₹400$.
  - Critical Fractile:
    $$CR = \frac{C_u}{C_u + C_o} = \frac{400}{400 + 400} = \frac{400}{800} = \mathbf{0.50}$$
- **Distractor Analysis**:
  - *(a) is wrong*: Mistook $C_u / P$.
  - *(d) is wrong*: Inverted the formula.

---

### Solution Q4: FTL vs. LTL Break-Even Economics
- **Correct Option: (c)** $12,000\text{ kg}$
- **Calculation**:
  $$\text{Break-Even Weight} = \frac{\text{FTL Charter Cost}}{\text{LTL Rate per kg}} = \frac{₹48,000}{₹4.00/\text{kg}} = \mathbf{12,000 \text{ kg}}$$
- **Distractor Analysis**:
  - *(d) is wrong*: $16,000\text{ kg}$ is the maximum vehicle capacity, not the economic break-even point.

---

### Solution Q5: Vendor Managed Inventory
- **Correct Option: (b)**
- **Explanation**: In VMI, the supplier takes responsibility for maintaining agreed inventory levels at the customer's location, eliminating the traditional purchase-order cycle and dampening the bullwhip effect.

---

### Solution Problem 6: Multi-Echelon Safety Stock
1. **Joint Variance Calculation**:
   $$\sigma_{DL}^2 = \bar{L} \cdot \sigma_d^2 + \bar{d}^2 \cdot \sigma_L^2$$
   $$\sigma_{DL}^2 = (25 \times 15^2) + (80^2 \times 5^2) = (25 \times 225) + (6400 \times 25) = 5,625 + 160,000 = 165,625$$
   $$\sigma_{DL} = \sqrt{165,625} \approx 406.97 \text{ units}$$
   $$SS = Z \times \sigma_{DL} = 1.645 \times 406.97 \approx \mathbf{669.46 \implies 670 \text{ units}}$$
2. **Variance Contribution Breakdown**:
   - Lead time variance contribution: $\frac{160,000}{165,625} \times 100\% = \mathbf{96.6\%}$.
   - Daily demand variance contribution: $\frac{5,625}{165,625} \times 100\% = \mathbf{3.4\%}$.
   - Over $96\%$ of safety stock inventory is maintained solely because overseas shipping transit is unpredictable!
3. **Deterministic Lead Time ($L = 10, \sigma_L = 0$)**:
   $$\sigma_{DL,\text{new}} = \sigma_d \sqrt{L} = 15 \times \sqrt{10} = 15 \times 3.1623 = 47.43 \text{ units}$$
   $$SS_{\text{new}} = 1.645 \times 47.43 \approx \mathbf{78 \text{ units}}$$
   - Inventory units released: $670 - 78 = \mathbf{592 \text{ units}}$.
   - Annual Holding Cost Saved $= 592 \times ₹1,000 = \mathbf{₹5,92,000 \text{ per year}}$.

---

### Solution Problem 7: Newsvendor Production Sizing
1. **Optimal Order Quantity**:
   - $C_u = 3800 - 1800 = ₹2,000$.
   - $C_o = 1800 - 800 = ₹1,000$.
   - Critical Fractile:
     $$CR = \frac{2000}{2000 + 1000} = \frac{2000}{3000} = 0.6667$$
   - From standard normal inverse table: $\Phi(Z) = 0.6667 \implies Z \approx +0.431$.
   - Optimal Quantity:
     $$Q^* = \mu + Z \cdot \sigma = 5000 + (0.431 \times 1200) = 5000 + 517.2 = \mathbf{5,517 \text{ jackets}}$$
2. **Probability of Stockout at $Q = 5,000$**:
   - When ordering exactly the mean $\mu$, the $Z$-score is $0$.
   - For a symmetric normal distribution, $P(D > \mu) = \mathbf{50\%}$.
   - There is a massive **$50\%$ probability of stocking out** and losing sales during the winter peak!
