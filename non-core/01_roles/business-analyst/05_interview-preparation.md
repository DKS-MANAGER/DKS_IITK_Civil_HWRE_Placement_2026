# 05. Business Analyst: Interview Preparation & Evaluation

> Comprehensive guide to mastering the multi-stage Business Analyst recruitment process, technical round formats, and evaluation criteria.

---

## 1. Interview Rounds Deconstruction

### Round 1: Online Assessment (OA)
- **Structure**: 60–90 minutes. 30 Quant/DI MCQs + 3–5 SQL coding problems.
- **Strategy**: Solve SQL questions first (high point weight). On DI tables, calculate approximations to save speed math time.

### Round 2: Technical SQL & Live Querying
- **Structure**: 45 minutes live shared coderpad (e.g., HackerRank / CoderByte).
- **Core Expectations**:
  - Always clarify table schema, NULL handling, and primary/foreign keys before typing.
  - Think out loud: *"I will first filter active users with a CTE, then join with orders table..."*
  - Optimize: Explain index utilization, avoid unnecessary subqueries if CTE is clearer.

### Round 3: Business Problem Solving & Analytical Case
- **Structure**: 45–60 minutes interactive business scenario with the interviewer.
- **Core Expectations**:
  - Clarify the objective: *"Is our goal to maximize immediate revenue or preserve long-term retention?"*
  - Build a MECE tree on paper before sharing hypotheses.
  - Ask targeted questions to request supplementary data points.

### Round 4: Behavioral & Fit Interview
- **Structure**: 30–45 minutes with a Senior Manager or Director.
- **Core Themes**: Cross-functional stakeholder influence, resolving disagreement with engineering/marketing, handling incomplete data under tight deadlines.

---

## 2. Live Interview Tips for BA Candidates
1. **Never jump directly into solutions**: Always validate the metric definition and problem boundary first.
2. **State hypotheses explicitly**: *"My hypothesis is that the checkout drop-off is concentrated on Android users following the recent app version update."*
3. **Quantify impact**: Conclude case discussions with clear, prioritized business actions and expected ROI.
