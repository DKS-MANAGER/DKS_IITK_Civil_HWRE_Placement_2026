# Technology / Tech-Adjacent — Role Study Plan

## Role Overview

The Technology role targets **tech-adjacent positions** at software companies (Google, Microsoft, Amazon), **IT services** (TCS, Infosys, Accenture, Wipro), **fintech** (Paytm, PhonePe, Razorpay), and **product companies**. The role covers SQL, Python, software development lifecycle, APIs, cloud fundamentals, and product/analytics thinking. Civil engineers with programming exposure (Python, MATLAB), CFD modeling, and data analysis transition well into tech-adjacent roles — you don't need a CS degree.

**Who targets this role:** B.Tech/M.Tech graduates with Python/SQL skills, students with computational projects (CFD, numerical methods), those interested in software and data, GATE qualifiers with coding interest.

---

## 3–4 Highest-Value Preparation Blocks

### Topic 1: SQL & Data Manipulation

#### Why This Matters
SQL is the most-tested technical skill in tech-adjacent interviews. Every role — analyst, PM, solutions engineer — requires querying data. You must be fluent in SELECT, JOINs, aggregations, and window functions.

#### What to Learn
- [ ] SELECT, WHERE, ORDER BY, LIMIT
- [ ] Aggregations: COUNT, SUM, AVG, MIN, MAX, GROUP BY, HAVING
- [ ] JOINs: INNER, LEFT, RIGHT, FULL, CROSS
- [ ] Subqueries and CTEs (WITH)
- [ ] Window functions: ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD, SUM OVER
- [ ] CASE statements
- [ ] String and date functions
- [ ] DISTINCT, UNION, INTERSECT, EXCEPT
- [ ] Query optimization basics (indexes, EXPLAIN)

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`tech-overview.md`](tech-overview.md) | SQL, Python, tech concepts | Full |
| [`sql-practice.md`](../business-analyst/sql-practice.md) | SQL practice problems | Full |
| [`sql.md`](../../software-and-tech/programming/sql.md) | SQL fundamentals | Reference |

#### Worked Example
**Problem:** Given tables `orders(order_id, customer_id, amount, order_date)` and `customers(customer_id, name, city)`, write SQL to: (a) find total revenue by city, (b) find the top 3 customers by revenue, (c) find customers who ordered in every month of 2025.

**Solution:**
```sql
-- (a) Total revenue by city
SELECT c.city, SUM(o.amount) AS total_revenue
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.city
ORDER BY total_revenue DESC;

-- (b) Top 3 customers by revenue
SELECT c.name, SUM(o.amount) AS revenue
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.name
ORDER BY revenue DESC
LIMIT 3;

-- (c) Customers who ordered in every month of 2025
SELECT customer_id
FROM orders
WHERE YEAR(order_date) = 2025
GROUP BY customer_id
HAVING COUNT(DISTINCT MONTH(order_date)) = 12;
```

**Interview insight:** "I'd use JOIN + GROUP BY for aggregations, and HAVING with COUNT(DISTINCT) for the 'every month' condition. For top-N, ORDER BY + LIMIT is simplest, but I'd mention ROW_NUMBER() OVER (PARTITION BY ...) if the interviewer wants per-group top-N."

#### Practice
**Basic (3–5):**
1. Write a query to find the total sales per product.
2. What is the difference between INNER and LEFT JOIN?
3. Write a query to find duplicate records.
4. What is the difference between WHERE and HAVING?
5. Write a query to find the second-highest salary.

**Intermediate (3–5):**
6. Write a query to find top 5 products by revenue per region (window function).
7. Find customers with no orders in the last 90 days.
8. Compute month-over-month revenue growth using LAG.
9. Write a query to find the running total of sales.
10. Find the most common product per customer segment.

**Interview-Level (5+):**
11. How do you optimize a slow query?
12. What is the difference between a primary key and a foreign key?
13. How do you handle NULLs in aggregations?
14. Write a query to find customers who bought product A but not product B.
15. How do you deduplicate a table?

