# Topic Diagnostic Test: Probability & Stochastic Models

> **Time Allowed:** 20 Minutes · **Questions:** 15 · **Marking Scheme:** $+1.00$ correct, $-0.25$ incorrect, $0.00$ unattempted  
> **Diagnostic Focus:** Bayes' Conditional Inversion, Binomial Mass Probability, Total Probability Law, Geometric Sequences & Card/Urn Selections  
> **Target Preparation Standard:** $\ge 12.50 / 15.00\text{ Marks}$ (Internal Target Benchmark: High-Selectivity Cutoff [PREPARATION HEURISTIC])

---

## Examination Paper (Questions 1–15)

#### Q1
Two fair six-sided dice are rolled simultaneously. What is the probability that the sum of the numbers appearing on top is greater than $9$?
- (A) $\frac{1}{9}$
- (B) $\frac{1}{6}$
- (C) $\frac{5}{18}$
- (D) $\frac{1}{4}$

#### Q2
A card is drawn at random from a well-shuffled standard deck of $52$ playing cards. What is the probability that the card drawn is either a King or a Heart?
- (A) $\frac{4}{13}$
- (B) $\frac{17}{52}$
- (C) $\frac{9}{26}$
- (D) $\frac{5}{13}$

#### Q3
An urn contains $5$ red balls, $4$ green balls, and $3$ blue balls. If $3$ balls are drawn at random without replacement, what is the probability that all $3$ balls are of different colors?
- (A) $\frac{3}{11}$
- (B) $\frac{6}{22}$
- (C) $\frac{9}{22}$
- (D) $\frac{12}{55}$

#### Q4
A problem in advanced econometrics is given to three graduate students $A, B,$ and $C$ whose chances of solving it independently are $\frac{1}{2}, \frac{1}{3},$ and $\frac{1}{4}$ respectively. What is the probability that the problem is solved?
- (A) $\frac{1}{4}$
- (B) $\frac{1}{2}$
- (C) $\frac{3}{4}$
- (D) $\frac{5}{6}$

#### Q5
In a high-tech manufacturing facility, Machine $M_1$ produces $60\%$ of total output and Machine $M_2$ produces $40\%$. The defect rate of $M_1$ is $2\%$ and that of $M_2$ is $5\%$. If a randomly selected finished product is found to be defective, what is the probability that it was produced by Machine $M_2$?
- (A) $\frac{3}{8}$
- (B) $\frac{5}{8}$
- (C) $\frac{1}{2}$
- (D) $\frac{2}{3}$

#### Q6
A fair coin is tossed $6$ times consecutively. What is the probability of obtaining exactly $4$ heads?
- (A) $\frac{15}{64}$
- (B) $\frac{5}{16}$
- (C) $\frac{21}{64}$
- (D) $\frac{3}{8}$

#### Q7
Two integers $a$ and $b$ are chosen at random from the set $\{1, 2, 3, \dots, 20\}$. What is the probability that their sum $(a + b)$ is an odd number?
- (A) $\frac{9}{19}$
- (B) $\frac{10}{19}$
- (C) $\frac{1}{2}$
- (D) $\frac{11}{20}$

#### Q8
$A$ and $B$ toss a fair coin alternately on the condition that the first one to throw a Head wins the wager. If $A$ tosses first, what is $A$'s probability of winning?
- (A) $\frac{1}{2}$
- (B) $\frac{2}{3}$
- (C) $\frac{3}{4}$
- (D) $\frac{4}{5}$

#### Q9
A bag contains $4$ white and $6$ black balls. Two balls are drawn at random without replacement. What is the probability that both balls are white?
- (A) $\frac{2}{15}$
- (B) $\frac{1}{5}$
- (C) $\frac{4}{15}$
- (D) $\frac{1}{3}$

#### Q10
In a software company, the probability that a server experiences downtime on any given day is $0.1$. Assuming independent daily operations, what is the probability that the server experiences downtime on at least one day during a 3-day operational sprint?
- (A) $0.271$
- (B) $0.297$
- (C) $0.300$
- (D) $0.331$

#### Q11
A diagnostic medical test for a rare disease has a sensitivity of $95\%$ (true positive) and a specificity of $90\%$ (true negative). The prevalence of the disease in the target population is $1\%$. If a patient tests positive, what is the posterior probability that the patient actually has the disease?
- (A) $8.76\%$
- (B) $9.50\%$
- (C) $10.25\%$
- (D) $12.50\%$

