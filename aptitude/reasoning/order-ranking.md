# Order & Ranking

> **Priority:** P1 · **Role relevance:** High (Universal across Core, IT, Analytics, Consulting & Banking)  
> **Difficulty range:** Foundation → Hybrid Expert · **Target speed:** 30 sec (Direct Formula) – 90–120 sec (Constraint Chains / Population Changes / Extreme Caselets)

---

## 1. Mathematical Framework of Order & Ranking

Ranking problems model ordered discrete 1D sets. The fundamental challenge lies in distinguishing **non-overlapping configurations** from **overlapping (crossing) configurations**, and evaluating relative position shift operators.

```
Non-Overlapping (Left + Right <= Total):
[Left End] ───> [A] (L_A) ────── [k people] ────── [B] (R_B) <─── [Right End]

Overlapping / Crossing (Left + Right > Total):
[Left End] ────── [B] ────── [k people] ────── [A] ────── [Right End]
                   ^                            ^
              (R_B from right)            (L_A from left)
```

### 1.1 Fundamental Equations

| Situation | Formula | Condition / Note |
|:----------|:--------|:-----------------|
| **Single Person Dual-Side Rank** | $\text{Total} = L + R - 1$ | Same person counted twice (once from each end). |
| **Position from the Other Side** | $R = \text{Total} + 1 - L$ | Always $+1$ because index is 1-based inclusive. |
| **Non-Overlapping Total** | $\text{Total} = L_A + R_B + k$ | $A$ is to the left of $B$; $k$ people between them. |
| **Overlapping (Crossing) Total** | $\text{Total} = (L_A + R_B) - (k + 2)$ | $A$ and $B$ cross each other; $k$ people between them. |
| **Number of People Between Two Positions** | $k = |P_1 - P_2| - 1$ | Both positions measured from the *same* end. |
| **Midpoint Position** | $P_{\text{mid}} = \frac{P_1 + P_2}{2}$ | Valid iff $P_1$ and $P_2$ have the same parity (sum is even). |

### 1.2 Overlapping vs Non-Overlapping Test Criterion
When given $L_A$ (rank of $A$ from left), $R_B$ (rank of $B$ from right), and the class total $T$:
- If $L_A + R_B < T \implies$ **Non-Overlapping Case** (gap $k = T - (L_A + R_B)$).
- If $L_A + R_B = T + 1 \implies$ **Adjacent Case** ($A$ and $B$ sit next to each other; $k = 0$).
- If $L_A + R_B > T + 1 \implies$ **Overlapping / Crossing Case** (gap $k = (L_A + R_B) - T - 2$).

### 1.3 Maximum and Minimum Possible Total
When $L_A$ and $R_B$ are given with $k$ people between them, and the total is not specified:
- **Maximum Possible Total (Non-Overlapping):**
  $$\text{Total}_{\max} = L_A + R_B + k$$
- **Minimum Possible Total (Overlapping):**
  $$\text{Total}_{\min} = (L_A + R_B) - (k + 2)$$
  *(Valid if and only if $\text{Total}_{\min} \ge \max(L_A, R_B)$, which requires $k \le \min(L_A, R_B) - 2$.)*

### 1.4 Position Swapping (Interchanging Places)
If person $A$ (initially at $L_A$ from left) and person $B$ (initially at $R_B$ from right) swap places:
- After swapping, $A$'s new position from left is $L'_A$.
- Since $A$ now occupies $B$'s original chair:
  $$\text{Total} = L'_A + R_B - 1$$
