# 🗄️ SQL for Civil Engineering

> **Tag:** `[MUST LEARN]` for BA/DA/PA/Analytics roles, `[HIGH ROI]` for operations | **Target Level:** L3
> **Time to L2:** 10–15 hours | **Time to L3:** 20–30 hours

---

## What is it?

SQL (Structured Query Language) is the standard language for querying and managing data in relational databases. For Civil students targeting non-core roles (BA, DA, PA, Analytics), SQL is a critical interview skill.

## Why is it used?

- Every company stores operational data in relational databases
- Analysts must query this data independently without engineering teams
- SQL tests appear in almost every analytics/BA/DA placement test
- Understanding databases helps with data pipeline and architecture discussions
- Construction companies use databases for project tracking, inventory, and costs

## Civil Engineering Applications

| Application | Branch | Context |
|:------------|:-------|:--------|
| Project data management | Construction | Tracking materials, costs, schedules |
| Sensor database queries | HWRE / Hydrology | Time-series from monitoring stations |
| Water quality records | Environmental | Lab results, compliance data |
| Traffic data analysis | Transportation | Count data, incident records |
| GIS attribute queries | GIS | Spatial database queries (PostGIS) |

## Relevant Branches

- [ ] Structural (limited use)
- [ ] Geotechnical (limited use)
- [x] Transportation (traffic data)
- [x] Environmental (water quality data)
- [x] Hydraulics / HWRE (sensor data)
- [x] Hydrology (rainfall/runoff databases)
- [x] Construction Management (project databases)
- [x] GIS / Geoinformatics (PostGIS)
- [x] General Civil (if targeting non-core)

## Relevant Job Roles

| Role | Required? | Proficiency Needed |
|:-----|:----------|:-------------------|
| Business Analyst | Essential | L3 |
| Data Analyst | Essential | L3 |
| Product Analyst | Essential | L3 |
| Analytics | Essential | L3 |
| Operations Analyst | Useful | L2–L3 |
| Supply Chain Analyst | Useful | L2–L3 |
| Consulting (analytics) | Useful | L2–L3 |
| Core Civil roles | Optional | L1–L2 |

## Required Prerequisites

```
Must know:
- None — SQL can be learned from scratch

Helpful:
- Basic data concepts (rows, columns, tables)
- Understanding of what a database is
```

## Core Features to Learn

### Must-know (L2)

```
1. SELECT, FROM, WHERE
2. ORDER BY, LIMIT
3. Comparison operators (=, <, >, <=, >=, !=, IN, BETWEEN)
4. AND, OR, NOT
5. LIKE and wildcard patterns (%)
6. COUNT, SUM, AVG, MIN, MAX
7. GROUP BY with HAVING
8. NULL handling (IS NULL, IS NOT NULL, COALESCE)
```

### Important for placement (L2–L3)

```
9. JOIN types: INNER, LEFT, RIGHT, FULL OUTER
10. Self-joins
11. Subqueries (WHERE, FROM, SELECT)
12. Common Table Expressions (WITH ... AS)
13. Window functions: ROW_NUMBER, RANK, DENSE_RANK
14. Window functions: LAG, LEAD, running totals
15. CASE WHEN conditional logic
16. Date functions (DATE_TRUNC, EXTRACT, DATEADD)
17. String functions (CONCAT, SUBSTRING, TRIM, UPPER)
```

### Advanced (L3+)

```
18. UNION, UNION ALL, INTERSECT, EXCEPT
19. EXISTS and NOT EXISTS
20. Correlated subqueries
21. PIVOT / UNPIVOT
22. Complex window functions (NTILE, PERCENT_RANK)
23. Query optimization basics (indexes, EXPLAIN)
24. CREATE TABLE, INSERT, UPDATE, DELETE basics
```

## What NOT to Waste Time Learning

```
Do NOT spend time on:
- Database administration (DBA tasks)
- Advanced performance tuning
- Stored procedures and functions
- NoSQL databases (for placement purposes)
- Database design / normalization deep-dive
- Oracle PL/SQL or T-SQL specifics (unless company-specific)
```

## Typical Industry Workflow

