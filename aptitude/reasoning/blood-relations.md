# Blood Relations

> **Priority:** P1 · **Role relevance:** High (Universal across Core, IT, Analytics, Consulting & Banking)  
> **Difficulty range:** Foundation → Super-Expert · **Target speed:** 30 sec (Direct) – 90–120 sec (Complex / Multi-Constraint / Hybrid)

---

## 1. Family Tree Diagramming Conventions

Drawing a standardized visual family tree removes ambiguity and prevents working-memory overload during high-pressure placement tests.

```
       [Grandfather] = (Grandmother)          <-- Generation +2
             |
       +-----+-----------------+
       |                       |
    [Father] = (Mother)     [Uncle]            <-- Generation +1
       |
  +----+----+
  |         |
[You] --- (Sister)          [Cousin]           <-- Generation 0
  |
[Son] --- (Daughter)                           <-- Generation -1
```

| Symbol | Representation | Example |
|:------:|:---------------|:--------|
| `[ ]` or `+` | Male | `[A]` is a male |
| `( )` or `-` | Female | `(B)` is a female |
| `=` or `↔` | Married Couple (Spouses) | `[A] = (B)` (A is husband, B is wife) |
| `—` | Siblings (Brother/Sister) | `[A] — (C)` (A is brother of C) |
| `│` | Vertical generation link | Older generation at the top, younger below |
| `?` | Gender unknown | `?D?` (Never assume gender from personal names) |

### Generational Distance Chart

| Generation Gap | Relations |
|:--------------:|:----------|
| **+2** | Grandfather, Grandmother, Maternal Grandfather, Maternal Grandmother |
| **+1** | Father, Mother, Uncle (paternal/maternal), Aunt (paternal/maternal), Father-in-law, Mother-in-law |
| **0 (Same)** | Self, Brother, Sister, Cousin, Husband, Wife, Brother-in-law, Sister-in-law |
| **-1** | Son, Daughter, Nephew, Niece, Son-in-law, Daughter-in-law |
| **-2** | Grandson, Granddaughter |

---

## 2. Terminology & Relationship Dictionary

| English Term | Precise Relationship |
|:-------------|:---------------------|
| **Maternal Uncle** | Mother's brother |
| **Paternal Uncle** | Father's brother |
| **Maternal Aunt** | Mother's sister (or wife of maternal uncle) |
| **Paternal Aunt** | Father's sister (or wife of paternal uncle) |
| **Nephew** | Brother's son OR Sister's son |
| **Niece** | Brother's daughter OR Sister's daughter |
| **Cousin** | Child of paternal or maternal uncle/aunt (Never say "cousin brother/sister") |
| **Brother-in-law** | Spouse's brother OR Sister's husband OR Husband of spouse's sister |
| **Sister-in-law** | Spouse's sister OR Brother's wife OR Wife of spouse's brother |
| **Father-in-law** | Spouse's father |
| **Mother-in-law** | Spouse's mother |
| **Son-in-law** | Daughter's husband |
| **Daughter-in-law** | Son's wife |

---

## 3. High-Speed Shortcut Methods

### 3.1 The Generation Score Method (for Coded Relations)
Assign an integer generation value to each operator:
- Parent / Father / Mother / Uncle / Aunt $\to \mathbf{+1}$
- Brother / Sister / Husband / Wife / Cousin $\to \mathbf{0}$
- Son / Daughter / Nephew / Niece $\to \mathbf{-1}$
- Grandfather / Grandmother $\to \mathbf{+2}$
- Grandson / Granddaughter $\to \mathbf{-2}$

**Application:** If asked *"Which expression shows $P$ is the Uncle of $Q$?"*, the target generation of $P$ relative to $Q$ must be $\mathbf{+1}$. Sum the operator values from $P$ to $Q$. Any option whose net sum $\ne +1$ is eliminated instantly without drawing the family tree!

### 3.2 The Gender Elimination Technique
If the target question asks for a female relation (e.g., "$A$ is the aunt/mother/daughter of $B$"):
1. Identify the gender of $A$ in each option.
2. In coded strings, the gender of person $A$ is determined by the operator immediately following $A$ (e.g., in $A \times B$, if $\times$ means "is sister", $A$ is female).
3. **The End-Person Trap:** If $A$ is at the very end of the expression (e.g., $C + D \times A$), $A$'s gender is usually **indeterminate** unless a spouse relation precedes $A$.
4. Eliminate options where $A$ is male or gender cannot be determined.

### 3.3 The Backward Reading Trick (for Pointing Problems)
Break narrative sentences from the possessive pronoun **"my"** or **"his/her"** and evaluate backwards:
- Sentence: *"She is the mother of the only daughter of my wife's father-in-law."*
  1. "My wife's father-in-law" = My father (if speaker is male).
  2. "Only daughter of my father" = My sister.
  3. "Mother of my sister" = My mother.
  4. "She is [my mother]" $\to$ Result: **Mother**.

### 3.4 Disambiguating Relative Pronouns ("Who", "Whose", "And")
- **"A is the father of B, who is the husband of C"**: The relative pronoun **"who"** connects strictly to the immediately preceding noun ($B$).
- **"A is the father of B and is the husband of C"**: The conjunction **"and"** refers to the primary subject ($A$).
- **"A's father B met C whose sister D is..."**: **"whose"** refers to the nearest subject ($C$).

### 3.5 The Graph Pruning Technique (for 10+ Link Puzzles)
In massive relational chains, 60% of the nodes are often **distractors** designed to consume time.
- **Rule:** Identify the target pair ($X$ and $Y$). Identify the common link or family junction between them. Prune all unreferenced branches immediately.

### 3.6 Parity & Tree-Collapse Principle
When multiple candidate trees can be constructed from a dense puzzle prompt:
1. Count the total stated married couples and male/female counts.
2. Check single-parent constraints ("No single parent has a child").
3. Any candidate tree violating parity or single-parent constraints is discarded, leaving a single unique configuration.

---

## 4. Advanced Placement Reasoning Strategies

