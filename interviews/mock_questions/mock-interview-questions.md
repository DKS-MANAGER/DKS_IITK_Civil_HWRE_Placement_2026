# Mock Interview Guide

## Overview
Based on Civil_Placement_IITK Phase 2 (Oct 1–20) focus: mock interviews, viva-style grilling, design-code numericals, coding drills.

## Mock Interview Schedule

### Daily Routine
| Time | Activity | Duration |
|------|----------|----------|
| 6:00–6:30 PM | Coding problem | 30 min |
| 6:30–6:45 PM | Review + error log | 15 min |

### Every 3 Days
| Activity | Duration | Format |
|----------|----------|--------|
| Mock technical interview | 60 min | 2-panelist or 1-interviewer |
| Feedback review | 15 min | Peer/maintainer |

### Weekly
| Activity | Duration | Participants |
|----------|----------|-------------|
| Viva-style session | 90 min | Core subject oral exam |

## Technical Mock Interview Template

### Structure
1. **Introduction (5 min)**
   - Candidate self-introduction (2 min)
   - Panel introductions (1 min)
   - Overview of interview structure (2 min)

2. **Core Technical (30 min)**
   - 2-3 derivation questions
   - 2-3 numerical problems
   - 1 design/code question

3. **Coding/Python (15 min)**
   - 1-2 coding problems (Python/NumPy/pandas)
   - 1 SQL query problem

4. **HR/Q&A (10 min)**
   - Candidate questions
   - Wrap-up

### Grading Rubric
| Category | Excellent (4) | Good (3) | Needs Work (2) | Poor (1) |
|----------|--------------|----------|----------------|----------|
| **Technical Depth** | Complete with edge cases | Minor gaps | Significant gaps | Fundamental errors |
| **Communication** | Crystal clear | Mostly clear | Somewhat unclear | Unclear/confusing |
| **Problem Solving** | Innovative approach | Logical approach | Slow/trails off | Stuck/no progress |
| **Code Quality** | Clean, efficient | Good structure | Minor issues | Poor structure |

## Subject-Wise Question Banks

### Fluid Mechanics
```
1. Derive the energy equation including head loss terms.
   Expected: Bernoulli + head loss + practical applications

2. A pipe of diameter 300mm carries water at 2 m/s. Calculate Reynolds number.
   Given: ν = 1×10⁻⁶ m²/s, ρ = 1000 kg/m³
   Formula: Re = ρVD/μ = VD/ν

3. What are the limitations of Bernoulli's equation?
   Expected: Viscous effects, compressibility, unsteady flow, heat transfer

4. Explain the Moody diagram and its applications.
   Expected: Friction factor vs Re, relative roughness, flow regimes
```

### Geotechnical Engineering
```
5. Derive Terzaghi's bearing capacity equation for strip footing.
   Expected: Assumptions, failure mechanisms, bearing capacity factors

6. A clay sample has LL=60%, PL=25%. Calculate plasticity index and classify soil.
   Formula: PI = LL - PL
   A-line: PI = 0.73(LL - 20)

7. Explain the concept of effective stress and its importance.
   Expected: Total stress, pore water pressure, effective stress principle

8. What is the critical hydraulic gradient? When does piping occur?
   Formula: i_cr = (G-1)/(1+e)
```

### Structural Engineering
```
9. A simply supported beam (span = 6m) carries UDL of 20 kN/m. Find max moment.
   Formula: M_max = wL²/8

10. Explain the moment distribution method with a simple example.
    Expected: Stiffness factors, distribution factors, carry-over factors

11. Design a singly reinforced beam for given loads and materials.
    Expected: Trial width, effective depth, steel area, check for shear

12. What is the difference between working stress and limit state design?
    Expected: Philosophy, safety factors, serviceability
```

### Environmental Engineering
```
13. Design a rectangular sedimentation tank for a flow of 10 MLD.
    Given: Overflow velocity = 30 m/day, detention time = 2 hours

14. Explain the nitrogen cycle in wastewater treatment.
    Expected: Nitrification, denitrification pathways

15. What is SVI and how is it calculated?
    Formula: SVI = (V_observe × 1000) / X where X = MLSS concentration
```

### Transportation Engineering
```
16. A pavement is 1500mm thick with modular values...
    Expected: Equivalent single wheel load, thickness design

17. Explain the superelevation design procedure.
    Formula: e + f = V²/(127R)

18. What are the factors affecting stopping sight distance?
    Expected: Perception-reaction time, brake efficiency, road friction
```

## Coding Mock Interview Template

### Python Problems
```
1. Given a list of daily temperatures, return the number of days you have to wait 
   for a warmer day (stack problem).
   Example: [73, 74, 73, 74, 71, 75]
   Output: [1, 1, 3, 2, 1, 0]

2. Implement a function to check if a binary tree is balanced.

3. Given a pandas DataFrame with student scores, write code to:
   - Add a 'grade' column based on score ranges
   - Find students scoring above 90th percentile
   - Handle missing values
```

### SQL Problems
```
1. Write a query to find the second highest salary from an Employee table.

2. Given a table of orders with order_date and customer_id, 
   write a query to find customers who placed orders in consecutive months.

3. Write a query to calculate month-over-month growth rate.
```

### GATE/PSU Numerical Problems
```
Template for each problem:
1. Problem statement
2. Given data
3. Formula to apply
4. Step-by-step solution
5. Final answer with units
```

## Mock Interview Feedback Form

```
=== MOCK INTERVIEW FEEDBACK ===

Candidate: [Name] | Date: [DD/MM] | Interviewer: [Name]

TECHNICAL (30 min)
□ Derivations: [Score 1-4] Comments: _____________________
□ Numerical: [Score 1-4] Comments: _______________________
□ Design/Code: [Score 1-4] Comments: _____________________
□ GATE/PYQ: [Score 1-4] Comments: ________________________

CODING (15 min)
□ Problem 1: [Score 1-4] Comments: ______________________
□ Problem 2: [Score 1-4] Comments: ______________________
□ SQL: [Score 1-4] Comments: _____________________________

COMMUNICATION
□ Clarity: [Score 1-4] Comments: ________________________
□ Confidence: [Score 1-4] Comments: _____________________
□ Time management: [Score 1-4] Comments: ________________

FEEDBACK SUMMARY
Strengths:
1. _________________________________________________
2. _________________________________________________

Areas to Improve:
1. _________________________________________________
2. _________________________________________________
3. _________________________________________________

Next Steps:
□ Practice derivations → 5 problems due [date]
□ Review [topic] → notes due [date]
□ Schedule follow-up mock → [date]

Overall Score: ___/16
Recommendation: □ Pass □ Conditional Pass □ Retest
```

## Error Log Template

| Date | Topic | Problem Type | Mistake | Root Cause | Correction | Status |
|------|-------|-------------|---------|------------|------------|--------|
| [DD/MM] | Fluid Mechanics | Numerical | Unit conversion error | Rushed | Double-check units | ⬜ |
| [DD/MM] | Geotech | Conceptual | Forgot effective stress | Incomplete recall | Remember σ'=σ-u | ⬜ |

---

## Sources
- `F:\2k26Placement\Civil_Placement_IITK\README.md` (Milestone Rubric, Company Profiles, Roadmap)
