# ACI Spec — Agent Capability Interface

An open standard for AI agent capability discovery and interoperability.

## Installation

```bash
pip install aci-spec
```

## Usage

```python
from aci import SpecValidator, MANIFEST_SCHEMA

manifest = {
    "agent_name": "research-agent-v1",
    "version": "1.0.0",
    "capabilities": ["web_search", "code_execution"],
    "constraints": {"max_tokens": 32000}
}

validator = SpecValidator()
result = validator.validate_manifest(manifest)
print(result)
```

## License

MIT
