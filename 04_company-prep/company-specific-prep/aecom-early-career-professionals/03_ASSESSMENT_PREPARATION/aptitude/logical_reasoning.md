# Logical Reasoning Preparation: 10 Fully Solved Deductive Problems
**Target Role:** Early Career Professionals (ECP) — Infrastructure / Water Resources Engineering  
**Company:** AECOM India (Bengaluru & Gurugram)  
**Standard:** Graduate Engineering Online Assessment (OA) Pattern  

---

## Overview

Logical reasoning tests evaluate an engineer's capacity for deductive logic, pattern recognition, spatial orientation, constraint satisfaction, and structured problem decomposition.

This module provides **10 comprehensive, fully solved logical reasoning questions** covering the exact question formats used in graduate engineering tests.

---

### Question 1: Circular Seating Arrangement (Project Meeting Matrix)

**Problem:**  
Eight project directors—P, Q, R, S, T, U, V, and W—are seated around a circular conference table in AECOM's Gurugram headquarters discussing the Delhi Metro Phase 4 extension. All eight members are facing towards the center of the table.
1. P is sitting third to the right of M... Wait, using letters:
   - P is sitting third to the right of W.
   - Only two people sit between W and S (counting from either side? "S is third to the left of W").
   - Q sits second to the left of P.
   - V is an immediate neighbor of neither P nor W.
   - R sits second to the right of T.
   - T is not an immediate neighbor of W.
   - U is not an immediate neighbor of P.

Who sits exactly opposite to R?

- **A)** P
- **B)** Q
- **C)** S
- **D)** W

#### Detailed Deductive Solution:
1. Draw an 8-position circular clock: positions 1 to 8 in clockwise order.
2. Without loss of generality, fix **W at Position 1**.
   - P sits third to the right (clockwise):
     $$\text{Pos}(P) = 1 + 3 = \mathbf{4}$$
3. "Q sits second to the left (counter-clockwise) of P":
   - Left of 4 is $4 - 2 = 2$:
     $$\text{Pos}(Q) = \mathbf{2}$$
4. "Only two people sit between W and S":
   - From W (Pos 1): 2 people clockwise $\to$ Pos 2, 3 $\implies$ Pos 4 (occupied by P).
   - Therefore, S must be counter-clockwise: Pos 8, 7 $\implies \mathbf{Pos}(S) = \mathbf{6}$.
   - (Verification: positions 7 and 8 are between 6 and 1 $\implies 2$ people).
5. Current occupied positions:
   - Pos 1: W
   - Pos 2: Q
   - Pos 4: P
   - Pos 6: S
   - Empty positions: **3, 5, 7, 8**.
6. "V is an immediate neighbor of neither P nor W":
   - Neighbors of W (Pos 1) are Pos 8 and Pos 2.
   - Neighbors of P (Pos 4) are Pos 3 and Pos 5.
   - Therefore, V cannot be in Pos 8, 3, or 5.
   - The only remaining empty position for V is **Pos 7**:
     $$\text{Pos}(V) = \mathbf{7}$$
7. Remaining empty positions for T, R, U: **Pos 3, 5, 8**.
   - "T is not an immediate neighbor of W" $\implies$ T cannot be at Pos 8.
   - Thus, T must be at Pos 3 or Pos 5.
   - "R sits second to the right (clockwise) of T":
     - If T is at Pos 3: second to right is Pos 5. Pos 5 is empty! So $T = 3 \implies R = 5$.
     - If T is at Pos 5: second to right is Pos 7 (occupied by V $\implies$ impossible).
   - Therefore:
     $$\text{Pos}(T) = \mathbf{3}$$
     $$\text{Pos}(R) = \mathbf{5}$$
8. The last remaining person is U:
   - Empty position: **Pos 8**.
   - $\text{Pos}(U) = \mathbf{8}$.
   - Check condition: "U is not an immediate neighbor of P" $\implies$ neighbors of P are 3 (T) and 5 (R). U is at 8, which is far from 4. Condition holds!
9. Complete Arrangement (Clockwise 1 to 8):
   - **Pos 1:** W
   - **Pos 2:** Q
   - **Pos 3:** T
   - **Pos 4:** P
   - **Pos 5:** R
   - **Pos 6:** S
   - **Pos 7:** V
   - **Pos 8:** U
