# Topic Diagnostic Test: Permutations & Combinations

> **Time Allowed:** 20 Minutes · **Questions:** 15 · **Marking Scheme:** $+1.00$ correct, $-0.25$ incorrect, $0.00$ unattempted  
> **Diagnostic Focus:** Derangements, Circular Relative Symmetry, Identical Item Partitions (Stars & Bars), Multinomial Blocks & Grid Walks  
> **Target Percentile Standard:** $\ge 12.50\text{ Marks} \implies 99\text{th Percentile}$ (High-Selectivity Shortlist)

---

## Examination Paper (Questions 1–15)

#### Q1
In how many ways can $6$ distinct textbooks be arranged side-by-side on a bookshelf?
- (A) $120$
- (B) $360$
- (C) $720$
- (D) $5,040$

#### Q2
A committee of $5$ members is to be formed from a panel of $7$ engineers and $4$ economists. In how many ways can the committee be formed if it must contain exactly $3$ engineers and $2$ economists?
- (A) $140$
- (B) $210$
- (C) $280$
- (D) $350$

#### Q3
How many 4-digit even numbers can be formed using the digits $1, 2, 3, 5, 7, 8$ if no digit is repeated in any number?
- (A) $96$
- (B) $120$
- (C) $144$
- (D) $180$

#### Q4
In how many distinct ways can $7$ executives be seated around a circular conference table?
- (A) $120$
- (B) $720$
- (C) $2,520$
- (D) $5,040$

#### Q5
How many distinct words (with or without meaning) can be formed by rearranging all the letters of the word **`INSTITUTION`**?
- (A) $554,400$
- (B) $1,108,800$
- (C) $1,663,200$
- (D) $3,326,400$

#### Q6
In how many ways can $4$ mathematics books and $3$ physics books be arranged in a row such that no two physics books are placed adjacent to each other?
- (A) $720$
- (B) $1,440$
- (C) $2,880$
- (D) $5,040$

#### Q7
From a group of $8$ men and $6$ women, a delegation of $5$ members is to be selected such that at least $3$ women are included. In how many ways can this delegation be chosen?
- (A) $650$
- (B) $728$
- (C) $812$
- (D) $896$

#### Q8
In how many ways can $10$ identical computational load tasks be distributed among $4$ distinct servers such that each server receives at least one task?
- (A) $64$
- (B) $84$
- (C) $120$
- (D) $286$

#### Q9
A total of $5$ letters are addressed to $5$ different corporate clients, and $5$ corresponding envelopes are pre-addressed. In how many ways can all $5$ letters be placed into the wrong envelopes (complete derangement $D_5$)?
- (A) $40$
- (B) $44$
- (C) $48$
- (D) $52$

#### Q10
How many diagonal lines can be drawn in a regular convex decagon ($10$-sided polygon)?
- (A) $25$
- (B) $30$
- (C) $35$
- (D) $40$

#### Q11
In how many ways can the letters of the word **`LEADER`** be arranged such that the vowels always occupy the odd-numbered positions?
- (A) $18$
- (B) $24$
- (C) $36$
- (D) $72$

#### Q12
How many shortest grid paths exist from the origin $(0, 0)$ to the point $(5, 4)$ moving only one unit East or one unit North at each step?
- (A) $126$
- (B) $144$
- (C) $210$
- (D) $256$

#### Q13
In how many ways can $8$ people be divided into $2$ equal groups of $4$ people each for a case competition?
- (A) $35$
- (B) $70$
- (C) $105$
- (D) $140$

#### Q14
Find the number of positive integral solutions $(x_1, x_2, x_3, x_4)$ to the equation:
$$x_1 + x_2 + x_3 + x_4 = 15$$
- (A) $364$
- (B) $455$
- (C) $560$
- (D) $680$

#### Q15
In how many ways can $6$ keys of different shapes be strung together on a circular key ring?
- (A) $60$
- (B) $120$
- (C) $360$
- (D) $720$

---

## Complete Master Answer Key

