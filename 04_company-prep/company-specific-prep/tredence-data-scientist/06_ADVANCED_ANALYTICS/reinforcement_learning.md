# Reinforcement Learning & Multi-Armed Bandits for Business Optimization

**Target Role:** Data Scientist / Associate Data Scientist | Tredence Analytics  
**Context:** IIT Kanpur Placement Season 2026–27  
**Prerequisites:** Markov Chains, Dynamic Programming, Probability Theory

---

## 1. Markov Decision Processes (MDP)

An MDP is a formal mathematical framework for modeling decision-making under uncertainty where outcomes are partly random and partly under the control of a decision maker.

$$\text{MDP Tuple: } (\mathcal{S}, \mathcal{A}, \mathcal{P}, \mathcal{R}, \gamma)$$

- $\mathcal{S}$: Set of valid environmental states.
- $\mathcal{A}$: Set of available actions.
- $\mathcal{P}(s' \mid s, a) = P(S_{t+1} = s' \mid S_t = s, A_t = a)$: State transition probability.
- $\mathcal{R}(s, a, s') = \mathbb{E}[R_{t+1} \mid S_t = s, A_t = a, S_{t+1} = s']$: Reward function.
- $\gamma \in [0, 1)$: Temporal discount factor (prioritizes immediate vs delayed rewards).

### 1.1 The Discounted Return
$$G_t = \sum_{k=0}^\infty \gamma^k R_{t+k+1} = R_{t+1} + \gamma G_{t+1}$$

---

## 2. Bellman Expectation & Optimality Equations

### 2.1 State-Value Function $V^\pi(s)$ & Action-Value Function $Q^\pi(s, a)$
- **$V^\pi(s)$:** Expected return starting from state $s$ following policy $\pi$:
  $$V^\pi(s) = \sum_{a \in \mathcal{A}} \pi(a \mid s) \sum_{s', r} \mathcal{P}(s', r \mid s, a) \left[ r + \gamma V^\pi(s') \right]$$
- **$Q^\pi(s, a)$:** Expected return starting from state $s$, taking action $a$, and thereafter following policy $\pi$:
  $$Q^\pi(s, a) = \sum_{s', r} \mathcal{P}(s', r \mid s, a) \left[ r + \gamma \sum_{a'} \pi(a' \mid s') Q^\pi(s', a') \right]$$

### 2.2 Bellman Optimality Equation for $Q^*(s, a)$
$$Q^*(s, a) = \sum_{s', r} \mathcal{P}(s', r \mid s, a) \left[ r + \gamma \max_{a'} Q^*(s', a') \right]$$
The optimal policy selects the action that greedily maximizes $Q^*(s, a)$: $\pi^*(s) = \arg\max_a Q^*(s, a)$.

---

## 3. Model-Free Reinforcement Learning

When environmental transition dynamics $\mathcal{P}$ and rewards $\mathcal{R}$ are unknown, the agent learns directly from experience.

### 3.1 Q-Learning (Off-Policy Temporal Difference Control)
Updates action-values using the greedy maximum over next-state actions, independent of the policy followed to generate the experience:

$$Q(S_t, A_t) \leftarrow Q(S_t, A_t) + \alpha \left[ R_{t+1} + \gamma \max_a Q(S_{t+1}, a) - Q(S_t, A_t) \right]$$

### 3.2 Deep Q-Networks (DQN - Mnih et al., DeepMind 2015)
Replaces lookup table $Q(s, a)$ with a deep neural network $Q(s, a; \theta)$.

**Two Stability Breakthroughs:**
1. **Experience Replay Buffer $\mathcal{D}$:** Stores transitions $(s_t, a_t, r_{t+1}, s_{t+1})$. Mini-batches are sampled uniformly at random during training, breaking autocorrelation between consecutive states and stabilizing gradient descent.
2. **Target Network $\theta^-$:** Uses a slowly updated copy of weights $\theta^-$ to calculate target values:
   $$y_t = R_{t+1} + \gamma \max_{a'} Q(S_{t+1}, a'; \theta^-)$$
   Loss: $\mathcal{L}(\theta) = \mathbb{E}\left[ (y_t - Q(S_t, A_t; \theta))^2 \right]$. Prevents chasing a non-stationary moving target.

---

## 4. Multi-Armed Bandits (MAB) for Business Decision Systems

A simplified single-state MDP ($|\mathcal{S}| = 1, \gamma = 0$) balancing **Exploitation** (reaping rewards from best-known option) vs **Exploration** (discovering unknown options).

```
                            Exploration vs Exploitation
 ┌───────────────────────────────┼───────────────────────────────┐
 │                               │                               │
ε-Greedy Strategy             UCB1 Algorithm              Thompson Sampling
 ├── Random uniform               ├── Deterministic optimism       ├── Bayesian posterior
 │   exploration                  │   in face of uncertainty       │   probability sampling
 └── Simple, but wastes           └── Optimal logarithmic          └── Industry standard for
     traffic on bad arms              regret O(ln T)                   A/B/n and ad ranking
```

### 4.1 Upper Confidence Bound (UCB1)
Selects arm $a$ that maximizes empirical mean plus an uncertainty bonus:

$$A_t = \arg\max_{a} \left[ \hat{\mu}_a + \sqrt{\frac{2 \ln t}{N_a(t)}} \right]$$
- $\hat{\mu}_a$: Current sample average reward of arm $a$.
- $N_a(t)$: Number of times arm $a$ has been pulled so far.
- $t$: Total time steps. Unexplored arms receive high uncertainty bonuses.

### 4.2 Thompson Sampling (Posterior Sampling)
For binary conversion outcomes (Click / No-Click):
1. Maintain prior distribution $\text{Beta}(\alpha_a, \beta_a)$ for each arm $a$.
2. At each decision step $t$, draw sample $\theta_a \sim \text{Beta}(\alpha_a, \beta_a)$ for all arms.
3. Select arm with highest sampled value: $A_t = \arg\max_a \theta_a$.
4. Observe outcome $r \in \{0, 1\}$. Update posterior:
   $$\alpha_a \leftarrow \alpha_a + r, \quad \beta_a \leftarrow \beta_a + (1 - r)$$
- Highly effective in production: naturally allocates traffic away from poorly performing variants without rigid A/B test sample size delays.

---

## 5. Enterprise Applications in Tredence Verticals

1. **Dynamic Markdown & Clearance Pricing:**
   - State: Days remaining until season end, current inventory depth, competitor price.
   - Action: Price discount tier ($0\%, 10\%, 20\%, 35\%$).
   - Reward: Gross margin revenue minus inventory carrying cost.
2. **Contextual Promotional Personalization:**
   - Contextual Bandits tailor promotional discount depth per user session based on real-time device, cart value, and browsing velocity.
3. **Automated Warehouse Inventory Replenishment:**
   - Multi-echelon stock replenishment policy learning under stochastic demand spikes and supplier lead-time delays.
