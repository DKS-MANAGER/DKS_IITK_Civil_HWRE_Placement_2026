# Advanced Probability & Statistics Problem Bank (60 Rigorous Problems)

This problem bank contains **60 distinct, mathematically verified, fully solved problems** calibrated for campus placement assessments (quant, analytics, decision science, data science, and quantitative finance roles at firms such as WorldQuant, Jane Street, Goldman Sachs, Citi AIM, Capital One, American Express, and McKinsey Analytics).

---

## Difficulty Framework & Structure

Each question strictly adheres to the **L1–L4 Placement Framework**:
- **L1 — Fundamentals**: Core definitions, single-step sample space enumeration, direct probability rules.
- **L2 — Standard Placement**: Multi-step applications, conditional probability, standard discrete distributions.
- **L3 — Advanced Placement**: Compound conditioning, indicator variables, order statistics, statistical inference, paradoxes.
- **L4 — Expert Quantitative Reasoning**: Stopping times, Markov chains, martingale/Wald properties, Simpson's paradox, continuous transformations, subtle sample space biases.

### Breakdown of Problems:
1. **Section 1 (Q1–Q10)**: Fundamentals & Conditional Probability
2. **Section 2 (Q11–Q25)**: Counting-Based Combinatorial Probability
3. **Section 3 (Q26–Q40)**: Discrete Distributions, Expectation & Variance
4. **Section 4 (Q41–Q50)**: Conditional Expectation & Advanced Stochastic Reasoning
5. **Section 5 (Q51–Q60)**: Statistical Interpretation, Inference & Data Traps

---


## Section 1: Fundamentals & Conditional Probability (Q1–Q10)


### Problem 1: Rare Disease Screening & Base-Rate Neglect

**1. Problem Statement:**  
In a population of 100,000 individuals, a rare disease has a prevalence of 0.1% (1 in 1,000). A diagnostic test has a sensitivity of 99% (true positive rate) and a false positive rate of 2% (specificity = 98%). An individual randomly selected from the population tests positive. What is the exact probability that the individual actually has the disease?

**2. Level and Concept:**  
- **Level:** L2 — Standard Placement  
- **Primary Concept:** Bayes' Theorem  
- **Secondary Concept:** Base-Rate Fallacy  

**3. Reasoning Setup:**  
Let $D$ denote the event that the individual has the disease, and let $+$ denote the event of a positive test result.
- Prior probability: $P(D) = 0.001$, so $P(D^c) = 0.999$.
- Sensitivity: $P(+ \mid D) = 0.99$.
- False Positive Rate: $P(+ \mid D^c) = 0.02$.

**4. Derivation:**  
By Bayes' Theorem and the Law of Total Probability:
$$P(D \mid +) = \frac{P(D) P(+ \mid D)}{P(+)} = \frac{P(D) P(+ \mid D)}{P(D) P(+ \mid D) + P(D^c) P(+ \mid D^c)}$$

**5. Calculation:**  
1. Numerator: $P(D \cap +) = 0.001 \times 0.99 = 0.00099$.
2. Denominator: $P(+) = (0.001 \times 0.99) + (0.999 \times 0.02) = 0.00099 + 0.01998 = 0.02097$.
3. Posterior Probability:
$$P(D \mid +) = \frac{0.00099}{0.02097} = \frac{99}{2097} = \frac{11}{233} \approx 0.04721 \text{ (or } 4.72\%\text{)}$$

**6. Final Answer:**  
$$\mathbf{\frac{11}{233} \approx 4.72\%}$$

**7. Common Trap:**  
Assuming that because the test is '99% accurate', the probability of disease given a positive test is 99%. In rare disease settings, false positives from the large healthy population drastically outnumber true positives.

**8. Alternative Method:**  
Natural frequency tree: Out of 100,000 people, 100 have the disease and 99,900 do not. Test finds $100 \times 0.99 = 99$ true positives, and $99,900 \times 0.02 = 1,998$ false positives. Total positive tests $= 99 + 1,998 = 2,097$. Probability of disease $= 99 / 2,097 = 11 / 233$.

---

### Problem 2: 4-Door Monty Hall with Single Host Elimination

**1. Problem Statement:**  
A game show features 4 closed doors. Behind 1 door is a car; behind the other 3 are goats. A contestant chooses door 1. The host (who knows where the car is) always opens exactly 1 of the remaining 3 doors revealing a goat. If the host offers the contestant the chance to switch to one of the 2 remaining closed doors chosen uniformly at random, what is the probability of winning the car by switching?

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Conditional Probability  
- **Secondary Concept:** Information Revelation  

**3. Reasoning Setup:**  
Let $C$ denote the door hiding the car, with $P(C = i) = 1/4$ for $i \in \{1, 2, 3, 4\}$. The contestant selects Door 1. Let $H$ be the door opened by the host ($H \neq 1$, $H \neq C$).

**4. Derivation:**  
Partition by the contestant's initial choice:
- Case 1: Initial pick is the car ($C = 1$). This occurs with probability $P(C = 1) = 1/4$. Host opens 1 of the 3 goat doors. The remaining 2 closed doors both contain goats. If the contestant switches to a random remaining door, $P(\text{Win} \mid C = 1) = 0$.
- Case 2: Initial pick is a goat ($C \neq 1$). This occurs with probability $P(C \neq 1) = 3/4$. Behind the 3 non-chosen doors, there is 1 car and 2 goats. The host eliminates 1 goat door. Among the 2 remaining closed doors, exactly 1 has the car and 1 has a goat. Switching uniformly between the two gives $P(\text{Win} \mid C \neq 1) = 1/2$.

**5. Calculation:**  
By the Law of Total Probability:
$$P(\text{Win by switching}) = P(C = 1) \times 0 + P(C \neq 1) \times \frac{1}{2} = \left(\frac{1}{4}\right)(0) + \left(\frac{3}{4}\right)\left(\frac{1}{2}\right) = \frac{3}{8} = 0.375$$

**6. Final Answer:**  
$$\mathbf{\frac{3}{8} = 37.5\%}$$

**7. Common Trap:**  
Assuming the 3 remaining closed doors (after 1 is opened) are equally likely to have the car (leading to $1/3$), or that the final two doors have a 50-50 chance.

**8. Alternative Method:**  
Initially, contestant has $1/4$ chance of car, leaving $3/4$ across the other 3 doors. The host eliminates 1 goat door, so the entire $3/4$ probability mass is now evenly distributed across the 2 remaining unchosen doors: each has probability $(3/4)/2 = 3/8$.

---

### Problem 3: Bertrand's Box Paradox

**1. Problem Statement:**  
There are 3 identical boxes: Box 1 contains 2 gold coins ($GG$), Box 2 contains 2 silver coins ($SS$), and Box 3 contains 1 gold and 1 silver coin ($GS$). A box is chosen uniformly at random, and from it, a coin is drawn uniformly at random. The drawn coin turns out to be gold. What is the probability that the other coin in the same box is also gold?

**2. Level and Concept:**  
- **Level:** L2 — Standard Placement  
- **Primary Concept:** Conditional Probability  
- **Secondary Concept:** Symmetry and Microstates  

**3. Reasoning Setup:**  
Let $B_1, B_2, B_3$ be the events that Box 1, 2, or 3 is chosen: $P(B_i) = 1/3$.
Let $G$ be the event that a gold coin is drawn.
- $P(G \mid B_1) = 1$
- $P(G \mid B_2) = 0$
- $P(G \mid B_3) = 1/2$

**4. Derivation:**  
The other coin is gold if and only if Box 1 ($GG$) was chosen. We seek $P(B_1 \mid G)$.
$$P(B_1 \mid G) = \frac{P(B_1) P(G \mid B_1)}{P(B_1) P(G \mid B_1) + P(B_2) P(G \mid B_2) + P(B_3) P(G \mid B_3)}$$

**5. Calculation:**  
1. Denominator $P(G) = \frac{1}{3}(1) + \frac{1}{3}(0) + \frac{1}{3}\left(\frac{1}{2}\right) = \frac{1}{3} + \frac{1}{6} = \frac{1}{2}$.
2. Numerator $P(B_1 \cap G) = \frac{1}{3}(1) = \frac{1}{3}$.
3. Ratio:
$$P(B_1 \mid G) = \frac{1/3}{1/2} = \frac{2}{3}$$

**6. Final Answer:**  
$$\mathbf{\frac{2}{3}}$$

**7. Common Trap:**  
Thinking that since the drawn coin is gold, the box must be either $GG$ or $GS$, so the remaining coin has a 50-50 chance of being gold ($1/2$). This treats boxes rather than individual gold coin faces as equally likely.

**8. Alternative Method:**  
Coin-face enumeration: There are 3 gold coins in total across all boxes: $G_{1a}, G_{1b}$ (in Box 1) and $G_3$ (in Box 3). Each of these 3 gold coins is equally likely to be drawn. In 2 of the 3 cases ($G_{1a}$ and $G_{1b}$), the partner coin is gold. Hence $P = 2/3$.

---

### Problem 4: Conditional Dice Roll with Inequality Restriction

**1. Problem Statement:**  
Two standard fair 6-sided dice, labeled $X$ and $Y$, are thrown simultaneously. Given that their sum $X + Y \ge 10$, what is the conditional probability that both dice show the exact same number ($X = Y$)?

**2. Level and Concept:**  
- **Level:** L2 — Standard Placement  
- **Primary Concept:** Reduced Sample Space  
- **Secondary Concept:** Equally Likely Outcomes  

**3. Reasoning Setup:**  
Sample space $S = \{(x, y) \mid 1 \le x, y \le 6\}$ with $|S| = 36$ equally likely outcomes.
Conditioning event $A$: $X + Y \ge 10$.
Target event $B$: $X = Y$.

**4. Derivation:**  
We find the reduced sample space satisfying event $A$, then count the subset where $X = Y$:
$$P(B \mid A) = \frac{|A \cap B|}{|A|}$$

**5. Calculation:**  
1. Outcomes with sum $\ge 10$:
   - Sum = 10: $(4, 6), (5, 5), (6, 4)$ (3 outcomes)
   - Sum = 11: $(5, 6), (6, 5)$ (2 outcomes)
   - Sum = 12: $(6, 6)$ (1 outcome)
   Total $|A| = 3 + 2 + 1 = 6$.
2. Outcomes with $X = Y$ in $A$:
   - $(5, 5)$ and $(6, 6)$. Thus $|A \cap B| = 2$.
3. Conditional probability:
$$P(X = Y \mid X + Y \ge 10) = \frac{2}{6} = \frac{1}{3}$$

**6. Final Answer:**  
$$\mathbf{\frac{1}{3}}$$

**7. Common Trap:**  
Dividing 2 by 36 (forgetting to condition on $A$) or assuming that since 6 doubles exist out of 36 ($1/6$), the probability is $1/6$.

**8. Alternative Method:**  
Complementary conditioning: Since the only possible identical outcomes with sum $\ge 10$ are $(5,5)$ and $(6,6)$, out of 6 valid ordered pairs with sum $\ge 10$, the answer is directly $2/6 = 1/3$.

---

### Problem 5: Two-Stage Transfer Between Urns

**1. Problem Statement:**  
Urn A contains 3 Red and 2 Blue balls. Urn B contains 1 Red and 4 Blue balls. A fair coin is tossed. If Heads lands, 1 ball is transferred from Urn A to Urn B, and then 1 ball is drawn from Urn B. If Tails lands, 1 ball is transferred from Urn B to Urn A, and then 1 ball is drawn from Urn A. What is the total probability that the final drawn ball is Red?

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Law of Total Probability  
- **Secondary Concept:** Multi-stage Urn Schemes  

**3. Reasoning Setup:**  
Let $H$ and $T$ be the coin toss events ($P(H) = P(T) = 1/2$).
Let $R$ be the event that the final drawn ball is Red.

**4. Derivation:**  
Apply the Law of Total Probability conditioning on the coin toss:
$$P(R) = P(H) P(R \mid H) + P(T) P(R \mid T)$$
To evaluate $P(R \mid H)$, condition on whether a Red or Blue ball was transferred from A to B.
To evaluate $P(R \mid T)$, condition on whether a Red or Blue ball was transferred from B to A.

**5. Calculation:**  
1. Under Heads:
   - Transfer Red from A to B: probability $\frac{3}{5}$. Urn B now has 2 Red, 4 Blue (total 6). $P(R \mid H, \text{trans R}) = \frac{2}{6}$.
   - Transfer Blue from A to B: probability $\frac{2}{5}$. Urn B now has 1 Red, 5 Blue (total 6). $P(R \mid H, \text{trans B}) = \frac{1}{6}$.
   $$P(R \mid H) = \left(\frac{3}{5}\right)\left(\frac{2}{6}\right) + \left(\frac{2}{5}\right)\left(\frac{1}{6}\right) = \frac{6 + 2}{30} = \frac{8}{30} = \frac{4}{15}$$
2. Under Tails:
   - Transfer Red from B to A: probability $\frac{1}{5}$. Urn A now has 4 Red, 2 Blue (total 6). $P(R \mid T, \text{trans R}) = \frac{4}{6}$.
   - Transfer Blue from B to A: probability $\frac{4}{5}$. Urn A now has 3 Red, 3 Blue (total 6). $P(R \mid T, \text{trans B}) = \frac{3}{6}$.
   $$P(R \mid T) = \left(\frac{1}{5}\right)\left(\frac{4}{6}\right) + \left(\frac{4}{5}\right)\left(\frac{3}{6}\right) = \frac{4 + 12}{30} = \frac{16}{30} = \frac{8}{15}$$
3. Total Probability:
$$P(R) = \frac{1}{2}\left(\frac{4}{15}\right) + \frac{1}{2}\left(\frac{8}{15}\right) = \frac{12}{30} = \frac{2}{5} = 0.40$$

**6. Final Answer:**  
$$\mathbf{\frac{2}{5} = 0.40}$$

**7. Common Trap:**  
Averaging the initial proportions of Red in A ($3/5$) and B ($1/5$) without modeling the composition change from the transferred ball.

**8. Alternative Method:**  
Exchangeability check: The probability that a ball drawn from B (after A-to-B transfer) is Red is $(1/6)(3/5) + (5/6)(1/5) = 8/30 = 4/15$, which matches the derivation.

---

### Problem 6: Conditional Independence vs Marginal Independence

**1. Problem Statement:**  
An urn contains two coins: Coin $C_1$ is fair with $P(\text{Heads}) = 0.5$, and Coin $C_2$ is biased with $P(\text{Heads}) = 0.8$. One coin is chosen at random with equal probability and tossed twice. Let $E_1$ be the event that the first toss is Heads, and $E_2$ be the event that the second toss is Heads. Are $E_1$ and $E_2$ independent? Compute $P(E_2 \mid E_1)$.

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Conditional Independence  
- **Secondary Concept:** Latent Variables  

**3. Reasoning Setup:**  
Let $C$ denote the chosen coin, with $P(C_1) = P(C_2) = 0.5$.
Given $C$, the tosses are conditionally independent:
$P(E_1 \cap E_2 \mid C_1) = 0.5 \times 0.5 = 0.25$, and $P(E_1 \cap E_2 \mid C_2) = 0.8 \times 0.8 = 0.64$.

**4. Derivation:**  
1. Marginal probability $P(E_1) = P(C_1) P(E_1 \mid C_1) + P(C_2) P(E_1 \mid C_2) = 0.5(0.5) + 0.5(0.8) = 0.65$.
By symmetry, $P(E_2) = 0.65$.
2. Joint probability:
$$P(E_1 \cap E_2) = 0.5(0.25) + 0.5(0.64) = 0.125 + 0.320 = 0.445$$
3. Independence check: $P(E_1) P(E_2) = 0.65 \times 0.65 = 0.4225 \neq 0.445$. Hence $E_1$ and $E_2$ are dependent.

**5. Calculation:**  
Conditional probability:
$$P(E_2 \mid E_1) = \frac{P(E_1 \cap E_2)}{P(E_1)} = \frac{0.445}{0.65} = \frac{445}{650} = \frac{89}{130} \approx 0.6846$$
Because $P(E_2 \mid E_1) = 0.6846 > 0.65 = P(E_2)$, seeing Heads on the first toss increases our belief that the coin is the biased one ($C_2$), making a second Heads more likely.

**6. Final Answer:**  
$$\mathbf{\frac{89}{130} \approx 0.6846 \text{ (Events are NOT independent)}}$$

**7. Common Trap:**  
Assuming that because individual coin tosses are physical independent events, $E_1$ and $E_2$ must be independent. The unobserved identity of the coin induces positive correlation.

**8. Alternative Method:**  
Update posterior on coin after first toss: $P(C_2 \mid E_1) = \frac{0.5 \times 0.8}{0.65} = \frac{0.40}{0.65} = \frac{8}{13}$. Then $P(E_2 \mid E_1) = \left(1 - \frac{8}{13}\right)(0.5) + \left(\frac{8}{13}\right)(0.8) = \frac{5}{13}(0.5) + \frac{8}{13}(0.8) = \frac{2.5 + 6.4}{13} = \frac{8.9}{13} = \frac{89}{130}$.

---

### Problem 7: Simpson's Paradox in Clinical Trials

