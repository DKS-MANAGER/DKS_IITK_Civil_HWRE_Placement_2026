# ⚖️ Integrity & Judgment Stories — Personalized Story Bank

> **How to use:** Each story below is a **template**. Replace bracketed items `[YOUR DETAILS]` with YOUR actual experiences. Keep the STAR structure. Time each story to 60-90 seconds when spoken aloud.

---

## Story Categories & Question Mapping

| Story | Covers These Interview Questions |
|-------|----------------------------------|
| Story 1 | "Tell me about an ethical decision you made" |
| Story 2 | "Describe a time you challenged the status quo" |
| Story 3 | "What would you do if a team member took credit for your work?" |
| Story 4 | "Tell me about a time you had to say no" |
| Story 5 | "How do you handle conflicts of interest?" |
| Story 6 | "Describe a time you maintained standards under pressure" |
| Story 7 | "What would you do if you found an error in published work?" |
| Story 8 | "Tell me about making a decision you weren't comfortable with" |
| Story 9 | "How do you handle confidential information?" |
| Story 10 | "Describe a time you admitted you were wrong" |

---

## 📝 Story 1: Data Integrity Under Pressure

**Situation:**
A team member at IIT Kanpur suggested "smoothing" some outlier data points in our CFD validation to improve the match with experimental data, saying "everyone does it" in their field.

**Task:**
Uphold research integrity without accusing the team member of misconduct or creating conflict.

**Action:**
1. Stated my principle calmly: "I'm not comfortable modifying data. Our credibility depends on transparency."
2. Explored alternatives together: "What if we analyze why those points are outliers? Could be a mesh issue, boundary condition, or a real physical phenomenon."
3. Investigated together — found the outliers corresponded to a known flow separation region where our turbulence model has documented limitations
4. Improved the approach — added a "limitations" section discussing the separation region, cited literature on model limitations there
5. Kept original data intact, added analysis of outliers as a feature, not a bug

**Result:**
Paper accepted with reviewer comment: "Appreciate the honest discussion of model limitations." The team member later thanked me for the principled stance. Integrity + curiosity > compliance.

⏱️ **Target time: 75 seconds**

---

## 📝 Story 2: Challenging Outdated Practices

**Situation:**
Our lab at IIT Kanpur had been using a deprecated OpenFOAM version (v1912) for all simulations, despite v2412 being available with significant bug fixes, new solvers, and better performance. Everyone accepted it because "that's how it's always been."

**Task:**
Challenge the status quo with evidence-based reasoning.

**Action:**
1. Documented benefits — bug fixes relevant to our work, new solver features, performance benchmarks on our typical cases
2. Tested compatibility — ran 3 existing lab cases on the new version to verify backward compatibility
3. Created a migration guide — step-by-step upgrade instructions with common issues and fixes
4. Presented to lab head — showed data: 30% stability improvement, 2 new solvers enabling previously impossible simulations
5. Offered to lead — "I'll handle the upgrade and support the team during transition"

**Result:**
Lab upgraded within 2 weeks. Stability improved by 30%. 3 new case types became possible. Challenging the status quo requires evidence, preparation, and willingness to own the implementation — not just pointing out problems.

⏱️ **Target time: 75 seconds**

---

## 📝 Story 3: Handling Credit Disputes

**Situation:**
During a collaborative project at IIT Kanpur, I noticed that one team member was presenting our joint results as primarily their work in group meetings, minimizing my contributions.

**Task:**
Address the credit imbalance without creating conflict or appearing petty.

**Action:**
1. Had a private conversation — "I noticed in the meeting that the results section was presented as your work. Our contributions were actually quite equal — I handled the meshing and validation, you handled the solver setup. Can we present this more accurately?"
2. Suggested a structural solution — "Let's use a contribution log so everyone's work is visible"
3. Created a shared document where each member logged their daily contributions
4. Suggested to the team lead that we present results with clear attribution in the next meeting
5. Focused on the process, not the person — "This helps all of us get recognized fairly"

