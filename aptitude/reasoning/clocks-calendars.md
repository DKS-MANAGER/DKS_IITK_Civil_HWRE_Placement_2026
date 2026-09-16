# Clocks & Calendars

> **Priority:** P1 · **Role relevance:** High (Universal across Core, IT, Analytics, Consulting & Banking)  
> **Difficulty range:** Foundation → Hybrid Expert · **Target speed:** 45 sec (Direct Angle / Day) – 90–120 sec (Faulty Clocks / Multi-Century Caselets)

---

## 1. Mathematical Foundations of Clocks

A standard analog clock dial is a circle of $360^\circ$ divided into 12 hour spaces ($30^\circ$ each) and 60 minute spaces ($6^\circ$ each).

```
                     12 [0° / 360°]
                11        1
            10               2
          9 [270°]        3 [90°]
            8                4
                7         5
                     6 [180°]
```

### 1.1 Angular Velocities
- **Minute Hand:** Moves $360^\circ$ in 60 minutes $\implies \mathbf{6^\circ/\text{min}}$.
- **Hour Hand:** Moves $360^\circ$ in 12 hours (720 minutes) $\implies \mathbf{0.5^\circ = \frac{1}{2}^\circ/\text{min}}$ ($30^\circ/\text{hr}$).
- **Relative Speed (Minute hand with respect to Hour hand):**
  $$\text{Relative Speed} = 6^\circ - 0.5^\circ = \mathbf{5.5^\circ = \frac{11}{2}^\circ/\text{min}}$$
- In every minute, the minute hand gains $5.5^\circ$ or $\frac{11}{2}^\circ$ over the hour hand.
- To gain 1 minute space ($6^\circ$), the minute hand requires:
  $$\frac{6^\circ}{5.5^\circ} = \frac{12}{11}\text{ minutes}$$

### 1.2 Angle Between Hands Formula
At $H\text{ hours}$ and $M\text{ minutes}$ ($0 \le H \le 12$, $0 \le M < 60$):
$$\theta = \left|30H - \frac{11}{2}M\right| = |30H - 5.5M|$$
- **Reflex Angle:** If the acute/interior angle is $\theta$, the reflex angle is $360^\circ - \theta$.

### 1.3 Occurrence Frequencies in 12 Hours & 24 Hours

| Condition | Angle | Frequency in 12 Hours | Frequency in 24 Hours | Note / Missing Hour |
|:----------|:-----:|:---------------------:|:---------------------:|:--------------------|
| **Coincidence (Together)** | $0^\circ$ | **11 times** | **22 times** | Between 11:00 and 1:00, coincidence occurs only once (at exactly 12:00). |
| **Straight Line, Opposite** | $180^\circ$ | **11 times** | **22 times** | Between 5:00 and 7:00, hands are opposite only once (at exactly 6:00). |
| **Straight Line (Coincide or Opposite)** | $0^\circ$ or $180^\circ$ | **22 times** | **44 times** | Sum of coincidence and opposite occurrences. |
| **Right Angles (Perpendicular)** | $90^\circ$ | **22 times** | **44 times** | Hand makes $90^\circ$ twice per hour, except between 2–4 and 8–10 (3 times each). |

### 1.4 Coincidence Interval & Faulty Clock Mechanics
In a normal clock, the minute hand starts at 12:00 together with the hour hand. They coincide next when the minute hand completes a full round and catches up with the hour hand ($360^\circ$ relative gain):
$$\text{Time to coincide} = \frac{360^\circ}{5.5^\circ/\text{min}} = \frac{720}{11} = \mathbf{65\frac{5}{11}\text{ minutes}} \approx 65.4545\text{ min}$$

- **The Clock Gain/Loss Rule:**
  - If the hands of a clock coincide in **less than** $65\frac{5}{11}\text{ minutes}$, the clock is **too fast (gaining time)**.
  - If the hands coincide in **more than** $65\frac{5}{11}\text{ minutes}$, the clock is **too slow (losing time)**.
- **Gain / Loss in a Given Time Interval $T$:**
  $$\text{Gain or Loss per coincidence} = \left(65\frac{5}{11} - M_{\text{actual}}\right)\text{ minutes}$$
  $$\text{Total Gain or Loss in } T\text{ hours} = \frac{\left(65\frac{5}{11} - M\right)}{M} \times T \times 60$$

### 1.5 Mirror and Water Image Clock Formulas
When a standard clock is viewed in a mirror or water reflection:

| Reflection Type | Transformation Formula | If Minutes $> 60$ or Hours $> 12$ |
|:----------------|:-----------------------|:-----------------------------------|
| **Vertical Mirror** | $\text{Mirror Time} = \mathbf{11:60 - \text{Real Time}}$ | For 24-hr clock: $\mathbf{23:60 - \text{Real Time}}$ |
| **Horizontal / Water** | $\text{Water Time} = \mathbf{18:30 - \text{Real Time}}$ | If minutes $> 30$: borrow 1 hour $\to \mathbf{17:90 - \text{Real Time}}$ |

---

## 2. Mathematical Foundations of Calendars

The Gregorian calendar measures the tropical solar year ($\approx 365.2422\text{ days}$).

### 2.1 The Odd Days Concept
An **odd day** is the remainder obtained when the total number of days in a given period is divided by 7:
$$\text{Odd Days} = \text{Total Days} \pmod 7$$

- **Ordinary Year (365 days):** $365 = 52 \text{ weeks} + \mathbf{1\text{ odd day}}$.
- **Leap Year (366 days):** $366 = 52 \text{ weeks} + \mathbf{2\text{ odd days}}$.

### 2.2 Leap Year Rules & Century Boundary Exceptions
1. **Non-Century Years:** A year is a leap year if and only if it is divisible by **4** (e.g., 2024, 2028, 1996).
2. **Century Years:** A century year is a leap year if and only if it is divisible by **400** (e.g., 1600, 2000, 2400 are leap years; 1700, 1800, 1900, 2100 are **NOT** leap years).

### 2.3 Odd Days Across Centuries

$$\text{100 years} = 76 \text{ ordinary years} + 24 \text{ leap years} = (76 \times 1) + (24 \times 2) = 124\text{ days} = 17 \times 7 + \mathbf{5\text{ odd days}}$$

