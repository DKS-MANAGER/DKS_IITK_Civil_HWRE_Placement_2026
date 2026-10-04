# 06. Technology & Systems Consulting: High-Yield Question Bank

> Categorized interview questions with model answers, technical solutions, and interviewer follow-up questions.

---

### Question 1: [P0][SYSTEM] Explain the CAP Theorem and how to choose between Consistency and Availability for a financial transaction system vs a social media feed.

**Direct Answer / Solution Approach:**
```text
CAP Theorem states a distributed system can guarantee at most 2 of Consistency, Availability, and Partition Tolerance. In network partitions: Financial systems choose CP (Consistency + Partition Tolerance) - reject transactions if exact account balance cannot be confirmed. Social media feeds choose AP (Availability + Partition Tolerance) - serve slightly stale posts to keep app online.
```

**Interviewer Follow-Up & Deep Dive:**
> Interviewer follow-up: How does eventual consistency work in AP distributed databases like Cassandra?


---

## Related Question Banks in Repository
- 📖 [HR & Behavioral Question Bank](../../02_interview-preparation/behavioral/hr-questions.md)
- 📖 [Guesstimates Master Guide](../../02_interview-preparation/guesstimates/guesstimate-guide.md)
