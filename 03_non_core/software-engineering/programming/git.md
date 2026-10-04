# 🔀 Git & GitHub for Civil Engineering

> **Tag:** `[MUST LEARN]` for all technical/research roles, `[HIGH ROI]` for every role | **Target Level:** L2 minimum, L3 recommended
> **Time to L2:** 5–8 hours | **Time to L3:** 15–20 hours

---

## What is it?

Git is a distributed version control system that tracks changes to files over time. GitHub is a cloud platform for hosting Git repositories, enabling collaboration, code review, and project portfolio hosting.

## Why is it used?

- Track changes to code, documents, and project files
- Collaborate with teams without overwriting each other's work
- Host your project portfolio for recruiters and interviewers
- Demonstrate technical competence even in non-coding roles
- Standard tool in every tech and research environment
- Enables reproducible research workflows

## Civil Engineering Applications

| Application | Branch | Context |
|:------------|:-------|:--------|
| Version control for research code | Research / CFD | Track solver modifications, scripts |
| Portfolio hosting | All | Showcase projects to recruiters |
| Collaborative project documentation | Construction / PM | Team-based project files |
| Script and automation management | All | Track Python/MATLAB scripts |
| Configuration file management | CFD / OpenFOAM | Track case setups and parameters |
| Reproducible workflows | All | Ensure research can be replicated |

## Relevant Branches

- [x] All branches — Git is universal

## Relevant Job Roles

| Role | Required? | Proficiency Needed |
|:-----|:----------|:-------------------|
| CFD / Simulation Engineer | Essential | L3 |
| Research / R&D | Essential | L3 |
| Data Analyst | Essential | L2–L3 |
| Business Analyst | Useful | L2 |
| Product roles | Useful | L2 |
| Core Civil roles | Useful | L1–L2 |
| Consulting | Useful | L1–L2 |

## Required Prerequisites

```
Must know:
- Command line basics (cd, ls, mkdir)
- A text editor (VS Code recommended)
- A GitHub account
```

## Core Features to Learn

### Must-know (L2)

```
1. git init — Initialize a repository
2. git add — Stage changes
3. git commit — Save changes with a message
4. git status — Check what's changed
5. git log — View commit history
6. git push — Upload to remote (GitHub)
7. git pull — Download from remote
8. git clone — Copy a remote repository
9. .gitignore — Exclude files from tracking
10. README.md — Project documentation
```

### Important (L2–L3)

```
11. git branch — Create/switch branches
12. git merge — Combine branches
13. git stash — Temporarily save changes
14. Pull requests (PR) — Code review workflow
15. Issues — Bug tracking and task management
16. git diff — See what changed
17. git checkout / git switch — Branch management
18. Remote management (origin, upstream)
```

### Advanced (L3+)

```
19. git rebase — Clean commit history
20. git cherry-pick — Select specific commits
21. Git tags — Mark releases
22. GitHub Actions — Basic CI/CD
23. Branch protection rules
24. Forking workflow (for open-source contribution)
```

## What NOT to Waste Time Learning

```
Do NOT spend time on:
- Advanced Git internals (pack files, refs)
- Complex rebase workflows
- GitHub Actions for deployment
- Git hooks (unless automating workflows)
- Submodules (unless managing large dependencies)
```

## Typical Workflow

```
Step 1: Create — git init + create files
Step 2: Stage — git add .
Step 3: Commit — git commit -m "Add initial project structure"
Step 4: Connect — git remote add origin [URL]
Step 5: Push — git push -u origin main
Step 6: Iterate — modify → add → commit → push
Step 7: Branch — git checkout -b feature-name (for new features)
Step 8: Merge — git checkout main && git merge feature-name
Step 9: PR — Create pull request on GitHub for review
```

## Example Project: Engineering Portfolio Repository

```
Project: Personal Engineering Portfolio on GitHub
Objective: Showcase 5 engineering projects with code, documentation, and results
Tools: Git, GitHub, VS Code, Markdown
Workflow:
    1. Create GitHub repository with README.md
    2. Organize: /project-1/, /project-2/, etc.
    3. Each project folder: code/, data/, results/, README.md
    4. Commit and push after each project completion
    5. Add badges, screenshots, and descriptions to README
    6. Share repository link on resume
Expected Output: Professional GitHub profile with 5+ documented projects
Portfolio Value: Very high — recruiters check GitHub
Interview Relevance: "Show me your work" → link to portfolio
```

## README Template for Projects

```markdown
# Project Name

## Objective
[One paragraph: what problem you're solving]

## Tools Used
- Python, Pandas, Matplotlib (list your stack)

## Workflow
1. Data collection
2. Processing
3. Analysis
4. Visualization

## Results
[Screenshot or description of output]

## How to Run
1. pip install -r requirements.txt
2. python main.py

## Interview Relevance
- Demonstrates: [skill 1], [skill 2]
- Discusses: [topic in interview]
```

## Resume Value

```
❌ Bad:  "Proficient in Git"
❌ Bad:  "Used GitHub for version control"
✅ Good: "Maintained GitHub portfolio with 5 documented engineering projects,
         including automated hydraulic analysis pipeline and GIS flood mapping,
         demonstrating version control, documentation, and reproducible workflows"
```

## Interview Questions

### Basic (101)
- What is version control? Why is it important?
- What is the difference between `git pull` and `git fetch`?
- What is a commit?

### Practical (201)
- How do you resolve a merge conflict?
- What is a branch? When would you create one?
- How do you undo the last commit?
- What is a pull request?

### Technical (301)
- What is the difference between `git merge` and `git rebase`?
- What is a detached HEAD state? How do you recover?
- How does Git store data internally? (briefly)

### Project Defense
- Show me your GitHub repository.
- How do you organize your projects?
- What's your commit message convention?

## Common Mistakes

| Mistake | Why It's Wrong | Correct Approach |
|:--------|:---------------|:-----------------|
| Committing large data files | Repository becomes huge | Use .gitignore or Git LFS |
| Committing with message "update" | Uninformative history | Write descriptive commit messages |
| Not using .gitignore | Credentials, temp files get tracked | Always use .gitignore |
| Working only on main branch | Risk of breaking working code | Use feature branches |
| Not committing regularly | Large, untraceable changes | Commit every logical change |

## Learning Roadmap

```
Beginner (0–5 hrs):
    → GitHub Skills (interactive, free)
    → git init, add, commit, push
    → Create your first repository

Intermediate (5–15 hrs):
    → Branches, merges, pull requests
    → README.md documentation
    → .gitignore setup
    → Create a portfolio repository

Advanced (15–20 hrs):
    → Collaborative workflows
    → Branch protection, code review
    → GitHub Pages (optional)
```

## Quick Reference Card

| Property | Value |
|:---------|:------|
| **Type** | Version control system |
| **Developer** | Linus Torvalds / GitHub (Microsoft) |
| **License** | Open-source (GPLv2) |
| **Platform** | Windows, Linux, macOS |
| **Difficulty** | Easy to start |
| **Time to L2** | 5–8 hours |
| **Time to L3** | 15–20 hours |
| **Primary use** | Version control, collaboration, portfolio |
| **Main platform** | GitHub, GitLab, Bitbucket |

---

*See also: [`python.md`](python.md), [`c-cpp.md`](c-cpp.md) for language-specific Git workflows.*
