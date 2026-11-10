# Module 15 — Market Sizing & Quantitative Consulting Cases

## 1. Consulting Market Sizing Philosophy in Life Sciences

In commercial strategy consulting at IQVIA, **Market Sizing (Guesstimation)** is not a trivia contest testing encyclopedic memorization of disease statistics. It evaluates:
1. **Structural Logic & MECE Architecture**: Can you break a messy, ambiguous real-world question into mutually exclusive, collectively exhaustive mathematical branches?
2. **Healthcare Intuition**: Do you grasp the critical distinctions between **Prevalence** (chronic stock) vs. **Incidence** (acute flow), diagnosed vs. undiagnosed fractions, drug-treated vs. lifestyle-managed patients, and Gross vs. Net pricing?
3. **Mental Math Fluency**: Can you perform rapid calculations under interview pressure without errors, rounding sensibly, tracking zeros, and retaining units?
4. **The Consulting "So-What"**: Do you conclude by interpreting the number for client strategy rather than just stating a bare dollar figure?

```
                    ┌──────────────────────────────────────────────┐
                    │           Healthcare Market Sizing           │
                    └──────────────────────┬───────────────────────┘
                                           │
                  ┌────────────────────────┴────────────────────────┐
                  ▼                                                 ▼
      ┌─────────────────────────┐                       ┌─────────────────────────┐
      │   Epidemiological Path  │                       │    Prescriber / Supply  │
      │       (Top-Down)        │                       │       (Bottom-Up)       │
      ├─────────────────────────┤                       ├─────────────────────────┤
      │ Total Population        │                       │ Total Target Prescribers│
      │   × Demographic Filter  │                       │   × Weekly Patient Vol  │
      │   × Disease Prevalence  │                       │   × Indication Share %  │
      │   × Diagnosis Rate %    │                       │   × Brand Adoption %    │
      │   × Treatment Rate %    │                       │   × Annual Value / Pt   │
      │   × Brand Share %       │                       │                         │
      │   × Net Price / Year    │                       │                         │
      └─────────────────────────┘                       └─────────────────────────┘
```

---

## 2. Core Mental Math & Estimation Techniques

### 2.1 The Consultant's Mental Arithmetic Toolkit
- **Factoring and Splitting**:
  $$72 \times 25 = 72 \times \frac{100}{4} = 18 \times 100 = 1,800$$
  $$14 \times 15 = 14 \times (10 + 5) = 140 + 70 = 210$$
- **Percentages via Decimals**:
  - $15\%$ of $80 \text{ M} = 0.10 \times 80 + 0.05 \times 80 = 8 + 4 = 12 \text{ M}$
  - $3.5\%$ of $400 \text{ M} = 3\% \times 400 + 0.5\% \times 400 = 12 + 2 = 14 \text{ M}$
- **Unit Dimensional Integrity**: Always explicitly carry units throughout every calculation:
  $$\text{Patients} \times \frac{\text{Vials}}{\text{Patient-Year}} \times \frac{\text{Net Price}}{\text{Vial}} = \frac{\text{Net Revenue}}{\text{Year}}$$

---

## 3. Standard Healthcare Demographic & Economic Benchmarks

Keep these foundational demographic anchor numbers committed to memory:

| Geography | Total Population | Age Distribution (<18 / 18–64 / 65+) | Healthcare Expenditure (% GDP) | Primary Payer Architecture |
| :--- | :--- | :--- | :--- | :--- |
| **United States** | **330 – 340 Million** (~335 M) | 22% / 60% / 18% (~60 M seniors) | ~18% of GDP (~$4.5 Trillion) | Multi-payer: Employer Commercial (50%), Medicare (18%), Medicaid (20%), Uninsured (8%) |
| **EU-5 (DE, FR, IT, ES, UK)** | **~325 Million** (DE 84M, UK 67M, FR 68M, IT 59M, ES 47M) | 17% / 61% / 22% (~70 M seniors) | ~10–12% of GDP | Single-payer / Statutory Health Insurance (SHI), Centralized HTA (G-BA, HAS, NICE) |
| **India** | **~1.40 Billion** (~1,400 M) | 26% / 67% / 7% (~100 M seniors) | ~3.0–3.5% of GDP (Public ~1.3%) | High Out-of-Pocket (OOP ~50%), Ayushman Bharat (PM-JAY), Private Health Insurance (rising) |

