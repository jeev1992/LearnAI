# AI Finance Assistant

## Core Milestones

### 1. Initial Research & Architecture Design
---
### `1.  Study existing financial education platforms and robo-advisors`

#### 🎯 Objective

Understand what existing platforms offer so you can:

- ✅ Identify capabilities to replicate  
- ✅ Spot gaps you can fill  
- ✅ Define minimum viable features for your LangGraph-powered agentic system  

#### 🧪 Categories of Platforms to Study

| Type                    | Examples                                                                | Purpose                                         |
|-------------------------|-------------------------------------------------------------------------|-------------------------------------------------|
| **Financial Education** | Investopedia, Khan Academy (Finance), SEC Investor.gov                 | Teach core financial literacy concepts          |
| **Robo-Advisors**       | Vanguard Digital Advisor, Betterment, Wealthfront, INDmoney            | Help users plan and manage investments          |
| **Portfolio Analysis**  | Morningstar, Tickertape, Zerodha Coin                                  | Provide visual tools, metrics, and comparisons  |

#### 🔍 Key Capabilities to Analyze

| Capability              | Education Sites (e.g., Investopedia)          | Robo-Advisors (e.g., Betterment)               |
|-------------------------|-----------------------------------------------|------------------------------------------------|
| Core Concepts           | ✅ Articles, quizzes, glossaries               | ⚠️ Sometimes – mostly hidden in onboarding     |
| Portfolio Visualization | ❌ No                                          | ✅ Charts, allocations, performance             |
| Goal-Based Planning     | ❌ No                                          | ✅ Retirement, education, etc.                  |
| Risk Profiling          | ❌ No                                          | ✅ Questionnaires                               |
| Tax Planning            | ⚠️ Sometimes                                   | ✅ Tax-loss harvesting                          |
| Market Data             | ⚠️ Static only                                 | ✅ Real-time, news, trends                      |
| Personalization         | ❌ No                                          | ✅ Based on user profile                        |
| Explainability          | ✅ High transparency                           | ❌ Often black-box                              |

---

#### 🧱 What to Replicate in Your System

✅ Must-Haves (based on educational gaps)

- ✅ Explain concepts like **ETFs**, **diversification**, **SIP vs. lumpsum**
- ✅ Simulate **portfolio allocation** (pie charts, risk score)
- ✅ **Goal-based projection** (e.g., *“How much to save monthly for ₹5L in 5 years?”*)
- ✅ **Source attribution** (explain where knowledge came from)
- ✅ **Disclaimers** (educational, not investment advice)

💡 Optional (advanced features from robo-advisors)

- 🧠 **Risk tolerance analysis** (simple quiz-based)
- 📊 **Dynamic rebalancing suggestions**
- 🧾 **Tax education integration** (rule-based logic)

#### 🧭 Your Architecture Goals

Design a **modular, agent-driven architecture** using LangGraph.

| Component              | Tool                                | Agent Name       |
|------------------------|-------------------------------------|------------------|
| Concept Q&A (RAG)      | LangChain + FAISS                   | `qna_agent`      |
| Portfolio Analyzer     | pandas or NumPy + charting libs     | `portfolio_agent`|
| Market Data Fetcher    | Alpha Vantage or yfinance API       | `market_agent`   |
| Goal Planner           | SIP/Compounding calculator          | `goal_agent`     |
| Router                 | Prompt + classification logic       | `router_node`    |
| UI                     | Streamlit                           | —                |
| Memory & Routing       | LangGraph                           | `StateGraph`     |

#### 📐 Sample Architecture Diagram (Conceptual)
```
            +--------------------------+
            |     User Input (Chat)    |
            +--------------------------+
                        |
                [LangGraph Router]
                        |
   +---------+----------+-----------+-----------+
   |         |                      |           |
[qna_agent] [portfolio_agent] [market_agent] [goal_agent]
   |         |                      |           |
+--------+ +----------------+ +-----------+ +---------------+
| RAG    | | Portfolio Calc | | API Fetch | | SIP Proj Calc |
+--------+ +----------------+ +-----------+ +---------------+

                        ↓
              [LangGraph State Update]
                        ↓
             +--------------------------+
             | Streamlit Chat + Charts |
             +--------------------------+
```

### `2. Research LangChain / LangGraph / CrewAI Multi-Agent Architectures`

#### 🎯 Objective

Understand how different multi-agent orchestration frameworks work so you can:

- ✅ Select the best tool for **modular, stateful, and explainable agent systems**
- ✅ Learn orchestration patterns (routing, memory, tool-use)
- ✅ Implement reusable agents with robust control flow

#### 🧪 Comparison: LangChain vs. LangGraph vs. CrewAI

| Feature / Tool        | **LangChain**                            | **LangGraph**                                        | **CrewAI**                                      |
|-----------------------|-------------------------------------------|------------------------------------------------------|--------------------------------------------------|
| **Core Use Case**     | LLM pipelines, tools, memory              | Multi-agent **stateful workflows** (graphs)         | Human-like multi-agent collaboration             |
| **Routing**           | Manual (via if-else or RouterChain)      | ✅ Declarative via `StateGraph`                     | Natural-language task delegation                 |
| **Memory**            | Individual memory classes                 | ✅ Global, centralized state (TypedDict)            | Local context or shared task queue               |
| **Inter-Agent State** | 🟡 Ad-hoc via context passing             | ✅ TypedDict shared state                           | 🟡 Weak - mostly persona-driven                  |
| **Custom Control Flow**| 🟡 Limited                               | ✅ Graph logic: loops, fallback, retry              | ❌ Limited (sequential only)                     |
| **Agent Modularity**  | ✅ via Chains/Tools                       | ✅ via Runnable nodes                               | 🟡 Personas with some tools                      |
| **Best For**          | Tool chaining, quick prototypes           | Complex workflows, AI systems                       | Team-style task simulation                       |

