# Talking Script — Inside A2A: How Agents Talk to Other Agents

> Companion deck for Module 2 of the Real-Estate Negotiation Simulator.
> Every concept is grounded in a runnable demo: `a2a_10`–`a2a_13`, the buyer/seller Agent Cards, and the MCP-backed negotiation agents.
> Read this line by line as you present. Runnable files are in `m2_adk_multiagents/`.

---

## SLIDE 1 — Title

[Presenter opens.] Welcome. Today we're going one level below "agents talking to agents." We're going all the way down to the wire — to the actual protocol that lets one agent discover another, hand it a piece of work, and get results back. That protocol is **A2A** — Agent2Agent. And by the end, you'll have watched a buyer agent and a seller agent negotiate the price of a house over it, live.

---

## SLIDE 2 — The One Sentence to Remember

Before any diagrams, let me give you the single sentence that unlocks everything else. Stop thinking of A2A as "chatbots messaging each other." Think of it this way:

> **A2A is a standardized distributed-systems protocol for discovering a remote agent, describing what it can do, sending it a stateful unit of work, and receiving progress and results back — asynchronously.**

Hold onto that. Discovery. Description. A stateful unit of work. Asynchronous results. Those four ideas are the whole session.

And here's the contrast that matters most in this workshop: in Module 1 you learned **MCP** — the Model Context Protocol. MCP standardizes how an agent talks to **tools and resources**. A2A standardizes how an agent talks to **other agents**. Same spirit — an open protocol so you don't hand-code every integration — but a different layer of the stack. MCP is the agent reaching *down* to its tools. A2A is the agent reaching *sideways* to a peer.

---

## SLIDE 3 — Agenda

Here's the path. We'll start with the mental model — why A2A exists at all, and how it differs from MCP. Then we walk the lifecycle in order, and every step maps to a demo you can run:

1. **Discovery** and the **Agent Card** — `a2a_10`
2. **Messages** and **Parts** — `a2a_11`
3. The **transport** — JSON-RPC over HTTP, the actual bytes — `a2a_10`
4. **Tasks** — the unit of work, its lifecycle, and Task-ID vs Context-ID — `a2a_11`
5. **Artifacts** — durable outputs — `a2a_12`
6. Three ways to get results — **polling, streaming, push**
7. **Orchestration** — one script playing matchmaker between a buyer and a seller — `a2a_13`
8. **A2A + MCP together**, and a bit of **security**

Along the way I'll drop numbered **Key Ideas**. We'll collect all of them on one slide at the end.

---

## SLIDE 4 — Section Divider: Why A2A Exists

Part one — Why A2A. Five minutes. Before we send a single message, let's be clear about the problem this protocol is actually solving.

---

## SLIDE 5 — The Problem: Integration Hell

Imagine you don't have A2A. Your orchestrator agent wants to ask a specialist agent — say, a pricing specialist — to do some work. Without a standard, what do you write?

You hard-code a URL. `pricing_agent_url = "https://foo.com/api/chat"`. You hand-craft the headers, you guess the payload shape, you parse whatever comes back. Fine — for one agent.

Now your system grows. You've got a buyer agent, a seller agent, a market-intel agent, a mediator agent. Each one a different company, a different framework, a different payload. Every pair is a bespoke integration. That's an N-times-M explosion of glue code, and it breaks every time anyone changes anything.

The orchestrator shouldn't need to know which LLM the remote agent uses, what framework it's built on, whether it's Python or Go, or how it stores state. It should only need to know four things: *Where are you? What can you do? How do I authenticate? How do I talk to you?*

That's the abstraction A2A gives you. And that's Key Idea 1: **A2A makes the description of an agent portable — so discovery and communication stop being bespoke glue code.**

---

## SLIDE 6 — MCP vs A2A: The Two-Protocol World

Let me make the MCP-versus-A2A distinction concrete, because in this repo you'll see both at once.

On one side, MCP. An agent calls a tool: `get_market_price(address)`. The tool doesn't reason. It executes an operation and returns data. That's what your `pricing_server.py` and `inventory_server.py` from Module 1 do.

On the other side, A2A. An agent calls another *agent*: "Seller, here's my offer of 400K." The seller agent doesn't just execute — it *reasons*. It checks its floor price, weighs its strategy, maybe calls its own tools, and decides on a counter-offer. You don't control those internal steps. You only see the boundary.