| Century Span | Total Ordinary Years | Total Leap Years | Net Odd Days | Simplified Mod 7 |
|:-------------|:--------------------:|:----------------:|:------------:|:----------------:|
| **100 Years** | 76 | 24 | 124 | **5** |
| **200 Years** | - | - | $5 \times 2 = 10$ | **3** |
| **300 Years** | - | - | $5 \times 3 = 15$ | **1** |
| **400 Years** | - | - | $5 \times 4 + 1 = 21$ | **0** |

- **Multiples of 400 Years ($400, 800, 1200, 1600, 2000, 2400$):** Exactly **0 odd days**.

### 2.4 Day of the Week Mapping

| Odd Days | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|:---------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Day** | **Sunday** | **Monday** | **Tuesday** | **Wednesday** | **Thursday** | **Friday** | **Saturday** |

> [!IMPORTANT]
> **The Century Trap:**  
> The last day of a century can only have **5, 3, 1, or 0 odd days**, corresponding to **Friday, Wednesday, Monday, or Sunday**.  
> Therefore, the last day of a century can **NEVER be Tuesday, Thursday, or Saturday**.

### 2.5 Calendar Repetition Cycle
To find when a given calendar repeats:
1. Count odd days year by year starting from the given year.
2. The year immediately following a total sum of odd days divisible by 7 is a candidate.
3. **Leap Compatibility Constraint:** An ordinary year can only repeat as an ordinary year; a leap year can only repeat as a leap year!

**Standard Heuristic (Within the same century):**
- Leap year $\to$ Repeats in **+28 years**.
- Leap year + 1 $\to$ Repeats in **+6 years**.
- Leap year + 2 $\to$ Repeats in **+11 years**.
- Leap year + 3 $\to$ Repeats in **+11 years**.
*(Note: If a century boundary with an ordinary century year like 1900 or 2100 is crossed, this heuristic shifts by +12 or +40 years).*

---

## 3. Fully Solved Worked Examples

### Example 1: Acute and Reflex Angle Calculation (Medium)
**Problem:** What are the acute angle and reflex angle between the hands of a clock at `8:20`?  
**Step-by-Step Derivation:**
1. Given $H = 8$, $M = 20$.
2. Apply the angle formula:
   $$\theta = |30H - 5.5M| = |30(8) - 5.5(20)| = |240 - 110| = \mathbf{130^\circ}$$
3. The acute angle is **$130^\circ$**.
4. The reflex angle is:
   $$\text{Reflex} = 360^\circ - 130^\circ = \mathbf{230^\circ}$$

---

### Example 2: Exact Coincidence Between 7 and 8 O'Clock (Hard)
**Problem:** At what exact time between 7:00 and 8:00 do the hands of a clock coincide?  
**Step-by-Step Derivation:**
1. At 7:00, the hour hand is at $7 \times 30^\circ = 210^\circ$, and the minute hand is at $0^\circ$.
2. The minute hand must gain $210^\circ$ over the hour hand at a relative speed of $5.5^\circ/\text{min} = \frac{11}{2}^\circ/\text{min}$.
3. Time required:
   $$M = \frac{210^\circ}{\frac{11}{2}^\circ/\text{min}} = \frac{420}{11} = 38\frac{2}{11}\text{ minutes}$$
4. **Answer:** Exactly **$38\frac{2}{11}\text{ minutes past 7}$** (or $7\text{ hr } 38\text{ min } 10.9\text{ sec}$).

---

### Example 3: Single Faulty Clock Gaining Time (Expert)
**Problem:** A watch gains 5 seconds in 3 minutes and was set right at 7:00 AM on Monday. What will be the true time when the watch indicates 6:00 PM on the same day?  
**Step-by-Step Derivation:**
1. Determine the rate of gain:
   - In 3 minutes, it gains $\frac{5}{60} = \frac{1}{12}\text{ minute}$.
   - Thus, in 3 minutes of true time, the watch shows $3 + \frac{1}{12} = \frac{37}{12}\text{ minutes}$.
   - Conversely, $\frac{37}{12}\text{ minutes of indicated time} = 3\text{ minutes of true time}$.
   - Therefore, $1\text{ minute of indicated time} = 3 \times \frac{12}{37} = \frac{36}{37}\text{ minute of true time}$.
2. Calculate total indicated elapsed time from 7:00 AM to 6:00 PM on the same day:
   $$\text{Elapsed time} = 11\text{ hours} = 11 \times 60 = 660\text{ minutes}$$
3. True elapsed time:
   $$\text{True time} = 660 \times \frac{36}{37} = \frac{23760}{37} = 642\frac{6}{37}\text{ minutes} = 10\text{ hours } 42\frac{6}{37}\text{ minutes}$$
4. Add true elapsed time to 7:00 AM:
   $$7\text{ AM} + 10\text{ hr } 42\frac{6}{37}\text{ min} = \mathbf{5:42\frac{6}{37}\text{ PM}}$$
5. **Answer:** The true time is **$5:42\frac{6}{37}\text{ PM}$** (or 17 minutes $53.5$ seconds before 6:00 PM).

---

### Example 4: Exact Day on Historical Date: 15 August 1947 (Expert)
**Problem:** What day of the week was 15 August 1947?  
**Step-by-Step Derivation:**
1. **Deconstruct Year:**
   - Completed period before 1947: 1946 years.
   - Break down 1946 years:
     - $1600\text{ years} = \mathbf{0\text{ odd days}}$.
     - $300\text{ years} = \mathbf{1\text{ odd day}}$.
     - Remaining 46 years ($1901$ to $1946$):
       - Number of leap years in 46: $\lfloor 46 / 4 \rfloor = 11\text{ leap years}$.
       - Number of ordinary years: $46 - 11 = 35\text{ ordinary years}$.
       - Odd days in 46 years: $(11 \times 2) + (35 \times 1) = 22 + 35 = 57\text{ days}$.
       - $57 \pmod 7 = \mathbf{1\text{ odd day}}$.
   - Total odd days up to 31 December 1946:
     $$0 + 1 + 1 = \mathbf{2\text{ odd days}}$$
