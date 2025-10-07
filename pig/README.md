
# Pig — Dice Game

Simple command-line implementation of the classic dice game Pig. This program supports 2–4 players and plays until a player reaches 50 points.

## Rules

- Players take turns rolling a single six-sided die.
- On a player's turn they may repeatedly choose to 'Roll' or 'Hold'.
- If the player rolls a 1, their turn ends immediately and they score 0 points for that turn.
- If the player rolls 2–6, the rolled value is added to their _turn total_. They may then choose to roll again or hold.
- If the player chooses to 'Hold', the current turn total is added to their overall score and their turn ends.
- The first player whose overall score reaches or exceeds 50 points wins the game.

## How to run

From the `pig` folder run:

```bash
python3 pig.py
```

Follow the interactive prompts to pick the number of players and to roll/hold each turn.

## Notes

- You can press `q` during a turn to quit the game early.
- The command-line UI includes simple colors and emoji for a friendlier experience. If colors don't render correctly, your terminal may not support ANSI color codes.

Enjoy! 🎲🐷
