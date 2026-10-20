# 07. Program Management: Practice Cases & Solutions

> **Track**: Technical Program Management (TPM) & Corporate Program Governance  
> **Target Audience**: IIT Kanpur candidates preparing for Program Manager, Technical Project Lead, and Strategic Operations interview loops.  
> **Content Structure**: Complex dependency networks, Earned Value financial audits, cross-functional deadlock resolution, and executive defenses.

---

## Case 1: Multi-Service Cloud Modernization Schedule Network

### Program Context
You are the Lead Program Manager overseeing the migration of a legacy monolithic core banking architecture to a distributed microservices cloud platform. The program comprises 8 interdependent technical workstreams:

| Activity | Workstream Description | Predecessors | Duration ($D_i$, Weeks) | Direct Budget ($₹\text{ Lakhs}$) |
| :---: | :--- | :---: | :---: | :---: |
| **A** | Data Classification & Security Architecture | None | 4 | 25 |
| **B** | Cloud VPC & Landing Zone Infrastructure | A | 6 | 40 |
| **C** | Database Schema Migration & Pipeline | A | 8 | 50 |
| **D** | Authentication & RBAC Microservice | B | 5 | 30 |
| **E** | Payment Processing Core Microservice | B, C | 7 | 60 |
| **F** | Frontend Web & Mobile Client Updates | D | 4 | 20 |
| **G** | End-to-End Penetration & Stress Testing | E, F | 6 | 35 |
| **H** | Production Cutover & Regulatory Audit | G | 3 | 20 |

---

### Step-by-Step Mathematical Analysis

#### 1. Forward Pass: Earliest Start ($ES$) & Earliest Finish ($EF$)
- Activity A: $ES = 0 \implies EF = 0 + 4 = \mathbf{4\text{ weeks}}$
- Activity B: $ES = 4 \implies EF = 4 + 6 = \mathbf{10\text{ weeks}}$
- Activity C: $ES = 4 \implies EF = 4 + 8 = \mathbf{12\text{ weeks}}$
- Activity D: $ES = 10 \implies EF = 10 + 5 = \mathbf{15\text{ weeks}}$
- Activity E: Predecessors B ($EF = 10$) and C ($EF = 12$).
  $$ES_E = \max(10, 12) = 12 \implies EF = 12 + 7 = \mathbf{19\text{ weeks}}$$
- Activity F: $ES_F = 15 \implies EF = 15 + 4 = \mathbf{19\text{ weeks}}$
- Activity G: Predecessors E ($EF = 19$) and F ($EF = 19$).
  $$ES_G = \max(19, 19) = 19 \implies EF = 19 + 6 = \mathbf{25\text{ weeks}}$$
- Activity H: $ES_H = 25 \implies EF = 25 + 3 = \mathbf{28\text{ weeks}}$

**Minimum Program Duration**: **28 Weeks**.

#### 2. Backward Pass: Latest Finish ($LF$) & Latest Start ($LS$)
Set $LF_H = 28\text{ weeks}$:
- Activity H: $LF = 28 \implies LS = 28 - 3 = \mathbf{25\text{ weeks}}$
- Activity G: $LF = 25 \implies LS = 25 - 6 = \mathbf{19\text{ weeks}}$
- Activity E: $LF = 19 \implies LS = 19 - 7 = \mathbf{12\text{ weeks}}$
- Activity F: $LF = 19 \implies LS = 19 - 4 = \mathbf{15\text{ weeks}}$
- Activity D: $LF = 15 \implies LS = 15 - 5 = \mathbf{10\text{ weeks}}$
- Activity C: $LF = 12 \implies LS = 12 - 8 = \mathbf{4\text{ weeks}}$
- Activity B: Successors are D ($LS = 10$) and E ($LS = 12$).
  $$LF_B = \min(10, 12) = 10 \implies LS = 10 - 6 = \mathbf{4\text{ weeks}}$$
- Activity A: Successors are B ($LS = 4$) and C ($LS = 4$).
  $$LF_A = \min(4, 4) = 4 \implies LS = 4 - 4 = \mathbf{0\text{ weeks}}$$

#### 3. Float Matrix & Critical Path Identification
$$\text{Total Float } (TF) = LS - ES = LF - EF$$
$$\text{Free Float } (FF) = \min \{ES_{\text{successors}}\} - EF$$

| Activity | $ES$ | $EF$ | $LS$ | $LF$ | Total Float ($TF$) | Free Float ($FF$) | Critical Status |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **A** | 0 | 4 | 0 | 4 | **0** | **0** | **Critical** |
| **B** | 4 | 10 | 4 | 10 | **0** | **0** | **Critical (Branch 1)** |
| **C** | 4 | 12 | 4 | 12 | **0** | **0** | **Critical (Branch 2)** |
| **D** | 10 | 15 | 10 | 15 | **0** | **0** | **Critical (Branch 1)** |
| **E** | 12 | 19 | 12 | 19 | **0** | **0** | **Critical (Branch 2)** |
| **F** | 15 | 19 | 15 | 19 | **0** | **0** | **Critical (Branch 1)** |
| **G** | 19 | 25 | 19 | 25 | **0** | **0** | **Critical** |
| **H** | 25 | 28 | 25 | 28 | **0** | **0** | **Critical** |