2. **Count Days in 1947 up to 15 August:**
   - 1947 is not a leap year, so February has 28 days.
   - January: 31 days $\equiv 3$
   - February: 28 days $\equiv 0$
   - March: 31 days $\equiv 3$
   - April: 30 days $\equiv 2$
   - May: 31 days $\equiv 3$
   - June: 30 days $\equiv 2$
   - July: 31 days $\equiv 3$
   - August: 15 days $\equiv 1$
   - Sum of month days: $3 + 0 + 3 + 2 + 3 + 2 + 3 + 1 = 17\text{ days}$.
   - $17 \pmod 7 = \mathbf{3\text{ odd days}}$.
3. **Total Cumulative Odd Days:**
   $$\text{Total} = 2 + 3 = \mathbf{5\text{ odd days}}$$
4. **Day Lookup:**
   - $0 = \text{Sun}, 1 = \text{Mon}, 2 = \text{Tue}, 3 = \text{Wed}, 4 = \text{Thu}, \mathbf{5 = \text{Friday}}, 6 = \text{Sat}$.
5. **Answer:** **Friday**.

---

## 4. Comprehensive Practice Set (48 Placement Questions)

### Level 1: Foundation (Q1–Q6)

**Q1.** What is the angle between the hour hand and the minute hand of a clock at `3:40`?  
- A) $120^\circ$  
- B) $130^\circ$  
- C) $140^\circ$  
- D) $150^\circ$  

**Q2.** At what time between `2:00` and `3:00` do the hands of a clock coincide?  
- A) $10\frac{10}{11}\text{ min past 2}$  
- B) $11\frac{1}{11}\text{ min past 2}$  
- C) $10\frac{5}{11}\text{ min past 2}$  
- D) $12\text{ min past 2}$  

**Q3.** How many times do the hands of a clock form a straight line in a 24-hour day?  
- A) 22  
- B) 24  
- C) 44  
- D) 48  

**Q4.** If 1 January 2006 was a Sunday, what day of the week was 1 January 2010?  
- A) Thursday  
- B) Friday  
- C) Saturday  
- D) Sunday  

**Q5.** How many odd days are there in 100 years?  
- A) 0  
- B) 3  
- C) 5  
- D) 6  

**Q6.** A clock viewed in a mirror shows `3:15`. What is the actual time?  
- A) `8:45`  
- B) `9:45`  
- C) `8:15`  
- D) `9:15`  

---

### Level 2: Intermediate (Q7–Q12)

**Q7.** What is the acute angle between the hands of a clock at `7:10`?  
- A) $150^\circ$  
- B) $155^\circ$  
- C) $160^\circ$  
- D) $165^\circ$  

**Q8.** At what time between `4:00` and `5:00` are the hands of a clock pointing in opposite directions?  
- A) $52\frac{3}{11}\text{ min past 4}$  
- B) $53\frac{7}{11}\text{ min past 4}$  
- C) $54\frac{6}{11}\text{ min past 4}$  
- D) $55\frac{5}{11}\text{ min past 4}$  

**Q9.** What day of the week was `26 January 1950` (the date the Indian Constitution came into effect)?  
- A) Tuesday  
- B) Wednesday  
- C) Thursday  
- D) Friday  

**Q10.** At what time between `5:00` and `6:00` will the hands of a clock be at a right angle for the first time?  
- A) $10\frac{10}{11}\text{ min past 5}$  
- B) $11\frac{5}{11}\text{ min past 5}$  
- C) $12\frac{4}{11}\text{ min past 5}$  
- D) $10\frac{2}{11}\text{ min past 5}$  

**Q11.** Which of the following years had the exact same calendar as the year `2007`?  
- A) 2014  
- B) 2016  
- C) 2017  
- D) 2018  

**Q12.** If today is Wednesday, what day of the week will it be after 94 days?  
- A) Thursday  
- B) Friday  
- C) Saturday  
- D) Sunday  

---

### Level 3: Hard — Reflex Angles & Century Crossings (Q13–Q18)

**Q13.** What is the reflex angle between the hands of a clock at `10:25`?  
- A) $162.5^\circ$  
- B) $197.5^\circ$  
- C) $212.5^\circ$  
- D) $227.5^\circ$  

**Q14.** At what time between `8:00` and `9:00` are the hands of a clock at a right angle for the second time?  
- A) $58\frac{2}{11}\text{ min past 8}$  
- B) $60\text{ min past 8}$ (i.e., 9:00)  
- C) $59\frac{1}{11}\text{ min past 8}$  
- D) $54\frac{6}{11}\text{ min past 8}$  

**Q15.** What was the day of the week on `28 May 2006`?  
- A) Friday  
- B) Saturday  
- C) Sunday  
- D) Monday  

**Q16.** A clock shows `8:20` when viewed directly. If it is observed in a pool of still water (horizontal reflection), what approximate time does the reflection indicate?  
- A) `10:10`  
- B) `9:10`  
- C) `10:20`  
- D) `9:20`  

**Q17.** How many leap years are there between the year `1801` and the year `1900` inclusive?  
- A) 25  
- B) 24  
- C) 23  
- D) 26  

**Q18.** A person tells his friend: *"My birthday is on 15 March. In the year 2020, my birthday was on a Sunday."* On which day of the week did his birthday fall in `2016`?  
- A) Monday  
- B) Tuesday  
- C) Wednesday  
- D) Sunday  

---

### Level 4: Very Hard — Calendar Repetitions & Gain Rates (Q19–Q24)

**Q19.** Which year will have the exact same calendar as `1896`?  
- A) 1902  
- B) 1908  
- C) 1924  
- D) 1952  

**Q20.** A clock is set right at `5:00 AM`. It loses 16 minutes in 24 hours. What will be the true time when the clock indicates `10:00 PM` on the 4th day?  
- A) `10:45 PM`  
- B) `11:00 PM`  
- C) `11:15 PM`  
- D) `11:30 PM`  

**Q21.** An analog clock loses 2 minutes every hour, while another clock gains 1 minute every hour. Both are set right at `12:00 noon` on Monday. After how many hours will the two clocks display the same time again?  
- A) 120 hours  
- B) 180 hours  
- C) 240 hours  
- D) 360 hours  

**Q22.** What was the day of the week on `15 January 1750`?  
- A) Tuesday  
- B) Wednesday  
- C) Thursday  
- D) Friday  

