# Prompt Engineering Tools Landscape

This chart provides a visual landscape of prompt engineering tools and frameworks, organized along two axes:

- **X-axis (Flexibility):** Ranges from Static Prompts to highly dynamic systems like Autonomous Agents and Prompt Tuning.
- **Y-axis (Complexity):** Shows increasing sophistication, from basic templating to full-scale orchestration and learning-based tuning.

---

## 🧱 1. Static Prompts

**Examples:** Flux, PromptTips.Tacks  
**Traits:** Hardcoded, simple, no variables.  
**Use Case:** Basic GPT chat without any logic or user context.

---

## 🧩 2. Prompt Templates

**Examples:** PromptLayer, PromptHero  
**Traits:** Templates with variables, still manually designed.  
**Use Case:** e.g., `${user_input}` injected into a template like:  
> "Summarize this: ${user_input}"

---

## 🏗️ 3. Prompt Composition

**Examples:** returne, PromptOps, Promptable  
**Traits:** Multiple prompts composed together or modularized.  
**Use Case:** Building modular NLP pipelines.

---

## 🧠 4. Contextual Prompts

**Examples:** Vellum, Drafter, HumanFirst  
**Traits:** Prompts informed by context (e.g., chat history, documents).  
**Use Case:** Context-aware assistants.

---

## 🔗 5. Prompt Chaining

**Examples:** PromptChainer, Prisms, ChainForge  
**Traits:** Sequential LLM calls with outputs fed into the next step.  
**Use Case:** Multi-step reasoning or task workflows.

---

## 📚 6. Retrieval-Augmented Generation (RAG) / Prompt Pipelines

**Examples:** Langchain, Haystack, Dust, RelevanceAI, gpt-engineer, Autogen  
**Traits:** Use of vector stores, semantic search, or orchestration frameworks to inject retrieved content into prompts.  
**Use Case:** Knowledge-grounded question answering, chat with documents, LLM apps using Pinecone/Faiss/Weaviate.

---

## 🤖 7. Autonomous Agents

**Examples:** AutoGPT, AgentGPT, CrewAI, SuperAGI  
**Traits:** Goal-oriented systems with memory, tools, and reasoning.  
**Use Case:** Agents that plan, act, and react autonomously.

---

## 🧬 8. Prompt Tuning / Soft Prompts

**Examples:** HuggingFace, Cohere, OpenAI fine-tuning, LangChain  
**Traits:** Trainable embeddings as prompts; model-internal techniques.  
**Use Case:** Personalized or domain-adapted performance tuning.

---

## 🔀 Diagonal Trend

The diagonal line reflects the natural evolution:  
From static templates → contextual chaining → retrieval-augmented workflows → agents and fine-tuning.

---

## 🧱 Level 1: Static Prompts

### ✅ What They Are

Static prompts are manually written, hardcoded input strings passed to an LLM (e.g., GPT-4) without any dynamic elements.  
These prompts do not change based on user context, data, or previous interactions.

---

### 🧠 Core Idea

> "The prompt is the program."

In static prompts, you write the complete instruction or input exactly as it should be passed to the model.  
There is no logic, templating, or retrieval—just plain text.

---

### 🔧 Examples

#### 🧾 Example 1: Instruction

```plaintext
Explain the difference between supervised and unsupervised learning.
```

#### 🎭 Example 2: Role-playing

```plaintext
You are a Shakespearean playwright. Describe modern-day AI as a soliloquy.
```

#### 🎨 Example 3: Style Transfer

```plaintext
Rewrite the following sentence in the style of Ernest Hemingway:  
"I saw the city lights flicker as we crossed the bridge."
```

### 🧰 Common Use Cases

| Use Case               | Prompt Example                                                                 |
|------------------------|--------------------------------------------------------------------------------|
| Summarization          | "Summarize this paragraph in one sentence: [text]"                             |
| Translation            | "Translate the following sentence to French: [text]"                           |
| Q&A                    | "What is the capital of France?"                                               |
| Sentiment Analysis     | "What is the sentiment of the following review? Positive, Negative, or Neutral"|
| Role-based Instructions| "You are an expert doctor. Give a diagnosis based on the symptoms."           |

---

### 💡 Best Practices

#### ✅ Be explicit: Avoid ambiguity  
LLMs respond best to **clear and specific instructions**.

Good Prompt:

```plaintext
Summarize this in one sentence.
```

Bad Prompt:

```plaintext
Make it shorter.
```

#### 🔁 Give examples (Few-shot prompting)

```plaintext
Q: What is 5 + 5?  
A: 10  
Q: What is 7 + 2?  
A: 9  
Q: What is 6 + 6?  
A:
```

#### 📐 Specify output format

```plaintext
Extract the following in JSON:  
{ "name": "", "email": "", "phone": "" }  
Text: John Doe, Email: john@example.com, Contact: 123-456-7890
```

