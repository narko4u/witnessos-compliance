# WitnessOS — Revenue Operations Framework

**Document:** Revenue Ops Framework  
**Product:** WitnessOS (Empire Labs Pty Ltd)  
**Phase:** Design Partner Alpha (Phase F)  
**Author:** Empire Labs Strategy  
**Date:** July 2026  
**Status:** Internal — not for external distribution

---

## 1. Executive Summary

WitnessOS is a runtime governance layer for autonomous AI agents — a new category with no direct incumbent. This framework defines the pricing model, packaging strategy, revenue operations, and commercial approach for alpha through to general availability (GA).

**Core thesis:** WitnessOS pricing must balance three constraints:
- **Category creation** — no market comp exists, so we are setting anchors
- **Enterprise procurement reality** — 6–12 month sales cycles, compliance buyer, security review
- **Bottom-up developer adoption** — self-serve tiers that pull enterprise through

**Recommended approach:** Usage-aware tiered SaaS with action-volume ceilings, agent caps, and retention-based differentiation. Enterprise is custom/negotiated. Design Partners get $0 preferential terms during alpha with locked-in pricing for 12 months post-GA.

---

## 2. Market Context — Comparable Pricing Research

### 2.1 GRC / Compliance Automation Platforms

| Platform | Entry Tier | Mid-Tier | Enterprise | Model |
|---|---|---|---|---|
| **Vanta** | ~$8K–$11.5K/yr (1 framework, small team) | $20K–$45K/yr (multi-framework, automation) | $80K+/yr custom | Tiered by business size + frameworks; per-framework add-ons ~$5K–$15K each |
| **Drata** | ~$10K–$12K/yr | — | Custom, typically $25K+ | Tiered, continuous compliance |
| **OneTrust (AI Governance module)** | $50K–$100K/yr | $100K–$200K/yr | $300K+/yr | Modular; admin users + AI inventory count; $10K min ACV from 2026 |
| **Strike Graph** | $10K/yr (Certify) | $21.5K/yr (Scale) | $35K/yr (Enterprise) | Published tiers (rare in this space) |
| **Sprinto** | ~$10K/yr (startup) | $20K–$30K/yr | Custom | Lower-cost alternative |
| **MetricStream** | — | — | $180K/3yr typical | Custom enterprise |
| **ServiceNow GRC** | ~$5K–$20K/yr+ | — | $50K–$500K+/yr | Per-module, enterprise |
| **CoreStream GRC** | £18K–£25K/yr | — | Custom | Unlimited licenses, per-use-case |

**Key takeaway:** Enterprise GRC floors are $10K–$20K/yr. AI governance (OneTrust module) starts at $50K. Mid-market compliance automation clusters around $15K–$45K/yr. Enterprise can exceed $250K. The market tolerates opaque pricing for enterprise and revealed pricing for SMB/self-serve.

### 2.2 AI Observability / Governance Platforms

| Platform | Entry | Mid | Enterprise | Model |
|---|---|---|---|---|
| **Fiddler AI** | Usage-based tiers | Premium (custom) | Enterprise (custom) | Usage-based on monitored models |
| **WhyLabs** | Free (limited) | $125/mo (Expert, 3 projects) | Custom | Per-project, per-volume |
| **Evidently AI** | Free (OSS) | $399/mo (Expert) | Custom (on-prem) | Per-user, per-volume |
| **Arize AI** | — | — | Custom | Enterprise-only custom quotes |

**Key takeaway:** AI observability platforms use usage-based or volume-based pricing (predictions monitored, models tracked). Entry points are lower than GRC ($0–$500/mo) but enterprise quickly goes custom. **No platform yet dominates runtime AI agent governance** — this is greenfield.

### 2.3 What WitnessOS Is Competing Against

WitnessOS does not directly compete with Vanta/Drata/OneTrust (which are compliance documentation platforms). It competes with:
- **The "build vs. buy" decision** — enterprises building in-house governance
- **Doing nothing** — the status quo of blind agent deployment (largest competitor)
- **Emerging agent framework vendors** — LangSmith, Anthropic's Console (if they add governance)

**Pricing implication:** We anchor against the cost of non-compliance (EU AI Act fines up to 7% of global revenue) and the cost of building in-house (estimated 3–6 eng-months = $150K–$300K+ for an MVP).

---

## 3. Pricing Model Options

### Option A: Pure Usage-Based (actions/month)

