"""Exercise 01: imports, modules and main guard."""

from bot_course.core import choose_action


def main() -> None:
    """Import and use the bot decision function."""
    position = 1
    goal = 4

    action = choose_action(position, goal)
    print(action)


if __name__ == "__main__":
    main()