| Level | Link Count | Key Challenge | Target Approach |
|:------|:----------:|:--------------|:----------------|
| **Level 1: Foundation** | 2–3 links | Direct narrative pointers & single-operator baseline | Direct backward reading |
| **Level 2: Intermediate** | 4–5 links | Basic coded relations & 2-generation family logic | Simple tree sketching |
| **Level 3: Hard** | 6–8 links | 3 generations, mixed in-laws, gender-count constraints | Forward tree diagramming |
| **Level 4: Very Hard** | 8–12 links | Dual-family marriages, branch crossover, great-grandparent span | Node-by-node unification |
| **Level 5: Expert** | 12–16 links | 5+ nested operators, distractor networks, indirect parentage | Generation sum + Gender filter + Pruning |
| **Level 6: Trap / Inference** | Variable | "Only", "exactly", gender indeterminacy, reciprocal traps | Strict verification of edge cases |
| **Level 7: Extreme Caselet** | Paragraph | Multi-person paragraph $\to$ 3–4 questions (Hybrid Seating/Direction) | Master relational grid before answering |
| **Level 8: Super-Expert** | 15–22 links | Multi-marriage in-laws, incomplete genders, dual-tree parity collapse | Global constraint constraint-satisfaction |

---

## 5. Worked Examples

### Example 1: Pointing / Narrative (Medium)
**Problem:** Pointing to a photograph of a boy, Suresh said, *"He is the son of the only son of my mother."* How is Suresh related to the boy?  
**Step-by-step Solution:**
1. Locate anchor: *"my mother"* $\to$ Suresh's mother.
2. *"Only son of my mother"* $\to$ Suresh himself (since Suresh is male speaking of his mother's only son).
3. *"Son of [Suresh]"* $\to$ The boy is Suresh's son.
4. Question asks: *How is Suresh related to the boy?*
5. Suresh is the **Father**.

### Example 2: Coded Relations with Generation & Gender Filtering (Hard)
**Problem:** Given:
- $P + Q \implies P$ is the father of $Q$ (Gen +1, $P$ male)
- $P - Q \implies P$ is the sister of $Q$ (Gen 0, $P$ female)
- $P \times Q \implies P$ is the brother of $Q$ (Gen 0, $P$ male)
- $P \div Q \implies P$ is the mother of $Q$ (Gen +1, $P$ female)

Which expression indicates that **"$M$ is the maternal uncle of $N$"**?  
- A) $M \times R + N$  
- B) $M \times R \div N$  
- C) `M - R ÷ N`  
- D) $M + R \times N$  

**Step-by-step Solution:**
1. **Target Analysis:** Maternal uncle means $M$ is **male**, generation of $M$ relative to $N$ is $\mathbf{+1}$, through $N$'s mother.
2. **Gender Check:**
   - In C: `M - R` → M is female $\to$ **Eliminated**.
   - In D: $M + R \implies M$ is father, but $R \times N$ makes $R$ brother $\to M$ is father of $N \to$ **Eliminated**.
3. **Generation & Path Check:**
   - In A: $M \times R$ ($M$ brother of $R$) $\to R + N$ ($R$ father of $N$) $\implies M$ is paternal uncle $\to$ **Eliminated**.
   - In B: `M × R` (M brother of R) → `R ÷ N` (R mother of N) → M is brother of N's mother → **Maternal Uncle**!
4. **Answer:** **B) $M \times R \div N$**.

### Example 3: The 14-Link Graph Pruning Master Example (Expert)
**Problem:** $A$ is the only daughter of $B$. $B$ is the elder brother of $C$. $C$ is married to $D$. $D$'s only sister $E$ is married to $F$. $F$'s maternal uncle $G$ has two children, $H$ and $I$. $H$'s daughter $J$ is married to $K$. $K$'s father is $L$, who is the only son of $M$. $M$'s daughter $N$ is the mother of $A$. How is $K$ related to $B$?  
**Step-by-step Solution (Pruning Method):**
1. Question asks for the relationship between **$K$** and **$B$**.
2. Locate statements containing $B$:
   - "$A$ is the only daughter of $B$." $\to B$ is the father of $A$ (or parent).
   - "$M$'s daughter $N$ is the mother of $A$." $\to N$ is the mother of $A$.
   - Since $B$ is the father and $N$ is the mother of $A$, **$B$ and $N$ are a married couple ($[B] = (N)$)**!
3. Locate statements connecting to $N$ and $K$:
   - "$K$'s father is $L$, who is the only son of $M$."
   - "$M$'s daughter $N$..."
   - Since $M$ has only one son ($L$) and a daughter ($N$), **$L$ and $N$ are brother and sister**!
   - $L$ is the brother of $N$. Since $B$ is married to $N$, **$L$ is the brother-in-law of $B$**.
4. Locate $K$:
   - "$K$'s father is $L$."
   - $K$ is the child of $B$'s brother-in-law (wife's brother's child).
   - Notice: The entire chain involving $C, D, E, F, G, H, I, J$ is a **pure distractor branch**!
5. Conclusion: $K$ is the child of $B$'s brother-in-law $\implies K$ is $B$'s **Nephew** (specifically, nephew by marriage / wife's nephew).

---

## 6. Comprehensive Practice Set (46 Placement Questions)

### Level 1: Foundation (Q1–Q5)

**Q1.** Pointing to a man in a photograph, a woman says, *"His mother is the only daughter of my mother."* How is the woman related to the man?  
- A) Mother  
- B) Sister  
- C) Daughter  
- D) Grandmother  

**Q2.** $A$ is the father of $B$, but $B$ is not the son of $A$. How is $B$ related to $A$?  
- A) Daughter  
- B) Son-in-law  
- C) Niece  
- D) Sister  

**Q3.** Introducing a man, a woman said, *"He is the only son of my mother's mother."* How is the woman related to the man?  
- A) Aunt  
- B) Niece  
- C) Sister  
- D) Mother  

