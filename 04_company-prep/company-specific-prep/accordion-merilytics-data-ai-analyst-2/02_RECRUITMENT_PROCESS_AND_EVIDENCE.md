# Module 02 — Recruitment Process, Selection Workflow & Evidence Ledger

## 1. Recruitment Pipeline Evidence Table

This table compares official campus proforma facts against verified candidate debriefs from Indian engineering campuses (IITs/NITs) and recruitment platforms:

```
┌────────────────────────┬───────────────────┬──────────────────────────────────────────┬───────────────────────┬────────────┐
│         Stage          │  Proforma Status  │         Publicly Reported Reality        │        Source         │ Confidence │
├────────────────────────┼───────────────────┼──────────────────────────────────────────┼───────────────────────┼────────────┤
│ 1. Pre-Placement Talk  │ Explicitly Listed │ 45–60 min overview of Accordion PE model │ Official CDPC Circular│ High       │
│    (PPT)               │                   │ and Merilytics analytics delivery hub.   │ & Campus Schedule     │            │
├────────────────────────┼───────────────────┼──────────────────────────────────────────┼───────────────────────┼────────────┤
│ 2. Resume Shortlist    │ Explicitly Listed │ Filters for quantitative GPA, Python/SQL │ Past Campus Placement │ High       │
│                        │                   │ projects, and analytical modeling.       │ Debriefs (IIT/NIT)    │            │
├────────────────────────┼───────────────────┼──────────────────────────────────────────┼───────────────────────┼────────────┤
│ 3. Technical Test      │ Explicitly Listed │ Online assessment covering SQL queries,  │ GeeksforGeeks, Glass- │ High       │
│                        │                   │ Excel modeling, Python logic, statistics.│ door, Campus Reports  │            │
├────────────────────────┼───────────────────┼──────────────────────────────────────────┼───────────────────────┼────────────┤
│ 4. Aptitude Test       │ Explicitly Listed │ Data interpretation, numerical reasoning,│ Board Infinity,       │ High       │
│                        │                   │ commercial arithmetic, logical puzzles.  │ GeeksforGeeks Debriefs│            │
├────────────────────────┼───────────────────┼──────────────────────────────────────────┼───────────────────────┼────────────┤
│ 5. Technical Interview │ Explicitly Listed │ 45–60 min round: Live SQL querying,      │ Verified Candidate    │ High       │
│    (Round 1 & Case)    │                   │ Excel modeling test, business caselet.   │ Interview Reports     │            │
├────────────────────────┼───────────────────┼──────────────────────────────────────────┼───────────────────────┼────────────┤
│ 6. HR & Values Fit     │ Explicitly Listed │ 30–45 min round: Behavioral fit, 5 Core  │ Glassdoor India,      │ High       │
│                        │                   │ Values, location fit (Hyderabad).        │ AmbitionBox           │            │
└────────────────────────┴───────────────────┴──────────────────────────────────────────┴───────────────────────┴────────────┘
```

> [!NOTE]
> Stages 3 & 4 (Technical and Aptitude tests) are typically administered as sequential sections within a single online test window on platforms like HackerEarth or Mettl.

---

## 2. Online Assessment Architecture (Stages 3 & 4)

