# Consulting & Digital Transformation Cases — Master Practice Suite

> **Document Focus**: End-to-end consulting case library tailored specifically to **Accenture Japan Digital Consultant** case interviews (`[JD VERIFIED]`).  
> **Role Alignment**: Business problem diagnosis, vendor-agnostic technology architecture, financial modeling, and change management.  
> **Classification Standard**: `[JD VERIFIED]` for role competencies; `[PREPARATION INFERENCE]` for case archetypes; `[HYPOTHETICAL PRACTICE]` for synthetic client figures and practice data.

---

## 🏛️ Pedagogical Framework: Solving Digital Consulting Cases

In traditional management consulting (strategy houses), case interviews focus primarily on market entry, mergers & acquisitions, or pure financial cost reduction.

At **Accenture Japan**, as a **Digital Consultant**, you are evaluated on your ability to connect **business strategy** directly with **technology execution**:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                 DIGITAL CONSULTING CASE METHODOLOGY ARCHITECTURE            │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. CLIENT CONTEXT & OBJECTIVE  ──► Clarify mandate, metrics, and timeline   │
│ 2. CLARIFYING QUESTIONS        ──► Uncover operational root causes & scope  │
│ 3. REASONED MECE ISSUE TREE    ──► Deconstruct into non-overlapping drivers │
│ 4. DATA & ASSUMPTIONS          ──► Extract quantitative baseline metrics    │
│ 5. STEP-BY-STEP CALCULATIONS   ──► Model financial impact, CapEx & OpEx     │
│ 6. EVIDENCE INTERPRETATION     ──► Diagnose core bottlenecks from numbers   │
│ 7. TECHNOLOGY ALTERNATIVES     ──► Compare AWS vs Azure vs Custom vs SaaS   │
│ 8. COSTS, BENEFITS & RISKS     ──► TCO, net ROI, payback, and mitigations   │
│ 9. IMPLEMENTATION ROADMAP      ──► Phased 12-to-24 month milestone rollout  │
│ 10. MEASURABLE KPIS            ──► Define leading & lagging success metrics │
│ 11. FINAL RECOMMENDATION       ──► Lead with answer via Pyramid Principle   │
│ 12. INTERVIEWER FOLLOW-UPS     ──► Defend against technical & partner push  │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🏭 CASE 1 — Industry X: Smart Factory IoT & Predictive Maintenance

* **Domain**: Industry X / Manufacturing Digitalization (`[JD VERIFIED]`)
* **Context**: `[HYPOTHETICAL PRACTICE]` Japanese Industrial Robotics Manufacturer

### 1. Client Context & Decision Objective
The client is a Tier-1 Japanese industrial robotics equipment manufacturer operating 4 assembly and machining plants across the Kanto and Kansai regions. Over the past two years, unexpected machine breakdowns on critical CNC lines and robotic welding cells have increased by 22%, causing JPY 450M in annual revenue losses, customer delivery penalties, and emergency repair overtime. The VP of Manufacturing has engaged Accenture Japan to design an **Industry X / IoT Predictive Maintenance Strategy** to cut downtime, improve plant OEE, and demonstrate a compelling ROI.

### 2. Clarifying Questions to Ask the Interviewer
1. *Is the breakdown concentrated on specific equipment types or distributed uniformly?*  
   **Interviewer response**: 75% of downtime originates from 120 critical high-precision CNC spindle machines and robotic arm joints.
2. *What is the current maintenance approach?*  
   **Interviewer response**: Purely reactive (repair after breakdown) with calendar-based semi-annual inspections.
3. *What are the factory network and cybersecurity constraints?*  
   **Interviewer response**: Operational Technology (OT) networks are air-gapped; any cloud connection must pass through an encrypted DMZ gateway complying with Japanese cybersecurity guidelines.

### 3. Reasoned MECE Issue Tree
```text
                            [JPY 450M Breakdown Loss]
                                       │
            ┌──────────────────────────┴──────────────────────────┐
            ▼                                                     ▼
   [Failure Prevention]                                  [Repair Efficiency]
            │                                                     │
   ┌────────┴────────┐                                   ┌────────┴────────┐
   ▼                 ▼                                   ▼                 ▼
[Real-Time Anomaly] [Predictive RUL]                   [Rapid Work Order] [Spare Parts Lead]
(Vibration/Temp)    (ML Degradation)                   (AR/Mobile Dispatch)(Auto Inventory)
```