So: **MCP exposes capabilities. A2A exposes agentic collaboration.** A tool is a function you drive. An agent is a peer you delegate to. That's Key Idea 2: **use MCP to give an agent hands; use A2A to give it colleagues.**

And here's the punchline for this whole workshop — they're not competitors. In our negotiation, each agent uses **MCP** to reach its pricing tools, and **A2A** to talk to the other side of the table. Two protocols, complementary, same system.

---

## SLIDE 7 — Section Divider: Discovery & the Agent Card

Part two — Discovery. Six minutes. You can't message an agent you can't find. So discovery comes first.

---

## SLIDE 8 — The Agent Card

Suppose our buyer agent wants to negotiate with a seller. It needs a machine-readable description of that seller before it can say a word. That description is the **Agent Card**.

Open `negotiation_agents/seller_agent/agent.json` and read it with me. It has:

1. `name` — "seller_agent". Who are you?
2. `description` — what you're for.
3. `url` — `http://localhost:8000/a2a/seller_agent`. Where do I call you?
4. `version` — "1.0.0".
5. `capabilities` — `{ "streaming": false, "pushNotifications": false }`. Can you stream? Can you push? We'll come back to why both are false.
6. `skills` — an array, each with an id, name, description, tags, and examples. What can you actually do?

The most important thing to understand: **the Agent Card is not the agent.** It's metadata *about* the agent. Think of it like a business card, or a service-registry entry — it tells you who to call and what to expect, but it isn't the person.

That's Key Idea 3: **an agent's public identity is a small JSON document — identity, endpoint, capabilities, and skills — and nothing about its internal wiring.**

---

## SLIDE 9 — How Discovery Actually Happens — `a2a_10`

So how does the buyer *get* that card? This is where `adk_demos/a2a_10_wire_lifecycle.py` comes in. Run it and watch.

The convention is a **well-known URL**. The card lives at a predictable path — `/.well-known/agent-card.json` — so any client knows where to look without being told. In the demo, we don't even parse it by hand. The A2A SDK gives us a resolver:

```python
resolver = A2ACardResolver(httpx_client=http, base_url=args.seller_url)
card = await resolver.get_agent_card()
```

That one call fetches the card over HTTP and hands you back a typed object. Notice what just happened: the buyer knew *nothing* about the seller a moment ago, and now it has the seller's endpoint, version, and skill list. That's discovery.

And here's a lovely detail about how we run these: Google ADK serves those cards for you. When you launch with `adk web --a2a`, ADK takes each `LlmAgent`, auto-generates its Agent Card, and publishes it at the well-known URL. You wrote an agent; you got a discoverable service for free.

That's Key Idea 4: **discovery is "fetch a card from a well-known URL" — the SDK resolves it into a typed object, and the framework publishes it automatically.**

[SPEAKER NOTE: A2A defines the *card format* and the well-known path — it does not give you a global DNS of every agent on Earth. In an enterprise you'd publish cards through a registry or catalog. For us, it's localhost.]

---

## SLIDE 10 — Capability Negotiation

Look back at that card: `capabilities: { streaming: false, pushNotifications: false }`. Why does that matter?

Because the client reads capabilities *before* choosing how to talk. If the seller advertised `streaming: true`, the buyer could open a live event stream. It advertised `false`, so the buyer uses a plain request-response call instead. The card is a contract: it tells you not just *what* the agent can do, but *how* you're allowed to interact with it.

In our repo these are both `false` on purpose — our negotiation is simple request/response, and it keeps the demos readable. But the field is the negotiation point. That's Key Idea 5: **capabilities on the card let client and server agree on the interaction style up front — no guessing, no failed calls.**

---

## SLIDE 11 — Section Divider: The Message

Part three — The Message. Five minutes. We've found the agent. Now, what do we actually send it?

---

## SLIDE 12 — Message, Role, and Parts — `a2a_11`

The thing you send is a **Message**, and a Message has two pieces: a `role` — is this from the user side or the agent side — and a list of `parts`. Open `adk_demos/a2a_11_context_threading.py`:

```python
Message(
    messageId=f"msg_{uuid.uuid4().hex[:8]}",
    role=Role.user,
    parts=[TextPart(text="I offer 400000 for the property."),
           DataPart(data={"offer": 400000})],
)
```