**Q4.** If $P$ is the brother of $Q$, $Q$ is the sister of $R$, and $R$ is the father of $S$, how is $P$ related to $S$?  
- A) Father  
- B) Brother  
- C) Paternal Uncle  
- D) Nephew  

**Q5.** Pointing to a gentleman, Deepak said, *"His only brother is the father of my daughter's father."* How is the gentleman related to Deepak?  
- A) Grandfather  
- B) Father  
- C) Paternal Uncle  
- D) Brother  

---

### Level 2: Intermediate (Q6–Q10)

**Q6.** A man said to a lady, *"Your mother's husband's sister is my aunt."* How is the lady related to the man?  
- A) Daughter  
- B) Sister  
- C) Mother  
- D) Aunt  

**Q7.** If $A + B$ means "$A$ is the son of $B$"; $A - B$ means "$A$ is the wife of $B$"; $A \times B$ means "$A$ is the brother of $B$"; $A \div B$ means "$A$ is the mother of $B$". What does $P + R - Q$ mean?  
- A) $Q$ is the father of $P$  
- B) $Q$ is the son of $P$  
- C) $Q$ is the uncle of $P$  
- D) $P$ is the brother of $Q$  

**Q8.** Pointing to a photograph, Anita said, *"He is the son of the only son of my grandfather."* If Anita's grandfather has only one child, how is the person in the photograph related to Anita?  
- A) Brother  
- B) Uncle  
- C) Cousin  
- D) Father  

**Q9.** In a family of 6 members ($P, Q, R, S, T, U$): $P$ and $Q$ are married, with $P$ being male. $S$ is the only son of $R$, who is the brother of $P$. $T$ is the sister of $S$. $Q$ is the daughter-in-law of $U$, whose husband has died. How is $U$ related to $P$?  
- A) Mother  
- B) Sister  
- C) Mother-in-law  
- D) Aunt  

**Q10.** If `X @ Y` means "X is sister of Y"; `X # Y` means "X is mother of Y"; `X $ Y` means "X is father of Y". Which of the following means **"M is the niece of T"**?  
- A) `T @ R $ M @ K`  
- B) `M @ K # T $ R`  
- C) `T $ R @ M @ K`  
- D) `R $ T @ M @ K`  

---

### Level 3: Hard — 6–8 Links & Multi-Generation (Q11–Q15)

**Q11.** Read the relations:
- `P ★ Q` → P is the father of Q
- `P Δ Q` → P is the daughter of Q
- `P □ Q` → P is the sister of Q
- `P ○ Q` → P is the husband of Q

Which expression indicates that **"$J$ is the paternal grandfather of $T$"**?  
- A) `J ★ K ○ L ★ T`  
- B) `J ★ K ★ T □ M`  
- C) `J ○ K Δ L ★ T`  
- D) `J ★ K □ L ★ T`  

**Q12.** Pointing to a photograph of a woman, a man says, *"She is the grandmother of my son's only brother's daughter."* How is the woman in the photograph related to the man?  
- A) Wife  
- B) Mother  
- C) Sister  
- D) Mother-in-law  

**Q13.** Seven members ($A, B, C, D, E, F, G$) belong to three generations. There are two married couples:
- $B$ is an engineer and father of $E$.
- $F$ is grandfather of $C$ and is a doctor.
- $C$ is a student and $D$ is grandmother of $C$.
- $E$ is an unmarried lecturer.
- $A$ is the mother of $C$.

How is $A$ related to $B$?  
- A) Daughter  
- B) Wife  
- C) Sister-in-law  
- D) Mother  

**Q14.** If $A + B$ means "$A$ is father of $B$"; $A - B$ means "$A$ is mother of $B$"; $A \times B$ means "$A$ is brother of $B$"; $A \div B$ means "$A$ is sister of $B$". In $P + Q \times R - S \div T$, how is $P$ related to $T$?  
- A) Paternal Grandfather  
- B) Maternal Grandfather  
- C) Uncle  
- D) Father  

**Q15.** A family consists of 6 members: $P, Q, R, X, Y, Z$.
- $Q$ is the son of $R$, but $R$ is not the mother of $Q$.
- $P$ and $R$ are a married couple.
- $Y$ is the brother of $R$.
- $X$ is the daughter of $P$.
- $Z$ is the brother of $P$.

How many female members are there in the family?  
- A) 1  
- B) 2  
- C) 3  
- D) 4  

---

### Level 4: Very Hard — 8–12 Links & Dual Branches (Q16–Q20)

**Q16.** In a joint family:
- $M$ is the father-in-law of $N$, who is the sister-in-law of $P$.
- $P$ is the unmarried paternal aunt of $Q$.
- $R$ is the brother of $M$.
- $S$ is the daughter-in-law of $R$ and has no siblings.
- $T$ is the only nephew of $P$.
- $M$ has only two children: a son and a daughter.
- No child in the family is born out of wedlock, and no divorces have taken place.

How is $S$ related to $Q$?  
- A) Paternal Aunt  
- B) Mother  
- C) Sister-in-law  
- D) Paternal Aunt-in-law / Cousin's mother  

**Q17.** $A$ is the paternal grandfather of $B$. $B$ is the brother of $C$. $C$ is married to $D$, whose mother $E$ is the only sister of $F$. $F$ is the brother-in-law of $G$, who has no siblings. $A$ has only one son, $H$. If $H$ is married to $I$, how is $D$ related to $H$?  
- A) Son-in-law or Daughter-in-law  
- B) Niece  
- C) Nephew  
- D) Daughter  

**Q18.** $P$ is the mother of $K$. $K$ is the sister of $S$. $S$ is married to $T$, who is the only son of $R$. $R$ is the husband of $U$. $V$ is the only daughter of $T$. $W$ is the brother of $U$. $X$ is the father of $P$. How is $V$ related to $P$?  
- A) Daughter  
- B) Granddaughter  
- C) Sister  
- D) Niece  

**Q19.** Six persons $U, V, W, X, Y, Z$ are in a family:
- There are two married couples.
- $X$ is the sister of $Z$, who is the husband of $Y$.
- $U$ is the father of $X$.
- $W$ is the mother of $X$.
- $V$ is the son of $Z$.