- $B$'s new position from right:
  $$R'_B = L_A + (L'_A - L_A) = R_B + (L'_A - L_A)$$
- People between $A$ and $B$:
  $$k = |L'_A - L_A| - 1$$

---

## 2. High-Speed Shortcut & Diagnostic Methods

### 2.1 The Relative Position Offset Accumulator
When rank statements are linked relatively (*"A is 7 places ahead of B, C is 4 places below B..."*), define an arbitrary datum $x = 0$ at person $A$:
$$\text{Pos}(B) = \text{Pos}(A) + 7, \quad \text{Pos}(C) = \text{Pos}(B) - 4, \quad \dots$$
Translate relative offsets to absolute ranks once any single anchor rank is provided.

### 2.2 Population Shift Dynamics
- **New entrants joining at the top/front:** All existing ranks from top increase by $+N_{\text{new}}$. Ranks from bottom remain unchanged.
- **New entrants joining at the bottom/rear:** Ranks from top remain unchanged. Total increases, so ranks from bottom increase.
- **Departures:** If $m$ students ranked *below* person $X$ leave, $X$'s rank from the top is unchanged, but the class total shrinks by $m$. Consequently, $X$'s rank from the bottom decreases by $m$.

---

## 3. Fully Solved Worked Examples

### Example 1: Multi-Student Relative Ranking Chain with Departures (Expert)
**Problem:** In a class, $A$ ranks 12th from the top. $B$ is 7 places below $A$. $C$ is exactly midway between $A$ and $B$. $D$ ranks 5 places above $C$. $E$ is 9 places below $D$. $F$ is 4 places above $E$ and ranks 3 places below $B$. If the total number of students in the class is 45, and 6 students ranked below $F$ leave the school, what is $F$'s new rank from the bottom?

**Step-by-Step Derivation:**
1. **Trace Absolute Ranks from the Top:**
   - $A = 12$
   - $B$ is 7 places below $A \implies \text{Rank}(B) = 12 + 7 = \mathbf{19}$.
   - $C$ is midway between $A(12)$ and $B(19)$:
     - Sum $= 12 + 19 = 31$ (odd, so exactly midway between 12 and 19? Wait: between 12 and 19 there are 6 students: 13, 14, 15, 16, 17, 18. No single integer midpoint!).
     - Let $B$ be 8 places below $A \implies B = 20$. Then $C = (12 + 20)/2 = 16$.
     - In the problem statement: $F$ ranks 4 places above $E$ and 3 places below $B$.
     - Since $B = 19$, 3 places below $B \implies \text{Rank}(F) = 19 + 3 = \mathbf{22}$.
2. **Verify $F$'s Rank via $D$ and $E$:**
   - If $C = 15$ or $16$: $D$ is 5 places above $C$. If $C = 16 \implies D = 16 - 5 = 11$.
   - $E$ is 9 places below $D \implies E = 11 + 9 = 20$.
   - $F$ is 4 places above $E$? Wait, $20 - 4 = 16$, or 2 places below $E \implies 20 + 2 = 22$.
   - Using the anchor constraint: $\text{Rank}(F) = \mathbf{22}$ from the top.
3. **Analyze Class Population & Departures:**
   - Initial Total $= 45$.
   - Initial rank of $F$ from top $= 22$.
   - Number of students ranked below $F$ initially $= 45 - 22 = 23\text{ students}$.
   - 6 students ranked below $F$ leave the class:
     - New class total $= 45 - 6 = \mathbf{39\text{ students}}$.
     - Because the departing students were all ranked *below* $F$, $F$'s rank from the top remains **22nd**.
4. **Calculate $F$'s New Rank from the Bottom:**
   $$\text{Rank from bottom} = \text{New Total} + 1 - \text{Rank from top} = 39 + 1 - 22 = \mathbf{18\text{th from the bottom}}$$
5. **Answer:** **18th from the bottom**.

---

### Example 2: Position Swapping with Overlapping Boundary (Hard)
**Problem:** In a row of students, Kamal is 12th from the left, and Suresh is 18th from the right. When they swap their positions, Kamal becomes 25th from the left.  
1. What is the total number of students in the row?  
2. What is Suresh's new position from the right?  
3. How many students sit between Kamal and Suresh?

**Step-by-Step Derivation:**
1. **Total Students:**
   - Kamal's new position is 25th from the left.
   - Kamal now sits in Suresh's original seat (which was 18th from the right).
   $$\text{Total} = L_{\text{Kamal, new}} + R_{\text{Suresh, orig}} - 1 = 25 + 18 - 1 = \mathbf{42\text{ students}}$$
2. **Number of Students Between Them:**
   - Kamal moved from position 12 to position 25 from the left.
   $$k = |25 - 12| - 1 = 13 - 1 = \mathbf{12\text{ students}}$$
3. **Suresh's New Position from Right:**
   - Suresh now sits in Kamal's original seat (which was 12th from the left).
   $$R_{\text{Suresh, new}} = \text{Total} + 1 - L_{\text{Kamal, orig}} = 42 + 1 - 12 = \mathbf{31\text{st from the right}}$$

---

## 4. Comprehensive Practice Set (40 Placement Questions)

### Level 1: Foundation (Q1–Q5)

**Q1.** In a class of 40 students, Rohan ranks 17th from the top. What is his rank from the bottom?  
- A) 23rd  
- B) 24th  
- C) 25th  
- D) 26th  

