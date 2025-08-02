# 📞 Call Center Summarization App

## 🧩 1. Business Use Case

### 🧠 Problem Statement
Modern call centers generate massive volumes of audio recordings and chat transcripts from daily customer interactions. These are rich in **customer intent**, **agent performance indicators**, and **actionable business insights**, but:

- They are **long and unstructured**.
- **Manual processing** (by QA teams or analysts) is **slow, expensive, and subjective**.
- Real-time insight generation is almost impossible at scale.

#### 💬 Example
A telecom company handling **5,000 calls/day** would need dozens of human analysts to manually:
- Read full transcripts.
- Score agent performance.
- Write summaries.
- Check compliance.

This is time-consuming, inconsistent, and not scalable.

---

## 💡 The Business Opportunity

### 🔁 1. Automated Insight Extraction
**Goal**: Use LLM agents to generate accurate call summaries instantly, reducing human effort.

#### ✅ What It Solves
- Summarizes 10+ minute calls in seconds.
- Extracts key issues, resolution steps, and customer sentiment.
- Makes insights available across the organization.

#### 🛠 Example
**Before AI**:
> QA analyst listens to a 12-minute call and writes manually:  
> _“Customer complained about broadband disconnection. Agent promised technician visit. ETA: 48 hrs.”_

**After AI**:
```json
{
  "customer_issue": "Broadband not working since 2 days",
  "resolution": "Technician scheduled for visit",
  "agent_response": "Polite and informative",
  "next_action": "Field visit in 48 hours"
}
```

## 📈 2. QA Monitoring at Scale

### 🎯 Goal
Use LLMs to automatically score agents on key performance indicators like:

- **Empathy**
- **Clarity**
- **Tone**
- **Resolution**

### ✅ What It Solves
- Scales QA operations from **50 calls/day** to **5,000+ calls/day**
- Allows **human reviewers to focus only** on edge cases or low-scoring calls
- Reduces bias and increases the **objectivity** of agent evaluations

### 🛠 Example Output

```json
{
  "empathy_score": 0.9,
  "resolution_score": 0.8,
  "tone_score": 0.95,
  "compliance_flag": false
}
```

## 🎯 3. Consistency & Compliance

### 🎯 Goal
Standardize call evaluations using LLM agents to reduce **subjectivity** and avoid **human error**.

### ✅ What It Solves
- Applies the **same rubric to all interactions**, ensuring fairness
- Flags **compliance issues in real-time**
- Reduces **legal and reputational risk**

### 🛠 Example – QA Rubric Used by the Agent

- ✅ Was the agent respectful?
- ✅ Did the customer confirm the resolution?
- ❌ Was the call recording notice given?

### 🧠 AI Output:
> _“Agent failed to inform the customer about data recording policy.”_

This helps companies comply with **privacy regulations** (like GDPR) and internal audit policies.

---

## 🔊 4. Voice-to-Insights Pipeline

### 🎯 Goal
Create a fully automated pipeline that converts **raw audio → structured insights → dashboards or CRMs**

### ✅ What It Solves
- Unlocks insights trapped in **audio files**
- Enables **real-time call analytics**
- Integrates seamlessly with **CRMs**, **dashboards**, and **monitoring tools**

### 🛠 Pipeline Flow

```text
[Audio Input] 
   ↓ (Whisper STT)
[Transcript] 
   ↓ (Summarization Agent)
[Key Summary & Points] 
   ↓ (Scoring Agent)
[Scores + Flags] 
   ↓ 
[UI / Dashboard / CRM]
```

> This pipeline is **modular**, **scalable**, and works in **real-time or batch mode**.

---

## 🧾 Example Output

```json
{
  "customer_name": "John Doe",
  "call_date": "2025-07-25",
  "main_issue": "Unable to activate SIM",
  "resolved": true,
  "agent_scores": {
    "empathy": 0.85,
    "clarity": 0.88,
    "compliance": true
  }
}
```

