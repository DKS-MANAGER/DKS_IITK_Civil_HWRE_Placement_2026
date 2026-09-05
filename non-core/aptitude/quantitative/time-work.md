# Time & Work

## Concept Definitions

- **Work**: The complete task is treated as $1$ unit (or $100\%$).
- **Efficiency**: Amount of work done in one unit of time (day or hour).
  $$\text{Efficiency} = \frac{\text{Total Work}}{\text{Total Time}}$$
- **Efficiency vs. Time**: Efficiency is inversely proportional to time taken. A worker twice as efficient finishes in half the time.
- **Inlet Pipe**: Fills a tank (positive work).
- **Outlet Pipe / Leak**: Empties a tank (negative work).
- **Wages**: Distributed in the ratio of work done, which equals the ratio of efficiencies when durations are equal.

---

## Key Formulas & Shortcuts

### Two or Three Persons
- If $A$ takes $x$ days and $B$ takes $y$ days:
  $$\text{Time together} = \frac{x \times y}{x + y}$$
- If $A, B, C$ take $x, y, z$ days respectively:
  $$\text{Time together} = \frac{x \cdot y \cdot z}{xy + yz + zx}$$

### Man-Day-Hour Chain Rule
$$\frac{M_1 \times D_1 \times H_1 \times E_1}{W_1} = \frac{M_2 \times D_2 \times H_2 \times E_2}{W_2}$$
where $M$ = workers, $D$ = days, $H$ = hours per day, $E$ = efficiency, $W$ = work done.

### Pipes and Cisterns
- Inlet $A$ fills in $x$ hours, outlet $B$ empties in $y$ hours:
  $$\text{Net rate} = \frac{1}{x} - \frac{1}{y}$$
- Time to fill the tank:
  $$\text{Time} = \frac{x \times y}{y - x}$$

### LCM Method (Best for Time & Work)
1. Total Work = LCM of individual times
2. Efficiency = Total Work / Time
3. Combined Efficiency = Sum of individual efficiencies
4. Time = Total Work / Combined Efficiency

### Shortcut: A leaves before completion
If A and B work together, A leaves $n$ days before completion:
$$\text{Total time} = \frac{xy + n(x+y)}{x+y}$$

### Shortcut: Efficiency Ratio
If A is $k$ times as efficient as B, then time taken by A : time taken by B = $1 : k$

---

## Practice Problems (10 Problems)

### Problem 1
A can finish a work in 12 days and B in 18 days. They start together, but A leaves 3 days before completion. How many days does the work take?

### Problem 2
A is thrice as efficient as B and finishes a work in 60 days less than B. Find their combined time.

### Problem 3
Pipe A fills a tank in 10 hours and Pipe B in 15 hours. A leak makes filling take 2 extra hours. How long does the leak take to empty the full tank?

### Problem 4
12 men finish a work in 8 days. 16 women finish the same work in 12 days. 8 men and 8 women work for 6 days. How many more men are needed to finish the remaining work in 1 day?

### Problem 5
A and B together take 12 days. B and C together take 15 days. A and C together take 20 days. How long do A, B, and C take together?

### Problem 6
A can do a work in 10 days, B in 15 days. They work together for 4 days, then A leaves. How many more days will B take to finish?

### Problem 7
Pipe A fills a tank in 6 hours, Pipe B in 8 hours, and Pipe C empties it in 12 hours. If all three are opened together, how long to fill the tank?

### Problem 8
20 men can complete a work in 15 days. After 5 days, 5 men leave. In how many more days will the work be completed?

### Problem 9
A and B can do a work in 8 days, B and C in 12 days, C and A in 16 days. They all work together for 4 days, then A and B leave. How many more days will C take to finish?

### Problem 10
A pump can fill a tank in 2 hours. Due to a leak, it takes 2.5 hours. How long will the leak take to empty the full tank?

---

## Step-by-Step Solutions

### Solution 1
1. Total work $= \text{LCM}(12, 18) = 36$ units.
2. Efficiency of A $= \frac{36}{12} = 3$ units/day. Efficiency of B $= \frac{36}{18} = 2$ units/day.
3. Let total days be $x$. A works $(x - 3)$ days, B works $x$ days.
4. Equation: $3(x - 3) + 2x = 36 \implies 5x - 9 = 36 \implies 5x = 45 \implies x = 9$
5. **Answer**: **9 days**.

### Solution 2
1. Efficiency ratio A : B $= 3 : 1$, so time ratio A : B $= 1 : 3$.
2. Let A take $t$ days and B take $3t$ days.
3. $3t - t = 60 \implies 2t = 60 \implies t = 30$. So A takes 30 days, B takes 90 days.
4. Total work $= 90$ units. Combined efficiency $= 3 + 1 = 4$.
5. Combined time: $\frac{90}{4} = 22.5$ days.
6. **Answer**: **$22\frac{1}{2}$ days**.

### Solution 3
1. Let tank capacity $= \text{LCM}(10, 15) = 30$ units.
2. Efficiency of A $= +3$/hour, B $= +2$/hour. Combined $= 5$/hour.
3. Time without leak $= \frac{30}{5} = 6$ hours. Actual time $= 6 + 2 = 8$ hours.
4. Let leak efficiency be $L$:
   $$8 \times (5 - L) = 30 \implies 5 - L = 3.75 \implies L = 1.25$$
