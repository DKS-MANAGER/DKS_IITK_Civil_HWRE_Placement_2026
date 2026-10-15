# What To Study — 4 Core Preparation Blocks

> **Target Role**: Digital Consultant, Accenture Japan Ltd.  
> **Structure**: 4 Modular Preparation Blocks designed specifically for IIT engineering students transitioning to Digital Consulting.

---

## Preparation Master Map

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                       4 CORE PREPARATION BLOCKS                             │
├──────────────────────────────┬──────────────────────────────┬───────────────┤
│ BLOCK 1: Consulting &        │ BLOCK 2: Digital Technology │ BLOCK 3: Data │
│ Problem Structuring          │ Fundamentals                 │ & Technical   │
│ (Issue Trees, MECE, Cases)   │ (Cloud, AI, IoT, Industry X) │ Test Prep     │
├──────────────────────────────┴──────────────────────────────┴───────────────┤
│ BLOCK 4: Manager & Director Interview Mastery (Case, HR, Cross-Cultural)    │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Block 1 — Consulting / Structured Problem Solving

### 1. Concept: MECE & Issue Trees
**Mutually Exclusive, Collectively Exhaustive (MECE)** is the foundational principle of consulting problem solving. It ensures a problem is broken down into sub-components that do not overlap and leave no gaps.

#### Framework: Business Problem Diagnosis Tree
When a client experiences operational inefficiency or declining digital adoption:

```text
                                [Client Problem]
                                       │
            ┌──────────────────────────┴──────────────────────────┐
            ▼                                                     ▼
  [Internal / Technology Factors]                       [External / Process Factors]
            │                                                     │
   ┌────────┴────────┐                                   ┌────────┴────────┐
   ▼                 ▼                                   ▼                 ▼
[Legacy Systems] [Data Silos]                         [User Resistance] [Vendor Lock-in]
```

#### Worked Example: Digitizing a Manufacturing Client's Quality Control
* **Problem**: 12% defect rate in high-precision automotive components; manual visual inspection is slow and error-prone.
* **MECE Issue Tree Structure**:
  1. **Detection & Accuracy**: Can automated AI vision systems inspect components faster and with higher accuracy?
  2. **Data Integration**: Can inspection data feed directly into the ERP/MES pipeline in real-time?
  3. **Process & People**: How easily can floor workers adopt the new digital scanning tools?
* **Solution Architecture**: Implement edge AI cameras connected to an IoT hub, feeding real-time anomaly alerts to an Azure cloud analytics portal.

#### Practice Exercises & Canonical Repository Links:
* Study fundamental consulting issue trees in [`03_non_core/consulting/06_case-practice.md`](../../../03_non_core/consulting/06_case-practice.md#1-profitability-framework).
* Review structured frameworks in [`01_common/group-discussion/CASE_GD.md`](../../../01_common/group-discussion/CASE_GD.md).

---

## Block 2 — Digital Technology Fundamentals

The JD explicitly highlights: **Cloud, AI/Data Analytics, Industry X (Manufacturing Digitalization), IoT, XR, and Customer Experience (`[JD VERIFIED]`)**.

### 1. Technology Domain Summaries for Consultants

| Technology Domain | Core Technical Concept | Business Transformation Value | Consulting Use-Case Example |
| :--- | :--- | :--- | :--- |
| **Cloud Computing** | AWS/Azure/GCP, IaaS/PaaS/SaaS, Microservices, Serverless | Elastic scalability, shift from CapEx to OpEx, rapid deployment. | Legacy mainframe migration to Azure hybrid cloud for a Japanese bank. |
| **AI & Data Analytics** | LLM RAG pipelines, predictive analytics, data lakes, BI tools | Automated decision-making, predictive maintenance, personalized CX. | Deploying an AI chatbot for customer service in a retail enterprise. |
| **Industry X & IoT** | Smart sensors, Edge Computing, Digital Twins, MES integration | Real-time shop floor visibility, reduced machine downtime, defect reduction. | Sensorizing factory equipment in a Tokyo manufacturing plant. |
| **Enterprise Systems** | ERP (SAP S/4HANA), CRM (Salesforce), API Gateways | Single source of truth, automated cross-departmental workflows. | Unifying sales & inventory systems post-merger for a conglomerate. |

#### Concept Checklist & Repository Link:
* Deep-dive into technical architecture definitions in [`03_non_core/software-engineering/03_domain-knowledge.md`](../../../03_non_core/software-engineering/03_domain-knowledge.md).

---

## Block 3 — Data / Coding / Technical Test

### 1. Key Skill Requirements
Accenture Japan's technical test evaluates:
1. **Algorithmic Logic**: String manipulations, array filtering, hash maps, simple sorting (Python / C++).
2. **SQL Data Queries**: Multi-table JOINs, GROUP BY, aggregations, window functions.
3. **Analytical & Numerical Aptitude**: Data interpretation, chart analysis, logical flow reasoning.

#### Worked SQL Example: Client Digital Adoption Analysis
**Question**: Find the top 3 departments with the highest rate of digital tool adoption where user count > 50.

```sql
SELECT 
    d.department_name,
    COUNT(u.user_id) AS total_users,
    SUM(CASE WHEN u.active_digital_status = 'ACTIVE' THEN 1 ELSE 0 END) * 100.0 / COUNT(u.user_id) AS adoption_rate
FROM departments d
JOIN users u ON d.department_id = u.department_id
GROUP BY d.department_name
HAVING COUNT(u.user_id) > 50
ORDER BY adoption_rate DESC
LIMIT 3;
```

#### Practice System & Practice Links:
* Full practice test and solution set in [`TECHNICAL_TEST.md`](TECHNICAL_TEST.md).
* General reasoning practice in [`01_common/aptitude/logical-reasoning/coding-decoding.md`](../../../01_common/aptitude/logical-reasoning/coding-decoding.md).

---

## Block 4 — Case & Interview Mastery

### 1. Differentiated Round Strategy

```text
               ┌───────────────────────────────────────────────┐
               │              INTERVIEW PIPELINE               │
               └───────────────────────┬───────────────────────┘
                                       │
            ┌──────────────────────────┴──────────────────────────┐
            ▼                                                     ▼
 ┌──────────────────────┐                              ┌──────────────────────┐
 │     MANAGER ROUND    │                              │    DIRECTOR ROUND    │
 ├──────────────────────┤                              ├──────────────────────┤
 │ • Problem Structuring│                              │ • Business Impact    │
 │ • Tech Architecture  │                              │ • Strategic Vision   │
 │ • Project Deep-Dive  │                              │ • Why Japan/Accenture│
 │ • Technical Case     │                              │ • Leadership & Fit   │
 └──────────────────────┘                              └──────────────────────┘
```

#### Master Preparation Links:
* Case practice suite: [`CONSULTING_CASES.md`](CONSULTING_CASES.md).
* Manager vs Director question strategies: [`INTERVIEW.md`](INTERVIEW.md).
* Behavioral, HR & Japanese cultural preparation: [`BEHAVIOURAL_HR.md`](BEHAVIOURAL_HR.md).