## 📦 This Structured Data Can:

- 🗂️ Be stored in a **database**  
  _Examples: PostgreSQL, MongoDB, DynamoDB_

- 📊 Populate **dashboards**  
  _Examples: Power BI, Tableau, Streamlit, Grafana_

- 🚨 Trigger **alerts or automated workflows**  
  _Examples: Slack alerts if resolution score < 0.6, auto-escalation via Zapier_

---

## 🧠 Summary Table

| 💢 Problem                          | ✅ Solution via Agentic AI                          |
|------------------------------------|-----------------------------------------------------|
| Long calls, hard to digest         | Summarization agents extract core insights          |
| Manual QA is slow/inconsistent     | LLMs score agents across 1,000s of calls            |
| Subjectivity in compliance checks  | Rubric-based consistency with function-calling      |
| Data locked in voice               | Voice-to-Insights unlocks structured decision data  |

---

## 🏗️ 2. Technical Architecture

The system uses a **modular, multi-agent setup** powered by LLMs, transcription APIs, and orchestration tools. It is designed to convert raw audio calls into structured **summaries**, **QA scores**, and **business insights** — efficiently and at scale.

Each component is **loosely coupled** to promote maintainability, flexibility, and rapid integration with newer technologies.

---

### 🧩 Component-wise Breakdown

| 🧱 Component        | ✅ Primary Tech              | 🔁 Alternatives                  | 🎯 Purpose                                                 |
|--------------------|-----------------------------|----------------------------------|------------------------------------------------------------|
| **Multi-Agent System** | `LangGraph`, `CrewAI`       | AutoGen, Semantic Kernel         | Orchestrates agent flow (e.g., intake → transcribe → summarize → score) |
| **Language Models**    | `GPT-4`, `Claude`            | Gemini, Mistral                  | Understands/translates language; generates summaries & scores |
| **Transcription Engine** | `Whisper API`                | Deepgram, AssemblyAI             | Converts audio calls into accurate text transcripts        |
| **Summarization**     | `LangChain + Prompts`        | PromptLayer                      | Generates structured call summaries from transcripts       |
| **QA Scoring**         | `Function Calling + Pydantic` | Ragas, Guardrails                | Scores agents on empathy, tone, resolution, etc. using structured rubrics |
| **Web Interface**      | `Streamlit`                  | Gradio, Flask                    | Allows file uploads and displays transcript, summary, and QA insights |
| **Memory Layer**       | `LangGraph Memory`           | Redis, Postgres                  | Remembers context across calls; supports follow-up evaluations |
| **Control Plane (MCP)**| `LangSmith`, `Router`        | LiteLLM, Helicone                | Manages cost-efficient routing, logging, and fallback logic |

---

### 🧠 How It Works Together (Example Pipeline)

1. 🔊 **Audio File Uploaded** via Streamlit
2. 🧾 **Call Intake Agent** validates input format
3. 📝 **Transcription Agent** converts audio to text using Whisper
4. 🧠 **Summarization Agent** uses GPT-4 + LangChain to extract key points
5. 📈 **QA Scoring Agent** evaluates agent behavior using function calling + rubric
6. 🧭 **Routing Agent** manages fallback or reprocessing using LangGraph
7. 🗂️ **Memory Layer** stores results for future comparison/training
8. 📊 **Streamlit UI** displays:
    - Transcript
    - Summary
    - QA Scores
    - Flags or highlights

---

### 🛠️ Why This Stack?

