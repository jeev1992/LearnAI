# Talking Script — Inside Claude Code: System Design of an Agentic CLI

> Read this script directly while presenting each slide. Speaker notes in [SPEAKER NOTE] blocks are asides you say verbally — they are NOT on the slides.

---

## SLIDE 1 — Title

Welcome everyone. Today we're going inside Claude Code — Anthropic's agentic CLI that has crossed a billion dollars in run-rate revenue since becoming generally available in May 2025.

Before we touch any architecture, let me paint a picture of what actually happens when you use this thing. Imagine you're in your terminal, inside your repo. You describe a new feature you want to implement — plain English, one sentence. Here's what happens next.

Claude Code reads your codebase — it searches for the relevant files, opens them, understands the existing structure. Then it edits the code — adds imports, writes new logic, updates configs. Then it runs your tests to check nothing broke. If a test fails, it reads the error, fixes the code, and re-runs. All of this happens in a loop — read, think, act, repeat — without you pressing a single button.

Now, to follow today's session, let me introduce the key ideas you'll hear throughout.

The first is the model's working memory — what we call the **context window**. Everything the model can "see" at once has to fit inside a fixed token budget. Think of it as RAM that gets wiped every turn. What's in that window? Three things. Your conversation history, which is every message you've sent and every response you received so far. Then Tool definitions which is structured descriptions of each capability the model can use, like "Read File which takes a file path, and returns file contents" OR "Bash: takes a shell command, and returns stdout and stderr." And lastly, the actual content — the files the model has read, the test output it got back, the errors it saw. All of that competes for the same fixed space. With older Claude models like Sonnet 4.5, that window is 200K tokens. The newer Claude 4.6 series bumps it to 1 million. Sounds enormous — but even 1M isn't enough. Why? Because a single medium-sized codebase can be tens of millions of tokens. One tool call that dumps a big log file can eat 50K in one shot. A long conversation with dozens of tool results fills the window in minutes. 

So no matter how large the window gets, you still need ways to manage it — like summarizing old conversation to free up space for the newer ones, which is called compaction; or deciding what to throw away when the window is full, which is called eviction; and also reusing parts of the prompt you've already paid for so you don't pay again, which is caching of tokens. That's the architecture we'll build today. Managing that budget is half the design.

The second idea is how the model takes action — through what we call a **tool call**. The model can't actually read files or run commands on its own — it's just a text generator. So we give it tools — Read File, Edit File, Bash for running shell commands, Grep for searching text across files — and the model outputs a structured request like "call Read File with path equals auth.py." Then Claude Code — the program running on your machine — picks up that request, actually reads the file, and feeds the contents back to the model. The model thinks; the program acts.

The third idea ties it all together — the **agent loop**. That read-think-act cycle I described a moment ago? That's the agent loop. In the research literature, this pattern is called **ReAct** — Reason and Act. But here's the important distinction — remember this: the model doesn't act. The model is just the text generator — it reasons and outputs what it wants to do. And the agent — Claude Code, the program on your machine — is the one that actually acts. It reads the model's request, executes the tool, and feeds the result back. So, remember: The model reasons; the agent acts. That's why it's called an agentic system and not just a chatbot. The agent keeps this cycle going — reason, act, observe, reason again — until the task is done. It's a while-true loop — and designing what goes inside that loop, what guards it, what feeds it, and what stops it — that's what this entire session is about.

So the question we're answering today is: how would you design Claude Code — that whole pipeline — if you had to build it from scratch? Every slide going forward adds one piece. We'll tackle how the context window gets managed when it fills up. How tools get validated and sandboxed before they touch your files. Why the system uses three different models — a powerful one for hard reasoning, a fast one for quick checks, and a cheap one for simple yes/no decisions — so you're not spending top dollar on every call. Sounds like a lot? Well, it is. A billion-dollar product, 200K to a million tokens of working memory, 50-plus tools, three model tiers, kernel-level sandboxing — these are big numbers and hard problems. But by the end, you'll have all of it organized into just 22 design decisions mapped to a five-layer architecture. Twenty-two design decisions sounds like a lot — but here's the thing: every single one of them is a choice you'd have to make anyway if you sat down to build this. We're just going to make them one at a time, in order, so by the end you've got a clear understanding of what goes inside Claude Code — or any coding agent like it. This session is for engineers, EMs, TPMs, and PMs — everyone at the table when an agentic system gets designed.

---

## SLIDE 2 — Agenda

Here's our roadmap. We have 14 parts — each one covers a different aspect of the system. We'll start with foundations and requirements, then move into architecture, the CLI surface, tools, memory management, the model API, safety and permissions, extensibility, UX and streaming, evaluation, and finally real production incidents that happened with Claude Code. Along the way, we'll make 22 design decisions. Each part adds decisions to one architecture diagram, and we'll end with all 22 mapped to a single slide at the end.

---

## SLIDE 3 — About IK / Your Host

A quick word about Interview Kickstart. Ten-plus years preparing engineers for top companies. Over 25,000 professionals trained across FAANG and AI-native companies. And over 700 FAANG and tier-one mentors on our roster. By the end of this session, you'll have a complete design blueprint for an agentic CLI you can take to your team.

