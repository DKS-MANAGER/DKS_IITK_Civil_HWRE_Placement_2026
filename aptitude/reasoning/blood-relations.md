# Blood Relations

> **Priority:** P1 · **Role relevance:** High (Universal across Core, IT, Analytics, Consulting & Banking)
> **Difficulty range:** Easy → Expert / Extreme · **Target speed:** 30 sec (Direct) – 90 sec (Complex/Puzzle)

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
| **Brother-in-law** | Spouse's brother OR Sister's husband |
| **Sister-in-law** | Spouse's sister OR Brother's wife |
| **Father-in-law** | Spouse's father |
| **Mother-in-law** | Spouse's mother |
| **Son-in-law** | Daughter's husband |
| **Daughter-in-law** | Son's wife |

---

## 3. High-Speed Shortcut Methods

### 3.1 The Generation Score Method (for Coded Relations)
Assign an integer generation value to each operator:
- Parent/Father/Mother/Uncle/Aunt $\to \mathbf{+1}$
- Brother/Sister/Husband/Wife/Cousin $\to \mathbf{0}$
- Son/Daughter/Nephew/Niece $\to \mathbf{-1}$
- Grandfather/Grandmother $\to \mathbf{+2}$
- Grandson/Granddaughter $\to \mathbf{-2}$

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

---

## 4. Advanced Placement Reasoning Strategies

| Level | Link Count | Key Challenge | Target Approach |
|:------|:----------:|:--------------|:----------------|
| **Hard** | 6–8 links | 3 generations, mixed in-laws | Forward tree diagramming |
| **Very Hard** | 8–12 links | Dual-family marriages, branch crossover | Node-by-node unification |
| **Expert** | 12–18 links | Distractor networks, indirect parentage | Graph pruning to target pair |
| **Code-Expert** | 4–6 operators | Multi-tiered coded conditions | Generation sum + Gender filter |
| **Traps** | Variable | "Only", "exactly", gender indeterminacy | Explicit verification of edge cases |
| **Extreme** | Paragraph | 1 caselet $\to$ 2–4 questions | Master family tree before answering |
| **Hybrid** | Variable | Relations combined with seating/direction | Multi-grid solving |

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
- C) $M - R \div N$  
- D) $M + R \times N$  

**Step-by-step Solution:**
1. **Target Analysis:** Maternal uncle means $M$ is **male**, generation of $M$ relative to $N$ is $\mathbf{+1}$, through $N$'s mother.
2. **Gender Check:**
   - In C: $M - R \implies M$ is female $\to$ **Eliminated**.
   - In D: $M + R \implies M$ is father, but $R \times N$ makes $R$ brother $\to M$ is father of $N \to$ **Eliminated**.
3. **Generation & Path Check:**
   - In A: $M \times R$ ($M$ brother of $R$) $\to R + N$ ($R$ father of $N$) $\implies M$ is paternal uncle $\to$ **Eliminated**.
   - In B: $M \times R$ ($M$ brother of $R$) $\to R \div N$ ($R$ mother of $N$) $\implies M$ is brother of $N$'s mother $\implies$ **Maternal Uncle**!
4. **Answer:** **B) $M \times R \div N$**.

### Example 3: The 14-Link Graph Pruning Master Example (Expert)
**Problem:** $A$ is the only daughter of $B$. $B$ is the elder brother of $C$. $C$ is married to $D$. $D$'s only sister $E$ is married to $F$. $F$'s maternal uncle $G$ has two children, $H$ and $I$. $H$'s daughter $J$ is married to $K$. $K$'s father is $L$, who is the only son of $M$. $M$'s daughter $N$ is the mother of $A$. How is $K$ related to $B$?  
**Step-by-step Solution (Pruning Method):**
1. Question asks for the relationship between **$K$** and **$B$**.
2. Locate statements containing $B$:
   - "$A$ is the only daughter of $B$." $\to B$ is the father of $A$ (or parent).
   - "$M$'s daughter $N$ is the mother of $A$." $\to N$ is the mother of $A$.
   - Since $B$ is the father and $N$ is the mother of $A$, **$B$ and $N$ are married couple ($[B] = (N)$)**!
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

## 6. Comprehensive Practice Set (32 Placement Questions)

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

**Q10.** If $X @ Y$ means "$X$ is sister of $Y$"; $X \# Y$ means "$X$ is mother of $Y$"; $X \$ Y$ means "$X$ is father of $Y$". Which of the following means **"$M$ is the niece of $T$"**?  
- A) $T @ R \$ M @ K$  
- B) $M @ K \# T \$ R$  
- C) $T \$ R @ M @ K$  
- D) $R \$ T @ M @ K$  

