# WitnessOS Technical Integration Guide

> For design partners connecting autonomous agents to the WitnessOS gateway.

**Gateway endpoint:** `https://<gateway-host>:8443`
**Protocol:** mTLS over HTTP/2 (FastAPI)

---

## Architecture Overview

The WitnessOS gateway enforces a zero-trust execution model for agent actions. Your agent never holds credentials — instead it requests action execution through four layered subsystems:

| Layer | Role |
|---|---|
| **Credential Broker** | Holds OAuth tokens, API keys, and secrets — agent never touches them |
| **Policy Engine** | Validates action intent against signed policy bundles |
| **Approval UI** | Presents exact-action hash bindings for human sign-off |
| **Event Store** | Append-only Merkle log producing tamper-proof receipts |

---

## Prerequisites

- Python 3.11+
- API key (issued to your partner account)
- mTLS client certificate (`.crt` + `.key`) from the [partner portal](https://<partner-portal-url>)
- `witnessos` CLI (`pip install witnessos-cli`)

---

## Quick Start

Post a signed action envelope to the `/api/action` endpoint:

```bash
curl -X POST https://<gateway-host>:8443/api/action \
  --cert /path/to/client.crt \
  --key /path/to/client.key \
  -H "X-API-Key: $WITNESS_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "agent_id": "partner-demo-01",
    "action": "gmail:send",
    "params": {
      "to": "user@example.com",
      "subject": "Test from WitnessOS",
      "body": "Hello from the gateway."
    },
    "action_hash": "sha256:abcd1234..."
  }'
```

**Successful response (202):**

```json
{
  "status": "pending_approval",
  "receipt": "E1-vQ7...",
  "approval_url": "https://<approval-host>/txn/vQ7..."
}
```

The receipt level indicates how far the action progressed:

- **E0** — Action logged to Event Store
- **E1** — Policy validated
- **E2** — Human approved (exact-action hash match)
- **E3** — Executed & Merkle-anchored

---

## Python Integration

```python
import requests

GATEWAY = "https://<gateway-host>:8443"
CERT = ("/path/to/client.crt", "/path/to/client.key")
HEADERS = {"X-API-Key": "your-api-key"}

def request_action(agent_id: str, action: str, params: dict) -> dict:
    payload = {
        "agent_id": agent_id,
        "action": action,
        "params": params,
        "action_hash": hashlib.sha256(
            f"{action}:{json.dumps(params, sort_keys=True)}".encode()
        ).hexdigest(),
    }
    resp = requests.post(
        f"{GATEWAY}/api/action",
        cert=CERT,
        headers=HEADERS,
        json=payload,
    )
    resp.raise_for_status()
    return resp.json()
```

---

## Connectors (Sandbox Mode)

Connectors translate abstract actions into API calls. Start in test mode:

| Connector | Sandbox | Live |
|---|---|---|
| **Gmail** | `gmail:sandbox:send` | `gmail:send` |
| **Stripe** | `stripe:test:charge` | `stripe:charge` |
| **Slack** | `slack:sandbox:post` | `slack:post` |

Sandbox actions are validated against the Policy Engine but never reach production APIs.

---

## Verification

After an action executes, verify its integrity with the CLI:

```bash
witnessos verify receipt E2-vQ7... \
  --gateway https://<gateway-host>:8443 \
  --cert client.crt \
  --key client.key
```

The tool fetches the Merkle proof from the Event Store and checks inclusion in the global ledger. A verified receipt guarantees that the action hash, policy bundle, and approval signature match — no tampering.

---

## Troubleshooting

| Symptom | Likely Cause | Fix |
|---|---|---|
| `401 Unauthorized` | Expired or missing API key | Regenerate key in partner portal |
| `403 Forbidden` | Policy bundle missing or revoked | Push a signed bundle via `witnessos policy push` |
| `412 Precondition Failed` | Action hash mismatch | Recompute hash with sorted params |
| `502 Bad Gateway` | Credential Broker unreachable | Check broker health at `/health` |

---

## Next Steps

1. Register your agent in the [partner portal](https://<partner-portal-url>)
2. Download your mTLS credentials
3. Set `WITNESS_API_KEY` in your deployment environment
4. Try the Gmail sandbox connector first
5. Run `witnessos verify` on every receipt in your test suite

For implementation details of the gateway itself, refer to the companion gateway repository (private, contact your partner engineer for access).