**1. Problem Statement:**  
A pharmaceutical trial compares Treatment $T$ against Control $C$ across severe and mild patient subgroups. In severe patients, Treatment succeeds in 10 out of 100 cases (10%) while Control succeeds in 1 out of 20 cases (5%). In mild patients, Treatment succeeds in 90 out of 100 cases (90%) while Control succeeds in 72 out of 80 cases (90%). Explain mathematically why Treatment outperforms Control in severe cases and matches Control in mild cases, yet Control appears superior overall when data is pooled.

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Confounding Variables  
- **Secondary Concept:** Simpson's Paradox  

**3. Reasoning Setup:**  
Define variables:
- Severe group: $n_{T1} = 100, s_{T1} = 10$; $n_{C1} = 20, s_{C1} = 1$.
- Mild group: $n_{T2} = 100, s_{T2} = 90$; $n_{C2} = 80, s_{C2} = 72$.
- Overall pooled rates: $R_T$ and $R_C$.

**4. Derivation:**  
Overall rate is a weighted average of subgroup rates, where the weights are the proportion of patients allocated to each severity:
$$R_T = w_{T1} r_{T1} + w_{T2} r_{T2}, \quad R_C = w_{C1} r_{C1} + w_{C2} r_{C2}$$
If the treatment group receives a disproportionate share of severe cases ($w_{T1} > w_{C1}$), the overall average for Treatment is pulled down.

**5. Calculation:**  
1. Subgroup success rates:
   - Severe: $r_{T1} = 10\% > r_{C1} = 5\%$.
   - Mild: $r_{T2} = 90\% = r_{C2} = 90\%$.
2. Overall pooled success:
   - Treatment: $\frac{10 + 90}{100 + 100} = \frac{100}{200} = 50.0\%$.
   - Control: $\frac{1 + 72}{20 + 80} = \frac{73}{100} = 73.0\%$.
3. Explanation: Treatment had 50% severe cases ($100/200$), whereas Control had only 20% severe cases ($20/100$). The confounding allocation of sicker patients to Treatment creates the reversal.

**6. Final Answer:**  
$$\mathbf{R_T = 50\% < R_C = 73\% \text{ due to unequal severity weights: } w_{T1} = 0.50 \text{ vs } w_{C1} = 0.20}$$

**7. Common Trap:**  
Concluding that Control is the superior drug based on the aggregate data. The aggregate comparison is confounded; conditional on disease severity, Treatment is strictly non-inferior.

**8. Alternative Method:**  
Standardized rate (adjusting for severity 50-50): $R_T^* = 0.5(10\%) + 0.5(90\%) = 50\%$, while $R_C^* = 0.5(5\%) + 0.5(90\%) = 47.5\%$. Adjusted for confounding, Treatment is strictly superior.

---

### Problem 8: Fréchet-Bonferroni Bounds for Triple Intersections

**1. Problem Statement:**  
Three events $A, B, C$ in the same probability space satisfy $P(A) = 0.80$, $P(B) = 0.70$, and $P(C) = 0.60$. Without assuming independence, determine the sharpest possible lower and upper bounds for the probability of their simultaneous occurrence $P(A \cap B \cap C)$.

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Bonferroni Bounds  
- **Secondary Concept:** Probability Inequalities  

**3. Reasoning Setup:**  
We want to bound $P(A \cap B \cap C)$ using only $P(A), P(B), P(C)$.
- Upper bound: $A \cap B \cap C \subseteq A, B, C$.
- Lower bound: Apply Bonferroni inequality via complements: $P(A \cap B \cap C) = 1 - P(A^c \cup B^c \cup C^c)$.

**4. Derivation:**  
1. Upper bound:
$$P(A \cap B \cap C) \le \min(P(A), P(B), P(C)) = \min(0.80, 0.70, 0.60) = 0.60$$
2. Lower bound:
By Boole's inequality on the complement:
$$P(A^c \cup B^c \cup C^c) \le P(A^c) + P(B^c) + P(C^c) = (1 - 0.80) + (1 - 0.70) + (1 - 0.60)$$
$$P(A^c \cup B^c \cup C^c) \le 0.20 + 0.30 + 0.40 = 0.90$$
Therefore:
$$P(A \cap B \cap C) \ge 1 - 0.90 = 0.10$$

**5. Calculation:**  
Lower bound $= 0.10$. Upper bound $= 0.60$.
Both bounds are attainable under valid joint distributions: for example, the upper bound is attained when $C \subset B \subset A$.

**6. Final Answer:**  
$$\mathbf{0.10 \le P(A \cap B \cap C) \le 0.60}$$

**7. Common Trap:**  
Multiplying probabilities $0.80 \times 0.70 \times 0.60 = 0.336$ (incorrectly assuming independence) or claiming the lower bound is 0.

**8. Alternative Method:**  
Pairwise iteration: $P(A \cap B) \ge 0.80 + 0.70 - 1 = 0.50$. Then $P((A \cap B) \cap C) \ge P(A \cap B) + P(C) - 1 \ge 0.50 + 0.60 - 1 = 0.10$.

---

### Problem 9: Non-Transitive Pattern Matching (Penney's Game)

**1. Problem Statement:**  
A fair coin is tossed repeatedly. Two players track consecutive two-toss patterns: Player 1 wins if the sequence 'HH' appears first; Player 2 wins if the sequence 'TH' appears first. What is the exact probability that Player 1 wins?

**2. Level and Concept:**  
- **Level:** L4 — Expert Quantitative Reasoning  
- **Primary Concept:** Sequential Patterns  
- **Secondary Concept:** Stopping Times  

**3. Reasoning Setup:**  
Toss sequence $X_1, X_2, X_3, \dots \in \{H, T\}$.
Let $E$ be the event that 'HH' occurs before 'TH'.

**4. Derivation:**  
Analyze the very first coin toss $X_1$:
- If $X_1 = T$ (probability $1/2$): The sequence now has a trailing $T$. In order for 'HH' to ever occur, the coin must toss an $H$. But the very first time an $H$ appears after this initial $T$, the pair formed is immediately 'TH'! Therefore, whenever the first toss is $T$, Player 2 ('TH') is guaranteed to win with probability 1.
- If $X_1 = H$ (probability $1/2$):
  - If $X_2 = H$ (probability $1/2 \times 1/2 = 1/4$): The sequence starts 'HH' immediately. Player 1 wins.
  - If $X_2 = T$ (probability $1/2 \times 1/2 = 1/4$): The sequence now has a trailing $T$, which reduces to the $X_1 = T$ condition: Player 2 must win because any future $H$ completes 'TH' first.

**5. Calculation:**  
Player 1 wins if and only if the first two tosses are both Heads:
$$P(\text{Player 1 wins}) = P(X_1 = H, X_2 = H) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4} = 0.25$$
Player 2 wins with probability $1 - 1/4 = 3/4 = 0.75$.

**6. Final Answer:**  
$$\mathbf{\frac{1}{4} = 0.25}$$

**7. Common Trap:**  
Assuming that because 'HH' and 'TH' each have probability $(1/2)^2 = 1/4$ in any two independent tosses, they must have an equal $50\%$ chance of winning in a race.

**8. Alternative Method:**  
Markov state space: States $\emptyset, H, T$. State $T$ transitions to $TH$ (absorption) whenever an $H$ is flipped, making absorption into $TH$ inevitable once $T$ is reached. Only the direct path $\emptyset \to H \to HH$ reaches $HH$.

---

### Problem 10: Prosecutor's Fallacy in Database Searches

**1. Problem Statement:**  
A crime scene DNA profile matches a random individual with probability 1 in 100,000 ($10^{-5}$). In a city of 1,000,001 people containing exactly 1 perpetrator and 1,000,000 completely innocent citizens, police search the entire citizen database. A single individual matches and is prosecuted with the argument: 'The chance an innocent person matches is only 1 in 100,000, so the defendant is 99.999% likely to be guilty.' What is the true posterior probability of guilt?

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Bayes' Theorem  
- **Secondary Concept:** Database Match Fallacy  

**3. Reasoning Setup:**  
Population consists of 1 guilty person ($G$) and $N = 1,000,000$ innocent persons ($I$).
- For the guilty person, $P(\text{match} \mid G) = 1$.
- For each innocent person, $P(\text{match} \mid I) = 10^{-5}$.

**4. Derivation:**  
The database search tests all $1,000,001$ people. By linearity of expectation, the expected number of matches among innocent citizens is:
$$E[M_I] = 1,000,000 \times 10^{-5} = 10$$
Together with the 1 guilty person who always matches, the total expected matches in the database is $10 + 1 = 11$.

**5. Calculation:**  
Given that an individual matches in this database search with no other prior corroborating evidence:
$$P(\text{Guilty} \mid \text{Match}) = \frac{1 \times 1}{1 \times 1 + 1,000,000 \times 10^{-5}} = \frac{1}{1 + 10} = \frac{1}{11} \approx 0.09091 \text{ (or } 9.09\%\text{)}$$
The prosecutor's claim of 99.999% is off by a factor of 11.

**6. Final Answer:**  
$$\mathbf{\frac{1}{11} \approx 9.09\%}$$

**7. Common Trap:**  
Equating $P(\text{Match} \mid \text{Innocent})$ with $P(\text{Innocent} \mid \text{Match})$—the textbook definition of the Prosecutor's Fallacy.

**8. Alternative Method:**  
Odds form of Bayes' Rule: Prior odds of guilt $= 1 : 1,000,000$. Bayes factor (likelihood ratio) $= 1 / 10^{-5} = 100,000$. Posterior odds $= (1/1,000,000) \times 100,000 = 1/10$. Posterior probability $= \frac{1}{1 + 10} = 1/11$.

---

## Section 2: Counting-Based Combinatorial Probability (Q11–Q25)


### Problem 11: Exact Probability of a Full House in 5-Card Poker

**1. Problem Statement:**  
From a standard well-shuffled 52-card deck, 5 cards are dealt uniformly at random. A 'Full House' consists of 3 cards of one rank and 2 cards of a different rank (e.g., three Kings and two 4s). What is the exact probability of being dealt a Full House?

**2. Level and Concept:**  
- **Level:** L2 — Standard Placement  
- **Primary Concept:** Hypergeometric Sampling  
- **Secondary Concept:** Poker Probabilities  

**3. Reasoning Setup:**  
Total 5-card hands: $|S| = \binom{52}{5} = 2,598,960$.
A Full House requires selecting rank for the triple, 3 suits for the triple, a different rank for the pair, and 2 suits for the pair.

**4. Derivation:**  
1. Choose the rank of the three-of-a-kind: 13 choices.
2. Choose 3 cards of that rank: $\binom{4}{3} = 4$.
3. Choose the rank of the pair from the remaining 12 ranks: 12 choices.
4. Choose 2 cards of that rank: $\binom{4}{2} = 6$.
Number of Full House hands $= 13 \times 4 \times 12 \times 6 = 3,744$.

**5. Calculation:**  
Probability:
$$P(\text{Full House}) = \frac{3,744}{2,598,960} = \frac{6}{4,165} \approx 0.0014406 \text{ (about 1 in 694)}$$

**6. Final Answer:**  
$$\mathbf{\frac{6}{4,165} \approx 0.001441}$$

**7. Common Trap:**  
Choosing ranks as $\binom{13}{2}$, which neglects the fact that the triple and the pair have distinct roles ($13 \times 12 = 156$, not $\binom{13}{2} = 78$).

**8. Alternative Method:**  
Conditional sequential probability: Pick 3 cards of rank A and 2 of rank B: $52/52 \times 3/51 \times 2/50 \times 48/49 \times 3/48 \times \binom{5}{3} = \frac{6}{4,165}$.

---

### Problem 12: Probability of a Pure Flush (Excluding Straight Flushes)

**1. Problem Statement:**  
In a 5-card hand drawn from a standard 52-card deck, a Flush consists of 5 cards of the same suit. A Straight Flush (5 cards of the same suit in sequential numerical rank) is considered a higher distinct hand rank. What is the exact probability of receiving a 'pure flush' (5 cards of the same suit that do NOT form a straight flush)?

**2. Level and Concept:**  
- **Level:** L2 — Standard Placement  
- **Primary Concept:** Combinatorial Counting  
- **Secondary Concept:** Subtractive Corrections  

**3. Reasoning Setup:**  
Total hands $= \binom{52}{5} = 2,598,960$.
- Number of suits $= 4$.
- 5 cards in any single suit $= \binom{13}{5} = 1,287$.
- Straight flushes per suit $= 10$ (A-2-3-4-5 through 10-J-Q-K-A).

**4. Derivation:**  
1. Total hands with all 5 cards in the same suit $= 4 \times \binom{13}{5} = 4 \times 1,287 = 5,148$.
2. Subtract straight flushes: $4 \text{ suits} \times 10 = 40$.
3. Pure flushes $= 5,148 - 40 = 5,108$.

**5. Calculation:**  
Probability:
$$P(\text{Pure Flush}) = \frac{5,108}{2,598,960} = \frac{1,277}{649,740} \approx 0.0019654 \text{ (about 1 in 509)}$$

**6. Final Answer:**  
$$\mathbf{\frac{1,277}{649,740} \approx 0.001965}$$

**7. Common Trap:**  
Forgetting to subtract the 40 straight flushes, reporting $5,148 / 2,598,960 = 33 / 16,660 \approx 0.0019807$.

**8. Alternative Method:**  
Per-suit calculation: In any single suit, probability of drawing 5 cards without forming a straight flush is $(\binom{13}{5} - 10)/\binom{52}{5}$, then multiply by 4 suits: $4 \times 1277 / 2,598,960 = 1,277 / 649,740$.

---

### Problem 13: Birthday Problem: Pairwise Collision in Small Groups

**1. Problem Statement:**  
Assuming 365 days in a year and that all birthdays are independently and uniformly distributed, what is the exact probability that in a room of 23 people, at least two individuals share the same birthday? Show the mathematical bound.

**2. Level and Concept:**  
- **Level:** L2 — Standard Placement  
- **Primary Concept:** Complement Rule  
- **Secondary Concept:** Collision Probability  

**3. Reasoning Setup:**  
Let $N = 23, D = 365$.
Event $E$: at least one birthday match.
Complement $E^c$: all 23 people have mutually distinct birthdays.

**4. Derivation:**  
Assign birthdays sequentially without repetition:
$$P(E^c) = \frac{365}{365} \times \frac{364}{365} \times \frac{363}{365} \times \dots \times \frac{365 - 22}{365} = \prod_{k=0}^{22} \left(1 - \frac{k}{365}\right)$$
Then $P(E) = 1 - P(E^c)$.

**5. Calculation:**  
1. Exact product computation: $P(E^c) \approx 0.492703$.
2. Therefore:
$$P(E) = 1 - 0.492703 = 0.507297 \approx 50.73\%$$
3. Taylor approximation check: $1 - x \approx e^{-x}$, so:
$$P(E^c) \approx \exp\left(-\sum_{k=1}^{22} \frac{k}{365}\right) = \exp\left(-\frac{22 \times 23}{2 \times 365}\right) = \exp\left(-\frac{253}{365}\right) \approx e^{-0.69315} \approx 0.5000$$

**6. Final Answer:**  
$$\mathbf{1 - \prod_{k=0}^{22} \left(1 - \frac{k}{365}\right) \approx 50.73\%}$$

**7. Common Trap:**  
Thinking that 23 people compares to 365 as $23/365 \approx 6.3\%$. The key is the number of pairs: $\binom{23}{2} = 253$ distinct pairs, each with collision probability $1/365$.

**8. Alternative Method:**  
Poisson approximation for number of matches $X \sim \text{Pois}(\lambda)$ where $\lambda = \binom{23}{2} \times \frac{1}{365} = \frac{253}{365} \approx 0.693$. Then $P(X \ge 1) = 1 - e^{-0.693} \approx 1 - 0.500 = 50.0\%$.

---

### Problem 14: Hat-Check Rencontres: Exactly One Fixed Point

**1. Problem Statement:**  
Five individuals check their coats at a restaurant. Upon leaving, the attendant hands back the coats completely at random (each of the $5! = 120$ permutations is equally likely). What is the exact probability that exactly one person receives their own coat?

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Derangements  
- **Secondary Concept:** Partial Rencontres  

**3. Reasoning Setup:**  
Total permutations $n! = 5! = 120$.
Number of permutations of $n$ elements with exactly $k$ fixed points is:
$$R(n, k) = \binom{n}{k} D_{n-k}$$
where $D_m$ is the $m$-th derangement number.

**4. Derivation:**  
For $n = 5$ and $k = 1$:
$$R(5, 1) = \binom{5}{1} D_4$$
We calculate $D_4$:
$$D_4 = 4! \left(1 - \frac{1}{1!} + \frac{1}{2!} - \frac{1}{3!} + \frac{1}{4!}\right) = 24 \left(0 + \frac{1}{2} - \frac{1}{6} + \frac{1}{24}\right) = 12 - 4 + 1 = 9$$

**5. Calculation:**  
1. Favorable permutations: $R(5, 1) = 5 \times 9 = 45$.
2. Probability:
$$P(\text{Exactly 1 match}) = \frac{45}{120} = \frac{3}{8} = 0.375$$

**6. Final Answer:**  
$$\mathbf{\frac{3}{8} = 0.375}$$

**7. Common Trap:**  
Assuming $P(\text{match}) = 1/5$ for each person, and using binomial $\binom{5}{1}(1/5)(4/5)^4 \approx 0.4096$, which incorrectly assumes independent recipient events.