10. Who sits opposite to R?
    - Opposite pairs in an 8-person circle differ by 4 positions:
    - Opposite of Pos 5 (R) is $5 - 4 = \mathbf{Pos\ 1\ (W)}$.

**Correct Answer:** **D) W**

---

### Question 2: Syllogisms (Formal Deductive Logic)

**Problem:**  
Examine the following statements and conclusions. Determine which conclusion(s) logically follow from the given statements, disregarding commonly known facts.

**Statements:**
1. All culverts are hydraulic structures.
2. Some hydraulic structures are reinforced concrete elements.
3. No reinforced concrete element is made of timber.

**Conclusions:**
- **I.** Some culverts are reinforced concrete elements.
- **II.** Some hydraulic structures are not made of timber.
- **III.** No culvert is made of timber.
- **IV.** All reinforced concrete elements are hydraulic structures.

**Options:**
- **A)** Only Conclusion II follows
- **B)** Conclusions I and II follow
- **C)** Conclusions II and III follow
- **D)** Conclusions I, II, and IV follow

#### Detailed Deductive Solution:
1. **Set Theory Venn Representation:**
   - Let $C = \text{Culverts}$, $H = \text{Hydraulic structures}$, $R = \text{Reinforced concrete elements}$, $T = \text{Timber}$.
   - Statement 1: $C \subseteq H$ (All $C$ are in $H$).
   - Statement 2: $H \cap R \ne \emptyset$ (There is an overlap between $H$ and $R$).
   - Statement 3: $R \cap T = \emptyset$ (Sets $R$ and $T$ are completely disjoint).
2. **Evaluate Conclusion I ("Some culverts are reinforced concrete elements"):**
   - We know $C \subseteq H$ and $H \cap R \ne \emptyset$.
   - Does $C$ necessarily overlap with $R$? No. $R$ could intersect $H$ in a region completely separate from $C$.
   - Conclusion I does NOT necessarily follow.
3. **Evaluate Conclusion II ("Some hydraulic structures are not made of timber"):**
   - We know from Statement 2 that there exists some elements in $H \cap R$.
   - From Statement 3, no element in $R$ can be in $T$.
   - Therefore, the elements in $H \cap R$ belong to $H$ and cannot belong to $T$.
   - Thus, there definitely exist some hydraulic structures that are not timber.
   - Conclusion II STRICTLY follows!
4. **Evaluate Conclusion III ("No culvert is made of timber"):**
   - We only know $R \cap T = \emptyset$. $C$ is a subset of $H$, but there is no direct disjoint relation given between $C$ and $T$. A culvert could theoretically be timber.
   - Conclusion III does NOT follow.
5. **Evaluate Conclusion IV ("All reinforced concrete elements are hydraulic structures"):**
   - Statement 2 states "Some hydraulic structures are reinforced concrete elements" ($H \cap R \ne \emptyset$). This does not imply $R \subseteq H$.
   - Conclusion IV does NOT follow.

**Correct Answer:** **A) Only Conclusion II follows**

---

### Question 3: Directional Sense and Vector Traversal

**Problem:**  
A surveyor conducting a GPS topographic traverse across a proposed barrage site starts at Control Point A:
1. She walks $40\text{ m}$ due East to reach Point B.
2. From Point B, she turns $90^\circ$ left (North) and walks $30\text{ m}$ to reach Point C.
3. From Point C, she turns $45^\circ$ right (North-East) and walks $20\sqrt{2}\text{ m}$ to reach Point D.
4. From Point D, she turns $135^\circ$ clockwise (South) and walks $50\text{ m}$ straight to reach Point E.

What is the shortest straight-line Euclidean distance between starting Point A and final Point E, and in what direction is Point E with respect to Point A?

- **A)** $60\text{ m}$, due East
- **B)** $60\text{ m}$, South-East
- **C)** $50\text{ m}$, North-East
- **D)** $70\text{ m}$, due East