### 4. Relevant Data & Assumptions (`[HYPOTHETICAL PRACTICE]`)
* Total annual breakdown loss: **JPY 450M/year**.
* Target machines: **120 critical machines** across 4 plants (30 per plant).
* Retrofit hardware cost: **JPY 500,000 per machine** (includes tri-axial vibration, infrared temperature, and acoustic sensors).
* Plant Edge Gateways: **JPY 5M per plant** (4 plants = JPY 20M).
* Central Cloud IoT Platform & ML Pipeline Development: **JPY 70M** (one-time CapEx).
* Annual Cloud Hosting & Support OpEx: **JPY 30M/year**.
* Expected downtime reduction: **70.0%**.

### 5. Step-by-Step Financial & Operational Calculations
1. **Total Initial Investment (CapEx)**:
   $$\text{Sensor Hardware} = 120 \times \text{JPY } 500,000 = \text{JPY } 60\text{M}$$
   $$\text{Edge Gateways} = 4 \times \text{JPY } 5\text{M} = \text{JPY } 20\text{M}$$
   $$\text{Platform & Model Development} = \text{JPY } 70\text{M}$$
   $$\text{Total CapEx} = 60\text{M} + 20\text{M} + 70\text{M} = \text{JPY } 150\text{M}$$
2. **Annual Financial Savings**:
   $$\text{Gross Annual Downtime Savings} = \text{JPY } 450\text{M} \times 70\% = \text{JPY } 315\text{M/year}$$
   $$\text{Net Annual Operating Benefit} = \text{JPY } 315\text{M} - \text{JPY } 30\text{M (OpEx)} = \text{JPY } 285\text{M/year}$$
3. **Payback Period & 3-Year ROI**:
   $$\text{Payback Period} = rac{\text{CapEx}}{\text{Net Annual Benefit}} = rac{\text{JPY } 150\text{M}}{\text{JPY } 285\text{M}} pprox 0.526\text{ years} pprox 6.3\text{ months}$$
   $$\text{3-Year Net Profit} = (3 \times \text{JPY } 285\text{M}) - \text{JPY } 150\text{M} = \text{JPY } 855\text{M} - 150\text{M} = \text{JPY } 705\text{M}$$
   $$\text{3-Year ROI} = rac{\text{JPY } 705\text{M}}{\text{JPY } 150\text{M}} \times 100\% = 470.0\%$$

### 6. Interpretation of Evidence
The data confirms that the client does not need to sensorize all 1,200 plant assets. Focusing on the 120 critical bottleneck machines (the top 10%) captures 75% of downtime risk, achieving an exceptional payback of ~6.3 months.

### 7. Technology & Architecture Alternatives
* **Alternative A (Full Cloud Streaming)**: Stream raw high-frequency vibration data (10 kHz) directly to AWS/Azure.  
  * *Verdict*: Rejected. Telemetry bandwidth would cost $> \text{JPY } 80\text{M/year}$ and violate air-gapped security latency constraints.
* **Alternative B (Hybrid Edge + Cloud Machine Learning — Recommended)**: Deploy edge industrial PCs running Fast Fourier Transform (FFT) algorithms locally to detect micro-anomalies in real-time ($<50\text{ ms}$). Transmit aggregated feature vectors (RMS, Peak, Kurtosis) every 5 minutes to Cloud Data Lake for predictive Remaining Useful Life (RUL) modeling.

### 8. Costs, Benefits & Risks
| Dimension | Findings | Mitigation Strategy |
| :--- | :--- | :--- |
| **Costs** | JPY 150M CapEx + JPY 30M/yr OpEx | Phased milestone releases tied to measurable plant savings. |
| **Benefits** | JPY 285M net annual savings; OEE improves from 72% to 85% | Re-invest savings into supply chain digital twins. |
| **Risks** | Shop floor technician resistance to tablet work orders | Conduct Kaizen co-design workshops; gamify compliance. |