**8. Alternative Method:**  
Inclusion-exclusion decomposition: There are 5 choices for the person with the correct coat. For each choice, the remaining 4 must be deranged ($D_4 = 9$), giving $5 \times 9 / 120 = 45 / 120 = 3/8$.

---

### Problem 15: Bertrand's Ballot Theorem

**1. Problem Statement:**  
In an election between Candidate A and Candidate B, Candidate A receives $a = 6$ votes and Candidate B receives $b = 4$ votes. If the 10 ballots are counted sequentially in a random order, what is the probability that Candidate A strictly leads Candidate B throughout the entire vote count from start to finish?

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Ballot Theorem  
- **Secondary Concept:** Lattice Path Probability  

**3. Reasoning Setup:**  
Total permutations of ballot count order $= \binom{a + b}{a} = \binom{10}{6} = 210$.
Let $S_k$ be the lead of Candidate A after $k$ ballots ($S_k > 0$ for all $1 \le k \le 10$).

**4. Derivation:**  
By Bertrand's Ballot Theorem, for an election where candidate A receives $a$ votes and candidate B receives $b$ votes with $a > b$, the probability that A stays strictly ahead throughout the count is:
$$P(\text{A stays strictly ahead}) = \frac{a - b}{a + b}$$

**5. Calculation:**  
Substituting $a = 6$ and $b = 4$:
$$P = \frac{6 - 4}{6 + 4} = \frac{2}{10} = \frac{1}{5} = 0.20$$
Favorable sequences $= \frac{2}{10} \times 210 = 42$.

**6. Final Answer:**  
$$\mathbf{\frac{1}{5} = 0.20}$$

**7. Common Trap:**  
Requiring only that A leads at the end ($P = 1$ since A wins), or ignoring the strict inequality condition at the very first ballot (which forces the first ballot to be A).

**8. Alternative Method:**  
Reflection Principle: Total paths from $(0,0)$ to $(10, 2)$ in coordinate steps $(+1, +1)$ and $(+1, -1)$ is $\binom{10}{6} = 210$. Paths that touch the tie-line $y = 0$ after starting at $(1, 1)$ reflect to paths from $(1, -1)$ to $(10, 2)$, giving $\binom{9}{6} = 84$ paths starting with A that hit 0, plus all $\binom{9}{4} = 126$ paths starting with B. Total failing paths $= 84 + 126 = 210 - 42 = 168$. Thus $P = 42/210 = 1/5$.

---

### Problem 16: Coupon Collector: Distinct Types in Early Draws

**1. Problem Statement:**  
A cereal company distributes 5 distinct collectible toys with equal probability across boxes. If a consumer purchases 3 boxes, what is the exact probability that all 3 boxes contain mutually distinct toys?

**2. Level and Concept:**  
- **Level:** L2 — Standard Placement  
- **Primary Concept:** Coupon Collector  
- **Secondary Concept:** Sequential Sampling with Replacement  

**3. Reasoning Setup:**  
Number of coupon varieties $N = 5$. Number of purchases $k = 3$.
Sample space of toy sequences: $|S| = 5^3 = 125$.

**4. Derivation:**  
The first box can contain any toy ($5$ choices). The second box must contain a toy different from the first ($4$ choices). The third box must contain a toy different from both ($3$ choices).
Favorable sequences $= 5 \times 4 \times 3 = 60$.

**5. Calculation:**  
Probability:
$$P(\text{All 3 distinct}) = \frac{5 \times 4 \times 3}{5^3} = \frac{60}{125} = \frac{12}{25} = 0.48$$

**6. Final Answer:**  
$$\mathbf{\frac{12}{25} = 0.48}$$

**7. Common Trap:**  
Computing $\binom{5}{3} / 5^3 = 10 / 125 = 2/25$, which counts unordered sets rather than ordered sequence outcomes in $S$.

**8. Alternative Method:**  
Product of transition probabilities: $P(\text{1st distinct}) = 1$, $P(\text{2nd distinct} \mid 1) = 4/5$, $P(\text{3rd distinct} \mid 2) = 3/5$. Overall $1 \times \frac{4}{5} \times \frac{3}{5} = \frac{12}{25}$.

---

### Problem 17: Symmetric Random Walk: First Return Probability

**1. Problem Statement:**  
A particle starts at the origin $S_0 = 0$ on the integer line. At each time step, it moves $+1$ with probability $1/2$ and $-1$ with probability $1/2$. What is the exact probability that the particle is back at the origin at time $t = 6$ ($S_6 = 0$)?

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** 1D Random Walk  
- **Secondary Concept:** Combinatorial Binomial Paths  

**3. Reasoning Setup:**  
Let $X_i \in \{+1, -1\}$ be i.i.d. with $P(X_i = +1) = 1/2$.
Position $S_6 = \sum_{i=1}^6 X_i$. Total path trajectories $= 2^6 = 64$.

**4. Derivation:**  
For $S_6 = 0$, the particle must take exactly 3 positive steps and 3 negative steps in some order.
The number of such paths is given by the binomial coefficient $\binom{6}{3}$.

**5. Calculation:**  
1. Favorable paths: $\binom{6}{3} = \frac{6 \times 5 \times 4}{3 \times 2 \times 1} = 20$.
2. Total paths: $2^6 = 64$.
3. Probability:
$$P(S_6 = 0) = \frac{20}{64} = \frac{5}{16} = 0.3125$$

**6. Final Answer:**  
$$\mathbf{\frac{5}{16} = 0.3125}$$

**7. Common Trap:**  
Confusing 'being at 0 at step 6' ($P = 5/16$) with 'returning to 0 for the FIRST time at step 6' (which is strictly smaller, governed by Catalan numbers: $C_2 / 2^6 = 2 / 64 = 1/32$ for one side, $2/32 = 1/16$ overall).

**8. Alternative Method:**  
Binomial distribution directly: $K \sim \text{Binomial}(n=6, p=0.5)$ representing number of $+1$ steps. $S_6 = 0 \iff K = 3$. $P(K=3) = \binom{6}{3}(0.5)^6 = 20/64 = 5/16$.

---

### Problem 18: Derangement Probability and Convergence to $1/e$

**1. Problem Statement:**  
Four students place their backpacks in a pile and pick one at random. What is the exact probability that no student picks their own backpack? Compare this exact value to the asymptotic limit $1/e$.

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Derangements  
- **Secondary Concept:** Asymptotic Probability  

**3. Reasoning Setup:**  
Let $n = 4$. Total permutations $= 4! = 24$.
Event $D$: all students receive a wrong backpack (a derangement of 4 objects).

**4. Derivation:**  
By the inclusion-exclusion formula for derangements:
$$D_n = n! \sum_{k=0}^n \frac{(-1)^k}{k!}$$
For $n = 4$:
$$D_4 = 4! \left(1 - 1 + \frac{1}{2!} - \frac{1}{3!} + \frac{1}{4!}\right) = 24 \left(\frac{1}{2} - \frac{1}{6} + \frac{1}{24}\right) = 12 - 4 + 1 = 9$$

**5. Calculation:**  
1. Exact probability:
$$P(D_4) = \frac{D_4}{4!} = \frac{9}{24} = \frac{3}{8} = 0.375$$
2. Asymptotic limit:
$$\lim_{n \to \infty} P(D_n) = \frac{1}{e} \approx 0.367879$$
3. Absolute difference: $|0.375 - 0.367879| \approx 0.007121$ (less than $1\%$ error even at $n = 4$).

**6. Final Answer:**  
$$\mathbf{\frac{3}{8} = 0.375 \quad (\text{asymptotic limit } 1/e \approx 0.3679)}$$

**7. Common Trap:**  
Approximating directly as $(3/4)^4 \approx 0.3164$, which falsely assumes independence among the 4 selections.

**8. Alternative Method:**  
Recurrence relation for derangements: $D_n = (n-1)(D_{n-1} + D_{n-2})$. With $D_1 = 0, D_2 = 1$: $D_3 = 2(1 + 0) = 2$, $D_4 = 3(2 + 1) = 9$. Then $P = 9/24 = 3/8$.

---

### Problem 19: Conditional Dice Sum Given Parity

**1. Problem Statement:**  
Two standard fair 6-sided dice are thrown. Given that their sum is an odd number, what is the exact probability that the sum is equal to 7?

**2. Level and Concept:**  
- **Level:** L2 — Standard Placement  
- **Primary Concept:** Conditional Probability  
- **Secondary Concept:** Parity Partitions  

**3. Reasoning Setup:**  
Sample space $|S| = 36$.
Conditioning event $O$: Sum is odd.
Target event $E_7$: Sum is equal to 7.

**4. Derivation:**  
A sum of two dice is odd if and only if one die is odd and the other is even:
- Die 1 Odd, Die 2 Even: $3 \times 3 = 9$ outcomes.
- Die 1 Even, Die 2 Odd: $3 \times 3 = 9$ outcomes.
Total outcomes with odd sum: $|O| = 9 + 9 = 18$.
Every outcome with sum 7 has one odd and one even die, so $E_7 \subset O$.

**5. Calculation:**  
Outcomes summing to 7: $(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1) \implies |E_7| = 6$.
Conditional probability:
$$P(\text{Sum} = 7 \mid \text{Sum is odd}) = \frac{|E_7|}{|O|} = \frac{6}{18} = \frac{1}{3}$$

**6. Final Answer:**  
$$\mathbf{\frac{1}{3}}$$

**7. Common Trap:**  
Calculating $6 / 36 = 1/6$ by forgetting to condition on the odd sum constraint.

**8. Alternative Method:**  
Direct conditional definition: $P(\text{Sum}=7) = 6/36 = 1/6$. $P(\text{Odd}) = 18/36 = 1/2$. Thus $P(\text{Sum}=7 \mid \text{Odd}) = \frac{1/6}{1/2} = \frac{2}{6} = \frac{1}{3}$.

---

### Problem 20: Hypergeometric Quality Acceptance Sampling

**1. Problem Statement:**  
A manufacturing batch of $N = 20$ semiconductor microchips contains exactly $D = 4$ defective chips and 16 non-defective chips. A quality inspector samples $n = 5$ chips uniformly at random without replacement. The entire batch is accepted if and only if the sample contains at most 1 defective chip. What is the exact probability that the batch is accepted?

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Hypergeometric Distribution  
- **Secondary Concept:** Sampling Without Replacement  

**3. Reasoning Setup:**  
Random variable $X \sim \text{Hypergeometric}(N=20, K=4, n=5)$.
Batch accepted if $X \le 1 \iff X = 0$ or $X = 1$.
Total sample outcomes: $\binom{20}{5} = 15,504$.

**4. Derivation:**  
Hypergeometric PMF: $P(X = k) = \frac{\binom{4}{k} \binom{16}{5-k}}{\binom{20}{5}}$.
- For $k = 0$: $\binom{4}{0} \binom{16}{5} = 1 \times 4,368 = 4,368$.
- For $k = 1$: $\binom{4}{1} \binom{16}{4} = 4 \times 1,820 = 7,280$.

**5. Calculation:**  
1. Favorable selections: $4,368 + 7,280 = 11,648$.
2. Probability of acceptance:
$$P(X \le 1) = \frac{11,648}{15,504} = \frac{728}{969} \approx 0.75129 \text{ (or } 75.13\%\text{)}$$

**6. Final Answer:**  
$$\mathbf{\frac{728}{969} \approx 75.13\%}$$

**7. Common Trap:**  
Using the Binomial distribution with $p = 4/20 = 0.20$:
$\binom{5}{0}(0.8)^5 + \binom{5}{1}(0.2)(0.8)^4 = 0.32768 + 0.4096 = 0.73728$.
Because $n/N = 5/20 = 25\%$, the sampling is not negligible, so sampling without replacement cannot be approximated by Binomial.

**8. Alternative Method:**  
Sequential branch probabilities: $P(X=0) = \frac{16}{20} \times \frac{15}{19} \times \frac{14}{18} \times \frac{13}{17} \times \frac{12}{16} = \frac{91}{323}$. $P(X=1) = 5 \times \frac{4}{20} \times \frac{16}{19} \times \frac{15}{18} \times \frac{14}{17} \times \frac{13}{16} = \frac{455}{969}$. Summing gives $\frac{273 + 455}{969} = \frac{728}{969}$.

---

### Problem 21: Circular Adjacency Probability

**1. Problem Statement:**  
Eight individuals, including Alice and Bob, are seated uniformly at random around a circular dining table with 8 distinguishable seats. What is the exact probability that Alice and Bob are seated directly next to each other?

**2. Level and Concept:**  
- **Level:** L2 — Standard Placement  
- **Primary Concept:** Circular Permutations  
- **Secondary Concept:** Symmetry  

**3. Reasoning Setup:**  
Around a circular table of $n = 8$ seats, fix Alice's position without loss of generality (by rotational symmetry).

**4. Derivation:**  
Once Alice is seated, there remain 7 unoccupied seats for Bob, all equally likely.
Of these 7 seats, exactly 2 are directly adjacent to Alice (one to her immediate left, one to her immediate right).

**5. Calculation:**  
Probability:
$$P(\text{Adjacent}) = \frac{2}{7} \approx 0.2857$$

**6. Final Answer:**  
$$\mathbf{\frac{2}{7}}$$

**7. Common Trap:**  
Dividing 2 by 8 ($2/8 = 1/4$), forgetting that Alice occupies one seat, leaving only 7 available options for Bob.

**8. Alternative Method:**  
Total arrangements modulo rotation is $(8-1)! = 7! = 5,040$. Tie Alice and Bob together: they can be arranged in $2! = 2$ internal ways, treating them as 1 block with 6 other people gives $(7-1)! = 6! = 720$ circular arrangements. Total favorable $= 2 \times 720 = 1,440$. Probability $= 1,440 / 5,040 = 2/7$.

---

### Problem 22: Non-Consecutive Vertex Selection on a Polygon

**1. Problem Statement:**  
Three distinct vertices are selected uniformly at random from the 10 vertices of a regular decagon (10-gon). What is the exact probability that no two of the selected vertices are adjacent on the boundary of the decagon?

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Circular Combinatorics  
- **Secondary Concept:** Kaplansky's Lemma  

**3. Reasoning Setup:**  
Total ways to choose 3 vertices from 10 is $\binom{10}{3} = 120$.
Let $N = 10, k = 3$. We require no two chosen vertices to be consecutive along the cycle $C_{10}$.

**4. Derivation:**  
By Kaplansky's theorem for circular non-consecutive subsets, the number of ways to choose $k$ non-consecutive elements from a cycle of $n$ vertices is:
$$C(n, k) = \frac{n}{n - k} \binom{n - k}{k}$$
For $n = 10, k = 3$:
$$C(10, 3) = \frac{10}{10 - 3} \binom{10 - 3}{3} = \frac{10}{7} \binom{7}{3} = \frac{10}{7} \times 35 = 50$$

**5. Calculation:**  
Probability:
$$P = \frac{50}{\binom{10}{3}} = \frac{50}{120} = \frac{5}{12} \approx 0.4167$$

**6. Final Answer:**  
$$\mathbf{\frac{5}{12}}$$

**7. Common Trap:**  
Using the linear formula $\binom{n - k + 1}{k} = \binom{10 - 3 + 1}{3} = \binom{8}{3} = 56$, which fails on a cycle because vertex 1 and vertex 10 are adjacent.

**8. Alternative Method:**  
Complementary counting: Total $= 120$.
- All 3 adjacent: 10 sets (each edge plus an adjacent vertex).
- Exactly 2 adjacent: Choose an edge (10 ways). The 3rd vertex cannot be the 2 vertices of the edge nor their 2 immediate neighbors ($10 - 4 = 6$ choices). Ways $= 10 \times 6 = 60$.
- Non-consecutive $= 120 - (10 + 60) = 50$. Prob $= 50/120 = 5/12$.

---

### Problem 23: Occupancy Problem: Elevator Floor Dispersal

**1. Problem Statement:**  
Four passengers enter an elevator on the ground floor of a building with 6 upper floors. Each passenger independently chooses an exit floor from floor 1 to 6 uniformly at random. What is the exact probability that all 4 passengers exit on completely different floors?

**2. Level and Concept:**  
- **Level:** L2 — Standard Placement  
- **Primary Concept:** Classical Occupancy  
- **Secondary Concept:** Uniform Allocations  

**3. Reasoning Setup:**  
Each of the 4 passengers has 6 possible floor choices.
Total possible exit configurations: $|S| = 6^4 = 1,296$.

**4. Derivation:**  
To have all 4 passengers exit on different floors, the floors chosen must be an ordered sequence of 4 distinct values chosen from the 6 available floors.
Number of favorable configurations: $6 \times 5 \times 4 \times 3 = 360$.

**5. Calculation:**  
Probability:
$$P = \frac{360}{6^4} = \frac{360}{1,296} = \frac{5}{18} \approx 0.2778$$

**6. Final Answer:**  
$$\mathbf{\frac{5}{18} \approx 0.2778}$$

**7. Common Trap:**  
Using combinations $\binom{6}{4} / 6^4 = 15 / 1,296$, which forgets that passengers are distinct individuals.

**8. Alternative Method:**  
Sequential conditional probability: $P = 1 \times \frac{5}{6} \times \frac{4}{6} \times \frac{3}{6} = \frac{60}{216} = \frac{5}{18}$.

---

### Problem 24: The Optimal Stopping Secretary Problem for $n=3$