**Structure:** Pay per action evaluated by the policy engine.
- Advantages: Aligns cost with value, easy to start, scales naturally
- Disadvantages: Unpredictable bills for enterprises, harder to forecast revenue; procurement prefers fixed costs
- Benchmark: Fiddler, WhyLabs use this for observability

### Option B: Tiered Seat-Based (agents)

**Structure:** Pay per governed agent (like per-seat SaaS).
- Advantages: Simple, predictable, easy to communicate
- Disadvantages: Doesn't capture volume differences (one agent doing 10K actions vs 100K); punishing for small teams with many agents
- Benchmark: Most enterprise SaaS (Slack, GitHub)

### Option C: Hybrid — Tiered Agent + Action Ceilings (Recommended)

**Structure:** Fixed monthly price includes X agents and Y actions/month. Overages or upgrades for higher ceilings.

**Advantages:**
- Predictable for both customer and vendor
- Natural upgrade path: Free → Starter → Pro → Enterprise
- Action ceiling captures usage intensity without billing surprise
- Agent cap keeps it intuitive
- Aligns with industry norms (Vanta tiers by frameworks, not actions; but action-based aligns with AI observability)

**Disadvantages:**
- Needs ongoing calibration of action ceiling per tier
- Overage handling needs clear policy

**Current implementation** (pricing.html) already follows this model.

### Option D: Value-Based — Percentage of AI Spend or Per-Incident

**Structure:** Price as % of customer's total AI agent infrastructure spend, or per-governed-incident prevented.

- Advantages: Captures massive enterprise value; aligns with risk reduction
- Disadvantages: Complex to negotiate; requires trust in customer reporting; early-stage products lack negotiating leverage
- Benchmark: Insurance-like models; enterprise security platforms sometimes use this

### Option E: Freemium + Enterprise-Only (Two-Part)

**Structure:** Free tier for developers; everything else is enterprise custom-quoted.

- Advantages: Simple, no mid-market support overhead
- Disadvantages: Misses SMB/mid-market; self-serve developers have no upgrade path; requires sales-led for every dollar
- Benchmark: OneTrust, MetricStream (no self-serve published pricing)

---

## 4. Recommended Pricing Structure

### 4.1 Tier Architecture

| Tier | Target | Price | Agents | Actions/mo | Retention | Support | Deployment |
|---|---|---|---|---|---|---|---|
| **Free** | Evaluation, hobbyists | $0 | 1 | 500 | 3 days | Discord community | Cloud |
| **Starter** | Small teams, first production | $95/mo ($950/yr) | 3 | 5,000 | 30 days | Email 24h | Cloud or self-host |
| **Pro** | Growing AI fleets | $495/mo ($4,950/yr) | 10 | 50,000 | 12 months | Email + priority | Cloud or self-host |
| **Enterprise** | Large orgs, regulated industries | Custom ($2K–$10K+/mo) | Unlimited | Unlimited | Custom (up to 7yr) | Dedicated SLAs | On-prem / air-gapped / VPC |

**Annual discount:** ~17% effective (2 months free on annual billing).

### 4.2 Design Partner — Alpha Pricing

| Component | Terms |
|---|---|
| **Fee** | $0 during alpha period |
| **Duration** | 2–4 week operational review cycle; extendable by mutual agreement |
| **Agents** | Up to 5 governed agents |
| **Actions** | Up to 25,000 actions/month |
| **Evidence grade** | E3 max (corroborated) — E4 disabled during alpha |
| **Deployment** | Single-tenant, empire-labs managed |
| **Credential management** | Sandbox/test mode only (Gmail + Stripe) |
| **Post-alpha conversion** | Locked-in pricing: 50% off first-year Enterprise tier for 12 months post-GA |
| **First partner** | IO Digital (previously flagged as potential first partner) |

**Rationale for $0:** Alpha is about learning, not revenue. Design partners provide:
- Product feedback and bug discovery
- Reference case studies and testimonials
- Referral network into their industry vertical
- Early credibility for category creation

### 4.3 Enterprise Tier — Commercial Framework

Enterprise pricing is custom-quoted based on:

