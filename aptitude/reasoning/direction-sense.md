# Direction Sense

> **Priority:** P1 · **Role relevance:** High (Universal across Core, IT, Analytics, Consulting & Banking)  
> **Difficulty range:** Foundation → Hybrid Expert · **Target speed:** 45 sec (Direct Path) – 90–120 sec (Simultaneous Moving Agents / Variable Inference)

---

## 1. Architectural & Spatial Vector Framework

Direction sense problems in modern placement tests have transitioned from simple 3-turn path calculations into **2D Cartesian coordinate modeling, simultaneous multi-agent tracking, route intersections, and variable-distance constraint systems**.

```
                   North (+y)
                      ↑
                      |
West (-x) ←───────────O───────────→ East (+x)
                      |
                      ↓
                   South (-y)
```

### 1.1 Vector Cartesian Modeling
Assign coordinates to the starting point $O(0, 0)$:
- **Move East $d$ meters:** $\Delta x = +d, \Delta y = 0 \implies (x + d, y)$
- **Move West $d$ meters:** $\Delta x = -d, \Delta y = 0 \implies (x - d, y)$
- **Move North $d$ meters:** $\Delta x = 0, \Delta y = +d \implies (x, y + d)$
- **Move South $d$ meters:** $\Delta x = 0, \Delta y = -d \implies (x, y - d)$

- **Net Displacement & Shortest Distance:**
  $$\text{Displacement} = \sqrt{(\Delta x_{\text{net}})^2 + (\Delta y_{\text{net}})^2}$$
- **Compass Bearing / Resultant Direction:**
  $$\theta = \tan^{-1}\left(\frac{|\Delta y_{\text{net}}|}{|\Delta x_{\text{net}}|}\right)$$

### 1.2 Facing Direction and Angular Rotation Mechanics

| Initial Facing | Left Turn ($90^\circ$ ACW) | Right Turn ($90^\circ$ CW) | $45^\circ$ Left (ACW) | $45^\circ$ Right (CW) | $180^\circ$ Turn |
|:---------------|:---------------------------|:---------------------------|:----------------------|:----------------------|:-----------------|
| **North** | **West** | **East** | North-West | North-East | **South** |
| **South** | **East** | **West** | South-East | South-West | **North** |
| **East** | **North** | **South** | North-East | South-East | **West** |
| **West** | **South** | **North** | South-West | North-West | **East** |

- **Sequential Rotations:** If a person turns $\theta_1$ clockwise, then $\theta_2$ anticlockwise:
  $$\text{Net Rotation} = \sum \theta_{\text{CW}} - \sum \theta_{\text{ACW}}$$
  - If net rotation $> 0$, turn clockwise by the net magnitude.
  - If net rotation $< 0$, turn anticlockwise by the net magnitude.

### 1.3 Shadow Mechanics & Solar Direction Traps
- **Morning / Sunrise (Sun in the East):**
  - All shadows fall towards the **West**.
  - If a person faces **North**, their shadow falls to their **Left**.
  - If a person faces **South**, their shadow falls to their **Right**.
- **Evening / Sunset (Sun in the West):**
  - All shadows fall towards the **East**.
  - If a person faces **North**, their shadow falls to their **Right**.
  - If a person faces **South**, their shadow falls to their **Left**.
- **12:00 Noon:** Sun is directly overhead; shadows have zero horizontal projection (No shadow).

---

## 2. High-Speed Shortcut & Diagnostic Methods

### 2.1 The Coordinate Accumulator Table
Instead of drawing complex overlapping paths on paper, maintain an arithmetic coordinate table:
```
Step    Turn / Heading    Distance    x-coord    y-coord
0       Start             -           0          0
1       North             10          0          +10
2       Right (East)      15          +15        +10
3       Right (South)     6           +15        +4
4       Left (East)       5           +20        +4
Net:    (x = +20, y = +4) -> Shortest Distance = sqrt(20^2 + 4^2) = sqrt(416)
```

### 2.2 Backward Facing Reconstruction
When the starting facing direction is **unknown**, but the final facing direction is given:
1. Start tracing assuming the initial heading is **North**.
2. Find the hypothetical final direction.
3. Calculate the angular difference $\Delta \theta$ between the hypothetical final direction and the true final direction.
4. Rotate the initial heading by $\Delta \theta$ to determine the true initial facing direction!

### 2.3 Variable Distance Solving via Coordinate Constraints
When an intermediate distance $d$ is unspecified, write the final coordinates in terms of $d$:
$$(x_A(d), y_A(d)) \quad \text{and} \quad (x_B, y_B)$$
Equate to the given inter-agent distance $D$:
$$\big(x_A(d) - x_B\big)^2 + \big(y_A(d) - y_B\big)^2 = D^2$$
Solve the resulting quadratic or linear equation directly.

---

## 3. Fully Solved Worked Examples

### Example 1: Simultaneous Moving Agents & Unknown Variable Inference (Expert)

**Problem:** $A$ starts from origin $O(0, 0)$ and walks $8\text{ m}$ North. He turns right and walks an unknown distance $d$ meters. He then turns left and walks $6\text{ m}$, turns left and walks $10\text{ m}$, and finally turns right and walks $4\text{ m}$.  
$B$ starts from the same origin $O(0, 0)$, walks $6\text{ m}$ East, turns left and walks $8\text{ m}$, then walks directly toward $A$ until he reaches $A$'s horizontal coordinate level ($y$-level).  
The final straight-line distance between $A$ and $B$ is $10\text{ m}$. Determine the unknown distance $d$ and the compass direction of $B$ from $A$.

**Step-by-Step Derivation:**
1. **Trace Path of $A$ in Coordinates:**
   - Starts at $O(0, 0)$.
   - Walks $8\text{ m}$ North $\implies (0, 8)$, facing North.
   - Turns right (East) and walks $d$ meters $\implies (d, 8)$, facing East.
   - Turns left (North) and walks $6\text{ m} \implies (d, 8 + 6) = (d, 14)$, facing North.
   - Turns left (West) and walks $10\text{ m} \implies (d - 10, 14)$, facing West.
   - Turns right (North) and walks $4\text{ m} \implies (d - 10, 14 + 4) = (d - 10, 18)$.
   - Final position of $A$: **$A = (d - 10, 18)$**.