#### ✅ When to Use Which?

| Use Case                                 | Best Tool     |
|------------------------------------------|---------------|
| Retrieval-based Q&A                      | LangChain     |
| Stateful multi-agent workflow            | **LangGraph** |
| Agent team (CEO, PM, Dev-style tasks)    | CrewAI        |
| Explicit routing and fallback            | **LangGraph** |
| One-off function calling chains          | LangChain     |

#### 🧱 Why LangGraph Fits This Project Best

Your system needs:

- Multiple agents (Q&A, Portfolio, Market, Goal)
- Central state (user input, portfolio, memory, etc.)
- Conditional routing + fallback
- Modularity and debugging support

✅ **LangGraph is ideal** because:
- Typed state schema (`TypedDict`) for memory and transitions  
- Every agent is a `Runnable` — testable, reusable  
- Full control over flow: retries, branching, fallbacks  
- Easy Streamlit integration using `graph.invoke()`  

#### ❌ Why CrewAI Is Not Suitable (With Examples & Intuition)

CrewAI is an exciting tool that simulates **human-like multi-agent collaboration**, but it's not a good fit for a **production-ready, stateful AI Finance Assistant** built with structured agent orchestration.

#### 🧠 What Is CrewAI Designed For?

CrewAI excels at:
- 🤖 Simulating a *team* of agents (e.g., CEO, Analyst, Developer)
- 🗣 Natural-language task delegation ("Research this", "Write that")
- 🧪 Loose, creative, human-like collaboration

Example use cases:
- Market research reports  
- Team brainstorming simulations  
- Fictional company simulations  

#### ⚠️ Why It Doesn’t Fit Your Use Case

##### 🔸 1. No Global, Structured State
---

**Your Need:**  
A shared `FinanceAssistantState` (`TypedDict`) that all agents can read/write — e.g., `user_query`, `portfolio_data`, `goal_result`.

**CrewAI Limitation:**  
Each agent holds its own memory — there is **no centralized state** between agents.

🧠 Example:
- You can't pass `portfolio_data` from the portfolio agent to the goal planner.
- You can't store intermediate outputs for reuse or debugging.

##### 🔸 2. No Conditional Routing or Fallback Logic
---

**Your Need:**  
Control flow like:

```text
If user query is about SIP → call goal_agent  
If portfolio is missing → fallback with error  
If API fails → retry or use cached response
```

CrewAI Limitation:

- No if-else branching
- No graph-like control over agent flow
- No fallbacks or retry mechanisms

🧠 LangGraph supports:

```python
if state["next_agent"] == "goal_agent":
    transition_to("goal_agent")
else:
    transition_to("fallback")
```
CrewAI does not.

##### 🔸 3. Not Tool-Oriented or Chain-Friendly
---

**Your Need:**  
Integrate external tools and APIs across modular agents:

- 🧠 FAISS + LangChain retriever in `qna_agent`  
- 📈 yfinance API in `market_agent`  
- 📊 pandas logic in `portfolio_agent`  

**CrewAI Limitation:**  
- ❌ Not designed for tool execution or LangChain Chains  
- ❌ Tool usage must be injected via prompts (brittle and error-prone)  
- ❌ No native support for `Runnable`, `Tool`, or `Chain` abstractions  
- ❌ Difficult to test or reuse agents as functional units  

##### 🔸 4. Output Is Probabilistic, Not Deterministic
---

**Your Need:**  
Consistent, structured outputs for:

- 📊 Charts and dashboards  
- 🧾 Streamlit UI rendering  
- 🧪 Reproducible analysis across runs  

**CrewAI Limitation:**  
- ❌ Agents chat with each other in freeform  
- ❌ Results vary across runs — high variance  
- ❌ No structured or typed data output  
- ❌ Output parsing becomes fragile and error-prone  

🧠 **Example:**  
“Developer” might say:  
> *"I guess you should invest ₹5,000/month."*  

But…  
- How do you extract `5000`?  
- How do you verify or visualize it?  
- What if next time it says `₹6,000`?

#### 🤖 Concrete Comparison Example

| Task                                   | ✅ **LangGraph**                                | ❌ **CrewAI**                                      |
|----------------------------------------|--------------------------------------------------|----------------------------------------------------|
| “How much to invest monthly?”          | Router → `goal_agent` → SIP calculator → state  | Planner chats with Researcher → vague estimate     |
| Fetch stock prices (e.g., yfinance)   | `market_agent` calls API                        | Developer "thinks about" fetching data             |
| Retry if portfolio is missing         | `fallback_node` returns graceful message        | ❌ Not supported                                    |
| Display bar chart from agent output   | Use Streamlit with `state["portfolio_data"]`    | ❌ Chat-based only — no structured output           |

#### 📌 Summary: LangGraph vs. CrewAI

