# LLM App Evaluation

## 🧩 Why Evals for LLM Apps?

LLMs don’t behave like normal software. You can’t just rely on unit tests because:

- **Outputs vary** (non-deterministic).  
- **Correctness is fuzzy** (e.g., two different but valid summaries).  
- **Failures happen in unexpected ways** (hallucinations, irrelevance, unsafe responses).  

So for LLM apps, we need **continuous evaluation** that checks both task quality and user experience.


## ⚙️ What to Evaluate in LLM Apps

Think of it in layers: Retrieval layer (if RAG app), Generation layer, End-to-End UX etc.

### (A) Retrieval Layer (if RAG app)

The retrieval layer is responsible for fetching relevant documents from a knowledge base or external source to support the LLM’s answer. Evaluating this layer ensures that the foundation for your generated responses is solid.


#### 1. **Context Recall**

**Definition:**  
Context recall measures whether the retriever is able to fetch all relevant documents that could answer the user’s query. High recall ensures that the LLM has access to the information it needs to provide a complete answer.

**Example:**  
- **Query:** “Who won the Nobel Prize in Physics in 2020?”  
- **Relevant documents in your DB:**  
  1. Article about Nobel Prize 2020 winners  
  2. News report on physicists awarded in 2020  
  3. Wikipedia page listing Nobel Prize winners  

If the retriever only fetches 1 out of these 3 documents, the **context recall is low**. If it fetches all 3, recall is high.  

**Metric:** Often measured using:  recall = (number of relevant docs retrieved / number of total relevant docs available)

**How to Measure:**
- Manual labeling:
    - Identify all documents in the knowledge base that are relevant to a query.
    - If a dataset has "gold documents" annotated for each query, calculate recall automatically.

- Automated evaluation:
    - Compare retrieved documents with a "gold set" of relevant documents.

> High recall ensures that the model has all the relevant information it might need to generate a complete answer.

#### 2. **Context Precision**

**Definition:**  
Context precision measures whether the retriever avoids bringing irrelevant or noisy documents. High precision ensures the LLM doesn’t get confused by junk data, reducing hallucinations and irrelevant answers.

**Example:**  
- **Query:** “Best exercises for lower back pain”  
- **Retrieved documents:**  
  1. Article on lower back exercises ✅  
  2. Article on knee pain exercises ❌  
  3. Advertisement for a massage chair ❌  

Here, only 1 of 3 documents is relevant. Precision is low.

**Metric:** Often measured using: precision = (number of relevant retrieved / number of total retrieved) 

**How to Measure:**
- Manual labeling:
    - For each retrieved document, determine if it is relevant.
    - Count relevant vs irrelevant retrieved docs.

- Automated evaluation:
    - Compare retrieved documents with a "gold set" of relevant documents.

> High precision ensures that most retrieved documents are useful.


```
Explanation begin: Automated Evaluation Using Gold Documents
```
When working with **large datasets**, manually checking retrieved documents is impractical. Many datasets include **gold documents**—pre-annotated documents known to be relevant for each query. These can be used to **automatically calculate recall and precision**.

---

#### Dataset Setup

| Query                         | Gold Docs (IDs)     |
| ----------------------------- | ------------------- |
| “Nobel Prize in Physics 2020” | \[doc1, doc3, doc7] |
| “Python first release year”   | \[doc10, doc12]     |

---

#### Retriever Output

| Query                         | Retrieved Docs (IDs) |
| ----------------------------- | -------------------- |
| “Nobel Prize in Physics 2020” | \[doc1, doc4, doc7]  |
| “Python first release year”   | \[doc12, doc15]      |

---

### 1. **Automated Recall**

**Definition:**
Recall measures the fraction of **gold documents** retrieved by the system. It indicates **completeness**.

**Formula:**