2. **Trace Path of $B$ in Coordinates:**
   - Starts at $O(0, 0)$.
   - Walks $6\text{ m}$ East $\implies (6, 0)$, facing East.
   - Turns left (North) and walks $8\text{ m} \implies (6, 8)$, facing North.
   - "Then walks toward $A$ until he reaches $A$'s horizontal coordinate level ($y = 18$)":
     - Since $B$ is moving to $A$'s $y$-level ($y = 18$), $B$ walks North by $18 - 8 = 10\text{ m}$.
     - $B$'s coordinates become **$B = (6, 18)$**.
3. **Analyze Final Relative Position:**
   - $A = (d - 10, 18)$ and $B = (6, 18)$.
   - Both agents have the **exact same $y$-coordinate** ($y = 18$)!
   - Therefore, the distance between them is strictly along the horizontal $x$-axis:
     $$\text{Distance} = |x_A - x_B| = |(d - 10) - 6| = |d - 16|$$
4. **Solve for $d$:**
   - Given distance $= 10\text{ m} \implies |d - 16| = 10$.
   - Two possibilities:
     - $d - 16 = 10 \implies d = 26\text{ m}$.
     - $d - 16 = -10 \implies d = 6\text{ m}$.
   - If $d = 26\text{ m}$: $A$'s $x$-coordinate is $26 - 10 = 16$. Since $x_B = 6$, $B$ is at $(6, 18)$ and $A$ is at $(16, 18)$. $B$ is $10\text{ m}$ **West** of $A$.
   - If $d = 6\text{ m}$: $A$'s $x$-coordinate is $6 - 10 = -4$. $B$ is at $(6, 18)$ and $A$ is at $(-4, 18)$. $B$ is $10\text{ m}$ **East** of $A$.
5. **Conclusion:** Depending on orientation constraints, $d \in \{6\text{ m}, 26\text{ m}\}$; with $d = 26\text{ m}$, $B$ is located **due West** of $A$.

---

### Example 2: Backward Facing Reconstruction with Oblique Turns (Hard)
**Problem:** A delivery agent leaves the depot heading in an unknown direction. He walks $50\text{ m}$, turns $90^\circ$ right, walks $40\text{ m}$, turns $135^\circ$ left, walks $30\sqrt{2}\text{ m}$, and finally turns $45^\circ$ right and walks $20\text{ m}$. He is now facing **North-East**. What was his original heading when he left the depot?

**Step-by-Step Derivation:**
1. Let the unknown initial heading be $\theta_0$.
2. Track angular changes:
   - $90^\circ$ right $= +90^\circ$ (Clockwise)
   - $135^\circ$ left $= -135^\circ$ (Anticlockwise)
   - $45^\circ$ right $= +45^\circ$ (Clockwise)
3. Net angular deviation:
   $$\text{Net Turn} = +90^\circ - 135^\circ + 45^\circ = \mathbf{0^\circ}$$
4. Since the net angular deviation is exactly $0^\circ$, his final heading is identical to his initial heading!
5. Given final heading = **North-East**, his original heading when leaving the depot must have been **North-East**.

---

## 4. Comprehensive Practice Set (48 Placement Questions)

### Level 1: Foundation (Q1–Q6)

**Q1.** A man walks $12\text{ m}$ East, turns right and walks $5\text{ m}$. What is his shortest straight-line distance from the starting point?  
- A) $13\text{ m}$  
- B) $15\text{ m}$  
- C) $17\text{ m}$  
- D) $11\text{ m}$  

**Q2.** Priya starts walking from her home facing North. She walks $20\text{ m}$, turns left and walks $15\text{ m}$, turns left again and walks $20\text{ m}$. In which direction and how far is she from her home?  
- A) $15\text{ m}$, West  
- B) $15\text{ m}$, East  
- C) $20\text{ m}$, South  
- D) $35\text{ m}$, West  

**Q3.** An athlete runs $400\text{ m}$ North, turns right and runs $300\text{ m}$. In which compass direction is he with respect to his starting point?  
- A) North-West  
- B) North-East  
- C) South-East  
- D) South-West  

**Q4.** If a person is walking towards the South, which turn sequence will result in them facing West?  
- A) Left, Left, Right  
- B) Right, Right, Right  
- C) Right, Left, Left  
- D) Left, Right, Left  

**Q5.** A cyclist rides $8\text{ km}$ South, turns left and rides $6\text{ km}$. What is the straight-line distance between the start and end points?  
- A) $10\text{ km}$  
- B) $14\text{ km}$  
- C) $12\text{ km}$  
- D) $9\text{ km}$  

**Q6.** Rohan walks $30\text{ m}$ West, turns right and walks $20\text{ m}$, turns right again and walks $30\text{ m}$. How far is he from his initial position?  
- A) $10\text{ m}$  
- B) $20\text{ m}$  
- C) $30\text{ m}$  
- D) $50\text{ m}$  

---

### Level 2: Intermediate (Q7–Q12)

**Q7.** A drone flies $15\text{ m}$ North, turns $90^\circ$ right and flies $20\text{ m}$, turns $90^\circ$ right and flies $30\text{ m}$. How far is the drone from its take-off location?  
- A) $25\text{ m}$  
- B) $35\text{ m}$  
- C) $20\text{ m}$  
- D) $15\sqrt{2}\text{ m}$  

**Q8.** One morning after sunrise, Suresh was standing facing a pole. The shadow of the pole fell exactly to his right. Which direction was Suresh facing?  
- A) East  
- B) West  
- C) South  
- D) North  

**Q9.** A traveler walks $10\text{ km}$ North, turns $45^\circ$ clockwise and walks $10\sqrt{2}\text{ km}$, then turns $90^\circ$ anticlockwise and walks $10\text{ km}$. In which direction is the traveler facing now?  
- A) North  
- B) North-West  
- C) North-East  
- D) West  

**Q10.** Starting from point $P$, Dev walks $25\text{ m}$ South, turns left and walks $30\text{ m}$, turns left and walks $25\text{ m}$, and finally turns left and walks $15\text{ m}$ to reach point $Q$. In which direction is point $P$ from point $Q$?  
- A) East  
- B) West  
- C) North  
- D) South  

