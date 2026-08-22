# Probability

## Concept Definitions

- **Random Experiment**: An experiment whose outcome cannot be predicted with certainty.
- **Sample Space ($S$)**: The set of all possible outcomes.
- **Event ($E$)**: A subset of the sample space.
- **Mutually Exclusive Events**: Events that cannot occur simultaneously. If $A$ and $B$ are mutually exclusive, $A \cap B = \emptyset$.
- **Independent Events**: The occurrence of one does not affect the probability of the other.

---

## Key Formulas & Shortcuts

### Basic Probability
$$P(E) = \frac{n(E)}{n(S)}$$
where $n(E)$ = number of favorable outcomes, $n(S)$ = total possible outcomes.

- $0 \le P(E) \le 1$
- $P(E') = 1 - P(E)$ (complement rule)

### Addition Theorem
- For any two events $A$ and $B$:
  $$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
- If $A$ and $B$ are mutually exclusive:
  $$P(A \cup B) = P(A) + P(B)$$

### Multiplication Theorem
- If $A$ and $B$ are independent:
  $$P(A \cap B) = P(A) \times P(B)$$

### Standard 52-Card Deck
- Total cards $= 52$; 4 suits (13 each).
- Face cards $= 12$ (4 Jacks, 4 Queens, 4 Kings).
- Aces $= 4$ (not face cards).

---

## Practice Problems

### Problem 1
Two unbiased dice are rolled. Find the probability that the sum is exactly 8.

### Problem 2
One card is drawn from a 52-card deck. What is the probability that it is either a Red Card or a King?

### Problem 3
A bag contains 5 red, 4 blue, and 3 green balls. Three balls are drawn at random. Find the probability that 2 are red and 1 is blue.

### Problem 4
Three unbiased coins are tossed. What is the probability of getting at least two heads?

### Problem 5
Two cards are drawn together from 52 cards. What is the probability that both are Kings?

---

## Step-by-Step Solutions

### Solution 1
1. Sample space size $n(S) = 6 \times 6 = 36$.
2. Favorable pairs for sum 8: $\{(2,6), (3,5), (4,4), (5,3), (6,2)\}$. So $n(E) = 5$.
3. Probability:
   $$P(E) = \frac{5}{36}$$
4. **Answer**: **$\frac{5}{36}$**.

### Solution 2
1. Let $A$ = Red Card, $B$ = King.
   - $P(A) = \frac{26}{52}$, $P(B) = \frac{4}{52}$.
2. Overlap (Red Kings) $= 2$ (King of Hearts, King of Diamonds).
   - $P(A \cap B) = \frac{2}{52}$.
3. Apply addition theorem:
   $$P(A \cup B) = \frac{26}{52} + \frac{4}{52} - \frac{2}{52} = \frac{28}{52} = \frac{7}{13}$$
4. **Answer**: **$\frac{7}{13}$**.

### Solution 3
1. Total ways to draw 3 balls from 12:
   $$n(S) = 12C_3 = \frac{12 \times 11 \times 10}{3 \times 2 \times 1} = 220$$
2. Favorable ways (2 red from 5, 1 blue from 4):
   $$n(E) = 5C_2 \times 4C_1 = 10 \times 4 = 40$$
3. Probability:
   $$P(E) = \frac{40}{220} = \frac{2}{11}$$
4. **Answer**: **$\frac{2}{11}$**.

### Solution 4
1. Tossing 3 coins: $n(S) = 2^3 = 8$.
   - Outcomes: $\{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\}$.
2. At least 2 heads: $\{HHH, HHT, HTH, THH\}$. So $n(E) = 4$.
3. Probability:
   $$P(E) = \frac{4}{8} = \frac{1}{2}$$
4. **Answer**: **$\frac{1}{2}$**.

### Solution 5
1. Total ways to draw 2 cards from 52:
   $$n(S) = 52C_2 = \frac{52 \times 51}{2} = 1326$$
2. Ways to draw 2 kings from 4:
   $$n(E) = 4C_2 = \frac{4 \times 3}{2} = 6$$
3. Probability:
   $$P(E) = \frac{6}{1326} = \frac{1}{221}$$
4. **Answer**: **$\frac{1}{221}$**.

---

## References

* [Aptitude](https://github.com/DKS-MANAGER/Aptitude) — Probability
* [Aptitude-For-Placements](https://github.com/DKS-MANAGER/Aptitude-For-Placements) — Probability practice problems