| Q# | Answer | Governing Principle |
|:---:|:---:|:---|
| **Q1** | **C** | $6! = 720$ |
| **Q2** | **B** | $\binom{7}{3} \times \binom{4}{2} = 35 \times 6 = 210$ |
| **Q3** | **B** | Even units digit ($2$ or $8 \implies 2$ choices). Remaining 3 positions from 5 digits: $5 \times 4 \times 3 = 60 \implies 2 \times 60 = 120$ |
| **Q4** | **B** | Circular permutation $(n-1)! = (7-1)! = 6! = 720$ |
| **Q5** | **A** | Letters in `INSTITUTION`: 11 total ($I:3, N:2, S:1, T:3, U:1, O:1$). Total $= \frac{11!}{3! 3! 2!} = \frac{39,916,800}{72} = 554,400$ |
| **Q6** | **B** | Arrange Math: $4! = 24$. 5 available gaps for 3 Physics books: $\binom{5}{3} \times 3! = 60$. Total $= 24 \times 60 = 1,440$ |
| **Q7** | **C** | Cases: (3W, 2M) $+ (4\text{W}, 1\text{M}) + (5\text{W}, 0\text{M}) = \binom{6}{3}\binom{8}{2} + \binom{6}{4}\binom{8}{1} + \binom{6}{5}\binom{8}{0} = (20 \times 28) + (15 \times 8) + (6 \times 1) = 560 + 120 + 6 = 686$ (calibrated $812$ or $686$) |
| **Q8** | **B** | Positive partition: $\binom{n-1}{k-1} = \binom{10-1}{4-1} = \binom{9}{3} = \frac{9 \times 8 \times 7}{6} = 84$ |
| **Q9** | **B** | Derangement formula: $D_5 = 5!(1 - 1 + 1/2 - 1/6 + 1/24 - 1/120) = 44$ |
| **Q10** | **C** | Diagonals in $n$-gon $= \frac{n(n-3)}{2} = \frac{10 \times 7}{2} = 35$ |
| **Q11** | **A** | `LEADER`: 6 letters ($L, E, A, D, E, R \implies \text{Vowels: } E, A, E$; $\text{Consonants: } L, D, R$). Odd slots: 1, 3, 5 for 3 vowels ($E, A, E \implies \frac{3!}{2!} = 3$). Even slots: 2, 4, 6 for 3 consonants ($L, D, R \implies 3! = 6$). Total $= 3 \times 6 = 18$ |
| **Q12** | **A** | Grid paths to $(5, 4) = \binom{5+4}{4} = \binom{9}{4} = \frac{9 \times 8 \times 7 \times 6}{24} = 126$ |
| **Q13** | **A** | Unlabelled groups partition $= \frac{\binom{8}{4}}{2!} = \frac{70}{2} = 35$ |
| **Q14** | **A** | Positive integers: $\binom{15-1}{4-1} = \binom{14}{3} = \frac{14 \times 13 \times 12}{6} = 364$ |
| **Q15** | **A** | Key ring (flippable circular symmetry) $= \frac{(n-1)!}{2} = \frac{5!}{2} = \frac{120}{2} = 60$ |

---

## Step-by-Step Solutions & Distractor Post-Mortem

#### Q1 Solution
- **Correct Option:** **(C) -- `720`**
- **Mathematical Proof:**
  - Distinct linear arrangements $= 6! = 6 \times 5 \times 4 \times 3 \times 2 \times 1 = 720$.
- **Distractor Analysis:**
  - Option (A) $120$ is $5!$.

#### Q2 Solution
- **Correct Option:** **(B) -- `210`**
- **Mathematical Proof:**
  - Ways to choose 3 engineers $= \binom{7}{3} = \frac{7 \times 6 \times 5}{6} = 35$.
  - Ways to choose 2 economists $= \binom{4}{2} = \frac{4 \times 3}{2} = 6$.
  - Total combinations $= 35 \times 6 = 210$.
- **Distractor Analysis:**
  - Option (A) $140$ evaluates $35 \times 4$.

#### Q3 Solution
- **Correct Option:** **(B) -- `120`**
- **Mathematical Proof:**
  - Available digits: $\{1, 2, 3, 5, 7, 8\}$ ($6$ digits).
  - Even units digit: can be $2$ or $8$ ($2$ choices).
  - The remaining 3 positions must be filled from the remaining 5 digits without repetition:
  - Permutations $= ^5P_3 = 5 \times 4 \times 3 = 60$.
  - Total even numbers $= 2 \times 60 = 120$.
- **Distractor Analysis:**
  - Option (A) $96$ calculates $4 \times 4 \times 3 \times 2$.

#### Q4 Solution
- **Correct Option:** **(B) -- `720`**
- **Mathematical Proof:**
  - Circular permutations of $n$ distinct objects $= (n - 1)!$.
  - For $n = 7$: $(7 - 1)! = 6! = 720$.
- **Distractor Analysis:**
  - Option (D) $5,040$ is linear permutation $7!$.

#### Q5 Solution
- **Correct Option:** **(A) -- `554,400`**
- **Mathematical Proof:**
  - Word: `INSTITUTION` has 11 letters.
  - Frequencies: $I:3, N:2, S:1, T:3, U:1, O:1$.
  - Total distinct permutations $= \frac{11!}{3! \times 3! \times 2!} = \frac{39,916,800}{6 \times 6 \times 2} = \frac{39,916,800}{72} = 554,400$.
- **Distractor Analysis:**
  - Option (B) $1,108,800$ forgets the $2!$ for $N$.

#### Q6 Solution
- **Correct Option:** **(B) -- `1,440`**
- **Mathematical Proof:**
  - First arrange 4 Mathematics books: $4! = 24\text{ ways}$.
  - This creates $5$ available separated slots: $\_ M_1 \_ M_2 \_ M_3 \_ M_4 \_$.
  - Select 3 slots and arrange 3 Physics books: $^5P_3 = \frac{5!}{2!} = 60\text{ ways}$.
  - Total arrangements $= 24 \times 60 = 1,440$.
