# Worked Case 04: Quick-Commerce Dark Store Unit Economics & Route Batching

> **Case Type**: Platform Profitability & Last-Mile Delivery Density
> **Industry**: E-Commerce & Retail Logistics

---

## Case 3: Quick Commerce Grocery Platform Unit Economics Turnaround

### Problem Statement & Candidate Brief
> *“A venture-backed quick commerce grocery platform operates 250 micro-fulfillment centers ('dark stores') across Tier-1 Indian cities. While gross merchandise value (GMV) grew 80% year-on-year, the company is burning ₹12 Crore per month. The Board requires each dark store to reach operational contribution break-even within 6 months.”*

### Step 1: Baseline Dark Store Unit Economics (Current State)
- Average dark store metrics: **1,000 orders per day**.
- Average Order Value (AOV) = **₹320**.
- Product Gross Margin = 18% of AOV = **₹57.60**.
- Delivery / Convenience Fee Collected = **₹15.00**.
- **Total Revenue Inflow per Order** = $57.60 + 15.00 = \mathbf{₹72.60}$.

#### Cost Structure per Order:
- Dark store picking & packing staff (in-store labor): **₹25.00**.
- Last-mile rider payout (per drop): **₹55.00**.
- Store Fixed Overheads (₹6.6 Lakhs monthly rent, electricity, deep-freezers across 30,000 orders/month): **₹22.00**.
- Payment gateway & packaging bag: **₹5.00**.
- **Total Operating Cost per Order** = $25 + 55 + 22 + 5 = \mathbf{₹107.00}$.

#### Current Economic Deficit:
$$\text{Net Contribution per Order} = ₹72.60 - ₹107.00 = \mathbf{-₹34.40 \text{ (Loss per order)}}$$
$$\text{Annual Loss per Dark Store} = 1,000\text{ orders/day} \times (-₹34.40) \times 365 = \mathbf{-₹1.25\text{ Crore / store / year}}$$

### Step 2: Diagnostic Levers & Turnaround Math

```text
                                [Contribution Margin Turnaround]
                                                │
        ┌───────────────────────────────────────┴───────────────────────────────────────┐
        ▼                                                                               ▼
[AOV & Margin Expansion]                                                [Cost Density & Batching]
• Increase AOV: ₹320 → ₹450                                             • Route batching: 1.0 → 1.4 orders/trip
• Margin expansion: 18% → 22%                                           • Rider cost per order: ₹55 → ₹39
• Private label penetration & FMCG ads                                  • Dark store picker throughput
```

#### Step-by-Step Mathematical Bridge:
1. **AOV Expansion (₹320 $\rightarrow$ ₹450)**:
   - Introduce minimum order threshold of ₹199 for free delivery; deploy algorithmic cart upsells (beverages, snacks).
   - Higher AOV expands absolute gross profit: ₹450 at 22% margin (supported by private-label staples) = **₹99.00 gross profit per order** (+$41.40 gain).
2. **FMCG Brand Advertising Monetization**:
   - Charge consumer brands for sponsored search placement and sample distribution: Contributes **+₹8.00 per order**.
3. **Route Batching & Rider Density**:
   - Increase order density within a tight 2.0 km radius: Riders deliver 1.4 orders per trip instead of single orders.
   - Effective rider cost per order drops from ₹55.00 to $\frac{₹55}{1.4} = \mathbf{₹39.30}$ (saves ₹15.70).
4. **Dark Store Picking Optimization**:
   - Re-organize dark store layout by fast-moving SKU velocity: Picking time reduced from 180 seconds to 90 seconds, improving labor efficiency from ₹25.00 to **₹18.00 per order** (saves ₹7.00).

### Step 3: Revised Post-Turnaround Unit Economics

| Metric / Cost Element | Baseline State | Post-Turnaround Target | Variance per Order |
| :--- | :---: | :---: | :---: |
| **Average Order Value (AOV)** | ₹320.00 | **₹450.00** | +₹130.00 |
| **Product Gross Margin (22%)** | ₹57.60 | **₹99.00** | +₹41.40 |
| **Customer Delivery Fee** | ₹15.00 | **₹15.00** | — |
| **Retail Media Ad Revenue** | ₹0.00 | **₹8.00** | +₹8.00 |
| **Total Revenue per Order** | **₹72.60** | **₹122.00** | **+₹49.40** |
| Last-Mile Delivery Cost | -₹55.00 | -₹39.30 | +₹15.70 |
| Store Picking & Labor | -₹25.00 | -₹18.00 | +₹7.00 |
| Store Rent & Utilities (Fixed) | -₹22.00 | -₹22.00 | — |
| Packaging & Gateway | -₹5.00 | -₹6.00 | -₹1.00 |
| **Net Contribution per Order** | **-₹34.40** | **+₹36.70** | **+₹71.10 (Positive)** |

### Step 4: Executive Recommendation
- **Annual Financial Impact across 250 Stores**:
  $$\text{Net Annual EBITDA Swing} = 250\text{ stores} \times 1,000\text{ orders/day} \times 365\text{ days} \times (+₹71.10) \approx \mathbf{+₹648\text{ Crore INR}}$$
- The platform shifts from a monthly burn of ₹12 Crore to generating positive operational cash flow.

---

