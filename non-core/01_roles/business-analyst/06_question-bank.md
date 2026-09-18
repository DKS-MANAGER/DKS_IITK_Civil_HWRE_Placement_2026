# 06. Business Analyst (BA): High-Yield Question Bank

> Categorized interview questions with model answers, technical solutions, and interviewer follow-up questions.

---

### Question 1: [P0][SQL] Write a query to find the top 3 highest spending customers in each city.

**Direct Answer / Solution Approach:**
```text
SELECT customer_id, city, total_spend, RANK() OVER (PARTITION BY city ORDER BY total_spend DESC) as rnk FROM (SELECT customer_id, city, SUM(amount) as total_spend FROM orders JOIN customers USING(customer_id) GROUP BY 1, 2) WHERE rnk <= 3;
```

**Interviewer Follow-Up & Deep Dive:**
> Interviewer follow-up: How would you handle ties where 2 customers have the exact same spend? (Use DENSE_RANK vs RANK vs ROW_NUMBER).

---

### Question 2: [P0][CASE] Monthly Active Users (MAU) dropped 12% in the last 14 days. Walk through your investigation.

**Direct Answer / Solution Approach:**
```text
Step 1: Metric definition & validation. Step 2: Segment by Platform (iOS/Android/Web), Region (Tier 1 vs Tier 2), and User Cohorts (New vs Retained). Step 3: Check external factors (network outages, holidays, competitor promo). Step 4: Check internal factors (app update crash rate, payment gateway errors). Step 5: Formulate hypothesis and propose targeted fix.
```

**Interviewer Follow-Up & Deep Dive:**
> Interviewer follow-up: If Android crash rate is normal but Tier-2 payment success dropped 25%, what do you check next? (Local payment gateway API outage or UPI bank integration failure).

---

### Question 3: [P1][EXCEL] Explain when to use XLOOKUP vs INDEX-MATCH and how to handle dynamic array spills.

**Direct Answer / Solution Approach:**
```text
XLOOKUP is the modern default: supports leftward lookups, default exact match, and built-in missing value handling `=XLOOKUP(val, lookup_arr, return_arr, 'Not Found')`. INDEX-MATCH is preferred for high-throughput 2D matrix lookups `=INDEX(grid, MATCH(row_val, row_range, 0), MATCH(col_val, col_range, 0))`.
```

**Interviewer Follow-Up & Deep Dive:**
> Interviewer follow-up: How do you prevent `#SPILL!` errors in shared Excel workbooks? (Ensure destination range is clear of non-empty cells).

---

### Question 4: [P1][METRICS] A client's revenue grew 20% YoY but net profit margin shrank from 18% to 11%. Diagnose.

**Direct Answer / Solution Approach:**
```text
Deconstruct Profit = (Volume x Price x Mix) - (COGS + CAC + Logistics + Fixed SG&A). Investigate if revenue growth was driven by aggressive discounting on low-margin SKUs, or if customer acquisition costs (CAC) / delivery freight expanded faster than gross margins.
```

**Interviewer Follow-Up & Deep Dive:**
> Interviewer follow-up: What immediate operational levers would you recommend to the CFO? (Cap ad spend on low-margin products, renegotiate 3PL logistics slabs).

---

### Question 5: [P0][FIT] Why should we hire a Civil Engineering graduate for a Business Analyst role?

**Direct Answer / Solution Approach:**
```text
Frame with conviction: 'Civil engineering at IIT Kanpur is rigorous applied systems engineering. In my computational research, I manage multi-variable datasets, build quantitative models, and solve complex optimization problems under constraints. These exact analytical, data-modeling, and problem-solving skills translate directly into deconstructing business metrics, writing SQL queries, and optimizing business operations.'
```

**Interviewer Follow-Up & Deep Dive:**
> Interviewer follow-up: Give an example of a real dataset you analyzed and the measurable conclusion you reached.


---

## Related Question Banks in Repository
- 📖 [HR & Behavioral Question Bank](../../02_interview-preparation/behavioral/hr-questions.md)
- 📖 [Guesstimates Master Guide](../../02_interview-preparation/guesstimates/guesstimate-guide.md)