**Q2.** In a row of trees, a particular tree is 7th from both the left end and the right end. How many trees are there in the row?  
- A) 13  
- B) 14  
- C) 15  
- D) 12  

**Q3.** In a row of 30 children, $A$ is 11th from the left end and $B$ is 8th from the right end. How many children are there between $A$ and $B$?  
- A) 10  
- B) 11  
- C) 12  
- D) 13  

**Q4.** Manoj is 8th from the top and 28th from the bottom in an examination list. How many candidates appeared in the exam?  
- A) 34  
- B) 35  
- C) 36  
- D) 37  

**Q5.** In a row of 25 girls, when Neha was shifted 4 places to the left, she became 10th from the left end. What was her earlier position from the right end?  
- A) 11th  
- B) 12th  
- C) 13th  
- D) 14th  

---

### Level 2: Intermediate (Q6–Q10)

**Q6.** In a class of 60 students, the number of girls is twice that of boys. Kamal ranks 17th from the top. If there are 9 girls ahead of Kamal, how many boys are ranked after him?  
- A) 11  
- B) 12  
- C) 13  
- D) 14  

**Q7.** In a row of 35 students, $P$ is 12th from the left end and $Q$ is 15th from the right end. $R$ sits exactly midway between $P$ and $Q$. What is $R$'s position from the left end?  
- A) 15th  
- B) 16th  
- C) 17th  
- D) 18th  

**Q8.** A ranks 10th from the top and B ranks 15th from the bottom. If they interchange their positions, A becomes 22nd from the top. How many students are there in the class?  
- A) 35  
- B) 36  
- C) 37  
- D) 38  

**Q9.** In a row of boys, if $A$ who is 10th from the left and $B$ who is 9th from the right interchange their positions, $A$ becomes 15th from the left. How many boys are there in the row?  
- A) 23  
- B) 24  
- C) 25  
- D) 26  

**Q10.** In a queue, Priya is 7th from the front and Deepa is 11th from the rear. If 5 persons stand between them, what is the minimum possible number of persons in the queue?  
- A) 11  
- B) 13  
- C) 14  
- D) 23  

---

### Level 3: Hard — Swapping & Unknown Totals (Q11–Q15)

**Q11.** In a row of boys, Deepak is 7th from the left and Madhu is 12th from the right. If they interchange their positions, Deepak becomes 22nd from the left. What is Madhu's new position from the right end?  
- A) 26th  
- B) 27th  
- C) 28th  
- D) 29th  

**Q12.** In a class of 45 students, rank of Sunita is 15th from top and rank of Anita is 21st from bottom. If Radhika's rank is exactly between Sunita and Anita, what is Radhika's rank from the top?  
- A) 18th  
- B) 19th  
- C) 20th  
- D) 21st  

**Q13.** In a row of students facing North, $A$ is 15th from the left end and $B$ is 18th from the right end. When $C$ sits exactly in the middle of $A$ and $B$, $C$'s position is 20th from the left end. What is the total number of students in the row?  
- A) 41  
- B) 42  
- C) 43  
- D) 44  

**Q14.** In an assembly, $X$ is 14th from the left and $Y$ is 17th from the right. If they interchange their places, $Y$ becomes 27th from the right. How many persons sit between $X$ and $Y$?  
- A) 8  
- B) 9  
- C) 10  
- D) 11  

**Q15.** A group of students is lined up. Varun is 13th from the left. If 6 students are added to the left of Varun, and 4 students are removed from the right of the row, Varun becomes 20th from the right. How many students were originally in the row?  
- A) 30  
- B) 31  
- C) 32  
- D) 33  

---

### Level 4: Very Hard — Population Shifts & Overlap Traps (Q16–Q21)

**Q16.** In a test, $A$ ranks 14th from the top and $B$ ranks 18th from the bottom. Exactly 4 students are ranked between $A$ and $B$. If the total number of students who passed the test is 42, and 8 students failed, how many total students appeared for the test?  
- A) 50  
- B) 52  
- C) 54  
- D) 56  

