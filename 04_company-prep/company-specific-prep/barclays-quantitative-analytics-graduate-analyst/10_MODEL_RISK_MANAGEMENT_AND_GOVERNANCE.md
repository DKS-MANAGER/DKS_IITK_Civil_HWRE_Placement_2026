# 10 — Model Risk Management (MRM) & Regulatory Governance

## IIT Kanpur Placement Preparation — Barclays Quantitative Analytics (QA Model Monitoring)

---

### Executive Overview & Definition of Model Risk

In modern institutional banking, mathematical models drive lending approvals, capital allocation, impairment provisioning, automated pricing, and regulatory reporting. While quantitative models enhance precision and operational efficiency, they introduce **Model Risk**: the potential for adverse financial losses, regulatory sanctions, or reputational damage arising from decisions based on incorrect or misused model outputs.

Under the definitive global regulatory guidance (**US Federal Reserve SR 11-7 / OCC 2011-12** and the **Bank of England PRA SS1/23**), model risk stems from two foundational failure modes:
1. **Fundamental Conceptual & Design Errors:** The model contains theoretical flaws, unverified mathematical assumptions, biased estimation algorithms, or unrepresentative historical training data.
2. **Implementation Flaws & Operational Misuse:** Errors in the production software pipeline, unmonitored feature drift, or application of the model to customer populations or economic regimes outside its documented design scope.

In Barclays, the **QA Model Monitoring** team acts as the ongoing quantitative surveillance engine within the First Line of Defense, ensuring that deployed models remain reliable, compliant, and continuously controlled throughout their active lifecycle.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                      Barclays Model Risk Management Architecture                       │
├───────────────────────────────┬────────────────────────────────┬───────────────────────┤
│ 1st Line of Defense (1LoD)    │ 2nd Line of Defense (2LoD)     │ 3rd Line of Defense   │
│ Model Dev & Model Monitoring  │ Independent Model Review (IMR) │ Internal Audit (BIA)  │
├───────────────────────────────┼────────────────────────────────┼───────────────────────┤
│ • Quantitative model dev.     │ • Independent validation.      │ • Independent         │
│ • Ongoing live surveillance   │ • Conceptual soundness audit.  │   assurance of 1LoD   │
│   (QA Model Monitoring).      │ • Challenger model building.   │   and 2LoD framework. │
│ • Monthly/Quarterly Model     │ • Annual model performance     │ • Verification of     │
│   Monitoring Packs (MMP).     │   review & re-certification.   │   regulatory MRM      │
│ • Remediation & PMA proposal. │ • Model policy enforcement.    │   compliance.         │
└───────────────────────────────┴────────────────────────────────┴───────────────────────┘
```

---

### 1. Global Regulatory Standards: SR 11-7 & PRA SS1/23

Barclays operates across both UK/European and US regulatory jurisdictions, subjecting its Model Risk Management framework to concurrent supervisory standards.

```
┌───────────────────────────────────┬────────────────────────────────────────────────────────────┐
│ Regulatory Mandate                │ Core Requirements & Scope for Model Monitoring             │
├───────────────────────────────────┼────────────────────────────────────────────────────────────┤
│ US Federal Reserve SR 11-7 /      │ • Formal definition of "Model" vs "Calculator/Heuristic".   │
│ OCC 2011-12                       │ • Rigorous development, implementation, and use.           │
│ "Supervisory Guidance on Model    │ • Comprehensive independent model validation (2LoD).       │
│ Risk Management"                  │ • Ongoing monitoring: process verification, benchmarking,  │
│                                   │   and performance outcomes analysis.                       │
├───────────────────────────────────┼────────────────────────────────────────────────────────────┤
│ Bank of England PRA SS1/23        │ • Effective from May 2024 for UK banking institutions.     │
│ "Model Risk Management            │ • Establishes 5 Core Principles:                           │
│ Principles for Banks"             │   - Principle 1: Model risk governance framework.          │
│                                   │   - Principle 2: Model identification & inventory.         │
│                                   │   - Principle 3: Model development, implementation & use.  │
│                                   │   - Principle 4: Independent model validation.             │
│                                   │   - Principle 5: Ongoing monitoring and review.            │
│                                   │ • Strict mandates on Post-Model Adjustment (PMA) sunset.   │
├───────────────────────────────────┼────────────────────────────────────────────────────────────┤
│ European Central Bank (ECB) TRIM  │ • Targeted Review of Internal Models for credit, market,   │
│ & EBA Guidelines                  │   and counterparty risk under the Single Supervisory Mech. │
└───────────────────────────────────┴────────────────────────────────────────────────────────────┘
```

#### Official Regulatory Definition of a "Model" (SR 11-7)
> *"A quantitative method, system, or approach that applies statistical, economic, financial, or mathematical theories, techniques, and assumptions to process input data into quantitative estimates."*

A model consists of three distinct components:
1. **Information Input:** Economic indicators, borrower credit history, accounting records.
2. **Processing Component:** Statistical algorithms, regression equations, machine learning logic.
3. **Reporting Component:** Output estimates utilized for business or regulatory decision-making (e.g., credit decision, risk rating, capital calculation, loss provision).

Tactical deterministic calculations (e.g., compounding interest via a fixed algebraic equation or reporting standard account balances) are classified as **User Developed Applications (UDAs)** or tools, which follow lighter governance than formal statistical models.

---

### 2. Model Tiering & Inventory Management

Not all models carry equal risk. Barclays maintains an exhaustive, centralized **Enterprise Model Inventory** that catalogues every active, developing, or decommissioned model across the Group. Each model is assigned a **Model Risk Tier (Tier 1, Tier 2, or Tier 3)** based on financial materiality, business impact, and complexity.

```
┌──────────┬─────────────────────────────┬────────────────────────────────┬──────────────────────────┐
│ Risk     │ Materiality & Impact        │ Typical Models in Barclays     │ Monitoring & Validation  │
│ Tier     │ Criteria                    │                                │ Governance Mandate       │
├──────────┼─────────────────────────────┼────────────────────────────────┼──────────────────────────┤
│ Tier 1   │ Financial impact > £100M,   │ • Basel A-IRB PD/LGD/EAD       │ • Full independent       │
│ (High    │ regulatory capital impact,  │ • IFRS 9 ECL Impairment        │   validation annually.   │
│  Risk)   │ board-level disclosure, or  │ • BoE / Fed Stress Testing     │ • Monthly/Quarterly      │
│          │ automated credit decisions. │ • Front Office Algo Trading    │   formal Model           │
│          │                             │ • Fraud Prevention Engines     │   Monitoring Pack (MMP). │
├──────────┼─────────────────────────────┼────────────────────────────────┼──────────────────────────┤
│ Tier 2   │ Financial impact £20M–£100M,│ • SME Underwriting Scorecards  │ • Validation every       │
│ (Medium  │ operational pricing,        │ • Marketing Propensity Models  │   24 months.             │
│  Risk)   │ customer attrition models.  │ • Deposit Attrition Models     │ • Quarterly monitoring.  │
├──────────┼─────────────────────────────┼────────────────────────────────┼──────────────────────────┤
│ Tier 3   │ Financial impact < £20M,    │ • Desktop tactical tools       │ • Validation every       │
│ (Low     │ internal management         │ • Heuristic ranking benchmarks │   36 months.             │
│  Risk)   │ information (MIS).          │ • Departmental calculators     │ • Semi-annual or annual  │
│          │                             │                                │   monitoring summary.    │
└──────────┴─────────────────────────────┴────────────────────────────────┴──────────────────────────┘
```

---

### 3. Model Lifecycle & Change Management

The model lifecycle progresses through six sequential, auditable stages:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                              The End-to-End Model Lifecycle                            │
└────────────────────────────────────────────────────────────────────────────────────────┘
  1. Conception & Model Design Document (MDD)
       │
       ▼
  2. Model Development & In-Sample / Out-of-Time Testing (1LoD Dev)
       │
       ▼
  3. Independent Model Review & Validation Sign-Off (2LoD IMR)
       │
       ▼
  4. Governance Approval (Model Risk Governance Committee & Regulators)
       │
       ▼
  5. Deployment into Production Infrastructure & Automated Pipeline
       │
       ▼
  6. Ongoing Model Monitoring & Annual Review (1LoD QA Model Monitoring)
       │
       ├─────────────────────────────────┬─────────────────────────────────┐
       ▼                                 ▼                                 ▼
   No Action Required          Minor Recalibration               Model Retirement & Rebuild
   (Green status)              (Amber / Parameter Drift)         (Red breach / Conceptual Flaw)
```

