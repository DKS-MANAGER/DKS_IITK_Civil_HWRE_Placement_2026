# Logical Reasoning Practice

Logical reasoning tests your ability to analyze patterns, deduce relationships, and solve structured puzzles. The main subtopics are:

- **Blood Relations**: Family tree puzzles, coded relationships.
- **Coding & Decoding**: Letter shifts, opposite letters, substitution coding.
- **Direction Sense**: Cardinal directions, shortest distance, shadows.
- **Seating Arrangement**: Linear, circular, square table layouts.
- **Puzzles & Scheduling**: Floor, box, month, and day scheduling.
- **Syllogism**: Venn diagrams, definite and possible conclusions.

---

## Key Concepts

### Blood Relations
- **Maternal**: From mother's side (e.g., Maternal Uncle = mother's brother).
- **Paternal**: From father's side (e.g., Paternal Aunt = father's sister).
- Solve narrative problems by working backwards from the last mentioned relation.

### Coding & Decoding
- **EJOTY Shortcut**: E=5, J=10, O=15, T=20, Y=25.
- **Reverse Rank**: Forward rank + Reverse rank = 27.
- **Opposite Letters**: A-Z, B-Y, C-X, etc. (sum to 27).

### Direction Sense
- **Right Turn**: $90^\circ$ clockwise. **Left Turn**: $90^\circ$ counter-clockwise.
- **Shortest Distance**: $\sqrt{a^2 + b^2}$ after two perpendicular moves.
- **Shadow Rule**: Morning shadows point West; evening shadows point East.

### Seating Arrangement
- **Linear**: Facing North means left is left; facing South means left is right.
- **Circular (Facing Center)**: Clockwise = left, Counter-clockwise = right.
- **Circular (Facing Outwards)**: Clockwise = right, Counter-clockwise = left.

### Puzzles & Scheduling
- Draw a skeleton table first (Floors, Months, Days).
- Place direct clues immediately.
- Branch into cases when a clue has two possibilities.

### Syllogism
- **A-Type**: All A are B.
- **E-Type**: No A is B.
- **I-Type**: Some A are B.
- **O-Type**: Some A are not B.
- A conclusion is definite only if it holds in **all** valid Venn diagrams.

---

## Practice Problems

### Problem 1 (Blood Relations)
Pointing to a photograph, Suresh said, "He is the son of the only son of my mother." How is Suresh related to the boy?

### Problem 2 (Coding & Decoding)
In a code, `COMPUTER` is written as `RFUVQNPC`. How will `MEDICINE` be written?

### Problem 3 (Direction Sense)
A man walks 10 km North, turns Right and walks 6 km, turns Left and walks 5 km, then turns Right and walks 2 km. What is the shortest distance from his starting point?

### Problem 4 (Seating Arrangement)
Eight friends A-H sit around a circular table facing the center. B sits third to the right of F. Only two people sit between B and G. A sits second to the left of D. Who sits third to the left of C if C sits third to the right of H?

### Problem 5 (Syllogism)
Statements: All pens are pencils. Some pencils are erasers.
Conclusions: 1. Some pens are erasers. 2. No pen is an eraser.
Decide which conclusions follow.

---

## Step-by-Step Solutions

### Solution 1
1. "The only son of my mother" = Suresh himself.
2. "He is the son of [Suresh]" = Suresh's son.
3. **Answer**: Suresh is the **Father**.

### Solution 2
1. Pattern: Reverse the word, then add $+1$ to all middle letters while keeping original first/last letters.
2. `MEDICINE` reversed inner letters: `E D I C I N` $\to$ `N I C I D E`.
3. Add $+1$: `N$\to$O`, `I$\to$J`, `C$\to$D`, `I$\to$J`, `D$\to$E`, `E$\to$F`.
4. Assemble: `E` + `OJDJEF` + `M` = `EOJDJEFM`.
5. **Answer**: `EOJDJEFM`.

### Solution 3
1. Trace path: $(0,0) \to (0,10) \to (6,10) \to (6,15) \to (8,15)$.
2. Horizontal $= 8$, vertical $= 15$.
3. Shortest distance:
   $$\sqrt{8^2 + 15^2} = \sqrt{289} = 17 \text{ km}$$
4. Direction: North-East.
5. **Answer**: **17 km** (North-East).

### Solution 4
1. Place F at 1. B is third to the right (counter-clockwise) $\to$ B at 4.
2. Two people between B (4) and G $\to$ G at 7.
3. A sits second to the left of D. D cannot be neighbor of B (4) or G (7), so D at 2, A at 8.
4. C sits third to the right of H. H at 3, C at 6.
5. Remaining seat 5 is E.
6. Arrangement: 1-F, 2-D, 3-H, 4-B, 5-E, 6-C, 7-G, 8-A.
7. Third to the left of C (6) facing center = clockwise: 6$\to$5$\to$4$\to$3. Seat 3 is H.
8. **Answer**: **H**.

### Solution 5
1. Basic diagram: Pen inside Pencil. Eraser intersects Pencil but does not touch Pen.
2. Alternative diagram: Eraser can expand to intersect Pen.
3. Conclusion 1 (Some pens are erasers): True in alternative, false in basic. Not definite.
4. Conclusion 2 (No pen is an eraser): True in basic, false in alternative. Not definite.
5. Both are individually doubtful, same subject/predicate, and form a complementary pair (Some + No).
6. **Answer**: **Either Conclusion 1 or Conclusion 2 follows**.

---

## References

* [Aptitude](https://github.com/DKS-MANAGER/Aptitude) — Logical reasoning topic sources
