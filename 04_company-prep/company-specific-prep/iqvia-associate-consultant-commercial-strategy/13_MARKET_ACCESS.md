# Module 13: Market Access, Pricing & Reimbursement (P&R)

> **Document Status**: Authoritative Strategy Reference `[TIER 1 / PROFORMA REQUIREMENT & TIER 4 / HEALTH ECONOMICS STANDARDS]`  
> **Core Focus**: Health Economics & Outcomes Research (HEOR), QALY, ICER Formulations, PBM Formulary Tiers, and US vs European Reimbursement Architectures  
> **Target Role**: Associate Consultant (Commercial Strategy Consulting)  

---

## 1. What is Market Access in Life Sciences Consulting?

A pharmaceutical drug can achieve FDA approval with flawless clinical data, yet fail completely in the market if health insurance plans refuse to pay for it.

**Market Access** is the strategic discipline that ensures a novel therapy achieves favorable reimbursement, sustainable pricing, and minimal patient out-of-pocket financial barriers across commercial and public health plans:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    THE THREE PILLARS OF MARKET ACCESS                       │
├────────────────────┬────────────────────┬───────────────────────────────────┤
│ 1. PRICING         │ 2. REIMBURSEMENT   │ 3. PATIENT ACCESS                 │
├────────────────────┼────────────────────┼───────────────────────────────────┤
│ • List Price (WAC) │ • Coverage approval│ • Affordable out-of-pocket copays │
│ • Net Realized     │ • Formulary Tier   │ • Zero restrictive step-therapy   │
│   Price after PBM  │   placement (Tier2)│ • Smooth Prior Authorization (PA) │
│   rebates (GTN)    │ • HTA cost-benefit │ • Co-pay assistance card support  │
└────────────────────┴────────────────────┴───────────────────────────────────┘
```

---

## 2. Health Economics & Outcomes Research (HEOR) Foundations

### 2.1 Quality-Adjusted Life Years (QALY)
A composite measure of disease burden combining length of life gained with health-related quality of life (HRQoL):
$$\text{QALY} = \text{Life Years Gained} \times \text{Health Utility Weight } (u), \qquad u \in [0, 1]$$
* $u = 1.0$: Perfect health.
* $u = 0.0$: Death.
* *Example*: A novel oncology drug that extends a patient's life by 2.0 years at a quality-of-life utility of $0.75$ generates:
  $$\text{QALY} = 2.0 \times 0.75 = \mathbf{1.5 \text{ QALYs gained}}$$

### 2.2 Incremental Cost-Effectiveness Ratio (ICER)
The global gold standard metric evaluated by Health Technology Assessment (HTA) bodies:
$$\boxed{\text{ICER} = \frac{\text{Cost}_{\text{New Drug}} - \text{Cost}_{\text{Standard of Care}}}{\text{QALY}_{\text{New Drug}} - \text{QALY}_{\text{Standard of Care}}} = \frac{\Delta \text{Cost}}{\Delta \text{QALY}}}$$

* **Willingness-to-Pay (WTP) Statutory Thresholds**:
  * **United Kingdom (NICE)**: £20,000 to £30,000 per QALY gained. If $\text{ICER} > £30,000$, NICE rejects NHS coverage unless the manufacturer provides confidential discounts.
  * **United States (ICER Institute)**: \$100,000 to \$150,000 per QALY gained (non-binding benchmark).

---

## 3. Comparative Systems: United States vs European Market Access

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 US vs EUROPEAN HEALTHCARE MARKET ACCESS COMPARISON          │
├──────────────────────────┬──────────────────────────┬───────────────────────┤
│ Dimension                │ United States Multi-Payer│ Western Europe Single-Payer│
├──────────────────────────┼──────────────────────────┼───────────────────────┤
│ **Payer Landscape**      │ Fragmented: Commercial   │ Single National Authority│
│                          │ Insurers (50%), Medicare │ or Statutory Sickness │
│                          │ (20%), Medicaid (20%).   │ Funds (NHS, G-BA, HAS)│
├──────────────────────────┼──────────────────────────┼───────────────────────┤
│ **Launch Pricing**       │ **Free Market Pricing**: │ **Strictly Regulated**:│
│                          │ Manufacturer sets list   │ Mandatory statutory   │
│                          │ price (WAC) freely.      │ HTA cost-benefit caps │
├──────────────────────────┼──────────────────────────┼───────────────────────┤
│ **Formulary Gatekeepers**│ **Pharmacy Benefit Mgrs**│ **HTA Regulatory Bodies│
│                          │ (CVS Caremark, Express   │ (NICE, G-BA/IQWiG,    │
│                          │ Scripts, OptumRx).       │ HAS, AIFA).           │
├──────────────────────────┼──────────────────────────┼───────────────────────┤
│ **Price Concessions**    │ **Rebates & Discounts**: │ **Mandatory Discounts**:│
│                          │ Manufacturers pay 40–60% │ Clawbacks and external│
│                          │ GTN rebates for Tier 2.  │ reference pricing.    │
└──────────────────────────┴──────────────────────────┴───────────────────────┘
```

---

## 4. US Formulary Tiers & Payer Restrictions

In the United States, commercial health plans and PBMs sort drugs into four distinct formulary tiers:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          US FORMULARY TIER HIERARCHY                        │
├────────┬──────────────────────┬─────────────┬───────────────────────────────┤
│ Tier   │ Classification       │ Patient Pay │ Commercial Impact on Brand    │
├────────┼──────────────────────┼─────────────┼───────────────────────────────┤
│ Tier 1 │ Generic Drugs        │ $0–$10      │ Frictionless adoption; zero PA│
├────────┼──────────────────────┼─────────────┼───────────────────────────────┤
│ Tier 2 │ Preferred Brand      │ $25–$50     │ **Sweet Spot**: High volume;  │
│        │                      │             │ manufacturer pays moderate reb│
├────────┼──────────────────────┼─────────────┼───────────────────────────────┤
│ Tier 3 │ Non-Preferred Brand  │ $75–$125    │ Severe friction; step-therapy;│
│        │                      │             │ conversion drops by 40–50%    │
├────────┼──────────────────────┼─────────────┼───────────────────────────────┤
│ Tier 4 │ Specialty Biologics  │ 20%–33%     │ High coinsurance; specialty   │
│        │                      │ coinsurance │ pharmacy distribution required│
└────────┴──────────────────────┴─────────────┴───────────────────────────────┘
```

### 4.1 Utilization Management Tools: PA and Step-Therapy
* **Prior Authorization (PA)**: The physician must submit detailed medical records proving the patient meets strict clinical diagnostic criteria before the insurer will approve coverage.
* **Step-Therapy ("Fail First")**: The insurer requires the patient to try and clinically fail 1 or 2 cheaper generic medications before approving the expensive branded drug.

