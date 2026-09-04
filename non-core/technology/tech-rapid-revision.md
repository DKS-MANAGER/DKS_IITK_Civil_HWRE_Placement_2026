# Technology / Tech-Adjacent — Rapid Revision Sheet

> Last-minute cheat sheet. Covers all core concepts, patterns, and quick-fire Q&A for tech-adjacent interviews.

---

## Framework 1: SQL Essential Patterns

### Core Query Structure
```sql
SELECT columns
FROM table
WHERE condition          -- row filter
GROUP BY columns         -- aggregation groups
HAVING condition         -- group filter
ORDER BY columns         -- sorting
LIMIT n;                 -- top-n
```

### JOINs
| Join | Returns |
|:-----|:--------|
| **INNER** | Matching rows in both tables |
| **LEFT** | All left rows + matches from right |
| **RIGHT** | All right rows + matches from left |
| **FULL** | All rows from both tables |

### Common Patterns
```sql
-- Top-N per group (window function)
SELECT * FROM (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY region ORDER BY revenue DESC) AS rn
  FROM sales
) t WHERE rn <= 3;

-- Month-over-month growth
SELECT month, revenue,
       revenue - LAG(revenue) OVER (ORDER BY month) AS mom_change
FROM monthly_sales;

-- Customers active every month
SELECT customer_id FROM orders
WHERE YEAR(order_date) = 2025
GROUP BY customer_id
HAVING COUNT(DISTINCT MONTH(order_date)) = 12;
```

### WHERE vs HAVING
```
WHERE  = filters rows BEFORE grouping
HAVING = filters groups AFTER grouping
```

---

## Framework 2: Python & Pandas

### Pandas Essentials
```python
    import pandas as pd

    df = pd.read_csv('data.csv')
    df.head(), df.info(), df.describe()

    # Groupby aggregation
    df.groupby('product')['amount'].sum()

    # Handle missing values
    df.dropna(), df.fillna(0)

    # Merge
    pd.merge(df1, df2, on='customer_id', how='left')

    # Pivot
    df.pivot_table(index='month', columns='product', values='amount', aggfunc='sum')
```

### Common Algorithms
```python
    # Two-pointer (find pair summing to target)
    def two_sum(nums, target):
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            seen[n] = i
        return []

    # Palindrome check
    def is_palindrome(s):
        return s == s[::-1]
```

### Performance Tips
```
Use vectorized Pandas (no loops)
Use .loc/.iloc for selection
Use groupby + agg instead of apply where possible
Chunk large files (read_csv chunksize)
```

---

## Framework 3: Software & Cloud Fundamentals

### SDLC
```
Requirements → Design → Development → Testing → Deployment → Maintenance
```

### REST API
```
HTTP Methods: GET (read), POST (create), PUT (update), DELETE (remove)
Status Codes: 200 OK, 201 Created, 400 Bad Request, 404 Not Found, 500 Server Error
REST Principles: Stateless, resource-based, standard methods
```

### Databases
| Type | Example | Best For |
|:-----|:--------|:---------|
| **Relational (SQL)** | MySQL, PostgreSQL | Structured data, transactions |
| **Non-relational (NoSQL)** | MongoDB, DynamoDB | Flexible schema, scale |

### Cloud Service Models
```
IaaS = Infrastructure (servers, storage) — AWS EC2
PaaS = Platform (deploy apps) — Heroku, AWS Elastic Beanstalk
SaaS = Software (use via browser) — Gmail, Salesforce
```

### Agile/Scrum
```
Sprint → Backlog → Stand-up → Review → Retrospective
Roles: Product Owner, Scrum Master, Dev Team
```

---

## Framework 4: Product Thinking & Analysis

### Metric Investigation Framework
```
1. Define the problem (what metric, what change)
2. Check data quality (is it a real change?)
3. Segment (platform, geography, user type, feature)
4. Check external factors (seasonality, incidents, campaigns)
5. Find root cause
6. Recommend (tied to root cause)
```