**Crucial Program Observation**:
Notice that Path 1 ($A \to B \to D \to F \to G \to H$) and Path 2 ($A \to C \to E \to G \to H$) **both have a duration of exactly 28 weeks**! The project contains **two simultaneous critical paths**. Any delay on either the infrastructure/frontend side OR the database/payment side will delay the final migration.

---

## Case 2: Earned Value Management (EVM) Financial Audit

### Program Status at Week 16
You are conducting a mid-program EVM review for an Enterprise SaaS implementation.
- Total Program Budget at Completion ($BAC$): $₹5,00,00,000$ ($₹5\text{ Crores}$).
- Planned Duration: $25\text{ weeks}$.
- Status at Week 16:
  - Planned Value ($PV$): The baseline project plan specified that $68\%$ of total project work should be completed by Week 16 ($PV = 0.68 \times 5\text{ Cr} = ₹3,40,00,000$).
  - Earned Value ($EV$): Independent engineering audit confirms that only $52\%$ of total milestone deliverables are fully tested and accepted ($EV = 0.52 \times 5\text{ Cr} = ₹2,60,00,000$).
  - Actual Cost ($AC$): Financial accounting registers total cash disbursed to contractors and engineers at Week 16 as $₹3,20,00,000$ ($₹3.2\text{ Crores}$).

---

### Step-by-Step EVM Derivations

#### 1. Cost & Schedule Variances
$$CV = EV - AC = ₹2.60\text{ Cr} - ₹3.20\text{ Cr} = \mathbf{-₹60 \text{ Lakhs (Cost Overrun)}}$$
$$SV = EV - PV = ₹2.60\text{ Cr} - ₹3.40\text{ Cr} = \mathbf{-₹80 \text{ Lakhs (Schedule Delay)}}$$

#### 2. Performance Indices
$$CPI = \frac{EV}{AC} = \frac{2.60}{3.20} = \mathbf{0.8125} \quad (\text{For every rupee spent, the program generates only } ₹0.81 \text{ of progress})$$
$$SPI = \frac{EV}{PV} = \frac{2.60}{3.40} = \mathbf{0.7647} \quad (\text{The program is progressing at only } 76.5\% \text{ of its planned velocity})$$

#### 3. Program Forecasting (EAC & TCPI)
Assuming current operational inefficiency continues:
$$\text{Estimate at Completion } (EAC) = \frac{BAC}{CPI} = \frac{₹5.00\text{ Cr}}{0.8125} \approx \mathbf{₹6.154 \text{ Crores}}$$
$$\text{Projected Total Budget Overrun} = 6.154 - 5.00 = \mathbf{+₹1.154 \text{ Crores (23.1\% Over Budget)}}$$

To finish within the original $₹5\text{ Crore}$ budget on the remaining work:
$$\text{TCPI} = \frac{BAC - EV}{BAC - AC} = \frac{5.00 - 2.60}{5.00 - 3.20} = \frac{2.40}{1.80} = \mathbf{1.333}$$
*Interpretation*: To bring the project in on budget, the team must perform at a $CPI$ of $1.33$ (a $33\%$ increase in cost productivity over baseline), which is historically unfeasible without descoping non-essential features.

---

## Executive Interview Defense Probes

> **Q1**: *"If your project has two simultaneous critical paths as seen in Case 1, how do you allocate limited engineering resources during a crunch?"*  
> **Model Answer**: "When dual critical paths exist, standard float-based prioritization fails because both paths have zero float. I would prioritize based on **risk profile and architectural irreversibility**. Workstream C (Database Schema Migration) involves stateful database storage and data integrity risks; if it fails, rollback is complex and high-risk. In contrast, Workstream D/F (Frontend & RBAC) involves stateless application logic where external contractor staffing can be augmented more easily. Therefore, senior core engineers are anchored to the database/payment path, while contract resources augment the frontend path."

> **Q2**: *"In the EVM Case, the business sponsor demands adding 10 more engineers to catch up on the schedule delay. How would you advise them?"*  
> **Model Answer**: "I would caution the sponsor against blindly adding staff by invoking **Brooks's Law** (*'Adding manpower to a late software project makes it later'*). Onboarding 10 new engineers requires existing senior developers to spend time training them, increasing communication overhead ($n(n-1)/2$ communication channels) and temporarily decreasing net output. Instead, I would recommend: (1) Fast-tracking non-critical tasks that can be performed in parallel, (2) Descoping secondary 'P2' features to reduce the denominator of remaining work, and (3) Eliminating manual testing bottlenecks by investing in automated deployment test suites."