Now, why *parts*, plural? Because agents don't only exchange chat. A2A defines three kinds of part:

1. **TextPart** — natural language. "I offer 400K."
2. **DataPart** — structured JSON. `{ "offer": 400000 }`. Machine-readable, no parsing prose.
3. **FilePart** — a document, an image, a binary blob.

See what that message did? It sent the human-readable sentence *and* the structured number, in the same envelope. The seller's LLM can read the text; the seller's code can read the data. That's Key Idea 6: **a Message is a role plus a list of typed Parts — so agents exchange prose, structured data, and files through one uniform envelope.**

[In our repo you'll see TextPart and DataPart heavily; FilePart is part of the spec but we don't need it to trade offers.]

---

## SLIDE 13 — Section Divider: The Transport

Part four — The Transport. Six minutes. Let's peel back the SDK and look at the actual bytes on the wire.

---

## SLIDE 14 — JSON-RPC 2.0 Over HTTP — `a2a_10`

A2A doesn't invent a new network protocol. Under the SDK, it's **JSON-RPC 2.0 over HTTP(S)**. `a2a_10_wire_lifecycle.py` literally dumps the wire format so you can see it. It looks like this:

```json
{
  "jsonrpc": "2.0",
  "id": "req_42",
  "method": "message/send",
  "params": { "message": { "role": "user", "parts": [ ... ] } }
}
```

Four fields. `jsonrpc` pins the version. `method` is what you're asking for — here, `message/send`. `params` carries the Message we just built. And `id` — that little `id` is doing real work: it lets the client match a response back to the request it belongs to. Request 42 comes back as response 42. The spec requires the server to echo that same id back.

That's Key Idea 7: **A2A rides on plain JSON-RPC over HTTP — the `id` correlates request and response, and `method` names the operation.** No magic. If you've written a web service, you already understand the transport.

[The spec also allows gRPC and REST bindings; our repo uses the JSON-RPC-over-HTTP binding, which is the one to teach first.]

---

## SLIDE 15 — `message/send`: Making the Call — `a2a_13`

So the actual call, in the SDK, is one line. From `a2a_13_orchestrated_negotiation.py`:

```python
response = await client.send_message(request)
```

That's it. `client.send_message` wraps everything we just saw — it builds the JSON-RPC envelope, POSTs it to the seller's endpoint, waits for the response, and hands you a typed result. The buyer just *sent an offer to the seller*.

Now something interesting happens on the other side. The seller can respond in one of two fundamentally different ways. And that split — response versus work — is the single most important concept in A2A. Next slide.

---

## SLIDE 16 — Section Divider: Tasks

Part five — Tasks. Ten minutes. This is the heart of A2A, and the part most explanations skip.

---

## SLIDE 17 — Message vs Task: Communication vs Work

A2A has two different concepts that beginners blur together: the **Message** and the **Task**.

A Message is *communication*. A Task is *work*.

Think about the difference. "What's the property's asking price?" — that's a quick question, a Message in, a Message back. Done. But "Analyze this property against every comparable in the neighborhood, model three financing scenarios, and produce a recommendation" — that's not a chat turn. That's a job. It might take five seconds or five minutes.

So A2A deliberately separates *communication* from *execution*. A trivial request gets a direct Message reply. A substantial request spins up a **Task** — a durable, identified unit of work that lives independently of the HTTP request that started it.

That's Key Idea 8: **A2A splits the quick reply from the long job — Messages carry communication, Tasks carry work.** That one design decision is why A2A is a distributed-systems protocol and not just `POST /chat`.

---

## SLIDE 18 — The Task Object and Its Lifecycle

When the work is substantial, the server returns a **Task**. Conceptually:

```json
{ "id": "task-abc123", "contextId": "context-xyz", "status": { "state": "working" } }
```

Three things: an `id`, a `contextId`, and a `status` with a `state`. And that state moves through a lifecycle — a small state machine:

```
submitted → working → completed
                   ↘ failed
                   ↘ canceled
                   ↘ input-required   (needs more from the caller)
```

Why does a durable Task matter so much? Because the HTTP request doesn't have to stay open. If the work takes thirty minutes, you do *not* want a socket held open for thirty minutes. Instead: you send the request, you get back `task-abc123`, the connection closes, and the work continues on the server. You reference the task later by its id.

