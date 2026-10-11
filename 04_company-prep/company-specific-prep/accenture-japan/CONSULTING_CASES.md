# Consulting Cases, Issue Trees & Market Sizing — Master Practice Suite

> **Document Status**: Comprehensive Case Interview Practice Workbook  
> **Target Role**: Digital Consultant, Accenture Japan Ltd. (`[JD VERIFIED]`)  
> **Coverage**: 15 End-to-End Enterprise Digital Cases (10-Point Analysis Structure), 15 MECE Issue-Tree / Root-Cause Drills, and 10 Structured Market Sizing Guesstimates.  
> **Classification**: All corporate scenarios, client names, monetary sums, and operational metrics are explicitly `[PRACTICE ASSUMPTION]`.

---

## 1. The 14-Point Digital Case Interview Architecture

Every substantial case in this workbook follows the rigorous 14-point digital consulting analysis framework:

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        14-POINT DIGITAL CASE ANALYSIS FRAMEWORK                        │
├──────────────────────────┬──────────────────────────┬──────────────────────────────────┤
│ 1. Candidate Prompt      │ 2. Context & Objectives  │ 3. Clarifying Questions & Why    │
│ 4. Issue Tree Structure  │ 5. Assumptions vs Facts  │ 6. Exhibits & Numerical Data     │
│ 7. Step-by-Step Math     │ 8. Alternative Explanations│ 9. Multiple Feasible Solutions │
│ 10. Trade-Off Comparison │ 11. Recommended Solution │ 12. Risks, Stages & KPIs         │
│ 13. Interviewer Q&A      │ 14. Transparent Rubric   │                                  │
└──────────────────────────┴──────────────────────────┴──────────────────────────────────┘
```

---

## 2. Solved Digital Transformation Cases (Full 14-Point Depth)

### Case 1: Industry X — Smart Factory Transformation for a Japanese Robotics Manufacturer

1. **Candidate-Facing Prompt**:
   *"Our client is a premier Japanese industrial robotics and precision component manufacturer operating 4 production facilities in the Kanto region. Over the past 24 months, unplanned machine downtime has surged by 22%, causing approximately JPY 450 Million in annual lost gross margin and delivery penalties to automotive clients. The CEO has engaged Accenture Japan to diagnose the root cause, evaluate technology options, and present a digital modernization roadmap to eliminate unplanned downtime."*
2. **Business Context & Objective**:
   * **Context**: Mid-sized specialized supplier facing rising raw material costs and acute skilled technician shortages in Japan.
   * **Objective**: Reduce unplanned machine downtime by at least $60\%$, lift Overall Equipment Effectiveness (OEE) from $72\%$ to $\ge 82\%$, and achieve positive financial payback within 12 months.
3. **Clarifying Questions (and Why They Matter)**:
   * *Question 1*: "What is the current machine maintenance regime — purely reactive run-to-failure or calendar-based preventive?"  
     *Why it matters*: Distinguishes whether the failure is organizational scheduling or lack of physical asset condition visibility.
   * *Question 2*: "Are the 200 production machines homogeneous or a mix of modern and legacy vintage?"  
     *Why it matters*: Determines sensor connectivity feasibility (modern OPC-UA bus vs legacy machines requiring non-invasive clip-on sensors).
   * *Question 3*: "What is the breakdown between Mean Time Between Failures (MTBF) and Mean Time to Repair (MTTR)?"  
     *Why it matters*: Isolates whether the primary bottleneck is failure frequency or prolonged repair duration due to spare-part logistics.
4. **Issue Tree & Problem Decomposition**:
   ```text
   TOTAL DOWNTIME LOSS (JPY 450M)
   ├── 1. Breakdown Frequency (MTBF = 340 hrs)
   │   ├── Spindle bearing friction & thermal expansion (65% of premature failures)
   │   ├── Coolant line blockage & pressure drop (20%)
   │   └── Electrical power supply & motor surges (15%)
   └── 2. Repair Duration (MTTR = 14 hrs/incident)
       ├── Detection & Diagnostic Latency (avg 3.5 hrs before technician arrives)
       ├── Spare Parts Procurement Latency (avg 7.0 hrs waiting for warehouse retrieval)
       └── Mechanical Repair & Recalibration (avg 3.5 hrs physical wrench time)
   ```
5. **Candidate Assumptions vs Supplied Facts**:
   * *Supplied Facts*: 4 plants; JPY 450M annual loss; 22% downtime surge; current OEE is 72%.
   * *Candidate Assumptions*: 200 total CNC machines; 50 mission-critical bottleneck machines on main lines; average technician labor rate JPY 5,000/hr; 250 production days/year.
6. **Numerical Exhibit (`[PRACTICE ASSUMPTION]` Exhibit 1.1)**:
   * Total machines: 200 units across 4 plants.
   * Annual operating hours per machine: $250\text{ days} \times 16\text{ hrs} = 4,000\text{ hours}$.
   * Total machine hours: $200 \times 4,000 = 800,000\text{ machine-hours/year}$.
   * Breakdown downtime: $5.5\%$ of operating hours $= 44,000\text{ lost machine-hours}$.
   * Financial impact: $\text{JPY } 450,000,000 / 44,000\text{ hrs} \approx \mathbf{\text{JPY } 10,227\text{ lost margin per machine-hour}}$.
7. **Step-by-Step Calculations & Interpretation**:
   * **Failure Reduction Benefit**:
     * Deploying IoT vibration/thermal predictive maintenance prevents $70\%$ of unplanned bearing failures.
     * Hours saved: $44,000 \times 0.70 = 30,800\text{ hours recovered}$.
     * Gross Annual Financial Benefit: $30,800\text{ hrs} \times \text{JPY } 10,227 \approx \mathbf{\text{JPY } 315,000,000/\text{year}}$.
   * **Cost & Investment Breakdown**:
     * Sensor retrofits for 50 critical machines (2 sensors/machine @ JPY 150,000 installed) $= \text{JPY } 15\text{M}$.
     * Edge IoT Gateways (1 per 10 machines = 5 gateways @ JPY 600,000) $= \text{JPY } 3\text{M}$.
     * Cloud IoT platform setup, ML model calibration & integration fees $= \text{JPY } 60\text{M}$ (One-time CapEx).
     * Ongoing Cloud ingestion, model inference & sensor maintenance OpEx $= \text{JPY } 18\text{M/year}$.
   * **Payback & Net ROI**:
     * Total Year 1 Investment: $15 + 3 + 60 + 18 = \mathbf{\text{JPY } 96\text{M}}$.
     * Net Year 1 Cash Flow: $\text{JPY } 315\text{M} - \text{JPY } 96\text{M} = \mathbf{+\text{JPY } 219\text{M}}$.
     * Simple Payback Period: $\frac{\text{JPY } 78\text{M CapEx}}{\text{JPY } 315\text{M} - \text{JPY } 18\text{M OpEx}} \times 12\text{ months} = \mathbf{3.15\text{ Months}}$.
8. **Alternative Explanations & Missing Information**:
   * *Alternative*: Could failures be caused by operator error rather than machine wear? (Audit shows failures occur uniformly across night and day shifts, ruling out specific operator shifts).
   * *Missing Info*: Vibration frequency spectra data on failed bearings; vendor lead-time SLAs for spare bearings.
9. **Multiple Feasible Solutions**:
   * *Solution A (Manual / Process)*: Hire 8 extra maintenance inspectors and inspect bearing temperatures manually with handheld infrared guns every 2 hours.
   * *Solution B (On-Premises Industrial SCADA)*: Install hardwired PLCs and dedicated factory servers.
   * *Solution C (Cloud-Edge IoT Predictive Maintenance)*: Retrofit wireless vibration/thermal sensors, stream to edge filter, run ML anomaly models on AWS/Azure IoT Core.
10. **Trade-Off Comparison Matrix**:
    * Solution A: Low initial CapEx, but high recurring labor cost (JPY 60M/yr), human error risk, and exacerbates Japanese factory technician shortages.
    * Solution B: High CapEx (JPY 200M), rigid architecture, slow 18-month rollout.
    * Solution C: Optimal balance. Modest CapEx (JPY 78M), rapid 90-day pilot, elastic machine learning scaling, 3.15-month payback.
11. **Recommended Approach Supported by Evidence**:
    * Deploy Solution C (Hybrid Cloud-Edge IoT). Retrofit wireless magnetic sensors on the 50 bottleneck CNC machines first. Stream high-frequency vibration via MQTT to edge gateways; push 10-second statistical aggregates to AWS IoT Core. Integrate automated maintenance work orders directly into the client's SAP PM system.
12. **Risks, Dependencies, Implementation Stages & KPIs**:
    * **Phased Roadmap**:
      * *Phase 1 (M1–M3)*: 10-machine pilot in Plant 1. Baseline vibration model training.
      * *Phase 2 (M4–M6)*: Expand to all 50 bottleneck machines in Plant 1 & 2. SAP integration.
      * *Phase 3 (M7–M12)*: Fleetwide rollout across all 4 plants (remaining 150 machines).
    * **Key Measurable KPIs**:
      * Primary: Unplanned Downtime Reduction ($\ge 70\%$).
      * Secondary: OEE increase from $72\% \to 83\%$.
      * Operational: MTTR reduction from 14 hours to $< 5$ hours.
13. **Interviewer Follow-Up Questions & Model Answers**:
    * *Interviewer*: *"What happens if factory Wi-Fi experiences interference or drops out during operation?"*
      * *Candidate*: *"We design the edge gateway with local circular storage caching up to 48 hours of telemetry. The edge gateway runs a lightweight local threshold anomaly script; if critical vibration spikes occur while offline, it triggers a local physical amber beacon on the machine directly, ensuring zero safety or failure risk during network outages."*
14. **Transparent Scoring Rubric**:
    * **Superior (5/5)**: Quantifies lost margin/hr; structures MECE MTBF vs MTTR tree; evaluates 3 distinct options; calculates 3.15-month payback; addresses edge offline resilience.
    * **Competent (3/5)**: Mentions IoT sensors and predictive maintenance; calculates rough savings; lacks edge gateway offline architecture or MTBF/MTTR split.
    * **Inadequate (1/5)**: Recommends "using AI" without explaining sensor physics, edge-to-cloud data flow, financial ROI, or Japanese factory workforce realities.

---

### Case 2: Enterprise GenAI / RAG — Policy Search for a Japanese Life Insurer

1. **Candidate-Facing Prompt**:
   *"A major Japanese life insurance company headquartered in Tokyo employs 1,200 claims adjusters. When reviewing complex claims, adjusters spend an average of 3.5 hours daily manually searching through 80,000 legacy PDF policy documents spanning 40 years of regulatory revisions. This delays claim payouts to an average of 14 days, driving customer dissatisfaction and increasing adjuster overtime costs. How would you design, evaluate, and implement an enterprise Generative AI solution to streamline claims processing while ensuring strict regulatory compliance?"*
2. **Business Context & Objective**:
   * **Context**: Highly regulated financial environment governed by the Japan Financial Services Agency (FSA). PII must be protected under Japan's Act on the Protection of Personal Information (APPI).
   * **Objective**: Cut claim research time by at least $60\%$, accelerate claim turnaround from 14 days to $< 3$ days, and eliminate regulatory hallucination risk.
3. **Clarifying Questions (and Why They Matter)**:
   * *Question 1*: "Are policy documents purely in Japanese, and do they include complex nested tables and historical clause amendments?"  
     *Why it matters*: Dictates PDF extraction strategy (standard OCR vs multimodal vision chunking) and Japanese tokenizer selection.
   * *Question 2*: "Does the search query involve live patient medical records or personally identifiable financial data?"  
     *Why it matters*: Dictates strict PII redaction guardrails before prompt assembly to comply with Japan APPI.
   * *Question 3*: "Is the business expecting full automated claims payout approvals, or an adjuster-assistance copilot?"  
     *Why it matters*: Establishes human-in-the-loop governance; fully automated decisions are high regulatory risk.
4. **Issue Tree & Architecture Decomposition**:
   ```text
   ENTERPRISE RAG ARCHITECTURE
   ├── 1. Ingestion & Document Pipeline
   │   ├── PDF OCR & Document Layout Analysis (Azure AI Document Intelligence)
   │   ├── Semantic Chunking with Clause Metadata (Policy ID, Effective Date, Product Type)
   │   └── Japanese Vector Embeddings (`text-embedding-3-large`)
   ├── 2. Retrieval & Re-ranking Engine
   │   ├── Hybrid Search: BM25 Keyword Search + Dense Vector Cosine Similarity
   │   ├── Metadata Filtering: Filter out repealed clauses based on incident date
   │   └── Cross-Encoder Re-Ranking: Select top-5 most relevant chunks
   └── 3. Generation, Grounding & Safety Guardrails
       ├── In-context Prompt Construction with Exact Page Citations
       ├── PII Redaction & Enterprise LLM (Azure OpenAI GPT-4o in Japan East Region)
       └── Human-in-the-Loop Adjuster Verification Interface
   ```
5. **Candidate Assumptions vs Supplied Facts**:
   * *Supplied Facts*: 1,200 adjusters; 3.5 hrs/day spent searching; 80,000 legacy PDFs; 14-day payout latency.
   * *Candidate Assumptions*: Adjuster hourly fully-loaded cost JPY 4,500/hr; 240 working days/year; target productivity gain 2.0 hours saved per adjuster/day.
6. **Numerical Exhibit (`[PRACTICE ASSUMPTION]` Exhibit 2.1)**:
   * Current Research Time: $1,200\text{ adjusters} \times 3.5\text{ hrs/day} = 4,200\text{ hours daily}$.
   * Target Time Saved: $2.0\text{ hours/day per adjuster} = 2,400\text{ hours saved daily}$.
   * Annual Productive Hours Saved: $2,400 \times 240 = 576,000\text{ hours/year}$.
   * Gross Annual Financial Value: $576,000\text{ hrs} \times \text{JPY } 4,500/\text{hr} = \mathbf{\text{JPY } 2,592,000,000/\text{year}}$ (JPY 2.59 Billion).
7. **Step-by-Step Calculations & Financial Business Case**:
   * **Azure Cloud & GenAI Operating Costs (OpEx)**:
     * Daily queries: $1,200\text{ adjusters} \times 15\text{ queries/day} = 18,000\text{ queries/day}$.
     * Average tokens per query (Prompt + Context + Generation) $\approx 4,000\text{ tokens}$.
     * Daily tokens: $18,000 \times 4,000 = 72,000,000\text{ tokens/day} \approx 72\text{M tokens}$.
     * Blended token cost @ JPY 0.75 per 1,000 tokens $\approx \text{JPY } 54,000/\text{day} \implies \mathbf{\text{JPY } 13\text{M/year}}$.
     * Azure AI Search vector storage + document hosting $\approx \mathbf{\text{JPY } 25\text{M/year}}$.
     * Total Ongoing Annual OpEx $\approx \mathbf{\text{JPY } 38\text{M/year}}$.
   * **Implementation Investment (CapEx)**:
     * Consulting design, document chunking pipeline, UI copilot development, security audit $= \mathbf{\text{JPY } 120\text{M}}$.
   * **Net Benefit & Payback**:
     * Net Year 1 Benefit: $\text{JPY } 2,592\text{M} - (\text{JPY } 120\text{M} + \text{JPY } 38\text{M}) = \mathbf{+\text{JPY } 2,434\text{M}}$.
     * Payback period: Less than **1 month** against labor productivity.
8. **Alternative Explanations & Missing Information**:
   * *Alternative*: Why not fine-tune an open-source model like Llama-3? Fine-tuning bakes static facts into model weights, which hallucinate specific policy numbers, cannot cite exact PDF page numbers, and cost millions to retrain whenever policy clauses update. RAG is strictly superior.
9. **Multiple Feasible Solutions**:
   * *Approach 1*: Standard Elasticsearch keyword search across transcribed PDFs (Fails on semantic queries like "heart attack" vs "myocardial infarction").
   * *Approach 2*: Pure Vector Search RAG (Fails on exact clause alphanumeric IDs like "Clause 14-B-3").
   * *Approach 3*: **Hybrid Search RAG (Keyword BM25 + Vector + Re-ranking)** (Recommended).
10. **Trade-Off Comparison**:
    * Hybrid Search combines BM25 keyword precision for alphanumeric policy codes with vector embeddings for semantic medical concept matching.
11. **Recommended Approach Supported by Evidence**:
    * Implement Approach 3 on Microsoft Azure (Japan East region data sovereignty). Enforce strict zero data retention API agreements with Microsoft so client queries never train foundational models.
12. **Risks, Dependencies, Implementation Stages & KPIs**:
    * **Roadmap**:
      * *M1–M2*: Ingest 5,000 most common policies (Life & Critical Illness). Benchmark retrieval accuracy.
      * *M3–M4*: Pilot with 50 senior adjusters. Validate citation faithfulness.
      * *M5–M8*: Full deployment across all 1,200 adjusters.
    * **KPIs**: Payout turnaround time ($\le 3$ days); retrieval citation accuracy ($\ge 99\%$); adjuster adoption ($\ge 90\%$).
13. **Interviewer Follow-Up Questions & Model Answers**:
    * *Interviewer*: *"How do you prevent the LLM from hallucinating an approved claim coverage that does not exist?"*
      * *Candidate*: *"We enforce three architectural guardrails: 1) System prompt constraint: 'Answer ONLY using the provided retrieved context. If the answer is not contained, explicitly state: Insufficient policy context'; 2) Hallucination verification: Run an automated factual consistency checker comparing generation against retrieved text; 3) Mandatory UI citation: The adjuster interface displays the exact highlighted PDF page snippet alongside the generated text; the adjuster must click to confirm before payout approval."*
14. **Transparent Scoring Rubric**:
    * **Superior (5/5)**: Explains RAG vs fine-tuning clearly; specifies hybrid search (BM25 + vector); addresses Japan APPI data sovereignty; calculates realistic token costs and payback; designs human-in-the-loop citation verification.
    * **Competent (3/5)**: Understands RAG and embeddings; provides general cost estimate; misses hybrid search or APPI regulatory safeguards.
    * **Inadequate (1/5)**: Proposes fine-tuning an LLM to "memorize policies"; ignores hallucinations and regulatory compliance.

---

### Case 3: Cloud Migration — Core Banking Modernization for a Regional Japanese Bank

1. **Candidate-Facing Prompt**:
   *"A tier-2 regional bank in the Kansai region (Osaka/Kyoto/Hyogo) manages JPY 4.5 Trillion in deposits across 120 retail branches and 1.8 million retail/SME accounts. Currently, 75% of the bank's annual IT budget (JPY 1.8 Billion) is consumed merely by maintaining a 32-year-old on-premise IBM mainframe running COBOL core banking applications. Releases of new digital mobile banking features take 9 to 12 months due to tightly coupled batch architectures, causing younger retail customers to defect to modern digital-only banks (neobanks). The CIO asks Accenture to evaluate cloud migration options, design a zero-downtime architecture satisfying Japan Financial Services Agency (FSA) compliance, build the financial business case, and provide a phased implementation roadmap."*
2. **Business Context & Objective**:
   * **Regulatory & Market Context**: Governed strictly by the Financial Services Agency of Japan (FSA) and Center for Financial Industry Information Systems (FISC) Security Guidelines. Strict data residency in Japan (Tokyo and Osaka regions). Zero customer ledger data loss tolerance (RPO = 0 for ledger balances).
   * **Core Objectives**:
     1. Slash recurring IT infrastructure run costs by at least 50% within 4 years.
     2. Accelerate digital feature release velocity from 9+ months to bi-weekly sprints.
     3. Ensure zero unplanned downtime during migration across 1.8M active accounts.
3. **Clarifying Questions (and Why They Matter)**:
   * *Question 1*: *"Can the bank tolerate a weekend maintenance blackout window to cut over to a new system in a single 'Big Bang' deployment?"*  
     *Why it matters*: In retail banking, a Big Bang cutover carries catastrophic operational and reputational risk; an unexpected failure can halt ATMs and point-of-sale debit nationwide, drawing punitive FSA sanctions. Confirms the necessity of an incremental coexistence pattern.
   * *Question 2*: *"What proportion of daily mainframe CPU consumption represents read queries (balance inquiries, transaction history) versus write transactions (fund transfers, deposit updates)?"*  
     *Why it matters*: Read queries typically constitute 80–90% of banking transaction volume and can be offloaded to cloud read replicas immediately without touching the core write ledger.
   * *Question 3*: *"What is the retirement profile of the internal COBOL engineering team?"*  
     *Why it matters*: Addresses the "2025 Digital Cliff" in Japan; if senior COBOL developers retire within 3 years, staying on-premise is an existential business continuity risk.
4. **Issue Tree & Architecture Decomposition**:
   ```text
   CORE BANKING MODERNIZATION
   ├── 1. Architectural Strategy & Migration Pattern
   │   ├── Option A: Re-host ("Lift & Shift" to Mainframe Cloud Emulators)
   │   ├── Option B: Re-platform / Big Bang Replacement with Vendor Package
   │   └── Option C: Strangler Fig Pattern with Event-Driven Microservices (Recommended)
   ├── 2. Data Synchronization & Coexistence Layer
   │   ├── Real-time Change Data Capture (CDC) via IBM MQ / Debezium
   │   ├── Event Streaming Backbone (Apache Kafka on AWS/Azure Japan)
   │   └── Dual-Write Verification & Continuous Reconciliation Engine
   ├── 3. Regulatory Compliance & Resilience (FSA / FISC)
   │   ├── Dual-Region Active-Standby (AWS Tokyo primary, AWS Osaka disaster recovery)
   │   ├── Encryption: TLS 1.3 in-transit, AES-256 at-rest with KMS Customer-Managed Keys
   │   └── RPO < 1 second, RTO < 15 minutes automated failover
   └── 4. Financial TCO & Value Realization
       ├── Legacy Run Cost Baseline vs Target Cloud OpEx
       ├── Multi-Year Migration CapEx & Delivery Sprints
       └── Deposit Retention & Developer Velocity Value
   ```
5. **Candidate Assumptions vs Supplied Facts**:
   * *Supplied Facts*: Kansai regional bank; 1.8M accounts; JPY 1.8B annual mainframe run cost (75% of IT budget); 9–12 month release cycles; FSA regulatory jurisdiction.
   * *Candidate Assumptions* (`[PRACTICE ASSUMPTION]`):
     * Daily transaction volume: 5,000,000 queries/day (85% reads, 15% writes).
     * Peak throughput: 450 transactions per second (TPS).
     * Customer churn rate: 3.5% annual loss of deposits to neobanks without modern mobile app.
6. **Numerical Exhibit (`[PRACTICE ASSUMPTION]` Exhibit 3.1)**:

   | Cost / Financial Dimension | Current On-Premise Mainframe (Annual) | Year 1–2 (Hybrid Coexistence) | Year 4+ (Target Cloud Steady State) |
   |---|---|---|---|
   | Hardware Lease & Maintenance | JPY 850M | JPY 850M | JPY 0 |
   | Specialized COBOL Contractor Licenses | JPY 650M | JPY 500M | JPY 100M |
   | Data Center Facility & Power (Osaka) | JPY 300M | JPY 250M | JPY 50M (Edge co-lo) |
   | Cloud Infrastructure (AWS Tokyo + Osaka) | JPY 0 | JPY 220M | JPY 480M |
   | Cloud Managed Services & Monitoring | JPY 0 | JPY 60M | JPY 120M |
   | **Total Recurring Run Cost (OpEx)** | **JPY 1,800M / year** | **JPY 1,880M / year** | **JPY 750M / year** |
   | **Net Annual OpEx Savings (Year 4+)** | — | — | **+ JPY 1,050M / year** |

7. **Step-by-Step Calculations & Financial Business Case**:
   * **CapEx Investment (Migration Implementation over 36 Months)**:
     * Year 1 (API Layer, CDC, Cloud Landing Zone, Mobile Read Service): JPY 850M.
     * Year 2 (Payments & Transfers Microservices, Core Ledger Parallel Run): JPY 950M.
     * Year 3 (Full Account Ledger Cutover, Mainframe Decommissioning): JPY 600M.
     * **Total Migration Investment**: $\text{JPY } 850\text{M} + 950\text{M} + 600\text{M} = \mathbf{\text{JPY } 2,400\text{M}}$ (JPY 2.4 Billion).
   * **Cumulative Cash Flow & Payback Schedule**:
     * Year 1: Net Cash Flow $= -\text{JPY } 850\text{M} - 80\text{M (coexistence OpEx)} = -\text{JPY } 930\text{M}$.
     * Year 2: Net Cash Flow $= -\text{JPY } 950\text{M} + 0\text{ savings} = -\text{JPY } 950\text{M}$.
     * Year 3: Partial Savings (JPY 400M) $- 600\text{M CapEx} = -\text{JPY } 200\text{M}$.
     * Year 4: Steady-State Savings $= +\mathbf{\text{JPY } 1,050\text{M}}$.
     * Year 5: Steady-State Savings $= +\mathbf{\text{JPY } 1,050\text{M}}$.
     * Year 6: Steady-State Savings $= +\mathbf{\text{JPY } 1,050\text{M}}$.
     * Cumulative Savings post-launch covers JPY 2.4B CapEx in approximately **4.3 years from project kickoff** (Year 5, Month 4).
   * **Commercial Value Beyond IT Cost**:
     * Preserving deposit base: Halting 3.5% customer attrition protects JPY 157.5B in retail deposits, saving an estimated JPY 450M annually in wholesale interbank liquidity borrowing costs.
8. **Alternative Explanations & Missing Information**:
   * *Alternative 1*: Full SaaS Core Banking Replacement (e.g., nCino / Thought Machine). While modern, completely rewriting Kansai regional commercial lending custom logic into SaaS takes 5+ years and risks severe mismatch with regional Japanese commercial conventions (*tegata* bills, specialized SME credit scoring).
   * *Missing Information*: Exact volume of batch jobs executing between 02:00 and 05:00, and external network links with the Zengin Net (Japanese domestic bank transfer clearing network).
9. **Multiple Feasible Solutions**:
   * *Option 1: Lift & Shift / Re-hosting*: Emulate COBOL environment on AWS EC2. Lowest upfront risk, but retains legacy technical debt, achieves only 15% cost savings, and fails to improve feature release speed.
   * *Option 2: Big-Bang Core Ledger Replacement*: High risk, catastrophic failure probability, requires 3-year freeze on all business features.
   * *Option 3: Strangler Fig Pattern with Event-Driven Architecture (Recommended)*: Wrap mainframe with REST APIs and Kafka; migrate microservices domain-by-domain (Inquiries $\to$ Payments $\to$ Loans $\to$ Core Ledger).
10. **Trade-Off Comparison Matrix**:

    | Criteria | Option 1: Lift & Shift | Option 2: Big-Bang Package | Option 3: Strangler Fig (Recommended) |
    |---|---|---|---|
    | **Upfront Risk** | Low | Extremely High | Low to Moderate |
    | **Time to First Business Value**| 6 Months | 36 Months | **4 Months (Mobile Inquiries)** |
    | **Annual OpEx Reduction** | 15% (~JPY 270M) | 60% (~JPY 1,080M) | **58% (~JPY 1,050M)** |
    | **Release Velocity Improvement**| Negligible | Moderate | **High (Bi-weekly CI/CD)** |
    | **Operational Disruption Risk** | Minimal | Existential | **Contained per microservice** |

11. **Recommended Approach Supported by Evidence**:
    * Implement Option 3 (Strangler Fig). Establish an AWS Tokyo (Primary) and AWS Osaka (Secondary DR) Landing Zone compliant with FISC guidelines.
    * Deploy Apache Kafka on Amazon MSK as the central enterprise event bus.
    * Use Debezium Change Data Capture (CDC) on mainframe DB2 transaction logs to stream read data into Amazon Aurora PostgreSQL, powering mobile banking inquiries immediately.
12. **Risks, Dependencies, Implementation Stages & Measurable KPIs**:
    * **Phased Roadmap**:
      * *Phase 1 (M1–M6)*: Landing zone setup, CDC pipeline, offload 85% read traffic to mobile banking cloud cache. Mainframe CPU load drops by 40%.
      * *Phase 2 (M7–M18)*: Decouple card payments and peer-to-peer transfers into containerized Spring Boot / Quarkus microservices running on Amazon EKS.
      * *Phase 3 (M19–M36)*: Migrate deposits and savings general ledger to Aurora PostgreSQL. Run parallel ledger shadow reconciliation for 90 days. Decommission mainframe.
    * **Key Measurable KPIs**:
      * Mainframe CPU utilization drop ($\ge 40\%$ by M6).
      * Mobile feature release lead time ($< 14$ days vs baseline 9 months).
      * Annual IT Run Cost ($\le \text{JPY } 750\text{M}$ by Year 4).
      * Data replication latency between on-prem and cloud ($< 200\text{ ms}$).
13. **Interviewer Follow-Up Questions & Model Answers**:
    * *Interviewer*: *"How do you prove to the Bank of Japan and FSA auditors that your data replication between on-premise mainframe and AWS did not drop or corrupt a single transaction during parallel run?"*
      * *Candidate*: *"We implement a cryptographic dual-run reconciliation engine. Every financial transaction event published to Kafka is tagged with a deterministic transaction ID and sequence number. An automated reconciliation worker continuously executes double-entry checksum audits comparing the on-prem DB2 balance table against the Aurora PostgreSQL ledger every 5 minutes. Any discrepancy triggers an immediate automated circuit-breaker alert to the operations center, isolating the affected account while keeping the rest of the bank operational."*
14. **Transparent Scoring Rubric**:
    * **Superior (5/5)**: Proposes Strangler Fig over Big-Bang; structures read vs write offloading; models TCO showing crossover payback; incorporates Japan FSA/FISC compliance (Tokyo/Osaka multi-region); explains CDC and reconciliation architecture.
    * **Competent (3/5)**: Recommends cloud migration; identifies microservices; calculates basic savings; lacks dual-region disaster recovery specifics or financial reconciliation mechanics.
    * **Inadequate (1/5)**: Recommends shutting down the mainframe overnight for a clean cloud reinstall; ignores banking regulatory rules and transaction integrity.

---

### Case 4: Omnichannel Retail — Preventing Point-of-Sale Inventory Stock-Outs

1. **Candidate-Facing Prompt**:
   *"A prominent Japanese convenience store (*konbini*) franchise operates 2,500 stores across the Kanto, Kansai, and Chubu regions. Across the network, daily sales average JPY 550,000 per store, yielding JPY 501.8 Billion in annual system sales. However, regional audits reveal that the chain suffers from an estimated 8% lost sales opportunity due to evening stock-outs of high-margin fresh bento boxes, onigiri, and ready-to-drink beverages between 17:00 and 21:00. Simultaneously, store managers overcompensate on rainy days, resulting in JPY 12.5 Billion in expired fresh food waste discarded annually. How would you diagnose the root cause, design an integrated IoT and predictive demand forecasting system, calculate the financial business case, and roll out the solution across 2,500 franchise stores?"*
2. **Business Context & Objective**:
   * **Context**: Convenience stores operate on razor-thin net margins with twice-daily deliveries from 18 regional distribution centers. Shelf-life of fresh bento is strictly 18 hours from production. Store managers currently place replenishment orders manually using paper order sheets or rudimentary POS terminals based on gut feel.
   * **Objectives**:
     1. Cut stock-out lost sales by at least 50% (recovering $\ge \text{JPY } 20\text{B}$ in lost gross merchandise value).
     2. Reduce fresh food expired waste by at least 25% (saving $\ge \text{JPY } 3.1\text{B}$ in disposal write-offs).
     3. Automate store order generation to save each store manager 1.5 hours of daily administrative ordering labor.
3. **Clarifying Questions (and Why They Matter)**:
   * *Question 1*: *"Are the stores company-owned or franchise-operated?"*  
     *Why it matters*: In a franchise model, store owners pay for food waste directly out of their store profits, while corporate headquarters earns a percentage royalty on gross sales. This creates conflicting incentives: corporate wants high stock on shelves to maximize sales, while franchise owners under-order to prevent waste write-offs. The solution must align store-level profitability.
   * *Question 2*: *"What is the lead time between store order placement and truck delivery?"*  
     *Why it matters*: Fresh food operates on tight supply windows. Morning delivery order cut-off is 10:00 AM for 17:00 PM delivery (7-hour lead time). The forecasting algorithm must run reliably before 09:30 AM.
   * *Question 3*: *"What data is logged by current POS scanners?"*  
     *Why it matters*: Determines feature availability for ML models. Confirms availability of timestamp, SKU, unit price, weather condition flag, and customer demographic estimate button pressed by cashier.
4. **Issue Tree & Root-Cause Decomposition**:
   ```text
   STORE INVENTORY IMBALANCE (STOCK-OUTS & FOOD WASTE)
   ├── 1. Demand Volatility & Forecasting Inaccuracy
   │   ├── Weather Sensitivity: Sudden rain drops evening foot traffic by 22%
   │   ├── Local Events: Concerts/train delays causing unpredictable demand surges
   │   └── Manual Bias: Store managers under-ordering high-margin bento to avoid waste risk
   ├── 2. Supply Chain & Delivery Bottlenecks
   │   ├── 7-hour order freeze window prevents midday dynamic replenishment
   │   ├── Distribution Center picking errors and delivery truck traffic delays
   │   └── Batch order processing creates delivery bunching during peak traffic
   └── 3. In-Store Inventory Visibility Gaps
       ├── POS registers what was sold, but NOT what was sought by customers (unmet demand)
       ├── Shoplifting / spoilage creates discrepancy between system stock and physical shelf
       └── Zero real-time shelf telemetry (smart weight sensors vs RFID tags)
   ```
5. **Candidate Assumptions vs Supplied Facts**:
   * *Supplied Facts*: 2,500 stores; JPY 550,000 daily sales/store; JPY 501.8B annual chain sales; 8% lost sales from stock-outs (JPY 40.1B GMV); JPY 12.5B annual food waste loss.
   * *Candidate Assumptions* (`[PRACTICE ASSUMPTION]`):
     * Fresh food gross margin $= 35\%$.
     * Franchise royalty fee $= 40\%$ of gross profit to headquarters, $60\%$ retained by franchisee.
     * Store manager hourly labor rate $= \text{JPY } 2,200/\text{hour}$.
6. **Numerical Exhibit (`[PRACTICE ASSUMPTION]` Exhibit 4.1)**:

   | Operational Metric | Current Baseline | Target Post-Deployment | Financial Impact |
   |---|---|---|---|
   | Total Chain Sales | JPY 501.8 Billion | JPY 521.9 Billion | + JPY 20.1 Billion gross revenue |
   | Stock-Out Lost Sales | 8.0% (JPY 40.1B) | 4.0% (JPY 20.0B) | **+ JPY 20.1B Recovered Sales** |
   | Recovered Gross Margin (@ 35%) | — | — | **+ JPY 7.04 Billion Gross Profit** |
   | Expired Food Disposal Waste | JPY 12.5 Billion | JPY 9.38 Billion (-25%) | **+ JPY 3.12 Billion Waste Avoidance** |
   | Total Annual Gross Financial Value | — | — | **+ JPY 10.16 Billion / year** |
   | Split: Corporate Headquarters (40%) | — | — | **JPY 4.06 Billion / year** |
   | Split: 2,500 Franchisees (60%) | — | — | **JPY 6.10 Billion / year (JPY 2.44M/store)**|

7. **Step-by-Step Calculations & Financial Business Case**:
   * **System Investment (CapEx & OpEx)**:
     * *CapEx (Year 1 Implementation)*:
       * Central AI Predictive Demand Platform (LightGBM + DeepAR neural time-series on AWS/GCP): JPY 380M.
       * POS Edge Gateway & Tablet App for 2,500 stores (@ JPY 120,000 per store setup): JPY 300M.
       * Integration with 18 Distribution Center ERPs & logistics routing: JPY 180M.
       * Change management & store manager training caravan: JPY 140M.
       * **Total CapEx**: $\mathbf{\text{JPY } 1,000\text{M}}$ (JPY 1.0 Billion).
     * *Ongoing Annual OpEx*:
       * Cloud data lakehouse ingestion, weather API feeds, continuous model retraining, store tablet LTE SIMs $= \mathbf{\text{JPY } 320\text{M / year}}$.
   * **Return on Investment (ROI) & Payback**:
     * Net Year 1 Benefit: $\text{JPY } 10,160\text{M (Gross Benefit)} - (\text{JPY } 1,000\text{M CapEx} + \text{JPY } 320\text{M OpEx}) = \mathbf{+\text{JPY } 8,840\text{M}}$.
     * Simple Payback Period: $\frac{\text{JPY } 1,000\text{M CapEx}}{\text{JPY } 10,160\text{M} - 320\text{M}} \times 12\text{ months} \approx \mathbf{1.22\text{ months}}$.
     * Even under conservative $20\%$ benefit capture, payback occurs in **under 6 months**.
8. **Alternative Explanations & Missing Information**:
   * *Alternative*: Computer Vision cameras on every shelf to detect empty slots in real time. Rejected due to high hardware cost (JPY 800,000/store = JPY 2.0B CapEx) and high camera maintenance overhead in dusty retail environments. Software-driven ML forecasting using POS scanner data achieves 90% of the benefit at 15% of the cost.
9. **Multiple Feasible Solutions**:
   * *Approach 1: Static Rule-Based Reorder Buffers*: Fixed +15% order buffer on weekends. Fails because demand varies dynamically with localized rainfall, temperature shifts, and public holidays.
   * *Approach 2: Pure Computer Vision Smart Shelves*: Visually tracks out-of-stock items, but cannot forecast forward demand 7 hours ahead for morning kitchen production.
   * *Approach 3: Cloud Machine Learning Predictive Ordering Copilot (Recommended)*: Multi-factor gradient boosting (XGBoost/LightGBM) forecasting store-SKU hourly demand 24 hours in advance, auto-populating recommended order quantities into store manager tablets with 1-click confirmation.
10. **Trade-Off Comparison Matrix**:

    | Decision Criteria | Approach 1: Rule-Based Buffer | Approach 2: Smart Camera Shelves | Approach 3: ML Predictive Ordering (Rec.) |
    |---|---|---|---|
    | **Waste Reduction Impact** | Negative (increases waste by 18%) | Zero (reactive detection only) | **High (-25% waste reduction)** |
    | **Stock-Out Elimination** | Moderate (+4% sales) | High (+7% sales) | **High (+4% to +6% sales)** |
    | **Hardware CapEx per Store**| JPY 0 | JPY 800,000 | **JPY 120,000 (Tablet + Edge Gateway)**|
    | **Implementation Horizon** | 1 Month | 18 Months | **6 Months** |
    | **Franchisee Adoption Ease**| High | Low (privacy/camera pushback) | **High (Saves 1.5 hrs/day labor)** |

11. **Recommended Approach Supported by Evidence**:
    * Implement Approach 3. Train hierarchical time-series models on 3 years of store POS receipts, enriched with Japan Meteorological Agency (JMA) hyper-local weather feeds (hourly precipitation and temperature per mesh code) and regional school/event calendars.
    * Provide store managers with a mobile ordering tablet where the AI suggests order quantities at 08:30 AM. Store managers retain override capability, building trust.
12. **Risks, Dependencies, Implementation Stages & Measurable KPIs**:
    * **Roadmap**:
      * *Stage 1 (M1–M2)*: Data pipeline ingestion on Google Cloud BigQuery / AWS. Feature engineering and model backtesting across historical POS logs.
      * *Stage 2 (M3–M4)*: 50-store pilot in Setagaya and Yokohama. Evaluate model Mean Absolute Percentage Error (MAPE) and store manager override rates.
      * *Stage 3 (M5–M8)*: Regional rollout across 2,500 stores; integrate delivery manifest EDI feeds with distribution centers.
    * **Key Measurable KPIs**:
      * Forecast Accuracy: SKU-level daily MAPE $\le 12\%$.
      * Store-Level Out-of-Stock Rate: Reduced from $8.0\% \to \le 3.5\%$.
      * Manager Order Override Rate: Drops from $60\%$ in Month 1 to $< 15\%$ by Month 4 as trust increases.
      * Store Labor Saved: $1.5\text{ hours/day}$ per store manager.
13. **Interviewer Follow-Up Questions & Model Answers**:
    * *Interviewer*: *"What happens if a store manager consistently overrides the AI recommendations, ordering 30% fewer bento boxes out of fear of waste, resulting in persistent evening stock-outs?"*
      * *Candidate*: *"We solve this using behavioral change management rather than top-down coercion: 1) Dashboard Transparency: The store manager tablet displays a simulated 'Opportunity Loss vs Waste Balance' card showing exact yen amounts lost to stock-outs versus waste over the past 30 days; 2) Guaranteed Shared Waste Safety Net: Corporate headquarters implements an incentive pilot where if the store follows the AI recommendation and fresh bento remains unsold, headquarters covers 50% of the discarded item wholesale cost during the first 90 days. This removes downside fear, aligns franchisee incentives, and dramatically lowers override rates."*
14. **Transparent Scoring Rubric**:
    * **Superior (5/5)**: Distinguishes corporate vs franchisee economic incentives; models both stock-out revenue gain and food waste savings; calculates sub-2-month payback; incorporates weather/lead-time features; designs change management for store manager overrides.
    * **Competent (3/5)**: Proposes machine learning demand forecasting; calculates basic sales increase; recognizes weather impact; overlooks franchise incentive split or change management.
    * **Inadequate (1/5)**: Proposes adding cameras to shelves without understanding 7-hour kitchen lead time; recommends ordering arbitrary excess inventory without addressing waste costs.

---

### Case 5: Automotive Connected Fleet — Predictive Battery Health for Commercial EVs
1. **Problem Statement**: A logistics delivery company in Tokyo operating 1,200 electric light commercial vehicles experiences unexpected battery failures during peak delivery hours, causing JPY 180M in towing and late delivery penalties.
2. **Clarifying Questions**: What telemetry is available from vehicles? (Battery voltage, cell temperature, state of charge, ambient temperature via CAN bus). What is the cellular connectivity reliability? (99.5% across Tokyo metro via 4G LTE).
3. **Framework**: IoT Ingestion $\to$ Time-Series Telemetry Pipeline $\to$ Machine Learning Degradation Modeling $\to$ Maintenance Dispatch Integration.
4. **Data Required**: CAN bus telematics (1 Hz sampling), historical battery replacement logs, ambient weather records, route topography.
5. **Analysis Plan**: Stream CAN bus telemetry through an on-vehicle edge logger using MQTT over TLS to AWS IoT Core. Process streams via AWS Kinesis and Amazon Timestream. Train physics-informed neural network predicting State of Health (SOH) and anomalous internal resistance spikes 7 days prior to catastrophic cell failure.
6. **Calculations**:
   * Unscheduled failure penalty = JPY 180M/year. Battery replacement cost = JPY 800,000/pack.
   * Predictive scheduling prevents 85% of road breakdowns $= \text{JPY } 153\text{M savings}$.
   * Scheduled depot replacement extends average pack life by 1.5 years, deferring JPY 240M in capital replacement across 5 years.
7. **Interpretation**: Immediate operating risk elimination combined with significant vehicle asset lifecycle extension.
8. **Recommendation**: Integrate battery alerts directly into depot nightly charging schedules: vehicles with degraded cells are routed to lower-mileage delivery routes.
9. **Risks**: Cellular dead zones in underground delivery loading docks; firmware updates bricking vehicle telematics units.
10. **Follow-up Questions**: *"How do you handle privacy concerns regarding driver GPS tracking?"* (Separate vehicle diagnostic telemetry from driver identity using tokenized pseudonymization).

---

### Case 6: Healthcare & Pharma — Cold-Chain Temperature Compliance Monitoring
1. **Problem Statement**: A major Japanese pharmaceutical distributor faces strict new regulatory audits for temperature-sensitive biologics transport, where 0.4% of shipments exceed temperature thresholds ($2^\circ\text{C} - 8^\circ\text{C}$), resulting in JPY 600M in destroyed inventory.
2. **Clarifying Questions**: What is the transit duration? (Under 24 hours nationwide). What sensors are currently used? (Passive USB data loggers inspected only after delivery).
3. **Framework**: Real-Time IoT Sensor Tracking $\to$ Cellular / Bluetooth Low Energy (BLE) Ingestion $\to$ Proactive Driver Routing Alert System.
4. **Data Required**: Continuous temperature/humidity logs, refrigerated truck compressor status, GPS route coordinates, traffic congestion feeds.
5. **Analysis Plan**: Replace passive USB loggers with BLE sensor tags inside cargo boxes connecting to a cellular gateway in the driver cab. If cargo temperature breaches $6.5^\circ\text{C}$ for over 10 minutes, automatically send high-priority audible alerts to driver and dispatch coordinator to adjust cooling or divert to nearest storage depot.
6. **Calculations**:
   * Destroyed drug inventory = JPY 600M annually.
   * Real-time alerts reduce temperature breach spoilage by 80% $= \text{JPY } 480\text{M saved}$.
   * Sensor hardware & connectivity = JPY 45M/year. Net annual savings = JPY 435M.
7. **Interpretation**: Solves regulatory compliance risk while paying for itself in under 2 months.
8. **Recommendation**: Implement immutable audit trail logging on an encrypted ledger database to provide unalterable inspection records for Ministry of Health (MHLW) audits.
9. **Risks**: Sensor battery depletion in freezing temperatures; false alarm alerts overwhelming drivers.
10. **Follow-up Questions**: *"What happens if the driver's phone/gateway loses signal in mountain tunnels?"* (BLE tags record internal memory logs and auto-sync immediately upon reconnecting).

---

### Case 7: Telecom — Private 5G Network for a Smart Port in Yokohama
1. **Problem Statement**: A container shipping terminal in Yokohama experiences congestion and safety hazards from human-operated gantry cranes, seeking to deploy autonomous container transport vehicles (AGVs) requiring $< 10\text{ ms}$ latency and 99.999% reliability.
2. **Clarifying Questions**: Why not standard Wi-Fi? (Terminal metal shipping containers cause severe Wi-Fi signal reflections and blind spots). How many AGVs? (60 vehicles).
3. **Framework**: Private 5G Core Architecture $\to$ Multi-Access Edge Computing (MEC) $\to$ Automated Fleet Orchestration.
4. **Data Required**: Terminal physical layout, radio frequency interference scans, vehicle sensor telemetry bandwidth (LiDAR + camera feeds), crane operational cycles.
5. **Analysis Plan**: Deploy Private 5G sub-6 GHz small cells across port light towers. Establish local on-premise Multi-Access Edge Computing (MEC) servers running containerized fleet control algorithms, keeping video telemetry local without routing across the public internet.
6. **Calculations**:
   * Port turnaround delay cost = JPY 1,200M annually.
   * Autonomous AGVs improve container throughput by 28%, capturing JPY 850M in annual capacity fees and reducing diesel fuel costs by JPY 180M.
   * Private 5G CapEx = JPY 650M. Payback in 1.8 years.
7. **Interpretation**: Private 5G provides deterministic low latency impossible with industrial Wi-Fi in high-metal environments.
8. **Recommendation**: Phase deployment: remote-control human operators first over 5G before transitioning to full autonomous navigation.
9. **Risks**: Spectrum licensing delays from Japan Ministry of Internal Affairs and Communications (MIC); adverse weather (heavy rain) attenuating radio signals.
10. **Follow-up Questions**: *"How do you ensure cybersecurity on a Private 5G network physically accessible to foreign shipping crews?"* (Strict SIM-based network authentication, network slicing, and physical air-gapping of crane controls from public terminal Wi-Fi).

---

### Case 8: Financial Services — Real-Time Transaction Anti-Money Laundering (AML)
1. **Problem Statement**: A Tokyo online brokerage processes 10M daily transactions. Legacy overnight batch rule engines produce a 95% false-positive rate, requiring 200 compliance officers to manually review alerts and failing to catch sophisticated smurfing rings.
2. **Clarifying Questions**: What is the regulatory SLA? (Suspicious activity reports must be filed within 72 hours). What is the peak transaction rate? (3,000 TPS during Tokyo Stock Exchange market open).
3. **Framework**: Streaming Architecture (Apache Flink / Kafka) $\to$ Graph Database Entity Resolution (Neo4j / Amazon Neptune) $\to$ Machine Learning Anomaly Detection.
4. **Data Required**: Account opening metadata, IP address logs, beneficiary bank details, transaction amounts, historical confirmed AML cases.
5. **Analysis Plan**: Implement streaming event ingestion via Kafka. Run real-time graph traversal detecting cyclic money laundering networks (A $\to$ B $\to$ C $\to$ A) and structuring patterns within 2 seconds of transfer initiation.
6. **Calculations**:
   * 200 compliance staff at JPY 6M/year $= \text{JPY } 1,200\text{M annual compliance cost}$.
   * Reducing false positives by 70% allows redeploying 120 staff $= \text{JPY } 720\text{M recurring annual cost reduction}$.
   * Mitigates potential JPY 2B regulatory non-compliance fines from Japan Financial Services Agency (FSA).
7. **Interpretation**: Transforms AML from a reactive end-of-day cost center into a real-time risk mitigation barrier.
8. **Recommendation**: Implement explainable AI (XAI) feature attribution (SHAP values) so compliance officers receive exact reasons why an alert was generated.
9. **Risks**: High latency during market opening spikes dropping transactions; changing regulatory AML definitions requiring frequent rule re-calibration.
10. **Follow-up Questions**: *"How do you handle graph query complexity explosion during large-scale network lookups?"* (Limit graph traversal depth to 3 degrees of separation during real-time transaction screening).

---

### Cases 9–15: Quick-Fire Digital Transformation Case Outlines
* **Case 9: Public Sector — Tokyo Municipal Digital Ward Services**: Migrating paper resident certificates (*Juminhyo*) to My Number Card smartphone app. Architecture: Gov-Cloud AWS with zero-trust API gateway. Impact: 85% drop in municipal counter wait times; JPY 420M annual administrative savings.
* **Case 10: Energy & Utilities — Smart Grid Smart Meter Analytics**: Ingesting 15-minute smart meter electricity telemetry from 8M homes across Kanto to forecast peak load and dynamically price solar feed-in tariffs. Architecture: Apache Spark on Google Cloud BigQuery. Impact: JPY 1.5B peak power procurement savings.
* **Case 11: Hospitality & Song — Personalized Guest Experience for Luxury Tokyo Hotel**: Deploying facial recognition check-in, keyless mobile entry, and GenAI room concierge. Impact: 30% increase in on-property dining spend; 95% guest satisfaction score.
* **Case 12: Mining & Construction — Autonomous Hydraulic Excavators**: Retrofitting construction equipment with centimeter-accuracy RTK-GPS and LiDAR for autonomous trenching. Architecture: Edge industrial computers with 4G LTE remote supervisory override. Impact: 40% reduction in project completion schedule; eliminates worksite accident hazards.
* **Case 13: Education & EdTech — Adaptive AI Learning for Japanese University**: Real-time knowledge graph mapping student engineering coursework mastery and generating personalized problem sets. Architecture: Serverless Python microservices with vector search. Impact: 25% improvement in course completion rates.
* **Case 14: Airline & Aviation — Predictive Aircraft Turnaround & Baggage Tracking**: RFID baggage tag tracking from check-in to aircraft cargo hold combined with computer vision tarmac turnaround monitoring. Impact: 60% reduction in delayed flight departures; JPY 380M in fuel and gate turnaround penalty savings.
* **Case 15: Fast-Fashion Supply Chain — Near-Real-Time Trend Sensing**: Scraping global fashion social media imagery using multi-modal AI to forecast Japanese seasonal apparel demand and adjust Southeast Asia garment production within 10 days. Impact: 50% drop in end-of-season markdown discounting; JPY 2.8B profit recovery.

---

## 3. Fifteen MECE Issue-Tree & Root-Cause Drills

For each drill, a 3-level MECE decomposition is provided:

### Drill 1: Enterprise Cloud Bill Inflation (+40% YoY)
```text
                            [Cloud Cost Inflation +40%]
                                        │
             ┌──────────────────────────┴──────────────────────────┐
             ▼                                                     ▼
     [Usage / Consumption]                                  [Pricing & Architecture]
             │                                                     │
   ┌─────────┴─────────┐                                 ┌─────────┴─────────┐
   ▼                   ▼                                 ▼                   ▼