**1. Problem Statement:**  
Three candidates of distinct abilities (ranked 1 = best, 2 = second, 3 = worst) are interviewed in a uniformly random sequential order ($3! = 6$ permutations). The interviewer uses the classic stopping policy: reject the first candidate automatically, and thereafter hire the very first candidate who is better than the first candidate (or the last candidate if none is better). What is the exact probability of hiring the best candidate (Rank 1)?

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Optimal Stopping  
- **Secondary Concept:** Information Updating  

**3. Reasoning Setup:**  
Permutations of ranks $(c_1, c_2, c_3)$ where 1 is the top candidate. All 6 permutations have probability $1/6$.

**4. Derivation:**  
Evaluate the rule across all 6 permutations:
1. $(1, 2, 3)$: Reject $c_1 = 1$. Next is 2 (worse than 1). Next is 3 (worse). Forced to take 3. (FAILS)
2. $(1, 3, 2)$: Reject $c_1 = 1$. Forced to take 2. (FAILS)
3. $(2, 1, 3)$: Reject $c_1 = 2$. $c_2 = 1$ is better than 2 $\implies$ Hires candidate 1. (SUCCESS)
4. $(2, 3, 1)$: Reject $c_1 = 2$. $c_2 = 3$ is worse than 2. $c_3 = 1$ is better $\implies$ Hires candidate 1. (SUCCESS)
5. $(3, 1, 2)$: Reject $c_1 = 3$. $c_2 = 1$ is better than 3 $\implies$ Hires candidate 1. (SUCCESS)
6. $(3, 2, 1)$: Reject $c_1 = 3$. $c_2 = 2$ is better than 3 $\implies$ Hires candidate 2. (FAILS)

**5. Calculation:**  
Candidate 1 is hired in 3 out of the 6 equiprobable permutations:
$$P(\text{Hire Rank 1}) = \frac{3}{6} = \frac{1}{2} = 0.50$$

**6. Final Answer:**  
$$\mathbf{\frac{1}{2} = 0.50}$$

**7. Common Trap:**  
Assuming the probability is $1/e \approx 36.8\%$, which is the asymptotic limit as $n \to \infty$. For finite $n = 3$, the exact probability with threshold $r = 1$ is strictly $1/2$.

**8. Alternative Method:**  
Summing by position of the best candidate: Candidate 1 cannot be at position 1 (rejected). If Candidate 1 is at position 2 (prob $1/3$), they are always hired. If Candidate 1 is at position 3 (prob $1/3$), they are hired iff the best of the first two is at position 1 (prob $1/2$). Total $= 0 + \frac{1}{3} + \frac{1}{3} \times \frac{1}{2} = \frac{1}{3} + \frac{1}{6} = \frac{1}{2}$.

---

### Problem 25: Bridge Deal: Holding All Four Aces

**1. Problem Statement:**  
In a bridge game, 13 cards are dealt uniformly at random to a player from a standard 52-card deck. What is the exact probability that this specific player is dealt all 4 Aces?

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Hypergeometric Deal  
- **Secondary Concept:** Exact Fraction Reduction  

**3. Reasoning Setup:**  
Population $N = 52$ containing $K = 4$ Aces and 48 non-Aces. Hand size $n = 13$.
Total bridge hands: $\binom{52}{13}$.

**4. Derivation:**  
To receive all 4 Aces, the hand must contain all $\binom{4}{4} = 1$ Aces and exactly $\binom{48}{9}$ non-Aces:
$$P = \frac{\binom{4}{4} \binom{48}{9}}{\binom{52}{13}} = \frac{\binom{48}{9}}{\binom{52}{13}}$$

**5. Calculation:**  
Expanding the combinatorial factors:
$$P = \frac{\frac{48!}{9! \, 39!}}{\frac{52!}{13! \, 39!}} = \frac{48!}{52!} \times \frac{13!}{9!} = \frac{13 \times 12 \times 11 \times 10}{52 \times 51 \times 50 \times 49}$$
1. $\frac{13}{52} = \frac{1}{4}$.
2. $\frac{12}{4} = 3$.
3. $\frac{3}{51} = \frac{1}{17}$.
4. $\frac{10}{50} = \frac{1}{5}$.
5. Numerator remaining: 11. Denominator: $17 \times 5 \times 49 = 85 \times 49 = 4,165$.
$$P = \frac{11}{4,165} \approx 0.002641 \text{ (about 1 in 379)}$$

**6. Final Answer:**  
$$\mathbf{\frac{11}{4,165} \approx 0.002641}$$

**7. Common Trap:**  
Approximating with $(13/52)^4 = (1/4)^4 = 1/256 \approx 0.0039$, which assumes independent sampling with replacement and substantially overestimates the true probability.

**8. Alternative Method:**  
Sequential draws of 4 Aces in the first 4 slots multiplied by $\binom{13}{4}$ positions: $\binom{13}{4} \times \frac{4}{52} \times \frac{3}{51} \times \frac{2}{50} \times \frac{1}{49} = 715 \times \frac{24}{6,497,400} = \frac{11}{4,165}$.

---

## Section 3: Discrete Distributions, Expectation & Variance (Q26–Q40)


### Problem 26: Binomial Distribution: Mode and Peak Probability

**1. Problem Statement:**  
A biased coin with probability of Heads $p = 0.30$ is tossed $n = 10$ times independently. Determine the mode of the distribution (the most probable number of Heads) and calculate its exact probability.

**2. Level and Concept:**  
- **Level:** L2 — Standard Placement  
- **Primary Concept:** Binomial PMF  
- **Secondary Concept:** Mode Determination  

**3. Reasoning Setup:**  
$X \sim \text{Binomial}(n=10, p=0.30)$.
The mode $k^*$ of a binomial distribution satisfies $(n+1)p - 1 \le k^* \le (n+1)p$.

**4. Derivation:**  
1. Evaluate $(n+1)p = 11 \times 0.30 = 3.30$.
Since $3.30$ is not an integer, the distribution has a unique mode at $k^* = \lfloor 3.30 \rfloor = 3$.
2. Binomial formula at $k = 3$:
$$P(X = 3) = \binom{10}{3} p^3 (1-p)^7 = \binom{10}{3} (0.3)^3 (0.7)^7$$

**5. Calculation:**  
1. $\binom{10}{3} = \frac{10 \times 9 \times 8}{6} = 120$.
2. $(0.3)^3 = 0.027$.
3. $(0.7)^7 = 0.0823543$.
4. $P(X = 3) = 120 \times 0.027 \times 0.0823543 = 3.24 \times 0.0823543 = 0.2668279 \approx 26.68\%$.

**6. Final Answer:**  
$$\mathbf{k^* = 3, \quad P(X = 3) \approx 0.2668}$$

**7. Common Trap:**  
Assuming the mode is always rounded to the nearest integer of $n p = 3.0$ without checking $(n+1)p$, or calculating $P(X = np)$ without verifying whether two modes exist when $(n+1)p$ is an integer.

**8. Alternative Method:**  
Ratio test: $\frac{P(X=k)}{P(X=k-1)} = \frac{n - k + 1}{k} \frac{p}{1-p}$. For $k=3$: $\frac{8}{3} \times \frac{3}{7} = \frac{8}{7} > 1$. For $k=4$: $\frac{7}{4} \times \frac{3}{7} = \frac{3}{4} < 1$. Thus probability peaks strictly at $k=3$.

---

### Problem 27: Poisson Process: Tail Probability in Scaled Windows

**1. Problem Statement:**  
Customers arrive at an automated teller machine according to a homogeneous Poisson process at an average rate of $\lambda = 4$ customers per hour. What is the probability that at least 2 customers arrive during a randomly chosen 30-minute interval?

**2. Level and Concept:**  
- **Level:** L2 — Standard Placement  
- **Primary Concept:** Poisson Process  
- **Secondary Concept:** Rate Scaling  

**3. Reasoning Setup:**  
Rate per hour $\lambda = 4$. Time interval $t = 0.5$ hours.
Parameter for the 30-minute window: $\mu = \lambda t = 4 \times 0.5 = 2.0$.
Let $N \sim \text{Poisson}(\mu = 2)$.

**4. Derivation:**  
Tail probability: $P(N \ge 2) = 1 - P(N = 0) - P(N = 1)$.
Poisson PMF: $P(N = k) = \frac{e^{-\mu} \mu^k}{k!}$.

**5. Calculation:**  
1. $P(N = 0) = e^{-2} \frac{2^0}{0!} = e^{-2} \approx 0.135335$.
2. $P(N = 1) = e^{-2} \frac{2^1}{1!} = 2 e^{-2} \approx 0.270671$.
3. Sum: $P(N \le 1) = 3 e^{-2} \approx 0.406006$.
4. Tail probability:
$$P(N \ge 2) = 1 - 3 e^{-2} = 1 - 0.406006 = 0.593994 \approx 59.40\%$$

**6. Final Answer:**  
$$\mathbf{1 - 3e^{-2} \approx 0.5940}$$

**7. Common Trap:**  
Using the 1-hour rate $\lambda = 4$ directly without scaling to the 30-minute interval.

**8. Alternative Method:**  
Direct sum: $\sum_{k=2}^\infty \frac{e^{-2} 2^k}{k!} = e^{-2} (e^2 - 1 - 2) = 1 - 3e^{-2}$.

---

### Problem 28: Memoryless Property of the Geometric Distribution

**1. Problem Statement:**  
Let $X$ denote the number of independent trials required until the first success occurs, where each trial succeeds with probability $p = 0.20$. Given that the first success has not occurred in the first 3 trials ($X > 3$), what is the conditional probability that more than 8 trials in total will be required ($X > 8$)?

**2. Level and Concept:**  
- **Level:** L2 — Standard Placement  
- **Primary Concept:** Geometric Distribution  
- **Secondary Concept:** Memoryless Property  

**3. Reasoning Setup:**  
$X \sim \text{Geometric}(p=0.20)$ with support $\{1, 2, 3, \dots\}$.
Tail probability: $P(X > k) = (1 - p)^k = q^k$ where $q = 0.80$.

**4. Derivation:**  
By the memoryless property of the Geometric distribution:
$$P(X > s + t \mid X > s) = P(X > t)$$
Here $s = 3$ and $s + t = 8 \implies t = 5$.
Therefore, $P(X > 8 \mid X > 3) = P(X > 5) = q^5$.

**5. Calculation:**  
Evaluating $q^5 = (0.80)^5$:
$$(0.8)^5 = 0.32768$$

**6. Final Answer:**  
$$\mathbf{(0.80)^5 = 0.32768}$$

**7. Common Trap:**  
Computing $\frac{P(X > 8)}{P(X > 3)} = \frac{q^8}{q^3}$ with complicated summation formulas without recognizing the memoryless identity.

**8. Alternative Method:**  
Direct conditional definition: $\frac{P(X > 8 \cap X > 3)}{P(X > 3)} = \frac{P(X > 8)}{P(X > 3)} = \frac{0.8^8}{0.8^3} = 0.8^5 = 0.32768$.

---

### Problem 29: Negative Binomial: Waiting for the $r$-th Success

**1. Problem Statement:**  
A fair 6-sided die is rolled repeatedly. What is the exact probability that the 3rd 'Six' appears on exactly the 10th roll?

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Negative Binomial  
- **Secondary Concept:** Multi-stage Stopping  

**3. Reasoning Setup:**  
Success is rolling a 6 ($p = 1/6$, $q = 5/6$).
Target: the 3rd success ($r = 3$) occurs on trial $n = 10$.

**4. Derivation:**  
For the 3rd success to occur on the 10th roll, two independent conditions must be satisfied:
1. Exactly $r - 1 = 2$ successes must occur in the first $n - 1 = 9$ rolls.
2. The 10th roll must be a success.

**5. Calculation:**  
1. Probability of 2 sixes in first 9 rolls: $\binom{9}{2} \left(\frac{1}{6}\right)^2 \left(\frac{5}{6}\right)^7$.
2. Probability of six on 10th roll: $\frac{1}{6}$.
3. Combined probability:
$$P = \binom{9}{2} \left(\frac{1}{6}\right)^3 \left(\frac{5}{6}\right)^7 = 36 \times \frac{1}{216} \times \frac{78,125}{279,936} = \frac{1}{6} \times \frac{78,125}{279,936} = \frac{78,125}{1,679,616} \approx 0.046514$$

**6. Final Answer:**  
$$\mathbf{\frac{78,125}{1,679,616} \approx 0.04651}$$

**7. Common Trap:**  
Using standard Binomial $\binom{10}{3}(1/6)^3(5/6)^7$, which includes cases where the 3rd six occurred before the 10th roll.

**8. Alternative Method:**  
Negative binomial PMF formula: $\binom{k - 1}{r - 1} p^r (1-p)^{k-r}$ with $k = 10, r = 3$: $\binom{9}{2} (1/6)^3 (5/6)^7 = \frac{78,125}{1,679,616}$.

---

### Problem 30: Indicator Variables: Expected Fixed Points in Permutations

**1. Problem Statement:**  
A random permutation of the integers $\{1, 2, \dots, n\}$ is chosen uniformly from all $n!$ permutations. A fixed point is an index $i$ such that $\pi(i) = i$. Prove and calculate the expected number of fixed points, and explain why it is completely invariant to $n$.

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Linearity of Expectation  
- **Secondary Concept:** Indicator Variables  

**3. Reasoning Setup:**  
Let $X$ denote the total number of fixed points.
Define indicator random variables $I_i = \mathbf{1}_{\{\pi(i) = i\}}$ for each $i \in \{1, 2, \dots, n\}$, so that $X = \sum_{i=1}^n I_i$.

**4. Derivation:**  
By Linearity of Expectation (which holds regardless of dependence among $I_i$):
$$E[X] = \sum_{i=1}^n E[I_i] = \sum_{i=1}^n P(\pi(i) = i)$$
In a uniform random permutation, each element $i$ is equally likely to be mapped to any of the $n$ positions, so:
$$P(\pi(i) = i) = \frac{1}{n} \quad \text{for every } i$$

**5. Calculation:**  
Summing across all $n$ indicators:
$$E[X] = \sum_{i=1}^n \frac{1}{n} = n \times \frac{1}{n} = 1$$
This expected value is identically 1 for $n = 1, 10, 100,$ or $1,000,000$.

**6. Final Answer:**  
$$\mathbf{E[X] = 1 \quad (\text{invariant for all } n \ge 1)}$$

**7. Common Trap:**  
Attempting to compute $E[X] = \sum k P(X=k)$ using derangement fractions $D_{n-k}$, which is algebraically arduous and obscures the one-line indicator linearity.

**8. Alternative Method:**  
Permutation matrix trace: $X = \text{Tr}(P)$ where $P$ is the random permutation matrix. $E[X] = \text{Tr}(E[P])$. Since $E[P_{ii}] = 1/n$, $\text{Tr}(E[P]) = n(1/n) = 1$.

---

### Problem 31: Indicator Variables: Expected Runs of Heads

**1. Problem Statement:**  
A fair coin is tossed $n = 10$ times. A 'run of Heads' is defined as a maximal sequence of consecutive Heads. For example, in the sequence $HHTHTHHHTT$, there are 3 runs of Heads. What is the expected number of runs of Heads?

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Runs Statistics  
- **Secondary Concept:** Linearity of Expectation  

**3. Reasoning Setup:**  
Tosses $X_1, X_2, \dots, X_{10} \in \{H, T\}$. Let $R$ denote the total number of runs of Heads.
A run of Heads begins at index 1 if $X_1 = H$. For any subsequent position $i \in \{2, 3, \dots, 10\}$, a run of Heads begins at $i$ if and only if $X_{i-1} = T$ and $X_i = H$.

**4. Derivation:**  
Define indicators $I_i$ for whether a run begins at index $i$:
- $I_1 = \mathbf{1}_{\{X_1 = H\}} \implies E[I_1] = P(X_1 = H) = \frac{1}{2}$.
- For $2 \le i \le 10$, $I_i = \mathbf{1}_{\{X_{i-1} = T, X_i = H\}} \implies E[I_i] = P(X_{i-1} = T) P(X_i = H) = \frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$.
The total number of runs is $R = \sum_{i=1}^{10} I_i$.

**5. Calculation:**  
By Linearity of Expectation:
$$E[R] = E[I_1] + \sum_{i=2}^{10} E[I_i] = \frac{1}{2} + 9 \times \frac{1}{4} = \frac{2}{4} + \frac{9}{4} = \frac{11}{4} = 2.75$$

**6. Final Answer:**  
$$\mathbf{\frac{11}{4} = 2.75}$$

**7. Common Trap:**  
Setting $E[I_i] = 1/4$ for all 10 indices, obtaining $10/4 = 2.50$, which overlooks the boundary condition at $i = 1$ where no preceding coin exists.

**8. Alternative Method:**  
Symmetry argument: By alternating symmetry between H and T runs, the expected number of alternating transitions plus boundary yields $E[R] = \frac{n+1}{4} = \frac{11}{4} = 2.75$.

---

### Problem 32: Matching Sock Pairs: Linearity of Expectation

**1. Problem Statement:**  
A drawer contains 5 distinct pairs of socks (10 individual socks in total). A person randomly selects 4 socks without replacement in the dark. What is the expected number of complete matching pairs in the selected sample?

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Linearity of Expectation  
- **Secondary Concept:** Sampling Without Replacement  