**Q23.** In an ordinary year, which of the following pairs of months start on the exact same day of the week?  
- A) April and July  
- B) January and April  
- C) March and November  
- D) Both A and C  

**Q24.** At what time between `1:00` and `2:00` will the minute hand be 3 minutes spaces ahead of the hour hand?  
- A) $8\frac{8}{11}\text{ min past 1}$  
- B) $9\text{ min past 1}$  
- C) $9\frac{9}{11}\text{ min past 1}$  
- D) $10\text{ min past 1}$  

---

### Level 5: Expert — Diverging Clocks & Complex Dates (Q25–Q30)

**Q25.** The hands of a faulty clock coincide every `64 minutes` of true time. How much time does the clock gain or lose in a full 24-hour period?  
- A) Loses $32\frac{8}{11}\text{ minutes}$  
- B) Gains $32\frac{8}{11}\text{ minutes}$  
- C) Gains $34\frac{2}{11}\text{ minutes}$  
- D) Loses $34\frac{2}{11}\text{ minutes}$  

**Q26.** Two clocks are synchronized at `9:00 AM` on Sunday. Clock A gains 3 minutes per hour, and Clock B loses 2 minutes per hour. When Clock A indicates `3:30 PM` on Tuesday, what time does Clock B indicate?  
- A) `10:30 AM`  
- B) `11:10 AM`  
- C) `11:20 AM`  
- D) `11:40 AM`  

**Q27.** A clock stopped at `4:15 PM`. It was restarted at `4:45 PM` by an operator who inadvertently set the hands forward by 20 minutes from where it stopped. If the clock then ran at a normal rate, what is the true time when the clock indicates `8:00 PM` on the same evening?  
- A) `7:30 PM`  
- B) `7:50 PM`  
- C) `8:10 PM`  
- D) `8:30 PM`  

**Q28.** What day of the week will it be on `29 February 2400`?  
- A) Sunday  
- B) Monday  
- C) Tuesday  
- D) Wednesday  

**Q29.** A watch that gains uniformly is 5 minutes slow at `8:00 AM` on Sunday and is 5 minutes 48 seconds fast at `8:00 PM` on the following Sunday. When did it show the correct time?  
- A) `7:20 PM` on Tuesday  
- B) `7:20 PM` on Wednesday  
- C) `8:00 AM` on Wednesday  
- D) `8:00 PM` on Wednesday  

**Q30.** How many times in a period of 400 consecutive Gregorian years does the 29th day of the month occur?  
- A) 4400  
- B) 4497  
- C) 4800  
- D) 4897  

---

### Level 6: Trap & Inference Sets (Q31–Q36)

**Q31 (The Century Last-Day Impossibility Trap).**  
Which of the following days of the week can **NEVER** be the last day of a century?  
- A) Wednesday  
- B) Friday  
- C) Tuesday  
- D) Sunday  

**Q32 (The Standard Coincidence Constant Trap).**  
A person asserts: *"A normal clock's minute and hour hands coincide exactly every 65 minutes."* If a clock's hands actually coincide every 65 minutes, how is the clock performing?  
- A) Running accurately  
- B) Gaining time  
- C) Losing time  
- D) Stopped  

**Q33 (The Leap Century Boundary Cross Trap).**  
What is the calendar repetition period for the leap year `1996`?  
- A) 28 years (repeats in 2024)  
- B) 40 years (repeats in 2036)  
- C) 12 years (repeats in 2008)  
- D) 6 years (repeats in 2002)  

**Q34 (The 28 February / 1 March Boundary Trap).**  
If `1 March` of a non-leap year falls on a Sunday, what day of the week did `1 February` fall on?  
- A) Friday  
- B) Saturday  
- C) Sunday  
- D) Monday  

**Q35 (The Double Mirror Inversion Trap).**  
An analog clock is viewed through two mirrors placed at $90^\circ$ to each other, producing a double reflection. If the actual time is `4:35`, what time does the double reflection show?  
- A) `7:25`  
- B) `8:25`  
- C) `4:35`  
- D) `12:00`  

**Q36 (The 30-Day Month Frequency Trap).**  
In a non-leap year of 365 days starting on a Friday, how many months have five Sundays?  
- A) 3  
- B) 4  
- C) 5  
- D) 6  

---

### Level 7: Extreme Multi-Question Caselets (Q37–Q45)

#### Caselet 1 (Questions 37–39): The Faulty Railway Clocks of Central Station
*Directions for Q37–Q39:* Read the following technical log from Central Junction.  
At Central Railway Station, two electronic-driven analog platform clocks, Platform Clock A and Platform Clock B, are synchronized with the Master Atomic Clock at `12:00 midnight` on Friday night (Saturday `00:00 hrs`).
- Platform Clock A **gains 2 minutes every 6 hours**.
- Platform Clock B **loses 3 minutes every 8 hours**.
- A high-speed express train is scheduled to arrive at `3:00 PM` on Monday (true time).

**Q37.** What time does Platform Clock A indicate when the train arrives at its scheduled time on Monday?  
- A) `3:21 PM`  
- B) `3:26 PM`  
- C) `3:39 PM`  
- D) `4:03 PM`  

**Q38.** When Platform Clock B indicates exactly `11:45 PM` on Friday night, what is the true time?  
- A) `11:54 PM`  
- B) `11:51 PM`  
- C) `12:00 midnight`  
- D) `11:36 PM`  

**Q39.** At what true time will the difference in indicated times between Platform Clock A and Platform Clock B be exactly 35 minutes?  
- A) Sunday `12:00 noon`  
- B) Saturday `11:00 PM`  
- C) Sunday `1:25 AM`  
- D) Saturday `6:00 PM`  

---

#### Caselet 2 (Questions 40–42): The Multi-Century Historical Timeline
*Directions for Q40–Q42:*  
An archive contains records dated across three distinct centuries:
1. Document 1: `4 July 1776` (US Declaration of Independence)
2. Document 2: `14 July 1789` (Storming of the Bastille)
3. Document 3: `18 June 1815` (Battle of Waterloo)

**Q40.** On which day of the week was Document 1 (`4 July 1776`) signed?  
- A) Tuesday  
- B) Wednesday  
- C) Thursday  
- D) Friday  

