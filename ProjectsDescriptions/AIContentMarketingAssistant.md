# 🧩 AI Content Marketing Assistant

Content marketing is essential in today’s digital landscape. However, scaling high-quality content creation remains a major bottleneck. This AI Content Marketing Assistant project addresses these challenges using a multi-agent, LangGraph-powered system.

---

## 💼 The Business Opportunity

### 🎯 Democratized Content Creation

**Problem:**  
Solo creators and small businesses often can't match the output of large content teams.

**Solution:**  
AI agents generate content across formats — blogs, LinkedIn posts, research summaries, and even images — giving small players enterprise-like capabilities.

**Example:**  
A solopreneur launching a product can:
- Use the **Blog Writer Agent** for SEO-friendly blogs
- Use the **LinkedIn Agent** for professional announcement posts
- Use the **Image Agent** to craft eye-catching visuals

---

### 🧠 Intelligent Content Strategy

**Problem:**  
Content often lacks strategic alignment with business goals.

**Solution:**  
The **Content Strategist Agent** tailors output to match tone, goals, and channel-specific needs — all while preserving brand voice.

**Example:**  
Input: `"Create a blog for our new eco-friendly packaging launch targeting Gen Z"`  
→ The strategist ensures casual yet informative tone and aligns messaging to eco-conscious Gen Z values.

---

### ⚡ Time-to-Market Acceleration

**Problem:**  
Research and writing can take days.

**Solution:**  
Parallel agent workflows generate polished content in minutes.

**Example:**  
Launching a feature today?  
- **Research Agent** summarizes competitors and trends  
- **Blog Agent** drafts an article with SEO  
- **Image Agent** produces the hero image  
→ All in ~10 minutes

---

### 🔁 Cross-Platform Content Optimization

**Problem:**  
Each platform has unique demands (SEO for blogs, hashtags for LinkedIn, visuals for social).

**Solution:**  
Platform-specialized agents ensure optimized output across channels.

**Example:**
- Blog → Keyword-optimized structure with H1–H3 headers
- LinkedIn → Includes emojis, hashtags, CTA
- Image → Right dimensions with text overlay

---

## 🤖 The Power of Multi-Agent LLMs

### 🎓 Specialized Expertise

**Problem:**  
Generalist tools produce mediocre results.

**Solution:**  
Each LangGraph agent is fine-tuned for its domain for expert-level output.

**Example:**
- **SEO Agent** understands keyword placement
- **LinkedIn Agent** mimics personal tone
- **Visual Agent** optimizes design prompts

---

### 🧠 Contextual Intelligence

**Problem:**  
One-off generations lack continuity.

**Solution:**  
Agents remember past requests and refine outputs iteratively.

**Example:**
- First prompt: `"Create a blog outline"`
- Follow-up: `"Add more on sustainability in point #3"`
→ Agent updates that specific point without rewriting everything

---

### 📏 Quality Consistency

**Problem:**  
Human output can vary due to fatigue or inconsistency.

**Solution:**  
AI agents apply structured rules and templates to deliver uniform quality.

**Example:**
- Brand tone remains consistent across 10 blog posts
- Grammar and citation standards are met automatically

---

## 🧨 Market Challenges Addressed

### 📈 Content Volume Pressure

**Problem:**  
Consistent content output is difficult to sustain.

**Solution:**  
Automate repetitive generation workflows.

**Example:**  
Startup outputs:
- 2 blog posts/week
- 3 LinkedIn posts/week
- 1 monthly newsletter  
→ All powered by AI agents

---

### 🔍 Research Bottlenecks

**Problem:**  
Effective content requires time-consuming research.

**Solution:**  
**Research Agent** uses SERP API or Perplexity to deliver quick insights.

**Example:**  
Prompt: `"Research AI trends in e-commerce for 2025"`  
→ Agent summarizes 5 articles, highlights stats, adds links

---

### 🧾 Format Expertise

**Problem:**  
Each content type requires specialized structuring.

**Solution:**  
Agents are trained with format-aware prompt templates.

**Example:**
- Blog: Intro–Body–Conclusion, metadata
- LinkedIn: Hook → Value → CTA + hashtags
- Visual: Brand palette + layout rules

---

### 💰 Resource Constraints

