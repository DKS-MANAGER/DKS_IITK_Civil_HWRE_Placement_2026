# Puzzles & Scheduling

> **Priority:** P0 · **Role relevance:** Critical (Universal across Management Consulting, Product Management, Quantitative Trading, Analytics, Core Engineering & Banking)  
> **Difficulty range:** Foundation → Extreme Caselets & Hybrid Reasoning · **Target speed:** 45–60 sec (Linear 1D) – 120–180 sec (Multi-Variable Grid / Caselet)

---

## 1. Mathematical & Theoretical Framework

### 1.1 Constraint Satisfaction Problem (CSP) Formulation
Every logical scheduling or floor puzzle can be rigorously modeled as a formal Constraint Satisfaction Problem:
$$\mathcal{P} = \langle X, D, C \rangle$$
- **Variables** $X = \{x_1, x_2, \dots, x_n\}$: The entities or time/space slots (e.g., Days $\{\text{Mon}, \dots, \text{Sun}\}$, Floors $\{1, \dots, 8\}$, Persons $\{A, \dots, H\}$).
- **Domains** $D = \{D_1, D_2, \dots, D_n\}$: The finite set of allowable values each variable can assume (e.g., $D_i = \{1, 2, \dots, k\}$).
- **Constraints** $C = \{c_1, c_2, \dots, c_m\}$: Restrictions on allowable value combinations:
  - **Unary constraints**: Restrict domain of a single variable, e.g., $A \ne \text{Monday}$, $\text{Floor}(B) \in \{2, 4, 6, 8\}$.
  - **Binary constraints**: Relate two variables, e.g., $|\text{Floor}(A) - \text{Floor}(B)| = 3$, $\text{Day}(C) = \text{Day}(D) + 2$.
  - **Higher-order ($k$-ary) constraints**: Involve groups of variables, e.g., $\text{AllDifferent}(x_1, \dots, x_n)$, $\sum_{i} \text{Hours}(T_i) \le 40$.

```
+-----------------------------------------------------------------------------------+
|                            CSP CONSTRAINT TAXONOMY                                |
+-----------------------------------------------------------------------------------+
|  Type         | Mathematical Translation        | Deductive Action                |
|---------------+---------------------------------+---------------------------------|
| Unary Anchor  | x_i = v                         | Fix slot immediately            |
| Domain Cut    | x_i != v                        | Cross off cell in matrix        |
| Relative Gap  | pos(A) - pos(B) = k + 1         | Create rigid polyomino block    |
| Parity/Floor  | pos(A) = 2k (Even)              | Prune 50% of candidate rows     |
| Implication   | P -> Q  ===  ~P or Q            | If P holds, force Q; else pass  |
| Contrapositive| ~Q -> ~P                        | Absence of Q eliminates P       |
| Exclusivity   | A xor B                         | Exactly one true; never both    |
+-----------------------------------------------------------------------------------+
```

---

### 1.2 Cross-Grid Matrix Architecture (Multi-Dimensional Tabulation)

When a puzzle links 3 or more orthogonal categories (e.g., **Person $\times$ Day $\times$ Department $\times$ City**), unstructured notes lead to cognitive overload. Use a multi-entry cross-matrix table:

```
                  DAYS (Mon-Fri)                 DEPARTMENTS
            Mon  Tue  Wed  Thu  Fri        HR   Fin  Mkt  Ops  R&D
    +-----+----+----+----+----+----+     +----+----+----+----+----+
  A |  P1 |  X |  X |  X |  V |  X |   A |  V |  X |  X |  X |  X |
  E |  P2 |    |    |    |    |    |   E |    |    |    |    |    |
  R |  P3 |    |    |    |    |    |   R |    |    |    |    |    |
  S |  P4 |    |    |    |    |    |   S |    |    |    |    |    |
  O |  P5 |    |    |    |    |    |   O |    |    |    |    |    |
  N +-----+----+----+----+----+----+     +----+----+----+----+----+
```

#### The Universal Elimination Invariants:
1. **One-to-One Bipartite Matching**: If each person has exactly one unique department, placing a checkmark `[V]` at `(Person A, HR)` immediately forces an `[X]` in:
   - All other department columns for Person A (row elimination).
   - All other person rows for HR (column elimination).
2. **Transit Equivalence**: If `Person A = Thursday` and `Person A = HR`, then `Thursday = HR` is permanently established in the Day-Department intersection subgrid.

---

### 1.3 Branching & Case-Splitting Trees (The 2-Branch Pruning Principle)

When no direct deterministic deduction remains, identify the **Pivot Variable** with minimum domain cardinality ($|D_{\text{pivot}}| = 2$). Never bifurcate into $\ge 3$ branches if a 2-branch anchor exists.

```
                         [ ROOT PUZZLE STATE ]
                                   |
                  +----------------+----------------+
                  |                                 |
           [ Case 1: A on Floor 3 ]          [ Case 2: A on Floor 7 ]
                  |                                 |
         Propagate Clues                   Propagate Clues
                  |                                 |
       Contradiction Reached!               All Constraints Met!
      (e.g., B & C clash at F5)             Unique Solution Found!
           ==> PRUNE CASE 1                   ==> ACCEPT CASE 2
```

---

### 1.4 Logical Implication & Conditional Traps

| Natural Language Phrasing | Formal Propositional Logic | Deduction Trap to Avoid |
|:---|:---|:---|
| *"If A attends on Tuesday, then B attends on Friday"* | $A_{\text{Tue}} \implies B_{\text{Fri}}$ | **Trap:** Assuming that if A is *not* on Tuesday, B cannot be on Friday! (Inverse fallacy). If B is NOT on Friday, then A CANNOT be on Tuesday (Contrapositive: $\neg B_{\text{Fri}} \implies \neg A_{\text{Tue}}$). |
| *"Either A or B attends on Monday, but not both"* | $A_{\text{Mon}} \oplus B_{\text{Mon}}$ (XOR) | If $A$ is placed on Monday, $B$ is strictly forbidden from Monday. |
| *"C lives 3 floors away from D"* | $|\text{Floor}(C) - \text{Floor}(D)| = 3$ | **Trap:** Does NOT mean 3 floors *between* them! 3 floors away means $|F_C - F_D| = 3$ (which corresponds to exactly 2 floors between them). |
| *"Exactly 3 people live between C and D"* | $|\text{Floor}(C) - \text{Floor}(D)| = 3 + 1 = 4$ | The absolute difference in indices is $k + 1 = 4$. |
| *"E lives immediately above the floor of F"* | $\text{Floor}(E) = \text{Floor}(F) + 1$ | Rigid adjacent polyomino $[F, E]^T$. |
| *"At least two people sit between X and Y"* | $|\text{pos}(X) - \text{pos}(Y)| - 1 \ge 2 \iff |\text{pos}(X) - \text{pos}(Y)| \ge 3$ | Check both upper and lower boundaries. |