### 9. Implementation Roadmap
* **Phase 1: Pilot Line (Months 1–3)**: Sensorize 30 machines on Plant 1's highest-risk CNC line; establish edge baseline.
* **Phase 2: Platform Integration (Months 4–7)**: Deploy cloud predictive models; integrate alerts with SAP Plant Maintenance (PM).
* **Phase 3: Nationwide Scale (Months 8–12)**: Roll out to remaining 3 plants; launch technician mobile workflow.

### 10. KPIs & Success Criteria
* **Leading**: Sensor data integrity $>99.8\%$; Mean Time To Detect (MTTD) anomaly $<15\text{ mins}$.
* **Lagging**: Unplanned downtime reduced by $\ge 70\%$; OEE $\ge 85\%$; Net annual savings $\ge \text{JPY } 280\text{M}$.

### 11. Final Recommendation (Pyramid Principle)
> *"We recommend the client invest JPY 150M in an Edge-Cloud Hybrid Predictive Maintenance architecture across 120 critical machines. This delivers JPY 285M in net annual savings with a 6.3-month payback and boosts plant OEE to 85%, supported by a 3-phase rollout over 12 months."*

### 12. Interviewer Follow-Up Questions & Model Answers
* **Q1**: *"What if the client's plant engineers distrust the AI's predictive failure alerts?"*  
  **Answer**: *"We institute a 'Human-in-the-Loop' transition period. For the first 90 days, the AI runs in advisory shadow mode alongside veteran technicians. Every alert presents explainable feature indicators (e.g., 'Spindle harmonic frequency exceeded threshold by 2.4x') rather than black-box scores, building operational trust before automating work order dispatches."*

---

## 🏦 CASE 2 — Cloud Migration: Legacy Mainframe to Hybrid Cloud

* **Domain**: Cloud Strategy & Enterprise Architecture (`[JD VERIFIED]`)
* **Context**: `[HYPOTHETICAL PRACTICE]` Tokyo Regional Commercial Bank

### 1. Client Context & Decision Objective
A Tokyo-based regional commercial bank processes retail and corporate banking transactions on an aging IBM z14 mainframe running legacy COBOL applications. Annual hardware maintenance, specialized COBOL contractor costs, and IBM MIPS software licenses exceed JPY 900M/year. The bank suffers a 4-month feature deployment cycle, lagging behind modern digital banks. The Board has commissioned Accenture Japan to evaluate migrating to a modern **Hybrid Multi-Cloud Architecture** compliant with Japanese Financial Services Agency (FSA) and Center for Financial Industry Information Systems (FISC) security standards.

### 2. Clarifying Questions to Ask
1. *What is the transaction volume and uptime SLA?*  
   **Interviewer**: 15 million daily transactions; mandatory 99.99% availability (maximum 52.56 mins downtime/year).
2. *Can the bank rewrite all COBOL applications from scratch?*  
   **Interviewer**: No. A complete Big-Bang rewrite carries unacceptable operational risk; business logic must be preserved or refactored incrementally.

### 3. Reasoned MECE Issue Tree
```text
                     [Modernization Strategy: Cost & Agility]
                                        │
             ┌──────────────────────────┴──────────────────────────┐
             ▼                                                     ▼
     [Technical Viability]                                  [Risk & Compliance]
             │                                                     │
    ┌────────┴────────┐                                   ┌────────┴────────┐
    ▼                 ▼                                   ▼                 ▼
[Core Re-platform] [Channel Microservices]              [FISC Security]   [Disaster Recovery]
(COBOL -> Linux)   (APIs on Kubernetes)                 (Dual Region)     (RPO=0, RTO<15m)
```

### 4. Relevant Data & Assumptions (`[HYPOTHETICAL PRACTICE]`)
* Current Mainframe Annual Operating Cost: **JPY 900M/year** (5-Year Baseline: **JPY 4.5B**).
* Modernization CapEx (3-year phased migration): **JPY 1,200M** (JPY 1.2B).
* Post-Migration Cloud OpEx (AWS/Azure Tokyo + Osaka dual-region): **JPY 350M/year**.
* Target 5-Year Net Cost Savings: $>30\%$.