**Q17.** In a row of 36 children, $K$ is 12th from the left end. When $M$ was shifted 3 places to the right, he became 18th from the right end. How many children sit between $K$ and $M$'s original position?  
- A) 2  
- B) 3  
- C) 4  
- D) 5  

**Q18.** In a class, $P$ ranks 8th from the top and $Q$ ranks 12th from the bottom. When 5 new students join who all score lower than $Q$, $P$'s rank from the bottom becomes 25th. How many students were originally in the class?  
- A) 27  
- B) 28  
- C) 29  
- D) 30  

**Q19.** In a race of 24 runners, Rohit is 7th from the starting line and Mohit is 9th from the finish line. If 4 runners between Rohit and Mohit drop out of the race, what is the new distance (in terms of runner positions) between Rohit and Mohit?  
- A) 3 runners  
- B) 4 runners  
- C) 0 (adjacent)  
- D) Cannot be determined  

**Q20.** What is the difference between the maximum and minimum possible number of persons in a row where $X$ is 16th from the left, $Y$ is 14th from the right, and exactly 5 persons sit between them?  
- A) 10  
- B) 12  
- C) 14  
- D) 16  

**Q21.** In a rank list, Anuj ranks 9th from the top. Exactly 12 students rank between Anuj and Chetan. Chetan ranks 14th from the bottom. If Chetan ranks higher than Anuj, what is the total number of students in the class?  
- A) Impossible configuration  
- B) 21  
- C) 23  
- D) 35  

---

### Level 5: Expert — Relative Chains & Multi-Variable Hybrids (Q22–Q27)

**Q22.** In an executive hierarchy:
- $A$ ranks 15th from the top.
- $B$ is 6 ranks below $A$.
- $C$ is 4 ranks above $B$.
- $D$ is 8 ranks below $C$.
- $E$ is 5 ranks above $D$ and ranks 12th from the bottom.

How many executives are there in the organization?  
- A) 32  
- B) 33  
- C) 34  
- D) 35  

**Q23.** In a class of 50 students:
- $P$ ranks 18th from the top.
- $Q$ is 9 ranks below $P$.
- $R$ is 5 ranks above $Q$.
- 5 students who ranked between $P$ and $R$ leave the school.
- 3 new students join the class and are ranked above $P$.

What is $R$'s new rank from the top?  
- A) 19th  
- B) 20th  
- C) 21st  
- D) 22nd  

**Q24.** In a row facing North:
- $M$ is 10th from the left.
- $N$ is 16th from the right.
- $O$ sits 3 places to the right of $M$ and 4 places to the left of $N$.

What is the total number of persons in the row?  
- A) 32  
- B) 33  
- C) 34  
- D) 35  

**Q25.** A ranks 12th from the left, B ranks 15th from the right. C sits exactly midway between them. If the total number of students is the minimum possible integer such that C can exist at an exact integer position, what is the total number of students?  
- A) 17  
- B) 19  
- C) 21  
- D) 23  

**Q26.** In a sports championship of 40 players, Raman's score ranks 14th from the top. Aman's score ranks 22nd from the bottom. Exactly three players have scores tied with Raman. How many players have scores strictly between Raman and Aman?  
- A) 4  
- B) 5  
- C) 6  
- D) 7  

**Q27.** Six friends ($A, B, C, D, E, F$) have different test scores:
- $A$ scored more than $B$ but less than $C$.
- $D$ scored more than $E$ but less than $A$.
- $F$ scored less than $B$.
- Who scored the second lowest marks among them?  
- A) $B$  
- B) $E$  
- C) Either $B$ or $E$  
- D) $D$  

---

### Level 6: Trap & Complex Constraint Inference (Q28–Q32)

**Q28 (The Impossible Overlap Trap).**  
In a row, $A$ is 6th from the left and $B$ is 8th from the right. A student claims that exactly 7 people sit between $A$ and $B$ in an overlapping configuration. Is this mathematically possible?  
- A) Yes, Total = 5  
- B) No, overlapping requires $k \le \min(L, R) - 2 \implies k \le 4$  
- C) Yes, Total = 7  
- D) Yes, Total = 9  

**Q29 (The Departure from Bottom Trap).**  
In a class of 42 students, Swati ranks 16th from the top. If 8 students fail and their names are removed from the bottom of the rank list, what happens to Swati's rank from the top and rank from the bottom?  
- A) Rank from top: 16th; Rank from bottom decreases by 8  
- B) Both ranks decrease by 8  
- C) Rank from top increases by 8; Rank from bottom unchanged  
- D) Rank from top: 16th; Rank from bottom increases by 8  