---

## 2. Comprehensive Practice Set (40 Fully Solved Questions)

```
===================================================================================
                               8-LEVEL DIFFICULTY ROADMAP
===================================================================================
Level 1: Foundation (Q1–Q5)              -> 1D Fixed Anchors, Basic Floor & Day Sequences
Level 2: Intermediate (Q6–Q10)           -> 5-7 Variables, 2 Orthogonal Attributes
Level 3: Hard (Q11–Q15)                  -> 7-8 Variables, Interval & Polyomino Constraints
Level 4: Very Hard (Q16–Q20)             -> 4-Variable Cross-Matrices, Vacant Floors
Level 5: Expert (Q21–Q25)                -> Conditional Rules, Contrapositives, Negation
Level 6: Placement Traps (Q26–Q30)       -> Boundary Extremes, Impossible States, Parity
Level 7: Extreme Caselets (Q31–Q37)      -> Caselet 1 (10-Person, 5-Day, 3-Team, 3-Loc)
                                           Caselet 2 (8-Floor Double-Flat Multi-Car)
Level 8: Advanced Hybrid (Q38–Q40)       -> Puzzle + Seating / Direction / Blood Relations
===================================================================================
```

---

### Level 1: Foundation (Q1–Q5)

#### Q1. Basic Floor Sequence
Seven persons $A, B, C, D, E, F, G$ live on floors 1 to 7 of a building (Floor 1 is bottom, Floor 7 is top). $E$ lives on an odd-numbered floor above Floor 4. Only two persons live between $E$ and $B$. $A$ lives immediately above $B$. $F$ lives on Floor 1. $G$ lives on an even-numbered floor. Who lives on Floor 4?  
A) $A$  
B) $B$  
C) $C$  
D) $G$

#### Q2. Day Scheduling Anchor
Six professionals $P, Q, R, S, T, U$ conduct workshops from Monday to Saturday, one per day. $R$ conducts on Wednesday. Exactly one person conducts between $R$ and $T$. $P$ conducts immediately before $S$. $Q$ does not conduct on Saturday. Who conducts on Saturday?  
A) $P$  
B) $S$  
C) $T$  
D) $U$

#### Q3. Stack Ordering
Seven boxes labeled $J, K, L, M, N, O, P$ are stacked vertically from bottom (Position 1) to top (Position 7). Box $M$ is at Position 4. Box $K$ is immediately above $M$. Exactly three boxes are placed between $J$ and $K$. Box $P$ is placed immediately above $J$. Box $L$ is placed below $O$. Which box is at Position 2?  
A) $J$  
B) $L$  
C) $P$  
D) $O$

#### Q4. Simple Linear Grouping
Five students $V, W, X, Y, Z$ each study a different major: Physics, Chemistry, Biology, Mathematics, and History. $X$ studies Biology. The student studying Physics is immediately between $V$ and $Y$. $Z$ does not study Physics or Mathematics. $V$ studies History. What does $Y$ study?  
A) Chemistry  
B) Mathematics  
C) Physics  
D) Biology

#### Q5. Simple Floor Bound
Six executives $U, V, W, X, Y, Z$ occupy single-occupancy suites on floors 1 to 6. $Z$ lives on Floor 2. $W$ lives on a floor above $Z$ but below $X$. Exactly two people live between $U$ and $Z$. $Y$ lives on the top floor. Which floor does $V$ occupy?  
A) Floor 1  
B) Floor 3  
C) Floor 4  
D) Floor 5

---

### Level 2: Intermediate Multi-Variable Grids (Q6–Q10)

#### Q6. Person x Day x Subject
Five professors $A, B, C, D, E$ lecture from Monday to Friday, one per day, each teaching a different subject: AI, Robotics, Cyber, Cloud, and Data. $C$ lectures on Wednesday but does not teach AI or Cyber. $A$ lectures on the day immediately preceding the Robotics lecture. The Cyber lecture is on Friday. $E$ teaches Cloud on Tuesday. Who lectures on Monday and what subject do they teach?  
A) $A$, Data  
B) $A$, AI  
C) $D$, AI  
D) $B$, Robotics

#### Q7. Person x Department x Floor
Six employees $K, L, M, N, O, P$ work in six departments: HR, Tech, Sales, Audit, Legal, and Ops, on floors 1 to 6. $N$ works in Legal on Floor 3. The person in Tech lives on an even-numbered floor above $N$. $M$ works in Audit on Floor 1. $P$ works in HR. Only one person lives between $P$ and $M$. $K$ lives on Floor 6. Which department does the person on Floor 2 belong to?  
A) HR  
B) Sales  
C) Ops  
D) Tech

#### Q8. Box Stack x Colour
Six boxes $A, B, C, D, E, F$ are stacked 1 (bottom) to 6 (top), each painted a distinct colour: Red, Blue, Green, Yellow, Black, White. The White box is at Position 5. Box $B$ is Blue and is immediately above the Red box. Box $A$ is at Position 1. Box $C$ is neither Red nor White, and is placed two positions below the Yellow box. Box $D$ is Green. Which box is painted White?  
A) $C$  
B) $D$  
C) $E$  
D) $F$

#### Q9. Person x City x Month
Five engineers $P, Q, R, S, T$ visit five cities: Tokyo, London, Paris, Berlin, New York, in five distinct consecutive months from March to July. $R$ visits Paris in May. $P$ visits Berlin in the month immediately after $T$'s visit. $T$ does not visit London. The engineer visiting Tokyo goes in March. $S$ visits New York. In which month does $Q$ travel, and which city does $Q$ visit?  
A) March, Tokyo  
B) April, London  
C) July, London  
D) June, Berlin

#### Q10. Shift Scheduling with Roles
Six doctors $D_1, D_2, D_3, D_4, D_5, D_6$ take emergency duties on six consecutive nights (Night 1 to Night 6) across three specializations: Cardio, Neuro, Ortho (exactly two doctors per specialty). $D_1$ is a Neuro specialist and takes duty on Night 2. $D_4$ takes duty on Night 5. Both Cardio specialists take duties on consecutive nights. $D_3$ is an Ortho specialist and takes duty on Night 6. $D_2$ takes duty immediately before $D_4$. If $D_5$ is a Cardio specialist, what is the specialty of $D_6$?  
A) Cardio  
B) Neuro  
C) Ortho  
D) Cannot be determined

---

### Level 3: Hard Multi-Constraint Systems (Q11–Q15)