---

## 4. Six Fully Solved Life Sciences Market Sizing Cases

### Case 1: US Annual Market Size for First-Line (1L) Metastatic Non-Small Cell Lung Cancer (NSCLC) Immunotherapy

#### Problem Statement
A global biopharma client wants to estimate the total US addressable market (both eligible patient volume and total dollar revenue) for 1L PD-1/PD-L1 checkpoint inhibitor therapies in metastatic Non-Small Cell Lung Cancer.

#### Step-by-Step Top-Down Solution

```
US Population: 335,000,000
  │ (Incidence of Lung Cancer: ~70 per 100,000)
  ▼
Total Annual Incident Lung Cancer: 235,000 patients
  │ (Histology split: 85% Non-Small Cell Lung Cancer - NSCLC)
  ▼
Total NSCLC Patients: ~200,000 patients
  │ (Stage at diagnosis: 50% Stage IV Metastatic / De Novo Advanced)
  ▼
Metastatic NSCLC Patients: 100,000 patients
  │ (Actionable Genomic Mutations: EGFR/ALK/ROS1/BRAF = 25% → Treated with targeted TKIs)
  ▼
Mutation-Negative (Wild-Type) Candidate Pool: 75% = 75,000 patients
  │ (ECOG Performance Status 0–1 fit for systemic immunotherapy: 80%)
  ▼
Treated in First-Line (1L): 60,000 patients
  │ (Immunotherapy adoption: Monotherapy or Chemo-IO combo = 85%)
  ▼
Total 1L IO Patient Volume: 51,000 patients / year
```

#### Financial Sizing: Gross to Net Valuation
- **Standard Dosing**: 200 mg IV infusion every 3 weeks (Q3W) = 17 infusions per year.
- **Median Progression-Free Survival (PFS) / Duration of Therapy (DoT)**: In 1L metastatic NSCLC, average treatment duration is approximately 9 months (~13 infusions).
- **List Price (WAC)**: \$10,000 per 200 mg single-dose vial.
- **Net Price (after mandatory statutory rebates, 340B discounts, and commercial formulary concessions)**: 30% gross-to-net discount $\rightarrow$ Net Price = \$7,000 per infusion.
- **Annual Treatment Cost per Patient**:
  $$\text{Net Cost} = 13 \text{ infusions} \times \$7,000 = \$91,000 \approx \$90,000 \text{ per patient}$$
- **Total Addressable Market (TAM)**:
  $$\text{TAM} = 51,000 \text{ patients} \times \$90,000 = \$4,590,000,000 \approx \mathbf{\$4.6 \text{ Billion / year}}$$

#### Sanity Check & "So-What"
- **Sanity Check**: Keytruda (pembrolizumab) global sales are \$25B+, with US NSCLC accounting for ~$4–5B. Our estimate of \$4.6B aligns precisely with audited IQVIA sales data.
- **Consulting "So-What"**: The market is approaching therapeutic saturation (85% IO penetration). Any new entrant cannot rely on market expansion; they must capture share via biomarker sub-segmentation (e.g., TROP2 ADCs or bispecifics in PD-L1 negative cohorts) or superior toxicity profiles.

---

### Case 2: Indian Market Size for Continuous Glucose Monitors (CGM) in Diabetes

#### Problem Statement
A medical device manufacturer is considering launching a wearable sensor (Continuous Glucose Monitor, 14-day wear cycle) in India. What is the addressable annual revenue market?

#### Step-by-Step Solution

