# Agentic AI 2.0 - Week 1: Notebook Explanations

This document provides detailed explanations of all six Colab notebooks in the Agentic AI 2.0 Week 1 curriculum. The notebooks progressively build your understanding from basic reflex agents to practical LLM-powered agents.

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

#### Critical Limitation

The simple reflex agent has **no memory**. If both rooms are clean, it will endlessly oscillate between them because it cannot recall whether the other room has already been cleaned.

**Simulation Output:**
```
Loc: A | Dirty: False -> Action: Right
Loc: B | Dirty: False -> Action: Left
Loc: A | Dirty: False -> Action: Right
Loc: B | Dirty: False -> Action: Left
... (infinite loop)
```

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
        # Internal State: Keeps track of the world status
        self.model = {
            'A': 'Unknown',
            'B': 'Unknown'
        }

    def update_state(self, location, is_dirty):
        """Updates internal model based on current percept"""
        self.model[location] = 'Dirty' if is_dirty else 'Clean'

    def decide(self, percept):
        location, is_dirty = percept
        
        # 1. Update Internal State first
        self.update_state(location, is_dirty)
        
        # 2. If internal model says EVERYWHERE is clean, Stop
        if all(status == 'Clean' for status in self.model.values()):
            return "NoOp (Job Done)"
        
        # Standard Cleaning Rules
        if is_dirty:
            return "Suction on"
        elif location == 'A':
            return "Right"
        elif location == 'B':
            return "Left"
```

#### Simulation Output

```
Loc: A | Dirty: False | Model: {'A': 'Clean', 'B': 'Unknown'} -> Action: Right
Loc: B | Dirty: True  | Model: {'A': 'Clean', 'B': 'Dirty'}  -> Action: Suction on
Loc: B | Dirty: False | Model: {'A': 'Clean', 'B': 'Clean'}  -> Action: NoOp (Job Done)
```

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

An agent 'A' must navigate a 5x5 grid to reach goal 'G' at position (4,4).

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
```

### Goal-Based Agent Implementation

```python
class GoalBasedAgent:
    def __init__(self, env):
        self.env = env
        self.plan = []

    def formulate_plan(self, start, goal):
        """
        Simple Planner: Calculate arithmetic difference to generate action sequence
        """
        plan = []
        
        # Calculate vertical distance
        diff_row = goal[0] - start[0]
        if diff_row > 0:
            plan.extend(["Down"] * diff_row)
        elif diff_row < 0:
            plan.extend(["Up"] * abs(diff_row))
        
        # Calculate horizontal distance
        diff_col = goal[1] - start[1]
        if diff_col > 0:
            plan.extend(["Right"] * diff_col)
        elif diff_col < 0:
            plan.extend(["Left"] * abs(diff_col))
        
        return plan

    def run(self):
        # 1. PERCEIVE current location
        current_loc = self.perceive()
        goal_loc = self.formulate_goal()
        
        # 2. PLAN - Generate FULL plan before taking any action
        self.plan = self.formulate_plan(current_loc, goal_loc)
        print(f"Plan created: {self.plan}")
        
        # 3. ACT - Execute plan
        for action in self.plan:
            self.env.update_agent_pos(action)
```

### Key Concepts Demonstrated

1. **Planning Before Acting**: The agent generates a complete sequence of actions (`['Down', 'Down', 'Down', 'Down', 'Right', 'Right', 'Right', 'Right']`) before moving.

2. **Explicit Goal Formulation**: The agent calls `formulate_goal()` to define exactly what success looks like.

3. **Open-Loop Execution**: Once the plan is made, the agent executes it blindly. If an obstacle appeared mid-execution, the agent wouldn't adapt.

4. **World Representation**: The agent understands the world through coordinates and uses simple arithmetic as a planning heuristic.

### Limitation

This is "open-loop control"—the agent assumes the world won't change while executing. More advanced agents use "closed-loop" control, re-checking sensors during execution.

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
```

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
        """Calculate 'Happiness Score' for a route"""
        u = 0
        u += route.time * self.weights.get('time', 0)
        u += route.cost * self.weights.get('cost', 0)
        u += route.safety * self.weights.get('safety', 0)
        u += route.view * self.weights.get('view', 0)
        return u

    def choose_route(self, routes):
        """Evaluate all options, pick highest utility"""
        best_route = None
        highest_utility = float('-inf')
        
        for route in routes:
            score = self.utility_function(route)
            if score > highest_utility:
                highest_utility = score
                best_route = route
        
        return best_route
```

### Two Different "Personalities"

#### Business Agent
```python
exec_weights = {'time': -2.0, 'cost': -0.1, 'safety': 2.0, 'view': 0.0}
```
- Hates wasting time (`time: -2.0`)
- Doesn't care about cost (`cost: -0.1`)
- Values safety (`safety: 2.0`)
- **Chooses: Highway** (fast and safe)

#### Student Agent
```python
student_weights = {'time': -0.1, 'cost': -5.0, 'safety': 1.0, 'view': 2.0}
```
- Hates spending money (`cost: -5.0`)
- Doesn't mind extra time (`time: -0.1`)
- Enjoys nice views (`view: 2.0`)
- **Chooses: Back Roads** (free and scenic)

### Key Insights

