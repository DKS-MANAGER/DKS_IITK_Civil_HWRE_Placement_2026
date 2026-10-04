# 06. Product Management (APM): High-Yield Question Bank

> Categorized interview questions with model answers, technical solutions, and interviewer follow-up questions.

---

### Question 1: [P0][PRODUCT] Design an ATM experience specifically tailored for visually impaired users.

**Direct Answer / Solution Approach:**
```text
1. Comprehend: Goal is accessible, dignified, secure banking without third-party dependence. Constraints: Hardware costs and fraud security. 2. Persona: Visually impaired individual navigating urban branch. Core frictions: Physical keypad navigation, screen reflection, fear of PIN theft. 3. Solutions: (A) Tactile audio-guided interface with standard 3.5mm jack & haptic key feedback; (B) Mobile NFC pairing where transaction is configured on personal smartphone with screen reader, ATM only dispenses cash upon biometric touch. 4. Prioritization: Mobile NFC pairing (Lowest hardware retrofit cost, highest security). 5. North Star: Monthly Independent Transactions Completed.
```

**Interviewer Follow-Up & Deep Dive:**
> Interviewer follow-up: What is a key failure mode and guardrail metric? (Card/cash trap timeout; Guardrail: Transaction fraud dispute rate <0.001%).

---

### Question 2: [P0][METRICS] Define the North Star metric and 2 guardrails for YouTube Shorts.

**Direct Answer / Solution Approach:**
```text
North Star: Daily Active Watch Hours of Satisfied Consumption (Watch time on videos with positive engagement signals like like/share/comment). Guardrails: (1) Creator Churn / Burnout Rate, (2) User Clickbait Attrition Rate (Shorts skipped in <2 seconds).
```

**Interviewer Follow-Up & Deep Dive:**
> Interviewer follow-up: Why not simply use Total Video Views as the North Star? (Views incentivize short clickbait spam without true user satisfaction).


---

## Related Question Banks in Repository
- 📖 [HR & Behavioral Question Bank](../../02_interview-preparation/behavioral/hr-questions.md)
- 📖 [Guesstimates Master Guide](../../02_interview-preparation/guesstimates/guesstimate-guide.md)