```
India Population: 1,400,000,000 (1.4 Billion)
  │ (Adult Population ≥ 20 years: ~65% = 910 Million)
  ▼
Adult Diabetic Prevalence: ~11% (ICMR-INDIAB study)
  ▼
Total Diabetic Population: ~100 Million
  │
  ├─► Type 1 Diabetes: 2% = 2.0 Million (Absolute insulin dependence)
  │     │ (Diagnosis & Access Rate: 40% = 800,000)
  │     ▼
  │   Affordable Urban Segment (Tier 1/2): 25% = 200,000 patients
  │
  └─► Type 2 Diabetes: 98% = 98.0 Million
        │ (Diagnosed fraction: 50% = 49 Million)
        │ (Insulin-dependent / Uncontrolled HbA1c > 9%: 15% = 7.35 Million)
        ▼
      Affordable Socioeconomic Segment (SEC A/B1, Out-of-Pocket capacity): 5% = 367,500 patients
```

#### Total Target Patient Pool
- Type 1 target patients: 200,000
- Type 2 intensive insulin target patients: ~370,000
- **Total Potential CGM User Pool**: $\approx 570,000 \text{ patients}$

#### Device Utilization & Pricing Dynamics
- **Adoption Rate**: CGM is premium cash-pay out-of-pocket in India. Assume 10% realistic penetration of this affluent cohort = 57,000 active users.
- **Usage Model**:
  - Full-time wear: 26 sensors/year (14 days each).
  - Intermittent/Holiday wear (common in India to save cost): ~6 sensors/year (1 sensor every 2 months for quarterly HbA1c review).
  - Weighted average utilization: 10 sensors/patient/year.
- **Sensor Pricing**:
  - Retail MRP: ₹4,000 per 14-day sensor.
  - Net Distributor / Manufacturer Selling Price: ₹2,500 per sensor.
- **Annual Market Valuation**:
  $$\text{Volume} = 57,000 \text{ users} \times 10 \text{ sensors/year} = 570,000 \text{ sensors}$$
  $$\text{Total Annual Market Value} = 570,000 \times ₹2,500 = \mathbf{₹142.5 \text{ Crore}} \approx \mathbf{\$17 \text{ Million USD}}$$

#### Consulting "So-What"
At \$17M, the current Indian CGM market is constrained by cash-pay affordability. Growth requires partnering with corporate wellness health insurance plans and packaging sensors with tele-endocrinology subscription services to demonstrate measurable HbA1c reduction.

---

### Case 3: Global Market Size for an Ultra-Rare Pediatric Enzyme Replacement Therapy (ERT)

#### Problem Statement
Size the global annual revenue opportunity for a breakthrough ERT treating a rare genetic lysosomal storage disorder with an incidence of 1 in 100,000 live births.

#### Step-by-Step Solution

```
Global Annual Births: ~130 Million
  │ (Incidence: 1 in 100,000 live births)
  ▼
Incident Patients Globally: 1,300 newborns / year
  │ (Target Geographies with Diagnostic & Reimbursement Infrastructure:
  │  US, EU, Japan, GCC, Select LatAm = ~20% of global births = 26M births)
  ▼
Incident Diagnosed Patients in Addressable Markets: 260 patients / year
  │ (Average Life Expectancy on ERT: 25 years → Steady-state prevalent pool)
  ▼
Total Prevalent Addressable Patient Pool: 260 × 25 years = 6,500 patients
  │ (Genetic confirmation and screening penetration: 70%)
  ▼
Active Diagnosed Patients: 4,550 patients
  │ (Treatment initiation rate: 90%)
  ▼
Treated Patient Population: ~4,100 patients globally
```

#### Orphan Drug Economics
- **Weight-Based Dosing**: Pediatric average weight transitions from 15 kg (toddler) to 50 kg (adolescent/adult). Mean treated weight $\approx 35 \text{ kg}$.
- **Annual Orphan Drug Net Price**: Ultra-rare orphan biologics are priced between \$300,000 and \$400,000 per patient per year in reimbursed markets.
- **Net Realized Price**: \$350,000 / patient / year.
- **Global Market Valuation**:
  $$\text{Global TAM} = 4,100 \text{ patients} \times \$350,000 = \mathbf{\$1.435 \text{ Billion / year}}$$

