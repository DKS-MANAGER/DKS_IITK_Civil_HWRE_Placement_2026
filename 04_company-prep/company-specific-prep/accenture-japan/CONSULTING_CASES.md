# Consulting Cases, Issue Trees & Market Sizing — Master Practice Suite

> **Document Status**: Comprehensive Case Interview Practice Workbook  
> **Target Role**: Digital Consultant, Accenture Japan Ltd. (`[JD VERIFIED]`)  
> **Coverage**: 15 End-to-End Enterprise Digital Cases (10-Point Analysis Structure), 15 MECE Issue-Tree / Root-Cause Drills, and 10 Structured Market Sizing Guesstimates.  
> **Classification**: All corporate scenarios, client names, monetary sums, and operational metrics are explicitly `[PRACTICE ASSUMPTION]`.

---

## 1. The 10-Point Digital Case Interview Architecture

Every case in this workbook is structured according to the standard 10-point digital consulting analysis framework:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                       10-POINT CASE ANALYSIS STRUCTURE                      │
├──────────────────────────┬──────────────────────────┬───────────────────────┤
│ 1. Problem Statement     │ 2. Clarifying Questions  │ 3. Structural Tree    │
│ 4. Data Required         │ 5. Analysis & Tech Plan  │ 6. Calculations       │
│ 7. Business Insights     │ 8. Recommendations       │ 9. Risks & Mitigation │
│ 10. Executive Follow-ups │                          │                       │
└──────────────────────────┴──────────────────────────┴───────────────────────┘
```

---

## 2. Fifteen End-to-End Digital Transformation Cases

### Case 1: Industry X — Smart Factory Transformation for a Japanese Robotics Manufacturer
1. **Problem Statement**: An industrial robotics manufacturer with 4 plants in Kanto faces a 22% increase in machine breakdown downtime over 2 years, resulting in JPY 450M annual lost gross margin. Goal: eliminate unscheduled downtime and improve Overall Equipment Effectiveness (OEE).
2. **Clarifying Questions**: What is current OEE? (72%). Are machines currently sensorized? (Only basic PLC cycle counters). What is the average repair lead time? (48 hours due to spare parts logistics).
3. **Framework**: Break down into Failure Prevention (IoT sensors, Edge anomaly detection) vs Repair Acceleration (AR technician tablets, automated spare parts inventory).
4. **Data Required**: Machine telemetry failure logs, maintenance repair orders, component spare part inventory turnover, MTBF (Mean Time Between Failures) and MTTR (Mean Time to Repair).
5. **Analysis & Tech Plan**: Deploy vibration and acoustic sensors on 50 critical CNC cutting machines. Stream high-frequency telemetry to factory Edge gateways running microsecond anomaly detection; push 10-second aggregations via MQTT to Azure IoT Hub. Run cloud predictive maintenance models forecasting component failure 48 hours prior.
6. **Calculations**:
   * Current breakdown losses = JPY 450M.
   * IoT Predictive Maintenance prevents 70% of unplanned downtime $\implies 450 \times 0.70 = \text{JPY } 315\text{M}$ saved annually.
   * System CapEx & Year 1 OpEx = JPY 85M $\implies \text{Net Year 1 Gain} = \text{JPY } 230\text{M}$.
7. **Interpretation**: Payback is achieved in under 4 months; primary bottleneck shifts from equipment breakdown to technician dispatch scheduling.
8. **Recommendation & Trade-offs**: Pilot on Plant 1 assembly line for 90 days before company-wide rollout. Trade-off: edge hardware CapEx vs cloud SaaS subscription.
9. **Risks & Limitations**: Worker resistance on shop floor; legacy machines lacking digital bus outputs (requires retrofitting non-invasive clip-on sensors).
10. **Follow-up Questions**: *"How do you handle edge node network dropouts during network maintenance?"* (Edge local circular buffer caches 48 hours of telemetry).

---

### Case 2: Enterprise GenAI / RAG — Policy Search for a Japanese Life Insurer
1. **Problem Statement**: Claims adjusters at a Tokyo life insurer spend 3.5 hours daily manually cross-referencing 80,000 legacy PDF policy guidelines, delaying claim payouts to 14 days and causing customer dissatisfaction.
2. **Clarifying Questions**: Are policies bilingual? (Pure Japanese). Are customer medical records attached? (Yes, PII protection is paramount).
3. **Framework**: Enterprise RAG Architecture: Document Ingestion $\to$ Chunking & Embedding $\to$ Hybrid Vector Search $\to$ LLM Synthesis with Grounded Citations $\to$ Role-Based Access Control (RBAC).
4. **Data Required**: Document taxonomy, historical claims queries, sample policy PDFs, adjuster review audit logs.
5. **Analysis & Tech Plan**: Ingest documents into Azure AI Search; generate vector embeddings using OpenAI `text-embedding-3-large`. When adjuster inputs claim details, perform hybrid search (BM25 keyword + dense vector cosine similarity). Prompt GPT-4o with top-5 retrieved chunks to extract policy coverage with exact page citations.
6. **Calculations**:
   * 1,000 adjusters saving 2.5 hours/day $= 2,500 \text{ hours daily} \times \text{JPY } 4,000/\text{hr} = \text{JPY } 10\text{M daily savings}$.
   * Annual productivity value $= \text{JPY } 2.4\text{B}$. Azure infrastructure & LLM token API cost $\approx \text{JPY } 60\text{M/year}$.
7. **Interpretation**: 40x ROI with immediate SLA reduction from 14 days to 48 hours.
8. **Recommendation**: Implement human-in-the-loop review: adjuster must approve generated claim decision; zero automatic payouts during Phase 1.
9. **Risks**: Hallucination on obscure policy amendments; data leakage of confidential policy clauses.
10. **Follow-up Questions**: *"What if the LLM cites a repealed 2018 policy clause instead of the 2024 update?"* (Implement metadata date filtering on vector index chunks).

---

### Case 3: Cloud Migration — Core Banking Modernization for a Regional Japanese Bank
1. **Problem Statement**: A regional bank in Kansai spends 75% of its annual IT budget maintaining a 30-year-old on-premise COBOL mainframe, preventing mobile banking feature releases.
2. **Clarifying Questions**: What is the regulatory constraint? (FSA Japan compliance requires financial data residency in Japan). Can we do big-bang migration? (No, mission-critical ledger cannot experience downtime).
3. **Framework**: Strangler Fig Pattern: incrementally wrap legacy mainframe with modern REST APIs and migrate read-heavy services first.
4. **Data Required**: Transaction volume (TPS), batch processing windows, database dependency maps, licensing costs.
5. **Analysis & Tech Plan**: Deploy AWS Tokyo and Osaka multi-region active-standby architecture. Build event-driven integration layer using Apache Kafka. Migrate customer portal and mobile banking read queries to PostgreSQL on Amazon Aurora. Keep core ledger on mainframe during Year 1, decoupling account balances via change-data-capture (CDC).
6. **Calculations**:
   * Current mainframe run cost = JPY 1,800M/year. Target hybrid cloud run cost = JPY 700M/year.
   * Migration CapEx over 3 years = JPY 2,200M. Annual run savings post-Year 3 = JPY 1,100M/year.
7. **Interpretation**: Migration pays for itself in 5 years while increasing developer release velocity from twice a year to bi-weekly.
8. **Recommendation**: Start with non-critical mobile statements service to validate cloud security compliance before migrating credit cards.
9. **Risks**: Legacy COBOL batch logic undocumented; transaction data drift between cloud cache and core ledger.
10. **Follow-up Questions**: *"How do you satisfy Japan FSA audits regarding cloud disaster recovery?"* (Demonstrate cross-region active replication between Tokyo and Osaka with RPO $< 1$ second and RTO $< 15$ minutes).

---

### Case 4: Omnichannel Retail — Preventing Point-of-Sale Inventory Stock-Outs
1. **Problem Statement**: A convenience store franchise with 2,500 stores across Japan suffers 8% lost sales due to daily evening bento and beverage stock-outs.
2. **Clarifying Questions**: How often is inventory replenished? (Twice daily from central distribution centers). What data is logged at POS? (Timestamp, item SKU, quantity, payment method).
3. **Framework**: Demand Forecasting (AI/ML) + Supply Chain Visibility (RFID/IoT telemetry) + Store Replenishment Optimization.
4. **Data Required**: Historical POS receipts, local weather forecasts, foot traffic, public transit disruption feeds, delivery truck GPS.
5. **Analysis Plan**: Build automated machine learning pipeline (XGBoost/LightGBM) forecasting store-level hourly demand incorporating rain/temperature anomalies. Feed store replenishment quantities directly to dispatch center ERP by 10:00 AM.
6. **Calculations**:
   * Annual retail sales = JPY 150B. 8% lost sales = JPY 12B opportunity.
   * Reducing stock-outs by 50% captures JPY 6B in recovered sales at 25% gross margin $= \text{JPY } 1.5\text{B gross profit boost}$.
   * IoT and analytics platform deployment = JPY 350M.
7. **Interpretation**: 4.3x Year 1 ROI with simultaneous food waste reduction by 15%.
8. **Recommendation**: Deploy digital handheld scanning for delivery drivers to confirm receipt automatically without manual paper manifests.
9. **Risks**: Store manager distrust of automated AI ordering suggestions; sudden weather forecast shifts after 10:00 AM dispatch.
10. **Follow-up Questions**: *"How do you handle store managers who override the AI recommendations?"* (Implement gamified store dashboard showing waste vs lost sale metrics).

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