**Problem:**  
Hiring writers, SEO experts, and designers is expensive.

**Solution:**  
One AI system mimics a full content team affordably.

**Example:**
$0 AI agents replace:
- $300/article writer
- $150 LinkedIn specialist
- $200 designer

---

## ⚠️ Challenges and Considerations

### ✅ Content Authenticity

**Challenge:**  
AI content can sound robotic or generic.

**Solution:**  
- Style presets (e.g., casual, witty, formal)  
- Natural language fine-tuning  
- Custom tone training

**Example:**  
Tone: "Witty, Gen Z"  
→ Output:  
> “We ditched plastic for good. Mother Earth just did a happy dance 💃🌱.”

---

### ✅ Source Credibility

**Challenge:**  
Content must avoid misinformation.

**Solution:**  
- Use verified research APIs (Tavily, Perplexity)  
- Auto-cite sources with links

**Example:**  
> “According to a 2024 Deloitte report, 76% of Gen Z buyers prioritize sustainability.”  
→ `[Source: www.deloitte.com]`

---

### ✅ Creative Differentiation

**Challenge:**  
AI output may become repetitive or boring.

**Solution:**  
- Dynamic prompts  
- Trend-based content generation  
- Original analogies and metaphors

**Example:**  
Generic:  
> “We help brands grow online.”  
Creative:  
> “We’re like compost for your digital presence—turning scraps into growth.”

---

## ✅ Summary Table

| Problem | AI Agent Solution |
|--------|--------------------|
| Low content velocity | Blog, LinkedIn, and Visual agents parallelize tasks |
| Inconsistent tone/voice | Content Strategist Agent + Brand Style Templates |
| Lack of platform knowledge | Specialized formatting logic per agent |
| Research fatigue | Dedicated Research Agent with API access |
| Budget constraints | All-in-one intelligent assistant, no need for large teams |

# 🏗️ Technical Architecture: AI Content Marketing Assistant

This project employs a **sophisticated multi-agent architecture** using LangGraph, orchestrating specialized AI agents to deliver intelligent, scalable, and platform-optimized content creation. Below is a breakdown of the key **core components**, their primary technologies, alternatives, and purpose — along with real-world examples for clarity.

---

## 🔧 Core Components

| **Component**           | **Primary Technology**      | **Alternatives**                                         | **Purpose** |
|-------------------------|-----------------------------|----------------------------------------------------------|-------------|
| Multi-Agent System      | `LangGraph`                 | CrewAI, AutoGen, Semantic Kernel                         | Orchestrates specialized agents for different content types |
| Language Model          | `OpenAI GPT-4`              | Claude Sonnet, Google Gemini, Anthropic Claude           | Powers natural language understanding and generation |
| Research Engine         | `SERP API + GPT`            | Perplexity Sonar, You.com Search, Tavily AI              | Provides comprehensive web research capabilities |
| Image Generation        | `DALL-E 3`                  | Midjourney API, Stability AI, Google Imagen              | Creates high-quality visual content |
| Content Optimization    | `Custom LLM Prompts`        | Jasper AI, Copy.ai, Writesonic                           | Optimizes content for SEO, readability, and engagement |
| Web Interface           | `Streamlit`                 | Gradio, React, Vue.js, Flask + HTML/CSS                  | Delivers interactive user experience |
| State Management        | `LangGraph Memory`          | Redis, MongoDB, PostgreSQL                               | Maintains conversation context and user sessions |

---

## 🔁 Component-Wise Details with Examples

### 1️⃣ **Multi-Agent System: `LangGraph`**

**Purpose:**  
Coordinates multiple agents to execute tasks like research, blog writing, image generation, and content structuring — all in a state-aware, directed graph.

**Why LangGraph?**  
- Supports memory
- Handles conditional routing
- Easy orchestration of asynchronous workflows

**Example:**  
A user requests a blog post → `QueryHandler Agent` routes the task to:
- `Research Agent` → gathers data  
- `SEO Blog Agent` → generates article  
- `Strategist Agent` → polishes final content

**Alternatives:**  
- **CrewAI** for human-like autonomous agents  
- **Semantic Kernel** for plugin-based orchestration  
- **AutoGen** for flexible tool + agent integration

---

