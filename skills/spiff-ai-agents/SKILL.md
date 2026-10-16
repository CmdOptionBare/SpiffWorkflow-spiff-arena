---
name: spiff-ai-agents
description: Design and implement LLM-assisted workflows and tool interactions orchestrated by SpiffWorkflow and SpiffArena, with explicit tool schemas, approvals, failure handling and process state. Use for agentic BPMN design, not for Camunda AI Agent connectors.
---

# AI agents with Spiff

A BPMN ad-hoc subprocess is **not by itself an LLM agent**. Camunda's AI Agent Sub-process connector, `fromAi()`, `toolCallResult`, model-call limits, provider templates and secret references are specific to Camunda's runtime. Do not insert them in Spiff diagrams.

## Architecture
- **Host/agent runtime:** the actual LLM runner; owns prompts, model selection, turn state and tool-call loop.
- **SpiffWorkflow:** orchestrates steps, branches, data and human tasks.
- **SpiffArena:** process management/UI plus configured service connectors.
- **Tool adapter:** controlled interface between BPMN service tasks and the LLM or other services, implemented in your installed Arena/Python stack.

## Workflow
1. Specify who owns agent decisions: an external agent called by a process service task, or an agent host that calls Arena/process APIs. Choose one; a diagram is not a substitute for a runner.
2. Define typed JSON inputs/outputs for each tool, along with timeouts, idempotency keys, errors and permission boundaries. Validate model-supplied arguments in deterministic code.
3. Use a registered Arena service connector or supported Python integration to invoke the model/tool adapter; verify the exact connector interface from target source. **Do not fabricate** a built-in Spiff AI connector.
4. Store process variables and durable state in the platform; keep provider credentials in a host secret manager, never in BPMN XML, logs or prompt text.
5. Model bounded retries, timeouts, compensation or BPMN incidents as appropriate; require explicit user approval before irreversible external actions, including sending communications or modifying records.
6. For multi-turn agents, define a stable conversation/process correlation identifier and own memory/context in a scoped external store. Distinguish tool output (untrusted data) from policy instructions.
7. Test success, malformed model output, authorization failure, timeout, missing tool, rejected approval and retry idempotence using the deployed version.

## Model-to-tool contract
```json
{
  "tool": "lookup_customer",
  "arguments": {"customer_id": "123"},
  "correlation_id": "process-instance-id"
}
```
This is **an example application contract**, not a built-in Spiff payload.

## Source checks
- https://github.com/sartography/spiff-arena
- https://spiff.works/docs/spiff-arena/
- https://github.com/sartography/SpiffWorkflow

Original inspiration: https://github.com/camunda/skills/tree/main/skills/camunda-ai-agents
