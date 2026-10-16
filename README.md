# SpiffWorkflow + SpiffArena Agent Skills

Five original, Spiff-targeted [Agent Skills](https://agentskills.io/specification) adapted from the *concepts* in [Camunda's open-source skills](https://github.com/camunda/skills). These are not a drop-in Zeebe compatibility layer.

| Skill | Focus |
|---|---|
| [spiff-bpmn](skills/spiff-bpmn/SKILL.md) | BPMN 2.0 modeling, Python expressions, Spiff parser validation |
| [spiff-dmn](skills/spiff-dmn/SKILL.md) | Decision tables, Python expressions, conservative feature support |
| [spiff-ai-agents](skills/spiff-ai-agents/SKILL.md) | Agent/tool boundaries, human approval, explicit external orchestration |
| [spiff-docs](skills/spiff-docs/SKILL.md) | Source-first SpiffWorkflow / Arena documentation lookup |
| [spiff-development](skills/spiff-development/SKILL.md) | Routing to Python code, Arena service connectors and integrations |

## Install

Copy the folders under `skills/` to the skills directory your agent host actually discovers (for example `.agents/skills/` in a compatible configuration). A skills directory alone does **not** make SpiffArena a skill runner. Your LLM host needs skill discovery, file access, and execution tools. Never give model prompts broad credentials merely because a skill asks to operate an external service.

## Compatibility

BPMN/DMN standard ideas carry over; Camunda Zeebe extensions, c8ctl commands, FEEL syntax, connector element templates, Camunda Form JSON, Java job workers, and Camunda AI Agent Sub-process runtime do not. SpiffWorkflow supports Python-script workflows and its own parser/execution semantics. SpiffArena has service connectors, BPMN extensions, and UI/runtime conventions that must be verified against the installed version.

All skills are conservative: inspect the target version/source; distinguish structural XML validation from executable compatibility; test with the actual Spiff runtime; and mark unverified integrations as unverified.

## Portability metadata

Each `portability.json` is an **informational sidecar** for this project, not an Agent Skills standard field or an executable adapter. It documents prerequisites and what is intentionally unsupported. The runtime discovers `SKILL.md`, not these files.

## Local validation

```sh
python scripts/validate_skills.py
# For actual generated BPMN/DMN, use the project's installed SpiffWorkflow parser
# and Arena deployment/runtime tests; metadata checks do not prove execution.
```

## Sources and attribution

- [Camunda Skills](https://github.com/camunda/skills) — conceptual inspiration (original instructions rewritten for Spiff; not copied wholesale)
- [SpiffWorkflow source](https://github.com/sartography/SpiffWorkflow) and [documentation](https://spiff.works/docs/spiffworkflow/)
- [SpiffArena source](https://github.com/sartography/spiff-arena) and [documentation](https://spiff.works/docs/spiff-arena/)
- [Agent Skills specification](https://agentskills.io/specification)

These skills are educational development tooling. No production compatibility or runtime execution was established by merely publishing these files.
