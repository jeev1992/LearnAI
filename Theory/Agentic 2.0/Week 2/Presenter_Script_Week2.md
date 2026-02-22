# Presenter Script — Week 2: RAG-Powered Knowledge Agents
## Embeddings, Chunking & Indexing
### Read this top-to-bottom during the class. Each section is labeled with its slide number.

---

---

## SLIDE 1 — Title Slide

Alright everyone, welcome. Let's get started. Today's session is Week 2 of our RAG-Powered Knowledge Agents series. We're going to be covering three core topics: Text Embeddings, Chunking Strategies, and Indexing Strategies for RAG. These three things together form the retrieval layer of any serious RAG system — the machinery that decides what information gets handed to your LLM before it generates an answer. By the end of today, you'll understand all of it, and you'll have written and run working code for each one. Let's go.

---

## SLIDE 2 — Introduction: Jeevendra Singh

Quick introduction for anyone who's new. My name is Jeevendra Singh. I've been a software engineer since 2013. I've worked at Ericsson, SAP, Q2, and I've been at Microsoft for the past four-plus years. My background spans full-stack development, integration architecture, and more recently, Agentic AI development. Right now I'm working on AI copilots using Microsoft Copilot Studio, RAG pipelines, and Agent Orchestration for the Business and Industry Copilot team. So everything we talk about today is stuff I work with directly in production. It's practical, it's real-world, and it's what you'll need to build intelligent AI systems.

---

## SLIDE 3 — Welcome: Chat Introduction

Before we dive in, let's do a quick round of introductions. Go ahead and pop into the chat and tell us three things: your name, what you do, and where you're based. You can also mention your current company if you're comfortable with that. I'll give you a minute. Take a look at the screen — I've shown you an example of what that might look like. It's just so we know who's in the room and make the session a little more personal.

---

## SLIDE 4 — Structure of Class

Let me quickly walk you through how this class is structured. We have a four-hour Sunday live session — that's what we're in right now. There are also assignments after class: both multiple choice questions and coding assignments. The coding assignments are where the real learning happens, so please make sure you're attempting them. You should see two images here — one showing a live classroom experience, and one showing collaborative project work. That's the spirit of this program: learn together, build together.

---

## SLIDE 5 — Optimize Your Experience

A few tips to get the most out of today. First — interact. If something's unclear, speak up. I'd rather you ask a question than sit with confusion. Second, work through your assignments after class and get feedback. The Thursday review sessions are there specifically to help you with that. And use your resources. The value you get out of this program is directly proportional to what you put in. You have access to videos, exercises, solutions, Discord, TAs — use all of it.

---

## SLIDE 6 — We're Here to Help

Now, you might be looking at the topics today and feeling a little uncertain. Embeddings, vector databases, chunking — this can seem like a lot if you haven't touched it before. Don't worry. We're going to build everything from scratch, step by step. Every concept will be explained before we touch any code. And if you're still confused after the explanation, ask. That's exactly what we're here for.

---

## SLIDE 7 — IK Support Features

Just a quick reminder about all the support channels available to you. UpLevel has all your learning resources — videos, MCQs, assignments. There are optional post-class videos for additional reference. Wednesday technical coaching sessions are available to clear up any queries. The Discord community is great for peer learning. TAs are here during live class to help with questions. And if you have any concerns at all — technical or otherwise — raise a support ticket on UpLevel and the team will get back to you. Use all of these. They exist for you.

---

## SLIDE 8 — Success Hacks

A few quick success tips. Watch the pre-class videos before coming to class — it makes a huge difference in how much you absorb during the live session. Attend every class. Participate — don't just watch. Attempt all the assignments. Advocate for yourself if you need help. And most importantly, keep your goal in mind. Why did you join this program? Keep that front and center. Consistency is the key here. It's not about being brilliant in one session — it's about showing up and putting in the work every week.

---

## SLIDE 9 — API Key Email

One quick logistical item. You should have received an email containing your OpenAI API key for this course. Please check your inbox. If you don't see it, check your spam folder. If you still can't find it, reach out to the operations team at the email shown on the slide. You're going to need this API key for the demos today and for your assignments. So take a moment right now to make sure you have it. This key is for course use only — don't use it for personal projects, and don't share it.

---

## SLIDE 10 — Week 1 Recap: Agentic AI Foundations

Before we get into today's content, let's take a few minutes to recap what we covered in Week 1. This helps us connect the dots between what we already know and where we're going today.

---

## SLIDE 11 — Week 1 Recap Diagram

In Week 1 we covered the big picture of Agentic AI. We talked about the shift from AI that assists humans to AI that acts autonomously. We covered AI-driven software development lifecycles. We went deep on agent architectures — reflex agents that follow if-then rules, goal-based agents that plan, and utility-based agents that optimize. We covered the technical core: how LLMs work at the token level, the ReAct loop which is the Thought-Action-Observation cycle that drives most modern agents, and the four modules that make up an agent: its brain, its planning system, its memory, and its tools. We also covered the routing pattern and built a Hello Agent that could answer questions from a CSV file. And we ended by starting to build a CRM Lead Qualification agent. That was Week 1. Today we go deeper into the retrieval side.

---

## SLIDE 12 — Recap: The Anatomy of an Agentic Loop

Here's a quick visual reminder of the agentic loop. You have a prompt coming in and a result going out, and in between, there's an agent. The agent invokes a model. The model thinks through the problem and selects the right tool. The agent executes that tool. The tool returns a result. The agent feeds that back to the model. And eventually the model decides it has a complete answer and returns the final response. This loop is at the heart of every agentic system we'll build. Today we're focused on one specific type of tool in this loop: retrieval tools — the ability to search through a knowledge base and pull back relevant information.

---

## SLIDE 13 — Today's Agenda

Here's what we're covering today. Three modules. Module 1 is Text Embeddings — the foundation of semantic search. Module 2 is Chunking Strategies — how to break documents into the right-sized pieces for retrieval. Module 3 is Indexing Strategies for RAG — how to organize your chunks so retrieval is fast and accurate. We'll start with Module 1. Each module has a theory section followed by a live coding demo, so you'll see everything in action. Let's go.

---

## SLIDE 14 — Hands-On Project

We're going to learn all of these concepts through a real, hands-on project. Not abstract examples. A real system with real code. That system is called the SupportDesk RAG Assistant. Let me tell you what it does and why it exists.

---

## SLIDE 15 — Clone the Repository

