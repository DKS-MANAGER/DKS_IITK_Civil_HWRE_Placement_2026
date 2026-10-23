# 03. Program Management: Governance, CPM/PERT & Earned Value Systems

> **Track**: Technical Program Management (TPM) & Corporate Program Governance  
> **Target Audience**: IIT Kanpur students preparing for Program Manager, Project Lead, and Strategic Operations roles.  
> **Methodological Focus**: Network scheduling (CPM/PERT), Earned Value Management (EVM), multi-stakeholder RACI governance, and quantitative risk registers.

---

## 1. Taxonomy: Program Management vs. Project vs. Product

In corporate and engineering organizations, clarity of ownership is vital:

```text
┌─────────────────────────┬────────────────────────────────────────────────────────┐
│ Role                    │ Core Focus & Accountability                            │
├─────────────────────────┼────────────────────────────────────────────────────────┤
│ **Product Manager**     │ **"WHAT & WHY"**: Customer needs, market opportunity,  │
│                         │ feature definition, roadmap strategy, ROI metrics.     │
├─────────────────────────┼────────────────────────────────────────────────────────┤
│ **Project Manager**     │ **"WHEN & HOW (Single Scope)"**: Time, budget, scope,  │
│                         │ tactical delivery of an individual project sprint.     │
├─────────────────────────┼────────────────────────────────────────────────────────┤
│ **Program Manager**     │ **"ORCHESTRATION & VALUE (Multi-Project)"**: Managing  │
│                         │ inter-project dependencies, cross-functional alignment,│
│                         │ strategic risk mitigation, and executive governance.   │
└─────────────────────────┴────────────────────────────────────────────────────────┘
```

---

## 2. Quantitative Schedule Network Modeling: CPM & PERT

### A. Critical Path Method (CPM)
The Critical Path is the longest sequence of dependent activities through a project network; it dictates the **minimum possible completion time** for the entire program. Any delay to a critical path activity causes a day-for-day delay to final program delivery.

#### Calculation Mechanics (Two-Pass Analysis)
1. **Forward Pass (Earliest Times)**:
   - $ES_i = \max \{EF_{\text{predecessors}}\}$
   - $EF_i = ES_i + D_i$
2. **Backward Pass (Latest Times)**:
   - $LF_i = \min \{LS_{\text{successors}}\}$
   - $LS_i = LF_i - D_i$
3. **Float / Slack Analysis**:
   - **Total Float ($TF$)**: Maximum delay an activity can experience without delaying project completion:
     $$TF_i = LS_i - ES_i = LF_i - EF_i$$
     *(Activities on the Critical Path have $TF = 0$)*
   - **Free Float ($FF$)**: Maximum delay without impacting the earliest start of any subsequent activity:
     $$FF_i = \min \{ES_{\text{successors}}\} - EF_i$$
   - **Interfering Float**: $TF_i - FF_i$ (delay that absorbs buffer from downstream activities without impacting final project deadline).

### B. PERT 3-Point Probabilistic Scheduling
When task durations are uncertain (e.g., deep-tech R&D, new regulatory approvals), PERT models task times as Beta probability distributions:
- Optimistic time ($a$)
- Most likely time ($m$)
- Pessimistic time ($b$)

1. **Expected Task Duration ($t_e$)**:
   $$t_e = \frac{a + 4m + b}{6}$$
2. **Task Standard Deviation ($\sigma_i$) and Variance ($\sigma_i^2$)**:
   $$\sigma_i = \frac{b - a}{6} \implies \sigma_i^2 = \left(\frac{b - a}{6}\right)^2$$
3. **Program Completion Probability (Central Limit Theorem)**:
   Assuming independent critical path activities, the total critical path duration follows a normal distribution:
   $$\mu_{\text{project}} = \sum_{i \in CP} t_{e,i} \quad \text{and} \quad \sigma_{\text{project}} = \sqrt{\sum_{i \in CP} \sigma_i^2}$$
   The probability of finishing before target deadline $T_s$:
   $$Z = \frac{T_s - \mu_{\text{project}}}{\sigma_{\text{project}}} \implies P(T \le T_s) = \Phi(Z)$$

---

## 3. Earned Value Management (EVM) Systems

Earned Value Management integrates project scope, schedule, and cost performance into unified metrics:

```text
Planned Value (PV)  ──► The budgeted cost of work scheduled to be completed by date T.
Earned Value (EV)   ──► The budgeted cost of the work ACTUALLY completed by date T.
Actual Cost (AC)    ──► The real financial expenditure incurred to date T.
```

### Variances & Performance Indices
1. **Cost Variance ($CV$)**:
   $$CV = EV - AC \quad (CV > 0 \implies \text{Under Budget / Favorable})$$
2. **Schedule Variance ($SV$)**:
   $$SV = EV - PV \quad (SV > 0 \implies \text{Ahead of Schedule / Favorable})$$
3. **Cost Performance Index ($CPI$)**:
   $$CPI = \frac{EV}{AC} \quad (CPI > 1.0 \implies \text{Getting }> ₹1 \text{ of value per rupee spent})$$
4. **Schedule Performance Index ($SPI$)**:
   $$SPI = \frac{EV}{PV} \quad (SPI > 1.0 \implies \text{Progressing faster than planned})$$

### Forecasting Final Program Cost & Schedule
- **Estimate at Completion (EAC)** (assuming current cost performance continues):
  $$EAC = \frac{BAC}{CPI}$$
  *(Where $BAC$ is the total Budget at Completion)*
- **To-Complete Performance Index (TCPI)**:
  $$\text{TCPI} = \frac{BAC - EV}{BAC - AC}$$
  *(The cost efficiency the team must achieve on remaining work to finish within the original budget).*

---

## 4. Multi-Stakeholder Governance & Risk Architecture

### A. RACI Responsibility Assignment Matrix
- **R (Responsible)**: The person who does the work to achieve the task.
- **A (Accountable)**: The sole individual with final approval authority (*exactly one 'A' per deliverable*).
- **C (Consulted)**: Subject matter experts providing two-way input before decisions are locked.
- **I (Informed)**: Stakeholders kept updated on progress (one-way communication).

### B. Quantitative Risk Register & Heatmap
Each identified risk event is logged with:
$$\text{Risk Severity Score} = \text{Probability } (1\text{--}5) \times \text{Financial / Schedule Impact } (1\text{--}5)$$

```text
┌───────────────┬────────────────────────────────────────────────────────┐
│ Score (1-25)  │ Governance Response & Protocol                         │
├───────────────┼────────────────────────────────────────────────────────┤
│ 15 – 25 (Red) │ Executive Escalation; mandatory funded fallback buffer.│
│  8 – 14 (Amb) │ Active PgM monitoring; pre-approved mitigation triggers.│
│  1 – 7 (Green)│ Accepted risk; log in quarterly risk review.          │
└───────────────┴────────────────────────────────────────────────────────┘
```

---

## 5. Civil & HWRE Engineering Transferable Foundation

The discipline of Program Management originated directly from large-scale civil infrastructure projects (such as the Hoover Dam and the Dupont engineering plants):
- **Scheduling**: Civil students routinely calculate forward/backward passes and floats in Construction Management (IS 15883 / CPWD Works Manual).
- **Resource Leveling**: Balancing concrete batching plant output and earthmoving equipment mirrors engineering sprint velocity leveling.
- **Contractual Escalation & Claims**: Handling contractor Delay Liquidated Damages (LD) and Variation Orders directly translates to SaaS vendor contract governance.
