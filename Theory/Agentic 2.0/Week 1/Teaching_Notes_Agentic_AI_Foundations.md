# Agentic AI Foundations - Teaching Script
## 4-Hour Class - Slide-by-Slide Speaking Notes

---

## SLIDE 1: Title - Agentic AI Foundations

"Welcome everyone! Today we're going to explore something that's fundamentally changing how we build software. We're moving from AI that assists us to AI that acts autonomously on our behalf. And trust me, by the end of this session, you'll see why this is one of the most exciting developments in AI right now."

---

## SLIDE 2: Introduction - About me

"TODO: Don't touch it, I'll update it."

---

## SLIDE 3: Icebreaker - Let's Get to Know Each Other

"Before we dive in, I want to know who's in the room. This works best when it's interactive, so don't be shy. Let's go around and share four quick things: your name, your role, where you're joining from, and what company you work for.

And as you're introducing yourselves, I want you to think about this question: Have you ever asked ChatGPT to write code for you, and it gave you something that almost worked but not quite? Keep that thought in mind - because what we're learning today is how to turn that 'almost' into 'completely autonomous.'"

*[Give students time to introduce themselves]*

"Awesome! So we've got a great mix here. That's perfect because what we're covering today applies whether you're building customer service bots, internal tools, or the next big AI product."

---

## SLIDE 4: Optimize Your Experience

"Quick housekeeping before we start. A few things to make sure you get the most out of today:

First, please interrupt me. Seriously. If something doesn't make sense, raise your hand and ask. I guarantee that if you're confused, at least three other people are too. We're all here to learn together.

Second, there's going to be a live Sunday class component. Make sure you attend - that's where we'll do live coding and debug things together.

Third, solve the assignments and MCQs. I know, I know - we all skip homework. But here's the thing: you can watch me code for hours, but until YOU write the code and hit those errors, it won't stick. The learning happens when you struggle a bit.

And finally, you have access to Testbuddy. Use it. It's like having a personal tutor available 24/7. What you put in is what you'll get out of this course."

---

## SLIDE 5: Before We Begin

"Let me show you something that'll blow your mind. This is a picture of a roadmap showing 'Empowering Software Engineering with AI' - and look at all these different components. We've got foundation models, code generation, testing, debugging, deployment automation.

Here's what's fascinating: two years ago, these were all separate tools. You'd use one AI for code generation, another for testing, another for documentation. Now? We're building unified agents that handle ALL of this autonomously.

That's the journey we're on today - understanding how we got here and where we're going."

---

## SLIDE 6: Interactive Question

"Let me start with a question for all of you. And I want you to actually think about this:

**What agents automate tasks in the software engineering domain?**

Take 15 seconds. Think about your daily work. What AI tools are you using? Where is automation happening?

*[Pause for responses]*

Great answers! I'm hearing things like GitHub Copilot, ChatGPT for debugging, automated testing tools. Here's what I want to point out: all of these are becoming more AGENTIC. They're moving from 'I suggest code' to 'I write, test, and deploy code.'

---

## SLIDE 7: From AI Tools to Agentic Systems

"This is the fundamental shift we're witnessing right now, and I want to make sure this lands because it's HUGE.

**Agentic AI is shifting software development from tools that assist developers to systems that execute goals autonomously.**

Instead of responding to single prompts, agents now **plan, decide, act, observe outcomes, and iterate**. They're not just tools anymore - they're teammates."

---

## SLIDE 8: The AI-Driven SDLC Pipeline

"Look at this diagram. This is beautiful. This shows the entire Software Development Lifecycle becoming AI-driven.

Let me walk you through what's happening at each stage:

**Plan:** AI analyzes requirements and creates technical specifications. I'm not talking about 'generate some ideas' - I mean it reads your product docs, understands your existing architecture, and creates detailed technical plans.

**Develop:** AI builds multi-file features. Not just 'write me a function' - it architects entire features across multiple files, follows your coding standards, and even names variables consistently with your codebase.

**Test:** AI runs tests automatically. It writes unit tests, integration tests, generates edge cases you didn't think of, and runs them all.

**Deploy:** AI deploys and monitors continuously. It handles rollback if something goes wrong. It watches metrics and can roll back automatically if error rates spike.

Here's what blows my mind about this: **The AI orchestrates itself.**

In the old world, you orchestrated these steps. You decided when to test, when to deploy. Now? You give the AI a goal - 'build user authentication' - and it handles EVERYTHING.

That's the shift from tools to agents."

---

## SLIDE 9: AI-Assisted vs. Agentic AI Systems

"This slide is critical. I want you to really see the difference here because this is the 'aha' moment.

**Top row - AI-Assisted Software (Human-Driven):**
Look at this flow: Engineer → Prompt/Request → AI Suggests → Human Decides → Manual Loop

This is what we were doing with ChatGPT or GitHub Copilot when it didn't have Agentic mode until a year ago:
- You: 'Write me a function to validate email addresses'
- ChatGPT: *generates code*
- You: 'Hmm, this doesn't handle international domains'
- ChatGPT: *updates code*
- You: 'Now add length validation'
- ChatGPT: *updates again*

See the pattern? YOU are in the loop. YOU decide every next step. YOU catch the bugs.

**Bottom row - Agentic AI Systems (Goal-Driven):**
Look at this: Goal → Agent (LLM) → Reason → Act (APIs, DB, Code) → Observe → Adapt & Re-plan

This is completely different:
- You: 'Build a user authentication system'
- Agent: *Thinks: I need database schema, password hashing, session management, API endpoints, tests*
- Agent: *Creates database schema*
- Agent: *Writes authentication logic*
- Agent: *Tests it*
- Agent: *Finds bug in session timeout*
- Agent: *Fixes bug*
- Agent: *Tests again*
- Agent: *Passes all tests*
- Agent: 'Done. Authentication system is live.'

**With execution responsibility delegated to agents, the focus shifts to what they can automate.**

You're no longer the orchestrator. You're the goal-setter. The agent figures out HOW."

In the two eternal questions of **building the right product** and **building the product right** we are at a point where we have a very great solution for the second question: to build the product right.

---

## SLIDE 10: What Kind of AI Automations Are We Looking At?

"This is a screenshot from GitHub Copilot's Agentic mode that writes code autonomously, detects errors in real-time, runs tests, and creates pull requests for review.

And I am sure most of us are using it RIGHT NOW in production at our workplaces."

---

## SLIDE 11: Google's Antigravity IDE

"This is Google's Antigravity IDE - where multiple AI agents work in the editor and terminal to build apps, test code, and manage workflows inside a development environment.

You open your IDE. But instead of just you coding, there are THREE agents working alongside you:
- **Agent A** is writing your backend code
- **Agent B** is writing frontend components
- **Agent C** is writing tests and running them

They're collaborating with EACH OTHER. Agent A finishes an API endpoint and tells Agent B 'Hey, the endpoint is ready at /api/users.' Agent B uses that endpoint in the frontend. Agent C tests both.

This is like having two senior developers pair programming with you 24/7. Except they never get tired, never need coffee breaks, and work at 100x speed.

Google is using this internally, and they've reported that developers are spending 70% less time on boilerplate code and 50% less time debugging."

---

## SLIDE 12: Before We Dive Into Agents

"Before we can build these sophisticated systems, we need to understand the foundations. We need to understand what makes something an 'agent' in the first place.

So let's take a quick look at what this course will cover."

---

## SLIDE 13: Agentic AI Program Structure

"Here's our roadmap. Let me walk you through this because it's designed very intentionally. Every week, we intend to land the concepts while working through one or more projects so that you're not just seeing theory, but also doing hands on.

**Week 0-1-2: Foundations of Agentic AI**
- Week 0: Pre-Program Foundations: Python Essentials – This is something you'll need to tackle on your own. It's a prerequisite for understanding Python, as it has become the de facto language for building agentic systems. In fact, Microsoft leadership has encouraged all engineers to start learning and using Python if they want to stay competitive in this field. Despite Microsoft’s strong emphasis on .NET, the push to learn Python speaks volumes about its growing importance. Since we are all engineers here, I trust that you believe in being language-agnostic and are capable of handling this independently. That's why we refer to it as Week 0. In Computer Science, we don't start counting from 1 — we start from 0.
- Week 1: Agentic AI Foundations: Here we talk about evolution of agents from Reflex -> Goal -> Utility agents, modular architecture, prompting techniques, tool calling logic etc. We would build two agents here: one a CRM lead qualifier agent and another a FAQ Agent. This is what we will do today.
- Week 2 is all about RAG pipelines: We will Understand the concept of Embeddings, chunking strategies, vector stores, indexing strategies, Agentic RAG, Evaluations of RAG pipelines using metrics like precision, recall, response completeness etc, and also build a RAG working RAG pipeline. All of this using frameworks like Langchain, LlamaIndex, Langsmith etc.

**Week 3-4-5: Intelligent Interaction & Reasoning**
This is where we level up:
- Week 3: Multi-Agent Systems: Agent orchestration frameworks like LangGraph. We will build a AI Research Team work project.
- Week 4: Conversational Agents: Memory systems, voice I/O integration, and multimodal pipelines. The project here we build is a Research Assistant.
- Week 5: Agent Protocols: Standards for agent messaging, workflow design, and asynchronous communication. The project here focuses on building a Negotiation System between two agents, and frameworks that we will explore are Google ADK and LangGraph.

**Week 6-7: Real-World Intelligence & Deployment**
This is where we ship to production:
- Week 6: Vertical Agents: API integrations, OAuth, structured workflows, and hybrid systems. The project is Price Comparison Agent.
- Week 7: Summarization & Recommendations: Text summarization, ranking systems, and recommendation dashboards. The project is Smart Recommender.

**Week 8-9-10-11: Optimization, Safety & Enterprise Deployment**
This is where we make it enterprise-ready:
- Week 8: Safe Agents: Guardrails, observability, and cost monitoring. The project here is the Safe Support Agent.
- Week 9: Fine-Tuning: Custom training pipelines and deployment strategies. The project is about building a Fine-Tuned Agent for a particular domain.
- Week 10 & 11: These two weeks will be where you will apply all the knowledge gained and build end-to-end systems with multi-agent architecture and cloud deployment.

Each week builds on the previous. By Week 11, you'll have a solid grasp on building agentic systems."

---

## SLIDE 13 (Cont.): The Shift Toward Agentic Systems

"Let me summarize what we've covered so far:

We have gone from from 'AI suggests' to 'AI executes.'

And that's exactly what we're going to learn to build today.

**Let me give you an intuition of this evolution using an HR Assistant - and I'm going to show you THREE versions of this system to really nail down what makes something agentic.**

We want to build an HR assistant that can help employees. Let's see how this evolves:

**Version 1: Simple RAG Chatbot (NOT Agentic)**

Imagine you build a chatbot that can answer questions like:
- 'How many vacation days do I have per year?'
- 'What is the policy on sick leave?'

You have all policy data in PDF files. You build a RAG system - Retrieval Augmented Generation - that pulls information from these PDFs and answers questions.

**Is this agentic AI?** No. This is just a workflow. It's reactive Q&A. You ask, it responds. No planning, no autonomy. Anthropic actually has a great document called 'Building Effective Agents' where they categorize this as a WORKFLOW, not an agent.

**Version 2: Tool-Augmented Chatbot (Still Not Agentic)**

Now let's advance this. We add APIs so employees can ask:
- 'How many leaves do I have left?'
- 'Apply for 3 days of vacation next week'

Notice what's different here - **you are taking actions**. Not just answering questions. The system is integrated with your HR management system through APIs. It can:
- Pull leave data for a specific employee
- Submit leave applications
- Detect who you are based on login

This is better! But **is it agentic?** Still no. This is a tool-augmented chatbot. Yes, it has access to tools and can take actions, but there's no complex reasoning or multi-step planning. You give it a direct task, it executes that one task.

**Version 3: True Agentic AI System (THIS is Agentic)**

Now let's give it a GOAL - not a simple task, but a complex goal:
- 'Prepare for Sara's maternity leave'
- 'Onboard the new intern joining next Monday'

This requires **multi-step reasoning and planning**. Let me walk you through what happens when you say 'Onboard the new intern joining next Monday':

The agent breaks this down and executes:

1. **Schedule a welcome meeting** - It sends a meeting invite through Outlook with the intern and their manager

2. **Create the intern's profile** in the HR system through API integration

3. **Generate content** - The LLM writes meeting descriptions, welcome emails, all customized

4. **Create IT tickets** - It automatically submits requests for Wi-Fi credentials, email access, Slack account through your helpdesk system

5. **Order equipment** - Creates inventory requests for laptop, ID card, etc.

**See what's happening here?** The agent is:
- Planning multiple steps autonomously
- Using LLMs for content generation
- Calling multiple APIs and tools
- Making decisions about what to do next
- Executing everything without you micromanaging each step

**This is agentic AI.** You gave it a high-level goal, and it figured out the plan and executed it.

**The Key Characteristics of Agentic AI Systems:**

Let me break down what makes something truly agentic:

1. **Goal-Oriented Planning** - You're not giving simple tasks like 'tell me my leave balance.' You're giving complex goals that require reasoning and planning.

2. **Multi-Step Reasoning** - The system breaks down complex goals into logical steps on its own.

3. **Autonomous Decision Making** - It's sending emails, creating tickets, scheduling meetings - all without asking you 'should I click this button?'

4. **Access to Tools** - Integration with Outlook, HR systems, helpdesk, inventory systems.

5. **Knowledge Access** - It can pull from PDF files, databases, documentation.

6. **Memory** - It maintains context during the conversation and remembers what it's already done.

**Here's my simple definition:** Agentic AI is an AI system that can make decisions and take actions on its own to achieve a goal without being told exactly what to do at every step.

**Real-World Examples You've Probably Seen:**

Think about AI coding tools like Lovable or Replit. When you say 'Build me a todo list app,' they don't just generate code. They:
1. Figure out what features a todo list needs
2. Create a multi-step plan
3. Write the code
4. Execute and test it
5. Debug issues
6. Iterate until it works

That's agentic AI in action.

Or imagine a travel assistant where you say: 'Book a 7-day trip to London in May with at least 4 sunny days, budget $3000.' An agentic system will:
- Check weather forecasts using AccuWeather API
- Search flights and hotels using Expedia API
- Plan an itinerary
- Make bookings
- Handle any issues that come up

You gave it a goal with constraints. It figured out the plan and executed it.

**This is the shift we're teaching today:** From hardcoded logic to goal-directed reasoning with autonomous execution, with the safety measures to make it production-ready."

---

## SLIDE 14: What You'll Be Learning Today

"Alright, let's take a breath. That was a lot of context. Now I want to outline exactly what we're covering today."

---

## SLIDE 15: Today's Agenda

"We've got four main sections, and we'll take breaks between each:

**Section 1: Reflex & Goal-based Agents**
This is where we start with the fundamentals. What IS an agent? We'll build up from the simplest possible agent to more sophisticated ones.

**Section 2: Utility Agents and Intro to LLMs**
Here we'll bridge from classical AI agents to modern LLM-based agents. We'll talk about what LLMs can and cannot do.

**Section 3: LLM-Based Agents**
This is where the magic happens. We'll learn the ReAct loop, which is THE fundamental pattern for building modern agents.

**Section 4: Q&A and two projects: CRM Lead Qualifier and Week 0 Mini Project**
We'll look at code for two different agents - one a CRM Lead Qualifier Agent which demonstrates tool calling by agents, and a FAQ Agent which answers question grounded on data from some CSVs, instead of using it's own general knowledge. 

Ofcourse we will have Q and A not only in this section but throughout the class. Please keep popping your questions in the chat and I'll answer them whenever I can.

---

## SLIDE 16: Reflex & Goal-based Agents

"Alright, Section 1. Let's start at the very beginning.

**Moving from simple reaction to intelligent planning and strategic foresight.**

That's our journey for the next hour. We're going to build up your intuition for what makes something an 'agent' and why certain designs work better than others."

---

## SLIDE 17: Evolution of AI Agents

"Look at this diagram. This shows the evolution from simple reflex agents to modern LLM-based agents.

On the left, you see simple agents that just react. On the right, you see complex agents that plan and reason.

Here's the key insight: **Every agent we're building today is built on these foundational concepts.**

Even the most sophisticated LLM agent is still using principles from classical AI agents. We're not throwing out decades of AI research - we're building on top of it."

---

## SLIDE 18: What is a Reflex Agent?

"Let me start with the absolute simplest type of agent. The reflex agent.

**The simplest form of intelligent agent in AI architecture.**

Here are the key characteristics:

**1. They act immediately based only on the current moment.**
A reflex agent doesn't think about the past or the future. It only knows RIGHT NOW.

**2. Purely Reactive: They do not 'think,' plan ahead, or analyze past history before acting.**
There's no deliberation. No 'hmm, let me consider my options.'