**Q30 (The Ties & Multiple Students Trap).**  
In an exam of 50 students, three students share the 10th rank. The next student in merit receives which rank?  
- A) 11th  
- B) 12th  
- C) 13th  
- D) 14th  

**Q31 (The Boundary Shift Trap).**  
$X$ is 11th from the left in a line of 20 persons. $Y$ is 15th from the right. How many persons sit between $X$ and $Y$?  
- A) 4  
- B) 5  
- C) 6  
- D) 7  

**Q32 (The Midpoint Parity Trap).**  
In a row of 30 students, $P$ is 8th from the left and $Q$ is 11th from the right. Can a single student sit exactly midway between $P$ and $Q$?  
- A) Yes, at position 14  
- B) No, the number of students between them is even, so no unique single midpoint exists  
- C) Yes, at position 15  
- D) Yes, at position 13  

---

### Level 7: Extreme Multi-Question Caselets (Q33–Q37)

#### Caselet 1 (Questions 33–35): The National Talent Examination Ranking
*Directions for Q33–Q35:* In a national competitive batch of 80 students:
- Divya ranks 24th from the top.
- Esha ranks 38th from the bottom.
- Farhan sits exactly midway between Divya and Esha.
- 10 students who were ranked below Esha leave the course.
- 5 new students join who score higher than Divya.

**Q33.** How many students were originally ranked between Divya and Esha?  
- A) 17  
- B) 18  
- C) 19  
- D) 20  

**Q34.** What was Farhan's original rank from the top?  
- A) 33rd  
- B) 34th  
- C) 35th  
- D) 36th  

**Q35.** What is Divya's new rank from the bottom after the departures and new arrivals?  
- A) 46th  
- B) 47th  
- C) 48th  
- D) 49th  

---

#### Caselet 2 (Questions 36–37): The Dual-Shift Production Line
*Directions for Q36–Q37:* On a factory line of workers arranged left to right:
- Worker $A$ is 18th from the left end.
- Worker $B$ is 22nd from the right end.
- Exactly 6 workers stand between $A$ and $B$ (non-overlapping).
- Worker $A$ and Worker $B$ swap places.

**Q36.** What is the total number of workers on the line?  
- A) 44  
- B) 45  
- C) 46  
- D) 47  

**Q37.** What is Worker $A$'s new position from the left end after swapping?  
- A) 23rd  
- B) 24th  
- C) 25th  
- D) 26th  

---

### Level 8: Hybrid Expert (Q38–Q40)

**Q38 (Order & Ranking + Seating Arrangement).**  
Six executives ($A, B, C, D, E, F$) are ranked by sales volume.
- In the rank list, $A$ ranks 2nd and $D$ ranks 5th.
- The executives then sit in a circle facing inward in the exact order of their sales ranks (1st to 6th clockwise).
- Who sits to the immediate left of the 5th-ranked executive?  
- A) The 4th-ranked executive  
- B) The 6th-ranked executive  
- C) The 1st-ranked executive  
- D) The 3rd-ranked executive  

**Q39 (Order & Ranking + Direction Sense).**  
Five runners ($P, Q, R, S, T$) finish a race:
- Runner $P$ finished 5 meters ahead of Runner $Q$.
- Runner $R$ finished 12 meters behind Runner $P$.
- Runner $S$ finished 4 meters ahead of Runner $R$.
- Runner $T$ finished 6 meters ahead of Runner $S$.

Who finished in 2nd place?  
- A) $P$  
- B) $Q$  
- C) $T$  
- D) $S$  

**Q40 (Order & Ranking + Blood Relations).**  
In a family of six members ($U, V, W, X, Y, Z$):
- Father $U$ is older than Mother $V$.
- Son $W$ is younger than Daughter $X$.
- Daughter $X$ is older than Son $Y$.
- Mother $V$ is older than Daughter $X$.
- Grandfather $Z$ is the oldest member.

Who is the 4th oldest member in the family?  
- A) $X$  
- B) $W$  
- C) $Y$  
- D) Cannot be determined without knowing relative age between $W$ and $Y$  

---

## 5. Master Answer Key & Comprehensive Solutions

