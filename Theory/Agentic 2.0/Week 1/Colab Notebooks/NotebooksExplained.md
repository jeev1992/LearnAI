# Agentic AI 2.0 - Week 1: Notebook Explanations

This document provides detailed explanations of all six Colab notebooks in the Agentic AI 2.0 Week 1 curriculum. The notebooks progressively build your understanding from basic reflex agents to practical LLM-powered agents.

Each section includes a **step-by-step code walkthrough** showing exactly what happens at each line and iteration, so you can trace the execution yourself.

---

## Table of Contents

1. [Reflex Agents](#1-reflex-agents)
2. [Goal-Based Agents](#2-goal-based-agents)
3. [Utility-Based Agents](#3-utility-based-agents)
4. [Calling LLMs Programmatically](#4-calling-llms-programmatically)
5. [CRM Lead Qualifier Agent](#5-crm-lead-qualifier-agent)
6. [CSV FAQ Agent (Stub File)](#6-csv-faq-agent-stub-file)

---

## 1. Reflex Agents

**File:** `1. Reflex_Agents.ipynb`

### Overview

Reflex AI Agents are the most fundamental class of intelligent agents. They are designed to react immediately to their environment without "thinking" about the future or analyzing complex consequences. Think of them like human reflexes (e.g., blinking when an object flies toward your eye)—purely reactive and fast.

### Key Characteristic

Reflex agents operate on **Condition-Action Rules** (often called "If-Then" logic):
- **Condition**: The agent perceives a specific state in the environment
- **Action**: The agent immediately executes a pre-assigned task associated with that state

They do **not** plan, strategize, or simulate future outcomes. They only care about the "here and now."

### The Vacuum World Scenario

The notebook uses a classic AI teaching example: a vacuum cleaner robot operating in two rooms (A and B).

---

### Part 1: Simple Reflex Agent

#### Rules
```
IF current room is dirty → Clean it (Suction on)
IF current room is clean → Move to the other room
```

#### Implementation

```python
class SimpleReflexAgent:
    def __init__(self):
        # No internal memory (state) here!
        pass

    def decide(self, percept):
        location, is_dirty = percept
        
        # Rule 1: If current spot is dirty, clean it
        if is_dirty:
            return "Suction on"
        
        # Rule 2: If clean, move to the other room
        elif location == 'A':
            return "Right"
        elif location == 'B':
            return "Left"
```

**Line-by-line breakdown:**

- `__init__` does nothing (`pass`) — the agent has **zero memory**. It cannot remember what it did before.
- `decide(self, percept)` receives a tuple `(location, is_dirty)` — the agent's only view of the world.
- The method is pure if-then logic: dirty → clean, clean at A → go right, clean at B → go left.
- There is no state tracking, no history, no model of the world.

#### Simulation Code & Step-by-Step Walkthrough

```python
env_state = {'A': True, 'B': False}  # A is Dirty (True), B is Clean (False)
agent_location = 'A'
agent = SimpleReflexAgent()

for i in range(4):
    is_dirty = env_state[agent_location]
    percept = (agent_location, is_dirty)
    action = agent.decide(percept)
    # Update environment based on action...
```

**Setup:** `env_state = {'A': True, 'B': False}` — Room A is **dirty**, Room B is **clean**. Agent starts at `'A'`.

| Step | `agent_location` | `is_dirty` | `percept` | Action | What Happens Next |
|------|-------------------|-----------|-----------|--------|-------------------|
| 0 | `'A'` | `True` | `('A', True)` | `"Suction on"` | Cleans A → `env_state['A'] = False`. Agent stays at A. |
| 1 | `'A'` | `False` | `('A', False)` | `"Right"` | A is now clean, so moves right → `agent_location = 'B'` |
| 2 | `'B'` | `False` | `('B', False)` | `"Left"` | B is clean, so moves left → `agent_location = 'A'` |
| 3 | `'A'` | `False` | `('A', False)` | `"Right"` | A is clean, so moves right → `agent_location = 'B'` |

**What's happening:** After the useful work is done in Step 0 (cleaning A), the remaining steps are **wasted oscillation**. Both rooms are clean, but the agent has no memory — it can't tell everything is done. It just keeps bouncing Left/Right forever. This is the fundamental limitation of a simple reflex agent.

---

### Part 2: Model-Based Reflex Agent

To overcome the simple agent's limitations, we introduce a **Model-Based Reflex Agent** that maintains an internal state.

#### Key Improvements

| Feature | Simple Reflex | Model-Based Reflex |
|---------|--------------|-------------------|
| Internal Memory | ❌ None | ✅ Tracks world state |
| Detects "Job Done" | ❌ No | ✅ Yes |
| Avoids Redundancy | ❌ No | ✅ Yes |

#### Implementation

```python
class ModelBasedReflexAgent:
    def __init__(self):
        self.model = {
            'A': 'Unknown',
            'B': 'Unknown'
        }

    def update_state(self, location, is_dirty):
        self.model[location] = 'Dirty' if is_dirty else 'Clean'

    def decide(self, percept):
        location, is_dirty = percept
        self.update_state(location, is_dirty)

        if all(status == 'Clean' for status in self.model.values()):
            return "NoOp (Job Done)"

        if is_dirty:
            return "Suction on"
        elif location == 'A':
            return "Right"
        elif location == 'B':
            return "Left"
```

**Line-by-line breakdown:**

- `self.model = {'A': 'Unknown', 'B': 'Unknown'}` — The agent starts knowing **nothing** about either room.
- `update_state()` is called **first** every time `decide()` runs. It records the observed room as `'Clean'` or `'Dirty'` in the model.
- `all(status == 'Clean' for status in self.model.values())` — This is the **new rule** the simple agent couldn't have: "If I know for a fact that every room is clean, stop."
- Only after the "all clean" check does it fall through to the standard clean/move rules.

#### Simulation Code & Step-by-Step Walkthrough

```python
env_state = {'A': False, 'B': True}  # A is Clean, B is Dirty
agent_location = 'A'
agent = ModelBasedReflexAgent()

for i in range(5):
    is_dirty = env_state[agent_location]
    percept = (agent_location, is_dirty)
    action = agent.decide(percept)
    if action == "NoOp (Job Done)":
        break
    # Update environment based on action...
```

**Setup:** `env_state = {'A': False, 'B': True}` — Room A is **clean**, Room B is **dirty**. Agent starts at `'A'`.

| Step | Location | `is_dirty` | `self.model` (after update) | All Clean? | Action |
|------|----------|-----------|---------------------------|------------|--------|
| 0 | `'A'` | `False` | `{'A': 'Clean', 'B': 'Unknown'}` | No (`'Unknown'` ≠ `'Clean'`) | `"Right"` → move to B |
| 1 | `'B'` | `True` | `{'A': 'Clean', 'B': 'Dirty'}` | No | `"Suction on"` → clean B |
| 2 | `'B'` | `False` | `{'A': 'Clean', 'B': 'Clean'}` | **Yes** | `"NoOp (Job Done)"` → **STOP** |

**What's happening:** The agent visits A, records it as clean, but doesn't know about B yet (`'Unknown'`), so it moves right. At B it sees dirty, cleans it. On the next check, B is now clean, and the model confirms **both rooms are clean** → the agent stops. No infinite loop! The `break` exits the for-loop entirely.

### Key Takeaway

Even without explicit planning, maintaining an internal model of the world enables significantly smarter and more efficient behavior. This idea—augmenting reactivity with state—scales directly into more sophisticated agent architectures.

---

## 2. Goal-Based Agents

**File:** `2. Goal_based_agents.ipynb`

### Overview

Goal-based agents represent a significant evolution from reflex agents. Instead of simply reacting to the current state, they **plan ahead** to achieve a specific objective.

### The Core Difference

| Agent Type | Behavior |
|------------|----------|
| **Reflex Agent** | "I see I'm not at the goal. I'll take one step Right." (Repeat 100 times) |
| **Goal-Based Agent** | "To get to (4,4), I need 4 Down moves and 4 Right moves. Here is my plan. Execute." |

### The Grid World Scenario

An agent `'A'` must navigate a 5×5 grid to reach goal `'G'` at position `(4, 4)`, starting from `(0, 0)`.

### Environment Class

```python
class Environment:
    def __init__(self, size, start, goal):
        self.size = size
        self.agent_pos = list(start)  # e.g., [0, 0]
        self.goal_pos = list(goal)    # e.g., [4, 4]
        self.path_taken = []

    def update_agent_pos(self, action):
        if action == "Down":
            self.agent_pos[0] += 1
        elif action == "Up":
            self.agent_pos[0] -= 1
        elif action == "Right":
            self.agent_pos[1] += 1
        elif action == "Left":
            self.agent_pos[1] -= 1
        self.path_taken.append(tuple(self.agent_pos))

    def display(self):
        # Clears console, prints grid with A (agent), G (goal), . (path)
        ...
```

**Line-by-line breakdown:**

- `self.agent_pos = list(start)` — Converts the start tuple `(0,0)` to a mutable list `[0, 0]` so we can modify it in-place. Index `[0]` = row, `[1]` = column.
- `update_agent_pos()` modifies the position: `"Down"` adds 1 to row (moves down the grid), `"Right"` adds 1 to column (moves right on the grid).
- `self.path_taken` accumulates every position visited as a tuple, used by `display()` to show dots `.` where the agent has been.
- `display()` clears the screen and redraws the 5×5 grid with `A` at the agent's position, `G` at the goal, and `.` for visited cells. `time.sleep(0.8)` creates an animation effect.

### Goal-Based Agent Implementation

```python
class GoalBasedAgent:
    def __init__(self, env):
        self.env = env
        self.plan = []

    def perceive(self):
        return self.env.agent_pos

    def formulate_goal(self):
        return self.env.goal_pos

    def formulate_plan(self, start, goal):
        plan = []
        
        diff_row = goal[0] - start[0]
        if diff_row > 0:
            plan.extend(["Down"] * diff_row)
        elif diff_row < 0:
            plan.extend(["Up"] * abs(diff_row))
        
        diff_col = goal[1] - start[1]
        if diff_col > 0:
            plan.extend(["Right"] * diff_col)
        elif diff_col < 0:
            plan.extend(["Left"] * abs(diff_col))
        
        return plan

    def run(self):
        current_loc = self.perceive()       # [0, 0]
        goal_loc = self.formulate_goal()     # [4, 4]
        
        self.plan = self.formulate_plan(current_loc, goal_loc)
        print(f"Plan created: {self.plan}")
        
        for action in self.plan:
            self.env.update_agent_pos(action)
            self.env.display()
        
        print("Goal Reached!")
```

**Line-by-line breakdown of `formulate_plan()`:**

- `diff_row = goal[0] - start[0]` → `4 - 0 = 4`. We need to go **4 rows down**.
- `plan.extend(["Down"] * 4)` → plan is now `["Down", "Down", "Down", "Down"]`.
- `diff_col = goal[1] - start[1]` → `4 - 0 = 4`. We need to go **4 columns right**.
- `plan.extend(["Right"] * 4)` → plan is now `["Down", "Down", "Down", "Down", "Right", "Right", "Right", "Right"]`.
- No BFS/DFS graph search — just simple arithmetic. This works because the grid has no obstacles.

**Line-by-line breakdown of `run()`:**

- `perceive()` reads current position `[0, 0]` from the environment.
- `formulate_goal()` reads goal position `[4, 4]` from the environment.
- `formulate_plan()` generates the **complete plan** before any movement happens.
- The `for` loop executes each action **blindly** — the agent doesn't re-check its sensors.

#### Simulation & Step-by-Step Walkthrough

```python
world = Environment(5, (0, 0), (4, 4))
agent = GoalBasedAgent(world)
world.display()
agent.run()
```

**Plan generated:** `['Down', 'Down', 'Down', 'Down', 'Right', 'Right', 'Right', 'Right']`

| Step | Action | `agent_pos` After | Grid Position |
|------|--------|-------------------|---------------|
| 0 | `"Down"` | `[1, 0]` | Row 1, Col 0 |
| 1 | `"Down"` | `[2, 0]` | Row 2, Col 0 |
| 2 | `"Down"` | `[3, 0]` | Row 3, Col 0 |
| 3 | `"Down"` | `[4, 0]` | Row 4, Col 0 (bottom-left) |
| 4 | `"Right"` | `[4, 1]` | Row 4, Col 1 |
| 5 | `"Right"` | `[4, 2]` | Row 4, Col 2 |
| 6 | `"Right"` | `[4, 3]` | Row 4, Col 3 |
| 7 | `"Right"` | `[4, 4]` | Row 4, Col 4 → **Goal Reached!** |

The agent first goes all the way down, then all the way right. It takes exactly 8 steps — the minimum possible. The path on the grid looks like an "L" shape.

### Key Concepts Demonstrated

1. **Planning Before Acting**: The agent generates a complete action sequence before moving. A reflex agent would move one step at a time without any plan.
2. **Explicit Goal Formulation**: `formulate_goal()` defines what success looks like — reaching `(4,4)`.
3. **Open-Loop Execution**: The `for action in self.plan` loop executes blindly. If an obstacle appeared at `(2,0)` mid-execution, the agent would crash into it because it's not re-checking sensors.
4. **Simple Arithmetic as Planning**: `goal[0] - start[0]` is the entire "intelligence" — no complex search algorithm needed for an obstacle-free world.

### Limitation

This is "open-loop control" — the agent assumes the world won't change while executing. More advanced agents use "closed-loop" control, re-checking sensors during execution.

---

## 3. Utility-Based Agents

**File:** `3. Utility_Agents.ipynb`

### Overview

While goal-based agents ask "Can I reach the goal?", utility-based agents ask "**Which path to the goal is best?**" They evaluate options not just by feasibility, but by **preference**, encoded through a **utility function**.

### The Travel Scenario

Agents must choose among routes that vary in multiple dimensions:

| Route | Time (min) | Cost ($) | Safety (1-10) | View (1-10) |
|-------|-----------|----------|---------------|-------------|
| Highway | 20 | 15 | 8 | 2 |
| Back Roads | 45 | 0 | 6 | 9 |
| City Center | 30 | 5 | 4 | 5 |

### Route Class

```python
class Route:
    def __init__(self, name, time_minutes, cost_dollars, safety_rating, view_rating):
        self.name = name
        self.time = time_minutes      # Lower is better
        self.cost = cost_dollars      # Lower is better
        self.safety = safety_rating   # Higher is better (1-10)
        self.view = view_rating       # Higher is better (1-10)

    def __repr__(self):
        return (f"{self.name}: {self.time}min, ${self.cost}, "
                f"Safety: {self.safety}/10, View: {self.view}/10")
```

**Line-by-line breakdown:**

- The `Route` class is a simple data container — each route has 4 numeric attributes.
- `__repr__` provides a human-readable string when you `print()` a Route object, e.g., `"Highway: 20min, $15, Safety: 8/10, View: 2/10"`.
- Some attributes you want to **minimize** (time, cost) and some to **maximize** (safety, view). The utility function handles this distinction via positive/negative weights.

### The Utility Function

The utility function translates a complex option into a **single numerical score**:

$$U(s) = w_1 \cdot f_1 + w_2 \cdot f_2 + w_3 \cdot f_3 + w_4 \cdot f_4$$

Where:
- $w_i$ = weights (the agent's "personality")
- $f_i$ = feature values (time, cost, safety, view)
- Negative weights → minimize that factor
- Positive weights → maximize that factor

### Agent Implementation

```python
class UtilityBasedAgent:
    def __init__(self, name, weights):
        self.name = name
        self.weights = weights  # The "personality"

    def utility_function(self, route):
        u = 0
        u += route.time * self.weights.get('time', 0)
        u += route.cost * self.weights.get('cost', 0)
        u += route.safety * self.weights.get('safety', 0)
        u += route.view * self.weights.get('view', 0)
        return u

    def choose_route(self, routes):
        best_route = None
        highest_utility = float('-inf')
        
        for route in routes:
            score = self.utility_function(route)
            if score > highest_utility:
                highest_utility = score
                best_route = route
        
        return best_route
```

**Line-by-line breakdown of `utility_function()`:**

- `self.weights.get('time', 0)` — Looks up the weight for `'time'`. If not found, defaults to `0` (that factor is ignored).
- Each attribute is multiplied by its weight and accumulated into `u`.
- A negative weight (e.g., `time: -2.0`) means higher time **reduces** the score (the agent is penalized for slow routes).
- A positive weight (e.g., `safety: 2.0`) means higher safety **increases** the score.

**Line-by-line breakdown of `choose_route()`:**

- `highest_utility = float('-inf')` — Starts at negative infinity so any real score will beat it.
- The loop evaluates every route, keeping track of the best one found so far.
- After iterating all routes, `best_route` holds the winner.

### Simulation & Step-by-Step Walkthrough

```python
possible_routes = [
    Route("Highway",      time_minutes=20, cost_dollars=15, safety_rating=8, view_rating=2),
    Route("Back Roads",   time_minutes=45, cost_dollars=0,  safety_rating=6, view_rating=9),
    Route("City Center",  time_minutes=30, cost_dollars=5,  safety_rating=4, view_rating=5)
]

exec_weights = {'time': -2.0, 'cost': -0.1, 'safety': 2.0, 'view': 0.0}
agent_exec = UtilityBasedAgent("Business Agent", exec_weights)

student_weights = {'time': -0.1, 'cost': -5.0, 'safety': 1.0, 'view': 2.0}
agent_student = UtilityBasedAgent("Student Agent", student_weights)
```

#### Business Agent Score Calculation

Weights: `time: -2.0, cost: -0.1, safety: 2.0, view: 0.0`

| Route | Time × -2.0 | Cost × -0.1 | Safety × 2.0 | View × 0.0 | **Total** |
|-------|-------------|-------------|--------------|------------|-----------|
| Highway | 20 × -2.0 = **-40** | 15 × -0.1 = **-1.5** | 8 × 2.0 = **16** | 2 × 0.0 = **0** | **-25.5** |
| Back Roads | 45 × -2.0 = **-90** | 0 × -0.1 = **0** | 6 × 2.0 = **12** | 9 × 0.0 = **0** | **-78.0** |
| City Center | 30 × -2.0 = **-60** | 5 × -0.1 = **-0.5** | 4 × 2.0 = **8** | 5 × 0.0 = **0** | **-52.5** |

**Winner: Highway (-25.5)** — The least negative score. The business agent hates wasting time, and Highway is the fastest (only 20 min gets the smallest time penalty).

#### Student Agent Score Calculation

Weights: `time: -0.1, cost: -5.0, safety: 1.0, view: 2.0`

| Route | Time × -0.1 | Cost × -5.0 | Safety × 1.0 | View × 2.0 | **Total** |
|-------|-------------|-------------|--------------|------------|-----------|
| Highway | 20 × -0.1 = **-2** | 15 × -5.0 = **-75** | 8 × 1.0 = **8** | 2 × 2.0 = **4** | **-65.0** |
| Back Roads | 45 × -0.1 = **-4.5** | 0 × -5.0 = **0** | 6 × 1.0 = **6** | 9 × 2.0 = **18** | **19.5** |
| City Center | 30 × -0.1 = **-3** | 5 × -5.0 = **-25** | 4 × 1.0 = **4** | 5 × 2.0 = **10** | **-14.0** |

**Winner: Back Roads (19.5)** — The only positive score! Back Roads costs $0 (no cost penalty at all) and has the best view (9 × 2.0 = 18 points). The student doesn't mind the 45 minutes (only -4.5 penalty).

### Key Insights

1. **Rational ≠ Identical**: Both agents are perfectly rational — they each pick the best option for their own priorities. The student isn't "wrong" for taking the slow road.

2. **Explicit Preferences**: Changing the weights dictionary completely changes the agent's behavior. You can "tune" an agent's personality by adjusting numbers.

3. **Scalable Decision-Making**: By reducing complex, multi-attribute choices to a single score, utility functions enable efficient comparison even among hundreds of options.

---

## 4. Calling LLMs Programmatically

**File:** `4. Calling_LLMs_programmatically.ipynb`

### Overview

This notebook teaches how to programmatically connect to the world's leading Large Language Models (LLMs) using two distinct strategies.

### Required API Keys

Set these in Colab Secrets:
- `OPENAI_APIKEY`
- `CLAUDE_APIKEY`
- `GEMINI_APIKEY`
- `OPENROUTER_APIKEY`

---

### Strategy 1: Direct Provider SDKs ("Siloed" Approach)

Each major AI lab releases its own Python SDK with slightly different syntax.

#### 1. OpenAI (GPT-4, GPT-4o)

```python
from openai import OpenAI

def query_openai(prompt):
    client = OpenAI(api_key=userdata.get('OPENAI_APIKEY'))
    
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content
```

**Line-by-line breakdown:**

- `OpenAI(api_key=...)` — Creates a client object authenticated with your API key. All subsequent calls go through this client.
- `client.chat.completions.create(...)` — This is the core API call. The `chat.completions` endpoint is the **industry standard** format.
- `model="gpt-4.1-mini"` — Specifies which model to use. Change this string to use `"gpt-4o"`, `"gpt-4"`, etc.
- `messages=[...]` — A list of message objects. Each has a `"role"` and `"content"`:
  - `"system"` — Sets the AI's behavior/personality. The model reads this first.
  - `"user"` — The actual question/prompt from the user.
- `temperature=0.7` — Controls randomness. `0.0` = deterministic (same answer every time), `1.0` = more creative/varied.
- `response.choices[0].message.content` — The API returns a `choices` array (usually 1 item). `.message.content` extracts the text string of the reply.

#### 2. Anthropic (Claude 3.5 Sonnet, Opus)

```python
import anthropic

def query_anthropic(prompt):
    client = anthropic.Anthropic(api_key=userdata.get('CLAUDE_APIKEY'))
    
    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return message.content[0].text
```

**Line-by-line breakdown:**

- `anthropic.Anthropic(...)` — Creates the Anthropic client. Different class from OpenAI's.
- `client.messages.create(...)` — Anthropic's API call. Note: `messages.create` instead of `chat.completions.create`.
- `max_tokens=1024` — **Required** by Anthropic (OpenAI makes this optional). Caps the response length.
- `messages=[...]` — Same role/content format as OpenAI, but Anthropic handles system instructions separately (via a `system` parameter in some versions).
- `message.content[0].text` — Key difference from OpenAI! Anthropic returns `content` as a **list of content blocks** (not a string). You access `[0].text` to get the text. OpenAI uses `choices[0].message.content` (a string directly).

#### 3. Google Gemini

```python
import google.generativeai as genai

def query_gemini(prompt):
    genai.configure(api_key=userdata.get('GEMINI_APIKEY'))
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    response = model.generate_content(prompt)
    return response.text
```

**Line-by-line breakdown:**

- `genai.configure(api_key=...)` — Sets the API key globally (module-level config, not per-client).
- `genai.GenerativeModel('gemini-2.5-flash')` — Creates a model **object**. This is fundamentally different from OpenAI/Anthropic where you pass the model name as a string to each API call.
- `model.generate_content(prompt)` — Sends the prompt directly as a string. No `messages=[...]` array needed for simple queries. This is the simplest API surface of the three.
- `response.text` — Extracts the generated text. Much simpler than navigating `choices[0].message.content`.

#### Side-by-Side API Comparison

| Step | OpenAI | Anthropic | Gemini |
|------|--------|-----------|--------|
| Create client | `OpenAI(api_key=...)` | `anthropic.Anthropic(api_key=...)` | `genai.configure(api_key=...)` |
| Call API | `client.chat.completions.create(...)` | `client.messages.create(...)` | `model.generate_content(prompt)` |
| Pass model | `model="gpt-4.1-mini"` (string param) | `model="claude-haiku-4-5"` (string param) | `GenerativeModel('gemini-2.5-flash')` (object) |
| Pass prompt | `messages=[{"role":..., "content":...}]` | `messages=[{"role":..., "content":...}]` | `prompt` (plain string) |
| Get response | `response.choices[0].message.content` | `message.content[0].text` | `response.text` |

---

### Strategy 2: Unified Aggregator (OpenRouter)

**What is OpenRouter?**

A unified interface that allows you to access almost any major LLM using a **single API format** (the OpenAI format). You use the `openai` Python library but point it at OpenRouter's URL instead:

```python
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=userdata.get('OPENROUTER_APIKEY')
)
```

The key trick is `base_url` — instead of calling `api.openai.com`, requests go to `openrouter.ai`, which forwards them to the right provider. You then switch models by changing a string:

```python
model="anthropic/claude-3-opus"    # Uses Claude via OpenRouter
model="meta-llama/llama-3-70b"     # Uses Llama via OpenRouter
model="openai/gpt-4o"              # Uses GPT-4o via OpenRouter
```

**Benefits:**
- **One SDK**: Only need the `openai` library to access Claude, Llama, Mistral, etc.
- **Model Shopping**: Switch models by changing a string — no code rewrite needed.
- **Cost Effective**: Usually charges standard provider prices.

### Comparison Table

| Aspect | Direct SDKs | OpenRouter |
|--------|-------------|------------|
| Libraries Needed | Multiple (openai, anthropic, google-generativeai) | One (openai) |
| API Syntax | Different for each | Unified (OpenAI format) |
| Model Switching | Requires code changes | String change only |
| Best For | Single provider, maximum control | Multi-model applications |

---

## 5. CRM Lead Qualifier Agent

**File:** `5. CRM_Lead_Qualifier_Agent.ipynb`

### Overview

This is a complete, practical AI agent that demonstrates **Function Calling** — the mechanism that bridges the gap between an AI model (text generator) and actual code (which can perform actions).

### The Business Problem

Sales representatives spend valuable time manually researching leads before calls. This agent automates that process.

### Agent Workflow

```
Email Input → Extract Domain → Lookup Company Info → Check CRM History → Calculate Lead Score → Generate Summary
```

Example: `jane@acmecorp.com` → Domain: `acmecorp.com` → Industry: Software/SaaS, Size: 501-1000, Revenue: $50M-$100M → CRM: Cold Lead, Attended webinar → Score: Medium → Summary for sales rep

---

### Understanding Function Calling

Think of the LLM as a smart receptionist. It understands what people want, but it doesn't have the keys to the file cabinet or the ability to make phone calls itself. **Function calling gives the receptionist a "menu" of services it can request**.

#### The Flow

```
1. You provide the tools (function definitions)
       ↓
2. User asks: "What's the weather in Tokyo?"
       ↓
3. Model outputs JSON: {"function": "get_weather", "arguments": {"city": "Tokyo"}}
       ↓
4. Your code executes the actual function → "Sunny, 25°C"
       ↓
5. You feed result back to model
       ↓
6. Model writes final answer: "It is currently sunny and 25 degrees in Tokyo."
```

---

### Tool Definitions (The Business Logic)

#### Tool 1: Domain Lookup

```python
def lookup_domain_info(domain: str) -> str:
    mock_data = {
        "acmecorp.com": {"industry": "Software/SaaS", "size": "501-1000 employees", "revenue": "$50M - $100M"},
        "widgetco.net": {"industry": "Manufacturing", "size": "100-250 employees", "revenue": "$10M - $25M"},
        "globalfin.org": {"industry": "Financial Services", "size": "5000+ employees", "revenue": "$1B+"},
    }
    info = mock_data.get(domain, {"industry": "Unknown", "size": "N/A", "revenue": "N/A"})
    return json.dumps(info)
```

**Line-by-line breakdown:**

- `mock_data` — A dictionary simulating an external API like Clearbit or Crunchbase. In production, this would be a real HTTP request.
- `mock_data.get(domain, {...})` — Looks up the domain. If the domain isn't in the mock data, returns a default dict with `"Unknown"` values. This handles unknown companies gracefully.
- `json.dumps(info)` — Converts the Python dict to a JSON string. The LLM can only receive text, not Python objects, so we serialize it.

#### Tool 2: CRM History Check

```python
def check_crm_history(email: str) -> str:
    mock_data = {
        "jane@acmecorp.com": {"last_contact": "2025-11-15", "status": "Cold Lead", "notes": "Attended webinar, no follow-up yet."},
        "bob@widgetco.net": {"last_contact": "2025-12-01", "status": "Active Opportunity", "notes": "Discussed Q1 budget and product integration."},
    }
    history = mock_data.get(email, {"last_contact": "N/A", "status": "No Record", "notes": "New lead, first contact opportunity."})
    return json.dumps(history)
```

**Line-by-line breakdown:**

- Same pattern as Tool 1 — mock data simulating a CRM database (Salesforce, HubSpot).
- The default fallback `"No Record"` handles completely new leads that aren't in the CRM yet.
- Returns JSON string with `last_contact` date, engagement `status`, and free-text `notes`.

#### Tool 3: Lead Score Calculator

```python
def calculate_lead_score(data_summary: str) -> str:
    data = json.loads(data_summary)
    score = "Low"  # Default score
    
    if data["domain_info"].get("revenue", "").startswith("$1B+"):
        score = "High"
    elif data["crm_history"].get("status") == "Active Opportunity":
        score = "High"
    elif data["domain_info"].get("revenue", "").startswith("$50M"):
        score = "Medium"
    
    return json.dumps({"lead_score": score})
```

**Line-by-line breakdown:**

- `json.loads(data_summary)` — Parses the incoming JSON string back to a Python dict. This dict contains both `domain_info` and `crm_history` from previous tool calls.
- The scoring logic is a simple priority cascade:
  - Revenue `"$1B+"` → **High** (massive company = high-value lead)
  - Status `"Active Opportunity"` → **High** (there's already a deal in progress)
  - Revenue starts with `"$50M"` → **Medium** (significant revenue but no active deal)
  - Everything else → **Low** (default)
- Returns a JSON string like `{"lead_score": "Medium"}`.

#### Function-to-Python Mapping

```python
AVAILABLE_FUNCTIONS = {
    "lookup_domain_info": lookup_domain_info,
    "check_crm_history": check_crm_history,
    "calculate_lead_score": calculate_lead_score,
}
```

This dictionary maps function **name strings** (what the LLM outputs) to actual **Python function objects** (what your code runs). When the LLM says "call `lookup_domain_info`", the code does `AVAILABLE_FUNCTIONS["lookup_domain_info"]` to get the real function and then calls it.

---

### Tool Schema (The "Menu" for the LLM)

The LLM cannot see Python code directly. We describe tools using JSON schema:

```python
tools_schema = [
    {
        "type": "function",
        "function": {
            "name": "lookup_domain_info",
            "description": "Retrieves general business information (industry, size, revenue) about a company based on its domain name.",
            "parameters": {
                "type": "object",
                "properties": {
                    "domain": {"type": "string", "description": "The company's domain name, e.g., 'acmecorp.com'"},
                },
                "required": ["domain"],
            },
        },
    },
    # ... similar definitions for check_crm_history and calculate_lead_score
]
```

**What each field does:**

- `"name"` — Must exactly match the key in `AVAILABLE_FUNCTIONS`. This is how the code knows which function to call.
- `"description"` — The LLM reads this to decide **when** to use the tool. A poor description = the LLM won't know when to call it.
- `"parameters"` — Tells the LLM what arguments to provide and their types. `"required"` ensures the LLM always includes mandatory fields.

---

### The Agent Loop

The core pattern: **Think → Act → Observe → Repeat**

```python
def run_agent(user_prompt: str):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    collected_data = {}  # Agent's "memory" across steps

    while True:
        # THINK: Send conversation to model
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            tools=tools_schema,
            tool_choice="auto",
        )
        
        response_message = response.choices[0].message
        messages.append(response_message)

        # ACT: If model wants to call tools
        if response_message.tool_calls:
            for tool_call in response_message.tool_calls:
                function_name = tool_call.function.name
                function_args = json.loads(tool_call.function.arguments)
                
                function_result = AVAILABLE_FUNCTIONS[function_name](**function_args)
                
                # Store in memory
                if function_name == "lookup_domain_info":
                    collected_data["domain_info"] = json.loads(function_result)
                elif function_name == "check_crm_history":
                    collected_data["crm_history"] = json.loads(function_result)
                
                # OBSERVE: Append result as new message
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": function_name,
                    "content": function_result
                })
        else:
            # No more tool calls - model is ready to respond
            print(response_message.content)
            break
```

**Line-by-line breakdown:**

- `messages = [...]` — Initializes the conversation with a system prompt (agent instructions) and the user's request.
- `collected_data = {}` — A dict that persists **across loop iterations** to accumulate data from multiple tool calls.
- **The `while True` loop** — This is the agent loop. It keeps running until the model decides it has enough info.
- `client.chat.completions.create(...)` — Sends the full conversation history + tool definitions to GPT-4o. `tool_choice="auto"` lets the model decide whether to call a tool or respond directly.
- `messages.append(response_message)` — Adds the model's response (including any tool call requests) to the conversation history; the model needs to "see" its own previous messages.
- `if response_message.tool_calls:` — The model either returns **tool calls** (it wants to act) or **text content** (it's ready to answer). This branch handles tools.
- `tool_call.function.name` — The string name of the function the model wants to call, e.g., `"lookup_domain_info"`.
- `json.loads(tool_call.function.arguments)` — The model provides arguments as a JSON string, e.g., `'{"domain": "acmecorp.com"}'`. We parse it to a dict.
- `AVAILABLE_FUNCTIONS[function_name](**function_args)` — Looks up the real Python function and calls it with the parsed arguments. `**function_args` unpacks the dict as keyword arguments.
- `collected_data["domain_info"] = ...` — Stores each tool's result so later tools (like `calculate_lead_score`) can access accumulated data.
- `"role": "tool"` message — Sends the tool's output **back to the model** so it can process the result and decide what to do next.
- `else: break` — When the model returns text instead of tool calls, it has finished reasoning. We print the final summary and exit the loop.

#### Step-by-Step Walkthrough: Scenario 1 (jane@acmecorp.com)

**Input:** `"Please qualify this lead for my call tomorrow: jane@acmecorp.com"`

| Loop Iteration | Model Decision | What Happens |
|---------------|----------------|--------------|
| 1 | Calls `lookup_domain_info(domain="acmecorp.com")` | Extracts domain from email. Tool returns `{"industry": "Software/SaaS", "size": "501-1000 employees", "revenue": "$50M - $100M"}`. Stored in `collected_data["domain_info"]`. Result appended to messages. |
| 2 | Calls `check_crm_history(email="jane@acmecorp.com")` | Tool returns `{"last_contact": "2025-11-15", "status": "Cold Lead", "notes": "Attended webinar, no follow-up yet."}`. Stored in `collected_data["crm_history"]`. Result appended to messages. |
| 3 | Calls `calculate_lead_score(data_summary="{...}")` | Model combines collected data into a JSON string and passes it. Scoring logic: revenue starts with `"$50M"` → score = **"Medium"**. Result appended to messages. |
| 4 | Returns text (no tool calls) | Model synthesizes all data into a readable summary for the sales rep. Loop `break`s. |

**Final output:** A formatted summary with company info, CRM history, lead score, and talking points for the sales call.

#### Step-by-Step Walkthrough: Scenario 2 (bob@widgetco.net)

| Loop Iteration | Model Decision | Key Detail |
|---------------|----------------|------------|
| 1 | `lookup_domain_info("widgetco.net")` | Revenue: `"$10M - $25M"` (smaller company) |
| 2 | `check_crm_history("bob@widgetco.net")` | Status: `"Active Opportunity"` (deal in progress!) |
| 3 | `calculate_lead_score(...)` | Status is "Active Opportunity" → score = **"High"** (despite lower revenue) |
| 4 | Returns final summary | Despite being a smaller company, the active deal status pushes it to High priority. |

---

## 6. CSV FAQ Agent (Stub File)

**File:** `6. Hello_Agent_CSV_FAQ_Agent_(Stub_File).ipynb`

### Overview

This is a **hands-on exercise** (stub file with TODOs) where students build a multi-file FAQ agent using LangChain's Pandas DataFrame Agent.

### What It Does

1. Downloads 4 CSV files from Google Drive
2. Creates a LangChain agent that can query across all datasets
3. Provides an interactive chat loop for natural language Q&A

---

### Part 1: Automatic File Downloader

```python
import gdown

files_to_download = {
    "saas_docs.csv":         "https://drive.google.com/file/d/...",
    "credit_card_terms.csv": "https://drive.google.com/file/d/...",
    "hospital_policy.csv":   "https://drive.google.com/file/d/...",
    "ecommerce_faqs.csv":    "https://drive.google.com/file/d/..."
}

for filename, url in files_to_download.items():
    if not os.path.exists(filename):
        gdown.download(url, filename, quiet=False, fuzzy=True)
```

**Line-by-line breakdown:**

- `files_to_download` — A dict mapping local filenames to Google Drive URLs. Each CSV covers a different domain.
- `os.path.exists(filename)` — Checks if the file was already downloaded. Avoids re-downloading on repeated runs.
- `gdown.download(url, filename, quiet=False, fuzzy=True)` — `gdown` is a library for downloading from Google Drive. `fuzzy=True` lets it handle various Google Drive URL formats (share links, direct links, etc.).

---

### Part 2: AI Agent Setup

#### Loading CSVs

```python
dataframes = []
loaded_names = []

for filename in files_to_download.keys():
    df = pd.read_csv(filename)
    dataframes.append(df)
    loaded_names.append(filename)
```

**Line-by-line breakdown:**

- `dataframes = []` — Will hold 4 Pandas DataFrames, one per CSV.
- `pd.read_csv(filename)` — Reads each CSV into a DataFrame (a table with rows and columns).
- `dataframes.append(df)` — The order matters: `dataframes[0]` = saas_docs, `dataframes[1]` = credit_card_terms, etc.
- The LangChain agent receives this **list** of DataFrames and can query any of them.

#### System Prompt

```python
system_prompt = """
You are a smart data assistant capable of reading multiple CSV files.
- You have access to 4 different datasets: SaaS Docs, Credit Card Terms, Hospital Policy, and Ecommerce FAQs.
- When asked a question, determine which DataFrame is most relevant.
- Do NOT answer from general knowledge.
- Answer in plain English.
"""
```

This prompt is prepended to every user question. The key instruction is **"Do NOT answer from general knowledge"** — forcing the agent to always look at the actual CSV data rather than making things up.

---

### TODOs for Students (Solutions)

#### TODO 1: Initialize the LLM

```python
# Replace None with:
llm = ChatOpenAI(
    api_key=api_key,
    model="gpt-4o-mini",
    temperature=0.0
)
```

- `ChatOpenAI` is LangChain's wrapper around the OpenAI API. It works like `OpenAI()` but integrates with LangChain's agent framework.
- `temperature=0.0` — Fully deterministic. Important for data queries — you want consistent, precise answers, not creative ones.

#### TODO 2: Create the Pandas Agent

```python
agent = create_pandas_dataframe_agent(
    llm,
    dataframes,  # <-- The list of 4 DataFrames
    verbose=True,
    agent_type="openai-functions",
    allow_dangerous_code=True
)
```

- `create_pandas_dataframe_agent` — A LangChain function that creates an agent capable of writing and executing Python/Pandas code to answer questions about DataFrames.
- `dataframes` — The list of 4 DataFrames. The agent gets access to all of them and can figure out which one to query.
- `verbose=True` — Prints the agent's internal reasoning (which DataFrame it picks, what Pandas code it writes). Very useful for debugging.
- `agent_type="openai-functions"` — Uses OpenAI's function calling mechanism (same concept as Notebook 5) under the hood.
- `allow_dangerous_code=True` — Required because the agent generates and executes Python code dynamically. The "dangerous" warning exists because arbitrary code execution can be risky in production.

#### TODO 3: Invoke the Agent

```python
# In the chat loop, replace "..." with:
result = agent.invoke(final_query)
response = result['output']
```

- `agent.invoke(final_query)` — Sends the combined system prompt + user question to the agent. The agent then:
  1. Reads the question
  2. Decides which DataFrame(s) to query
  3. Writes Pandas code (e.g., `df[df['category'] == 'visiting hours']['answer'].values[0]`)
  4. Executes the code
  5. Returns the result
- `result['output']` — The agent returns a dict; the `'output'` key contains the final text answer.

---

### Part 3: Chat Loop

```python
while True:
    user_input = input("You: ")
    
    if user_input.lower() in ["exit", "quit", "q"]:
        break
    
    final_query = system_prompt + "\n\nQuestion: " + user_input
    
    result = agent.invoke(final_query)
    print(f"AI: {result['output']}")
```

**Line-by-line breakdown:**

- `while True:` — Infinite loop that keeps the conversation going until the user types "exit".
- `input("You: ")` — Reads user input from the terminal.
- `user_input.lower() in ["exit", "quit", "q"]` — Case-insensitive exit check.
- `final_query = system_prompt + "\n\nQuestion: " + user_input` — Prepends the system prompt to every question. This ensures the agent always remembers its rules (use data, not general knowledge).
- `agent.invoke(final_query)` — Under the hood, the agent may make multiple LLM calls: one to understand the question, one to write Pandas code, one to interpret the result.

#### Example Interaction Walkthrough

**User:** `"What is the visiting hour in the hospital?"`

1. Agent sees the question, determines `hospital_policy.csv` (DataFrame index 2) is relevant
2. Agent generates Pandas code like: `df2[df2['question'].str.contains('visiting', case=False)]['answer'].iloc[0]`
3. Code executes, returns the answer from the CSV
4. Agent formats and returns: `"Visiting hours are from 9:00 AM to 8:00 PM daily."`

### Example Questions

- "What is the visiting hour in the hospital?"
- "What is the API limit?"
- "What's the return policy for electronics?"
- "What is the credit card annual fee?"

---

## Summary: Learning Progression

| # | Notebook | Agent Type | Core Learning |
|---|----------|------------|---------------|
| 1 | Reflex Agents | Simple & Model-Based Reflex | React to current state; memory avoids infinite loops |
| 2 | Goal-Based Agents | Goal-Based | Plan first, then execute; explicit goal formulation |
| 3 | Utility Agents | Utility-Based | Optimize decisions with weighted preferences; rationality is relative |
| 4 | Calling LLMs | N/A (Foundation) | Connect to OpenAI, Anthropic, Google APIs |
| 5 | CRM Lead Qualifier | Tool-Using LLM Agent | Function calling enables LLMs to take real actions |
| 6 | CSV FAQ Agent | Multi-Data LLM Agent | Build practical FAQ agents with LangChain |

### The Big Picture

The notebooks build a conceptual bridge:

1. **Notebooks 1-3**: Classical AI agent theory (no LLMs)
   - Reflex → Goal → Utility represents increasing sophistication in decision-making

2. **Notebook 4**: Technical foundation for LLM integration
   - How to programmatically call modern AI APIs

3. **Notebooks 5-6**: Practical LLM agents
   - Combining classical agent concepts with LLM capabilities
   - Function calling allows LLMs to "do" things, not just "say" things

By the end of Week 1, you understand both the theoretical foundations of intelligent agents AND how to implement practical LLM-powered agents that can interact with real systems.
