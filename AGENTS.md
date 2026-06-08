# AGENTS.md — `langgraph-playground`

This repository is a standalone LangGraph learning lab for simulated-agent experiments migrated out of a private repo.

## Scope

- Keep learning-only simulated graph experiments under `simulated_agents/<agent_name>/`.
- Keep platform-neutral skills related to these experiments under `.agents/skills/simulated-agent-*`; keep `.codex/skills/simulated-agent-*` as thin compatibility references only.
- Keep agent-pattern practice docs under `docs/agent-patterns/`; do not add personal/private-repo learning archives here.
- Do not add production API, frontend, database, auth, or deployment surfaces here unless the user explicitly changes the repo purpose.

## Simulated-agent style

Prioritize:

1. accurate implementation of the target LangGraph pattern;
2. learner readability;
3. explicit inline code over reusable wrappers;
4. small tests or examples that prove the pattern;
5. honest simulation boundaries.

It is acceptable for simulated graphs to be verbose or inconsistent with each other when that makes the pattern easier to study.

## Documentation

Each concrete simulated-agent folder should keep a README pair when present (`README.md` and `README.en.md`) semantically aligned. README files should explain:

- the pattern being practiced;
- graph shape and node responsibilities;
- key state fields;
- routing, loop limits, approvals, or stop conditions;
- what is fake/simulated;
- how to run or test the example.

Use Mermaid diagrams when they clarify graph shape or state flow.

## Settings

Use `simulated_agents.settings` for shared OpenAI knobs. Prefer `LANGGRAPH_PLAYGROUND_OPENAI_*` names for new docs and snippets. Short `PLAYGROUND_OPENAI_*` aliases may remain supported for local convenience.

## Verification

Run before claiming completion:

```bash
uv run pytest -q
uv run ruff check . --no-cache
uv run ruff format --check .
```

When changing only one simulated-agent module, also run `python -m py_compile` for the changed Python files if a full test is not warranted.
