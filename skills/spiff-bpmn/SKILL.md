---
name: spiff-bpmn
description: Create, inspect, edit and validate executable BPMN 2.0 workflows for Python SpiffWorkflow and SpiffArena, including tasks, events, gateways, subprocesses, expressions and diagram interchange. Use for BPMN generation or migration away from Camunda/Zeebe.
---

# Spiff BPMN

## Preconditions
Identify the target: raw SpiffWorkflow library vs SpiffArena, its exact version, the parser/runtime and any Arena service connectors. Do not assume Camunda 8 compatibility.

## Workflow
1. Identify start and end event(s), gateways and joins, human/service/script tasks, message/timer dependencies and data shape.
2. Create ordinary BPMN 2.0 XML with unique stable IDs, correct sequence flow references and `isExecutable="true"` for executable processes. Add BPMN DI shapes and edges for diagrams intended for a BPMN.js-based editor. Only add vendor namespaces/extensions after checking Spiff target version and demonstrated parser support.
3. Model XOR branches with clearly defined conditions and a safe default where supported. Guard for absent or mistyped data. Model parallel joins explicitly when synchronization is needed. Avoid undocumented BPMN elements for the target parser.
4. Script and condition expressions are **Spiff Python expressions/scripts**, not FEEL. For example use `status == "approved"` (not `=status = "approved"`). Execution context and script-task XML encoding depend on parser configuration: verify against target source or a known-good process before emitting.
5. User tasks should integrate with the configured Arena forms/task system; service tasks with registered Python behavior or Arena service connectors. Do **not** add `zeebe:userTask`, `zeebe:taskDefinition`, `zeebe:ioMapping`, `zeebe:calledDecision`, `zeebe:script`, Camunda form IDs or element templates.
6. If referencing DMN, create a matching DMN asset and consult `spiff-dmn`. If invoking an LLM, consult `spiff-ai-agents`.
7. Validate XML, check element IDs and flow references, parse with target SpiffWorkflow's `BpmnParser` or the configured Arena parser, then execute representative branches in the actual runtime. Confirm diagrams render in Arena. Report which checks actually ran.

## Structural constraints
- XML escape characters properly; maintain valid BPMN element order per schema.
- Include `bpmndi:BPMNDiagram` and diagram shapes/edges when graphical editing is required; a parsable non-visual BPMN file is not necessarily usable in the Arena editor.
- Never claim `c8ctl bpmn lint` proves Spiff execution. Generic BPMN lint is supplementary, not sufficient.
- Some standard BPMN constructs are only partially implemented in specific Spiff versions. Confirm support rather than silently omitting behavior.

## Verification example (illustrative, adapt to project)
```python
from SpiffWorkflow.bpmn.parser.BpmnParser import BpmnParser
parser = BpmnParser()
parser.add_bpmn_file("process.bpmn")
# Next: retrieve the selected process and run tests with your installed Spiff version.
```

## References
- https://github.com/sartography/SpiffWorkflow/tree/main/SpiffWorkflow/bpmn/parser
- https://spiff.works/docs/spiffworkflow/
- https://spiff.works/docs/spiff-arena/

Original inspiration: https://github.com/camunda/skills/tree/main/skills/camunda-bpmn
