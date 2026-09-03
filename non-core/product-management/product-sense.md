# Product Sense — Design & Improvement Questions

> Master "Design X", "Improve Y", and product thinking questions with frameworks, examples, and practice.

---

## The Core Framework: User → Need → Solution

```
1. WHO — Define the user
   - Primary user segment
   - Context / use case
   - User characteristics

2. WHAT — Define the need
   - Problem statement
   - Current alternatives
   - Pain points
   - Jobs to be done

3. HOW — Define the solution
   - Core features (MVP)
   - Differentiation
   - Trade-offs
   - Constraints

4. SUCCESS — Define metrics
   - How to measure impact
   - Key metrics to track
   - Guardrail metrics
```

---

## Question Type 1: "Design X"

**Example:** "Design a mobile app for college students to find study groups."

### Sample Answer Structure

**1. Clarify (30 sec)**
> "Before I design, let me clarify a few things. Is this for a specific college or general? What's the primary goal — helping students find groups, or improving study outcomes? Who's the primary user — freshmen or all students?"

**2. User (1 min)**
> "The primary user is a college student who wants to study with peers but doesn't know who's studying the same subject. Secondary users are TAs and professors who want to facilitate group learning."

**3. Need (1 min)**
> "The core need is discovery — finding compatible study partners. Pain points: no central place to find study groups, difficulty coordinating schedules, fear of joining the wrong group. Current alternatives: WhatsApp groups, word of mouth — both fragmented."

**4. Solution (2 min)**
> "MVP features:
> 1. Create/join study groups by subject and course
> 2. Schedule matching (find groups that fit your timetable)
> 3. Group chat and file sharing
> 4. Study session scheduling with reminders
>
> Differentiation: schedule-based matching (unique vs. generic group apps). Trade-off: simplicity vs. feature richness — start with core discovery + scheduling."

**5. Metrics (1 min)**
> "Success metrics:
> - North Star: Weekly active study groups
> - Supporting: Group creation rate, join rate, session attendance
> - Guardrail: Drop-off after joining, spam reports"

**6. Recommendation (30 sec)**
> "I'd launch an MVP focused on discovery + scheduling, measure group activity, and iterate based on what drives retention."

---

## Question Type 2: "Improve X"

**Example:** "How would you improve WhatsApp?"

### Sample Answer Structure

**1. Understand current state**
> "WhatsApp's core value is reliable, private communication. Current users: 2B+ globally. Key features: messaging, calls, status, groups."

**2. Identify improvement areas**
> "I'd focus on three areas:
> 1. **Group management** — large groups are chaotic (no threading, hard to find info)
> 2. **Business communication** — businesses use WhatsApp but lack tools
> 3. **Information overload** — important messages get lost"

**3. Prioritize**
> "I'd prioritize group management because it affects the most users and has clear pain points."

**4. Solution**
> "Add message threading within groups, pin important messages, and smart filters (unread, mentions, media)."

**5. Metrics**
> "Measure: group engagement, time-to-find-information, message read rate. Guardrail: don't increase complexity for casual users."

---

## Question Type 3: "Design for a Specific User"

**Example:** "Design a product for elderly users to manage medications."

**Framework:**
1. **User:** Elderly (65+), may have limited tech literacy, vision issues
2. **Need:** Remember to take medications, track doses, avoid errors
3. **Solution:** Voice-first interface, large text, simple reminders, family sharing
4. **Metrics:** Medication adherence rate, error reduction, family engagement

---

## Question Type 4: "Prioritize Features"

**Example:** "You have 3 features and time for 1. Which do you build?"

**Framework: RICE**
```
RICE Score = (Reach × Impact × Confidence) / Effort

Reach: How many users affected?
Impact: How much impact per user? (0.25-3)
Confidence: How sure are you? (50-100%)
Effort: Person-months
```

**Example:**
| Feature | Reach | Impact | Confidence | Effort | RICE |
|:--------|:-----:|:------:|:----------:|:------:|:----:|
| A: Onboarding | 10,000 | 3 | 80% | 2 | 12,000 |
| B: New theme | 50,000 | 1 | 90% | 1 | 45,000 |
| C: Search | 20,000 | 2 | 70% | 3 | 9,333 |

**Decision:** Feature B (highest RICE) — but consider strategic priorities too.

---

## Question Type 5: "Metrics"

**Example:** "What metrics would you track for a music streaming app?"

**Framework: AARRR (Pirate Metrics)**
```
Acquisition: How users find the app
  - Downloads, installs, signups

Activation: First meaningful experience
  - First song played, playlist created

Retention: Users keep coming back
  - DAU/MAU, weekly retention, churn

Revenue: Monetization
  - ARPU, subscription conversion, ad revenue

Referral: Users bring users
  - Invites sent, referral conversion
```

**North Star Metric:** Weekly active listeners (captures engagement + retention)

---

## Common Mistakes

| Mistake | Why It's Bad | Fix |
|:--------|:-------------|:----|
| Jumping to solution without user | Shows no user empathy | Always start with WHO |
| Too many features | Unrealistic, unfocused | Focus on MVP |
| No metrics | Can't measure success | Always define success metrics |
| Ignoring trade-offs | Unrealistic | Acknowledge constraints |
| Not clarifying | Assumes wrong scope | Ask clarifying questions first |
| Generic answers | No differentiation | Make it specific to the product |

---

## Practice Questions (20)

1. Design a feature for a food delivery app.
2. How would you improve Instagram Reels?
3. Design a product for remote workers.
4. How would you improve the checkout flow of an e-commerce app?
5. Design a fitness app for beginners.
6. How would you improve Google Maps?
7. Design a product for first-time home buyers.
8. How would you improve LinkedIn's job search?
9. Design a payment app for small businesses.
10. How would you improve a ride-hailing app?
11. Design a study app for GATE aspirants.
12. How would you improve YouTube's recommendation?
13. Design a product for urban commuters.
14. How would you improve a banking app?
15. Design a health tracking app for chronic patients.
16. How would you improve a hotel booking app?
17. Design a product for event organizers.
18. How would you improve a news app?
19. Design a collaboration tool for students.
20. How would you improve a grocery delivery app?

---

## Practice Method

1. **Pick a question** from the list
2. **Time yourself** (5 minutes for full answer)
3. **Follow the framework:** User → Need → Solution → Metrics
4. **Record** your answer
5. **Review** against the sample structure
6. **Identify gaps** and redo

---

## Cross-Links

| Resource | Link |
|:---------|:-----|
| PM Overview | [pm-overview.md](pm-overview.md) |
| Metrics & Strategy | [pm-metrics-strategy.md](pm-metrics-strategy.md) |
| Interview Frameworks | [interview-frameworks.md](../common/interview-frameworks.md) |

---

*Product sense is not about having the "right" answer — it's about showing structured, user-centered thinking.*