The initial screening test is designed to evaluate both foundational numerical reasoning and practical coding proficiency under tight time constraints.

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 ONLINE ASSESSMENT SECTIONAL BREAKDOWN                                  │
├──────────────────────┬─────────────┬───────────┬───────────────────────────────────────────────────────┤
│       Section        │  Questions  │ Time Alloc│                      Core Topics                      │
├──────────────────────┼─────────────┼───────────┼───────────────────────────────────────────────────────┤
│ Section 1: Aptitude  │ 15–20 MCQs  │ 25–30 min │ • Percentages, ratios, profit & loss, weighted avg    │
│ & Commercial Math    │             │           │ • Data Interpretation (tables, stacked bar charts)    │
│                      │             │           │ • Speed, time & work, permutations & probability      │
├──────────────────────┼─────────────┼───────────┼───────────────────────────────────────────────────────┤
│ Section 2: Technical │ 15–20 MCQs  │ 25–30 min │ • SQL syntax, joins, grouping, null handling, windows │
│ Concepts (SQL/Excel) │             │           │ • Excel lookup logic (VLOOKUP, INDEX/MATCH, XLOOKUP)  │
│                      │             │           │ • Python data structures (lists, dicts, Pandas series)│
├──────────────────────┼─────────────┼───────────┼───────────────────────────────────────────────────────┤
│ Section 3: Hands-On  │ 2–3 Coding  │ 30–40 min │ • Write SQL queries to aggregate sales, detect nulls, │
│ SQL / Data Problems  │ Problems    │           │   find second-highest metric, and join 3 tables.      │
└──────────────────────┴─────────────┴───────────┴───────────────────────────────────────────────────────┘
```

### 2.1 Essential Online Test Mechanics
- **Negative Marking**: Typically 0.25 negative marking for multiple-choice questions; none for open coding queries.
- **Data Interpretation Heavy**: Unlike software engineer OAs that focus purely on LeetCode algorithms, Accordion (Merilytics) assessments feature multi-tiered financial tables (e.g., quarterly P&L statements, multi-region sales charts) where candidates must compute year-over-year growth, product mix contributions, and margin compressions.

---

## 3. The Technical & Case Interview (Stage 5)

The Technical Interview is conducted by Senior Analysts, Team Leads, or Delivery Managers from the Hyderabad office. It lasts between 45 and 60 minutes and is divided into three distinct segments:

```
┌─────────────────────────────────┬─────────────────────────────────┬─────────────────────────────────┐
│ Segment 1: Technical (20 mins)  │   Segment 2: Business (25 mins) │  Segment 3: Project (15 mins)   │
├─────────────────────────────────┼─────────────────────────────────┼─────────────────────────────────┤
│ • Live SQL query formulation    │ • Interactive business caselet  │ • Deep-dive into candidate's    │
│ • Screen-share or whiteboard    │ • Unit economics & trade-offs   │   analytical projects           │
│ • Excel modeling architecture   │ • Profitability decomposition   │ • Verification of model choices │
│ • Data cleaning edge cases      │ • "So-What" recommendation      │ • Data handling & validation    │
└─────────────────────────────────┴─────────────────────────────────┴─────────────────────────────────┘
```

### 3.1 Live SQL Screen-Share Drills
Interviewers frequently share a schema or paste sample table records into a collaborative editor (e.g., CoderPad, HackerRank, Google Docs) and ask the candidate to write queries in real time:
- *"Write a query to find the department that currently has no employees assigned."* (Requires `LEFT JOIN ... WHERE emp.id IS NULL` or `NOT EXISTS`).
- *"Find the top 2 highest-spending customers in each region."* (Requires `DENSE_RANK() OVER(PARTITION BY region ORDER BY spend DESC)`).
- *"Detect duplicate customer transactions occurring within 5 minutes of each other."* (Requires self-join or `LAG()` with `DATEDIFF`).

### 3.2 The Business Caselet Format
Merilytics evaluates how you structure ambiguous business problems. A classic interview archetype is the **Marketing / Commercial Trade-off Case**:
- **Scenario**: *"A client is deciding between two promotional channels to acquire customers: Channel A costs \$100,000 upfront with an expected conversion rate of 4% on 500,000 impressions; Channel B requires a 15% revenue share with an expected conversion rate of 7% on 300,000 impressions. The product sells for \$50 with an 80% gross margin. Which channel should the client select, and what is the break-even volume threshold?"*
- **Evaluation Criteria**: The interviewer is not just checking mental arithmetic; they evaluate whether you clarify assumptions (Does Channel A require creative production costs? Are repeat purchases included?), structure your calculations aloud, and conclude with a decisive recommendation and risk sensitivity.

---

## 4. The Managerial & HR Fit Interview (Stage 6)

Conducted by Associate Directors, Delivery Heads, or HR Leadership, this round evaluates **communication maturity, resilience under pressure, alignment with Accordion's 5 Core Values, and long-term commitment to Hyderabad**.

### 4.1 What Interviewers Look For
```
┌─────────────────────────────────┬────────────────────────────────────────────────────────────────────────┐
│       Evaluation Pillar         │                         What Interviewers Seek                         │
├─────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ 1. Client First Mindset         │ Demonstrates empathy for client deadlines, business impact, and zero-  │
│                                 │ error quality control.                                                 │
├─────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ 2. Handling Ambiguity           │ Shows structured autonomy; doesn't freeze when requirements are vague; │
│                                 │ asks clarifying questions and creates structured hypotheses.           │
├─────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ 3. Analytical Integrity         │ Transparent about data limitations; never hides anomalies or fabricates│
│                                 │ outputs; proactively flags risks early.                                │
├─────────────────────────────────┼────────────────────────────────────────────────────────────────────────┤
│ 4. Teamwork & Humility          │ Receptive to critical feedback; collaborative under intense client     │
│                                 │ pressure; zero arrogance regarding technical credentials.              │
└─────────────────────────────────┴────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Common Candidate Elimination Traps
1. **The "Pure Data Scientist" Trap**: Overemphasizing complex deep-learning neural networks while struggling to write a basic `GROUP BY ... HAVING` SQL query or explain an Excel `SUMIFS` formula.
2. **Descriptive Without Prescriptive**: Presenting numbers without answering the **"So-What?"** (e.g., stating *"Revenue dropped 12%"* without identifying which product line drove the drop and what operational action the client should take).
3. **Calculation Errors Under Pressure**: Rushing mental math without writing down intermediate units, leading to order-of-magnitude mistakes.
4. **Defensiveness on Engineering Background**: Being apologetic about an engineering degree rather than framing it as a quantitative and computational strength.