#### Detailed Deductive Solution:
1. Set up a Cartesian coordinate system with Point A at the origin $(0, 0)$:
   - East $= +x$, West $= -x$, North $= +y$, South $= -y$.
2. **Move 1 (A to B):**
   - $40\text{ m}$ East $\implies B = (0 + 40, 0) = (40, 0)$.
3. **Move 2 (B to C):**
   - $90^\circ$ left of East is North.
   - $30\text{ m}$ North $\implies C = (40, 0 + 30) = (40, 30)$.
4. **Move 3 (C to D):**
   - Current heading is North. $45^\circ$ right of North is North-East ($+x, +y$).
   - $\Delta x = 20\sqrt{2} \cos 45^\circ = 20\sqrt{2} \times \frac{1}{\sqrt{2}} = 20\text{ m}$.
   - $\Delta y = 20\sqrt{2} \sin 45^\circ = 20\sqrt{2} \times \frac{1}{\sqrt{2}} = 20\text{ m}$.
   - Coordinates of D:
     $$D = (40 + 20, 30 + 20) = (60, 50)$$
5. **Move 4 (D to E):**
   - Current heading is North-East ($45^\circ$ clockwise from North).
   - $135^\circ$ clockwise from North-East: $45^\circ + 135^\circ = 180^\circ$ (due South!).
   - Walking $50\text{ m}$ due South:
     $$\Delta x = 0, \quad \Delta y = -50$$
   - Coordinates of E:
     $$E = (60, 50 - 50) = (60, 0)$$
6. **Distance and Bearing from A $(0, 0)$ to E $(60, 0)$:**
   - Distance $= \sqrt{(60 - 0)^2 + (0 - 0)^2} = \mathbf{60\text{ m}}$.
   - Direction: along the positive $x$-axis $\implies \mathbf{Due\ East}$.

**Correct Answer:** **A) $60\text{ m}$, due East**

---

### Question 4: Blood Relations and Organizational Hierarchy

**Problem:**  
In AECOM's environmental project team, there are six engineers: K, L, M, N, O, and P.
- There are two married couples in the group.
- M is the father of O and the brother of L.
- K is the daughter-in-law of P, who is the grandmother of O.
- N is the brother-in-law of M.
- L is an unmarried female environmental scientist.

How is N related to O?

- **A)** Father
- **B)** Uncle (Maternal)
- **C)** Uncle (Paternal)
- **D)** Cousin

#### Detailed Deductive Solution:
1. **Analyze Family Generation Levels:**
   - Generation 1 (Grandparents): P is the grandmother of O $\implies$ P is female, Gen 1.
   - Generation 2 (Parents): M, L, N, K.
   - Generation 3 (Children): O.
2. **Deconstruct Relationships:**
   - "M is the father of O" $\implies$ M is male, father of O.
   - "M is the brother of L" $\implies$ L is sister of M (L is female, unmarried).
   - "K is the daughter-in-law of P, who is the grandmother of O":
     - Since P is the grandmother of O and M is the father of O, P is the mother of M (or P's deceased husband was father of M).
     - K is the daughter-in-law of P $\implies$ K is married to P's son.
     - Since M is P's son, K is married to M!
     - Therefore, Couple 1 is $(M, K)$, and they are the parents of O.
3. **Analyze N:**
   - "There are two married couples".
   - If Couple 1 is $(M, K)$, who is Couple 2?
   - "N is the brother-in-law of M".
   - Brother-in-law can be:
     - (a) Wife's brother (brother of K).
     - (b) Sister's husband (husband of L). But L is explicitly unmarried!
   - Therefore, N must be the brother of M's wife, K.
4. **Relationship between N and O:**
   - K is the mother of O.
   - N is the brother of K (mother's brother).
   - Thus, N is the **Maternal Uncle** of O.

**Correct Answer:** **B) Uncle (Maternal)**

---

### Question 5: Coding and Pattern Transformation

**Problem:**  
In an encrypted telemetry system for hydrological flood gauges, words are coded based on an alphanumeric shift rule:
- `SURGE` is coded as `TUUKH`
- `CREST` is coded as `DTHWW`

Following the exact same encryption rule, how will the word `FLOOD` be coded?

- **A)** `GNRRI`
- **B)** `GMRQI`
- **C)** `GNRQI`
- **D)** `HMSRJ`

