"""Runtime configuration for standalone simulated-agent experiments."""

from __future__ import annotations

import os
from dataclasses import dataclass
from functools import lru_cache


@dataclass(frozen=True)
class Settings:
    """Small settings surface used by the learning-only simulated graphs.

    The playground intentionally keeps only the OpenAI knobs that migrated graphs use.
    Both the explicit ``LANGGRAPH_PLAYGROUND_*`` names and shorter ``PLAYGROUND_*``
    aliases are accepted for local shell snippets.
    """

    openai_model: str = "gpt-5.5"
    openai_api_key: str | None = None
    openai_timeout_seconds: float = 30.0
    openai_max_output_tokens: int = 1200

    def openai_api_key_value(self) -> str | None:
        """Return the raw API key only at the SDK boundary."""
        return self.openai_api_key


def _env(*names: str, default: str | None = None) -> str | None:
    for name in names:
        value = os.environ.get(name)
        if value is not None and value.strip():
            return value.strip()
    return default


def _env_float(*names: str, default: float) -> float:
    raw = _env(*names)
    if raw is None:
        return default
    return float(raw)


def _env_int(*names: str, default: int) -> int:
    raw = _env(*names)
    if raw is None:
        return default
    return int(raw)


@lru_cache
def get_settings() -> Settings:
    """Return cached process settings for local graph experiments."""
    return Settings(
        openai_model=_env(
            "LANGGRAPH_PLAYGROUND_OPENAI_MODEL",
            "PLAYGROUND_OPENAI_MODEL",
            default="gpt-5.5",
        )
        or "gpt-5.5",
        openai_api_key=_env(
            "OPENAI_API_KEY",
            "LANGGRAPH_PLAYGROUND_OPENAI_API_KEY",
            "PLAYGROUND_OPENAI_API_KEY",
        ),
        openai_timeout_seconds=_env_float(
            "LANGGRAPH_PLAYGROUND_OPENAI_TIMEOUT_SECONDS",
            "PLAYGROUND_OPENAI_TIMEOUT_SECONDS",
            default=30.0,
        ),
        openai_max_output_tokens=_env_int(
            "LANGGRAPH_PLAYGROUND_OPENAI_MAX_OUTPUT_TOKENS",
            "PLAYGROUND_OPENAI_MAX_OUTPUT_TOKENS",
            default=1200,
        ),
    )