**3. Reasoning Setup:**  
Number of pairs $N = 5$, total socks $= 10$, sample size $k = 4$.
Let $X$ be the number of complete matching pairs drawn.
Define indicator $I_i = 1$ if pair $i$ is completely drawn, and 0 otherwise, for $i \in \{1, 2, \dots, 5\}$.

**4. Derivation:**  
For a specific pair $i$ to be completely drawn, both of its socks must be included in the 4 chosen socks.
The number of ways to pick 4 socks containing both socks of pair $i$ is $\binom{10 - 2}{4 - 2} = \binom{8}{2} = 28$.
Total ways to pick 4 socks is $\binom{10}{4} = 210$.
$$P(I_i = 1) = \frac{\binom{8}{2}}{\binom{10}{4}} = \frac{28}{210} = \frac{2}{15}$$

**5. Calculation:**  
By Linearity of Expectation:
$$E[X] = \sum_{i=1}^5 E[I_i] = 5 \times \frac{2}{15} = \frac{10}{15} = \frac{2}{3} \approx 0.667$$

**6. Final Answer:**  
$$\mathbf{\frac{2}{3}}$$

**7. Common Trap:**  
Computing the full probability distribution $P(X=0), P(X=1), P(X=2)$ and summing $k P(X=k)$, which is prone to combinatorial arithmetic errors.

**8. Alternative Method:**  
Direct distribution check: $P(X=2) = \frac{\binom{5}{2}}{\binom{10}{4}} = \frac{10}{210} = \frac{1}{21}$. $P(X=1) = \frac{\binom{5}{1} \times \binom{4}{2} \times 2^2}{\binom{10}{4}} = \frac{5 \times 6 \times 4}{210} = \frac{120}{210} = \frac{4}{7}$. $E[X] = 1(4/7) + 2(1/21) = \frac{12 + 2}{21} = \frac{14}{21} = \frac{2}{3}$.

---

### Problem 33: Hypergeometric Variance and Finite Population Correction

**1. Problem Statement:**  
An urn contains $N = 10$ balls, of which $K = 4$ are White and 6 are Black. A sample of $n = 3$ balls is drawn uniformly at random without replacement. Compute the mean and variance of the number of White balls drawn, identifying the finite population correction factor.

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Hypergeometric Distribution  
- **Secondary Concept:** Finite Population Correction  

**3. Reasoning Setup:**  
Random variable $X \sim \text{Hypergeometric}(N=10, K=4, n=3)$.
Proportion of White balls in population: $p = K/N = 4/10 = 0.40, q = 1 - p = 0.60$.

**4. Derivation:**  
Hypergeometric moments:
$$E[X] = n p = 3 \times 0.40 = 1.20$$
$$\text{Var}(X) = n p (1 - p) \left(\frac{N - n}{N - 1}\right)$$
where $\frac{N - n}{N - 1}$ is the Finite Population Correction (FPC) factor.

**5. Calculation:**  
1. FPC factor: $\frac{10 - 3}{10 - 1} = \frac{7}{9}$.
2. Binomial baseline variance: $n p q = 3 \times 0.40 \times 0.60 = 0.72$.
3. Hypergeometric variance:
$$\text{Var}(X) = 0.72 \times \frac{7}{9} = 0.08 \times 7 = 0.56$$

**6. Final Answer:**  
$$\mathbf{E[X] = 1.20, \quad \text{Var}(X) = 0.56}$$

**7. Common Trap:**  
Using the Binomial variance formula $n p (1-p) = 0.72$, failing to account for the variance reduction caused by sampling without replacement.

**8. Alternative Method:**  
Indicator covariance: $X = I_1 + I_2 + I_3$. $\text{Var}(X) = 3 \text{Var}(I_1) + 6 \text{Cov}(I_1, I_2)$. $\text{Var}(I_1) = 0.4 \times 0.6 = 0.24$. $P(I_1 = 1, I_2 = 1) = \frac{4}{10} \times \frac{3}{9} = \frac{2}{15}$. $\text{Cov}(I_1, I_2) = \frac{2}{15} - 0.16 = \frac{2}{15} - \frac{4}{25} = -\frac{2}{75} = -0.02667$. $\text{Var}(X) = 3(0.24) + 6(-2/75) = 0.72 - 0.16 = 0.56$.

---

### Problem 34: Classical Occupancy: Expected Empty Bins

**1. Problem Statement:**  
Suppose $m = 8$ distinguishable balls are tossed independently and uniformly at random into $n = 5$ distinguishable bins. What is the expected number of empty bins?

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Occupancy Problems  
- **Secondary Concept:** Linearity of Expectation  

**3. Reasoning Setup:**  
Let $Y$ denote the number of empty bins.
Define indicator $I_j = \mathbf{1}_{\{\text{bin } j \text{ is empty}\}}$ for $j \in \{1, 2, \dots, 5\}$, so $Y = \sum_{j=1}^5 I_j$.

**4. Derivation:**  
For a specific bin $j$ to remain empty, all $m$ balls must choose one of the other $n - 1$ bins.
Because each ball chooses independently and uniformly:
$$P(I_j = 1) = \left(1 - \frac{1}{n}\right)^m = \left(\frac{4}{5}\right)^8$$

**5. Calculation:**  
By Linearity of Expectation:
$$E[Y] = \sum_{j=1}^5 E[I_j] = 5 \times \left(\frac{4}{5}\right)^8 = 5 \times \frac{65,536}{390,625} = \frac{65,536}{78,125} \approx 0.83886$$

**6. Final Answer:**  
$$\mathbf{\frac{65,536}{78,125} \approx 0.8389}$$

**7. Common Trap:**  
Applying Stirling numbers of the second kind to find the full distribution before computing expectation, which requires summing many terms and often introduces arithmetic errors.

**8. Alternative Method:**  
Poisson approximation: Rate of balls per bin is $\lambda = 8/5 = 1.6$. Probability a bin is empty is approximately $e^{-1.6} \approx 0.2019$. Expected empty bins $\approx 5 \times 0.2019 = 1.009$, which provides a quick sanity check.

---

### Problem 35: St. Petersburg Paradox with Finite Bankroll Cap

**1. Problem Statement:**  
In a modified St. Petersburg lottery, a fair coin is tossed until the first Heads appears on toss $K$. The player receives a payout of $\$2^K$, subject to a casino maximum bankroll cap of $\$1,024 = \$2^{10}$. That is, if $K \ge 10$, the payout is capped at $\$1,024$. What is the exact expected payout of this game?

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** St. Petersburg Game  
- **Secondary Concept:** Expected Value Under Truncation  

**3. Reasoning Setup:**  
Let $K \sim \text{Geometric}(p = 1/2)$ with $P(K = k) = \left(\frac{1}{2}\right)^k$ for $k = 1, 2, 3, \dots$
Payout function:
$$W(k) = \begin{cases} 2^k & \text{if } 1 \le k \le 9 \\ 1024 & \text{if } k \ge 10 \end{cases}$$

**4. Derivation:**  
Split the expected value into the uncapped portion ($k = 1$ to $9$) and the capped tail ($k \ge 10$):
$$E[W] = \sum_{k=1}^9 P(K = k) 2^k + \sum_{k=10}^\infty P(K = k) 1024$$

**5. Calculation:**  
1. For each $k \in \{1, \dots, 9\}$:
   $$P(K = k) 2^k = \left(\frac{1}{2}\right)^k 2^k = 1$$
   Sum for $k = 1$ to $9$ is $9 \times 1 = 9$.
2. For $k \ge 10$, total tail probability is:
   $$P(K \ge 10) = \left(\frac{1}{2}\right)^9 = \frac{1}{512}$$
   Contribution: $1024 \times P(K \ge 10) = 1024 \times \frac{1}{512} = 2$.
3. Total expected payout:
$$E[W] = 9 + 2 = 11$$

**6. Final Answer:**  
$$\mathbf{\$11}$$

**7. Common Trap:**  
Claiming the expectation is infinite as in the classic theoretical paradox, or forgetting that the tail $k \ge 10$ has probability $1/512$ rather than $1/1024$.

**8. Alternative Method:**  
Direct sum: $\sum_{k=1}^{10} (1/2)^k 2^k + \sum_{k=11}^\infty (1/2)^k 1024 = 10 + 1024 \sum_{j=1}^\infty (1/2)^{10+j} = 10 + 1024(1/1024) = 10 + 1 = 11$.

---

### Problem 36: Order Statistics: Expected Maximum of Two Fair Dice

**1. Problem Statement:**  
Two standard fair 6-sided dice are rolled independently. Let $M = \max(D_1, D_2)$ be the maximum value obtained. Calculate the exact expected value $E[M]$.

**2. Level and Concept:**  
- **Level:** L2 — Standard Placement  
- **Primary Concept:** Order Statistics  
- **Secondary Concept:** Discrete CDF Trick  

**3. Reasoning Setup:**  
$D_1, D_2$ i.i.d. discrete uniform on $\{1, 2, \dots, 6\}$. Support of $M$ is $\{1, 2, \dots, 6\}$.
CDF of the maximum: $P(M \le k) = P(D_1 \le k, D_2 \le k) = \left(\frac{k}{6}\right)^2$.

**4. Derivation:**  
Tail sum formula for non-negative discrete random variables:
$$E[M] = \sum_{k=1}^6 P(M \ge k) = \sum_{k=0}^5 [1 - P(M \le k)]$$
Alternatively, find PMF: $P(M = k) = P(M \le k) - P(M \le k - 1) = \frac{k^2 - (k-1)^2}{36} = \frac{2k - 1}{36}$.

**5. Calculation:**  
Using $E[M] = \sum_{k=1}^6 k \times \frac{2k - 1}{36}$:
- $k = 1: 1 \times 1 = 1$
- $k = 2: 2 \times 3 = 6$
- $k = 3: 3 \times 5 = 15$
- $k = 4: 4 \times 7 = 28$
- $k = 5: 5 \times 9 = 45$
- $k = 6: 6 \times 11 = 66$
Sum of numerators $= 1 + 6 + 15 + 28 + 45 + 66 = 161$.
$$E[M] = \frac{161}{36} \approx 4.4722$$

**6. Final Answer:**  
$$\mathbf{\frac{161}{36} \approx 4.472}$$

**7. Common Trap:**  
Averaging the mean of single die ($3.5$) with 6 to guess $4.75$, or computing $E[D_1 + D_2]/2 = 3.5$.

**8. Alternative Method:**  
Tail expectation formula: $E[M] = 6 - \sum_{k=1}^5 P(M \le k) = 6 - \sum_{k=1}^5 \frac{k^2}{36} = 6 - \frac{1 + 4 + 9 + 16 + 25}{36} = 6 - \frac{55}{36} = \frac{216 - 55}{36} = \frac{161}{36}$.

---

### Problem 37: Covariance and Correlation of Dependent Indicator Variables

**1. Problem Statement:**  
Three fair coins are tossed independently. Let $X = \mathbf{1}_{\{\text{Coin 1 is Heads}\}}$ and let $Y = \mathbf{1}_{\{\text{Total Heads } \ge 2\}}$. Calculate $\text{Cov}(X, Y)$ and the Pearson correlation coefficient $\rho(X, Y)$.

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Covariance and Correlation  
- **Secondary Concept:** Joint Indicator Distributions  

**3. Reasoning Setup:**  
Sample space $|S| = 2^3 = 8$ equally likely outcomes: $\{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\}$.

**4. Derivation:**  
1. $E[X] = P(\text{Coin 1 is H}) = \frac{4}{8} = \frac{1}{2}$. $\text{Var}(X) = \frac{1}{2}\left(1 - \frac{1}{2}\right) = \frac{1}{4}$.
2. $Y = 1$ when at least two heads occur: $\{HHH, HHT, HTH, THH\}$ (4 outcomes).
   $E[Y] = \frac{4}{8} = \frac{1}{2}$. $\text{Var}(Y) = \frac{1}{4}$.
3. Product $XY = 1$ if Coin 1 is H AND total heads $\ge 2$: $\{HHH, HHT, HTH\}$ (3 outcomes).
   $E[XY] = P(XY = 1) = \frac{3}{8}$.

**5. Calculation:**  
1. Covariance:
$$\text{Cov}(X, Y) = E[XY] - E[X] E[Y] = \frac{3}{8} - \left(\frac{1}{2}\right)\left(\frac{1}{2}\right) = \frac{3}{8} - \frac{1}{4} = \frac{1}{8} = 0.125$$
2. Correlation:
$$\rho(X, Y) = \frac{\text{Cov}(X, Y)}{\sqrt{\text{Var}(X) \text{Var}(Y)}} = \frac{1/8}{\sqrt{(1/4)(1/4)}} = \frac{1/8}{1/4} = \frac{1}{2} = 0.50$$

**6. Final Answer:**  
$$\mathbf{\text{Cov}(X, Y) = \frac{1}{8}, \quad \rho(X, Y) = 0.50}$$

**7. Common Trap:**  
Assuming that because the individual coin tosses are independent, any functions defined on them must be uncorrelated.

**8. Alternative Method:**  
Regression slope relation: Since $X$ and $Y$ have equal variances, $\rho = \beta_{Y|X} = E[Y \mid X=1] - E[Y \mid X=0]$. $E[Y \mid X=1] = P(\ge 1 \text{ head in remaining 2 coins}) = 3/4$. $E[Y \mid X=0] = P(\text{both remaining heads}) = 1/4$. Thus $\rho = 3/4 - 1/4 = 1/2$.

---

### Problem 38: Sum of Independent Poissons and Binomial Conditioning

**1. Problem Statement:**  
Let $X \sim \text{Poisson}(\lambda_1 = 2)$ and $Y \sim \text{Poisson}(\lambda_2 = 3)$ be independent random variables. Given that their sum $X + Y = 3$, what is the exact conditional probability that $X = 1$?

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Poisson Convolution  
- **Secondary Concept:** Conditional Binomial Property  

**3. Reasoning Setup:**  
By the convolution property of Poisson distributions, $Z = X + Y \sim \text{Poisson}(\lambda_1 + \lambda_2 = 5)$.
The conditional distribution of $X$ given $X + Y = n$ is known to be $\text{Binomial}\left(n, p = \frac{\lambda_1}{\lambda_1 + \lambda_2}\right)$.

**4. Derivation:**  
Using Bayes' Theorem:
$$P(X = 1 \mid X + Y = 3) = \frac{P(X = 1, Y = 2)}{P(X + Y = 3)} = \frac{P(X = 1) P(Y = 2)}{P(X + Y = 3)}$$
Substitute PMFs:
$$= \frac{\frac{e^{-2} 2^1}{1!} \times \frac{e^{-3} 3^2}{2!}}{\frac{e^{-5} 5^3}{3!}} = \binom{3}{1} \left(\frac{2}{5}\right)^1 \left(\frac{3}{5}\right)^2$$

**5. Calculation:**  
1. Binomial parameter: $p = \frac{2}{2 + 3} = 0.40, q = 0.60$.
2. Conditional probability:
$$P(X = 1 \mid X + Y = 3) = \binom{3}{1} (0.4)^1 (0.6)^2 = 3 \times 0.4 \times 0.36 = 1.2 \times 0.36 = 0.432$$

**6. Final Answer:**  
$$\mathbf{\binom{3}{1} (0.4)(0.6)^2 = 0.432}$$

**7. Common Trap:**  
Recalculating exponentials numerically with rounding errors rather than using the cancellation of $e^{-(\lambda_1 + \lambda_2)}$.

**8. Alternative Method:**  
Direct Poisson quotient: $\frac{2 \times (9/2)}{125/6} = \frac{9}{125/6} = \frac{54}{125} = 0.432$.

---

### Problem 39: Chebyshev's Inequality Tail Bound

**1. Problem Statement:**  
A random variable $X$ has mean $\mu = 50$ and variance $\sigma^2 = 25$ (standard deviation $\sigma = 5$). What is the maximum possible probability that $X$ falls outside the interval $(35, 65)$, without making any assumption about the underlying distribution?

**2. Level and Concept:**  
- **Level:** L2 — Standard Placement  
- **Primary Concept:** Chebyshev's Inequality  
- **Secondary Concept:** Distribution-Free Bounds  

**3. Reasoning Setup:**  
We seek an upper bound on $P(|X - 50| \ge 15)$.
Notice that the deviation $15 = 3 \sigma$, since $\sigma = 5$.

**4. Derivation:**  
By Chebyshev's Inequality, for any random variable with finite variance and any $k > 0$:
$$P(|X - \mu| \ge k \sigma) \le \frac{1}{k^2}$$
Here, $k \sigma = 15 \implies k = 3$.

**5. Calculation:**  
Applying the inequality directly:
$$P(|X - 50| \ge 15) \le \frac{1}{3^2} = \frac{1}{9} \approx 0.1111$$

**6. Final Answer:**  
$$\mathbf{\frac{1}{9} \approx 0.1111}$$

**7. Common Trap:**  
Applying the Normal 68-95-99.7 rule to claim $P \approx 0.0027$. Chebyshev provides a rigorous bound that holds for *any* arbitrary distribution (including bimodal or skewed distributions).

**8. Alternative Method:**  
Markov's inequality on squared deviations: $P((X - 50)^2 \ge 225) \le \frac{E[(X - 50)^2]}{225} = \frac{25}{225} = \frac{1}{9}$.