**Result:**
The contribution log was adopted by the team. Credit was properly attributed going forward. The teammate thanked me for addressing it directly rather than letting it fester. Prevention through transparent processes beats confrontation.

⏱️ **Target time: 75 seconds**

---

## 📝 Story 4: Saying No with Integrity

**Situation:**
A friend at IIT Kanpur asked me to share my thesis code before publication, saying they needed it urgently for their own project deadline.

**Task:**
Protect our publication priority while preserving the friendship.

**Action:**
1. Acknowledged the need: "I understand you need this for your project, and I want to help"
2. Explained honestly: "Premature sharing could compromise our publication priority. I hope you understand."
3. Offered meaningful alternatives: "I can share the methodology document, help you build your own case setup step-by-step, and we can discuss the approach in detail"
4. Followed up: Checked on their project progress weekly and offered additional guidance

**Result:**
The friend built their own simulation successfully. Our relationship stayed strong — they actually appreciated the honesty. Saying no with a helpful alternative maintains relationships while protecting commitments.

⏱️ **Target time: 60 seconds**

---

## 📝 Story 5: Navigating Conflicting Interests

**Situation:**
During placement prep at IIT Kanpur, a senior offered to refer me to their company — but only if I helped them with their thesis data analysis on the side. The request was reasonable but felt transactional.

**Task:**
Navigate the situation without compromising my values or losing the referral opportunity.

**Action:**
1. Offered to help genuinely — "I'm happy to help with your data analysis because it's a learning opportunity, not as a condition"
2. Helped with the data analysis on my own terms — spent 3 hours teaching them Python techniques they could reuse
3. Let the referral happen naturally — they offered it after seeing the quality of help
4. Maintained the relationship on professional terms — connected on LinkedIn, stayed in touch

**Result:**
Got the referral and the interview. The senior became a valuable professional contact. I learned that helping people genuinely — without transactional framing — creates better outcomes than conditional exchanges.

⏱️ **Target time: 60 seconds**

---

## 📝 Story 6: Maintaining Quality Under Deadline Pressure

**Situation:**
Two days before a conference paper deadline at IIT Kanpur, a co-author wanted to submit with known minor issues in the validation section, arguing "perfect is the enemy of done."

**Task:**
Maintain quality standards while meeting the deadline and preserving the co-author relationship.

**Action:**
1. Quantified the risk objectively: "The validation gap could lead to reviewer rejection. Fixing it takes ~8 hours. Rejection means 3-month delay."
2. Proposed a compromise: "I'll fix the validation tonight (4 hours). You handle formatting and references. We submit by tomorrow noon."
3. Divided labor clearly — I fixed validation, co-author handled references, figures, and submission logistics
4. Set a quality gate: "If validation fix takes >6 hours, we submit as-is with a note to reviewers"
5. Executed the plan — validation fixed in 5 hours, paper submitted on time

**Result:**
Paper accepted with minor revisions. Co-author thanked me for the push. Quantifying risk makes quality arguments objective, not personal. The deadline can be met AND quality can be maintained with smart planning.

⏱️ **Target time: 75 seconds**

---

## 📝 Story 7: Catching an Error Before Publication

**Situation:**
Before submitting our CFD results for journal publication at IIT Kanpur, I noticed inconsistencies in the validation data — 2 minor calculation errors in drag coefficient and 1 missing mesh independence plot.

**Task:**
Ensure accuracy without delaying the submission or damaging team morale.

**Action:**
1. Created a validation checklist — mesh independence, residual convergence, BC verification, y+ compliance
2. Audited independently — re-ran 3 key cases from scratch, cross-checked all values against raw data
3. Found and documented the issues with specific evidence
4. Assigned fixes to responsible members with a 24-hour deadline — collaborative, not accusatory
5. Verified all corrections personally before submission

