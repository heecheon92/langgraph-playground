# Agent pattern practice catalog overview

Use `README.md` as the primary index. Load individual files under `patterns/` only after selecting a pattern.

Core progression:

1. Basic state graph
2. Conditional routing
3. Tool-calling router and agent loop
4. State reducers and parallel merge rules
5. Public/private/input/output schemas
6. Message trimming and summarization
7. Human-in-the-loop interrupt and approval
8. Command routing
9. Time travel, replay, and state editing
10. Fixed parallelization
11. Dynamic map-reduce with Send
12. Subgraphs and bridge nodes
13. Persona workers and research panel
14. Long-term memory and profile updates
15. Runtime and double-texting policy
16. Prompt chaining and quality gates
17. Evaluator-optimizer loop
18. Supervisor and subagents
19. Handoff network
20. Streaming and observability
21. Tool-skill-workflow-agent escalation

Pattern families:

- 1-6: state, routing, messages, and interface boundaries
- 7-9: human control, dynamic routing, checkpoint timelines
- 10-13: fan-out, map-reduce, subgraphs, persona workers
- 14-15: memory and runtime policy
- 16-17: LLM workflow quality patterns
- 18-21: multi-agent architecture and abstraction selection

Recommended next-build order is documented in `README.md`.