| Variable | Guidance | Notes |
|---|---|---|
| **Annual floor** | $24,000/yr ($2,000/mo) | Under $24K, route to Pro tier |
| **Typical range** | $24K–$120K/yr | Scales with agent count, regulatory burden |
| **High-complexity** | $120K–$250K+/yr | Air-gapped, multi-region, custom SLAs, E4+ |
| **Agents included** | 25+ (negotiable) | First 25 included, additional agents priced per-block |
| **Actions ceiling** | Negotiable | Typically 500K–5M/mo |
| **Evidence grade** | E4+ (TSA-anchored) | Requires revocation infra; post-alpha deliverable |
| **Deployment** | On-prem / air-gapped / VPC | Enterprise standard |
| **Onboarding fee** | $5K–$25K one-time | Covers integration, policy setup, security review |
| **Annual escalator** | 10–15% YoY | Standard enterprise SaaS practice |

**Enterprise pricing per additional agent block (beyond included):**  
- Blocks of 10 additional agents: $500/mo per block ($50/agent/mo)

---

## 5. Recommended Pricing Strategy

### 5.1 Positioning

Anchor WitnessOS against:
1. **Cost of non-compliance risk** — EU AI Act fines up to 7% global revenue; Colorado AI Act penalties
2. **Cost of building in-house** — $150K–$300K+ engineering investment for an MVP governance layer
3. **Cost of breach/incident** — average AI governance failure cost estimated at $14.8M (Ponemon)

| WitnessOS is… | WitnessOS is NOT… |
|---|---|
| Runtime AI agent governance | A compliance documentation tool (like Vanta/OneTrust) |
| Pre-action policy enforcement | Post-hoc log analysis (like SIEM) |
| Cryptographic proof (Merkle chain) | A logging library |
| Agent-agnostic infrastructure | An agent framework (like LangChain) |

### 5.2 Pricing Philosophy

1. **Free tier is a growth engine, not a revenue center.**  
   - 1 agent, 500 actions, 3-day retention
   - Converts developers who need more (more agents, longer retention, team features)
   - Low friction entry for the enterprise bottom-up wedge

2. **Starter and Pro are self-serve revenue.**  
   - No sales involvement up to $495/mo
   - Stripe-powered, automated upgrades
   - Annual discount incentivises commitment

3. **Enterprise is solution-sold.**  
   - Regulated industries (financial services, health, legal, government)
   - Sold as risk reduction + compliance readiness, not just software
   - Deal sizes $24K–$250K+/yr

4. **Design Partner → Enterprise conversion is the critical path.**  
   - Alpha pricing locks in reference customers
   - 50% first-year discount post-GA rewards early commitment
   - IO Digital as first partner validates Australian market viability

### 5.3 Currency Strategy

WitnessOS must work for Australian market while being US-competitive.

| Currency | Default for | Approach |
|---|---|---|
| **USD** | Published pricing; SaaS platform | All tiers published in USD |
| **AUD** | Australian customers; Enterprise deals | Convert at ~0.65 USD/AUD floor; accept AUD invoicing for AU Enterprise deals |
| **GBP/EUR** | Future UK/EU expansion | Post-Series A; annual subscription only |

**AUD pricing (indicative):**

| Tier | AUD Monthly | AUD Annual |
|---|---|---|
| Free | $0 | $0 |
| Starter | $145/mo | $1,450/yr |
| Pro | $760/mo | $7,600/yr |
| Enterprise | From $3,100/mo | From $37,000/yr |

**Note:** AUD pricing uses ~0.65 FX floor. Revisit quarterly. AU enterprise deals can quote in AUD to simplify procurement (no FX hedging needed).

### 5.4 Competitive Pricing Map

```ascii
                     SERVICE
                     COST
                       ▲
                       │                    OneTrust AI Gov
                       │                         ● ($50K–$300K)
                       │
               $50K   │                    MetricStream
                       │                         ● ($60K+/yr)
                       │
                       │              Vanta Enterprise
                       │                   ● ($80K+/yr)
               $20K   │
                       │         Vanta Pro     │
                       │            ● ($22K/yr)│
                       │                       │
                $6K   │   Vanta Starter        │
                       │      ● ($8K–$11K/yr)  │
                       │                       │
                       │   Free                 │
                $0    └──────────────────────────►
                                  COMPLEXITY /
                                  REGULATORY BURDEN

         WITNESSOS POSITIONING:
         Free ($0) ── Starter ($1,140/yr) ── Pro ($5,940/yr) ── Enterprise ($24K+)
                       SELF-SERVE ──────────────────────────► SALES-ASSISTED
```

WitnessOS is deliberately priced below Vanta/OneTrust at the mid-tier because:
- We are a new category (no incumbent premium)
- We need to incentivise adoption over build-vs-buy
- We can raise prices as category matures (land-and-expand)

---

