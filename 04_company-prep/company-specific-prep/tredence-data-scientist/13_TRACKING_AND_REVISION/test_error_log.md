# Test Error Log & Root-Cause Analysis Framework

**Target Role:** Data Scientist / Associate Data Scientist | Tredence Analytics  
**Context:** IIT Kanpur Placement Season 2026–27  
**Purpose:** Systematically log, categorize, and remediate errors from practice assessments and mock interviews.

---

## 1. Error Taxonomy

Every error must be tagged with one of the following root causes:
1. **Conceptual Flaw (CF):** Fundamental misunderstanding of the theory, theorem, or mathematical mechanism (e.g., confusing ROC-AUC with PR-AUC under imbalance).
2. **Algorithmic / Implementation Gap (AG):** Understood the high-level concept but failed to write efficient code or query syntax (e.g., using `HAVING` instead of `WHERE`, off-by-one window frame).
3. **Calculation / Arithmetic Slip (CS):** Correct formula applied but simple calculation or sign error made under time pressure.
4. **Misreading / Comprehension Trap (MT):** Failed to notice negative phrasing (e.g., *"Which of the following is NOT true?"*) or edge-case constraints.
5. **Time Management Failure (TM):** Spent excessive time on a low-yield puzzle, running out of time for easy high-weightage questions.

---

## 2. Active Test Error Log Template

| Date | Test / Source | Q# | Topic | Error Description | Root Cause Tag | Correct Solution & Mathematical Rule | Action Taken / Prevention Rule |
|---|---|:---:|---|---|:---:|---|---|
| *Sample* | *Diag Test 1* | *Q15* | *SQL Nulls* | *Thought `NULL = NULL` evaluates to `TRUE`.* | *CF* | *In ANSI three-valued logic, comparison against `NULL` evaluates to `UNKNOWN`.* | *Added rule: Always use `IS NULL` or `COALESCE`.* |
| *Sample* | *Mock Test 1* | *Q1* | *Pipes & Cistern* | *Forgot that Pipe C empties, accidentally added its rate instead of subtracting.* | *MT / CS* | *Net rate $= 1/12 + 1/18 - 1/24 = 7/72 \implies 10.28\text{ hrs}$.* | *Read inlet vs outlet tags twice before writing equations.* |
| *Sample* | *Mock Test 1* | *Q38* | *CUPED* | *Calculated remaining variance factor instead of eliminated variance.* | *MT* | *Eliminated variance is $\rho^2 = 0.64 = 64\%$. Remaining is $1 - \rho^2 = 36\%$.* | *Highlight bold action verbs in probability/stats prompts.* |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

---

## 3. Weekly Remediation Protocol

1. **Review cycle:** Review the error log every Sunday evening.
2. **Re-test rule:** Any question logged under **Conceptual Flaw (CF)** must be solved independently 3 days later without referencing notes.
3. **Pattern identification:** If $> 3$ errors fall in the same domain (e.g., SQL Window Frames or Probability Distributions), immediately dedicate a 2-hour sprint to that specific module.
