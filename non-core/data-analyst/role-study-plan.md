# Data Analyst — Study Plan

> 4-week preparation roadmap for civil/M.Tech students targeting data analyst roles.

---

## Role Overview

**What DAs do:** Clean, analyze, and visualize data to drive business decisions. Bridge between raw data and actionable insights.

**Day-to-day:** SQL queries, Python/Pandas analysis, statistical testing, dashboard creation, stakeholder communication.

**Civil/M.Tech advantage:** Statistical analysis from research/thesis, Python/MATLAB programming, experimental methodology, data-driven problem solving.

**Target companies:** Merilytics, Barclays, Accenture, American Express, Abacus.AI, any analytics-heavy role.

---

## Topic 1: SQL Mastery

### Why This Matters
SQL is tested in 100% of data analyst interviews. You must write complex queries under time pressure.

### What to Learn
- [ ] SELECT, WHERE, GROUP BY, HAVING, ORDER BY
- [ ] JOINs: INNER, LEFT, RIGHT, FULL, CROSS
- [ ] Subqueries and CTEs (WITH clause)
- [ ] Window functions: ROW_NUMBER, RANK, LAG, LEAD, running totals
- [ ] CASE statements
- [ ] Date functions and string functions
- [ ] Query optimization basics

### Study Material
| Topic | File | Depth |
|:------|:-----|:------|
| SQL Practice | [sql-practice.md](../business-analyst/sql-practice.md) | Practice problems |
| DA Overview | [da-overview.md](da-overview.md) | SQL context + questions |
| BA SQL Practice | [sql-practice.md](../business-analyst/sql-practice.md) | Additional practice |

### Worked Example
```sql
-- Problem: Find the top 3 customers by total order value in the last 30 days
SELECT c.customer_id, c.name, SUM(o.amount) AS total_spend
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_date >= DATEADD(day, -30, GETDATE())
GROUP BY c.customer_id, c.name
ORDER BY total_spend DESC
LIMIT 3;
```

### Practice
- [ ] Basic: 5 queries (SELECT, WHERE, GROUP BY)
- [ ] Intermediate: 5 queries (JOINs, subqueries, window functions)
- [ ] Interview-level: 5 timed queries (10 min each)

### Interview Questions
1. Write a query to find customers who haven't ordered in 90 days. — *Tests: subqueries, date functions*
2. What's the difference between WHERE and HAVING? — *Tests: conceptual understanding*
3. Write a query to find the 2nd highest salary. — *Tests: window functions or subqueries*
4. Explain the difference between INNER JOIN and LEFT JOIN. — *Tests: JOIN knowledge*
5. Write a query to calculate running total of sales. — *Tests: window functions*

### Completion Criterion
- [ ] Can write any SQL query in 10 minutes
- [ ] Can explain window functions clearly
- [ ] Can optimize slow queries

---

## Topic 2: Statistics & Probability

### Why This Matters
20% of DA interview weight. You must understand distributions, hypothesis testing, and statistical significance.

### What to Learn
- [ ] Descriptive stats: mean, median, mode, variance, std dev
- [ ] Normal distribution, z-scores, percentiles
- [ ] Central Limit Theorem
- [ ] Hypothesis testing: null/alternative, p-value, significance level
- [ ] Type I and Type II errors
- [ ] Confidence intervals
- [ ] Correlation vs. causation
- [ ] A/B testing design and analysis

### Study Material
| Topic | File | Depth |
|:------|:-----|:------|
| Statistics Practice | [statistics-practice.md](statistics-practice.md) | Full practice set |
| DA Overview | [da-overview.md](da-overview.md) | Statistical concepts |

### Worked Example
> **"Is the new checkout flow better?"**
>
> 1. Define metric: conversion rate
> 2. Set up A/B test: control (old) vs. treatment (new)
> 3. Random assignment, sufficient sample size
> 4. Run test for 2 weeks
> 5. Calculate conversion rates
> 6. Run chi-square test
> 7. Check p-value < 0.05
> 8. Check practical significance (effect size)

### Practice
- [ ] Basic: 5 probability problems
- [ ] Intermediate: 5 hypothesis testing problems
- [ ] Interview-level: 3 A/B test design questions

