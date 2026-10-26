"""Tests for Week 15 bot strategies and strategy composition."""

import pytest

from student_bot.bot import Bot, choose_action
from student_bot.strategies import balanced_strategy, cautious_strategy

STATE = {
    "turn": 1,
    "max_turns": 6,
    "position": 0,
    "opponent_position": 4,
    "goal": 4,
    "min_position": 0,
    "max_position": 4,
}


def test_balanced_strategy_moves_right_toward_goal() -> None:
    assert balanced_strategy(STATE) == "right"


def test_balanced_strategy_moves_left_toward_goal() -> None:
    state = {**STATE, "position": 4, "goal": 0}
    assert balanced_strategy(state) == "left"


def test_balanced_strategy_waits_after_reaching_goal() -> None:
    state = {**STATE, "position": 4, "goal": 4}
    assert balanced_strategy(state) == "wait"


def test_cautious_strategy_waits_when_opponent_is_near() -> None:
    state = {**STATE, "position": 2, "opponent_position": 3, "goal": 4}
    assert cautious_strategy(state) == "wait"


def test_cautious_strategy_moves_when_opponent_is_far() -> None:
    state = {**STATE, "position": 1, "opponent_position": 4, "goal": 4}
    assert cautious_strategy(state) == "right"


def test_bot_accepts_a_strategy_without_changing_its_core() -> None:
    def wait_strategy(state: dict[str, int]) -> str:
        return "wait"

    bot = Bot(strategy=wait_strategy)
    assert bot.choose_action(STATE) == "wait"


def test_public_interface_uses_balanced_strategy() -> None:
    assert choose_action(STATE) == balanced_strategy(STATE)


def test_invalid_position_is_rejected() -> None:
    state = {**STATE, "position": 99}
    with pytest.raises(ValueError, match="position must be between"):
        balanced_strategy(state)


def test_missing_state_field_is_rejected() -> None:
    state = {key: value for key, value in STATE.items() if key != "goal"}
    with pytest.raises(ValueError, match="missing required field"):
        balanced_strategy(state)


def test_non_integer_state_is_rejected() -> None:
    state = {**STATE, "position": True}
    with pytest.raises(ValueError, match="must be integers"):
        balanced_strategy(state)