## 6. Revenue Operations

### 6.1 Billing Infrastructure

| Component | Implementation | Notes |
|---|---|---|
| **Payment processor** | Stripe (current) | Test mode active during alpha; live mode for GA |
| **Subscription model** | Stripe Subscriptions + Usage-based billing | Metered actions via Stripe usage records |
| **Tax handling** | Stripe Tax (automatic) | Covers GST (AU), VAT (UK/EU), sales tax (US) |
| **Invoicing** | Stripe Invoicing for Enterprise | Net-30 terms standard; net-60 for enterprise |
| **Multi-currency** | Stripe multi-currency | USD primary; AUD, GBP, EUR as needed |
| **Dunning** | Stripe automated retry | 3 retries over 7 days before suspension |
| **Coupon codes** | Stripe Coupons | Design partner discount codes, annual promo |

### 6.2 Key Revenue Metrics & Targets

| Metric | Current (Alpha) | Month 12 Target | Month 18 Target |
|---|---|---|---|
| **MRR** | $0 (alpha) | $36,000 | $60,000 |
| **ARR run-rate** | $0 | $432,000 | $720,000 |
| **Paying customers** | 0 | 45 | 75 |
| **Blended ACV** | — | ~$800/mo | ~$800/mo |
| **Gross margin** | — | 85% | 85% |
| **Net revenue retention (NRR)** | — | Target 110%+ | Target 120%+ |
| **Monthly burn** | ~$35K | ~$35K | ~$35K |
| **Months runway** | ~18 | ~14 | ~8 |
| **CAC (Starter/Pro/Enterprise)** | — | $500/$1,500/$5,000 | — |
| **LTV:CAC** | — | 5:1–10:1 | 5:1–10:1 |

### 6.3 Revenue Mix Projection (Month 18)

| Tier | Customers | % of Customers | Avg MRR/Customer | Segment MRR | % of MRR |
|---|---|---|---|---|---|
| Free | ~1,500 | 95% | $0 | $0 | 0% |
| Starter | ~30 | 2% | $95 | $2,850 | 5% |
| Pro | ~25 | 1.5% | $495 | $12,375 | 21% |
| Enterprise | ~20 | 1.5% | ~$2,240 avg | ~$44,775 | 74% |
| **Total paying** | **75** | — | **$800 blended** | **$60,000** | **100%** |

**Key insight:** Enterprise is 1.5% of customers but 74% of revenue. **The business lives or dies on enterprise sales.** The self-serve tiers (Free/Starter/Pro) are lead generation for enterprise, not primary revenue drivers.

### 6.4 Expansion Revenue Levers

| Lever | Mechanism | Expected Uplift |
|---|---|---|
| **Agent count growth** | Customer adds agents → exceeds tier cap → upgrades | 20–30% of expansion revenue |
| **Action volume growth** | More usage hits action ceiling → upsell or overage | 15–25% of expansion revenue |
| **Framework/connector expansion** | More integrations (Salesforce, SAP, Xero) increase stickiness and switching cost | Enabler, not direct revenue |
| **Evidence grade upgrade** | E3 → E4+ for regulated customers | Justifies enterprise tier |
| **Multi-deployment (geo expansion)** | Same customer, multiple regions | 2–3x deal size for global customers |

### 6.5 Discounting Guidelines

| Scenario | Max Discount | Approval |
|---|---|---|
| Annual prepay (Starter/Pro) | 17% (2 months free) | Automated (Stripe) |
| Annual prepay (Enterprise, <$50K) | 10–20% | Founder/CEO |
| Multi-year commit (Enterprise, $50K–$150K) | 15–25% | Founder/CEO |
| Multi-year commit (>$150K) | 20–30% | Founder/CEO + investor consultation |
| Design Partner → Enterprise conversion | 50% first year | Design partner agreement terms |
| Non-profit / academic | 30% (Starter/Pro); case-by-case (Enterprise) | Founder/CEO |
| Channel partner resale margin | 20% recurring commission | Partner agreement |
| Proof-of-concept discount (Enterprise) | 3 months at $500/mo | Founder/CEO |

**Principle:** Discount for commitment (annual, multi-year, reference case study), not for negotiation skill. Never discount below unit economics viability (80% gross margin floor).

---

## 7. Customer Segmentation & Pricing Elasticity

### 7.1 Segments