#### Consulting "So-What"
Despite tiny patient counts (4,100 patients globally), ultra-orphan pricing creates a \$1.4B commercial franchise. Commercial strategy hinges on **Universal Newborn Screening (NBS) panels**, specialized Center of Excellence (CoE) engagement, and dedicated Patient Support Programs (PSPs) guaranteeing zero out-of-pocket copay friction.

---

### Case 4: US Market Size for Hospital-Acquired Pneumonia (HAP) IV Antibiotic Infusions

#### Problem Statement
Size the annual US hospital inpatient market (volume of IV treatment courses and revenue) for a novel IV cephalosporin/beta-lactamase inhibitor targeting multidrug-resistant (MDR) *Pseudomonas aeruginosa* in Hospital-Acquired / Ventilator-Associated Bacterial Pneumonia (HABP/VABP).

#### Step-by-Step Solution

```
US Inpatient Admissions: ~35 Million / year
  │ (Patients acquiring Hospital-Acquired Infections - HAI: ~4% = 1.4 Million)
  ▼
HAI Cohort: 1,400,000
  │ (Proportion that are Pneumonia - HAP/VABP: ~25%)
  ▼
Total Annual US HAP/VABP Inpatients: 350,000 patients
  │ (Gram-negative bacterial etiology: 60%)
  ▼
Gram-Negative HAP/VABP Cases: 210,000
  │ (Pseudomonas aeruginosa involvement: 25%)
  ▼
P. aeruginosa Pneumonia Cases: 52,500
  │ (Multidrug-Resistant - MDR strain confirmed via microbiology: 30%)
  ▼
Target MDR P. aeruginosa Patient Pool: 15,750 patients / year
```

#### Hospital Inpatient Economics
- **Course of Therapy**: 14 days of IV infusion, 3 infusions per day (TID) = 42 vials per treatment course.
- **Inpatient Pricing Dynamic**: In the US, hospital inpatients are reimbursed under **Medicare MS-DRG (bundled payment)**. Hospitals view IV antibiotics as a cost center unless the drug qualifies for the **NTAP (New Technology Add-on Payment)** or DISARM Act incentives.
- **Acquisition Cost to Hospital**: \$300 per vial $\rightarrow 42 \text{ vials} \times \$300 = \$12,600$ per course.
- **Hospital Pharmacy & Therapeutics (P&T) Committee Restriction**: Reserved strictly for confirmed resistant cultures (3rd-line salvage therapy = 40% adoption).
- **Treated Courses**: $15,750 \times 40\% = 6,300 \text{ courses / year}$.
- **Total US Hospital Market Value**:
  $$\text{Revenue} = 6,300 \text{ courses} \times \$12,600 = \mathbf{\$79.38 \text{ Million}} \approx \mathbf{\$80 \text{ Million / year}}$$

#### Consulting "So-What"
Hospital IV antibiotic markets are severely constrained by bundled DRG reimbursement and antimicrobial stewardship restrictions. Commercial success requires securing NTAP hospital add-on payment status to neutralize the hospital pharmacy's budget penalty.

---

### Case 5: European Market for Robotic Surgical Assisted Systems (Capital + Consumables)

#### Problem Statement
Size the EU-5 annual market for robotic-assisted laparoscopic surgery across urology, gynecology, and general surgery.

#### Step-by-Step Solution

```
EU-5 Population: 325 Million
  │ (Major Acute Care Hospitals with > 300 surgical beds: ~2,500 hospitals)
  ▼
Robotic System Capital Penetration:
  │ (High-volume surgical centers acquiring robotic consoles: 40% = 1,000 centers)
  │ (Annual replacement & expansion install rate: 10% = 100 consoles / year)
  ▼
Console Capital Market:
  100 consoles × €1.5 Million / console = €150 Million / year

Capital Service Contracts:
  1,000 installed base × €150,000 annual maintenance SLA = €150 Million / year
```