How is $Y$ related to $U$?  
- A) Daughter  
- B) Daughter-in-law  
- C) Sister-in-law  
- D) Niece  

**Q20.** $K$ is the brother of $T$. $M$ is the mother of $K$. $W$ is the sister of $M$. $R$ is the father of $W$. $Z$ is the sister-in-law of $K$. $T$ has only one brother. $S$ is the daughter of $T$. How is $R$ related to $S$?  
- A) Grandfather  
- B) Great-grandfather  
- C) Paternal Uncle  
- D) Father-in-law  

---

### Level 5: Expert & Code-Expert (Q21–Q26)

**Q21.** If:
- `A & B` → A is the wife of B
- `A # B` → A is the father of B
- `A @ B` → A is the son of B
- `A % B` → A is the sister of B
- `A ★ B` → A is the brother of B

In the expression `P @ Q # R & S # T % U`, how is P related to T?  
- A) Paternal Uncle  
- B) Maternal Uncle  
- C) Brother  
- D) Father  

**Q22.** Using the codes from Q21, which of the following expressions establishes that **"D is the paternal aunt of H"**?  
- A) `D % E # H @ K`  
- B) `D & E # H ★ K`  
- C) `E # D % F # H`  
- D) `D % E @ F # H`  

**Q23.** In a coded kinship system:
- `P(1)Q` → P is the father of Q
- `P(2)Q` → P is the mother of Q
- `P(3)Q` → P is the sister of Q
- `P(4)Q` → P is the brother of Q
- `P(5)Q` → P is the spouse of Q

Which of the following expressions represents that **"$A$ is the son-in-law of $F$"**?  
- A) `A(5)B(3)C(2)F`  
- B) `A(5)B(4)C(1)F`  
- C) `A(5)B(3)C(2)E(5)F` where E is male  
- D) `A(5)B(3)C` and `B(2)F`  

**Q24.** Consider the statement: *"Pointing to a woman in a painting, Vikram said: 'Her only brother's only nephew's paternal grandfather is my father, who has only one daughter.' "* If Vikram has only one brother, how is the woman in the painting related to Vikram?  
- A) Mother  
- B) Sister  
- C) Paternal Aunt  
- D) Wife  

**Q25.** If:
- `A ÷ B` means A is the father of B
- `A × B` means A is the sister of B
- `A + B` means A is the brother of B
- `A - B` means A is the mother of B

Which of the following expressions shows that **"$K$ is the nephew of $T$"**?  
- A) `T × M ÷ K + N`  
- B) `T + M - K × N`  
- C) `K + N ÷ M × T`  
- D) `T ÷ M + K - N`  

**Q26.** In a business family of eight members across three generations:
- $A$ is the CEO and father of two children: $B$ and $C$.
- $B$ is married to $D$, an architect.
- $D$ is the daughter-in-law of $E$, who is the CFO.
- $C$ is unmarried and is the maternal uncle of $F$.
- $G$ is the sister of $F$, and both are children of $B$.
- $H$ is the father of $D$.

How is $H$ related to $B$?  
- A) Uncle  
- B) Father-in-law  
- C) Brother-in-law  
- D) Son-in-law  

---

### Level 6: Trap, Inference & Indeterminacy Sets (Q27–Q31)

**Q27 (The "Only Daughter" Ambiguity).** A person said, *"That girl is the daughter of the only daughter-in-law of the father of my only sister."* If the speaker is a female, who is the girl to the speaker?  
- A) Daughter  
- B) Niece  
- C) Sister  
- D) Sister-in-law  

**Q28 (Pronoun Reference Trap).** $A$ is the father-in-law of $B$ who is the brother-in-law of $C$. $C$ is the unmarried sister of $D$, the mother of $E$. $A$ has only two children. How is $E$ related to $A$?  
- A) Granddaughter  
- B) Grandson  
- C) Grandchild (Gender cannot be determined)  
- D) Son  

**Q29 (Parity Indeterminacy).** In a family of seven members ($J, K, L, M, N, O, P$):
- $J$ is the father of $K$ and has at least two children.
- $L$ is the brother of $K$.
- $M$ is the mother of $N$.
- $O$ is the spouse of $J$.
- $P$ is the child of $L$.
- No gender is specified for $K$ or $N$.

How is $K$ related to $P$?  
- A) Uncle  
- B) Aunt  
- C) Either Uncle or Aunt (Cannot be determined)  
- D) Father  

**Q30 (The Reciprocal Perspective Trap).** If $A$ is the paternal uncle of $B$, what is $B$ to $A$?  
- A) Nephew  
- B) Niece  
- C) Cousin  
- D) Either Nephew or Niece (Cannot be determined)  

**Q31 (The Name-Gender Trap).** Introducing a visitor, Rohit said: *"Kiran is the only sibling of my wife's only brother-in-law."* Rohit has no brothers. How is Kiran related to Rohit?  
- A) Brother  
- B) Sister  
- C) Wife  
- D) Cannot be determined  

---

### Level 7: Extreme Caselets (Q32–Q41)

#### Caselet 1 (Questions 32–34): The Three-Generation Joint Family
*Directions for Q32–Q34:* Read the following paragraph carefully and answer the questions.  
Eight members of a family—$A, B, C, D, E, F, G, H$—belong to three generations. There are three married couples.
- $C$ is the sister-in-law of $E$, who is the daughter of $A$.
- $G$ is the only brother of $C$.
- $B$ is the father-in-law of $H$, who is the mother of $D$.
- $A$ is married to $B$ and has only one son and one daughter.
- $D$ is the granddaughter of $A$.
- $F$ is the brother-in-law of $G$, and $F$ is married.
- No single parent has a child.

**Q32.** How is $C$ related to $D$?  
- A) Mother  
- B) Maternal Aunt  
- C) Paternal Aunt  
- D) Grandmother  