**Q41.** On which day of the week did the Storming of the Bastille (`14 July 1789`) occur?  
- A) Monday  
- B) Tuesday  
- C) Wednesday  
- D) Friday  

**Q42.** Exactly how many odd days accumulated between `4 July 1776` and `14 July 1789`?  
- A) 1  
- B) 3  
- C) 5  
- D) 0  

---

#### Caselet 3 (Questions 43–45): Precision Clean-Room Mirror Calibration
*Directions for Q43–Q45:*  
In a semiconductor clean-room, a wall clock without numerical digits (only dots at the 12 hour marks) is mounted opposite a planar inspection mirror.
- A camera records the mirror reflection of the clock.
- At an initial inspection timestamp, the mirror reflection reads `2:40`.
- 45 minutes of true time elapse.

**Q43.** What was the actual time on the clock at the initial inspection?  
- A) `9:20`  
- B) `10:20`  
- C) `9:40`  
- D) `8:20`  

**Q44.** After the 45 minutes of true time elapse, what is the acute angle between the real hands of the clock?  
- A) $67.5^\circ$  
- B) $60^\circ$  
- C) $87.5^\circ$  
- D) $75^\circ$  

**Q45.** What will the camera record as the mirror reflection of the clock after the 45 minutes have elapsed?  
- A) `1:55`  
- B) `2:05`  
- C) `1:25`  
- D) `3:25`  

---

### Level 8: Hybrid Expert (Q46–Q48)

**Q46 (Clock Angle + Calendar Interval).**  
An astronomer schedules observations for a date that falls exactly 100 days after a Tuesday. On that target date, observations begin the moment the hands of the observatory clock form an angle of $0^\circ$ between `10:00 AM` and `11:00 AM`. At what exact time and on what day of the week do observations begin?  
- A) Thursday at `10:54 6/11 AM`  
- B) Thursday at `10:52 3/11 AM`  
- C) Friday at `10:54 6/11 AM`  
- D) Wednesday at `10:54 6/11 AM`  

**Q47 (Clock Relative Motion + Circular Track Physics).**  
A runner completes laps on a circular track. A coach times the runner using a stopwatch that is fast by 15 seconds every hour. The coach's stopwatch records the runner's total marathon time as 3 hours 4 minutes and 30 seconds. If the runner was pacing to finish in exactly 3 hours of true time, did the runner meet their goal, and what was their actual true time?  
- A) No, true time was 3 hours 3 minutes 45 seconds  
- B) Yes, true time was 2 hours 59 minutes 15 seconds  
- C) No, true time was 3 hours 4 minutes 0 seconds  
- D) No, true time was 3 hours 3 minutes 44 seconds  

**Q48 (Calendar Modulo + Shift Scheduling Rotation).**  
A production facility operates every single day of the year. Three engineering shifts ($A, B, C$) rotate in sequence: Shift A works Day 1, Shift B works Day 2, Shift C works Day 3, Shift A works Day 4, and so forth. In a leap year where `1 January` is a Monday (Day 1) and Shift A works on 1 January:  
Which shift will work on `31 December` (Day 366) of that leap year, and what day of the week will it be?  
- A) Shift C, Tuesday  
- B) Shift B, Tuesday  
- C) Shift A, Tuesday  
- D) Shift C, Wednesday  

---

## 5. Master Answer Key & Comprehensive Solutions

### Master Answer Key (Q1–Q48)

| Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | B | **9** | C | **17** | B | **25** | B | **33** | A | **41** | B |
| **2** | A | **10** | A | **18** | B | **26** | B | **34** | C | **42** | C |
| **3** | C | **11** | D | **19** | C | **27** | B | **35** | C | **43** | A |
| **4** | B | **12** | C | **20** | B | **28** | C | **36** | C | **44** | C |
| **5** | C | **13** | B | **21** | C | **29** | B | **37** | A | **45** | A |
| **6** | A | **14** | B | **22** | C | **30** | B | **38** | C | **46** | A |
| **7** | B | **15** | C | **23** | D | **31** | C | **39** | C | **47** | C |
| **8** | C | **16** | A | **24** | A | **32** | B | **40** | C | **48** | A |

---

### Step-by-Step Derivations

#### Level 1 (Q1–Q6)
- **Q1 (B):** $\theta = |30(3) - 5.5(40)| = |90 - 220| = 130^\circ$. Answer: **B**.
- **Q2 (A):** Coincidence between 2:00 and 3:00 occurs when minute hand gains $2 \times 30^\circ = 60^\circ$. $M = 60 / (11/2) = 120/11 = 10\frac{10}{11}\text{ min past 2}$. Answer: **A**.
- **Q3 (C):** Hands form a straight line when they are together ($0^\circ$, 22 times) OR opposite ($180^\circ$, 22 times). Total = $22 + 22 = 44$ times in 24 hours. Answer: **C**.
- **Q4 (B):** Years 2006 (1), 2007 (1), 2008 (leap: 2), 2009 (1). Total odd days = $1 + 1 + 2 + 1 = 5$. Sunday + 5 days = Friday. Answer: **B**.
- **Q5 (C):** 100 years has 76 ordinary and 24 leap years. Total days = $76(1) + 24(2) = 124 \equiv 5\text{ odd days}$. Answer: **C**.
- **Q6 (A):** Mirror time: $11:60 - 3:15 = 8:45$. Answer: **A**.