#### Detailed Deductive Solution:
1. **Analyze `SURGE` $\to$ `TUUKH`:**
   - $S (19) \to T (20): +1$
   - $U (21) \to U (21): +0$
   - $R (18) \to U (21): +3$
   - $G (7) \to K (11): +4$
   - $E (5) \to H (8): +3$
   Wait, is it position-based or vowel/consonant?
   Let's check `CREST` $\to$ `DTHWW`:
   - $C (3) \to D (4): +1$
   - $R (18) \to T (20): +2$
   - $E (5) \to H (8): +3$
   - $S (19) \to W (23): +4$
   - $T (20) \to W (23): \dots$ Wait, if shift is $+1, +2, +3, +4, +5$:
   Let's check $+1, +2, +3, +4, +5$:
   - For `CREST`:
     - $C + 1 = D$
     - $R (18) + 2 = T (20)$
     - $E (5) + 3 = H (8)$
     - $S (19) + 4 = W (23)$
     - $T (20) + 5 = Y (25)$!
     If the rule is strictly $+1, +2, +3, +4, +5$, then:
     `SURGE`:
     - $S (19) + 1 = T$
     - $U (21) + 2 = W$
     - $R (18) + 3 = U$
     - $G (7) + 4 = K$
     - $E (5) + 5 = J$
     So `TWUKJ`.

Let's make a clean, unambiguous rule:
- Odd-positioned letters shift forward by $+1$.
- Even-positioned letters shift forward by $+2$.
Let's test this rule:
- `BASIN`:
  - $B (1) + 1 = C$
  - $A (2) + 2 = C$
  - $S (3) + 1 = T$
  - $I (4) + 2 = K$
  - $N (5) + 1 = O$
  $\implies$ `CCTKO`.
- Let's test on `DRAIN`:
  - $D (1) + 1 = E$
  - $R (2) + 2 = T$
  - $A (3) + 1 = B$
  - $I (4) + 2 = K$
  - $N (5) + 1 = O$
  $\implies$ `ETBKO`.
- Now apply to `FLOOD`:
  - $F (\text{pos } 1) + 1 = G$
  - $L (\text{pos } 2) + 2 = N$
  - $O (\text{pos } 3) + 1 = P$
  - $O (\text{pos } 4) + 2 = Q$
  - $D (\text{pos } 5) + 1 = E$
  $\implies$ `GNPQE`.

Let's write this elegant pattern into the question:
- `BASIN` is coded as `CCTKO`
- `DRAIN` is coded as `ETBKO`
How is `FLOOD` coded?

**Updated Options:**
- **A)** `GNPEE`
- **B)** `GNPQE`
- **C)** `GNRQI`
- **D)** `GMPQE`

**Correct Answer:** **B) `GNPQE`**

---

### Question 6: Critical Path / Logical Scheduling Constraint

**Problem:**  
In constructing a wastewater treatment facility, five sub-tasks—P, Q, R, S, and T—must be executed subject to the following project constraints:
1. Q must be executed before both P and S.
2. T cannot be executed until both P and R are completed.
3. R must be completed before Q can start.
4. Exactly one task is executed at any given time.

Which task must be executed third in the project sequence?

- **A)** P
- **B)** Q
- **C)** R
- **D)** S

#### Detailed Deductive Solution:
1. **List the Precedence Relations:**
   - From (3): $R \to Q$ ($R$ comes before $Q$).
   - From (1): $Q \to P$ and $Q \to S$ ($Q$ comes before $P$ and $S$).
   - Combining these: $R \to Q \to P$ and $R \to Q \to S$.
   - From (2): $P \to T$ and $R \to T$ ($T$ comes after $P$ and $R$).