Here's the GitHub repository you'll be working with throughout this course: SupportDesk-RAG-Workshop. The URL is on the slide. If you haven't already cloned it, do this now: run `git clone` with the URL shown, then `pip install -r requirements.txt` to get your dependencies, then configure your OpenAI API key in a `.env` file, and then you can run the demos from each module's directory. The repo has six complete modules: Embeddings, Chunking, Indexing, RAG Pipeline, Evaluation, and Agentic RAG. Each module has a demo, exercises, and solutions. Today we're doing modules one through three. Modules four, five, and six are Week 3. Quick note — you'll see that on the slide.

---

## SLIDE 16 — Problem Statement

Let me explain what we're actually building. We're building the retrieval layer for the SupportDesk RAG assistant. Specifically, the part of the system that can reliably find the most relevant past support tickets for any new issue that comes in.

Here's the real-world problem. Engineering and support teams deal with recurring issues. Users can't log in after a password reset. Database connections timeout in production. International payments fail. Emails aren't delivered. The thing is, someone has probably already solved these exact problems before, and the solution is sitting somewhere in a ticket database. But finding it is slow and painful, because: the data is unstructured text, not clean tables; people describe the same problem in completely different words; most search is keyword-based, so it misses conceptually similar tickets; and there are just too many tickets to read manually. That's the problem we're solving. We're building the system that can search that ticket history intelligently.

---

## SLIDE 17 — Why This Matters for Engineering Teams

Let me give you a sense of the business impact here, because this isn't academic. Look at the numbers on this slide. In terms of efficiency: without RAG, average resolution time is anywhere from six to thirty-six hours. With RAG and semantic retrieval, you can get that down to under an hour. That's a seventy-seven percent improvement in response time and a sixty percent reduction in ticket volume — because the system can handle more queries autonomously. In terms of intelligence: currently teams rely on tribal knowledge. When a senior engineer leaves, that knowledge walks out the door. RAG gives you institutional memory — a globally searchable history of everything that's ever been solved. In terms of reliability: instead of reactive fire-fighting, you can proactively spot failure patterns before they become incidents. That's a twenty-five percent improvement in customer satisfaction and a forty percent reduction in repeat incidents. These are real numbers. This is what you're building toward.

---

## SLIDE 18 — Why We Need Semantic Retrieval

Let me explain exactly why we need semantic retrieval and why simple keyword search isn't good enough. There are three critical gaps.

Gap one: LLMs don't know your data. If a user asks about a login failure after a password reset, and you just ask GPT-4 that question without any context, it'll give you generic steps. It has no idea what happened in your system, what tickets you've already resolved, or what the specific fix was. It guesses. And that's hallucination.

Gap two: Keyword search misses synonyms. If you search for "authentication failed" in a keyword-based system, you'll completely miss tickets that were filed under "auth login error" or "invalid credentials" or "can't log in." They're all the same problem but described differently. Keyword search returns zero results for those.

Gap three: Context and noise limits. You can't just dump millions of tickets into an LLM's context window. There's a limit, and even if there weren't, it would be incredibly expensive and slow.

The solution is semantic retrieval. Embeddings capture meaning, not just words. A vector store indexes all your tickets. Metadata filters let you narrow by category and priority. And the result is a grounded answer that cites real past solutions. That's what we're building.

---

## SLIDE 19 — The Dataset

Let's look at the dataset we'll be working with. We have a set of synthetic support tickets, each with a ticket ID, title, description, resolution, category, priority, and dates. The pipeline transforms these raw JSON ticket objects into LangChain Document objects with `page_content` and `metadata`. Those documents get chunked and split. The chunks get stored in a vector database. And when a new query comes in, we retrieve the top-k most relevant chunks and use them as context for the LLM.

The metadata is important — it carries the ticket ID, category, priority, and chunk information. This is what lets us filter results later. You can say "find me the most similar ticket, but only from the Authentication category." The metadata makes that possible.

---

## SLIDE 20 — Key Tech Stack

Here's the technology stack we're using across Weeks 2 and 3. The orchestration layer is LangChain — specifically the LangChain Expression Language, or LCEL. For advanced indexing in Module 3, we'll use LlamaIndex, which has excellent built-in support for different indexing strategies. Embeddings are generated via OpenAI's `text-embedding-3-small` model. The vector database is Chroma — a lightweight, local vector store that persists to disk. The LLM for generation is `gpt-4o-mini`. And the whole thing feeds into an evaluation layer in Week 3. Everything flows together: embed → store → retrieve → generate → evaluate.

---

## SLIDE 21 — Example Queries

Let me show you three concrete examples of what this system can do. A user types: "Users can't log in after resetting their password." Our system should find ticket TICK-001 in the Authentication category and return: "This is caused by stale session tokens. The fix is to clear active sessions and force re-authentication." A user types: "I'm seeing 402 errors on international payments." The system finds ticket TICK-003 in the Payment Gateway category and returns: "Enable the international processing flag in the gateway configuration." A user types: "Why is the dashboard slow?" The system finds ticket TICK-010 in the Performance category and returns: "It's likely an N+1 query issue. Check if Redis caching is enabled for aggregate stats."

Notice that none of those user queries used the exact words in the ticket titles. "Can't log in" maps to "Authentication failure." "402 errors" maps to "payment gateway configuration." "Dashboard slow" maps to "N+1 query." That's the power of semantic search. Let's build it.

---

## SLIDE 22 — Let's Get It Started

Alright, before we dive into any code, I want to spend a few minutes giving you the big picture — because if you understand *why* we're building each piece and where it fits, everything else will click into place much faster.

**The fundamental problem we're solving.**

You have a large language model — something like GPT-4. It's incredibly capable. It can reason, summarize, explain, write code. But it has one critical limitation: it only knows what it was trained on. It has a knowledge cutoff. It has never read your internal documentation. It has never seen your support tickets. It has no idea what happened in your company last week. If you ask it about those things, it will either say "I don't know" — or worse, it will make something up. That's called hallucination. And in enterprise settings, hallucination is not acceptable.

So the question becomes: how do you give a pre-trained LLM access to your private, specific, up-to-date knowledge — without retraining it from scratch?

**Why not just fine-tune the model?**

This is the question everyone asks. And it's a fair question. Fine-tuning means taking a pre-trained model and continuing to train it on your own data so it "learns" your domain. Here's why that's often not the right answer:

First, cost. Fine-tuning requires GPU compute, large datasets, training pipelines, evaluation infrastructure. You're looking at thousands of dollars per run, minimum. And every time your data changes, you run it again.

Second, freshness. A fine-tuned model has a snapshot of your data baked into its weights from the moment of training. If your documentation changes tomorrow, the model doesn't know. You'd have to retrain. RAG retrieves from a live database — update your documents, the system updates instantly.

Third, transparency. When a fine-tuned model answers a question, you have no idea where that answer came from. Was it from document A or document B? You can't tell. RAG can cite exact source chunks — you know exactly what grounded every answer.