---

### Level 3: Hard — 6–8 Links & Multi-Generation (Q11–Q15)

**Q11.** Read the relations:
- $P \star Q \implies P$ is the father of $Q$
- $P \Delta Q \implies P$ is the daughter of $Q$
- $P \square Q \implies P$ is the sister of $Q$
- $P \circ Q \implies P$ is the husband of $Q$

Which expression indicates that **"$J$ is the paternal grandfather of $T$"**?  
- A) $J \star K \circ L \star T$  
- B) $J \star K \star T \square M$  
- C) $J \circ K \Delta L \star T$  
- D) $J \star K \square L \star T$  

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

### Level 5: Expert & Code-Expert (Q21–Q24)

**Q21.** If:
- $A \ \& \ B \implies A$ is the wife of $B$
- $A \ \# \ B \implies A$ is the father of $B$
- $A \ @ \ B \implies A$ is the son of $B$
- $A \ \% \ B \implies A$ is the sister of $B$
- $A \ \star \ B \implies A$ is the brother of $B$

In the expression $P \ @ \ Q \ \# \ R \ \& \ S \ \# \ T \ \% \ U$, how is $P$ related to $T$?  
- A) Paternal Uncle  
- B) Maternal Uncle  
- C) Brother  
- D) Father  

**Q22.** Using the codes from Q21, which of the following expressions establishes that **"$D$ is the paternal aunt of $H$"**?  
- A) $D \ \% \ E \ \# \ H \ @ \ K$  
- B) $D \ \& \ E \ \# \ H \ \star \ K$  
- C) $E \ \# \ D \ \% \ F \ \# \ H$  
- D) $D \ \% \ E \ @ \ F \ \# \ H$  

**Q23.** In a coded kinship system:
- $P(1)Q \implies P$ is the father of $Q$
- $P(2)Q \implies P$ is the mother of $Q$
- $P(3)Q \implies P$ is the sister of $Q$
- $P(4)Q \implies P$ is the brother of $Q$
- $P(5)Q \implies P$ is the spouse of $Q$

Which of the following expressions represents that **"$A$ is the son-in-law of $F$"**?  
- A) $A(5)B(3)C(2)F$  
- B) $A(5)B(4)C(1)F$  
- C) $A(5)B(3)C(2)E(5)F$ where $E$ is male  
- D) $A(5)B(3)C$ and $B(2)F$  

**Q24.** Consider the statement: *"Pointing to a woman in a painting, Vikram said: 'Her only brother's only nephew's paternal grandfather is my father, who has only one daughter.' "* If Vikram has only one brother, how is the woman in the painting related to Vikram?  
- A) Mother  
- B) Sister  
- C) Paternal Aunt  
- D) Wife  

---

### Level 6: Trap & Disambiguation Sets (Q25–Q26)

**Q25 (The "Only Daughter" Ambiguity).** A person said, *"That girl is the daughter of the only daughter-in-law of the father of my only sister."* If the speaker is a female, who is the girl to the speaker?  
- A) Daughter  
- B) Niece  
- C) Sister  
- D) Sister-in-law  

**Q26 (Pronoun Reference Trap).** $A$ is the father-in-law of $B$ who is the brother-in-law of $C$. $C$ is the unmarried sister of $D$, the mother of $E$. $A$ has only two children. How is $E$ related to $A$?  
- A) Granddaughter  
- B) Grandson  
- C) Grandchild (Gender not determinable)  
- D) Son  

---

### Level 7: Extreme Multi-Question Caselets (Q27–Q32)

#### Caselet 1 (Questions 27–29): The Three-Generation Joint Family
*Directions for Q27–Q29:* Read the following paragraph carefully and answer the questions.  
Eight members of a family—$A, B, C, D, E, F, G, H$—belong to three generations. There are three married couples.
- $C$ is the sister-in-law of $E$, who is the daughter of $A$.
- $G$ is the only brother of $C$.
- $B$ is the father-in-law of $H$, who is the mother of $D$.
- $A$ is married to $B$ and has only one son and one daughter.
- $D$ is the granddaughter of $A$.
- $F$ is the brother-in-law of $G$, and $F$ is married.
- No single parent has a child.

**Q27.** How is $C$ related to $D$?  
- A) Mother  
- B) Maternal Aunt  
- C) Paternal Aunt  
- D) Grandmother  

**Q28.** How is $F$ related to $B$?  
- A) Son  
- B) Son-in-law  
- C) Brother-in-law  
- D) Nephew  