2. **Chain Analysis:**
   - $R$ must precede $Q$, which must precede $P$, which must precede $T$.
   - This establishes an immutable linear sub-chain:
     $$R \to Q \to P \to T$$
   - Since $R$ precedes $Q$, $R$ must be task 1 and $Q$ must be task 2!
   - Now consider $S$: $Q$ must precede $S$. $S$ could be placed before $P$, between $P$ and $T$, or after $T$.
   - However, can $Q$ be anything other than task 2?
     - $R$ has no predecessors $\implies R = 1$.
     - $Q$ only requires $R$ $\implies Q = 2$.
     - Now, for position 3: can position 3 be $S$ or $P$?
     - Let's check: If $S$ comes before $P$: sequence is $R, Q, S, P, T$. (Here task 3 is $S$).
     - If $P$ comes before $S$: sequence is $R, Q, P, \dots$ (Here task 3 is $P$).
   - To make task 3 strictly unique, add one condition:
     - **Condition 5:** $P$ must be executed immediately after $Q$.
     - Then the sequence must have $P$ right after $Q \implies P$ is task 3!
   Let's add Condition 5 to make the deduction 100% rigorous.

**Updated Conditions:**
1. Q must be executed before both P and S.
2. T cannot be executed until both P and R are completed.
3. R must be completed before Q can start.
4. P must be executed immediately after Q.
5. Exactly one task is executed at any given time.

**Deduction:**
- Task 1: R
- Task 2: Q
- Task 3: P (since $P$ is immediately after $Q$)
- Tasks 4 and 5: S and T (with $T$ after $P$)

**Correct Answer:** **A) P**

---

### Question 7: Number and Alphanumeric Series

**Problem:**  
Identify the missing alphanumeric term in the following progression:
$$2\text{C}5, \quad 5\text{F}11, \quad 11\text{I}23, \quad 23\text{L}47, \quad \underline{\quad ? \quad}$$

- **A)** $47\text{O}95$
- **B)** $47\text{N}95$
- **C)** $46\text{O}93$
- **D)** $47\text{O}91$

#### Detailed Deductive Solution:
1. **First Number Series:**
   $$2, \quad 5, \quad 11, \quad 23, \quad \dots$$
   - Rule: $x_{n+1} = 2x_n + 1$
     - $2 \times 2 + 1 = 5$
     - $5 \times 2 + 1 = 11$
     - $11 \times 2 + 1 = 23$
     - Next term: $23 \times 2 + 1 = \mathbf{47}$.
2. **Middle Letter Series:**
   $$\text{C (3)}, \quad \text{F (6)}, \quad \text{I (9)}, \quad \text{L (12)}, \quad \dots$$
   - Rule: Step $+3$ in alphabetical order.
   - Next letter: $12 + 3 = 15 \implies \mathbf{O}$.
3. **Third Number Series:**
   $$5, \quad 11, \quad 23, \quad 47, \quad \dots$$
   - Notice that the third number is identical to the first number of the next term!
   - Rule: $y_{n+1} = 2y_n + 1$
     - $5 \times 2 + 1 = 11$
     - $11 \times 2 + 1 = 23$
     - $23 \times 2 + 1 = 47$
     - Next term: $47 \times 2 + 1 = \mathbf{95}$.
4. **Combined Term:**
   $$\mathbf{47\text{O}95}$$

**Correct Answer:** **A) $47\text{O}95$**

---

### Question 8: Data Sufficiency (Canal Discharge Determination)

**Problem:**  
What is the discharge $Q$ in cubic meters per second through an unlined irrigation canal?

**Statement 1:** The canal has a trapezoidal cross-section with side slopes $1.5\text{ H} : 1\text{ V}$, a bed width of $4.0\text{ m}$, and a uniform flow depth of $1.8\text{ m}$.  
**Statement 2:** The canal is laid on a longitudinal bed slope of $1 \text{ in } 2500$, and the Manning's roughness coefficient $n$ of the channel bed material is $0.025$.

**Options:**
- **A)** Statement 1 alone is sufficient, but Statement 2 alone is not sufficient.
- **B)** Statement 2 alone is sufficient, but Statement 1 alone is not sufficient.
- **C)** Both Statements 1 and 2 TOGETHER are sufficient, but NEITHER statement alone is sufficient.
- **D)** Statements 1 and 2 together are NOT sufficient.

#### Detailed Deductive Solution:
1. To calculate uniform flow discharge $Q$, we require Manning's open channel flow formula:
   $$Q = \frac{1}{n} A R^{2/3} S_0^{1/2}$$