In `a2a_13`, our negotiation is fast, so you'll mostly see tasks come back `completed`. But the object model is the real thing — `extract_agent_text(task)` in that file reaches into `task.artifacts`, `task.status.message`, and `task.history`. That's Key Idea 9: **a Task is a durable identity for a unit of work — so the caller can walk away and come back to it.**

---

## SLIDE 19 — Task ID vs Context ID — `a2a_11`

Now the subtle one, and it's the star of `a2a_11_context_threading.py`. There are *two* IDs, and they mean different things.

A **Task ID** identifies one unit of work — one execution. A **Context ID** groups related interactions into a conversation.

The mental model:

```
context = the whole negotiation
task    = one round within it
message = one turn within a round
```

Watch how the demo threads it. On round one, the buyer sends a message with no context id. The seller's response comes back carrying a fresh `contextId`. From round two onward, the buyer *reuses* that same context id — and now the seller remembers the whole thread. Drop the context id, and every message starts from amnesia.

And here's the punchline in `a2a_13`: the orchestrator keeps **two separate context ids** — `buyer_context_id` and `seller_context_id` — because the buyer and the seller are two independent conversations. Each side remembers its own thread; neither sees the other's. That's Key Idea 10: **Task ID tracks one job; Context ID threads a conversation — and multi-agent orchestration means juggling one context per counterpart.**

---

## SLIDE 20 — Artifacts: Durable Outputs — `a2a_12`

When a Task produces a result, that result isn't just a chat message — it's an **Artifact**. `adk_demos/a2a_12_parts_and_artifacts.py` is built around this distinction:

- A **Message** is communication — a turn in the conversation.
- An **Artifact** is a produced *result* — durable, attached to the Task.

Why separate them? Because outputs can be big, incremental, binary, or plural. A negotiation might emit a signed-offer artifact. A research agent might emit a report in chunks — artifact part 1, part 2, part 3 — streaming the result as it's generated rather than making you wait for the whole thing.

And notice the shape: an Artifact is itself made of **Parts** — the same TextPart / DataPart / FilePart we met earlier. In `a2a_13` you can see the consumer side: `for artifact in task.artifacts: for part in artifact.parts:` — pulling the durable output back out. That's Key Idea 11: **Messages are the conversation; Artifacts are the deliverables — and both are built from the same Parts.**

---

## SLIDE 21 — Section Divider: Getting Results Back

Part six — Delivery models. Six minutes. The work is running on the server. How does the caller find out what happened? Three ways.

---

## SLIDE 22 — Polling, Streaming, Push

A2A gives you three fundamentally different delivery models, and which one you use depends on how long the work takes.

1. **Polling.** The client asks, "are we done yet?" by calling `tasks/get` with the task id. It gets back the current state — working, working, working, completed. Simple. It's distributed job-polling.
2. **Streaming.** If the agent advertised `streaming: true`, the client calls `message/stream` and the server pushes a live feed over **Server-Sent Events** — SSE. What travels aren't raw text chunks; they're structured events: a `TaskStatusUpdateEvent` when the state changes, a `TaskArtifactUpdateEvent` when a piece of output is ready. State → status update → artifact → artifact → completed.
3. **Push.** For work that takes hours, you don't hold *any* connection. The client registers a webhook up front. The server runs the job, and when it's done, it POSTs the result to the client's callback URL. Fire and forget, with a knock on the door when it's finished.

That's Key Idea 12: **short work → poll; live work → stream over SSE; long or disconnected work → push to a webhook.** Same Task, three ways to hear about it.

---

## SLIDE 23 — Surviving Disconnection

One more piece that shows how much A2A is a *distributed* protocol and not a chat API. Suppose you're streaming and the network drops. The Task doesn't die — the server still holds `task-abc123`. The client can reconnect later and call `tasks/resubscribe` to resume the event stream where it left off.

That's the difference between a job system and a chatbot. A chatbot loses its place when the connection drops. An A2A Task keeps running, and you rejoin it.

[Honesty check for our repo, next slide — because we don't implement all three delivery models, and I want you to know exactly what's real here.]

---

## SLIDE 24 — Honest Coverage: Our Repo vs the Full Spec

