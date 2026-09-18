# 06. Data Analyst: High-Yield Question Bank

> Categorized interview questions with model answers, technical solutions, and interviewer follow-up questions.

---

### Question 1: [P0][SQL] Write a query to find the second highest salary without using LIMIT or TOP.

**Direct Answer / Solution Approach:**
```text
SELECT MAX(salary) as second_highest FROM employees WHERE salary < (SELECT MAX(salary) FROM employees); -- Or using DENSE_RANK(): WITH ranked AS (SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) as rnk FROM employees) SELECT salary FROM ranked WHERE rnk = 2 LIMIT 1;
```

**Interviewer Follow-Up & Deep Dive:**
> Interviewer follow-up: What if there are multiple employees tied for the 2nd highest salary?

---

### Question 2: [P0][TECH] Explain how a composite database index works and the Leftmost Prefix rule.

**Direct Answer / Solution Approach:**
```text
A composite index on `(city, signup_date, user_status)` creates a multi-column B-Tree. The database engine can use the index for queries filtering on `(city)`, `(city, signup_date)`, or `(city, signup_date, user_status)`. It CANNOT use the index efficiently if the query filters only on `(signup_date)` without `city`.
```

**Interviewer Follow-Up & Deep Dive:**
> Interviewer follow-up: How do you check if your SQL query is actually using the index? (Run `EXPLAIN ANALYZE` and look for Index Scan vs Sequential Scan).


---

## Related Question Banks in Repository
- 📖 [HR & Behavioral Question Bank](../../02_interview-preparation/behavioral/hr-questions.md)
- 📖 [Guesstimates Master Guide](../../02_interview-preparation/guesstimates/guesstimate-guide.md)