Fourth, hallucination is not solved by fine-tuning. A fine-tuned LLM still generates from memory. It still invents things confidently. RAG grounds every answer in retrieved evidence — the LLM reads actual relevant context before responding.

Fifth, catastrophic forgetting. Fine-tuning on a narrow domain can cause the model to degrade on everything else it knew. RAG preserves the base model completely.

**RAG: the architecture that solves all of this.**

RAG — Retrieval Augmented Generation — works in two phases. First, an offline phase: you take all your documents, process them, and build a searchable knowledge store. Second, an online phase: when a query comes in, you retrieve the most relevant pieces from that store and feed them to the LLM as context. The LLM doesn't need to memorize your data — it reads the relevant parts, on demand, for every single query.

Here is the complete RAG pipeline:

```
╔══════════════════════════════════════════════════════════════════════════╗
║                    OFFLINE — KNOWLEDGE INGESTION                        ║
╚══════════════════════════════════════════════════════════════════════════╝

  Raw Documents                                          Vector Store
  (PDFs, tickets,  →  [CHUNKING]  →  [EMBEDDING]  →  [ INDEX / DB ]
   wikis, code)         ▲                 ▲                 ▲
                        │                 │                 │
                   Module 2 ◄─────── Module 1 ────────► Module 3
                  (this week)         (this week)        (this week)


╔══════════════════════════════════════════════════════════════════════════╗
║                     ONLINE — RETRIEVAL + GENERATION                     ║
╚══════════════════════════════════════════════════════════════════════════╝

  User Query                                                   Answer
      │                                                           ▲
      ▼                                                           │
  [EMBEDDING]  →  [VECTOR SEARCH]  →  [RETRIEVED CHUNKS]  →  [ LLM ]
                        ▲                      ▲                  ▲
                        │                      │                  │
                   Module 3 ◄──────────── Week 3 ──────────►  Week 3
                  (this week)            (next week)          (next week)
```

Let me walk you through this left to right.

On the offline side — which is what today is all about — you start with raw documents. Those could be support tickets, internal wikis, PDFs, code files, anything. The first step is **chunking**: you break those documents into smaller, meaningful pieces. Too large and the chunk is noisy — it has too much irrelevant context. Too small and you lose coherence. Getting chunking right is an art, and Module 2 is entirely about that.

Once you have chunks, you run each one through an **embedding model**. The model converts each chunk from text into a vector — a list of numbers that represents its meaning in high-dimensional space. That's Module 1, and we start there. Understanding embeddings is the foundation of everything.

Those vectors are then stored in a **vector index** — a searchable database organized so you can find the nearest vectors quickly. How you structure that index — flat, hierarchical, keyword-based, hybrid — dramatically changes what you can retrieve and how fast. That's Module 3.

On the online side — which comes in Weeks 3, 4, and 5 — a user query arrives, gets embedded into the same vector space, and a similarity search finds the most relevant chunks. Those chunks get assembled into a prompt for the LLM. The LLM reads that context and generates a grounded, cited answer. That's the full pipeline: not the LLM hallucinating from memory, but the LLM reading actual relevant evidence and reasoning over it.

**What we're building today — the knowledge infrastructure.**

Modules 1, 2, and 3 are the left side of that diagram. The offline pipeline. The knowledge foundation. Without this side done well, no amount of clever prompting or agent design on the generation side will save you. Garbage in, garbage out. If your chunks are bad, your retrieval is bad. If your retrieval is bad, your LLM answers are bad — even with a perfect model.

So today we're building the foundation. Next week, we wire it all together into a working RAG pipeline and start building agents on top of it.

Alright. Let's start with Module 1: Text Embeddings.

---

## SLIDE 23 — Text Embeddings: Vector Databases

Alright, this is the heart of everything we're doing today, so I want to take my time here and make sure everyone truly gets it before we touch any code.

Let me start with a question. Think about how you search for data in a traditional system. If you're working with a relational database — say a MySQL table — you write a SQL query. You say: give me all rows where `status = 'open'` or where `ticket_id = 'TICK-001'`. The database looks for an exact match and returns the result. Simple. Fast. Works great for structured data.

Now what if the data isn't structured? What if instead of looking up a ticket ID, a user types something like: "My app keeps crashing when I try to log in on mobile." That's a sentence. A natural language question. It doesn't match any column value exactly. So how do you find the relevant ticket in a database of thousands?

The naive answer is: search for those words. Find tickets that contain "crashing" or "log in" or "mobile." That's a keyword search, and it's what most systems do by default. And it works — sometimes. But it completely falls apart the moment someone phrases things differently. What if the ticket was filed as "iOS authentication failure"? The words "crashing," "log in," and "mobile" don't appear. The keyword search returns nothing. But the meaning is identical.

This is the fundamental problem that embeddings and vector databases solve.

Here's the core idea. Instead of representing text as a string of characters, we represent it as a point in a mathematical space. Specifically, a very high-dimensional space — think of it like a coordinate system, but instead of x, y, z for three dimensions, we have 1536 dimensions. Each piece of text gets mapped to a specific point in that space by an embedding model. And here's the magic: the embedding model is trained so that texts with similar meanings end up near each other in that space. "iOS authentication failure" and "app keeps crashing when I try to log in" would be close to each other. "Today's weather is sunny" would be far away from both of them.

So when a user types a query, we convert that query into a point in the same space. Then we search the database to find which stored points are closest to it. Those closest points are the most semantically similar documents. That's semantic search.

Look at the diagram on screen. On the left, your text — whether it's a support ticket, a document, or a user question — goes into the embedding model. The model outputs a vector: a list of numbers, like `[3.8, 4.8, 8.3, 1.5, ..., 0.67]`. That vector gets stored in the vector database, represented as a point in that high-dimensional space. On the right, when a query comes in, it goes through the same embedding model, becomes a vector itself, and the database finds the nearest points to it. That search result — those nearest points — gets returned as your matched documents.

One thing I want you to internalize right now: the vector database is not magic. It's just a very efficient way to answer the question: "which of these stored vectors are closest to this query vector?" Everything else — the intelligence, the understanding of meaning — lives entirely inside the embedding model. That model was trained on massive amounts of text to understand relationships between words and concepts. The database just stores and searches the output.

This whole system has a name: retrieval via semantic similarity. And it is the foundation on which RAG is built. Without this, there is no RAG. Everything else we do today sits on top of this idea.

---

## SLIDE 24 — Storing Embeddings in Vector Databases

And here's what makes it really powerful: it's not just text. The same idea applies to images, audio, any kind of data. You pass it through an appropriate embedding model — a text model, an image model, an audio model — and you get back a vector. All of those vectors live together in the same vector database. And you can do similarity search across all of them. Today we're focused on text, but the underlying principle is the same regardless of data type.