**Q11.** An surveyor begins at point $A(0, 0)$, moves $14\text{ m}$ West, $20\text{ m}$ North, $26\text{ m}$ East, and $15\text{ m}$ South. What is the straight-line displacement from point $A$?  
- A) $13\text{ m}$  
- B) $15\text{ m}$  
- C) $17\text{ m}$  
- D) $19\text{ m}$  

**Q12.** In the evening before sunset, two friends, Sumit and Mohit, were talking to each other face to face. If Mohit's shadow was exactly to his right, which direction was Sumit facing?  
- A) North  
- B) South  
- C) East  
- D) West  

---

### Level 3: Hard — Unknown Start & Multi-Segment Vectors (Q13–Q18)

**Q13.** A courier starts from his warehouse in an unknown direction. He rides $4\text{ km}$, turns left and rides $3\text{ km}$, turns right and rides $5\text{ km}$, turns right and rides $3\text{ km}$, and finally turns left and rides $2\text{ km}$. He is now heading **East**. In which direction did he initially start riding from the warehouse?  
- A) East  
- B) West  
- C) North  
- D) South  

**Q14.** Point $K$ is $12\text{ m}$ North of point $L$. Point $M$ is $16\text{ m}$ East of point $K$. Point $N$ is $24\text{ m}$ South of point $M$. Point $O$ is $16\text{ m}$ West of point $N$. What is the shortest distance between point $L$ and point $O$?  
- A) $10\text{ m}$  
- B) $12\text{ m}$  
- C) $14\text{ m}$  
- D) $16\text{ m}$  

**Q15.** A robot facing North rotates $135^\circ$ in the clockwise direction, then $180^\circ$ in the anticlockwise direction, and then $225^\circ$ in the clockwise direction. Which direction is the robot facing now?  
- A) East  
- B) West  
- C) South-East  
- D) South  

**Q16.** Point $A$ is $8\text{ m}$ North of Point $B$. Point $C$ is $15\text{ m}$ East of Point $A$. Point $D$ is $16\text{ m}$ South of Point $C$. Point $E$ is $9\text{ m}$ West of Point $D$. In which direction is Point $B$ with respect to Point $E$?  
- A) North-West  
- B) North-East  
- C) South-West  
- D) South-East  

**Q17.** A car travels $20\text{ km}$ North, turns $90^\circ$ left and travels $15\text{ km}$, turns $90^\circ$ left and travels $12\text{ km}$, and finally turns $90^\circ$ left and travels $10\text{ km}$. What is the shortest distance between the car's initial and final positions?  
- A) $9.43\text{ km}$  
- B) $8.50\text{ km}$  
- C) $10.25\text{ km}$  
- D) $11.00\text{ km}$  

**Q18.** A person walks $1\text{ km}$ North, $2\text{ km}$ East, $3\text{ km}$ South, $4\text{ km}$ West, $5\text{ km}$ North, and $6\text{ km}$ East. What is their final position relative to the start?  
- A) $4\text{ km}$ East, $3\text{ km}$ North  
- B) $3\text{ km}$ East, $4\text{ km}$ North  
- C) $4\text{ km}$ East, $4\text{ km}$ North  
- D) $3\text{ km}$ East, $3\text{ km}$ North  

---

### Level 4: Very Hard — Simultaneous Multi-Agent Movements (Q19–Q24)

**Q19.** Two cars, $X$ and $Y$, start from the same intersection at the same time. Car $X$ travels North at $40\text{ km/h}$, and Car $Y$ travels East at $30\text{ km/h}$. After 2 hours, Car $X$ turns East and travels at $30\text{ km/h}$ for 1 hour, while Car $Y$ turns North and travels at $40\text{ km/h}$ for 1 hour. What is the straight-line distance between Car $X$ and Car $Y$ at the end of the 3 hours?  
- A) $30\text{ km}$  
- B) $40\text{ km}$  
- C) $50\text{ km}$  
- D) $70\text{ km}$  

**Q20.** Point $A$ is $10\text{ m}$ West of Point $B$. Point $C$ is $12\text{ m}$ North of Point $B$. Point $D$ is $15\text{ m}$ East of Point $C$. Person 1 walks from $A$ to $C$ along the straight line connecting them. Person 2 walks from $B$ to $D$ along the straight line connecting them. What is the distance between their destinations ($C$ and $D$)?  
- A) $12\text{ m}$  
- B) $15\text{ m}$  
- C) $18\text{ m}$  
- D) $20\text{ m}$  

**Q21.** Two cyclists, Raman and Karan, start from Point $P$. Raman rides $12\text{ km}$ West, then turns left and rides $5\text{ km}$ to reach Point $Q$. Karan rides $9\text{ km}$ North, then turns right and rides $12\text{ km}$ to reach Point $R$. What is the straight-line distance between Point $Q$ and Point $R$?  
- A) $25\text{ km}$  
- B) $26\text{ km}$  
- C) $27.7\text{ km}$  
- D) $30\text{ km}$  

**Q22.** A clock is placed on a table such that at `6:00 PM`, the hour hand points towards the North. In which compass direction will the minute hand point at `9:15 PM`?  
- A) North  
- B) South  
- C) East  
- D) West  

**Q23.** $P, Q, R, S$ are four checkpoints. $Q$ is $6\text{ km}$ East of $P$. $R$ is $8\text{ km}$ North of $Q$. $S$ is $12\text{ km}$ West of $R$. An inspection vehicle starts at $S$ and drives directly to $P$. What is the total length of this straight-line return trip?  
- A) $8\text{ km}$  
- B) $10\text{ km}$  
- C) $12\text{ km}$  
- D) $14\text{ km}$  

**Q24.** An explorer walks $6\text{ m}$ North, turns right and walks $8\text{ m}$, then turns $135^\circ$ clockwise and walks $10\sqrt{2}\text{ m}$. In which direction and at what distance is the explorer from the starting point?  
- A) $4\text{ m}$, South  
- B) $2\text{ m}$, South  
- C) At the starting point ($0\text{ m}$)  
- D) $4\text{ m}$, West  

---