#### Consumables / Procedure Instrumentation
- **Procedures per Console**: Average robotic console executes 200 procedures / year.
- **Total Procedures**: $1,000 \text{ consoles} \times 200 \text{ procedures} = 200,000 \text{ procedures / year}$.
- **Consumable Instruments per Procedure**: Robotic EndoWrist instruments, drapes, energy blades with strict 10-life limiters $\rightarrow €1,800$ per procedure.
- **Total Annual Consumable Market**:
  $$200,000 \text{ procedures} \times €1,800 = \mathbf{€360 \text{ Million / year}}$$
- **Total Annual Market Size (Capital + Service + Consumables)**:
  $$\text{TAM} = €150\text{M (Consoles)} + €150\text{M (Service)} + €360\text{M (Consumables)} = \mathbf{€660 \text{ Million / year}}$$

#### Consulting "So-What"
Robotic medtech operates on a "razor-and-blade" model: recurring revenue (service + consumables = €510M or 77% of total) dominates capital sales (€150M). A commercial consultant advises the client to offer flexible console leasing or volume-commitment placement models to accelerate hospital adoption.

---

### Case 6: Indian Annual Demand and Market Value for Seasonal Influenza Pediatric Vaccines

#### Problem Statement
Size the annual private commercial market in India for pediatric seasonal influenza quadrivalent vaccines (6 months to 5 years).

#### Step-by-Step Solution

```
India Annual Birth Cohort: ~25 Million
  │ (Pediatric Cohort aged 6 months to 5 years: ~4.5 birth years = ~112 Million)
  ▼
Total Eligible Pediatric Pool: 112 Million children
  │ (Urban Population Fraction: 35% = ~39 Million)
  ▼
Target Middle & High-Income Households (Private Pediatrician Visitations):
  │ (SEC A/B tier: 30% of urban children = ~11.7 Million)
  ▼
Pediatrician Influenza Vaccination Recommendation Rate:
  │ (IAP - Indian Academy of Pediatrics recommends annually, but uptake is selective: 25%)
  ▼
Annual Vaccinated Children: ~2.9 Million children / year
```

#### Dosage and Commercial Pricing
- **Dosage Schedule**:
  - First-time infants (<9 months): 2 doses (prime + boost).
  - Previously vaccinated / older children: 1 annual dose.
  - Weighted average doses per vaccinated child: 1.2 doses/year.
- **Total Dose Volume**: $2.9 \text{ Million} \times 1.2 = 3.48 \text{ Million doses / year}$.
- **Vaccine Commercial Pricing**:
  - Private Clinic MRP: ₹1,800 per pre-filled syringe (PFS).
  - Manufacturer Realized Price (ex-factory / distributor): ₹1,000 per dose.
- **Total Annual Market Value**:
  $$\text{Volume} \approx 3.5 \text{ Million doses / year}$$
  $$\text{Annual Value} = 3.5 \text{ Million} \times ₹1,000 = \mathbf{₹350 \text{ Crore}} \approx \mathbf{\$42 \text{ Million USD}}$$

---

## 5. Common Healthcare Sizing Pitfalls & Mitigation Strategies

