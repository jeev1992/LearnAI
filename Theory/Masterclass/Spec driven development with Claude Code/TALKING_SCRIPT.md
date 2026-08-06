# Talking Script — Spec-Driven Development with Claude Code: From Idea to Deployed App

---

## SLIDE 1 — Title

[IK presenter opens the session — welcomes the audience and introduces today's masterclass: "Spec-Driven Development with Claude Code — From idea to deployed app."]

---

## SLIDE 2 — About IK / Your Host

A quick word about Interview Kickstart. Twelve-plus years in this space. Over 27,000 enrolments. More than 200 hiring partners. We focus on outcomes — 18 domain-specific tracks, with student compensation ranging from 63 lakhs to 1.7 crore, and top student comp at 1.7 crore. Behind the curriculum: 700-plus FAANG+ instructors, 70-plus dedicated AI/ML instructors, and an average of 13 years of experience per instructor. IK has been recognized by Time magazine in the Top 100, and by GSV in the Top 150, of their global EdTech lists for 2025.

[SPEAKER NOTE: IK's site says "enrolments" and "instructors," not "placements" or "hiring managers." Frame it honestly.]

---

## SLIDE 3 — IK Instructors

These are the people behind the curriculum — AI/ML engineers, hiring managers, and technical recruiters from FAANG+ and Tier-1 companies. Names you'll recognize: Omkar Deshpande from Interview Kickstart, plus instructors from Meta, Walmart, Amazon, Microsoft, Google, Disney, Indeed, Airbnb, Box, and Uber. The point isn't the logos — the point is that the curriculum is designed and delivered by practitioners who've actually shipped this stuff at scale.

---

## SLIDE 4 — Introduction: Parijat Roy

Hi everyone, my name is Parijat Roy. I'm a Lead Data Scientist at Microsoft, with about 11 years at the company — I started as a software engineer and I'm now a lead scientist. Today I lead business metrics and recommendations for M365 Copilot Desktop, and most of my work sits in textual processing, AI relevance metric design, and search relevance on Microsoft Copilot.

Here's why I'm the right person to run this session. I don't just build AI — I use it every single day. GitHub Copilot and Claude for my day-to-day engineering work; M365 Copilot for planning my day, taking meeting notes, doing org-wide document search. So I've lived on both sides — designing the AI systems, and being the user who has to actually get work done with them. And what I've learned is that the engineers pulling ahead right now aren't the ones with the cleverest prompts. They're the ones who've changed *how* they build — who treat the AI as a builder they direct, not a search box they copy from. That shift is exactly what we're going to do live today. So with that, let's jump in.

---

## SLIDE 5 — The Hook

Before I put anything on the screen, let me ask you something — and I actually want answers. Chat or out loud, both work. **How many of you are already using an AI tool to build apps — Claude, ChatGPT, GitHub Copilot, Cursor, anything?** Hands up. Okay, good — most of the room.

Now the real question I care about: **when you sit down to build something with one of these tools, what does that actually look like for you?** Walk me through your workflow. Do you open a chat and describe the whole thing in one big prompt? Do you go function by function, tab-completing as you type? Do you paste an error back in and ask it to fix it? Do you write anything down first — or do you just start typing and see what comes out?

[PAUSE — pull 2-3 answers. Reflect them back:] "So a lot of you are in the chat, describe-and-paste camp." … "Someone said they just prompt and fix, prompt and fix — that's super common." … "One person writes notes first — hold that thought, you're ahead of the curve."

[Optional probe:] **And be honest — how often does that approach fall apart on you?** The app works for the demo, then breaks the moment it gets bigger? … Yeah. I see the nods.

I'm asking because *how* you drive these tools matters more than *which* tool you pick — and most people are using a Level-4 tool with a Level-1 workflow. So keep your own approach in mind as we go, because by the end of this session I want you comparing it against what we do here.

And here's the promise that frames the whole hour: **What if you could go from a product idea to a deployed, production-ready app in under 90 minutes?** No boilerplate. No copy-pasting from Stack Overflow. No context-switching between fifteen browser tabs. That's exactly what we're going to do together — take an idea that's one sentence long right now, and finish with a live URL you can open on your phone before you leave. Not a slide about it. The real thing.

---

## SLIDE 6 — Power-Packed Agenda

Here's where we're going. Eight stops. First, **why AI changes everything** — the context on how the software development lifecycle is shifting. Then we **meet Claude Code**. Then the heart of it: we **write the spec**, we **scaffold from the spec**, we **build the core features**, and we **iterate and polish**. Then a short section on how IK can help you **become a 10x professional**. And finally, we **deploy and demo** the real thing. We'll keep coming back to this map so you always know where we are.

---

## SLIDE 7 — Section: How AI Is Reshaping the SDLC

Part one — how AI is reshaping the software development lifecycle. This is the context every engineer, PM, and EM needs right now, before we touch a single tool.

---

## SLIDE 8 — The SDLC You Know

Here's the lifecycle you already know. Requirements, design, implement, test, deploy — a straight line, left to right. And three things define it. **Timeline** — weeks to months. **Handoffs** — every stage passes work to a different role, and every handoff leaks information. And the quiet killer: **drift.** The spec lives in a doc somewhere. The code lives in a repo. And the moment they're written, they start drifting apart — until six months later the doc describes an app that no longer exists. Hold onto that word, drift. It's the exact problem spec-driven development is built to solve.

---

## SLIDE 9 — The Pain Points, by Role

And this drift shows up differently depending on where you sit.

**Software engineers** — 60-plus percent of your time goes to boilerplate and setup, constant context-switching between tools, and translating vague specs into working code.

**Product managers** — weeks between writing a spec and seeing a working prototype, no easy way to validate an idea without borrowing engineering capacity, and specs that drift from what actually gets built.

**TPMs** — estimation is guesswork, velocity is unpredictable, and cross-team dependencies slow everything down.

**Engineering managers** — hiring can't keep up with demand, senior engineers burn time on junior-level tasks, and it's expensive to prototype before you commit real resources.

Different symptoms, same root cause: the gap between intent and working software is too wide, and too manual.

---

## SLIDE 10 — The AI-Augmented SDLC

Now watch what AI does to that same lifecycle. The stages don't disappear — requirements, design, implement, deploy are all still here. What changes is the *gaps between them collapse.* Requirements become a concise, scoped spec. Design becomes rapid architecture and wireframes. Implementation becomes automated coding by AI agents. Deploy becomes continuous delivery with an AI bridge. The line is the same — but the distance from one end to the other goes from sprints to hours. Spec to working prototype in an afternoon. That's the whole shift in one picture.

---

## SLIDE 11 — Not All AI Coding Tools Are Equal

But here's the catch — and it's important, because people lump all AI coding tools together, and they are not equal. There are four levels of autonomy.

**Level 1 — Autocomplete.** GitHub Copilot tab-completion. It suggests the next line. Helpful, but it's still you driving every keystroke.

**Level 2 — Chat-based.** ChatGPT, in-IDE chat panels. It answers questions and generates snippets, but *you* are the one moving code around.

**Level 3 — Edit-based.** Cursor, Copilot Edits. Now it can modify files in context — a real step up.

**Level 4 — Agentic.** This is Claude Code. It reads your codebase. It plans. It executes. It iterates. It even manages git. The autonomy and the codebase-awareness both jump. Everything we do today lives at Level 4 — and that difference is the whole reason this session is possible.

---

## SLIDE 12 — The "Vibe Coding" Trap

Now, a warning — because having a Level 4 tool doesn't automatically save you. There's a trap I call vibe coding.

**What most people do:** prompt an LLM with a vague idea, copy-paste the output into their project, fix the errors by hand, and repeat — with no structure. And it *works*… for a demo. Then it falls apart the moment you try to scale it, because there's no source of truth. Every prompt is a fresh guess.

**What actually works:** start with a structured spec. Feed that spec to an agentic tool. Let the AI build *from the spec*, not from ad-hoc prompts. And iterate against the spec. The result is reproducible, scalable, and team-aligned. Same AI, completely different outcome. The difference is entirely whether there's a spec in the loop.

---

## SLIDE 13 — Spec-Driven Development

Which brings us to the core idea of today: **spec-driven development.**

Your product spec becomes the executable blueprint. Read the flow left to right: the **product spec** is the single source of truth. It feeds the **AI agent** — Claude Code — which executes *against* that spec. Out comes a **working application** that humans review and iterate on. The critical word is *from.* The AI builds from the spec, not from whatever you happened to type in the moment. The spec is the contract. Everything downstream is held accountable to it.

---

## SLIDE 14 — What This Means for You

And this changes the job for everyone at the table.

**Software engineers** — you write less boilerplate and focus on architecture. Your value shifts to making the right technical choices, not typing them out.

**Product managers** — your spec directly drives implementation. You validate ideas in hours, not sprints.

**TPMs** — velocity becomes predictable, because the spec defines scope and the AI delivers against it. Cleaner scope-to-effort mapping.

**Engineering managers** — smaller teams ship more, because you can prototype first and commit resources second, and your senior engineers get to do senior work.

Notice the theme: the human moves *up* the value chain. Less typing, more deciding.

---

## SLIDE 15 — Section: Introducing Claude Code

Part two. Let's meet the tool — Claude Code, an agentic coding tool that lives in your terminal.

---

## SLIDE 16 — What Is Claude Code?

So what exactly is it? It's an agentic AI coding tool built by Anthropic. And the first surprising thing: it lives in your **terminal** — not a browser, not an IDE plugin. It reads your entire codebase and understands your project context. And then it takes multi-step actions on its own — it creates and edits files, runs commands and tests, manages git operations, and installs dependencies.

Look at the little terminal on this slide. You type `claude`, then "Read the spec and scaffold the project," and it starts working — reading the spec, planning the structure, creating files. The mental model I want you to hold: think of it as a *tireless junior engineer* sitting in your terminal. You give it intent and context; it does the legwork.

---

## SLIDE 17 — How It Compares

Let's put it side by side with the tools you already use. Look down the columns. **Autocomplete** — Copilot and Cursor do it; Claude Code isn't really about that. **Chat and Q&A** — Cursor and ChatGPT do it, Claude Code does it. But then look at the bottom rows, where it separates. **Full codebase awareness** — only Claude Code, fully. **Multi-file editing** — Cursor and Claude Code. And then the three that only Claude Code checks: **running commands and tests, git operations, and agentic multi-step execution.**

One honest caveat, and it's on the slide: Claude Code doesn't *replace* your IDE. It works alongside it — VS Code plus the terminal. This isn't "throw away your editor." It's "add a builder next to it."

---

## SLIDE 18 — Three Concepts to Know

Before the demo, three concepts that'll show up over and over, so they don't slow us down later.

First, **CLAUDE.md** — a project memory file that gives Claude Code persistent context about your project. Think of it as the project's brain: your conventions, your stack decisions, your file structure. It's the thing Claude re-reads so it doesn't forget who you are between sessions.

Second, **spec files** — structured documents that describe what to build. Claude Code treats these as build instructions. Not vague prompts — detailed blueprints.

Third, **the agentic loop** — Claude plans, executes, verifies, and iterates. It doesn't just generate code and walk away; it checks whether the code actually works and fixes issues on its own. That loop is what makes it Level 4 instead of Level 2.

Those three — CLAUDE.md, spec files, and the agentic loop — are the backbone of everything we build today.

---

## SLIDE 19 — Claude Code in Practice

Here's what it actually looks like when you fire it up. You run `claude`. It greets you — "Welcome to Claude Code, project: wandertogether, files indexed: zero, new project." It asks what you'd like to do. You type: "Read the product spec and scaffold a Next.js project." And it goes — reading spec.md, planning the project structure, creating files. That's the entire interface. No dashboard, no fifteen tabs. A conversation in your terminal that results in real files on disk. Now let's give it something to build.

---

## SLIDE 20 — Section: Writing the Product Spec

Part three — writing the product spec. This is the single most important artifact in spec-driven development, so we're going to slow down here.

---

## SLIDE 21 — "The Spec Is the New Code"

Here's the principle, and I want it to land: **in spec-driven development, the quality of your spec determines the quality of your output.** Garbage spec, garbage app. Precise spec, production-quality app. It's that direct. The AI is not going to rescue a vague idea — it's going to faithfully build whatever ambiguity you hand it. So the spec isn't a formality you do before the "real work." The spec *is* the real work. It's the most important thing you'll write all session.

---

## SLIDE 22 — Anatomy of an AI-Consumable Product Spec

So what goes into a good spec? Seven parts.

One, **product overview** — what is it, and who is it for. Two, **user personas** — your target users, with real context. Three, **core features** — modules with clear scope. Four, **tech stack** — framework, database, auth, hosting. Five, **data model** — your key entities and how they relate. Six, **UI/UX requirements** — pages, navigation, design language. And seven, **non-functional requirements** — performance, security, accessibility.

Three of these deserve extra care. On **core features**, be specific — write "user can filter by date," not "add filters." On **tech stack**, decide upfront; don't make the AI guess, because it *will* guess, and you may not like the guess. And on the **data model** — pay attention here, because this is what the AI reads *first* when it builds your database schema. Get the entities right and everything downstream falls into place.

---

## SLIDE 23 — The WanderTogether Spec

And here's the exact spec we'll build from today. Our app is **WanderTogether**. Read it with me: "Create a spec for a React-based website with three user scenarios — one, plan trips collaboratively; two, find and connect with other travellers; three, build a personal travel portfolio that tracks every journey."

Then we fill in the anatomy from the last slide. **Product overview** — a collaborative travel-planning platform that combines trip planning, companion matching, and travel stories. **Tech stack** — ReactJS and a SQL database. **Core feature modules** — Planning, Matching, Stories, Explore. **Data model** — the key entities are Users, Trips, Itineraries, Matches, and Stories. **UI structure** — landing page sections, navigation, and a light-blue color palette.

Notice how much decision-making is packed into that. Every one of those lines removes a guess the AI would otherwise have to make. That's what a good spec does — it converts ambiguity into instructions.

---

## SLIDE 24 — From Spec to CLAUDE.md

Now, one more move before we build. We have two documents doing two jobs. On the left, the **product spec** — written for humans *and* AI. It's the plain-language description of what we want. On the right, **CLAUDE.md** — written specifically for Claude Code. It's where the conventions, stack decisions, and structure live so Claude has persistent context.

The way to think about it: CLAUDE.md is the *bridge* between human intent and AI execution. The spec says what to build; CLAUDE.md makes sure Claude remembers *how* we build, every time it acts. With both in place, we're ready to scaffold.

---

## SLIDE 25 — Section: Scaffold the App from Spec

Part four — scaffold the app from the spec. From an idea to a project skeleton in minutes.

---

## SLIDE 26 — The Scaffolding Step

Here's what scaffolding means. On the left, the **product spec**. In the middle, **Claude Code**. On the right, a full **project skeleton** — the project structure and routing, the layout components and shared UI, the config files like env and Tailwind, and the package dependencies actually installed.

Now sit with the number at the bottom: this normally takes two to four hours of manual setup. Choosing the folder structure, wiring the router, configuring Tailwind, getting env files right — the boring, error-prone plumbing before you've written a single feature. Watch what happens when the spec drives it instead.

---

## SLIDE 27 — What Just Happened

And here's what Claude Code generated. A complete `wandertogether/` tree — an `app/` folder with `layout.tsx`, `page.tsx`, and route groups for auth, plan, connect, and stories; a `components/` folder split into ui, layout, and shared; plus `lib/`, `prisma/`, and — right there in the root — `CLAUDE.md`, `spec.md`, and `package.json`.

Look at *why* each choice was made. The app routing matches the page structure from the spec. The component organization follows the conventions in CLAUDE.md. The database schema is scaffolded and ready for implementation. Every single decision traces back to something we wrote down. There was no guesswork — the spec drove all of it. That's the payoff for the time we spent on the spec.

---

## SLIDE 28 — Section: Build Core Features

Part five — build the core features. This is the biggest block, twenty minutes, because this is where you'll see the agentic loop in action.

---

## SLIDE 29 — What We're Building

Three things in this block. **Auth and user management** — sign up, sign in, session handling. **Database and data model** — schema, migrations, and seed data. And the **UI landing page and components** — the hero, the feature sections, the personas, all responsive. These three turn the empty skeleton into something you can actually click through. Let's start with auth and watch how Claude approaches it.

---

## SLIDE 30 — What Claude Code Just Did, Without Being Asked

This is the slide I want you to really watch, because it's the whole thing in miniature. I asked for auth. Here's the sequence Claude ran on its own: it read the spec to determine the auth requirements. It selected the right auth library and approach. It installed the dependencies. It created the auth routes and middleware. It set up the environment variables. It wired auth into the layout. And then — this is the part — it *tested the flow, found an issue, and fixed it.*

I didn't tell it to do steps two through seven. I said "build auth." That gap — between an AI that *suggests* and an AI that *builds, verifies, and repairs* — is the entire reason we're here. That's Level 4.

---

## SLIDE 31 — The Agentic Development Cycle

Let's name the loop you just watched. Four steps, going around. One — you **prompt with intent**: what you want, not how to do it. Two — Claude Code **reads context**: the spec, CLAUDE.md, and the existing code. Three — it **implements and verifies**: writes, runs, tests, fixes. Four — you **review and iterate**: accept, adjust, or redirect.

And then it goes around again. Two things stay constant every lap: the spec is the source of truth at every step, and the engineer doesn't write boilerplate — the engineer makes decisions. That's the new shape of the work.

---

## SLIDE 32 — Section: Iterate & Polish

Part six — iterate and polish. Because the last 20% is where quality actually lives.

---

## SLIDE 33 — Why the Polish Step Matters

Here's an honest truth about AI-built apps: the first pass gets you 80% of the way, fast — but it's the last 20% that separates a demo from a product. So what needs attention after that first pass? UI inconsistencies — spacing, alignment, colors. Responsive behavior across screen sizes. Edge cases and error states. Copy and content refinement. Micro-interactions and animations. And accessibility gaps.

And the good news is you polish the *same way* you built — by talking to Claude against the spec. "Fix the spacing on the hero section to match the spec." "Make the companion cards responsive for mobile." "Add error handling for the auth flow." "The heading font should be X, not Y — update it globally." Notice these are all intent, not implementation. You're still the architect; Claude still does the typing. Polish isn't a different mode — it's the same loop, aimed at quality.

---

## SLIDE 34 — Section: Be a 10x Professional with IK

[Transition to the IK section.] So — we've seen what's possible. Let me spend a few minutes on how you actually build these skills, and where IK fits.

---

## SLIDE 35 — The Four Stages of AI Denial

Let me start with something I see constantly. I call it the Four Stages of AI Denial. Stage one: "I can't do AI — it's moving too fast for me." Stage two: "I can't do AI — but my job is unique, so I'm safe." Stage three: "I can't do AI — there's just too much out there." And stage four: "I can't do AI — I'll have to downlevel to get in."

If you've felt any of these, you're normal — and you're also wrong on all four counts. The pace is manageable if you have a path. No job is permanently safe *or* permanently unique. The volume is only overwhelming without a curriculum. And you don't downlevel — you re-level around your existing domain expertise. The real challenge isn't ability. It's picking the right path.

---

## SLIDE 36 — AI Upskilling Curve

So here's the map. Think of AI skills as a curve with five levels. Level one — **working with LLMs.** Level two — **productivity with AI copilots.** These first two are *augmentation* — you get more productive with what you already do; this is where "10x your productivity" lives. Then level three — **building complex AI agents and GenAI apps.** Level four — **building modern ML models.** Level five — **deep ML.** These upper levels are *transformation* — building genuinely new, industry-scale use cases.

The key message: there's no one-size-fits-all. You don't need to be at level five to be valuable. You build your AI-quotient by finding the right rung for *your* goals.

---

## SLIDE 37 — Roles to Target

And each part of that curve maps to real roles. The augmentation and agent levels — LLMs, copilots, GenAI — point you toward **AI SWE, AI product managers, AI EMs and TPMs.** The next level up points to **AI engineering** roles. And the deep-ML end points to **modern ML engineer** roles. So the curve isn't abstract — every rung is a concrete career target with real job titles attached.

---

## SLIDE 38 — IK's Programs Across the Curve

And IK has a program for each stretch of that curve. If you're at the productivity-and-agents end, there's the **Agentic AI Accelerator and Interview Lab** — agentic AI, industry-relevant projects, and interview prep in your domain. In the middle, the **Transformative GenAI and Agentic AI program** — GenAI plus agentic AI plus interview prep. And at the far end, **Forward Deployed AI Engineering** — for AI engineering and dedicated FDE roles, with interview prep tailored to them. Wherever you are on the curve, there's an on-ramp.

---

## SLIDE 39 — Customizable Interview Prep

And this is fully customizable to who you are. Whether you're **early career**, an **experienced IC**, or in **management**, and whatever your track — backend, frontend, full-stack, ML, data engineering, data science, security, SRE/DevOps, embedded, test, cloud, mobile, BI — or on the management side, EM, technical PM, TPM — the prep and career support bend to fit your path. It's not a single fixed course. It's built around your starting point.

---

## SLIDE 40 — Driving Acceleration

Two engines drive the acceleration. **Mock interviews** — live sessions from Tier-1 experts, simulated interviews with actual hiring managers, detailed written and verbal feedback, and regular check-ins to catch your anti-patterns before they cost you an offer. And **placement assistance** — LinkedIn and resume masterclasses, behavioral interview strategies, and offer-negotiation coaching. Prep *and* the path to the offer, together.

---

## SLIDE 41 — Interview Prep + Career Services

Broken out, it's two pillars. **Interview prep** — DSA, system design, domain-based interview modules, and leadership-round prep for EMs. And **career services** — personalized mock interviews, resume optimization, LinkedIn and personal branding, behavioral coaching, a salary-negotiation masterclass, and job referrals. The technical bar and the career machinery, side by side.

---

## SLIDE 42 — Placement Assistance

And the outcomes are backed by real infrastructure. Performance-based referrals. 200 hiring partners in India. A 5x-to-7x ROI. And roughly 250 profiles shared with hiring partners every quarter. The referrals are earned through performance — but the network is there, and it's active.

---

## SLIDE 43 — Our Offerings: From AI Enablement to Modern ML

Let me line up the three pathways so it's concrete. The **Agentic AI Accelerator and Interview Lab** — 12 weeks plus 3 months — is where you *become AI-enabled*, and it's where the bulk of the AI jobs are today. It's also the place to start if you're unsure. The **Transformative GenAI and Agentic AI program** — 3 plus 3 months — goes deeper. And **Forward Deployed AI Engineering** — 6 months — is for *transitioning into an FDE role.* Three clear on-ramps, depending on how far you want to go.

---

## SLIDE 44 — Pricing

And the pricing, transparently. The Agentic AI Accelerator runs roughly 1.5 to 2.8 lakh. Forward Deployed AI Engineering is around 2.75 lakh. The Transformative program sits in the 2-to-2.8 lakh range. And there's a 50% refund option, financing with EMIs, alumni and other scholarships, enroll-now-start-anytime flexibility, and placement assistance backed by those 200-plus hiring partners. The details will be shared — for now, just know there's a path that fits your budget and your timeline.

---

## SLIDE 45 — Section: Deploy to Vercel + Final Demo

Part seven — deploy. From local to live in minutes. Let's make good on the promise from the opening slide.

---

## SLIDE 46 — From Code to Live URL

Three steps to a live URL. Step one — **git push, via Claude Code.** I just say "commit all changes and push to main," and Claude stages the files, writes a meaningful commit message, and pushes. Step two — **connect to Vercel.** Link the GitHub repo; Vercel auto-detects Next.js and configures the build settings for us. Step three — **live in 90 seconds.** The build runs, it deploys to a `.vercel.app` URL, and you share the link. And it's *real* — not a mockup, a running application on the internet.

---

## SLIDE 47 — Spec → Deployed App

Step back and look at the arc. On the left, the spec we wrote. On the right, the deployed result. And here's the one line I want you to remember from this whole session: **the spec was the blueprint, Claude Code was the builder, and the engineer was the architect.** Three distinct roles — and notice the human's role is the architect. You didn't lay every brick. You decided what to build and held it to the plan.

---

## SLIDE 48 — Section: Wrap-Up & Key Takeaways

Let's wrap up — what we just did, and what it means for you.

---

## SLIDE 49 — What We Built

Retrace the whole journey. We started with a blank slate — no code, just an idea. We wrote a spec, with every decision documented. We scaffolded the full project — routing, layouts, config. We implemented auth, database, and UI. We polished it — responsive, error-handled. And we deployed it — a live URL, a real app. In fact, you're looking at it right now.

Idea, to spec, to scaffold, to build, to polish, to deploy — all in one session. That's not a someday capability. That's today, and you just watched it happen end to end.

---

## SLIDE 50 — Key Takeaways

Four things to carry out of this room. One — **the SDLC is compressing.** AI collapses the gap between idea and product; the timeline is hours, not sprints. Two — **spec-driven development beats vibe coding.** Structure and reproducibility win at every scale beyond a throwaway prototype. Three — **Claude Code is the most capable agentic tool today.** It doesn't suggest — it reads, plans, builds, tests, and fixes. And four — **every role is affected.** Engineers, PMs, TPMs, EMs — everyone gets new superpowers, and new responsibilities.

---

## SLIDE 51 — The Real Question

I'll leave you with this. The engineers who thrive won't be the ones who type the fastest — they'll be the ones who learn to *architect* with AI, not just code with it. Because the question was never whether AI will change how you build software. It already has. The only real question is whether you'll lead that change — or react to it. My hope is that today nudged you toward leading it.

---

## SLIDE 52 — Q&A / Thank You

That's it — thank you. I'm Parijat Roy, and I'd love to take your questions. You can find me on LinkedIn at linkedin.com/in/parijatroyy. The full WanderTogether project is on GitHub at github.com/parroy/WanderTogetherIK, and the Claude Code documentation is at code.claude.com/docs. Let's open it up for Q&A.