**Q33.** How is $F$ related to $B$?  
- A) Son  
- B) Son-in-law  
- C) Brother-in-law  
- D) Nephew  

**Q34.** How many female members are there in the family?  
- A) 3  
- B) 4  
- C) 5  
- D) Cannot be determined  

---

#### Caselet 2 (Questions 35–37): Hybrid Blood Relations + Circular Seating
*Directions for Q35–Q37:* Read the following information carefully.  
Six family members—$P, Q, R, S, T, U$—are seated in a circle facing the center.
- There are two married couples in the group.
- $P$ is the father-in-law of $T$.
- $Q$ sits second to the left of her husband.
- $R$ is the brother of $Q$.
- $T$ is seated opposite her father-in-law.
- $S$ is the mother of $R$ and sits adjacent to her husband.
- $U$ is the son of $T$.

**Q35.** Who is the husband of $Q$?  
- A) $P$  
- B) $T$  
- C) Cannot be determined  
- D) The person sitting opposite $S$  

**Q36.** How is $U$ related to $P$?  
- A) Son  
- B) Grandson  
- C) Nephew  
- D) Brother  

**Q37.** Who sits immediately to the right of $U$'s mother?  
- A) $P$  
- B) $Q$  
- C) $R$  
- D) $S$  

---

#### Caselet 3 (Questions 38–41): Hybrid Blood Relations + Direction Sense
*Directions for Q38–Q41:* Read the following positional and genealogical data carefully.  
A family of seven members—$A, B, C, D, E, F, G$—are positioned on an open field:
- $A$ is the father of $B$ and stands $12\text{ m}$ North of $B$.
- $B$ is the brother of $C$, who is married to $D$.
- $D$ stands $9\text{ m}$ East of $C$.
- $E$ is the mother of $B$ and stands $5\text{ m}$ West of $A$.
- $F$ is the son of $D$ and stands $6\text{ m}$ South of $D$.
- $G$ is the brother of $E$ and stands $8\text{ m}$ North of $E$.
- $C$ stands at the exact midpoint of the line segment joining $B$ and a point directly South of $A$.

**Q38.** In which direction and at what shortest straight-line distance is $B$ located with respect to $A$'s wife $E$?  
- A) South-East, $13\text{ m}$  
- B) South-West, $13\text{ m}$  
- C) South-East, $17\text{ m}$  
- D) South, $12\text{ m}$  

**Q39.** How is $G$ related to $C$?  
- A) Paternal Uncle  
- B) Maternal Uncle  
- C) Grandfather  
- D) Father  

**Q40.** How is $F$ related to $A$?  
- A) Grandson  
- B) Son  
- C) Nephew  
- D) Son-in-law  

**Q41.** If $C$ is at $(0, 0)$, $B$ is at $(-4, 0)$, and $D$ is at $(9, 0)$, in which quadrant/direction is $F$ positioned with respect to his maternal grandfather $A$?  
- A) North-East  
- B) South-East  
- C) South-West  
- D) North-West  

---

### Level 8: Super-Expert — Multi-Marriage, Parity Collapse & 15+ Constraints (Q42–Q46)

**Q42 (Dual-Tree Parity Collapse).**  
A family of 10 members ($A, B, C, D, E, F, G, H, I, J$) spans three generations.
- There are exactly three married couples and exactly four females in the family.
- $A$ is the paternal grandfather of $G$ and $H$.
- $B$ is the wife of $A$.
- $C$ is the brother of $D$, who is the father of $G$.
- $E$ is the sister-in-law of $D$, and $E$ is married with two children ($I$ and $J$).
- $F$ is the daughter-in-law of $A$.
- No unmarried member has children, and no individual has married more than once.
- $H$ is the only sister of $G$.

How is $C$ related to $I$?  
- A) Father  
- B) Paternal Uncle  
- C) Maternal Uncle  
- D) Brother  

**Q43 (Co-Sibling & In-Law Web).**  
In an interconnected joint family:
- $P$ is the father-in-law of $Q$, who is the brother-in-law of $R$.
- $R$ is the only son of $S$, who is married to $P$.
- $T$ is the daughter-in-law of $P$ and is the sister of $U$.
- $V$ is the maternal aunt of $W$, who is the son of $Q$.
- $U$ is married to the only brother of $T$'s husband.
- $P$ has only two sons and no daughters.

How is $V$ related to $Q$?  
- A) Wife  
- B) Sister  
- C) Sister-in-law  
- D) Mother  

**Q44 (The 18-Constraint Distractor Network).**  
Read the following relational network:
- $K$ is the only brother of $L$, whose daughter $M$ is married to $N$.
- $N$'s mother $O$ is the only daughter of $P$.
- $P$ is married to $Q$.
- $Q$'s brother $R$ is the father of $S$.
- $S$'s maternal grandmother is $T$.
- $U$ is the father of $K$ and is married to $V$.
- $W$ is the son of $M$.
- $X$ is the sister-in-law of $N$, having no brothers.

How is $W$ related to $K$?  
- A) Grandson  
- B) Great-nephew (Sister's grandson)  
- C) Nephew  
- D) Son  

**Q45 (Nested Multi-Tier Coded Kinship with Incomplete Leaf).**  
Symbols are defined as:
- `P ↑ Q` → P is the mother of Q
- `P ↓ Q` → P is the father of Q
- `P ↔ Q` → P is the spouse of Q
- `P ⇒ Q` → P is the brother of Q
- `P ⇐ Q` → P is the sister of Q

Given the composite expression:  
```
Z ↓ Y ↔ X ⇐ W ↓ V ⇒ U ↔ T
```  
Which of the following statements is **definitely TRUE**?  
- A) $X$ is the paternal aunt of $V$  
- B) $W$ is the brother-in-law of $Y$  
- C) $T$ is the daughter-in-law of $W$  
- D) $Z$ is the grandfather of $U$  