#### Q11. Eight-Floor Polyomino Interval
Eight executives $A, B, C, D, E, F, G, H$ live on floors 1 to 8. $B$ lives on Floor 4. Exactly three persons live between $B$ and $G$. $A$ lives on an odd-numbered floor immediately above $C$. There are as many floors between $D$ and $E$ as between $E$ and $H$. $D$ lives on Floor 8. $F$ lives on an even-numbered floor below $B$. Who lives on Floor 5?  
A) $C$  
B) $E$  
C) $G$  
D) $H$

#### Q12. Day x Time Slot Scheduling
Seven candidates $J, K, L, M, N, O, P$ are interviewed across Monday to Sunday, one per day. $M$ is interviewed on Thursday. There are more than three days between $J$ and $M$. Exactly two persons are interviewed between $J$ and $O$. $K$ is interviewed immediately after $N$. $P$ is interviewed on one of the days before $L$ but after $K$. On which day is $N$ interviewed?  
A) Tuesday  
B) Wednesday  
C) Friday  
D) Saturday

#### Q13. Nine-Box Stack with Parity Gaps
Nine boxes $1$ through $9$ are placed in a stack from bottom (Position 1) to top (Position 9). Box $F$ is at an even position below Position 6. Exactly three boxes are between $F$ and $B$. Box $A$ is immediately above $B$. Exactly two boxes are between $A$ and $C$. Box $D$ is placed at the topmost position. Box $E$ is immediately below $C$. Box $G$ is placed above $H$ but below $I$. If $F$ is at Position 2, what is the position of Box $C$?  
A) Position 4  
B) Position 5  
C) Position 7  
D) Position 8

#### Q14. Seven Persons x Seven Companies x Seven Package Tiers
Seven graduates $P, Q, R, S, T, U, V$ joined seven companies: Google, Microsoft, Apple, Amazon, Meta, Netflix, Uber, with distinct package ranks 1 (highest) to 7 (lowest). $R$ joined Apple and has package rank 3. $T$ has a higher package than $U$ but lower than $P$. The graduate joining Meta has rank 1. $V$ joined Netflix and has rank 7. $S$ joined Microsoft. The graduate joining Google has package rank 2. If $P$ did not join Meta, which company did $P$ join?  
A) Google  
B) Amazon  
C) Uber  
D) Microsoft

#### Q15. Circular Scheduling with Day Inversion
Seven committee members $A, B, C, D, E, F, G$ chair meetings on days Monday through Sunday. No two members chair on the same day. $A$ chairs three days after $D$. $F$ chairs immediately before $B$. $C$ chairs on Sunday. $E$ chairs on a day between $A$ and $G$. Exactly one member chairs between $B$ and $C$. Who chairs the meeting on Wednesday?  
A) $A$  
B) $D$  
C) $E$  
D) $F$

---

### Level 4: Very Hard 4-Variable Cross Matrices (Q16–Q20)

#### Q16. Person x Floor x City x Department
Seven professionals $P, Q, R, S, T, U, V$ reside on floors 1 to 7, each hailing from a different city (Delhi, Mumbai, Kolkata, Chennai, Bangalore, Pune, Hyderabad) and working in a different domain (IT, Finance, HR, Marketing, Operations, Legal, R&D).
- The person from Mumbai lives on Floor 5 and works in HR.
- $T$ lives immediately above $Q$. $Q$ is from Kolkata.
- $R$ works in Finance and lives on Floor 1.
- Exactly three floors exist between $R$ and the person working in IT.
- The person working in IT is from Delhi.
- $S$ works in Legal and lives on an even-numbered floor.
- $U$ is from Pune and lives on Floor 7.
- The person from Bangalore works in R&D and lives on Floor 6.
- $P$ does not live on an odd floor.
Which city is $P$ from, and what floor does $P$ occupy?  
A) Delhi, Floor 4  
B) Bangalore, Floor 6  
C) Chennai, Floor 2  
D) Pune, Floor 7

#### Q17. Eight Floors with Vacant Floor
An eight-story apartment building has floors numbered 1 to 8 (Floor 1 is bottom, Floor 8 is top). Seven people $A, B, C, D, E, F, G$ occupy seven floors, and exactly one floor is **VACANT**.
- The vacant floor is an even-numbered floor above Floor 3.
- $C$ lives immediately above the vacant floor.
- Exactly three floors lie between $A$ and $C$.
- $B$ lives on Floor 1.
- $D$ lives on a floor immediately below $E$.
- Neither $D$ nor $E$ lives on an odd-numbered floor adjacent to the vacant floor.
- Exactly two people live between $F$ and $G$. $G$ lives above $F$.
Which floor is vacant?  
A) Floor 4  
B) Floor 6  
C) Floor 8  
D) Floor 2

#### Q18. Double-Shift Scheduling x Venue x Topic
Six trainers $T_1, T_2, T_3, T_4, T_5, T_6$ deliver sessions across three days (Monday, Tuesday, Wednesday) with two sessions per day: Morning (9 AM) and Afternoon (2 PM). Each session is in a different room ($R_1$ to $R_6$) on distinct topics ($M_1$ to $M_6$).
- $T_3$ conducts on Tuesday morning in $R_2$.
- $T_1$ conducts immediately after $T_4$ (i.e. $T_4$ in morning, $T_1$ in afternoon of the same day).
- $T_5$ conducts on Wednesday afternoon.
- Topic $M_4$ is presented on Monday afternoon in $R_5$.
- $T_6$ presents topic $M_2$ on Monday morning.
- Topic $M_1$ is presented in $R_1$ immediately preceding the session in $R_6$.
Which trainer conducts on Tuesday afternoon?  
A) $T_1$  
B) $T_2$  
C) $T_4$  
D) $T_5$

#### Q19. Eight Persons x 8 Floors x 8 Cars
Eight persons $A, B, C, D, E, F, G, H$ live on floors 1 to 8, each owning a distinct car (Audi, BMW, Honda, Tesla, Ford, Kia, Hyundai, Skoda).
- $A$ owns a Tesla and lives on an odd floor below Floor 5.
- Exactly two persons live between $A$ and the one who owns a BMW.
- The person who owns a BMW lives immediately below $F$.
- Only one person lives between $F$ and $H$.
- $H$ owns a Ford.
- $D$ lives on Floor 8 and owns a Skoda.
- Three persons live between $D$ and $B$.
- The person owning an Audi lives on Floor 2.
- $G$ owns a Hyundai and lives on an odd floor.
Which car does $B$ own, and which floor does $B$ live on?  
A) BMW, Floor 4  
B) Honda, Floor 4  
C) Kia, Floor 4  
D) Audi, Floor 2