**Q29.** How many female members are there in the family?  
- A) 3  
- B) 4  
- C) 5  
- D) Cannot be determined  

---

#### Caselet 2 (Questions 30–32): Hybrid Blood Relations + Circular Seating
*Directions for Q30–Q32:* Read the following information carefully.  
Six family members—$P, Q, R, S, T, U$—are seated in a circle facing the center.
- There are two married couples in the group.
- $P$ is the father-in-law of $T$.
- $Q$ sits second to the left of her husband.
- $R$ is the brother of $Q$.
- $T$ is seated opposite her father-in-law.
- $S$ is the mother of $R$ and sits adjacent to her husband.
- $U$ is the son of $T$.

**Q30.** Who is the husband of $Q$?  
- A) $P$  
- B) $T$  
- C) Cannot be determined  
- D) The person sitting opposite $S$  

**Q31.** How is $U$ related to $P$?  
- A) Son  
- B) Grandson  
- C) Nephew  
- D) Brother  

**Q32.** Who sits immediately to the right of $U$'s mother?  
- A) $P$  
- B) $Q$  
- C) $R$  
- D) $S$  

---

## 7. Answer Key & Comprehensive Solutions

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | A | **9** | A | **17** | A | **25** | B |
| **2** | A | **10** | A | **18** | B | **26** | C |
| **3** | B | **11** | B | **19** | B | **27** | A |
| **4** | C | **12** | A | **20** | B | **28** | B |
| **5** | C | **13** | B | **21** | B | **29** | B |
| **6** | B | **14** | B | **22** | C | **30** | D |
| **7** | A | **15** | B | **23** | C | **31** | B |
| **8** | A | **16** | B | **24** | B | **32** | A |

---

### Step-by-Step Derivations

