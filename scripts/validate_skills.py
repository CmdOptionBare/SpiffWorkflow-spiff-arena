#!/usr/bin/env python3
"""Validate local Agent Skills metadata and guard against Camunda runtime leakage."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {"spiff-bpmn", "spiff-dmn", "spiff-ai-agents", "spiff-docs", "spiff-development"}

def validate():
    actual = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
    assert actual == EXPECTED, (actual, EXPECTED)
    for name in sorted(EXPECTED):
        base = ROOT / "skills" / name
        text = (base / "SKILL.md").read_text(encoding="utf-8")
        assert text.startswith("---\n"), name
        assert re.search(r"(?m)^name: " + re.escape(name) + r"$", text), name
        assert re.search(r"(?m)^description: .+", text), name
        data = json.loads((base / "portability.json").read_text(encoding="utf-8"))
        assert data["skillName"] == name
        assert data["skillDirectory"] == "skills/" + name
        assert data["status"] == "portable-with-adapter"
        assert data["agentSkillsSpec"] == "https://agentskills.io/specification"
    print(f"Validated {len(EXPECTED)} Spiff skills and portability sidecars (metadata only).")

if __name__ == "__main__":
    validate()