### 2️⃣ **Language Model: `OpenAI GPT-4`**

**Purpose:**  
Drives content generation across all agents using natural language reasoning.

**Example:**  
- Converts structured research data into blog paragraphs  
- Mimics brand voice in LinkedIn posts  
- Summarizes data into bullet points for infographics

**Alternatives:**  
- **Claude Sonnet** for longer context and safer completions  
- **Google Gemini** for tight Google ecosystem integration  
- **Anthropic Claude** for safety-focused generation

---

### 3️⃣ **Research Engine: `SERP API + GPT`**

**Purpose:**  
Enables agents to gather real-time information from the web, fact-checking, and citation.

**Example:**  
Prompt: `"Find the top AI trends in retail for 2025"`  
→ Uses `SERP API` to extract links  
→ GPT summarizes findings into 3 key points  
→ Links are cited in output

**Alternatives:**  
- **Perplexity Sonar** (natural language search)  
- **Tavily AI** (reliable factual search API)  
- **You.com** (chat-based search engine)

---

### 4️⃣ **Image Generation: `DALL·E 3`**

**Purpose:**  
Generates visuals to complement written content using text-to-image prompts.

**Example:**  
Prompt: `"Create a futuristic retail store with AI-powered shelves"`  
→ Output image embedded in blog or shared as LinkedIn banner

**Alternatives:**  
- **Midjourney API** for artistic, stylized images  
- **Stability AI (Stable Diffusion)** for open-source generation  
- **Google Imagen** for enterprise-grade photo-realism

---

### 5️⃣ **Content Optimization: `Custom LLM Prompts`**

**Purpose:**  
Refines outputs by optimizing:
- SEO keywords
- Meta descriptions
- Header structure
- Readability

**Example:**  
Generated content is fed back into GPT with a prompt like:  
> “Rewrite the blog to include the keyword *‘AI in e-commerce’* in the title, H2, and first 100 words.”

**Alternatives:**  
- **Jasper AI** for marketing copy generation  
- **Copy.ai**, **Writesonic** for ready-made content templates

---

### 6️⃣ **Web Interface: `Streamlit`**

**Purpose:**  
Acts as the user-facing front-end where content requests are made and results previewed.

**Features:**
- Chat-like input
- Preview/edit sections
- Side-by-side comparison of variations

**Example:**  
User types:  
> `"Create a LinkedIn post about our eco-packaging launch"`  
→ Output shown in editable text box, image preview included

**Alternatives:**  
- **Gradio** for easy UI demos  
- **React** or **Vue** for fully customizable frontend  
- **Flask + HTML/CSS** for backend-driven rendering

---

### 7️⃣ **State Management: `LangGraph Memory`**

**Purpose:**  
Preserves session context across multi-turn conversations and related content requests.

**Example:**  
User:  
> “Write a blog about eco-packaging.”  
Then:  
> “Now create a LinkedIn post based on it.”  
→ System remembers previous blog and reuses content contextually.

**Alternatives:**  
- **Redis** for in-memory context store  
- **MongoDB / PostgreSQL** for persistent session and user history

---

## ✅ Summary Table

| **Component**         | **Tech Used**      | **What It Enables** |
|-----------------------|--------------------|----------------------|
| Multi-Agent System    | LangGraph          | Modular, flexible workflows |
| Language Model        | GPT-4              | High-quality text generation |
| Research Engine       | SERP API + GPT     | Reliable web research |
| Image Generation      | DALL·E 3           | Branded visuals |
| Content Optimization  | Custom Prompts     | SEO, structure, polish |
| Web Interface         | Streamlit          | User interaction, content preview |
| State Management      | LangGraph Memory   | Context awareness |

# 🚀 How the AI Content Marketing Assistant System Will Be Used

This system enables marketers, entrepreneurs, and creators to generate high-quality content through a simple conversational interface powered by **LangGraph**, orchestrating multiple specialized agents.

Below, we walk through **real-world usage scenarios**, explain **how the agents collaborate**, and showcase how LangGraph handles **state, routing, and context**.

---

## 🧑‍💻 Example 1: Creating an SEO Blog Post with Visuals

**User Goal:**  
Generate a blog post about "AI in sustainable packaging" and include a featured image.