### 5. Step-by-Step Financial & Architecture Calculations
1. **5-Year Total Cost Comparison**:
   $$\text{Baseline 5-Year Mainframe TCO} = 5 \times \text{JPY } 900\text{M} = \text{JPY } 4,500\text{M} \quad (\text{JPY } 4.5\text{B})$$
   $$\text{Modernized 5-Year Cloud TCO} = \text{CapEx } (1,200\text{M}) + [5 \times \text{OpEx } (350\text{M})] = 1,200\text{M} + 1,750\text{M} = \text{JPY } 2,950\text{M} \quad (\text{JPY } 2.95\text{B})$$
   $$\text{5-Year Net Financial Savings} = 4,500\text{M} - 2,950\text{M} = \text{JPY } 1,550\text{M} \quad (\text{JPY } 1.55\text{B})$$
   $$\text{Percentage Cost Reduction} = rac{1,550\text{M}}{4,500\text{M}} \times 100\% = 34.44\% pprox 34.4\%$$
2. **Break-even Payback Period**:
   $$\text{Annual OpEx Differential} = \text{JPY } 900\text{M} - \text{JPY } 350\text{M} = \text{JPY } 550\text{M/year}$$
   $$\text{Payback Period} = rac{\text{JPY } 1,200\text{M}}{\text{JPY } 550\text{M/year}} pprox 2.18\text{ years} \quad (pprox 26.2\text{ months})$$

### 6. Evidence Interpretation & Strategy
The financial payback of 2.18 years confirms strong commercial viability. However, executing a "Big Bang" migration would risk operational catastrophe. The recommended strategy is the **Strangler Fig Pattern**: extract peripheral customer-facing services (mobile banking, payments) into cloud microservices first, while keeping the core ledger stable.

### 7. Technology Alternatives & Architecture
* **Strategy Selected**: Hybrid Multi-Region Cloud (AWS Tokyo Primary + AWS Osaka DR, with Azure backup for reporting).
* **Core Ledger**: Containerized Linux re-platforming using Micro Focus / OpenShift, eliminating mainframe MIPS licensing.
* **API Layer**: Kong Enterprise API Gateway exposing RESTful endpoints, decoupling frontend apps from backend batch jobs.

### 8. Costs, Benefits & Risks
* **Benefits**: 34.4% cost savings (JPY 1.55B); release cycle accelerates from 4 months to 2 weeks.
* **Risks**: Data residency and FISC compliance audit failures.
* **Mitigation**: Dedicated AWS Direct Connect interconnects, Customer-Managed KMS encryption keys, and active-active data replication ensuring RPO = 0.

### 9. Implementation Roadmap
* **Year 1**: Establish Cloud Landing Zone; migrate internet banking frontends and reporting data warehouse.
* **Year 2**: Re-platform COBOL batch processing to Linux containers; implement dual-write transaction validation.
* **Year 3**: Cut over core transaction ledger; decommission mainframe hardware.

### 10. Success KPIs
* Availability: $\ge 99.99\%$; RPO: 0 seconds; RTO: $<15$ minutes; Deployment frequency: bi-weekly releases.

### 11. Final Recommendation
> *"Accenture Japan advises the bank to execute an incremental 3-year Strangler Fig cloud modernization. This achieves JPY 1.55B in 5-year net savings (34.4% reduction), cuts feature lead time to 2 weeks, and maintains 100% FISC compliance with an active-active Tokyo-Osaka disaster recovery topology."*

### 12. Interviewer Follow-Up Questions
* **Q1**: *"Why recommend AWS + Azure instead of a single cloud provider?"*  
  **Answer**: *"For a regulated financial institution in Japan, multi-cloud redundancy mitigates single-vendor lock-in and satisfies regulatory resilience audits under BOJ guidelines, while leveraging best-of-breed services (AWS for high-throughput transactional OLTP, Azure for enterprise analytics and PowerBI reporting)."*

---

## 📑 CASE 3 — Enterprise GenAI: Knowledge Retrieval & Policy Copilot

* **Domain**: AI, Generative AI & Knowledge Management (`[JD VERIFIED]`)
* **Context**: `[HYPOTHETICAL PRACTICE]` Japanese Major Life Insurance Provider

### 1. Client Context & Decision Objective
A leading life insurance enterprise in Tokyo with 12,000 agents and adjusters manages over 80,000 legacy PDF policy manuals, underwriting riders, and regulatory circulars. Claims adjusters in the complex claims review unit spend 3.5 hours per claim manually cross-referencing policy clauses, causing claims processing times of 14 days and leading to customer attrition. Management wants an **Enterprise RAG (Retrieval-Augmented Generation) Copilot** that reduces search time to minutes while ensuring zero customer PII leakage and strict legal accuracy.

