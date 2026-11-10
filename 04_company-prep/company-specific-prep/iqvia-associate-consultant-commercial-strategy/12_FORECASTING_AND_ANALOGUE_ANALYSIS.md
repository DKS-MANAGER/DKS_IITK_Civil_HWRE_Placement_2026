# Module 12: Forecasting & Analogue Analysis in Commercial Strategy

> **Document Status**: Authoritative Strategy Reference `[TIER 1 / PROFORMA REQUIREMENT & TIER 2 / IQVIA CONSULTING PRACTICE]`  
> **Core Focus**: Patient-Based Epidemiology Forecasting, Bottom-Up Prescriber Models, Analogue Selection Criteria, S-Curve Calibration, and Sensitivity Tornado Models  
> **Target Role**: Associate Consultant (Commercial Strategy Consulting)  

---

## 1. Top-Down vs Bottom-Up Commercial Forecasting

In commercial strategy consulting, forecasting projects the 5-to-10 year unit volume (TRx) and net revenue trajectory for biopharmaceutical assets. The methodology chosen depends on product maturity:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 EPIDEMIOLOGY-BASED (TOP-DOWN) FORECASTING FLOW              │
│                                                                             │
│ [ Total National Population (e.g., US: 340 Million) ]                       │
│     │                                                                       │
│     ▼  x Disease Prevalence / Incidence Rate (%)                            │
│ [ Total Disease Population ]                                                │
│     │                                                                       │
│     ▼  x Diagnosis Rate (%)                                                 │
│ [ Diagnosed Patient Pool ]                                                  │
│     │                                                                       │
│     ▼  x Drug Treatment Rate (%)                                            │
│ [ Drug-Treated Patient Pool ]                                               │
│     │                                                                       │
│     ▼  x Clinical Sub-Pop / Biomarker Eligibility (%)                       │
│ [ Target Addressable Patient Population ]                                   │
│     │                                                                       │
│     ▼  x Brand Market Share Adoption Curve (%)                              │
│ [ Brand Treated Patients ]                                                  │
│     │                                                                       │
│     ▼  x Compliance Rate (PDC %)  x  Annual Net Realized Price ($/year)     │
│ [ FINAL ANNUAL NET BRAND REVENUE ]                                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Analogue Analysis: Calibrating the Launch Adoption Curve

When forecasting a pre-launch Phase II or Phase III asset, historical brand sales do not exist. Consultants calibrate forward-looking S-curves using **Historical Launch Analogues**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     ANALOGUE SELECTION CRITERIA MATRIX                      │
├────────────────────┬────────────────────────────────────────────────────────┤
│ Selection Pillar   │ Benchmark Matching Criteria                            │
├────────────────────┼────────────────────────────────────────────────────────┤
│ **1. Clinical**    │ • First-in-Class (Novel mechanism, requires physician  │
│ **Differentiation**│   education) vs Best-in-Class (Fast follower with      │
│                    │   proven superior safety or convenient oral dosing).   │
├────────────────────┼────────────────────────────────────────────────────────┤
│ **2. Disease &**   │ • Acute therapy (short course, hospital buy-and-bill)  │
│ **Patient Setting**│   vs Chronic maintenance (long-term specialty refills).│
├────────────────────┼────────────────────────────────────────────────────────┤
│ **3. Competitive** │ • Monopoly launch (uncontested space) vs Launching into│
│ **Crowdedness**    │   a duopoly vs Launching 4th in an established class.  │
├────────────────────┼────────────────────────────────────────────────────────┤
│ **4. Market Access**│ • Seamless Tier 2 preferred coverage vs Tier 3 with   │
│ **Hurdles**        │   mandatory step-therapy (slows adoption by 12–18 mos).│
└────────────────────┴────────────────────────────────────────────────────────┘
```

### 2.1 The Logistic S-Curve Formulation
Adoption over time $t$ (years post-launch) is modeled via the logistic adoption curve:
$$\text{Market Share}(t) = \frac{\text{Peak Share}}{1 + e^{-k(t - t_0)}}$$
* $\text{Peak Share}$: Maximum achievable market penetration (typically $20\text{–}45\%$ in competitive classes).
* $k$: Uptake velocity parameter (governed by sales rep detailing and KOL advocacy).
* $t_0$: Inflection point where uptake velocity is maximal (typically Year 2.5–3.5 post-launch).

---

## 3. Scenario Planning & Sensitivity Tornado Analysis

Because clinical and commercial environments are uncertain, consultants never present a single static forecast. We formulate three probabilistic scenarios:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 THE THREE PROBABILISTIC FORECAST SCENARIOS                  │
├────────────────────┬───────────┬────────────────────────────────────────────┤
│ Scenario           │ Weight    │ Commercial Assumptions                     │
├────────────────────┼───────────┼────────────────────────────────────────────┤
│ **Bull Case**      │ $25\%$    │ Superior Phase III OS; Tier 2 access with  │
│ (Upside)           │           │ zero step-therapy; Peak Share $= 40\%$.    │
├────────────────────┼───────────┼────────────────────────────────────────────┤
│ **Base Case**      │ $50\%$    │ Non-inferior efficacy, superior safety;    │
│ (Most Likely)      │           │ Moderate rebates ($45\%$ GTN); Share $= 25\%$.│
├────────────────────┼───────────┼────────────────────────────────────────────┤
│ **Bear Case**      │ $25\%$    │ Black-box safety warning; Tier 3 access;   │
│ (Downside)         │           │ Rival launches 6 months earlier; Share $= 12\%$.│
└────────────────────┴───────────┴────────────────────────────────────────────┘
```

### 3.1 Tornado Diagram Sensitivity Analysis
To identify which business variables have the largest impact on valuation, consultants calculate the net revenue sensitivity range when swinging each variable by $\pm 20\%$:
1. **Net Annual Price** ($\pm \$25,000$ swing): Generates a $\mathbf{\pm \$140\text{M}}$ revenue swing.
2. **Peak Market Share** ($\pm 5$ percentage points): Generates a $\mathbf{\pm \$95\text{M}}$ revenue swing.
3. **Patient Adherence / PDC** ($\pm 15\%$ compliance): Generates a $\mathbf{\pm \$48\text{M}}$ revenue swing.
4. **Diagnosis Rate** ($\pm 10\%$ diagnosed): Generates a $\mathbf{\pm \$28\text{M}}$ revenue swing.

> **C-Suite Recommendation**: Price realization and peak market share are the primary value drivers. Commercial teams should prioritize PBM rebate negotiations to secure Tier 2 access rather than spending heavily on early diagnostic screening campaigns.

