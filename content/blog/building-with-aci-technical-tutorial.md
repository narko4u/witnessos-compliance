---
title: Building with ACI — The Open Standard for Agent Capability Discovery
published: true
description: A practical walkthrough of the Agent Capability Interface (ACI) — defining manifests, validating with SpecValidator, and integrating with WitnessOS for production-ready agent governance.
tags: ai, agents, standards, python, devops
cover_image: https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1200&h=630&fit=crop
---

# Building with ACI — The Open Standard for Agent Capability Discovery

**By Empire Labs Engineering**
**Published: July 2026**

---

*TL;DR — The Agent Capability Interface (ACI) is an open standard for declaring what your AI agent can do, how it can do it, and what constraints govern its actions. This tutorial walks through writing an ACI manifest, validating it programmatically, and integrating it with the WitnessOS gateway for credential-brokered governance.*

---

## What Is ACI?

The **Agent Capability Interface (ACI)** is an open, schema-based standard for machine-readable agent capability discovery. Think of it as a contract your agent publishes — a manifest that answers three questions:

1. **Who are you?** — A unique `agent_name` identifier.
2. **What can you do?** — A list of `capabilities` the agent supports.
3. **How are you constrained?** — Optional operational guardrails like rate limits and allowed tool sets.

ACI is the first standard in the agent-interoperability stack. It sits alongside AIP (Agent Interaction Protocol) for agent-to-agent negotiation and AJSON for schema-enforced agent communication. Together, they form an open, governance-aware foundation for multi-agent systems.

The standard is language-agnostic, Python-friendly, and published under MIT. The reference implementation lives in a single Python package — `aci-spec` — that you can install today.

---

## Installing the ACI Package

Grab the reference implementation from anywhere you keep your Python packages:

```bash
pip install aci-spec
```

Or, if you're working from source:

```bash
cd aci/py
pip install -e .
```

Once installed, you can verify it's working:

```python
import aci
print(aci.VERSION)  # 0.1.0
print(dir(aci))      # ['MANIFEST_SCHEMA', 'SpecValidator', 'VERSION', ...]
```

Two things are exported: `MANIFEST_SCHEMA` (the JSON Schema definition) and `SpecValidator` (the validation class). That's the entire surface area — minimal by design.

---

## Anatomy of an ACI Manifest

An ACI manifest is a plain dictionary (or JSON/YAML document) conforming to the `MANIFEST_SCHEMA`. Here's the full schema structure directly from the source:

```python
MANIFEST_SCHEMA = {
    "type": "object",
    "required": ["agent_name", "version", "capabilities"],
    "properties": {
        "agent_name": {
            "type": "string",
            "description": "Unique identifier for the agent",
        },
        "version": {
            "type": "string",
            "description": "Semantic version of the agent's capability set",
        },
        "capabilities": {
            "type": "array",
            "items": {"type": "string"},
            "description": "List of capability identifiers the agent supports",
        },
        "constraints": {
            "type": "object",
            "description": "Operational constraints on the agent",
            "properties": {
                "max_tokens": {"type": "integer"},
                "allowed_tools": {"type": "array", "items": {"type": "string"}},
                "rate_limit": {"type": "integer"},
            },
        },
        "metadata": {
            "type": "object",
            "description": "Additional agent metadata",
        },
    },
}
```

Three fields are **required**:

| Field | Type | Description |
|-------|------|-------------|
| `agent_name` | string | Unique identifier for the agent (e.g., `"data-analyzer-v2"`) |
| `version` | string | Semantic version of this capability declaration (e.g., `"1.0.0"`) |
| `capabilities` | [string] | Ordered list of capability identifiers the agent supports |

Two fields are **optional**:

| Field | Type | Description |
|-------|------|-------------|
| `constraints` | object | Operational bounds — `max_tokens`, `allowed_tools`, `rate_limit` |
| `metadata` | object | Arbitrary key-value metadata (your extensibility hook) |

---

## Writing Your First Manifest

Let's define a manifest for a hypothetical security analysis agent called **"Sentinel"**:

```python
sentinel_manifest = {
    "agent_name": "sentinel-threat-analyzer",
    "version": "1.2.0",
    "capabilities": [
        "threat:intel:query",
        "log:analyze:syslog",
        "alert:create:high",
        "report:generate:pdf",
    ],
    "constraints": {
        "max_tokens": 8192,
        "allowed_tools": [
            "vulnerability-db",
            "log-parser",
            "alert-manager",
        ],
        "rate_limit": 100,
    },
    "metadata": {
        "vendor": "Empire Labs",
        "risk_level": "high",
        "audit_required": True,
    },
}
```

Notice the conventions:
- **Capability identifiers** use a colon-delimited namespace pattern: `domain:action:scope`. This makes discovery and policy-matching predictable.
- The `version` field tracks the capability declaration, not the agent binary — bump it when capabilities change, not when internal logic changes.
- `constraints` are advisory but discoverable. A governance gateway (like WitnessOS) can read them to pre-configure policy.

---

## Validating With SpecValidator

The `SpecValidator` class provides a single method — `validate_manifest()` — that returns a structured result:

```python
from aci import SpecValidator

validator = SpecValidator()

result = validator.validate_manifest(sentinel_manifest)

print(result)
# {
#     "valid": True,
#     "errors": [],
#     "manifest": { ... },
# }
```

The return dict always contains three keys:

- **`valid`** — `True` if all checks pass, `False` otherwise.
- **`errors`** — A list of human-readable error messages (empty when valid).
- **`manifest`** — The original manifest dict (passed through unchanged).

### Handling Invalid Manifests

Let's see what happens with a broken manifest:

```python
bad_manifest = {
    "agent_name": 42,                          # wrong type
    "version": "1.0.0",
    # "capabilities" is missing — required field
    "constraints": {
        "unknown_constraint": True,            # not in schema
    },
}

result = validator.validate_manifest(bad_manifest)
print(result["valid"])   # False
print(result["errors"])
# [
#     "Missing required field: 'capabilities'",
#     "'agent_name' must be a string",
#     "Unknown constraint: 'unknown_constraint'",
# ]
```

The validator catches all three issues in one pass — missing required fields, type mismatches, and unknown constraint keys. No silent failures, no partial validation.

### What Gets Checked

The validator runs four categories of checks:

1. **Required fields** — `agent_name`, `version`, and `capabilities` must all be present.
2. **Type correctness** — `agent_name` and `version` must be strings; `capabilities` must be a list of strings.
3. **Capabilities integrity** — Every item in the capabilities list must be a string.
4. **Constraints validity** — If present, `constraints` must be a dict, and its keys must be one of `max_tokens`, `allowed_tools`, or `rate_limit`.

That's it. Deliberately simple. The spec is meant to be a **discovery and declaration layer**, not a policy engine. Policy enforcement is what comes next.

---

## Integrating With WitnessOS

WitnessOS is a credential-brokered enforcement gateway for autonomous AI agents. It doesn't *watch* agent actions — it **mediates** them. Agents hold no credentials; all secrets live in the gateway vault. Every action is evaluated against signed, versioned policies before execution, and every outcome is recorded in a cryptographically chained evidence receipt.

ACI manifests are the **identity and capability layer** of this architecture. Here's how they connect:

### 1. Agent Registration

When an agent registers with the WitnessOS gateway, it presents its ACI manifest. The gateway stores the manifest and uses it to:

- Map the `agent_name` to an identity record (with mTLS certificate binding).
- Index the `capabilities` list for policy evaluation — a policy rule can allow or deny specific capabilities.
- Apply the `constraints` as default guardrails (e.g., `rate_limit` becomes a rate limiter on the gateway).

```python
# Pseudocode — WitnessOS agent registration flow
gateway.register_agent(
    manifest=sentinel_manifest,
    tls_cert=agent_cert_pem,
)
# Gateway response:
# {
#   "agent_id": "ag_9f3b2a1c",
#   "status": "registered",
#   "capabilities_indexed": 4,
#   "constraints_applied": True,
# }
```

### 2. Capability-Based Policy Evaluation

Policies in WitnessOS are written in Rego (from the Open Policy Agent ecosystem). A policy can reference capability identifiers directly:

```rego
# Example Rego rule: Allow threat intel queries from Sentinel only
allow if {
    input.action.capability == "threat:intel:query"
    input.agent.agent_name == "sentinel-threat-analyzer"
}
```

Because the ACI manifest declared `threat:intel:query` as a capability, the gateway knows it's a valid action for this agent. Unknown capabilities are automatically denied — no default-permit footgun.