### 2. Clarifying Questions to Ask
1. *How many complex claims are processed annually?*  
   **Interviewer**: 60,000 complex claims per year (5,000 per month).
2. *What is the fully burdened cost of claims adjusters?*  
   **Interviewer**: JPY 3,000 per hour.
3. *What are the hallucination tolerances?*  
   **Interviewer**: Zero tolerance for invented clauses. Every generated recommendation must cite the exact document name, version, and page number.

### 3. Reasoned MECE Issue Tree
```text
                     [GenAI RAG Solution Architecture]
                                     │
           ┌─────────────────────────┴─────────────────────────┐
           ▼                                                   ▼
 [Knowledge Ingestion & Vector Index]                [Governance & Security Guardrails]
           │                                                   │
   ┌───────┴───────┐                                   ┌───────┴───────┐
   ▼               ▼                                   ▼               ▼
[Chunking & OCR] [Hybrid Search (Dense+BM25)]       [PII Redaction]   [RBAC & Page Citations]
```

### 4. Relevant Data & Assumptions (`[HYPOTHETICAL PRACTICE]`)
* Complex claims volume: **60,000 claims/year** (5,000 claims/month).
* Search time per claim: Drops from **3.5 hours to 0.25 hours (15 mins)** -> Savings of **3.25 hours/claim**.
* Adjuster hourly rate: **JPY 3,000/hour**.
* Direct annual labor savings: $60,000 \times 3.25\text{ hrs} \times \text{JPY } 3,000 = \text{JPY } 585\text{M/year}$.
* Retained customer lifetime value from faster payout turnaround: **JPY 180M/year**.
* Total Gross Annual Benefit: $585\text{M} + 180\text{M} = \text{JPY } 765\text{M/year}$.
* Solution CapEx (OCR, Vector DB, embedding pipeline, UI integration): **JPY 160M**.
* Cloud GenAI Compute & Vector DB OpEx: **JPY 45M/year**.

### 5. Step-by-Step Financial & Technical Calculations
1. **Net Annual Financial Benefit**:
   $$\text{Net Annual Savings} = \text{JPY } 765\text{M} - \text{JPY } 45\text{M} = \text{JPY } 720\text{M/year}$$
2. **Payback Period**:
   $$\text{Payback Period} = rac{\text{JPY } 160\text{M}}{\text{JPY } 720\text{M/year}} \times 12\text{ months} pprox 2.67\text{ months} \quad (pprox 80\text{ days})$$

### 6. Evidence Interpretation
A payback under 3 months represents an exceptionally high-yield AI investment. The primary bottleneck is not LLM reasoning capability, but **document pre-processing quality** (handling scanned Japanese kanji PDFs and complex tables).

### 7. Technology Selection: RAG vs Fine-Tuning
* **Fine-Tuning Alone (Rejected)**: Static weights cannot update when policies change monthly; prone to hallucinations; impossible to cite exact page clauses.
* **Hybrid RAG Pipeline (Recommended)**:
  1. *Ingestion*: Layout-aware OCR (Azure AI Document Intelligence) parses tables and text.
  2. *Chunking*: Semantic chunking preserving section headers.
  3. *Indexing*: Azure AI Search combining **Vector Embeddings (Dense)** with **BM25 Keyword Search (Sparse)** and Cross-Encoder Re-ranking.
  4. *Generation*: GPT-4o with strict system prompt: *"Only answer using provided context. If unknown, state unverified. Always provide [DocID, Page#] citation."*

### 8. Implementation Roadmap
* **Months 1–2**: Data sanitization, OCR ingestion of top 10,000 active policies, vector indexing.
* **Months 3–4**: Pilot with 50 senior adjusters; evaluate recall, precision, and hallucination rates.
* **Months 5–6**: Roll out enterprise-wide to all 12,000 field personnel.

### 9. Success KPIs
* Claim research time reduced by $\ge 90\%$; Claim approval turnaround from 14 days to 48 hours; Citation accuracy: 100%.