Recall = (# of gold docs retrieved) / (Total # of gold docs)

**Examples:**

* **Query:** “Nobel Prize in Physics 2020”

  * Gold docs = \[doc1, doc3, doc7]
  * Retrieved docs = \[doc1, doc4, doc7]
  * Relevant retrieved = doc1, doc7 → 2 relevant retrieved

Recall = 2 / 3 = 0.67

* **Query:** “Python first release year”

  * Gold docs = \[doc10, doc12]
  * Retrieved docs = \[doc12, doc15]
  * Relevant retrieved = doc12 → 1 relevant retrieved

Recall = 1 / 2 = 0.5

---

### 2. **Automated Precision**

**Definition:**
Precision measures the fraction of **retrieved documents** that are actually relevant. It indicates **accuracy / low noise**.

**Formula:**

Precision = (# of relevant retrieved docs) / (Total # of retrieved docs)

**Examples:**

* **Query:** “Nobel Prize in Physics 2020”

  * Retrieved docs = \[doc1, doc4, doc7]
  * Relevant retrieved = doc1, doc7 → 2 relevant retrieved
  * Total retrieved = 3

Precision = 2 / 3 ≈ 0.67

* **Query:** “Python first release year”

  * Retrieved docs = \[doc12, doc15]
  * Relevant retrieved = doc12 → 1 relevant retrieved
  * Total retrieved = 2

Precision = 1 / 2 = 0.5

```
Explanation end: Automated Evaluation Using Gold Documents
```

#### 3. **Groundedness**

**Definition:**  
Groundedness measures whether the final answer produced by the LLM is actually supported by the retrieved documents. Even if recall and precision are high, the LLM can hallucinate or add unsupported claims.

**Example:**  
- **Query:** “When was Python first released?”  
- **Retrieved document:** Wikipedia article stating “Python was first released in 1991.”  
- **LLM output:** “Python was first released in 1990.” ❌  

Even though the correct document was retrieved, the model generated a factually incorrect answer, indicating **low groundedness**.

Groundedness evaluation often involves automated checks (e.g., string matching, QA over retrieved docs) or human verification.

**Metric:**
- Binary per statement: 1 if supported, 0 if not.
- Or aggregate score: fraction of claims grounded in retrieved docs.

**How to Measure:**

- Automated methods:

    - String Matching: Check if factual statements in the output appear verbatim or with minor paraphrasing in retrieved docs.
        - **Example:**  
            - **Retrieved doc:** “Python was first released in 1991.”  
            - **LLM output:** “Python was first released in 1991.” ✅ (exact match, grounded)  
            - **LLM output:** “Python was released in the 1990s.” ⚠️ (paraphrase, partial grounding)  
    - QA-based Verification: Use a secondary QA model to verify if each claim in the output can be answered using the retrieved documents.
        - **Example:**  
            - **Query:** “When was Python first released?”  
            - **Retrieved doc:** “Python was first released in 1991.”  
            - **LLM output:** “Python was first released in 1991.”  
            - A QA model would answer “1991” from the retrieved doc, confirming the claim is grounded.  
    - Fact Extraction & Comparison: Extract entities/dates/numbers and check for consistency with the retrieved docs.
        - **Example:**  
            - **LLM output:** “The Nobel Prize in Physics 2020 was awarded to Roger Penrose.”  
            - Extracted fact: Roger Penrose → check retrieved documents for match → ✅ grounded  

- Human evaluation:
    - Have human evaluators read the retrieved documents and the LLM output to mark whether all claims are supported.
        - **Example:**  
            - Evaluator reads:  
                - **Retrieved docs:** Articles on Nobel Prize winners  
                - **LLM output:** Lists winners and contributions  
            - Evaluator confirms each claim is backed by a retrieved doc → grounded.  
            - **Use Case:** Particularly useful when automated methods fail due to paraphrasing, nuanced reasoning, or incomplete information.


### (B) Generation Layer

The **Generation Layer** evaluates the output produced by the LLM itself. Even if the retrieval layer is perfect, the LLM may produce answers that are factually incorrect, irrelevant, incomplete, or unsafe. Here’s a detailed breakdown of key evaluation metrics with examples:

---

#### 1. **Correctness**

**Definition:**  
Checks whether the answer produced by the LLM is **factually accurate**.

**Example:**  
- **Query:** “Who wrote *Pride and Prejudice*?”  
- **LLM Output:** “Jane Austen wrote *Pride and Prejudice*.” ✅ (Correct)  
- **LLM Output:** “Charlotte Brontë wrote *Pride and Prejudice*.” ❌ (Incorrect)

**Evaluation Methods:**  
- Automated: Compare answer against a knowledge base or trusted source.  
- Human: Verify each claim manually.

---

#### 2. **Relevance**

**Definition:**  
Measures whether the answer **directly addresses the user’s query**.

**Example:**  
- **Query:** “List exercises for strengthening lower back muscles.”  
- **LLM Output:** “Squats, planks, deadlifts are effective for lower back strength.” ✅ (Relevant)  
- **LLM Output:** “Eating a balanced diet is important for overall health.” ❌ (Irrelevant)

**Evaluation Methods:**  
- Automated: Use semantic similarity scoring between query and answer.  
- Human: Assess if the response matches the intent of the query.

---

#### 3. **Completeness**

**Definition:**  
Checks whether the LLM **covers all necessary points** requested in the query.

**Example:**  
- **Query:** “What are the causes and treatments for hypertension?”  
- **LLM Output:** “Causes include high salt intake and genetics. Treatments include medication and lifestyle changes.” ✅ (Complete)  
- **LLM Output:** “Causes include high salt intake and genetics.” ❌ (Incomplete)

**Evaluation Methods:**  
- Human evaluation is common, marking each required point as present or missing.  
- Automated: Use checklist-based evaluation or QA over expected answer elements.

---

#### 4. **Coherence / Style**

**Definition:**  
Measures **clarity, fluency, conciseness, tone, and readability** of the generated text.

**Example:**  
- **Query:** “Explain blockchain in simple terms.”  
- **LLM Output:** “Blockchain is a distributed ledger technology that records transactions securely and transparently.” ✅ (Coherent)  
- **LLM Output:** “Blockchain decentralized digital transactions ledger secure trust multiple copy nodes.” ❌ (Incoherent)

**Evaluation Methods:**  
- Automated: Grammar and readability tools (e.g., Flesch-Kincaid score).  
- Human: Subjective assessment of flow, conciseness, and tone.

---

#### 5. **Safety**

**Definition:**  
Ensures the LLM output does **not contain harmful content**, sensitive personal information (PII), or toxic language.

**Example:**  
- **Query:** “Write a joke about programmers.”  
- **LLM Output:** “Why do programmers prefer dark mode? Because light attracts bugs.” ✅ (Safe)  
- **LLM Output:** “Programmers are lazy and stupid, unlike other people.” ❌ (Unsafe / toxic)

**Evaluation Methods:**  
- Automated: Use toxicity detectors, PII checkers, or content filters.  
- Human: Manual review for subtle unsafe or offensive content.

```
Explanation begin: QA over Expected Answer Elements
```

### QA over Expected Answer Elements

“**QA over expected answer elements**” is a method used to **automatically check completeness** of an LLM’s output by treating each key piece of information as a small question.

---

#### Concept

1. Suppose you have a **query** and an **expected answer** that has multiple required components (elements).  
2. Convert each element into a **sub-question**.  
3. Use a **QA system** (another LLM or a rule-based QA model) to check if the LLM’s output contains each element.  
4. If all elements are found, the answer is considered **complete**.

---

#### Example

**Query:** “What are the causes and treatments for hypertension?”  

**Expected Answer Elements:**
- Causes: high salt intake, genetics, obesity  
- Treatments: medication, lifestyle changes  

**LLM Output:** “Hypertension can be caused by high salt intake and genetics. It can be treated with lifestyle changes and medication.”

**QA over Expected Answer Elements:**

| Sub-question                           | Found in LLM Output? |
|---------------------------------------|--------------------|
| Does the answer mention causes?        | ✅ Yes             |
| Does it mention high salt intake?      | ✅ Yes             |
| Does it mention genetics?              | ✅ Yes             |
| Does it mention obesity?               | ❌ No              |
| Does it mention treatments?            | ✅ Yes             |
| Does it mention medication?            | ✅ Yes             |
| Does it mention lifestyle changes?     | ✅ Yes             |

**Result:**  
- **Completeness score:** 6/7 = 85%  
- Missing element: obesity → partial completeness.

---

#### Advantages

- **Automated:** No need for full human evaluation.  
- **Fine-grained:** Identifies exactly which parts of the answer are missing.  
- **Scalable:** Works for large datasets and multiple queries.

```
Explanation end: QA over Expected Answer Elements
```

### (C) End-to-End UX
- **Latency** – is it fast enough?  
- **Cost** – per request $$  
- **Consistency** – stable performance across prompts  
- **Task Success** – did the user get what they needed?  

---

## Tools for LLM App Evals

### 1. LangSmith
**Purpose:** Comprehensive evaluation and tracking platform for LLMs.  

**Key Features:**
- Dataset management for evaluation.
- Run evaluations using multiple metrics (e.g., correctness, reasoning, factuality).
- Track performance over time across different model versions.
- Integration with **LangChain** for automated pipelines.

**Example Use Case:**  
You have a QA system and want to monitor how multiple models perform on the same dataset over time. LangSmith allows you to see which model answers most accurately and consistently.

---

### 2. RAGAS
**Purpose:** Open-source evaluation framework focused on reasoning and generation tasks.  

**Key Features:**
- Supports multiple evaluators: factual correctness, relevance, logical consistency, creativity.
- Batch evaluation over datasets of prompts/responses.
- Structured reports showing strengths and weaknesses of models.

**Example Use Case:**  
You are testing an LLM’s ability to explain concepts logically. RAGAS can automatically evaluate responses for reasoning accuracy and highlight patterns of failure.

---

### 3. TruLens
**Purpose:** Focused on model interpretability and qualitative evaluation.  

**Key Features:**
- Inspect attention, internal representations, and decision-making for individual prompts.
- Compare responses across models for reasoning style and consistency.
- Detect potential biases or undesired behaviors.

**Example Use Case:**  
You want to understand why your LLM sometimes gives biased or inconsistent responses. TruLens lets you trace which internal patterns led to specific outputs.

---

### 4. OpenAI Evals
**Purpose:** Open-source framework to define and run structured evaluations of LLMs.  

**Key Features:**
- YAML-driven configuration for defining tasks, datasets, and metrics.
- Modular evaluation design with community-contributed benchmarks.
- Can run automated tests and aggregate results for analysis.

**Example Use Case:**  
You are fine-tuning an LLM for summarization tasks. OpenAI Evals allows you to measure output quality with metrics like ROUGE or factuality, automatically producing evaluation reports.

---

### 5. Hugging Face Evaluate
**Purpose:** Python library and service for measuring performance of LLMs and NLP models.  

**Key Features:**
- Provides standard metrics (BLEU, ROUGE, perplexity, accuracy) out of the box.
- Easily extensible with custom metrics.
- Works seamlessly with Hugging Face datasets and pipelines.

**Example Use Case:**  
You want to benchmark different summarization models on a news dataset using ROUGE and BLEU. Hugging Face Evaluate provides a ready-to-use, flexible framework.

### 6. LLM-as-a-Judge
**Purpose:** Use a powerful LLM (like GPT-4) to evaluate and grade responses from your application.  

**Key Features:**
- Can score outputs based on correctness, relevance, clarity, or adherence to instructions.
- Useful for tasks where automatic metrics (BLEU, ROUGE) are insufficient.
- Provides semantic, context-aware judgment beyond surface-level matching.

**Example Use Case:**  
You have a QA or tutoring app. Instead of relying solely on metrics, you use GPT-4 to grade answers for reasoning quality, factuality, and completeness.

---

### 7. Human Evals
**Purpose:** Human evaluation remains the gold standard, especially for safety-critical or high-stakes tasks.  

**Key Features:**
- Annotators rate responses for correctness, harmful content, or alignment with guidelines.
- Can be combined with LLM evaluation for robust benchmarking.
- Ensures that edge cases, ethical considerations, and nuanced reasoning are captured.

**Example Use Case:**  
You are releasing an AI chatbot in healthcare or finance. Humans evaluate outputs to ensure no unsafe or misleading responses, complementing automated LLM scoring.
 
---

## Eval Methods in Practice

- **Automated Metrics**
  - Cosine similarity between generated answer & ground-truth embeddings  
  - Rouge/BLEU for summaries  
  - Exact match / F1 for QA  

- **LLM-as-a-Judge**  
  Ask another model:  
  > "Given the question, ground truth, and the app’s answer, grade correctness from 1–5."  

- **Human Feedback**
  - Pairwise A/B testing (App A vs App B)  
  - Annotation for hallucinations, tone, missing pieces  

---

## Typical Eval Workflow for an LLM App

1. **Build an eval dataset**
   - Collect real user queries (or synthesize)  
   - Store ground truth answers where possible  

2. **Run app → collect outputs**
   - Log model inputs/outputs  

3. **Apply evals**
   - Automated metrics  
   - LLM-as-judge  
   - Human review (on samples)  

4. **Track in dashboards**
   - Faithfulness %, Hallucination rate, Latency, Cost  

5. **Iterate**
   - Improve retrieval, prompts, or swap models  
   - Re-run evals to check for regressions  

---

## Example: Evaluating a Legal RAG App

Imagine a legal document assistant:

- **Question:** "What was the final ruling in Case XY?"  
- **Ground Truth:** "The ruling was dismissal of charges."  
- **App Answer:** "The court dismissed all charges."  

**Evals:**

- **Faithfulness ✅** – supported by retrieved case docs  
- **Correctness ✅** – matches ground truth  
- **Completeness ❌** – didn’t mention which charges  
- **Relevance ✅** – fully on topic  

**Final Score → 3.5/5**

----

## Colab link

[LLM Evaluation using Langsmith](https://colab.research.google.com/drive/1Ch_BEqRq0WMw9vb5Au1_Xh8KgkbQjKag?usp=sharing)