### Step-by-Step Interaction:

1. **User Prompt:**  
   > "Write a blog on how AI is transforming sustainable packaging in e-commerce."

2. **LangGraph Routing (Query Handler Agent):**  
   - Detects intent: needs **research**, **SEO blog writing**, and **visuals**.
   - Routes task to:
     - `Research Agent`
     - `SEO Blog Writer Agent`
     - `Image Generator Agent`
     - `Content Strategist Agent`

3. **Agent Workflow:**
   - ✅ `Research Agent`: Calls SERP API → summarizes 5 sources → extracts facts/statistics  
     Output: structured research
   - ✅ `SEO Blog Writer Agent`: Uses GPT-4 to generate a blog using research, keyword-optimized  
     Output: ~1000-word SEO blog
   - ✅ `Image Generator Agent`: Prompts DALL·E 3 with → "futuristic eco-friendly packaging powered by AI"  
     Output: Hero image
   - ✅ `Content Strategist Agent`: Reviews tone, structure, links, meta description  
     Output: Final polished blog post + image

4. **User Interface (Streamlit):**
   - Blog and image displayed in preview dashboard
   - User can edit and export as Markdown or HTML

---

## 📣 Example 2: LinkedIn Post + Blog Follow-up

**User Goal:**  
Announce a product update on LinkedIn, then create a blog post expanding the same.

### Conversation Flow:

1. **User Input:**  
   > "Write a LinkedIn post about our new AI-powered product for supply chains."

2. **Query Handler Agent:**
   - Routes to `LinkedIn Writer Agent`

3. **LinkedIn Writer Agent:**
   - Output:  
     > "We just launched our smartest tool yet: an AI-powered supply chain assistant 🚀  
     Say goodbye to delays and hello to data-driven efficiency.  
     #AI #SupplyChain #ProductLaunch"

4. **User Follow-up:**  
   > "Now create a blog post based on that."

5. **LangGraph Memory Module:**
   - Fetches prior LinkedIn content for context
   - Passes it as background to `SEO Blog Writer Agent`

6. **Blog Writer Agent:**
   - Uses GPT-4 to expand the post into a full-length blog article

7. **Content Strategist Agent:**
   - Ensures alignment in tone and branding across both outputs

---

## 🔍 Example 3: Research-First Campaign Planning

**User Goal:**  
Plan an entire content campaign for the topic: “AI in Healthcare Compliance”.

### Steps:

1. **User Input:**  
   > "Research AI's role in healthcare compliance and create a campaign plan."

2. **Query Handler Agent:**
   - Routes to:
     - `Research Agent`
     - `Content Strategist Agent`

3. **Research Agent:**
   - Collects sources, compiles a research doc

4. **Content Strategist Agent:**
   - Reads research  
   - Suggests multi-format campaign:
     - 📄 Blog: “5 Ways AI Is Revolutionizing Healthcare Compliance”
     - 📷 Infographic: “HIPAA + AI – What You Need to Know”
     - 💼 LinkedIn Post: "AI for Compliance — Boon or Burden?"

5. **User Approves Plan:**  
   > "Generate the blog and infographic."

6. **Execution:**
   - Blog → `SEO Blog Writer Agent`
   - Visual → `Image Generator Agent`
   - Strategist reviews both before sending to user

---

## 🧵 Example 4: Multi-Turn Iterative Refinement

**User Prompt:**  
> "Generate a blog on AI in education."

**LangGraph Flow:**
- Routes to `Research Agent` → `Blog Agent` → `Strategist`

**Output:**  
- Blog is shown in UI

**User Follow-up #1:**  
> "Add more examples from India."

→ System re-routes to:
- `Research Agent` with `context='India'`
- `Blog Agent` updates relevant sections

**User Follow-up #2:**  
> "Make the tone more conversational."

→ `Content Strategist Agent` rewrites in desired tone

---

## ⚙️ How LangGraph Enables This

| LangGraph Feature      | Functionality Used |
|------------------------|--------------------|
| **StateGraph**         | Models agent flow: query → research → writing → strategy |
| **Memory Module**      | Remembers previous turns in multi-step conversations |
| **Conditional Routing**| Sends input to different agents based on user intent |
| **Error Handling**     | Fallbacks to alternative services if one agent/API fails |
| **Streaming Responses**| For fast UI updates while LLM generates |