| Feature                     | ✅ **LangGraph**                        | ❌ **CrewAI**                          |
|-----------------------------|----------------------------------------|----------------------------------------|
| Centralized memory/state    | `TypedDict` shared across agents       | Each agent has isolated memory         |
| Tool / chain integration    | LangChain `Runnable`, `Tool`, `Chain` | Prompt hacking only                    |
| Conditional flow / routing  | Full control via graph transitions     | Linear or cyclic only — no logic paths |
| Error handling / retries    | Built-in with fallback nodes           | ❌ Not supported                        |
| Reusability & testing       | Modular, testable agent units          | No unit boundaries — hard to test      |
| Output for dashboards       | Structured data (Streamlit ready)      | Unstructured text replies              |


#### ✅ Intuition Recap

**Use `LangGraph` for:**  
> "Deterministic, stateful agent workflows that behave like APIs."

**Use `CrewAI` for:**  
> "Simulating a fictional startup team discussing a topic together."

### `3. Design System Architecture and Agent Communication Protocols`

#### 🎯 Objective

Design a modular, scalable, and testable architecture for your AI Finance Assistant, ensuring:

- ✅ Clear separation between agents, state, and orchestration logic
- ✅ Robust inter-agent communication
- ✅ Deterministic outputs for integration with UI and metrics
- ✅ Production-ready design (fallbacks, retries, logging)

#### 🧱 High-Level System Components

| Component               | Responsibility                                         |
|-------------------------|--------------------------------------------------------|
| 🧠 LangGraph (StateGraph)| Orchestrates agent flow and manages shared state       |
| 📚 QnA Agent             | Handles conceptual financial queries using RAG         |
| 📈 Portfolio Agent       | Parses and analyzes user portfolios                    |
| 📊 Market Agent          | Fetches real-time market data using APIs              |
| 🎯 Goal Agent            | Projects future value / SIP amounts based on inputs   |
| 🧠 Router Node           | Determines which agent to route the query to           |
| 🪪 Fallback Agent        | Catches errors or unsupported requests gracefully      |
| 💬 Streamlit UI          | Chat interface and dashboard visualizations           |
| 📦 Data Store (optional) | Stores sample articles, glossary, and portfolio data   |
---

#### 📡 Agent Communication Protocol

Agents are **loosely coupled** and interact only via the **centralized state** defined by `FinanceAssistantState`.

##### 🧠 Central State: `FinanceAssistantState`

Each agent receives and updates this shared state:

```python
class FinanceAssistantState(TypedDict, total=False):
    user_query: str
    next_agent: Optional[str]
    agent_response: Optional[str]
    conversation_history: List[Dict[str, str]]
    portfolio_data: Optional[Dict]
    market_data: Optional[Dict]
    goal_plan_result: Optional[Dict]
    rag_docs: Optional[List[str]]
    error: Optional[str]
```

#### 🔄 Agent Execution Flow


**🔹 Router Node**
- Reads `user_query` from the incoming state  
- Classifies intent (via keyword matching or LLM-based classifier)  
- Sets `state["next_agent"] = "goal_agent"` or any other appropriate agent  

**🔹 Selected Agent Node**
- Executes core logic:
  - Retrieval (e.g., via RAG)
  - Computation (e.g., SIP calculator)
  - API calls (e.g., yfinance)
- Updates:
  - `state["agent_response"]`
  - (Optional) `portfolio_data`, `goal_plan_result`, etc.

**🔹 Streamlit UI**
- Displays latest `agent_response`
- Renders interactive charts based on structured state (e.g., pie charts, line graphs)

---
#### 📬 Communication Pattern

- Agents **do not call each other directly**
- **Routing and memory flow** through the centralized LangGraph `state`

This architecture enables:

- ✅ Decoupled agent design  
- ✅ Clear debug traces via state logs  
- ✅ Retry/fallback without cross-agent coupling  


#### 🔁 Retry & Fallback Strategy

| Scenario                        | Behavior                                      |
|----------------------------------|-----------------------------------------------|
| API failure in `market_agent`    | Try cached response or fallback message       |
| Missing portfolio in state       | `portfolio_agent` triggers `fallback_agent`   |
| Unrecognized user intent         | `router_node` routes to `fallback_agent`      |

##### 🔎 Debugging & Observability

- 🪵 Use **LangGraph logs** to trace the evolution of state at each node
- Each agent should log:
  - ✅ Input extracted from `state`
  - ✅ Output updates written back to `state`
  - ❗️ Errors or exceptions stored in `state["error"]`

#### ✅ Design Principles Summary

| Principle               | Implementation                                          |
|-------------------------|----------------------------------------------------------|
| 🔁 Stateless Agents      | Operate via pure functions using input/output state      |
| 📦 Shared State Model    | Central `FinanceAssistantState` passed across nodes     |
| 🧱 Modular Agents        | Each agent is a reusable, testable `RunnableLambda`     |
| 🧠 Explicit Routing      | Handled via `router_node` using intent classification    |
| 💬 Explainable Outputs   | Responses include structured text + source attribution  |
| 🧪 Testability           | All agents and router are independently unit-testable    |
| 🧩 UI-Ready              | Streamlit reads from `state` for charts and responses    |

#### ✅ Next Step