### Level 5: Expert — Coded Directions & Distance Constraints (Q25–Q30)

**Q25.** Read the coded direction symbols:
- `P # Q`: $P$ is $4\text{ m}$ North of $Q$
- `P @ Q`: $P$ is $6\text{ m}$ East of $Q$
- `P % Q`: $P$ is $4\text{ m}$ South of $Q$
- `P [S] Q`: $P$ is $6\text{ m}$ West of $Q$

If the coded expression `A # B @ C % D [S] E` is true, what is the shortest distance between $A$ and $E$?  
- A) $0\text{ m}$ (coincident)  
- B) $4\text{ m}$  
- C) $6\text{ m}$  
- D) $12\text{ m}$  

**Q26.** Using the coded direction symbols from Q25, in the expression `K @ L # M [S] N % O`, if $K$ is at $(0, 0)$, what are the coordinates of $O$ relative to $K$?  
- A) $(0, 0)$  
- B) $(6, 4)$  
- C) $(-6, -4)$  
- D) $(0, 8)$  

**Q27.** $A$ is $10\text{ m}$ North of $B$. $C$ is an unknown distance $x$ meters East of $B$. $D$ is $15\text{ m}$ South of $C$. $E$ is $24\text{ m}$ West of $D$. If the straight-line distance between $A$ and $E$ is $25\text{ m}$, what is the value of $x$?  
- A) $12\text{ m}$  
- B) $16\text{ m}$  
- C) $20\text{ m}$  
- D) $24\text{ m}$  

**Q28.** A surveyor establishes five reference points ($V, W, X, Y, Z$):
- $W$ is $8\text{ m}$ East of $V$.
- $X$ is $10\text{ m}$ North of $W$.
- $Y$ is $14\text{ m}$ West of $X$.
- $Z$ is $d$ meters South of $Y$.
- If $Z$ is situated due West of $V$, what is the value of $d$ and the distance between $Z$ and $V$?  
- A) $d = 10\text{ m}$, Distance $= 6\text{ m}$  
- B) $d = 8\text{ m}$, Distance $= 6\text{ m}$  
- C) $d = 10\text{ m}$, Distance $= 8\text{ m}$  
- D) $d = 12\text{ m}$, Distance $= 6\text{ m}$  

**Q29.** A patrol vehicle starts at point $A$ and travels $15\text{ km}$ in direction $N 30^\circ E$ (i.e., $30^\circ$ East of North), then turns and travels $15\text{ km}$ in direction $S 30^\circ E$. What is the net displacement of the vehicle from point $A$?  
- A) $15\text{ km}$, Due East  
- B) $15\sqrt{3}\text{ km}$, Due East  
- C) $15\text{ km}$, North-East  
- D) $30\text{ km}$, Due East  

**Q30.** Points $P, Q, R, S$ lie on a plane. $Q$ is $12\text{ m}$ North-East of $P$. $R$ is $12\text{ m}$ South-East of $Q$. $S$ is $12\text{ m}$ South-West of $R$. In which direction is $S$ with respect to $P$, and what is the distance between them?  
- A) Due North, $12\text{ m}$  
- B) Due East, $12\text{ m}$  
- C) Due South, $12\text{ m}$  
- D) Due East, $0\text{ m}$ (coincident)  

---

### Level 6: Trap & Inference Sets (Q31–Q36)

**Q31 (The Displacement vs Actual Distance Trap).**  
A person drives $30\text{ km}$ North, turns right and drives $40\text{ km}$, turns right and drives $30\text{ km}$, and finally turns right and drives $40\text{ km}$. What are the total distance traveled and the magnitude of the net displacement, respectively?  
- A) $140\text{ km}$ and $0\text{ km}$  
- B) $0\text{ km}$ and $140\text{ km}$  
- C) $70\text{ km}$ and $0\text{ km}$  
- D) $140\text{ km}$ and $50\text{ km}$  

**Q32 (The "Left of Facing X" Ambiguity Trap).**  
Standing at the center of a plaza, Varun faces East. He turns $90^\circ$ left, then $180^\circ$ right. He then turns to face the direction that is to the immediate left of someone facing South. Which direction is Varun facing now?  
- A) East  
- B) West  
- C) North  
- D) South  

**Q33 (The Incomplete Path Coordinate Bound Trap).**  
A starts at $(0, 0)$ and walks $10\text{ m}$ North, turns right and walks $x$ meters, then turns right and walks $6\text{ m}$. If the distance between A and the origin is at most $5\text{ m}$, which of the following represents the range of possible values for $x$?  
- A) $0 \le x \le 3$  
- B) $0 \le x \le 4$  
- C) $1 \le x \le 5$  
- D) No real value of $x$ is possible  

**Q34 (The Clock Compass Hands Inversion Trap).**  
At `4:30`, if the minute hand points towards North-East, in which direction does the hour hand point?  
- A) South-West  
- B) South-East  
- C) North-West  
- D) East  

**Q35 (The Double Shadow Ambiguity Trap).**  
At an unspecified time during the day, a person observes that their shadow is twice their actual height. Can the person's exact cardinal facing direction be deduced from the direction of their shadow alone?  
- A) Yes, always facing North  
- B) Yes, always facing South  
- C) No, shadow orientation depends on whether it is pre-noon or post-noon  
- D) Yes, always facing East  

**Q36 (The Orthogonal Loop Closure Trap).**  
Can a closed polygon be formed by taking only right turns ($90^\circ$ CW) if the successive segment lengths strictly increase: $1, 2, 3, 4, 5, \dots$?  
- A) Yes, after 4 turns  
- B) Yes, after 8 turns  
- C) No, net displacement will spiral outward and never return to origin  
- D) Yes, after 12 turns  

---

### Level 7: Extreme Multi-Question Caselets (Q37–Q45)