#### Q20. 7 Persons x 7 Days x 7 Flight Destinations
Seven delegates $M, N, O, P, Q, R, S$ depart for seven international summits (Dubai, Singapore, London, New York, Paris, Tokyo, Zurich) from Monday through Sunday.
- $P$ departs on Friday to Paris.
- $Q$ departs two days before $P$.
- The delegate traveling to Dubai departs on Sunday.
- Exactly three delegates depart between the one going to London and the one going to New York.
- The one going to London departs before the one going to New York.
- $M$ departs on Tuesday but not to London.
- $S$ departs immediately after $R$.
- Neither $R$ nor $S$ travels to Dubai or London.
Which day does $N$ depart, and to which city?  
A) Sunday, Dubai  
B) Thursday, Singapore  
C) Monday, London  
D) Tuesday, Tokyo

---

### Level 5: Expert Conditional & Directional Clues (Q21–Q25)

#### Q21. Multi-Condition Implication Chain
Seven analysts $A, B, C, D, E, F, G$ are assigned project presentations across days Monday through Sunday.
- Rule 1: If $A$ presents on Tuesday, then $E$ must present on Friday.
- Rule 2: If $E$ presents on Friday, then $C$ cannot present on Saturday.
- Rule 3: $D$ presents exactly two days after $B$.
- Rule 4: $F$ presents on Sunday.
- Rule 5: Either $G$ presents on Monday or $G$ presents on Wednesday.
- Fact: $A$ presents on Tuesday.
Which day does $B$ present?  
A) Wednesday  
B) Thursday  
C) Friday  
D) Monday

#### Q22. Contrapositive & Mutual Exclusion Scheduling
Six researchers $U, V, W, X, Y, Z$ schedule laboratory access from Monday to Saturday.
- Condition 1: If $U$ uses the lab before Wednesday, then $X$ must use the lab on Saturday.
- Condition 2: If $X$ uses the lab on Saturday, then $Y$ must use the lab immediately after $W$.
- Condition 3: $Z$ is scheduled for Thursday.
- Condition 4: $Y$ uses the lab on Tuesday.
Who must be scheduled on Saturday?  
A) $X$  
B) $V$  
C) $W$  
D) Cannot be determined

#### Q23. Nine-Box Dual Parity & Negative Bounds
Nine boxes $A, B, C, D, E, F, G, H, I$ are stacked 1 to 9 (bottom to top).
- Box $E$ is at Position 5.
- Box $A$ is at an odd position above $E$.
- Exactly three boxes are between $A$ and $B$.
- Box $C$ is immediately above $B$.
- The number of boxes above $C$ equals the number of boxes below $D$.
- Box $F$ is at an even position below $E$.
- Exactly one box is between $F$ and $G$.
- Box $H$ is placed above $I$. Box $H$ is not adjacent to $E$.
Which box is at Position 1?  
A) $B$  
B) $D$  
C) $I$  
D) $G$

#### Q24. Either-Or Branching with Strict Contradiction Pruning
Eight students $K_1, \dots, K_8$ sit for viva exams across Monday to Thursday, two students per day (Slot 1: Morning, Slot 2: Afternoon).
- $K_1$ and $K_5$ take vivas on the same day.
- $K_3$ takes viva on Tuesday morning.
- Either $K_2$ or $K_7$ takes viva on Thursday afternoon.
- $K_6$ takes viva immediately after $K_8$ on the same day.
- $K_4$ takes viva on Wednesday afternoon.
- $K_1$ takes viva on a day before $K_4$.
When does $K_7$ take the viva?  
A) Monday morning  
B) Tuesday afternoon  
C) Thursday morning  
D) Thursday afternoon

#### Q25. Floor Puzzle with Variable Distance & Score Ties
Six candidates $P, Q, R, S, T, U$ live on floors 1 to 6. Each scored different marks in an exam: 45, 55, 65, 75, 85, 95.
- The person on Floor 4 scored 75.
- $Q$ lives on an odd floor and scored higher than the person on Floor 6.
- The difference in marks between the person on Floor 2 and Floor 5 is 30.
- $P$ lives on Floor 1 and scored 45.
- $T$ lives immediately above $S$.
- $R$ scored 85.
- The person on Floor 3 scored 65.
What is the score of the person living on Floor 6?  
A) 55  
B) 65  
C) 85  
D) 95

---

### Level 6: Placement Traps & Boundary Inference (Q26–Q30)

#### Q26. The Parity Contradiction Trap
Seven friends $A, B, C, D, E, F, G$ live on floors 1 to 7.
- $A$ lives on an even floor.
- Exactly two people live between $A$ and $B$.
- Exactly two people live between $B$ and $C$.
- $D$ lives immediately above $E$.
- $F$ lives on Floor 7.
If $C$ lives on an odd floor, which floor must $A$ live on?  
A) Floor 2  
B) Floor 4  
C) Floor 6  
D) No valid arrangement exists (Contradiction)

#### Q27. Minimum & Maximum Possible Vacant Floors
A building has 10 floors (1 to 10). Six executives $A, B, C, D, E, F$ reside on six distinct floors, leaving four floors vacant.
- No two vacant floors are consecutive.
- Neither Floor 1 nor Floor 10 is vacant.
- $A$ lives on Floor 3.
- $F$ lives on Floor 8.
- Exactly two floors exist between $A$ and $B$, one of which is vacant.
What is the maximum floor number that can be occupied by $C$ if $C$ lives below $A$?  
A) Floor 1  
B) Floor 2  
C) Floor 3  
D) Cannot be determined

#### Q28. Underdetermined System Detection
Six products $P_1, P_2, P_3, P_4, P_5, P_6$ are launched on six consecutive months (January to June).
- $P_3$ is launched after $P_1$.
- Exactly two products are launched between $P_2$ and $P_5$.
- $P_6$ is launched in May.
- $P_4$ is launched immediately before $P_2$.
In which month is $P_1$ launched?  
A) January  
B) February  
C) March  
D) Cannot be determined from the given information

#### Q29. Boundary Collision Trap
Eight boxes $A$ through $H$ are arranged from 1 (bottom) to 8 (top).
- $A$ is placed at Position 4.
- Exactly 4 boxes are between $A$ and $B$.
- $C$ is placed 3 boxes above $D$.
- $E$ is placed immediately below $B$.
- How many boxes can possibly be placed between $C$ and $E$?  
A) Exactly 1  
B) Exactly 2  
C) Exactly 3  
D) No such configuration is mathematically possible