1. **Rational ≠ Identical**: Two agents can be perfectly rational yet make opposite choices because they value outcomes differently.

2. **Explicit Preferences**: The utility function makes an agent's priorities transparent and tunable.

3. **Scalable Decision-Making**: By reducing complex, multi-attribute choices to a single score, utility functions enable efficient comparison among hundreds of options.

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

**Key Feature**: The `chat.completions.create` format has become the industry standard.

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
    # Note: Different response structure
    return message.content[0].text
```

**Key Feature**: Known for large context windows and safety focus.

#### 3. Google Gemini

```python
import google.generativeai as genai

def query_gemini(prompt):
    genai.configure(api_key=userdata.get('GEMINI_APIKEY'))
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    response = model.generate_content(prompt)
    return response.text
```

**Key Feature**: Creates a `GenerativeModel` object rather than using chat completion style. Native multimodal capabilities.

---

### Strategy 2: Unified Aggregator (OpenRouter)

**What is OpenRouter?**

A unified interface that allows you to access almost any major LLM using a **single API format** (the OpenAI format).

**Benefits:**
- **One SDK**: Only need the `openai` library to access Claude, Llama, Mistral, etc.
- **Model Shopping**: Switch models by changing a string (e.g., `gpt-4` to `anthropic/claude-3-opus`)
- **Cost Effective**: Usually charges standard provider prices

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

This is a complete, practical AI agent that demonstrates **Function Calling**—the mechanism that bridges the gap between an AI model (text generator) and actual code (which can perform actions).

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
    """Simulates calling an external API like Clearbit or Crunchbase"""
    mock_data = {
        "acmecorp.com": {"industry": "Software/SaaS", "size": "501-1000 employees", "revenue": "$50M - $100M"},
        "widgetco.net": {"industry": "Manufacturing", "size": "100-250 employees", "revenue": "$10M - $25M"},
        "globalfin.org": {"industry": "Financial Services", "size": "5000+ employees", "revenue": "$1B+"},
    }
    info = mock_data.get(domain, {"industry": "Unknown", "size": "N/A", "revenue": "N/A"})
    return json.dumps(info)
```

#### Tool 2: CRM History Check

```python
def check_crm_history(email: str) -> str:
    """Simulates querying a CRM system like Salesforce"""
    mock_data = {
        "jane@acmecorp.com": {"last_contact": "2025-11-15", "status": "Cold Lead", "notes": "Attended webinar, no follow-up yet."},
        "bob@widgetco.net": {"last_contact": "2025-12-01", "status": "Active Opportunity", "notes": "Discussed Q1 budget and product integration."},
    }
    history = mock_data.get(email, {"last_contact": "N/A", "status": "No Record", "notes": "New lead, first contact opportunity."})
    return json.dumps(history)
```

#### Tool 3: Lead Score Calculator

```python
def calculate_lead_score(data_summary: str) -> str:
    """Analyzes collected data to assign High/Medium/Low priority"""
    data = json.loads(data_summary)
    score = "Low"
    
    if data["domain_info"].get("revenue", "").startswith("$1B+"):
        score = "High"
    elif data["crm_history"].get("status") == "Active Opportunity":
        score = "High"
    elif data["domain_info"].get("revenue", "").startswith("$50M"):
        score = "Medium"
    
    return json.dumps({"lead_score": score})
```

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
        # THINK: Send to model
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
                
                # Execute the function
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

### Test Scenarios

**Scenario 1: Jane @ AcmeCorp** (High-value enterprise)
- Domain: acmecorp.com → Software/SaaS, $50M-$100M revenue
- CRM: Cold Lead, attended webinar
- Score: **Medium**

**Scenario 2: Bob @ WidgetCo** (Active deal)
- Domain: widgetco.net → Manufacturing, $10M-$25M revenue
- CRM: Active Opportunity
- Score: **High** (due to active opportunity status)

---

## 6. CSV FAQ Agent (Stub File)

**File:** `6. Hello_Agent_CSV_FAQ_Agent_(Stub_File).ipynb`

### Overview

This is a **hands-on exercise** (stub file with TODOs) where students build a multi-file FAQ agent using LangChain's Pandas DataFrame Agent.

### What It Does

1. Downloads 4 CSV files from Google Drive:
   - `saas_docs.csv` - SaaS documentation
   - `credit_card_terms.csv` - Credit card terms
   - `hospital_policy.csv` - Hospital policies
   - `ecommerce_faqs.csv` - E-commerce FAQs

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

---

### Part 2: AI Agent Setup

#### Load All CSVs

```python
dataframes = []
for filename in files_to_download.keys():
    df = pd.read_csv(filename)
    dataframes.append(df)
```

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

---

### TODOs for Students

#### TODO 1: Initialize the LLM

```python
# Replace None with:
llm = ChatOpenAI(
    api_key=api_key,
    model="gpt-4o-mini",
    temperature=0.0
)
```

#### TODO 2: Create the Pandas Agent

```python
agent = create_pandas_dataframe_agent(
    llm,
    dataframes,  # <-- Pass the list of DataFrames here
    verbose=True,
    agent_type="openai-functions",
    allow_dangerous_code=True
)
```

#### TODO 3: Invoke the Agent

```python
# In the chat loop, replace "..." with:
result = agent.invoke(final_query)
response = result['output']
```

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
