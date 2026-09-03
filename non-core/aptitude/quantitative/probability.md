# Probability

## Concept Definitions

- **Experiment**: An operation with well-defined outcomes.
- **Sample Space (S)**: Set of all possible outcomes.
- **Event (E)**: Subset of sample space.
- **Probability**: $P(E) = \frac{n(E)}{n(S)}$ where $n(E)$ = favorable outcomes, $n(S)$ = total outcomes.

---

## Key Formulas & Shortcuts

### Basic Probability
| Formula | Equation |
|---------|----------|
| Probability | $P(E) = \frac{n(E)}{n(S)}$ |
| Complement | $P(E') = 1 - P(E)$ |
| Range | $0 \leq P(E) \leq 1$ |

### Addition Rule
- **Mutually Exclusive**: $P(A \cup B) = P(A) + P(B)$
- **Not Mutually Exclusive**: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$

### Multiplication Rule
- **Independent Events**: $P(A \cap B) = P(A) \times P(B)$
- **Dependent Events**: $P(A \cap B) = P(A) \times P(B|A)$

### Conditional Probability
$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

### Bayes' Theorem
$$P(A|B) = \frac{P(B|A) \times P(A)}{P(B)}$$
Where $P(B) = P(B|A)P(A) + P(B|A')P(A')$

### Odds
- Odds in favor: $\frac{P(E)}{P(E')}$
- Odds against: $\frac{P(E')}{P(E)}$

### Shortcut: At Least One
$$P(\text{at least one}) = 1 - P(\text{none})$$

### Shortcut: Exactly One
$$P(\text{exactly one}) = P(A)P(B') + P(A')P(B)$$

---

## Practice Problems (10 Problems)

### Problem 1
A bag contains 5 red, 4 blue, and 3 green balls. Two balls are drawn at random. Find the probability that both are red.

### Problem 2
A die is rolled twice. Find the probability that the sum of numbers is 7.

### Problem 3
Two cards are drawn from a standard deck of 52 cards without replacement. Find the probability that both are aces.

### Problem 4
A bag contains 6 white and 4 black balls. Two balls are drawn one by one with replacement. Find the probability that both are white.

### Problem 5
The probability that A solves a problem is 2/3 and B solves it is 3/4. Find the probability that the problem is solved if both try independently.

### Problem 6
A box contains 10 bulbs, 3 are defective. Two bulbs are drawn at random. Find the probability that at least one is defective.

### Problem 7
In a class, 40% students study Math, 30% study Physics, and 20% study both. A student is selected at random. Find the probability that he studies Math given that he studies Physics.

### Problem 8
A man speaks truth 3 out of 4 times. He throws a die and reports it is a 6. Find the probability that it is actually a 6.

### Problem 9
Two dice are thrown. Find the probability that the sum is a prime number.

### Problem 10
A bag contains 4 red, 5 blue, and 6 green balls. Three balls are drawn at random. Find the probability that they are of different colors.

---

## Step-by-Step Solutions

### Solution 1
1. Total balls = 12. Total ways = $^{12}C_2 = 66$.
2. Favorable ways = $^5C_2 = 10$.
3. $P = 10/66 = 5/33$.
4. **Answer**: **5/33**.

### Solution 2
1. Total outcomes = $6 \times 6 = 36$.
2. Favorable pairs for sum 7: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1) = 6 ways.
3. $P = 6/36 = 1/6$.
4. **Answer**: **1/6**.

### Solution 3
1. Total ways = $^{52}C_2 = 1326$.
2. Favorable ways = $^4C_2 = 6$.
3. $P = 6/1326 = 1/221$.
4. **Answer**: **1/221**.

### Solution 4
1. With replacement: $P(\text{white}) = 6/10 = 3/5$.
3. $P(\text{both white}) = (3/5) \times (3/5) = 9/25$.
4. **Answer**: **9/25**.

### Solution 5
1. $P(A) = 2/3$, $P(B) = 3/4$.
2. $P(\text{neither}) = (1/3) \times (1/4) = 1/12$.
3. $P(\text{solved}) = 1 - 1/12 = 11/12$.
4. **Answer**: **11/12**.

### Solution 6
1. Total ways = $^{10}C_2 = 45$.
2. Non-defective = 7. Ways to choose 2 non-defective = $^7C_2 = 21$.
3. $P(\text{none defective}) = 21/45 = 7/15$.
4. $P(\text{at least one defective}) = 1 - 7/15 = 8/15$.
5. **Answer**: **8/15**.

### Solution 7
1. $P(M) = 0.4$, $P(P) = 0.3$, $P(M \cap P) = 0.2$.
2. $P(M|P) = P(M \cap P) / P(P) = 0.2 / 0.3 = 2/3$.
3. **Answer**: **2/3**.

### Solution 8
1. Let $T$ = truth, $R$ = reports 6.
2. $P(T) = 3/4$, $P(T') = 1/4$.
3. $P(R|T) = 1/6$, $P(R|T') = 1/4 \times 1/6 = 1/24$ (lies and says 6).
4. $P(R) = P(R|T)P(T) + P(R|T')P(T') = (1/6)(3/4) + (1/24)(1/4) = 1/8 + 1/96 = 13/96$.
5. $P(T|R) = \frac{P(R|T)P(T)}{P(R)} = \frac{(1/6)(3/4)}{13/96} = \frac{1/8}{13/96} = \frac{12}{13}$.
6. **Answer**: **12/13**.

### Solution 9
1. Total outcomes = 36.
2. Prime sums: 2, 3, 5, 7, 11.
3. Ways: 2→1, 3→2, 5→4, 7→6, 11→2. Total = 15.
4. $P = 15/36 = 5/12$.
5. **Answer**: **5/12**.

### Solution 10
1. Total ways = $^{15}C_3 = 455$.
2. Favorable: $^4C_1 \times ^5C_1 \times ^6C_1 = 4 \times 5 \times 6 = 120$.
3. $P = 120/455 = 24/91$.
4. **Answer**: **24/91**.

---

## Additional Practice Questions (5 More)

### Q11
A coin is tossed 3 times. Find the probability of getting at least 2 heads.

### Q12
A bag contains 5 red and 7 blue balls. 3 balls are drawn without replacement. Find the probability that exactly 2 are red.

### Q13
The probability that it rains on a given day is 0.3. Find the probability that it rains on exactly 2 days out of 5.

### Q14
A box contains 5 defective and 15 non-defective items. 3 items are drawn. Find the probability that at most 1 is defective.

### Q15
A and B play a game where A wins with probability 0.6. They play 3 games. Find the probability that A wins at least 2 games.

---

## Quick Reference Card

| Concept | Formula |
|---------|---------|
| Basic | $P(E) = n(E)/n(S)$ |
| Complement | $P(E') = 1 - P(E)$ |
| Independent | $P(A \cap B) = P(A)P(B)$ |
| Conditional | $P(A|B) = P(A \cap B)/P(B)$ |
| Bayes | $P(A|B) = P(B|A)P(A)/P(B)$ |
| At least one | $1 - P(\text{none})$ |
| Odds in favor | $P(E)/P(E')$ |

---

## References

* [Aptitude](https://github.com/DKS-MANAGER/Aptitude) — Probability
* [Aptitude-For-Placements](https://github.com/DKS-MANAGER/Aptitude-For-Placements) — Practice problems
* [`aptitude-shortcuts.md`](../shortcuts/aptitude-shortcuts.md) — 55 speed math tricks