#### Q30. The "Adjacent Means Preceding or Succeeding" Trap
Seven colleagues $A, B, C, D, E, F, G$ attend interviews on days Monday through Sunday.
- $A$ is interviewed on Thursday.
- $B$ is interviewed on a day adjacent to $A$.
- $C$ is interviewed on a day adjacent to $B$.
- Exactly two days pass between $C$ and $D$.
- $E$ is interviewed on Monday.
If $B$ is interviewed on Friday, what day is $D$ interviewed?  
A) Tuesday  
B) Wednesday  
C) Saturday  
D) Either Tuesday or Saturday

---

### Level 7: Extreme Caselets (Q31–Q37)

#### Caselet 1: The Multi-Dimensional Enterprise Scheduler (Q31–Q34)
**Scenario:**  
Ten team leads: $A, B, C, D, E, F, G, H, J, K$ must be scheduled across five working days: **Monday, Tuesday, Wednesday, Thursday, Friday** (exactly two team leads per day).  
Each lead belongs to one of three project teams: **Alpha, Beta, Gamma** (Team Alpha has 4 leads, Team Beta has 3 leads, Team Gamma has 3 leads).  
Each lead operates out of one of three campus locations: **Loc-1, Loc-2, Loc-3**.

**Constraints:**
1. $A$ and $F$ belong to the same team but cannot be scheduled on the same day.
2. $B$ is scheduled exactly two days after $D$ (i.e. $\text{Day}(B) - \text{Day}(D) = 2$).
3. If $C$ is assigned to Team Alpha, then $G$ must be in Loc-2.
4. $H$ and $J$ cannot occupy the same location.
5. Exactly two members of Team Beta are scheduled before Wednesday.
6. $K$ is scheduled on the day immediately after whoever is assigned to Loc-3 on Wednesday.
7. $A$ is scheduled on Tuesday in Loc-1 as part of Team Alpha.
8. $D$ is scheduled on Monday in Loc-3 as part of Team Beta.
9. $F$ is assigned to Team Alpha and works on Thursday.
10. $C$ works on Monday in Loc-2 as part of Team Alpha.
11. $H$ and $J$ are scheduled together on Friday. Neither belongs to Team Alpha.
12. $E$ and $G$ are scheduled on Wednesday. $E$ works in Loc-3.

##### Q31. Location & Team Identification
Which team and location does $B$ belong to?  
A) Team Beta, Loc-1  
B) Team Gamma, Loc-2  
C) Team Beta, Loc-3  
D) Team Alpha, Loc-2

##### Q32. Wednesday Scheduling
What is the location and team assignment of $G$ on Wednesday?  
A) Loc-1, Team Beta  
B) Loc-2, Team Gamma  
C) Loc-2, Team Beta  
D) Loc-1, Team Gamma

##### Q33. Thursday Co-Lead Assignment
Who is scheduled alongside $F$ on Thursday, and which location do they operate from?  
A) $K$, Loc-1  
B) $K$, Loc-2  
C) $B$, Loc-3  
D) $J$, Loc-2

##### Q34. Friday Team Distribution
If $H$ belongs to Team Beta, which team does $J$ belong to, and what is the team composition on Friday?  
A) Team Gamma; 1 Beta and 1 Gamma  
B) Team Beta; 2 Beta  
C) Team Gamma; 2 Gamma  
D) Cannot be determined

---

#### Caselet 2: The Double-Flat 8-Story Matrix (Q35–Q37)
**Scenario:**  
An eight-story residential building has floors 1 to 8. Each floor contains exactly two flats: **Flat P** and **Flat Q**.  
Flat P is to the west of Flat Q.  
Eight residents $M_1, M_2, M_3, M_4, M_5, M_6, M_7, M_8$ live in Flat P across different floors, and eight residents $N_1, N_2, N_3, N_4, N_5, N_6, N_7, N_8$ live in Flat Q across different floors.
- $M_3$ lives on an even-numbered floor above Floor 4 in Flat P.
- $N_4$ lives on the same floor as $M_3$ (i.e. in Flat Q).
- Exactly two floors exist between $M_3$ and $M_1$. $M_1$ lives below $M_3$.
- $N_2$ lives on Floor 1 in Flat Q.
- $M_7$ lives immediately above $M_1$ in Flat P.
- $N_6$ lives on an odd-numbered floor immediately below the floor containing $N_4$.
- $M_5$ lives on Floor 8 in Flat P.

##### Q35. Flat P Floor Localization
Which floor does $M_1$ reside on in Flat P?  
A) Floor 2  
B) Floor 3  
C) Floor 4  
D) Floor 5

##### Q36. Flat Q Adjacency
Which resident lives in Flat Q on the same floor as $M_7$?  
A) $N_1$  
B) $N_6$  
C) $N_4$  
D) $N_2$

##### Q37. Boundary Counting
How many floors exist between the floor occupied by $M_5$ and the floor occupied by $M_7$?  
A) 1 floor  
B) 2 floors  
C) 3 floors  
D) 4 floors

---

### Level 8: Advanced Hybrid Reasoning (Q38–Q40)

#### Q38. Puzzle + Circular Seating Hybrid
Six executives $A, B, C, D, E, F$ work in departments $D_1$ to $D_6$ and live on floors 1 to 6. They sit around a circular table facing the center for a board meeting.
- The person living on Floor 3 sits second to the left of the person from department $D_1$.
- $A$ lives on Floor 6 and sits opposite $C$.
- $C$ works in $D_2$ and lives on Floor 1.
- The person on Floor 4 works in $D_4$ and sits immediately right of $A$.
- $E$ lives on Floor 2, works in $D_5$, and sits adjacent to neither $A$ nor $C$.
- $B$ sits immediately left of the person from $D_2$.
Which department does $A$ work in, and who sits opposite the person living on Floor 2?  
A) $D_1$, Person on Floor 4  
B) $D_6$, Person on Floor 3  
C) $D_3$, Person on Floor 4  
D) $D_1$, Person on Floor 3

#### Q39. Puzzle + Direction Sense Hybrid
Five consultants $V, W, X, Y, Z$ have offices on floors 1 to 5 of an office tower. At 5 PM, they depart the building ground floor and walk to client sites:
- The consultant from Floor 5 walks 4 km North, then 3 km East.
- The consultant from Floor 1 walks 5 km South.
- $X$ lives on Floor 3 and walks 3 km West, then 4 km North.
- $Z$ lives on Floor 5.
- $V$ lives on Floor 1.
- $Y$ lives on an even floor and walks to a point exactly at the origin (0, 0).
What is the straight-line shortest distance between the final location of $Z$ and the final location of $X$?  
A) 5 km  
B) 6 km  
C) $6\sqrt{2}$ km  
D) 10 km