#### Interview Questions (What Interviewer Tests)
| Question | What They're Testing |
|:---------|:---------------------|
| Write a query to find top 5 by revenue | SQL fluency |
| What's the difference between WHERE and HAVING? | Fundamentals |
| How do you optimize a slow query? | Performance thinking |
| Write a window function query | Advanced SQL |
| How do you handle NULLs? | Edge cases |

#### Common Mistakes
- **Confusing** WHERE (row filter) with HAVING (group filter)
- **Forgetting** that JOINs can create duplicates — use DISTINCT carefully
- **Not** handling NULLs in aggregations
- **Writing** queries without testing edge cases
- **Ignoring** query performance on large tables

#### Completion Criterion
✅ Can write JOIN, aggregation, and window function queries
✅ Can solve top-N, dedup, and month-over-month problems
✅ Can explain query optimization basics
✅ Can handle NULLs and edge cases

---

### Topic 2: Python & Data Analysis

#### Why This Matters
Python is the second most-tested skill. You need Pandas/NumPy for data manipulation and basic algorithmic thinking for coding rounds.

#### What to Learn
- [ ] Python basics: Lists, dicts, loops, functions, comprehensions
- [ ] Pandas: DataFrame, Series, read_csv, groupby, merge, pivot
- [ ] NumPy: Arrays, vectorized operations
- [ ] Data cleaning: Missing values, duplicates, type conversion
- [ ] Data visualization: Matplotlib, Seaborn basics
- [ ] Basic algorithms: Two-pointer, sliding window, hash maps
- [ ] File handling and JSON
- [ ] Error handling (try/except)

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`tech-overview.md`](tech-overview.md) | Python, data concepts | Full |
| [`python.md`](../../software-and-tech/programming/python.md) | Python fundamentals | Reference |
| [`data-analytics-stack.md`](../../software-and-tech/data/data-analytics-stack.md) | Data tools | Reference |

#### Worked Example
**Problem:** Using Pandas, load a CSV of sales data, compute total revenue by product, find the top 3 products, and identify the month with highest sales.

**Solution:**
```python
    import pandas as pd

    # Load data
    df = pd.read_csv('sales.csv')  # columns: product, amount, month

    # Total revenue by product
    revenue_by_product = df.groupby('product')['amount'].sum().sort_values(ascending=False)
    print(revenue_by_product)

    # Top 3 products
    top_3 = revenue_by_product.head(3)
    print(top_3)

    # Month with highest sales
    monthly = df.groupby('month')['amount'].sum()
    best_month = monthly.idxmax()
    print(f"Best month: {best_month}, Sales: {monthly.max()}")
```

**Interview insight:** "I'd use groupby + sum for aggregation, sort_values for ranking, and idxmax for the best month. The key is writing clean, vectorized Pandas rather than loops — it's faster and more readable."

#### Practice
**Basic (3–5):**
1. What is the difference between a list and a tuple?
2. How do you read a CSV in Pandas?
3. What is a DataFrame?
4. How do you handle missing values?
5. Write a function to reverse a string.

**Intermediate (3–5):**
6. Compute groupby aggregations in Pandas.
7. Merge two DataFrames.
8. Write a function to find duplicates in a list.
9. How do you handle a large dataset in Python?
10. Write a function to check if a string is a palindrome.

**Interview-Level (5+):**
11. How do you optimize a slow Python script?
12. Explain the difference between a list comprehension and a generator.
13. How do you handle memory issues with large datasets?
14. Write a function to find the two numbers that sum to a target.
15. How do you automate a reporting task with Python?

#### Common Mistakes
- **Using** loops instead of vectorized Pandas operations
- **Not** handling missing values before analysis
- **Ignoring** memory for large datasets
- **Writing** code without testing edge cases
- **Not** using functions — repetitive code

#### Completion Criterion
✅ Can load, clean, and analyze data with Pandas
✅ Can write basic algorithms (two-pointer, hash map)
✅ Can handle missing values and large datasets
✅ Can automate a reporting task

---

### Topic 3: Software Development & Cloud Fundamentals

#### Why This Matters
Tech-adjacent roles require understanding how software is built and deployed. SDLC, Agile, APIs, and cloud concepts are tested in interviews to assess your technical literacy.