### ⚠️ Limitations

- ❌ **No adaptability:** Works poorly if input changes  
- ❌ **Not reusable:** You must manually change text for each use  
- ❌ **No memory/context:** Can’t incorporate chat history or user-specific data  
- ❌ **No chaining:** Cannot support multi-step workflows or tasks  

---

### 🧪 Tools Supporting Static Prompts

While many tools support more advanced workflows, static prompts are often used in:

- **ChatGPT / Claude / Gemini interfaces**
- **OpenAI Playground**
- **Basic API calls** like:

```python
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Explain black holes like I'm 5"}]
)
```

### 🧭 When to Use

| Situation                            | Should Use? |
|-------------------------------------|-------------|
| Just trying out ideas quickly       | ✅ Yes      |
| Internal dev experiments            | ✅ Yes      |
| User-specific context required      | ❌ No       |
| Reusable components or workflows    | ❌ No       |
| Multi-turn conversations            | ❌ No       |

---

### 🧗 From Here to Next Level

If static prompts feel limiting, the natural next step is **Prompt Templates – Level 2** —  where you inject variables into predefined structures, allowing **some flexibility and reusability**.

---

## 🧩 Level 2: Prompt Templates

### ✅ What They Are

Prompt templates introduce parameterization to static prompts. Rather than hardcoding every input, you define a reusable prompt with placeholders (variables), which can be filled dynamically at runtime.

> “Prompt templates let you reuse prompt logic across different inputs or tasks.”

---

### 🔧 Structure

A prompt template includes:

- **Fixed parts:** Instruction or context that remains constant  
- **Variable parts:** Placeholders like `{user_input}`, `{name}`, `{topic}`, etc.

---

### 📦 Examples

#### 🧾 Basic Template

```plaintext
"Summarize the following in one sentence: {text}"
```

With input:

```json
{ "text": "Machine learning is a field of computer science that gives computers the ability to learn without being explicitly programmed." }
```

Final prompt:

```plaintext
Summarize the following in one sentence: Machine learning is a field of computer science that gives computers the ability to learn without being explicitly programmed.
```

#### 🧑‍⚕️ Role-Based Example:

```plaintext
You are a doctor. Based on the symptoms below, provide a diagnosis and next steps.
Symptoms: {symptoms}
```

#### 🛠️ With LangChain (Python):
```python
from langchain.prompts import PromptTemplate

template = PromptTemplate.from_template(
    "Translate the following to {language}: {sentence}"
)
filled_prompt = template.format(language="French", sentence="Hello, how are you?")
```
---

### 🧠 Benefits:

| Feature              | Benefit                                                    |
|----------------------|-------------------------------------------------------------|
| 🔁 Reusability       | One prompt works across many different inputs              |
| 🧩 Composability      | Can combine templates in pipelines                         |
| 🛠️ Tool Integration   | Used in LangChain, Haystack, Dust, etc.                   |
| 👨‍💻 Cleaner Code      | Keeps logic and data separate                             |

---

### 🧰 Real-World Use Cases:

| Use Case             | Prompt Template Example                                    |
|----------------------|-------------------------------------------------------------|
| 🧾 Invoice extractor  | "Extract the invoice number and total from: {text}"       |
| 🧑‍🎓 Flashcard generator | "Create a flashcard for: {concept}"                    |
| 📤 Email reply drafts | "Write a polite response to: {email_text}"               |
| 🌐 SEO Blog assistant | "Write a blog post on '{topic}' for a tech-savvy audience." |

---

### 🔥 Best Practices:

**Use Descriptive Variables**:
- ✅ `{job_description}`, `{candidate_resume}`
- ❌ `{input1}`, `{input2}`

**Validate Input Before Filling**:
- Check nulls, character limits, formatting

**Use `format()` or LangChain-style templating safely**:
- Avoid injection issues or malformed prompts

**Version Your Templates**:
- Keep track of changes over time in a structured repo

---

### ⚙️ Tools & Libraries:

| Tool                | Usage                           |
|---------------------|----------------------------------|
| **LangChain**       | Built-in `PromptTemplate` class |
| **PromptLayer**     | Prompt analytics and logging     |
| **PromptOps, Vellum** | Visual template builders       |
| **Jinja2 (Python)** | Generic templating engine        |
| **Mustache, Handlebars** | Web template standards     |

---

### 🔒 Limitations:

- Still doesn’t understand **user context** or chat history
- No **conditionals** or logic (e.g., "if the language is French, do X")
- No **memory** or tool use
- No **chaining** — a single prompt at a time

---

### 🧗 What’s Next:

To go beyond static templates, you'll want **Prompt Composition (Level 3)** — where templates can be assembled, parameterized, and used dynamically in branching logic or workflows.