**Result:**
Paper passed peer review without data-related comments. The validation checklist became mandatory for all lab publications. Catching errors early prevents public embarrassment — systematic quality gates are investments, not overhead.

⏱️ **Target time: 60 seconds**

---

## 📝 Story 8: Disagreeing with a Supervisor's Approach

**Situation:**
My thesis supervisor at IIT Kanpur suggested changing my validation approach from Grid Convergence Index (GCI) to a simpler Richardson extrapolation, saying GCI was "overkill" for our study.

**Task:**
Respectfully advocate for my methodological choice while respecting the supervisor's experience.

**Action:**
1. Respected hierarchy — requested a meeting: "I'd like to discuss the validation approach"
2. Prepared evidence — ASME V&V 20 standard recommending GCI, 3 recent journal papers in our field using GCI
3. Showed concrete difference — Richardson gave 15% different result on our test case
4. Acknowledged validity — agreed that for quick internal checks, Richardson is faster
5. Proposed compromise — GCI for final publication results, Richardson for intermediate checks

**Result:**
Supervisor agreed to GCI for final results. The compromise saved ~20 hours of computation during development. Paper was accepted with reviewer praise for rigorous validation. Evidence + flexibility wins respect.

⏱️ **Target time: 75 seconds**

---

## 📝 Story 9: Handling Confidential Information

**Situation:**
During placement prep at IIT Kanpur, a friend shared company-specific interview questions from their earlier interview experience, asking me not to share them. Another friend asked me for the same information.

**Task:**
Protect the confidentiality of the shared information while navigating the social pressure.

**Action:**
1. Respected the trust — didn't share the specific questions
2. Explained to the requesting friend: "I was given this in confidence. I can't share the exact questions, but I can help you prepare for similar topics."
3. Helped without breaking trust — created a study plan covering the same topic areas without revealing specific questions
4. Encouraged them to find their own sources — connected them with another senior who might help

**Result:**
Maintained trust with the original friend. Helped the requesting friend prepare effectively. Built a reputation for being trustworthy — more seniors shared resources with me because they knew I'd respect confidentiality.

⏱️ **Target time: 60 seconds**

---

## 📝 Story 10: Admitting a Mistake

**Situation:**
During a group project at IIT Kanpur, I confidently recommended a mesh refinement strategy that turned out to be incorrect — it increased computational cost without improving accuracy.

**Task:**
Acknowledge the mistake and course-correct without damaging team confidence.

**Action:**
1. Owned it immediately: "My mesh refinement recommendation was wrong. The finer mesh didn't improve results — I should have tested first."
2. Analyzed why: "I assumed finer mesh = better results, but for this flow regime, the original mesh was already converged"
3. Proposed a fix: "Let me run a proper mesh sensitivity study with 3 levels and use GCI to find the optimal mesh"
4. Completed the study — found the optimal mesh was actually coarser than our original, saving 40% computation time
5. Documented the lesson — added "Always test mesh sensitivity before recommending refinement" to our project checklist

**Result:**
Team saved 40% computation time on remaining simulations. The mesh sensitivity protocol was adopted by the team. Admitting mistakes quickly, analyzing why, and fixing them builds more trust than pretending you're always right.

⏱️ **Target time: 75 seconds**

---

## 🔗 Cross-Links

- [`../conflict_resolution/conflict-resolution.md`](../conflict_resolution/conflict-resolution.md) — 10 conflict resolution stories
- [`../behavioral-interview-guide.md`](../behavioral-interview-guide.md) — STAR framework reference
- [`../question-master-database.md`](../question-master-database.md) — All integrity/judgment questions
- [`../strategies/answering-strategies.md`](../strategies/answering-strategies.md) — SOAR framework for ethical questions

---

## References

* [awesome-behavioral-interviews](https://github.com/arialdomartini/awesome-behavioral-interviews)
* [behavioral-interview-list-of-questions](https://github.com/rShearer/behavioral-interview-list-of-questions)
