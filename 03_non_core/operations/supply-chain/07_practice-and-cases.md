# 07. Supply Chain Management: Practice Cases & Solutions

> **Track**: Supply Chain Management (SCM) & Logistics Optimization  
> **Target Audience**: IIT Kanpur candidates preparing for supply chain consulting, corporate logistics, and distribution strategy interviews.  
> **Content Structure**: Multi-echelon network optimization, cold-chain logistics, risk-pooling derivations, and executive interview defenses.

---

## Case 1: Multi-Facility Warehouse Footprint Consolidation

### Strategic Context
A national consumer electronics brand currently operates $N_1 = 16\text{ decentralized regional warehouses}$ across India. While local delivery lead times are rapid ($1\text{ day}$), total inventory carrying costs and facility rent are severely eroding operating margins. 

The Chief Operating Officer (COO) commissions a network redesign study to evaluate consolidating the 16 regional warehouses into $N_2 = 4\text{ large regional mega-distribution centers}$ (North: NCR, West: Bhiwandi/Mumbai, South: Bengaluru, East: Kolkata).

### Operational & Financial Baseline Data
- Total average inventory held across all 16 existing warehouses: $₹320\text{ Crores}$ ($₹20\text{ Cr per warehouse}$).
  - Safety stock component: $₹120\text{ Crores}$ ($₹7.5\text{ Cr per warehouse}$).
  - Working cycle stock component: $₹200\text{ Crores}$ ($₹12.5\text{ Cr per warehouse}$).
- Annual inventory carrying cost rate ($i$): $18\%$ per year (capital interest, obsolescence, insurance, shrinkage).
- Warehouse fixed operating expense: $₹2.5\text{ Crores/year}$ per decentralized warehouse ($₹40\text{ Cr/year}$ across all 16 facilities).
- A mega-DC incurs higher automated lease costs: $₹6.5\text{ Crores/year}$ per mega-DC ($₹26\text{ Cr/year}$ across 4 mega-DCs).
- Outbound transportation freight:
  - Current decentralized freight cost: $₹45\text{ Crores/year}$ (short last-mile transit).
  - Consolidated 4-DC outbound freight cost: Expected to increase by $25\%$ due to longer delivery distances from mega-DCs to peripheral cities ($₹45 \times 1.25 = ₹56.25\text{ Cr/year}$).

---

### Quantitative Evaluation & Mathematical Derivations

#### 1. Inventory Savings via Risk Pooling (Square Root Law)
Assuming customer demand across regions is statistically independent and identically distributed:
$$I_{\text{consolidated}} = I_{\text{decentralized}} \times \sqrt{\frac{N_2}{N_1}} = I_{\text{decentralized}} \times \sqrt{\frac{4}{16}} = I_{\text{decentralized}} \times \sqrt{0.25} = 0.50 \times I_{\text{decentralized}}$$

1. **Safety Stock Impact**:
   - Initial Safety Stock across 16 hubs: $₹120\text{ Crores}$.
   - New Safety Stock across 4 mega-DCs:
     $$SS_{\text{new}} = ₹120\text{ Cr} \times \sqrt{\frac{4}{16}} = ₹120\text{ Cr} \times 0.50 = \mathbf{₹60 \text{ Crores}}$$
   - **Safety Stock Released**: $120 - 60 = \mathbf{₹60 \text{ Crores}}$ in working capital freed up!
2. **Cycle Stock Impact**:
   - Working cycle stock ($Q/2$) is driven by supplier batch delivery sizes. Because each mega-DC consolidates 4 regional demands, it can accept Full Truckload (FTL) shipments directly from factories without increasing overall cycle stock duration. Total cycle stock decreases modestly by $15\%$ through bulk replenishment:
     $$CS_{\text{new}} = ₹200\text{ Cr} \times 0.85 = \mathbf{₹170 \text{ Crores}}$$
3. **Total New Inventory**:
   $$I_{\text{new}} = SS_{\text{new}} + CS_{\text{new}} = 60 + 170 = \mathbf{₹230 \text{ Crores}} \quad (\text{Net reduction of } ₹90\text{ Cr})$$
4. **Annual Inventory Carrying Cost Savings**:
   $$\text{Annual Holding Savings} = (₹320\text{ Cr} - ₹230\text{ Cr}) \times 18\% = ₹90\text{ Cr} \times 0.18 = \mathbf{+₹16.20 \text{ Crores/year}}$$

#### 2. Warehouse Facility Fixed Cost Impact
- Current 16 warehouse leases: $16 \times ₹2.5\text{ Cr} = ₹40.00\text{ Cr/year}$.
- Proposed 4 mega-DC leases: $4 \times ₹6.5\text{ Cr} = ₹26.00\text{ Cr/year}$.
- **Net Facility Cost Savings**: $40.00 - 26.00 = \mathbf{+₹14.00 \text{ Crores/year}}$.

