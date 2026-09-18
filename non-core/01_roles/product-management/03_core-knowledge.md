# PM Metrics & Strategy

> Product metrics, strategy frameworks, and execution questions for PM interviews.

---

## Part 1: Product Metrics

### The Metric Hierarchy

```
North Star Metric (the one that captures core value)
├── Acquisition metrics
├── Activation metrics
├── Retention metrics
├── Revenue metrics
└── Referral metrics
```

### Key Metrics by Product Type

| Product Type | North Star | Supporting Metrics |
|:-------------|:-----------|:-------------------|
| **Social media** | DAU/MAU | Engagement, retention, shares |
| **E-commerce** | GMV / Revenue | Conversion, AOV, repeat rate |
| **SaaS** | Weekly active users | Activation, churn, MRR |
| **Content** | Time spent / sessions | DAU, retention, completion |
| **Marketplace** | Successful transactions | Liquidity, take rate, GMV |
| **Fintech** | Transaction volume | Activation, retention, ARPU |

### Funnel Metrics

```
Awareness → Interest → Consideration → Purchase → Retention → Advocacy
   100%       60%         30%           10%         8%          3%

Key: Where is the biggest drop-off? That's where to focus.
```

### Retention & Churn

| Metric | Formula | Meaning |
|:--------|:--------|:--------|
| **Retention** | (End - New) / Start | % of users who stay |
| **Churn** | Lost / Start | % of users who leave |
| **Cohort retention** | Active in cohort / Total in cohort | Retention over time |

### Engagement Metrics

| Metric | Formula | Meaning |
|:--------|:--------|:--------|
| **DAU** | Daily active users | Daily engagement |
| **MAU** | Monthly active users | Monthly reach |
| **Stickiness** | DAU / MAU | Engagement intensity |
| **Session length** | Total time / Sessions | Depth of engagement |
| **Feature adoption** | Users using feature / Total users | Feature success |

### Revenue Metrics

| Metric | Formula | Meaning |
|:--------|:--------|:--------|
| **ARPU** | Revenue / Users | Revenue per user |
| **ARPPU** | Revenue / Paying users | Revenue per paying user |
| **MRR** | Monthly recurring revenue | SaaS revenue |
| **LTV** | Avg revenue × lifespan | Lifetime value |
| **CAC** | Marketing spend / New customers | Acquisition cost |

---

## Part 2: Product Strategy

### Market Entry Strategy

```
1. Market attractiveness
   - Size, growth, trends
   - Competitive landscape
   - Regulatory environment

2. Company fit
   - Capabilities
   - Brand strength
   - Distribution

3. Entry mode
   - Organic vs. acquisition vs. partnership

4. Financial viability
   - Investment, returns, timeline
```

### Competitive Strategy

```
1. Who are the competitors?
2. What's their positioning?
3. What's our differentiation?
4. What's our sustainable advantage?
5. How do we defend against competition?
```

### Growth Strategy

```
1. Market penetration (sell more to existing)
2. Market development (new markets)
3. Product development (new products)
4. Diversification (new + new)
```

### Pricing Strategy

```
1. Cost-based (floor)
2. Value-based (ceiling)
3. Competition-based (anchor)
4. Strategy: penetration, skimming, freemium, tiered
```

---

## Part 3: Execution Questions

### "A Metric Fell. Diagnose Why."

**Framework:**
```
1. Define the metric precisely
   - What exactly is being measured?
   - Is the definition correct?

2. Segment the drop
   - By platform, region, cohort, feature
   - New vs. returning users

3. Check external factors
   - Seasonality
   - Competitor activity
   - Market events
   - Technical issues (outages)

4. Check internal factors
   - Product changes (recent releases)
   - Marketing changes
   - Pricing changes
   - Infrastructure issues

5. Form hypothesis → test → validate
```

### "A Feature Shipped But Didn't Move the Metric."

**Framework:**
```
1. Was the metric the right one?
2. Was the feature actually used? (adoption)
3. Was the feature discoverable?
4. Was the sample size adequate?
5. Was there a confounding factor?
6. Was the hypothesis wrong?
```

### "How Do You Prioritize?"

**Frameworks:**
| Framework | Formula | Use |
|:----------|:--------|:----|
| **RICE** | (Reach × Impact × Confidence) / Effort | Quantitative prioritization |
| **MoSCoW** | Must, Should, Could, Won't | Categorization |
| **ICE** | Impact × Confidence × Ease | Quick scoring |
| **Kano** | Basic, Performance, Delight | User satisfaction |

---

## Part 4: Strategy Question Bank

### Market & Competition
1. Should [company] enter [market]?
2. How would you compete with [dominant player]?
3. What's the biggest threat to [product]?
4. How would you differentiate [product]?

### Growth
5. How would you grow [product] 2x?
6. What's your go-to-market strategy for [product]?
7. How would you expand to a new geography?

### Pricing
8. How would you price [product]?
9. Should we move to a freemium model?
10. How do you handle price-sensitive customers?

### Trade-offs
11. Growth vs. profitability — which first?
12. Speed vs. quality — how do you decide?
13. New features vs. fixing bugs — which first?

---

## Part 5: Behavioral Questions (PM-Specific)

| Question | Focus |
|:---------|:------|
| Tell me about a product you built. | Product ownership |
| Describe a time you influenced without authority. | Stakeholder management |
| How do you handle disagreement with engineering? | Conflict resolution |
| Tell me about a time you made a tough trade-off. | Decision-making |
| Describe a time a product failed. | Learning, resilience |
| How do you prioritize competing demands? | Prioritization |
| Tell me about a time you worked with a difficult stakeholder. | Stakeholder management |

---

## Quick Reference: PM Frameworks

| Framework | Use |
|:----------|:----|
| **User → Need → Solution → Metrics** | Product design |
| **AARRR** | Growth metrics |
| **RICE** | Prioritization |
| **North Star Metric** | Core value metric |
| **Funnel Analysis** | Conversion optimization |
| **Cohort Analysis** | Retention tracking |
| **SWOT** | Strategic analysis |
| **Porter's Five Forces** | Competitive analysis |

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| PM Overview | [pm-overview.md](pm-overview.md) |
| Product Sense | [product-sense.md](product-sense.md) |
| Business Fundamentals | [business-fundamentals.md](../common/business-fundamentals.md) |
| Product Analyst | [pa-overview.md](../product-analyst/pa-overview.md) |

---

*Metrics tell you what happened; strategy tells you what to do about it. A great PM masters both.*
