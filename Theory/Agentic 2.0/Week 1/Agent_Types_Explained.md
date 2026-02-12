# AI Agent Types Explained

This document explains the three foundational agent types covered in Colab Notebooks 1-3.

---

## 1. Reflex Agents (Notebook 1)

Reflex agents are the **most fundamental type of AI agent**—they react immediately to their environment without planning or memory.

### Core Concept

Reflex agents use **Condition-Action Rules** (If-Then logic):
- **Perceive** the current state → **Execute** a pre-assigned action
- No planning, no future simulation—purely reactive

### The Vacuum World Scenario

The notebook uses a classic 2-room vacuum cleaner example (rooms A and B) to demonstrate two agent types:

#### Simple Reflex Agent

| Condition | Action |
|-----------|--------|
| Room is dirty | Clean it (`Suction on`) |
| Room A is clean | Move `Right` to B |
| Room B is clean | Move `Left` to A |

**Problem**: No memory. If both rooms are clean, it oscillates forever between them—it can't remember that both are already done.

#### Model-Based Reflex Agent

Adds an **internal model** (dictionary) that tracks the state of both rooms:

```python
self.model = {'A': 'Unknown', 'B': 'Unknown'}
```

**Key improvement**: Before acting, it checks its world model. If both rooms are marked `'Clean'`, it returns `"NoOp (Job Done)"` and stops.

### Key Takeaway

> Even without explicit planning, **adding memory/state** enables much smarter behavior.

This is the foundation for more advanced agents:
- **Goal-based agents** → plan to achieve objectives
- **Utility-based agents** → optimize for efficiency/preferences

---

## 2. Goal-Based Agents (Notebook 2)

This notebook builds on the reflex agent concept by introducing **planning**—the agent thinks through the entire problem before taking a single step.

### Key Distinction from Reflex Agents

| Agent Type | Approach |
|------------|----------|
| **Reflex** | "I'm not at the goal. Move Right." (repeat 100× reactively) |
| **Goal-Based** | "To reach (4,4), I need 4 Down + 4 Right. Here's my complete plan." |

### The Scenario: 2D Grid Navigation

An agent `A` at position `(0,0)` must reach goal `G` at position `(4,4)` on a 5×5 grid.

### How It Works

**1. Perceive** → Get current position  
**2. Formulate Goal** → Define target coordinates  
**3. Formulate Plan** → Calculate the full action sequence *before* moving:
```python
diff_row = goal[0] - start[0]  # 4 Down moves
diff_col = goal[1] - start[1]  # 4 Right moves
plan = ["Down", "Down", "Down", "Down", "Right", "Right", "Right", "Right"]
```
**4. Execute** → Run through the plan step-by-step

### Key Concepts Demonstrated

| Concept | Description |
|---------|-------------|
| **Planning Before Acting** | Generates the complete action sequence before moving |
| **Explicit Goal** | Defines exactly what "success" looks like |
| **Open-Loop Execution** | Executes the plan blindly—assumes the world won't change |
| **World Representation** | Uses coordinate math as a simple heuristic |

### Limitation

This is **open-loop control**—if an obstacle appears mid-execution, the agent would crash because it doesn't re-check sensors while moving. More advanced agents would use **closed-loop** control with continuous feedback.

---

## 3. Utility-Based Agents (Notebook 3)

This notebook advances from goal-based agents to agents that evaluate **which path is best**, not just whether a goal is reachable.

### The Key Question

| Agent Type | Question Asked |
|------------|----------------|
| Goal-Based | "Can I reach the goal?" |
| **Utility-Based** | "Which path to the goal is *best*?" |

### The Scenario: Route Selection

Three routes to a destination, each with different trade-offs:

| Route | Time | Cost | Safety | View |
|-------|------|------|--------|------|
| Highway | 20 min | $15 | 8/10 | 2/10 |
| Back Roads | 45 min | $0 | 6/10 | 9/10 |
| City Center | 30 min | $5 | 4/10 | 5/10 |

### The Utility Function

The agent's "personality" is encoded as **weights**—how much it cares about each factor:

$$U(s) = w_1 f_1 + w_2 f_2 + w_3 f_3 + ...$$

- **Negative weights** → minimize that factor (time, cost)
- **Positive weights** → maximize that factor (safety, view)

### Two Agents, Same Options, Different Choices

| Agent | Weights | Choice |
|-------|---------|--------|
| **Business Executive** | time: -2.0, cost: -0.1, safety: 2.0, view: 0.0 | **Highway** (fast & safe) |
| **Broke Student** | time: -0.1, cost: -5.0, safety: 1.0, view: 2.0 | **Back Roads** (free & scenic) |

Both agents are **rational**—they're optimizing for their own utility function.

### Key Takeaways

1. **Rational ≠ Identical** — Two agents can make opposite choices and both be correct
2. **Explicit Preferences** — The utility function makes priorities transparent and tunable
3. **Scalable** — Reduces complex multi-attribute decisions to a single comparable score

This is foundational for AI alignment—defining *what* an agent should optimize for.

---

## Summary: Agent Evolution

| Agent Type | Memory | Planning | Optimization |
|------------|--------|----------|--------------|
| Simple Reflex | ❌ | ❌ | ❌ |
| Model-Based Reflex | ✅ | ❌ | ❌ |
| Goal-Based | ✅ | ✅ | ❌ |
| Utility-Based | ✅ | ✅ | ✅ |

Each agent type builds on the previous, adding more sophisticated decision-making capabilities.
