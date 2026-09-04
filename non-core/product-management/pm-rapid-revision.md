# Product Manager — Rapid Revision Sheet

> Last-minute revision for PM interviews. Covers frameworks, metrics, and key concepts in 15 minutes.

---

## Framework 1: Product Sense (User → Need → Solution)

```
1. WHO    → Define the user (primary segment, context, characteristics)
2. WHAT   → Define the need (problem, pain points, alternatives)
3. HOW    → Define the solution (core features, MVP, differentiation, trade-offs)
4. SUCCESS → Define metrics (North Star, supporting, guardrail)
```

**"Design X" Structure (6 min):**
- Clarify (30s) → User (1min) → Need (1min) → Solution (2min) → Metrics (1min)

**"Improve X" Structure (6 min):**
- Current State (1min) → Identify Areas (1min) → Prioritize (1min) → Solution (2min) → Metrics (1min)

---

## Framework 2: Product Metrics (AARRR Funnel)

```
Acquisition → Activation → Retention → Revenue → Referral
   ( signup )   ( first use )  ( return )  ( pay )  ( invite )
```

### Key Metrics by Product Type

| Product | North Star | Supporting |
|:--------|:-----------|:-----------|
| Social | DAU/MAU | Engagement, shares, time spent |
| E-commerce | GMV / Revenue | Conversion, AOV, repeat rate |
| SaaS | Weekly active users | Activation, churn, MRR |
| Content | Time spent / sessions | DAU, completion rate |
| Marketplace | Successful transactions | Liquidity, take rate |
| Fintech | Transaction volume | Activation, retention |

### Metric Formulas

| Metric | Formula | Meaning |
|:-------|:--------|:--------|
| DAU/MAU Stickiness | DAU ÷ MAU | Engagement intensity (>20% = good) |
| Day N Retention | Active Day N ÷ Active Day 0 | User stickiness |
| ARPU | Revenue ÷ Users | Revenue per user |
| LTV | Avg revenue × lifespan | Lifetime value |
| CAC | Marketing spend ÷ New customers | Acquisition cost |
| LTV/CAC | LTV ÷ CAC | Target: >3 |
| Churn | Lost ÷ Start | % who leave |
| Conversion Rate | Converted ÷ Total | Funnel efficiency |

---

## Framework 3: Prioritization

### RICE Score
```
RICE = (Reach × Impact × Confidence) ÷ Effort
```
- Reach: # of users affected (per quarter)
- Impact: 0.25 (minimal), 0.5 (low), 1 (medium), 2 (high), 3 (massive)
- Confidence: 100% (high), 80% (medium), 50% (low)
- Effort: person-months

### MoSCoW
```
Must have    → Product fails without it
Should have  → Important but not critical
Could have   → Nice to have
Won't have   → Not this time
```

### Impact vs. Effort Matrix
```
High Impact, Low Effort  → DO FIRST (quick wins)
High Impact, High Effort → PLAN (major projects)
Low Impact, Low Effort   → MAYBE (fill-ins)
Low Impact, High Effort  → DROP (time wasters)
```

---

## Framework 4: Strategy

### Market Entry Analysis
```
1. Market Attractiveness → Size, growth, competition, trends
2. Company Fit → Capabilities, brand, distribution
3. Entry Mode → Organic vs. acquisition vs. partnership
4. Financial Viability → Investment, returns, timeline
```

### Competitive Positioning
```
1. Who are the competitors?
2. What's their positioning?
3. What's our differentiation?
4. What's our sustainable advantage?
5. How do we defend?
```

---

## Common Diagnosis Framework

### "Metric Dropped — Diagnose"
```
1. DEFINE → What exactly dropped? By how much? Since when?
2. SEGMENT → By platform? Region? User type? Feature?
3. EXTERNAL → Competitor activity? Seasonality? Outages?
4. INTERNAL → Product changes? Bugs? Marketing changes?
5. HYPOTHESIS → Form 2-3 hypotheses
6. TEST → Data to validate each
7. RECOMMEND → Fix + prevent recurrence
```

### "Feature Shipped But Nobody Uses It"
```
1. Was the problem real? (User research)
2. Is the solution right? (Usability testing)
3. Do users know about it? (Discovery/awareness)
4. Is the value clear? (Onboarding/communication)
5. Is there friction? (Activation barriers)
```

---

## Key Concepts

| Concept | Definition |
|:--------|:-----------|
| **MVP** | Smallest product that tests a hypothesis |
| **North Star Metric** | One metric that best captures core product value |
| **Guardrail Metric** | Metric you don't want to break while improving another |
| **Cohort Analysis** | Tracking behavior of a group over time |
| **A/B Testing** | Comparing two versions to see which performs better |
| **Network Effects** | Product becomes more valuable as more people use it |
| **Viral Loop** | Users naturally invite other users |
| **Unit Economics** | Revenue and cost per unit/customer |

---

## 10 Quick-Fire Answers

| Question | 30-Second Answer |
|:---------|:-----------------|
| What is product sense? | Understanding users deeply, identifying their needs, and translating those into solutions that create value. |
| What is a North Star metric? | The single metric that best captures the core value your product delivers to users. |
| What is MVP? | The smallest version of a product that tests whether a hypothesis about user needs is correct. |
| DAU dropped — what do you do? | Segment the drop (platform, region, cohort), check external factors (competitor, outage), check internal factors (product change), form hypothesis, test. |
| RICE framework? | Reach × Impact × Confidence ÷ Effort. Use to score and rank feature candidates. |
| What is cohort analysis? | Tracking a group of users who share a common characteristic over time to understand behavior patterns. |
| What is LTV/CAC? | Lifetime Value ÷ Customer Acquisition Cost. Should be >3 for sustainable business. |
| What is AARRR? | Acquisition, Activation, Retention, Revenue, Referral — the user lifecycle funnel. |
| How do you handle stakeholder conflict? | Listen, understand their perspective, present data-driven reasoning, propose alternatives, escalate if needed. |
| What makes a good PM? | Deep user empathy, structured thinking, clear communication, data-driven decisions, ability to influence without authority. |

---

## Last-Minute Checklist (1 hour before interview)

- [ ] Reviewed User → Need → Solution framework
- [ ] Practiced 3 "Design X" questions out loud (timed)
- [ ] Reviewed metric taxonomy (AARRR + key formulas)
- [ ] Reviewed RICE framework with example calculation
- [ ] Prepared 4 STAR stories:
  - [ ] Leadership story
  - [ ] Conflict/disagreement story
  - [ ] Failure + learning story
  - [ ] Success + impact story
- [ ] Researched [company]:
  - [ ] Recent product launches
  - [ ] Competitors
  - [ ] 2 improvements you'd suggest
- [ ] Reviewed company's product on your phone

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| Full Study Plan | [role-study-plan.md](role-study-plan.md) |
| Product Sense Practice | [product-sense.md](product-sense.md) |
| Metrics & Strategy | [pm-metrics-strategy.md](pm-metrics-strategy.md) |
| Behavioral Guide | [../../prep/behavioral/behavioral-interview-guide.md](../../prep/behavioral/behavioral-interview-guide.md) |
| Self-Introduction | [../../prep/behavioral/self_intro/self-introduction.md](../../prep/behavioral/self_intro/self-introduction.md) |
| Mock Questions | [../../prep/interview/mock-tests/mock-interview-questions.md](../../prep/interview/mock-tests/mock-interview-questions.md) |

---

*Print this sheet 1 hour before your PM interview.*