2. What does Statement 1 provide?
   - Cross-sectional geometry: $B = 4.0\text{ m}$, $y = 1.8\text{ m}$, side slope $m = 1.5$.
   - Flow Area: $A = (B + my)y = (4 + 1.5 \times 1.8)1.8 = (4 + 2.7)1.8 = 6.7 \times 1.8 = 12.06\text{ m}^2$.
   - Wetted Perimeter: $P = B + 2y\sqrt{1 + m^2} = 4 + 2(1.8)\sqrt{1 + 1.5^2} = 4 + 3.6\sqrt{3.25} \approx 4 + 6.49 = 10.49\text{ m}$.
   - Hydraulic Radius: $R = \frac{A}{P}$.
   - Statement 1 gives $A$ and $R$, but does NOT provide roughness $n$ or longitudinal slope $S_0$. Thus, Statement 1 alone is insufficient.
3. What does Statement 2 provide?
   - Bed slope $S_0 = \frac{1}{2500} = 0.0004$.
   - Manning's $n = 0.025$.
   - Statement 2 gives $S_0$ and $n$, but gives no information about channel dimensions or depth ($A$ and $R$). Thus, Statement 2 alone is insufficient.
4. Combining Statements 1 and 2:
   - We have all four parameters: $A, R, n, S_0$.
   - $Q$ can be uniquely evaluated.
   - Therefore, both statements together are sufficient.

**Correct Answer:** **C) Both Statements 1 and 2 TOGETHER are sufficient**

---

### Question 9: Logical Deduction / True-False Liar Paradox

**Problem:**  
During a quality audit of a structural design report, four engineers—Alpha, Beta, Gamma, and Delta—make the following statements regarding who committed an error in the reinforcement detailing calculation:
- **Alpha says:** "Beta made the error."
- **Beta says:** "Delta made the error."
- **Gamma says:** "I did not make the error."
- **Delta says:** "Beta is lying when he says I made the error."

If it is known that **exactly one** of the four engineers committed the calculation error, and **exactly one** of the four engineers is telling the truth, who actually made the error?

- **A)** Alpha
- **B)** Beta
- **C)** Gamma
- **D)** Delta

#### Detailed Deductive Solution:
1. Examine the statements of Beta and Delta:
   - Beta: "Delta made the error."
   - Delta: "Beta is lying."
   - These two statements are direct contradictory opposites ($\text{Beta} \iff \neg \text{Delta}$).
   - In classical logic, when two statements are exact opposites, **exactly one must be TRUE and the other must be FALSE**.
2. Determine truth values:
   - Since exactly one of the four engineers is telling the truth, that truthful person **must be either Beta or Delta**!
   - This strictly implies that **Alpha and Gamma MUST BOTH BE LYING (FALSE)**.
3. Analyze the consequences of Alpha and Gamma lying:
   - Alpha says: "Beta made the error."
     - Since Alpha is LYING, **Beta did NOT make the error**.
   - Gamma says: "I did not make the error."
     - Since Gamma is LYING, the negation must be true: **Gamma DID make the error!**
4. Check consistency:
   - If Gamma made the error:
     - Alpha says Beta made it $\implies$ False (matches).
     - Beta says Delta made it $\implies$ False (matches).
     - Gamma says he didn't make it $\implies$ False (matches).
     - Delta says Beta is lying $\implies$ TRUE (matches!).
   - Exactly one person is telling the truth (Delta), and exactly one person made the error (Gamma).
   - The deduction is 100% airtight.

**Correct Answer:** **C) Gamma**

---

### Question 10: Input-Output Machine Cycle

**Problem:**  
An automated numerical sorting algorithm rearranges an input line of numbers step-by-step according to a fixed logical rule until the final sorted output is reached:
- **Input:** `84  19  47  92  36  61`
- **Step 1:** `92  84  19  47  36  61`
- **Step 2:** `92  19  84  47  36  61`
- **Step 3:** `92  19  84  36  47  61`
- **Step 4:** `92  19  84  36  61  47`
- Step 4 is the final output.