---

## SLIDE 25 — Vector Store: How Do You Search Text?

Let me frame the core question. We know how to search for structured data in SQL or NoSQL databases. But how do you search for text data? You've got two obvious options. You could search by looking at a database of text documents. Or you could search within the text itself. Both feel natural. But here's the question I want you to think about: can we just do a string match?

---

## SLIDE 26 — Vector Store: Why Not String Match?

Why not? What's wrong with string matching? Let's think about it.

---

## SLIDE 27 — Vector Store: Limitations of String Match

Two problems. First: it doesn't handle synonyms or rephrasing. "Car" and "Vehicle" mean the same thing, but a string match won't connect them unless the exact word appears. Second: no semantic understanding. If a user asks "I'm travelling to Mexico, what phone plan should I use?" — a string match against "international plans" will return nothing. There's no overlap in the words. But those two things are clearly related. A human reading both would immediately understand the connection. String matching can't do that. What can we use instead? Embeddings.

---

## SLIDE 28 — Vector Store: The Embedding Pipeline

Here's the full picture. On the left side — the offline side — you take your documents, pass them through an embedding model, and get back vectors. You store those vectors in a vector database. On the right side — the online side — when a query comes in, you pass it through the same embedding model, get back a vector, and search the database for the closest matches using K-Nearest Neighbors. The search returns the most similar documents. Quick question: what type does the output return?

---

## SLIDE 29 — Vector Store: Output is Text

The answer is: text. Not embeddings. The vector store does the similarity comparison internally, but what it returns to you is the original text of the matching documents. This is an important point: embeddings are a mechanism for search, but you never hand embeddings to your LLM. You hand it the text. The embeddings are just how you find the right text.

Now — before we move on, I want to go a level deeper here, because a question I get constantly is: "What is actually inside a vector database? What does it store?" Let's answer that properly.

---

### How Vector Databases Store Data and Metadata

A vector database doesn't just store a vector. Every record is actually made up of four components. Let me walk through each one.

**Component 1: ID.** Every record has a unique identifier — a primary key. It could be something like `"ticket_001"`, or a UUID, or even something that encodes information like `"doc_2024_01_15_001"`. Best practice is to keep the ID consistent with your source database, so you can always trace a result back to where it came from.

**Component 2: The Vector.** This is the embedding itself — a list of 1536 floating point numbers for `text-embedding-3-small`. Each number is a 32-bit float, which is 4 bytes. So a single vector takes up about 6 kilobytes. Scale that up: one million vectors is around 6 gigabytes of vector storage alone. This is why vector storage dominates the size of any RAG system's database.

**Component 3: The Document.** This is the original text that generated the vector. The reason we store it here is simple: you cannot reverse an embedding back into text. Embeddings are a one-way transformation. So if you want to return the original content to the user, you have to store it. The vector is for searching. The document is for returning.

**Component 4: Metadata.** This is structured, filterable information attached to each record — things like category, priority, date created, status, tags, customer tier. This is arguably the most powerful component, because it lets you combine semantic search with structured filtering. For example: "Find me the most similar ticket to this query, but only within the Authentication category, and only High priority ones." The semantic search narrows by meaning. The metadata filter narrows by structure. Together, they're extremely precise.

Here's what that looks like in code for our workshop:

```python
metadata = {
    "category": "Authentication",
    "priority": "High",
    "created_at": "2024-01-15",
    "tags": ["password", "reset", "login"],
    "chunk_index": 0
}
```

And then you search with:

```python
results = collection.query(
    query_texts=["login issue after password reset"],
    where={"category": "Authentication"},
    n_results=5
)
```

The `where` clause applies the metadata filter. Only documents matching that category even get considered for the similarity search. This is called pre-filtering — filter first, then search within the filtered set. Some databases also support post-filtering — get the top hundred by similarity, then filter down to high priority. Each approach has trade-offs, and we'll see both in the code.

---

### A Quick Look at Popular Vector Databases

You'll hear several names in the wild. Let me give you the landscape so you know what you're looking at.

**ChromaDB** — this is what we use in this workshop. It's open source, embedded, zero configuration. It runs right inside your Python process, stores everything locally on disk using SQLite for metadata and a binary HNSW index for vectors. It's ideal for learning, prototyping, and small to medium projects. If you're building a proof of concept or an internal tool with under a million vectors, ChromaDB is perfect. It's free, requires no accounts or external services, and the concepts you learn with it transfer directly to everything else.

**Pinecone** — the fully managed cloud option. Zero infrastructure to run. You create an index, upsert vectors, and query — Pinecone handles everything else: scaling, replication, uptime. It's production-grade with a 99.99% SLA, and it has strong metadata filtering. The trade-off is cost — it starts at around seventy dollars a month for production tiers — and there's no self-hosting option. You're committing to their cloud. For teams that want to move fast and not manage infrastructure, it's a strong choice.

**Weaviate** — the most powerful and most complex option. Open source, self-hosted or managed cloud. It has built-in vectorizers, meaning you can configure it to call OpenAI automatically when you insert a document — no separate embedding step. It supports hybrid search natively, combining vector similarity with BM25 keyword search in a single query. It uses a GraphQL API. It requires a schema upfront, which adds overhead but also enforces consistency. Best for complex search scenarios, multi-modal applications, or teams that need open-source at scale.

Here's how to think about the choice: use ChromaDB while learning and prototyping. Move to Pinecone if you want managed production with minimal ops. Move to Weaviate if you need hybrid search, multi-modal support, or want open-source at enterprise scale.

For today and for your assignments, everything runs on ChromaDB. You'll see exactly how the four components — ID, vector, document, metadata — get stored and queried as we run the demos.

---

## SLIDE 30 — What is an Embedding?

Let me make this concrete. An embedding is a vector representation of a piece of text — a list of numbers that encodes the meaning of that text. Think of it as coordinates in a high-dimensional space, where similar meanings are located close to each other. In a simplified 2D space, "cat" and "dog" would be close. "Car" and "truck" would be close. "Cat" and "car" would be far apart. But instead of 2 dimensions, we're working in 1536 dimensions — which is what OpenAI's `text-embedding-3-small` model produces. Each word or phrase maps to a vector of 1536 floating point numbers. You can't read those numbers directly and understand them, but together they encode the semantic meaning of the text. And that's what makes semantic search possible.

---

## SLIDE 31 — Demo 1: Text Embeddings

Alright, let's open the code. Navigate to `modules/1_embeddings/demo.py`. Before we run anything, let me tell you exactly what we're going to do in this demo so you know what to watch for.

The demo is structured in five parts:

**Part 1 — Generate Embeddings.** We take each support ticket, combine its title and description into a single text string, and call the OpenAI embeddings API to get one vector per ticket. By the end of this part we have a NumPy array of shape `(num_tickets, 1536)` — every ticket represented as a point in 1536-dimensional space.

**Part 2 — Compute Similarity Scores.** We take a test query — "Users can't login after changing password" — embed it with the same model, and then compare that query vector against every ticket vector using cosine similarity. Cosine similarity is our distance metric here. There are others — dot product, Euclidean distance — but cosine is the standard for text embeddings and that's what we focus on. The result is one similarity score per ticket, ranging from negative one to positive one.

**Part 3 — Retrieve the Most Similar Tickets.** We sort all tickets by their similarity score in descending order and return the top five. This is the retrieval step — the core of semantic search. No keywords, no exact matching — just ranked similarity.

**Part 4 — Visualize Embedding Relationships.** This is an optional visualization step, not core retrieval logic. We generate a similarity heatmap to sanity-check what the model has understood: which tickets are close to each other, and how strongly each one matches the query. It's useful for building intuition, especially when you're learning.

**Part 5 — Experiment with Different Queries.** We run four more test queries — about database timeouts, international payment failures, app crashes on iPhone, and emails not sending — and for each one we show the best-matching ticket. The point here is to demonstrate semantic matching across completely different wording. The query and the ticket won't share the same words, but the model finds the right match anyway.

Now let's walk through it.

*[Open the file and walk through it live]*

*[Run the demo, walk through the output, show the heatmap]*

Any questions on embeddings before we move on?

---

## SLIDE 32 — Q&A

Let's take a few minutes for questions. Ask about anything — the concepts we just covered, how this applies to your specific work, implementation details, anything you want to clarify. If your question gets missed accidentally, please repost it in the chat. Remember: if you're wondering about something, there are probably five other people wondering the same thing.

---

## SLIDE 33 — Break

We're going to take a ten-minute break now. Please come back when the timer hits zero. Grab some water, stretch. We'll pick up with Module 2 — Chunking Strategies — which is where things get really interesting.

---

## SLIDE 34 — Today's Agenda: Module 2

We're back. Module 1 is done — embeddings, cosine similarity, semantic search. Now we move to Module 2: Chunking Strategies. This is all about how you break long documents into the right-sized pieces before you embed and store them.

---

## SLIDE 35 — Chunking: What We've Covered

So far we've covered embeddings and vector stores. We know how to convert text into vectors, how to store them, and how to search them. But here's a question: what if your document is too long to embed in one shot? Or what if embedding the whole document means you lose precision — the embedding captures the general topic but misses the specific detail you actually need to retrieve? That's what chunking solves.

---

## SLIDE 36 — Chunking: What Is This?

Chunking is the process of splitting a long document into smaller, more manageable pieces before embedding them. This slide introduces the third component alongside embeddings and vector stores. The question on screen is "what is this though?" — and that's exactly what we're going to answer now.

---

## SLIDE 37 — Strategy 1: Fixed-Size Chunking

The first and simplest strategy is fixed-size chunking. You split the text into uniform segments based on a predefined number of characters, words, or tokens. In this example, you can see "Artificial intelligence is transforming technology and shaping the future" split into Chunk 1 and Chunk 2, with an overlap in the middle. That overlap region — "transforming technology" in this case — is repeated in both chunks. Why? Because without overlap, you lose context at chunk boundaries. Imagine a sentence split in half. The second chunk starts mid-thought, with no context about how the thought began. The overlap makes sure you always have enough context.

Fixed-size chunking is simple and predictable. But it has one problem: it's not semantic. It might split mid-sentence, mid-word, or mid-concept. It doesn't know anything about the meaning of the text. It's just counting characters.

---

## SLIDE 38 — Strategy 2: Semantic Chunking

Semantic chunking is at the other extreme of the spectrum. Instead of counting characters, you use the embedding model itself to detect when the topic changes. Look at the bottom of this slide — you can see a real example of semantic chunking in action. The paragraph is about Artificial Intelligence, and it's highlighted in two different colours showing where the chunker decided to split.

The paragraph reads: "Artificial intelligence is transforming industries by automating processes, enhancing decision-making, and providing insights through data analysis. Machine learning, a subset of AI, enables systems to learn and improve from experience without explicit programming. Deep learning, a branch of machine learning, uses neural networks with multiple layers to model complex patterns in data."

Now, you might look at that and say — those sentences all seem to be about the same thing. And they are, broadly. But watch what the algorithm detects. The first two sentences are about AI and machine learning at a general level: transforming industries, automating processes, learning from experience. The third sentence introduces Deep Learning — a more specific sub-domain with its own vocabulary: neural networks, multiple layers, complex patterns. The embedding model picks up on that subtle shift. The first two sentences cluster together in vector space. The third sentence sits slightly apart. The similarity between sentence two and sentence three drops just enough to trigger a split. You get two chunks: one covering the general AI and machine learning description, and one starting from "Deep learning."

That's the power of semantic chunking. It doesn't need headers or markers. It reads the meaning. And it can detect not just obvious topic changes but subtle conceptual shifts within what looks like a single topic.

Here is the algorithm, step by step.

**Step 1: Split the document into sentences.** The text gets broken into individual sentences — in this case three.

**Step 2: Embed each sentence.** The embedding model is called once per sentence. Sentence 1 and sentence 2 produce vectors pointing in a similar direction — both about AI at a high level. Sentence 3 introduces Deep Learning terminology and produces a vector that sits slightly apart in the embedding space.

**Step 3: Compare consecutive sentences using cosine similarity.** Sentence 1 to sentence 2 — high similarity, same general topic, keep them together. Sentence 2 to sentence 3 — the similarity drops enough to cross the threshold. That's the split point.

**Step 4: Create chunks at the split points.** Chunk 1: the two general AI and machine learning sentences. Chunk 2: the deep learning sentence. No marker was provided. The model inferred the boundary from meaning.

The diagram at the top of the slide shows the full algorithm loop: segment the document, create an initial chunk, keep adding new segments until cosine similarity drops drastically, at which point you finalise the first chunk and start the second.

Now — there are two real-world edge cases that will catch you out if you don't know about them.

**Edge Case 1: Related sentences that are not consecutive.** Imagine a document where the topics alternate — an AI sentence, then a deep learning sentence, then a general AI sentence again, then another deep learning sentence. Basic semantic chunking only compares consecutive pairs. It would see a drop at every boundary and create four single-sentence chunks, even though the two AI sentences belong together and the two deep learning sentences belong together. The fix is to compare each new sentence not against the previous sentence alone, but against the average embedding of the current chunk as a whole. That way the chunk "remembers" its overall topic and a related sentence that arrives a few positions later will still match it.