| Objective                          | Tool Used                  | Why It's Ideal                                               |
|-----------------------------------|----------------------------|--------------------------------------------------------------|
| Modular Agent Control             | LangGraph, CrewAI          | Lightweight, agent-first, state-aware                        |
| Transcription Accuracy            | Whisper                    | Best open-source STT model; high accuracy in noisy data      |
| LLM Flexibility                   | GPT-4, Claude              | Supports function calling, strong contextual understanding   |
| Prompt Engineering & Structuring | LangChain + Pydantic       | Clean outputs, schema validation, structured pipelines       |
| QA at Scale                       | Function Calling + Rubrics | Ensures rubric-based scoring (e.g., empathy, resolution)     |
| UI Simplicity                    | Streamlit                  | Rapid prototyping; supports file uploads + live previews     |
| Memory & State Tracking           | LangGraph Memory           | Tracks context across calls/agents                           |
| Observability & Fallbacks         | LangSmith, Router          | Model monitoring, fallback rules, and prompt versioning      |

---

## 🤖 3. Agent Architecture

The system is designed around **modular AI agents**, each responsible for a specific task in the call processing pipeline. This follows the **single-responsibility principle** — making the system extensible, testable, and production-ready.

Each agent is implemented as a node in a `LangGraph` workflow and connected through routing logic.

---

### 🧠 Overview Table

| 🧾 Agent Name             | 🎯 Responsibility                                                                 |
|--------------------------|------------------------------------------------------------------------------------|
| **Call Intake Agent**     | Validates incoming input (audio or transcript), checks schema, extracts metadata |
| **Transcription Agent**   | Converts raw audio to clean text using Whisper or Deepgram                       |
| **Summarization Agent**   | Generates a concise, structured summary using GPT-4 or Claude                    |
| **Quality Scoring Agent** | Evaluates tone, empathy, and resolution using a rubric + function calling        |
| **Routing Agent**         | Directs flow to fallback paths or next steps based on model output confidence    |

---

### 🧩 Agent Details

---

#### 1. 📨 Call Intake Agent

**Responsibility**:
- Check if the user uploaded a valid file (audio or transcript)
- Extract metadata (e.g., call date, duration, file type)
- Log format inconsistencies or unsupported inputs

**Example**:
```json
{
  "input_type": "audio/mp3",
  "duration": "4m32s",
  "agent_id": "A2098",
  "customer_language": "English"
}
```
✅ **Fails Fast**: Prevents corrupted or unsupported files from entering the pipeline.

---

### 2. 🗣️ Transcription Agent

**Responsibility**:
- Convert `.wav`, `.mp3`, etc. into a punctuated transcript
- Use **Whisper** as the default transcription engine
- Fallback to **Deepgram** or **AssemblyAI** if Whisper fails
- Return segment-wise transcripts if required for advanced QA

**Example Output**:
```json
{
  "transcript": "Hi, I need help with my SIM activation...",
  "language": "en",
  "confidence_score": 0.93
}
```

### 3. 🧾 Summarization Agent

**Responsibility**:
- Use **LLM + LangChain** to generate structured summaries.
- Extract key elements:
  - `issue`
  - `resolution`
  - `customer_sentiment`
  - `next_steps`
- Format output using a **Pydantic schema** to ensure structure and consistency.

**Example Output**:
```json
{
  "issue": "Customer unable to activate SIM",
  "resolution": "Agent escalated to backend team",
  "next_steps": "Resolution in 24-48 hrs",
  "customer_sentiment": "Neutral"
}
```
---

### 4. 📊 Quality Scoring Agent

**Responsibility**:
- Evaluate agent performance using a **structured rubric**:
  - ✅ Empathy
  - ✅ Clarity
  - ✅ Tone
  - ✅ Resolution handling
