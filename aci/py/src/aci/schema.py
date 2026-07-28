"""ACI manifest schema and validation logic."""

from typing import Any, Dict, List, Optional

MANIFEST_SCHEMA: Dict[str, Any] = {
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


class SpecValidator:
    """Validates ACI manifests against the specification."""

    def validate_manifest(self, manifest: Dict[str, Any]) -> Dict[str, Any]:
        """Validate an agent capability manifest.

        Args:
            manifest: The agent capability manifest to validate.

        Returns:
            A dict with keys:
                - valid: bool
                - errors: list of error messages (empty if valid)
                - manifest: the validated manifest
        """
        errors: List[str] = []

        # Check required fields
        required = ["agent_name", "version", "capabilities"]
        for field in required:
            if field not in manifest:
                errors.append(f"Missing required field: '{field}'")

        if errors:
            return {"valid": False, "errors": errors, "manifest": manifest}

        # Validate types
        if not isinstance(manifest["agent_name"], str):
            errors.append("'agent_name' must be a string")
        if not isinstance(manifest["version"], str):
            errors.append("'version' must be a string")
        if not isinstance(manifest["capabilities"], list):
            errors.append("'capabilities' must be a list")
        elif not all(isinstance(c, str) for c in manifest["capabilities"]):
            errors.append("All items in 'capabilities' must be strings")

        # Validate optional constraints
        if "constraints" in manifest:
            constraints = manifest["constraints"]
            if not isinstance(constraints, dict):
                errors.append("'constraints' must be an object")
            else:
                for key in constraints:
                    if key not in ("max_tokens", "allowed_tools", "rate_limit"):
                        errors.append(f"Unknown constraint: '{key}'")

        return {
            "valid": len(errors) == 0,
            "errors": errors,
            "manifest": manifest,
        }