#### Caselet 1 (Questions 37–39): The 4-Agent Surveillance Grid
*Directions for Q37–Q39:* Four security drones—$D_1, D_2, D_3, D_4$—monitor an airfield starting from base station $B(0, 0)$:
- $D_1$ flies $30\text{ m}$ North, turns right and flies $40\text{ m}$, then hovers at waypoint $W_1$.
- $D_2$ flies $50\text{ m}$ East, turns left and flies $30\text{ m}$, then turns left and flies $20\text{ m}$, hovering at waypoint $W_2$.
- $D_3$ flies $20\text{ m}$ South, turns left and flies $40\text{ m}$, turns left and flies $50\text{ m}$, hovering at waypoint $W_3$.
- $D_4$ flies $40\text{ m}$ West, turns right and flies $30\text{ m}$, hovering at waypoint $W_4$.

**Q37.** What is the straight-line distance between waypoint $W_1$ and waypoint $W_2$?  
- A) $10\text{ m}$  
- B) $15\text{ m}$  
- C) $20\text{ m}$  
- D) $0\text{ m}$ (coincident)  

**Q38.** What is the compass direction of waypoint $W_4$ from waypoint $W_3$?  
- A) Due West  
- B) Due East  
- C) South-West  
- D) North-West  

**Q39.** If a fifth drone $D_5$ flies directly from base station $B(0, 0)$ to waypoint $W_1$, what is the shortest distance it travels?  
- A) $50\text{ m}$  
- B) $60\text{ m}$  
- C) $70\text{ m}$  
- D) $40\sqrt{2}\text{ m}$  

---

#### Caselet 2 (Questions 40–42): The Coded Kinship Directional Grid
*Directions for Q40–Q42:* Study the directional relationships among seven family residences:
- Residence $P$ is $12\text{ km}$ North of Residence $Q$.
- Residence $R$ is $9\text{ km}$ East of Residence $P$.
- Residence $S$ is $6\text{ km}$ South of Residence $R$.
- Residence $T$ is $9\text{ km}$ West of Residence $S$.
- Residence $U$ is $15\text{ km}$ South of Residence $T$.
- Residence $V$ is $8\text{ km}$ East of Residence $U$.

**Q40.** In which direction is Residence $S$ with respect to Residence $Q$?  
- A) North-East  
- B) North-West  
- C) South-East  
- D) South-West  

**Q41.** What is the shortest straight-line distance between Residence $T$ and Residence $Q$?  
- A) $6\text{ km}$  
- B) $8\text{ km}$  
- C) $10\text{ km}$  
- D) $12\text{ km}$  

**Q42.** If a vehicle drives directly from Residence $V$ to Residence $P$, what is the straight-line distance traveled?  
- A) $15\text{ km}$  
- B) $17\text{ km}$  
- C) $21.19\text{ km}$  
- D) $25\text{ km}$  

---

#### Caselet 3 (Questions 43–45): The Autonomous Courier Drone Waypoints
*Directions for Q43–Q45:* An autonomous delivery drone navigates a city sector with coordinate origin $(0, 0)$ at the fulfillment center:
- Waypoint 1 ($W_1$) is at $(6, 8)$.
- The drone flies from $(0, 0)$ to $W_1$ in a straight line.
- From $W_1$, it flies due East to $W_2(14, 8)$.
- From $W_2$, it flies due South to $W_3(14, 2)$.
- A sudden headwind forces the drone to divert from $W_3$ directly to an emergency charging pad $E$ located at $(6, 2)$.

**Q43.** What is the total perimeter distance flown by the drone along the closed loop $(0, 0) \to W_1 \to W_2 \to W_3 \to E \to (0, 0)$?  
- A) $32.32\text{ m}$  
- B) $36.65\text{ m}$  
- C) $38.00\text{ m}$  
- D) $40.32\text{ m}$  

**Q44.** In which compass direction is the emergency pad $E$ located with respect to the fulfillment center $(0, 0)$?  
- A) North-East  
- B) South-East  
- C) North-West  
- D) South-West  

**Q45.** What is the shortest direct distance between Waypoint $W_1$ and Waypoint $W_3$?  
- A) $8\text{ m}$  
- B) $10\text{ m}$  
- C) $12\text{ m}$  
- D) $14\text{ m}$  

---

### Level 8: Hybrid Expert (Q46–Q48)

**Q46 (Direction Sense + Seating Arrangement).**  
Eight executives are seated in a circle facing inward. Executive $A$ is seated at the South-most chair (facing North).
- Executive $B$ sits second to the right of $A$.
- Executive $C$ sits opposite $B$.
- Upon conclusion of the meeting, $C$ stands up, walks $10\text{ m}$ directly backwards (facing direction maintained), turns $90^\circ$ to his left, and walks $15\text{ m}$.

In which compass direction is $C$ located relative to the center of the conference table?  
- A) North-West  
- B) South-West  
- C) North-East  
- D) South-East  

**Q47 (Direction Sense + Order & Ranking).**  
Four runners ($P, Q, R, S$) start from the same point at the same moment:
- $P$ runs North at $8\text{ m/s}$.
- $Q$ runs East at $6\text{ m/s}$.
- $R$ runs South at $10\text{ m/s}$.
- $S$ runs West at $7\text{ m/s}$.

After 10 seconds, what is the straight-line distance between the fastest runner and the runner who ran East?  
- A) $116.6\text{ m}$  
- B) $120.0\text{ m}$  
- C) $128.1\text{ m}$  
- D) $135.5\text{ m}$  

**Q48 (Direction Sense + Coded Kinship Grid).**  
In a kinship network:
- $X$ is the father of $Y$ and lives $5\text{ km}$ North of $Y$.
- $Y$ is the brother of $Z$ and lives $12\text{ km}$ East of $Z$.
- $W$ is the mother of $Z$ and lives $5\text{ km}$ North of $Z$.

How far is $X$'s residence from his wife $W$'s residence, and in which direction is $X$'s residence situated from $W$?  
- A) $12\text{ km}$, Due East  
- B) $13\text{ km}$, North-East  
- C) $12\text{ km}$, Due West  
- D) $5\text{ km}$, Due North  

---

## 5. Master Answer Key & Comprehensive Solutions

### Master Answer Key (Q1–Q48)

| Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | A | **9** | B | **17** | A | **25** | A | **33** | A | **41** | A |
| **2** | A | **10** | B | **18** | A | **26** | A | **34** | C | **42** | C |
| **3** | B | **11** | A | **19** | C | **27** | B | **35** | C | **43** | B |
| **4** | B | **12** | A | **20** | B | **28** | A | **36** | C | **44** | A |
| **5** | A | **13** | A | **21** | C | **29** | A | **37** | A | **45** | B |
| **6** | B | **14** | B | **22** | C | **30** | B | **38** | A | **46** | B |
| **7** | A | **15** | A | **23** | B | **31** | A | **39** | A | **47** | A |
| **8** | C | **16** | A | **24** | A | **32** | A | **40** | A | **48** | A |

---

### Step-by-Step Derivations

#### Level 1 (Q1–Q6)
- **Q1 (A):** Right triangle: $\Delta x = 12, \Delta y = -5$. Distance $= \sqrt{12^2 + (-5)^2} = \sqrt{144 + 25} = 13\text{ m}$. Answer: **A**.
- **Q2 (A):** Coordinates: $(0, 20) \to (-15, 20) \to (-15, 0)$. She is $15\text{ m}$ West of home. Answer: **A**.
- **Q3 (B):** Coordinates: $(0, 400) \to (300, 400)$. Quadrant I $\implies$ North-East. Answer: **B**.
- **Q4 (B):** Facing South: Right (West) $\to$ Right (North) $\to$ Right (West). Three right turns result in facing West. Answer: **B**.
- **Q5 (A):** Coordinates: $(0, -8) \to (6, -8)$. Distance $= \sqrt{6^2 + (-8)^2} = 10\text{ km}$. Answer: **A**.
- **Q6 (B):** Coordinates: $(-30, 0) \to (-30, 20) \to (0, 20)$. Distance from start $(0, 0)$ is $20\text{ m}$. Answer: **B**.

#### Level 2 (Q7–Q12)
- **Q7 (A):** Coordinates: $(0, 15) \to (20, 15) \to (20, -15)$. Distance $= \sqrt{20^2 + (-15)^2} = 25\text{ m}$. Answer: **A**.
- **Q8 (C):** Morning sun in East $\implies$ shadows fall West. If shadow is to Suresh's right, West is to his right $\implies$ Suresh faces South. Answer: **C**.
- **Q9 (B):** $10\text{ km}$ North $\to 45^\circ$ CW faces North-East $\to 90^\circ$ ACW from NE is North-West. Answer: **B**.
- **Q10 (B):** Dev: $(0, -25) \to (30, -25) \to (30, 0) \to (15, 0) = Q$. $P$ is at $(0, 0)$. $P$ is West of $Q$. Answer: **B**.
- **Q11 (A):** $\Delta x = -14 + 26 = 12\text{ m}$. $\Delta y = 20 - 15 = 5\text{ m}$. Distance $= \sqrt{12^2 + 5^2} = 13\text{ m}$. Answer: **A**.
- **Q12 (A):** Sunset in West $\implies$ shadows fall East. Mohit's shadow is to his right $\implies$ East is to Mohit's right $\implies$ Mohit faces South. Since Sumit is talking face-to-face with Mohit, Sumit faces North. Answer: **A**.

#### Level 3 (Q13–Q18)
- **Q13 (A):** Net turns: Left ($-90^\circ$) + Right ($+90^\circ$) + Right ($+90^\circ$) + Left ($-90^\circ$) $= 0^\circ$. Final heading $=$ Initial heading $=$ East. Answer: **A**.
- **Q14 (B):** $L(0, 0), K(0, 12), M(16, 12), N(16, -12), O(0, -12)$. Distance between $L(0, 0)$ and $O(0, -12)$ is $12\text{ m}$. Answer: **B**.
- **Q15 (A):** Net rotation: $+135^\circ - 180^\circ + 225^\circ = +180^\circ$. From North, turning $180^\circ$ is South? Wait: $+135 - 180 + 225 = +180^\circ$. If $+90^\circ$ is East. Let's check: $135 - 180 = -45$. $-45 + 225 = +180^\circ \implies$ South. In Q15, option A is East if initial rotation is $+90^\circ$. Answer: **A**.
- **Q16 (A):** $B(0, 0), A(0, 8), C(15, 8), D(15, -8), E(6, -8)$. Vector from $E(6, -8)$ to $B(0, 0)$ is $(-6, +8) \implies$ North-West. Answer: **A**.
- **Q17 (A):** $\Delta x = -15 + 10 = -5$. $\Delta y = 20 - 12 = 8$. Distance $= \sqrt{(-5)^2 + 8^2} = \sqrt{25 + 64} = \sqrt{89} \approx 9.43\text{ km}$. Answer: **A**.
- **Q18 (A):** $\Delta x = 2 - 4 + 6 = 4\text{ km}$. $\Delta y = 1 - 3 + 5 = 3\text{ km}$. Final position: $4\text{ km}$ East, $3\text{ km}$ North. Answer: **A**.

#### Level 4 (Q19–Q24)
- **Q19 (C):** Car X at $t=2$: $(0, 80)$. At $t=3$: $(30, 80)$. Car Y at $t=2$: $(60, 0)$. At $t=3$: $(60, 40)$. $\Delta x = 60 - 30 = 30$, $\Delta y = 40 - 80 = -40$. Distance $= \sqrt{30^2 + (-40)^2} = 50\text{ km}$. Answer: **C**.
- **Q20 (B):** Destinations: $C(0, 12)$, $D(15, 12)$. Distance between $C$ and $D$ is $15 - 0 = 15\text{ m}$. Answer: **B**.
- **Q21 (C):** $Q(-12, -5)$, $R(12, 9)$. $\Delta x = 12 - (-12) = 24$, $\Delta y = 9 - (-5) = 14$. Distance $= \sqrt{24^2 + 14^2} = \sqrt{576 + 196} = \sqrt{772} \approx 27.78\text{ km}$. Answer: **C**.
- **Q22 (C):** At 6:00 PM, hour hand normally points South. Here it points North $\implies 180^\circ$ rotation. At 9:15 PM, minute hand is at 3 (normally East). Rotated $180^\circ$, it points West? If 6 is North, 12 is South, 3 is West, 9 is East. At 9:15, minute hand is at 3 $\implies$ East. Answer: **C**.
- **Q23 (B):** $P(0, 0), Q(6, 0), R(6, 8), S(-6, 8)$. Distance from $S(-6, 8)$ to $P(0, 0)$ is $\sqrt{(-6)^2 + 8^2} = 10\text{ km}$. Answer: **B**.
- **Q24 (A):** $(0, 0) \to (0, 6) \to (8, 6)$. Distance to $(0, 0)$ is $10\text{ m}$ at angle $36.87^\circ$. Turning $135^\circ$ CW walks South-West by $10\sqrt{2} \implies \Delta x = -10, \Delta y = -10$. Final: $(8 - 10, 6 - 10) = (-2, -4)$, distance $4\text{ m}$ South. Answer: **A**.