#### Material vs. Minor Model Changes
Under PRA SS1/23 and ECB regulations, any alteration to a production model must be classified before implementation:

```
┌─────────────────────────────────┬─────────────────────────────────┐
│ Material Model Change           │ Minor Model Change              │
├─────────────────────────────────┼─────────────────────────────────┤
│ • Quantitative impact:          │ • Quantitative impact:          │
│   RWA change > 5% or ECL > 5%.  │   RWA change < 5% and ECL < 5%. │
│ • Change in mathematical        │ • Routine annual parameter      │
│   architecture (e.g., Logistic  │   update within pre-approved    │
│   Scorecard -> XGBoost).        │   recalibration boundaries.     │
│ • Change in definition of       │ • Technical bug fix in ETL code │
│   default (e.g., 90 DPD rule).  │   with negligible score shift.  │
│ • Mandatory Requirement:        │ • Mandatory Requirement:        │
│   Requires formal pre-approval  │   Requires 2LoD IMR sign-off    │
│   from the PRA / Fed before     │   and post-implementation       │
│   deployment in production!     │   quarterly notification.       │
└─────────────────────────────────┴─────────────────────────────────┘
```

---

### 4. The Model Monitoring Pack (MMP) & Committee Governance

The primary operational deliverable of a Graduate Analyst in Barclays Risk QA is the **Model Monitoring Pack (MMP)**. Distributed to executive risk committees on a monthly or quarterly cadence, the MMP provides an auditable, evidence-based performance assessment of deployed model suites.