### 10. Final Recommendation
> *"We recommend deploying an Enterprise Hybrid RAG Copilot with Azure AI Search and private LLM endpoints. At a CapEx of JPY 160M, the platform delivers JPY 720M in net annual value, pays back in 2.7 months, and compresses customer claims turnaround from 14 days to under 48 hours."*

### 11. Interviewer Follow-Up Questions
* **Q1**: *"How do you prevent Japanese PII (Personal Identifiable Information) from leaking into the AI?"*  
  **Answer**: *"We deploy an upstream PII anonymization gateway using Japanese Presidio / NER models. Names, My Number identifiers, and medical IDs are masked before vector embedding. Furthermore, data is hosted in tenant-isolated Japanese cloud regions with zero-data-retention agreements."*

---

## 🛍️ CASE 4 — Omnichannel Retail: POS & Supply Chain Synchronization

* **Domain**: Retail Digital Transformation & Real-Time Data Pipelines (`[JD VERIFIED]`)
* **Context**: `[HYPOTHETICAL PRACTICE]` Nationwide Japanese Convenience Store Chain (3,500 Stores)

### 1. Client Context & Decision Objective
A Japanese convenience store chain operates 3,500 franchise stores nationwide generating JPY 210B in gross sales. Due to overnight batch data synchronization, inventory records lag by up to 18 hours. Out-of-Stock (OOS) rates on high-margin fresh items during lunch peaks reach 8.5%, while end-of-day perishable food waste is 6.2%. Management wants an **Event-Driven Real-Time Omnichannel Architecture** to synchronize store POS terminals with regional distribution centers.

### 2. Relevant Data & Calculations (`[HYPOTHETICAL PRACTICE]`)
* Chain annual revenue: **JPY 210,000M (JPY 210B)**.
* Baseline OOS revenue loss (8.5% rate, 40% non-recovery): $210,000\text{M} \times 0.085 \times 0.40 = \text{JPY } 7,140\text{M/year}$.
* Baseline food waste loss: **JPY 4,200M/year**.
* Digital impact:
  * OOS rate reduced by 6.0 percentage points -> Recovers **JPY 5,040M/year**.
  * Dynamic demand forecasting cuts food waste by 40% -> Saves **JPY 1,680M/year**.
  * Total Gross Annual Gain: $5,040\text{M} + 1,680\text{M} = \text{JPY } 6,720\text{M/year}$.
* Platform Implementation CapEx (IoT scanners, Apache Kafka streaming, cloud inventory): **JPY 2,200M**.
* Annual Cloud & Support OpEx: **JPY 550M/year**.
* Net Annual Benefit: $6,720\text{M} - 550\text{M} = \text{JPY } 6,170\text{M/year}$.
* **Payback Period**: $rac{2,200\text{M}}{6,170\text{M}} \times 12 pprox 4.3\text{ months}$.

### 3. Architecture & Recommendation
* Replace nightly batch jobs with **Apache Kafka event streaming**. Every POS barcode scan triggers a real-time decrement event.
* Machine Learning dynamic replenishment models predict daily bento orders based on hyper-local weather, transit delays, and school events.
* Recommendation: Full rollout across 3,500 stores over 14 months, unlocking **JPY 6.17B in net annual operating profit**.

---

## 🚚 CASE 5 — Smart Logistics: Telematics & Fleet Route Optimization

* **Domain**: Mobility, IoT & Supply Chain Logistics (`[JD VERIFIED]`)
* **Context**: `[HYPOTHETICAL PRACTICE]` Japanese Express Parcel Courier Major

### 1. Client Context & Decision Objective
A Japanese logistics firm operates 8,500 delivery vans nationwide. Facing Japan's strict 2024 logistics labor reform laws (annual truck driver overtime capped at 960 hours) and an 18% fuel price surge, the firm struggles with driver shortages and a 14% package re-delivery rate. Management seeks an **IoT Telematics and Dynamic Route Dispatch System** to reduce mileage and eliminate illegal driver overtime.