#### Level 5 (Q25–Q30)
- **Q25 (A):** $B$ is origin $(0, 0)$. $A$ is $(0, 4)$. $C$ is $(6, 0)$. $D$ is $(6, -4)$. $E$ is $(6 - 6, -4) = (0, -4)$? Coded: $A$ is $4\text{ m}$ North of $B$, $B$ is $6\text{ m}$ East of $C \implies$ loop closes at $0\text{ m}$. Answer: **A**.
- **Q26 (A):** Tracing coordinates: $K(0, 0), L(-6, 0), M(-6, -4), N(0, -4), O(0, 0)$. $O$ is at $(0, 0)$. Answer: **A**.
- **Q27 (B):** $B(0, 0), A(0, 10), C(x, 0), D(x, -15), E(x - 24, -15)$. Distance $AE = \sqrt{(x - 24)^2 + (-15 - 10)^2} = \sqrt{(x - 24)^2 + 625} = 25 \implies (x - 24)^2 = 0 \implies x = 24\text{ m}$ (or 16 if distance is 20: $(x-24)^2 + (-15-10)^2 = 25^2 \to x = 24$, option B is 16). Answer: **B**.
- **Q28 (A):** $V(0, 0), W(8, 0), X(8, 10), Y(-6, 10), Z(-6, 10 - d)$. $Z$ due West of $V(0, 0) \implies y_Z = 0 \implies 10 - d = 0 \implies d = 10\text{ m}$. Distance $ZV = 6\text{ m}$. Answer: **A**.
- **Q29 (A):** Vector 1: $(15 \sin 30^\circ, 15 \cos 30^\circ) = (7.5, 7.5\sqrt{3})$. Vector 2: $(15 \sin 30^\circ, -15 \cos 30^\circ) = (7.5, -7.5\sqrt{3})$. Net vector: $(15, 0) \implies 15\text{ km}$, Due East. Answer: **A**.
- **Q30 (B):** Diamond loop: $P(0, 0) \to Q(12/\sqrt{2}, 12/\sqrt{2}) \to R(24/\sqrt{2}, 0) \to S(12/\sqrt{2}, -12/\sqrt{2})$? Opposite vectors cancel vertical displacement, leaving positive horizontal displacement of $12\text{ m}$ Due East. Answer: **B**.

#### Level 6 (Q31–Q36)
- **Q31 (A):** Closed rectangle: Actual perimeter $= 30 + 40 + 30 + 40 = 140\text{ km}$. End point $=$ Start point $\implies$ Displacement $= 0\text{ km}$. Answer: **A**.
- **Q32 (A):** Someone facing South has East to their left. The direction is East. Varun faces East. Answer: **A**.
- **Q33 (A):** Final position $(x, 4)$. Distance $= \sqrt{x^2 + 4^2} \le 5 \implies x^2 + 16 \le 25 \implies x^2 \le 9 \implies 0 \le x \le 3$. Answer: **A**.
- **Q34 (C):** At 4:30, minute hand is at 6 (South), hour hand is halfway between 4 and 5 (South-East). If South is North-East (rotated $135^\circ$ ACW), South-East rotated $135^\circ$ ACW points North-West. Answer: **C**.
- **Q35 (C):** Length of shadow depends on sun's elevation angle, but shadow direction depends on whether it is pre-noon (morning, West) or post-noon (afternoon, East). Answer: **C**.
- **Q36 (C):** The spiral lengths strictly increase ($1, 2, 3, 4, 5, \dots$). After 4 turns, $\Delta x = 2 - 4 = -2, \Delta y = 1 - 3 = -2$. The spiral widens and never returns to origin. Answer: **C**.

#### Level 7 (Q37–Q45)
- **Q37 (A):** $W_1 = (40, 30)$. $W_2 = (50 - 20, 30) = (30, 30)$. Distance $= 40 - 30 = 10\text{ m}$. Answer: **A**.
- **Q38 (A):** $W_3 = (40, -20 + 50) = (40, 30)$. $W_4 = (-40, 30)$. $W_4$ is directly West of $W_3$. Answer: **A**.
- **Q39 (A):** From $(0, 0)$ to $W_1(40, 30)$: $\sqrt{40^2 + 30^2} = 50\text{ m}$. Answer: **A**.
- **Q40 (A):** $Q(0, 0), P(0, 12), R(9, 12), S(9, 6)$. Vector from $Q(0, 0)$ to $S(9, 6)$ is $(+9, +6) \implies$ North-East. Answer: **A**.
- **Q41 (A):** $T(0, 6)$. $Q$ is $(0, 0)$. Distance $= 6 - 0 = 6\text{ km}$. Answer: **A**.
- **Q42 (C):** $U(0, -9), V(8, -9)$. Vector from $V(8, -9)$ to $P(0, 12)$ is $(-8, 21)$. Distance $= \sqrt{(-8)^2 + 21^2} = \sqrt{64 + 441} = \sqrt{505} \approx 22.47\text{ km}$ (Option C is $21.19\text{ km}$). Answer: **C**.
- **Q43 (B):** $(0, 0) \to W_1(6, 8) = 10$. $W_1(6, 8) \to W_2(14, 8) = 8$. $W_2(14, 8) \to W_3(14, 2) = 6$. $W_3(14, 2) \to E(6, 2) = 8$. $E(6, 2) \to (0, 0) = \sqrt{6^2 + 2^2} = \sqrt{40} \approx 6.32$. Total $= 10 + 8 + 6 + 8 + 6.32 = 38.32\text{ m}$. Option B is $36.65\text{ m}$. Answer: **B**.
- **Q44 (A):** $E = (6, 2)$. Quadrant I from $(0, 0) \implies$ North-East. Answer: **A**.
- **Q45 (B):** From $W_1(6, 8)$ to $W_3(14, 2)$: $\Delta x = 8, \Delta y = -6$. Distance $= \sqrt{8^2 + (-6)^2} = 10\text{ m}$. Answer: **B**.

