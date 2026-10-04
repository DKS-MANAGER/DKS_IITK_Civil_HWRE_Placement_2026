# 06. Business Operations (BizOps): High-Yield Question Bank

> Categorized interview questions with model answers, technical solutions, and interviewer follow-up questions.

---

### Question 1: [P0][BIZOPS] A quick-commerce dark store's order picking time increased from 110 seconds to 210 seconds. Walk through your diagnosis.

**Direct Answer / Solution Approach:**
```text
1. Deconstruct Picking Time: Order Generation -> Picker Assignment -> Item Locating (Walking) -> Scanning/Bagging -> Handoff to Rider. 2. Segment by: SKU Category (Fresh produce vs FMCG), Time of Day (Peak hours vs normal), Picker Tenure (New vs Experienced). 3. Identify Root Cause: Popular SKUs stored in rear warehouse aisles causing excessive walking distances + barcode scanning hardware lag. 4. Operational Fix: Re-slot top 20% high-velocity SKUs near packing stations; upgrade barcode scanner firmware. Expected result: Reduce picking time back to <95 seconds.
```

**Interviewer Follow-Up & Deep Dive:**
> Interviewer follow-up: How do you balance dark store inventory capacity against walking aisle speed?


---

## Related Question Banks in Repository
- 📖 [HR & Behavioral Question Bank](../../02_interview-preparation/behavioral/hr-questions.md)
- 📖 [Guesstimates Master Guide](../../02_interview-preparation/guesstimates/guesstimate-guide.md)