- [ ] Finalize your `FinanceAssistantState` schema  
- [ ] Implement `router_node` for intent classification  
- [ ] Build modular `Runnable` agents (`qna_agent`, `portfolio_agent`, etc.)  
- [ ] Define all LangGraph edges and fallback transitions  
- [ ] Connect LangGraph output with Streamlit UI for full loop  

---

### 2. Knowledge Base Development
---

### `1. Curate 50–100 Financial Education Articles Covering Basics`

#### 🎯 Objective

Build a strong, beginner-friendly knowledge base to support your RAG-powered `qna_agent`, covering core financial topics like:

- 📈 Stocks, Bonds, ETFs, SIPs  
- 💰 Compound Interest, Inflation, Risk  
- 📊 Diversification, Asset Allocation  
- 🧾 Tax-saving instruments  
- 💡 Financial goal setting  

The curated documents will be **embedded**, **indexed**, and **retrieved** using a vector store like FAISS.

#### 🧪 Sources to Use

| Source                   | URL                                                 | Notes                               |
|--------------------------|-----------------------------------------------------|--------------------------------------|
| **Investopedia**         | https://www.investopedia.com                       | High-quality, concept-focused        |
| **Khan Academy (Finance)** | https://www.khanacademy.org/economics-finance-domain | Great for structured topic breakdown |
| **Bogleheads Wiki**      | https://www.bogleheads.org/wiki/Main_Page          | Ideal for passive investing basics   |
| **SEC Investor.gov**     | https://www.investor.gov                           | U.S.-centric, but reliable           |
| **Groww Learn**          | https://groww.in/p/learn                           | India-specific investing education   |
| **Zerodha Varsity**      | https://zerodha.com/varsity                        | Deep and visual explanation of basics|


#### 📄 Target Content Format

You can extract and save each article in plain `.txt` or `.md` format, like this:

```txt
# What is an ETF?

An ETF (Exchange-Traded Fund) is a basket of securities that trades on an exchange...

Tags: [etf, investing, passive, index]
Source: Investopedia
```
⚠️ Keep content educational, avoid including specific advice or promotional material.

#### 📦 Directory Structure (Example)
```bash
/data/financial_articles/
├── etfs_basics.md
├── diversification_vs_risk.txt
├── sip_vs_lumpsum.txt
├── compound_interest.md
├── asset_allocation_strategies.md
└── glossary.json
```

##### 📌 Curation Guidelines

| Guideline                       | Why It Matters                                      |
|----------------------------------|-----------------------------------------------------|
| 🧠 Choose beginner-friendly tone | Ensures QnA responses are understandable to all     |
| 📚 Structure by category         | Helps with document chunking and semantic indexing  |
| 🔖 Tag metadata (topics, source) | Enables filtered retrieval and source attribution   |
| 📄 Use Markdown or plain text    | Easy to embed, parse, and debug                    |
| ⚠️ Avoid PDF or HTML clutter     | Noise degrades embedding and chunking quality      |
| ✅ Clean grammar and format      | Prevents retrieval errors and improves UX          |

---

##### 🧠 Example Topics to Include

| Category         | Articles to Include                                                  |
|------------------|-----------------------------------------------------------------------|
| **Basics**       | What is a stock? What is an ETF? What is inflation?                  |
| **Investing**    | SIP vs. Lumpsum, Mutual Funds, Index Investing                       |
| **Risk Management** | Diversification, Asset Classes, Volatility                        |
| **Tax Planning** | ELSS, PPF, Section 80C benefits, Capital Gains Tax                   |
| **Goal Planning**| Retirement Planning, Child Education Fund                            |
| **Tools & Terms**| NAV, CAGR, IRR, Risk Score, Alpha/Beta                               |

---

### 3. Core Agent Implementation
---

### `1. Implement Base Agent Class with Common Functionality`

#### 🎯 Objective

Establish a reusable base class for all LangGraph agents to:

- ✅ Promote modular, testable, and DRY agent design  
- ✅ Centralize shared behaviors (e.g., logging, response formatting, error handling)  
- ✅ Ensure consistent state updates across all agents  
- ✅ Make it easy to plug into LangGraph as a `RunnableLambda`  


#### 🧱 Why Use a Base Agent Class?

| Benefit               | Description                                                            |
|------------------------|------------------------------------------------------------------------|
| 🧠 Shared logic         | Standardize how agents process state and produce output                |
| 🔁 Stateless pattern     | Each agent acts on `state`, not on internal memory                    |
| 🧪 Testability          | Easy to test agent logic in isolation                                  |
| 🧩 Plug-and-play ready  | Compatible with LangGraph and LangChain `Runnable` design pattern      |
| 📦 Extendable           | Can easily add logging, error handling, tool support later             |

---

#### ⚙️ Base Agent Design (Python Template)

```python
from typing import Dict, Any
from langchain_core.runnables import RunnableLambda

class BaseAgent:
    def __init__(self, name: str):
        self.name = name

    def run(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        To be overridden by child agent. Takes full state and returns updated state.
        """
        raise NotImplementedError("Subclasses must implement `run()`")

    def as_runnable(self) -> RunnableLambda:
        return RunnableLambda(self.run)

    def update_state(self, state: Dict[str, Any], response: str, updates: Dict[str, Any] = {}) -> Dict[str, Any]:
        new_state = {
            **state,
            "agent_name": self.name,
            "agent_response": response,
            **updates
        }
        return new_state
```