**Q46 (The Ultimate Master Puzzle: Complete Kinship Graph Reconstruction).**  
A group of nine professionals ($A, B, C, D, E, F, G, H, I$) belong to one family spanning three generations.
- There are three married couples, each having at least one child.
- $A$, a surgeon, is the father-in-law of $E$, who is an advocate.
- $B$ is the grandmother of $H$ and $I$.
- $D$ is the maternal uncle of $H$.
- $C$ is the mother of $H$ and is married to $F$.
- $F$ is an architect and the only son of $A$.
- $G$ is the daughter of $E$.
- $I$ is the grandson of $A$.
- Exactly four members are females.

How is $D$ related to $A$?  
- A) Son  
- B) Son-in-law  
- C) Brother-in-law  
- D) Brother  

---

## 7. Answer Key & Comprehensive Solutions

### Master Answer Key (Q1–Q46)

| Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | A | **9** | A | **17** | A | **25** | A | **33** | B | **41** | B |
| **2** | A | **10** | A | **18** | B | **26** | B | **34** | B | **42** | A |
| **3** | B | **11** | B | **19** | B | **27** | B | **35** | D | **43** | C |
| **4** | C | **12** | A | **20** | B | **28** | C | **36** | B | **44** | B |
| **5** | C | **13** | B | **21** | B | **29** | C | **37** | A | **45** | C |
| **6** | B | **14** | B | **22** | C | **30** | D | **38** | A | **46** | B |
| **7** | A | **15** | B | **23** | C | **31** | C | **39** | B | — | — |
| **8** | A | **16** | D | **24** | B | **32** | A | **40** | A | — | — |

---

### Step-by-Step Derivations

#### Level 1 (Q1–Q5)
- **Q1 (A):** "Only daughter of my mother" = the woman herself. Her statement: "His mother is me." Hence, **Mother**.
- **Q2 (A):** If $A$ is the father of $B$ and $B$ is not a son, $B$ must be the **Daughter**.
- **Q3 (B):** "My mother's mother" = maternal grandmother. "Only son of maternal grandmother" = maternal uncle. The man is her maternal uncle; she is his **Niece**.
- **Q4 (C):** $P, Q, R$ are siblings ($P$ male, $Q$ female, $R$ male). $R$ is the father of $S$. $P$ is father's brother = **Paternal Uncle**.
- **Q5 (C):** "My daughter's father" = Deepak himself. "Father of Deepak" = Deepak's father. The gentleman's only brother is Deepak's father $\implies$ the gentleman is Deepak's **Paternal Uncle**.

#### Level 2 (Q6–Q10)
- **Q6 (B):** "Lady's mother's husband" = Lady's father. "Father's sister" = Lady's paternal aunt. That aunt is also the man's aunt. Hence, the lady is the man's **Sister**.
- **Q7 (A):** `P + R` (P is son of R). `R - Q` (R is wife of Q, so Q is male). Q is the **Father** of P.
- **Q8 (A):** "My grandfather's only son" = Anita's father (since grandfather has only one child). "Son of Anita's father" = Anita's **Brother**.
- **Q9 (A):** $[P] = (Q)$. $Q$ is daughter-in-law of $U \implies U$ is parent of $P$. Since $U$'s husband died, $U$ is female $\implies U$ is the **Mother** of $P$.
- **Q10 (A):** `T @ R` (T is sister of R). `R $ M` (R is father of M). `M @ K` (M is sister of K, so M is female). T is paternal aunt of M → M is the **Niece** of T.

#### Level 3 (Q11–Q15)
- **Q11 (B):** `J ★ K` (J is father of K). `K ★ T` (K is father of T). Father's father = **Paternal Grandfather**.
- **Q12 (A):** "My son's only brother" = my other son. "Son's daughter" = granddaughter. The child's father is the speaker's son. Paternal grandmother of the child is the speaker's **Wife**.
- **Q13 (B):** $[F] = (D)$. Their son is $[B]$ (engineer). $B$'s wife is $(A)$ (mother of $C$). Children of $B$ and $A$ are $C$ and $E$. Hence, $A$ is the **Wife** of $B$.
- **Q14 (B):** `P + Q` (P is father of Q). `Q × R` (Q brother of R). `R - S` (R mother of S). `S ÷ T` (S sister of T). R is mother of T, and P is father of R. Mother's father = **Maternal Grandfather**.
- **Q15 (B):** $Q$ is son of $R$, but $R$ not mother $\implies R$ is father (Male). $P$ is married to $R \implies P$ is female (1). $Y$ is brother of $R$ (Male). $X$ is daughter of $P$ (Female 2). $Z$ is brother of $P$ (Male). Total females = **2** ($P, X$).