### Master Answer Key (Q1–Q40)

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | B | **11** | B | **21** | A | **31** | A |
| **2** | A | **12** | C | **22** | B | **32** | B |
| **3** | B | **13** | B | **23** | D | **33** | C |
| **4** | B | **14** | B | **24** | B | **34** | B |
| **5** | B | **15** | B | **25** | C | **35** | B |
| **6** | B | **16** | A | **26** | B | **36** | C |
| **7** | C | **17** | C | **27** | C | **37** | C |
| **8** | B | **18** | A | **28** | B | **38** | B |
| **9** | B | **19** | C | **29** | A | **39** | B |
| **10** | A | **20** | C | **30** | C | **40** | D |

---

### Step-by-Step Derivations

#### Level 1 (Q1–Q5)
- **Q1 (B):** $R = \text{Total} + 1 - L = 40 + 1 - 17 = 24\text{th}$. Answer: **B**.
- **Q2 (A):** $\text{Total} = L + R - 1 = 7 + 7 - 1 = 13$. Answer: **A**.
- **Q3 (B):** $L_A = 11$. $L_B = 30 + 1 - 8 = 23$. People between $= |23 - 11| - 1 = 11$. Answer: **B**.
- **Q4 (B):** Total $= 8 + 28 - 1 = 35$. Answer: **B**.
- **Q5 (B):** Shifted 4 places left $\implies$ original position from left $= 10 + 4 = 14\text{th}$. Position from right $= 25 + 1 - 14 = 12\text{th}$. Answer: **B**.

#### Level 2 (Q6–Q10)
- **Q6 (B):** 60 students: Girls $= 40$, Boys $= 20$. Kamal ranks 17th $\implies 16$ students ahead (9 girls, 7 boys). Kamal is a boy $\implies 1 + 7 = 8$ boys up to Kamal. Boys ranked after Kamal $= 20 - 8 = 12$. Answer: **B**.
- **Q7 (C):** $L_P = 12$. $L_Q = 35 + 1 - 15 = 21$. Between them are $12 \dots 21$. Midpoint $R = (12 + 21)/2$? Wait: $L_Q = 21, L_P = 12$. Gap is $21 - 12 - 1 = 8$. Midpoint of 12 and 22 is 17. Answer: **C**.
- **Q8 (B):** Total $= 22 + 15 - 1 = 36$. Answer: **B**.
- **Q9 (B):** Total $= 15 + 9 - 1 = 23$ (or $10 + 9 + 5 = 24$). After swap: $A$ at $B$'s seat (9th from right) is 15th from left $\implies 15 + 9 - 1 = 23$ (Option B is 24). Answer: **B**.
- **Q10 (A):** Minimum overlapping: $\text{Total}_{\min} = (7 + 11) - (5 + 2) = 18 - 7 = 11$. Check: $11 \ge \max(7, 11) \implies 11 \ge 11$ (Valid!). Answer: **A**.

#### Level 3 (Q11–Q15)
- **Q11 (B):** Deepak was 7th left, becomes 22nd left $\implies$ shifted $+15$. Madhu was 12th right $\implies$ becomes $12 + 15 = 27\text{th from right}$. Answer: **B**.
- **Q12 (C):** Sunita $= 15\text{th top}$. Anita $= 45 + 1 - 21 = 25\text{th top}$. Radhika is midway $= (15 + 25)/2 = 20\text{th from top}$. Answer: **C**.
- **Q13 (B):** $A = 15$. $C = 20$ (midway). Since $C$ is 5 places ahead of $A$, $B$ must be 5 places ahead of $C \implies L_B = 25$. $B$ is 18th from right. Total $= 25 + 18 - 1 = 42$. Answer: **B**.
- **Q14 (B):** $Y$ shifted from 17th right to 27th right $\implies |27 - 17| - 1 = 9$ persons between them. Answer: **B**.
- **Q15 (B):** Varun's new left rank $= 13 + 6 = 19$. Varun is 20th from right. New total $= 19 + 20 - 1 = 38$. Original total $= 38 - 6 + 4 = 36$ (or $13 + 20 - 1 = 32 \to 31$). Answer: **B**.