#### What to Learn
- [ ] SDLC: Requirements → Design → Development → Testing → Deployment → Maintenance
- [ ] Agile/Scrum: Sprints, backlog, stand-ups, retrospectives
- [ ] APIs: REST, HTTP methods (GET, POST, PUT, DELETE), status codes
- [ ] Databases: Relational vs non-relational, primary/foreign keys
- [ ] Cloud: IaaS, PaaS, SaaS; AWS/Azure/GCP basics
- [ ] Version control: Git basics (commit, branch, merge)
- [ ] Testing: Unit, integration, regression
- [ ] DevOps concepts: CI/CD

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`tech-overview.md`](tech-overview.md) | SDLC, Agile, APIs, cloud | Full |
| [`software-interview-guide.md`](../../prep/interview/software-interview-guide.md) | Software interview prep | Full |
| [`git.md`](../../software-and-tech/programming/git.md) | Git fundamentals | Reference |

#### Worked Example
**Problem:** Explain how a request flows through a web application, from the user's browser to the database and back.

**Solution:**
1. **Client:** User clicks a button in the browser
2. **HTTP Request:** Browser sends a GET/POST request to the server via an API endpoint
3. **Server:** The application server receives the request, routes it to the appropriate handler
4. **Business Logic:** The handler processes the request (validation, calculations)
5. **Database:** The server queries the database (SQL) to read/write data
6. **Response:** The server formats the result (JSON) and sends an HTTP response with a status code (200 OK)
7. **Client:** The browser renders the response to the user

**Interview insight:** "I'd describe this as a request-response cycle: client → API → server → database → back. I'd mention REST principles (stateless, resource-based), HTTP methods, and status codes. This shows I understand the full stack even without being a developer."

#### Practice
**Basic (3–5):**
1. What is the software development lifecycle?
2. What is an API? What is REST?
3. What are the HTTP methods?
4. What is the difference between relational and non-relational databases?
5. What is Agile development?

**Intermediate (3–5):**
6. Explain the difference between IaaS, PaaS, and SaaS.
7. What is a primary key vs a foreign key?
8. What is CI/CD?
9. How do you handle a production bug?
10. What is the difference between unit and integration testing?

**Interview-Level (5+):**
11. How would you design a database for an e-commerce site?
12. Explain the difference between on-premise and cloud.
13. How do you decide between building vs buying software?
14. How do you translate technical requirements to business stakeholders?
15. How do you handle a system that's slow under load?

#### Common Mistakes
- **Confusing** IaaS, PaaS, and SaaS
- **Not** knowing HTTP status codes (200, 404, 500)
- **Treating** Agile as a process, not a mindset
- **Ignoring** the business value of technical decisions
- **Not** being able to explain technical concepts simply

#### Completion Criterion
✅ Can explain SDLC, Agile, and APIs
✅ Can describe cloud service models (IaaS/PaaS/SaaS)
✅ Can explain database concepts and design basics
✅ Can translate technical concepts to business stakeholders

---

### Topic 4: Product Thinking & Analytical Case Studies

#### Why This Matters
Tech-adjacent roles increasingly test product thinking and analytical problem-solving. You must be able to analyze metrics, investigate problems, and make data-driven recommendations.

#### What to Learn
- [ ] Product metrics: DAU/MAU, retention, churn, conversion, LTV, CAC
- [ ] A/B testing: Hypothesis, control vs treatment, significance
- [ ] Funnel analysis: Identify drop-off points
- [ ] Root-cause analysis for metric changes
- [ ] Framework: Define → Measure → Analyze → Recommend
- [ ] SQL + Python for metric analysis
- [ ] Data storytelling and visualization
- [ ] Prioritization: RICE, MoSCoW

#### Study Material
| File | Focus Area | Depth |
|:-----|:-----------|:------|
| [`tech-overview.md`](tech-overview.md) | Product metrics, A/B testing | Full |
| [`pm-overview.md`](../product-management/pm-overview.md) | Product thinking | Reference |
| [`statistics-practice.md`](../data-analyst/statistics-practice.md) | Statistics for analysis | Reference |