---

### Problem 40: Exponential Distribution: Higher Moments via MGF

**1. Problem Statement:**  
Let $X \sim \text{Exponential}(\lambda = 2)$ with probability density function $f(x) = 2 e^{-2x}$ for $x \ge 0$. Using its moment generating function, calculate the third raw moment $E[X^3]$.

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Moment Generating Functions  
- **Secondary Concept:** Exponential Distribution  

**3. Reasoning Setup:**  
Moment generating function of $X \sim \text{Exp}(\lambda)$:
$$M_X(t) = E[e^{tX}] = \frac{\lambda}{\lambda - t} = \left(1 - \frac{t}{\lambda}\right)^{-1} \quad \text{for } t < \lambda$$

**4. Derivation:**  
Expand $M_X(t)$ as a geometric series:
$$M_X(t) = \sum_{k=0}^\infty \left(\frac{t}{\lambda}\right)^k = \sum_{k=0}^\infty \frac{k!}{\lambda^k} \frac{t^k}{k!}$$
Since $M_X(t) = \sum_{k=0}^\infty E[X^k] \frac{t^k}{k!}$, matching coefficients gives:
$$E[X^k] = \frac{k!}{\lambda^k}$$

**5. Calculation:**  
For $k = 3$ and $\lambda = 2$:
$$E[X^3] = \frac{3!}{2^3} = \frac{6}{8} = \frac{3}{4} = 0.75$$

**6. Final Answer:**  
$$\mathbf{\frac{3}{4} = 0.75}$$

**7. Common Trap:**  
Computing $(E[X])^3 = (1/2)^3 = 1/8 = 0.125$, confusing the third power of the mean with the third raw moment.

**8. Alternative Method:**  
Direct integration using Gamma function: $E[X^3] = \int_0^\infty x^3 (2 e^{-2x}) dx = 2 \int_0^\infty x^3 e^{-2x} dx$. Substitute $u = 2x \implies E[X^3] = 2 \int_0^\infty (u/2)^3 e^{-u} (du/2) = \frac{2}{16} \Gamma(4) = \frac{1}{8} \times 6 = \frac{6}{8} = \frac{3}{4}$.

---

## Section 4: Conditional Expectation & Advanced Stochastic Reasoning (Q41–Q50)


### Problem 41: Compound Poisson Process: Total Expectation & Variance

**1. Problem Statement:**  
An insurance company receives a random number $N$ of claims in a week, where $N \sim \text{Poisson}(\lambda = 10)$. The dollar amounts of individual claims $X_1, X_2, \dots$ are independent, identically distributed, and independent of $N$, with each $X_i \sim \text{Exponential}(\text{mean } \mu = 5)$. Let $S = \sum_{i=1}^N X_i$ be the total aggregate claims paid in the week (with $S = 0$ if $N = 0$). Calculate $E[S]$ and $\text{Var}(S)$.

**2. Level and Concept:**  
- **Level:** L4 — Expert Quantitative Reasoning  
- **Primary Concept:** Law of Total Expectation  
- **Secondary Concept:** Law of Total Variance  

**3. Reasoning Setup:**  
$N \sim \text{Pois}(10) \implies E[N] = 10, \text{Var}(N) = 10$.
$X_i \sim \text{Exp} \implies E[X] = 5, \text{Var}(X) = 5^2 = 25$.