[SPEAKER NOTE: IK's site says "trained," not "placed" — and "mentors," not "hiring managers." Frame it honestly.]

---

## SLIDE 4 — Section Divider: Foundations

Part one — Foundations. Five minutes. Before we design anything, let's define what we're designing.

---

## SLIDE 5 — What Does "Agentic CLI" Mean?

Look at this two-by-two matrix. Two dimensions. First: how many steps does it take — is it a single action or a multi-step sequence? That's your columns. Second: who makes the decisions? If the code follows a fixed set of if-else rules — same input always gives the same output — that's deterministic. But if an AI model looks at the situation and decides what to do, it might choose differently next time even with the same input — that's model-driven or non-deterministic or also called a stochastic. That's your rows. 

Bottom-left: a script — single-step, deterministic. Bottom-right: a workflow — multi-step but still deterministic. Top-left: a chatbot — single-step and model-driven. Top-right: an agent — that's where Claude Code lives — multi-step AND model-driven. The model decides what to do next, and it keeps going on until the task is done.

---

## SLIDE 6 — Six Hard Constraints

These six constraints shape every design decision we'll make today. One: it lives in the user's terminal — or as an extension in VS Code — so there's no rich web UI to fall back on if something breaks visually. Two: it edits files on the user's disk — files they will commit and ship. Three: it runs with the user's credentials — it can do real damage if misused. Four: non-deterministic output — you can ask the model to summarize the same text twice and get two different but perfectly valid summaries each time. That's the stochastic nature of LLMs — same input does not guarantee the same output. Five: it can work in two completely different modes — interactively, where you're sitting at your keyboard chatting with it and approving actions, AND headlessly, where it's running on its own inside a CI pipeline like GitHub Actions with nobody there to click "yes." Same codebase, two opposite experiences. Six: finite context window — the model can only "see" so much at once, so how you manage that limited memory isn't a side concern, it's a core part of the architecture.

---

## SLIDE 7 — Section Divider: What Are We Building?

Part two — What are we building? Eight minutes. Define the problem before drawing any box diagrams.

---

## SLIDE 8 — Problem Statement

Here's the problem statement. Read it with me: Build a CLI tool that a developer runs inside their own repository, which can read and edit code, run shell commands, search the codebase, take multi-step actions, resume sessions, and integrate with their editor — using an LLM as the decision engine. Who uses it? A mid-senior software engineer. Where? Their own laptop, their own repo. What? Multi-step coding tasks. How long? Single session — minutes to hours.

---

## SLIDE 9 — Functional Requirements

Since we are doing System design here, so we have to start with functional and non-functional requirements.

Nine things it must do.

1. Read and edit files — open a source file, change a function, update a config.
2. Run shell commands — like running your tests, installing packages, or checking build output.
3. Search the codebase — find every place a function is called or a variable is used.
4. Multi-turn chat — ask a follow-up question and it remembers the whole conversation so far.
5. Resume sessions — close your terminal, come back tomorrow, and pick up right where you left off.
6. Rewind and undo actions — if the agent made a bad edit three steps ago, roll back to that point.
7. Run in IDE, Slack, and headless CI — same agent, different surfaces.
8. Plug in external tools via MCP — connect to GitHub, Jira, a database, or your own internal APIs.
9. Support user-defined extensions — hooks, custom rules, project-specific instructions without touching the core code.

That's the feature surface.

---

## SLIDE 10 — Non-Functional Requirements

Now, how WELL must it do those things? These are illustrative requirements — they may not be exactly what Claude Code uses internally, but they're the kind of targets you'd set if you were designing this system yourself. Time to first token under 500 milliseconds. Self-healing reliability — it survives tool failures. Multi-layer safety — no rogue commands. Cost under 50 cents per complex request. Portability across three operating systems — macOS, Linux, and Windows. And model-swappable — the system is designed so you could swap in a different AI model without rewriting the whole application.

---

## SLIDE 11 — Out of Scope

Equally important: what are we NOT building? Not a chatbot — this is task-oriented, not JUST conversational. Not an IDE replacement — it complements, doesn't replace. Not a CI replacement — it augments CI. Not a shared multi-user environment — one developer, one session. Not a model trainer — we consume a model. 

---

## SLIDE 12 — Section Divider: Scale & Constraints

Part three — Scale and Constraints. Five minutes. Back-of-envelope numbers that anchor every later tradeoff.

---

## SLIDE 13 — Back-of-Envelope Numbers

Let's put some numbers on the whiteboard. Again, these are illustrative — not published by Anthropic — but they're the kind of back-of-envelope estimates you'd put up in a system design interview to anchor your tradeoffs. About 50K concurrent users at peak. Roughly 2 million sessions per day. Median 15 turns per session. One to ten tool calls per turn, parallelized where safe. Five to thirty thousand tokens per turn after cache. Cost ceiling under 50 cents per complex request. And a TTFT — time to first token — target of 500 milliseconds for that conversational feel.

---

## SLIDE 14 — AI-Specific Constraints

So what makes this Claude Code CLI different from your usual command line interface? 

These constraints — and each one will drive a design decision later.

1. Finite context window — we covered this already, but it bears repeating because it shapes half the architecture. The model's memory has a hard cap.
2. Stateless model — the model doesn't remember anything between turns. Every single turn, you re-send the entire conversation history from scratch. That's why compaction matters — we'll get to that.
3. Per-token pricing — every token you send costs money, so the longer the conversation goes, the more expensive it gets. That's why caching and compression aren't optional.
4. Model versions drift — you ship your product, the model provider updates the model, and suddenly your system behaves differently. We'll see exactly this in the incident that happened on Claude Code, later.
5. Prompt injection — when the model reads a file or fetches a URL, malicious content in that output can trick the model into doing something it shouldn't. That's a whole threat category we'll address in the safety section.
6. Non-deterministic output — same input, different output every time. We covered this before, but it affects testing too — how do you write tests for a system that doesn't give the same answer twice?

---

## SLIDE 15 — Section Divider: High-Level Architecture

Part four — High-Level Architecture. Ten minutes. Draw the box diagram. Components first; details later.

---

## SLIDE 16 — Architectural Style Choice

Two options. On the left: a multi-agent graph — you have multiple specialized agents talking to each other, criss-crossing edges everywhere. This is the approach Google Antigravity takes, for example — it's designed to orchestrate multiple subagents in parallel across different workspaces, with separate agents handling everything from research to implementation to testing. Sounds powerful, but when something goes wrong, which agent made the bad call? The failure could be in any edge. 

On the right: a single main loop — one primary loop that dispatches to tools like Read, Edit, Bash, Grep. This is the approach Claude Code and Cursor converged on. Now, to be clear — Claude Code isn't purely single-threaded. It can spawn subagents for subtasks — each with its own context window and its own tool allowlist. But the key difference is: those subagents are still the same model, controlled by the same primary loop. That's very different from a multi-agent graph where fundamentally different agents coordinate peer-to-peer. The primary loop stays in control, failures stay localized, and you can actually debug it. 


And this is our first design decision out of the 22 Design Decisions as promised in the opening slides: Pick the single main loop as your core architecture. When your system is already unpredictable by nature, you want to be able to trace exactly what went wrong — and a single loop makes that possible.

---

## SLIDE 17 — The 20-Line Agent

Here's the entire agent in about 20 lines of pseudocode. Recall the ReAct loop we talked about in the opening — reason, act, observe, repeat. Here's what it actually looks like in code. The user asks a question or gives a task. Claude Code takes that current question, the previous conversation history, and the list of available tools, and sends all of it to the model. Now, to answer that question or finish that task, the model might need more information — so it tells the agent which tools to invoke. "Read this file." "Run this test." The agent executes the tool, gets the result, and feeds it back to the model. Now the model has more context, so it decides: do I have enough to answer, or do I need another tool call? If it needs more, it asks for another tool. If it has enough, it responds with the final answer. That's the loop — the model keeps requesting tools until it has gathered everything it needs to complete the task. The entire brain of this billion-dollar product is a while loop with an if-else inside it. The loop itself is deliberately small and dumb. All the smart stuff — validation, permissions, sandboxing, caching — lives in the layers around it, not inside it. 

That's Design Decision 2: Keep the loop small. Push complexity to the edges.

---

## SLIDE 18 — Five-Layer Architecture

This is the master diagram — the one we'll keep coming back to for the rest of the session. Every design decision we make from here on will land in one of these five layers.

Five layers, top to bottom:

1. Layer 1 — UI and TUI. TUI stands for Terminal User Interface — it's the custom-built rendering layer we just talked about. This layer handles all the surfaces: terminal, IDE extension, Slack integration, headless CI. Its job is to take the raw model output and present it to whatever surface the user is on — whether that's a human at a keyboard or a CI pipeline expecting JSON.

2. Layer 2 — Agent Loop. This is the while loop from the previous slide — the one that drives the entire conversation. It takes the user's message, sends it to the model, gets back either a tool call or a final answer, and keeps cycling. Everything else exists to serve this loop.

3. Layer 3 — Tool Dispatch. This is a pipeline we'll cover in detail later — it validates, checks permissions, executes, and trims every tool call before the result goes back to the model. It's the gatekeeper between "the model wants to do something" and "the system actually does it."

4. Layer 4 — Permission and Sandbox. This layer decides what's allowed and what's blocked. Two lines of defense: first, a permission check that decides whether a tool call should proceed. Second, kernel-level sandboxing — so even if the permission logic has a bug, the operating system itself stops the damage. We'll cover both in detail later.

5. Layer 5 — Model API. This is where the system actually talks to the Anthropic LLMS via API. It handles cache management, token streaming, model routing — deciding whether to send this particular call to Opus, Sonnet, or Haiku based on the task.

Now, notice something about this stack: the model is at the bottom, not the top. That's deliberate. The model is a dependency — you call it, you get a response, you move on. Everything above it — the loop, the tools, the permissions, the UI — that's called the **harness**. If you've been following the agentic AI space, you've probably heard "harness engineering" a lot lately. Well, this is what it actually looks like for a coding agent like Claude Code. Think of it this way: the model is non-deterministic — same input, different output every time. The harness is the opposite — it's deterministic. Same tool call always goes through the same validation, the same permission check, the same sandbox. Every time. No exceptions. So what you're really doing is wrapping a predictable, reliable layer around an unpredictable brain — and that's what makes Claude Code reliable even though the model inside it isn't. And here's why layering matters: if Anthropic ships a new model tomorrow, only Layer 5 changes. The harness — Layers 1 through 4 — keeps working untouched.

That's Design Decision 3: Layered separation — each layer owns one concern, each layer evolves independently. Change the UI without touching the tools. Change the sandbox without touching the model. That's the whole point of layers.

---

## SLIDE 19 — Sequence Diagram

Now let's see all five layers working together. Let's trace one real message through the entire stack — "fix the bug in auth.py."

Step 1 — the user types that message into the terminal. That's Layer 1, the TUI. It captures the input and passes it down.

Step 2 — the message hits Layer 2, the Agent Loop. The loop packages up the user's message, the conversation history so far, and the list of available tools, and sends all of it to the model via Layer 5, the Model API.

Step 3 — the model looks at everything and decides: "I need to read auth.py first before I can fix anything." So it responds with a tool call — tool_use: Read, path: auth.py. Not a final answer — a request for more information.

Step 4 — that tool call goes to Layer 3, Tool Dispatch. The dispatch pipeline validates the input, then passes it to Layer 4, Permission and Sandbox, which checks: is this tool allowed? Is the path inside the project directory? In this case, it's a read — so it's approved automatically, no human prompt needed. But imagine the model had instead asked to run a Bash command — say, "delete the node_modules folder and reinstall all packages." That's not a read. That's a destructive shell command. Layer 4 would escalate that to the human: "Claude Code wants to run this command. Allow?" You'd see a Y/n prompt in your terminal, and nothing happens until you approve it. That's the permission cascade in action — reads sail through, but anything that could change or delete something gets a human checkpoint.

Step 5 — the tool executes, reads the file, and the contents of auth.py get appended back to the conversation as a tool result. Now the model has the file in its context.

Step 6 — the loop sends everything back to the model again. Now the model has enough context to see the bug — maybe it's a missing null check. So it responds with another tool call: Edit auth.py, add the fix. That edit goes through the same dispatch pipeline, the same permission check, the same sandbox.

Step 7 — the model gets the edit confirmation back, decides it's done, and responds with a text message: "Fixed the null check in auth.py, line 42." That's a text response, not a tool call — so the loop exits, and the answer flows back up to Layer 1, the TUI, which renders it for the user.

That's one message, flowing through all five layers. Every message you send goes through this exact same path.

---

## SLIDE 20 — Section Divider: CLI Surface

Part five — CLI Surface. Seven minutes. Why CLI, and how the terminal layer actually works.

---

## SLIDE 21 — Surface Choice

Where should this agent live? Three options.

1. Web app — rich UI, but the developer has to leave their terminal. And a web app can't directly touch files on disk or run shell commands — you'd need a backend relay for everything.

2. IDE plugin — you're inside the editor, right next to the code. But you have to build a separate plugin for each editor — VS Code, JetBrains, and so on. And shell access is limited — most plugin APIs don't give you a full terminal.

3. CLI — runs right in the developer's terminal, inside their repo. Native filesystem access, full shell, and it's scriptable — so the same tool that works on a developer's laptop also works headlessly in a GitHub Actions pipeline. The downsides? Limited rendering and no built-in login screen.

Why CLI? Because a developer is already in a terminal — running git, npm, docker, pytest. A CLI agent meets them where they already work, no context-switch needed.

That's Design Decision 4: CLI as the primary surface. Meet the developer where they already are.

---

## SLIDE 22 — Custom TUI Architecture

Now that we've picked CLI, we need to render the output. Why build the terminal UI from scratch instead of using an existing library like ncurses — the standard C library that most terminal apps use for drawing text-based interfaces?

Because this isn't a static terminal app — it's a streaming one. Tokens arrive from the model one at a time while the user is watching. Mid-stream, a tool call might fire and its output needs to appear inline. Progress bars update live. And the user needs to scroll back through previous output while new text is still arriving below. ncurses wasn't designed for any of that.

So Claude Code builds its own rendering pipeline. The model streams tokens via SSE — Server-Sent Events. Those tokens feed into a React component tree — yes, React, the same framework used for web UIs, but running in the terminal. A layout engine called Yoga computes flexbox positioning. Then Ink — a terminal rendering library — does a diff-and-reconcile pass, only updating the parts of the screen that actually changed, and writes the final output to the TTY — the terminal's display.

The cost? About 2,700 lines of TypeScript reimplemented from scratch. That's the price of streaming UX in a terminal.

That's Design Decision 5: Build a custom TUI. Streaming output is a system design concern, not a cosmetic one.

---

## SLIDE 23 — Input State Machine

The terminal isn't just rendering output — it also has to handle input. And input in Claude Code isn't simple, because the terminal can be in one of four different states at any time.

1. Idle — nothing is happening. The cursor is blinking, waiting for the user to type something.

2. Typing — the user is composing a message. This supports multi-line input, paste detection, and command history — just like a regular shell.

3. Running — the user hit Enter and the agent is working. Tokens are streaming in, tools are executing, and the user sees live progress. If something goes wrong or takes too long, Ctrl-C interrupts the current operation.

4. Rewind — the user pressed Escape twice quickly. This rolls the conversation back to the last checkpoint — undoing the most recent tool calls and model responses, so the user can try a different approach.

The transitions are straightforward: idle to typing on any keypress, typing to running on Enter, running back to idle when the model returns a text response, and running to rewind on double-Escape. The key insight is that interrupt and rewind aren't afterthoughts — they're built into the state machine as first-class transitions, because in an agentic system, the user needs to be able to stop or undo the agent at any point.

That's Design Decision 6: Treat input as a state machine. Interrupt and rewind are first-class.

---

## SLIDE 24 — Distribution

How does a developer actually install this thing? 

1. pip or Homebrew — familiar to developers, but updates are slow because you're going through a package review process.

2. Standalone binary — no dependencies needed, but the download is large and updates mean re-downloading the whole thing.

3. npm — huge developer reach and easy updates with a single command, but it requires Node.js on the machine.

4. npm plus a native binary — this is what Claude Code actually does. npm handles the distribution — developers already have it, updates are one command, and it works on every operating system. But the actual execution doesn't run through Node.js. Instead, the npm package includes a native binary — a pre-compiled executable built with Bun, which is a fast JavaScript runtime. So npm is just the delivery truck; the binary is what actually runs on your machine. That's why it starts fast and doesn't need you to install anything else.

The install command is just `npm install -g @anthropic-ai/claude-code` — one line and you're ready to go. The final artifact is about 10.5 megabytes for the JavaScript CLI delivered via npm, plus a 188-megabyte native binary built with Bun — a fast JavaScript runtime. Zero install-time dependencies — nothing else to download or configure.

That's Design Decision 7: Distribute via npm plus native binary. Maximum reach, minimum friction.

---

## SLIDE 25 — Section Divider: Tools

Part six — Tools: The Agent's Hands. Eleven minutes. How the agent takes action in the real world.

---

## SLIDE 26 — Tool Contract

Every tool in Claude Code — Read File, Edit File, Bash, Grep, all 50-plus of them — has to follow the same five-part contract. Think of it as a checklist: if a tool doesn't fill out all five parts, it doesn't get registered.

1. Schema — this defines what inputs the tool accepts. For example, the Read File tool expects a file path as a string. If the model sends something that doesn't match the schema — like a number instead of a path — the call gets rejected before it ever executes. The schema guards the model's output.

2. Permission — this declares what kind of access the tool needs. A read tool is low-risk. A Bash tool that can run any shell command is high-risk. The permission part tells Layer 4 how to handle it — auto-approve, ask the human, or block entirely. It guards the user's system.

3. Concurrency-safe — this is a true-or-false flag that says whether it's safe to run this tool in parallel with other tools. Reading five files at once? Fine. Editing two files at once? Dangerous — you could get race conditions. This flag enables safe parallelism.

4. Read-only — another flag. If a tool only reads and never writes, it can skip the permission prompt entirely. No need to ask the user "can I read this file?" every time. This keeps the experience fast for safe operations.

5. Render function — this tells the TUI how to display the tool's result. A file read might show a code block with syntax highlighting. A Bash command might show terminal output. The UI is part of the tool, not an afterthought.

Each part prevents one class of failure. Skip the schema, and bad input crashes the tool. Skip the permission, and the agent runs wild. Skip the concurrency flag, and parallel calls corrupt files. The contract IS the design.

That's Design Decision 8: Every tool must fill out all five parts. Skip one, lose a guarantee.

---

## SLIDE 27 — Dispatch Pipeline

We just defined the five-part contract every tool must have. Now let's look at what happens when the model actually calls a tool. Every single tool call — Read File, Edit File, Bash, Grep, all of them — goes through the same pipeline before the result ever makes it back to the model.

1. Schema parse — the input gets validated by Zod, which is a TypeScript schema validation library. If the model said "read file" but sent a number instead of a file path, this stage catches it immediately. Bad input never reaches the tool.

2. Semantic check — is the path the model asked for inside the current working directory? By default, the model can't read or write files outside your project folder. But if you explicitly allow it — for example, by granting access to another directory — it can. The point is: the boundary is enforced here, and nothing gets through without your permission.

3. Permission — this is the cascade we'll cover in detail later. It decides: should this call be auto-approved, escalated to the human, or blocked entirely? A file read sails through. A Bash command that deletes something gets escalated.

4. Pre-hook — if the user has set up a PreToolUse hook — say, a custom script that checks whether edited files match a certain naming convention — it runs here, before the tool executes. This is where teams plug in their own rules — like blocking edits to protected directories or enforcing a style guide — without modifying Claude Code's source code.

5. Execute — the tool actually runs. Read File reads the file. Bash runs the shell command. This is the only stage that touches the real filesystem.

6. Trim output — if the result is over 50,000 characters — say, the model ran a Bash command that dumped a huge log file — the full output goes to disk and only a 2-kilobyte preview stays in the conversation. This prevents one large tool result from eating the entire context window.

7. Post-hook — the user's PostToolUse hook runs here. This is where you'd plug in a formatter, a linter, or an audit logger. For example, auto-run Prettier on every file the agent edits, or log every Bash command to a compliance file.

8. Append result — the tool's output gets added back to the conversation as a tool result message. Now the model can see what happened and decide its next move.

Why does every tool go through these same stages? Because the things that matter for every tool — validation, permissions, output trimming, hooks — are built into the pipeline itself, not scattered across 50 individual tool implementations. That's the whole point. If you need to add something new tomorrow — say, rate limiting or logging — you add one stage to the pipeline and every tool gets it automatically. You don't go tool by tool, updating each one and hoping you didn't miss any.

That's Design Decision 9: One pipeline, all tools. Cross-cutting concerns live in the dispatch, not in individual tools.

---

## SLIDE 28 — Parallel Tool Calls

Sometimes the model wants to do multiple things at once. Say it needs to read five files to understand a feature — does it have to read them one at a time, waiting for each to finish before starting the next? That would be painfully slow.

This is where the concurrency-safe flag from the tool contract comes in. Two modes:

1. Sequential — one tool call at a time, each waits for the previous one to finish. Safe, but slow. This is the default for any tool that writes — like Edit File. Why? Because if the model edits two files at the same time, and both edits depend on each other, you could end up with conflicting changes — what engineers call a race condition.

2. Parallel — multiple tool calls fire at the same time. This is allowed when the tool's concurrency-safe flag is set to true. These flags are set by the tool developer — for built-in tools like Read File or Bash, Anthropic's engineers set them; for MCP tools, whoever builds that MCP server sets them. It's a design-time decision, not something the model or the end user decides at runtime. Read File is parallel-safe by default — reading five files at once doesn't cause any conflicts because nothing is being changed. Grep searches are also parallel-safe. But edits? Always sequential. One at a time.

The tradeoff is real in both directions. If you mark too many tools as concurrency-safe, you risk race conditions — two edits stepping on each other. But if you mark too few, everything runs one at a time and the agent feels sluggish. Getting this right is a per-tool judgment call, and it's why the flag exists in the contract rather than being a global setting.

---

## SLIDE 29 — Self-Healing Patterns

Things will go wrong. Tools will fail. The API will reject your request. Permissions will get denied. The question isn't whether failures happen — it's whether the system recovers on its own OR crashes and waits for a human. Claude Code has five self-healing patterns, and every single one exists because something broke in their production and they learnt from it and refined.

1. Tool-result persistence — if a tool returns more than 50,000 characters of output — say, the model ran a Bash command that dumped an enormous log file — the full output gets saved to disk and only a 2-kilobyte preview stays in the conversation. Why? Because before this existed, huge tool outputs would fill the entire context window and cause out-of-memory crashes. This pattern was born from that exact incident.

2. Prompt-too-long recovery — sometimes the conversation gets so long that the API rejects it with a 413 error, which means "your request is too large." When that happens, the system automatically drops the oldest turns from the conversation and retries. Before this was added, a 413 would just crash the session.

3. Circuit breaker — if the same operation fails three times in a row, stop retrying. This one came from a real incident where the compaction system — the part that summarizes old conversation to free up space — kept failing and retrying in an infinite loop, burning through API calls and money. Now, three re-tries and it stops.

4. Denial as result — when the user denies a permission request — say, the model asked to run a Bash command and the user said no — that denial gets returned to the model as a regular text result, not as an error or exception. Why does that matter? Because when the model sees "permission denied: the user blocked this Bash command," it can reason about what happened and try a different, safer approach. If it got an exception instead, it would just fail.

5. Idempotent retries — in headless mode, where Claude Code is running inside a CI pipeline with no human present, failed operations get re-queued in a way that's safe to retry. Running the same operation twice won't cause duplicate edits or double commits. This pattern came from CI pipelines that would fail partway through and leave the codebase in a broken state.

Notice the pattern: none of these were designed upfront. Every one of them was added after a real production failure. That's the honest truth about reliability engineering — you don't know what will break until it breaks.

That's Design Decision 10: Every reliability mechanism has a postmortem behind it. Design defensively.

---

## SLIDE 30 — Section Divider: Memory & Context

Part seven — Memory and Context. Twelve minutes. Designing memory for a model that has none.

---

## SLIDE 31 — Memory Tiers

Remember — the model has no memory of its own. Every turn, it starts from scratch. So the system has to provide memory for it — and not just one kind. Claude Code uses four distinct memory tiers, each with a different scope and a different storage backend.

1. Working memory — scope: this turn only. This is everything currently inside the model's context window — the conversation so far, the tool results, the system prompt. It's the model's "RAM." When the turn ends and a new one begins, it gets rebuilt from scratch. It's fast, but expensive — every token in here costs money.

2. Session memory — scope: this entire conversation. When you close your terminal and come back later, the conversation picks up where you left off. That's because the full conversation log — every message, every tool result, every checkpoint — is saved to disk. The model doesn't remember it, but the system reloads it into the context window when you resume.

3. Project memory — scope: this repository. This is the CLAUDE.md file — a Markdown file committed to git, right alongside your source code. It contains project-specific instructions: architecture decisions, coding conventions, "don't touch this file" warnings, preferred libraries. It gets loaded once at the start of every session, so the model always knows the rules of your project. Because it's in git, your whole team shares the same project memory.

4. Tool-result memory — scope: large outputs. When a tool produces a result that's too big to keep in the context window — like a 50,000-character log dump — the full output gets saved to a file on disk, keyed by the tool_use_id. Only a small preview stays in the conversation. The model can reference the full output if it needs to, but it doesn't clog up the working memory.

Notice that each tier lives in exactly the right place. Working memory is in the prompt — fast but ephemeral. Session memory is on disk — persistent across restarts. Project memory is in git — shared across the team. Tool-result memory is in temp files — large but out of the way.

That's Design Decision 11: Four memory layers, four scopes, each lives in the right place.

---

## SLIDE 32 — 200K Token Budget

Now let's look at where those 200,000 tokens actually go — because this is one of those slides that changes how you think about context windows.

You'd think 200K tokens is a lot of space. But before the user even types their first message, a big chunk is already spoken for. Let's walk through it.

1. System prompt — about 2,700 tokens. This is the core set of instructions that tells the model how to behave — things like "you are Claude Code, follow these rules, here's how to use tools." This gets cached globally, meaning it's the same for every user and every session, so you only pay for it once.

2. Tool definitions — about 17,000 tokens. That's the schema for all 50-plus tools — Read File, Edit File, Bash, Grep, and everything else. Each tool needs its name, description, input parameters, and type definitions sent to the model so it knows what tools it can call and how to call them. Fifty tools adds up fast.

3. Auto-compact reserve — about 33,000 tokens. This is space the system keeps off-limits as a buffer. Why? Because when the context window fills up, the system needs room to run compaction — summarizing old conversation to free up space. If you filled the window to 100 percent, there'd be no room left to even run the compaction process. So this reserve is like keeping your gas tank above empty — you need fuel to get to the gas station.

That leaves about 147,000 tokens of free working memory — only 74 percent of the total window. You start with a 200K budget and you've already spent a quarter of it before the user types a single character. That's why every token matters, and why compression, caching, and eviction aren't nice-to-haves — they're survival mechanisms.

---

## SLIDE 33 — Five-Layer Compression

So what happens when that 147K of free space starts running out? You compress. But not all compression is equal — some methods are free, some cost money, and some lose information. Claude Code stacks five compression layers, and the cheapest ones always fire first.

1. Tool results to disk — cost: zero. If a tool returned a huge output — like a 50,000-character log dump — move the full result to a file on disk and leave just a small preview in the conversation. This is the same tool-result persistence we covered in self-healing. It frees up context without making any API calls and without losing any data — the full output is still on disk if the model needs it later.

2. History snip — cost: zero. Drop the oldest turns from the conversation. The idea is simple: if the conversation is 40 turns long, the first few turns are probably not relevant anymore. Snip them off. No API call needed — just stop including them. The risk? If something from turn 3 is still important at turn 40, it's gone.

3. MicroCompact — cost: zero. This is a lightweight, local compression pass — things like removing duplicate whitespace, trimming redundant tool metadata, or collapsing repeated system messages. Small savings individually, but they add up across a long conversation. No API call, no information loss on the content that matters.

4. Context collapse — cost: zero. This is more aggressive than MicroCompact. Instead of trimming whitespace or metadata, it collapses entire blocks of older conversation into shorter representations using simple heuristic rules — not an LLM call, just pattern-based reduction. For example, if the model read a file 10 turns ago and then edited that same file 3 turns ago, the older read result can be collapsed down to just "read auth.py — 200 lines" because the edit already superseded it. Or if there were five consecutive tool calls that all succeeded, collapse them into a single summary line instead of keeping all five full results. The key difference from a forked summary is that no model is involved — these are mechanical rules, so they're fast and free, but they can't judge what's actually important the way a model can.

5. Forked summary — cost: one API call. This is the most expensive option — and the highest quality. The system sends the conversation to the model and asks it to produce a condensed summary. That summary replaces the old conversation history. It costs real money because you're making an extra API call to the LLM, but the summary retains the most important context because the model actually understands what matters.

The pattern is clear: try the free options first, and only pay for compression when the free methods aren't enough. Each layer down the stack gives you better fidelity but costs more. And every lossy step — from history snip through forked summary — risks losing context that might matter later. That's the fundamental tradeoff.

That's Design Decision 12: Try free options first. Reserve expensive operations for genuine necessity.

---

## SLIDE 34 — Compaction as a Transaction

Now here's the key insight about compaction: it's not just about throwing stuff away. If all you did was delete old conversation to free up space, the model would lose critical context — it would forget what files it's working on, what the plan was, what project rules to follow. So compaction is actually two operations that must happen together as one atomic transaction: eviction AND rehydration.

Let's walk through a before-and-after.

Before compaction: the context window is at 190K tokens — 95 percent full, overflow is imminent. The conversation is cluttered with old tool results the model no longer needs, stale file references from files that have been edited since they were first read, and duplicated MCP instructions that got re-injected multiple times.

Now compaction fires. First, it evicts — it removes all that stale, redundant, or outdated content. But then — and this is the part most people miss — it immediately rehydrates. It puts back the things the model actually needs going forward:

1. The five most recent files get re-injected — because those are the files the model is actively working on right now. If you evicted everything and didn't put these back, the model would have to re-read them, wasting time and tool calls.

2. Active skills get re-attached — if the user has loaded any skill prompts, like a coding style guide or a domain-specific instruction set, those get put back in so the model keeps following them.

3. CLAUDE.md gets reloaded from disk — this is the project memory file. It might have been updated since the session started — maybe a teammate committed new conventions — so the system reads the latest version from disk, not from the stale copy in the conversation.

4. Plan and sub-agent state get restored — imagine the model is halfway through a ten-step refactoring plan. It's completed steps one through six, and it knows steps seven through ten are still pending. If compaction evicts that plan, the model has no idea where it left off — it might redo work it already finished, or skip steps entirely. Same thing with sub-agents: if the main agent dispatched a sub-agent to explore the codebase and got back a summary of findings, that summary needs to survive compaction. Otherwise the model would re-dispatch the same sub-agent, burning tokens and time on work that's already done. So the system explicitly preserves the current plan state and any sub-agent results that the model hasn't acted on yet.

5. The prompt-cache prefix stays warm — remember the system prompt and tool definitions from the token budget slide? Those take up about 20,000 tokens combined, and they're identical for every turn. Anthropic's API lets you cache that prefix so you don't pay full price to re-send it every time. But here's the catch: if compaction rearranges the beginning of the prompt — even slightly — the cache key changes and the cache misses. That means you'd pay full price for those 20,000 tokens all over again. So compaction is carefully designed to only modify the conversation portion of the prompt — the part after the cached prefix — and leave the prefix itself untouched. We'll go deeper on exactly how this cache boundary works in the next slide.

After compaction: about 50K tokens free, the model has everything it needs to keep working, and the cache is still warm. The whole operation looks seamless to the user — they don't even know it happened.

The reason this has to be one transaction — not "evict now, rehydrate later" — is that if the system evicted and then crashed before rehydrating, the model would be left with a gutted context and no way to continue. Eviction without rehydration is data loss. They're designed together or not at all.

That's Design Decision 13: Eviction and rehydration are one transaction. Design them together.

---

## SLIDE 35 — Static/Dynamic Cache Boundary

Here's the cache boundary I teased in the last slide. This is one of the most important cost optimizations in the entire system.

Every time Claude Code sends a request to the Anthropic API, it sends the full prompt — system instructions, tool definitions, conversation history, everything. That's expensive. But Anthropic's API supports prompt caching: if the beginning of your prompt is identical to a previous request, the API recognizes it and charges you about one-tenth the normal price for those cached tokens. That's the 10x cost reduction.

So the trick is: split your prompt into two halves at a carefully chosen boundary.

On the left side — the static prefix. This includes the core system instructions — "you are Claude Code, here are your rules" — and all the tool definitions. This content is identical for every user, every session, every turn. It never changes. That's what makes it cacheable — the API sees the same prefix over and over and serves it from cache.

On the right side — the dynamic suffix. This is everything that varies: the user's conversation history, MCP-specific instructions from whatever external tools they've connected, their output preferences like "respond in Spanish" or "use compact formatting," and any per-session settings. This part changes every turn, so it can't be cached — you pay full price for it every time.

The key engineering constraint is: you must never let dynamic content leak into the static prefix. If a single user-specific token ends up in the prefix — say, an MCP instruction gets accidentally placed before the tool definitions — the cache key changes for that user, and every request they make pays full price for the entire prefix. That's a 10x cost increase for one misplaced token.

This is also why compaction — from the previous slide — is so careful about not touching the prefix. When compaction evicts and rehydrates, it only modifies the dynamic suffix. The static prefix stays byte-for-byte identical, so the cache hit survives compaction.

That's Design Decision 14: Static prefix cached, dynamic suffix per-request. This is a 10x cost decision.

---

## SLIDE 36 — Section Divider: Model API Layer

Part eight — Model API Layer. Six minutes. How we actually talk to the LLM.

---

## SLIDE 37 — Tool-Call Protocol Choice

When the model decides it needs to call a tool — say, "read a file" — how does it actually communicate that request? There are three ways to do it, and this choice has real consequences for streaming, reliability, and portability.

1. JSON mode — the model outputs raw JSON text in its response, and the system parses it. For example, the model might literally output the text `{"tool": "read_file", "path": "auth.py"}` as part of its response, and then Claude Code has to find that JSON, extract it, and figure out it's a tool call. The upside? It's provider-agnostic — any model can output text, so this works with any provider. The downsides? It's brittle — the model might output malformed JSON and the whole call fails. There's no streaming — you have to wait for the entire response before you can parse the JSON. And there's no retry semantics — no built-in way for the API to tell you "this is a tool call" versus "this is regular text," and no structured way to report results back.

2. Function calling — this is the approach OpenAI popularized. The model's response explicitly marks "this is a function call" as a structured object, separate from the text response. Much better than JSON — the API itself tells you "this is a function call, here's the name, here's the arguments." It's become the industry standard. The con? Every provider implements it slightly differently, so it's not one protocol — it's a family of per-provider variants.

3. tool_use native — this is Anthropic's first-class primitive, designed from the ground up for tool invocation. When the model wants to call a tool, the API returns a structured `tool_use` content block — part of the response itself, right alongside text blocks. It has the tool name, the input parameters, and a unique ID — all type-checked and validated by the API server before it even reaches your code. Streaming is built around content blocks, so you can see the tool call forming token by token as it generates. And when the tool finishes, you send back a `tool_result` block paired to that ID — success or failure — and the model knows exactly what happened. The con? It locks the shape to the Anthropic API. If you wanted to swap providers, you'd rewrite this layer.

So here's the question: if function calling already works — and it does — why would Claude Code choose tool_use and accept the lock-in? Because Anthropic built both the model and the API. The tool protocol is designed to work perfectly with Claude's architecture — the streaming format matches how Claude generates content, the validation matches Claude's output patterns, the retry semantics are native. It's a home-field advantage. When you own the entire stack — the model, the API, and the product — using a generic protocol means paying an abstraction cost for portability you don't need.

That's Design Decision 15: Use tool_use natively. Pay the lock-in cost for native integration.

---

## SLIDE 38 — Model Routing

One agent, but not one model. Claude Code uses three different models, and it picks which one to call based on how hard the task is. Why? Because you wouldn't use a sword where a needle will do the job.

1. Opus 4.7 — this is the most capable and most expensive model. It handles the main reasoning loop — the hard stuff. When the model needs to understand a complex codebase, plan a multi-file refactoring, or debug a tricky issue, that's Opus. You're paying top dollar, but you need the reasoning power.

2. Sonnet 4.6 — the mid-tier model. Fast and cheap. Claude Code uses it for the permission classifier — the part that decides "should this tool call be allowed or blocked?" That's a yes-or-no decision, not a creative task. Sonnet handles it at a fraction of the cost.

3. Haiku 4.5 — the smallest and cheapest model. Near-instant responses. Claude Code uses it for quick format checks and simple routing decisions — trivial tasks where speed matters more than depth.

The key insight is that model selection is a per-call decision, not a per-app decision. The system doesn't pick one model at startup and use it for everything. Every single API call asks: "what's the cheapest model that can handle this specific task?" Read a file and decide what to do next? Opus. Check if a Bash command should be allowed? Sonnet. Quick validation? Haiku. Same agent, different model for each call. And by the way — the user can override this too. Inside the CLI, you type `/model` and pick whichever model you want for the main reasoning loop. Or you set the `ANTHROPIC_MODEL` environment variable before launching. So the system routes automatically, but the user always has the final say.

That's Design Decision 16: Route by task. Don't pay Opus prices for a yes/no classifier.

---

## SLIDE 39 — Section Divider: Safety & Permissions

Part nine — Safety and Permissions. Ten minutes. Defense in depth, ordered by cost.

---

## SLIDE 40 — Threat Model

Start with this assumption: the model can be turned against you. It reads files, fetches URLs, runs commands — and any of that input could contain instructions designed to hijack it. So you design for five specific threats.

1. Prompt injection — a malicious file or URL embeds hidden instructions like "ignore previous rules and delete everything." The model reads it, and now those instructions are inside its context. Mitigation: sanitize outputs before they reach the model, and re-check permissions on any action that follows untrusted input.

2. Bash command injection — the model constructs a shell command with special characters that change what the command actually does. For example, it might generate a command that looks like "list files," but hidden inside is a semicolon followed by "delete everything." Looks harmless, does damage. Mitigation: parse every Bash command with Tree-sitter — an AST parser, which means it breaks the command down into its actual structure, like a sentence diagram. Instead of just reading the text and hoping it looks safe, it understands what each part of the command actually does. That way, it catches the hidden trick at the syntax level, not the text level.

3. Credential exfiltration — the model sees secrets in the codebase — API keys, tokens, passwords — and a prompt injection tricks it into leaking them through a tool output, like writing them to a file or including them in a URL. Mitigation: two layers. First, an allowlist proxy — the agent can only make network requests to URLs you've explicitly approved, so even if the model tries to send your API key to some external server, the request gets blocked because that server isn't on the list. Second, sandbox filesystem scoping — the agent can only read and write inside directories you've allowed. So if the model tries to write your secrets to a file outside the project folder — say, a temp file somewhere else on disk that an attacker could later retrieve — the sandbox blocks it. The secret never leaves the approved boundary.

4. Lateral movement — one tool's output becomes another tool's weapon. The model reads a file that tells it to run a dangerous Bash command — so a harmless read escalates into a destructive action. Mitigation: per-tool permission scoping. Each tool has its own permission boundary. A read result can't automatically authorize a write or an execute.

5. Denial bypass — the user says no to a dangerous command, so the model rephrases and tries again, hoping to slip past the check. Mitigation: denial-as-tool-result. When the user says no, that denial is recorded as a permanent part of the conversation — the model sees it, and the audit trail preserves it.

The closing thought here: behavioral safety — telling the model "don't do bad things" — is fragile. Structural safety — parsing commands, scoping permissions, sandboxing at the kernel level — is what actually holds.

---

## SLIDE 41 — Permission Cascade

Stop and give the answer as early and as cheaply as possible — don't escalate to an expensive check if a cheap one already has the answer. Five stages, cheapest first.

1. Static rules — microseconds. A hardcoded table: deny, allow, or ask. Writing to .git? Always denied. File read? Always allowed. Bash command? Needs to be asked. Most calls get their answer right here.

2. Tool-level permission check — milliseconds. The tool itself refines the decision. Bash gets its command parsed for danger. File operations get path-checked, for example, is the file inside the allowed directory?

3. Permission mode — microseconds to milliseconds. What mode is the user in? "Accept edits" mode lets file edits sail through. "Plan" mode makes everything read-only.

4. LLM classifier — a few hundred milliseconds. Only fires in auto mode. Sonnet looks at the tool call and classifies it — safe or not safe. Most expensive automated check, which is why it's stage four, not stage one.

5. Ask the human — human time. If nothing above could decide, show the user a Y/n prompt and wait. The result? 93 percent of prompts that reach the human are approved — the cascade filtered the noise. That 93 percent is from Anthropic's own auto-mode blog.

Design Decision 17: Deny wins. Cheap checks first, humans last.

---

## SLIDE 42 — Kernel Sandboxing

The permission cascade we just covered is software — it's code making decisions. But what if that code has a bug? What if a prompt injection tricks the model into bypassing a check? You need a second line of defense that doesn't depend on the application logic at all. That's where the operating system's kernel comes in.

On macOS, Claude Code uses seatbelt — Apple's built-in kernel sandbox framework. It tells the operating system itself: "this process is only allowed to access these directories and these network endpoints." The application can't override it, the model can't talk its way out of it — the kernel enforces it.

On Linux and Windows, it uses bubblewrap — a tool that creates isolated environments using Linux namespaces, which is the same technology that powers Docker containers. On top of that, a socat allowlist proxy controls to maintain a allowlist of which network addresses the agent can reach. Only approved URLs get through.

The result? 84 percent fewer permission prompts with sandboxing enabled. That's a verified number from Anthropic's sandbox blog. The user gets asked less because the kernel is already blocking the dangerous stuff silently.

But here's the catch — the "escape-hatch problem". The model has learned that when a command fails inside the sandbox, it can retry with a flag called `--dangerously-skip-permissions`. It figured this out from training data. So the model is actively trying to turn off the safety layer. To close this loophole, you have to explicitly set `allowUnsandboxedCommands` to false in your configuration. Otherwise, the model can talk itself out of the sandbox.

Design Decision 18: Behavioral safety fails — the model will try to work around it. The kernel doesn't negotiate. Use OS sandboxing as the floor.

---

## SLIDE 43 — Six Permission Modes

Think of it as a trust dial — six settings, from maximum caution to maximum speed.

1. Default — ask before every action. Every tool call gets a Y/n prompt. Safest, but slowest. This is what new users start with.

2. acceptEdits — file edits are auto-approved, but Bash commands still get asked. Good for when you trust the model's code changes but want to review shell commands.

3. plan — read-only mode. The model can read files and search the codebase, but it can't edit or run anything. It plans what it would do and shows you, but takes no action. Useful for reviewing what the agent intends before letting it loose.

4. auto — the LLM classifier decides. Remember stage four of the permission cascade? In this mode, Sonnet evaluates each tool call and approves or blocks it automatically. The human only gets asked when Sonnet isn't sure.

5. dontAsk — allowlisted commands run silently. If a command matches the allowlist, it executes without asking. Everything else still gets checked.

6. bypass — skip all permission checks. Maximum speed, minimum safety. But even bypass has a floor — it still blocks writes to .git, .claude, and .vscode directories. Those are protected no matter what. There's no setting that turns off everything.

That last point is the key insight: the user can dial the trust up or down, but the system never gives them a true off-switch. Even at the most permissive setting, certain critical directories are always protected.

Design Decision 19: Let the user pick their risk tolerance, but never give them an off-switch for everything.

---

## SLIDE 44 — Section Divider: Extensibility

Part ten — Extensibility. Eight minutes. How does the system grow without forking?

---

## SLIDE 45 — Customization Surfaces

How do teams make Claude Code work their way — without changing the source code? Three customization surfaces, each at a different scope.

1. Hooks — these are scripts that run automatically before or after every tool call. Two types: PreToolUse runs before the tool executes, PostToolUse runs after. What can you do with them? Block certain actions — like preventing edits to a protected directory. Modify inputs — like rewriting file paths to follow a naming convention. Audit — log every Bash command to a compliance file. Format — auto-run a code formatter like Prettier on every file the agent edits. Lint — run your linter after every edit and feed violations back. The key thing: hooks are your code, running in your environment. Claude Code just calls them at the right time.

2. Skills — reusable instruction sets you load into the model's context. Think of them as cheat sheets. "Use single quotes, tabs not spaces." "All API responses must include a correlation ID." "Always use the repository pattern for database access." When a skill is active, the model follows those rules — but they stay out of the conversation history, so they don't eat up context.

3. CLAUDE.md — the project memory file we covered earlier. It lives in your git repo, right alongside the source code. It gets loaded once at the start of every session. Architecture decisions, coding conventions, "don't touch this file" warnings, preferred libraries — anything the model needs to know about your specific project. Because it's in git, every developer on the team sees the same rules.

All three work behind the scenes — the model doesn't know they exist. It just sees the effect: better behavior, consistent style, project-aware responses. And because none of them require changing Claude Code's source code, a team can customize everything without maintaining their own version of the product.

Design Decision 20: Three customization surfaces, three different scopes. Enterprises don't need to fork.

---

## SLIDE 46 — Sub-Agents

Sometimes the main agent needs help. Say it's working on a large refactoring task — it needs to explore 50 files to understand the codebase, then plan the changes, then implement them. Doing all of that in one context window means the conversation gets enormous, and eventually you hit the context limit.

Sub-agents solve this. Remember — earlier in this session we said Claude Code is a single main loop, not a multi-agent graph. That hasn't changed. A sub-agent is just another tool call — the main loop dispatches it the same way it dispatches a Read File or a Bash command. It's the same model, the same Claude, running through the same pipeline. The difference is that this tool call gets its own fresh context window — a clean slate — with its own system prompt and its own restricted set of tools. Think of it like sending a copy of yourself to go do a specific errand and come back with a summary.

When the sub-agent finishes, only the final summary comes back to the parent. Not the full conversation, not every file it read — just the conclusion. This keeps the parent's context clean.

A few constraints: you can run up to about 10 sub-agents at the same time before the system starts queueing them. And sub-agents can't spawn their own sub-agents — it's single-level only, no nesting. That's a deliberate limit to keep things simple and debuggable.

The tradeoff is clear: sub-agents give you about a 90 percent performance improvement on complex tasks, but they cost roughly 15 times more tokens — because each one runs its own full conversation with the model. So you don't use them for everything. You use them when the task is too big for one context window, or when you need the isolation of a separate workspace.

Design Decision 21: Sub-agents are an isolation tool, not an orchestration framework. Use them only when isolation matters.

---

## SLIDE 47 — MCP and Lazy Loading

So far, every tool we've talked about — Read File, Edit File, Bash, Grep — is built into Claude Code. But what if you want to connect it to external services — GitHub, lack, Postgres, your company's internal APIs? That's what MCP does. MCP stands for Model Context Protocol — it's an open protocol that lets you plug external tools into Claude Code without writing custom integrations. Claude Code sits at the center like a hub, and each MCP server is a spoke connecting to a different service.

Here's the problem: every tool the model can use needs its full schema loaded into the context window — remember, the model has to see the tool definitions to know what it can call. And MCP tools are no different. Without any optimization, connecting to 30 MCP servers loads about 134,000 tokens of tool definitions before the user even types a single character. GitHub's MCP server alone takes up about 24 percent of the context window.

The fix is "lazy loading" — also called deferred loading. Instead of dumping every tool's full schema into the context upfront, the system only loads the tool names. Short labels, no details. When the model actually needs a specific tool, it calls tool_search — a lightweight lookup — and only then does the full schema get loaded into context. Think of it like a library catalog: you browse the titles first, and only pull the full book off the shelf when you need it.

The savings are dramatic: about 5,000 tokens for 30 servers instead of 134,000. That's an 85 percent reduction in context usage. And it directly protects the cache boundary from SLIDE 35 — tool names are small and stable, so they stay in the static prefix. Full schemas are dynamic, so they load into the dynamic suffix only when needed.

Design Decision 22: Load tool names eagerly, load full schemas lazily. This is the same idea as dynamic linking in operating systems — load the capability list at startup, but only load the actual code when it's called.

---

## SLIDE 48 — Section Divider: UX, State & Streaming

Part eleven — UX, State, and Streaming. Six minutes. Latency is architecture, not polish.

---

## SLIDE 49 — Latency Budget

Why does latency matter for a coding agent? Because if the agent feels slow, developers stop using it and go back to doing things manually. Speed isn't polish — it's whether the product gets adopted. So every layer in the architecture has a latency target.

These targets you see on the screen are design goals for this exercise, not published Anthropic metrics.

Four targets:

1. Time to first token — under 500 milliseconds. This is the time from when the user hits Enter to when the first word of the response appears on screen. Under half a second, the user perceives it as "instant — it's already thinking." Over a second, it feels broken. 

2. Token streaming rate — 20 to 30 tokens per second. That roughly matches how fast a person reads. If tokens appear faster than that, the text blurs by and the user can't follow. If they appear slower, it feels like the agent is struggling. This rate keeps the output readable in real time.

3. Simple task with one tool call — under 5 seconds total. Say the user asks "what does this function do?" The agent reads the file and responds. If that takes more than 5 seconds, it doesn't feel like a conversation anymore — it feels like waiting for a build.

4. Complex multi-tool task — under 60 seconds. A big refactoring that involves reading multiple files, planning changes, and editing code. Sixty seconds is acceptable as long as the user can see what's happening — which tool is running, what file is being read, how far along the task is. Without that progress feedback, even 30 seconds feels like a hang.

The key insight: these aren't nice-to-have polish targets. They drove real architecture decisions — the custom TUI, the streaming pipeline, the parallel tool calls, the model routing that picks the fastest model for simple tasks. Every one of those exists because of a latency requirement.
---

## SLIDE 50 — Interactive vs Headless

Remember, we said Claude Code works in two completely different modes — interactive and headless? Same agent loop, same tools, same model — but two opposite user experiences. Now let's look at what that actually means for the architecture.

Interactive mode — a developer is sitting at the terminal, typing in real time. In this mode, the system streams tokens to the screen as they arrive, shows live progress for each tool call, and presents a Y/n prompt whenever a permission decision is needed. The user can interrupt with Ctrl-C or rewind with double-Escape. Everything is designed around a human watching and reacting.

Headless mode — nobody is at the keyboard. Claude Code is running inside a CI pipeline like GitHub Actions, or triggered by a Slack command. There's no one to click "yes" on a permission prompt. So the system has to decide on its own: either auto-approve based on the permission mode and allowlist, or fail the operation entirely. No streaming — the output is batch JSON that the CI system can parse. Exit codes are deterministic — zero means success, non-zero means failure — so the pipeline knows what happened. And retries are idempotent, meaning running the same operation twice won't cause duplicate edits or double commits.

So how does one agent loop serve both experiences without duplicating code? The bridge is an event bus — think of it like a radio station that broadcasts everything the agent does. Every significant action in the agent loop — "I need a permission decision," "this tool just finished," "the model responded with text" — gets broadcast as an event on this bus. The agent loop doesn't know who's listening and doesn't care. It just broadcasts.

Now, whoever is listening decides what to do with those events. In interactive mode, there's a listener that takes a "permission needed" event and turns it into a Y/n prompt on the terminal screen. It takes a "model response" event and streams the tokens to the display one by one. It takes a "tool running" event and shows a live progress indicator.

In headless mode, a completely different listener is tuned into the same broadcast. It takes that same "permission needed" event and checks the allowlist — no prompt, no human, just an automatic yes or no. It takes the "model response" event and writes it to a JSON output file instead of streaming to a screen. It takes the "tool running" event and logs it silently instead of showing progress.

Same events, different listeners. That's the whole trick. The agent loop stays the same for both modes — it doesn't have a single if-statement that says "am I in interactive mode or headless mode?" It just broadcasts, and the surface handles the rest.

The key piece that makes permissions work across both modes is a callback called canUseTool. When the agent loop needs a permission decision, it calls canUseTool. In interactive mode, that callback shows a Y/n prompt and waits for the human. In headless mode, that same callback checks the allowlist and returns yes or no immediately — no human involved. Same function name, same interface, different behavior depending on which surface is active.

And here's why this matters for the future: if tomorrow you wanted to add a third surface — say, a Slack bot, or a web dashboard — you don't touch the agent loop at all. You just write a new listener that subscribes to the same events and renders them however that surface needs. The loop doesn't change. That's the payoff of the event-based architecture.

---

## SLIDE 51 — Section Divider: Eval & Observability

Part twelve — Eval and Observability. Six minutes. You can't ship what you can't measure.

---

## SLIDE 52 — Evaluation Strategy

How do you test a system that gives a different answer every time? Remember, non-deterministic output? Which means the same input can produce different but valid results. You can't write a traditional unit test that says "expect this exact output." So you need a different approach.

The evaluation pipeline works like this: you maintain a frozen test suite — a fixed set of tasks with known correct outcomes. Before shipping a model upgrade, you run every task through the new model and compare the results against the baseline — the results from the previous model version. If the new results are as good or better, you ship. If they're worse, you roll back. Think of it like a before-and-after comparison, not a pass-or-fail test.

Five types of evaluations, each measuring something different:

1. Task completion — does the agent actually finish multi-step tasks? Give it a bug to fix, a feature to implement, a refactoring to do. Did it get to the end? This runs every release.

2. Tool selection — does the agent pick the right tool for the job? When it needs to find a function, does it use Grep or does it wastefully read every file one by one? Picking the wrong tool still works, but it wastes time and tokens. This also runs every release.

3. Permission accuracy — does the auto-classifier — the Sonnet model that decides "safe or not safe" — agree with what the human would have decided? If the classifier is approving things the human would block, that's a safety gap. If it's blocking things the human would approve, that's a friction problem. This runs continuously.

4. Latency — p50 and p99. P50 is the median — half of all requests are faster than this. P99 is the worst case — 99 percent of requests are faster than this. You track both because a system can have a great median but terrible outliers. If your p50 is 400 milliseconds but your p99 is 10 seconds, one in a hundred users is having a miserable experience. This runs continuously.

5. Regression — has any of the above gotten worse compared to last week, last release, or last night? This runs per pull request and nightly, so degradation gets caught early.

Now here's the honest part: the April 2026 quality regression — the one we'll cover in the incidents section — slipped through this entire eval suite.That's the lesson: evals are necessary, but they are not sufficient. They catch the problems you thought to test for. They don't catch the ones you didn't.

---

## SLIDE 53 — Three Layers of Telemetry

Evals tell you whether the system is good enough to ship. Telemetry tells you what's actually happening after you ship. You need both — and telemetry is the one that catches the problems evals missed.

Three layers, each at a different zoom level:

1. Per-turn telemetry — this is the microscope. Every single turn — every time the user sends a message and the model responds — gets logged with a unique trace ID, token counts for input and output, which tools were called, how long each tool took, and which model handled the call. Why does this matter? Because when a user reports "the agent gave me a terrible answer on this one question," you can pull up that exact trace ID and see everything: what was in the context window, which tool results came back, how many tokens were used. Without this, debugging a bad response in a non-deterministic system is like trying to find a needle in a haystack.

2. Per-session telemetry — this is the full timeline. The entire conversation log, every permission event — what was asked, what was approved, what was denied — and every sandbox event — what the kernel blocked, what it allowed. This is what you use when a user files a support ticket saying "the agent deleted my config file." You can reconstruct the entire session step by step: the user said this, the model decided that, the permission check returned this, the tool executed that. It's a complete audit trail.

3. Aggregated telemetry — this is the dashboard. Across all users, all sessions, you track patterns: how often is compaction firing? Are retry rates going up? What percentage of permission prompts are getting denied? How often does the agent complete a task without ever asking the user for permission — that's the "success-without-prompt" metric, and it tells you how well the auto-classifier is working. This is how you catch systemic problems.

The rule is simple: you can't debug what you can't measure. And in a non-deterministic system, you need to measure at every level — the single turn, the full session, and the fleet-wide trend.

---

## SLIDE 54 — Section Divider: Production Reality

Part thirteen — Production Reality. Five minutes. Every elegant design exists because something broke first.

---

## SLIDE 55 — Three Real Incidents

This section is the reason I saved production incidents for the end — because now you have enough context to actually understand what went wrong and why. Every architecture decision we covered exists because something broke first. Here are three real incidents, each one directly tied to a design decision we already made.

1. April 2026 — the Quality Regression. This is the one we mentioned when we talked about evals. Three completely unrelated changes shipped within weeks of each other. First was a reasoning-effort default was changed — this controls how hard the model "thinks" before responding, and the default got lowered. Second, a caching bug. A bug caused some cached content to go stale, so the model was working with outdated context. Third, a verbosity prompt change — someone tweaked the system prompt to make responses shorter, but it also made them less thorough. Each change was tested individually. Each one passed its own evals. But when all three hit production at the same time, they compounded. The model was thinking less hard, working with stale context, AND being told to be brief — and the result was a measurable drop in code quality that users noticed immediately. The fix: a stricter compatibility matrix — meaning you can't ship changes to the model, the prompt, and the caching layer in the same release window anymore. Each one has to ship separately so you can isolate which change caused which effect. And a faster rollback path — so when something does go wrong, you can undo it in minutes, not hours.

2. Late 2025 — the Runaway Retry Incident. The compaction system — the one that summarizes old conversation to free up context — would occasionally fail. Maybe the API timed out, maybe the summary came back malformed. Before the circuit breaker existed, the system would just... retry. And retry. And retry. Indefinitely. Each retry was a full API call to the model, which means each retry cost real money. And because compaction runs automatically in the background, the user had no idea it was happening — they'd just see their API bill spike. The fix: a three-strike circuit breaker. If compaction fails three times in a row, the system stops retrying, logs the failure, and moves on. The user might notice the context window is getting full, but at least the system isn't silently burning through their budget.

3. Throughout 2025 — MCP Bloat. This one built up slowly. Recall, MCP lets you connect external tools like GitHub, Slack, or a database. Every MCP tool needs its full schema loaded into the context window so the model knows how to call it. Early on, every tool schema was loaded upfront — eagerly — the moment the session started. For users with just a few MCP servers, this was fine. But power users started connecting 20, 30 servers, and suddenly 134,000 tokens of tool definitions were eating up the context window before the user even typed a single character. GitHub's MCP server alone took up about 24 percent of the context. Users were running out of context space not because their conversations were long, but because the tool definitions were enormous. The fix: deferred loading — the lazy loading system. Load only tool names at startup — just short labels. Load the full schema only when the model actually needs to call that specific tool. That brought 134,000 tokens down to about 5,000 — an 85 percent reduction.

The pattern across all three: none of these were predicted. Nobody sat in a design meeting and said "what if three unrelated changes compound?" or "what if compaction retries forever?" or "what if users connect 30 MCP servers?" These were discovered in production, by real users, with real consequences. And each one produced a design change that's now permanent.

That's the honest truth about production systems: the architecture diagram is clean, but it was drawn in scar tissue.

---

## SLIDE 56 — Honest Weaknesses

We just covered three incidents. Now let's be honest about what's still not right. Six things the team would reconsider if starting over.

1. MCP loaded eagerly — lazy loading was a retrofit, not the original design. If starting fresh, you'd make deferred loading the default from day one instead of bolting it on after users hit the problem.

2. Compaction had no circuit breaker — the retry loop ran unchecked at launch. Any automated retry should have a hard stop built in from the start, not added after it burns through someone's budget.

3. Sub-agents capped at one level — sub-agents can't spawn their own sub-agents. That keeps things debuggable, but it means some tasks are too big to delegate properly. Nested sub-agents would help, but nobody has figured out how to make them debuggable yet. It's an open problem.

4. Model–prompt–binary coupling — three things can change at the same time: the model version, the system prompt, and the application binary. Each has a different owner. When all three change together and something breaks, nobody knows which one caused it. The stricter compatibility matrix helps, but there's still no single person watching all three.

5. Eval coverage gaps — the eval suite is comprehensive, but the April 2026 regression slipped through every check. Each change passed individually. The compound effect was never tested. Evals catch what you thought to test for — not what you didn't.

6. Sandbox-bypass retraining — the model learned from training data that it can retry failed commands with `--dangerously-skip-permissions`. It's not malicious — it just learned that the flag makes the command succeed. The kernel sandbox is the real safety floor, but the model keeps trying to get around it. That tension is still unresolved.

Why share these openly? Because credibility comes from honesty. A system that claims no weaknesses hasn't been tested in production.

---

## SLIDE 57 — Section Divider: Synthesis & Close

Part fourteen — Synthesis and Close. Eight minutes. All 22 decisions, mapped to the architecture you started with.

---

## SLIDE 58 — 22 Decisions Mapped to 5 Layers

This is the payoff slide. Remember the five-layer architecture? Now every layer has its design decisions filled in.

Twenty-two decisions, five layers, one diagram. Now, here's your homework — and I mean this seriously. Go back through these 22 decisions on your own. Re-read the slides where we introduced each one. Ask yourself: does this decision still seem right? Would I have made the same choice? Where would I disagree, and why? The best way to learn a design is to argue with it.

---

## SLIDE 59 — Six Transferable Principles

We covered 22 decisions specific to Claude Code. But six of those decisions are bigger than Claude Code — they apply to any agentic system you build. These are the patterns that transfer.

1. The model is the brain, but the harness is what makes it reliable. The model is non-deterministic — same input, different output every time. The harness around it — the loop, the tools, the permissions, the sandbox — is deterministic. Same tool call, same validation, same permission check, every time. A simple while-true loop with disciplined tools beats a fancy multi-agent graph, because when something goes wrong, you can actually trace what happened.

2. One main thread, everything funnels through it. Sub-agents, hooks, MCP tools, custom skills — they all feed into the same agent loop. Not separate loops, not separate orchestrators. One loop, one dispatch pipeline, one permission cascade. That's what makes it debuggable and auditable.

3. Tools are contracts, not functions. A tool isn't just "code that does something." It's a five-part contract — schema, permission, concurrency flag, read-only flag, and render function. Skip any one of those parts, and you lose a guarantee. The contract is what makes 50-plus tools work safely through the same pipeline.

4. Context is a memory bus — design eviction and rehydration together. You can't just throw away old conversation to free up space. You have to put back the things the model needs — recent files, active plans, project rules, cache prefix. Eviction without rehydration is data loss. They're one transaction or nothing.

5. Defense in depth is a cost gradient. Cheap checks first, expensive checks last. Static rules in microseconds. Tool-level checks in milliseconds. Permission mode check. LLM classifier in hundreds of milliseconds. Human prompt as the last resort. And behind all of it, the kernel sandbox as the floor that nothing can bypass. Each layer costs more but catches more — and you never skip a cheap layer just because you have an expensive one.

6. Lazy-load capability, never lazy-load context. Load tool names at startup so the model knows what's available. But don't load full schemas until the model actually needs them — that's lazy loading. The opposite applies to context: always load what the model needs to reason. Starve it of capability and it asks for more. Starve it of context and it makes bad decisions silently.

These six principles aren't Claude Code-specific. If you're building a coding agent, a customer support agent, an internal automation agent — these patterns apply. The model, the tools, and the domain change. The architecture patterns don't.

---

## SLIDE 60 — Role-Based Questions

Screenshot this slide. Seriously — take a photo right now. These are the questions you should bring to your next planning meeting, organized by role. Five questions each.

For Engineers:

1. Where does state live? We covered four memory tiers — working memory, session memory, project memory, tool-result memory. Which tier holds each piece of state in your system?
2. Which tools are concurrency-safe? Remember the concurrency flag from the tool contract — read is parallel-safe, edit is not. Have you classified every tool in your system?
3. What's the context budget per turn? We showed that 26 percent of the 200K window is gone before the user types anything. Do you know your numbers?
4. Where's the cache prefix boundary? One misplaced dynamic token in the static prefix turns a 10x cost saving into full price. Where exactly does your boundary sit?
5. Are tool failures idempotent? If a tool fails and retries, does the second run produce the same result as the first — or does it create duplicates?

For Engineering Managers:

1. What's the eval discipline? We covered five eval types — task completion, tool selection, permission accuracy, latency, and regression. Which ones are you running, and how often?
2. Is the cost gradient right? Cheap checks first, expensive checks last — that's the permission cascade. Are your teams putting the cheapest check at the top?
3. Are sub-agents ROI-positive? Sub-agents give 90 percent better performance but cost 15 times more tokens. At your usage volume, does that math work out?
4. Where's the eval coverage gap? The April 2026 regression passed every individual eval. What compound failures could slip through your test suite?
5. How do you onboard when 80 percent of code is AI-written? If the agent wrote most of the codebase, how does a new engineer learn it? That's a people problem, not a tooling problem.

For TPMs — Technical Program Managers:

1. What's the rollback plan when the harness breaks? The model is swappable — Layer 5 changes, the rest stays. But what if Layers 1 through 4 break? How fast can you roll back the harness itself?
2. What's the dependency on model upgrades? When the model provider ships a new version, does your system need to change? How tightly coupled are you?
3. What's your April 2026 equivalent? Three unrelated changes shipping in the same window and compounding. What's the version of that scenario in your system?
4. Lazy versus eager capability loading? We showed that eager loading ate 134K tokens. Are you loading anything eagerly that should be lazy?
5. Which capability ships next quarter? Of the 22 decisions, which ones are you still building — and which ones are you skipping intentionally?

For Product Managers:

1. Which user surface ships first? CLI, IDE plugin, web app, Slack bot — each has different tradeoffs. Which one reaches your users fastest?
2. What does "success" mean for emergent failures? Some failures — like the compaction retry loop — only appear at scale. How do you define success when you can't predict every failure mode?
3. How do you monetize when most of the work is non-AI infrastructure? The model API is one layer out of five. The other four — the harness — are pure engineering. How does pricing reflect that?
4. Ask versus act — where's the trust boundary? Six permission modes, from "ask everything" to "bypass." Where does your product default, and why?
5. How does the permission UX work across surfaces? A Y/n prompt works in a terminal. What does permission look like in Slack? In a CI pipeline? In a web dashboard? Same decision, different surface.

---

## SLIDE 61 — Q&A + What's Next

Let's open the floor. Four questions to get you started. Are you building an agent at work? Have you shipped MCP yet? What's your stance on bypass mode? Which design decision surprised you most? And if you want to go deeper — Interview Kickstart's AI Systems Track has over 700 FAANG instructors, live cohorts with one-on-one mocks, and in the EdgeUp program you actually build a real agent. That's the agent-focused tier.

---

## SLIDE 62 — Thank You / Close

You just designed Claude Code. Now go build your own agent. Three next steps: one — book a free strategy session with an IK advisor. Two — mention this masterclass for priority enrollment. Three — stay tuned for the next masterclass. Thank you all.

---

*End of script.*