#### 📌 How to Use This Base Class
Each specific agent subclass (e.g., QnA Agent, Portfolio Agent) will:

- Inherit from BaseAgent
- Implement the run() method
- Use self.update_state(...) to return LangGraph-compatible output

#### 🤖 Example: QnA Agent

```python
class QnAAgent(BaseAgent):
    def __init__(self, qa_chain):
        super().__init__("qna_agent")
        self.qa_chain = qa_chain  # LangChain RetrievalQA

    def run(self, state: Dict[str, Any]) -> Dict[str, Any]:
        query = state["user_query"]
        try:
            result = self.qa_chain.run(query)
            return self.update_state(state, result)
        except Exception as e:
            return self.update_state(state, f"Error: {str(e)}", {"error": str(e)})
```

Then wrap it as a LangGraph node:

```python
qna_agent = QnAAgent(qa_chain)
graph.add_node("qna_agent", qna_agent.as_runnable())
```

🧪 Testability Example

```python
def test_qna_agent():
    agent = QnAAgent(dummy_chain)  # pass a mock or fake RetrievalQA
    state = {"user_query": "What is an ETF?"}
    result = agent.run(state)
    assert "agent_response" in result
    assert result["agent_name"] == "qna_agent"
```

#### ✅ Next Step
- Implement BaseAgent class
- Create agent subclasses: QnAAgent, PortfolioAgent, MarketAgent, GoalAgent
- Wrap each as RunnableLambda for use in LangGraph
- Add unit tests for each agent with mock inputs

---
### `2. Develop Finance Q&A Agent with RAG Integration`


#### 🎯 Objective

Build a Q&A agent that answers conceptual finance questions by retrieving relevant content from your curated knowledge base using **RAG** (Retrieval-Augmented Generation).

This agent will:
- ✅ Accept natural-language queries
- ✅ Retrieve relevant documents (e.g., from FAISS or Chroma)
- ✅ Generate a grounded response using LangChain’s `RetrievalQA`
- ✅ Return structured output to LangGraph state

---

#### 📦 Components Required

| Component             | Technology          | Purpose                                   |
|------------------------|---------------------|--------------------------------------------|
| Embedding model        | OpenAI or HuggingFace | Convert text to vector form                |
| Vector store           | FAISS / Chroma       | Store and retrieve document chunks         |
| Retriever              | LangChain retriever  | Finds semantically relevant documents      |
| LLM                    | OpenAI / Gemini / Claude | Generates answer from retrieved docs   |
| RAG chain              | LangChain `RetrievalQA` | Wraps retriever + LLM into Q&A agent   |

##### ✅ Output Format in State

| Key              | Description                                         |
|------------------|-----------------------------------------------------|
| `agent_response` | Answer generated by the LLM                         |
| `rag_docs`       | List of document sources for attribution            |
| `agent_name`     | Set to `"qna_agent"`                                |
| `error` (optional) | Populated if retrieval or LLM call fails           |

---

##### 📌 Best Practices

| Recommendation                    | Why                                                |
|-----------------------------------|-----------------------------------------------------|
| ✅ Use chunk size 400–600         | Balances context richness and retrieval accuracy    |
| ✅ Use `k=3` in retriever          | Keeps responses concise and grounded                |
| ⚠️ Handle empty query / no match | Return default fallback from agent                 |
| 💬 Source attribution             | Increases explainability and user trust             |
| 🧪 Write unit tests               | Covers correct and malformed input scenarios        |

---

### `3. Build Portfolio Analysis Agent with Calculation Capabilities`

#### 🎯 Objective

Design an agent that analyzes a user’s portfolio (e.g., assets, weights, returns), computes insights like risk exposure and diversification, and outputs structured data for charts in the UI.

This agent will:
- ✅ Read portfolio data from state
- ✅ Perform calculations using `pandas` or `NumPy`
- ✅ Return a summary + structured results (e.g., risk score, allocation breakdown)
- ✅ Power pie/bar charts in Streamlit

---

#### 📦 Required Inputs (from state)

| Key                | Description                                          |
|---------------------|------------------------------------------------------|
| `portfolio_data`    | List of holdings with name, weight, category, etc.   |
| `user_query`        | Optional, to customize response tone/context         |

Example `portfolio_data`:

```json
[
  {"asset": "Nifty 50 ETF", "weight": 60, "type": "Equity"},
  {"asset": "PPF", "weight": 20, "type": "Debt"},
  {"asset": "Gold ETF", "weight": 20, "type": "Commodity"}
]
```

##### ⚙️ Core Features

| Feature                 | Description                                                 |
|--------------------------|-------------------------------------------------------------|
| ✅ Allocation summary    | Total % per asset class (Equity, Debt, etc.)                |
| ✅ Risk scoring          | Simple rules-based score (0–100) based on equity %          |
| ✅ Imbalance detection   | Warn if asset weights don’t sum to 100%                     |
| ✅ Response generation   | Returns `agent_response` + `portfolio_metrics`              |

---

#### 🧠 Sample Computation Logic (Python)

