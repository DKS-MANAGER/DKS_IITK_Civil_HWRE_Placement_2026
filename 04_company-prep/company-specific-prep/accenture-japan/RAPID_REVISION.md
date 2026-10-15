# Rapid Revision & Emergency Interview Cheat Sheet

> **Target Role**: Digital Consultant (Analyst Entry Level), Accenture Japan Ltd. (`[JD VERIFIED]`)  
> **Purpose**: High-yield formulas, essential SQL patterns, core architecture definitions, and interview-day mental checklists for 60-minute, 3-hour, and 24-hour review windows.

---

## 1. High-Yield Business & Consulting Math Formulas

* **Gross Margin**:
  $$\text{Gross Margin} = \frac{\text{Revenue} - \text{COGS}}{\text{Revenue}}$$
* **Operating (EBIT) Margin**:
  $$\text{Operating Margin} = \frac{\text{Operating Income (EBIT)}}{\text{Revenue}}$$
* **Break-Even Volume**:
  $$\text{Break-Even Units} = \frac{\text{Fixed Costs}}{\text{Price per Unit} - \text{Variable Cost per Unit}}$$
* **Customer Lifetime Value (LTV)**:
  $$\text{LTV} = \frac{\text{Annual Gross Profit per Customer}}{\text{Annual Churn Rate}}$$
* **LTV / CAC Ratio**: Target $> 3.0x$ (healthy SaaS / subscription business). Payback Period $= \text{CAC} / \text{Annual Gross Profit} < 12\text{ months}$.
* **Rule of 72 (Doubling Time)**:
  $$\text{Years to Double} \approx \frac{72}{\text{Annual Growth Rate \%}}$$
* **Overall Equipment Effectiveness (OEE)**:
  $$\text{OEE} = \text{Availability} \times \text{Performance} \times \text{Quality}$$

---

## 2. Top 10 SQL Cheat Sheet Patterns

#### 1. Safe Divide-by-Zero Protection
```sql
SELECT ROUND(numerator * 100.0 / NULLIF(denominator, 0), 2) AS safe_ratio;
```

#### 2. DENSE_RANK without Gaps
```sql
DENSE_RANK() OVER (PARTITION BY industry ORDER BY contract_value_jpy DESC) AS rank_num
```

#### 3. Month-over-Month Growth with LAG
```sql
ROUND(((current_val - LAG(current_val) OVER (ORDER BY month_dt)) * 100.0) / 
      NULLIF(LAG(current_val) OVER (ORDER BY month_dt), 0), 2) AS mom_growth_pct
```

#### 4. Running Cumulative Sum
```sql
SUM(actual_cost_jpy) OVER (PARTITION BY project_id ORDER BY completion_date 
                           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
```

#### 5. 3-Period Moving Average
```sql
AVG(latency_ms) OVER (PARTITION BY server_id ORDER BY recorded_at 
                      ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING)
```

#### 6. Conditional Aggregation (Pivot)
```sql
SUM(CASE WHEN domain = 'Cloud Migration' THEN contract_value_jpy ELSE 0 END) AS cloud_jpy
```

#### 7. Deduplicating Latest Record per Group
```sql
WITH Ranked AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY server_id ORDER BY recorded_at DESC) AS rn
    FROM system_metrics
)
SELECT * FROM Ranked WHERE rn = 1;
```

#### 8. Common Table Expression (CTE) Multi-Stage Pipeline
```sql
WITH Step1 AS (...), Step2 AS (...) SELECT * FROM Step2;
```

#### 9. Finding Groups with Zero Events
```sql
SELECT c.company_name FROM clients c LEFT JOIN projects p ON c.client_id = p.client_id WHERE p.project_id IS NULL;
```

#### 10. Gap Analysis with CROSS JOIN
```sql
SELECT r.region, i.industry FROM regions r CROSS JOIN industries i LEFT JOIN ... WHERE ... IS NULL;
```

---

## 3. Technology Architecture & Digital Concepts in 30 Seconds

* **Technology-Agnostic Model (`[JD VERIFIED]`)**: Accenture does not push proprietary tools; we evaluate AWS, Azure, GCP, SAP, and Salesforce purely on client business fit, TCO, and security.
* **Strangler Fig Pattern**: Incrementally replacing legacy mainframes by routing read APIs through modern cloud services before migrating core write transactions.
* **RAG (Retrieval-Augmented Generation)**: Grounding LLM responses in company vector databases to ensure fresh information, verifiable citations, and zero hallucinated facts.
* **Zero Trust Architecture**: "Never trust, always verify." Requires continuous authentication, least-privilege RBAC, and encryption for every single request.
* **Edge Computing vs Cloud in IoT**: Edge processes microsecond telemetry on factory gateways for safety and local anomaly detection; Cloud handles fleet-wide training and long-term trend analysis.
* **CAP Theorem**: Distributed systems must balance Consistency versus Availability during network Partitions.

---

## 4. Candidate Project Defense Cheat Sheet (The 4-Step Answer)

When asked: *"Walk me through your key technical project."*

1. **Problem (30s)**: State the physical/engineering problem and why existing methods were inadequate.
2. **Method & Stack (45s)**: Name Python, data structures, and mathematical modeling methods used.
3. **Bottleneck Overcome (45s)**: Explain how you solved data sparsity, numerical divergence, or computational memory bottlenecks without adding artificial complexity.
4. **Outcome (30s)**: Deliver quantified results (% error reduction, speedup, NSE score) and state how this demonstrates readiness for digital consulting.

---

## 5. Japanese Professional Norms Cheat Sheet

* **Ho-Ren-So (報・連・相)**:
  * *Hokoku (報告)*: Proactively report milestone progress to your Manager before being asked.
  * *Renraku (連絡)*: Immediately inform teammates of changes, scope shifts, or blockers.
  * *Sodan (相談)*: Consult seniors early when encountering ambiguity.
* **Nemawashi (根回し)**: Informal alignment with stakeholders prior to formal decision-making meetings to ensure smooth consensus and zero surprises.
* **Kaizen (改善)**: Relentless daily incremental refinement in code quality, data accuracy, and presentation clarity.

---

## 6. Interview Day Mental Checklist

### T-Minus 60 Minutes:
- [ ] Test Zoom connection, microphone audio, camera lighting, and quiet environment.
- [ ] Review 60-second role pitch and 90-second "Why Accenture Japan" answer.
- [ ] Review the 4-step project defense framework for quantitative engineering projects.
- [ ] Prepare notepad and pen for case structuring diagrams.

### During the 30-Minute Interview:
- [ ] **Listen Actively**: Do not interrupt the interviewer; write down key problem constraints.
- [ ] **Ask Clarifying Questions**: Clarify client objective, time horizon, and geographic scope.
- [ ] **Lead with the Answer**: State recommendations first using the Pyramid Principle.
- [ ] **Stay Calm Under Pushback**: Acknowledge interviewer comments, state assumptions, and evaluate trade-offs.
- [ ] **Ask 2 Thoughtful Closing Questions**: Showcase genuine curiosity about Accenture Japan's digital practice.
