"""Exercise 02: compose Bot with a strategy."""

from collections.abc import Callable
from typing import TypedDict


class State(TypedDict):
    position: int
    goal: int


Strategy = Callable[[State], str]


def movement(position: int, goal: int) -> str:
    """Choose a movement action that works for goals on either side."""
    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"


def defensive(state: State) -> str:
    """Prefer waiting when the goal is more than one step away."""
    distance = abs(state["goal"] - state["position"])
    if distance > 1:
        return "wait"
    return movement(state["position"], state["goal"])


def balanced(state: State) -> str:
    """Move toward the goal, or wait when already there."""
    return movement(state["position"], state["goal"])


def aggressive(state: State) -> str:
    """Always choose movement toward the goal when not already there."""
    return movement(state["position"], state["goal"])


class Bot:
    """A bot whose behavior can be changed by supplying a strategy."""

    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def choose_action(self, state: State) -> str:
        """Delegate the decision to the configured strategy."""
        return self.strategy(state)


def main() -> None:
    """Demonstrate swapping strategies without changing Bot."""
    state: State = {"position": 1, "goal": 4}

    for name, strategy in (
        ("defensive", defensive),
        ("balanced", balanced),
        ("aggressive", aggressive),
    ):
        bot = Bot(strategy)
        print(f"{name}: {bot.choose_action(state)}")

    print(f"goal=0: {movement(position=1, goal=0)}")
    print(f"goal=4: {movement(position=1, goal=4)}")


if __name__ == "__main__":
    main()