Let me be straight about what's *runnable* in this workshop versus what's spec-you-should-know. Credibility comes from honesty.

**Fully implemented and runnable here:**
- Agent Card + discovery via `A2ACardResolver` — `a2a_10`
- Message / Parts / Task object model, typed by the `a2a-sdk`
- `message/send` over JSON-RPC — `a2a_10`, `a2a_13`
- Context-ID threading — `a2a_11`
- Artifacts — `a2a_12`
- Full multi-agent orchestration — `a2a_13`
- A2A **and** MCP in the same agents

**Documented in `notes/a2a_protocols.md`, but not wired up in a demo:**
- SSE streaming and `message/stream` — our cards say `streaming: false`
- `tasks/get` polling — we read the Task returned inline instead
- The full lifecycle state machine — we mostly see `completed`

**Not in the repo at all:**
- `tasks/resubscribe`
- Push notifications / webhooks — cards say `pushNotifications: false`
- Authentication / `securitySchemes`

That's Key Idea 13: **our demos cover the core happy path end-to-end; the advanced async and enterprise pieces are spec knowledge, and knowing the boundary is part of knowing the protocol.**

---

## SLIDE 25 — Section Divider: Orchestration

Part seven — Orchestration. Seven minutes. Now let's put two agents in a room and let them negotiate.

---

## SLIDE 26 — The Matchmaker Pattern — `a2a_13`

This is the payoff demo: `a2a_13_orchestrated_negotiation.py`. The scenario is 742 Evergreen Terrace. A buyer agent wants it cheap. A seller agent wants top dollar. Neither talks to the other directly — a script plays **matchmaker** in the middle.

Here's the flow. The orchestrator:

1. Discovers both agents — fetches the buyer's card and the seller's card via `A2ACardResolver`.
2. Opens two independent conversations — one `buyer_context_id`, one `seller_context_id`.
3. Runs the loop: asks the buyer for an offer, carries that offer to the seller, gets a counter, carries it back to the buyer — round after round — until someone accepts or the loop ends.

Every hop is a `message/send`. Every reply is a Task with an artifact the orchestrator reads and relays. Notice the architecture: the two agents never share memory, never see each other's context, never even know the other's internal state. They only exchange Messages through the protocol boundary. That's Key Idea 14: **an orchestrator coordinates specialist agents purely through A2A messages — no shared state, just the wire.**

---

## SLIDE 27 — The Agent Boundary

Step back and notice what the orchestrator can *not* see. When it hands the seller an offer, the seller might check its floor price, weigh its strategy, call a tool, reason for three steps — and the orchestrator sees none of it. It sees a counter-offer come back. That's all.

This is exactly like microservices. A microservice exposes an API and hides its database, its business logic, its internals. A2A does the same thing for agents. The Agent Card is the API; everything behind it — the LLM, the planner, the memory, the MCP tools — is private implementation.

That's Key Idea 15: **A2A draws an agent boundary — you consume the protocol, not the implementation.** Which means the seller could swap its model, change frameworks, rewrite its tools tomorrow, and the buyer wouldn't need to change a single line.

---

## SLIDE 28 — Section Divider: A2A + MCP Together

Part eight — The two protocols in one system. Four minutes. This is where Module 1 and Module 2 fuse.

---

## SLIDE 29 — Both Protocols, One Agent

Open `negotiation_agents/seller_agent/agent.py`. The seller is an `LlmAgent` with an `MCPToolset` wired to `pricing_server` and `inventory_server` — those are the MCP tools from Module 1. And that same agent is exposed over A2A by `adk web --a2a`.

So trace one offer through the whole stack:

```
Buyer agent  ──A2A (message/send)──►  Seller agent
                                          │
                                          │ MCP (get_minimum_acceptable_price)
                                          ▼
                                      inventory_server
```

The buyer reaches the seller **sideways** over A2A. The seller reaches its pricing floor **downward** over MCP. Two protocols, doing two different jobs, in one request. That's the complete picture this workshop is building toward — Key Idea 16: **A2A connects agents to each other; MCP connects each agent to its tools; real systems use both at once.**

---

## SLIDE 30 — A Word on Security

One thing our demos skip that production never can: **security**. The Agent Card has a slot for it — `securitySchemes` — describing what authentication the agent requires, like OAuth2.