#### Level 4 (Q16–Q20)
- **Q16 (D):** $M$ has two children: a son and a daughter ($P$). $N$ is married to $M$'s son. $Q$ is child of $M$'s son and $N$. $R$ is brother of $M$. $S$ is daughter-in-law of $R$. Since $S$ is married to $R$'s son (who is a cousin of $Q$'s father), $S$ is the **Paternal Aunt-in-law / Cousin's mother** to $Q$.
- **Q17 (A):** $A$ has only one son $H$, married to $I$. Children of $H$ are $B$ and $C$. $C$ is married to $D$. Since $D$ is the spouse of $H$'s child $C$, $D$ is $H$'s **Son-in-law or Daughter-in-law** (depending on $C$'s gender).
- **Q18 (B):** $P$ is mother of $K$ and $S$. $S$ is married to $T$. $V$ is daughter of $T$ and $S$. Since $S$ is $P$'s child, $V$ is $P$'s **Granddaughter**.
- **Q19 (B):** $[U] = (W)$. Their children are $[Z]$ and $(X)$. $[Z] = (Y)$. Since $Y$ is the wife of $U$'s son $Z$, $Y$ is the **Daughter-in-law** of $U$.
- **Q20 (B):** $M$ and $W$ are sisters, daughters of $R$. $K$ and $T$ are sons of $M$. $S$ is daughter of $T$. Generational difference between $R$ and $S$ is $+3$. Thus $R$ is the **Great-grandfather** of $S$.

#### Level 5 (Q21–Q26)
- **Q21 (B):** `P @ Q` (P is son of Q). `Q # R` (Q is father of R → P and R are brothers). `R & S` (R is wife of S → R is sister of P). `S # T` (S is father of T, so R is mother of T). Since P is the brother of T's mother R, P is the **Maternal Uncle** of T.
- **Q22 (C):** Paternal aunt means D is sister of H's father. In C: `E # D` (E is father of D). `D % F` (D is sister of F). `F # H` (F is father of H). Since D is the sister of H's father F, D is the **Paternal Aunt** of H.
- **Q23 (C):** $A(5)B$ ($A$ married to $B$). $B(3)C$ ($B$ sister of $C$). $C(2)E$ ($C$ mother of $E$). $E(5)F$ where $E$ is male $\implies F$ is female. Deducing $A$ male married to $B$ female, daughter of $F \implies A$ is **Son-in-law** of $F$.
- **Q24 (B):** "My father, who has only one daughter" $\to$ Vikram's father has only 1 daughter. "Her only brother's only nephew's paternal grandfather is Vikram's father." Vikram's father is the paternal grandfather of the nephew $\implies$ the nephew's father is Vikram (or Vikram's brother). Vikram's father's only daughter is Vikram's **Sister**.
- **Q25 (A):** In A: `T × M` (T is sister of M). `M ÷ K` (M is father of K). `K + N` (K is brother of N, hence K is male). K is the son of T's brother M → K is the **Nephew** of T.
- **Q26 (B):** $A$ and $E$ are parents of $B$ and $C$. $B$ is married to $D$. $H$ is the father of $D$. Hence, $H$ is the father of $B$'s wife $\implies H$ is $B$'s **Father-in-law**.

#### Level 6 (Q27–Q31)
- **Q27 (B):** Speaker is female. "Father of my only sister" = my father. "Only daughter-in-law of my father" = wife of my only brother. "Daughter of my brother's wife" = daughter of my brother = **Niece**.
- **Q28 (C):** $D$ is married to $B$. $A$ is father-in-law of $B$, so $A$ is father of $D$. $D$ is mother of $E$. Therefore $A$ is grandfather of $E$. But $E$'s gender is nowhere stated! Hence **Grandchild (Gender cannot be determined)**.
- **Q29 (C):** $J$ is father of $K$ and $L$. $P$ is child of $L$. $K$ is sibling of $L$. Since $K$'s gender is unspecified, $K$ can be either uncle or aunt to $P$. Answer: **Either Uncle or Aunt (Cannot be determined)**.
- **Q30 (D):** $A$ is the paternal uncle of $B$. $B$ is the child of $A$'s brother. Since $B$'s gender is not given, $B$ could be male (nephew) or female (niece). Answer: **Either Nephew or Niece (Cannot be determined)**.
- **Q31 (C):** "My wife's only brother-in-law" $\to$ Since Rohit has no brothers, his wife's only brother-in-law would normally be her sister's husband. But the statement specifies *"Kiran is the only sibling of my wife's only brother-in-law"*. In families with no other brothers or sisters, Rohit's wife is the unique solution when parsed as Rohit's own spouse: Kiran is Rohit's **Wife**.

#### Level 7 (Q32–Q41)
- **Q32 (A):** In Caselet 1: $B$ is husband of $A$. Their children are son $G$ and daughter $E$. $G$ is married to $C$. $E$ is married to $F$. $H$ is mother of $D \implies H = C$. Hence, $C$ is the **Mother** of $D$.
- **Q33 (B):** $F$ is married to $E$ (the daughter of $B$). Therefore, $F$ is the **Son-in-law** of $B$.
- **Q34 (B):** Females are $A$ (grandmother), $E$ (daughter), $C$ (daughter-in-law), $D$ (granddaughter). Males are $B, G, F$, and one child if male. Exactly **4 females** ($A, C, E, D$).
- **Q35 (D):** In Caselet 2: $P$ (male) is married to $S$ (female). Their son is $R$, daughter is $Q$. $T$ is female, married to $R$. $Q$'s husband is the person sitting opposite $S$.
- **Q36 (B):** $U$ is son of $T$ and $R$. Since $R$ is son of $P$, $U$ is the **Grandson** of $P$.
- **Q37 (A):** $U$'s mother is $T$. In the circle, $T$ sits opposite $P$. Moving clockwise, immediately to the right of $T$ sits **$P$**.
- **Q38 (A):** In Caselet 3: Let $B$ be at $(0, 0)$. $A$ is $12\text{ m}$ North of $B \implies A = (0, 12)$. $E$ is $5\text{ m}$ West of $A \implies E = (-5, 12)$. The vector from $E$ to $B$ is $(0 - (-5), 0 - 12) = (+5, -12)$. Distance $= \sqrt{5^2 + (-12)^2} = \sqrt{25 + 144} = \sqrt{169} = 13\text{ m}$. Direction is South-East. Answer: **South-East, $13\text{ m}$**.
- **Q39 (B):** $E$ is mother of $B$ and $C$. $G$ is brother of $E$. Mother's brother = **Maternal Uncle**.
- **Q40 (A):** $A$ is father of $C$. $C$ is mother of $F$. Daughter's son = **Grandson**.
- **Q41 (B):** $A$ is at $(0, 12)$. $F$ is $6\text{ m}$ South of $D(9, 0) \implies F = (9, -6)$. Vector from $A$ to $F$ is $(9 - 0, -6 - 12) = (9, -18)$ $\implies$ East and South. Hence **South-East**.

#### Level 8 (Q42–Q46)
- **Q42 (A):** Generational analysis of 10 members: Generation 1: $[A] = (B)$ (2 members). Generation 2: Sons $[C]$ and $[D]$. $[D] = (F)$ (parents of $G, H$). For 3 married couples, $E$ must be married to $C$ ($[C] = (E)$). Their children are $I$ and $J$. Since $C$ is the husband of $E$, $C$ is the **Father** of $I$.
- **Q43 (C):** Trace constraints: $P$ is married to $S$. Their two sons are $R$ and another son (say $X$). $T$ is married to $R$ or $X$. $U$ is married to the other brother. $Q$ is brother-in-law of $R$. $W$ is son of $Q$. $V$ is maternal aunt of $W \implies V$ is sister of $W$'s mother (who is $Q$'s wife). Hence $V$ is $Q$'s **Sister-in-law**.
- **Q44 (B):** Pruning analysis: Target is relationship between $W$ and $K$. $K$ and $L$ are brother and sister. $L$'s daughter is $M$. $M$'s son is $W$. Thus $W$ is the grandson of $K$'s sister $L$. $W$ is $K$'s sister's grandson = **Great-nephew**.
- **Q45 (C):** In the coded chain: `W ↓ V` (W father of V). `V ⇒ U` (V brother of U → W is father of U). `U ↔ T` (U married to T). Since W is father of U, U's wife T is the daughter-in-law of W. Hence **T is the daughter-in-law of W** is definitely TRUE.
- **Q46 (B):** Three couples across three generations: Gen 1: $[A] = (B)$. Gen 2: Son $[F] = (C)$ (parents of $H, I$). Since $D$ is maternal uncle of $H$, $D$ is the brother of $C$. $A$ is father-in-law of $E$. Since $F$ is the only son of $A$, $A$ must also have a daughter who is married to $D$, or $D$ is married into the family. With 3 married couples: $[A]=(B)$, $[F]=(C)$, $[D]=(E)$. Since $D$ is married to $A$'s daughter $E$, $D$ is the **Son-in-law** of $A$.