```
┌─────────────────────────────────┬─────────────────────────────────┬─────────────────────────────────┐
│         Common Mistake          │        Underlying Flaw          │        Consulting Remedy        │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Confusing Incidence with        │ Multiplying chronic price by    │ Use INCIDENCE for acute events  │
│ Prevalence                      │ annual incident diagnoses only  │ (acute infections, new cancer). │
│                                 │ or vice versa.                  │ Use PREVALENCE for ongoing Rx.  │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Neglecting Compliance &         │ Assuming 100% of patients take  │ Apply PDC (Proportion of Days   │
│ Persistency (PDC)               │ medication 365 days a year.     │ Covered) or average 8–9 months  │
│                                 │                                 │ therapy duration.               │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Using List Price (WAC) Instead  │ Forgetting statutory and        │ Clarify gross vs. net. Biopharma│
│ of Net Realized Price           │ commercial rebates (340B, PBM). │ GTN discounts range 25% to 50%. │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ Ignoring Biomarker Segmentation │ Assuming all cancer patients are│ Filter for HER2, EGFR, KRAS,    │
│                                 │ eligible for targeted therapies.│ PD-L1 expression levels.        │
└─────────────────────────────────┴─────────────────────────────────┴─────────────────────────────────┘
```

---

## 6. Verbatim Candidate Delivery Script (Interviewer Simulation)

**Scenario**: The interviewer asks: *"Could you estimate the annual US market size for a new subcutaneous injectable biologic treating Severe Uncontrolled Eosinophilic Asthma?"*

> **Candidate Response (Verbatim Delivery)**:
> *"Thank you. To size this market accurately, I will structure my approach in four sequential steps:
> First, establish the US addressable patient funnel using an epidemiological top-down approach from total population to severe eosinophilic phenotype.
> Second, isolate the commercially addressable target pool by filtering for diagnosis, specialty care access, and biologic eligibility.
> Third, apply annual dosing compliance and net annual realized pricing to calculate total annual market revenue.
> Finally, I'll sanity check the number against known respiratory biologic benchmarks and discuss commercial implications.
> 
> Let's start with the patient funnel:
> - The US population is approximately 335 million.
> - Adult asthma prevalence in the US is roughly 8%, giving ~27 million asthmatic individuals.
> - Among all asthmatics, clinical literature suggests that approximately 5% to 10% suffer from severe, uncontrolled asthma despite high-dose ICS-LABA inhaler therapy. Taking 7.5%, that yields approximately 2 million severe uncontrolled asthma patients.
> - Within severe asthma, eosinophilic asthma—characterized by elevated blood eosinophil counts—represents about 50% to 60% of cases. Let's take 50%, which leaves us with a candidate pool of 1.0 million patients.
> 
> Now, let's filter for clinical accessibility:
> - Not all severe patients see a pulmonologist or allergist capable of prescribing specialty biologics. Assuming 40% access specialized respiratory care, that gives 400,000 patients.
> - Among those evaluated, commercial payer Prior Authorization criteria typically approve biologic initiation in about 50% of candidates, leaving 200,000 biologic-eligible, approved patients.
> 
> Regarding treatment economics:
> - Subcutaneous asthma biologics (like Fasenra, Nucala, or Dupixent) are dosed either monthly or every 8 weeks. Let's assume standard monthly dosing (12 injections/year).
> - Due to patient compliance, real-world persistence averages about 9 months of active therapy per year (75% compliance), or ~9 doses annually.
> - The net price per monthly pre-filled syringe after PBM statutory and commercial rebates is approximately $3,000 to $3,500. Let's use $3,000 net per syringe.
> - Annual treatment revenue per patient is therefore:
>   $$9 \text{ doses} \times \$3,000 = \$27,000 \text{ per patient-year}$$
> 
> Sizing the market:
> - Multiplying our 200,000 treated patients by $27,000 gives:
>   $$200,000 \times \$27,000 = \mathbf{\$5.4 \text{ Billion / year}}$$
> 
> Sanity Check & Strategic So-What:
> - Comparing this to industry benchmarks: The US severe asthma biologic category (Dupixent, Nucala, Fasenra, Tezspire) collectively generates ~$5–6B in US respiratory indications. Our estimate of $5.4B aligns closely with actual market revenues.
> - From a commercial strategy standpoint, because physician awareness is already high, a new entrant's primary challenge won't be market creation, but overcoming entrenched payer formulary exclusions and differentiation on dosing convenience (e.g., Q8W at-home autoinjector) or broader efficacy across non-eosinophilic subsets."*