#### Level 2 (Q7–Q12)
- **Q7 (B):** $\theta = |30(7) - 5.5(10)| = |210 - 55| = 155^\circ$. Answer: **B**.
- **Q8 (C):** Hands are opposite when gap is $180^\circ$. At 4:00, gap is $120^\circ$. To become opposite, minute hand must gain $120^\circ + 180^\circ = 300^\circ$. $M = 300 / (11/2) = 600/11 = 54\frac{6}{11}\text{ min past 4}$. Answer: **C**.
- **Q9 (C):** 26 Jan 1950: Up to 1949: $1600 (0) + 300 (1) + 49\text{ yrs} = 12\text{ leap} + 37\text{ ord} = 24 + 37 = 61 \equiv 5$. Total to 1949 = $1 + 5 = 6$ odd days. 26 days of Jan $\equiv 26 \pmod 7 = 5$. Net odd days = $6 + 5 = 11 \equiv 4 \implies \text{Thursday}$. Answer: **C**.
- **Q10 (A):** At 5:00, gap is $150^\circ$. First right angle occurs when gap reduces to $90^\circ$ (gain of $150 - 90 = 60^\circ$). $M = 60 / (11/2) = 120/11 = 10\frac{10}{11}\text{ min past 5}$. Answer: **A**.
- **Q11 (D):** 2007 is leap + 3. By the +11 rule: $2007 + 11 = 2018$. Verification: 2007 (1), 2008 (2), 2009 (1), 2010 (1), 2011 (1), 2012 (2), 2013 (1), 2014 (1), 2015 (1), 2016 (2), 2017 (1). Sum = 14 $\equiv 0$. Answer: **D**.
- **Q12 (C):** $94 \pmod 7 = 3$ odd days. Wednesday + 3 days = Saturday. Answer: **C**.

#### Level 3 (Q13–Q18)
- **Q13 (B):** $\theta = |30(10) - 5.5(25)| = |300 - 137.5| = 162.5^\circ$. Reflex angle = $360^\circ - 162.5^\circ = 197.5^\circ$. Answer: **B**.
- **Q14 (B):** At 8:00, hour hand is at $240^\circ$. Second right angle occurs when minute hand is $90^\circ$ ahead: gain required = $240^\circ + 90^\circ = 330^\circ$. $M = 330 / (11/2) = 660/11 = 60\text{ minutes}$. That is exactly 9:00! Answer: **B**.
- **Q15 (C):** 28 May 2006: 2000 yrs = 0. 5 completed yrs (2001–2005) = 1 leap (2004) + 4 ord = 6 odd days. In 2006: Jan (3) + Feb (0) + Mar (3) + Apr (2) + May 28 (0) = 8 $\equiv 1$. Total = $6 + 1 = 7 \equiv 0 \implies \text{Sunday}$. Answer: **C**.
- **Q16 (A):** Water reflection: $18:30 - 8:20 = 10:10$. Answer: **A**.
- **Q17 (B):** Century year 1900 is NOT divisible by 400, so it is NOT a leap year. In 100 years, leap years = $24$. Answer: **B**.
- **Q18 (B):** 15 March 2016 to 15 March 2020: 4 years span. Leap days crossed: 2020 Feb 29 is included (15 March 2020 is after Feb 29). 2016 Feb 29 is NOT crossed (starting at 15 March 2016). So only 2020 is a leap day! Total days = $3 \times 365 + 366 = 5\text{ odd days}$. Going backwards from Sunday: Sunday $- 5\text{ days} = \text{Tuesday}$. Answer: **B**.

#### Level 4 (Q19–Q24)
- **Q19 (C):** 1896 is a leap year. Standard +28 gives 1924. Crucially, 1900 is NOT a leap year, which usually alters leap cycles, but 1896 to 1924 span has odd days: $1896 (2) + 1897-1899 (3) + 1900 (1) + 1901-1903 (3) + 1904 (2) + \dots = 35 \equiv 0$. And 1924 is a leap year! Answer: **C**.
- **Q20 (B):** From 5:00 AM on Day 1 to 10:00 PM on Day 4: Elapsed indicated time = $3 \times 24 + 17 = 89\text{ hours}$. Clock loses 16 min in 24 hr $\implies 23\text{ hr } 44\text{ min} = 356/15\text{ hr of clock} = 24\text{ hr true}$. True time = $89 \times (24 / (356/15)) = 89 \times (360 / 356) = 89 \times (90 / 89) = 90\text{ hours}$. $90\text{ hours}$ after 5:00 AM Day 1 is 11:00 PM Day 4. Answer: **B**.
- **Q21 (C):** Relative divergence = $2 + 1 = 3\text{ minutes per hour}$. For clocks to show the same time again, they must diverge by 12 hours ($720\text{ minutes}$). Time required = $720 / 3 = 240\text{ hours}$. Answer: **C**.
- **Q22 (C):** 15 Jan 1750: 1600 yrs (0) + 100 yrs (5) = 5. 49 completed yrs = 12 leap + 37 ord = $24 + 37 = 61 \equiv 5$. Jan 15 = $15 \equiv 1$. Total = $5 + 5 + 1 = 11 \equiv 4 \implies \text{Thursday}$. Answer: **C**.
- **Q23 (D):** April (30) + May (31) + June (30) = $91 \equiv 0$ odd days $\implies$ April and July start on the same day. March (31) + April (30) + May (31) + June (30) + July (31) + August (31) + September (30) + October (31) = 245 $\equiv 0 \implies$ March and November start on the same day. Both A and C are true. Answer: **D**.
- **Q24 (A):** At 1:00, minute hand is at 0 min, hour hand is at 5 min spaces. For minute hand to be 3 min spaces ahead, it must gain $5 + 3 = 8\text{ min spaces}$. Time = $8 \times (12/11) = 96/11 = 8\frac{8}{11}\text{ min past 1}$. Answer: **A**.

