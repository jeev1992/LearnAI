# Talking Script — Mastering AI System Design with GenAI & RAG

---

## SLIDE 1 — Title

[IK presenter opens the session — welcomes the audience and introduces today's masterclass: "Mastering AI System Design with GenAI & RAG — Build scalable Retrieval-Augmented pipelines with prompt orchestration and guardrails."]

---

## SLIDE 2 — Agenda

Here's the agenda for the next hour. We'll start with a quick intro to IK and your host. Then we'll spend most of our time on the actual craft: how to think about building ML/AI systems, how to frame a problem statement, how to scope it, how to identify the right components — LLM, RAG, vector store, embeddings — then operations or LLMOps, and finally privacy, security, and compliance. After that, a short section on how IK can help you uplevel into AI, and we'll close with Q&A.

---

## SLIDE 3 — About IK / Your Host

A quick word about Interview Kickstart. Ten-plus years in this space. Over 27,000 enrolments. More than a thousand alumni at Tier-1 companies. We focus on outcomes — domain-specific curriculum across 24 tracks, with student compensation ranging from 63 lakhs to 2 crore, and top student comp at 2 crore. Behind the curriculum: 700-plus FAANG+ instructors, 70-plus dedicated AI/ML instructors, and an average of 13 years of experience per instructor. IK has been recognized by Time magazine and GSV in their global EdTech lists for 2025.

[SPEAKER NOTE: IK's site says "enrolments" and "alumni," not "placements" — and "instructors," not "hiring managers." Frame it honestly.]

---

## SLIDE 4 — IK Instructors

These are the people behind the curriculum — AI/ML engineers, hiring managers, and technical recruiters from FAANG+ and Tier-1 companies. Names you'll recognize: Omkar Deshpande from Interview Kickstart, plus instructors from Meta, Walmart, Amazon, Microsoft, Google, Disney, Indeed, Airbnb, Box, and Uber. The point isn't the logos — the point is that the curriculum is designed and delivered by practitioners who've actually shipped this stuff at scale.

---

## SLIDE 5 — Introduction: Jeevendra Singh

Hi everyone, my name is Jeevendra Singh. I'm a Software Engineer at Microsoft, with about 11 years of experience in the industry. Over those years I've worked across the stack — building distributed systems, shipping products, and more recently spending a lot of time in the AI and agentic tooling space, which is exactly what brought me to today's session.

At Microsoft I've developed and deployed several agents to production. And if you've tried taking an agent from a prototype to a real production deployment, you know that building the agent is only half the battle. The harder half is everything that comes after — passing compliance reviews like Responsible AI, running rigorous evaluations to make sure the system behaves correctly across edge cases, and meeting the bar your organization sets before anything goes live. A huge part of that work — for any GenAI system, agentic or not — is exactly what we're covering today: the RAG pipeline, the prompt design, the operations layer, and the safety guardrails. Those design decisions aren't academic. They're the same ones you face when you're trying to get a GenAI feature past compliance and into the hands of real users.

I put this session together because I see the same pattern over and over with engineers entering the GenAI space — they jump straight to picking a model or wiring up a framework, and skip the part that actually decides whether the system works in production. That's the part we're going to cover today. Not "here's how to call the OpenAI API," but "here's how you'd architect a real GenAI system from scratch, end to end, with all the pieces that have to fit together." So with that, let's jump in.

---

## SLIDE 6 — Agenda (repeat)

Quick recap of where we're going so the structure is clear in your head. Intro, then notes on building ML/AI systems, then problem statement, scope, key components, operations, privacy, the IK pitch, and Q&A. We'll keep coming back to this agenda as we move between sections.

---

## SLIDE 7 — Disclaimers

One disclaimer before we go further. The focus today is on building an **end-to-end AI/ML system** — not on building the ML model itself, and not just on model quality. There are great courses on training models, on transformer internals, on RLHF. This isn't one of them. Today is about everything around the model — the data pipeline, the retrieval layer, the prompt, the tools, the operations, the safety — because in a real product, that's where most of the engineering effort actually goes.

---

## SLIDE 8 — Goals / Non-Goals / Scope

Let me set expectations.

The **goal** is to give you a general framework for scoping and approaching AI/ML projects. A repeatable mental model — so the next time someone hands you "build us a GenAI feature," you have a structured way to attack it. Now, the details will vary from one project to another — your domain, your data, your constraints will all be different — but the framework is the same.

The **non-goals** are deep dives into specific ML models, and focusing on a single project. We'll use one project as a running example throughout the session, but the example is just a vehicle for the framework — it's not the destination.

---

## SLIDE 9 — Notes on Building ML/AI Systems

If you take one thing away from this entire session, take this: **Do NOT jump to the ML modeling right away.**

This is the single most common mistake I see. Someone is told "build an AI feature," and the first thing they do is open a notebook and start picking a model. That's backwards. The model is a tool. You have to know what you're building first.

---

## SLIDE 10 — Notes on Building ML/AI Systems (cont.)

So before the model — **think first about the business or engineering problem you're solving.** What is the user actually trying to accomplish? What does success look like for them, in plain English, before you've written a single line of code?

---

## SLIDE 11 — Notes on Building ML/AI Systems (cont.)

Once you understand the problem — then ask **how ML or AI can help.** Sometimes the honest answer is "it can't" — a SQL query or a rules engine is enough. Sometimes ML helps but a small classical model is the right call. Sometimes you genuinely need a large language model. Knowing which it is starts with the problem, not the technology.

---

## SLIDE 12 — Notes on Building ML/AI Systems (cont.)

And only after those two questions — what's the problem, and how does AI help — can you **set up the right ML problem.** Is it classification, retrieval, generation, ranking? What are the inputs and outputs? What does ground truth look like? You can't answer any of those well until you've done the first two steps. That's the discipline.

---

## SLIDE 13 — What Are the New Concepts

Now, since we're focused on GenAI today, there are three concepts that will show up over and over, and I want to name them up front so they don't slow us down later.

First, **Retrieval Augmented Generation**, or RAG — giving the model relevant information at inference time instead of trying to bake it into the model's weights. We'll spend a lot of time here.

Second, **prompt technique** — the structured way you actually phrase what you send to the model. Prompting is part of the system; it's not a soft skill.

Third, **tool call** — letting the model invoke external functions, like searching a database or calling an API, instead of trying to do everything from its own internal knowledge. That's how you get an agent instead of a chatbot.

Those three ideas are the backbone of what we're building today.

---

## SLIDE 14 — Agenda (Problem Statement)

Now into the part where we actually design something. Problem statement first.

---

## SLIDE 15 — Problem Statement

Here's the problem we'll use as our running example for the rest of the session. Read it with me: **"Design a system that generates personalized health and wellness articles for users in real time using GenAI."**

It looks like one sentence. It's actually packed with decisions. "Personalized" — personalized on what? "Health and wellness" — that's a regulated domain. "Real time" — that's a latency constraint. "Articles" — that's a long-form generation task, not a short answer. Every word is a design lever. We're going to pull each one and see what it forces in the architecture.

---

## SLIDE 16 — Agenda (Scope)

Before we draw any diagrams, we have to scope the problem.

---

## SLIDE 17 — Scope of Problem

The first thing you should do is **work with the product team to better understand the problem.** A system design exercise is not a solo activity. The PM, the designer, the domain experts — they hold context you don't have. You're going to walk into that conversation with structured questions.

---

## SLIDE 18 — Scope of Problem (cont.)

Question one: **What's the input?** What does the system receive every time it runs? This sounds basic, but I've seen entire designs derailed because nobody agreed on what was coming in.

---

## SLIDE 19 — Scope of Problem (cont.)

For our health article problem, the inputs are three things. **The user's profile or preferences** — age, conditions, what they care about. **The user's question** — what they actually want to know right now. And **a collection of health articles** — the source material the system can pull from. Notice that the third one isn't really an "input" per call; it's a corpus the system has access to. Both kinds of input matter, and you need to be explicit about which is which.

---

## SLIDE 20 — Scope of Problem (cont.)

Question two: **What's the output?** Just as important. Is it a paragraph? A bullet list? A full article? JSON? Each of those is a different system.

---

## SLIDE 21 — Scope of Problem (cont.)

For us, the output is a **personalized, medically reliable article.** Two adjectives doing a lot of work. "Personalized" means we're conditioning on the user's profile. "Medically reliable" means we cannot make things up — which immediately tells us we'll need retrieval grounding and probably a safety review layer. Already, the output spec is constraining the architecture.

---

## SLIDE 22 — Scope of Problem (cont.)

Question three: **What are the constraints?** These are the non-functional requirements — latency, cost, throughput, accuracy, compliance. Constraints are where designs live or die.

---

## SLIDE 23 — Scope of Problem (cont.)

For our system, we have two big ones. **Reasonable latency** — let's say on the order of a few hundred milliseconds for first response, with the full article streaming after. Real time means the user can't be waiting on a spinner for 30 seconds. And second, **answers have to be factually correct.** That's not a "nice to have" — for health content, a hallucination isn't just wrong, it can be harmful. That single constraint is going to drive every choice we make about retrieval, grounding, and evaluation.

So now we have inputs, outputs, and constraints. We can actually design.

---

## SLIDE 24 — Agenda (Identify Key Components)

Now, with the problem scoped, let's identify the components.

---

## SLIDE 25 — Identify Key Components

**What are the main components in the system?** Don't draw boxes yet. List the capabilities first. We'll group them into components in a minute.

---

## SLIDE 26 — Identify Key Components

The most obvious one — **LLM**. We need a model that can generate text. That's the engine.

---

## SLIDE 27 — Identify Key Components

Now the real question: **Can we use the LLM alone?** Just hand the user's question to GPT or Claude and stream back an answer. Done. Right?

---

## SLIDE 28 — Identify Key Components

**No.** And it's important to understand why, because every component we add after this exists to fix a specific limitation of using the model alone.

---

## SLIDE 29 — Identify Key Components

**Why not?** Let's make it concrete.

---

## SLIDE 30 — Identify Key Components

Imagine a user asks: **"I took my blood pressure and it was 145/90. Is that bad?"** A raw LLM will give you an answer — but that answer is based on whatever was in its training data, which could be two years old. It doesn't know your specific health guidelines. It doesn't know what your medical team considers normal for you. It might hallucinate a threshold or cite a study that doesn't exist. For a wellness chatbot, that's a problem. For a health system, that's a liability. So the LLM alone is not enough. We need to ground it in trusted data.

---

## SLIDE 31 — Option: Fine-Tuning

One way to get the model to know your domain is **fine-tuning.** You take a pre-trained off-the-shelf LLM, you feed it a dataset of your domain, and out comes a customized model that "knows" your content.

---

## SLIDE 32 — Option: Fine-Tuning (cont.)

Sounds great. Two problems. **You need a labeled dataset for every task.** That's expensive — both in money and in engineering time. And **you have to re-tune the model every time** your content changes, or your guidelines change, or a new article gets published. In a domain like health, where guidelines update constantly, fine-tuning becomes a treadmill you never get off.

---

## SLIDE 33 — LLM vs Fine-Tuning

Let's compare side by side. **Off-the-shelf LLM** — can't add domain-specific data, but easy to set up and use. **Fine-tuning** — can add domain-specific data, but it is NOT an easy setup. You're picking between freshness and capability on one side, and operational simplicity on the other. Neither is satisfying.

---

## SLIDE 34 — LLM vs Fine-Tuning (the third option)

So is there a third path? Yes. **What if we provide the model with the additional data at inference time?** Instead of baking knowledge into the weights, we hand the model the relevant facts in the prompt, right when it needs them. The model stays generic. The data stays fresh. We get the best of both columns. That's the entire idea behind RAG.

---

## SLIDE 35 — Retrieval Augmented Generation (RAG)

So let's introduce **Retrieval Augmented Generation** — RAG. This is the architectural pattern that has effectively become the default for any LLM application that needs to reason over private or up-to-date content.

---

## SLIDE 36 — RAG Diagram

Here's the loop. User asks **"Is my blood pressure high?"** That question goes to a retrieval step that pulls **relevant information and instructions on how to use them** from our dataset. The retrieved chunks plus the original question get handed to the **pre-trained LLM**, which generates a grounded answer — **"High blood pressure is…"** — using the facts we just gave it. The model never had to be trained on our content. The content lives outside the model, and we inject what's relevant per query.

---

## SLIDE 37 — RAG Diagram (cont.)

Let's walk this picture quickly.

The user asks **"Is my blood pressure high?"** That question does two things at once — it goes to the **Data Set** to look up relevant content, and it also goes to the **LLM** so the model knows what's being asked.

From the Data Set, we pull out the **relevant information** — a passage about hypertension — and hand it to the LLM along with the question. The LLM reads both and produces the answer: **"High blood pressure is…"**

The key point: **the model itself is unchanged.** It's the same off-the-shelf LLM. All the customization happens around it — in the retrieval and the prompt. That's RAG.

Now we'll **zoom in on each component** — the vector store, the embeddings, the prompt — because each one has design decisions that matter.

---

## SLIDE 38 — RAG Architecture (numbered flow)

Now let's look at the same RAG idea, but with the actual components a real system would have, and numbered steps so we can follow the flow.

**Step 1** — the **user** sends a **query** to the **chat app**. That's the entry point — could be a web UI, a mobile app, anything the user types into.

**Step 2** — the chat app forwards the **query to the vector store** to find relevant documents.

Quick pause here, because two words on this slide need to be unpacked: **vector store** and how it actually finds the right docs.

A **vector store** is just a special kind of database — but instead of storing rows of text and searching by keyword, it stores each document as a list of numbers called a **vector**, and searches by **meaning**. That's called **semantic search** — search by meaning, not by exact words.

Why does that matter? Imagine the user asks **"my heart rate is high after walking up stairs"** and your document says **"elevated pulse during light exertion."** No words overlap. A keyword search returns nothing. A semantic search understands that "heart rate" and "pulse" mean the same thing, that "high" and "elevated" mean the same thing, that "walking up stairs" and "light exertion" describe the same situation — and it returns the right document. That's the whole point of using a vector store instead of a regular one. We'll go deeper into how embeddings make this work in a few slides.

Now, on the right side of the diagram: the vector store was filled ahead of time by **ingesting documents** offline. We take our entire knowledge base, convert each document into vectors, and load them in. That's a batch job — it runs once when we set up the system, and again whenever the documents change.

**Step 3** — the vector store returns the **relevant docs** — the ones whose meaning is closest to the user's question. The chat app combines those docs with the original query to build an **augmented prompt**, and sends it to the **LLM**. "Augmented" just means "the original query plus the retrieved context."

**Step 4** — the LLM reads the augmented prompt and generates a **response**, grounded in the docs we provided.

**Step 5** — the chat app forwards the **response back to the user**.

Five steps. That's the whole loop.

---

## SLIDE 39 — RAG Architecture (Augmented Prompt)

Same diagram — but notice what's highlighted now: the **Augmented Prompt**. This is the heart of RAG, so let me make it really clear by contrasting it with a normal prompt.

A **normal prompt** is just the user's question, handed straight to the LLM:

> *"Is my blood pressure high?"*

That's it. The model has to answer from whatever it remembers from training. Could be right, could be wrong, could be made up.

An **augmented prompt** is the user's question **plus the relevant context** retrieved from the vector store, both packaged together:

> *"Use the following context to answer the question.*
> *Context: [retrieved medical article about blood pressure thresholds]*
> *Question: Is my blood pressure high?"*

Same question, completely different behavior. Now the model isn't guessing — it's reading the docs we handed it and answering based on those.

That's the whole difference. **Normal prompt = question only.** **Augmented prompt = question + retrieved context.** And that one change is what turns a regular LLM call into a RAG system. The next slide shows you exactly what an augmented prompt looks like in real text.

---

## SLIDE 40 — What Is in the Prompt?

Let's make the "prompt" concrete, because it's where a lot of the magic — and a lot of the bugs — actually live. Here's what we'd send to the model:

> *Answer the following question based only on the provided context:*
> *<context> High blood pressure, also known as hypertension, is often called a 'silent killer' because it typically has no obvious symptoms…* *</context>*
> *Question: What are the symptoms for high blood pressure?*

Three parts. An **instruction** that tells the model to answer **only from the provided context** — not from its own knowledge. The **context** itself — the retrieved passage. And the **question.** The instruction is doing critical safety work — it's the line of defense against the model making something up. If you drop that instruction, you've technically still got RAG, but you've lost the grounding guarantee. The prompt template is part of your architecture.

---

## SLIDE 41 — RAG Architecture (Vector Store + Documents)

Same diagram — now the **vector store and documents** are highlighted. This is the part that has to be ready **before any user shows up**.

Think of it like a regular database. Before a user can read data, somebody has to load it in first. That loading happens in advance, in batch — we call that **offline work**. The user's actual query is **online** — it happens live, and the user is waiting.

RAG works the same way. The vector store is empty when you first set it up. You can't query something that's empty. So you have to **ingest the documents first** — and that's what the arrow on the right is showing.

Ingest isn't just a copy-paste. For each document, you do three things:

1. **Chunk it** — split the document into smaller passages. A 50-page PDF becomes maybe 200 chunks.
2. **Embed each chunk** — turn it into a vector, so it can be searched by meaning later.
3. **Store the chunk and its vector** in the vector store.

You do this once, ahead of time, for every document in your knowledge base. When a user finally asks a question, the vector store is ready to answer immediately.

And here's why this side of the diagram matters so much: **the LLM can only use what's in the vector store.** If a document isn't ingested, it doesn't exist as far as the system is concerned. If it's chunked badly, retrieval returns the wrong piece. If the data is stale, the answers are stale. Get the offline side right, or nothing downstream can save you.

---

## SLIDE 42 — Vector Store

**We need to store the data such that…** what? What are the actual requirements on the storage layer?

---

## SLIDE 43 — Vector Store (cont.)

Two non-negotiables. **Retrieval has to be based on semantics, not word-for-word match.** If the user asks about "cars" and your document says "vehicles," you still want that document to come back. Lexical search misses this; semantic search catches it. And second, **retrieval cannot be slow.** This sits in your online path — every millisecond here is a millisecond the user is waiting.

---

## SLIDE 44 — Vector Store (cont.)

So the question becomes — **how do we actually store text in a way that makes semantic search both possible and fast?** Plain text in a database with a LIKE query gives you neither. We need a different representation. That's where embeddings come in.

---

## SLIDE 45 — What Is Embedding

So how do we actually search by meaning? The answer is **embeddings**.

An **embedding is just a list of numbers that represents a piece of text.** You take a sentence — say, **"My blood pressure is high"** — feed it into an embedding model, and out comes something like `[0.21, -0.45, 0.88, …, 0.13]`. Usually a few hundred to a few thousand numbers long. That list of numbers is called a **vector**, and you can think of it as the **coordinates of that sentence in some high-dimensional space.**

Here's the magic property — and this is the only thing you really need to remember: **sentences that mean similar things end up with similar vectors.** So "my blood pressure is high" and "I have hypertension" land near each other in that space. "My blood pressure is high" and "I want to buy a car" land far apart.

Once your text is in this space, **searching by meaning becomes a math problem** — you just find the vectors closest to the query's vector. And finding nearest neighbors in a vector space is something computers can do fast, even across millions of documents.

That's the whole trick behind semantic search. Convert text to vectors, then do geometry instead of word matching.

---

## SLIDE 46 — How to Store Text?

So our **requirements** for the storage layer are:

---

## SLIDE 47 — How to Store Text? (cont.)

**Store text. Search text — based on meaning.** Two simple-looking lines, but the second one is what forces us into a vector database instead of a regular one.

---

## SLIDE 48 — How to Store Text? (cont.)

Let's make this concrete. Suppose the user types **"My bill is 50 dollars instead of 30 dollars"** into a support system. The user is clearly complaining about an unexpected charge.

Now look at the articles sitting in our knowledge base: **"New 50-dollar plan," "Unexpected high fees," "30 days free plan."**

If we used a plain **keyword search** — the kind a regular database does — what would it match on? It would latch onto the numbers "50" and "30," and probably surface **"New 50-dollar plan"** or **"30 days free plan"** at the top. Both of those are completely irrelevant to what the user is asking. Keyword matching has no idea what the user actually means.

---

## SLIDE 49 — How to Store Text? (cont.)

Now look at the same picture — but this time **"Unexpected high fees"** is highlighted. That's the article a **semantic search** would return.

Why? Because semantic search compares the **meaning** of the user's message — "I'm being charged more than I expected" — against the meaning of each article. "Unexpected high fees" lines up perfectly with that complaint, even though the words "bill," "50," and "30" never appear in its title.

That's the difference in one slide. **Keyword search matches words. Semantic search matches meaning.** The user wins, because the user wasn't searching for "50" or "30" — they were searching for "why is my charge wrong?"

This is the entire reason we need a vector store instead of a regular database. Now let's see how embeddings actually make this work, mechanically.

---

## SLIDE 50 — Embedding

Mechanically, here's what happens. You take a piece of text — **"My blood pressure is…"** — and pass it through an **embedding model**, which outputs a vector like [0.3, -0.1, …, 0.8, 0.1]. That vector lives in a high-dimensional space. Every chunk in your knowledge base gets the same treatment, ahead of time.

---

## SLIDE 51 — Embedding (multiple chunks)

Now you do this for every passage in your corpus. The chunk about **"people who took a blood pressure reading of 145/90 often forget to log results"** gets its own vector. The chunk about **"persistent hypertensive readings exceeding stage two benchmarks elevate cardiovascular risk"** gets another vector. All these vectors get stored — in a vector store — alongside their source text.

---

## SLIDE 52 — Embedding (comparison)

Now the interesting step — **comparison.**

When a user query comes in — at the top of the diagram — we run it through the **same embedding model** that we used for our stored chunks, and we get a vector for the query. So now we have one vector for the question, and many vectors already sitting in the store for our knowledge base chunks.

How do we find the right chunk? We **compare the query vector against every stored vector** and ask one question: **how close are they?**

Remember, each vector is just a point in a high-dimensional space. Vectors that point in similar directions represent similar meanings. So "closeness" here is literally a geometric measurement — under the hood it's usually cosine similarity, but you don't need to memorize that. The intuition is enough: **closer vectors mean closer meaning.**

We rank all the chunks by closeness and return the top few — say, the top 3 or top 5. Those are the chunks that get handed to the LLM as context. That's the entire retrieval step in one operation: **embed the query, compare to everything, return the nearest matches.**

---

## SLIDE 53 — Embedding (retrieval)

Same diagram one more time — but now you've seen every piece, so let's zoom out and lock in the full mental model. This is the heartbeat of RAG, and if you remember nothing else from this section, remember this:

**Offline, once per document:**
- Take each chunk → run it through the embedding model → store the vector.

**Online, once per user query:**
- Take the query → run it through the **same** embedding model → compare against all stored vectors → return the top matches.

That's it. Two passes through the same embedding model, one comparison step, and the right chunks come back. No keyword matching, no manual tagging, no rules. The embedding model does the heavy lifting of converting language into geometry — and once you're in geometry, finding similar things is just math.

This pattern is what makes RAG work at scale. You can have a million documents in the store, and a query still comes back in milliseconds. Now let's look at the vector store itself from a system perspective — what these two paths look like as actual infrastructure.

---

## SLIDE 54 — Vector Store (online / offline split)

Now let's look at the vector store at a system level. The diagram has a vertical line down the middle — **Offline on the left, Online on the right** — because the vector store really does live a double life. Same database, two completely different access patterns. Let's walk both sides.

**Offline side — left:**
- You start with your raw **documents**.
- You feed them through an **embedding model**. The little logos under the model — Cohere, OpenAI, Hugging Face, and others — are reminders that you don't build this yourself. You pick a provider, hit their API, and you get back vectors.
- Out come **vector embeddings** — lists of numbers, one per chunk, like `[0.5, 0.8, -0.3, 0.2]`.
- Those vectors get written into the **vector database**.

This is the batch job. It can be slow, it can run overnight, nobody cares — there's no user waiting.

**Online side — right:**
- A user submits a **query**.
- The query goes through the **same embedding model** you used offline. This is critical — if you embed your documents with one model and your queries with a different one, the vectors don't live in the same space and the comparison is meaningless. **Same model, both sides.**
- You get back a query vector — something like `[-0.9, -0.7, -1.0, -0.8]`.
- That query vector goes into the vector database, which runs a **KNN search** — **k-Nearest Neighbors**. That's just the formal name for "find the k vectors closest to this one." Pick k=3 or k=5, depending on how much context you want.
- Out come the **query results** — the top matching chunks, ready to be packed into the augmented prompt and sent to the LLM.

So the vector database is the shared piece in the middle. The offline side **fills it**. The online side **queries it**. And the embedding model bridges both sides — that's why it appears twice in the picture.

---

## SLIDE 55 — Vector Store (output type)

A subtle but important question: **what is the type of the output from the vector store?** When the online query hits the store, what comes back?

---

## SLIDE 56 — Vector Store (output type)

It **returns text, not embeddings.** The vector is the *index key* — it's how we found the right chunk. But what we hand to the LLM is the original text. People get this wrong all the time — they retrieve vectors and try to do something clever with them. You don't. You retrieve text, you put text in the prompt, the LLM consumes text. The vector is plumbing; it never reaches the model.

---

## SLIDE 57 — RAG Architecture (recap)

One more look at the full diagram, now that you've seen all the pieces. Offline: documents → chunks → embeddings → vector store. Online: question → embedding → similarity search → top-k chunks → prompt → LLM → answer. You can draw this on a whiteboard from memory now. Good. Let's add the next layer: tools.

---

## SLIDE 58 — Agent with Tools

So far, our system can answer questions over a static corpus. But real applications need to do more than read a knowledge base. They need to **look something up in a live database**, **call an internal API**, **trigger a workflow**, **check a user's account status.** That's where **agents with tools** come in. Here's the picture: a **question** arrives at the **server backend**, which talks to the **LLM**, which has access to **tools**. The tools are external capabilities the model can ask the backend to invoke.

---

## SLIDE 59 — Agent with Tools (step 1)

**Step 1 — the question** arrives at the backend. The backend doesn't try to answer it. It forwards the question, along with the list of available tools, to the LLM. The model is in charge of deciding what to do next.

---

## SLIDE 60 — Agent with Tools (step 2)

**Step 2 — the LLM decides it needs more information** and responds with a tool call — "query external source" — telling the backend exactly which tool to call and with what arguments. The model itself doesn't reach out to anything. It just describes the call it wants made.

---

## SLIDE 61 — Agent with Tools (step 3)

**Step 3** — the backend executes the tool. It actually makes the API call, hits the database, runs the query. The result comes back to the backend.

---

## SLIDE 62 — Agent with Tools (step 4)

**Step 4** — the backend forwards the tool result back to the LLM. Now the model has new information it didn't have before — the live data it asked for.

---

## SLIDE 63 — Agent with Tools (step 5)

**Step 5 — the LLM forwards a response** back to the backend, which forwards it to the user. The model has reasoned over the new data and produced the final answer.

---

## SLIDE 64 — Agent with Tools (full loop)

Step back and look at the whole cycle. The model **reasons**; the backend **acts**. The model never touches the database, never makes an HTTP call, never executes code. It just describes the actions it wants taken, and the backend carries them out. That separation is what makes this safe and debuggable — every action is mediated by code you control.

---

## SLIDE 65 — ReAct: How the Model Drives the Loop

So how does the model actually "decide" to call a tool? It's not magic — it's a prompting pattern called **ReAct: Reason + Act.** This slide shows what such a prompt looks like.

The instruction at the top sets the rules: *"Solve a question answering task with interleaving Thought, Action, Observation steps."* In plain English — don't just answer; work in a cycle. **Think, act, observe. Repeat.**

Then we hand the model a menu of allowed actions — **Search**, **Lookup**, **Finish**. That's its entire toolbox.

Given this prompt, the model produces output like:
> *Thought: I need to know when X was founded.*
> *Action: Search[X]*
> *Observation: X was founded in 1998.*
> *Action: Finish[1998]*

Now the most important point on this slide, and the one most people miss: **the LLM is just a reasoning engine. It only generates text.** When it writes *"Action: Search[X]"*, it's not actually searching anything. It can't. It has no internet, no database, no ability to execute code. All it does is output a string that *describes* the action.

**The agent — the code around the model — is what actually runs the tool.** It reads the model's text, sees "Search[X]," runs the real search, and feeds the result back as the next Observation.

So the split is sharp: **LLM reasons in text. Agent acts in code.** That separation is the whole reason agentic systems are safe and debuggable — every real-world action goes through code you control.

ReAct is the pattern underneath Claude Code, LangChain, CrewAI, MCP — all of them. Once you spot it, you'll see it everywhere.

---

## SLIDE 66 — Agent with Tools (repeat)

And here's the key point: **this loop repeats.** The model might need to call one tool, see the result, decide it needs another tool, call that, see the next result, and only then produce a final answer. So step 1 through step 5 isn't a single round trip — it's a cycle that runs until the model says "I'm done." That's what makes it an **agent** instead of a chatbot. The model is in a loop, not a single turn.

So now you have the full architecture: RAG for grounding in static knowledge, plus tool-calling for reaching out to live systems. Most production GenAI applications are some combination of these two.

---

## SLIDE 67 — Agenda (Operations)

We've designed the system. We're not done. Designing it is maybe half the work. Operating it in production is the other half.

---

## SLIDE 68 — Operations

After the system has been launched, **your job is not done.** This is the part people new to ML systems miss. A regular software service, you ship it, you monitor for crashes, you patch when something breaks. An ML system, you ship it, and then it starts drifting — the data changes, the model changes, user behavior changes — and you need a discipline for keeping it healthy. **You may need to…**

---

## SLIDE 69 — Operations (cont.)

**Update the model.** A new version of the underlying LLM gets released. Maybe you're getting better latency, better quality, lower cost. You want to upgrade.

**Update the prompt.** You discover the model is misbehaving on a certain class of questions, or product wants to change the tone, or you need to add a new safety instruction. The prompt changes.

---

## SLIDE 70 — Operations (cont.)

And here's the catch: **these have to be consistent.** A model upgrade can change how the model interprets your prompt. A prompt change can interact with retrieval in unexpected ways. You cannot ship a new model and an unchanged prompt and assume the system still works. They're coupled.

---

## SLIDE 71 — Versioning

**Think of these as a bundle** — the model version, the prompt template, the retrieval configuration, the tool set. They travel together.

---

## SLIDE 72 — Versioning (cont.)

**That has to be versioned.** Just like you version your code, you version your model-plus-prompt-plus-config bundle. Every deployment to production is a specific version of that bundle. When something breaks in production, the first question is "which version is running, and what changed?" — and you can only answer that if you've been versioning all along.

---

## SLIDE 73 — Is the System Good Enough?

The other half of operations is **evaluation** — is the system actually good enough? You need an evaluation framework, and it's **useful at two moments.** First, **at initial launch** — to decide whether you should go live at all. Second, **at every model or prompt update** — to decide whether the new version is better, worse, or the same as what's in production.

---

## SLIDE 74 — Is the System Good Enough? (cont.)

Evaluation gives you a snapshot. But production is continuous. So you also need **monitoring** — running in the background, watching real traffic. **What metrics do we need to track?**

---

## SLIDE 75 — Is the System Good Enough? (cont.)

Three to start with. **Number of active users** — basic adoption signal. **Number of turns** — are users having productive multi-turn conversations, or are they bouncing after one bad answer? And **containment rate** — the ratio of calls that did NOT need a human escalation. For an assistant or support agent, containment is one of the cleanest signals of real-world usefulness. If containment is going down over time, something is regressing, and you want to know before the user complaints start rolling in.

These aren't the only metrics, but they're the right starting set. Latency, cost per call, hallucination rate, user satisfaction scores — they all belong in the dashboard too. The point is: monitoring is not optional, and it has to be designed in from day one, not bolted on after launch.

---

## SLIDE 76 — Agenda (Privacy)

Last design topic before we wrap. Privacy, security, and compliance.

---

## SLIDE 77 — Privacy, Security & Compliance

This matters for every domain, but it matters **more for the health domain** — and for anything regulated. Three principles, at minimum.

**Users' data should not be used for training unless they consent.** This is both a legal requirement in many jurisdictions and a basic trust requirement everywhere. If your provider's terms of service say your prompts may be used for training, you need to disable that pathway for sensitive content, or use a deployment tier that guarantees no training.

**Models have to give factually correct answers.** This is where RAG, grounding, and evaluation come back together. In a health context, "the model usually gets it right" is not a passing grade. You need explicit citations, source linking, and an escalation path when confidence is low.

**No biases.** Models inherit bias from their training data, and bias in health, finance, or hiring can do real harm. You need bias evaluation as a first-class part of your testing pipeline, with explicit slices across the demographics that matter for your use case.

These three aren't a checklist you do once. They're properties you have to keep proving, every time the bundle changes.

---

## SLIDE 78 — Summary

Let me tie the whole session together in five points.

**One — it's about building an end-to-end system, not just a model.** The model is a component. The system is what ships.

**Two — as an ML engineer, your job does not stop once you've deployed.** You have to monitor the system continuously, because data, models, and users all drift.

**Three — GenAI design has four pillars:** **data sources** — where does grounded knowledge come from; **data flow** — how does data move through ingest, retrieval, and prompt assembly; **operations** — how do you version, evaluate, and monitor; and **safety and security** — how do you protect users and their data.

If you walked in today not knowing how to attack a GenAI system design problem, walk out using these four pillars as your checklist. Every interview question, every real project — start there.

---

## SLIDE 79 — Agenda (10x Professional)

Quick transition into how IK can help you actually build these skills, and then we'll open up Q&A.

---

## SLIDE 80 — Transforming Talent

IK focuses on two parallel tracks: **interview prep upleveling** for engineers preparing for FAANG and tier-one interviews, and **AI upleveling** for engineers who want to add or deepen AI/ML skills. Same platform, two journeys.

---

## SLIDE 81 — AI/ML/Data Job Growth

The macro picture. **AI/ML/data job openings on LinkedIn are up between 35 and 80 percent in 2024.** ML, AI, and data scientist roles are up about 4.7x. Data engineering is up about 2.5x. And the projection is that AI, ML, DS, and DE roles continue to rise through 2028. If you're an engineer thinking about where to invest your learning budget over the next two years, the answer is obvious.

---

## SLIDE 82 — Compensation Gap

And it's not just volume — it's compensation. There's a **significant gap between traditional SWE ladders and AI/ML ladders.** At the early SWE 1 level the gap is maybe a lakh. By the time you get to senior staff and principal levels, the gap can be 35 lakhs or more. **AI/ML expertise puts you in the top earning bracket** — and that gap has been widening, not narrowing.

---

## SLIDE 83 — New AI Role Stack

A lot of you are software engineers right now, and the question is "what does my next role even look like in an AI-native world?" Four buckets are emerging. **Build autonomous AI agents and multi-agent systems.** **Develop multimodal AI applications.** **Deploy and scale AI models in cloud environments.** And **RAG, LLM orchestration, LangChain, LlamaIndex** — the agentic stack we've been talking about today. These are real job titles being posted right now.

---

## SLIDE 84 — Picking the Right Path

We get it — **it's challenging to pick the right path.** Different backgrounds, different goals, different time budgets. Let's walk through how IK organizes the choices.

---

## SLIDE 85 — Two Years In: No One Size Fits All

The honest framing: **two years into the AI shift, there is no one-size-fits-all path.** What you should do next genuinely depends on where you're starting from and where you want to land.

---

## SLIDE 86 — Three Learning Paths

So IK has three flagship learning paths.

**Transformative GenAI** — add AI skills to your current domain or tech stack. Best for engineers who want to stay in their current role but add GenAI capability.

**Flagship Machine Learning** — gain ML skills to fully pivot into AI-intensive roles. Best for engineers transitioning careers.

**Agentic AI Career Accelerator** — build enterprise-grade agentic AI systems. Best for engineers who want to specialize in the exact kind of system we designed today.

All three are paired with the **Interview Prep Lab**, which is widely used across Silicon Valley.

---

## SLIDE 87 — 18 Tracks

And inside those flagship paths, there are **18 different tracks** covering every major role — backend, frontend, full stack, mobile, test engineering, cloud, security, SRE, ML, data engineering, data science, engineering management, PM-T, and TPM. Not one curriculum forced on everyone — customizable pathways for every engineer, manager, and PM, with customizable timelines.

---

## SLIDE 88 — Transformative GenAI (curriculum)

Quick tour of the Transformative GenAI path — a **14-week program** for adding AI to your current SWE skill set. Four phases: **Python basics for AI** (NumPy, Pandas, scikit-learn, PyTorch); **building foundational AI agents** (LangChain, LangGraph, CrewAI); **building advanced AI agents** (multi-agent systems, RAG, vector DBs, fine-tuning, evaluation, cost optimization); and **domain-specific capstone projects** (your choice of real-world AI build).

---

## SLIDE 89 — Three Paths (recap)

Same three paths I mentioned — Transformative GenAI, Flagship ML, Agentic AI Career Accelerator — with the Interview Prep Lab on every one. Pick the one that matches your trajectory.

---

## SLIDE 90 — Flagship Machine Learning

For the deepest ML pivot, this is the **Flagship Machine Learning** program — **6 to 4 months** depending on pace. Month 1 is Python basics. Months 2–3 are ML engineering and case studies — data analysis, supervised and unsupervised methods, ensembles, deep learning, neural net architectures, transformers. Months 4–6 are GenAI, agentic AI, and a capstone project. Months 7–10 are interview prep tailored to your specialization — DS, MLE, DA, or BA. Optional add-ons in advanced NLP, advanced computer vision, MLOps, and big data with Apache Spark.

---

## SLIDE 91 — Flagship ML Capstones

The Flagship ML program is **project-centric** — you build a multi-project portfolio under MAANG mentors. Live coding workshops with instructors on real systems — SmartPrice AI mobile cost predictor, intelligent targeting for banking campaigns, image classification with neural architectures. Self-guided case studies on fraud detection and movie recommendation chatbots. And capstone projects across browser analytics, fraud shield, fashion image retrieval, and Medibot AI — an agentic bot that gives context-aware responses, which is almost exactly the system we designed today.

---

## SLIDE 92 — Three Paths (recap)

Three paths, one more time, for emphasis. Choose your trajectory.

---

## SLIDE 93 — Agentic AI Career Accelerator

For those of you specifically interested in agentic systems — what we built today — there's the **Agentic AI Career Accelerator**, a **12-week program** designed end to end around enterprise agent engineering. Weeks 1–4: agentic AI foundations, LLM tool use, MCP, ReAct, CrewAI, plus your first agent deployed on AWS. Weeks 5–6: enterprise capstone selection across healthcare, BFSI, e-commerce, or supply chain, plus multi-agent patterns. Weeks 7–9: enterprise agent engineering — advanced MCP pipelines, guardrails, LangSmith evaluation, domain deep dives, capstone build. Weeks 10–12: production, optimization, observability, and final portfolio packaging.

---

## SLIDE 94 — Agentic AI Capstones

The capstone choices map directly onto the high-value enterprise use cases hiring right now. **Healthcare Diagnostic Agent** — symptom analysis to recommendations. **BFSI Compliance Agent** — regulatory parsing and risk checks. **E-Commerce Intelligence Agent** — dynamic pricing and competitor tracking. **Supply Chain Optimizer Agent** — demand prediction and vendor coordination. Pick one, build it, deploy it, ship it as part of your portfolio.

---

## SLIDE 95 — Driving Acceleration

Beyond the curriculum, you also get the **Interview Prep Lab** infrastructure. **Mock interviews** — live sessions with Tier-1 experts, simulated interviews with hiring managers, detailed written and verbal feedback, check-ins to identify anti-patterns. **Placement assistance** — LinkedIn masterclasses, resume optimization, behavioral interview strategies, offer negotiation. The technical learning is necessary; this is what gets it converted into an offer.

---

## SLIDE 96 — Placement Assistance Stats

Some numbers on the placement side, performance-based: **199 hiring partners in India**, **450 profiles shared by hiring partners**, **87 percent of offers go to candidates with 7+ years of experience**, **41 percent of offers are for management roles**, **32 percent for SWEs.** Performance-based referrals — meaning IK refers candidates who've demonstrated the skill bar — not just everyone who enrolls.

---

## SLIDE 97 — Getting Started

How to actually get started. **Transformative Generative AI** — 2 to 3 months, INR 1 to 1.3 lakhs for the core program; INR 1.5 to 2.8 lakhs with the Interview Lab. **Flagship Machine Learning + Interview Lab** — 6 to 4 months, INR 2 to 2.8 lakhs. **Agentic AI Career Accelerator + Interview Lab** — 3 to 3 months, INR 3 lakhs. All programs include placement assistance, enroll-now-start-anytime scheduling, financing options, scholarships on selected courses, and a 50% refund clause on qualifying programs.

---

## SLIDE 98 — Q&A

Alright — that wraps the structured content. **Have questions? Let us help you.** Open it up — what's on your mind? Anything from the system design we walked through, the agent loop, RAG, embedding choices, evaluation, operations, or the IK pathways. Fire away.

---

## SLIDE 99 — Future Masterclasses

One more ask before we close. **What topics would you like us to cover in future masterclasses?** Drop your suggestions in the chat — multi-agent orchestration, advanced RAG (re-ranking, hybrid search), evaluation frameworks for LLM apps, fine-tuning vs. RAG deep dives, MCP and tool design, LLMOps in detail — whatever would be most useful for you next. We use this feedback directly to plan upcoming sessions.

---

## SLIDE 100 — Close

Thank you for spending this time with us. The framework we walked through today — scope the problem, identify the components, design data and tool flows, plan operations, lock down safety — is the same one I use on real projects at Google, and it's the same one you can take into your next system design interview or your next sprint. Practice it. Use the running example. Build something small end-to-end, then make it bigger. That's how it sticks.

Thanks again — see you in the next session.