Why does it matter? Because a remote agent is just another distributed service, and you should not assume it's trusted. And there's a subtle identity question hiding here. When a user asks the buyer agent, which asks the seller agent, which reaches a CRM — *whose* identity authorizes that CRM call? The user's? The buyer's? The seller's? A2A gives you the hooks to describe authentication; the actual identity architecture — OAuth, OIDC, workload identities, delegated permissions — is your deployment's job.

Our cards carry no `securitySchemes` because we run on localhost with no auth. That's fine for learning and unacceptable for production. That's Key Idea 17: **treat every remote agent as an untrusted service — authenticate at the boundary, and be deliberate about whose identity flows through the call.**

---

## SLIDE 31 — Section Divider: Synthesis

Part nine — Synthesis. Five minutes. Let's tie the whole lifecycle into one picture.

---

## SLIDE 32 — The Full A2A Lifecycle

Here's the entire protocol on one slide. Read it top to bottom:

```
Agent Card      →  "Who are you, where, what can you do?"
Discovery       →  fetch the card from a well-known URL
Message + Parts →  "Here's the work" (text / data / file)
message/send    →  JSON-RPC over HTTP
Task            →  a durable unit of work, with a state
Context ID      →  thread it into a conversation
Status/Artifacts→  progress and durable results
Poll/Stream/Push→  how you hear back
Completed       →  done
```

That's A2A. Discover, describe, send work, track it, collect results. Everything we did today is one lap around that loop — and `a2a_13` runs the lap over and over until a house gets sold.

---

## SLIDE 33 — The Seventeen Key Ideas

Let's collect them. Read down the list; each one is a choice you'd have to make if you designed an agent-to-agent protocol yourself.

1. Portable agent description beats bespoke glue code.
2. MCP gives an agent hands; A2A gives it colleagues.
3. Public identity is a small JSON card — not the internals.
4. Discovery is "fetch a card from a well-known URL."
5. Capabilities let both sides agree on interaction style.
6. A Message is a role plus typed Parts.
7. Transport is plain JSON-RPC over HTTP; `id` correlates.
8. Messages carry communication; Tasks carry work.
9. A Task is a durable identity for a unit of work.
10. Task ID tracks a job; Context ID threads a conversation.
11. Messages are the conversation; Artifacts are the deliverables.
12. Poll, stream, or push — pick by how long the work runs.
13. Know the boundary between what's built and what's spec.
14. Orchestrators coordinate through the wire, not shared state.
15. A2A draws an agent boundary — consume the protocol, not the code.
16. Real systems use A2A and MCP at once.
17. Treat every remote agent as untrusted; authenticate at the boundary.

Seventeen ideas, one protocol, one negotiation.

---

## SLIDE 34 — Transferable Principles

Four of these are bigger than A2A — they apply to any distributed agent system you build.

1. **Separate description from implementation.** A card, an API, a contract — publish the boundary, hide the internals. This is what lets pieces evolve independently.
2. **Separate communication from work.** Quick replies and long jobs are different animals. Give long work a durable, referenceable identity so nothing has to hold a connection open.
3. **Make delivery a choice, not a default.** Poll, stream, push — match the mechanism to the duration. The same result can arrive three different ways.
4. **Compose protocols; don't reinvent them.** A2A sits on JSON-RPC on HTTP; agents use A2A sideways and MCP downward. You get more power by stacking clean layers than by building one monolith.

Change the domain — real estate, finance, support, logistics — and these still hold. The agents change. The protocol shape doesn't.

---

## SLIDE 35 — Your Turn

Three things to try before next session:

1. Run `a2a_10_wire_lifecycle.py` and read the JSON-RPC dump. Match every field to Slide 14.
2. Run `a2a_11_context_threading.py` and delete the context-id reuse. Watch the seller lose its memory. Then put it back.
3. Run `a2a_13_orchestrated_negotiation.py` and follow one offer from buyer, to orchestrator, to seller, and back. Find where the two context ids live.

And one question to argue with: our cards say `streaming: false`. If you flipped it to true, what would you have to build? That's your bridge into the streaming section of `notes/a2a_protocols.md`.

You've now seen two agents negotiate the price of a house over an open protocol. Go wire up your own. Thank you.

---

*End of script.*
