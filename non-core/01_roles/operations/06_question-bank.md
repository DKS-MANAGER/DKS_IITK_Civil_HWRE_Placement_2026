# 06. Operations Management: High-Yield Question Bank

> Categorized interview questions with model answers, technical solutions, and interviewer follow-up questions.

---

### Question 1: [P0][OPS] A manufacturing line has 4 sequential workstations with cycle times: 4 min, 7 min, 5 min, 3 min. Calculate maximum throughput and WIP under Little's Law.

**Direct Answer / Solution Approach:**
```text
1. Bottleneck = Station 2 (Cycle Time = 7 min). 2. Maximum Throughput $\lambda = rac{60	ext{ min}}{7	ext{ min}} pprox 8.57$ units/hour. 3. Total Lead Time $W = 4 + 7 + 5 + 3 = 19$ minutes. 4. Work in Progress $L = \lambda 	imes W = rac{1}{7} 	imes 19 pprox 2.71$ units in queue/processing.
```

**Interviewer Follow-Up & Deep Dive:**
> Interviewer follow-up: If you invest 50 Lakh INR to reduce Station 2 cycle time to 4 min, what is the new bottleneck and new throughput? (Station 3 becomes bottleneck with 5 min -> Throughput = 12 units/hour).


---

## Related Question Banks in Repository
- 📖 [HR & Behavioral Question Bank](../../02_interview-preparation/behavioral/hr-questions.md)
- 📖 [Guesstimates Master Guide](../../02_interview-preparation/guesstimates/guesstimate-guide.md)