**Edge Case 2: A very long passage on the same topic.** Imagine the deep learning section expanded from one sentence to fifty — all highly similar to each other. Semantic chunking would never split and you'd end up with one giant chunk, potentially thousands of tokens, well above your embedding model's limit. Production semantic chunking always enforces two conditions simultaneously: has the topic changed significantly, OR would adding this sentence exceed the size limit? If either is true, start a new chunk. LangChain's `SemanticChunker` handles this through its `breakpoint_threshold_type` parameter and optional size constraints. The key takeaway: pure semantic chunking without a size limit is almost never used in production. The real implementation is always topic-aware plus size-aware together.

The cost implication is worth stating clearly. For this three-sentence paragraph, we make three embedding API calls just to determine where to put the chunk boundaries — before any retrieval query has been issued. In the demo code you'll see shortly, we use a longer paragraph with thirteen sentences covering three completely unrelated topics — database performance, weather, and authentication security. That's thirteen API calls just for chunking. For a small, high-value corpus — documentation, runbooks, legal contracts — that upfront cost is absolutely justified by the quality of the resulting chunks. For a dataset of fifty thousand support tickets, you would use recursive chunking instead and accept slightly less semantic precision in exchange for dramatically lower cost and faster indexing.

---

## SLIDE 39 — Strategy 3: Recursive Chunking

This is the one you'll use most often, and it's my recommended default for most use cases. Recursive chunking tries to split on natural boundaries, starting with the most natural ones first. Here's the hierarchy: first try paragraph breaks (`\n\n`). If a paragraph is still too big, split on line breaks (`\n`). Still too big? Split on sentences. Still too big? Split on words. Last resort — characters. The key insight is that this approach respects the natural structure of text. It won't split in the middle of a sentence if it can possibly avoid it. The diagram on screen shows this recursive loop: if a segment exceeds the size limit, split further. If not, keep it as is. The result is chunks that are semantically coherent even though the algorithm doesn't use embeddings.

---

## SLIDE 40 — Strategy 4: Document Structure-Based Chunking

If your documents have explicit structure — like markdown headers, HTML tags, or chapter headings — you can use that structure to define your chunks. For markdown, you split on heading levels: H1, H2, H3. Each section becomes a chunk. And critically, the metadata of each chunk includes the header hierarchy. So a chunk about "Authentication Failures" in the "Database Troubleshooting Guide" would carry that context in its metadata — even if the chunk text doesn't mention the guide title. This is incredibly useful for documentation, runbooks, wikis, anything with an inherent table of contents. The diagram shows a document with title, Section 1, Section 2, and Conclusion — each becoming its own chunk, with optional recursive splitting if any section is too large.

---

## SLIDE 41 — Strategy 5: LLM-Based Chunking

The most powerful and most expensive approach. Instead of using heuristics or embedding similarity to detect boundaries, you simply ask the LLM to create semantically isolated, meaningful chunks. You prompt it: "Here is a document. Please split it into self-contained chunks where each chunk covers a single coherent idea." The LLM can understand context and meaning in ways that no heuristic can match. The downside is obvious: you're calling the LLM for every document at indexing time. For a small, high-value knowledge base, that might be worth it. For millions of support tickets, you'd be bankrupt before you finished indexing.

---

## SLIDE 42 — Cheat Sheet: 5 Chunking Strategies

Take a photo of this slide or bookmark it for reference. We've covered all five strategies: fixed-size, semantic, recursive, document structure, and LLM-based. Each one has a diagram summarizing how it works. The mental model is simple: simpler strategies are cheaper and faster; smarter strategies are more expensive but produce higher quality chunks. For most real-world use cases, recursive chunking is your default. Add semantic chunking if you have a high-quality, smaller corpus and retrieval precision is critical.

---

## SLIDE 43 — Demo 2: Chunking Strategies

Let's open the code. Navigate to `modules/2_chunking/demo.py`.

Before we run it, let me tell you something important about this demo. Everything in Module 2 is built using the **LangChain framework**. This is a deliberate choice, and I want you to recognise the specific LangChain building blocks as we go through the code, because these are components you'll use in almost every RAG system you build.

Here are the LangChain concepts this demo uses, end to end:

**1. Document Abstraction — `langchain_core.documents.Document`.** LangChain has a standard wrapper for any piece of text you want to index. It has two fields: `page_content`, which is the actual text, and `metadata`, which is a dictionary of structured attributes — things like ticket ID, category, priority. This abstraction is consistent across all of LangChain. Every splitter, every vector store, every retriever speaks the same Document language. This is how chunkers receive their input, and how retrieval results come back to you.

**2. Text Splitters — `langchain_text_splitters`.** LangChain gives us a suite of chunking classes:
- `CharacterTextSplitter` — fixed-size chunks
- `RecursiveCharacterTextSplitter` — hierarchical splitting by paragraph, sentence, and word boundaries (your default)
- `MarkdownHeaderTextSplitter` — structure-aware splitting for markdown documents
- `HTMLHeaderTextSplitter` — structure-aware splitting for HTML documents
- `SemanticChunker` from `langchain_experimental` — embedding-based topic-aware boundaries

All of these take a list of Documents in and return a list of smaller Documents out. Same interface, different splitting logic.

**3. Embedding Model Wrapper — `langchain_openai.OpenAIEmbeddings`.** Rather than calling the OpenAI API directly as we did in Module 1, here we use LangChain's wrapper. It handles batching, retries, and plugs directly into LangChain's vector store layer. You pass it to Chroma and it takes care of converting text to vectors automatically.

**4. Vector Store — `langchain_community.vectorstores.Chroma`.** LangChain integrates with Chroma through a single call: `Chroma.from_documents(documents, embedding=embeddings_model, persist_directory="./chroma_db")`. This one line chunks your documents, embeds them, stores the vectors alongside the original text and metadata, and persists everything to disk. When you restart your script, the data is still there.

**5. Retrieval Methods.** LangChain's Chroma integration exposes three retrieval patterns:
- `similarity_search(query, k)` — top-k nearest neighbours by cosine similarity
- `max_marginal_relevance_search(query, k)` — MMR, which balances relevance with diversity
- `similarity_search(query, k, filter={...})` — metadata-filtered semantic search

So the full pipeline this demo implements is: Documents → Chunking (text splitters) → Embeddings (OpenAIEmbeddings) → Vector store (Chroma) → Semantic retrieval + filtering. That is the canonical LangChain retrieval pipeline. Every piece of it is a named, reusable LangChain component.

The demo is structured in four parts:

**Part 1 — Chunking Strategies.** We walk through five different chunking approaches: fixed-size, recursive, semantic, markdown-aware, and HTML-aware. Each one uses a different LangChain splitter class. We'll see what chunks each one produces and understand when you'd choose each.

**Part 2 — Chroma Vector Store.** We take the chunked documents, embed them using `OpenAIEmbeddings`, and load them into a Chroma vector store. Then we run similarity search against a test query and see what comes back.

**Part 3 — Metadata Filtering.** We re-run the same search but this time with a filter — first filtering by category, then by priority. This shows how you can constrain the semantic search space using structured metadata, giving you precision you can't get from embeddings alone.

**Part 4 — Compare Chunking Strategies.** We build three separate vector stores — one with whole documents, one with fixed-size chunks, one with recursive chunks — run the same query against all three, and compare what gets returned. This makes the impact of chunking concrete and observable.

Now let's walk through it.

*[Open the file and walk through it live]*

*[Run the demo, walk through the output]*

Questions on chunking before we continue?

---

## SLIDE 44 — Q&A

Questions on either embeddings or chunking? Now is a good time. If you've been waiting to ask something, please go ahead. Post in chat too — I'll try to get to everything.

---

## SLIDE 45 — Short Break

Five-minute break. We're moving into Module 3 after this — Indexing Strategies. This is where we talk about the different ways to organize your chunks for retrieval. We'll be using a different framework for this one: LlamaIndex instead of LangChain. I'll explain why when we get back. See you in five.

---

## SLIDE 46 — Today's Agenda: Module 3

We're back. Module 3: Indexing Strategies for RAG. This is the final module for today and it's where we step back and think at a higher level about how the retrieval layer is organized in a production system.

---

## SLIDE 47 — Why Indexing Is Required in RAG

Let me explain why indexing matters — and before I do, I need to flag something important, because this is a word that gets used in two completely different ways and causes a lot of confusion.

**Two meanings of "indexing" — do not mix them up.**

The first meaning is what I'll call RAG-level indexing, or knowledge indexing. This is what *you*, the developer, control. It's about how you organize your private data before any query ever happens — how you chunk documents, whether you build hierarchies, whether you create summaries or keyword tables or multiple logical indexes. The question this answers is: *what knowledge is even retrievable in this system?*

The second meaning is DB-level indexing, which is about how a vector database internally searches vectors quickly. HNSW, IVF, Product Quantization — these are database algorithms that determine *how fast* the search runs once the vectors exist. You typically don't design this; your vector DB handles it for you.

In this module, we focus entirely on the first kind — RAG-level knowledge indexing. The higher-level design that determines what your system can retrieve.

Now, here's an insight from the notes that I want you to carry with you: **Storage is flat. Retrieval is smart.**

When you hear the words "Vector Index" or "Tree Index" or "Keyword Index," don't think of them as different ways of storing data. The underlying storage is almost always the same — a flat array of embedding vectors in a database. What's different is the *retrieval logic* — how you traverse, filter, and combine results when a query comes in. Different indexes are really different retrieval strategies sitting on top of the same flat storage.

So why does indexing strategy matter at all? Because not all queries need the same retrieval approach. A specific question like "What's the API key for the staging environment?" needs a fast, targeted vector similarity match — get me the one chunk that answers this. A broad question like "Tell me about common authentication problems" needs to pull together multiple related chunks from different places. An exploratory query like "What kinds of issues are most common overall?" needs to browse across the entire knowledge base hierarchically. One retrieval strategy cannot serve all three of these well.

The diagram on screen shows the full RAG architecture. On the left, documents flow through chunking, embedding, and into vector storage. On the right, a user query gets vectorized, matched, and the relevant context gets passed to the LLM for generation. The key sentence: *Indexing happens offline. Retrieval happens online at query time.* You build the index once — or update it on a schedule. Every query benefits from it instantly.

One more thing before we go into the demo. In this module we're switching from LangChain to LlamaIndex. A quick word on why. LangChain is excellent at orchestration — chains, agents, memory, integrations. LlamaIndex was purpose-built for document indexing and retrieval. It has clean, first-class abstractions for all five indexing strategies we're about to explore — Vector, Summary, Tree, Keyword, and Hybrid. LangChain would require significantly more custom code to demonstrate the same patterns. In production, these two frameworks integrate seamlessly — LlamaIndex handles your indexing, LangChain handles your chains and agents. Think of them as complementary tools, not competing ones. Different frameworks, same concepts. Everything you learn here applies universally.

---

## SLIDE 48 — Why Multiple Indexes Exist in Production

Here's something important that we don't often talk about in tutorials: in production, you almost never have a single index. You have multiple indexes, each optimized for a different use case. Look at the five reasons on this slide.

Different data types. PDFs want large chunks. FAQs want small question-answer chunks. Code wants syntax-aware chunks. Structured tables want a completely different approach. You can't index all of these the same way.

Different search strategies. Dense vector search is great for semantic meaning. Keyword search is great for exact terms, IDs, error codes. Hybrid combines both.

Domain separation. Your HR policies should live in a different index from your engineering runbooks. Mixing them creates noise. Keeping them separate means better hit relevance for each query type.

Update frequency. Weekly policy documents can be batch-processed overnight. Hourly incident tickets need mini-batch updates. Real-time log events need streaming ingestion. Each data source has a different freshness requirement.

Security and access. PII data needs to be isolated. Legal documents need restricted access. Multi-tenant systems need indexes separated by team or customer. Metadata filters and routing enforce these boundaries.

The bottom line: a production RAG system is not one index. It's a collection of specialized indexes, and a routing layer that decides which index to use for each query.

---

## SLIDE 49 — Intent-Based Query Routing

This is what that routing layer looks like in practice. Every incoming query goes through intent classification. Based on what the user is trying to do, the query gets routed to the right index with the right search strategy.

Fact lookup queries — like "What's the PTO carryover limit?" — go to a FAQ or policy index with keyword plus hybrid search and weekly batch updates. Troubleshooting queries — like "Error 500 on service X?" — go to runbooks and incident tickets with recent filtering and hourly updates. How-to queries go to a dense knowledge base. Status queries go to a real-time incident index with recency weighting. Code questions go to a syntax-aware code index. Structured metric queries go straight to SQL or a structured backend.

This is what a mature RAG system looks like. You're not just throwing all your data into one Chroma collection and calling it a day. You're thinking about what queries are being asked, where the right data lives, and how to route intelligently. Keep this picture in mind as we build out the rest of the course.

---

## SLIDE 50 — Live Zoom Poll

We're launching a quick poll on Zoom right now. Please take two minutes to fill it out. It's a quick check-in on where everyone is with the material. We'll look at the results together.

*[Wait for poll results, briefly comment on them]*

---

