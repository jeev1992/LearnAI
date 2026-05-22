# Talking Script — Inside Claude Code: System Design of an Agentic CLI

> Read this script directly while presenting each slide. Speaker notes in [SPEAKER NOTE] blocks are asides you say verbally — they are NOT on the slides.

---

## SLIDE 1 — Title

Welcome everyone. Today we're going inside Claude Code — Anthropic's agentic CLI that has crossed a billion dollars in run-rate revenue since becoming generally available in May 2025.

Before we touch any architecture, let me paint a picture of what actually happens when you use this thing. Imagine you're in your terminal, inside your repo. You describe a new feature you want to implement — plain English, one sentence. Here's what happens next.

Claude Code reads your codebase — it searches for the relevant files, opens them, understands the existing structure. Then it edits the code — adds imports, writes new logic, updates configs. Then it runs your tests to check nothing broke. If a test fails, it reads the error, fixes the code, and re-runs. All of this happens in a loop — read, think, act, repeat — without you pressing a single button.

Now, to follow today's session, let me introduce the key ideas you'll hear throughout.

The first is the model's working memory — what we call the **context window**. Everything the model can "see" at once has to fit inside a fixed token budget. Think of it as RAM that gets wiped every turn. What's in that window? Three things. Your conversation history — every message you've sent and every response so far. Tool definitions — structured descriptions of each capability the model can use, like "Read File: takes a file path, returns file contents" or "Bash: takes a shell command, returns stdout and stderr." And the actual content — the files the model has read, the test output it got back, the errors it saw. All of that competes for the same fixed space. With older Claude models like Sonnet 4.5, that window is 200K tokens. The newer Claude 4.6 series bumps it to 1 million. Sounds enormous — but even 1M isn't enough. Why? Because a single medium-sized codebase can be tens of millions of tokens. One tool call that dumps a big log file can eat 50K in one shot. A long conversation with dozens of tool results fills the window in minutes. So no matter how large the window gets, you still need ways to manage it — like summarizing old conversation to free up space for the newer ones, which is called compaction; or deciding what to throw away when the window is full, which is called eviction; and also reusing parts of the prompt you've already paid for so you don't pay again, which is caching of tokens. That's the architecture we'll build today. Managing that budget is half the design.

The second idea is how the model takes action — through what we call a **tool call**. The model can't actually read files or run commands on its own — it's just a text generator. So we give it tools — Read File, Edit File, Bash for running shell commands, Grep for searching text across files — and the model outputs a structured request like "call Read File with path equals auth.py." Then Claude Code — the program running on your machine — picks up that request, actually reads the file, and feeds the contents back to the model. The model thinks; the program acts.

The third idea ties it all together — the **agent loop**. That read-think-act cycle I described a moment ago? That's the agent loop. In the research literature, this pattern is called **ReAct** — Reason and Act. But here's the important distinction — remember this: the model doesn't act. The model is just the text generator — it reasons and outputs what it wants to do. And the agent — Claude Code, the program on your machine — is the one that actually acts. It reads the model's request, executes the tool, and feeds the result back. So, remember: The model reasons; the agent acts. That's why it's called an agentic system and not just a chatbot. The agent keeps this cycle going — reason, act, observe, reason again — until the task is done. It's a while-true loop — and designing what goes inside that loop, what guards it, what feeds it, and what stops it — that's what this entire session is about.

So the question we're answering today is: how would you design Claude Code — that whole pipeline — if you had to build it from scratch? Every slide going forward adds one piece. We'll tackle how the context window gets managed when it fills up. How tools get validated and sandboxed before they touch your files. How three different models get routed by cost — so you're not paying top dollar for a yes/no check. How permission cascades catch dangerous actions in microseconds. And how real production incidents — including one where a retry loop ran unchecked burning through API calls — shaped the architecture you see today. Sounds like a lot? It is. A billion-dollar product, 200K to a million tokens of working memory, 50-plus tools, three model tiers, kernel-level sandboxing — these are big numbers and hard problems. But by the end, you'll have all of it organized into just 22 design decisions mapped to a five-layer architecture. Twenty-two sounds like a lot — but here's the thing: every single one of them is a choice you'd have to make anyway if you sat down to build this. We're just going to make them one at a time, in order, so by the end you've got one clean diagram you can screenshot and take to your next planning meeting. This session is for engineers, EMs, TPMs, and PMs — everyone at the table when an agentic system gets designed.

