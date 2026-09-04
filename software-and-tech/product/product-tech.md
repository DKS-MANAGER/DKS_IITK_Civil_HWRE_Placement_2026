# 📱 Product Management Technology

> **Target:** Product Manager, Product Analyst, Technical PM roles
> **Teach PM candidates enough technology to collaborate with engineering teams without pretending they are software engineers.**

---

## The PM Technology Principle

> **A PM does NOT need to be a software engineer. A PM needs enough technical literacy to:**
> - Understand what's technically feasible
> - Communicate with engineers
> - Make data-driven product decisions
> - Evaluate technical trade-offs

---

## Priority Stack

| Tool | Tag | Level | Purpose |
|:-----|:----|:------|:--------|
| Excel | `[MUST LEARN]` | L3 | Metrics, analysis, prioritization |
| SQL | `[MUST LEARN]` | L2–L3 | Querying product data |
| Analytics platforms | `[HIGH ROI]` | L2 | Product analytics (Mixpanel, Amplitude) |
| Dashboards | `[HIGH ROI]` | L2 | Power BI / Tableau |
| Experimentation | `[HIGH ROI]` | L2 | A/B testing concepts |
| Wireframing tools | `[ROLE DEPENDENT]` | L1–L2 | Figma, Balsamiq |
| Documentation tools | `[ROLE DEPENDENT]` | L2 | Confluence, Notion |
| Project management tools | `[ROLE DEPENDENT]` | L2 | Jira, Asana, Trello |
| APIs | `[ROLE DEPENDENT]` | L1–L2 | Understanding integration |
| Technical fundamentals | `[ROLE DEPENDENT]` | L1–L2 | Databases, cloud, frontend/backend |

---

## Technical Fundamentals for PM

### API

```
What: Application Programming Interface — how software components communicate
Key concepts:
    - REST vs GraphQL
    - HTTP methods (GET, POST, PUT, DELETE)
    - Endpoints, requests, responses
    - Authentication (API keys, OAuth)
Why PM needs it: To understand integrations, evaluate feasibility, write PRDs
```

### Database

```
What: Structured storage of data
Key concepts:
    - Relational (SQL) vs NoSQL
    - Tables, rows, columns
    - Primary keys, foreign keys
    - Data modeling basics
Why PM needs it: To understand what data is available, define requirements
```

### Frontend / Backend

```
Frontend: What users see (UI) — HTML, CSS, JavaScript
Backend:  Server-side logic, data processing — Python, Java, Node.js
Why PM needs it: To scope features, understand effort, communicate with teams
```

### Cloud Basics

```
What: Computing resources over the internet
Key concepts:
    - IaaS, PaaS, SaaS
    - AWS, Azure, GCP
    - Scaling, availability, cost
Why PM needs it: To understand deployment, cost implications, SLAs
```

### Authentication

```
What: Verifying user identity
Key concepts:
    - Login, signup, sessions
    - OAuth, SSO, 2FA
    - Tokens, cookies
Why PM needs it: To scope auth features, understand security requirements
```

### Data Pipeline

```
What: Moving/processing data from source to analysis
Key concepts:
    - ETL (Extract, Transform, Load)
    - Batch vs streaming
    - Data warehouse vs data lake
Why PM needs it: To understand data availability, latency, reliability
```

### Analytics

```
What: Measuring product usage and performance
Key concepts:
    - Events, properties, funnels
    - DAU/MAU, retention, churn
    - Cohort analysis
    - North Star metric
Why PM needs it: To make data-driven decisions
```

### A/B Testing

```
What: Comparing two versions to measure impact
Key concepts:
    - Control vs treatment
    - Statistical significance
    - Sample size, power
    - Guardrail metrics
Why PM needs it: To validate product changes
```

---

## Product Analytics Concepts

### Metrics Hierarchy

```
North Star Metric (top-level goal)
    ↓
Input Metrics (drivers)
    ↓
Guardrail Metrics (protect against harm)
```

### Key Metrics

```
Acquisition:   New users, installs, signups
Activation:    % completing key action
Retention:     % returning after day 7/30
Revenue:       ARPU, ARPPU, LTV
Referral:      Virality coefficient
Engagement:    DAU/MAU, session length
```

### Funnel Analysis

```
Step 1: Define funnel (e.g., visit → signup → first action → purchase)
Step 2: Measure conversion at each step
Step 3: Identify drop-off points
Step 4: Prioritize improvements
```

---

## Tools for PM

### Wireframing

| Tool | Use Case | Level |
|:-----|:---------|:------|
| Figma | UI design, prototyping, collaboration | L1–L2 |
| Balsamiq | Low-fidelity wireframes | L1 |
| Miro | Whiteboarding, flow diagrams | L1 |

### Documentation

| Tool | Use Case | Level |
|:-----|:---------|:------|
| Confluence | PRDs, specs, team docs | L2 |
| Notion | Notes, wikis, project docs | L2 |
| Google Docs | Collaborative documents | L2 |

### Project Management

| Tool | Use Case | Level |
|:-----|:---------|:------|
| Jira | Agile development, sprints, issues | L2 |
| Asana | Task tracking, project planning | L2 |
| Trello | Kanban boards | L1–L2 |

---

## Interview Questions

### Technical Fundamentals
- What is an API? Explain REST.
- What is the difference between SQL and NoSQL databases?
- Explain the difference between frontend and backend.
- What is A/B testing? How do you design one?

### Product Analytics
- What metrics would you track for a new feature?
- How do you define a North Star metric?
- Your DAU dropped 20%. How do you investigate?

### Product Sense
- How would you improve [product]?
- Design a feature for [specific user].
- How do you prioritize features?

---

## Cross-Links

| Related Section | Link |
|:----------------|:-----|
| Data/Analytics Stack | [`data/`](../data/data-analytics-stack.md) |
| SQL | [`programming/sql.md`](../programming/sql.md) |
| Non-Core PM | [`non-core/product-management/`](../../non-core/product-management/pm-overview.md) |
| Tech Careers | [`technology-careers/`](../technology-careers/tech-careers.md) |

---

*See also: [`tech-careers.md`](../technology-careers/tech-careers.md) for the Technical PM track.*