## SLIDE 51 — Demo 3: Indexing Strategies

Alright, let's open the code for Module 3. Navigate to `modules/3_indexing/demo.py`. And this is where we switch frameworks. We're using LlamaIndex instead of LangChain for this demo. Quick explanation of why. LangChain is excellent at orchestration — chains, agents, integrations. LlamaIndex is excellent at document indexing and retrieval patterns. It has built-in support for all five of the indexing strategies we're about to demo. In practice, you can mix both — LlamaIndex handles your indexing, LangChain handles your chains and agents, and they integrate seamlessly.

*[Open the file and walk through it live]*

Let me walk you through the five strategies.

**Part 1: Vector Index.** This is the most common approach and your default starting point for any RAG application. At build time, each document gets embedded and stored as a vector. At query time, the query gets embedded and the nearest neighbors are found by cosine similarity. In the code, we call `VectorStoreIndex.from_documents(documents)` — LlamaIndex handles chunking, embedding, and storage automatically. We create a query engine with `similarity_top_k=3` and call `query()`. The response includes both the synthesized answer and the source documents with similarity scores. Fast. Effective for most use cases. The default.

**Part 2: Summary Index.** Completely different approach — no embeddings at all. At build time, documents are just stored as-is. At query time, the LLM looks at each document and asks: is this relevant to the query? The ones that are get combined and summarized into an answer. The power of this: the LLM has full document context, not just fragments. The weakness: it's linear — O(n). For ten documents it's fine. For ten thousand documents, you'd be waiting hours. Use this only for small collections where you need deep, nuanced relevance judgement that embedding similarity might miss.

**Part 3: Tree Index.** This is for large document collections. At build time, LlamaIndex creates leaf nodes from each document, then calls the LLM to generate summaries for groups of related documents, building up a tree until you have a single root summary. This is expensive to build — many LLM calls. But at query time, you start at the root and traverse downward: "which branch is most relevant?" — then go deeper. Instead of searching fifty documents linearly, you make about three or four LLM decisions and arrive at the right answer in logarithmic time. For a thousand documents: flat search is a thousand comparisons. Tree traversal is about ten LLM decisions. That's the trade-off: expensive to build, efficient to query.

**Part 4: Keyword Table Index.** This is the traditional approach — the one that predates embeddings. It builds an inverted index: keyword maps to a list of document IDs. If you search for "password reset," it looks up all documents that contain those words. Exact match. The limitation is obvious: "authentication" won't match "login" unless they appear in the same document. No semantic understanding. But there are use cases where this is exactly what you want: error codes, ticket IDs, product names, version numbers. These are exact tokens that should match exactly.

**Part 5: Hybrid Retrieval.** This is the production approach. Vector search and keyword search are complementary. Vector search finds conceptually similar content even when the words are different. Keyword search finds exact matches even when they're not semantically prominent. Together, they're stronger. The code runs both retrievers, collects the union of results, deduplicates by ticket ID, and the documents found by both are likely the most relevant — they passed both the semantic and the keyword filter. More sophisticated fusion uses Reciprocal Rank Fusion, or RRF, which scores each document based on its rank position in each retriever's results. That's the production standard.

The summary table at the end of the demo tells you when to use each: Vector Index for general semantic search, fast and accurate. Summary Index for high-level queries on small collections. Tree Index for large, hierarchically structured document sets. Keyword Index for exact term matching. Hybrid for production — highest accuracy, slightly slower.

My recommendation: start with Vector Index. It handles ninety percent of use cases. Add Keyword Index for specific terminology. Use Hybrid for production. Avoid Summary Index unless your collection is genuinely small.

*[Run the demo, walk through the output]*

---

## SLIDE 52 — Q&A

Excellent. That was all three modules. Questions on indexing specifically, or anything we've covered today? This is your chance to ask about anything — the concepts, the code, how this maps to something you're working on, anything. Please post in chat as well. If a question gets missed, repost it.

---

## SLIDE 53 — Retrieval in One Picture

Before we go to the summary, I want to show you the complete retrieval loop in a single diagram. This is the core sequence for any RAG system. Step one: user sends a question to the retriever. Step two: the retriever calls `similarity_search()` on the vector database with the query embedding and a value of k. Step three: the vector database returns candidate chunks with their metadata. Step four: those candidates get passed to a reranker, which scores them more precisely and reorders them. Step five: the top-n reranked chunks come back. Step six: the retriever bundles those chunks with the question into a prompt and sends it to the LLM. Step seven: the LLM returns an answer with citations. That's the full loop. Everything we've built today — embeddings, chunking, indexing — is in service of making steps two through five work as well as possible.

---

## SLIDE 54 — Week 2 Summary

Let's recap what we covered today.

---

## SLIDE 55 — Week 2 Summary Diagram

Three modules. Module 1, Embeddings and Similarity: text gets converted into a 1536-dimensional vector by OpenAI's embedding model. Cosine similarity is your distance metric — range minus one to one. Semantic search means "reset" finds "forgot" because they mean the same thing in context. Module 2, Chunking and Vector Stores: recursive chunking is your default choice. Semantic chunking gives you higher quality if you can afford the cost. Chroma DB is your vector store with metadata filtering. Similarity search plus MMR gives you relevant and diverse results. Module 3, Indexing Strategies: Vector Index for fast, semantic search. Keyword Index for exact match. Tree Index for hierarchical retrieval on large collections. Hybrid is best for production.

The key takeaways: embeddings equal semantic meaning. Recursive chunking is your default starting point. Hybrid retrieval is your production target. Always measure retrieval quality — we'll get into evaluation in Week 3.

---

## SLIDE 56 — Glimpse of Week 3

Let's preview what's coming up next week.

---

## SLIDE 57 — Week 3: Putting It All Together

Week 3 is where everything connects. We'll build the end-to-end RAG flow: from user question, to retrieving the right context, to generating a grounded answer, to returning it with source citations. We'll add quality checking: are we retrieving the right information? Are the answers accurate? We'll cover evaluation methods for both retrieval and generation. And we'll tackle complex query handling — multi-step questions that require breaking the query apart, retrieving information from multiple places, and combining the results. This is where RAG becomes truly intelligent. Everything we built today is the foundation. Week 3 builds on top of it.

---

## SLIDE 58 — Thank You

That's a wrap for Week 2. Thank you all for being here, for asking questions, and for running the code. You now understand embeddings, chunking, and indexing — the three pillars of the RAG retrieval layer. Your assignment this week is to run all three demos, complete the exercises in each module, and try at least one modification: change the chunk size, try a different query, add a metadata filter. The solutions are in the repo if you get stuck, but try it yourself first. See you next Sunday for Week 3. Have a great week.

---

*End of Script*