---

## 8. Placement-Specific High-Tier MCQs

### Q1 (Accenture / Deloitte Style — Multi-Branch Distractor Trap)
**Q:** $A$ is the brother of $B$. $B$ is the father of $C$. $D$ is the wife of $A$. $E$ is the daughter of $D$. $F$ is the sister of $B$. $G$ is the brother of $E$. How is $G$ related to $B$?  
- A) Son  
- B) Nephew  
- C) Brother  
- D) Cousin  

**Answer:** B) Nephew  
**Distractor Analysis:**  
- $A$ and $D$ are husband and wife. Their children are daughter $E$ and son $G$.  
- $B$ is the brother of $A$.  
- Therefore, $G$ is the son of $B$'s brother $A \implies G$ is $B$'s **Nephew**.  
- Option A (Son) is the classic trap for candidates confusing $A$ and $B$'s parental roles.

---

### Q2 (TCS Digital / Infosys DSE Style — Coded Generation Elimination)
**Q:** Given:
- `P # Q` → P is the father of Q (+1, Male)
- `P $ Q` → P is the mother of Q (+1, Female)
- `P @ Q` → P is the sister of Q (0, Female)
- `P % Q` → P is the son of Q (-1, Male)

Which expression indicates that **"M is the maternal grandmother of S"**?  
- A) `M $ N @ O $ S`  
- B) `M # N $ O @ S`  
- C) `M $ N % O $ S`  
- D) `M @ N $ O # S`  

**Answer:** A) `M $ N @ O $ S`  
**Distractor Analysis:**  
- Target generation of M relative to S is **+2**, and M must be female through a maternal line.  
- In B: `M # N` → M is father (male) → Eliminated instantly.  
- In C: Generation sum: $+1 - 1 + 1 = +1 \ne +2$ → Eliminated.  
- In D: `M @ N` → Generation sum: $0 + 1 + 1 = +2$, but M is sister of N who is mother → M is maternal grand-aunt, not grandmother → Eliminated.  
- In A: M is mother of N (+1). N is sister of O (0). O is mother of S (+1). Net = +2. M is mother of O (mother of S) → **Maternal Grandmother**!

---

### Q3 (Cognizant / Capgemini Style — Reciprocal Perspective Trap)
**Q:** Pointing to a woman, a man says, *"Her father-in-law is the father of my paternal uncle."* How is the woman related to the man?  
- A) Mother  
- B) Aunt  
- C) Either Mother or Aunt  
- D) Sister-in-law  

**Answer:** C) Either Mother or Aunt  
**Distractor Analysis:**  
- "Father of my paternal uncle" = Man's paternal grandfather.  
- "Her father-in-law is [my paternal grandfather]" $\implies$ The woman is married to a son of the man's paternal grandfather.  
- A son of the grandfather could be:
  1. The man's own father $\implies$ Woman is the man's **Mother**.
  2. The man's paternal uncle $\implies$ Woman is the man's **Aunt** (Paternal Aunt by marriage).  
- Since the problem does NOT state "only son", both cases are valid.  
- Correct Answer: **C) Either Mother or Aunt**.

---

## 9. Rapid Revision & Exam Checklist

- [ ] **Generation Score Shortcut:** Pre-calculate $+1, 0, -1$ to eliminate 2–3 options in coded relations within 10 seconds.
- [ ] **Gender Elimination:** Discard options where target person has the wrong gender or appears at the end without gender definition.
- [ ] **Pointing Problems:** Backward parsing from "my" solves 90% of questions in under 30 seconds.
- [ ] **Graph Pruning:** In 10+ link chains, cross out branches that do not link the source and target.
- [ ] **Trap Alert 1:** "Only son" does NOT mean "Only child" — sisters may exist!
- [ ] **Trap Alert 2:** Never assume gender from Indian personal names (Suman, Snehal, Kiran).
- [ ] **Trap Alert 3:** Always re-check the question subject: *"How is A related to B?"* is the reciprocal of *"How is B related to A?"*
- [ ] **Parity Check:** In caselets, use the number of married couples and female count constraints to eliminate candidate trees.

---

## 🔗 Cross-Links

- [Seating Arrangement](seating-arrangement.md) — Complex circular & linear family arrangements
- [Puzzles & Scheduling](puzzles-scheduling.md) — Multi-parameter family floor/profession puzzles
- [Direction Sense](direction-sense.md) — Positional vectors and coordinate-based kinship grids
- [Formula Sheet](../FORMULA_SHEET.md) — Comprehensive aptitude formula reference