# Week 15 — Capstone report

## 1. Problem and scope

Build a deterministic Python bot that chooses a legal action in the course-local Line Arena. The bot receives a state dictionary and returns `left`, `right` or `wait`.

**In scope:** goal-directed decisions, state validation, strategy composition, automated tests, local tournament evaluation and README documentation.

**Out of scope:** connecting to the real VuaCóc service, production API compatibility, network access, authentication, machine learning and advanced search algorithms.

## 2. Main features

1. Choose a one-step action toward the goal.
2. Wait when already at the goal.
3. Reject malformed state with a clear `ValueError`.
4. Inject a different strategy into `Bot` without rewriting the bot core.
5. Compare the default bot with WaitBot, ForwardBot and CautiousBot in both A/B seats.
6. Report match outcome, completion rate, legal-action rate and known failures separately.

## 3. Design decisions

- Use a dictionary because the arena already supplies named state fields.
- Use small functions for state validation and action selection.
- Use composition: `Bot(strategy)` delegates decisions to the selected callable.
- Keep the default strategy deterministic and goal-directed.
- Keep the cautious strategy as a teaching comparison. In this local model, pausing near an opponent may waste turns; it is not automatically a better strategy.
- Do not claim that the local model is compatible with the real VuaCóc runtime.

## 4. Tests and evidence

Run from the repository root:

```bash
python -m pytest projects/vuacoc-bot-journey/tests -q
python projects/vuacoc-bot-journey/local_arena/tournament_cli.py
```

The tests cover normal movement, goal reached, cautious behavior, strategy injection, malformed state and tournament metrics.

Record the actual command output from your machine here before submission. Do not report a test as passing unless you have run it.

## 5. Known limitations

- The Line Arena is a small educational model, not the full VuaCóc game.
- Cautious behavior can stall when both bots repeatedly pause near each other.
- The bot uses fixed rules; it does not learn from previous matches.
- Results from the local tournament are educational evidence, not a production rating.

## 6. Demo plan (5–8 minutes)

1. Explain the problem and the three legal actions.
2. Show `student_bot/strategies.py` and explain how position and goal determine an action.
3. Show how `Bot(strategy=...)` lets us replace a strategy.
4. Run the tests and local tournament.
5. Explain one edge case and the cautious strategy's trade-off.
6. State the limitations honestly.
