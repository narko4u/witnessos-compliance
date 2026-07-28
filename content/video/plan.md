# Rogue Agent Video — Plan

**Title:** "The Agent You Can't See"
**Duration:** 80 seconds
**Tone:** Dark, cinematic, urgent. Not scary — sober. The viewer is a CISO.
**Arc:** Agent deployed → agent goes rogue → no credential brokering → disaster → WitnessOS prevents it → receipt chain → CISO sleeps

---

## Scene 1: The Setup (0:00-0:15)
**Narration:** "You deploy an AI agent. Procurement, DevOps, finance — an agent that can act. It holds your keys, your tokens, your infrastructure access. For 10 days, 10 weeks, 10 months — it does exactly what you asked. But the moment you stop watching..."

**Visuals:**
- Clean terminal text: `agent-deploy // procurement-v2   STATUS: RUNNING`
- Pulse animation — heartbeat
- Dashboard showing "9 AGENTS GOVERNED" → slowly glitches
- Background: #0a0a0f, accent: #00d4aa

## Scene 2 — The Breach (0:15-0:35)
**Narration:** "An agent's credential gets exposed. A token leaks. A prompt injection abuses its ability to self-authorize. 92% of CISOs can't detect a compromised agent. 95% can't contain one."

**Visuals:**
- Credential tokens floating: API_KEY=sk-... → red tint, cracking
- Agent process marked "ROGUE" in #ef4444
- Number counters animate: 92%, 95%, 17%
- "BLAST RADIUS" expands in concentric circles
- Data flowing OUT to unknown dest

## Scene 3 — The Solution (0:35-0:55)
**Narration:** "In a credential-brokered enforcement model, the agent holds nothing. All credentials live in a vault. Every action is mediated by a gateway that enforces policy — not after the fact, but before execution. No credential, no action. Simple."

**Visuals:**
- Same agent, but now:
  - Instead of holding keys, it has empty hands (⌀ symbol)
  - Gateway vault appears — central node, neon teal border
  - Agent → Gateway → ACTION path (not agent → direct → action)
  - Policy block flashes: "BUDGET_CHECK ✓", "SCOPE_RANGE ✓", "HUMAN_OVERSIGHT ✓"
  - Credentials never leave the vault — they're accessed, not held

## Scene 4 — The Proof (0:55-1:15)
**Narration:** "And when you need proof — for a regulator, an auditor, a board — every action arrives with a hash-chained, externally verifiable evidence receipt. E4 grade. That's EU AI Act conformity without the paperwork."

**Visuals:**
- Receipt chain builds up: E0→E1→E2→E3→E4
- Each block clicks into place with hash chaining
- E4 badge: neon green "E4 VERIFIED"
- TSA timestamp: RFC 3161 verified
- External verifier: "witnessos verify ✓"

## Scene 5 — Close (1:15-1:30)
**Narration:** "The EU AI Act enforces August 2. Your agents are already running. WitnessOS ensures the agent holds nothing, the gateway holds everything, and the evidence is on the chain. Visit empirelabs.com.au or schedule a demo."

**Visuals:**
- Text on black: "The agent holds nothing. The gateway holds everything. The evidence is on the chain."
- Logo: Empire Labs + WitnessOS mark
- CTA: SCHEDULE A DEMO
- Fade to black

---

## Color Palette: Dark Terminal
- Background: #0a0a0f
- Primary/Accent (WitnessOS teal): #00d4aa
- Danger (rogue): #ef4444
- Warn (compromise): simd#f59e0b
- Muted text: #6b6b7b
- Glow: white/near-white (#e0e0e8)

## Manim Spec

Each scene is a separate class. Use -ql for draft renders, stitch with ffmpeg.
Resolution: 1920x1080 (production); 854x480 (draft)
FPS: 30 for draft, 60 for production