#### 3. Transportation Freight Penalty
- Additional outbound freight: $₹56.25\text{ Cr} - ₹45.00\text{ Cr} = \mathbf{-₹11.25 \text{ Crores/year}}$.

#### 4. Net Annual Financial Impact
$$\text{Net Annual Benefit} = \text{Holding Savings } (+16.20) + \text{Facility Savings } (+14.00) - \text{Freight Increase } (-11.25)$$
$$\text{Net Annual Benefit} = 16.20 + 14.00 - 11.25 = \mathbf{+₹18.95 \text{ Crores/year (Net Operating Profit Improvement)}}$$

**Executive Recommendation**:
Consolidate the network into 4 mega-DCs. In addition to delivering **₹18.95 Crores** in ongoing annual recurring EBITDA savings, the transition permanently unlocks **₹90 Crores of cash** from working capital.

---

## Case 2: Cold-Chain Logistics & Spoilage Mitigation in Dairy Supply Chain

### Business Context
A premium dairy brand distributes organic yogurt and milk cartons across 250 supermarket retail outlets in the National Capital Region (NCR). Product shelf-life is strictly $7\text{ days}$ under refrigerated cold-chain storage ($2^\circ\text{C}\text{--}4^\circ\text{C}$).

### Operational Problem
- Over the last two quarters, supermarket return and spoilage rates surged from $3.2\%$ to $9.8\%$, costing $₹42\text{ Lakhs/month}$ in destroyed inventory.
- Retailers complain that deliveries arrive warm during peak summer months.

### Quantitative Investigation & Root Cause Identification
A cross-functional supply chain audit tracking 50 refrigerated reefer delivery vans using IoT temperature loggers reveals three critical failure points:
1. **Pre-Cooling Protocol Failure**: $40\%$ of reefer vans were loaded immediately after turning on the chilling unit, before the cargo hold reached $4^\circ\text{C}$.
2. **Door Open Frequency**: Drivers open rear doors an average of 18 times during an 8-hour delivery route, with each door opening spiking interior air temperature by $3.5^\circ\text{C}$.
3. **Delivery Route Duration**: Unoptimized route sequencing causes peripheral stores to receive milk 7 hours after leaving the mother dairy.

### Implemented Interventions & Results
1. **Curtain Barrier & Multi-Chamber Van Partitioning**:
   - Installed PVC thermal strip curtains across rear doors, reducing ambient air intrusion by $65\%$.
2. **Dynamic Route Clustering & Night Dispatch**:
   - Shifted store deliveries from daytime traffic hours ($10:00\text{ to }18:00$) to early morning window ($03:00\text{ to }07:00$). Ambient road temperature is $10^\circ\text{C}$ cooler, and transit time dropped by $45\%$.
3. **IoT Real-Time Telemetry & Automated Driver Alerts**:
   - Drivers receive an automated haptic beep if cargo doors remain open for $> 90\text{ seconds}$.
- **Turnaround Metric**: Spoilage rate plummeted from $9.8\%$ to **$1.8\%$** within 60 days, recovering $₹34.3\text{ Lakhs/month}$ in gross profit.

---

## Interview Defense Questions & Follow-Up Probes

> **Q1**: *"In the 16-to-4 warehouse consolidation case, won't delivery times increase from 1 day to 2-3 days for peripheral tier-2 cities, potentially losing sales to local competitors?"*  
> **Model Answer**: "That is a valid strategic risk. To protect customer service levels, we must segment SKUs using an ABC/XYZ velocity matrix. Fast-moving 'A' items (which represent $75\%$ of volume but only $15\%$ of unique catalog items) can be stocked in small, forward cross-docking transit hubs near tier-2 cities using third-party logistics (3PL) on a pay-per-pallet basis. Slow-moving 'B' and 'C' long-tail items remain centralized at the 4 mega-DCs. This hybrid topology captures $80\%$ of the inventory consolidation savings while safeguarding same-day and next-day SLAs for high-demand products."

> **Q2**: *"Why does the Square Root Law assume independent demands? What happens if demands between regions are positively correlated?"*  
> **Model Answer**: "The Square Root Law derives from the statistical variance of sums: $\text{Var}(X_1 + \dots + X_N) = \sum \text{Var}(X_i) + 2 \sum \text{Cov}(X_i, X_j)$. If regional demands are completely independent ($\text{Cov} = 0$), the standard deviation scales as $\sqrt{N}$. However, if regional demands are strongly positively correlated ($\rho \to +1$, such as during a nationwide monsoon or macroeconomic recession), pooling offers zero diversification benefit, and total safety stock scales linearly ($N$) rather than by $\sqrt{N}$. Conversely, if demands are negatively correlated ($\rho < 0$), consolidation achieves even greater inventory savings than the square root rule predicts."