#### Standard Structure of a Barclays Model Monitoring Pack
1. **Executive Summary & Dashboard:**
   - Portfolio overview: active loan count, outstanding balances, total drawn exposure.
   - Master Traffic-Light Summary (Red / Amber / Green) across all monitored models.
   - Active Post-Model Adjustments (PMAs) and current drawdown levels.
2. **Data Integrity & Lineage Verification:**
   - Upstream SQL ingestion record counts, missing value rates, and automated pipeline latency.
   - Outlier detection and variable range checks.
3. **Population & Feature Stability (PSI & CSI):**
   - Quarterly score distribution plots vs. development baseline.
   - Feature-level CSI tables highlighting shifting demographic or behavioral drivers.
4. **Discrimination Performance (Rank-Ordering):**
   - 12-month trailing ROC-AUC, Gini, and Kolmogorov-Smirnov (KS) trajectories.
   - Decile bad-rate separation and rank-order monotonicity checks.
5. **Calibration & Back-Testing (Accuracy):**
   - Observed vs. Expected ($O/E$) default ratios by internal rating grade.
   - Binomial test $Z$-scores and Hosmer-Lemeshow goodness-of-fit statistics.
6. **Policy Overrides & Usage Analysis:**
   - Underwriter manual override frequency, notch-upgrade vs. downgrade distribution, and subsequent performance of overridden accounts.
7. **Remediation Action Plan & Governance Approvals:**
   - Formal recommendations for parameter updates, PMA sizing, or model re-development.

#### Barclays Governance Committees Hierarchy
```
┌───────────────────────────────────────────────────────────┐
│               Barclays Board Risk Committee               │
│               (Ultimate Board Oversight)                  │
└─────────────────────────────▲─────────────────────────────┘
                              │
┌─────────────────────────────┴─────────────────────────────┐
│          Model Risk Governance Committee (MRGC)           │
│  (Chaired by Head of Enterprise Risk; approves Tier 1 MMP)│
└─────────────────────────────▲─────────────────────────────┘
                              │
┌─────────────────────────────┴─────────────────────────────┐
│         Technical Approval Committee (Risk QA TAC)        │
│   (Senior Quant Analytics Leads; reviews technical MMP)   │
└─────────────────────────────▲─────────────────────────────┘
                              │
┌─────────────────────────────┴─────────────────────────────┐
│    1LoD QA Model Monitoring & 2LoD Independent Review     │
└───────────────────────────────────────────────────────────┘
```

---

### 5. Post-Model Adjustments (PMA) Governance & PRA SS1/23 Compliance

One of the most heavily scrutinized areas in modern model risk management is the application and persistence of Post-Model Adjustments.

#### The 5 Pillars of Compliant PMA Governance:
1. **Formal Justification & Documentation:** Every PMA must have an accompanying quantitative paper detailing the specific model limitation, root cause, and why algorithmic recalibration cannot immediately resolve the deficit.
2. **Transparent Quantification Methodology:** Heuristic "expert guesses" are strictly prohibited. Overlays must be derived using transparent satellite regression models, stress testing analogues, or external credit bureau benchmarks.
3. **Independent Review Sign-Off:** All Tier 1 PMAs exceeding materiality thresholds (£10M capital or provision impact) must receive written concurrence from 2LoD IMR and approval from the Chief Risk Officer.
4. **Mandatory Sunset Plan:** Under PRA SS1/23, every PMA must feature an explicit exit strategy with a predetermined expiration date (typically not exceeding 12 months).
5. **Re-development Trigger:** If an underlying structural shift causes a PMA to remain active across 4 consecutive quarterly reporting cycles, Risk QA must automatically initiate a formal model rebuild project to integrate the effect directly into the production code.

---

### 6. Audit Trails, Code Governance & Production Control

To satisfy internal audit (Barclays Internal Audit — BIA) and external regulators (PRA, ECB, Fed, PwC/EY), Model Monitoring pipelines must exhibit end-to-end mathematical reproducibility.

#### Best Practices Enforced in Barclays Risk QA:
- **Version Control & Repository Discipline:** All SQL extraction queries, Python analytical scripts, and Excel automated workbooks must be managed under Git version control with atomic commit histories and peer-reviewed pull requests.
- **Data Lineage Immutability:** Monitoring datasets must snapshot raw production data partitions with immutable timestamps, ensuring that any historical MMP metric can be replicated exactly years later.
- **Automated Sanity Asserts:** Production scripts must execute automated sanity assertions (e.g., verifying that probabilities are bounded in $[0, 1]$, decile sums equal 100%, and SQL primary keys contain zero duplicates) before generating committee outputs.
- **Clear Segregation of Duties:** The analyst who builds the monitoring pack cannot independently approve the resolution of an Amber or Red breach; formal committee governance is required.

---

*Authoritative cross-reference: US Federal Reserve Board SR Letter 11-7 / OCC Bulletin 2011-12 ("Guidance on Model Risk Management"); Bank of England Prudential Regulation Authority (PRA) Supervisory Statement SS1/23 ("Model risk management principles for banks"); Barclays Enterprise Model Risk Policy (EMRP).*

