# WanderTogether — Live Demo Runbook (Plan-Mode-First Approach)

> Spec-Driven Development with Claude Code. This is the **"CLAUDE.md / spec first, then build, then deploy"** flow — the cleaner, more pedagogical demo that maps directly to the deck (Spec → Scaffold → Build → Polish → Deploy).

---

## 0. Pre-Flight (do the DAY BEFORE, off-screen)

### Install & verify
```powershell
node --version      # v18+
npm --version
git --version
claude --version
vercel whoami        # must print your username
```
Install anything missing:
```powershell
winget install OpenJS.NodeJS.LTS Git.Git GitHub.cli
npm install -g @anthropic-ai/claude-code vercel
vercel login          # log in WITH GITHUB
```

### Accounts
- **Anthropic / Claude** account with access (Pro/Max or API).
- **GitHub** — same account used for the repo and Vercel.
- **Vercel** — free Hobby tier, logged in with GitHub.

### Create the hosted database ahead of time (needed for a working Vercel deploy)
Use **Vercel Postgres (Neon-backed)** — no Docker, persists on Vercel:
1. vercel.com → (create/select a project) → **Storage → Create Database → Postgres**.
2. Copy the `DATABASE_URL` connection string — you'll paste it into `.env` and Vercel env vars.

### Fallback safety net
Build the whole thing once in rehearsal, commit it, and keep it on a branch:
```powershell
git add -A; git commit -m "Working fallback"; git branch fallback
```
If a live step stalls: `git checkout fallback` and keep narrating.

> **Timing note:** the scaffold+build takes ~20–30 min ("Cooked for 28m" in testing). **Do NOT watch it live.** Either do the fast interactive wizard live and cut to a pre-built app, OR kick the build and talk slides 20–27 while it cooks.

---

## PHASE A — Fresh Start

```powershell
cd ~\Desktop
mkdir wandertogether; cd wandertogether
git init
claude
```
Press **Shift+Tab** until it shows **plan mode** (or launch `claude --permission-mode plan`).

> **Narration:** "I'm starting in *plan mode*. That means Claude can read and think and propose — but it can't touch a single file until I approve. The engineer stays in control."

---

## PHASE B — Write the Blueprint FIRST (spec.md + CLAUDE.md)

**Prompt 1 — forbid code, produce only the two blueprint files:**
> We're building WanderTogether, a collaborative travel app. Do NOT write any application code yet. In plan mode, produce two files only: (1) `spec.md` — a full product spec with Product Overview, User Personas, Core Feature Modules, Tech Stack, Data Model, UI/UX, Non-Functional Requirements; and (2) `CLAUDE.md` — our persistent project memory capturing stack decisions and rationale, folder conventions, the data model, and coding standards.
>
> Lock these in: React/Next.js full-stack + TypeScript + Tailwind, Prisma with **PostgreSQL (Vercel Postgres, Neon-backed)**, NextAuth email/password auth. Four modules: Planning (collaborative trips + itinerary voting), Matching (connect travellers), Stories (personal travel portfolio), Explore (public feed). Entities: Users, Trips, Itineraries, Matches, Stories — expand as needed. Deploy target: Vercel.

### The wizard decisions (and WHY) — this is the teaching core

Claude Code runs an interactive intake. **Every choice below is deliberate.** The theme: *the AI recommends smart defaults; the engineer picks based on constraints.*