| Segment | Description | Willingness to Pay | Price Sensitivity | Recommended Tier |
|---|---|---|---|---|
| **Startup (<20 emp)** | Building first AI agent; no compliance function | <$100/mo | High | Free → Starter |
| **Scale-up (20–200 emp)** | 1–5 agents in production; starting compliance conversations | $200–$2,000/mo | Moderate | Starter → Pro |
| **Mid-market (200–1K emp)** | 5–20 agents; active compliance/risk team; SOC 2 underway | $2K–$5K/mo | Low-Moderate | Pro → Enterprise ($24K–$60K/yr) |
| **Enterprise (1K+ emp)** | 20+ agents; dedicated GRC team; regulated industry | $5K–$20K+/mo | Low | Enterprise ($60K–$250K+/yr) |
| **Government** | Highest compliance requirements; air-gapped | $10K–$30K+/mo | Very Low (procurement-driven) | Enterprise (custom, long cycle) |
| **Data centre partners** | Reselling to tenants | Commission-based | N/A | Reseller agreement |

### 7.2 Pricing Elasticity by Market

| Market | Price Sensitivity | FX Impact | Strategy |
|---|---|---|---|
| **Australia (home)** | Moderate | Low (AUD invoicing) | Anchor domestic; AU Enterprise slightly below US Enterprise to reflect smaller scale |
| **United States** | Low (enterprise), Moderate (SMB) | USD = base currency | US pricing as published; full self-serve for SMB; enterprise sales-led |
| **UK/Europe** | Moderate | GBP/EUR (post-Series A) | Slightly below US to account for VAT and longer sales cycles |
| **SE Asia (SG, MY)** | Higher | SGD/MYR | Discounted Starter/Pro; Enterprise by quote; partner-led |
| **Australia (government)** | Very Low (procurement) | AUD | Separate government pricing schedule; longer payment terms (net-60) |

---

## 8. Revenue Timeline — Alpha to GA

### Phase F: Design Partner Alpha (Current — July 2026)

| Element | Detail |
|---|---|
| **Revenue** | $0 |
| **Partners** | 1 design partner (invitation-only), IO Digital target |
| **Evidence grade** | E3 max |
| **Deployment** | Single-tenant, empire-labs managed |
| **Pricing** | $0, preferential locked-in terms for first partner |
| **Billing** | Stripe test mode only |
| **Key goal** | Validate product-market fit; gather reference case study |

### Phase G: Public Preview (Target: Q4 2026)

| Element | Detail |
|---|---|
| **Revenue** | Early Starter/Pro self-serve |
| **Pricing** | Published tiers (Free/Starter/Pro/Enterprise) live on Stripe |
| **Target** | 5–10 paying customers; $4K–$8K MRR |
| **Evidence grade** | E3; E4 readied for Enterprise |
| **Deployment** | Cloud (multi-tenant SaaS) + self-host docs |
| **Enterprise** | Manual quote + onboarding; no self-serve |
| **Billing** | Stripe live mode (USD); AUD via request |

### v1.0 GA (Target: Q1 2027)

| Element | Detail |
|---|---|
| **Revenue** | $36K MRR ($432K ARR run-rate) |
| **Customers** | 45 paid (mix of all tiers) |
| **Enterprise** | Formalised sales process; SLAs; on-prem deployment |
| **Evidence grade** | E4+ (TSA-anchored) for enterprise |
| **Partners** | NEXTDC/Equinix channel active |
| **Series A ready** | $432K ARR, 85% margins, 5:1+ LTV:CAC |

---

## 9. Risks & Mitigations

### Pricing Risks