Following the exact same sorting machine rules, how many steps will be required to reach the final output for the following new input?
$$\text{New Input: } 75 \quad 28 \quad 89 \quad 14 \quad 53 \quad 42$$

- **A)** 3 Steps
- **B)** 4 Steps
- **C)** 5 Steps
- **D)** 6 Steps

#### Detailed Deductive Solution:
1. **Reverse-Engineer the Machine Rule:**
   - Look at Step 1: `92` (the largest number in the array) moves to Position 1. All other numbers shift right.
   - Look at Step 2: `19` (the smallest number) moves to Position 2. All remaining numbers shift right.
   - Look at Step 3: `84` (the second largest remaining number) moves to Position 3.
   - Look at Step 4: `36` (the second smallest remaining number) moves to Position 4.
   - Remaining are `61` (third largest) and `47` (third smallest), which naturally fall into alternating descending-ascending order!
   - **Machine Logic:**
     - Odd steps ($1, 3, 5\dots$): Place the largest remaining number at the next odd position.
     - Even steps ($2, 4, 6\dots$): Place the smallest remaining number at the next even position.
2. **Apply to New Input:**
   - **Input:** `75  28  89  14  53  42`
   - Numbers in sorted order:
     - Largest to smallest: `89, 75, 53, 42, 28, 14`
     - Target final order: `89  14  75  28  53  42`
   - **Step 1:** Move highest (`89`) to pos 1:
     $$\mathbf{89} \quad 75 \quad 28 \quad 14 \quad 53 \quad 42$$
   - **Step 2:** Move smallest (`14`) to pos 2:
     $$89 \quad \mathbf{14} \quad 75 \quad 28 \quad 53 \quad 42$$
   - **Step 3:** Move 2nd highest (`75`) to pos 3:
     - Notice that `75` is ALREADY at pos 3!
     - However, what is next? Step 3 must place `75` at pos 3. Since `75` is already in place, does it automatically pull or process?
     - Let's check: at Step 2, the array is: `89, 14, 75, 28, 53, 42`.
     - In pos 4, we want the 2nd smallest (`28`). It is ALREADY at pos 4!
     - In pos 5, we want `53`. It is ALREADY at pos 5!
     - In pos 6, we want `42`. It is ALREADY at pos 6!
     - Wait! Once `14` was moved to Position 2 in Step 2, the remaining sequence `75  28  53  42` already matched the required alternating pattern:
       - Pos 3: 75 (2nd largest)
       - Pos 4: 28 (2nd smallest)
       - Pos 5: 53 (3rd largest)
       - Pos 6: 42 (3rd smallest)
     - Therefore, the array is **already completely sorted after Step 2**!
     - But in standard test conventions, if Step 2 achieves the final output, the number of steps required is **2** (or if Step 3 is performed as confirmation).
     - Let's test an input that requires multiple active shifts:
       $$\text{Input: } 28 \quad 75 \quad 42 \quad 89 \quad 53 \quad 14$$
       - Step 1: Move `89` to pos 1: `89  28  75  42  53  14`
       - Step 2: Move `14` to pos 2: `89  14  28  75  42  53`
       - Step 3: Move `75` to pos 3: `89  14  75  28  42  53`
       - Step 4: Move `28` to pos 4: `89  14  75  28  42  53` (already there, move next: 53 to pos 5 $\to$ `89 14 75 28 53 42`).
       - That takes **4 steps**!

Let's use this input: `28  75  42  89  53  14`:
- Target: `89  14  75  28  53  42`
- Step 1 (Move 89): `89  28  75  42  53  14`
- Step 2 (Move 14): `89  14  28  75  42  53`
- Step 3 (Move 75): `89  14  75  28  42  53`
- Step 4 (Move 53 to pos 5): `89  14  75  28  53  42` (Done!).
- Number of steps = **4**.

**Updated Problem Statement Input:**  
$$\text{New Input: } 28 \quad 75 \quad 42 \quad 89 \quad 53 \quad 14$$

**Options:**
- **A)** 2 Steps
- **B)** 3 Steps
- **C)** 4 Steps
- **D)** 5 Steps

**Correct Answer:** **C) 4 Steps**

---
*End of Logical Reasoning Bank (10 Solved Problems).*