#### Q40. Puzzle + Blood Relations Hybrid
A three-generation family of six members $P, Q, R, S, T, U$ (consisting of two married couples, two fathers, two mothers, and two children) are scheduled for dental checkups on six consecutive days from Monday to Saturday.
- The grandfather is scheduled on Monday.
- $P$ is the father of $T$ and is scheduled on Thursday.
- $Q$ is married to $P$ and is scheduled immediately after $P$.
- The grandmother is scheduled on Wednesday.
- $S$ is the grandson of $R$ and is scheduled on Saturday.
- $U$ is scheduled on Monday.
Who is scheduled on Tuesday, and what is their relation to $P$?  
A) $T$, Daughter/Son of $P$  
B) $R$, Mother of $P$  
C) $U$, Father of $P$  
D) $S$, Son of $P$

---

## 3. Master Answer Key & Comprehensive Solutions

### Master Answer Key (Q1–Q40)

| Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | B | **8** | C | **15** | B | **22** | A | **29** | D | **35** | B |
| **2** | D | **9** | A | **16** | A | **23** | C | **30** | B | **36** | A |
| **3** | C | **10** | B | **17** | B | **24** | B | **31** | A | **37** | C |
| **4** | B | **11** | B | **18** | B | **25** | D | **32** | B | **38** | A |
| **5** | A | **12** | A | **19** | B | **26** | D | **33** | B | **39** | B |
| **6** | B | **13** | A | **20** | A | **27** | B | **34** | A | **40** | A |
| **7** | C | **14** | A | **21** | B | **28** | A | - | - | - | - |

---

### Step-by-Step Derivations


#### Level 1 (Foundation)

#### Q1 Solution
- Total floors: 1 to 7. $F = 1$.
- $E$ is on an odd floor above Floor 4 $\implies E \in \{5, 7\}$.
- If $E = 7$: exactly 2 persons live between $E$ and $B \implies B = 7 - 3 = 4$. Then $A$ lives immediately above $B \implies A = 5$. $G$ is even $\implies G \in \{2, 6\}$. Remaining floors for $C, D \in \{2, 3, 6\}$. Floor 4 is occupied by $B$.
- If $E = 5$: 2 persons between $E$ and $B \implies B = 5 - 3 = 2$. Then $A$ immediately above $B \implies A = 3$. Even floors available for $G$: $\{4, 6\}$.
- In Case 1, Floor 4 is $B$.
- **Answer:** B) $B$

#### Q2 Solution
- Mon to Sat: 6 days. $R = \text{Wed}$ (Day 3).
- Exactly one person between $R$ and $T \implies T$ is either Mon (Day 1) or Fri (Day 5).
- $P$ is immediately before $S \implies [P, S]$ is a 2-day block.
- If $T = \text{Mon}$, available days: Tue, Thu, Fri, Sat. Block $[P, S]$ must take (Thu, Fri). Then remaining for $Q, U$: Tue and Sat. Since $Q \ne \text{Sat} \implies Q = \text{Tue}, U = \text{Sat}$.
- If $T = \text{Fri}$, available days: Mon, Tue, Thu, Sat. $[P, S]$ must be (Mon, Tue). Then Thu and Sat are left for $Q, U$. Since $Q \ne \text{Sat} \implies Q = \text{Thu}, U = \text{Sat}$.
- In both valid branches, $U$ is scheduled on Saturday!
- **Answer:** D) $U$

#### Q3 Solution
- Positions 1 to 7. $M = 4$. $K = 5$ (immediately above $M$).
- Exactly three boxes between $J$ and $K \implies |pos(J) - 5| = 4 \implies pos(J) = 1$ (since $5 + 4 = 9 > 7$).
- $P$ immediately above $J \implies P = 2$.
- Remaining positions: 3, 6, 7 for $L, O, N$.
- Box at Position 2 is uniquely $P$.
- **Answer:** C) $P$

#### Q4 Solution
- 5 majors: Physics, Chemistry, Biology, Mathematics, History.
- $X = \text{Biology}$. $V = \text{History}$.
- Physics is immediately between $V$ and $Y \implies [V, \text{Physics}, Y]$ or $[Y, \text{Physics}, V]$.
- Since $V = \text{History}$ is at one end of this triad, Physics cannot be History.
- $Z$ does not study Physics or Mathematics. Remaining subjects for $Z$: Chemistry.
- Thus, $Z = \text{Chemistry}$.
- The only unassigned subject for $Y$ in the triad is Mathematics!
- **Answer:** B) Mathematics

#### Q5 Solution
- Floors 1 to 6. $Z = 2$. $Y = 6$.
- Exactly two people between $U$ and $Z \implies pos(U) = 2 + 3 = 5$. So $U = 5$.
- $W$ lives above $Z$ but below $X \implies 2 < pos(W) < pos(X)$.
- Available floors: 1, 3, 4.
- For $2 < W < X$, we must have $W = 3$ and $X = 4$.
- The only remaining floor for $V$ is Floor 1.
- **Answer:** A) Floor 1

---

#### Level 2 (Intermediate)

#### Q6 Solution
- Mon to Fri: 5 days.
- $C = \text{Wed}$, $C \notin \{\text{AI}, \text{Cyber}\}$.
- $E = \text{Cloud}$ on Tuesday.
- Cyber lecture is on Friday.
- $A$ is immediately before Robotics $\implies [A, \text{Robotics}]$.
- For $A$ to lecture on Monday and teach AI, Tuesday is Robotics (or $E$ teaches Robotics while having Cloud? No, $A$ on Monday teaching AI matches option B).
- **Answer:** B) $A$, AI

#### Q7 Solution
- Floors 1 to 6. $M = \text{Audit}$ on Floor 1. $N = \text{Legal}$ on Floor 3. $K = \text{Floor 6}$.
- $P = \text{HR}$. Tech is on an even-numbered floor above $N(3) \implies \text{Floor 4 or 6}$.
- Person on Floor 2 belongs to Ops.
- **Answer:** C) Ops

#### Q8 Solution
- 6 boxes: 1 to 6. Box $A = 1$. White box = 5.
- Box $B$ is Blue and immediately above Red: $[\text{Red}, B(\text{Blue})]$.
- Box $C$ is two positions below Yellow: $pos(\text{Yellow}) - pos(C) = 2$.
- Yellow = 6, $C = 4$. Positions 2 and 3 are Red and Blue ($B$).
- White is at Position 5, which must be Box $E$.
- **Answer:** C) $E$

#### Q9 Solution
- Mar, Apr, May, Jun, Jul.
- Tokyo is visited in March.
- $R$ visits Paris in May.
- $S$ visits New York.
- $P$ visits Berlin immediately after $T$.
- $Q$ visits Tokyo in March.
- **Answer:** A) March, Tokyo

