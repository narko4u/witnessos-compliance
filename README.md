# WitnessOS Compliance Pack

**Regulatory readiness for autonomous AI agents.**
Built on the [WitnessOS](https://github.com/narko4u/witnessos) credential-brokered enforcement gateway ([private repo](https://github.com/narko4u/witnessos-gateway)).

## What This Repo Contains

| Directory | Purpose |
|-----------|---------|
| `mappings/` | NSA MCP Security Guidance → WitnessOS feature mapping + NIST/ISO/C SA/ Singapore alignment |
| `templates/eu-ai-act/` | E0-E4 evidence templates for EU AI Act Articles 9, 14, 43 |
| `cli/` | `witnessos compliance` CLI — generate compliance reports |
| `content/blog/` | Positioning docs, blog posts, competitive analysis, technical tutorials |
| `docs/` | Updated architecture docs, deployment guide, interactive demos |
| `aci/py/` | ACI (Agent Capability Interface) Python package — schema + validation |
| `aip/go/` | AIP (Agent Interaction Protocol) Go module |
| `tools/` | Compliance scanner — fleet-wide agent governance audit |
| `docker/` | Enterprise deployment: Dockerfile + docker-compose.yml |
| `k8s/` | Kubernetes manifests for production deployment |

## Linked Repositories

- [`witnessos`](https://github.com/narko4u/witnessos) — Core WitnessOS runtime governance platform (public)
- [`witnessos-gateway`](https://github.com/narko4u/witnessos-gateway) — Proprietary credential-brokered enforcement gateway (private)
- [`witnessos-alpha`](https://github.com/narko4u/witnessos-alpha) — Alpha preview (public)
- [`witnessos-rogue-agent-audit`](https://github.com/narko4u/witnessos-rogue-agent-audit) — Agent discovery tool (public)
- [`eu-ai-act-compliance-grade`](https://github.com/narko4u/eu-ai-act-compliance-grade) — Self-assessment tool (public)

## Standards Alignment

- **NSA CSI** — Model Context Protocol: Security Design Considerations (June 2, 2026)
- **EU AI Act** — Articles 9 (Risk Management), 14 (Human Oversight), 43 (Conformity Assessment)
- **CSA** — Cloud Security Alliance AI Agent Governance Gap Research Note (April 3, 2026)
- **NIST AI 600-1** — AI Risk Management Framework
- **ISO/IEC 42001** — AI Management System
- **Singapore AI Verify** — AI Governance Testing Framework

## Phase Completion Status

| Phase | Title | Status | Date |
|-------|-------|--------|------|
| **Phase 1** | Foundation — NSA mapping, EU AI Act templates, CLI, positioning | ✅ Complete | Jul 28, 2026 |
| **Phase 2** | Build & Deploy — interactive demo, receipt visualizer, blog, GitHub push | ✅ Complete | Jul 28, 2026 |
| **Phase 3** | Commerce & Content — commerce demo, rogue agent video, landing page, compliance mapping | ✅ Complete | Jul 28, 2026 |
| **Phase 4** | Revenue & Reach — OpenAI pipeline, lead capture, ACI docs, content pipeline, community | ✅ Complete | Jul 29, 2026 |
| **Phase 5** | Scale & Enterprise — Docker Compose, k8s manifests, CI/CD, design partner kit | 🔄 In Progress | Jul 29, 2026 |

## Quick Start

```bash
# Install the CLI
pip install witnessos-compliance

# Run a compliance report
witnessos-compliance nsa-mcp
witnessos-compliance eu-ai-act --grade E3

# Fleet-wide compliance scan
python tools/compliance-scanner.py
```

## Enterprise Deployment

```bash
# Docker
cd docker && docker compose up

# Kubernetes
kubectl apply -f k8s/
```

---

**Empire Labs Security Division** · [empirelabs.com.au](https://www.empirelabs.com.au)