### 3. Evidence Receipts

Every mediated action produces a structured evidence receipt. The receipt includes the agent's identity (from the manifest), the action hash, the policy decision, and a cryptographic chain link:

```json
{
    "case_id": "ev_7d8e9f0a",
    "agent_id": "ag_9f3b2a1c",
    "agent_name": "sentinel-threat-analyzer",
    "capability": "threat:intel:query",
    "evidence_grade": "E2",
    "evidence_status": "CHAINED",
    "chain": {
        "head_commitment_hash": "sha256:a1b2c3d4...",
        "event_count": 142,
        "signature": "mechash:0x..."
    }
}
```

An external auditor can verify this receipt against the evidence chain without trusting the agent, the gateway operator, or the infrastructure. The evidence is **independently verifiable** — a property no proxy-based monitoring solution can offer.

---

## Complete Workflow Example

Here's a full end-to-end script that ties it all together — defining a manifest, validating it, submitting it to a WitnessOS gateway, and performing a governed action:

```python
"""ACI + WitnessOS: Complete integration example."""

import json
import urllib.request
from aci import SpecValidator

# 1. Define the manifest
manifest = {
    "agent_name": "data-analyzer-v2",
    "version": "2.1.0",
    "capabilities": [
        "data:query:sql",
        "data:aggregate:stats",
        "report:generate:csv",
    ],
    "constraints": {
        "max_tokens": 4096,
        "allowed_tools": ["sql-engine", "stats-lib"],
        "rate_limit": 50,
    },
    "metadata": {
        "team": "data-platform",
        "environment": "production",
    },
}

# 2. Validate locally
validator = SpecValidator()
result = validator.validate_manifest(manifest)
assert result["valid"], f"Invalid manifest: {result['errors']}"
print("✓ Manifest validated successfully")

# 3. Register with WitnessOS gateway
gateway_url = "http://localhost:8100"
payload = json.dumps({"manifest": manifest}).encode()

req = urllib.request.Request(
    f"{gateway_url}/v1/agents",
    data=payload,
    headers={"Content-Type": "application/json"},
    method="POST",
)

with urllib.request.urlopen(req, timeout=10) as resp:
    registration = json.loads(resp.read())
    agent_id = registration["agent_id"]
    print(f"✓ Agent registered: {agent_id}")

# 4. Query live evidence
with urllib.request.urlopen(
    f"{gateway_url}/v1/evidence?agent_id={agent_id}", timeout=10
) as resp:
    evidence = json.loads(resp.read())
    print(f"✓ Evidence cases: {len(evidence.get('cases', []))}")

print("Done — agent is governed and auditable.")
```

---

## Why This Matters

The agent ecosystem is growing faster than the governance infrastructure. The NSA's MCP Security Guidance (June 2026) identified eight critical gaps in agent communication protocols — no authentication, no authorization, no audit trails. The EU AI Act enforces high-risk conformity requirements starting August 2026. Regulators want proof, not promises.

ACI addresses the first gap: **discoverability**. An agent that can declare its identity, capabilities, and constraints in a machine-readable format can be governed before it acts. Without that declaration, a gateway has no way to distinguish a legitimate capability call from a prompt injection or a compromised agent.

The standard is open, the validator is a single import, and the integration surface is minimal. Start with a manifest — it's the foundation everything else builds on.

---

## Next Steps

- **Install ACI:** `pip install aci-spec`
- **Read the schema:** `from aci import MANIFEST_SCHEMA` and inspect it at runtime
- **Write a manifest** for your own agents — start with `agent_name`, `version`, and one capability
- **Validate it** with `SpecValidator().validate_manifest()`
- **Wire it to WitnessOS** for credential-brokered enforcement and cryptographic evidence

The repository is at [github.com/narko4u/agent-interaction-specs](https://github.com/narko4u/agent-interaction-specs). Contributions, feedback, and integration stories welcome.

---

*Empire Labs builds open standards for autonomous agent governance. ACI, AIP, and AJSON are the interoperability layer. WitnessOS is the enforcement layer. Both are open-source, MIT-licensed, and designed for production agent fleets.*

---

Regards,
Engineering Division
Empire Labs
[www.empirelabs.com.au](https://www.empirelabs.com.au)