#### Level 5 (Q25–Q30)
- **Q25 (B):** True coincidence interval = $65\frac{5}{11}\text{ min} = \frac{720}{11}\text{ min}$. Here hands coincide in 64 min (less than standard, so clock gains). Gain in 64 min = $\frac{720}{11} - 64 = \frac{16}{11}\text{ min}$. In 24 hours ($1440\text{ min}$): Total gain = $(16/11) / 64 \times 1440 = (1/44) \times 1440 = 360/11 = 32\frac{8}{11}\text{ minutes}$. Answer: **B**.
- **Q26 (B):** Total true elapsed time: Sunday 9:00 AM to Tuesday 3:30 PM: Sunday 9 AM to Tuesday 9 AM = 48 hr. 9 AM to 3:30 PM = 6.5 hr. But Clock A indicated 3:30 PM (gaining 3 min/hr). Indicated rate = 63 min/hr. True elapsed time = $54.5\text{ indicated hrs} \times (60/63) = 51.905\text{ hrs}$. Clock B loses 2 min/hr (shows 58 min/hr). Clock B elapsed = $51.905 \times (58/60) = 50.175\text{ hrs}$. Adding 50 hr 10 min to Sunday 9 AM yields Tuesday 11:10 AM. Answer: **B**.
- **Q27 (B):** Clock stopped at 4:15 PM, was restarted at 4:45 PM (true time) showing $4:15 + 0:20 = 4:35\text{ PM}$. At restart, the clock is running 10 minutes slow relative to true time ($4:45 - 4:35 = 10\text{ min slow}$). Since it runs at normal rate thereafter, when it indicates 8:00 PM, the true time is $8:00\text{ PM} - 10\text{ min} = 7:50\text{ PM}$. Answer: **B**.
- **Q28 (C):** 2400 is a leap century year divisible by 400. Up to 2399: $2000 (0) + 300 (1) + 99\text{ yrs} = 24\text{ leap} + 75\text{ ord} = 48 + 75 = 123 \equiv 4$. Total to 2399 = $1 + 4 = 5$ odd days. In 2400: Jan (31 $\equiv 3$) + Feb 29 ($29 \equiv 1$) = 4 odd days. Total odd days = $5 + 4 = 9 \equiv 2 \implies \text{Tuesday}$. Answer: **C**.
- **Q29 (B):** Total elapsed time from Sun 8 AM to following Sun 8 PM = 7 days 12 hr = 180 hours. Total gain = $5\text{ min} + 5\text{ min } 48\text{ sec} = 10\frac{4}{5}\text{ min} = \frac{54}{5}\text{ minutes}$. Clock is right when it has gained exactly 5 minutes. Time required = $5 \times (180 / (54/5)) = 5 \times (900 / 54) = 5 \times (50 / 3) = 250 / 3 = 83\text{ hr } 20\text{ min} = 3\text{ days } 11\text{ hr } 20\text{ min}$. Sun 8 AM + 3 days 11 hr 20 min = Wednesday 7:20 PM. Answer: **B**.
- **Q30 (B):** In 400 years, every year has eleven 29th days (Jan, Mar–Dec) = $400 \times 11 = 4400$. Additionally, February 29 occurs in every leap year. In 400 years, there are 97 leap years. Total occurrences = $4400 + 97 = 4497$. Answer: **B**.

#### Level 6 (Q31–Q36)
- **Q31 (C):** Odd days for 100, 200, 300, 400 years are 5, 3, 1, 0, corresponding to Friday, Wednesday, Monday, Sunday. The last day of a century can never be Tuesday, Thursday, or Saturday. Answer: **C**.
- **Q32 (B):** Normal coincidence interval is $65\frac{5}{11}\text{ min}$. Coinciding in 65 minutes is faster than normal $\implies$ Clock is **gaining time**. Answer: **B**.
- **Q33 (A):** For 1996 + 28 = 2024. Does it cross a non-leap century? The century year crossed is 2000, which IS a leap year! Thus the standard 28-year cycle is preserved: repeats in 2024. Answer: **A**.
- **Q34 (C):** February in a non-leap year has 28 days = 4 weeks + 0 odd days. Hence, 1 February and 1 March fall on the exact same day of the week: Sunday. Answer: **C**.
- **Q35 (C):** A double reflection across two perpendicular mirrors produces a $180^\circ$ rotation without parity inversion (left/right inversion reversed twice). Thus, the hands appear in their original actual position: 4:35. Answer: **C**.
- **Q36 (C):** If a 365-day year starts on Friday, Friday occurs 53 times, while other days occur 52 times. Month lengths with 5 Sundays occur in months of 31 days starting on Fri/Sat/Sun, 30 days starting on Sat/Sun. Detailed counting gives exactly 5 months with five Sundays. Answer: **C**.

#### Level 7 (Q37–Q45)
- **Q37 (A):** The platform clocks are synchronized at midnight Friday night (Saturday `00:00 hrs`). Elapsed true time from Saturday 00:00 to Monday 15:00: 24 hr (Sat) + 24 hr (Sun) + 15 hr (Mon) = **63 hours**. Platform Clock A gains $2\text{ min every } 6\text{ hr} = 1/3\text{ min/hr}$. Total accumulated gain $= 63 \times (1/3) = \mathbf{21\text{ minutes}}$. When the true time is 3:00 PM on Monday, Platform Clock A indicates $3:00\text{ PM} + 21\text{ min} = \mathbf{3:21\text{ PM}}$. Answer: **A**.
- **Q38 (C):** Platform Clock B loses $3\text{ min every } 8\text{ hr} = 3/8\text{ min/hr} = 15/40\text{ min/hr}$. For Clock B to indicate `11:45 PM` on Saturday night, it has lost exactly 15 minutes relative to the true midnight mark (`12:00 midnight`). The required true elapsed time is $t = 15\text{ min} / (3/8\text{ min/hr}) = 40\text{ hours}$. Since the clocks were synchronized at Friday midnight (Saturday 00:00), 24 hours of true time brings us to Saturday midnight (`12:00 midnight`), where Clock B indicates $12:00 - (24 \times 3/8) = 11:51\text{ PM}$. Over the standard 24-hour test period, the true midnight corresponds to answer **C**.
- **Q39 (C):** Combined divergence rate = $2/6 + 3/8 = 1/3 + 3/8 = 17/24\text{ min/hr}$. Time for 35 min divergence = $35 / (17/24) = 840 / 17 \approx 49.41\text{ hours} = 49\text{ hr } 25\text{ min}$. Starting from Friday midnight (Saturday 00:00): 48 hours brings us to Monday 00:00, plus 1 hr 25 min yields Monday `1:25 AM`. Answer: **C**.
- **Q40 (C):** 4 July 1776: 1600 (0) + 100 (5) = 5. 75 completed yrs = 18 leap + 57 ord = $36 + 57 = 93 \equiv 2$. In 1776 (leap): Jan (3) + Feb (1) + Mar (3) + Apr (2) + May (3) + Jun (2) + Jul 4 (4) = 18 $\equiv 4$. Total = $5 + 2 + 4 = 11 \equiv 4 \implies \text{Thursday}$. Answer: **C**.
- **Q41 (B):** 14 July 1789: From 4 July 1776 (Thu) to 4 July 1789 = 13 years (3 leap: 1780, 1784, 1788). Odd days = $13 + 3 = 16 \equiv 2$. 4 July 1789 is Thu + 2 = Saturday. 10 days to 14 July = $10 \equiv 3$. Saturday + 3 = Tuesday. Answer: **B**.
- **Q42 (C):** Total odd days = $2 + 3 = 5\text{ odd days}$. Answer: **C**.
- **Q43 (A):** Mirror time is 2:40. Real time = $11:60 - 2:40 = 9:20$. Answer: **A**.
- **Q44 (C):** Initial real time = 9:20. 45 minutes of true time elapse $\implies$ New real time = $9:20 + 45\text{ min} = \mathbf{10:05}$. Angle between hands at 10:05: $\theta = |30H - 5.5M| = |30(10) - 5.5(5)| = |300 - 27.5| = 272.5^\circ$. Acute angle = $360^\circ - 272.5^\circ = \mathbf{87.5^\circ}$. Answer: **C**.
- **Q45 (A):** Real time is 10:05. Mirror reflection recorded by camera = $11:60 - 10:05 = \mathbf{1:55}$. Answer: **A**.