**3. Analogy: Like touching a hot stove and immediately pulling your hand back.**
Your brain didn't weigh the pros and cons. It didn't consult past experiences. It just reacted INSTANTLY to the stimulus.

Let me give you some real-world examples:

**Example 1: A Thermostat**
```
IF temperature < 68°F THEN turn on heat
IF temperature > 72°F THEN turn on AC
```
That's it. That's the entire 'intelligence' of your thermostat. It doesn't remember yesterday's temperature. It doesn't predict tomorrow's weather. It just reacts to RIGHT NOW.

**Example 2: Automatic Door**
```
IF sensor detects motion THEN open door
IF no motion for 5 seconds THEN close door
```
The door doesn't remember who walked through. It doesn't learn patterns like 'oh, lots of people come through at 9am.' It just reacts.

**Example 3: Simple Spam Filter**
```
IF email contains 'FREE MONEY' THEN mark as spam
IF email from known contact THEN mark as safe
```

These are reflex agents. Simple, fast, but limited."

---

## SLIDE 19: Reflex Agents - The Mechanism

"Now let me show you HOW reflex agents work under the hood.

**Condition-Action Rules**

Reflex agents operate on rigid 'If-Then' logic. Look at this loop:

**1. Sensors:** Perceive the environment (e.g., a camera seeing a red light)

**2. Condition Match:** Find the rule that applies to this exact moment (e.g., 'If light is red...')

**3. Actuators:** Execute the pre-defined action immediately (e.g., '...press brake')

**It is essentially a fast lookup table. There is no deliberation process.**

Let me say that again because it's important: **There is NO thinking.** The agent doesn't wonder 'Should I brake? What are my options?' It just matches the condition and fires the action instantly.

That's it. No memory. No planning. Just immediate reaction.

Now you might be thinking: 'That seems too simple to be useful.' And you're partially right. These agents are VERY limited. Which brings us to their critical flaw..."

---

## SLIDE 20: Reflex Agent's Critical Flaw - Amnesia

"This is the most important slide about reflex agents. Pay close attention because this flaw is WHY we need more sophisticated agents.

**Why basic reflex agents fail**

**No Memory:** Standard reflex agents have zero knowledge of what happened one second ago.

Think about that. ZERO knowledge. They live entirely in the present moment. They have no history. No context. No memory.

**The Requirement of Full Observability:** They only function correctly if they can see everything relevant to the decision right now.

**The Failure Mode:** If vital information is hidden, they will make the wrong decision based only on visible local data.

Let me give you two examples that really drive this home:

**Example 1: The Robotic Vacuum**

Imagine a Roomba that's a pure reflex agent:
```
IF sensor detects dust nearby THEN move to dust and clean
```

What's the problem here? The vacuum doesn't REMEMBER that it already cleaned this spot 30 seconds ago. So if its sensors still detect trace dust, it might clean the same spot FOREVER.

Meanwhile, the rest of your floor is filthy. But the agent doesn't know that because it has no memory and can't see the whole house.

**Example 2: The Self-Driving Car (This is terrifying)**

Imagine a self-driving car using only a reflex agent. Here's a scenario that happened in early autonomous vehicle research:

- Self-driving car is approaching an intersection
- A cyclist enters the camera's view
- Car's reflex rule: 'IF cyclist visible THEN slow down'
- Car slows down
- Cyclist passes behind a bus
- Cyclist is now NOT visible to the car's sensors
- Car's reflex rule: 'IF no obstacles visible THEN proceed'
- **Car accelerates → COLLISION!**

WHY DID THIS HAPPEN?

Because the agent doesn't REMEMBER that the cyclist existed. As soon as the cyclist left the sensor's field of view, they ceased to exist in the agent's 'mind.'

A human driver would remember: 'That cyclist went behind that bus and is probably still there on the other side.' But a pure reflex agent CAN'T do that.

This is why Tesla, Waymo, and every other self-driving car company had to move beyond reflex agents. **You literally cannot build a safe self-driving car with just reflex agents.**

The amnesia problem is CRITICAL."

---

## SLIDE 21: The Upgrade - Model-Based Reflex Agents

"So how do we fix this? How do we give agents memory?

**Adding short-term memory**

The solution is called a **Model-Based Reflex Agent.**

Here's the key innovation:
**To handle environments that aren't fully visible (partially observable), we add an internal state.**

Think of it like giving the agent a notebook. It can write down: 'I saw a cyclist 3 seconds ago behind that bus.' Now even though the cyclist isn't visible RIGHT NOW, the agent REMEMBERS they exist.

The agent keeps a mental 'model' of the world that tracks things it cannot currently see.

**Current Perception + Internal Memory = Action**

Let me show you the self-driving car example fixed:

**Without Memory (Reflex Agent):**
- See cyclist → Slow down
- Don't see cyclist → Speed up → CRASH

**With Memory (Model-Based Reflex Agent):**
- See cyclist → Slow down
- Cyclist goes behind bus
- Don't see cyclist BUT REMEMBER cyclist went behind bus
- Stay slow and cautious
- Wait for cyclist to emerge → SAFE

See the difference? Now the agent has CONTEXT. It has MEMORY.

This is a HUGE upgrade from pure reflex agents. But we're still not at full autonomy. For that, we need to go even further..."

---

## SLIDE 22: Prerequisites & Environment Setup

"Here is a pre-requisite guide to work with Google Colab Notebooks, like how to add API keys in the secrets manager etc.

We will work mostly with Colab Notebooks in today's class so it maybe helpful for you."

---

## SLIDE 23: Reflex Agents - Hands-On Notebook

"Alright, we covered reflex agents in theory, now I want you to SEE them in action.

Here is a Google Colab notebook that demonstrates everything we just discussed - with working code you can run right now.

**Link:** https://colab.research.google.com/drive/1NkgRA-YidiyYc-wB6u3oSCzlOPEGTtW6

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

## SLIDE 24: Goal-Based Agents

"**Moving from simple reaction to intelligent planning and strategic foresight.**

So far, we've talked about agents that REACT to their environment. Reflex agents see something and immediately respond.

But what if we want an agent that can PLAN? What if we want an agent that can think several steps ahead?

That's where goal-based agents come in."

---

## SLIDE 25: The Paradigm Shift

**Why reacting to the present is no longer enough.**

Let me give you a concrete example. Imagine you're playing chess.

**Reflex Approach:**
- Opponent moves their bishop
- You react: 'My queen is threatened, move queen to safety'
- That's it. You reacted to the immediate threat.

**Goal-Based Approach:**
- Your goal: Checkmate the opponent
- You analyze: 'If I move my queen here, opponent will likely move their rook there, then I can bring my knight in for a fork, and in 4 moves, I have checkmate'
- You're not just reacting. You're PLANNING multiple steps ahead.

In software, this difference is massive. The reflex approach handles the current request. The goal-based approach completes the entire objective."

---

## SLIDE 26: Beyond Pure Reaction

**Reflex Agents live in the 'now':**
- They wait and react
- 'If X happens, do Y'
- No consideration of future states

**Goal-Based Agents live in the 'future':**
- They plan toward a desired state
- 'I want to achieve Z. What sequence of actions gets me there?'
- They navigate complex environments by considering multiple future possibilities

Here's a real-world example that everyone can relate to:

**Traffic Navigation**

**Reflex Agent Approach:**
- At intersection: Turn right (because the rule says turn right here)
- At next intersection: Turn left
- At next intersection: Go straight
- You're following local rules, but do you even know where you're going? Not really.

**Goal-Based Agent Approach:**
- Goal: Get to the airport
- Plan: Calculate the entire route BEFORE starting
- Consider: Traffic, road closures, time of day
- Navigate with the END in mind

The goal-based agent has a MAP. The reflex agent is just following signs."

---

## SLIDE 27: Core Components

"Every goal-based agent has three essential components:

**1. The Goal**
A description of the desirable situation. Examples:
- 'Checkmate' in chess
- 'Destination Reached' in GPS
- 'All tests passing' in CI/CD pipeline

The goal tells the agent WHERE it's trying to go.

**2. World Model (Transition Model)**
Knowledge about how the world changes and how actions affect the state.

This is the agent's understanding of cause and effect:
- 'If I move my knight to E5, the opponent's bishop on D6 is captured'
- 'If I take Highway 101, I'll save 10 minutes but pay $5 in tolls'
- 'If I deploy this code, the API response time will improve by 20ms'

**3. Search & Plan**
The algorithmic process of simulating sequences of actions to find the path to the goal.

This is where the agent 'thinks.' It considers different options:
- Option A: Takes 30 minutes, costs $5
- Option B: Takes 40 minutes, costs $0
- Option C: Takes 25 minutes, costs $10

And picks the best one based on your priorities.

Let me show you a real example of these three components working together..."

---

## SLIDE 28: Example: GPS Navigation

"This is the perfect example because everyone has used GPS.

**A GPS is a quintessential goal-based agent.**

**The Problem:** I'm at my house. I want to reach the airport.

**Component 1 - The Goal:** Destination (Airport)
That's simple. You type 'SFO Airport' into Google Maps. That's your goal.

**Component 2 - World Model:**
This is where it gets interesting. Your GPS knows:
- **Road network:** Every road, every intersection, every connection
- **Traffic conditions:** Real-time data from millions of phones
- **Speed limits:** How fast you can legally go on each road
- **Road closures:** Construction, accidents, events

This is the GPS's understanding of 'how the world works.'

**Component 3 - Search & Plan:**
Now comes the magic. The GPS doesn't just pick a random route. It:
- Calculates EVERY possible route from your house to the airport
- Evaluates each route for time, distance, traffic
- Uses algorithms like A* or Dijkstra's algorithm
- Selects the optimal path

And here's what's beautiful: It does this in SECONDS. Your GPS might be considering thousands of possible routes and evaluating millions of path segments.

**The result?**
You get three options:
- Fastest: 34 min via I-90 (tolls)
- Avoid tolls: 42 min via Route 20
- Shortest: 38 min via city streets

The agent PLANNED all of this before you even started driving. That's the power of goal-based agents."

---

## SLIDE 29: Reflex vs. Goal-Based Performance

"Look at this comparison chart. This is really important because it helps you choose which type of agent to build for your use case.

Look at these three dimensions:

**1. Adaptability**
- **Reflex agents:** LOW adaptability - They follow fixed rules. Change the environment, and they break.
- **Goal-based agents:** HIGH adaptability - They can handle new situations by replanning.

Example: A reflex vacuum cleaner has rules like 'If obstacle, turn right.' But if you move furniture, it might get stuck in a corner. A goal-based vacuum says 'My goal is to clean the whole room' and finds a NEW path around the furniture.

**2. Reaction Speed**
- **Reflex agents:** FAST - Instant reaction because they don't think, they just follow rules
- **Goal-based agents:** SLOWER - They need time to search and plan

This is why reflex agents are great for real-time systems. A self-driving car uses reflex rules for 'If pedestrian in front, BRAKE IMMEDIATELY.' There's no time to plan a 5-step sequence.

**3. Complexity**
- **Reflex agents:** LOW complexity - Good for simple, well-defined environments
- **Goal-based agents:** HIGH complexity - Excel in complex scenarios with many possibilities

Example:
- **Reflex:** Thermostat - 'If temp > 72°F, turn on AC' (simple, fast, effective)
- **Goal-based:** Chess engine - Needs to think through millions of possible moves (complex, slow, powerful)

**The takeaway:**
- Need speed and simplicity? Reflex agents.
- Need intelligence and adaptability? Goal-based agents.
- Most real systems? A HYBRID of both. Fast reflexes for safety, goal-based planning for complex tasks."

---

## SLIDE 30: Goal-based agents

"Alright, we've covered the theory. Now I want to show you code.

I've prepared a Colab notebook that demonstrates a goal-based agent in action. This will make everything click.

**Notebook Link:** https://colab.research.google.com/drive/1DfdNEMhmHONouKs3JGEI62iPAEGfST7s

Here's what the notebook shows:

**The Scenario:**
You have a 5x5 grid. The agent starts at position (0,0) in the top-left corner. The goal is at position (4,4) in the bottom-right corner.

**What makes this a goal-based agent?**

Watch what happens when you run the code:

**Step 1: PERCEIVE**
- Agent checks: 'Where am I?' → (0,0)
- Agent checks: 'Where's my goal?' → (4,4)

**Step 2: PLAN (This is the magic)**
- Agent calculates: 'I need to go 4 steps DOWN and 4 steps RIGHT'
- Agent creates the COMPLETE plan: `['Down', 'Down', 'Down', 'Down', 'Right', 'Right', 'Right', 'Right']`
- **Notice: It hasn't moved yet! It's just thinking.**

**Step 3: EXECUTE**
- Now it follows the plan step by step
- Down, Down, Down, Down, Right, Right, Right, Right
- Goal reached in exactly 8 moves!

**Compare this to a reflex agent:**
A reflex agent would:
- Look around: 'Am I at the goal? No.'
- Take one step (maybe randomly)
- Look around again: 'Am I at the goal? No.'
- Take another step
- Repeat until it stumbles onto the goal

That's reactive. No intelligence. Just trial and error.

**The goal-based agent is different:**

Look at this code from the notebook:

```python
def run(self):
    # 1. PERCEIVE
    current_loc = self.perceive()
    goal_loc = self.formulate_goal()

    # 2. PLAN (Generate FULL plan before moving)
    self.plan = self.formulate_plan(current_loc, goal_loc)
    print(f'Plan created: {self.plan}')

    # 3. ACT (Execute the plan)
    for action in self.plan:
        self.env.update_agent_pos(action)
```

See that? The agent calls `formulate_plan()` BEFORE it takes even a single step. It thinks through the ENTIRE problem first. That's intelligence.

**Open-Loop vs Closed-Loop:**

This specific implementation uses **open-loop execution:**
- Make a plan
- Execute it without checking sensors again
- Assume the world won't change

In more advanced systems, you'd use **closed-loop execution:**
- Make a plan
- Execute one step
- Check sensors again (PERCEIVE)
- Adjust plan if needed
- Execute next step

GPS does this! It recalculates your route if you miss a turn.

Now, you might be thinking: 'What if obstacles appear while the agent is moving?' Great question! That's where re-planning comes in, and that's what real-world agents do. They continuously cycle through PERCEIVE → SEARCH → ACT.

For now, the key takeaway: **Goal-based agents plan BEFORE they act. That's what separates them from reflex agents.**"

---

## SLIDE 31(Cont.): Question - Interactive Discussion

"Alright everyone, before we move forward, I want to hear from YOU.

Look at the question on the screen:

**'What can reflex and goal-based agents do to automate some complex tasks, especially for software developers/engineers?'**

**'Can you share an example from your experience?'**

Think about your day-to-day work:
- Code reviews
- Testing
- Deployment pipelines
- Bug triage
- Documentation
- Monitoring and alerts

Where do you see reflex agents helping? Where do you see goal-based agents?

Let me give you a starting example to get the discussion going:

**Reflex Agent Example:**
- GitHub Actions CI/CD pipeline
- **Rule:** If push to main branch, run tests
- **Rule:** If tests fail, block the merge
- Fast, reactive, rule-based

**Goal-Based Agent Example:**
- Automated bug fix agent
- **Goal:** Fix failing tests in the codebase
- **Planning:** Analyze error logs, search codebase for root cause, generate fix, test fix
- **Execution:** Create PR with fix

---

## SLIDE 32: Break Time!

"Alright everyone, let's take a 10-minute break. When we come back, we're diving into LLMs and how they fit into the agent framework.

---

## SLIDE 33: Today's Agenda (Checkpoint)

"Welcome back!

**Section 1: Reflex & Goal-based Agents** ✅ DONE
- We just finished this section!
- You learned about reflex agents, model-based reflex agents, and goal-based agents
- You ran two hands-on notebooks
- You understand the Decision Cycle: Perceive → Search → Act

**Section 2: Utility Agents and Intro to LLMs** ⏭️ UP NEXT
- This is where we're going now
- We'll talk about agents that optimize for the BEST outcomes
- We'll bridge from classical agents to LLM-powered agents

---

## SLIDE 34: Utility-Based Agents

"Alright, we've covered reflex agents and goal-based agents. Now we're moving to the next level of sophistication.

**Utility-Based Agents**

**Subtitle: Optimizing for the Best Outcome, Not Just Any Outcome**

This is a game-changer. Let me explain what makes utility-based agents different.

Goal-based agents ask: 'Can I reach my goal?'
Utility-based agents ask: 'What's the BEST way to reach my goal?'

It's the difference between:
- Getting to the airport (goal-based)
- Getting to the airport in the fastest, cheapest, most comfortable way possible (utility-based)

The key concept here is **optimization**. Utility agents don't just solve problems - they solve problems WELL.

We're going to explore:
1. What makes an agent utility-based
2. How they evaluate different options
3. Real-world applications where this matters