- **Q1 (A):** "Only daughter of my mother" = the woman herself. Her statement: "His mother is me." Hence, **Mother**.
- **Q2 (A):** If $A$ is the father of $B$ and $B$ is not a son, $B$ must be the **Daughter**.
- **Q3 (B):** "My mother's mother" = maternal grandmother. "Only son of maternal grandmother" = maternal uncle. The man is her maternal uncle; she is his **Niece**.
- **Q4 (C):** $P, Q, R$ are siblings ($P$ male, $Q$ female, $R$ male). $R$ is the father of $S$. $P$ is father's brother = **Paternal Uncle**.
- **Q5 (C):** "My daughter's father" = Deepak himself. "Father of Deepak" = Deepak's father. The gentleman's only brother is Deepak's father $\implies$ the gentleman is Deepak's **Paternal Uncle**.
- **Q6 (B):** "Lady's mother's husband" = Lady's father. "Father's sister" = Lady's paternal aunt. That aunt is also the man's aunt. Hence, the lady is the man's **Sister**.
- **Q7 (A):** $P + R \implies P$ is son of $R$. $R - Q \implies R$ is wife of $Q$ ($Q$ is male). $Q$ is the **Father** of $P$.
- **Q8 (A):** "My grandfather's only son" = Anita's father (since grandfather has only one child). "Son of Anita's father" = Anita's **Brother**.
- **Q9 (A):** $[P] = (Q)$. $Q$ is daughter-in-law of $U \implies U$ is parent of $P$. Since $U$'s husband died, $U$ is female $\implies U$ is the **Mother** of $P$.
- **Q10 (A):** $T @ R \implies T$ is sister of $R$. $R \$ M \implies R$ is father of $M$. $M @ K \implies M$ is sister of $K$ ($M$ is female). $T$ is paternal aunt of $M \implies M$ is the **Niece** of $T$.
- **Q11 (B):** $J \star K \implies J$ is father of $K$. $K \star T \implies K$ is father of $T$. Father's father = **Paternal Grandfather**.
- **Q12 (A):** "My son's only brother" = my other son. "Son's daughter" = granddaughter. The child's father is the speaker's son. Paternal grandmother of the child is the speaker's **Wife**.
- **Q13 (B):** $[F] = (D)$. Their son is $[B]$ (engineer). $B$'s wife is $(A)$ (mother of $C$). Children of $B$ and $A$ are $C$ and $E$. Hence, $A$ is the **Wife** of $B$.
- **Q14 (B):** $P + Q$ ($P$ is father of $Q$). $Q \times R$ ($Q$ brother of $R$). $R - S$ ($R$ mother of $S$). $S \div T$ ($S$ sister of $T$). $R$ is mother of $T$, and $P$ is father of $R$. Mother's father = **Maternal Grandfather**.
- **Q15 (B):** $Q$ is son of $R$, but $R$ not mother $\implies R$ is father (Male). $P$ is married to $R \implies P$ is female (1). $Y$ is brother of $R$ (Male). $X$ is daughter of $P$ (Female 2). $Z$ is brother of $P$ (Male). Total females = **2** ($P, X$).
- **Q16 (B):** Trace family tree: $M$ has two children: a son and a daughter. $N$ is married to $M$'s son. $P$ is the unmarried daughter ($P$ is paternal aunt of $Q \implies Q$ is child of $M$'s son and $N$). $T$ is the only nephew of $P \implies T$ is $Q$'s brother (or $Q$ is female and $T$ is male). $R$ is brother of $M$. $S$ is daughter-in-law of $R$. But wait, $S$ has no siblings and is married into $R$'s line. Now re-evaluating: $M$ is father-in-law of $N$. Could $S$ be $N$? If $S$ is married to $M$'s son, then $S=N$, meaning $S$ is the **Mother** of $Q$!
- **Q17 (A):** $A$ is paternal grandfather of $B \implies A$'s only son $H$ is the father of $B$ and $C$. $C$ is married to $D$. Since $C$ is child of $H$, $C$'s spouse $D$ is $H$'s **Son-in-law or Daughter-in-law** (depending on $C$'s gender).
- **Q18 (B):** $P$ is mother of $K$ and $S$. $S$ is married to $T$. $V$ is daughter of $T$ and $S$. Since $S$ is $P$'s child, $V$ is $P$'s **Granddaughter**.
- **Q19 (B):** $[U] = (W)$. Their children are $[Z]$ and $(X)$. $[Z] = (Y)$. Since $Y$ is the wife of $U$'s son $Z$, $Y$ is the **Daughter-in-law** of $U$.
- **Q20 (B):** $M$ and $W$ are sisters, daughters of $R$. $K$ and $T$ are sons of $M$. $S$ is daughter of $T$. Generations: $R$ (+2 from $T$) $\to S$ is generation -1 from $T$. Total gap between $R$ and $S$ is +3 generations! Thus $R$ is the **Great-grandfather** of $S$.
- **Q21 (B):** Break down: $P @ Q$ ($P$ is son of $Q$). $Q \# R$ ($Q$ is father of $R \implies P$ and $R$ are brothers). $R \& S$ ($R$ is wife of $S \implies R$ is sister of $P$). $S \# T$ ($S$ is father of $T$, so $R$ is mother of $T$). Since $P$ is the brother of $T$'s mother $R$, $P$ is the **Maternal Uncle** of $T$.
- **Q22 (C):** Paternal aunt means $D$ is sister of $H$'s father. In C: $E \# D$ ($E$ is father of $D$). $D \% F$ ($D$ is sister of $F$). $F \# H$ ($F$ is father of $H$). Since $D$ is the sister of $H$'s father $F$, $D$ is the **Paternal Aunt** of $H$.
- **Q23 (C):** $A(5)B$ ($A$ married to $B$). $B(3)C$ ($B$ sister of $C$). $C(2)E$ ($C$ mother of $E$). $E(5)F$ where $E$ is male $\implies F$ is female. $A$ being son-in-law of $F$ requires $A$ married to $F$'s child. In C: $B$ is daughter of $F$ if $E$ and $F$ are parents of $B, C$. Here $C(2)E(5)F$ connects to $F$. Trace: $A$ male married to $B$ female, daughter of $F \implies A$ is **Son-in-law** of $F$.
- **Q24 (B):** "My father, who has only one daughter" $\to$ Vikram's father has only 1 daughter. "Her only brother's only nephew's paternal grandfather is Vikram's father." Vikram's father is the paternal grandfather of the nephew $\implies$ the nephew's father is Vikram (or Vikram's brother). Vikram's father's only daughter is Vikram's **Sister**.
- **Q25 (B):** Speaker is female. "Father of my only sister" = my father. "Only daughter-in-law of my father" = wife of my only brother. "Daughter of my brother's wife" = daughter of my brother = **Niece**.
- **Q26 (C):** $D$ is married to $B$. $D$'s mother is not $A$, $A$ is father-in-law of $B$, so $A$ is father of $D$. $D$ is mother of $E$. Therefore $A$ is grandfather of $E$. But $E$'s gender is nowhere stated! Hence **Grandchild (Gender not determinable)**.
- **Q27 (A):** Trace Caselet 1: $B$ is husband of $A$. Their children are son $G$ and daughter $E$. $G$ is married to $C$. $E$ is married to $F$. $C$'s children are $D$ and $H$ (or $G$ and $C$ are parents of $D$). $H$ is mother of $D \implies H=C$. Hence, $C$ is the **Mother** of $D$.
- **Q28 (B):** $F$ is married to $E$ (the daughter of $B$). Therefore, $F$ is the **Son-in-law** of $B$.
- **Q29 (B):** Females are $A$ (grandmother), $E$ (daughter), $C$ (daughter-in-law), $D$ (granddaughter). Males are $B, G, F$, and one child if male. Exactly **4 females** ($A, C, E, D$).
- **Q30 (D):** Circular seating trace: $P$ (male) is married to $S$ (female). Their son is $R$, daughter is $Q$. $Q$ is married to $T$'s brother or $P$'s other child. $T$ is female, married to $R$. $Q$'s husband sits opposite $S$.
- **Q31 (B):** $U$ is son of $T$ and $R$. Since $R$ is son of $P$, $U$ is the **Grandson** of $P$.
- **Q32 (A):** $U$'s mother is $T$. In the circle, $T$ sits opposite $P$. Moving clockwise, immediately to the right of $T$ sits **$P$**.

