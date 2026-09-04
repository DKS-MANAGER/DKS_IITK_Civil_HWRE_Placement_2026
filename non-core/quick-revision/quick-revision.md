# Non-Core Quick Revision — Night-Before Cards

> High-priority cheat sheets for the night before your interview. Focus on what 80% of interviews test.

---

## Card 1: Business Fundamentals (Must-Know)

| Concept | Formula / Definition |
|:--------|:---------------------|
| **Revenue** | Price × Quantity |
| **Gross Profit** | Revenue - COGS |
| **EBITDA** | Earnings before interest, tax, depreciation, amortization |
| **Net Profit** | Revenue - all costs |
| **Gross Margin** | Gross Profit / Revenue |
| **Break-even** | Fixed Costs / (Price - Variable Cost) |
| **CAC** | Marketing Spend / New Customers |
| **LTV** | Avg Revenue × Lifespan / Churn |
| **CAGR** | (End/Start)^(1/n) - 1 |
| **Market Share** | Company Revenue / Total Market |
| **Conversion** | Conversions / Visitors |
| **Churn** | Customers Lost / Customers at Start |

---

## Card 2: Case Interview Frameworks

| Question Type | Framework |
|:--------------|:----------|
| "Profits declining" | Profitability: Revenue - Costs |
| "Enter new market" | Market Entry: Attractiveness + Capability + Mode |
| "Estimate X" | Market Sizing: Top-down / Bottom-up |
| "How to grow" | Growth: Penetration, Development, Product, Diversification |
| "How to price" | Pricing: Cost floor + Value ceiling + Competition |
| "Improve efficiency" | Operations: Map → Bottleneck → Root cause → Improve |
| "Acquire X" | M&A: Fit + Target + Valuation + Integration |
| "How to compete" | Five Forces + Positioning |

**Golden rule:** Structure → Questions → Data → Analysis → Insight → Recommendation

---

## Card 3: Guesstimate Method

```
1. CLARIFY — scope, geography, time
2. STRUCTURE — choose method
3. ASSUME — state assumptions
4. CALCULATE — show math
5. SANITY CHECK — compare to benchmark
6. STATE — clean answer with range
```

**Key benchmarks:**
- India population: 1.4 billion
- Urban population: 35%
- Household size: 4.5
- Water per person: 150-200 L/day
- Cement per capita: ~250 kg/year

---

## Card 4: SQL Cheat Sheet

```sql
-- Filter
SELECT * FROM table WHERE condition;

-- Aggregate
SELECT col, COUNT(*), SUM(amount)
FROM table
GROUP BY col
HAVING COUNT(*) > 1;

-- Join
SELECT a.*, b.*
FROM table_a a
LEFT JOIN table_b b ON a.id = b.id;

-- Window function
SELECT col, SUM(amount) OVER (PARTITION BY col ORDER BY date) AS running
FROM table;

-- CTE
WITH cte AS (
    SELECT col, SUM(amount) AS total
    FROM table
    GROUP BY col
)
SELECT * FROM cte WHERE total > 1000;
```

**Execution order:** FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT

---

## Card 5: Statistics Cheat Sheet

| Concept | Formula |
|:--------|:--------|
| **Mean** | Σx / n |
| **Variance** | Σ(x-μ)² / n |
| **Std Dev** | √Variance |
| **Z-score** | (x - μ) / σ |
| **Bayes** | P(A|B) = P(B|A)P(A)/P(B) |
| **95% CI** | x̄ ± 1.96 × σ/√n |
| **Binomial mean** | np |
| **Poisson mean** | λ |

**68-95-99.7 rule:** μ±1σ=68%, μ±2σ=95%, μ±3σ=99.7%

**p-value:** p < 0.05 → statistically significant

---

## Card 6: Product Metrics

| Metric | Meaning |
|:--------|:--------|
| **DAU / MAU** | Daily / Monthly active users |
| **Stickiness** | DAU / MAU |
| **Retention** | (End - New) / Start |
| **Churn** | Lost / Start |
| **Conversion** | Conversions / Visitors |
| **ARPU** | Revenue / Users |
| **LTV** | Avg revenue × lifespan |
| **CAC** | Marketing spend / new customers |

**North Star:** The one metric that captures core value.

**AARRR:** Acquisition → Activation → Retention → Revenue → Referral

---

## Card 7: Behavioral Frameworks

| Question | Framework |
|:---------|:----------|
| "Tell me about a time..." | STAR (Situation, Task, Action, Result) |
| "Describe a failure..." | CARL (Context, Action, Result, Learning) |
| "Why this role?" | PPP (Present, Past, Future) |
| "What would you do if..." | SOAR (Situation, Options, Action, Result) |
| "What do you think about..." | PREP (Point, Reason, Example, Point) |

**STAR timing:** S=15s, T=10s, A=45s, R=20s (total 90s)

---

## Card 8: Civil → Non-Core Translations

| Civil Skill | Business Translation |
|:------------|:---------------------|
| CFD / Modelling | Quantitative modeling, analytical thinking |
| Research / Thesis | Independent problem solving, ambiguity tolerance |
| Project management | Ownership, execution, delivery |
| Lab work | Experimentation, data analysis |
| Python / MATLAB | Quantitative automation |
| GIS | Spatial analytics, data visualization |
| Teaching / TA | Communication, simplification |

**Formula:** Actual experience → Transferable competency → Evidence → Role relevance

---

## Card 9: Power Phrases

| Situation | Phrase |
|:----------|:-------|
| Starting a case | "Let me structure my thoughts..." |
| Breaking down | "I'd approach this by breaking it into..." |
| Analyzing | "Looking at this data, I notice..." |
| Stuck | "Let me reconsider. Another way to look at this..." |
| Concluding | "My recommendation is... because (1), (2), (3)..." |
| Handling pushback | "That's a fair point. Let me reconsider..." |
| Buying time | "Let me think about that for a moment..." |

---

## Card 10: 5-Minute Pre-Interview Routine

1. **Review your resume** — know every line
2. **Rehearse your intro** — 90-second version
3. **Review 3 STAR stories** — leadership, problem-solving, teamwork
4. **Review 2 frameworks** — your role's most likely case type
5. **Prepare 3 questions** for the interviewer
6. **Deep breaths** — calm, confident, ready

---

## Role-Specific Quick Prep

### Consulting
- Profitability + Market Entry frameworks
- 2 STAR stories (leadership, problem-solving)
- 1 guesstimate practice
- "Why consulting?" answer

### Business Analyst
- SQL: joins, GROUP BY, window functions
- KPI investigation framework
- 1 STAR story (data-driven decision)
- "Why BA?" answer

### Data Analyst
- SQL: advanced queries
- Statistics: hypothesis testing, distributions
- A/B testing framework
- "Why DA?" answer

### Product Manager
- Product sense framework (User → Need → Solution)
- Metrics for your product type
- Prioritization framework (RICE)
- "Why PM?" answer

### Operations
- Process improvement framework
- Bottleneck analysis
- 1 STAR story (process optimization)
- "Why Ops?" answer

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| Full Roadmap | [placement-roadmap.md](../placement-roadmap.md) |
| Role Selector | [role-selector.md](../role-selector.md) |
| Business Fundamentals | [business-fundamentals.md](../common/business-fundamentals.md) |
| Case Frameworks | [case-frameworks.md](../consulting/case-frameworks.md) |

---

*The night before, you're not learning — you're reminding yourself of what you already know. Trust your preparation.*
