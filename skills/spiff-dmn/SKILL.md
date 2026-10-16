---
name: spiff-dmn
description: Author, review and test SpiffWorkflow DMN decision tables, rules, hit policies, input and output expressions using Spiff's Python expression environment. Use when creating DMN assets for executable Spiff BPMN business decisions.
---

# Spiff DMN

Camunda's DMN skill assumes Camunda's FEEL evaluator, hit policy matrix, Zeebe decision bindings and test framework. **None of those are a safe execution contract for Spiff.**

## Workflow
1. Check the exact target parser. The upstream `SpiffWorkflow/dmn/parser/DMNParser.py` describes limitations, including a single decision table per decision in the inspected code. Do not assume full DMN/DRD specification support.
2. Start with a simple standalone decision table, stable `decision` and table IDs, explicit input/output names and types. Use existing DMN from the target Arena project as XML reference; avoid Camunda-specific DMN namespace or vendor extensions.
3. Use **Python-compatible expressions** in the Spiff execution environment (example `customer_total > 1000` and `status == "active"`). Do not use FEEL syntax such as `=status = "active"`, `if x then y else z`, `fromAi()` or FEEL unary-test grammar without confirming explicit support.
4. Verify available hit policies and aggregators in the installed `SpiffWorkflow/dmn/specs` and evaluator before generating a policy. Do not borrow Camunda's `UNIQUE`, `FIRST`, `COLLECT` semantics as a guarantee.
5. Reference the decision from a BPMN business-rule task using the target Spiff parser's conventions; do not use `<zeebe:calledDecision>`.
6. Validate DMN XML, parse via the installed DMN/BPMN parser, exercise matching, non-matching, multiple-match and null-input examples. Assert actual output names/types.
7. State limitations and untested cases clearly; a general-purpose `dmnlint` pass is not a Spiff runtime test.

## Source checks
- https://github.com/sartography/SpiffWorkflow/blob/main/SpiffWorkflow/dmn/parser/DMNParser.py
- https://github.com/sartography/SpiffWorkflow/tree/main/SpiffWorkflow/dmn/specs
- https://spiff.works/docs/spiffworkflow/

Original inspiration: https://github.com/camunda/skills/tree/main/skills/camunda-dmn