5. Leak emptying time: $\frac{30}{1.25} = 24$ hours.
6. **Answer**: **24 hours**.

### Solution 4
1. 1 man's 1-day work $= \frac{1}{12 \times 8} = \frac{1}{96}$.
2. 1 woman's 1-day work $= \frac{1}{16 \times 12} = \frac{1}{192}$.
3. Let total work $= 192$ units. 1 man $= 2$ units/day, 1 woman $= 1$ unit/day.
4. Combined efficiency of 8 men + 8 women: $8(2) + 8(1) = 24$ units/day.
5. Work done in 6 days $= 24 \times 6 = 144$ units. Remaining $= 192 - 144 = 48$ units.
6. To finish 48 units in 1 day, target efficiency $= 48$ units/day.
7. Additional efficiency needed $= 48 - 24 = 24$ units/day.
8. Since 1 man provides 2 units/day, men to add $= \frac{24}{2} = 12$.
9. **Answer**: **12 more men**.

### Solution 5
1. Let rates of A, B, C be $a, b, c$.
2. $a + b = \frac{1}{12}$, $b + c = \frac{1}{15}$, $c + a = \frac{1}{20}$.
3. Add all three: $2(a + b + c) = \frac{1}{12} + \frac{1}{15} + \frac{1}{20} = \frac{5 + 4 + 3}{60} = \frac{12}{60} = \frac{1}{5}$
4. $a + b + c = \frac{1}{10}$.
5. Combined time $= \frac{1}{a+b+c} = 10$ days.
6. **Answer**: **10 days**.

### Solution 6
1. Total work $= \text{LCM}(10, 15) = 30$ units.
2. A's efficiency $= 3$, B's efficiency $= 2$. Combined $= 5$.
3. Work in 4 days $= 4 \times 5 = 20$ units. Remaining $= 10$ units.
4. B's time $= 10/2 = 5$ days.
5. **Answer**: **5 days**.

### Solution 7
1. Total work $= \text{LCM}(6, 8, 12) = 24$ units.
2. A $= +4$/hr, B $= +3$/hr, C $= -2$/hr. Net $= 5$/hr.
3. Time $= 24/5 = 4.8$ hours $= 4$ hrs 48 min.
4. **Answer**: **4 hours 48 minutes**.

### Solution 8
1. Total work $= 20 \times 15 = 300$ man-days.
2. Work in 5 days $= 20 \times 5 = 100$ man-days. Remaining $= 200$ man-days.
3. Men remaining $= 15$. Days $= 200/15 = 13.33$ days.
4. **Answer**: **$13\frac{1}{3}$ days** (or 13 days 8 hours).

### Solution 9
1. $a+b = 1/8$, $b+c = 1/12$, $c+a = 1/16$.
2. $2(a+b+c) = 1/8 + 1/12 + 1/16 = (6+4+3)/48 = 13/48$.
3. $a+b+c = 13/96$. In 4 days: $4 \times 13/96 = 13/24$ done.
4. Remaining $= 11/24$. C's rate $= (a+b+c) - (a+b) = 13/96 - 1/8 = 1/96$.
5. C's time $= (11/24) / (1/96) = 44$ days.
6. **Answer**: **44 days**.

### Solution 10
1. Pump rate $= 1/2$ tank/hr. With leak $= 1/2.5 = 0.4$ tank/hr.
2. Leak rate $= 0.5 - 0.4 = 0.1$ tank/hr.
3. Time to empty $= 1/0.1 = 10$ hours.
4. **Answer**: **10 hours**.

---

## Additional Practice Questions (5 More)

### Q11
A can do a work in 20 days, B in 30 days. They work on alternate days starting with A. In how many days will the work be completed?

### Q12
Pipe A fills a tank in 5 hours, Pipe B in 10 hours, Pipe C empties in 15 hours. If A is opened for 1 hour, then B for 1 hour, then C for 1 hour, and this cycle repeats, how long to fill the tank?

### Q13
A contractor undertakes to complete a work in 40 days with 100 men. After 30 days, only 3/5 of the work is done. How many more men should be employed to finish on time?

### Q14
A and B together can do a work in 6 days. A alone can do it in 10 days. They start together but after 2 days B leaves. In how many days will A finish the remaining work?

### Q15
Three pipes A, B, C can fill a tank in 6, 8, 12 hours respectively. They are opened alternately for 1 hour each starting with A. How long to fill the tank?

---

## Quick Reference Card

| Concept | Formula |
|---------|---------|
| Two persons | $\frac{xy}{x+y}$ |
| Three persons | $\frac{xyz}{xy+yz+zx}$ |
| LCM method | Work = LCM, Eff = Work/Time |
| Pipes (fill) | $\frac{1}{x} + \frac{1}{y}$ |
| Pipes (fill+empty) | $\frac{1}{x} - \frac{1}{y}$ |
| Chain rule | $\frac{M_1D_1H_1}{W_1} = \frac{M_2D_2H_2}{W_2}$ |
| A leaves n days early | $\frac{xy+n(x+y)}{x+y}$ |
| Same SP, ±x% | Loss = $x^2/100$ |

---

## References

* [`aptitude-shortcuts.md`](../shortcuts/aptitude-shortcuts.md) — 55 speed math tricks