```
Step 1: Understand — What business question are you answering?
Step 2: Identify — Which tables contain the relevant data?
Step 3: Join — Connect tables using keys
Step 4: Filter — Apply WHERE conditions
Step 5: Aggregate — GROUP BY for summaries
Step 6: Window — Use window functions for rankings, running totals
Step 7: Format — CASE WHEN, aliases, formatting for presentation
Step 8: Validate — Check row counts, null values, edge cases
```

## Example Project: Construction Project Analytics

```sql
-- Problem: Find the top 5 contractors by total project value,
-- along with average delay per project

WITH contractor_stats AS (
    SELECT
        c.contractor_name,
        COUNT(p.project_id) AS total_projects,
        SUM(p.budget) AS total_value,
        AVG(DATEDIFF(day, p.planned_end, p.actual_end)) AS avg_delay_days
    FROM contractors c
    JOIN projects p ON c.contractor_id = p.contractor_id
    WHERE p.status IN ('completed', 'delayed')
    GROUP BY c.contractor_name
)
SELECT
    contractor_name,
    total_projects,
    total_value,
    ROUND(avg_delay_days, 1) AS avg_delay_days,
    CASE
        WHEN avg_delay_days > 30 THEN 'High Risk'
        WHEN avg_delay_days > 10 THEN 'Medium Risk'
        ELSE 'Low Risk'
    END AS risk_category
FROM contractor_stats
ORDER BY total_value DESC
LIMIT 5;
```

## Interview Questions

### Basic (101)
- What is the difference between WHERE and HAVING?
- What are the different types of JOINs?
- How does GROUP BY work?

### Practical (201)
- Write a query to find duplicate records in a table.
- How do you find the second highest salary without LIMIT?
- Write a query to calculate running total of daily sales.
- What is the difference between RANK() and DENSE_RANK()?

### Technical (301)
- Explain correlated subqueries with an example.
- When would you use a CTE vs a subquery?
- How do window functions differ from GROUP BY?
- Optimize a query that's scanning an entire table.

### Project Defense
- Describe your database schema. Why did you design it that way?
- What was the most complex query you wrote?
- How did you handle data quality issues (missing values, duplicates)?

## Common Mistakes

| Mistake | Why It's Wrong | Correct Approach |
|:--------|:---------------|:-----------------|
| SELECT * in production queries | Slow, returns unnecessary data | Select specific columns |
| Missing GROUP BY for aggregates | SQL error or incorrect results | Group all non-aggregated columns |
| Using WHERE instead of HAVING | WHERE filters rows, HAVING filters groups | Use HAVING for aggregate conditions |
| Not handling NULLs | NULL comparisons return NULL, not TRUE/FALSE | Use IS NULL, COALESCE |
| Joining without specifying join type | May produce unexpected Cartesian products | Always specify INNER/LEFT/RIGHT |

## Alternatives

| Alternative | When to Use Instead | Key Difference |
|:------------|:-------------------|:---------------|
| Python (Pandas) | Complex transformations, non-tabular data | In-memory, more flexible |
| Excel | Small datasets, non-technical stakeholders | Visual, but limited scale |
| R | Statistical analysis | Stronger statistical functions |

## Learning Roadmap

```
Beginner (0–10 hrs):
    → SQLBolt or W3Schools SQL tutorial
    → SELECT, WHERE, ORDER BY, basic aggregates
    → 10 easy practice problems

Intermediate (10–20 hrs):
    → JOINs (all types), subqueries, GROUP BY + HAVING
    → Window functions basics
    → 20 LeetCode/HackerRank SQL problems (Easy–Medium)

Advanced (20–30 hrs):
    → CTEs, complex window functions, CASE WHEN
    → 15 LeetCode SQL problems (Medium–Hard)
    → Build a mini-project with real data
```

## Quick Reference Card

| Property | Value |
|:---------|:------|
| **Type** | Query language for relational databases |
| **Standard** | ANSI SQL |
| **License** | Open standard (implementations vary) |
| **Platform** | Any database system (PostgreSQL, MySQL, SQLite) |
| **Difficulty** | Easy to start, moderate to master |
| **Time to L2** | 10–15 hours |
| **Time to L3** | 20–30 hours |
| **Primary use** | Data querying and analysis |
| **Main alternative** | Pandas (Python) |

---

*See also: [`python.md`](python.md) for Pandas data analysis, [`data-analytics-stack.md`](../data/data-analytics-stack.md) for the full data stack.*
