# Campus Assessment Strategy & Test Structure

**Target Role:** Data Scientist / Associate Data Scientist | Tredence Analytics  
**Context:** IIT Kanpur Placement Season 2026–27  
**Test Formats:** Online Assessment (OA) — Typically hosted on platforms such as HackerEarth, Mettl, or Glider.ai

---

## 1. Typical Assessment Section Breakdown

Based on campus recruitment benchmarks for Tredence Analytics Data Scientist roles:

```
 Total Assessment Duration: 90 - 120 Minutes
 ┌────────────────────────────────────────────────────────────────────────┐
 │ Section 1: Quantitative Aptitude & Logical Reasoning (20 Qs, ~25 mins)  │
 ├────────────────────────────────────────────────────────────────────────┤
 │ Section 2: Core Python & Algorithmic Fluency (10 MCQs + 1 Code, ~30 mins)│
 ├────────────────────────────────────────────────────────────────────────┤
 │ Section 3: Advanced ANSI SQL & Data Manipulation (10 MCQs + 1 Query)   │
 ├────────────────────────────────────────────────────────────────────────┤
 │ Section 4: Machine Learning, Statistics & GenAI (20 MCQs, ~25 mins)    │
 └────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Topic Weightage & Time Allocation Matrix

| Section | Questions | Weightage | Target Time per Question | Strategy & Traps |
|---|---|---|---|---|
| **Quantitative & Logical Aptitude** | 15–20 | 25% | 60–75 seconds | Skip lengthy time-consuming puzzle arrangements; lock quick math (P&C, Bayes, Speed/Distance, Work). |
| **Data Structures & Python** | 10–15 | 25% | 90 seconds (MCQs), 15 mins (Coding) | Watch for Python mutable default arguments, integer slicing, and dictionary memory references. |
| **SQL & Relational Analytics** | 10–12 | 25% | 90 seconds (MCQs), 15 mins (Query) | Window functions (`DENSE_RANK()`, `LEAD`/`LAG`), `NULL` logic in outer joins, aggregation filtering via `HAVING`. |
| **Probability, Statistics & ML** | 15–20 | 25% | 60 seconds | High conceptual clarity needed on Bias-Variance, ROC vs PR-AUC, GBDT hyperparameters, and hypothesis test selection. |

---

## 3. High-Scoring Execution Strategy

1. **First-Pass Sweep (Minutes 0–40):**
   - Answer all direct conceptual MCQs across Probability, Statistics, and ML.
   - Answer standard SQL MCQs and quick aptitude questions.
   - Do NOT get bogged down by complex multi-paragraph case puzzles.
2. **Coding & Query Execution (Minutes 40–85):**
   - **SQL Live Query:** Write clean, sargable ANSI SQL using CTEs (`WITH` clauses). Verify corner cases: duplicate rows, `NULL` values, empty joins.
   - **Python Coding:** Ensure algorithmic complexity meets requirements ($\mathcal{O}(N)$ or $\mathcal{O}(N \log N)$). Handle boundary conditions ($N=0, N=1$, negative numbers).
3. **Second-Pass Review (Minutes 85–100):**
   - Tackle marked aptitude questions.
   - Verify that all questions have an answer (if no negative marking is enforced).
