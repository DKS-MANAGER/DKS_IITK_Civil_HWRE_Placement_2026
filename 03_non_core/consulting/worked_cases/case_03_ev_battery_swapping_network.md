# Worked Case 03: EV Two-Wheeler Battery Swapping Network Infrastructure

> **Case Type**: Market Entry, CapEx Modeling & Infrastructure Payback
> **Industry**: CleanTech Mobility & Energy

---

## Case 2: EV Battery Swapping Infrastructure Market Entry

### Problem Statement & Candidate Brief
> *“Our client is a major Indian renewable energy conglomerate with strong balance sheet capital. They are evaluating entering the Electric Vehicle (EV) battery swapping infrastructure market for commercial two-wheelers (E2W) and three-wheelers (E3W). The CEO wants to know: What is the addressable market size, what are the station-level unit economics, and should we enter?”*

### Step 1: Market Sizing (TAM for Commercial EV Swapping in Top-10 Metros)
1. **Target Fleet**: Commercial two-wheelers (food delivery, e-commerce couriers) and commercial three-wheelers (cargo and auto-rickshaws).
   - Commercial 2W & 3W addressable fleet by 2028 across top 10 Indian metros $\approx \mathbf{4.0\text{ Million vehicles}}$.
2. **Usage & Swapping Frequency**:
   - A commercial delivery driver covers ~120 km/day. Average battery range per swap = ~60 km.
   - Frequency = **2 battery swaps per day**.
   - Operating days = **300 days / year**.
   - Annual swaps per vehicle = $2 \times 300 = \mathbf{600\text{ swaps / vehicle / year}}$.
3. **Pricing Benchmark**:
   - Contractual swap fee = **₹90 per swap** (competitive with petrol operating cost of ₹2.2/km).
   - Annual revenue per vehicle = $600 \times ₹90 = \mathbf{₹54,000 / \text{vehicle / year}}$.
4. **Total Addressable Market (TAM)**:
   $$\text{TAM} = 4.0\text{ Million vehicles} \times ₹54,000/\text{year} = \mathbf{₹21,600\text{ Crore INR / year (\$2.6 Billion)}}$$

### Step 2: Station-Level Unit Economics & Payback Period (Bottom-Up)

#### Initial Capital Expenditure (CapEx per Kiosk):
- Automated 15-bay swapping cabinet: ₹4.5 Lakhs.
- 15 Lithium Iron Phosphate (LFP) 2kWh battery packs: $15 \times ₹40,000 = ₹6.0\text{ Lakhs}$.
- Grid transformer, metering, and civil setup: ₹1.5 Lakhs.
- **Total CapEx per Station** = **₹12.0 Lakhs**.

#### Operational Parameters & Daily Throughput:
- Battery capacity: 15 packs. Charge time from 0% to 100% = 2.0 hours.
- Maximum theoretical swaps per 24-hour cycle = $\frac{24}{2} \times 15 = 180\text{ swaps/day}$.
- Realistic operating utilization (target steady state) = 50% = **90 swaps / day**.

#### Annual Financials per Station:
1. **Annual Revenue**:
   $$\text{Revenue} = 90\text{ swaps/day} \times ₹90/\text{swap} \times 365\text{ days} = \mathbf{₹29.56\text{ Lakhs / year}}$$
2. **Annual Operating Expenses (OpEx)**:
   - **Electricity Cost**: 2 kWh per swap $\times 90\text{ swaps} \times ₹8/\text{kWh commercial tariff} \times 365\text{ days} = \mathbf{₹5.26\text{ Lakhs}}$.
   - **Battery Amortization / Reserve**: Batteries degrade over 1,500 full cycles. Battery replacement reserve fund $\approx \mathbf{₹6.50\text{ Lakhs/year}}$.
   - **Real Estate Lease (Footprint at Petrol Station / Metro Hub)**: ₹30,000/month = $\mathbf{₹3.60\text{ Lakhs/year}}$.
   - **Maintenance, IoT Telemetry & Insurance**: $\mathbf{₹2.00\text{ Lakhs/year}}$.
   - **Total Annual OpEx** = $5.26 + 6.50 + 3.60 + 2.00 = \mathbf{₹17.36\text{ Lakhs / year}}$.
3. **Station EBITDA & Payback**:
   $$\text{Annual Station EBITDA} = ₹29.56\text{ Lakhs} - ₹17.36\text{ Lakhs} = \mathbf{₹12.20\text{ Lakhs / year}}$$
   $$\text{Simple Payback Period} = \frac{\text{CapEx}}{\text{Annual EBITDA}} = \frac{₹12.00\text{ Lakhs}}{₹12.20\text{ Lakhs}} \approx \mathbf{0.98\text{ years (12 Months)}}$$

### Step 3: Strategic Recommendation & Entry Execution
- **Decision**: **Enter the market via a B2B anchor-tenant model**.
- **Execution Blueprint**:
  1. **Anchor Demand**: Secure multi-year fleet contracts with Swiggy, Zomato, and Amazon delivery partners before deploying kiosks, guaranteeing baseline 40% utilization from Day 1.
  2. **Real Estate Synergies**: Partner with state oil marketing companies (IOCL / HPCL) to lease existing forecourt land, avoiding standalone retail zoning permits.
  3. **Battery Standardization Risk**: Build multi-form-factor battery trays to support multiple vehicle OEMs and prevent lock-in to a single scooter manufacturer.

---