[Zombie Compute VMs] [Uncompressed Data Egress]        [On-Demand vs Reserved] [Over-Provisioned Instances]
```

### Drill 2: Mobile Banking App User Drop-off (35% Abandonment at KYC)
```text
                            [KYC Abandonment 35%]
                                        │
             ┌──────────────────────────┴──────────────────────────┐
             ▼                                                     ▼
       [Technical UX]                                       [Process & Trust]
             │                                                     │
   ┌─────────┴─────────┐                                 ┌─────────┴─────────┐
   ▼                   ▼                                 ▼                   ▼
[Camera OCR Failure] [Slow SMS OTP Delivery]           [Excessive Data Fields] [Privacy Concerns]
```

### Drills 3–15 Summaries:
* **Drill 3: Low Enterprise Tool Adoption (<25%)**: Divide into **Awareness/Training** (lack of onboarding, poor manuals) vs **System Friction** (slow single-sign-on, clunky UI, duplicate data entry).
* **Drill 4: Factory Assembly Defect Spike**: Divide into **Machine/Tooling** (sensor drift, worn bearings) vs **Material** (batch impurity) vs **Operator** (shift turnover, training gaps).
* **Drill 5: Retail E-Commerce Cart Abandonment (70%)**: Divide into **Checkout Friction** (mandatory account creation, limited payment options like PayPay) vs **Financial Surprise** (unexpected shipping costs, taxes).
* **Drill 6: Enterprise API Gateway Latency Spike**: Divide into **Network Infrastructure** (DNS resolution, bandwidth saturation) vs **Application Layer** (unindexed database queries, synchronous downstream microservice calls).
* **Drill 7: Customer Churn in B2B SaaS**: Divide into **Product Fit** (missing core features, frequent bugs) vs **Economic Value** (poor ROI, budget cuts) vs **Relationship** (poor customer success responsiveness).
* **Drill 8: Unplanned Database Failover**: Divide into **Hardware/Host Failure** (disk I/O exhaustion, memory leak) vs **Software/Query Lockout** (deadlocks, unindexed table scans during backup).
* **Drill 9: Data Lake Storage Cost Surge**: Divide into **Ingestion Volume** (unfiltered debug telemetry) vs **Lifecycle Management** (lack of automatic tiering to S3 Glacier) vs **Duplicate Replication**.
* **Drill 10: Logistics Delivery Delays in Tokyo**: Divide into **Sorting Hub Processing** (scanner breakdowns, labor shortages) vs **Last-Mile Transportation** (traffic congestion, parking search, failed first-attempt deliveries).
* **Drill 11: Corporate Cybersecurity Phishing Failures**: Divide into **Technical Filters** (spam gateway misconfiguration) vs **Employee Awareness** (lack of simulated drills) vs **Process Controls** (lack of multi-factor authentication).
* **Drill 12: Declining POS Loyalty Program Sign-ups**: Divide into **Cashier Behavior** (speed pressure skipping pitch) vs **Customer Value Proposition** (trivial reward points, tedious paper form).
* **Drill 13: High LLM API Token Spend**: Divide into **Prompt Bloat** (unnecessarily massive context windows, redundant system instructions) vs **Architecture Inefficiency** (calling GPT-4 for simple classification instead of fine-tuned small language models).
* **Drill 14: Smart Meter Telemetry Packet Drop (15%)**: Divide into **Wireless Mesh Congestion** (radio frequency collisions) vs **Meter Firmware Hangs** vs **Concentrator Gateway Backhaul Failure**.
* **Drill 15: Cross-Border Team Project Delivery Delay**: Divide into **Communication & Language** (ambiguous requirement specs, timezone lag) vs **Technical Misalignment** (disparate environments, merge conflicts) vs **Scope Creep**.

---

## 4. Ten Market Sizing & Guesstimate Problems

### Guesstimate 1: Annual Market for Commercial Cloud Gaming in Japan
* **Clarifying Questions**: Hardware streaming to mobile and PC; paid subscriptions.
* **Step-by-Step Mathematical Sizing**:
  1. **Population of Japan**: 125 Million.
  2. **Target Demographics**: Gamers aged 15–45 $\approx 30\%$ of population $= 37.5\text{M people}$.
  3. **Cloud Gaming Adoption**: Currently niche $\approx 8\%$ of gamers $= 3.0\text{M active cloud gamers}$.
  4. **Average Revenue per User (ARPU)**: JPY 1,500 monthly subscription (e.g., Xbox Cloud Gaming / GeForce NOW) $\implies \text{JPY } 18,000 / \text{year}$.
  5. **In-game Purchases / Microtransactions**: Additional JPY 5,000 / year.
  6. **Total Annual Spend per User**: JPY 23,000.
  7. **Total Market Size**: $3.0\text{M users} \times \text{JPY } 23,000 = \mathbf{\text{JPY } 69\text{ Billion}}$ (~USD 460M).
* **Sanity Check**: Represents ~3.5% of Japan's total JPY 2 Trillion domestic gaming software market, which is logically sound for cloud streaming penetration.

---

### Guesstimate 2: Number of Daily Convenience Store (*Konbini*) Transactions in Tokyo
* **Approach**: Supply-Side (Store Count $\times$ Daily Transactions per Store).
* **Calculations**:
  1. Tokyo Population: 14 Million daytime population (including commuters) $\approx 16$ Million.
  2. Convenience store density in Tokyo: ~1 store per 2,000 residents $\implies \frac{16,000,000}{2,000} \approx \mathbf{8,000 \text{ stores}}$ (7-Eleven, Lawson, FamilyMart).
  3. Operating hours: 24 hours/day. Peak morning rush (7–9 AM), lunch rush (12–1 PM), evening (6–8 PM).
  4. Average customer flow: Peak hours (120 customers/hr $\times$ 5 peak hrs = 600); Off-peak (30 customers/hr $\times$ 19 hrs = 570) $\implies \approx \mathbf{1,170 \text{ customers/store/day}}$.
  5. Total Daily Transactions: $8,000 \text{ stores} \times 1,170 \approx \mathbf{9.36 \text{ Million transactions/day}}$.
* **Sanity Check**: Demand-side check: 16M people visiting a konbini on average 0.6 times daily $= 9.6\text{M transactions}$. Closely aligns!

---

### Guesstimate 3: Annual Market for Smart Factory IoT Sensors in Japanese Manufacturing
* **Approach**: Machine base $\times$ Sensorization rate $\times$ Unit sensor cost.
* **Calculations**:
  1. Manufacturing plants in Japan: ~200,000 facilities.
  2. Large and medium automated plants: Top 10% $= 20,000 \text{ plants}$.
  3. Average industrial machines per plant: 50 CNC, robotic, or press machines $\implies 1,000,000 \text{ target machines}$.
  4. Annual sensor retrofit adoption rate: 10% of fleet annually $= 100,000 \text{ machines/year}$.
  5. Sensors per machine: 4 sensor points (vibration, temperature, current, acoustic) $= 400,000 \text{ sensors/year}$.
  6. Blended sensor hardware + installation cost: JPY 50,000 per sensor point.
  7. **Hardware & Installation Market**: $400,000 \times 50,000 = \text{JPY } 20\text{ Billion}$.
  8. Cloud IoT Software Subscription: JPY 3,000 / machine / month $\times 12 = \text{JPY } 36,000 \times 100,000 = \text{JPY } 3.6\text{B}$.
  9. **Total Annual Market**: $\mathbf{\text{JPY } 23.6 \text{ Billion}}$ (~USD 160M).

---

### Guesstimates 4–10 Summaries:
* **Guesstimate 4: Annual Mobile Commuter Pass (*Suica/Pasmo*) Digital Recharges in Tokyo Metro**: 14M population $\times$ 60% transit commuter share $= 8.4\text{M daily users} \times 20 \text{ work days/mo} \times 12 \text{ mos} \times \text{JPY } 600/\text{trip} \approx \mathbf{\text{JPY } 1.2 \text{ Trillion/year}}$.
* **Guesstimate 5: Number of Commercial Passenger Flights Landing Daily at Tokyo Haneda & Narita**: Haneda (4 runways, ~1,300 daily movements) + Narita (2 runways, ~700 daily movements) $\implies \mathbf{\sim 1,000 \text{ landing flights daily}}$.
* **Guesstimate 6: Annual Data Center Power Consumption in Tokyo Metropolitan Area**: 150 enterprise data centers $\times$ average 20 MW IT load $\times 8,760 \text{ hours/year} \times \text{PUE } 1.4 \approx \mathbf{36.8 \text{ Terawatt-hours (TWh)/year}}$ (~4% of Japan's total electricity).
* **Guesstimate 7: Annual Number of Food Delivery App Orders in Japan**: 50M households $\times$ 15% adoption $\times$ 2.5 orders/month $\times 12 \text{ months} \approx \mathbf{225 \text{ Million orders/year}}$.
* **Guesstimate 8: Annual Market for Enterprise Cybersecurity Services in Japan**: 10,000 large enterprises $\times$ average JPY 40M annual cybersecurity spend $+ 50,000$ mid-market firms $\times$ JPY 6M annual spend $\approx \mathbf{\text{JPY } 700 \text{ Billion}}$ (~USD 4.7B).
* **Guesstimate 9: Total Active Shared Electric Scooters (Luup) in Tokyo**: 500 square km central Tokyo $\times$ 8 scooters per sq km $\approx \mathbf{4,000 \text{ active scooters}}$, generating ~24,000 daily trips.
* **Guesstimate 10: Annual Number of Automated Teller Machine (ATM) Transactions in Japan**: 120,000 ATMs $\times$ 150 transactions/day $\times 365 \text{ days} \approx \mathbf{6.57 \text{ Billion ATM transactions/year}}$.
