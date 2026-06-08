---
created: 2026-05-18
updated: 2026-06-08
status: active
topics:
  - langgraph
  - simulated-agents
  - pattern-catalog
related_code:
  - simulated_agents/
---

# Pattern 7: Human-in-the-loop interrupt and approval

[Back to agent pattern index](../README.md)

**Difficulty:** Intermediate

## What this pattern is

Human-in-the-loop graphs pause execution so a person can approve, reject, edit, or provide missing information. In LangGraph, dynamic `interrupt()` pauses inside a node; static breakpoints pause before or after configured nodes. Both need checkpointed state if execution should resume safely.

This pattern is for meaningful decision points: risky tools, expensive actions, missing required data, or quality gates.

## Flowchart

```mermaid
flowchart TD
    Start([START]) --> Draft[draft_action]
    Draft --> Review[interrupt: ask human]
    Review --> Decision{resume value}
    Decision -->|approve| Execute[fake_execute]
    Decision -->|edit| Revise[revise_with_feedback]
    Decision -->|reject| Cancel[cancel]
    Revise --> Review
    Execute --> End([END])
    Cancel --> End
```

## Interrupt sequence

```mermaid
sequenceDiagram
    participant Caller
    participant Graph
    participant Node as approval_node
    participant Human
    participant Checkpointer

    Caller->>Graph: invoke(input, thread_id)
    Graph->>Node: run node
    Node->>Checkpointer: save state at interrupt
    Node-->>Caller: interrupt payload
    Caller->>Human: show pending action
    Human-->>Caller: approve/edit/reject
    Caller->>Graph: Command(resume=value), same thread_id
    Graph->>Node: restart node and inject resume value
    Node-->>Graph: state update
```

## State contract

```python
from typing import Literal
from typing_extensions import NotRequired, TypedDict

class State(TypedDict):
    request: str
    draft: NotRequired[str]
    human_decision: NotRequired[Literal["approve", "edit", "reject"]]
    human_feedback: NotRequired[str]
    revision_count: NotRequired[int]
    final_result: NotRequired[str]
```

## What to practice

- Use JSON-serializable interrupt payloads.
- Resume with the same `thread_id`; it is the persistent cursor.
- Keep interrupt calls in stable order inside a node.
- Remember that the node restarts from the beginning after resume.
- Add a maximum revision count for loops.

## Common mistakes

- Wrapping `interrupt()` in broad `try/except`, which can swallow the pause signal.
- Performing side effects before asking for approval.
- Using interruption for every minor step, making the graph unusable.
- Continuing silently without storing the human decision in state.

## Simulated-agent idea seeds

### Editor-in-Chief Review Loop

Generate a draft, pause for human review, revise on feedback, or publish on approval.

### Risky Tool Approval Agent

Prepare a fake action such as “send email” or “delete file,” pause for approval, then either execute a fake tool or cancel.

### Missing Info Interviewer

Pause until required fields are complete and valid, then proceed.

## Smallest deterministic version

Draft a fake newsletter title, interrupt for approval, and either publish, revise once, or cancel.

## How the bootstrap skill should use this file

When this pattern is selected, the bootstrap skill should turn the graph shape, state contract, and smallest deterministic exercise into the per-agent README pair. Keep the first scaffold offline and simulated. Add real model calls only after the learner can explain the deterministic version.

## Revision history

- 2026-06-08: Expanded into a descriptive, pattern-accurate guide with diagrams and implementation cautions.
- 2026-05-18: Split from the original monolithic candidate-materials note.
