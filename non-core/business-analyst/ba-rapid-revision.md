# Business Analyst — Rapid Revision Sheet

> Last-minute revision for BA interviews. SQL, Excel, KPI analysis quick reference in 15 minutes.

---

## SQL Quick Reference

### Essential Patterns
```sql
-- Ranking
SELECT *, RANK() OVER (ORDER BY metric DESC) AS rank FROM table;

-- Running total
SELECT *, SUM(metric) OVER (ORDER BY date ROWS UNBOUNDED PRECEDING) AS running_total FROM table;

-- Previous/next row
SELECT *, LAG(metric, 1) OVER (ORDER BY date) AS prev FROM table;

-- Top N per group
WITH ranked AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY group ORDER BY metric DESC) AS rn
    FROM table
)
SELECT * FROM ranked WHERE rn <= 3;

-- CTE for readability
WITH cte AS (SELECT ... FROM ... WHERE ...)
SELECT ... FROM cte WHERE ...;
```

### JOIN Types
```
INNER JOIN → Matching rows only
LEFT JOIN  → All left rows + matching right
FULL JOIN  → All rows from both
```

---

## Excel Quick Reference

### Key Formulas
| Formula | Purpose |
|:--------|:--------|
| VLOOKUP(value, range, col, FALSE) | Look up value in table |
| INDEX(MATCH()) | Flexible lookup (better than VLOOKUP) |
| IF(condition, true, false) | Conditional logic |
| SUMIF(range, criteria, sum_range) | Conditional sum |
| COUNTIF(range, criteria) | Conditional count |
| PIVOT TABLE | Summarize large datasets |

---

## KPI Quick Reference

| Business | Key KPIs |
|:---------|:---------|
| E-commerce | Conversion rate, AOV, cart abandonment, repeat rate |
| SaaS | MRR, churn, activation rate, NPS |
| Banking | CAC, LTV, default rate, NPS |
| Ride-hailing | Ride completion, surge frequency, driver utilization |
| Social media | DAU/MAU, engagement rate, content creation rate |

### Root-Cause Analysis Framework
```
1. DEFINE → What exactly happened? By how much? Since when?
2. SEGMENT → By customer type? Region? Product? Channel?
3. EXTERNAL → Seasonality? Competitor? Regulation?
4. INTERNAL → Product change? Process change? System issue?
5. HYPOTHESIS → Form 2-3 hypotheses
6. VALIDATE → Check data for each
7. RECOMMEND → Fix + prevent recurrence
```

---

## Last-Minute Checklist

- [ ] Practiced 5 SQL queries (JOINs, window functions)
- [ ] Reviewed pivot table creation
- [ ] Reviewed KPI frameworks for 3 business types
- [ ] Reviewed root-cause analysis framework
- [ ] Prepared 4 STAR stories
- [ ] Researched [company] business model

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| Full Study Plan | [role-study-plan.md](role-study-plan.md) |
| SQL Practice | [sql-practice.md](sql-practice.md) |
| Statistics | [../data-analyst/statistics-practice.md](../data-analyst/statistics-practice.md) |
| Behavioral Guide | [../../prep/behavioral/behavioral-interview-guide.md](../../prep/behavioral/behavioral-interview-guide.md) |

---

*Print this sheet 1 hour before your BA interview.*
