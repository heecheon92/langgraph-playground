"""Tests for shared simulated-agent runtime settings."""

from __future__ import annotations

from collections.abc import Iterator

import pytest

from simulated_agents.settings import get_settings


@pytest.fixture(autouse=True)
def clear_settings_cache() -> Iterator[None]:
    get_settings.cache_clear()
    yield
    get_settings.cache_clear()


def test_playground_openai_aliases_are_accepted(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("LANGGRAPH_PLAYGROUND_OPENAI_MODEL", raising=False)
    monkeypatch.delenv("LANGGRAPH_PLAYGROUND_OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("LANGGRAPH_PLAYGROUND_OPENAI_TIMEOUT_SECONDS", raising=False)
    monkeypatch.delenv("LANGGRAPH_PLAYGROUND_OPENAI_MAX_OUTPUT_TOKENS", raising=False)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)

    monkeypatch.setenv("PLAYGROUND_OPENAI_MODEL", "gpt-test-alias")
    monkeypatch.setenv("PLAYGROUND_OPENAI_API_KEY", "sk-playground")
    monkeypatch.setenv("PLAYGROUND_OPENAI_TIMEOUT_SECONDS", "12.5")
    monkeypatch.setenv("PLAYGROUND_OPENAI_MAX_OUTPUT_TOKENS", "333")

    settings = get_settings()

    assert settings.openai_model == "gpt-test-alias"
    assert settings.openai_api_key == "sk-playground"
    assert settings.openai_timeout_seconds == 12.5
    assert settings.openai_max_output_tokens == 333


def test_langgraph_playground_names_take_precedence(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("LANGGRAPH_PLAYGROUND_OPENAI_MODEL", "gpt-preferred")
    monkeypatch.setenv("PLAYGROUND_OPENAI_MODEL", "gpt-alias")
    monkeypatch.setenv("LANGGRAPH_PLAYGROUND_OPENAI_TIMEOUT_SECONDS", "20")
    monkeypatch.setenv("PLAYGROUND_OPENAI_TIMEOUT_SECONDS", "10")
    monkeypatch.setenv("LANGGRAPH_PLAYGROUND_OPENAI_MAX_OUTPUT_TOKENS", "2000")
    monkeypatch.setenv("PLAYGROUND_OPENAI_MAX_OUTPUT_TOKENS", "1000")

    settings = get_settings()

    assert settings.openai_model == "gpt-preferred"
    assert settings.openai_timeout_seconds == 20.0
    assert settings.openai_max_output_tokens == 2000