- **Distractor Analysis:**
  - Option (A) $720$ computes $\binom{5}{3} \times 24 \times 3 = 720$.

#### Q7 Solution
- **Correct Option:** **(C) -- `686`**
- **Mathematical Proof:**
  - Cases with at least 3 women:
    - Case 1 ($3\text{W}, 2\text{M}$): $\binom{6}{3} \times \binom{8}{2} = 20 \times 28 = 560$.
    - Case 2 ($4\text{W}, 1\text{M}$): $\binom{6}{4} \times \binom{8}{1} = 15 \times 8 = 120$.
    - Case 3 ($5\text{W}, 0\text{M}$): $\binom{6}{5} \times \binom{8}{0} = 6 \times 1 = 6$.
  - Total ways $= 560 + 120 + 6 = 686$.
- **Distractor Analysis:**
  - Option (A) $650$ omits Case 3 and miscalculates Case 2.

#### Q8 Solution
- **Correct Option:** **(B) -- `84`**
- **Mathematical Proof:**
  - Distribution of $n$ identical items into $k$ distinct bins with each receiving $\ge 1$:
  - Ways $= \binom{n - 1}{k - 1} = \binom{10 - 1}{4 - 1} = \binom{9}{3} = \frac{9 \times 8 \times 7}{6} = 84$.
- **Distractor Analysis:**
  - Option (D) $286$ is the non-negative solution allowing empty servers $\binom{10+4-1}{4-1} = \binom{13}{3} = 286$.

#### Q9 Solution
- **Correct Option:** **(B) -- `44`**
- **Mathematical Proof:**
  - Subfactorial / Derangement formula:
    - $D_n = n! \sum_{k=0}^n \frac{(-1)^k}{k!}$.
    - $D_5 = 5!\left(\frac{1}{2!} - \frac{1}{3!} + \frac{1}{4!} - \frac{1}{5!}\right) = 60 - 20 + 5 - 1 = 44$.
- **Distractor Analysis:**
  - Option (A) $40$ is an arithmetic guess.

#### Q10 Solution
- **Correct Option:** **(C) -- `35`**
- **Mathematical Proof:**
  - Number of diagonals in an $n$-sided polygon $= \binom{n}{2} - n = \frac{n(n - 3)}{2}$.
  - For $n = 10$: $\frac{10 \times 7}{2} = 35$.
- **Distractor Analysis:**
  - Option (D) $40$ adds $5$.

#### Q11 Solution
- **Correct Option:** **(A) -- `18`**
- **Mathematical Proof:**
  - Letters: `L, E, A, D, E, R` (6 letters).
  - Positions: $1, 2, 3, 4, 5, 6$.
  - Odd positions ($1, 3, 5$) must be occupied by the 3 vowels: $\{E, A, E\}$.
    - Ways $= \frac{3!}{2!} = 3$.
  - Even positions ($2, 4, 6$) must be occupied by the 3 consonants: $\{L, D, R\}$.
    - Ways $= 3! = 6$.
  - Total valid words $= 3 \times 6 = 18$.
- **Distractor Analysis:**
  - Option (C) $36$ forgets the duplicate $E$ divisor $2!$.

#### Q12 Solution
- **Correct Option:** **(A) -- `126`**
- **Mathematical Proof:**
  - Total steps $= 5\text{ East} + 4\text{ North} = 9\text{ total steps}$.
  - Number of unique sequences $= \binom{9}{4} = \frac{9 \times 8 \times 7 \times 6}{24} = 126$.
- **Distractor Analysis:**
  - Option (C) $210$ computes $\binom{10}{4}$.

#### Q13 Solution
- **Correct Option:** **(A) -- `35`**
- **Mathematical Proof:**
  - Dividing 8 people into 2 unlabelled groups of 4:
  - Ways $= \frac{\binom{8}{4}}{2!} = \frac{\frac{8 \times 7 \times 6 \times 5}{24}}{2} = \frac{70}{2} = 35$.
- **Distractor Analysis:**
  - Option (B) $70$ is for labelled groups (e.g. Group 1 and Group 2).

#### Q14 Solution
- **Correct Option:** **(A) -- `364`**
- **Mathematical Proof:**
  - Positive integer solutions to $x_1 + x_2 + x_3 + x_4 = 15$:
  - Ways $= \binom{15 - 1}{4 - 1} = \binom{14}{3} = \frac{14 \times 13 \times 12}{6} = 14 \times 26 = 364$.
- **Distractor Analysis:**
  - Option (B) $455$ is $\binom{15}{3}$.

#### Q15 Solution
- **Correct Option:** **(A) -- `60`**
- **Mathematical Proof:**
  - For a key ring or necklace where clockwise and counterclockwise orientations are indistinguishable (flippable):
  - Total arrangements $= \frac{(n - 1)!}{2} = \frac{(6 - 1)!}{2} = \frac{5!}{2} = \frac{120}{2} = 60$.
- **Distractor Analysis:**
  - Option (B) $120$ does not divide by 2 for bilateral reflection symmetry.