### Interview Questions
1. What is a p-value? — *Tests: conceptual understanding*
2. Explain Type I vs. Type II errors. — *Tests: statistical reasoning*
3. How would you design an A/B test? — *Tests: experimental design*
4. What's the difference between correlation and causation? — *Tests: critical thinking*
5. Explain the Central Limit Theorem. — *Tests: foundational stats*

---

## Topic 3: Python/Pandas for Data Analysis

### Why This Matters
25% of DA interview weight. You must manipulate and analyze data using Python.

### What to Learn
- [ ] Pandas: DataFrame, Series, indexing
- [ ] Data loading: read_csv, read_excel
- [ ] Data manipulation: filter, sort, groupby, merge, pivot
- [ ] Data cleaning: missing values, duplicates, outliers
- [ ] NumPy: arrays, vectorized operations
- [ ] Visualization: matplotlib, seaborn basics

### Study Material
| Topic | File | Depth |
|:------|:-----|:------|
| Python for Analytics | [non-core-prep.md](../analytics/non-core-prep.md) | Python templates |
| Technical Stack | [technical-stack.md](../analytics/technical-stack.md) | Tool guide |

### Practice
- [ ] Basic: 5 Pandas operations (filter, groupby, merge)
- [ ] Intermediate: 3 data cleaning exercises
- [ ] Interview-level: 2 timed data analysis problems

### Interview Questions
1. How do you handle missing data in Pandas? — *Tests: data cleaning knowledge*
2. What's the difference between merge and join in Pandas? — *Tests: operation knowledge*
3. Write code to find the top 5 products by revenue. — *Tests: coding ability*
4. How would you detect outliers in a dataset? — *Tests: analytical thinking*

---

## Topic 4: Data Visualization & Communication

### Why This Matters
10% of DA weight. You must present insights clearly to stakeholders.

### What to Learn
- [ ] Chart selection (bar, line, scatter, heatmap, etc.)
- [ ] Dashboard design principles
- [ ] Data storytelling
- [ ] Common visualization mistakes

### Practice
- [ ] Design 2 dashboards for given datasets
- [ ] Present 3 data stories (What happened? Why? What to do?)

---

## Mock Test

| Section | Questions | Time | Topics |
|:--------|:----------|:-----|:-------|
| SQL | 3 queries | 30 min | Topic 1 |
| Statistics | 3 problems | 20 min | Topic 2 |
| Python | 2 coding problems | 20 min | Topic 3 |
| Case/Communication | 2 scenarios | 20 min | Topic 4 |
| Behavioral | 3 questions | 10 min | Prep/behavioral |
| **Total** | **13** | **100 min** | |

---

## Rapid Revision

### Must-Know SQL Patterns
```sql
-- Window function
SELECT *, ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary DESC) AS rank
FROM employees;

-- CTE
WITH monthly_sales AS (
    SELECT DATE_TRUNC('month', order_date) AS month, SUM(amount) AS total
    FROM orders GROUP BY 1
)
SELECT month, total, LAG(total) OVER (ORDER BY month) AS prev_month
FROM monthly_sales;
```

### Statistics Quick Reference
| Concept | Formula/Rule |
|:--------|:-------------|
| Mean | Sum ÷ Count |
| Std Dev | √(Σ(x−μ)² ÷ N) |
| Z-score | (x − μ) ÷ σ |
| p-value | Probability of observing result if null is true |
| CI (95%) | Mean ± 1.96 × (σ ÷ √n) |

### Last-Minute Checklist
- [ ] Practiced 5 SQL queries (JOINs, window functions, CTEs)
- [ ] Reviewed hypothesis testing steps
- [ ] Reviewed Pandas operations (groupby, merge, pivot)
- [ ] Prepared 4 STAR stories
- [ ] Reviewed common chart types and when to use each
- [ ] Researched [company] data stack

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| Full Study Plan | [role-study-plan.md](role-study-plan.md) |
| Statistics Practice | [statistics-practice.md](statistics-practice.md) |
| SQL Practice | [../business-analyst/sql-practice.md](../business-analyst/sql-practice.md) |
| Non-Core Prep | [../analytics/non-core-prep.md](../analytics/non-core-prep.md) |
| Technical Stack | [../analytics/technical-stack.md](../analytics/technical-stack.md) |
| Behavioral Guide | [../../prep/behavioral/behavioral-interview-guide.md](../../prep/behavioral/behavioral-interview-guide.md) |

---

*Based on role-study-plan-template.md. Customized for Data Analyst role.*
