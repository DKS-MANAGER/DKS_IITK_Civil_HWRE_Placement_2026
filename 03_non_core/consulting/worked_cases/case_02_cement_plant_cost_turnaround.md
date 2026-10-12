# Worked Case 02: Cement Manufacturer Cost Turnaround & Lead Distance Optimization

> **Case Type**: Cost Reduction & Logistics Network Rationalization
> **Industry**: Heavy Building Materials

---

## Case 1: Indian Cement Manufacturer Regional EBITDA Recovery

### Problem Statement & Candidate Brief
> *“Our client is a top-5 cement manufacturer in India generating ₹12,000 Crore in annual revenue across four regional clusters. Over the past 18 months, their consolidated EBITDA margin declined from 22% to 14%, while industry peers maintained a stable 20% margin. The CEO has commissioned our team to diagnose the root cause and deliver a 12-month EBITDA recovery plan.”*

### Step 1: Clarification & Scoping Dialogue
- **Candidate**: *“Has this margin contraction occurred uniformly across all regions, or is it isolated to specific geographic clusters?”*  
  **Interviewer**: *“The client operates nationwide, but our internal financial audit reveals that 80% of the margin contraction is concentrated in the South India regional cluster.”*
- **Candidate**: *“In the South cluster, did top-line realization collapse due to a regional price war, or are operational and logistics costs escalating?”*  
  **Interviewer**: *“Average realized price in the South slipped only 4% (from ₹320 to ₹307 per 50kg bag), but total delivered cost per bag escalated by 16% (from ₹250 to ₹290 per bag). Focus your analysis on the cost drivers.”*

### Step 2: Cost Breakdown & Root Cause Isolation

```text
Cost Per 50kg Cement Bag (South India Cluster): ₹250 → ₹290 (+₹40 / +16%)
├── Raw Materials (Clinker & Gypsum): ₹80 → ₹82 (+₹2)
├── Power & Fuel (Kiln Thermal Energy): ₹65 → ₹85 (+₹20 / +30.8%) ◄── Key Driver 1!
├── Freight & Outbound Logistics: ₹60 → ₹76 (+₹16 / +26.7%) ◄── Key Driver 2!
└── Plant Fixed Overheads & Depreciation: ₹45 → ₹47 (+₹2)
```

#### Interviewer Data Releases:
1. **Power & Fuel Spike**: Due to domestic rail rake shortages from Coal India mines, the South manufacturing plant substituted domestic linkage coal with imported petroleum coke (petcoke). Concurrently, global benchmark petcoke prices surged 35%.
2. **Logistics Escalation**: To chase top-line volume growth, regional sales managers aggressively onboarded dealer accounts outside their natural economic freight radius. The average lead distance from plant to distributor expanded from **180 km to 310 km**.

### Step 3: Step-by-Step Mathematical Impact Calculation
- Southern regional cluster production volume = **15 Million Metric Tons (MMT) per year**.
- In standard packaging: 1 Ton = 20 bags (50 kg each) $\rightarrow 15\text{M Tons} \times 20 = \mathbf{300\text{ Million bags / year}}$.

1. **Annual Fuel Cost Escalation**:
   $$\Delta \text{Fuel Cost} = 300\text{M bags} \times ₹20/\text{bag} = \mathbf{₹600\text{ Crore INR / year}}$$
2. **Annual Logistics Freight Escalation**:
   $$\Delta \text{Freight Cost} = 300\text{M bags} \times ₹16/\text{bag} = \mathbf{₹480\text{ Crore INR / year}}$$
3. **Total Annual EBITDA Contraction in South Cluster**:
   $$\text{Total Cost Drag} = ₹600\text{ Cr} + ₹480\text{ Cr} = \mathbf{₹1,080\text{ Crore INR / year}}$$

### Step 4: Executive Recommendation & Turnaround Roadmap
> *“We recommend a three-pillar operational restructuring to recover **₹800 Crore in annual EBITDA** over 12 months:*  
> 1. **Freight Route Rationalization (Recovers ₹320 Cr)**: Terminate 120 unprofitable peripheral dealer contracts beyond 250 km; establish rail-linked grinding terminals to bring average lead distance back under 200 km.  
> 2. **Alternative Fuel & Raw Materials (AFR) Substitution (Recovers ₹300 Cr)**: Increase thermal substitution rate (TSR) to 15% using industrial hazardous waste, municipal refuse-derived fuel (RDF), and agricultural biomass, reducing dependence on imported petcoke.  
> 3. **Dynamic Regional Net-Realization Slabs (Recovers ₹180 Cr)**: Overhaul distributor rebate schemes to incentivize full truckload (FTL) orders and tie dealer discounts directly to delivered margin rather than gross volume.  
> *Key Implementation Risks: Temporary volume loss during dealer pruning; biomass seasonal price volatility during monsoon.*”

---

