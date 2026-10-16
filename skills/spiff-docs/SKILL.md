---
name: spiff-docs
description: Find and verify version-appropriate SpiffWorkflow and SpiffArena documentation or source implementation details before creating BPMN, DMN, service connector configurations and process integrations.
---

# Spiff documentation research

## Preferred sources
1. Official SpiffWorkflow docs: https://spiff.works/docs/spiffworkflow/
2. SpiffArena docs: https://spiff.works/docs/spiff-arena/
3. SpiffWorkflow source: https://github.com/sartography/SpiffWorkflow
4. SpiffArena source: https://github.com/sartography/spiff-arena

## Retrieval procedure
- Determine installed package/repository commit and whether a feature is from the library or Arena.
- Search official documentation by exact feature name. If docs are absent or old, inspect source, tests, config and examples for that version. Cite file path, code symbol and commit/branch where possible.
- Read the relevant sections, not only search snippets. Distinguish documented contract from inferred behavior and from untested examples.
- For sensitive integrations, verify auth boundaries, connector secrets and expected payload shapes in source.
- If a relevant answer is unverified, say so; never invent a `spiffctl` CLI, an official Spiff MCP endpoint, `c8ctl` equivalents or deployment API endpoints.

## Handoff
Use `spiff-bpmn`, `spiff-dmn`, `spiff-ai-agents` or `spiff-development` for implementation tasks after retrieval.

Camunda docs can be consulted for general BPMN comparisons, but must **not** be treated as authoritative for Spiff execution.

Original inspiration: https://github.com/camunda/skills/tree/main/skills/camunda-docs