### Key Metrics
```
DAU/MAU = Daily/Monthly Active Users
Retention = % of users returning after period
Churn = % of users lost
Conversion = % completing target action
LTV = Lifetime Value (revenue per user over lifetime)
CAC = Customer Acquisition Cost
```

### A/B Testing
```
Hypothesis → Split users (control vs treatment)
→ Run → Check significance (p < 0.05)
→ Decide (ship, iterate, or kill)
Pitfalls: small samples, peeking, multiple tests, novelty effect
```

### Funnel Analysis
```
Define steps → Measure conversion at each step
→ Identify biggest drop-off → Investigate → Improve
```

---

## 10 Quick-Fire Interview Answers

**Q1: What is the difference between SQL and Python?**
A: SQL is for querying and aggregating data in databases. Python is a general-purpose language for data manipulation, analysis, automation, and building applications. They're complementary — SQL extracts, Python analyzes.

**Q2: What is an API?**
A: An Application Programming Interface — a way for software to talk to each other. REST APIs use HTTP methods (GET, POST, PUT, DELETE) to access resources, returning JSON responses.

**Q3: What is the difference between a primary key and a foreign key?**
A: A primary key uniquely identifies each row in a table. A foreign key references a primary key in another table, creating a relationship between tables.

**Q4: What is the difference between WHERE and HAVING?**
A: WHERE filters rows before grouping; HAVING filters groups after aggregation. You use HAVING with GROUP BY conditions like COUNT(*) > 5.

**Q5: What is Agile development?**
A: An iterative approach to software development with short sprints, continuous feedback, and adaptive planning. Key events: sprint planning, daily stand-up, review, retrospective.

**Q6: What is the difference between IaaS, PaaS, and SaaS?**
A: IaaS provides infrastructure (servers, storage), PaaS provides a platform to deploy apps, SaaS provides ready-to-use software. They differ in how much you manage vs the provider.

**Q7: How do you handle a large dataset in Python?**
A: Use vectorized Pandas operations, chunk the file with read_csv(chunksize), filter early, and use appropriate dtypes. For very large data, consider sampling or distributed tools.

**Q8: What is a window function in SQL?**
A: A function that computes a value across a set of rows related to the current row — like ROW_NUMBER, RANK, LAG, or SUM OVER. It lets you do top-N per group and running totals without collapsing rows.

**Q9: How does a civil engineering background help in tech?**
A: Python/MATLAB programming, CFD and numerical methods (computational thinking), data analysis from research, and project management — all transferable to tech-adjacent roles.

**Q10: A product metric fell. How do you investigate?**
A: Check data quality first, then segment (platform, geography, user type), check external factors (seasonality, incidents), find the root cause, and recommend a fix tied to that cause.

---

## Last-Minute Checklist

### Before Any Tech Interview
- [ ] SQL: JOINs, GROUP BY, window functions (practice 5 queries)
- [ ] Python: Pandas groupby/merge, 2-3 algorithms
- [ ] Know SDLC, Agile, REST, cloud models
- [ ] Your "Why tech?" answer (link to civil engineering)

### Must-Know Concepts
- [ ] WHERE vs HAVING
- [ ] INNER vs LEFT JOIN
- [ ] Window functions (ROW_NUMBER, LAG)
- [ ] IaaS vs PaaS vs SaaS
- [ ] HTTP methods and status codes
- [ ] DAU/MAU, retention, churn, LTV/CAC

### Behavioral Prep
- [ ] "Tell me about a technical project" (STAR)
- [ ] "Describe a time you learned a new tool" (STAR)
- [ ] "How do you handle ambiguity?" (STAR)
- [ ] "Tell me about a time you used data to make a decision" (STAR)

---

## Cross-Links

**Technology:**
→ [Technology Overview](tech-overview.md) — Complete preparation system
→ [Role Study Plan](role-study-plan.md) — Structured study plan

**Related:**
→ [SQL Practice](../business-analyst/sql-practice.md) — SQL problems
→ [Statistics Practice](../data-analyst/statistics-practice.md) — Stats for analysis
→ [Software Interview Guide](../../prep/interview/software-interview-guide.md) — Interview prep

---

*Last updated: 2026-09-04*