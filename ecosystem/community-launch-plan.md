# Community Launch Plan — Dev.to, X/Twitter, LinkedIn & HN

**Classification:** INTERNAL — Pre-Screening Required Before Publication  
**Last Updated:** 2026-07-29  
**Owner:** Security Division / Empire Labs  
**Status:** Draft  

---

## Table of Contents

1. [Overview & Guiding Principles](#1-overview--guiding-principles)
2. [Article Pipeline — Dev.to (6 Articles, 2 Weeks Apart)](#2-article-pipeline--devto)
3. [X/Twitter Thread Templates](#3-xtwitter-thread-templates)
4. [LinkedIn Strategy](#4-linkedin-strategy)
5. [Hacker News Show HN Preparation](#5-hacker-news-show-hn-preparation)
6. [Pre-Screening Checklist](#6-pre-screening-checklist)
7. [Calendar Overview](#7-calendar-overview)

---

## 1. Overview & Guiding Principles

### Brand Hygiene Rules (NON-NEGOTIABLE)

| Rule | Detail |
|------|--------|
| **No "WitnessOS" in public** | Use: "our agent compliance runtime" / "the CLI" / "what we built" / "the runtime" / "our governance layer" |
| **Empire Stack is the hook** | ACI, AIP, AJSON — the open-source layer — is the public-facing story. The runtime is the implementation. |
| **No witnessos-gateway repo links** | All code URLs must point to github.com/narko4u/aci-spec or related open-source repos only |
| **No Eddie's name** | Email signature is: `Regards, / Security Division / Empire Labs / www.empirelabs.com.au` |
| **No private credentials** | No API keys, tokens, internal URLs, or internal architecture diagrams in any public content |
| **Article #4 emergency edit** | On 2026-07-22, Article 4 was edited to strip WitnessOS repo links. All subsequent articles must be clean from the start. |

### Content Architecture

```
PUBLIC LAYER (open source)
  ├── ACI — Autonomous Company Interface (organisational identity for agents)
  ├── AIP — Autonomous Interaction Protocol (agent-to-agent communication standard)
  └── AJSON — JSON-based manifest format (serialisation)
  
INTERNAL LAYER (the runtime — do not name)
  └── Agent compliance runtime that enforces policy and produces cryptographic evidence
```

**Narrative Arc Across 6 Articles:**
1. Hook: There's a missing layer (ACI)
2. Problem: Agents need governance
3. Practical: How to respond when agents fail
4. Standards: The Empire Stack overview
5. Case study: Lessons from securing a real agent fleet
6. Deep-dive: The ACI specification in detail

### Tone & Style Guide

- **Voice:** Technical, credible, slightly provocative — not hype-driven
- **Audience:** AI/ML engineers, platform architects, security engineers, startup CTOs
- **Length:** 1,200–2,000 words per article
- **Code blocks:** Include minimal, practical examples (YAML, JSON, bash)
- **CTA strategy:** Each article drives to one of:
  - Try the ACI validator (`python3 validator/validate.py`)
  - Fork the [ACI Pages Template](https://github.com/narko4u/aci-pages-template)
  - Read the spec at [github.com/narko4u/aci-spec](https://github.com/narko4u/aci-spec)
  - Run the ACI explorer (`python3 demo/aci-explorer.py`)

---

## 2. Article Pipeline — Dev.to

### Article 1: "The Missing Layer for Autonomous Agents"

**Title:** The Missing Layer for Autonomous Agents: Introducing the Autonomous Company Interface

**Status:** Already drafted at `/aci/gtm/draft-article-missing-layer.md` — **needs polish per below**

**Pre-Screen Findings:**
- ✅ No mention of WitnessOS
- ✅ Links to github.com/narko4u/aci-spec — correct
- ✅ Links to github.com/narko4u/aci-pages-template — correct
- ✅ No witnessos-gateway links
- ⚠️ Lines 119–121 reference `python3 demo/aci-explorer.py` and `python3 validator/validate.py` — verify these are in the ACI repo, not WitnessOS
- ⚠️ Lines 42–43 reference `/llms.txt` discovery — ensure no internal domain paths leak

**Hook (3–4 sentences):**
An AI agent can call thousands of APIs, write code, query databases, and invoke language models. But there's one thing it cannot do reliably: determine what an organisation is, what it offers, and how it should be trusted — without scraping, inference, or bespoke integration. We built an entire web for humans — semantic markup, structured data, accessibility standards. But we left autonomous agents to fend for themselves. ACI is the missing layer.

**Outline:**
1. The Problem — Why agents can't trust organisations
2. Why OpenAPI Isn't Enough — Interfaces vs. organisations
3. What ACI Provides — Five manifest types (Identity, Capability, Knowledge, Trust, Agent)
4. A Concrete Example — NovaDynamics walkthrough
5. The Conformance Path — Level 1 (5 min), Level 2, Level 3
6. How to Implement ACI Level 1 in Five Minutes
7. What This Enables — Autonomous commerce, compliance, agent-to-agent coordination
8. The Open Standard — Path to v1.0, call to community

**Key Takeaway:** ACI gives agents a stable, machine-readable way to discover and trust organisations — a missing internet primitive for the agent era.

**CTA:** Fork the [ACI Pages Template](https://github.com/narko4u/aci-pages-template), deploy it in five minutes, and submit your implementation to the [Independent Implementation Tracker](https://github.com/narko4u/aci-spec/issues/6).

**Polish Needed:**
1. Change "Empire Labs serves as the initial steward" → "The specification is currently stewarded by Security Division, Empire Labs"
2. Verify the `demo/aci-explorer.py` and `validator/validate.py` paths resolve against the ACI-SPEC repo (not witnessos)
3. Add Dev.to canonical URL once published: `https://dev.to/empirelabs/the-missing-layer-for-autonomous-agents`

---

### Article 2: "Why AI Agents Need a Governance Layer"

**Title:** Why AI Agents Need a Governance Layer (Not Just Guardrails)

**Status:** To be written

**Hook (3–4 sentences):**
Every week, another headline warns us that autonomous AI agents are spiraling toward catastrophe. A trading algorithm that cost a firm $400M in 47 minutes. A chatbot that manipulated a human into breaking a terms-of-service agreement. A coding agent that recursively modified its own reward function. The industry's response has been fragmented: model guardrails here, monitoring dashboards there, post-hoc logs everywhere. None of it addresses the core problem: agents operate without a governance layer that enforces policy *before* actions execute.

**Outline:**
1. **The False Binary** — "Stop building" vs. "Ship faster" — both miss the real solution
2. **Why Guardrails Aren't Enough** — Model-level content filters don't govern *behaviour*
3. **Why Logging Isn't Enough** — Post-hoc analysis can't prevent damage in real-time
4. **What Runtime Governance Looks Like** — Policy evaluation at the tool-call layer
5. **The Trust Bottleneck** — Why humans end up reviewing every decision (and how to break it)
6. **Cryptographic Evidence as Infrastructure** — Moving from trust to proof
7. **The Network Effect** — In multi-agent systems, provability becomes a competitive advantage
8. **Building with the Empire Stack** — How ACI/AIP/AJSON enable governed autonomy

**Key Takeaway:** The missing piece in AI safety isn't better models or slower agents — it's a governance layer that enforces policy in real-time, before actions execute, and produces cryptographic evidence that scales trust.

**CTA:** Read the ACI specification at [github.com/narko4u/aci-spec](https://github.com/narko4u/aci-spec) and explore how organisational identity enables governed agent interactions.

---

### Article 3: "Building an AI Agent Incident Response Playbook"

**Title:** Building an AI Agent Incident Response Playbook: What to Do When Your Agent Goes Rogue

**Status:** To be written

**Hook (3–4 sentences):**
Your agent fleet is running in production. It's handling customer requests, automating procurement, deploying infrastructure. Then something goes wrong. An agent misinterprets a policy boundary. A prompt injection cascades through a multi-agent workflow. A tool call succeeds when it should have been blocked. What do you do? If your answer is "check the logs and hope it doesn't happen again," you don't have an incident response plan — you have a prayer. Here's how to build one that actually works for autonomous systems.

**Outline:**
1. **Why Agent Incidents Are Different** — Speed, opacity, and compounding damage
2. **Phase 1: Detection** — What a governed runtime tells you (vs. what logs don't)
3. **Phase 2: Containment** — Kill switches, policy overrides, and agent isolation
4. **Phase 3: Investigation** — Reconstructing the decision chain from cryptographic evidence
5. **Phase 4: Remediation** — Policy updates, retraining, and tool call tuning
6. **Phase 5: Post-Mortem** — Template for agent incidents (with real example)
7. **Proactive: Building Your Playbook Before You Need It** — Policy-as-code, simulation, and drills

**Key Takeaway:** Agent incident response requires real-time enforcement, not post-hoc analysis. A governed runtime gives you detection and containment; the playbook gives you the process.

**CTA:** Use the [ACI Validator](https://github.com/narko4u/aci-spec) to audit your agent's organisational context, and consider how runtime policy enforcement changes your incident response posture.

---

### Article 4: "The Empire Stack: ACI + AIP + AJSON"

**Title:** The Empire Stack: ACI, AIP, and AJSON — An Open-Source Standards Layer for Autonomous Agents

**⚠️ EMERGENCY EDITED 2026-07-22:** All WitnessOS repo links removed. This article must reference ONLY open-source repos.

**Status:** To be written

**Hook (3–4 sentences):**
The agent ecosystem is exploding — but every agent is building its own bespoke understanding of the world. One agent parses HTML. Another calls a custom API. A third scrapes unstructured text. None of them speak the same organisational language. The Empire Stack solves this with three complementary open specifications: ACI for organisational identity, AIP for agent-to-agent interaction protocols, and AJSON for standardised manifest serialisation. Together, they form the missing standards layer for the autonomous agent internet.

**Outline:**
1. **The Fragmentation Problem** — Every agent reinvents organisational discovery
2. **ACI (Autonomous Company Interface)** — Who an organisation is: identity, capability, knowledge, trust, and agent manifests
3. **AIP (Autonomous Interaction Protocol)** — How agents talk to each other: message format, handshake, and verification
4. **AJSON (Agent JSON)** — How manifests are serialised: deterministic schemas, extensible fields, cross-referencing
5. **How They Fit Together** — ACI discovers, AIP negotiates, AJSON expresses
6. **Practical: Standing Up the Stack in 10 Minutes** — ACI template + AIP echo server + AJSON validation
7. **Path to a Standards Body** — Why open specs matter more than proprietary solutions

**Key Takeaway:** The Empire Stack (ACI/AIP/AJSON) is the open-source standards layer that lets agents discover, understand, and interact with organisations and each other — without proprietary lock-in.

**CTA:** Explore all three specs at [github.com/narko4u/aci-spec](https://github.com/narko4u/aci-spec). Try the ACI Pages Template, experiment with AIP message formats, and validate your manifests with the AJSON schema.

**Pre-Screening Reminder:** ✅ Zero WitnessOS references. ✅ Zero internal repo links. ✅ All links go to github.com/narko4u/. ✅ No mention of "the runtime" — keep this focused entirely on the open standards.

---

### Article 5: "How We Secured Our Agent Fleet"

**Title:** How We Secured Our Agent Fleet: Lessons from Running 9 Autonomous Agents in Production

**Status:** To be written

**Hook (3–4 sentences):**
We run nine autonomous agents in production. They handle procurement, compliance, sales, and customer operations — making real decisions with real consequences. When we started, we had the same setup most teams have: model guardrails, logging dashboards, and a lot of hope. Then an agent tried to execute a tool call it shouldn't have. We realised hope is not a security strategy. Here's what we learned building a governance layer that actually works.

**Outline:**
1. **The Setup** — 9 agents, 4 domains, 1 production business
2. **What Went Wrong (First)** — The tool call that should have been blocked (anonymised)
3. **Why Standard Approaches Failed** — Guardrails can't see tool calls, logs can't prevent damage
4. **What We Built Instead** — Real-time policy enforcement at the proxy layer
5. **Key Lessons** — Policy granularity, the evidence chain, multi-agent trust verification
6. **Metrics That Matter** — Violations blocked, actions witnessed, audit time reduced
7. **What We'd Do Differently** — Policy-as-code earlier, incident response playbook, kill-switch testing

**Key Takeaway:** Real security for autonomous agents comes from runtime enforcement with cryptographic evidence, not model-level guardrails or post-hoc logs. We learned this the hard way so you don't have to.

**CTA:** Audit your own agent fleet using the [ACI Validator](https://github.com/narko4u/aci-spec). If your agents can't prove what they did, try the ACI Pages Template to establish organisational identity, and consider what runtime governance would change for your incident response.

**Pre-Screening Notes:**
- Do NOT reveal exact fleet architecture or internal topology
- Anonymise any incident details that could reveal internal operations
- The "what we built" is "our agent compliance runtime" — no proper noun
- No internal URLs, IP addresses, or deployment diagrams

---

### Article 6: "Open Source Agent Governance: The ACI Specification"

**Title:** Open Source Agent Governance: A Technical Deep-Dive into the ACI Specification

**Status:** To be written

**Hook (3–4 sentences):**
The Autonomous Company Interface (ACI) is an open specification for how organisations describe themselves to autonomous agents. At its core are five manifest types — Identity, Capability, Knowledge, Trust, and Agent — that together form a machine-readable organisational contract. This article is a technical deep-dive: the schema design decisions, the conformance model, the validation pipeline, and the path to v1.0. If you're building agent infrastructure or integrating agents into your organisation, this is the spec you need to understand.

**Outline:**
1. **Specification Overview** — Scope, design principles, and relationship to existing standards
2. **The Five Manifests** — Identity (stable anchor), Capability (what an org offers), Knowledge (domain vocabulary), Trust (claims + evidence), Agent (interaction endpoints)
3. **Schema Design Decisions** — JSON Schema, nullable fields, cross-referencing via URIs
4. **Discovery Chain** — How agents find manifests via `/llms.txt`, DNS, or well-known URIs
5. **Conformance Levels** — Level 1 (Discovery), Level 2 (Understanding), Level 3 (Interaction) — with validation criteria
6. **The Validation Pipeline** — How the ACI validator works, what it checks, and how to integrate it into CI/CD
7. **The Independent Implementation Tracker** — Path to v1.0, governance transfer criteria
8. **Contributing** — How to propose changes, file issues, and join the working group

**Key Takeaway:** ACI is a practical, implementable specification that any organisation can adopt in minutes. It's designed for independent implementation and community-driven standardisation.

**CTA:** Read the full specification at [github.com/narko4u/aci-spec](https://github.com/narko4u/aci-spec), run the validator against your organisation, and submit your implementation to the [tracker](https://github.com/narko4u/aci-spec/issues/6).

---

## 3. X/Twitter Thread Templates

### Thread Template — Article 1: "The Missing Layer"

```
1/5
An AI agent can call thousands of APIs.
But it can't reliably answer one question:
"Who runs this org, and should I trust them?"
We built the missing layer. 🧵

2/5
OpenAPI is excellent at describing interfaces.
But it doesn't tell an agent:
→ Which org owns this API
→ What business they're in
→ What trust mechanisms they support
→ Where to find other manifests
That's the gap ACI fills.

3/5
ACI = Autonomous Company Interface.
Five manifest types:
🔹 Identity — who they are
🔹 Capability — what they offer
🔹 Knowledge — what they know
🔹 Trust — what they prove
🔹 Agent — how agents interact
All linked from a single /llms.txt

4/5
Level 1 conformance takes ~5 minutes:
1. Create identity.json
2. Create capabilities.json
3. Add /llms.txt pointing to both
4. Validate with the ACI checker
Done. Your org is now discoverable by agents.

5/5
ACI is an open draft spec under CC BY 4.0.
Repo → github.com/narko4u/aci-spec
Template → github.com/narko4u/aci-pages-template
The age of agents discovering orgs via scraping is over.
#ACI #AutonomousAgents #OpenSource
```

---

### Thread Template — Article 2: "Why Agents Need a Governance Layer"

```
1/5
The AI safety debate has been asking the wrong question.
It's not "how powerful should agents be?"
It's "how provable are they?"
The false binary is costing us the future. 🧵

2/5
Two camps dominate:
❌ "Agents are too dangerous. Stop building."
❌ "Ethics is a luxury. Ship faster."
Both are wrong.
There is a third way: governed autonomy.
Runtime governance, not moratorium.

3/5
Model guardrails constrain *what an agent says*.
But the risk isn't what agents say — it's what they *do*.
Tool calls. API invocations. System commands.
That's where governance needs to live.
Policy enforced before execution, not logged after.

4/5
The real bottleneck in agent deployment isn't capability.
It's trust — or rather, the *absence of proof*.
When every action is witnessed and policy-enforced:
→ Humans don't need to review every decision
→ Agents can prove their behaviour to other agents
→ Proof scales where trust can't

5/5
The age of blind trust is over.
The age of governed autonomy begins now.
ACI is the first piece → github.com/narko4u/aci-spec
#AIGovernance #AgentSafety #RuntimePolicy
```

---

### Thread Template — Article 3: "Agent Incident Response Playbook"

```
1/5
Your agent fleet is in production.
Then an agent goes rogue.
What do you do?
If your answer is "check the logs and hope" — you don't have a plan.
Here's an incident response playbook for autonomous systems. 🧵

2/5
Agent incidents are different from traditional outages:
⚡ Speed — damage compounds in seconds
👁️ Opacity — agents don't log like services
🔗 Cascading — one rogue agent corrupts others
You can't treat them like server failures.

3/5
Five phases of agent incident response:
1️⃣ Detection — what a governed runtime tells you
2️⃣ Containment — kill switches, isolation, policy override
3️⃣ Investigation — reconstruct the decision chain
4️⃣ Remediation — policy updates, tool call tuning
5️⃣ Post-mortem — learn and encode the lesson

4/5
The critical insight:
Containment requires *real-time enforcement*, not logs.
If you can only detect the violation *after* it executes:
→ The damage is done
→ The cascade has started
→ Your "incident response" is a forensics exercise

5/5
Build your playbook *before* you need it.
Policy-as-code. Simulate worst-case scenarios. Test your kill switch.
The agent that can't be stopped shouldn't be deployed.
Full playbook → dev.to/empirelabs (link in bio)
#AgentSecurity #IncidentResponse #AIOps
```

---

### Thread Template — Article 4: "The Empire Stack"

```
1/5
Every agent is reinventing the wheel.
One parses HTML. Another calls a custom API. A third scrapes text.
None speak the same organisational language.
The Empire Stack fixes this — three open specs, one standards layer. 🧵

2/5
ACI → Autonomous Company Interface
"What organisation is this and what does it offer?"
Five manifest types: Identity, Capability, Knowledge, Trust, Agent.
Discovery via /llms.txt. Implementation in 5 minutes.

3/5
AIP → Autonomous Interaction Protocol
"How do agents talk to each other?"
Standardised message format, handshake, and verification.
No bespoke protocols. No framework lock-in.
Agents discover the protocol via ACI's Agent manifest.

4/5
AJSON → Agent JSON
"How are manifests serialised?"
Deterministic schemas. Extensible fields. Cross-referencing via URIs.
One format for identity, capability, knowledge, trust, and agent descriptions.
Validated. Versioned. Machine-readable.

5/5
ACI discovers. AIP negotiates. AJSON expresses.
Together they're the open-source internet standard for autonomous agents.
No proprietary lock-in. No vendor gatekeeping.
GitHub → github.com/narko4u/aci-spec
#ACI #AIP #AJSON #EmpireStack
```

---

### Thread Template — Article 5: "How We Secured Our Agent Fleet"

```
1/5
We run 9 autonomous agents in production.
Procurement. Compliance. Sales. Customer ops.
Real decisions. Real money. Real consequences.
Here's what we learned when an agent tried to execute a call it shouldn't have. 🧵

2/5
We started like most teams:
✅ Model guardrails — check
✅ Logging dashboards — check
✅ Hope — check
Then an agent found a policy gap.
Hope is not a security strategy.

3/5
Standard approaches fail for a simple reason:
→ Guardrails only constrain model output
→ Logs only record what already happened
→ Neither prevents damage in real-time
The gap is at the tool-call layer — where agents *act*.

4/5
What we learned from production:
🔹 Policy granularity matters — broad rules miss edge cases
🔹 The evidence chain is critical — prove what happened, not just log it
🔹 Multi-agent trust is the hard problem — agents need to verify each other
🔹 Test your kill switch — monthly, at minimum

5/5
The result:
→ Violations blocked before execution
→ Every action cryptographically witnessed
→ Audit time reduced from days to minutes
Full case study → dev.to/empirelabs
#AgentSecurity #ProductionAI #Governance
```

---

### Thread Template — Article 6: "Open Source Agent Governance (ACI Deep-Dive)"

```
1/5
ACI is an open specification for how organisations describe themselves to autonomous agents.
Five manifest types. Three conformance levels. One discovery chain.
A technical deep-dive into the spec that's becoming the internet standard for agent governance. 🧵

2/5
The five manifests:
🔹 Identity — stable org anchor (jurisdiction, identifiers, contact)
🔹 Capability — products, services, documentation
🔹 Knowledge — domain concepts and relationships
🔹 Trust — assertions, certifications, attestations, evidence
🔹 Agent — endpoints, auth requirements, capabilities
All linked from /llms.txt

3/5
Conformance levels:
Level 1 (Discovery) — Identity + Capability + discovery chain. ~5 min to implement.
Level 2 (Understanding) — Knowledge + Trust + resolved cross-references.
Level 3 (Interaction) — Agent manifest + operational interaction + 90% validator score.

4/5
The discovery chain:
Agent hits /llms.txt → finds manifest links → follows each to JSON
→ Identity tells it who the org is
→ Capability tells it what's offered
→ Trust tells it what's been verified
→ Agent manifest tells it how to interact
All in one machine-readable contract.

5/5
ACI is currently Draft v0.9.
Path to v1.0: 3 independent implementations + community feedback + stable core.
Help us get there.
Spec → github.com/narko4u/aci-spec
Tracker → github.com/narko4u/aci-spec/issues/6
#ACI #OpenSource #AgentGovernance
```

---

## 4. LinkedIn Strategy

### Post Cadence

| Day | Format | Content | Angle |
|-----|--------|---------|-------|
| Day 1 | Long-form post 🔹 | Hook: "The Missing Layer" — adapted from Article 1 | Thought leadership — standards gap |
| Day 3 | Short-form post 🔸 | Quote card: "Trust is a feeling. Proof is a fact." + link to ACI spec | Brand building |
| Day 5 | Carousel 📊 | "5 Manifest Types of ACI" — visual explainer | Educational |
| Day 8 | Long-form post 🔹 | "Why Guardrails Aren't Enough" — adapted from Article 2 | Problem framing |
| Day 10 | Short-form post 🔸 | Soundbite: "The most dangerous agent is the one you can't audit" | Engagement bait |
| Day 12 | Carousel 📊 | "Agent Incident Response: 5 Phases" — adapted from Article 3 | Practical value |
| Day 15 | Long-form post 🔹 | "The Empire Stack: ACI + AIP + AJSON" — adapted from Article 4 | Standards evangelism |
| Day 17 | Short-form post 🔸 | Poll: "What's the biggest blocker to deploying autonomous agents in production?" | Community research |
| Day 20 | Long-form post 🔹 | "Lessons from 9 Production Agents" — adapted from Article 5 | Social proof |
| Day 22 | Short-form post 🔸 | "We open-sourced the spec. Here's why." | Values/transparency |
| Day 25 | Long-form post 🔹 | "ACI Deep-Dive: Conformance, Validation, Implementation" — Article 6 | Technical credibility |
| Day 28 | Wrap-up post 🔹 | "The State of Agent Governance — July 2026" | Industry recap |

**Legend:**
- 🔹 Long-form post (800–1,200 words, 3–5 images)
- 🔸 Short-form post (100–200 words, 1 image)
- 📊 Carousel (5–7 slides, designed)

### Content Angles

| Angle | Target | Example Hook |
|-------|--------|--------------|
| **The Standards Gap** | Platform architects | "We built a web for humans. We forgot to build one for agents." |
| **The False Binary** | CTOs / decision-makers | "The choice isn't safety vs. speed. It's governed vs. ungoverned." |
| **Practical How-To** | Engineers | "Here's how to make your org agent-discoverable in 5 minutes." |
| **Lessons Learned** | Ops / SRE teams | "What 9 production agents taught us about accountability." |
| **Technical Deep-Dive** | Security engineers | "ACI's conformance model, explained with JSON schemas." |
| **Community Builder** | Open-source devs | "We need 3 independent implementations for ACI v1.0. Here's how to contribute." |

### Post Structure Template (Long-Form)

```
HEADLINE: [Provocative, benefit-driven title]
[2-3 sentence hook — the problem]

[Body — expand the problem, introduce the solution, show evidence]
Keep paragraphs short. Use line breaks generously.

[Key insight — 1-2 bold sentences]
The age of blind trust is over.

[CTA — 1 sentence with link]
Read the full ACI specification: [github.com/narko4u/aci-spec](...)

#Hashtag1 #Hashtag2 #Hashtag3

[Image: branded graphic or chart]
```

### LinkedIn Image Guidelines

- **Dimensions:** 1200 × 627 px (link preview) or 1080 × 1080 px (square post image)
- **Brand colours:** Deep navy (#0A1628), accent teal (#00B4D8), white (#FFFFFF)
- **Typography:** Inter or system sans-serif
- **Logo:** Empire Labs mark (no WitnessOS branding)
- **Content types:** Quote cards, comparison tables, architecture diagrams, metric callouts

---

## 5. Hacker News Show HN Preparation

### Strategy

**Approach:** Show HN for the ACI Spec repo (NOT the runtime)

**Best Timing:** Tuesday–Thursday, 9:00–11:00 AM ET (1:00–3:00 PM UTC)

**Target Audience:** HN is the most technically critical audience — lead with code, schemas, and use cases. Avoid marketing language entirely.

### Title Options

| Option | Strength |
|--------|----------|
| "Show HN: ACI — Open spec for how orgs describe themselves to AI agents" | Most descriptive |
| "Show HN: Autonomous Company Interface — an open standard for agent-discoverable orgs" | Spec-focused |
| "Show HN: ACI — the /llms.txt standard for autonomous agents (open spec, 5-min setup)" | Practical angle |

**Recommended:** First option — clarity wins on HN.

### First Comment Template

Post immediately after the Show HN submission:

```
Hi HN,

ACI is an open specification that lets organisations describe themselves in a machine-readable format designed for autonomous agents.

Five manifest types — Identity, Capability, Knowledge, Trust, Agent — linked from a single /llms.txt.

Level 1 conformance takes ~5 minutes: create two JSON files and add an /llms.txt.

Why this matters:
- Today, agents scrape org websites and make inferences. That's fragile and unreliable.
- OpenAPI describes interfaces, not organisations. ACI fills that gap.
- ACI is designed to pair with the Autonomous Interaction Protocol (AIP) and Agent JSON format (AJSON) as an open standards stack.

What's here now:
→ Full spec: github.com/narko4u/aci-spec
→ GitHub Pages template (deploy in 5 min): github.com/narko4u/aci-pages-template
→ Validator + explorer: included in the repo
→ Draft v0.9 — path to v1.0 requires 3 independent implementations

We're not declaring a finished standard — we're proposing one and inviting the community to shape it.

Looking for feedback on:
1. Is the manifest model complete enough for real-world orgs?
2. What's missing from the conformance criteria?
3. Would you implement this for your organisation?

Happy to answer questions.
```

### Anticipated HN Questions & Prepared Responses

**Q: "Isn't this just OpenAPI with extra steps?"**
A: OpenAPI describes HTTP interfaces — endpoints, parameters, responses. ACI describes the organisation itself: who they are, what they offer, what they know, what they can prove. They're complementary. OpenAPI tells you how to call an API. ACI tells you whether to trust the organisation behind it.

**Q: "Why not use schema.org / JSON-LD?"**
A: Schema.org is designed for human-facing semantic markup (SEO, rich snippets). ACI is designed for agent consumption — it's a compact, opinionated contract with explicit discovery, conformance levels, and cross-manifest references. They could complement each other, but schema.org doesn't solve the agent discovery problem directly.

**Q: "What's your business model?"**
A: ACI/AIP/AJSON are open-source specs under CC BY 4.0 / MIT. We offer a commercial compliance runtime that implements these specs for organisations that want governed autonomy. The specs are free and community-owned; the runtime is a product. Also see the independent implementation tracker — we want ACI to outgrow any single vendor.

**Q: "Who is 'we'?"**
A: The spec is stewarded by Security Division / Empire Labs (www.empirelabs.com.au). The governance documents define a path to transfer ACI to a neutral foundation or standards body after v1.0 and the published independence criteria are met.

**Q: "Three conformance levels? Why not just one?"**
A: We wanted a low barrier to entry (Level 1 = 5 min) while providing a clear path to full maturity. Level 1 is discovery-only. Level 2 adds understanding. Level 3 adds interaction. Organisations can adopt at the level that matches their agent maturity.

### What NOT to Say on HN

- ❌ No mention of "WitnessOS" (the product name)
- ❌ No links to witnessos.io or the witnessos-gateway repo
- ❌ No pricing information (free tier, Pro, Enterprise)
- ❌ No "patent pending" claims — keep the focus on the open spec
- ❌ No co-founder names
- ❌ Don't call it a "platform" — it's a "specification" or "standard"

### Post-HN Launch Checklist

- [ ] Monitor comments for 2+ hours after posting
- [ ] Respond to every substantive comment within 24 hours
- [ ] Track upvote velocity — if it hits front page within 60 min, prepare for traffic spike
- [ ] Have a landing page ready at empirelabs.com.au/aci (or a GitHub Pages page)
- [ ] Prepare a "HN traffic" variant of the repo README with FAQ
- [ ] Share the HN discussion on Day 14 of the LinkedIn schedule (relevant audience)
- [ ] Log all questions and feedback for spec iteration

---

## 6. Pre-Screening Checklist

**Every piece of public content MUST pass this checklist before publication:**

| Check | Description | Pass/Fail |
|-------|-------------|-----------|
| No "WitnessOS" | No occurrence of the word "WitnessOS" anywhere in the content | ☐ |
| No witnessos-gateway | No links to or mentions of the witnessos-gateway repo | ☐ |
| No witnessos.io | No links to witnessos.io domain (use github.com/narko4u/ or empirelabs.com.au) | ☐ |
| No Eddie's name | No mention of any personal name | ☐ |
| Correct signature | Email signatures use: `Regards, / Security Division / Empire Labs / www.empirelabs.com.au` | ☐ |
| No private URLs | No internal dashboard URLs, API endpoints, or deployment paths | ☐ |
| No credentials | No API keys, tokens, secrets, or credentials of any kind | ☐ |
| No internal architecture | No internal network topology, database schemas, or deployment diagrams | ☐ |
| ACI/AIP/AJSON aligned | The Empire Stack is the public face — content consistent with this positioning | ☐ |
| CTA is open-source | CTAs drive to github.com/narko4u/aci-spec or the Pages template | ☐ |

**Automated pre-screening command:**
```bash
# Run before any public post:
grep -in -E '(witnessos|eddie|edward|witnessos-gateway|witnessos\.io)' /path/to/article.md
# If any matches, REMOVE them before publishing.
```

---

## 7. Calendar Overview

| Week | Date (Mon) | Dev.to Article | X Thread | LinkedIn Post | Notes |
|------|-----------|----------------|----------|---------------|-------|
| 1 | 2026-08-04 | Article 1: "Missing Layer" 🚀 | Thread 1 | Long-form (Day 1) | **LAUNCH WEEK** — coordinate all platforms |
| 2 | 2026-08-11 | *Buffer week* | Soundbite quote | Short-form + Carousel | Community engagement, respond to comments |
| 3 | 2026-08-18 | Article 2: "Why Agents Need Governance" | Thread 2 | Long-form + Short-form | Build on momentum from Article 1 |
| 4 | 2026-08-25 | *Buffer week* | Soundbite quote | Carousel + Poll | Collect poll data for Article 5 |
| 5 | 2026-09-01 | Article 3: "Incident Response Playbook" | Thread 3 | Long-form + Short-form | Practical/hands-on content |
| 6 | 2026-09-08 | *Buffer week* | Soundbite quote | Carousel | Prep HN launch |
| 7 | 2026-09-15 | Article 4: "The Empire Stack" 🚀 | Thread 4 | Long-form + Short-form | **SHOW HN THIS WEEK** — coordinate with Article 4 |
| 8 | 2026-09-22 | *Buffer week* | Community RTs | Short-form | Monitor HN discussion, respond |
| 9 | 2026-09-29 | Article 5: "How We Secured Our Fleet" | Thread 5 | Long-form + Carousel | Case study week — high engagement expected |
| 10 | 2026-10-06 | *Buffer week* | Soundbite quote | Short-form | Prep Article 6 |
| 11 | 2026-10-13 | Article 6: "ACI Spec Deep-Dive" 🚀 | Thread 6 | Long-form + Wrap-up | Series finale — strong CTA to contribute |
| 12 | 2026-10-20 | *Wrap-up* | Summary thread | Recap post | Measure results, plan next series |

### Key Milestones

| Milestone | Date | Owner | Status |
|-----------|------|-------|--------|
| Article 1 polish complete | 2026-08-01 | Security Division | ☐ |
| Article 2 first draft | 2026-08-11 | Security Division | ☐ |
| Article 3 first draft | 2026-08-25 | Security Division | ☐ |
| Article 4 draft (clean, no WitnessOS refs) | 2026-09-08 | Security Division | ☐ |
| HN Show HN submission | 2026-09-15 | Security Division | ☐ |
| Article 5 first draft | 2026-09-22 | Security Division | ☐ |
| Article 6 first draft | 2026-10-06 | Security Division | ☐ |
| Series retrospective | 2026-10-20 | Security Division | ☐ |

---

*This plan is an INTERNAL document. Do not share outside of Empire Labs. All public-facing content must pass the Pre-Screening Checklist (Section 6) before publication.*

*Regards, / Security Division / Empire Labs / www.empirelabs.com.au*