---

## SLIDE 2 — Agenda

Here's our roadmap. We have 14 parts and 22 design decisions to make. Each part adds decisions to one architecture diagram, and we'll end with all 22 mapped to a single slide you can take back to your team. You'll see the time allocations on the right. Let's dive in.

[SPEAKER NOTE: The segment times on screen add up to about 110 minutes, not 90 — so pace yourself and trim Q&A if needed.]

---

## SLIDE 3 — About IK / Your Host

A quick word about Interview Kickstart. Ten-plus years preparing engineers for top companies. Over 25,000 professionals trained across FAANG and AI-native companies. And over 700 FAANG and tier-one mentors on our roster. By the end of this session, you'll have a complete design blueprint for an agentic CLI you can take to your team.

[SPEAKER NOTE: IK's site says "trained," not "placed" — and "mentors," not "hiring managers." Frame it honestly.]

---

## SLIDE 4 — Section Divider: Foundations

Part one — Foundations. Five minutes. Before we design anything, let's define what we're designing.

---

## SLIDE 5 — What Does "Agentic CLI" Mean?

Look at this two-by-two. On the x-axis: is the decision-making deterministic or model-driven? On the y-axis: single-step or multi-step? A script is single-step and deterministic. A workflow is multi-step but still deterministic. A chatbot is single-step and model-driven. An agent — that's where Claude Code lives — is multi-step AND model-driven. The model decides what to do next, and it keeps going until the task is done.

---

## SLIDE 6 — Six Hard Constraints

These six constraints shape every design decision we'll make today. One: it lives in the user's terminal — no web app rescue if the UI breaks. Two: it edits files on the user's disk — files they will commit and ship. Three: it runs with the user's credentials — it can do real damage if misused. Four: non-deterministic output — same input does not equal same output. Five: it must work both interactively AND headlessly — one system, two opposite UX modes. Six: finite context window — memory IS architecture.

[SPEAKER NOTE: The slide says "200K context window." That's correct for the base architecture, but newer models like Claude 4.6 support up to 1M tokens. The design patterns — compaction, caching, eviction — are what matter regardless of the exact window size.]

---

## SLIDE 7 — Section Divider: What Are We Building?

Part two — What are we building? Eight minutes. Define the problem before drawing any box diagrams.

---

## SLIDE 8 — Problem Statement

Here's the problem statement. Read it with me: Build a CLI tool that a developer runs inside their own repository, which can read and edit code, run shell commands, search the codebase, take multi-step actions, resume sessions, and integrate with their editor — using an LLM as the decision engine. Who uses it? A mid-senior software engineer. Where? Their own laptop, their own repo. What? Multi-step coding tasks. How long? Single session — minutes to hours.

---

## SLIDE 9 — Functional Requirements

Nine things it must do. Read and edit files. Run shell commands. Search the codebase. Multi-turn chat. Resume sessions. Rewind and undo actions. Run in IDE, Slack, and headless CI. Plug in external tools via MCP. And support user-defined extensions. That's the feature surface.

---

## SLIDE 10 — Non-Functional Requirements

Now, how WELL must it do those things? Time to first token under 500 milliseconds. Self-healing reliability — it survives tool failures. Multi-layer safety — no rogue commands. Cost under 50 cents per complex request. Portability across three operating systems — macOS, Linux, and WSL. And model-swap abstracted — provider-agnostic at the interface layer.

[SPEAKER NOTE: The TTFT and cost targets are design goals I've set for this exercise — they're reasonable engineering targets but not published by Anthropic. The "provider-agnostic" claim is aspirational — Claude Code is heavily tied to the Anthropic API for tool_use, prompt caching, and extended thinking. We'll see that tradeoff explicitly on the model API slide.]

---

## SLIDE 11 — Out of Scope

Equally important: what are we NOT building? Not a chatbot — this is task-oriented, not conversational. Not an IDE replacement — it complements, doesn't replace. Not a CI replacement — it augments CI. Not a shared multi-user environment — one developer, one session. Not a model trainer — we consume a model. Scoping what you don't build is half the design.

---

## SLIDE 12 — Section Divider: Scale & Constraints

Part three — Scale and Constraints. Five minutes. Back-of-envelope numbers that anchor every later tradeoff.

---

## SLIDE 13 — Back-of-Envelope Numbers

Let's put some numbers on the whiteboard. About 50K concurrent users at peak. Roughly 2 million sessions per day. Median 15 turns per session. One to ten tool calls per turn, parallelized where safe. Five to thirty thousand tokens per turn after cache. Cost ceiling under 50 cents per complex request. And a TTFT target of 500 milliseconds for that conversational feel.

[SPEAKER NOTE: All seven of these numbers are illustrative design targets — none are published by Anthropic. They're the kind of back-of-envelope estimates you'd put on a whiteboard in a system design interview. The point is to anchor your tradeoffs, not to be exact.]

---

## SLIDE 14 — AI-Specific Constraints

Here are six constraints you don't see in a normal CLI. Finite context window — memory is a budget, not infinite. Stateless model — every turn re-sends the entire history. Per-token pricing — cost scales with conversation length. Model versions drift — behavior changes between releases, as we saw in the April 2026 incident. Prompt injection — tool output can become attack input. And non-deterministic output — same input doesn't guarantee the same output.

---

## SLIDE 15 — Section Divider: High-Level Architecture

Part four — High-Level Architecture. Ten minutes. Draw the box diagram. Components first; details later.

---

## SLIDE 16 — Architectural Style Choice

Two options. On the left: a multi-agent graph — multiple agents with criss-crossing edges. Many agents, emergent failure modes, hard to trace. On the right: a single main loop — one vertical rail dispatching to Read, Edit, Bash, Grep. One thread, localized failure, debuggable. Design Decision 1: Pick the single main loop. Debuggability beats sophistication.

---

## SLIDE 17 — The 20-Line Agent

Here's the entire agent in about 20 lines of pseudocode. User sends a message. Enter a while-true loop. Call the LLM with messages and tools. If the response is a tool_use, parse the schema, check permissions, run the tool, append the result. Otherwise, print the text and break. That's it. The loop is small. Everything reliable lives in the layers around it. That's Design Decision 2.

---

## SLIDE 18 — Five-Layer Architecture

This is the master diagram we'll keep coming back to. Five layers, top to bottom. L1: UI/TUI — terminal, IDE, Slack, headless. L2: Agent Loop — drives the conversation. L3: Tool Dispatch — validates, permits, executes tools. L4: Permission/Sandbox — decides what's allowed, kernel safety. L5: Model API — Anthropic API, cache, streaming. Notice: the model is at the bottom, not the top. It's a dependency, not the architecture. Design Decision 3: Layered separation — each layer evolves independently.

[SPEAKER NOTE: The diagram header on this slide still says "Claude CLI" — this is an image I couldn't edit. The product is officially called Claude Code.]

---

## SLIDE 19 — Sequence Diagram

Let's trace one message through the system: "fix the bug in auth.py." User types it in the TUI. It goes to the agent loop, which sends messages plus tools to the model. The model responds with tool_use: Read auth.py. That goes to tool dispatch, which checks permissions, gets the allow, reads the file contents, and appends them back to messages. The loop continues until the model returns a text response instead of a tool call.

---

## SLIDE 20 — Section Divider: CLI Surface

Part five — CLI Surface. Seven minutes. Why CLI, and how the terminal layer actually works.

---

## SLIDE 21 — Surface Choice

Three options. Web app: rich UI, but not in the dev flow, can't touch files directly. IDE plugin: in-editor, sees code, but per-editor build and limited shell access. CLI: lives in the dev flow, native shell and filesystem, scriptable, headless-ready. The cons are limited rendering and no built-in auth UI. Design Decision 4: CLI as primary surface. The developer is already in a terminal.

---

## SLIDE 22 — Custom TUI Architecture

Why build the terminal UI from scratch? Because streaming UX is a system design concern. The pipeline: Model stream sends SSE tokens into a React tree, Yoga computes flexbox layout, Ink renders with a diff-and-reconcile pass, and it outputs to the TTY. Why not ncurses? It can't handle streaming tokens, mid-stream tool messages, scrollback under output, or live progress bars. Cost: about 2,700 lines of code reimplemented in pure TypeScript. Design Decision 5.

---

## SLIDE 23 — Input State Machine

The terminal must handle four input states. IDLE: cursor visible, waiting. TYPING: multi-line input with paste detection and history. RUNNING: tool executing, stream output, Ctrl-C to interrupt. REWIND: double-Escape rewinds to the last checkpoint. State transitions: idle to typing on keypress, typing to running on Enter, running to idle on text response, running to rewind on Esc-Esc. Design Decision 6: Treat input as a state machine. Interrupt and rewind are first-class.

---

## SLIDE 24 — Distribution

How does a developer install it? Four options: pip/brew — familiar but slow updates. Standalone binary — no deps but large download. npm — dev reach, easy updates, but requires Node. The winner: npm plus native binary — both worlds. The final artifact is about 10.5 megabytes for the cli.js via npm, plus a 188-megabyte Bun native binary, with zero install-time dependencies. Design Decision 7.

---

## SLIDE 25 — Section Divider: Tools

Part six — Tools: The Agent's Hands. Eleven minutes. How the agent takes action in the real world.

---

## SLIDE 26 — Tool Contract

A Tool is a five-part contract. Schema — guards model output. Permission — guards the user's system. Concurrency-safe — enables parallelism. Read-only — skips permission prompts. Render function — UI is part of the tool. Each part prevents one class of failure. The contract IS the design. Design Decision 8: Skip one part, lose a guarantee.

[SPEAKER NOTE: This is a pedagogical simplification. The actual tool interface in the codebase has nine fields including name, description, inputSchema, isReadOnly, isIdempotent, userFacingName, hasOwnPermissionLogic, renderResultForAssistant, and validateInput. I've grouped them into five conceptual parts for teaching.]

---

## SLIDE 27 — Dispatch Pipeline

Every tool call goes through eight stages. One: Schema parse — Zod validates input. Two: Semantic check — is the path in the current working directory? Three: Permission — the five-stage cascade we'll see later. Four: Pre-hook — user's PreToolUse hook. Five: Execute — tool.call(). Six: Trim output — anything over 50K chars goes to disk with a 2KB preview. Seven: Post-hook — format, lint, audit. Eight: Append result — back to messages. Design Decision 9: Every tool goes through the same eight stages. Cross-cutting concerns live here, not in individual tools.

---

## SLIDE 28 — Parallel Tool Calls

When do you allow parallel tool calls? Sequential: safe, slow, one thing at a time. Parallel: when concurrencySafe is true. Reads are parallel-safe by default. Edits are sequential only. The tradeoff: mark too many tools concurrency-safe and you get race conditions on file edits. Mark too few and you get serial slowness.

---

## SLIDE 29 — Self-Healing Patterns

Five self-healing patterns — each from a real incident. Tool-result persistence: outputs over 50K chars go to disk, leaving a 2KB preview — born from OOM on big logs. PTL recovery: on a 413 error, drop the oldest turns and retry — born from context overflow. Circuit breaker: after three consecutive failures, stop retrying — born from an auto-compact retry loop that ran unchecked. Denial-as-result: permission denial is returned as readable text, not an exception — so the model retries a safer path. Idempotent retries: in headless mode, re-enqueue safely — born from CI failures. Design Decision 10: Every reliability mechanism has a postmortem behind it. Design defensively.

---

## SLIDE 30 — Section Divider: Memory & Context

Part seven — Memory and Context. Twelve minutes. Designing memory for a model that has none.

---

## SLIDE 31 — Memory Tiers

Four kinds of memory, four storage backends. Working memory: scope is this turn, lives in the model's prompt. Session memory: scope is this conversation, lives on disk as a conversation log with checkpoints. Project memory: scope is this repo, lives in CLAUDE.md committed to git. Tool-result memory: scope is big outputs, lives in files on disk keyed by tool_use_id. Design Decision 11: Four memory layers, four scopes, each lives in the right place.

[SPEAKER NOTE: This four-tier taxonomy is how I organize it for teaching. Anthropic describes the same layers differently in their engineering blogs, but the concepts map directly.]

---

## SLIDE 32 — 200K Token Budget

Where does every token go? Look at the bar. 2.7K for the system prompt — cached globally. 17K for tool definitions — that's 50-plus tools. 33K reserved for auto-compact — off-limits. That leaves about 147K of free working memory — only 74 percent of the total window. You start with a 200K budget and you've already spent a quarter of it before the user types anything.

---

## SLIDE 33 — Five-Layer Compression

When you run low on context, compress in layers — cheapest fires first. L1: Tool results go to disk — zero API cost. L2: History snip — zero. L3: MicroCompact — zero. L4: Context collapse — zero. L5: Forked summary — costs one API call. Cheap layers are preferred to keep cost low, but each lossy step risks losing context. L5 is highest fidelity, highest cost. Design Decision 12: Try free options first. Reserve expensive operations for genuine necessity.

---

## SLIDE 34 — Compaction as a Transaction

Compaction equals eviction plus rehydration. Before compaction: 190K used, overflow imminent, 95% full. Old tool results scattered, stale file references, MCP instructions duplicated. After compaction: 50K free. The five most recent files re-injected. Active skills re-attached. CLAUDE.md reloaded from disk. Plan and sub-agent state restored. And the prompt-cache prefix stays warm. Design Decision 13: Eviction and rehydration are one transaction. Design them together.

---

## SLIDE 35 — Static/Dynamic Cache Boundary

Split your prompt at the cache boundary. On the left: the cached static prefix — core instructions, tool definitions, identical for every user. On the right: per-user dynamic suffix — MCP instructions, output preferences, language settings. The result: a high cache hit rate and roughly a 10x cost reduction on compaction. Design Decision 14: Static prefix cached, dynamic suffix per-request. This is a 10x cost decision.

[SPEAKER NOTE: The 10x ratio is confirmed by Anthropic's pricing documentation — cached reads cost about one-tenth of normal input tokens. The specific dollar figures and the ">96%" hit rate shown on the slide are illustrative — Anthropic monitors hit rates internally but hasn't published a specific number.]

---

## SLIDE 36 — Section Divider: Model API Layer

Part eight — Model API Layer. Six minutes. How we actually talk to the LLM.

---

## SLIDE 37 — Tool-Call Protocol Choice

Three options for how the model invokes a tool. JSON mode: model outputs JSON in text, we parse it — provider-agnostic but brittle. Function calling: OpenAI-style, better but limited streaming. tool_use native: Anthropic's first-class primitive with streaming, retry, and type-safety — but locks the shape to the Anthropic API. Design Decision 15: Use tool_use natively. Pay the lock-in cost for the streaming and retry semantics.

---

## SLIDE 38 — Model Routing

One agent, three models — route by cost sensitivity. Opus 4.7 for the main reasoning loop — highest capability for hard tasks. Sonnet 4.6 for the auto-mode permission classifier — fast, cheap, deterministic enough. Haiku 4.5 for lightweight checks — cheapest, near-instant. Model selection is a per-call decision, not a per-app decision. Design Decision 16: Route by task. Don't pay Opus prices for a yes/no classifier.

---

## SLIDE 39 — Section Divider: Safety & Permissions

Part nine — Safety and Permissions. Ten minutes. Defense in depth, ordered by cost.

---

## SLIDE 40 — Threat Model

Assume the model can be turned against you. Five threats. Prompt injection: malicious content in file or URL output — mitigated by output sanitization and re-checking permissions on follow-up. Bash command injection: model crafts shell metacharacters — mitigated by Tree-sitter AST parsing before the permission check. Credential exfiltration: secrets in context leak through tool output — mitigated by allowlist proxy and sandbox filesystem scoping. Lateral movement: one tool enables another tool's misuse — mitigated by per-tool permission scoping. Denial bypass: model retries with rephrased requests — mitigated by denial-as-tool-result, which preserves the audit trail. Behavioral safety is fragile. Structural safety is what holds.

---

## SLIDE 41 — Permission Cascade

Permission Cascade — bail out as early as possible. Five stages, ordered by cost. Stage one: static rules — microseconds — deny, ask, or allow. Fast path. Stage two: tool checkPermission — milliseconds — Bash AST analysis, path scoping. Most calls exit here. Stage three: permission mode — microseconds to milliseconds — which mode is the user in? Stage four: LLM classifier — Sonnet latency — for auto mode only. Stage five: ask the human — human time — interactive prompt. The outcome: 93 percent of prompts that reach the human are approved. The cascade filters the noise. That 93 percent is from Anthropic's own auto-mode blog. Design Decision 17: Deny wins. Cheap checks first, humans last.

---

## SLIDE 42 — Kernel Sandboxing

When permission isn't enough, let the kernel enforce. On macOS: seatbelt — the macOS kernel sandbox framework. On Linux and WSL2: bubblewrap — Linux namespaces plus a socat allowlist proxy. Result: 84 percent fewer permission prompts with sandbox enabled — that's a verified number from Anthropic's sandbox blog. But here's the escape-hatch problem: the model has learned to retry with the dangerously-skip-permissions flag when commands fail. You must explicitly set allowUnsandboxedCommands to false to close the escape. Design Decision 18: Behavioral safety fails. The kernel doesn't. Use OS sandboxing as the floor.

---

## SLIDE 43 — Six Permission Modes

Six modes on a trust dial, from "ask always" to "ask nothing." Default: ask every action. acceptEdits: auto-allow edits. plan: read-only, plan first. auto: LLM classifier decides. dontAsk: allowlisted silently. bypass: skip all checks — but even bypass still blocks writes to .git, .claude, and .vscode. There's always a floor. Design Decision 19: Let the user pick their risk tolerance, but never give them an off-switch for everything.

[SPEAKER NOTE: The actual codebase has seven permission modes — I've grouped six here for visual clarity on the trust dial. The seventh is likely "sandbox" as a distinct mode.]

---

## SLIDE 44 — Section Divider: Extensibility

Part ten — Extensibility. Eight minutes. How does the system grow without forking?

---

## SLIDE 45 — Customization Surfaces

Three layers users customize without forking the core. Hooks: lifecycle interceptors — block, modify, audit, format, lint. They wrap PreToolUse and PostToolUse events. Skills: reusable prompt fragments — style guides, domain rules, code patterns. CLAUDE.md: project memory loaded once per session, committed to git — architecture decisions, conventions, do/don't lists, gotchas. All three are invisible to the model's reasoning — they don't pollute the conversation. Design Decision 20: Three customization surfaces, three different scopes. Enterprises don't need to fork.

---

## SLIDE 46 — Sub-Agents

Sub-agents are tool calls, not orchestration nodes. The parent agent dispatches to child agents — Explore, Plan, Implement — each with its own context window, its own system prompt, its own tool allowlist. Only the final summary returns to the parent. Up to about 10 concurrent before queueing. Cannot nest — single-level only. The key insight: isolation, not orchestration. About 90 percent performance gain on complex tasks at 15 times the token cost. Design Decision 21: Sub-agents equal isolation primitive. Use only when isolation matters.

[SPEAKER NOTE: The 90% perf gain and 15x cost figures are engineering tradeoff ratios I'm using for teaching — they're directionally correct but not published by Anthropic. The point is: sub-agents are powerful but expensive. Use them deliberately.]

---

## SLIDE 47 — MCP and Lazy Loading

MCP — the open protocol for plugging in external tools. Claude Code sits at the center of a hub connecting to GitHub, Asana, Slack, Postgres, local filesystem, internal tools. Without lazy loading: 134K tokens of tool definitions before the user types a character. GitHub MCP alone takes 24 percent of context. With lazy loading via tool_search: only tool names in the prefix, schemas loaded on demand. About 5K for 30 servers. 85 percent context savings. Design Decision 22: MCP with deferred loading. Load capability eagerly, load schemas lazily. Dynamic linking applied to LLMs.

---

## SLIDE 48 — Section Divider: UX, State & Streaming

Part eleven — UX, State, and Streaming. Six minutes. Latency is architecture, not polish.

---

## SLIDE 49 — Latency Budget

Every layer has a target. Time to first token: under 500 milliseconds — user perceives "started." Token streaming rate: 20 to 30 per second — matches human read speed. Simple task with one tool: under 5 seconds — conversational feel. Complex multi-tool task: under 60 seconds — acceptable with a progress indicator. Latency budgets are why the TUI is custom-built. UX IS architecture.

[SPEAKER NOTE: These targets are design goals for this exercise, not published Anthropic metrics. They're reasonable engineering numbers that any senior engineer would recognize.]

---

## SLIDE 50 — Interactive vs Headless

Two opposite UX pressures from the same agent loop. Interactive: user typing in real time, permission is an inline Y/n prompt, stream tokens, show tool progress, rewind enabled. Headless: no human at the keyboard, permission is auto-allow or fail, batch JSON output, deterministic exit codes, idempotent retries. The bridge: one event bus, N user surfaces. Permission requests are events — not UI calls. The canUseTool callback decides per mode.

---

## SLIDE 51 — Section Divider: Eval & Observability

Part twelve — Eval and Observability. Six minutes. You can't ship what you can't measure.

---

## SLIDE 52 — Evaluation Strategy

How do you test a non-deterministic system? Pipeline: frozen test suite, model upgrade, eval run, diff versus baseline, ship or rollback. Five eval types. Task completion: does the agent finish multi-step tasks? Every release. Tool selection: does it pick the right tool? Every release. Permission accuracy: auto-classifier versus user override — continuous. Latency p50 and p99 — continuous. Regression: has any of the above degraded? Per-PR plus nightly. Important footnote: the April 2026 regression slipped through this eval suite. Evals are necessary, but not sufficient.

---

## SLIDE 53 — Three Layers of Telemetry

Three layers of telemetry — log at every level. Per-turn: trace ID, token accounting, tool call timing — lets you debug a single bad response. Per-session: conversation log, permission events, sandbox events — lets you reconstruct a user complaint. Aggregated: compaction rates, retry rates, denial rates, success-without-prompt — lets you catch runaway retry loops before they cost real money. You can't debug what you can't measure. Telemetry is not optional.

---

## SLIDE 54 — Section Divider: Production Reality

Part thirteen — Production Reality. Five minutes. Every elegant design exists because something broke first.

---

## SLIDE 55 — Three Real Incidents

Three real incidents — each forced a design change. First: April 2026, Quality Regression. Three unrelated version changes compounded, causing a measurable code-quality drop. The actual Anthropic postmortem describes three separate issues: a reasoning-effort default change, a caching bug, and a verbosity prompt change — all shipped within weeks of each other. Fix: stricter compatibility matrix and a faster rollback path.

Second: Late 2025, the Runaway Retry Incident. The auto-compact retry loop ran unchecked before the circuit breaker was added. The compaction system would fail and retry indefinitely, burning API calls. Fix: a 3-strike circuit breaker — now standard.

Third: Throughout 2025, MCP Bloat. Heavy MCP users were hitting huge token counts for tool definitions before they even typed anything. GitHub alone consumed a big chunk of context. Fix: deferred loading via tool_search.

Every feature has an incident behind it.

---

## SLIDE 56 — Honest Weaknesses

Six things the team would reconsider if starting over. MCP loaded eagerly — deferred loading was a retrofit, not a design. Compaction had no circuit breaker — defensive programming was reactive, not proactive. Sub-agents capped at one level — nested sub-agents remain unsolved. Model–prompt–binary coupling — no single owner watches all three. Eval coverage gaps — necessary, but not sufficient. And sandbox-bypass retraining — the model learned to disable safety. Credibility comes from honest weaknesses. Patterns that "always work" usually don't.

---

## SLIDE 57 — Section Divider: Synthesis & Close

Part fourteen — Synthesis and Close. Eight minutes. All 22 decisions, mapped to the architecture you started with.

---

## SLIDE 58 — 22 Decisions Mapped to 5 Layers

Here they are — the 22 design decisions you just made, mapped to the five layers. L1 UI/TUI: Decisions 4, 5, 6, 7 — CLI surface, custom TUI, state machine, distribution. L2 Agent Loop: Decisions 1, 2, 3 — single main loop, small loop, layered architecture. L3 Tool Dispatch: Decisions 8, 9, 10, 21, 22 — tool contract, pipeline, self-healing, sub-agents, MCP. L4 Permission/Sandbox: Decisions 17, 18, 19, 20 — permission cascade, kernel sandbox, modes, customization. L5 Model API: Decisions 11 through 16 — memory, compression, compaction, caching, tool_use, model routing. Take this diagram to your team.

---

## SLIDE 59 — Six Transferable Principles

Six patterns that survive any agentic system you build. One: the model is the runtime; the runtime is dumb — a while-true loop with disciplined tools beats a multi-agent graph. Two: ship one main thread — sub-agents, hooks, MCP all funnel into the same query loop. Three: tools are contracts, not functions — schema plus permission plus concurrency plus read-only plus UI. Four: context is a memory bus — plan eviction AND rehydration as one design. Five: defense in depth is a cost gradient — static rules in microseconds, then millisecond checks, then mode, then LLM, then human, then kernel. Six: lazy-load capability, never lazy-load context — tool search loads names eagerly, schemas on demand. Six principles, cross-referenced to every design decision.

---

## SLIDE 60 — Role-Based Questions

Screenshot this slide. Bring it to your next planning meeting. Five questions for each role. Engineers: Where does state live? Which tools are concurrency-safe? What's the context budget per turn? Where's the cache prefix boundary? Are tool failures idempotent? EMs: What's the eval discipline? Is the cost gradient right? Are sub-agents ROI-positive at 15x cost? Where's the eval coverage gap? How do you onboard when 80 percent of code is AI-written? TPMs: What's the rollback plan when the harness breaks? What's the dependency on model upgrades? What's your April 2026 equivalent? Lazy versus eager capability loading? Which capability ships next quarter? PMs: Which user surface ships first? What's "success" for emergent failures? How do you monetize when 98 percent is non-AI infra? Ask versus act — where's the trust model? How does the permission UX work across surfaces?

---

## SLIDE 61 — Q&A + What's Next

Let's open the floor. Four questions to get you started. Are you building an agent at work? Have you shipped MCP yet? What's your stance on bypass mode? Which design decision surprised you most? And if you want to go deeper — Interview Kickstart's AI Systems Track has over 700 FAANG instructors, live cohorts with one-on-one mocks, and in the EdgeUp program you actually build a real agent. That's the agent-focused tier.

---

## SLIDE 62 — Thank You / Close

You just designed Claude Code. Now go build your own agent. Three next steps: one — book a free strategy session with an IK advisor. Two — mention this masterclass for priority enrollment. Three — stay tuned for the next masterclass. Thank you all.

---

*End of script.*