```python
import pandas as pd

def analyze_portfolio(portfolio_data: list[dict]) -> dict:
    df = pd.DataFrame(portfolio_data)
    df["weight"] = df["weight"].astype(float)
    
    allocation = df.groupby("type")["weight"].sum().to_dict()
    total_weight = df["weight"].sum()
    
    risk_score = round(allocation.get("Equity", 0) * 1.2)
    risk_score = min(risk_score, 100)

    imbalance_flag = abs(total_weight - 100) > 5

    return {
        "allocation": allocation,
        "risk_score": risk_score,
        "imbalance": imbalance_flag
    }

```

##### ✅ Output Format in State

| Key                | Description                                         |
|---------------------|-----------------------------------------------------|
| `agent_response`    | Text summary for the user                          |
| `portfolio_metrics` | Dict with `allocation`, `risk_score`, etc.         |
| `agent_name`        | Set to `"portfolio_agent"`                         |
| `error` (optional)  | Captures any failure (e.g., missing data, exception) |

---

##### 📌 Best Practices

| Practice                      | Why                                                    |
|-------------------------------|--------------------------------------------------------|
| ✅ Enforce weight normalization | Prevent user errors in input                          |
| 💬 Use tone consistent with agent | Avoid abrupt/robotic feedback                      |
| 🧱 Return structured metrics     | Makes frontend charting easy                         |
| 🧪 Validate numeric values       | Avoid float conversion errors                        |
| ⚠️ Handle empty/invalid state   | Return helpful fallback messages                     |

---

#### To get portfolio_data, you have 3 main options, depending on your use case and user experience goals. Since you're building an AI Finance Assistant with LangGraph + Streamlit, here's a breakdown of all three with production-level reasoning:

#### ✅ Option 1: 🧑‍💼 User-Enters-Portfolio (Simplest MVP)
Let users manually enter or paste their portfolio holdings via a Streamlit form:

```python
import streamlit as st
import json

st.subheader("🧾 Enter Your Portfolio Holdings")

default_input = """[
  {"asset": "Nifty 50 ETF", "weight": 60, "type": "Equity"},
  {"asset": "PPF", "weight": 20, "type": "Debt"},
  {"asset": "Gold ETF", "weight": 20, "type": "Commodity"}
]"""

portfolio_json = st.text_area("Paste your portfolio data (JSON format):", value=default_input)

if st.button("Submit Portfolio"):
    try:
        portfolio_data = json.loads(portfolio_json)
        st.session_state["portfolio_data"] = portfolio_data
        st.success("✅ Portfolio submitted!")
    except Exception as e:
        st.error(f"❌ Invalid JSON: {e}")
```

Then send `st.session_state["portfolio_data"]` into LangGraph's state:

```python
langgraph_input = {
    "user_query": "Analyze my portfolio",
    "portfolio_data": st.session_state.get("portfolio_data", [])
}
```

#### ✅ Option 2: 📁 Upload CSV or Excel (For real-world users)

Let users upload a file with their holdings:

```python
uploaded_file = st.file_uploader("Upload portfolio file (CSV/Excel)")

if uploaded_file:
    import pandas as pd
    df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)
    
    # Validate columns: asset, weight, type
    if set(df.columns).issuperset({"asset", "weight", "type"}):
        portfolio_data = df.to_dict(orient="records")
        st.session_state["portfolio_data"] = portfolio_data
        st.success("✅ Portfolio uploaded and parsed!")
    else:
        st.error("❌ Missing required columns: asset, weight, type")
```

##### ✅ Option 3: 🔗 Integrate with APIs (Advanced Phase)

In future versions, you can auto-fetch portfolios via third-party APIs and services for a seamless, real-world experience.