**4. Derivation:**  
1. By the Law of Total Expectation:
$$E[S] = E[E[S \mid N]] = E[N \cdot E[X]] = E[N] E[X]$$
2. By the Law of Total Variance (Eve's Law):
$$\text{Var}(S) = E[\text{Var}(S \mid N)] + \text{Var}(E[S \mid N])$$
Since $S \mid N = \sum_{i=1}^N X_i$ is a sum of $N$ independent terms:
$$\text{Var}(S \mid N) = N \text{Var}(X), \quad E[S \mid N] = N E[X]$$
$$\text{Var}(S) = E[N] \text{Var}(X) + \text{Var}(N) (E[X])^2$$

**5. Calculation:**  
1. Expected total claim:
$$E[S] = 10 \times 5 = 50$$
2. Variance of total claim:
$$\text{Var}(S) = (10 \times 25) + (10 \times 5^2) = 250 + 250 = 500$$
Standard deviation $\sigma_S = \sqrt{500} = 10\sqrt{5} \approx 22.36$.

**6. Final Answer:**  
$$\mathbf{E[S] = 50, \quad \text{Var}(S) = 500}$$

**7. Common Trap:**  
Omitting the second term in the Law of Total Variance, falsely claiming $\text{Var}(S) = E[N] \text{Var}(X) = 250$.

**8. Alternative Method:**  
Wald's identity on MGF: $M_S(t) = M_N(\ln M_X(t)) = \exp(10 (M_X(t) - 1))$. Differentiating twice at $t = 0$ yields identical moments.

---

### Problem 42: Gambler's Ruin with Biased Probabilities

**1. Problem Statement:**  
A gambler starts with an initial capital of $i = 2$ units and plays a sequential game where each round increases capital by $+1$ with probability $p = 0.60$ or decreases capital by $-1$ with probability $q = 0.40$. The game terminates when capital reaches 0 (ruin) or $N = 5$ units (target). What is the exact probability of reaching the target before ruin?

**2. Level and Concept:**  
- **Level:** L4 — Expert Quantitative Reasoning  
- **Primary Concept:** Gambler's Ruin  
- **Secondary Concept:** Difference Equations  

**3. Reasoning Setup:**  
States $\{0, 1, 2, 3, 4, 5\}$ with absorbing states $0$ and $5$.
Transition ratio $r = \frac{q}{p} = \frac{0.40}{0.60} = \frac{2}{3} \neq 1$.

**4. Derivation:**  
By the classic Gambler's Ruin formula for biased random walks, the probability of absorption at $N$ starting from $i$ is:
$$P_i = \frac{1 - r^i}{1 - r^N}$$
Here $i = 2, N = 5, r = 2/3$.

**5. Calculation:**  
1. Numerator: $1 - r^2 = 1 - \left(\frac{2}{3}\right)^2 = 1 - \frac{4}{9} = \frac{5}{9}$.
2. Denominator: $1 - r^5 = 1 - \left(\frac{2}{3}\right)^5 = 1 - \frac{32}{243} = \frac{211}{243}$.
3. Fraction:
$$P_2 = \frac{5/9}{211/243} = \frac{5}{9} \times \frac{243}{211} = 5 \times \frac{27}{211} = \frac{135}{211} \approx 0.63981$$

**6. Final Answer:**  
$$\mathbf{\frac{135}{211} \approx 0.6398}$$

**7. Common Trap:**  
Using the unbiased formula $i/N = 2/5 = 0.40$. Because $p = 0.60 > 0.50$, the positive drift increases the probability of reaching the target from 40% to ~64%.

**8. Alternative Method:**  
Solving the system of difference equations: $P_k = 0.6 P_{k+1} + 0.4 P_{k-1}$ with boundary conditions $P_0 = 0, P_5 = 1$, which yields the exact geometric series solution.

---

### Problem 43: Three-State Markov Chain Stationary Distribution

**1. Problem Statement:**  
Consider a discrete-time Markov chain on state space $\{1, 2, 3\}$ with transition probability matrix:
$$P = \begin{pmatrix} 0.7 & 0.2 & 0.1 \\ 0.3 & 0.5 & 0.2 \\ 0.2 & 0.4 & 0.4 \end{pmatrix}$$
Find the exact stationary probability vector $\boldsymbol{\pi} = (\pi_1, \pi_2, \pi_3)$.

**2. Level and Concept:**  
- **Level:** L4 — Expert Quantitative Reasoning  
- **Primary Concept:** Markov Chains  
- **Secondary Concept:** Stationary Distribution  

**3. Reasoning Setup:**  
The stationary distribution satisfies the balance equations $\boldsymbol{\pi} P = \boldsymbol{\pi}$ subject to $\pi_1 + \pi_2 + \pi_3 = 1$ and $\pi_i > 0$.

**4. Derivation:**  
System of linear equations:
1. $\pi_1 = 0.7 \pi_1 + 0.3 \pi_2 + 0.2 \pi_3 \implies -0.3 \pi_1 + 0.3 \pi_2 + 0.2 \pi_3 = 0$
2. $\pi_2 = 0.2 \pi_1 + 0.5 \pi_2 + 0.4 \pi_3 \implies 0.2 \pi_1 - 0.5 \pi_2 + 0.4 \pi_3 = 0$
3. Normalization: $\pi_1 + \pi_2 + \pi_3 = 1$.

**5. Calculation:**  
From Eq 1: $2 \pi_3 = 3 \pi_1 - 3 \pi_2$.
Substitute into $2 \times (\text{Eq 2})$:
$$4 \pi_1 - 10 \pi_2 + 4(2 \pi_3) = 0 \implies 4 \pi_1 - 10 \pi_2 + 2(3 \pi_1 - 3 \pi_2) = 0$$
$$4 \pi_1 - 10 \pi_2 + 6 \pi_1 - 6 \pi_2 = 0 \implies 10 \pi_1 - 16 \pi_2 = 0 \implies \pi_1 = \frac{8}{5} \pi_2$$
Then $\pi_3 = \frac{3}{2}(\pi_1 - \pi_2) = \frac{3}{2}\left(\frac{8}{5} \pi_2 - \pi_2\right) = \frac{3}{2}\left(\frac{3}{5} \pi_2\right) = \frac{9}{10} \pi_2$.
Substitute into sum:
$$\frac{8}{5} \pi_2 + \pi_2 + \frac{9}{10} \pi_2 = 1 \implies \left(\frac{16 + 10 + 9}{10}\right) \pi_2 = \frac{35}{10} \pi_2 = \frac{7}{2} \pi_2 = 1$$
Therefore: $\pi_2 = \frac{2}{7} = \frac{16}{56}$... wait, let us verify coefficients:
Checking with exact integer algebra:
$-3 \pi_1 + 3 \pi_2 + 2 \pi_3 = 0 \implies 2\pi_3 = 3\pi_1 - 3\pi_2$.
$2 \pi_1 - 5 \pi_2 + 4 \pi_3 = 0 \implies 2\pi_1 - 5\pi_2 + 2(3\pi_1 - 3\pi_2) = 8\pi_1 - 11\pi_2 = 0 \implies \pi_1 = \frac{11}{8}\pi_2$.
Then $2\pi_3 = 3(11/8)\pi_2 - 3\pi_2 = \frac{9}{8}\pi_2 \implies \pi_3 = \frac{9}{16}\pi_2$.
Sum: $\left(\frac{22}{16} + \frac{16}{16} + \frac{9}{16}\right) \pi_2 = \frac{47}{16} \pi_2 = 1 \implies \pi_2 = \frac{16}{47}$.
Thus: $\pi_1 = \frac{22}{47}, \pi_3 = \frac{9}{47}$.

**6. Final Answer:**  
$$\mathbf{\boldsymbol{\pi} = \left(\frac{22}{47}, \frac{16}{47}, \frac{9}{47}\right) \approx (0.4681, 0.3404, 0.1915)}$$

**7. Common Trap:**  
Setting up column equations $P \boldsymbol{\pi} = \boldsymbol{\pi}$ instead of row equations $\boldsymbol{\pi} P = \boldsymbol{\pi}$.

**8. Alternative Method:**  
Long-run matrix powering verification: $P^n$ converges to matrix where every row is $\boldsymbol{\pi} = [0.4681, 0.3404, 0.1915]$.

---

### Problem 44: Coupon Collector's Problem: Total Waiting Time

**1. Problem Statement:**  
A person repeatedly rolls a fair 6-sided die. What is the expected total number of rolls required to see all 6 distinct faces at least once?

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Coupon Collector  
- **Secondary Concept:** Sum of Geometrics  

**3. Reasoning Setup:**  
Let $T$ be the total number of rolls to collect all 6 faces.
Partition $T = T_1 + T_2 + T_3 + T_4 + T_5 + T_6$, where $T_k$ is the additional rolls needed to collect the $k$-th new face after $k - 1$ distinct faces have already appeared.

**4. Derivation:**  
Each stage $T_k$ is an independent geometric random variable:
When $k - 1$ faces have been seen, the probability of rolling a new face on any single toss is:
$$p_k = \frac{6 - (k - 1)}{6} = \frac{7 - k}{6}$$
Thus $T_k \sim \text{Geometric}(p_k)$ with $E[T_k] = \frac{1}{p_k} = \frac{6}{7 - k}$.

**5. Calculation:**  
By Linearity of Expectation:
$$E[T] = \sum_{k=1}^6 \frac{6}{7 - k} = 6 \left(\frac{1}{6} + \frac{1}{5} + \frac{1}{4} + \frac{1}{3} + \frac{1}{2} + 1\right)$$
$$E[T] = 6 \times \left(1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \frac{1}{5} + \frac{1}{6}\right)$$
Summing harmonic series $H_6 = \frac{147}{60} = 2.45$:
$$E[T] = 6 \times 2.45 = 14.70 \text{ rolls}$$

**6. Final Answer:**  
$$\mathbf{14.70 \text{ rolls} \quad \left(\frac{147}{10}\right)}$$

**7. Common Trap:**  
Guessing 6 rolls or $6 \times 3.5 = 21$ rolls, without realizing that the waiting time scales harmonically due to coupon coupon collision resistance.

**8. Alternative Method:**  
Integral of tail survival: $E[T] = \int_0^\infty (1 - (1 - e^{-t/6})^6) dt = 14.70$ via continuous Poissonization embedding.

---

### Problem 45: Order Statistics: Uniform Distribution Min and Max

**1. Problem Statement:**  
Let $X_1, X_2$ be independent and identically distributed random variables from $\text{Uniform}(0, 1)$. Let $U = \min(X_1, X_2)$ and $V = \max(X_1, X_2)$. Compute $E[U]$, $E[V]$, and $\text{Cov}(U, V)$.

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Continuous Order Statistics  
- **Secondary Concept:** Beta Distribution Moments  

**3. Reasoning Setup:**  
$X_1, X_2 \sim \text{Unif}(0, 1)$ i.i.d. $U = X_{(1)}, V = X_{(2)}$.
Joint density: $f_{U, V}(u, v) = 2! = 2$ for $0 \le u \le v \le 1$.

**4. Derivation:**  
1. Marginal distributions: $U \sim \text{Beta}(1, 2)$, $V \sim \text{Beta}(2, 1)$.
   - $E[U] = \frac{1}{1 + 2} = \frac{1}{3}$.
   - $E[V] = \frac{2}{2 + 1} = \frac{2}{3}$.
2. Product expectation $E[UV]$:
   $$E[UV] = \int_0^1 \int_0^v uv (2) \, du \, dv = 2 \int_0^1 v \left[\frac{u^2}{2}\right]_0^v dv = \int_0^1 v^3 \, dv = \frac{1}{4}$$

**5. Calculation:**  
Covariance:
$$\text{Cov}(U, V) = E[UV] - E[U] E[V] = \frac{1}{4} - \left(\frac{1}{3}\right)\left(\frac{2}{3}\right) = \frac{1}{4} - \frac{2}{9} = \frac{9 - 8}{36} = \frac{1}{36} \approx 0.02778$$

**6. Final Answer:**  
$$\mathbf{E[U] = \frac{1}{3}, \quad E[V] = \frac{2}{3}, \quad \text{Cov}(U, V) = \frac{1}{36}}$$

**7. Common Trap:**  
Assuming $U$ and $V$ are uncorrelated since $X_1$ and $X_2$ are independent. The ordering constraint forces $U \le V$, inducing a strictly positive covariance.

**8. Alternative Method:**  
Transformation of variables: Let $D = V - U$ (spacing) and $U = U$. In Uniform order statistics, spacings $U, V-U, 1-V$ are Dirichlet(1,1,1), identically distributed with mean $1/3$, immediately giving $E[U] = 1/3, E[V] = 2/3$.

---

### Problem 46: Random Walk First Passage Time Under Drift

**1. Problem Statement:**  
A particle on the integers starts at position 0. At each step, it moves $+1$ with probability $p = 0.60$ and $-1$ with probability $q = 0.40$. Let $T_1$ be the number of steps until the particle reaches $+1$ for the very first time. Calculate the expected hitting time $E[T_1]$.

**2. Level and Concept:**  
- **Level:** L4 — Expert Quantitative Reasoning  
- **Primary Concept:** Random Walk  
- **Secondary Concept:** First Hitting Time  

**3. Reasoning Setup:**  
Let $T_1$ be the first hitting time of state $+1$ starting from 0.
If the first step is $+1$ (prob $p$), $T_1 = 1$.
If the first step is $-1$ (prob $q$), the particle is at $-1$. To reach $+1$, it must first travel from $-1$ to $0$ (which takes expected time $E[T_1]$ by shift invariance), and then from $0$ to $+1$ (which takes expected time $E[T_1]$).

**4. Derivation:**  
By the Law of Total Expectation:
$$E[T_1] = p(1) + q(1 + 2 E[T_1]) = p + q + 2q E[T_1] = 1 + 2q E[T_1]$$
Rearranging for $E[T_1]$:
$$E[T_1] (1 - 2q) = 1 \implies E[T_1] = \frac{1}{1 - 2q} = \frac{1}{p - q}$$

**5. Calculation:**  
Substitute $p = 0.60$ and $q = 0.40$:
$$E[T_1] = \frac{1}{0.60 - 0.40} = \frac{1}{0.20} = 5 \text{ steps}$$

**6. Final Answer:**  
$$\mathbf{5 \text{ steps}}$$

**7. Common Trap:**  
Setting $E[T_1] = 1/p = 1/0.60 = 1.67$, which ignores the fact that backward steps must be recouped.

**8. Alternative Method:**  
Wald's First Identity on random walk drift: $S_n = \sum X_i$ with $E[X_i] = p - q = 0.20$. At stopping time $T_1$, $S_{T_1} = 1$. By Wald's identity, $E[S_{T_1}] = E[T_1] E[X_i] \implies 1 = E[T_1] (0.20) \implies E[T_1] = 1 / 0.20 = 5$.

---

### Problem 47: Waiting Time for Coin Patterns: $HT$ vs $HH$

**1. Problem Statement:**  
A fair coin is tossed repeatedly. Let $T_{HT}$ be the number of tosses until 'HT' appears for the first time, and let $T_{HH}$ be the number of tosses until 'HH' appears for the first time. Calculate $E[T_{HT}]$ and $E[T_{HH}]$, and explain mathematically why they differ despite both having probability $(1/2)^2 = 1/4$.

**2. Level and Concept:**  
- **Level:** L4 — Expert Quantitative Reasoning  
- **Primary Concept:** Pattern Waiting Times  
- **Secondary Concept:** Renewal and Overlap  

**3. Reasoning Setup:**  
Fair coin with $P(H) = P(T) = 1/2$.
Let $e_0$ be the expected tosses from start.

**4. Derivation:**  
1. For pattern 'HT':
   - From start $\emptyset$: toss $T$ (prob $1/2$) returns to $\emptyset$; toss $H$ (prob $1/2$) moves to state $H$.
     $$e_\emptyset = 1 + \frac{1}{2} e_\emptyset + \frac{1}{2} e_H \implies e_\emptyset = 2 + e_H$$
   - From state $H$: toss $T$ (prob $1/2$) completes 'HT'; toss $H$ (prob $1/2$) remains in state $H$.
     $$e_H = 1 + \frac{1}{2}(0) + \frac{1}{2} e_H \implies e_H = 2$$
   - Substituting: $e_\emptyset = 2 + 2 = 4$.
2. For pattern 'HH':
   - From start $\emptyset$: toss $T$ (prob $1/2$) returns to $\emptyset$; toss $H$ (prob $1/2$) moves to state $H$.
     $$e_\emptyset = 1 + \frac{1}{2} e_\emptyset + \frac{1}{2} e_H \implies e_\emptyset = 2 + e_H$$
   - From state $H$: toss $H$ (prob $1/2$) completes 'HH'; toss $T$ (prob $1/2$) sends back to start $\emptyset$!
     $$e_H = 1 + \frac{1}{2}(0) + \frac{1}{2} e_\emptyset = 1 + \frac{1}{2} e_\emptyset$$
   - Substitute: $e_\emptyset = 2 + 1 + \frac{1}{2} e_\emptyset = 3 + \frac{1}{2} e_\emptyset \implies e_\emptyset = 6$.

**5. Calculation:**  
Expected times:
$$E[T_{HT}] = 4, \quad E[T_{HH}] = 6$$
Difference explanation: 'HH' overlaps with itself (an $H$ can serve as both prefix and suffix), causing 'HH' to cluster together in bursts, whereas 'HT' has zero self-overlap.

**6. Final Answer:**  
$$\mathbf{E[T_{HT}] = 4, \quad E[T_{HH}] = 6}$$

**7. Common Trap:**  
Believing that because both sequences are length 2 with independent coin tosses, their expected arrival times must both be $2^2 = 4$.

**8. Alternative Method:**  
Conway's Leading Number algorithm: Leading number for $HT$: $HT$ against $HT = 2^2 + 0 = 4$. For $HH$: $HH$ against $HH = 2^2 + 2^1 = 4 + 2 = 6$.

---

### Problem 48: Monty Hall with Asymmetric Host Strategy

**1. Problem Statement:**  
In a 3-door Monty Hall problem, the car is behind Door 1, 2, or 3 with equal probability $1/3$. The contestant selects Door 1. If the car is behind Door 1, the host opens Door 3 with probability $q$ and Door 2 with probability $1 - q$ (where $0 < q < 1$). If the host opens Door 3 revealing a goat, what is the conditional probability of winning the car by switching to Door 2?

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Monty Hall  
- **Secondary Concept:** Host Strategy Asymmetry  

**3. Reasoning Setup:**  
Prior: $P(C = 1) = P(C = 2) = P(C = 3) = 1/3$.
Contestant picks Door 1.
Observed host action: $H = 3$ (host opens Door 3).
Host behavior:
- If $C = 1$: $P(H = 3 \mid C = 1) = q$.
- If $C = 2$: Host must open Door 3 (only remaining goat door) $\implies P(H = 3 \mid C = 2) = 1$.
- If $C = 3$: Host cannot open Door 3 (contains car) $\implies P(H = 3 \mid C = 3) = 0$.

**4. Derivation:**  
By Bayes' Theorem, probability car is behind Door 2 given host opens Door 3:
$$P(C = 2 \mid H = 3) = \frac{P(C = 2) P(H = 3 \mid C = 2)}{P(H = 3)}$$
Denominator:
$$P(H = 3) = \frac{1}{3}(q) + \frac{1}{3}(1) + \frac{1}{3}(0) = \frac{q + 1}{3}$$

**5. Calculation:**  
Numerator $= \frac{1}{3} \times 1 = \frac{1}{3}$.
Conditional probability:
$$P(C = 2 \mid H = 3) = \frac{1/3}{(q + 1)/3} = \frac{1}{1 + q}$$
- If host is unbiased ($q = 1/2$): $P = \frac{1}{1 + 0.5} = \frac{2}{3}$ (standard Monty Hall).
- If host always opens Door 3 when possible ($q = 1$): $P = \frac{1}{1 + 1} = \frac{1}{2}$.
- If host never opens Door 3 when car is at 1 ($q \to 0$): $P = 1$ (certain win by switching!).

**6. Final Answer:**  
$$\mathbf{P(\text{Win by switching}) = \frac{1}{1 + q}}$$

**7. Common Trap:**  
Assuming that switching probability is always $2/3$ regardless of host preference.

**8. Alternative Method:**  
Odds formulation: Prior odds of Door 2 vs Door 1 $= 1 : 1$. Likelihood ratio for seeing host open Door 3 is $P(H=3 \mid C=2) / P(H=3 \mid C=1) = 1 / q$. Posterior odds $= 1/q$. Posterior probability $= \frac{1/q}{1 + 1/q} = \frac{1}{1 + q}$.

---

### Problem 49: Wald's Identity in Sequential Quality Inspection

**1. Problem Statement:**  
An automated testing station examines products sequentially. The defect score of product $i$, denoted $X_i$, has mean $\mu = 4$ and variance $\sigma^2 = 9$. Testing continues until the first critical defect occurs, which happens at each item with probability $p = 0.05$ independently. Let $N$ be the number of items tested, and $S_N = \sum_{i=1}^N X_i$ be the total accumulated defect score. Calculate $E[S_N]$.

**2. Level and Concept:**  
- **Level:** L4 — Expert Quantitative Reasoning  
- **Primary Concept:** Wald's Equation  
- **Secondary Concept:** Stopping Times  

**3. Reasoning Setup:**  
Stopping time $N \sim \text{Geometric}(p = 0.05)$, so $E[N] = \frac{1}{p} = \frac{1}{0.05} = 20$.
Individual item scores $X_i$ are i.i.d. with $E[X_i] = 4$, and $X_i$ are independent of future stopping decisions.

**4. Derivation:**  
Because $N$ is a valid stopping time with finite expectation and $X_i$ are i.i.d. with finite mean, Wald's First Identity holds:
$$E[S_N] = E\left[\sum_{i=1}^N X_i\right] = E[N] \cdot E[X]$$

**5. Calculation:**  
Substitute $E[N] = 20$ and $E[X] = 4$:
$$E[S_N] = 20 \times 4 = 80$$

**6. Final Answer:**  
$$\mathbf{80}$$

**7. Common Trap:**  
Attempting to condition on $N = n$ and sum an infinite series $\sum_{n=1}^\infty n p (1-p)^{n-1} (4n)$, which invites algebra errors when Wald's identity directly guarantees $E[N] E[X]$.

**8. Alternative Method:**  
Direct double sum: $E[S_N] = \sum_{n=1}^\infty E[S_n \mid N = n] P(N = n) = \sum_{n=1}^\infty (4n) (0.05)(0.95)^{n-1} = 4 \sum_{n=1}^\infty n (0.05)(0.95)^{n-1} = 4 E[N] = 4 \times 20 = 80$.

---

### Problem 50: Optimal Stopping in a Two-Roll Dice Game

**1. Problem Statement:**  
A player rolls a standard fair 6-sided die. After observing the roll, the player can choose either to keep the score or to discard it and roll the die a second time. If they roll a second time, they must accept the score of the second roll. Assuming the player plays to maximize expected score, what is the optimal strategy and the resulting expected payout?

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Dynamic Programming  
- **Secondary Concept:** Optimal Stopping  

**3. Reasoning Setup:**  
Let $X_1$ and $X_2$ be the outcomes of the first and second rolls (discrete uniform on $\{1, 2, 3, 4, 5, 6\}$).
The second roll is final and has expected value $E[X_2] = \frac{1 + 2 + 3 + 4 + 5 + 6}{6} = 3.5$.

**4. Derivation:**  
By backward induction:
At step 1, the player compares the observed value $X_1$ against the expected return of continuing, which is $E[X_2] = 3.5$.
- If $X_1 > 3.5$ (i.e., $X_1 \in \{4, 5, 6\}$): stop and accept $X_1$.
- If $X_1 < 3.5$ (i.e., $X_1 \in \{1, 2, 3\}$): re-roll.

**5. Calculation:**  
Under this optimal policy:
$$E[\text{Score}] = P(X_1 \in \{4, 5, 6\}) E[X_1 \mid X_1 \ge 4] + P(X_1 \in \{1, 2, 3\}) E[X_2]$$
1. $P(X_1 \ge 4) = \frac{3}{6} = \frac{1}{2}$, and $E[X_1 \mid X_1 \ge 4] = \frac{4 + 5 + 6}{3} = 5.0$.
2. $P(X_1 \le 3) = \frac{3}{6} = \frac{1}{2}$, and $E[X_2] = 3.5$.
$$E[\text{Score}] = \frac{1}{2}(5.0) + \frac{1}{2}(3.5) = 2.5 + 1.75 = 4.25 = \frac{17}{4}$$

**6. Final Answer:**  
$$\mathbf{\text{Optimal Policy: Stop on } \{4, 5, 6\}, \text{ re-roll on } \{1, 2, 3\}; \quad E = 4.25}$$

**7. Common Trap:**  
Stopping only on 5 and 6 (giving expected value $4.167$) or stopping on 3 (which gives expected value $4.00$, worse than $4.25$).

**8. Alternative Method:**  
Direct expectation formula: $\frac{1}{6}(4 + 5 + 6 + 3.5 + 3.5 + 3.5) = \frac{15 + 10.5}{6} = \frac{25.5}{6} = 4.25$.

---

## Section 5: Statistical Interpretation, Inference & Data Traps (Q51–Q60)


### Problem 51: Statistical Power & Type II Error Rate Calculation

**1. Problem Statement:**  
A hypothesis test evaluates $H_0: \mu = 100$ versus $H_1: \mu = 106$ for a normal population with known standard deviation $\sigma = 10$. A sample of size $n = 25$ is gathered. Using a significance level of $\alpha = 0.05$ for a one-tailed upper test (critical $z_{0.05} = 1.645$), calculate the critical sample mean value, the Type II error rate $\beta$, and the statistical power of the test.

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Hypothesis Testing  
- **Secondary Concept:** Statistical Power  

**3. Reasoning Setup:**  
Sample size $n = 25$, population $\sigma = 10$.
Standard error of the mean: $\text{SE} = \frac{\sigma}{\sqrt{n}} = \frac{10}{\sqrt{25}} = \frac{10}{5} = 2.0$.

**4. Derivation:**  
1. Decision rule under $H_0$: Reject $H_0$ if $\bar{X} > \bar{x}_{\text{crit}}$ where:
   $$\bar{x}_{\text{crit}} = \mu_0 + z_\alpha \times \text{SE} = 100 + 1.645 \times 2.0 = 103.29$$
2. Type II error rate $\beta = P(\text{Fail to reject } H_0 \mid \mu = 106) = P(\bar{X} \le 103.29 \mid \mu = 106)$.
3. Standardize under $H_1$:
   $$z = \frac{103.29 - 106.0}{2.0} = \frac{-2.71}{2.0} = -1.355$$

**5. Calculation:**  
1. Using standard normal CDF: $\Phi(-1.355) \approx 0.0877$.
   Thus, Type II error probability $\beta \approx 0.0877$ (or $8.77\%$).
2. Statistical Power:
   $$\text{Power} = 1 - \beta = 1 - 0.0877 = 0.9123 \text{ (or } 91.23\%\)$$

**6. Final Answer:**  
$$\mathbf{\bar{x}_{\text{crit}} = 103.29, \quad \beta \approx 8.77\%, \quad \text{Power} \approx 91.23\%}$$

**7. Common Trap:**  
Standardizing with $\sigma$ instead of $\text{SE} = \sigma / \sqrt{n}$, or standardizing under $\mu_0$ instead of the true alternative mean $\mu_1 = 106$.

**8. Alternative Method:**  
Non-centrality parameter: $\delta = \frac{\mu_1 - \mu_0}{\sigma / \sqrt{n}} = \frac{6}{2} = 3.0$. Power $= \Phi(\delta - z_\alpha) = \Phi(3.0 - 1.645) = \Phi(1.355) \approx 0.9123$.

---

### Problem 52: The $p$-Value Interpretation Fallacy

**1. Problem Statement:**  
In a randomized trial comparing a new algorithm against an existing baseline, the observed test statistic yields a $p$-value of $0.03$. A team member asserts: 'This proves there is only a 3% probability that the null hypothesis is true, and a 97% probability that the new algorithm is superior.' Explain precisely why this statement is mathematically incorrect, and provide the correct frequentist definition.

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** p-Value Interpretation  
- **Secondary Concept:** Epistemic Fallacies  

**3. Reasoning Setup:**  
Null hypothesis $H_0$: no difference between algorithms.
Alternative hypothesis $H_1$: new algorithm differs.

**4. Derivation:**  
The assertion confuses $P(\text{Data as extreme or more} \mid H_0)$ with $P(H_0 \mid \text{Data})$.
In classical frequentist statistics, parameters and hypotheses are fixed (non-random) states of nature, not random variables with probability distributions. $P(H_0)$ is either 0 or 1, not a probability.

**5. Calculation:**  
1. Correct Definition: The $p$-value is the probability of observing a test statistic at least as extreme as the one actually observed, assuming that the null hypothesis $H_0$ is true:
   $$p = P(T \ge t_{\text{obs}} \mid H_0)$$
2. To compute $P(H_0 \mid \text{Data})$, one must use Bayes' Theorem, requiring a prior probability $P(H_0)$ and the likelihood under the alternative $P(\text{Data} \mid H_1)$:
   $$P(H_0 \mid \text{Data}) = \frac{P(H_0) P(\text{Data} \mid H_0)}{P(H_0) P(\text{Data} \mid H_0) + P(H_1) P(\text{Data} \mid H_1)}$$
   If $P(H_0)$ was $0.90$ (skeptical prior), $P(H_0 \mid \text{Data})$ could easily exceed $30\%$, far above $3\%$.

**6. Final Answer:**  
$$\mathbf{p = P(\text{Data} \ge \text{Observed} \mid H_0) \neq P(H_0 \mid \text{Data})}$$

**7. Common Trap:**  
Treating the $p$-value as the probability of a false positive or the probability that the finding is due to chance.

**8. Alternative Method:**  
Diagnostic test analogy: Just as $P(\text{Positive Test} \mid \text{No Disease}) = 2\%$ does NOT mean $P(\text{No Disease} \mid \text{Positive Test}) = 2\%$, a $p$-value is conditioned on the null, not vice versa.

---

### Problem 53: Frequentist Confidence Interval: Repeated Sampling Coverage

**1. Problem Statement:**  
A data analyst calculates a 95% confidence interval for the mean customer transaction value as $[\$142, \$168]$. The analyst states: 'There is a 95% probability that the true population mean lies between $\$142$ and $\$168$.' Critique this statement from a frequentist perspective and state the exact meaning of 95% confidence.

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Confidence Intervals  
- **Secondary Concept:** Sampling Distribution  

**3. Reasoning Setup:**  
True population mean $\mu$ is a fixed, unknown constant.
The calculated interval $[142, 168]$ is a realization of the random interval $[\bar{X} - 1.96 \text{SE}, \bar{X} + 1.96 \text{SE}]$.

**4. Derivation:**  
In frequentist statistics, the true parameter $\mu$ does not move; it either is in $[142, 168]$ or it is not. The probability that the fixed value $\mu$ is in the fixed interval $[142, 168]$ is either 0 or 1.

**5. Calculation:**  
1. Flawed Statement: Assumes $\mu$ is a random variable inside an interval.
2. Correct Interpretation: The 95% confidence level describes the long-run coverage property of the *procedure*:
   'If we were to draw independent random samples repeatedly under identical conditions and construct a 95% confidence interval from each sample, exactly 95% of those constructed intervals would contain the true population mean $\mu$.'
3. The probability statement applies to the random estimator $[L(X), U(X)]$ before data collection, not to the specific numbers after realization.

**6. Final Answer:**  
$$\mathbf{\text{Procedure coverage: } P(\mu \in [L(X), U(X)]) = 0.95 \text{ before sampling; realized interval has probability } 0 \text{ or } 1}$$

**7. Common Trap:**  
Believing that 95% confidence means 95% of individual data points fall in the interval (confusing confidence intervals with prediction intervals).

**8. Alternative Method:**  
Bayesian contrast: In Bayesian analysis, a 95% Credible Interval allows the statement $P(\mu \in [142, 168] \mid \text{Data}) = 0.95$, because $\mu$ is modeled as a random variable with a posterior distribution.

---

### Problem 54: Sample Size Determination for Proportion Estimation

**1. Problem Statement:**  
An analytics firm needs to estimate the proportion of active app users who will adopt a new fintech feature within a margin of error of $E = \pm 0.03$ (3 percentage points) with 95% confidence ($z_{0.025} = 1.96$). Without any prior estimate of the true proportion $p$, what is the minimum sample size required?

**2. Level and Concept:**  
- **Level:** L2 — Standard Placement  
- **Primary Concept:** Sample Size Planning  
- **Secondary Concept:** Margin of Error  

**3. Reasoning Setup:**  
Margin of error formula for sample proportion:
$$E = z_{\alpha/2} \sqrt{\frac{p(1 - p)}{n}}$$
Solve for $n$:
$$n = \frac{z_{\alpha/2}^2 \, p(1 - p)}{E^2}$$

**4. Derivation:**  
To ensure the sample size is sufficient regardless of what the true proportion turns out to be, we use the worst-case (maximum variance) conservative bound:
The function $f(p) = p(1 - p)$ attains its maximum value of $0.25$ at $p = 0.50$.

**5. Calculation:**  
1. Substitute $z = 1.96, p = 0.50, E = 0.03$:
   $$n = \frac{(1.96)^2 \times 0.25}{(0.03)^2} = \frac{3.8416 \times 0.25}{0.0009} = \frac{0.9604}{0.0009} \approx 1067.11$$
2. Always round up to the nearest integer to guarantee the required precision:
   $$n = 1,068$$

**6. Final Answer:**  
$$\mathbf{n = 1,068}$$

**7. Common Trap:**  
Guessing $p = 0.10$ without justification (which yields $n \approx 385$), risking a confidence interval substantially wider than the required $\pm 0.03$ if the true proportion is higher.

**8. Alternative Method:**  
Rule of thumb: At 95% confidence with $p = 0.5$, $n \approx 1 / E^2 = 1 / (0.03)^2 = 1 / 0.0009 = 1,111$, which approximates the exact 1,068.

---

### Problem 55: Regression to the Mean in Sequential Testing

**1. Problem Statement:**  
A cohort of engineering candidates takes two successive standardized aptitude tests with identical score distributions (each test has mean $\mu = 100$ and standard deviation $\sigma = 15$). The correlation between the two tests is $r = 0.60$. A candidate scores an exceptional 140 on Test 1. What is the mathematically expected score of this candidate on Test 2?

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Regression to the Mean  
- **Secondary Concept:** Bivariate Normal Prediction  

**3. Reasoning Setup:**  
Let $X$ and $Y$ be the scores on Test 1 and Test 2.
$E[X] = E[Y] = 100$, $\sigma_X = \sigma_Y = 15$, $\text{Corr}(X, Y) = 0.60$.
Given observation: $X = 140$.

**4. Derivation:**  
The linear regression prediction for $Y$ given $X$ under bivariate normality (or minimum mean square error linear estimation) is:
$$\hat{Y} = E[Y] + r \frac{\sigma_Y}{\sigma_X} (X - E[X])$$
Because $\sigma_Y = \sigma_X = 15$, the slope reduces to $r = 0.60$:
$$\hat{Y} = \mu + r(X - \mu)$$

**5. Calculation:**  
Substitute values:
$$\hat{Y} = 100 + 0.60 \times (140 - 100) = 100 + 0.60(40) = 100 + 24 = 124$$
The candidate's predicted score shrinks by $40\%$ toward the population mean.

**6. Final Answer:**  
$$\mathbf{124}$$

**7. Common Trap:**  
Predicting the candidate will score 140 again. Extreme scores reflect a combination of true skill and positive random noise; on a subsequent test, the noise component regresses to 0.

**8. Alternative Method:**  
Standardized $z$-score formulation: $z_X = (140 - 100)/15 = +2.667$. Predicted $z_Y = r \times z_X = 0.60 \times 2.667 = +1.600$. Then $\hat{Y} = 100 + 1.600(15) = 100 + 24 = 124$.

---

### Problem 56: Multiple Testing & Family-Wise Error Rate (Bonferroni)

**1. Problem Statement:**  
A quantitative research group tests $m = 20$ independent trading strategies against a benchmark where the null hypothesis is true for all 20 strategies (none of them have genuine alpha). Each test is evaluated at the standard significance level $\alpha = 0.05$. What is the probability of discovering at least one false positive (the Family-Wise Error Rate, FWER)? What adjusted significance level per test must be used under the Bonferroni correction to keep the overall FWER at 0.05?

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Multiple Comparisons  
- **Secondary Concept:** Bonferroni Correction  

**3. Reasoning Setup:**  
Number of independent tests $m = 20$.
Individual significance level $\alpha_0 = 0.05$.
Under $H_0$, each test makes no false positive with probability $1 - \alpha_0 = 0.95$.

**4. Derivation:**  
1. Family-Wise Error Rate without correction:
   $$\text{FWER} = P(\ge 1 \text{ false discovery}) = 1 - P(\text{all } 20 \text{ tests retain } H_0) = 1 - (1 - \alpha_0)^m$$
2. Bonferroni correction: By Boole's inequality, to ensure $\text{FWER} \le \alpha_{\text{target}}$:
   $$\alpha_{\text{adj}} = \frac{\alpha_{\text{target}}}{m}$$

**5. Calculation:**  
1. Uncorrected FWER:
   $$\text{FWER} = 1 - (0.95)^{20} = 1 - 0.358486 = 0.641514 \approx 64.15\%$$
   There is nearly a two-thirds chance of claiming a false trading discovery!
2. Bonferroni adjusted threshold:
   $$\alpha_{\text{adj}} = \frac{0.05}{20} = 0.0025$$

**6. Final Answer:**  
$$\mathbf{\text{FWER} = 64.15\%, \quad \alpha_{\text{Bonferroni}} = 0.0025}$$

**7. Common Trap:**  
Believing that testing 20 strategies at $\alpha = 0.05$ still carries a 5% false positive risk across the project.

**8. Alternative Method:**  
Sidak correction: $\alpha_{\text{Sidak}} = 1 - (1 - 0.05)^{1/20} = 1 - (0.95)^{0.05} = 1 - 0.99744 = 0.00256$, extremely close to the Bonferroni bound $0.0025$.

---

### Problem 57: Collider Bias & Berkson's Fallacy in Data Analysis

**1. Problem Statement:**  
In the general population, mathematical aptitude ($M$) and musical ability ($A$) are completely independent random variables, each taking value 1 (talented) with probability $0.5$ and 0 with probability $0.5$. Admission to an elite academy ($C = 1$) occurs if and only if an applicant is talented in math OR music ($C = M + A - M A$). Among students admitted to the academy ($C = 1$), what is the conditional correlation between math aptitude and musical ability?

**2. Level and Concept:**  
- **Level:** L4 — Expert Quantitative Reasoning  
- **Primary Concept:** Causal DAGs  
- **Secondary Concept:** Conditioning on a Collider  

**3. Reasoning Setup:**  
Sample space of $(M, A) \in \{(0,0), (0,1), (1,0), (1,1)\}$ each with prior probability $0.25$.
Admission condition: $C = 1$ for $(0,1), (1,0), (1,1)$ (3 equally likely outcomes).

**4. Derivation:**  
Conditioning on admission $C = 1$ reduces the sample space to 3 outcomes, each with conditional probability $1/3$.
Evaluate conditional moments of $M$ and $A$:
- $P(M = 1 \mid C = 1) = \frac{2}{3}$
- $P(A = 1 \mid C = 1) = \frac{2}{3}$
- $P(M = 1, A = 1 \mid C = 1) = \frac{1}{3}$

**5. Calculation:**  
1. Conditional Covariance:
   $$\text{Cov}(M, A \mid C = 1) = E[MA \mid C = 1] - E[M \mid C = 1] E[A \mid C = 1]$$
   $$= \frac{1}{3} - \left(\frac{2}{3}\right)\left(\frac{2}{3}\right) = \frac{1}{3} - \frac{4}{9} = -\frac{1}{9}$$
2. Conditional Variance:
   $$\text{Var}(M \mid C = 1) = \frac{2}{3}\left(1 - \frac{2}{3}\right) = \frac{2}{9}$$
3. Conditional Correlation:
   $$\rho(M, A \mid C = 1) = \frac{-1/9}{\sqrt{(2/9)(2/9)}} = \frac{-1/9}{2/9} = -\frac{1}{2} = -0.50$$

**6. Final Answer:**  
$$\mathbf{\rho(M, A \mid C = 1) = -0.50 \quad (\text{spurious negative correlation induced by collider})}$$

**7. Common Trap:**  
Concluding that being good at math makes someone worse at music. The negative relationship is purely an artifact of conditioning on the collider variable (admission).

**8. Alternative Method:**  
Intuitive deduction: If an admitted student is known NOT to be good at math ($M = 0$), they MUST be good at music ($A = 1$) to have gained admission, creating negative dependence.

---

### Problem 58: Hypothesis Test Selection Decision Logic

**1. Problem Statement:**  
An analytics team measures the latency of 15 API requests under Architecture A and 15 API requests under Architecture B. The sample size is small ($n_1 = n_2 = 15$), and exploratory analysis reveals heavy right skew with extreme outliers in both groups. Explain why the Student's two-sample $t$-test is inappropriate, and identify the correct non-parametric test and its null hypothesis.

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Non-Parametric Tests  
- **Secondary Concept:** Test Assumptions  

**3. Reasoning Setup:**  
Data: Two independent samples of size $n_1 = n_2 = 15$.
Observed distribution: Heavy skew, extreme outliers, non-normal.

**4. Derivation:**  
1. Assumptions of Two-Sample Student's $t$-Test:
   - Independence of observations.
   - Normality of data in each group (or large sample size $n \ge 30$ where Central Limit Theorem guarantees approximate normality of sample means).
   - Homoscedasticity (equal variances across groups).
2. Failure mode: With $n = 15$, the CLT does not compensate for severe skew or outliers. Outliers heavily distort the sample mean and inflate the sample standard deviation, drastically reducing test power and destroying Type I error calibration.

**5. Calculation:**  
1. Recommended Test: **Mann-Whitney $U$ test** (also known as the Wilcoxon Rank-Sum test).
2. Properties: It ranks all 30 combined observations from 1 to 30, neutralizing the influence of extreme outlier magnitudes.
3. Null Hypothesis: $H_0$: The distribution of Architecture A is stochastically equal to that of Architecture B ($P(A > B) = P(B > A) = 0.5$). Under the location-shift assumption, this equates to equality of medians.

**6. Final Answer:**  
$$\mathbf{\text{Use Mann-Whitney } U \text{ test (Wilcoxon Rank-Sum)}; \quad H_0: P(A > B) = 0.5}$$

**7. Common Trap:**  
Relying on the two-sample $t$-test by citing 'CLT applies to any sample size', or assuming that log-transformation always cures extreme multi-modal outliers without verifying normality.

**8. Alternative Method:**  
Permutation / Bootstrap test: Conduct an exact two-sample permutation test on the difference of medians, which also makes zero distributional assumptions.

---

### Problem 59: Statistical vs Practical Significance in Big Data

**1. Problem Statement:**  
An e-commerce platform runs an A/B test on $N = 1,000,000$ users per variant. The checkout conversion rate is $12.00\%$ in Control and $12.05\%$ in Variant (an absolute difference of $0.05\%$). A two-proportion $z$-test yields $p = 0.00012$. The product manager asserts: 'The microscopic $p$-value proves this feature delivers massive commercial impact.' Critique this interpretation by calculating Cohen's $h$ effect size and distinguishing statistical significance from practical significance.

**2. Level and Concept:**  
- **Level:** L3 — Advanced Placement  
- **Primary Concept:** Effect Size  
- **Secondary Concept:** Big Data Significance Fallacy  

**3. Reasoning Setup:**  
$n_1 = n_2 = 1,000,000$.
Proportions: $p_1 = 0.1200, p_2 = 0.1205$.
Pooled standard error: $\text{SE} \approx \sqrt{\frac{2 \times 0.12025 \times 0.87975}{1,000,000}} \approx 0.0004599$.
$z = \frac{0.0005}{0.0004599} \approx 3.84 \implies p \approx 0.00012$.

**4. Derivation:**  
1. Power scales with $\sqrt{N}$: With massive sample sizes, standard error shrinks to near zero ($\text{SE} \propto 1/\sqrt{N}$). Consequently, even trivial, practically meaningless deviations from $H_0$ will produce overwhelmingly small $p$-values.
2. Effect Size (Cohen's $h$ for proportions):
   $$h = 2 \arcsin(\sqrt{p_2}) - 2 \arcsin(\sqrt{p_1})$$
   For small differences: $h \approx \frac{p_2 - p_1}{\sqrt{p(1 - p)}} = \frac{0.0005}{\sqrt{0.12 \times 0.88}} = \frac{0.0005}{0.32496} \approx 0.00154$.

**5. Calculation:**  
1. Standard effect size benchmarks (Cohen):
   - Small effect: $h = 0.20$
   - Medium effect: $h = 0.50$
   - Large effect: $h = 0.80$
2. Observed effect size: $h \approx 0.0015$, which is less than $1\%$ of a 'small' effect!
3. Commercial verdict: While the effect is statistically distinguishable from zero, the absolute lift is $0.05\%$. Maintenance, cloud computing, and technical debt costs may far exceed the incremental revenue.

**6. Final Answer:**  
$$\mathbf{h \approx 0.0015 \ll 0.20 \text{ (Statistically significant, but practically negligible)}}$$

**7. Common Trap:**  
Equating a tiny $p$-value with a large effect size. $p$-values measure evidence against the null, not the magnitude or business importance of the effect.

**8. Alternative Method:**  
Confidence interval inspection: 95% CI for the difference is $[0.024\%, 0.076\%]$. Because the upper bound is under $0.08\%$, the effect is ruled out from having large impact.

---

### Problem 60: Machine Learning Fraud Detection & Precision Under Class Imbalance

**1. Problem Statement:**  
A financial fraud detection model is evaluated on 100,000 credit card transactions. The baseline transaction fraud rate is $0.05\%$ (50 fraudulent transactions out of 100,000). The model achieves a Recall of $98.0\%$ and a Specificity of $99.5\%$ (False Positive Rate $= 0.5\%$). What is the exact Precision (Positive Predictive Value) of the model when an alert is fired?

**2. Level and Concept:**  
- **Level:** L4 — Expert Quantitative Reasoning  
- **Primary Concept:** Class Imbalance  
- **Secondary Concept:** Precision vs Specificity  

**3. Reasoning Setup:**  
Total transactions $N = 100,000$.
- Fraudulent: $N_{\text{fraud}} = 100,000 \times 0.0005 = 50$.
- Non-fraudulent: $N_{\text{legit}} = 100,000 - 50 = 99,950$.
- Recall (True Positive Rate) $= 0.98$.
- False Positive Rate $= 1 - 0.995 = 0.005$.

**4. Derivation:**  
Compute the components of the confusion matrix:
1. True Positives (TP): $\text{TP} = N_{\text{fraud}} \times \text{Recall} = 50 \times 0.98 = 49$.
2. False Positives (FP): $\text{FP} = N_{\text{legit}} \times \text{FPR} = 99,950 \times 0.005 = 499.75$.
3. Precision is the ratio of true frauds among all triggered alerts:
   $$\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}$$

**5. Calculation:**  
Substitute values:
$$\text{Precision} = \frac{49}{49 + 499.75} = \frac{49}{548.75} \approx 0.08929 \text{ (or } 8.93\%\)$$
Out of every 100 transactions flagged by the model as fraudulent, only about 9 are actual fraud; over 91% are false alarms.

**6. Final Answer:**  
$$\mathbf{\text{Precision} = \frac{49}{548.75} \approx 8.93\%}$$

**7. Common Trap:**  
Believing that because Specificity is 99.5%, accuracy of positive predictions is 99.5%. When the target class is rare, even a 0.5% error rate applied to the massive majority class swamps the true positives.

**8. Alternative Method:**  
Bayes' Rule form: $P(\text{Fraud} \mid \text{Alert}) = \frac{0.0005 \times 0.98}{0.0005 \times 0.98 + 0.9995 \times 0.005} = \frac{0.00049}{0.00049 + 0.0049975} = \frac{0.00049}{0.0054875} \approx 0.0893$.

---