---

## ✅ Summary: What Users Can Do

| Use Case | Agents Involved |
|----------|-----------------|
| Blog creation from scratch | Query → Research → SEO Blog → Strategist |
| LinkedIn + blog sync | LinkedIn → Strategist → Blog |
| Visual content generation | Image Generator + Strategist |
| Full campaign planning | Research → Strategist → all content types |
| Multi-turn content editing | Strategist + Memory-enabled routing |

# 🧠 LangGraph Agent Overview

## ✅ Agent 1: Query Handler Agent

### 🔧 Purpose:
Detects the user's intent (e.g., "write a blog", "generate an image") and routes the request to the appropriate downstream agents.

### 🧠 When It Kicks In:
It’s the entry point of the LangGraph workflow — the first agent invoked.

### 📌 Example Use Case:
**User**: “Create a LinkedIn post and an image about our new AI launch.”

**Routes request to:**
- LinkedIn Writer Agent
- Image Generator Agent

### 🧪 Sample Code:
```python
# query_handler.py
def query_handler_agent(state):
    user_input = state["user_input"].lower()
    if "research" in user_input:
        return "research"
    elif "blog" in user_input:
        return "blog"
    elif "linkedin" in user_input:
        return "linkedin"
    elif "image" in user_input:
        return "image"
    elif "strategy" in user_input:
        return "strategy"
    else:
        return "strategy"
```
---

## ✅ Agent 2: Deep Research Agent

### 🔧 Purpose:
Conducts web research using APIs like SERP, Tavily, or Perplexity, then summarizes the results.

### 🧠 When It Kicks In:
- When user requests background info  
- Or when downstream agents require fact-based support

### 📌 Example Use Case:
**User**: “Research how AI is used in education compliance.”

**Used By:**
- Blog Writer Agent  
- Strategist Agent

### 🧪 Sample Code:
```python
# research_agent.py
from tavily import TavilyClient

def research_agent(state):
    query = state["user_input"]
    client = TavilyClient(api_key="your_api_key")
    results = client.search(query=query)
    return {"research_data": results["results"]}
```
---

## ✅ Agent 3: SEO Blog Writer Agent

### 🔧 Purpose:

Writes long-form, SEO-optimized blogs using LLMs like GPT-4 or Claude.

### 🧠 When It Kicks In:

When Query Handler detects “blog” intent

Often takes research\_data as input

### 📌 Example Use Case:

User: “Write a blog on sustainable AI in logistics.”

**Output:**

* Headings (H2, H3)
* Keywords
* Meta descriptions

### 🧪 Sample Code:

```python
# blog_writer.py
from openai import OpenAI

def blog_writer_agent(state):
    research = state.get("research_data", "")
    prompt = f"Write an SEO blog using the following research:\n{research}"
    response = OpenAI().chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"blog_post": response.choices[0].message.content}
```

---

## ✅ Agent 4: LinkedIn Post Writer Agent

### 🔧 Purpose:

Creates short, engaging LinkedIn-style posts with hashtags and emojis.

### 🧠 When It Kicks In:

When user wants promotional social media content

Often complements blogs for cross-promotion

### 📌 Example Use Case:

User: “Announce our launch of an AI tool for HR.”

**Output:**

* Hook → Insight → CTA
* Format optimized for mobile/social

### 🧪 Sample Code:

```python
# linkedin_writer.py
from openai import OpenAI

def linkedin_writer_agent(state):
    topic = state["user_input"]
    prompt = f"Write a professional yet engaging LinkedIn post about:\n{topic}\nInclude emojis and hashtags."
    response = OpenAI().chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"linkedin_post": response.choices[0].message.content}
```

---

## ✅ Agent 5: Image Generation Agent

### 🔧 Purpose:

Generates visuals using tools like DALL·E 3, Midjourney API, or Stability AI.

### 🧠 When It Kicks In:

When the user requests an image

Or when the content strategist wants a visual for a blog/post

### 📌 Example Use Case:

User: “Generate an image of a futuristic AI classroom.”

**Output:**

* Base64/URL or raw image stream
* Can be embedded in Streamlit

### 🧪 Sample Code:

```python
# image_generator.py
from openai import OpenAI

def image_generator_agent(state):
    topic = state["user_input"]
    prompt = f"Create an illustration for: {topic}"
    response = OpenAI().images.generate(prompt=prompt, n=1, size="1024x1024")
    return {"image_url": response.data[0].url}
```

---

## ✅ Agent 6: Content Strategist Agent

### 🔧 Purpose:

Formats, polishes, and aligns all content pieces with brand voice and campaign goals.

### 🧠 When It Kicks In:

As the final agent in every flow

It reviews outputs from other agents

Can combine multiple content types

### 📌 Example Use Case:

Blog + LinkedIn post + Image need to be bundled with a cohesive CTA

**Output:**

* Unified markdown/export package
* Reviewed for grammar, tone, voice

### 🧪 Sample Code:

```python
# content_strategist.py
from openai import OpenAI

def content_strategist_agent(state):
    content_blocks = []
    for key in ["blog_post", "linkedin_post", "image_url", "research_data"]:
        if key in state:
            content_blocks.append(f"### {key.replace('_', ' ').title()}:\n{state[key]}\n")
    prompt = "Polish and unify the following content into a final format:\n" + "\n".join(content_blocks)
    response = OpenAI().chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"final_content": response.choices[0].message.content}
```

---

## 🧠 How They Work Together

Here’s a LangGraph sequence for a full content generation request:

```sql
User: "Research AI in retail, write a blog, and generate an image"
```

1. `QueryHandlerAgent` → detects: research, blog, image
2. `DeepResearchAgent` → gets facts from Tavily/SERP
3. `BlogWriterAgent` → writes 1000-word SEO article
4. `ImageGeneratorAgent` → creates hero visual
5. `ContentStrategistAgent` → merges all into a final deliverable

# 📦 Shared State in LangGraph Agent Workflows

## 📦 Sample Shared State Definition

Let’s define a dictionary to represent your state:

```python
# shared_state.py
def initialize_state(user_input: str) -> dict:
    return {
        "user_input": user_input,
        "research_data": None,
        "blog_post": None,
        "linkedin_post": None,
        "image_url": None,
        "final_content": None,
        "context": {}  # optional: for memory/multi-turn
    }
```

This shared state is passed through the graph during execution. Each agent updates the relevant keys.

---

## 🔄 Shared State Lifecycle Example

### 🎯 User Input:

> "Research AI in healthcare, write a blog, and generate an image."

### 🧪 Initial State

```python
{
    "user_input": "Research AI in healthcare, write a blog, and generate an image.",
    "research_data": None,
    "blog_post": None,
    "linkedin_post": None,
    "image_url": None,
    "final_content": None,
    "context": {}
}
```

### 🔍 After DeepResearchAgent

```python
{
    ...
    "research_data": "AI is helping reduce diagnostic errors by 20%...",
}
```

### ✍️ After SEO Blog Writer Agent

```python
{
    ...
    "blog_post": "In today’s healthcare landscape, AI is transforming diagnostics...",
}
```

### 🖼️ After Image Generation Agent

```python
{
    ...
    "image_url": "https://image-server.ai/output/healthcare_ai_1.png"
}
```

### 📢 After Content Strategist Agent

```python
{
    ...
    "final_content": "# AI in Healthcare\n\nIn today’s healthcare landscape...\n![hero image](https://...)"
}
```

---

## ✅ Shared State Keys Overview

| Key             | Type   | Description                                     |
| --------------- | ------ | ----------------------------------------------- |
| `user_input`    | `str`  | Original prompt from user                       |
| `research_data` | `str`  | Text from Deep Research Agent                   |
| `blog_post`     | `str`  | Output from Blog Writer Agent                   |
| `linkedin_post` | `str`  | Output from LinkedIn Agent                      |
| `image_url`     | `str`  | URL or base64 image from Image Generation Agent |
| `final_content` | `str`  | Unified final output from Content Strategist    |
| `context`       | `dict` | Optional session/memory context                 |

---

## 🧱 Using Shared State in LangGraph

You pass the shared state into the LangGraph workflow using `.invoke()`:

```python
from src.workflow.langgraph_workflow import graph
from src.shared_state import initialize_state

if __name__ == "__main__":
    state = initialize_state("Create a blog on AI in education with a visual")
    result = graph.invoke(state)
    print(result["final_content"])
```

# 🧠 Streamlit UI for LangGraph Agent Workflow

This Streamlit UI allows users to input a prompt and visualize the output of a LangGraph-based multi-agent workflow. The UI fetches the final output from the `final_content` key in the shared state and optionally shows other intermediate results.

## ✅ `app.py`

```python
import streamlit as st
from src.workflow.langgraph_workflow import graph
from src.shared_state import initialize_state

st.set_page_config(page_title="Content Agent", layout="centered")

st.title("🧠 AI Content Generator")
st.markdown("This app uses a multi-agent LangGraph to generate blogs, LinkedIn posts, and images.")

# 📥 User input
user_input = st.text_area("Enter your prompt", placeholder="e.g., Write a blog on AI in agriculture")

# 🚀 Submit button
if st.button("Run LangGraph"):
    if not user_input.strip():
        st.warning("Please enter a prompt.")
    else:
        with st.spinner("Running LangGraph agents..."):
            # 1. Initialize shared state
            state = initialize_state(user_input)

            # 2. Invoke the LangGraph workflow
            updated_state = graph.invoke(state)

        # ✅ 3. Use final_content correctly from the updated state
        final_output = updated_state.get("final_content", "No final content generated.")

        st.subheader("📄 Final Content")
        st.markdown(final_output)

        # 🔍 Optional breakdown
        with st.expander("🔍 Research Summary"):
            st.markdown(updated_state.get("research_data", "_No research summary available._"))

        with st.expander("✍️ Blog Draft"):
            st.markdown(updated_state.get("blog_post", "_No blog post available._"))

        with st.expander("🖼️ Generated Image"):
            image_url = updated_state.get("image_url")
            if image_url:
                st.image(image_url)
            else:
                st.markdown("_No image generated._")

        with st.expander("🔗 LinkedIn Post"):
            st.markdown(updated_state.get("linkedin_post", "_No LinkedIn post available._"))
```

# 🧠 Incorporating Memory & Multi-Turn Chat in LangGraph + Streamlit

## 🗂️ Shared State Extension

Update your `initialize_state` to optionally accept a previous context:

```python
# shared_state.py

def initialize_state(user_input: str, prev_context: dict = None) -> dict:
    return {
        "user_input": user_input,
        "research_data": None,
        "blog_post": None,
        "linkedin_post": None,
        "image_url": None,
        "final_content": None,
        "context": prev_context or {}
    }
```

## 🔄 How the Context Evolves
Each agent can read from and write to the shared context (`state["context"]`), enabling memory and multi-step refinement.

### 🧠 Example: After `DeepResearchAgent`
```python
state["context"]["topics_researched"] = state["research_data"]
```

### ✅ Example: `ContentStrategistAgent` Using Prior Memory

```python
prior_posts = state["context"].get("prior_posts", [])
prior_posts.append(state["blog_post"])
state["context"]["prior_posts"] = prior_posts
```

This allows the agent to remember previously created posts and build upon them.

---

## 💬 Streamlit Multi-Turn UI

You can persist session state using `st.session_state`.

```python
import streamlit as st
from src.workflow.langgraph_workflow import graph
from src.shared_state import initialize_state

# Initialize or get prior context
if "context" not in st.session_state:
    st.session_state.context = {}

st.title("🧠 AI Content Generator (Multi-Turn)")

prompt = st.text_input("Enter your next instruction:", "")

if st.button("Submit") and prompt:
    state = initialize_state(prompt, prev_context=st.session_state.context)
    result = graph.invoke(state)

    # Store updated context
    st.session_state.context = result["context"]

    st.markdown("## ✍️ Final Output")
    st.markdown(result["final_content"], unsafe_allow_html=True)
```

## 🧪 Optional: Add Chat History UI

```python
if "history" not in st.session_state:
    st.session_state.history = []

# After invoking the graph
st.session_state.history.append({
    "prompt": prompt,
    "response": result["final_content"]
})

# Show chat history
for item in st.session_state.history:
    st.markdown(f"**You:** {item['prompt']}")
    st.markdown(f"**AI:** {item['response']}")

```


