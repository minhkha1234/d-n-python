# Student Bot

Week 15 implementation keeps the arena's simple function interface while
making the decision strategy replaceable.

- `bot.py`: exposes `choose_action(state)` and the small `Bot` composition class.
- `strategies.py`: validates the state and provides a goal-directed default
  strategy plus a cautious comparison strategy.
- `../tests/test_student_bot_strategies.py`: tests normal movement, boundary
  behavior, malformed state and strategy injection.

> This is a Python Journey teaching contract. It is not the production
> contract of vuacoc.com.

## Interface

```python
def choose_action(state: dict[str, int]) -> str:
    ...
```

The arena passes a dictionary containing the bot's position, opponent position,
goal and position bounds. The allowed actions are `left`, `right` and `wait`.
The default strategy moves one step toward the goal and waits after reaching it.
Malformed state raises a clear `ValueError`, which can be diagnosed in tests.

## Strategy composition

```python
from student_bot.bot import Bot
from student_bot.strategies import cautious_strategy

bot = Bot(strategy=cautious_strategy)
```

The bot core does not need to change when a different strategy is injected.
The cautious strategy is a teaching example: pausing near an opponent may waste
turns in this simplified model.

## Run

From the repository root, use:

```bash
cd projects/vuacoc-bot-journey
python -m student_bot.bot
python local_arena/tournament_cli.py
python -m pytest tests -q
```

Read `../local_arena/CONTRACT.md` before relying on state fields or actions.
This local contract is not the production VuaCóc schema.

> Local Arena is not a security sandbox. Do not run untrusted Python code.