- Use **function calling** to return scores in a consistent schema.
- Optionally validate outputs using:
  - [`Guardrails`](https://www.guardrailsai.com/) for rule enforcement
  - [`Ragas`](https://github.com/explodinggradients/ragas) for evaluation metrics

**Example Output**:
```json
{
  "empathy": 0.85,
  "tone": 0.92,
  "resolution_score": 0.78,
  "compliance_flag": false
}
```

---

### 5. 🔀 Routing Agent

**Responsibility**:
- Acts as a **decision node** in the LangGraph pipeline
- Evaluates the current shared state to decide the next step
- Routes the flow based on:
  - ❌ Presence of errors
  - 📉 Evaluation scores (e.g., low resolution rating)
  - ⚙️ Business rules (e.g., QA thresholds, compliance)

---

**Routing Logic (Python)**:
```python
if state.error:
    return "fallback"
elif state.qa_scores["resolution_score"] < 0.6:
    return "review"
else:
    return "done"
```
---

✅ **This agent ensures the system is:**

- 🛡️ **Resilient** to failures with automatic fallback logic  
- 💸 **Cost-aware**, avoiding unnecessary LLM/API calls  
- 🔍 **Observant**, enabling runtime evaluation-based branching  

---

### ✅ Langgraph Implementation
---

#### Sample code:

```python
# call_summarizer_agents/langgraph_app.py

from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableLambda
from pydantic import BaseModel
from typing import Optional, Dict, Literal

# -------------------- 1. Shared State --------------------

class CallState(BaseModel):
    input_file: Optional[str] = None
    metadata: Optional[Dict] = None
    transcript: Optional[str] = None
    summary: Optional[Dict] = None
    qa_scores: Optional[Dict] = None
    error: Optional[str] = None
    next_step: Optional[Literal["transcribe", "summarize", "score", "done", "fallback"]] = "transcribe"

# -------------------- 2. Agent Functions --------------------

def call_intake_agent(state: CallState) -> CallState:
    if not state.input_file:
        return state.copy(update={"error": "Missing input file", "next_step": "fallback"})
    metadata = {"file_type": "audio/mp3", "language": "English"}
    return state.copy(update={"metadata": metadata, "next_step": "transcribe"})

def transcription_agent(state: CallState) -> CallState:
    if state.input_file.endswith(".mp3") or state.input_file.endswith(".wav"):
        transcript = f"Transcript of {state.input_file}"
        return state.copy(update={"transcript": transcript, "next_step": "summarize"})
    else:
        return state.copy(update={"error": "Unsupported file type", "next_step": "fallback"})

def summarization_agent(state: CallState) -> CallState:
    if not state.transcript:
        return state.copy(update={"error": "Transcript missing", "next_step": "fallback"})
    summary = {
        "issue": "Customer cannot activate SIM",
        "resolution": "Escalated to backend",
        "sentiment": "Neutral"
    }
    return state.copy(update={"summary": summary, "next_step": "score"})

def quality_scoring_agent(state: CallState) -> CallState:
    if not state.summary:
        return state.copy(update={"error": "No summary to evaluate", "next_step": "fallback"})
    qa_scores = {
        "empathy": 0.85,
        "resolution_score": 0.78,
        "tone": 0.92,
        "compliance_flag": False
    }
    return state.copy(update={"qa_scores": qa_scores, "next_step": "done"})

def fallback_agent(state: CallState) -> CallState:
    return state.copy(update={"summary": {"error": state.error}, "next_step": "done"})

# -------------------- 3. Routing Logic --------------------

def router(state: CallState) -> str:
    return state.next_step or "done"

# -------------------- 4. Build LangGraph --------------------

builder = StateGraph(CallState)

builder.add_node("intake", RunnableLambda(call_intake_agent))
builder.add_node("transcribe", RunnableLambda(transcription_agent))
builder.add_node("summarize", RunnableLambda(summarization_agent))
builder.add_node("score", RunnableLambda(quality_scoring_agent))
builder.add_node("fallback", RunnableLambda(fallback_agent))

# Transitions
builder.set_entry_point("intake")
builder.add_edge("intake", router)
builder.add_edge("transcribe", router)
builder.add_edge("summarize", router)
builder.add_edge("score", router)
builder.add_edge("fallback", router)
builder.set_finish_point("done")

graph_app = builder.compile()

```

#### 🧪 Sample Execution

```python
if __name__ == "__main__":
    initial_state = CallState(input_file="customer_call.mp3")
    final_state = graph_app.invoke(initial_state)
    print(final_state.model_dump())
```