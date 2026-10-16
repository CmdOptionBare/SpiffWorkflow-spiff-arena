---
name: spiff-development
description: Choose and implement the correct SpiffWorkflow/SpiffArena integration boundary—Python script behavior, existing Arena service connectors, external APIs, background processing or an LLM adapter—before changing an executable BPMN process.
---

# Spiff integration development

This is the decision/router skill for cross-system calls. Camunda's out-of-the-box connector / Java SDK / Zeebe worker matrix is **not valid** for Spiff.

## Decision procedure
1. Is the task pure deterministic calculation or decision logic, bounded in execution time? Use supported Spiff script expression/task or DMN; check sandbox and available execution environment. Delegate to `spiff-bpmn` or `spiff-dmn`.
2. Is it an HTTP/API or third-party service integration already supported by the target Arena service connector catalog? Prefer the existing connector, verify its schema, input mappings, auth and timeouts from installed Arena docs/source.
3. Does it require custom Python behavior, multiple calls or a proprietary protocol? Build a narrow Python service/integration adapter with explicit input/output contracts and expose through a supported Arena connector or worker architecture verified in the installed version.
4. Does it need long-running asynchronous work, polling, webhook ingestion or heavy processing? Separate execution into an appropriate authenticated service/queue and use Arena-supported start/event/callback paths. Do not assume Camunda's webhook connector or Zeebe job activation.
5. Is a model choosing tools or generating arguments? Consult `spiff-ai-agents`; keep LLM calls and side effects behind explicit authorization and validation.

## Delivery checklist
- Declare interface, authentication identity, authorization, secret location and least privileges.
- Specify side effects, idempotency key, retry/timeout behavior, status/error formats, observability and compensation.
- Model the correct BPMN task/event and mappings for the **target version**, not a generic sample.
- Test adapter contracts, run BPMN/DMN parse checks, execute end-to-end in the configured SpiffArena environment.
- Do not claim deployment, working connectors or runtime compatibility until observed.

## Source checks
- https://spiff.works/docs/spiff-arena/
- https://github.com/sartography/spiff-arena
- https://github.com/sartography/SpiffWorkflow

Original inspiration: https://github.com/camunda/skills/tree/main/skills/camunda-development
