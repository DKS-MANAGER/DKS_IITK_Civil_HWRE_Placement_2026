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

---

## Practice Problems

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

---

## Step-by-Step Solutions

### Solution 1
1. Let total work $= \text{LCM}(12, 18) = 36$ units.
2. Efficiency of A $= \frac{36}{12} = 3$ units/day. Efficiency of B $= \frac{36}{18} = 2$ units/day.
3. Let total days be $x$. A works $(x - 3)$ days, B works $x$ days.
4. Equation:
   $$3(x - 3) + 2x = 36 \implies 5x - 9 = 36 \implies 5x = 45 \implies x = 9$$
5. **Answer**: **9 days**.

### Solution 2
1. Efficiency ratio A : B $= 3 : 1$, so time ratio A : B $= 1 : 3$.
2. Let A take $t$ days and B take $3t$ days.
3. $3t - t = 60 \implies 2t = 60 \implies t = 30$. So A takes 30 days, B takes 90 days.
4. Total work $= 90$ units. Combined efficiency $= 3 + 1 = 4$.
5. Combined time:
   $$\frac{90}{4} = 22.5 \text{ days}$$
6. **Answer**: **$22\frac{1}{2}$ days**.

### Solution 3
1. Let tank capacity $= \text{LCM}(10, 15) = 30$ units.
2. Efficiency of A $= +3$/hour, B $= +2$/hour. Combined $= 5$/hour.
3. Time without leak $= \frac{30}{5} = 6$ hours. Actual time $= 6 + 2 = 8$ hours.
4. Let leak efficiency be $L$:
   $$8 \times (5 - L) = 30 \implies 5 - L = 3.75 \implies L = 1.25$$
5. Leak emptying time:
   $$\frac{30}{1.25} = 24 \text{ hours}$$
6. **Answer**: The leak empties the tank in **24 hours**.

### Solution 4
1. 1 man's 1-day work $= \frac{1}{12 \times 8} = \frac{1}{96}$.
2. 1 woman's 1-day work $= \frac{1}{16 \times 12} = \frac{1}{192}$.
3. Let total work $= 192$ units. 1 man $= 2$ units/day, 1 woman $= 1$ unit/day.
4. Combined efficiency of 8 men + 8 women:
   $$8(2) + 8(1) = 24 \text{ units/day}$$
5. Work done in 6 days $= 24 \times 6 = 144$ units. Remaining $= 192 - 144 = 48$ units.
6. To finish 48 units in 1 day, target efficiency $= 48$ units/day.
7. Additional efficiency needed $= 48 - 24 = 24$ units/day.
8. Since 1 man provides 2 units/day, men to add $= \frac{24}{2} = 12$.
9. **Answer**: **12 more men** are needed.

### Solution 5
1. Let rates of A, B, C be $a, b, c$.
2. $a + b = \frac{1}{12}$, $b + c = \frac{1}{15}$, $c + a = \frac{1}{20}$.
3. Add all three:
   $$2(a + b + c) = \frac{1}{12} + \frac{1}{15} + \frac{1}{20} = \frac{5 + 4 + 3}{60} = \frac{12}{60} = \frac{1}{5}$$
4. $a + b + c = \frac{1}{10}$.
5. Combined time $= \frac{1}{a+b+c} = 10$ days.
6. **Answer**: **10 days**.

---

## Sources

- `F:\2k26Placement\Aptitude\Time_Work.md`
- `F:\2k26Placement\Aptitude-For-Placements\Time and Work\`