#### Q10 Solution
- Nights 1 to 6. Specialties: 2 Cardio, 2 Neuro, 2 Ortho.
- $D_1 = \text{Neuro}$ on Night 2.
- $D_4$ on Night 5. $D_3 = \text{Ortho}$ on Night 6.
- $D_2$ immediately before $D_4 \implies D_2$ on Night 4.
- $D_5 = \text{Cardio}$. Both Cardio on consecutive nights $\implies$ Nights 3 & 4.
- Remaining nights: Night 1 and Night 5 must be 1 Neuro and 1 Ortho.
- $D_6$ on Night 1 is Neuro.
- **Answer:** B) Neuro

---

#### Level 3 (Hard)

#### Q11 Solution
- Floors 1 to 8. $B = 4$. $D = 8$.
- As many floors between $D(8)$ and $E$ as between $E$ and $H \implies E$ is the midpoint of 8 and $H$.
- For $H = 2$, midpoint is $E = 5$.
- Floors between 8 and 5: 6, 7 (2 floors). Floors between 5 and 2: 3, 4 (2 floors).
- Matches all constraints. Floor 5 is $E$.
- **Answer:** B) $E$

#### Q12 Solution
- Mon to Sun (7 days: 1 to 7). $M = \text{Thu}$ (Day 4).
- $K$ immediately after $N$.
- Candidate placements place $N$ on Tuesday.
- **Answer:** A) Tuesday

#### Q13 Solution
- Positions 1 to 9. $F = 2$.
- Three boxes between $F(2)$ and $B \implies pos(B) = 2 + 4 = 6$.
- $A$ immediately above $B \implies A = 7$.
- Exactly two boxes between $A(7)$ and $C$:
  - Index difference of 3 gives $pos(C) = 4$.
- Therefore Box $C$ is at Position 4.
- **Answer:** A) Position 4

#### Q14 Solution
- Meta = 1. Google = 2. Apple = 3 ($R$). Netflix = 7 ($V$).
- $T$ higher than $U$ but lower than $P \implies P > T > U$.
- If $P$ did not join Meta (rank 1), $P$ must take rank 2 (Google).
- **Answer:** A) Google

#### Q15 Solution
- Days: Mon(1) to Sun(7). $C = \text{Sun}$ (7).
- Exactly one member between $B$ and $C(7) \implies B = \text{Fri}$ (5).
- $F$ immediately before $B \implies F = \text{Thu}$ (4).
- $A$ chairs three days after $D \implies \text{Day}(A) - \text{Day}(D) = 3$.
- With $D = \text{Wed}$ (3) and $A = \text{Sat}$ (6), $D$ chairs on Wednesday.
- **Answer:** B) $D$

---

#### Level 4 (Very Hard)

#### Q16 Solution
- Mumbai on Floor 5 (HR). Bangalore on Floor 6 (R&D). Pune on Floor 7 ($U$).
- Floor 1 is $R$ (Finance).
- IT is from Delhi on Floor 4.
- Since $P$ does not live on an odd floor, $P$ is on Floor 4 (Delhi).
- **Answer:** A) Delhi, Floor 4

#### Q17 Solution
- 8 floors: 1 to 8. Vacant is even above 3 $\implies$ Vacant $\in \{4, 6, 8\}$.
- If Vacant = 6: $C = 7$. Three floors between $A$ and $C(7) \implies F_A = 3$.
- $B = 1$. This satisfies all adjacency and non-occupancy constraints.
- Vacant floor is Floor 6.
- **Answer:** B) Floor 6

#### Q18 Solution
- 3 days $\times$ 2 slots.
- Mon AM = $T_6$, Mon PM = Topic $M_4$ in $R_5$.
- Tue AM = $T_3$ in $R_2$. Wed PM = $T_5$.
- Trainer on Tuesday afternoon is $T_2$.
- **Answer:** B) $T_2$

#### Q19 Solution
- 8 floors. $D = 8$ (Skoda). Audi = Floor 2.
- Three persons between $D(8)$ and $B \implies B = 4$.
- $A = 3$ (Tesla). BMW = Floor 6. $F = 7$. $H = 5$ (Ford). $G = 1$ (Hyundai).
- Floor 4 ($B$) owns Honda.
- **Answer:** B) Honda, Floor 4

#### Q20 Solution
- Mon to Sun. $P = \text{Fri}$ (Paris). $Q = \text{Wed}$. Dubai = Sun.
- $N$ departs on Sunday to Dubai.
- **Answer:** A) Sunday, Dubai

---

#### Level 5 (Expert)

#### Q21 Solution
- Fact: $A = \text{Tue}$ (2).
- Rule 1: $A_{\text{Tue}} \implies E_{\text{Fri}}$ (5).
- $F = \text{Sun}$ (7).
- $D$ exactly two days after $B \implies \text{Day}(D) - \text{Day}(B) = 2$.
- With $B = \text{Thu}$ (4) and $D = \text{Sat}$ (6), all constraints are met.
- **Answer:** B) Thursday

#### Q22 Solution
- $Z = \text{Thu}$. $Y = \text{Tue}$.
- Condition 2: $X = \text{Sat} \implies Y$ immediately after $W \implies W = \text{Mon}$.
- $W = \text{Mon}, Y = \text{Tue}, Z = \text{Thu}$ leaves Saturday for $X$.
- **Answer:** A) $X$

#### Q23 Solution
- Positions 1 to 9. $E = 5$.
- $A = 7$. Three boxes between $A(7)$ and $B \implies B = 3$.
- $C = 4$. Boxes above $C(4)$ is 5 $\implies$ boxes below $D$ is $5 \implies D = 6$.
- Position 1 is occupied by Box $I$.
- **Answer:** C) $I$

#### Q24 Solution
- $K_3 = \text{Tue Morning}$, $K_4 = \text{Wed Afternoon}$.
- $K_1, K_5$ on Monday.
- $K_8, K_6$ on Thursday.
- $K_7$ takes viva on Tuesday afternoon.
- **Answer:** B) Tuesday afternoon

#### Q25 Solution
- Scores: 45, 55, 65, 75, 85, 95.
- Floor 1 = 45 ($P$). Floor 3 = 65. Floor 4 = 75.
- Floors 2 and 5 have scores 55 and 85 (diff = 30).
- Floor 6 must have the remaining score: 95.
- **Answer:** D) 95

---

#### Level 6 (Traps & Inferences)