| Wizard step | Options | **Pick** | Why |
|---|---|---|---|
| **App concept** | Group planner / personal organizer / social / other | **Type: "a mix"** | Full spec needs all 3 scenarios (plan + match + portfolio), not the narrow default. |
| **Tech stack** | React+Express (Rec) / Next.js full-stack / frontend-only | **Next.js full-stack** | One app, one deploy. Express = 2 services to deploy. Overrode "Recommended." |
| **Scope** | Small slice (Rec) / Broader scaffold | **Broader scaffold** | Demo must show all 4 modules, not one flow. Overrode "Recommended." |
| **Auth method** | Email+Google OAuth (Rec) / Email only / Stub | **Email/password only** | Google OAuth = Google Cloud Console detour = live-failure trap. Still *real* auth. Overrode "Recommended." |
| **Database** | Postgres via Docker (Rec) / SQLite | **Postgres (hosted)** | Vercel deploy needs persistence; hosted Postgres = no Docker, persists. |
| **Postgres host** | Vercel Postgres (Rec) / Neon / Supabase | **Vercel Postgres (Neon-backed)** | Simplest env-var setup for a Vercel app. **Took** the recommendation — it matched the constraint. |
| **Media storage** | Vercel Blob (Rec) / Cloudinary / Defer to v2 | **Defer to v2** | Images are optional URL strings; uploads add breakable scope. Overrode "Recommended." |
| **Realtime** | Polling (Rec) / WebSockets / No sync | **Polling / refetch-on-focus** | Nice UX, zero extra infra. WebSockets = most demo-fragile choice. **Took** the recommendation. |
| **Matching UX** | Swipe deck (Rec) / Search feed / Trip board | **Search feed** | Swipe gestures = build-heavy + fragile. Maps to connect/accept. Overrode "Recommended." |
| **Messaging gate** | Open messaging (Rec) / Connect-then-message / Type | **Type: "no messaging in v1"** | Plan agent added chat = scope creep. Cut it in the spec, where cutting is free. |
| **NextAuth version** | v4 stable (Rec) / Auth.js v5 beta | **NextAuth v4 (stable)** | First build used v5 beta and it broke (Node-vs-Edge runtime bug). Stable beats beta for a live demo. **Took** the recommendation. |
| **Explore scope** | Both Trips + Stories (Rec) / Stories only | **Stories only** | Both = tabbed feed + public-trip logic = more scope. Explore isn't the hero module. Overrode "Recommended." |
| **Voting rights** | Viewers can vote (Rec) / Editors+Owner only | **Viewers can vote** | Best collaboration story AND simpler (no role-gate). Low-stakes call — **took** the recommendation, didn't agonize. |

### Key narration beats during the wizard
- **On overriding "Recommended":** "Five times it recommended something; I overrode it three. Not because it's wrong — because *I* know my constraints and it doesn't. AI is the builder; I'm the architect."
- **On taking "Recommended" (Postgres host, Polling):** "This time I'm *taking* the recommendation — it matches my constraint. The lesson isn't 'distrust the AI,' it's 'check the recommendation against your constraint.'"
- **On the Plan subagent:** "It spawned a *Plan agent* — its own context, its own task — designed the data model in 4 minutes, and handed it back. That's multi-agent delegation, automatic."
- **On cutting messaging (scope creep):** "The plan agent added messaging. I never asked for it. **This is why you review the spec before you build** — killing scope in a doc is free; killing it in code costs an afternoon."
- **On NextAuth v4 vs v5 (callback):** "An earlier run used the *beta* auth library and it broke mid-build on a runtime conflict. It self-healed — impressive — but the tool now recommends the stable v4. On a live stage, boring and stable beats new and clever."
- **On low-stakes choices (pacing):** "After several deliberate overrides, I just *took* the voting recommendation without a fight. A good architect knows which decisions don't matter and doesn't waste time on them."

### Review, then lock
Read `spec.md` + `CLAUDE.md` on screen (slides 20–24 payoff). Then:
> Approve. Save spec.md and CLAUDE.md. Still no app code.

> **Narration:** "This is the difference from vibe coding — I wrote the *brain* first. Every line of code from here is accountable to these two files."

### What a great generated CLAUDE.md looks like (Phase B payoff — slides 18/22/24)
The plan-mode-first run produced a **senior-engineer-grade** memory file — point these out on screen:
- **Stack table with rationale** + a **Scope Discipline** section listing everything deferred to v2 (no chat, no uploads, no public Trips in Explore) so future work can't creep back in.
- **Judgment nobody typed**, e.g.:
  - `bcryptjs` not native `bcrypt` — "native bcrypt risks build failures on Vercel serverless."
  - Vercel Postgres **two-connection-string** gotcha (`POSTGRES_PRISMA_URL` runtime, `POSTGRES_URL_NON_POOLING` migrations).
  - `notFound()` not `403` for private resources — a **security** call so resources don't leak their existence.
  - `Match` must check **both directions** before creating a request; `TripCollaborator` is the single source of truth for authz.