#### Q12
From a pack of $52$ cards, $2$ cards are drawn at random together. What is the probability that both are aces?
- (A) $\frac{1}{221}$
- (B) $\frac{1}{169}$
- (C) $\frac{2}{221}$
- (D) $\frac{1}{13}$

#### Q13
A fair die is thrown repeatedly until a $6$ appears. What is the probability that the number of throws required is an even number?
- (A) $\frac{5}{11}$
- (B) $\frac{6}{11}$
- (C) $\frac{1}{2}$
- (D) $\frac{5}{12}$

#### Q14
Seven persons seat themselves at random in a row. What is the probability that two designated individuals $X$ and $Y$ are seated adjacent to each other?
- (A) $\frac{1}{7}$
- (B) $\frac{2}{7}$
- (C) $\frac{3}{7}$
- (D) $\frac{1}{3}$

#### Q15
An anti-aircraft battery fires three independent interceptor missiles at an incoming threat drone. The hit probabilities of the three missiles are $0.4, 0.5,$ and $0.6$ respectively. What is the probability that the drone is intercepted by at least one missile?
- (A) $0.85$
- (B) $0.88$
- (C) $0.90$
- (D) $0.92$

---

## Complete Master Answer Key

| Q# | Answer | Governing Principle |
|:---:|:---:|:---|
| **Q1** | **B** | Outcomes summing to $>9$ (i.e. $10, 11, 12$): $(4,6),(5,5),(6,4),(5,6),(6,5),(6,6) \implies \frac{6}{36} = \frac{1}{6}$ |
| **Q2** | **A** | $P(K \cup H) = P(K) + P(H) - P(K \cap H) = \frac{4}{52} + \frac{13}{52} - \frac{1}{52} = \frac{16}{52} = \frac{4}{13}$ |
| **Q3** | **A** | $P(1R, 1G, 1B) = \frac{\binom{5}{1}\binom{4}{1}\binom{3}{1}}{\binom{12}{3}} = \frac{5 \times 4 \times 3}{220} = \frac{60}{220} = \frac{3}{11}$ |
| **Q4** | **C** | $P(\text{Solved}) = 1 - P(A' \cap B' \cap C') = 1 - (1/2 \times 2/3 \times 3/4) = 1 - 1/4 = \frac{3}{4}$ |
| **Q5** | **B** | Bayes: $P(M_2 \mid D) = \frac{0.40 \times 0.05}{(0.60 \times 0.02) + (0.40 \times 0.05)} = \frac{0.020}{0.012 + 0.020} = \frac{0.020}{0.032} = \frac{5}{8}$ |
| **Q6** | **A** | Binomial: $\binom{6}{4} (1/2)^4 (1/2)^2 = 15 \times \frac{1}{64} = \frac{15}{64}$ |
| **Q7** | **B** | Sum is odd iff 1 odd & 1 even: $P = \frac{\binom{10}{1}\binom{10}{1}}{\binom{20}{2}} = \frac{100}{190} = \frac{10}{19}$ |
| **Q8** | **B** | Geometric series: $P(A) = \frac{1}{2} + \frac{1}{8} + \frac{1}{32} + \dots = \frac{1/2}{1 - 1/4} = \frac{1/2}{3/4} = \frac{2}{3}$ |
| **Q9** | **A** | $P(2W) = \frac{\binom{4}{2}}{\binom{10}{2}} = \frac{6}{45} = \frac{2}{15}$ |
| **Q10** | **A** | $1 - (1 - 0.1)^3 = 1 - 0.9^3 = 1 - 0.729 = 0.271$ |
| **Q11** | **A** | $P(D \mid +) = \frac{0.01 \times 0.95}{(0.01 \times 0.95) + (0.99 \times 0.10)} = \frac{0.0095}{0.0095 + 0.0990} = \frac{0.0095}{0.1085} = 8.76\%$ |
| **Q12** | **A** | $\frac{\binom{4}{2}}{\binom{52}{2}} = \frac{6}{1326} = \frac{1}{221}$ |
| **Q13** | **A** | $P(\text{Even}) = q p + q^3 p + q^5 p + \dots = \frac{q p}{1 - q^2} = \frac{(5/6)(1/6)}{1 - 25/36} = \frac{5/36}{11/36} = \frac{5}{11}$ |
| **Q14** | **B** | Treat $(XY)$ as 1 unit: $\frac{6! \times 2!}{7!} = \frac{2}{7}$ |
| **Q15** | **B** | $1 - (1-0.4)(1-0.5)(1-0.6) = 1 - (0.6 \times 0.5 \times 0.4) = 1 - 0.12 = 0.88$ |

---

## Step-by-Step Solutions & Distractor Post-Mortem

#### Q1 Solution
- **Correct Option:** **(B) -- `1 / 6`**
- **Mathematical Proof:**
  - Sample space size $= 6 \times 6 = 36$.
  - Favorable sums $> 9$ ($10, 11, 12$):
    - Sum 10: $(4, 6), (5, 5), (6, 4)$ ($3$ pairs).
    - Sum 11: $(5, 6), (6, 5)$ ($2$ pairs).
    - Sum 12: $(6, 6)$ ($1$ pair).
  - Total favorable outcomes $= 3 + 2 + 1 = 6$.
  - Probability $= \frac{6}{36} = \frac{1}{6}$.
- **Distractor Analysis:**
  - Option (A) $1/9$ counts only 4 outcomes.

#### Q2 Solution
- **Correct Option:** **(A) -- `4 / 13`**
- **Mathematical Proof:**
  - Number of Kings $= 4$, Number of Hearts $= 13$.
  - King of Hearts is counted in both ($1$ card).
  - $n(K \cup H) = 4 + 13 - 1 = 16$.
  - $P(K \cup H) = \frac{16}{52} = \frac{4}{13}$.
- **Distractor Analysis:**
  - Option (B) $\frac{17}{52}$ forgets to subtract the intersection.

#### Q3 Solution
- **Correct Option:** **(A) -- `3 / 11`**
- **Mathematical Proof:**
  - Total balls $= 5 + 4 + 3 = 12$.
  - Total ways to draw 3 balls $= \binom{12}{3} = \frac{12 \times 11 \times 10}{6} = 220$.
  - Favorable ways (1 Red, 1 Green, 1 Blue) $= \binom{5}{1} \times \binom{4}{1} \times \binom{3}{1} = 5 \times 4 \times 3 = 60$.
  - Probability $= \frac{60}{220} = \frac{3}{11}$.
- **Distractor Analysis:**
  - Option (C) $\frac{9}{22}$ computes $\frac{90}{220}$.

#### Q4 Solution
- **Correct Option:** **(C) -- `3 / 4`**
- **Mathematical Proof:**
  - $P(\text{Problem Solved}) = 1 - P(\text{None Solves})$.
  - $P(\text{None Solves}) = (1 - 1/2)(1 - 1/3)(1 - 1/4) = \frac{1}{2} \times \frac{2}{3} \times \frac{3}{4} = \frac{1}{4}$.
  - $P(\text{Problem Solved}) = 1 - \frac{1}{4} = \frac{3}{4}$.
- **Distractor Analysis:**
  - Option (D) $5/6$ naively adds the individual probabilities without independence discounting.

#### Q5 Solution
- **Correct Option:** **(B) -- `5 / 8`**
- **Mathematical Proof:**
  - By Bayes' Theorem:
  - $P(M_2 \mid D) = \frac{P(M_2) P(D \mid M_2)}{P(M_1) P(D \mid M_1) + P(M_2) P(D \mid M_2)} = \frac{0.40 \times 0.05}{(0.60 \times 0.02) + (0.40 \times 0.05)} = \frac{0.020}{0.012 + 0.020} = \frac{0.020}{0.032} = \frac{5}{8}$.
- **Distractor Analysis:**
  - Option (A) $3/8$ calculates $P(M_1 \mid D)$.

#### Q6 Solution
- **Correct Option:** **(A) -- `15 / 64`**
- **Mathematical Proof:**
  - Binomial probability: $P(X = 4) = \binom{6}{4} p^4 q^{6-4} = 15 \times \left(\frac{1}{2}\right)^4 \left(\frac{1}{2}\right)^2 = \frac{15}{64}$.
- **Distractor Analysis:**
  - Option (B) $5/16 = \frac{20}{64}$ is $P(X = 3)$.

#### Q7 Solution
- **Correct Option:** **(B) -- `10 / 19`**
- **Mathematical Proof:**
  - Set has 10 odd and 10 even integers. Total ways to choose 2 $= \binom{20}{2} = 190$.
  - Sum is odd if and only if one is odd and one is even:
  - Favorable ways $= \binom{10}{1} \times \binom{10}{1} = 10 \times 10 = 100$.
  - Probability $= \frac{100}{190} = \frac{10}{19}$.
- **Distractor Analysis:**
  - Option (C) $1/2$ assumes replacement.

#### Q8 Solution
- **Correct Option:** **(B) -- `2 / 3`**
- **Mathematical Proof:**
  - $A$ wins if: $H$ on 1st toss, or $TTH$ on 3rd toss, or $TTTTH$ on 5th toss...
  - $P(A) = \frac{1}{2} + \left(\frac{1}{2}\right)^3 + \left(\frac{1}{2}\right)^5 + \dots$
  - Sum of infinite GP $= \frac{a}{1 - r} = \frac{1/2}{1 - 1/4} = \frac{1/2}{3/4} = \frac{2}{3}$.
- **Distractor Analysis:**
  - Option (A) $1/2$ assumes equal winning chances.

#### Q9 Solution
- **Correct Option:** **(A) -- `2 / 15`**
- **Mathematical Proof:**
  - $P(2W) = \frac{\binom{4}{2}}{\binom{10}{2}} = \frac{6}{45} = \frac{2}{15}$.
- **Distractor Analysis:**
  - Option (C) $4/15$ assumes replacement.

#### Q10 Solution
- **Correct Option:** **(A) -- `0.271`**
- **Mathematical Proof:**
  - $P(\text{At least 1 downtime}) = 1 - P(\text{No downtime in 3 days})$.
  - $P(\text{No downtime in 3 days}) = (1 - 0.1)^3 = (0.9)^3 = 0.729$.
  - $P = 1 - 0.729 = 0.271$.
- **Distractor Analysis:**
  - Option (C) $0.300$ is linear addition $0.1 \times 3$.

#### Q11 Solution
- **Correct Option:** **(A) -- `8.76%`**
- **Mathematical Proof:**
  - Prior $P(D) = 0.01 \implies P(D') = 0.99$.
  - $P(+ \mid D) = 0.95$, $P(+ \mid D') = 1 - 0.90 = 0.10$.
  - $P(D \mid +) = \frac{0.01 \times 0.95}{(0.01 \times 0.95) + (0.99 \times 0.10)} = \frac{0.0095}{0.0095 + 0.0990} = \frac{0.0095}{0.1085} \approx 0.087557 \implies 8.76\%$.
- **Distractor Analysis:**
  - Option (B) $9.50\%$ ignores the high false positive baseline of the large healthy cohort.

#### Q12 Solution
- **Correct Option:** **(A) -- `1 / 221`**
- **Mathematical Proof:**
  - $P(2\text{ Aces}) = \frac{\binom{4}{2}}{\binom{52}{2}} = \frac{6}{\frac{52 \times 51}{2}} = \frac{6}{1326} = \frac{1}{221}$.
- **Distractor Analysis:**
  - Option (B) $\frac{1}{169}$ is with replacement $\left(\frac{1}{13} \times \frac{1}{13}\right)$.

#### Q13 Solution
- **Correct Option:** **(A) -- `5 / 11`**
- **Mathematical Proof:**
  - $p = P(6) = \frac{1}{6}$, $q = P(\text{not } 6) = \frac{5}{6}$.
  - Even throws $\implies$ throw 2, throw 4, throw 6...
  - $P(\text{Even}) = q p + q^3 p + q^5 p + \dots = \frac{q p}{1 - q^2} = \frac{(5/6)(1/6)}{1 - 25/36} = \frac{5/36}{11/36} = \frac{5}{11}$.
- **Distractor Analysis:**
  - Option (B) $6/11$ is the odd throw probability.

#### Q14 Solution
- **Correct Option:** **(B) -- `2 / 7`**
- **Mathematical Proof:**
  - Total linear arrangements $= 7!$.
  - Bundle $(XY)$ as one entity: 6 units can be arranged in $6!$ ways, and $X, Y$ internally in $2!$ ways.
  - Probability $= \frac{6! \times 2!}{7!} = \frac{2}{7}$.
- **Distractor Analysis:**
  - Option (A) $1/7$ forgets internal permutation $2!$.

#### Q15 Solution
- **Correct Option:** **(B) -- `0.88`**
- **Mathematical Proof:**
  - $P(\text{Hit}) = 1 - P(\text{All Miss}) = 1 - (1 - 0.4)(1 - 0.5)(1 - 0.6) = 1 - (0.6 \times 0.5 \times 0.4) = 1 - 0.12 = 0.88$.
- **Distractor Analysis:**
  - Option (C) $0.90$ is an estimation slip.