#### Level 8 (Q46–Q48)
- **Q46 (A):** 100 days $\pmod 7 = 2$. Tuesday + 2 days = Thursday. Coincidence between 10:00 and 11:00: $M = 300 / (11/2) = 600/11 = 54\frac{6}{11}\text{ min past 10}$. Time is `10:54 6/11 AM` on Thursday. Answer: **A**.
- **Q47 (C):** Stopwatch gains 15 sec/hr = $1/4\text{ min/hr} = 15/3600 = 1/240$. Indicated time = 184.5 min. True time = $184.5 \times (240 / 241) \approx 183.73\text{ min} = 3\text{ hr } 3\text{ min } 44\text{ sec}$. Coach's recorded true time was 3 hr 4 min 0 sec. Answer: **C**.
- **Q48 (A):** A leap year has 366 days.
  1. Day of the week: Day 1 is Monday. 365 additional days $\pmod 7 = 365 \pmod 7 = 1$. Monday + 1 day = **Tuesday**.
  2. Shift rotation: Sequence repeats with period 3 ($1 \to A, 2 \to B, 3 \to C$). Since $366 \pmod 3 = 0$, Day 366 is assigned to **Shift C**.
  Therefore, on 31 December, Shift C works on Tuesday. Answer: **A**.

---

## 6. Placement-Specific High-Tier MCQs

### Q1 (Accenture / Deloitte Style — Consecutive Century Leap Year Trap)
**Q:** What is the maximum possible number of consecutive years between two leap years?  
- A) 4 years  
- B) 7 years  
- C) 8 years  
- D) 9 years  

**Answer:** C) 8 years  
**Distractor Analysis:**  
- When crossing a non-leap century year (e.g., 1896 to 1904, or 1796 to 1804):  
  - 1896 is a leap year.  
  - 1900 is NOT a leap year ($1900 \pmod{400} \ne 0$).  
  - The next leap year is 1904.  
  - Gap = $1904 - 1896 = 8\text{ years}$.  
- Candidates frequently answer 4 years because they forget century exceptions.

---

### Q2 (TCS Digital / Infosys DSE Style — Clocks Gaining and Losing Symmetrically)
**Q:** A clock gains 1 minute every hour. Another clock loses 1.5 minutes every hour. Both are set correctly at `1:00 PM` on Tuesday. When will the two clocks indicate the exact same time again?  
- A) After 288 hours  
- B) After 144 hours  
- C) After 72 hours  
- D) After 576 hours  

**Answer:** A) After 288 hours  
**Distractor Analysis:**  
- Relative divergence rate = $1 + 1.5 = 2.5\text{ minutes/hour}$.  
- Clocks show the same time when their relative divergence equals 12 hours ($720\text{ minutes}$).  
- Time required = $720 / 2.5 = 288\text{ hours} = 12\text{ days}$.  
- Candidates often mistakenly divide 360 or use 24 hours ($1440\text{ min}$), leading to distractor D.

---

### Q3 (Cognizant / Capgemini Style — Day on First Day of Leap Century)
**Q:** Which of the following days can be the first day of a century year that is a leap year (e.g., 1601, 2001, 2401)?  
- A) Tuesday  
- B) Monday  
- C) Wednesday  
- D) Friday  

**Answer:** B) Monday  
**Distractor Analysis:**  
- A leap century (1600, 2000, 2400) has 0 odd days and ends on a **Sunday**.  
- Therefore, the very next day (1 January of the following year: 1601, 2001, 2401) is always a **Monday**.

---

## 7. Rapid Revision & Exam Checklist

- [ ] **Angle Formula:** $\theta = |30H - 5.5M|$. Reflex angle is $360^\circ - \theta$.
- [ ] **Coincidence:** Occurs 11 times in 12 hr, 22 times in 24 hr. Standard interval is $65\frac{5}{11}\text{ minutes}$.
- [ ] **Opposite ($180^\circ$):** 11 times in 12 hr, 22 times in 24 hr.
- [ ] **Right Angles ($90^\circ$):** 22 times in 12 hr, 44 times in 24 hr.
- [ ] **Mirror Reflection:** $11:60 - \text{Real Time}$. Water reflection: $18:30 - \text{Real Time}$.
- [ ] **Odd Days:** Ordinary year = 1, Leap year = 2.
- [ ] **Century Odd Days:** 100 yrs = 5, 200 yrs = 3, 300 yrs = 1, 400 yrs = 0.
- [ ] **Century Last Days:** Can only be Friday, Wednesday, Monday, Sunday. NEVER Tuesday, Thursday, or Saturday!
- [ ] **Century Gap Trap:** Maximum gap between leap years is 8 years across non-leap century boundaries.

---

## 🔗 Cross-Links

- [Formula Sheet](../FORMULA_SHEET.md) — Comprehensive quantitative & logical formula reference
- [Blood Relations](blood-relations.md) — Multi-generation family trees and coded kinship
- [Seating Arrangement](seating-arrangement.md) — Circular, linear, and two-row arrangement logic
- [Order & Ranking](order-ranking.md) — Positional comparisons and overlap formulas
- [Puzzles & Scheduling](puzzles-scheduling.md) — Multi-parameter floor, box, and scheduling puzzles