### 2. Relevant Data & Calculations (`[HYPOTHETICAL PRACTICE]`)
* Annual fleet operational costs (fuel + maintenance): **JPY 8,500M**.
* Annual driver overtime payroll: **JPY 3,400M**.
* Operational improvements:
  * Dynamic routing cuts fleet mileage by 12% -> Fuel savings = $8,500\text{M} \times 0.12 = \text{JPY } 1,020\text{M/year}$.
  * Smart dispatch & customer time-window notifications cut driver overtime by 25% -> Overtime savings = $3,400\text{M} \times 0.25 = \text{JPY } 850\text{M/year}$.
  * Total Gross Annual Savings: $1,020\text{M} + 850\text{M} = \text{JPY } 1,870\text{M/year}$.
* IoT OBD Telematics hardware & Cloud optimization engine CapEx: **JPY 650M**.
* Ongoing cellular data & Cloud SaaS OpEx: **JPY 120M/year**.
* Net Annual Benefit: $1,870\text{M} - 120\text{M} = \text{JPY } 1,750\text{M/year}$.
* **Payback Period**: $rac{650\text{M}}{1,750\text{M}} \times 12 pprox 4.5\text{ months}$.

### 3. Recommendation
Retrofit 8,500 vans with IoT OBD dongles; integrate automated dispatch algorithms with LINE messaging for delivery pre-alerts. Achieves **JPY 1.75B net annual savings**, resolves driver overtime compliance, and pays back in 4.5 months.

---

## ⚡ CASE 6 — Green IT: Data Center PUE & Energy Optimization

* **Domain**: Sustainability, Cloud Infrastructure & Operational Efficiency (`[JD VERIFIED]`)
* **Context**: `[HYPOTHETICAL PRACTICE]` Japanese Tech Conglomerate Kanto Data Centers

### 1. Client Context & Decision Objective
A technology enterprise operates 3 enterprise data centers in the Kanto region consuming 120 GWh of electricity annually (annual utility bill JPY 3.6B at JPY 30/kWh). The conglomerate has committed to Japan's 2030 Green Transformation (GX) goals. The current Power Usage Effectiveness (PUE) is 1.65. Management needs a strategy to reduce PUE to $\le 1.25$ and lower carbon taxation liabilities.

### 2. Step-by-Step Numerical Calculations (`[HYPOTHETICAL PRACTICE]`)
1. **Deconstruct Energy Consumption**:
   $$\text{Total Facility Power} = 120.0\text{ GWh/year}$$
   $$\text{IT Equipment Power} = rac{120.0}{1.65} pprox 72.73\text{ GWh/year}$$
   $$\text{Cooling & Facility Overhead} = 120.0 - 72.73 = 47.27\text{ GWh/year}$$
2. **Target Energy at PUE = 1.25**:
   $$\text{New Total Facility Power} = 72.73\text{ GWh} \times 1.25 = 90.91\text{ GWh/year}$$
   $$\text{Annual Energy Saved} = 120.0 - 90.91 = 29.09\text{ GWh/year} \quad (24.24\%\text{ energy reduction})$$
3. **Financial Savings & Payback**:
   $$\text{Annual Electricity Savings} = 29,090,000\text{ kWh} \times \text{JPY } 30/\text{kWh} pprox \text{JPY } 872.7\text{M/year}$$
   $$\text{Optimization CapEx (AI airflow baffles, liquid cooling retrofits)} = \text{JPY } 750\text{M}$$
   $$\text{Sensor & Cloud Analytics OpEx} = \text{JPY } 50\text{M/year}$$
   $$\text{Net Annual Benefit} = 872.7\text{M} - 50\text{M} = \text{JPY } 822.7\text{M/year}$$
   $$\text{Payback Period} = rac{750\text{M}}{822.7\text{M}} \times 12 pprox 10.9\text{ months}$$

### 3. Recommendation
Deploy IoT temperature/pressure sensor grids across server racks combined with AI dynamic chiller control. Reduces facility energy by 24.2%, saves **JPY 822.7M net annually**, and achieves targeted PUE of 1.25 in 11 months.

---

## 🎯 Case Interview Performance Checklist

- [ ] Clarify client objective, time horizon, and target metrics within the first 60 seconds.
- [ ] Draw a structured 3-level MECE issue tree before performing any math.
- [ ] State formulas and assumptions clearly before multiplying numbers.
- [ ] Compare at least two technical architectures (e.g. Edge vs Cloud, RAG vs Fine-tuning).
- [ ] Conclude with the Pyramid Principle: Recommendation -> 3 Evidence Pillars -> Risks & Roadmap.