Let's dive in."

---

## SLIDE 35: What is a Utility-Based Agent?

"Look at this diagram on the screen. You see a speedometer-like gauge showing different zones from red (bad) to green (good).

**Going Beyond 'Success'**

Here's the key insight:

**Goal-based agents are binary:** They either succeed or fail.
- Did I reach the airport? Yes/No.
- Did the robot pick up the object? Yes/No.
- Did I win the chess game? Yes/No.

**Utility-based agents operate on a continuous spectrum:**
- They don't just ask: 'Does this path lead to the goal?'
- They ask: **'How GOOD is this path compared to the others?'**

The agent attempts to maximize their **'happiness'** or **utility** in scenarios where multiple valid solutions exist.

**Think of it like this:**

You're booking a flight from New York to San Francisco. There are 20 flights available. They all achieve the goal (getting you there), but:
- Some are cheaper
- Some are faster
- Some have better seats
- Some have fewer layovers

**Goal-based agent:** Pick ANY flight that gets you there.
**Utility-based agent:** Evaluate all flights and pick the one that maximizes your utility based on your preferences (price, time, comfort).

**The Utility Function:**

This is the mathematical heart of utility agents. It's a function that assigns a score to each possible state:

utility_score = f(state)

For flights:
- utility(cheap, slow, uncomfortable) = 6/10
- utility(expensive, fast, comfortable) = 8/10
- utility(moderate price, moderate speed, good comfort) = 9/10

The agent picks the option with the HIGHEST utility score.

**Real-World Example:**

Think about Uber pricing:
- **Goal:** Get a ride
- **Utility optimization:** Balance price, wait time, and car quality
  - UberX: Cheap, longer wait, basic car → utility = 7
  - UberXL: More expensive, short wait, bigger car → utility = 6
  - Uber Comfort: Moderate price, short wait, nice car → utility = 9

You pick Uber Comfort because it maximizes YOUR utility given your preferences.

This is what makes utility agents powerful - they consider trade-offs and optimize for what matters most."

---

## SLIDE 36: Goal vs. Utility Agents

"Let me show you this comparison side by side. This really clarifies the difference.

**Goal-Based Agents: Binary Decision Making**
- ✓ Did I get there? Yes/No.
- ✓ Any valid path is acceptable.
- ✓ Good for simple puzzles.

It's black and white. Either you achieved the goal or you didn't.

**Utility-Based Agents: Optimized Decision Making**
- ✓ Which path is faster/cheaper?
- ✓ Trade-offs are evaluated.
- ✓ Crucial for complex economics.

It's a spectrum. You're looking for the BEST solution among many valid options.

---

## SLIDE 37: Utility Agent Architecture - The Evaluation Step

"Now let me show you how utility-based agents actually work under the hood. Look at this architecture diagram.

**The top differentiator in the architecture is the Utility Function block.**

This is what sets utility agents apart. After the agent's world model predicts 'What happens if I take action X?', the utility function asks: **'How happy will I be if that happens?'**

Let me walk through the flow:

**Step 1: SENSORS**
- Perceive the environment
- 'Where am I? What's the current state?'

**Step 2: WORLD MODEL**
- Predict outcomes: 'If I take action A, what happens?'
- Model different scenarios

**Step 3: UTILITY FUNCTION** ← This is the key difference!
- Evaluate each predicted outcome: 'How good is this outcome?'
- Assign scores based on your objectives
- Compare options

**Step 4: DECISION MAKER**
- Pick the action that leads to the highest utility
- 'This is the best choice.'

**Step 5: ACTUATORS**
- Execute the chosen action

**The Utility Function is where the magic happens.**

Think of it as the agent's value system. It encodes what the agent cares about.

Example: Self-driving car

**Utility function might be:**
```python
utility = (
    weight_safety * safety_score +
    weight_speed * speed_score +
    weight_comfort * comfort_score +
    weight_efficiency * fuel_efficiency
)
```

You can adjust the weights based on context:
- **City driving:** High weight on safety, low weight on speed
- **Highway driving:** Moderate weight on speed, high weight on efficiency
- **Luxury mode:** High weight on comfort

**This stone allows the Decision Maker to pick conflicting goals (e.g., Speed vs. Safety).**

If the action 'Go 80 mph' has:
- High speed score (good!)
- Low safety score (bad in current traffic)
- Utility = 0.3 * 10 + 0.7 * 2 = 4.4

But 'Go 60 mph' has:
- Moderate speed score
- High safety score
- Utility = 0.3 * 7 + 0.7 * 9 = 8.4 ← BETTER!

The agent picks 60 mph because the utility function prioritizes safety over speed in this context.

**Key takeaway:** The utility function lets agents balance competing objectives and make nuanced decisions. This is how real-world agents handle complexity."

---

## SLIDE 38: Real World Example: Navigation

"Let me bring this back to something we all use: GPS routing.

Look at this map with multiple routes. This is a perfect example of utility-based agents in action.

**GPS Routing is Utility-Based**

When you open Google Maps and ask for directions, you're interacting with a utility-based agent. Here's what's happening:

**A simple goal agent might just find ANY connected road to the destination.**

But Google Maps does something much smarter. It evaluates multiple routes based on a **complex utility function.**

**The utility function considers:**
- **Minimize Time (Cost):** How long will this route take?
- **Minimize Tolls (Cost):** Does this route have toll roads?
- **Maximize Safety (Reward):** Is this route well-lit, low-crime, well-maintained?

And it gives you THREE options:

**Route 1: Fastest route - 16 min via I-90**
- High speed, tolls required
- Utility for someone prioritizing time: ★★★★★

**Route 2: Route avoiding tolls - 18 min via Route 20**
- Slightly longer, but free
- Utility for someone on a budget: ★★★★★

**Route 3: Scenic route - 20 min via city streets**
- Longer, but nicer drive
- Utility for someone who wants to enjoy the drive: ★★★★★

**The agent calculates utility for each route and presents the top options.**

But here's where it gets even smarter: Google Maps LEARNS your preferences over time.
- If you always pick toll-free routes, it increases the weight on minimizing cost
- If you always pick fastest routes regardless of tolls, it increases the weight on minimizing time

