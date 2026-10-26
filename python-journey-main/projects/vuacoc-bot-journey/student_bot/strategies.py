"""Small, deterministic strategies for the course-local Line Arena."""

from __future__ import annotations

REQUIRED_FIELDS = (
    "position",
    "opponent_position",
    "goal",
    "min_position",
    "max_position",
)


def _validated_state(state: dict[str, int]) -> tuple[int, int, int, int, int]:
    """Read the fields used by strategies and reject malformed state early."""
    if not isinstance(state, dict):
        raise ValueError("state must be a dictionary")

    missing = [key for key in REQUIRED_FIELDS if key not in state]
    if missing:
        raise ValueError(f"state is missing required field(s): {', '.join(missing)}")

    values = [state[key] for key in REQUIRED_FIELDS]
    if any(type(value) is not int for value in values):
        raise ValueError("position, opponent_position, goal and bounds must be integers")

    position = state["position"]
    opponent_position = state["opponent_position"]
    goal = state["goal"]
    minimum = state["min_position"]
    maximum = state["max_position"]

    if minimum > maximum:
        raise ValueError("min_position cannot be greater than max_position")

    for name, value in (
        ("position", position),
        ("opponent_position", opponent_position),
        ("goal", goal),
    ):
        if not minimum <= value <= maximum:
            raise ValueError(f"{name} must be between min_position and max_position")

    return position, opponent_position, goal, minimum, maximum


def _move_toward(position: int, goal: int) -> str:
    """Return the one-step action that moves toward a goal."""
    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"


def balanced_strategy(state: dict[str, int]) -> str:
    """Move toward the goal; wait only after reaching it."""
    position, _, goal, _, _ = _validated_state(state)
    return _move_toward(position, goal)


def cautious_strategy(state: dict[str, int]) -> str:
    """Demonstration strategy: pause when the opponent is one step away."""
    position, opponent_position, goal, _, _ = _validated_state(state)
    if position == goal:
        return "wait"
    if abs(position - opponent_position) <= 1:
        return "wait"
    return _move_toward(position, goal)