| Platform           | Method                                                     |
|--------------------|-------------------------------------------------------------|
| **Zerodha / Kite** | Use [Kite Connect API](https://kite.trade) to fetch user holdings (requires OAuth, tokens, rate limits apply) |
| **INDmoney**       | ⚠️ No public API — scraping possible but brittle and legally risky |
| **Google Sheets**  | Use `gspread` with Google OAuth or Apps Script to read structured sheets with asset info |
| **Wealth API**     | Use Indian fintech aggregators like **Yodlee**, **Fintso**, or **Finbox** (if accessible) |

---

> ⚠️ **Caution**  
Always implement **secure OAuth2-based authentication**, encrypt API tokens, and **log access securely** when integrating with real financial data sources.

---

##### 📌 Future Feature Ideas

- [ ] Sync with Zerodha portfolio daily  
- [ ] Import from Google Sheets via URL or file picker  
- [ ] View real-time prices alongside stored portfolio  
- [ ] Compare actual vs. suggested asset allocations  

---

### `4. Create Market Analysis Agent with API Integration`

#### 🎯 Objective

Design a `market_agent` that fetches **real-time stock/index prices**, company metadata, or recent market indicators using public APIs such as **`yfinance`** or **Alpha Vantage**.

This agent will:
- ✅ Read target symbols from user query or state
- ✅ Fetch current price, daily % change, and basic metadata
- ✅ Output structured info in `market_data` for Streamlit charts

---

#### 📦 Inputs Required (from state)

| Key              | Description                            |
|------------------|----------------------------------------|
| `user_query`     | Natural language input (e.g., "Get TCS price") |
| `ticker_symbols` | Optional list of ticker codes (e.g., ["TCS.NS"]) |

If not explicitly provided, agent can extract ticker names via LLM-based regex or fuzzy mapping.

---

#### 🌐 API Options

| API            | Notes                                                                 |
|----------------|-----------------------------------------------------------------------|
| `yfinance`     | ✅ Free, supports Indian stocks (e.g., `TCS.NS`, `RELIANCE.NS`)        |
| Alpha Vantage  | Requires free API key, more control (intraday, fundamentals, etc.)    |

We’ll use `yfinance` for simplicity and broad symbol coverage.

---

#### ⚙️ Sample Data Fetch Logic

```python
import yfinance as yf

def fetch_market_data(tickers: list[str]) -> dict:
    result = {}
    for symbol in tickers:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        result[symbol] = {
            "name": info.get("shortName", symbol),
            "price": round(info.get("regularMarketPrice", 0), 2),
            "change_percent": round(info.get("regularMarketChangePercent", 0), 2),
            "currency": info.get("currency", "INR")
        }
    return result
```

---

### 4. Advanced Agent Development
---
### `1.  Implement Goal Planning Agent with Projection Algorithms`


#### 🎯 Objective

Design a `goal_agent` that answers queries like:

- “How much to invest monthly to reach ₹10L in 10 years?”
- “What will ₹5,000/month grow to in 15 years at 12%?”
- “How much corpus can I expect by age 60?”

It uses financial projection formulas (SIP, compounding) to calculate outcomes and return both a clear response and structured values for UI display.

---

#### 📦 Required Inputs (from state)

| Key              | Description                                                  |
|------------------|--------------------------------------------------------------|
| `user_query`     | Freeform question from user (e.g., "How much for 1 crore in 10 years?") |
| `goal_details`   | Optional dict with parsed goal parameters                    |

---

#### 🔣 Projection Logic (SIP formula)

**Future Value (FV) of SIP:**

\[
FV = P \times \frac{(1 + r)^n - 1}{r} \times (1 + r)
\]

Where:

- `P` = monthly investment  
- `r` = monthly interest rate (annual / 12 / 100)  
- `n` = number of months (years × 12)  

You can also reverse it to solve for `P` if the goal is to reach a fixed corpus.

---

#### 🧠 Projection Utilities

```python
def sip_future_value(monthly_invest: float, years: int, annual_rate: float) -> float:
    r = annual_rate / 12 / 100
    n = years * 12
    fv = monthly_invest * (((1 + r)**n - 1) / r) * (1 + r)
    return round(fv)

def sip_required_amount(target: float, years: int, annual_rate: float) -> float:
    r = annual_rate / 12 / 100
    n = years * 12
    p = target / (((1 + r)**n - 1) / r / (1 + r))
    return round(p)
```

#### ✅ Output Format in State

| Key                 | Description                                                |
|----------------------|------------------------------------------------------------|
| `agent_response`     | Text summary of result                                     |
| `goal_plan_result`   | Dict with `monthly_investment` or `future_value`           |
| `agent_name`         | Set to `"goal_agent"`                                      |
| `error` (optional)   | Captures any failure during projection computation         |

---

#### 🧪 Example Input & Output

**State Input:**

```json
{
  "goal_details": {
    "mode": "target_corpus",
    "target_amount": 1000000,
    "years": 10,
    "annual_rate": 12
  }
}
```

**Output:**

```json
{
  "agent_response": "To reach ₹10,00,000 in 10 years at 12% annual return, invest ₹4,900 monthly.",
  "goal_plan_result": {
    "monthly_investment": 4900
  }
}
```

---

#### `2. Test Inter-Agent Communication`

#### 🎯 Objective

Verify that agents communicate **indirectly through the shared LangGraph state**, by simulating sequential agent execution:

- ✅ Validate correct routing from `router_node`
- ✅ Ensure downstream agent (e.g., `goal_agent`) can read and act on updated state
- ✅ Confirm final state contains all expected outputs

---

#### 🧪 Example: `router_node` → `goal_agent`

```python
from agents.router import RouterNode
from agents.goal_agent import GoalAgent

# Step 1: Simulate a user input
initial_state = {
    "user_query": "How much should I invest monthly to reach 10 lakh in 10 years?"
}

# Step 2: Router decides the next agent
router = RouterNode()
state_after_routing = router.run(initial_state)

# Step 3: Goal agent reads from the shared state
goal_agent = GoalAgent()
final_state = goal_agent.run(state_after_routing)

# Step 4: Inspect the result
print("Final State:")
print(final_state["agent_response"])
print(final_state["goal_plan_result"])
```

#### 🧪 Full Inter-Agent Unit Test

```python
def test_router_to_goal_agent():
    state = {
        "user_query": "Want 5 lakh in 5 years. How much monthly?",
    }

    # Route the query
    state = RouterNode().run(state)
    assert state.get("next_agent") == "goal_agent"
    assert "goal_details" in state

    # Compute goal planning
    state = GoalAgent().run(state)
    assert "agent_response" in state
    assert "goal_plan_result" in state
```

---

### 5. Workflow Orchestration  
---
### `1. Add Conversation Memory and Context Preservation`



#### 🎯 Objective

Enable the system to:

- 🧠 Maintain user context across multiple turns  
- 🧾 Refer back to prior queries or portfolio preferences  
- 🔁 Reuse state fields like `goal_details`, `portfolio_data`, etc.  

LangGraph supports **shared, persistent state** across agents, allowing **deterministic, explainable memory** without needing embeddings or chat history parsing.

#### 🧠 Memory Model

Use a central `FinanceAssistantState` dict that persists across agent invocations:

```python
from typing import TypedDict

class FinanceAssistantState(TypedDict, total=False):
    user_query: str
    next_agent: str
    agent_name: str
    agent_response: str
    error: str

    # Memory-like fields
    goal_details: dict
    goal_plan_result: dict
    portfolio_data: dict
    portfolio_metrics: dict
    market_data: dict
    rag_docs: list
```

### 🧠 Why You Need Centralized Memory (`FinanceAssistantState`)

LangGraph doesn’t use chat history or agent-to-agent communication.

Instead, all information is passed and preserved through a shared state object — your `FinanceAssistantState`.

---

#### ✅ 1. Agents Are Decoupled by Design

LangGraph encourages modular agents that don’t call each other directly.  
➡️ Shared memory (`state`) is the **only mechanism** for communication.

**Example:**  
If `goal_agent` computes an SIP projection, and `portfolio_agent` later wants to reflect this in the current plan — it reads `goal_plan_result` from state.

---

#### ✅ 2. Conversations Span Multiple Turns

Users don’t always give complete details up front.  
You need to preserve context for intelligent follow-up.

**Example flow:**

> **User:** How much to invest monthly for ₹10L in 10 years?  
> → Router → `goal_agent` → Updates `goal_plan_result`

> **User (next message):** What if I want ₹20L instead?  
> → `router_node` reuses old `goal_details`, changes only `target_amount`

No need to re-ask duration or return rate.

---

#### ✅ 3. Streamlit UI Requires Structured Memory

To show:

- 📊 Portfolio pie charts  
- 📈 Market price metrics  
- 🧮 SIP projections  

You must retain:

- `portfolio_metrics`  
- `market_data`  
- `goal_plan_result`  

These values live in `state` — not transient messages.

---

#### ✅ 4. Enables Retry, Fallback, and Debugging

LangGraph supports:

- `fallback_nodes`  
- Retry flows  
- Debugging broken nodes

All require a consistent, inspectable `state`.

**Example:**

If `market_agent` fails to fetch data, fallback can try cached data in:

```python
state.get("market_data_cache")
```

---

### 7. User Interface Development  
#### Build Conversational Chat Interface & Visual Dashboards

---

#### 🎯 Objective

Create a Streamlit-based frontend to:

- 💬 Chat with the assistant in natural language  
- 📊 Visualize portfolio analysis results  
- 📈 Show real-time market data  
- 🎯 Display goal-based investment projections  

---

#### 🖥️ Core UI Components

| Component                    | Description                                                   |
|------------------------------|---------------------------------------------------------------|
| `chat_box`                   | User input field for questions or commands                    |
| `chat_history_display`       | Scrollable log of Q&A exchanges                               |
| `portfolio_dashboard`        | Pie chart, risk score, and imbalance detection                |
| `market_overview`            | Price line chart and table using APIs like yfinance           |
| `goal_projection_display`    | Monthly SIP amount and goal visualization                     |

---

#### 💡 Best Practices

| Practice                              | Why It Matters                                          |
|----------------------------------------|----------------------------------------------------------|
| ✅ Use `st.session_state`               | Maintains conversation memory during reruns             |
| ✅ Modularize with `st.tabs`            | Organizes views: Chat | Portfolio | Market | Goals     |
| ✅ Show `state["agent_response"]`      | Ensures consistent LLM output presentation               |
| ✅ Use structured state for charts     | Enables robust visual rendering via `portfolio_metrics` etc. |
| ⚠️ Validate keys before rendering      | Prevents `KeyError` on missing agent output              |

---

#### 📊 Example: Portfolio Dashboard (Matplotlib)

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

if "portfolio_metrics" in state:
    st.subheader("Portfolio Allocation")
    data = state["portfolio_metrics"]["allocation"]
    df = pd.DataFrame(data.items(), columns=["Asset", "Weight (%)"])
    
    fig, ax = plt.subplots()
    ax.pie(df["Weight (%)"], labels=df["Asset"], autopct="%1.1f%%")
    st.pyplot(fig)

    st.metric("Risk Score", state["portfolio_metrics"]["risk_score"])
```

#### 📈 Example: Market Overview (yfinance)

```python
import yfinance as yf
import streamlit as st

data = yf.download("NIFTYBEES.NS", period="6mo")
st.line_chart(data["Close"])
```

#### 🧩 Layout with Tabs

```python
tab1, tab2, tab3, tab4 = st.tabs(["💬 Chat", "📊 Portfolio", "📈 Market", "🎯 Goal Plan"])

with tab1:
    show_chat_history()

with tab2:
    render_portfolio_dashboard()

with tab3:
    render_market_overview()

with tab4:
    render_goal_projection()
```

#### ✅ Agent Outputs Used by UI

| Agent             | Keys in `state` used for rendering         |
|-------------------|---------------------------------------------|
| `qna_agent`       | `agent_response`, `rag_docs`               |
| `portfolio_agent` | `portfolio_metrics`, `agent_response`      |
| `market_agent`    | `market_data`, `agent_response`            |
| `goal_agent`      | `goal_plan_result`, `agent_response`       |

---

#### 🧪 Optional: Developer Debug Panel

```python
with st.expander("🛠️ Debug: Raw LangGraph State"):
    st.json(state)
```