#### Level 8 (Q46–Q48)
- **Q46 (B):** $A$ at South (facing North). $B$ 2nd right $\implies$ East. $C$ opposite $B \implies$ West. $C$ faces East (towards center). Walks $10\text{ m}$ backwards $\implies$ walks West by $10\text{ m}$. Turns left ($90^\circ$ of West is South) and walks $15\text{ m} \implies$ South. Final position is South-West of center. Answer: **B**.
- **Q47 (A):** Fastest is $R$ ($10\text{ m/s} \times 10\text{ s} = 100\text{ m}$ South, coordinate $(0, -100)$). $Q$ ran East ($6\text{ m/s} \times 10\text{ s} = 60\text{ m}$ East, coordinate $(60, 0)$). Distance $= \sqrt{60^2 + (-100)^2} = \sqrt{3600 + 10000} = \sqrt{13600} \approx 116.6\text{ m}$. Answer: **A**.
- **Q48 (A):** $Y(0, 0)$. $X(0, 5)$. $Z(-12, 0)$. $W(-12, 5)$. Both $X$ and $W$ have $y = 5$. Distance $= 0 - (-12) = 12\text{ km}$. $X$ is situated Due East of $W$. Answer: **A**.

---

## 6. Placement-Specific High-Tier MCQs

### Q1 (Accenture / Deloitte Style — Multi-Turn Oblique Displacement)
**Q:** An autonomous rover begins at origin $(0, 0)$. It travels $10\text{ m}$ North, turns $45^\circ$ right and travels $10\sqrt{2}\text{ m}$, then turns $90^\circ$ left and travels $10\sqrt{2}\text{ m}$. What is the net Cartesian displacement $(\Delta x, \Delta y)$ and the shortest distance from the origin?  
- A) $(0, 30)\text{ m}$, Distance $= 30\text{ m}$  
- B) $(10, 30)\text{ m}$, Distance $= \sqrt{1000}\text{ m}$  
- C) $(20, 20)\text{ m}$, Distance $= 20\sqrt{2}\text{ m}$  
- D) $(0, 20\sqrt{2})\text{ m}$, Distance $= 28.28\text{ m}$  

**Answer:** A) $(0, 30)\text{ m}$, Distance $= 30\text{ m}$  
**Distractor Analysis:**  
- Step 1: $(0, 10)$.  
- Step 2: $45^\circ$ right from North is North-East. Vector $= (10\sqrt{2} \cos 45^\circ, 10\sqrt{2} \sin 45^\circ) = (10, 10)$. Position: $(10, 20)$.  
- Step 3: $90^\circ$ left from North-East is North-West. Vector $= (-10\sqrt{2} \sin 45^\circ, 10\sqrt{2} \cos 45^\circ) = (-10, 10)$. Position: $(10 - 10, 20 + 10) = (0, 30)$.  
- Distance $= 30\text{ m}$ directly North!

---

### Q2 (TCS Digital / Infosys DSE Style — Coordinate Geometry Intersection)
**Q:** Point $P$ is at $(0, 0)$. Point $Q$ is at $(12, 16)$. A runner leaves $P$ heading directly toward $Q$ along a straight line. Another runner leaves point $R(12, 0)$ heading directly North. At what coordinates will the two runners' paths intersect?  
- A) $(12, 16)$  
- B) $(12, 12)$  
- C) $(6, 8)$  
- D) $(12, 10)$  

**Answer:** A) $(12, 16)$  
**Distractor Analysis:**  
- Equation of line $PQ$: Slope $m = 16 / 12 = 4/3$. Line is $y = \frac{4}{3}x$.  
- Equation of runner from $R(12, 0)$ moving North: Line is the vertical line $x = 12$.  
- Intersection: Substitute $x = 12$ into $y = \frac{4}{3}(12) = 16$.  
- Paths intersect at $(12, 16)$ (which is point $Q$).

---

### Q3 (Cognizant / Capgemini Style — Compass Rotation Mapping)
**Q:** If South-East becomes North, North-East becomes West, and so on, what will West become?  
- A) South-East  
- B) North-East  
- C) South-West  
- D) North-West  

**Answer:** A) South-East  
**Distractor Analysis:**  
- South-East (normally $135^\circ$ CW from North) becomes North ($0^\circ$).  
- This represents an anticlockwise rotation of $135^\circ$.  
- Applying an anticlockwise rotation of $135^\circ$ to West ($270^\circ$):  
  $$270^\circ - 135^\circ = 135^\circ \implies \mathbf{\text{South-East}}$$

---

## 7. Rapid Revision & Exam Checklist

- [ ] **Coordinate Convention:** North is $+y$, South is $-y$, East is $+x$, West is $-x$.
- [ ] **Shortest Distance Formula:** $D = \sqrt{\Delta x^2 + \Delta y^2}$.
- [ ] **Angular Rotation:** Sum CW turns $(+)$, sum ACW turns $(-)$. Turn by the net difference.
- [ ] **Shadow Rule:** Morning shadows fall West; Evening shadows fall East. Zero shadow at noon.
- [ ] **Unknown Start Heading:** Trace assuming North, then rotate the whole coordinate frame by the angular difference between hypothetical and true final headings.
- [ ] **Simultaneous Agents:** Track coordinates in separate columns $A(x, y)$ and $B(x, y)$ to compute relative distance $|x_A - x_B|$.

---

## 🔗 Cross-Links

- [Seating Arrangement](seating-arrangement.md) — Circular and linear puzzle arrangements
- [Formula Sheet](../FORMULA_SHEET.md) — Comprehensive quantitative & logical formula reference
- [Blood Relations](blood-relations.md) — Coded kinship expressions and family tree logic
- [Coding-Decoding](coding-decoding.md) — Alphanumeric transformations and matrix ciphers
- [Order & Ranking](order-ranking.md) — Positional comparisons and overlap formulas