> **Narration:** "I didn't tell it to use bcryptjs, or return 404 instead of 403 to avoid leaking data. It baked senior-engineer judgment into the project's brain — so every future edit and every teammate inherits it. The first time I built this, the brain was empty. This time it's smarter than most onboarding docs."

---

## PHASE C — Build FROM the Memory

**Prompt 2:**
> Now read CLAUDE.md and spec.md and scaffold + build the full app: all four module routes, NextAuth email/password, the Prisma schema on Postgres, seed data, and a responsive landing page with a light-blue palette. Follow the conventions in CLAUDE.md exactly.

- Review the plan → **approve** (the plan review *is* your human checkpoint).
- Choose **auto mode** so it builds the whole skeleton (slide 26–27 "watch what happens").
- If it asks to use the Chrome browser skill to self-test → **"Not now"** for a safe first run (you'll demo the UI yourself). Note the behavior out loud: "It wanted to test its own work in a real browser — that's self-verification."

### Things it does autonomously — narrate them (slides 30–32)
- **Self-heals around environment blockers** (e.g. picked the libsql/Neon driver when a native toolchain was missing).
- **Finds & fixes its own bugs** (e.g. split an edge-safe `auth.config.ts` from `auth.ts` for a Node-vs-Edge runtime conflict).
- **Verifies for real** — logs in via the actual auth flow, hits every page, tests create-trip/create-story end to end.
- **Is honest about what's NOT done** — no tests, no uploads, no OAuth.

### CLAUDE.md is already a real brain (plan-mode-first advantage)
Unlike the "build-first" approach — where `CLAUDE.md` came out thin (just `@AGENTS.md` / Next.js rules) — doing the **spec/CLAUDE.md first** produces a rich memory file up front. Just confirm on screen that the build followed it. If you ever find it thin, regenerate:
> Update CLAUDE.md into full persistent project memory: stack decisions and rationale, folder conventions, the full data model with all entities and relationships, module scope for Planning/Matching/Stories/Explore, coding standards, and a Scope Discipline list of v2-deferred items.

> **Narration:** "Repo memory is the project's brain — it survives across sessions and teammates. Empty brain → full brain, in one prompt."

### Drift control — Claude can self-sync the memory (great live beat)
In testing, when Next 16 renamed `middleware.ts` → `proxy.ts`, Claude **updated the code AND updated `CLAUDE.md` to match** — on its own. Use this to answer the common question "does it keep the docs in sync?":
> **Narration:** "It won't *systematically* police drift, but watch — when the framework renamed a convention mid-build, it fixed the code *and* the memory file so they didn't diverge. Drift is still your discipline to own, but the tool helps."

To force a re-sync anytime:
> Review the code against spec.md and CLAUDE.md. If anything drifted, update the docs to match reality and list what changed.

---

## PHASE D — Demo the App (Build + Polish sections)

### ⚠️ FIRST: seed demo data (or the app is empty!)
The generated `seed.ts` only seeds the **15 Interest lookup rows** — there are **no demo users/trips/stories** by default (and verification test rows get deleted). Without this step your click-through is all empty states and **you can't even log in.** Run once before rehearsing:
> Add rich demo seed data: 3–4 sample users with a shared known password (`password123`), each with a travel profile + interests; two collaborative trips with day-grouped itinerary items and votes; a couple of accepted and pending connection requests; and several published stories that appear on Explore. Keep the 15 interests. Then run the seed and print the login emails.

```powershell
npm run dev
```
Open **localhost:3000** (in testing it fell back to **3001** because 3000 was taken — free up 3000 before the session, or just use whatever port it prints). Click-path (routes match the generated spec):
1. **Landing page** (`/`) — "Idea → this UI, zero boilerplate."
2. **Register / Login** — sign in with a seeded account (`password123`, emails from the seed output). "Real NextAuth v4, hashed passwords with bcryptjs."
3. **Trips** (`/trips` → `/trips/[tripId]`) — itinerary grouped by day + **up/down voting** + collaborators. "Collaborative, from the TripCollaborator + ItemVote model it designed."
4. **Matches** (`/matches`) — filter travellers by destination/date/interest → view profile → send connection request → `/matches/requests` accept. **No chat — deliberately cut in v1.**
5. **Stories** (`/stories`) — view portfolio → `/stories/new` create a story (markdown + photo URLs).
6. **Explore** (`/explore`) — public feed of published stories (unauthenticated).
7. **Log out → visit `/trips`** → the auth guard (`proxy.ts`, formerly `middleware.ts` in Next 16) **bounces to `/login`**. "A security guard it wrote, working live."

### One live Polish prompt (slide 33)
> The hero section spacing feels cramped — fix it to match the spec's light-blue design.

---

## PHASE E — Deploy to Vercel (working + persistent)

> **Note:** the generated spec pins **two** DB env vars (not `DATABASE_URL`):
> - `POSTGRES_PRISMA_URL` — pooled, used at runtime
> - `POSTGRES_URL_NON_POOLING` — direct, used for `prisma migrate`
> Vercel Postgres injects both automatically once you link the DB to the project.

### E1. Create + link the DB, pull env vars locally
1. Vercel → project → **Storage → Create Database → Postgres** (Neon-backed).
2. Pull the injected vars into a local `.env`:
   ```powershell
   vercel link          # link this folder to the Vercel project
   vercel env pull .env # writes POSTGRES_PRISMA_URL + POSTGRES_URL_NON_POOLING
   ```
3. Run the migration + seed against the hosted DB:
   > Run `prisma migrate deploy` against the Postgres database and seed it.

### E2. Real NEXTAUTH_SECRET + init git, then push (via Claude)
The build leaves `NEXTAUTH_SECRET` as a placeholder and the folder is **not a git repo yet**. Generate a real secret (Windows-friendly):
```powershell
node -e "console.log(require('crypto').randomBytes(32).toString('base64'))"
```
Put it in `.env`, then:
> Set NEXTAUTH_SECRET in .env to <value>. Initialize a git repo with a sensible .gitignore (exclude .env), commit everything with a meaningful message, create a public GitHub repo named WanderTogether, and push to main.

### E3. Deploy
1. vercel.com → **Add New → Project** → import `WanderTogether` (auto-detects Next.js).
2. The Postgres vars are already present (from linking the DB). Also add under **Settings → Environment Variables**:
   - `NEXTAUTH_SECRET` — generate: `openssl rand -base64 32`
   - `NEXTAUTH_URL` — your `https://<app>.vercel.app` URL
3. **Deploy** → live `.vercel.app` URL in ~90s.
4. **Open it on your phone.**

> **Close (slide 47):** "The spec was the blueprint. Claude was the builder. You were the architect."

### Deploy gotchas (or the live deploy fails)
- **`prisma migrate` needs `POSTGRES_URL_NON_POOLING`** (the direct connection). Migrating against the pooled URL alone fails — the spec/CLAUDE.md already configured `directUrl` for this.
- `NEXTAUTH_SECRET` and `NEXTAUTH_URL` **must** be set in Vercel env vars before deploy, or auth breaks in prod.
- Run the **migration against the hosted DB** (E1) before deploy, or pages load but DB queries error.

---

## Timing (≈60 min live)
| Phase | Time | Notes |
|---|---|---|
| A — Fresh start | 2 min | |
| B — Spec/CLAUDE.md + wizard | 12 min | The interactive, high-energy part — do it LIVE |
| C — Build | 20–30 min | Do NOT watch live — cut to slides or pre-built app |
| D — Demo app + polish | 12 min | |
| E — Deploy | 10 min | Pre-create the DB to save time |

---

## The Through-Line (use in your close)
Every wizard step was a **decision**, not a keystroke. You overrode the AI when your constraints differed, and accepted it when they matched. You cut scope in the spec before it became code. **That** is spec-driven development: the spec is the source of truth, the AI is the builder, and the engineer is the architect.
