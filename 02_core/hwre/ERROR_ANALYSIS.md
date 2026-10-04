# HWRE — Error Analysis

> Systematic error tracking + reattempt system. Log every mistake from practice problems and mock tests, then reattempt until clean.

## How to Use

1. After every practice session or mock test, log each error below.
2. Classify the error type (see categories).
3. Reattempt the problem after 24 hours.
4. Mark `✅ Clean` only when you solve it correctly without hints.

## Error Categories

| Code | Category | Description |
|:----:|----------|-------------|
| **C1** | Concept gap | Didn't know the concept/formula |
| **C2** | Formula error | Wrong formula or misapplied |
| **C3** | Unit error | Unit conversion mistake |
| **C4** | Sign/direction | Wrong sign, direction, or orientation |
| **C5** | Calculation | Arithmetic error |
| **C6** | Trap | Fell for a common GATE/interview trap |
| **C7** | Reading | Misread the question |
| **C8** | Time | Ran out of time / poor time allocation |

## Error Log

| Date | Problem/Question | Topic | Error Type | Root Cause | Fix | Reattempt | Status |
|------|------------------|-------|:----------:|------------|-----|-----------|:------:|
| | | | | | | | |

## Reattempt Protocol

```
1. Wait 24 hours after logging the error.
2. Cover the solution. Solve from scratch.
3. If correct → mark ✅ Clean.
4. If wrong → re-log with the same error code, review the concept, retry in 48 hours.
5. After 3 failed attempts → escalate to a study session on that topic.
```

## High-Frequency Error Patterns (HWRE)

| Pattern | Why It Happens | Prevention |
|---------|----------------|------------|
| Rational method unit error | A in km² vs ha, i in mm/hr | Use `Q = CiA/360` (A in ha, i in mm/hr); `/3.6` for km² |
| Muskingum coefficient sum | Forgot `C₀ + C₁ + C₂ = 1` | Always check sum after computing |
| Theis vs Cooper-Jacob | Applied CJ when u > 0.01 | Check `u = r²S/(4Tt)` first |
| GVF profile misclassification | Confused M1/M2/M3 | Draw y_n and y_c lines first |
| Hydraulic jump depth | Used wrong conjugate formula | `y₂/y₁ = 0.5(√(1+8Fr₁²) − 1)` |
| BOD₅ vs ultimate BOD | Mixed up L₀ and BOD₅ | `BOD₅ = L₀(1 − e^(−5k))` |
| Specific energy minimum | Forgot `E_min = 1.5y_c` | At critical depth, E = 1.5y_c |
| Darcy velocity vs seepage | Used Darcy velocity for travel time | Seepage velocity = K·i/n |
| Manning n units | Mixed SI and imperial | SI: `V = (1/n)R^(2/3)S^(1/2)` |
| SCS-CN S units | S in mm vs inches | `S = 25400/CN − 254` (mm) |

## Weekly Review

- [ ] Week 1: Review all C1 (concept) errors — re-study those topics
- [ ] Week 2: Review all C2 (formula) errors — re-memorize formulas
- [ ] Week 3: Review all C3 (unit) errors — practice unit conversions
- [ ] Week 4: Review all C6 (trap) errors — re-read [`TRAPS.md`](TRAPS.md)

## Related

- [MASTER_INDEX.md](MASTER_INDEX.md) · [TRAPS.md](TRAPS.md) · [practice/hwre-practice.md](practice/hwre-practice.md) · [mocks/hwre-mock-1.md](mocks/hwre-mock-1.md)