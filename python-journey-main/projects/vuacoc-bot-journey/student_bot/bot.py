"""Student bot with an injectable strategy for the course-local Line Arena."""

from collections.abc import Callable

from .strategies import balanced_strategy

Strategy = Callable[[dict[str, int]], str]


class Bot:
    """A small bot that delegates decisions to a supplied strategy."""

    def __init__(self, strategy: Strategy = balanced_strategy) -> None:
        self.strategy = strategy

    def choose_action(self, state: dict[str, int]) -> str:
        """Return the action chosen by the configured strategy."""
        return self.strategy(state)


_default_bot = Bot()


def choose_action(state: dict[str, int]) -> str:
    """Keep the arena's function interface while using the default bot."""
    return _default_bot.choose_action(state)


def main() -> None:
    """Run one small example so the bot can be smoke-tested directly."""
    teaching_state = {
        "turn": 1,
        "max_turns": 6,
        "position": 0,
        "opponent_position": 4,
        "goal": 4,
        "min_position": 0,
        "max_position": 4,
    }
    print(choose_action(teaching_state))


if __name__ == "__main__":
    main()