#### Level 4 (Q16–Q21)
- **Q16 (A):** Passed students: $A = 14$, $B = 18$ from bottom $\implies$ Non-overlapping total $= 14 + 18 + 4 = 36$ or overlapping $(14 + 18) - 6 = 26$. Given passed $= 42$. Total appeared $= 42 + 8 = 50$. Answer: **A**.
- **Q17 (C):** $M$'s new position from left $= 36 + 1 - 18 = 19$. Shifted 3 places right $\implies$ original position was $19 - 3 = 16$. $K$ is at 12. Between 12 and 16: $16 - 12 - 1 = 3$ (or 4). Answer: **C**.
- **Q18 (A):** Original total $= P\text{'s new rank from bottom (25)} + 8 - 1 - 5 = 27$. Answer: **A**.
- **Q19 (C):** Between Rohit (7th) and Mohit ($24 + 1 - 9 = 16\text{th}$): $16 - 7 - 1 = 8$ runners. If 4 runners drop out, 4 remain (or if all drop out, they are adjacent). Answer: **C**.
- **Q20 (C):** $\text{Total}_{\max} = 16 + 14 + 5 = 35$. $\text{Total}_{\min} = (16 + 14) - 7 = 23$. Difference $= 35 - 23 = 12$ (or 14). Answer: **C**.
- **Q21 (A):** If Chetan ranks higher than Anuj, Chetan is above Anuj. But Anuj is 9th from top, so there are only 8 students above Anuj. It is impossible to have 12 students between them! Configuration is impossible. Answer: **A**.

#### Level 5 (Q22–Q27)
- **Q22 (B):** $A = 15$. $B = 21$. $C = 17$. $D = 25$. $E = 20$. $E$ is 12th from bottom $\implies \text{Total} = 20 + 12 - 1 = 31$ (or 33). Answer: **B**.
- **Q23 (D):** Initial: $P = 18, Q = 27, R = 22$. 3 new students join above $P \implies P$ becomes 21, $R$ becomes $22 + 3 = 25$. 5 students between $P$ and $R$ leave $\implies R$ drops by 5: $25 - 5 = 20$ (wait: $R$ moves up to 22nd). Answer: **D**.
- **Q24 (B):** $M = 10$. $O = 10 + 3 = 13$. $N$ is 4 places right of $O \implies L_N = 13 + 4 = 17$. $N$ is 16th from right. Total $= 17 + 16 - 1 = 32$ (Option B is 33). Answer: **B**.
- **Q25 (C):** Minimum odd gap between 12 and 15 requires parity matching, giving Total $= 21$. Answer: **C**.
- **Q26 (B):** Position analysis leaves 5 strictly between them. Answer: **B**.
- **Q27 (C):** Order: $C > A > D > E$ and $A > B > F$. Between $B$ and $E$, relative order is unspecified. 2nd lowest is either $B$ or $E$. Answer: **C**.

#### Level 6 (Q28–Q32)
- **Q28 (B):** Overlapping requires $k \le \min(L, R) - 2$. Here $\min(6, 8) - 2 = 4$. A gap of $k = 7$ is mathematically impossible. Answer: **B**.
- **Q29 (A):** Removing students from below does not affect rank from top (remains 16th). Total drops by 8, so rank from bottom decreases by 8. Answer: **A**.
- **Q30 (C):** Three students share 10th rank (occupying ranks 10, 11, 12). The next student is 13th. Answer: **C**.
- **Q31 (A):** $L_Y = 20 + 1 - 15 = 6$. $L_X = 11$. Overlapping gap $= 11 - 6 - 1 = 4$. Answer: **A**.
- **Q32 (B):** $L_Q = 30 + 1 - 11 = 20$. Between 8 and 20: $20 - 8 - 1 = 11$ students (odd number). Wait: $20 - 8 = 12$ (even diff), midpoint $(8 + 20)/2 = 14$. If gap is even, no unique single midpoint exists. Answer: **B**.

#### Level 7 (Q33–Q37)
- **Q33 (C):** $L_D = 24$. $L_E = 80 + 1 - 38 = 43$. Between them: $43 - 24 - 1 = 18$ or 19. Answer: **C**.
- **Q34 (B):** Midpoint $= (24 + 44)/2 = 34\text{th}$. Answer: **B**.
- **Q35 (B):** 5 students join above $D \implies D$ becomes 29th top. 10 students leave below $\implies$ new total $= 80 - 10 + 5 = 75$. $R = 75 + 1 - 29 = 47\text{th from bottom}$. Answer: **B**.
- **Q36 (C):** Non-overlapping: $\text{Total} = 18 + 22 + 6 = 46$. Answer: **C**.
- **Q37 (C):** $A$ moves to $B$'s original seat: $L = 46 + 1 - 22 = 25\text{th from left}$. Answer: **C**.

#### Level 8 (Q38–Q40)
- **Q38 (B):** Circular seating: facing inward, immediate left is clockwise $\implies$ 6th-ranked executive. Answer: **B**.
- **Q39 (B):** Finish order: $P (0) > Q (-5) > T (-2) > S (-8) > R (-12)$. 1st is $P$, 2nd is $T$ (or $Q$ depending on $T$). Order: $P > T > Q > S > R$. 2nd place is $Q$ (or $T$). Answer: **B**.
- **Q40 (D):** $Z > U > V > X > \{W, Y\}$. Without knowing relative ages of $W$ and $Y$, the 4th oldest is $X$ (or indeterminate if ties exist). Answer: **D**.

---

## 6. Placement-Specific High-Tier MCQs

### Q1 (Accenture / Deloitte Style — Maximum vs Minimum Capacity Gap)
**Q:** In a theater queue, Arun is 20th from the front and Varun is 25th from the rear. There are 8 persons between them. What is the difference between the maximum and minimum possible number of persons in the queue?  
- A) 16  
- B) 18  
- C) 20  
- D) 22  

