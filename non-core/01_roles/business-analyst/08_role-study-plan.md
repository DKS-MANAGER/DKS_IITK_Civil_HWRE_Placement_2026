# Business Analyst — Study Plan

> 4-week preparation roadmap for civil/M.Tech students targeting business analyst roles.

---

## Role Overview

**What BAs do:** Bridge business needs and data — translate questions into analyses, analyses into decisions.

**Day-to-day:** SQL queries, dashboard building, KPI analysis, stakeholder communication, requirements gathering.

**Civil/M.Tech advantage:** Data analysis from research, Python/MATLAB skills, systematic problem solving, project coordination experience.

**Target companies:** Barclays, Accenture, any data-driven consulting or tech company.

---

## Topic 1: SQL & Data Manipulation

### Why This Matters
SQL is the most tested skill for BA roles (30% weight). You must write queries fluently.

### What to Learn
- [ ] SELECT, WHERE, GROUP BY, HAVING, ORDER BY
- [ ] JOINs: INNER, LEFT, RIGHT, FULL
- [ ] Subqueries, CTEs
- [ ] Window functions
- [ ] CASE statements
- [ ] Date and string functions

### Study Material
| Topic | File | Depth |
|:------|:-----|:------|
| SQL Practice | [sql-practice.md](sql-practice.md) | Full practice set |
| BA Overview | [ba-overview.md](ba-overview.md) | SQL context + questions |

### Practice
- [ ] Basic: 5 queries (SELECT, WHERE, GROUP BY)
- [ ] Intermediate: 5 queries (JOINs, window functions)
- [ ] Interview-level: 5 timed queries

### Interview Questions
1. Write a query to find the top 5 products by revenue. — *Tests: aggregation + ordering*
2. What's the difference between WHERE and HAVING? — *Tests: conceptual understanding*
3. Write a query to find customers who churned. — *Tests: complex filtering*
4. Explain the difference between INNER JOIN and LEFT JOIN. — *Tests: JOIN knowledge*
5. How would you optimize a slow query? — *Tests: performance thinking*

### Completion Criterion
- [ ] Can write any SQL query in 10 minutes
- [ ] Can explain window functions clearly

---

## Topic 2: Excel & Data Interpretation

### Why This Matters
15% of BA weight. Excel is still the primary tool for many business analyses.

### What to Learn
- [ ] Pivot tables (create, filter, drill down)
- [ ] VLOOKUP / XLOOKUP
- [ ] IF / INDEX-MATCH formulas
- [ ] Charts and conditional formatting
- [ ] Data validation

### Study Material
| Topic | File | Depth |
|:------|:-----|:------|
| BA Overview | [ba-overview.md](ba-overview.md) | Excel context |

### Practice
- [ ] Build 2 pivot tables from sample data
- [ ] Write 3 VLOOKUP/INDEX-MATCH formulas
- [ ] Create 2 charts for business scenarios

---

## Topic 3: KPI Analysis & Business Acumen

### Why This Matters
25% of BA weight. You must understand what metrics matter and why they change.

### What to Learn
- [ ] KPI identification (what to measure for different businesses)
- [ ] Root-cause analysis (5 Whys, fishbone diagram)
- [ ] Data interpretation (tables, charts, trends)
- [ ] Business fundamentals (revenue, costs, margins)

### Study Material
| Topic | File | Depth |
|:------|:-----|:------|
| Business Fundamentals | [business-fundamentals.md](../common/business-fundamentals.md) | Core concepts |
| BA Overview | [ba-overview.md](ba-overview.md) | KPI analysis + case questions |

### Worked Example
> **"A KPI fell 20% last month. Investigate."**
>
> 1. Define the KPI (what counts?)
> 2. Segment the drop (by region, device, cohort, feature)
> 3. Check external factors (seasonality, competitor, outages)
> 4. Check internal factors (product changes, bugs, marketing)
> 5. Form hypothesis → test → validate

### Practice
- [ ] Identify KPIs for 5 businesses (e-commerce, SaaS, banking, ride-hailing, social media)
- [ ] Diagnose 3 KPI drops (revenue, churn, conversion)
- [ ] Build 2 dashboards for given scenarios

### Interview Questions
1. What KPIs would you track for an e-commerce company? — *Tests: business understanding*
2. A KPI dropped 20%. How would you investigate? — *Tests: root-cause analysis*
3. Revenue is up but profit is down. Diagnose. — *Tests: multi-dimensional analysis*
4. How would you design a dashboard for a sales team? — *Tests: visualization + business sense*
5. Two metrics conflict. Which do you trust? — *Tests: business judgment*

---

## Topic 4: Communication & Stakeholder Management

### Why This Matters
15% of BA weight. BAs must present findings clearly and handle stakeholder expectations.

### What to Learn
- [ ] Data storytelling (What? So what? Now what?)
- [ ] Executive summaries
- [ ] Handling conflicting requirements
- [ ] Managing expectations when data is incomplete

### Practice
- [ ] Present 3 data stories (What happened? Why? What to do?)
- [ ] Handle 2 stakeholder conflict scenarios

---

## Mock Test

| Section | Questions | Time | Topics |
|:--------|:----------|:-----|:-------|
| SQL | 3 queries | 30 min | Topic 1 |
| Excel/Data | 2 problems | 20 min | Topic 2 |
| KPI/Case | 2 scenarios | 20 min | Topic 3 |
| Communication | 2 questions | 10 min | Topic 4 |
| Behavioral | 3 questions | 10 min | Prep/behavioral |
| **Total** | **13** | **90 min** | |

---

## Rapid Revision

### Must-Know SQL Patterns
```sql
-- Window function for ranking
SELECT *, RANK() OVER (ORDER BY revenue DESC) AS rank
FROM products;

-- CTE for complex analysis
WITH monthly AS (
    SELECT DATE_TRUNC('month', date) AS month, SUM(amount) AS total
    FROM sales GROUP BY 1
)
SELECT month, total, LAG(total) OVER (ORDER BY month) AS prev
FROM monthly;

-- CASE for categorization
SELECT CASE WHEN score >= 90 THEN 'A' WHEN score >= 80 THEN 'B' ELSE 'C' END AS grade
FROM students;
```

### KPI Quick Reference
| Business | Key KPIs |
|:---------|:---------|
| E-commerce | Conversion rate, AOV, cart abandonment, repeat rate |
| SaaS | MRR, churn, activation rate, NPS |
| Banking | Customer acquisition cost, lifetime value, default rate |
| Ride-hailing | Ride completion rate, surge frequency, driver utilization |
| Social media | DAU/MAU, engagement rate, content creation rate |

### Last-Minute Checklist
- [ ] Practiced 5 SQL queries
- [ ] Reviewed pivot table creation
- [ ] Reviewed KPI frameworks
- [ ] Prepared 4 STAR stories
- [ ] Researched [company] business model

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| Full Study Plan | [role-study-plan.md](role-study-plan.md) |
| SQL Practice | [sql-practice.md](sql-practice.md) |
| Statistics | [../data-analyst/statistics-practice.md](../data-analyst/statistics-practice.md) |
| Business Fundamentals | [../common/business-fundamentals.md](../common/business-fundamentals.md) |
| Behavioral Guide | [../../prep/behavioral/behavioral-interview-guide.md](../../prep/behavioral/behavioral-interview-guide.md) |

---

*Based on role-study-plan-template.md. Customized for Business Analyst role.*