This is utility-based agents evolving toward learning agents (which we'll cover soon).

**Another example: The route isn't just about distance**

Imagine two routes:
- **Route A:** 10 miles, highway, clear roads → 15 minutes
- **Route B:** 8 miles, city streets, 20 traffic lights → 25 minutes

A simple goal-based agent might pick Route B (shorter distance).
A utility-based agent picks Route A (better utility given traffic conditions).

**This is the power of utility agents - they optimize for what actually matters, not just binary goal achievement.**"

---

## SLIDE 39: Utility-based agents

"Before we move on to LLMs and modern agents, I want to show you utility-based agents in action with a hands-on example.

**Colab Notebook:** https://colab.research.google.com/drive/1k9KsEJ0FhuYfssIIplov8y1D1I2MrJWh

Let me walk you through what this notebook demonstrates.

**The Scenario: Choosing a Travel Route**

Imagine you need to get somewhere. You have three route options:

1. **Highway** - Fast (20 min), expensive ($15), safe (8/10), boring views (2/10)
2. **Back Roads** - Slow (45 min), free ($0), less safe (6/10), scenic (9/10)
3. **City Center** - Medium time (30 min), cheap ($5), less safe (4/10), okay views (5/10)

**A goal-based agent would say:** 'All three routes reach the destination, so they're all equally good.'

**But that's not how humans think!** We have preferences. We make trade-offs.

**This is where utility agents come in.**

**The Notebook Shows Two Agents:**

**Agent 1: Business Executive**
- Utility function weights:
  - `time: -2.0` (HATES wasting time)
  - `cost: -0.1` (doesn't care much about money)
  - `safety: 2.0` (values safety)
  - `view: 0.0` (doesn't care about scenery)

**Agent 2: Broke Student**
- Utility function weights:
  - `time: -0.1` (doesn't mind spending time)
  - `cost: -5.0` (HATES spending money)
  - `safety: 1.0` (cares somewhat about safety)
  - `view: 2.0` (enjoys nice views)

**Watch what happens when you run the notebook:**

**Business Agent evaluates:**
- Highway: Score = -25.5 ← **BEST for business agent**
- Back Roads: Score = -78.0 ← Worst (too slow!)
- City Center: Score = -52.5

**Decision: Business Agent chooses 'Highway'**

**Student Agent evaluates:**
- Highway: Score = -65.0 ← Worst (too expensive!)
- Back Roads: Score = 19.5 ← **BEST for student**
- City Center: Score = -14.0

**Decision: Student Agent chooses 'Back Roads'**

**This is beautiful! Look at what just happened:**

Both agents:
- Had the same options
- Used the same algorithm
- Made completely different choices
- **Both were acting rationally!**

The student isn't 'wrong' for taking the slow route. They're optimizing for THEIR utility function (saving money).

**The Key Equation:**

$$U(s) = w_1 f_1 + w_2 f_2 + w_3 f_3 + ...$$

Where:
- U(s) = Utility score for a state/action
- w = weights (the agent's 'personality')
- f = features (time, cost, safety, view)

**The Magic of Utility Functions:**

1. **Explicit Preferences** - The agent's priorities are transparent and tunable
2. **Rational ≠ Identical** - Different agents can make different rational choices
3. **Complex Trade-offs** - Reduces multi-dimensional decisions to a single score
4. **Scalable** - Works with hundreds of options, not just three routes

**Real-world applications of this exact pattern:**

- **Google Maps** showing you 'fastest', 'shortest', and 'eco-friendly' routes - different utility functions!
- **Netflix recommendations** - your viewing history defines YOUR utility function
- **Autonomous vehicles** - balancing speed, safety, fuel efficiency, passenger comfort
- **Financial trading bots** - optimizing for risk vs. reward

**Open the notebook and run it yourself.** Change the weights. Make the student value safety more. Make the business exec care about cost. Watch how the decisions change.

This is the foundation of rational decision-making in AI."

---

## SLIDE 40: Conclusion

"Let me wrap up this section on utility-based agents with one key statement:

**'Utility Agents provide the foundation for rational decision-making in complex, uncertain environments.'**

This is huge. Think about what we've learned:

- **Reflex agents** react to immediate stimuli
- **Goal-based agents** plan to reach a goal
- **Utility-based agents** optimize to reach the goal in the BEST possible way

Utility agents are the bridge between simple goal achievement and intelligent optimization. They're what allows AI systems to make human-like trade-offs:
- Speed vs. Safety
- Cost vs. Quality
- Short-term gain vs. Long-term benefit

**Real-world impact:**

Every time you:
- Get three route options from Google Maps
- See personalized recommendations on Netflix
- Use algorithmic trading platforms
- Benefit from smart energy systems

You're experiencing utility-based agents in action.

---

## SLIDE 41: Question - Interactive Discussion

"Alright, here's a question I want YOU to think about:

**'How can I understand where to use utility-based agents, especially for the software engineering domain?'**

Let me give you a framework:

**Use utility-based agents when:**

1. **Multiple valid solutions exist**
   - Example: Code refactoring - many ways to improve code, which is best?

2. **Resources are constrained**
   - Example: CI/CD pipeline - optimize for speed AND cost AND reliability

3. **Trade-offs must be balanced**
   - Example: Caching strategy - memory usage vs. performance vs. staleness

4. **Optimization matters**
   - Example: Database query planning - many query execution plans, pick the fastest

**Software engineering examples:**

**Example 1: Automated Code Review**
- **Goal-based:** 'Find bugs in the code'
- **Utility-based:** 'Find bugs, but prioritize critical security issues, reduce false positives, and suggest fixes that are easy to implement'

**Example 2: Test Suite Optimization**
- **Goal-based:** 'Run all tests'
- **Utility-based:** 'Run tests that maximize coverage while minimizing execution time and infrastructure cost'

**Example 3: Resource Allocation in Kubernetes**
- **Goal-based:** 'Deploy the application'
- **Utility-based:** 'Deploy with optimal pod distribution to balance load, minimize latency, reduce cost, and maintain redundancy'

**Example 4: Dependency Resolution**
- **Goal-based:** 'Install all required packages'
- **Utility-based:** 'Install packages that satisfy all constraints while minimizing version conflicts, download size, and security vulnerabilities'

**Now, I want to hear from you:**

Can anyone think of a scenario in your work where a utility-based agent would be valuable?

*[Take 5-7 minutes for discussion. Call on 3-4 people. Encourage specific examples.]*

Great examples, everyone! You're starting to think like agent builders."

---

## SLIDE 42: From Words to Action

"Alright, now we're transitioning to the most exciting part of this course.

**From Words to Action**

**Subtitle: Understanding Large Language Models (LLMs) and the Rise of AI Agents**

Up until now, we've been talking about classical AI agents - reflex agents, goal-based agents, utility agents. These are built with traditional programming logic:
- IF-THEN rules
- Search algorithms
- Utility functions

But now we're going to talk about something that changed EVERYTHING:

**Large Language Models.**

ChatGPT came out in November 2022. That was almost 3 years ago. And it completely transformed what's possible with AI agents.

Before LLMs, agents were:
- Narrow: Built for specific tasks
- Rigid: Followed pre-programmed logic
- Expensive to build: Required expert AI engineering

After LLMs, agents became:
- General-purpose: Can handle diverse tasks
- Flexible: Can reason through novel situations
- Accessible: Anyone can build agents with prompts and APIs

**Here's the big question we're going to answer:**

How do we bridge from reactive language models (like ChatGPT) to proactive AI agents that can plan, reason, and take actions in the real world?

That's the journey we're about to take. Buckle up."

---

## SLIDE 43: What are LLMs?

"Alright, now let's talk about Large Language Models. Look at this diagram on the screen.

You see three overlapping circles representing the three words: **Large, Language, Model.**

Let me break this down:

**Large:**
- Trained on **massive datasets** to learn patterns, meaning, and reasoning
- We're talking billions of parameters - GPT-4 has over 1 trillion parameters
- These models have read more text than any human could in a thousand lifetimes

**Language:**
- **Understand and generate** language and other modalities (text, code, images, audio)
- They can comprehend context, nuance, idioms, technical jargon
- They can write in different styles, tones, languages

**Model:**
- Built on **transformer architectures that scale** to billions of parameters and long context
- The transformer architecture is what made this breakthrough possible
- Self-attention mechanisms allow them to understand relationships between words across long distances

**Key capabilities:**

These models can:
- Answer questions
- Write code
- Summarize documents
- Translate languages
- Reason through problems
- Generate creative content

But here's the key question: Does understanding language make something an agent?

**No.**

ChatGPT by itself is NOT an agent. It's a powerful language model, but it's missing critical pieces.

Let me show you what I mean..."

---

## SLIDE 44: If LLMs are the engine, prompts are how we steer them

"I love this analogy. Look at the diagram:

**Prompt → LLM**

**The Steering → The Engine**

LLMs are incredibly powerful, but they're like a car engine sitting in a garage. They have potential energy, but they need direction.

**Prompts are how we steer them.**

Think about it:
- The LLM has all this knowledge and capability
- But it doesn't know WHAT you want it to do until you tell it
- Your prompt is the instruction manual

**Why this matters:**

The quality of your prompt directly determines the quality of the output.

Same LLM, different prompts = dramatically different results.

**Bad prompt:** 'Write code'
→ LLM: 'What kind of code? For what purpose? In what language?'

**Good prompt:** 'Write a Python function that takes a list of integers and returns the sum of all even numbers. Include error handling and docstrings.'
→ LLM: *[Produces exactly what you need]*

This is where prompt engineering comes in. And it's NOT just about being polite or saying 'please.' It's about structuring your instructions so the LLM can execute precisely.

Let me show you the framework..."

---

## SLIDE 45: Prompt Engineering

"Look at this framework for effective prompt engineering. This is a game-changer.

**Four key components:**

**1. Context** - Set the stage: role, goal, plan, etc.

Example: 'You are a senior SRE reviewing a post-mortem'

This tells the LLM WHO it is and WHAT perspective to take.

**2. Structure** - Use delimiters, Markdown, or XML-like tags

Example shown on screen:
```
## Role
You are a senior SRE reviewing a post-mortem.

## Task
Summarize the root cause and recommend 3 action items.

## Input
{incident report}

## Constraints
- Max 200 words
- Respond in JSON
- Use only the data provided
```

Using headers (##) organizes your prompt. The LLM can clearly see what each section is for.

**3. Constraints** - Output format, tone, edge cases

- 'Respond in JSON'
- 'Max 200 words'
- 'Use only the data provided'

Constraints prevent the LLM from going off-track or hallucinating.

**4. Iterate** - Draft, evaluate, review output, refine

Prompt engineering is iterative. Your first prompt is rarely perfect.
- Run it
- See what you get
- Adjust
- Run again

**The power of structure:**

Compare these:

**Unstructured:** 'Hey can you help me figure out why this incident happened and what we should do about it?'

**Structured:** Uses the framework above with clear sections

The structured approach gets you:
- More accurate responses
- Consistent formatting
- Fewer hallucinations
- Results you can actually use in production

This is how you turn LLMs from toys into tools."

---

## SLIDE 46: Types of Prompts

"Let me show you the evolution of prompting techniques with REAL examples you can copy and use.

**Zero Shot:**
- No examples provided
- Just give the task directly
- The LLM figures it out from its training

**Real Zero Shot Prompt:**
```
Classify the sentiment of this review as positive, negative, or neutral:
"The product arrived late but works perfectly."
```

That's it! No examples. The LLM uses its training to understand what sentiment classification means.

---

**One Shot:**
- Provide ONE example to show the format
- Helps the LLM understand exactly what you want

**Real One Shot Prompt:**
```
Extract the person's name and company from the text.

Example:
Input: "John Smith works as an engineer at Microsoft."
Output: {"name": "John Smith", "company": "Microsoft"}

Now extract from:
"Sarah Johnson is the CEO of Tesla."
```

See? You gave it ONE example showing the format, then asked it to do the same for new text.

---

**Few Shot:**
- Provide 2-5 examples
- The LLM learns the pattern from your examples
- More reliable than zero shot

**Real Few Shot Prompt:**
```
I want you to categorize customer support tickets into: BILLING, TECHNICAL, or ACCOUNT.

Examples:
Input: "I was charged twice for my subscription."
Output: BILLING

Input: "The app crashes when I try to login."
Output: TECHNICAL

Input: "I forgot my password and can't reset it."
Output: ACCOUNT

Input: "How do I update my credit card?"
Output: BILLING

Now categorize this:
"The dashboard is not loading any data."
```

Notice: The LLM now has a clear pattern to follow based on 4 examples.

---

**Chain of Thought (CoT):**
- Ask the LLM to show its reasoning step by step
- This DRAMATICALLY improves accuracy on reasoning tasks
- Just add: "Let's think step by step" or "Show your work"

**Real Chain of Thought Prompt:**
```
Question: A store sells notebooks at $3 each. If I buy 5 notebooks and pay with a $20 bill, how much change do I get?

Let's solve this step by step:
```

**LLM Response:**
```
Step 1: Calculate total cost of notebooks
- 5 notebooks × $3 = $15

Step 2: Calculate change
- Amount paid: $20
- Cost: $15
- Change = $20 - $15 = $5

Answer: You get $5 in change.
```

**Why it works:** By forcing the LLM to show steps, it catches its own mistakes.

---

**Chain of Thought - Self Consistency (CoT-SC):**
- Generate multiple reasoning paths
- Pick the most consistent answer
- Best for high-stakes decisions

**Real CoT-SC Prompt:**
```
Solve this problem using 3 different approaches and tell me which answer appears most often:

Question: A train travels 120 miles in 2 hours, then 180 miles in 3 hours. What is its average speed for the entire trip?

Approach 1: [Think step by step using total distance / total time]
Approach 2: [Think step by step using weighted average]
Approach 3: [Think step by step using segments then combining]

Final Answer: [Report the most consistent answer]
```

**LLM Response:**
```
Approach 1: Total distance = 300 miles, Total time = 5 hours, Average = 60 mph
Approach 2: (120/2 × 2 + 180/3 × 3) / 5 = 60 mph
Approach 3: Segment averages don't directly give overall average, but total distance/time = 60 mph

Most consistent answer: 60 mph ✓
```

---

**Tree of Thoughts:**
- Explore multiple reasoning paths like a tree
- Evaluate each branch
- Backtrack if needed
- Most sophisticated approach

**Real Tree of Thoughts Prompt:**
```
I need to plan a 3-day trip to Paris with a $500 budget. Help me explore different options:

Consider these decision branches:
1. Accommodation options:
   - Budget hostel ($30/night)
   - Mid-range hotel ($100/night)
   - Luxury hotel ($200/night)

2. For each accommodation choice, evaluate:
   - Remaining budget for food and activities
   - Location quality vs price trade-off
   - Impact on overall trip experience

3. For the top 2 most promising paths, create a detailed itinerary

4. Compare final options and recommend the best one

Show your decision tree and explain why you chose each branch.
```

**LLM Response:**
```
Branch 1: Budget Hostel
- Cost: $90 for 3 nights
- Remaining: $410
- Can afford: Good restaurants ($40/day) + attractions ($50/day)
- Assessment: High value ✓

Branch 2: Mid-range Hotel
- Cost: $300 for 3 nights
- Remaining: $200
- Can afford: Budget meals ($20/day) + limited attractions
- Assessment: Tight budget ✗

Branch 3: Luxury Hotel
- Cost: $600 for 3 nights
- Over budget immediately ✗

Exploring Branch 1 further:
[Detailed itinerary for hostel option]

Recommendation: Budget hostel option maximizes experiences within budget.
```

---

**When to use each:**

- **Zero Shot:** Quick tasks, well-known operations (translation, basic classification)
- **One/Few Shot:** When you need specific formatting or the task is unusual
- **Chain of Thought:** Math, logic, reasoning, anything where errors can compound
- **CoT-SC:** High-stakes decisions where you need maximum accuracy
- **Tree of Thoughts:** Complex planning, optimization problems, multi-step decisions

**Pro tip:** Start with the simplest approach (zero shot). Only add complexity if you're not getting good results.

The more complex your problem, the more sophisticated your prompting technique should be."

---

## SLIDE 47: Limitations of LLMs

"Before we talk about what LLMs can do as agents, we need to be brutally honest about what they CAN'T do by themselves.

Look at this diagram showing four major limitations:

**1. No Fresh Knowledge**

**Trained on a snapshot of the world. Can't access your docs, your databases, or what happened today.**

Example: If you ask ChatGPT 'What's the weather in Paris right now?' it will say 'I don't have access to real-time weather data.'

The LLM was trained on data with a cutoff date. GPT-4's training data ends around April 2023. It knows NOTHING about what happened after that unless you tell it.

It can't access:
- Your company's internal documents
- Your database
- Today's news
- Current stock prices
- Real-time weather

**2. No Memory**

**Every conversation starts from zero. No recall of past interactions or accumulated context.**

Close the ChatGPT window and open a new one? It has ZERO memory of what you just discussed.

Example:
- Session 1: 'My name is John, I'm working on a Python project for data analysis'
- *[Close window]*
- Session 2: 'What's my name?' → ChatGPT: 'I don't know your name'

It forgot EVERYTHING. You have to re-explain context every single time.

**3. No Actions**

**Generates text, not outcomes. Can't call an API, run a query, or update a ticket.**

LLMs can describe how to do things, but they can't DO things.

Example: 'Can you email this report to my manager?'
→ ChatGPT: 'I can't send emails, but here's a template you can use...'

It can't:
- Call APIs
- Execute code
- Query databases
- Send emails
- Update tickets
- Browse the web

**4. Hallucinations**

**Confidently wrong. No built-in way to verify or say 'I don't know.'**

LLMs make things up and present them as facts.

Example: I asked ChatGPT about a Python library function. It gave me detailed documentation, syntax, parameters, code examples. I tried it. **The function doesn't exist.** It fabricated everything.

And it was SO confident. No hesitation. No 'I'm not sure.' Just pure hallucination.

This happens constantly with:
- Code that doesn't work
- Citations to papers that don't exist
- Historical 'facts' that are wrong
- API endpoints that aren't real

**So here's the critical question:**

If LLMs have all these limitations, how do we turn them into agents that can actually DO things?

The answer? We give them what they're missing..."

---

## SLIDE 48: What if we gave the LLM tools, memory, and a loop?

"This is the breakthrough question.

Look at this slide: **'What if we gave the LLM tools, memory, and a loop?'**

Let that sink in.

LLMs by themselves have limitations. But what if we AUGMENT them?

What if we give them:
- **Tools** to take actions (call APIs, query databases, send emails)
- **Memory** to remember context across conversations
- **A loop** to iterate until the problem is solved

This is how we transform a language model into an agent.

Think about it:
- LLM provides the BRAIN (reasoning, understanding, decision-making)
- Tools provide the HANDS (ability to take action)
- Memory provides CONTINUITY (context across interactions)
- Loop provides PERSISTENCE (keeps going until done)

**This combination changes everything.**

Instead of:
- User asks question → LLM responds → Done

We get:
- User gives goal → Agent plans → Agent acts → Agent checks result → Agent adjusts → Agent acts again → ... → Goal achieved

Let me show you exactly how this works..."

---

## SLIDE 49: Agent = loop(prompt + tool + memory)

"Look at this formula on the screen. This is THE definition of a modern AI agent:

**Agent = loop(prompt + tool + memory)**

And look at this diagram showing the AI Agent cycle:

**PERCEIVE** (Look at the world)
↓
**THINK** (Decide what to do)
↓
**ACT** (Take action)
↓
**LEARN** (Did that work out? How could it be better next time?)
↓ (Loop back to PERCEIVE)

Let me break down each component:

**Prompt:**
- Defines the behavior
- 'You are a helpful assistant that can access weather data and recommend whether to bring an umbrella'
- This is the agent's identity and instructions

**Tools:**
- Enable actions
- APIs, search, code execution, databases
- 'get_weather(city)' - a function the agent can call
- 'send_email(to, subject, body)' - another function

**Memory:**
- Remembers between turns
- Conversation history
- 'User lives in Paris' - remembered for next time

**Loop:**
- Decides what to do next
- Call a tool, evaluate the result, repeat until done
- 'Did I get the weather? Yes. Do I have enough info to answer? Yes. Respond to user.'

**An agent allows LLM to use tools, remember context, and decide what to do next.**

This is not just ChatGPT. This is ChatGPT with superpowers.

Let me show you what agents can actually do..."

---

## SLIDE 50: Agents with Tools

"Now let's talk about what tools actually give agents. This is where it gets powerful.

**Enables the LLM to retrieve information from APIs, databases, and knowledge repositories.**

Example: Instead of hallucinating about today's weather, the agent calls OpenWeatherMap API and gets REAL data.

**Allows the LLM to execute actions in external systems, such as sending emails or querying web services.**

Example: Agent can send a Slack message, create a Jira ticket, or trigger a deployment pipeline.

**Performs specialized functions like code execution, calculations, or document processing based on the task at hand.**

Example: Agent can run Python code to analyze a CSV, or parse a PDF document.

**Enhances responses by dynamically selecting the right tool for the given task, improving accuracy and efficiency.**

Example: User asks 'What's the sentiment of this customer review?' Agent picks the sentiment analysis tool, not the weather tool.

**Look at this diagram on screen:**

You have a Query coming in.
↓
Agent (Pick the right tool at every step)
↓
Four tools available:
- Tool 1: Extraction QA Pipeline
- Tool 2: Websearch with APIs
- Tool 3: Generative QA with LLM
- Tool 4: Document Search Pipeline
↓
Answer ✓

**The agent intelligently CHOOSES which tool to use based on the question.**

This is fundamentally different from hardcoded workflows. The agent REASONS about which tool to use.

Let me show you a concrete example..."

---

## SLIDE 51: Agent's way of solving problems - Example

"Alright, this is one of my favorite examples because it's simple but shows EVERYTHING.

**The Question:** 'I am in in Paris today. Should I carry an umbrella?'

Look at the flow on this diagram:

**Step 1:** You → Agent
- 'I am in in Paris today. Should I carry an umbrella?'

**Step 2:** Agent → LLM
- User message + prompt + tool definitions
- Agent: 'I need to check the weather in Paris. I have a weather tool available. Let me use it.'

**Step 3:** LLM returns
- `get_weather("Paris")`
- The LLM decided to call a function!

**Step 4:** Agent → Weather API
- Executes: `get_weather("Paris")`

**Step 5:** API returns
- Tool result: 'Paris, 14°C, rain expected'

**Step 6:** Agent → LLM (again!)
- Here's what the weather API returned. Now what should I tell the user?

**Step 7:** LLM responds
- 'Yes, bring an umbrella! ☂️ Rain is expected today.'

**Step 8:** Agent → You
- 'Yes, bring an umbrella! ☂️'

**Look at what just happened:**

The agent went through MULTIPLE steps autonomously:
1. Understood the question required weather data
2. Identified the right tool (weather API)
3. Called the tool
4. Got the result
5. Reasoned about the result
6. Generated a response

This is the agent loop in action. The user asked ONE question, but the agent took MULTIPLE actions to answer it correctly.

Let me show you the architecture behind this..."

---

## SLIDE 52: Agent's way of solving problems

"Look at this flowchart. This shows the full problem-solving process for an AI agent.

**The AI Agent Problem-Solving Process:**

**1. AI Agent Initiation**
- AI agent begins its task
- Example: 'Help the user decide about the umbrella'

**2. Problem Identification**
- AI agent identifies the problem
- Example: 'User needs to know if it will rain in Paris'

**3. Problem Breakdown**
- AI agent breaks down the problem
- Example: 'I need weather data. I need to interpret that data. I need to give a recommendation.'

**4. Planning Phase**
- AI agent plans each step
- Example: 'Step 1: Call weather API. Step 2: Check if rain is expected. Step 3: Recommend accordingly.'

**5. Execution of Plan**
- AI agent executes the plan
- Example: Calls the API, gets data

**6. Dynamic Adjustment**
- AI agent adjusts if needed
- Example: 'API returned an error? Try a different API. API returned ambiguous data? Ask for clarification.'

**The key difference from traditional programs:**

Traditional program:
- Fixed sequence of steps
- If something breaks, it fails

AI Agent:
- Dynamic sequence of steps
- If something breaks, it adapts
- Continuously evaluates: 'Did that work? What should I do next?'

This is why agents can handle messy, real-world problems. They don't just execute a script - they THINK through the problem.

---


## SLIDE 53: What is an LLM?

"Now let's dive deeper into what LLMs actually are under the hood.

Look at this slide. Two key concepts:

**Next-Token Prediction:** At their core, LLMs are probabilistic engines designed to predict the next token in a sequence. They are trained on vast datasets comprising a significant portion of the public internet.

Think about it like this: You type 'The sky is...' and the LLM predicts 'blue' is the most likely next word based on billions of examples it saw during training.

It's not magic - it's statistics at an incredible scale.

**Pattern Matching:** They don't 'know' facts in the way humans do. Instead, they recognize statistical relationships between tokens (words or sub-words) to generate coherent text.

Example: The LLM has seen millions of sentences like 'Paris is the capital of France' during training. So when you ask 'What's the capital of France?', it recognizes the pattern and generates 'Paris'.

But here's the thing - it's not looking up a fact in a database. It's recognizing a pattern.

This is why LLMs can be incredibly fluent but sometimes confidently wrong. They're predicting what SHOULD come next based on patterns, not what IS true.

Understanding this is crucial for understanding both their power and their limitations."

---

## SLIDE 54: The Engine: Transformers

"So what makes modern LLMs possible? The answer is: **Transformers**.

**The breakthrough that made modern LLMs possible is the Transformer architecture (2017).**

Before transformers, we had RNNs (Recurrent Neural Networks). They processed text word by word, sequentially. Like reading a book one word at a time without looking ahead.

**Its key innovation is 'Self-Attention'.**

This allows the model to weigh the importance of different words in a sentence regardless of their distance from each other, enabling it to learn context over long passages of text.

Look at this diagram showing the attention mechanism.

Here's what's revolutionary: When processing the word 'it' in a sentence like 'The dog ate its food because it was hungry', the attention mechanism can look BACK at 'dog' and understand that 'it' refers to the dog, not the food.

It can do this across hundreds or thousands of tokens simultaneously.

**Key insight:** Transformers can process entire sentences or paragraphs in parallel, not just word by word. This makes them:
- Much faster to train
- Better at understanding context
- Capable of handling longer text

This architecture is what powers GPT, Claude, Gemini - every modern LLM.

The 'T' in GPT literally stands for 'Transformer' - Generative Pre-trained Transformer.

Without transformers, we wouldn't have the LLMs we have today."

---

## SLIDE 55: Calling LLMs via client libs

"Now let's talk about the practical side - how do you actually build with LLMs?

**Colab Notebook:** https://colab.research.google.com/drive/1wvbvCG_GdhMCxwLuZfc9Ch4XvHpdkJVJ

This notebook demonstrates two strategies for connecting to LLMs programmatically.

---

**Strategy 1: The 'Siloed' Approach (Official SDKs)**

Each major AI lab releases its own Python SDK. Let me show you each one:

**1. OpenAI (GPT-4, GPT-4o-mini)**

The Standard: OpenAI's format has effectively become the industry standard.

```python
from openai import OpenAI
client = OpenAI(api_key="your-api-key")

response = client.chat.completions.create(
    model="gpt-4-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is an agent?"}
    ],
    temperature=0.7
)

print(response.choices[0].message.content)
```

**Key Features:**
- Simple message history list format
- Industry standard API format
- Best for accessing GPT-4o, GPT-4-Turbo

**2. Anthropic (Claude 3.5 Sonnet, Claude Haiku)**

The Difference: Anthropic uses a slightly different syntax.

```python
from anthropic import Anthropic
client = Anthropic(api_key="your-api-key")

message = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "What is an agent?"}
    ]
)

print(message.content[0].text)
```

**Key Features:**
- Known for large context windows (100K+ tokens)
- Excellent safety and instruction following
- Uses `max_tokens` instead of OpenAI's `max_completion_tokens`

**3. Google Gemini (Gemini 2.5 Flash, Pro)**

The Difference: Google's API is distinct - creates a GenerativeModel object.

```python
import google.generativeai as genai
genai.configure(api_key="your-api-key")

model = genai.GenerativeModel('gemini-2.5-flash')
response = model.generate_content("What is an agent?")

print(response.text)
```

**Key Features:**
- Native multimodal capabilities (video/image analysis)
- Very large context windows
- Integrated with Google services

---

**Strategy 2: The Unified Approach (OpenRouter)**

Now here's where it gets interesting. What if you don't want to learn 3 different SDKs?

**What is OpenRouter?**

OpenRouter is a unified interface (an aggregator) that allows you to access almost ANY major LLM using a SINGLE standard API format (specifically, the OpenAI format).

**Why use it?**

✅ **One SDK:** You only need the `openai` Python library to access Claude, Llama, Mistral, everything
✅ **Model Shopping:** Switch models just by changing a string without rewriting code
✅ **Cost:** They charge standard provider prices (sometimes even less for open models)

**Example - Accessing Claude via OpenRouter:**

```python
from openai import OpenAI

# Use OpenRouter endpoint with OpenAI SDK
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="your-openrouter-key"
)

# Access Claude using OpenAI format!
response = client.chat.completions.create(
    model="anthropic/claude-3-opus",
    messages=[
        {"role": "user", "content": "What is an agent?"}
    ]
)

print(response.choices[0].message.content)
```

**Switch to Llama? Just change the model string:**

```python
response = client.chat.completions.create(
    model="meta-llama/llama-3-70b",  # Different model, same code!
    messages=[
        {"role": "user", "content": "What is an agent?"}
    ]
)
```

**Key Takeaway:**

For production agents, you have two approaches:
- **Direct SDKs:** More control, model-specific features
- **OpenRouter:** Easier model switching, unified interface, great for experimentation

**In this course, we'll use both approaches depending on the project.**

The complexity isn't in calling the API - it's in:
- Structuring prompts effectively
- Managing conversation history
- Integrating tools
- Handling errors and retries

**That's what we'll build together in the hands-on sessions.**"

---

## SLIDE 56: Question: What LLM is used in what scenario...

"This is a good moment for discussion. Let me pose a question to all of you:

**What LLM should you use in what scenario?**

Think about this:

**GPT-4:**
- Most capable OpenAI model
- Best for complex reasoning, coding, analysis
- Slower, more expensive
- When to use: Complex tasks where accuracy matters more than speed

**GPT-3.5:**
- Faster, cheaper
- Still very capable for most tasks
- When to use: High-volume, simpler tasks, chatbots, classification

**Claude (Anthropic):**
- Strong at long context (100K+ tokens)
- Excellent at instruction following
- Very safe, less likely to generate harmful content
- When to use: Processing long documents, safe content generation, careful analysis

**Gemini (Google):**
- Multimodal (text, images, video)
- Integrated with Google services
- When to use: Tasks involving images, Google Workspace integration

**Local/Open Source (Llama, Mistral):**
- Run on your own hardware
- Complete data privacy
- No per-token costs
- When to use: Sensitive data, high volume, specialized fine-tuning

**Discussion question for the class:**

*'If you were building a customer support chatbot that needs to read 50-page legal documents and answer questions about them, which LLM would you choose and why?'*

Let's hear some thoughts. Anyone?

*[Pause for discussion]*

Great answers. The key is: there's no single 'best' LLM. It depends on your requirements:
- Budget
- Speed needs
- Data sensitivity
- Task complexity
- Context length
- Multimodal needs

Let's take a quick break and come back to build our first agent!"

---

## SLIDE 57: Break Time!

"Alright everyone, we've covered a LOT in this section.

We went from understanding what LLMs are, to their limitations, to how agents solve those limitations.

**Let's take a 15-minute break.**

When we come back, we're going to get hands-on. We'll write actual code to build agents.

---

## SLIDE 58: Today's Agenda

"Alright everyone, welcome back from the break! Let's quickly review where we are in today's agenda.

Look at this slide showing our four sections with breaks in between:

**Section 1:** Reflex & Goal-based agents ✓ (DONE!)
- We covered simple reflex agents, model-based agents, and goal-based agents

**BREAK** ✓

**Section 2:** Utility agents and Intro to LLMs ✓ (DONE!)
- We covered utility-based agents and introduced Large Language Models

**BREAK** ✓

**Section 3:** LLM-Based Agents ⭐ (WE ARE HERE!)
- This is where we are now - diving deep into how LLMs become agents
- This is the most exciting part!

**We're in Section 3 now - the core of modern agentic AI. This is where everything comes together.**

Let's dive in!"

---

## SLIDE 59: Enter the Agent

"Now we get to the transformation moment.

**Enter the Agent**

**Giving the 'Brain' a Body and Tools**

Think about it: LLMs are incredibly smart. They can reason, understand language, write code, analyze complex problems.

But they're trapped. Like a brain in a jar.

They can THINK, but they can't DO.

**What if we gave that brain:**
- A body (ability to execute actions)
- Tools (APIs, databases, code execution)
- Memory (to remember past interactions)
- A loop (to keep working until the task is done)

**That's what an agent is.**

An agent is an LLM that's been unleashed. It's no longer just a text generator - it's an autonomous system that can:
- Access real-time information
- Execute code
- Call APIs
- Remember context
- Take actions
- Keep working until the goal is achieved

**This is the bridge from AI tools to Agentic AI.**

Let me show you what this looks like..."

---

## SLIDE 60: What is an AI Agent?

"Let me give you the formal definition.

**What is an AI Agent?**

**LLM + Action**

An agent is a system that uses an LLM as its computational 'brain' but, instead of just outputting text, it is connected to external interfaces ('body').

Look at the diagram showing different types of agents:

**Gaming Agents:**
- Can play games autonomously
- Make strategic decisions

**Stock Market Trading Agents:**
- Analyze market data
- Execute trades

**Content Writing Agents:**
- Research topics
- Generate articles
- Fact-check and revise

**Customer Service Agents:**
- Answer questions
- Access knowledge bases
- Escalate when needed

**Robots:**
- Navigate physical spaces
- Manipulate objects

**Personal Assistants:**
- Schedule meetings
- Send emails
- Book reservations

**What do all these have in common?**

They all have:
1. An LLM that can reason and understand
2. The ability to TAKE ACTIONS in the real world

Instead of just outputting text, an agent can execute code, browse the web, and interact with software APIs to accomplish its goal autonomously.

**The key word here is 'autonomously'.**

You give it a goal, and it figures out how to achieve it. You don't tell it every step."

---

## SLIDE 61: The Cognitive Engine

"Let me break down how this actually works inside an agent.

**The Cognitive Engine**

**More Than Just Text**

In an agentic system, the LLM stops being a simple chatbot and becomes the **Reasoning Core.**

Look at this diagram showing the LLM at the center with all these connections:

**The LLM acts as the central controller that:**

**Parses user intent from ambiguous natural language**
- You say: 'Book me a flight to New York'
- LLM understands: User wants flight booking, destination is New York, need to check dates/preferences

**Decomposes complex problems into steps**
- Breaking down 'Plan my vacation' into: research destinations, check weather, book flights, reserve hotels, create itinerary

**Synthesizes data returned from those tools**
- Gets weather data, flight prices, hotel availability
- Combines all this information into a coherent recommendation

**This is fundamentally different from traditional software:**

Traditional software:
```
if (action == "book_flight") {
    call_flight_api()
}
```

Agentic system:
```
LLM: "User wants to travel. I should:
1. Ask about dates
2. Check their budget
3. Search for flights
4. Compare options
5. Book the best one"
```

**The LLM is making DECISIONS at each step, not following a fixed script.**

This flexibility is what makes agents so powerful - and so different from traditional automation."

---

## SLIDE 62: The ReAct Loop

"Welcome back! Now we're getting to the MOST IMPORTANT pattern in modern agentic AI.

If you remember ONE thing from this entire class, remember this:

**The ReAct Loop: Reasoning + Acting**

This is how virtually EVERY modern LLM agent works. OpenAI's GPT agents, Anthropic's Claude agents, LangChain, AutoGPT - they all use variations of this pattern.

**The standard loop for modern agents is ReAct:**

Let me break it down:

**Thought:** The agent analyzes the request.
**Action:** It decides which tool to call.
**Observation:** It reads the tool's output.
**Repeat:** It updates its thought process and continues until the final answer is found.

**This cycle continues until the final answer is found.**

Let me walk you through this with a detailed example.

**User Query:** 'Book me a flight from San Francisco to New York for next Monday under $300.'

**Iteration 1:**
- **THOUGHT:** 'I need to search for flights from SFO to NYC for next Monday. Let me use the flight search tool.'
- **ACTION:** `search_flights(origin='SFO', destination='NYC', date='2025-02-17', max_price=300)`
- **OBSERVATION:** Returns: `[Flight1: $285, Flight2: $420, Flight3: $275]`

**Iteration 2:**
- **THOUGHT:** 'I found flights under $300: Flight1 ($285) and Flight3 ($275). I should book the cheaper one.'
- **ACTION:** `book_flight(flight_id='Flight3')`
- **OBSERVATION:** Returns: `{'status': 'success', 'confirmation': 'XYZ123'}`

**Iteration 3:**
- **THOUGHT:** 'Flight successfully booked. I can now provide the final answer.'
- **FINAL ANSWER:** 'I've booked you a flight from San Francisco to New York for Monday, February 17th. The cost is $275, and your confirmation number is XYZ123.'

**This is the ReAct loop in action.**

Notice: The agent didn't do everything in one step. It LOOPED. It thought, acted, observed, and repeated until the task was complete.

This is incredibly powerful because it means the agent can:
- Handle multi-step tasks
- Recover from errors
- Adapt based on observations
- Keep going until success"

---

## SLIDE 63: Anatomy of an Agent

"Now let me show you the internal architecture of a functional agent.

**Anatomy of an Agent**

**A functional agent consists of four main modules:**

Look at this diagram showing the Agent Core at the center connected to four modules:

**1. The Brain (LLM):** The decision-maker.
- This is the LLM doing all the reasoning
- Decides what to do next based on the current state

**2. Planning:** Breaking down complex goals.
- Takes a big task like 'Plan a vacation' and breaks it into steps
- Sequences actions in the right order

**3. Memory:** Storing history and context.
- Remembers what happened earlier in the conversation
- Stores important facts and context
- Can recall relevant information when needed

**4. Tools:** Capabilities to interact with the world.
- Weather API
- Database queries
- Web search
- Email sending
- Code execution
- Any external capability

**Flow:**
User Request → Agent Core → (Coordinates with Planning Module, Memory Module, Tool(s)) → Output

**The Agent Core orchestrates everything:**
- Receives user request
- Consults memory for context
- Uses planning to break down the task
- Calls appropriate tools
- Synthesizes the results
- Returns output

**This architecture is based on NVIDIA's agent framework.**

Reference: https://developer.nvidia.com/blog/introduction-to-llm-agents/

**Key insight:** The agent is not just the LLM. It's a complete system where the LLM is the brain, but it needs the other modules to function effectively.

Without planning, it can't handle complex tasks.
Without memory, every interaction starts from zero.
Without tools, it can't take actions.

**Together, these four modules create a truly autonomous agent.**"

---

## SLIDE 64: The Three Pillars of Agency

"Let me simplify this even further. Every agent fundamentally needs three things.

**The Three Pillars of Agency**

Look at these three images representing the core capabilities:

**1. Planning**
*[Image shows someone at a whiteboard with complex diagrams]*

**Decomposing goals into sub-tasks (Chain of Thought).**

Without planning, the agent can't handle complex, multi-step problems. Planning gives the agent the ability to think ahead.

Example:
- Goal: 'Plan a company retreat'
- Planning breaks it down: Research locations → Check budgets → Get team preferences → Book venue → Arrange transportation → Plan agenda

**2. Memory**
*[Image shows a person thinking/remembering]*

**Vector Databases allow long-term recall of past events.**

Without memory, every conversation starts from scratch. Memory gives the agent continuity and context.

Example:
- You tell the agent: 'I'm allergic to peanuts'
- Two weeks later, you ask: 'Suggest a restaurant'
- Agent remembers your allergy and filters recommendations accordingly

**3. Tools**
*[Image shows a database/server infrastructure]*

**APIs, Calculators, and Search Engines extend capability.**

Without tools, the agent is stuck in its training data. Tools give the agent the ability to access real-time information and take actions.

Example:
- Weather API → Gets current weather
- Calculator → Performs precise computations
- Web search → Accesses latest information
- Email API → Sends messages

**Think of it like this:**

An LLM alone is like a brilliant professor locked in a library from 2023.

**Add Planning:** Now they can break down complex problems systematically.
**Add Memory:** Now they remember what you told them yesterday.
**Add Tools:** Now they can make phone calls, access the internet, run calculations.

**That's an agent.**"

---

## SLIDE 65: Extending Capabilities with Tools

"Let's dive deeper into tools because this is where agents become truly powerful.

**Extending Capabilities with Tools**

Look at these three categories of tools:

**1. Web Browsing**
*[Icon showing a web browser window]*

**Accessing real-time information, news, and live data that is not in the training set.**

Example use cases:
- 'What's the weather in Tokyo right now?'
- 'What are today's top news stories?'
- 'Find me the latest research papers on quantum computing'

The agent can browse the web, scrape content, and return up-to-date information.

**2. Code Execution**
*[Icon showing code editor]*

**Writing and running Python scripts to perform complex math or data analysis.**

Example use cases:
- 'Analyze this CSV file and create visualizations'
- 'Calculate the compound interest for these investment scenarios'
- 'Run a linear regression on this dataset'

The agent can write Python code, execute it in a sandbox, and return the results.

**3. External APIs**
*[Icon showing database servers]*

**Interacting with services like Slack, Jira, or SQL databases to perform actions.**

Example use cases:
- 'Send a summary of this meeting to #engineering on Slack'
- 'Create a Jira ticket for this bug'
- 'Query our customer database for users who signed up last month'

The agent can authenticate with external services and perform real actions.

**Why this matters:**

Without tools, an LLM can only TALK about doing things.

With tools, an agent can ACTUALLY DO things.

**This is the difference between:**
- 'Here's how you could check the weather...' (LLM)
- *[Actually checks weather API]* 'It's 72°F and sunny in Paris' (Agent)

**In the projects we build in this course, you'll implement multiple tools and see how agents intelligently choose which tool to use for each task.**"

---

## SLIDE 66: Memory: Short vs. Long Term

"Now let's talk about memory, because this is crucial for agents that work over extended periods.

**Memory: Short vs. Long Term**

**Two types of memory:**

**Short-Term (Context)**
*[Left panel with blue background]*

**The 'RAM' of the Agent.**

This is limited by the model's context window (e.g., 128k tokens). It holds the immediate conversation history, the current prompt, and recent tool outputs.

**Limitation: Cleared when the session ends.**

Example:
- During a single conversation, the agent remembers everything you've said
- You: 'My name is Sarah'
- *[10 messages later]*
- Agent: 'Of course, Sarah, I remember you mentioned that earlier'

But close the window and reopen it? Gone.

**Long-Term (Vector Store)**
*[Right panel with green background]*

**The 'Hard Drive' of the Agent.**

Uses Vector Databases (RAG) to store vast amounts of information. The agent retrieves only relevant 'memories' based on semantic similarity to the current task.

**Benefit: Infinite persistence.**

Example:
- Six months ago, you told an agent: 'I prefer morning meetings'
- Today, you ask: 'Schedule a meeting with my team'
- Agent searches vector store, finds your preference, schedules it in the morning

**This is implemented using RAG (Retrieval-Augmented Generation):**

1. Store memories as embeddings in a vector database
2. When agent needs to remember something, convert the query to an embedding
3. Search for similar embeddings in the vector store
4. Retrieve relevant memories
5. Add them to the agent's context

**Real-world application:**

Imagine a customer support agent:
- **Short-term memory:** Current conversation with a customer
- **Long-term memory:** All past interactions with this customer, their purchase history, past issues

The agent can say: 'I see you had a similar issue last month that was resolved by updating your software. Would you like to try that again?'

**This combination of short and long-term memory makes agents feel intelligent and personalized.**"

---

## SLIDE 67: Planning & Reasoning

"Now let me show you two advanced techniques that make agents even more powerful:

**1. Chain of Thought: Stepping through logic**

Agents cannot solve complex tasks in one shot. They need to break problems down.

Example problem: 'If a train leaves Chicago at 3pm going 60 mph, and another train leaves New York at 4pm going 80 mph, when do they meet?'

**Without Chain of Thought:**
LLM might just guess: 'They meet at 6pm' (wrong)

**With Chain of Thought:**
LLM thinks step-by-step:
- 'First, I need to know the distance between Chicago and New York: ~790 miles'
- 'Train 1 travels for 1 hour before Train 2 starts: 60 miles'
- 'Remaining distance: 730 miles'
- 'Combined speed: 60 + 80 = 140 mph'
- 'Time to meet: 730 / 140 = 5.2 hours after Train 2 starts'
- 'Train 2 starts at 4pm, so they meet at 9:12pm' (correct)

By forcing the agent to think step-by-step, accuracy goes WAY up.

**2. Reflection: Reviewing past actions**

This is where the agent looks back at what it did and asks: 'Did that work? Should I try something else?'

Example:
- **ACTION:** Call API with parameter X
- **OBSERVATION:** Error: 'Invalid parameter format'
- **REFLECTION:** 'The API expected JSON but I sent a string. Let me try again with proper formatting.'
- **ACTION:** Call API with proper JSON
- **OBSERVATION:** Success!

Without reflection, the agent would just fail and give up. With reflection, it can LEARN from errors and try again.

This makes agents much more robust in real-world scenarios where things don't always work the first time."

---

## SLIDE 68: The Future: Multi-Agent Systems

"Before we get to implementation, I want to show you where this is all heading.

**The Future: Multi-Agent Systems**

Look at these three concepts:

**1. Specialization**
*[Icon showing people with gears]*

**Instead of one generalist, swarms of specialized agents (Coder, Designer, Writer) will collaborate.**

Think about how companies work:
- You don't have one person doing everything
- You have specialists: engineers, designers, marketers, legal, finance
- They collaborate on projects

Multi-agent systems work the same way:
- **Coder Agent:** Specialized in writing and debugging code
- **Designer Agent:** Specialized in UI/UX and visual design
- **Writer Agent:** Specialized in documentation and content
- **QA Agent:** Specialized in testing and finding bugs

For a project like 'Build a landing page':
- Designer agent creates the mockup
- Coder agent implements it
- Writer agent creates the copy
- QA agent tests it

**Each agent is an expert in its domain.**

**2. Orchestration**
*[Icon showing connected nodes]*

**'Manager' agents will break down huge projects and assign tasks to 'worker' agents.**

Like a project manager:
- Receives high-level goal: 'Launch new product'
- Breaks it down into tasks
- Assigns each task to the right specialist
- Coordinates between agents
- Ensures everything comes together

**3. Autonomy**
*[Icon showing infinity symbol]*

**Agents will run continuously in the background, optimizing workflows without human input.**

Imagine:
- Agents monitoring your systems 24/7
- Detecting issues before they become problems
- Auto-generating reports
- Optimizing processes
- Self-healing systems

**This is already happening:**
- AutoGPT: Multiple agents working together
- Microsoft's AutoGen: Agent collaboration framework
- CrewAI: Multi-agent orchestration platform

**Within 2-3 years, most software development teams will include AI agents as permanent team members.**"

---

## SLIDE 69: You've learned what agents can do. Now let's learn how to design them for real-world applications.

"Perfect transition point. We've covered the theory. Now let's get practical.

**You've learned what agents can do.**

**Now let's learn how to design them for real-world applications.**

Everything so far has been conceptual:
- What agents are
- How they work
- Why they're powerful

**Now we're shifting gears:**

From theory → To practice
From concepts → To patterns
From understanding → To building

**In the next section, I'm going to show you:**
- Design patterns for building robust agents
- The routing pattern (critical for complex agents)
- How to architect multi-step agent workflows
- Best practices from production systems

**This is the bridge between knowing what agents are and actually building them.**

Let's dive into agentic design patterns!"

---

## SLIDE 70: Agentic design Pattern

"Here's the framework for building production-grade agents.

**Agentic Design Patterns**

These are the **building blocks for LLM systems** that go beyond single prompt-response interactions.

They structure reasoning, decisions, tools, and control flow to replace hard-coded logic—enabling scalable, adaptable systems from basic assistants to autonomous agents.

Look at this diagram showing the design pattern hierarchy:

**Design Patterns** (at the top)
↓
Five core patterns:

**1. Reflection Pattern**
*[Icon showing circular arrows]*
- Agent reviews and improves its own output

**2. Routing Pattern**
*[Icon showing branching paths]*
- Agent decides which path to take

**3. Tool Use Pattern**
*[Icon showing wrench/tools]*
- Agent selects and uses external tools

**4. Planning Pattern**
*[Icon showing checklist]*
- Agent breaks down complex tasks

**5. Multi-Agent Pattern**
*[Icon showing multiple connected agents]*
- Multiple agents collaborate

**Why patterns matter:**

When you're building a production agent, you can't just wing it. You need proven architectural patterns.

These five patterns cover 90% of real-world agent applications:
- Customer support? Routing + Tool Use
- Research assistant? Planning + Reflection
- Complex workflows? Multi-Agent + Planning

**We're going to focus on the Routing Pattern today because it's the most fundamental.**

But know that these patterns can be combined and layered to create sophisticated agent systems."

---

## SLIDE 71: Reflection Pattern

"Let me quickly show you one powerful pattern: Reflection.

**Reflection Pattern**

**The agent reflects on its actions, decisions and reasoning. It critiques and refines its own outputs before finalizing a response.**

Look at this flow diagram:

User → Query
↓
LLM (Generate) → Initial Output
↓
Iterate? → Yes → Reflected Output → LLM (Reflect) → [loops back to Iterate]
↓ No
Response

**How it works:**

1. User asks a question
2. LLM generates an initial response
3. BEFORE sending it to the user, the LLM reflects: 'Is this answer complete? Is it accurate? Did I miss anything?'
4. LLM generates improvements
5. Repeat until satisfied
6. Send final response

**Example:**

User: 'Write a Python function to calculate Fibonacci numbers'

**Without Reflection:**
```python
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)
```

**With Reflection:**
Agent thinks: 'Wait, this is exponentially slow. Let me use memoization.'

```python
def fib(n, memo={}):
    if n in memo: return memo[n]
    if n <= 1: return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

**The agent IMPROVED its own output without human intervention.**

This pattern dramatically increases output quality, especially for:
- Code generation
- Essay writing
- Problem solving
- Complex reasoning tasks

**The cost? A few extra LLM calls. The benefit? Much higher quality results.**"

---

## SLIDE 72: Routing - A Core Pattern

"Here's one more critical pattern I want to show you:

**Routing - a core pattern for LLM-based agents.**

As your agent gets more sophisticated, it might have DOZENS of tools available. You don't want it randomly trying all of them.

**Routing is like having a smart dispatcher.**

Example: You're building a customer support agent. It has tools for:
- Billing questions
- Technical support
- Account management
- Returns and refunds

User asks: 'I was charged twice for my last order.'

A naive agent might try:
- Technical support tool (wrong)
- Account management tool (wrong)
- Billing tool (correct!)

That wastes time and API calls.

A routing agent would:
1. Analyze the query: 'This is about billing'
2. Route to billing specialist agent
3. Get answer immediately

**Routing improves:**
- Speed (no wasted tool calls)
- Accuracy (right specialist for the job)
- Cost (fewer LLM calls)

In production systems, routing is CRITICAL. You might have:
- Main router agent
- Specialized sub-agents for different domains
- Each sub-agent has its own tools

This is how companies like Intercom, Zendesk, and Shopify build their AI support systems."

---

## SLIDE 73: Routing

"Let me show you a detailed routing implementation.

**Routing**

**Routing is the mechanism that decides what the agent should do next or which system to call.**

Instead of following a fixed sequence of steps, the agent:
- **Evaluates current input**
- **Assesses context**
- **Chooses the most appropriate next action**

Look at this ROUTING PATTERN diagram:

User Query → Is Topic A? → Yes → LLM 1 → Find Response
                         ↓ No
                    Is Topic B? → Yes → LLM 2 → Find Response
                                 ↓ No
                            Is it Question? → Yes → LLM 3 → Find Response

**In practice, routing handles complex decision flow:**
- **When to call which tool** or skip it
- **Whether to continue**, retry, fallback, or stop
- **Which workflow path to take**
- **When to involve a human**

**Example scenario:**

User asks: 'I need help with my order'

Router evaluates:
- Is this billing? → Route to billing agent
- Is this technical? → Route to tech support
- Is this returns? → Route to returns agent
- Is this general inquiry? → Route to general support

**Better routing** = agent is just a little smarter workflow.

This pattern is fundamental to building sophisticated agents that can handle diverse tasks."

---

## SLIDE 74: Routing Mechanisms

"Let me show you the different ways to implement routing.

**Routing Mechanisms**

**Routing uses an evaluation mechanism to direct control flow. Common implementations include:**

**1. LLM-based Routing:** the LLM selects the next step based on input and context

Example:
```
Given the user's question, which tool should I use?
- weather_api for weather questions
- calculator for math
- database for user data
```

The LLM analyzes the question and picks the right tool.

**Pros:** Most flexible, handles ambiguous queries
**Cons:** Slower, costs more per decision

**2. Embedding-based Routing:** routes are chosen by **semantic similarity in vector space.**

Example:
- User query: 'How do I reset my password?'
- Convert to embedding: [0.23, -0.45, 0.67, ...]
- Compare with route embeddings
- Closest match: 'account_management' route

**Pros:** Very fast, cost-effective
**Cons:** Less flexible, requires good examples

**3. Rule-based Routing:** deterministic if–else logic; fast but inflexible.

Example:
```python
if 'weather' in query:
    route_to_weather_api()
elif 'order' in query and 'cancel' in query:
    route_to_order_cancellation()
else:
    route_to_general_support()
```

**Pros:** Fastest, most predictable, no LLM cost
**Cons:** Brittle, can't handle variations

**4. Machine Learning Model-based Routing:** a trained classifier makes routing decisions using learned weights.

Example:
- Train a classifier on historical routing decisions
- Input: User query features
- Output: Route probability distribution
- Pick highest probability route

**Pros:** Fast, accurate with good training data
**Cons:** Requires training data and maintenance

**We will actively apply the Routing pattern in the CRM Lead Qualification Agent project.**

**For most projects in this course, we'll use LLM-based routing because it's the most flexible and requires the least upfront work.**"

---

## SLIDE 75: LLM as a Router

"Let me show you a practical example of LLM-based routing.

**LLM as a Router**

**In our project, we use LLM-based routing as:**

Look at this diagram showing the routing flow:

User → Prompt → Router (LLM at center) → Agent 1 → Output
                                       ↓
                                     Agent 2 → Output

**Input is noisy and decisions require contextual, runtime evaluation.**

**The LLM Router:**

**Decides domain extraction vs human input**
- Can I extract company domain from this inquiry automatically?
- Or do I need to ask the user for more information?

**Selects tools (enrichment, CRM, scoring)**
- Which tool should I use to enrich this lead data?
- Should I check the CRM first?
- Do I need to calculate a lead score?

**Handles failures and fallbacks**
- Tool returned an error? Try a different approach
- No data found? Ask for clarification
- Low confidence? Route to human review

**Routes between auto-qualification and human review**
- Lead score > 80? Auto-qualify
- Lead score 50-80? Human review
- Lead score < 50? Auto-reject with feedback

**The beauty of LLM-based routing:**

It can handle the messy, ambiguous real-world scenarios that rule-based systems struggle with.

Example:
- User input: 'We're a mid-size company looking to improve our sales process'
- Router thinks: 'Company size mentioned, sales focus, but no explicit domain. I should ask for their website or company name to enrich data before proceeding.'

**This level of contextual decision-making is what makes LLM routers so powerful.**"

---

## SLIDE 76: Let's build a CRM Lead qualifier agent using an LLM as the router

"Now we're going to put all this theory into practice. Let me walk you through a REAL production-grade agent design. This isn't a toy example - this is how you'd actually build and deploy an agent in a company.

We'll do this in two parts:
1. **First**: I'll walk you through the architecture and design using a comprehensive README document
2. **Then**: We'll implement it together with live code in a Colab notebook

---

### PART 1: ARCHITECTURE & DESIGN (README Document)

**Full README Document:** https://docs.google.com/document/d/19xSMzhgHF90Vvy7Htzz6XRx5WuPJXNPg1PyTKfzS2tA/edit?tab=t.0

Before we write a single line of code, we need to understand what we're building and WHY we're building it this way. This README is your blueprint for production-grade agent design.

---

**1. PROJECT TITLE & VALUE PROPOSITION**

**Autonomous Lead Qualification Agent for Sales Development Representatives**

Reducing lead research time by **~70%** and improving first-call conversion rates by **~25%** by autonomously synthesizing enrichment data, CRM history, and business rules into a sales-ready qualification summary.

That's not incremental improvement. That's transformation.

---

**2. BACKGROUND & PROBLEM CONTEXT**

**The Reality:**

In high-velocity outbound sales teams, SDRs handle **50+ new leads daily**.

Each lead requires manual research across:
- Enrichment tools (Clearbit, ZoomInfo)
- CRM systems (Salesforce)
- Company websites
- LinkedIn

**The Cost:**

This research consumes **3-4 hours per day** per SDR and results in:
- ❌ Inconsistent qualification
- ❌ Missed historical context
- ❌ Poorly prepared discovery calls
- ❌ Burnt-out SDRs

**Why Automation Fails:**

Simple automation fails because lead data is:
- Incomplete (missing company info)
- Conflicting (CRM says "Cold" but attended 3 webinars)
- Non-deterministic (requires judgment calls)

**You need an agent, not a workflow.**

---

**3. TARGET USER & JOB TO BE DONE (JTBD)**

**Primary User:** Sales Development Representative (SDR)

**JTBD:** Within **60 seconds** of receiving a new lead, understand:
- Company context (industry, size, revenue)
- Prior engagement history (emails, webinars, calls)
- Priority level (hot lead vs. cold outreach)

...to prepare a personalized first outreach.

**Secondary Users:**
- **Sales Managers:** Monitor pipeline quality and consistency
- **RevOps:** Audit scoring logic, trace decisions, enforce standards

---

**4. WHY AN AGENTIC APPROACH**

**Why scripts fail:**
- CRM/enrichment data is missing or ambiguous
- "What if the email is invalid?" → Script breaks

**Why workflow tools fail:**
- Zapier/RPA assume deterministic paths
- "Unexpected state" → Workflow stops

**Why chatbots fail:**
- Require step-by-step prompting
- Disrupts SDR workflow

**An agentic approach is required because the system must autonomously:**

✅ **Decide** when to proceed automatically vs. request human input
✅ **Interpret** ambiguous CRM states ("Cold Lead" vs. "Active Opportunity")
✅ **Reconcile** conflicting signals (mid-tier revenue + high buying intent)
✅ **Trigger** human review when confidence falls below threshold

**This is judgment, not automation.**

---

**5. AGENT ROLE, SCOPE & AUTONOMY LEVEL**

**Agent Responsibilities:**

1. **Autonomous Lead Qualification:** Evaluates inbound leads end-to-end
2. **Data Synthesis:** Reads and interprets information from multiple sources
3. **Lead Summary & Scoring:** Generates sales-ready summary with confidence score

**Autonomy & Boundaries:**

| Task | Autonomy Level | Human Escalation |
|------|---------------|------------------|
| Domain extraction | ✅ Fully autonomous | ❌ Invalid email formats |
| Company enrichment | ✅ Fully autonomous | ❌ Company not found |
| CRM lookups | ✅ Fully autonomous | ❌ PII/compliance flags |
| Lead scoring | ✅ Fully autonomous | ❌ Confidence < 70% |
| Summary generation | ✅ Fully autonomous | N/A |
| Sending outreach | ❌ **ALWAYS requires human approval** | ✅ All cases |

**Operational Guardrail:**

The agent **never writes** directly to the CRM or contacts prospects. All sensitive actions are mediated by humans.

---

**6. AGENT ARCHITECTURE & COMPONENTS**

```
┌─────────────────────────────────────────────────────────────┐
│                    AGENT ORCHESTRATOR                       │
│  (LLM with Function Calling + Stateful Reasoning Loop)      │
└───────────────┬───────────────────────────┬─────────────────┘
                │                           │
    ┌───────────▼───────────┐   ┌───────────▼───────────┐
    │   PLANNER LAYER       │   │   MEMORY LAYER        │
    │ • Task decomposition  │   │ • Session state       │
    │ • Tool selection      │   │   (collected_data{})  │
    │ • Validation checks   │   │ • No long-term memory │
    └───────────┬───────────┘   └───────────────────────┘
                │
    ┌───────────▼───────────────────────────────────────┐
    │           EXECUTOR LAYER (Tools)                  │
    ├───────────────────┬───────────────────┬───────────┤
    │ lookup_domain_info│ check_crm_history │calculate_ │
    │ (Enrichment API)  │ (CRM API)         │lead_score │
    └───────────────────┴───────────────────┴───────────┘
```

**Key Design Decisions:**

**Planner Layer:** Uses LLM reasoning to dynamically sequence tool calls (domain extraction → enrichment → CRM lookup → scoring) without a hard-coded workflow.

**Executor Layer:** Composed of idempotent tool functions; mock implementations are used in the demo, with production equivalents mapped to enrichment and CRM APIs.

**Memory Layer:** Maintains a stateful `collected_data{}` dictionary that persists across tool calls within a single lead qualification session. **No long-term memory.**

**Orchestration Logic:** The orchestrator manages retries and failure handling within tool wrappers, with errors logged for observability.

---

**7. END-TO-END AGENT WORKFLOW**

Let me walk you through what happens when an SDR submits a lead:

**Input:** SDR submits lead email: `jane@acmecorp.com`

**Step 1: Context Extraction**
- Agent extracts company domain: `acmecorp.com`

**Step 2: Parallel Tool Execution**
- Calls `lookup_domain_info(acmecorp.com)`
  - Returns: `{industry: "SaaS", revenue: "$50M–$100M"}`
- Calls `check_crm_history(jane@acmecorp.com)`
  - Returns: `{status: "Cold Lead", notes: "Attended webinar"}`

**Step 3: Validation**
- Agent validates presence of required fields
- Flags any missing or invalid data

**Step 4: Scoring**
- Agent calls `calculate_lead_score()` using combined data
- Applies business rules:
  - "Active Opportunity" → High score
  - "$50M+ revenue" → Boost score
  - "Attended webinar" → Engagement signal

**Step 5: Output Generation**
- Agent synthesizes enrichment data, CRM history, and score
- Generates sales-ready lead summary

**Step 6: Fallback Handling**
- If domain lookup fails → Request manual domain input from SDR

**This entire process takes <15 seconds.**

Compare that to the 4+ minutes of manual research.

---

**8. TOOLS, MODELS & STACK**

| Component | Technology | Rationale |
|-----------|-----------|-----------|
| **Core Model** | GPT-4o | High accuracy for reasoning, tool selection, and natural-language synthesis; large context window |
| **Orchestration** | OpenAI Function Calling | Reliable, production-grade tool invocation; avoids brittle parsing |
| **Enrichment** | Clearbit API (mocked) | Industry-standard B2B enrichment; high domain coverage |
| **CRM Integration** | Salesforce REST API (mocked) | Native support for lead/contact objects with OAuth 2.0 |
| **Deployment** | Azure Functions | Serverless execution suitable for spiky SDR workloads |
| **Observability** | Datadog RUM | End-to-end visibility into agent steps, per-tool latency |

---

**9. EVALUATION STRATEGY & METRICS**

**Primary Evaluation Metrics:**

1. **Qualification Accuracy (≥85%):** Human audit of 200 agent-scored leads vs. sales manager assessments
2. **Time-to-Insight (<15 seconds):** P95 latency from submission to summary
3. **SDR Adoption Rate (≥90%):** Percentage of SDRs using agent for 80%+ of leads
4. **First-Call Conversion Lift (+25%):** A/B test agent-prepped vs. manually researched leads
5. **False Positive Rate (<8%):** Leads scored "High" but rejected by AEs during discovery
6. **Cost per Qualification (<$0.03):** Total API + compute cost per qualified lead

**Baseline Comparison:**

Manual lead qualification currently averages:
- **4.2 minutes per lead**
- **62% consistency** across SDRs

This is what we're benchmarking against.

---

**10. GUARDRAILS, TRUST & SAFETY**

**Data Boundaries:** Read-only CRM access; no write/modify/delete permissions

**PII Handling:** Email addresses hashed before logging; no raw PII in observability systems

**Human Override:** SDRs can reclassify lead scores before outreach

**Compliance:** Enrichment data tagged with source/timestamp for GDPR "right to explanation"

**Audit Trail:** All tool invocations logged with unique `lead_id` for RevOps auditing

**Kill Switch:** Circuit breaker disables agent if error rate >5% for 5 continuous minutes

**Trust is not optional in production agents.**

---

**11. FAILURE MODES & TRADEOFFS**

The system explicitly acknowledges and plans for known failure modes:

**Domain extraction failures** (e.g., `jane.doe+tag@acme.com`)
- **Fallback:** Manual domain input
- **Cost:** +8 seconds latency for ~3% of leads

**Enrichment API timeouts**
- **Fallback:** Use cached, last-known company data
- **Cost:** Default score to "Medium," ~12% accuracy reduction

**Ambiguous CRM statuses** (e.g., "Maybe interested")
- **Fallback:** Default to lower score tier
- **Cost:** Reduces false positives, may miss some opportunities

**Cost vs. speed tradeoff**
- **Decision:** Use GPT-4o-mini for scoring step only
- **Result:** +18% latency, -60% model costs

**Cold start latency**
- **Mitigation:** Pre-warm serverless instances during business hours
- **Cost:** $22/month infrastructure

**Critical Limitation:**

The agent does **not** assess external buying intent signals (funding announcements, hiring spikes).

Addressing this requires integration with intent data providers like 6sense, planned for version 2.

---

**12. RESULTS, LEARNINGS & INSIGHTS**

**What Worked:**

✅ Function calling reduced tool invocation errors by **92%** vs. regex parsing
✅ Stateful `collected_data{}` pattern prevented redundant tool calls
✅ SDRs trusted scores more when agent explained rationale

**What Failed:**

❌ Initial version used single prompt with all tools → 41% tool selection errors
❌ Hard-coded tool sequence broke when CRM returned "No Record"
❌ Over-engineered scoring algorithm (ML model) underperformed simple business rules

**Surprising Behavior:**

🤯 Agent autonomously combined "Webinar attendee" + "$100M revenue" to suggest talking points: *"Mention scalability features"*

🤯 When enrichment failed, agent used email domain TLD (`.gov`, `.edu`) as fallback signal for scoring

**The agent was smarter than we expected.**

---

**13. FUTURE IMPROVEMENTS & ITERATION PLAN**

**v1.1 (Q1) — Reliability**
- Robust retry logic and circuit breakers for all external API calls

**v2.0 (Q2) — Intent Data**
- Integrate 6sense API for technographic and intent signals

**v2.5 (Q3) — Multi-Lead Qualification**
- Support batch qualification for account-based workflows (all contacts at @acmecorp.com)

**v3.0 (Q4) — Predictive Scoring**
- Fine-tune model on historical win/loss data to predict conversion probability

---

**14. DEMO & ARTIFACTS**

**Live Demo Video:** 2-minute walkthrough of lead submission → agent reasoning → output

**Sample Qualification Trace:**

```json
{
  "lead_email": "bob@widgetco.net",
  "domain_info": {
    "industry": "Manufacturing",
    "revenue": "$10M-$25M"
  },
  "crm_history": {
    "status": "Active Opportunity",
    "last_contact": "2025-12-01"
  },
  "lead_score": "High",
  "reasoning": "Active Opportunity status overrides mid-tier revenue"
}
```

---

**15. ROLE-BASED SIGNALS**

This project demonstrates different signals depending on who's evaluating it:

**For Product Managers:**
- Strong problem framing around SDR time inefficiency
- Clearly defined, measurable outcomes (70% time reduction)
- Explicit tradeoff decisions (conservative scoring)
- Trust-aware design (human override mechanisms)

**For Engineering Managers:**
- Production-ready agent orchestration pattern
- Clear failure containment strategies (circuit breakers)
- Thoughtful scalability planning (serverless deployment)

**For Software Engineers:**
- Modular, idempotent tool design
- Robust validation and error-handling logic
- End-to-end observability with per-tool tracing

---

**Key Quote:**

*"The best sales agents don't replace humans—they eliminate the work that prevents humans from being human."*

---

**That's the architecture and design philosophy. Now you understand WHAT we're building, WHY we're building it, and HOW it should work.**

---

### PART 2: IMPLEMENTATION (Live Code in Notebook)

**Colab Notebook:** https://drive.google.com/drive/folders/1HV5-yWn6wVf_nFokVR_y9PCI6HURwXyg?usp=drive_link

Now let's roll up our sleeves and implement this agent from scratch.

In the notebook, we'll build:

1. **Tool Functions** - The actual Python functions the agent can call:
   - `lookup_domain_info()` - Mock enrichment API
   - `check_crm_history()` - Mock CRM lookup
   - `calculate_lead_score()` - Scoring logic

2. **Function Calling Setup** - Teaching the LLM about available tools using OpenAI's function calling format

3. **Agent Orchestrator** - The ReAct loop that:
   - Calls the LLM with the user's lead email
   - Receives tool call instructions from the LLM
   - Executes those tools
   - Feeds results back to the LLM
   - Repeats until the agent generates the final summary

4. **End-to-End Test** - Running a full lead qualification with `jane@acmecorp.com`

**What you'll see:**

The agent autonomously deciding which tools to call, in what order, without any hard-coded workflow. That's the magic of LLM-based routing.

**Ready? Let's code this together.**"

---

## SLIDE 77: Questions?

"Alright, we've covered a TON of material. Before we jump into the hands-on project, let's pause for questions.

What's confusing? What do you want to dive deeper into?

Don't be shy - this is your time."

*[Take 10-15 minutes for Q&A]*

**Some common questions I anticipate:**

**Q: 'How do agents avoid getting stuck in infinite loops?'**

Great question! You implement safeguards:
- Maximum iteration limit (e.g., stop after 10 loops)
- Timeout (stop after 60 seconds)
- Cost limit (stop if you've spent $1 in API calls)
- Loop detection (if agent repeats same action 3 times, stop)

**Q: 'What if the agent calls the wrong tool?'**

This happens! That's why the ReAct loop has OBSERVATION. The agent calls a tool, sees it got the wrong result, and tries a different tool.

**Q: 'Isn't this expensive with API costs?'**

It can be. Best practices:
- Use cheaper models (GPT-3.5) for simple tasks
- Use expensive models (GPT-4) only for complex reasoning
- Cache common queries
- Implement good routing to avoid unnecessary calls

**Q: 'Can I trust agents in production?'**

Depends on the use case:
- High-stakes (medical, financial): Use human-in-the-loop
- Low-stakes (draft emails, data queries): Full autonomy is fine
- Always log agent actions for auditing"

---

## SLIDE 78: Now that the agent is built, we package the project with a clear README and publish it to our GitHub portfolio.

"Perfect! So we've built this amazing CRM Lead Qualifier agent. But building it is only half the battle.

**Now that the agent is built, we package the project with a clear README and publish it to our GitHub portfolio.**

**README Template Document:** https://docs.google.com/document/d/1TZgno-_AuO6C1Pcg_DxrXNk7BB2FntddAfcsrgim8-M/edit?tab=t.0

This is CRITICAL. Your GitHub becomes your portfolio.

Let me show you **the only Agentic AI project template you should ever use.**

This template is designed to make it immediately clear:
- What problem the agent solves
- Why an agent is required (not just automation)
- How it thinks and makes decisions
- How success is measured

**Here's the complete structure:**

---

### 1️⃣ PROJECT TITLE & VALUE PROPOSITION

**Format:** Agent type + primary user + outcome

**Example:**
*"Autonomous Incident Triage Agent for SRE teams, reducing MTTR by 30%"*

Not: "AI Chatbot" or "Smart Assistant"

Be specific. Quantify impact if possible.

---

### 2️⃣ BACKGROUND & PROBLEM CONTEXT

This section answers:
- What's the real-world context where this problem appears?
- Who experiences the pain and how frequently?
- Why does this problem become hard at scale?
- What breaks with manual processes or simple automation?

**Avoid generic AI framing.** This should read like a real operational problem.

Example:
*"Support teams receive 500+ tickets daily. Each requires classification (billing, technical, account) before routing. Manual classification takes 2-3 minutes per ticket and results in 15% misrouting."*

---

### 3️⃣ TARGET USER & JOB TO BE DONE (JTBD)

**Primary user persona** (role, environment)
**Secondary users** (if any)
**Clear Job To Be Done**

**Example format:**
- **Primary User:** Support Operations Manager
- **JTBD:** Accurately classify and route incoming tickets within SLA without manual intervention

---

### 4️⃣ WHY AN AGENTIC APPROACH (⚠️ VERY IMPORTANT)

**This section is a hard requirement. If this is weak, the project is weak.**

Explicitly justify:
- Why scripts, workflows, or chatbots are insufficient
- Where reasoning, planning, or autonomy is required
- What decisions the agent must make dynamically

**Example:**
*"Rule-based routing fails because ticket content is ambiguous. 'Password reset' could be BILLING (subscription access) or TECHNICAL (login issue). The system must interpret context, not match keywords."*

---

### 5️⃣ AGENT ROLE, SCOPE & AUTONOMY LEVEL

Define clearly:
- What the agent owns end-to-end
- Where humans intervene
- What actions are restricted

**Example:**
- ✅ Agent autonomously plans and executes classification and routing
- ⚠️ Human approval required for escalations
- ❌ Agent CANNOT send customer-facing messages

**Use a table if helpful:**

| Task | Autonomy Level | Human Escalation |
|------|---------------|------------------|
| Ticket classification | ✅ Fully autonomous | ❌ Only on errors |
| Routing decisions | ✅ Fully autonomous | N/A |
| Customer replies | ❌ Human approval required | ✅ All cases |

---

### 6️⃣ AGENT ARCHITECTURE & COMPONENTS

Break the system into thinking and execution units.

**a) Planner / Decision Layer**
- How tasks are decomposed
- Static vs dynamic planning

**b) Executors / Sub-Agents**
- Individual responsibilities
- Tools or APIs used

**c) Memory**
- Short-term (conversation / session state)
- Long-term (vector DB, logs, historical data)

**d) Orchestration Logic**
- Control flow (sequential, parallel, conditional)
- Retry logic
- Failure handling

**Diagrams are encouraged but not mandatory.**

---

### 7️⃣ END-TO-END AGENT WORKFLOW

Describe the lifecycle step-by-step:

1. **Input ingestion** - How data enters the system
2. **Context extraction** - What information is parsed
3. **Planning / decomposition** - How the agent breaks down the task
4. **Tool execution** - What actions are taken
5. **Validation or self-check** - How accuracy is verified
6. **Output generation** - What the agent produces
7. **Escalation or fallback** (if needed) - What happens on failure

**This should read like a trace of the agent's thinking.**

Example:
*"Step 1: Ticket received → Step 2: Extract key phrases → Step 3: Call classification tool → Step 4: Validate confidence score → Step 5: If <70%, escalate to human"*

---

### 8️⃣ TOOLS, MODELS & STACK (WITH RATIONALE)

**For each major component:**
- What tool/model is used
- Why it was chosen
- What role it plays in the system

**Listing tools without justification is considered incomplete.**

**Example:**

| Component | Technology | Rationale |
|-----------|-----------|-----------|
| Core Model | GPT-4o | High reasoning capability for ambiguous classification |
| Orchestration | LangGraph | Stateful workflow with retry logic |
| Memory | Pinecone | Vector search for similar past tickets |
| API Integration | Zendesk REST API | Native ticket management |

---

### 9️⃣ EVALUATION STRATEGY & METRICS

Define how success is measured:

- **Accuracy or task success rate** (e.g., 92% classification accuracy)
- **Latency** (e.g., <5 seconds per ticket)
- **Cost per run** (e.g., $0.02 per classification)
- **Human intervention rate** (e.g., 8% escalation rate)
- **Known false positives / negatives**

**Even approximate metrics are acceptable if reasoning is clear.**

**Baseline comparison is powerful:**
- Manual classification: 2.5 minutes, 85% accuracy
- Agent classification: 4 seconds, 92% accuracy

---

### 🔟 GUARDRAILS, TRUST & SAFETY

Explain:
- Where the agent is allowed to act
- Where it must stop
- How users can override decisions
- Logging and observability

**This section is critical for PMs and EMs.**

**Example:**
- ✅ Read-only access to ticket system
- ❌ Cannot delete or modify tickets
- 🔍 All decisions logged with `ticket_id` for auditing
- 🚨 Kill switch if error rate >10% for 5 minutes

---

### 1️⃣1️⃣ FAILURE MODES & TRADEOFFS

**Known edge cases:**
- Where the agent fails or becomes unreliable
- Tradeoffs between accuracy, cost, and speed
- Constraints intentionally accepted

**Honesty here increases credibility.**

**Example:**
- ❌ Agent struggles with tickets in non-English languages (fallback: route to multilingual team)
- ⚖️ Chose GPT-4o over GPT-4o-mini: +$0.015/ticket, but +7% accuracy
- 🎯 Optimized for precision over recall (better to escalate than misroute)

---

### 1️⃣2️⃣ RESULTS, LEARNINGS & INSIGHTS

- What worked better than expected
- What failed initially
- Surprising agent behavior
- Key system or product learnings

**This should feel like a postmortem, not marketing.**

**Example:**
- ✅ Function calling reduced parsing errors by 94% vs regex
- ❌ Initial single-prompt approach had 38% tool selection errors
- 🤯 Agent learned to use ticket urgency tags as routing signals without explicit instruction

---

### 1️⃣3️⃣ FUTURE IMPROVEMENTS & ITERATION PLAN

- What v2 would change
- What would be needed to scale
- Additional agents, tools, or controls planned

**Example:**
- **v1.1:** Add multilingual support via translation API
- **v2.0:** Multi-agent system with specialized classifiers per category
- **v3.0:** Fine-tuned model on historical ticket data

---

### 1️⃣4️⃣ DEMO & ARTIFACTS

- Live demo link or video walkthrough
- Architecture diagram (optional)
- Sample logs or traces (optional)

**Visual proof matters.**

---

### 1️⃣5️⃣ ROLE-BASED SIGNAL (MANDATORY)

**Explicitly state what this project demonstrates:**

**For Product Managers:**
- Problem framing and impact measurement
- Metrics, tradeoffs, trust considerations
- User-centric design decisions

**For Engineering Managers:**
- System design and orchestration patterns
- Scalability and failure handling
- Observability and monitoring strategy

**For Software Engineers:**
- Code correctness and robustness
- Modular architecture
- Clean tool integration and error handling

---

### ✅ DO'S AND ❌ DON'TS (EVALUATION-READY)

| Area | ✅ Do | ❌ Don't |
|------|------|----------|
| **Problem** | Describe a real, scaled pain | Pick a toy or generic problem |
| **Agent Justification** | Explain why an agent is needed | Use agents "because AI" |
| **Autonomy** | Clearly define boundaries | Claim full autonomy blindly |
| **Architecture** | Decompose into planner/executor/memory | Treat agent as a single prompt |
| **Workflow** | Show step-by-step reasoning | Jump straight to output |
| **Tools** | Justify every major tool | List tools as buzzwords |
| **Metrics** | Define how success is measured | Say "works well" |
| **Safety** | Add guardrails and overrides | Ignore trust and control |
| **Failure Modes** | Admit limitations | Claim no failures |
| **Learnings** | Share insights and tradeoffs | Only highlight positives |
| **PM Signal** | Focus on decisions and impact | Over-index on code |
| **EM Signal** | Explain orchestration and scale | Stay at surface level |
| **SWE Signal** | Show robustness and structure | Rely on demos only |

---

**Why this template matters:**

When you apply for jobs or freelance work:
- Recruiters will look at your GitHub
- They want to see REAL projects, not toy examples
- Agents are hot right now - having 3-4 agent projects following this template makes you stand out

**Every agent we build in this course will follow this structure.**

Not just code that works - but code that's:
- Well-documented
- Production-ready
- Professionally presented

**This is what separates students who get jobs from students who don't.**"

---

## SLIDE 79: Build → Document → Publish (Every Agent)

"Let me make this crystal clear. This is the workflow we'll follow for EVERY project in this course.

**Build → Document → Publish (Every Agent)**

**For every agent built in this course:**

**1. Package the project with a clear, structured README**
- Not optional - REQUIRED
- Use the template I provide
- Make it professional

**2. Upload it to your GitHub portfolio**
- Public repository
- Clear name: 'CRM-Lead-Qualifier-Agent', not 'project-1'
- Add relevant tags/topics

**3. Treat each agent as a standalone, portfolio-ready artifact**
- Should be runnable by anyone who clones it
- Include requirements.txt or environment setup
- Add example data if needed
- Document any API keys needed

**This workflow will be applied consistently in every class as agents are built and published.**

**By the end of this course, you'll have:**
- 10-12 agent projects in your GitHub
- Each one professionally documented
- Each one demonstrating different agent patterns
- A portfolio that screams 'I know how to build production agents'

**When you apply for jobs:**

Interviewer: 'Have you built any AI agents?'
You: 'Yes, here are 12 projects I've built' *[shares GitHub]*
Interviewer: 'When can you start?'

**This is the difference between learning and LEARNING.**

We're not just building projects - we're building your career portfolio."

---

## SLIDE 80: Week 0 - Mini Project

"Alright, now let's get our hands dirty with your first agent project.

**Week 0 - Mini Project**

This is your warmup project. Simple, but complete.

**Purpose:**
- Get comfortable with the build-document-publish workflow
- Implement a simple agent with tools
- Create your first portfolio piece

**What you'll build:**

A lightweight agent that's immediately useful but not overwhelming.

**Requirements:**
- Single tool or small set of tools
- Clear, specific use case
- Completable in 2-3 hours
- Fully documented

**Due date: End of this week**

This sets the foundation for the more complex agents we'll build in coming weeks.

Think of this as your 'Hello World' for agentic AI.

---

### Hands-On: Multi-File CSV Agent (Colab Notebook)

**Colab Notebook:** https://colab.research.google.com/drive/1vb9Y34MaoyrAd0QMYsUGkKW11WZfeSAI

Now let me walk you through the hands-on implementation. Open the notebook and follow along.

**What you'll build:**

A smart data assistant that can answer questions across MULTIPLE CSV files:
- `saas_docs.csv` - SaaS product documentation
- `credit_card_terms.csv` - Credit card terms and conditions
- `hospital_policy.csv` - Hospital visiting policies
- `ecommerce_faqs.csv` - E-commerce frequently asked questions

**The Challenge:**

Imagine you're a customer support agent juggling 4 different knowledge bases. A customer asks: *"What's the API rate limit?"*

You need to:
1. Figure out which CSV contains this info (probably saas_docs.csv)
2. Search through it
3. Find the answer
4. Respond accurately

**With our agent, this happens automatically in seconds.**

---

### The Code Structure

The notebook has **3 parts**:

**PART 1: AUTOMATIC FILE DOWNLOADER**
- Automatically downloads all 4 CSV files from Google Drive
- Uses `gdown` to handle Google Drive links
- Skips files that already exist locally

**PART 2: AI AGENT SETUP (Multi-File)**
- Gets your OpenAI API key securely using `getpass()`
- Loads all 4 CSV files into pandas DataFrames
- Creates a Pandas DataFrame Agent using LangChain
- The agent can intelligently route questions to the right CSV

**PART 3: CHAT LOOP**
- Interactive conversation with the agent
- Type questions in natural language
- Agent determines which CSV to query
- Returns answers based on actual data

---

### Your Tasks (TODOs in the Notebook)

**TODO 1: Initialize the LLM**
```python
llm = None  # <--- Replace with ChatOpenAI initialization
```

**Hint:** Use `ChatOpenAI(api_key=api_key, model="gpt-4o-mini", temperature=0.0)`

---

**TODO 2: Create the Pandas Agent**
```python
agent = create_pandas_dataframe_agent(
    llm,
    # <--- Pass the dataframes list here
    verbose=True,
    agent_type="openai-functions",
    allow_dangerous_code=True
)
```

**Hint:** Pass `dataframes` as the second argument

---

**TODO 3: Invoke the Agent**
```python
response = "..."  # <--- Replace with agent.invoke() call
```

**Hint:** Use `agent.invoke(final_query)['output']`

---

### How It Works Behind the Scenes

When you ask: *"What are the visiting hours at the hospital?"*

**Step 1:** The agent receives your question + the system prompt

**Step 2:** The LLM reasons:
- "This question is about hospital policy"
- "I should query the hospital_policy.csv DataFrame"

**Step 3:** The agent generates and executes Python code:
```python
df[df['topic'].str.contains('visiting hours', case=False)]
```

**Step 4:** The agent reads the result and formats a natural language answer:
*"Visiting hours are 9 AM to 8 PM daily."*

**This is the magic of LLM-powered routing!**

The agent autonomously decides:
- Which CSV file to query
- What pandas operations to perform
- How to synthesize the answer

---

### Try These Example Queries

Once your agent is running, test it with:

1. *"What is the API rate limit for the SaaS product?"* (queries saas_docs.csv)
2. *"What's the annual fee for the credit card?"* (queries credit_card_terms.csv)
3. *"What are the hospital visiting hours?"* (queries hospital_policy.csv)
4. *"What's your return policy?"* (queries ecommerce_faqs.csv)

Watch how the agent automatically figures out which file contains the answer!

---

### Key Learning Points

✅ **Multi-file routing:** Agent intelligently selects the right data source
✅ **Pandas integration:** Executes actual Python code to query DataFrames
✅ **Natural language interface:** No need to write SQL or pandas code manually
✅ **Error handling:** Gracefully handles questions when data isn't found

**This is a production-ready pattern.** Companies use this exact architecture to:
- Query internal knowledge bases
- Answer customer support questions
- Analyze business data
- Generate reports from multiple sources

---

**Now open the notebook and complete the TODOs. Once you're done, test your agent with the example queries!**"

---

## SLIDE 81: Mini Project: Hello Agent – CSV FAQ Agent

"Here's your first project.

**Mini Project: Hello Agent – CSV FAQ Agent**

**The Challenge with Manual CSV Queries:**

Look at this diagram showing the problem:

Many organizations store key knowledge in CSV files (FAQs, policies, docs).

Teams manually search these files during live conversations.

**This leads to:**
- **Slow responses** — information is hard to query quickly
- **Inconsistent answers** — different team members may interpret differently
- **Inefficient workflows** — time wasted on repetitive searches

*[Image shows team members with CSV files, question marks, and frustrated expressions]*

**Your solution:**

Build an agent that:
1. Ingests CSV files
2. Understands natural language questions
3. Queries the data intelligently
4. Returns accurate answers
5. Handles missing data gracefully

**Example interaction:**

User uploads employee_benefits.csv

User: 'What's the policy on remote work?'
Agent: *[Searches CSV]* 'According to the policy document, employees can work remotely up to 3 days per week with manager approval.'

User: 'What about parking?'
Agent: *[Searches CSV]* 'I don't see any information about parking policies in the uploaded document.'

**This is practical, useful, and great for your portfolio.**"

---

## SLIDE 82: Mini Project: Hello Agent – CSV FAQ Agent

"Let me give you the detailed requirements.

**Mini Project: Hello Agent – CSV FAQ Agent**

**CSV FAQ Agent Requirements:**

**1. CSV Upload:** Users can upload one or more CSV files.

**2. Natural Language Queries:** Users can ask questions in plain English.

**3. Data-Driven Answers:** Responses are strictly based on the uploaded CSV data.

**4. Missing Data Handling:** Clearly indicate when an answer is not found in the data.

Let me show you what this looks like in practice:

**Example 1:**
User uploads customer_data.csv:
```
name,location,purchase_amount,status
John,California,500,completed
Mary,Texas,300,pending
Bob,California,800,completed
```

User asks: 'How many customers are from California?'
Agent responds: 'There are 2 customers from California.'

**Example 2:**
User asks: 'What's the total purchase amount for completed orders?'
Agent responds: 'The total purchase amount for completed orders is $1,300.'

**Example 3:**
User asks: 'How many customers are from Florida?'
Agent responds: 'No customers from Florida were found in the data.'

See how it works? The agent:
1. Understands the question
2. Translates it to a data query
3. Executes the query
4. Returns a natural language answer

Now let me show you how to build this step by step..."

*[Continue with hands-on implementation as in the previous notes]*

---

## SLIDE 83: Hello Agent – CSV FAQ Agent: Solution

"Let me walk you through the solution architecture.

**Hello Agent – CSV FAQ Agent: Solution**

**To solve the problem efficiently and meet the requirements:**

Look at this flowchart showing the complete agent flow:

**User Question** (Pink)
↓
**LLM Reasoning Agent** (Pink) - Agent analyzes the question
↓
**Select Relevant CSV** (Purple) - Agent picks which CSV file to query
↓
**Query & Process Data** (Green/Pink split)
↓ ↙
**Return Answer in Plain English** (Green) | **Indicate Missing Data** (Pink)

**The implementation:**

**1. Load all CSV files** into memory for access.
- When user uploads CSVs, parse and store them
- Maintain a dictionary: {filename: dataframe}

**2. Initialize an LLM agent** (ChatOpenAI, GPT-4o-mini) to reason over data.
- Use a fast, cost-effective model for reasoning
- Configure with appropriate temperature (lower for factual queries)

**3. Connect multiple CSVs** to the agent for multi-source decision making.
- Agent can intelligently choose which CSV to query
- Can combine information from multiple sources if needed

**4. Design system prompts** to guide the agent: pick the correct CSV, answer only from data, return plain English responses.
- Explicit instructions: 'Only answer based on data in the CSV files'
- 'If information is not found, clearly state that'
- 'Provide concise, accurate responses'

**5. Implement a chat loop:** user question → agent queries → returns answer or indicates missing data.
- Simple interaction loop
- Maintains conversation context
- Handles errors gracefully

**Let's now look at the Solution**

*[This is where you would demo the actual code or Colab notebook]*

**Key technical components:**

```python
# Load CSVs
csv_data = {
    'policies.csv': pd.read_csv('policies.csv'),
    'faqs.csv': pd.read_csv('faqs.csv')
}

# Initialize LLM agent
agent = ChatOpenAI(model='gpt-4o-mini', temperature=0)

# System prompt
system_prompt = '''
You are a helpful FAQ agent. You have access to multiple CSV files.
When answering questions:
1. Determine which CSV file is most relevant
2. Query that CSV for the answer
3. Return only information found in the data
4. If not found, clearly state "I don't have information about that in the uploaded files"
'''

# Chat loop
while True:
    user_question = input('Ask me anything: ')
    response = agent.query(csv_data, user_question, system_prompt)
    print(response)
```

**This agent demonstrates:**
- Tool use (CSV querying)
- Routing (selecting the right CSV)
- Natural language understanding
- Graceful error handling

**Perfect first portfolio project!**"

---

## SLIDE 84: Thank You

"And that's a wrap!

**Thank You**

*[Image showing 'Thank You' in cheerful yellow cloud with coffee cup]*

**We've covered:**
- Traditional agent types (Reflex, Model-based, Goal-based, Utility-based)
- LLMs and their limitations
- How LLMs become agents with tools, memory, and loops
- The ReAct pattern
- Agentic design patterns
- Real-world agent architectures
- Your first hands-on project

**Your homework:**
Build the CSV FAQ Agent and push it to GitHub by next Sunday.

**Next week:**
We'll dive into more advanced agent patterns and build a CRM Lead Qualifier with routing logic.

**Remember:**

The future of software is agentic. You're now equipped with the foundational knowledge to build that future.

Keep building. Keep learning. Keep pushing to GitHub.

**See you next week!**

Any final questions? Catch me after class or on Slack."

---

## WRAP-UP (Final 10 minutes)

"Alright everyone, we've come to the end of this 4-hour journey. Let me recap what we've covered:

**1. We started with the FUNDAMENTALS:**
- Reflex agents that react instantly
- Model-based agents that have memory
- Goal-based agents that plan ahead

**2. We bridged to MODERN AI:**
- Limitations of LLMs alone
- How to turn LLMs into agents with tools and memory

**3. We learned the CORE PATTERN:**
- The ReAct loop: Thought → Action → Observation → Repeat
- This is how virtually every modern agent works

**4. We BUILT something:**
- Your own CSV FAQ agent using these principles

**What's next?**

In the coming weeks, we'll go deeper:
- Multi-agent systems (agents collaborating)
- Advanced memory systems
- Production deployment
- Safety and monitoring

**Your homework:**
Complete the CSV FAQ Agent with these requirements:
- Upload multiple CSV files
- Answer natural language queries
- Handle edge cases
- BONUS: Add visualization support

**Due: Next Sunday before class**

Before you go, I want to leave you with this thought:

**Two years ago, building an autonomous agent required a PhD and months of research.**

**Today, you can build one in an afternoon.**

That's how fast this field is moving. And you're now equipped with the foundational knowledge to be part of this revolution.

Thank you all for your attention. See you next week!"

---

## END OF TEACHING SCRIPT

Remember as you teach:
- **Pause for effect** after important points
- **Make eye contact** when asking questions
- **Use hand gestures** to emphasize key concepts
- **Vary your pace** - slow down for complex topics, speed up for reviews
- **Show enthusiasm** - your energy is contagious
- **Tell stories** - people remember stories better than facts

You've got this! This script gives you everything you need to deliver an engaging, impressive 4-hour class.