| Risk | Impact | Mitigation |
|---|---|---|
| **Enterprise prospects balk at $24K floor** | Slower enterprise adoption | Offer 3-month POC at $500/mo; prove value before negotiating |
| **Free tier cannibalises Starter** | Low conversion rate | Tight free tier limits (1 agent, 500 actions, 3-day retention); make pain of data loss real |
| **Action ceiling too low for Pro** | Customers churn or get frustrated at overage | Monitor usage data during beta; adjust ceilings before GA; communicate "soft limit with warning" |
| **Annual discount too generous** | Revenue timing pressure | 17% is competitive (< Vanta's implied 20%); cap at 2 months free |
| **AUD/USD widening** | AU Enterprise becomes too cheap | Quarterly FX review; include FX adjustment clause in contracts |
| **Category not recognised in budget** | No budget line item for "AI agent governance" | Sell as "risk reduction + compliance readiness"; map to existing GRC/cybersecurity budgets |
| **Open-source alternative emerges** | Price pressure | Empire Stack (open-source ACI/AIP/AJSON) complements WitnessOS; proprietary Merkle chain + policy engine = moat |

### Go-To-Market Risks

| Risk | Impact | Mitigation |
|---|---|---|
| **Enterprise sales cycle too long (6–12 mo)** | Miss MRR targets | Bottom-up self-serve keeps revenue flowing; enterprise pipeline builds in parallel; 18-month runway accounts for slow start |
| **Single design partner risk** | Narrow feedback; reference dependency | Alpha is single-partner by design (quality over quantity); expand to 2–3 design partners before public preview |
| **Data centre partnership delay** | Distribution channel stalled | Direct sales fills gap; bottom-up self-serve continues regardless |
| **Regulatory timeline slower than expected** | Urgency to buy diminishes | Sell value proposition (agent safety, visibility, control) independent of regulation; regulatory compliance is accelerant, not foundation |
| **In-house build by well-funded enterprise** | Lost deal | Most enterprises will not build their own governance layer (not core competency); price in-house at 3–6 eng-months and compare against WitnessOS annual cost |

---

## 10. Appendix: Pricing FAQ (Internal)

### Q: Why not pure usage-based pricing?

Usage-based pricing creates budget unpredictability for enterprise procurement. Enterprise buyers prefer fixed costs. The hybrid model (tiered agent + action ceilings) gives them predictability while capturing usage intensity at scale.

### Q: Why is Enterprise floor $24K when Vanta Essentials is $8K?

Vanta Essentials is a compliance documentation tool — a different category. WitnessOS Enterprise covers runtime governance, cryptographic proof, on-prem deployment, and dedicated SLAs. $24K/yr aligns with the bottom of managed-enterprise SaaS ($2K/mo). Startups and small teams use Starter or Pro.

### Q: Should we offer a free trial for Enterprise?

Yes — 3-month POC at $500/mo with full Enterprise features. This reduces friction, demonstrates value, and converts to full Enterprise pricing. The POC fee covers onboarding costs and signals commitment.

### Q: What about usage overage charges?

For Starter and Pro: action usage over 100% of ceiling triggers a notification (80%, 90%, 100% warnings). At 110%, actions are paused until billing reset or upgrade. No surprise overage charges. For Enterprise: overage is negotiated in contract (typically 1.5x per-unit rate for excess actions).

### Q: When do we raise prices?

Two triggers:
1. **Category maturity** — when analyst firms recognise the category and competitors emerge (raise 15–25% and invest in enterprise features)
2. **Evidence grade parity** — when E4+ is live and independently audited (justifies premium over self-built alternatives)

### Q: Should we offer on-premise pricing differently?

On-premise (Enterprise tier) is priced at the same subscription rate as cloud. The value is in the software, not the hosting. Enterprise customers pay for the governance layer; we provide Docker images and deployment scripts. If they want managed on-prem (we run it for them), that's a professional services add-on ($5K–$15K/mo depending on complexity).

---

## 11. Summary of Recommended Decisions

| Decision | Recommendation | Rationale |
|---|---|---|
| **Pricing model** | Tiered + usage-aware hybrid | Industry standard; predictable for customers; natural upgrade path |
| **Number of tiers** | 4 (Free, Starter, Pro, Enterprise) | Covers evaluation → SMB → mid-market → enterprise |
| **Design Partner pricing** | $0 during alpha; 50% off first year post-GA | Incentivises early adoption and case study; builds reference base |
| **Enterprise floor** | $24K/yr ($2K/mo) | Below $24K, route to Pro tier; protects enterprise sales team capacity |
| **Currency** | USD published; AUD for AU enterprise | Localisation for home market; simplicity in global pricing |
| **Annual discount** | 17% (2 months free) | Competitive; incentivises commitment |
| **Billing processor** | Stripe (test → live at public preview) | Already integrated; supports subscriptions, usage metering, tax |
| **Revenue focus** | Enterprise (74% of projected MRR at Month 18) | Self-serve is marketing; enterprise is revenue |
| **First design partner** | IO Digital (previously flagged) | AIM-listed advisory firm; strong UK-AU regulatory use case |

---

*This is a living document. Revisit quarterly as pricing data, competitor moves, and customer feedback accumulate. Next review: End of Design Partner Alpha (Phase F).*

---

**WitnessOS by Empire Labs Pty Ltd**  
Patent Pending — AU 2026906017  
contact@empirelabs.com.au