#### Worked Example
**Problem:** A product's DAU dropped 15% this week. How do you investigate?

**Solution (Structured):**
1. **Define the problem:** DAU dropped 15% week-over-week. Is it a real drop or a data issue?
2. **Segment the data:**
   - By platform (iOS, Android, Web)
   - By geography
   - By user segment (new vs returning)
   - By feature usage
3. **Check external factors:**
   - Seasonality (holiday, weekend effect)
   - Competitor launches
   - Marketing campaigns (spend changes)
   - Technical incidents (outage, crash)
4. **Analyze root cause:**
   - If iOS-only → app store issue or iOS bug
   - If new users only → acquisition problem
   - If returning users only → retention/engagement problem
5. **Recommend:**
   - Fix the identified bug/issue
   - Adjust campaign timing
   - Improve onboarding or engagement features

**Interview insight:** "I'd segment before concluding — a 15% overall drop could be driven by one segment (e.g., iOS users after a crash). I'd check data quality first, then external factors, then segment-level analysis. The recommendation follows the root cause, not the symptom."

#### Practice
**Basic (3–5):**
1. What is DAU? What is MAU?
2. What is retention rate?
3. What is a funnel analysis?
4. What is A/B testing?
5. What is the difference between LTV and CAC?

**Intermediate (3–5):**
6. A metric fell 20%. How do you investigate?
7. Design an A/B test for a new feature.
8. How do you measure the impact of a product change?
9. What is churn? How do you reduce it?
10. How do you prioritize features?

**Interview-Level (5+):**
11. How do you decide if a metric change is significant?
12. What are the pitfalls of A/B testing?
13. How do you balance short-term metrics and long-term value?
14. How do you communicate a data insight to non-technical stakeholders?
15. How would you improve the onboarding flow of an app?

#### Common Mistakes
- **Jumping** to conclusions without segmenting data
- **Ignoring** external factors (seasonality, incidents)
- **Not** checking data quality first
- **Confusing** correlation with causation
- **Not** tying analysis to a recommendation

#### Completion Criterion
✅ Can investigate a metric change systematically
✅ Can design and interpret an A/B test
✅ Can analyze a funnel and identify drop-offs
✅ Can communicate insights with data

---

## Mock Test (45 Minutes)

| # | Question | Topic | Marks |
|---|:---------|:------|------:|
| 1 | Write SQL: total revenue by city, top 3 customers, customers who ordered every month of 2025. | SQL | 25 |
| 2 | Write Python (Pandas): load sales CSV, compute revenue by product, find top 3 and best month. | Python | 25 |
| 3 | Explain the request flow through a web application. Describe REST, HTTP methods, and status codes. | Software | 20 |
| 4 | A product's DAU dropped 15%. Structure your investigation and recommendations. | Product Thinking | 20 |
| 5 | Explain IaaS, PaaS, SaaS with examples. | Cloud | 10 |
| | | **Total** | **100** |

---

## Company Navigation

| Company | What They Test | Focus |
|:--------|:---------------|:------|
| **Google** | Analytical, Googleyness | SQL + Product |
| **Microsoft** | Growth mindset, technical | SQL + Python |
| **Amazon** | Leadership principles | Behavioral + Data |
| **TCS/Infosys** | Aptitude, basics, communication | SQL + SDLC |
| **Accenture** | Case + technical | SQL + Product |
| **Paytm/PhonePe** | SQL + product | SQL + Metrics |
| **Razorpay** | Technical + product | SQL + APIs |
| **Flipkart** | Ownership, data | SQL + Case |

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| Technology Overview | [tech-overview.md](tech-overview.md) |
| SQL Practice | [sql-practice.md](../business-analyst/sql-practice.md) |
| Statistics Practice | [statistics-practice.md](../data-analyst/statistics-practice.md) |
| Product Management | [pm-overview.md](../product-management/pm-overview.md) |
| Software Interview Guide | [software-interview-guide.md](../../prep/interview/software-interview-guide.md) |
| Rapid Revision | [tech-rapid-revision.md](tech-rapid-revision.md) |

---

*You don't need to be a software engineer to work in tech. You need to understand how tech works and how it creates business value.*