#### [How Microsoft defends against indirect prompt injection attacks](https://msrc.microsoft.com/blog/2025/07/how-microsoft-defends-against-indirect-prompt-injection-attacks/)

---

## 🏗️ Level 3: Prompt Composition

### 🧩 What They Are

Prompt composition is about combining multiple prompt templates into larger, modular systems.  
Instead of one giant prompt, you break it into smaller pieces (modules) and assemble them into workflows.  

"Prompt composition = modular building blocks of prompts."

This makes prompts reusable, testable, and maintainable, much like functions in programming.  

---

### 🧠 Core Idea

"Compose small, reusable prompts into bigger workflows."  

Just as software engineers don’t hardcode everything in one function, prompt engineers modularize instructions and connect them to form a pipeline.  

---

### 🔧 Examples

#### 🧾 Example 1: Modular QA System

```
[Prompt 1: Rewriter]
Rewrite the user question to make it precise and unambiguous: {question}

[Prompt 2: Knowledge Query]
Based on the rewritten question, search the knowledge base for relevant content.

[Prompt 3: Answer Generator]
Using the knowledge content: {retrieved_text}, answer the user’s question clearly.
```

---

#### 📝 Example 2: Role Split Composition

```plaintext
[Prompt A: Critic]
Evaluate the clarity and tone of this draft: {draft}

[Prompt B: Improver]
Rewrite the draft in a clearer and friendlier way, considering Critic’s feedback: {critic_feedback}
```

---

#### 🛠️ Example 3: With LangChain (Python)

```python
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain, LLMChain

rewrite_template = PromptTemplate.from_template("Rewrite this question: {question}")
rewrite_chain = LLMChain(llm=llm, prompt=rewrite_template, output_key="rewritten")

search_template = PromptTemplate.from_template("Find relevant knowledge for: {rewritten}")
search_chain = LLMChain(llm=llm, prompt=search_template, output_key="knowledge")

answer_template = PromptTemplate.from_template(
    "Answer the question '{rewritten}' using: {knowledge}"
)
answer_chain = LLMChain(llm=llm, prompt=answer_template, output_key="answer")

pipeline = SequentialChain(
    chains=[rewrite_chain, search_chain, answer_chain],
    input_variables=["question"],
    output_variables=["answer"]
)
```

---

### 🧰 Common Use Cases

| Use Case                    | Composition Example                         |
|-----------------------------|---------------------------------------------|
| Multi-step QA               | Rewrite → Retrieve → Answer                 |
| Content generation pipeline | Outline → Expand sections → Proofread → Format |
| Code generation             | Describe → Generate code → Write tests → Review |
| Multi-role feedback loops   | Author → Critic → Editor                     |
| Structured reasoning        | Break problem → Solve subproblems → Merge answers |

---

### 💡 Benefits

| Feature       | Benefit                                               |
|---------------|-------------------------------------------------------|
| Modularity    | Easier to debug, reuse, and maintain prompts          |
| Reusability   | Prompts can be shared across pipelines                |
| Transparency  | Each step is interpretable (vs. giant monolithic one) |
| Composability | Works well with logic/branching (if/else, retries)    |

---

### 🔥 Best Practices

- Keep prompts small and focused  
  One prompt = one role/task. Avoid “do everything” prompts.  

- Name your modules clearly  
  Example: `QuestionRewriter`, `ContentSummarizer` — not `Prompt1`, `Prompt2`.  

- Test submodules independently  
  Debug each step before combining them.  

- Add guardrails between steps  
  Validate outputs (format, length, JSON validity) before passing forward.  

- Log intermediate results  
  Helps with observability and error tracing.  

---

### ⚙️ Tools and Libraries

| Tool                  | Usage                                          |
|-----------------------|-----------------------------------------------|
| LangChain             | SequentialChain, RouterChain, map-reduce flows |
| PromptOps             | Composition and version control of prompts     |
| Returne / Promptable  | Modular pipelines                              |
| ChainForge            | Visual prompt chaining experiments             |
| Jinja2 + Custom Code  | Lightweight manual composition                 |

---

### 🔒 Limitations

- Still lacks contextual memory (doesn’t remember across sessions unless managed manually).  
- Can become brittle if one module produces unexpected output.  
- Complexity grows fast — pipelines can become hard to manage without tooling.  
- Not autonomous — still requires human-defined flow.  

---

### 🧭 When to Use

| Situation                        | Should Use? |
|---------------------------------|--------------|
| Building reusable NLP pipelines | Yes          |
| Multi-step reasoning workflows  | Yes          |
| Context-rich assistants         | No           |
| Long-running conversations      | No           |

---

### 🧗 From Here to Next Level

Once you’re composing prompts into pipelines, the next step is Contextual Prompts (Level 4) — where prompts dynamically adapt based on chat history, documents, or external signals.