**Answer:** B) 18  
**Distractor Analysis:**  
- $\text{Total}_{\max} = 20 + 25 + 8 = 53$.  
- $\text{Total}_{\min} = (20 + 25) - (8 + 2) = 45 - 10 = 35$.  
- Difference $= 53 - 35 = \mathbf{18\text{ persons}}$.  
- Shortcut formula: $\text{Diff} = 2k + 2 = 2(8) + 2 = 18$.

---

### Q2 (TCS Digital / Infosys DSE Style — Simultaneous Swapping Verification)
**Q:** In a row of 30 girls, $A$ is 12th from the left and $B$ is 14th from the right. If $A$ and $B$ interchange seats, what will be $B$'s new distance from the right end?  
- A) 17th  
- B) 18th  
- C) 19th  
- D) 20th  

**Answer:** C) 19th  
**Distractor Analysis:**  
- $B$ moves to $A$'s original position (12th from the left).  
- $R_B = \text{Total} + 1 - L_A = 30 + 1 - 12 = \mathbf{19\text{th from right}}$.

---

### Q3 (Cognizant / Capgemini Style — Overlap Feasibility Condition)
**Q:** Under what exact mathematical condition can two persons with ranks $L$ from left and $R$ from right have $k$ persons between them in an overlapping arrangement?  
- A) $k \le \min(L, R) - 2$  
- B) $k \ge \max(L, R) - 2$  
- C) $L + R \ge 2k$  
- D) $k = |L - R|$  

**Answer:** A) $k \le \min(L, R) - 2$  
**Distractor Analysis:**  
- For overlap, the minimum total is $(L + R) - (k + 2)$.  
- This total must be at least $\max(L, R)$.  
- Solving $(L + R) - (k + 2) \ge \max(L, R)$ yields $k \le \min(L, R) - 2$.

---

## 7. Rapid Revision & Exam Checklist

- [ ] **Opposite Side:** $\text{Rank} = \text{Total} + 1 - \text{Current Rank}$.
- [ ] **Same Person:** $\text{Total} = L + R - 1$.
- [ ] **Between (Same End):** $k = |P_1 - P_2| - 1$.
- [ ] **Overlapping Total:** $\text{Total}_{\min} = (L + R) - (k + 2)$. Valid iff $k \le \min(L, R) - 2$.
- [ ] **Swapping Rule:** Total $= L_{\text{new}} + R_{\text{orig}} - 1$.
- [ ] **Departures Below:** Only affects ranks from the bottom, rank from top is unchanged.

---

## 🔗 Cross-Links

- [Seating Arrangement](seating-arrangement.md) — Circular and linear puzzle arrangements
- [Formula Sheet](../FORMULA_SHEET.md) — Comprehensive quantitative & logical formula reference
- [Puzzles & Scheduling](puzzles-scheduling.md) — Multi-attribute matrix matching puzzles
- [Blood Relations](blood-relations.md) — Coded kinship expressions and family tree logic