#### Q26 Solution
- Parity property: $\text{even} \pm 3 = \text{odd}$; $\text{odd} \pm 3 = \text{even}$.
- If $A$ is even, $B = A \pm 3$ must be odd.
- Then $C = B \pm 3$ must be even!
- Contradicts the statement that $C$ is on an odd floor.
- No valid arrangement exists.
- **Answer:** D) No valid arrangement exists (Contradiction)

#### Q27 Solution
- 10 floors, 4 vacant.
- Floors 1 and 10 occupied. $A = 3, F = 8$.
- Below $A(3)$, Floor 1 is occupied and Floor 2 can be occupied.
- Maximum floor for $C$ below $A$ is Floor 2.
- **Answer:** B) Floor 2

#### Q28 Solution
- 6 months: Jan to Jun. $P_6 = \text{May}$.
- $[P_4, P_2]$ with two products between $P_2$ and $P_5$.
- Forcing $P_4 = \text{Feb}, P_2 = \text{Mar}, P_5 = \text{Jun}$.
- $P_1$ must be in January.
- **Answer:** A) January

#### Q29 Solution
- Positions 1 to 8. $A = 4$.
- 4 boxes between $A$ and $B \implies |pos(B) - 4| = 5$.
- $4 + 5 = 9 > 8$; $4 - 5 = -1 < 1$.
- No such configuration is mathematically possible.
- **Answer:** D) No such configuration is mathematically possible

#### Q30 Solution
- $A = \text{Thu}$ (4). $B = \text{Fri}$ (5).
- $C$ adjacent to $B(5) \implies C = \text{Sat}$ (6).
- Two days between $C(6)$ and $D \implies |pos(D) - 6| = 3 \implies D = 3$ (Wednesday).
- **Answer:** B) Wednesday

---

#### Level 7 (Extreme Caselets)

#### Q31 Solution
- Deductions for Caselet 1:
  - Total 10 leads, 5 days, 3 teams (Alpha: 4, Beta: 3, Gamma: 3), 3 locations.
  - $ is scheduled 2 days after (Mon) ==> B$ is on Wednesday in Loc-1 as part of Team Beta.
- **Answer:** A) Team Beta, Loc-1

#### Q32 Solution
- In Caselet 1: If $ is assigned to Team Alpha, then $ must be in Loc-2.
- Since $ is Alpha, $ is in Loc-2. To balance quotas, $ belongs to Team Gamma.
- **Answer:** B) Loc-2, Team Gamma

#### Q33 Solution
- In Caselet 1: $ is scheduled on the day after whoever is in Loc-3 on Wednesday ($).
- Hence $ is on Thursday in Loc-2 alongside $.
- **Answer:** B) $, Loc-2

#### Q34 Solution
- In Caselet 1: Friday has $ and $, neither belonging to Alpha.
- If $ is Beta, then $ must be Gamma (1 Beta and 1 Gamma).
- **Answer:** A) Team Gamma; 1 Beta and 1 Gamma
#### Q35 Solution
- Deductions for Caselet 2:
  - 8 floors, Flat P (West) and Flat Q (East).
  - $ is Floor 8 (P). $ is on an even floor above 4 in P ==>  = Floor 6$.
  - Exactly two floors between (6)$ and $ ==>  = 6 - 3 = Floor 3$ (P).
- **Answer:** B) Floor 3

#### Q36 Solution
- In Caselet 2: $ is on Floor 4 in Flat P.
- Resident in Flat Q on Floor 4 alongside $ is $.
- **Answer:** A) $

#### Q37 Solution
- In Caselet 2: $ is on Floor 8 and $ is on Floor 4.
- Intervening floors = (8 - 4) - 1 = 3 floors (Floors 5, 6, 7).
- **Answer:** C) 3 floors
#### Q38 Solution
- 6 people around a circular table.
- $A$ (Floor 6) opposite $C$ (Floor 1, $D_2$).
- Floor 4 ($D_4$) sits immediately right of $A$.
- Matching all cross-constraints: $A$ works in $D_1$, and the person opposite Floor 2 is the person on Floor 4.
- **Answer:** A) $D_1$, Person on Floor 4

#### Q39 Solution
- $Z$ (Floor 5): $(3, 4)$.
- $X$ (Floor 3): $(-3, 4)$.
- Distance: $\sqrt{(3 - (-3))^2 + (4 - 4)^2} = \sqrt{6^2 + 0} = 6 \text{ km}$.
- **Answer:** B) 6 km

#### Q40 Solution
- 3 generations: Grandparents $U$ (Mon), $R$ (Wed). Parents $P$ (Thu), $Q$ (Fri). Children $S$ (Sat), $T$ (Tue).
- Person scheduled on Tuesday is $T$, who is Daughter/Son of $P$.
- **Answer:** A) $T$, Daughter/Son of $P$

---

## 4. Rapid Revision & Strategic Exam Traps

```
+-----------------------------------------------------------------------------------+
|                        TOP 5 HIGH-PRESSURE PLACEMENT TRAPS                        |
+-----------------------------------------------------------------------------------+
| 1. "Between" vs "Floors Away":                                                    |
|    "k floors between A and B"  ==>  |Floor(A) - Floor(B)| = k + 1                 |
|    "A is k floors away from B" ==>  |Floor(A) - Floor(B)| = k                     |
|-----------------------------------------------------------------------------------|
| 2. Vacant Floor Phantom Entity:                                                   |
|    A vacant floor counts as a floor in index calculations, but DOES NOT count as  |
|    a "person" in "k persons live between X and Y"!                                |
|-----------------------------------------------------------------------------------|
| 3. Inverse Fallacy on Conditional Clues:                                         |
|    "If P then Q" DOES NOT imply "If not P then not Q".                            |
|    Only the contrapositive "If not Q then not P" is logically guaranteed.        |
|-----------------------------------------------------------------------------------|
| 4. Parity Mismatch on Difference Trees:                                           |
|    Even + Odd = Odd;  Odd + Odd = Even. Always check parity consistency before    |
|    investing 4 minutes building invalid case splits!                              |
|-----------------------------------------------------------------------------------|
| 5. "Immediately Before/After" on Shift Rotations:                                 |
|    Ensure whether Sunday wraps around to Monday or if the week terminates strictly|
|    on Sunday before chaining relative day polyominoes.                            |
+-----------------------------------------------------------------------------------+
```

---

## 🔗 Cross-Links & Conceptual Continuations

- [Seating Arrangement](seating-arrangement.md) — Circular, Linear & Two-Row Spatial Formations
- [Order & Ranking](order-ranking.md) — Overlapping Bounds & Relative Ranking Chains
- [Blood Relations](blood-relations.md) — Generational Trees & Coded Pedigree Inference
- [Direction Sense](direction-sense.md) — 2D Cartesian Coordinate Displacements & Bearings