---

## 8. Placement-Specific MCQs

### Q1 (TCS / Infosys Style — Distractor Trap)
**Q:** Pointing to a person in a photograph, Raman said, *"My only brother's wife's only daughter is the person."* How is the person in the photograph related to Raman?  
- A) Daughter  
- B) Niece  
- C) Sister  
- D) Sister-in-law  

**Answer:** B) Niece  
**Explanation:**  
- "My only brother's wife" = Raman's sister-in-law.  
- "Only daughter of Raman's sister-in-law" = Raman's brother's daughter.  
- Brother's daughter = **Niece** (Common trap: Selecting "Daughter" due to misreading "only daughter").

### Q2 (Cognizant / Accenture Style — Coded Deduction)
**Q:** If '$A \$ B$' means '$A$ is father of $B$', '$A \# B$' means '$A$ is daughter of $B$', and '$A @ B$' means '$A$ is sister of $B$'. In the expression $K \$ L @ M \# N$, how is $K$ related to $N$?  
- A) Brother  
- B) Husband  
- C) Father-in-law  
- D) Son  

**Answer:** B) Husband  
**Explanation:**  
- $K \$ L$: $K$ is father of $L$ ($[K]$ is male).  
- $L @ M$: $L$ is sister of $M$ ($(L)$ is female).  
- $M \# N$: $M$ is daughter of $N$ ($(M)$ is female, $N$ is parent).  
- Since $K$ is father of $L$, and $L, M$ are siblings, $K$ is also the father of $M$.  
- Since $N$ is also the parent of $M$ and $K$ is male father, $N$ must be the mother.  
- Thus, $K$ is the **Husband** of $N$.

### Q3 (Wipro / Capgemini Style — Speaker Ambiguity)
**Q:** A lady introduces a man saying, *"His wife is the only daughter of my father."* How is the man related to the lady?  
- A) Brother  
- B) Father  
- C) Husband  
- D) Uncle  

**Answer:** C) Husband  
**Explanation:**  
- The speaker is a **lady**.  
- "The only daughter of my father" $\implies$ Because the speaker is a female and her father has only one daughter, the only daughter must be the lady herself!  
- "His wife is [the lady herself]" $\implies$ The man is the lady's **Husband**.

---

## 9. Rapid Revision & Exam Checklist

- [ ] **Generation Score Shortcut:** Match $+1, 0, -1$ before drawing trees in coded relations.
- [ ] **Gender Elimination:** Discard options where target person has the wrong gender or appears at the end without gender definition.
- [ ] **Pointing Problems:** Backward parsing from "my" solves 90% of questions in under 30 seconds.
- [ ] **Graph Pruning:** In 10+ link chains, immediately cross out branches that do not link the source and target.
- [ ] **Trap Alert 1:** "Only son" does NOT mean "Only child" — sisters may exist!
- [ ] **Trap Alert 2:** Never assume gender from Indian personal names (Suman, Snehal, Kiran).
- [ ] **Trap Alert 3:** Always re-check the question subject: *"How is A related to B?"* is the reciprocal of *"How is B related to A?"*

---

## 🔗 Cross-Links

- [Seating Arrangement](seating-arrangement.md) — Complex circular & linear family arrangements
- [Puzzles & Scheduling](puzzles-scheduling.md) — Multi-parameter family floor/profession puzzles
- [Formula Sheet](../FORMULA_SHEET.md) — Comprehensive aptitude formula reference
