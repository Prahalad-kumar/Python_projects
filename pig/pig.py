import random

# ANSI color codes for a friendlier CLI (works on most Linux/macOS terminals)
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RED = '\033[91m'
RESET = '\033[0m'


def roll():
    """Return a random die roll between 1 and 6."""
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)


def print_title(max_score):
    print(CYAN + "🐖  Welcome to Pig — the Dice Game!  🐖" + RESET)
    print(f"First to reach {YELLOW}{max_score}{RESET} points wins. Good luck!\n")


def print_scoreboard(scores):
    print('\n' + GREEN + 'Scoreboard:' + RESET)
    for idx, s in enumerate(scores, start=1):
        print(f"  Player {idx}: {YELLOW}{s}{RESET}")
    print()


def get_num_players():
    while True:
        players = input("Enter number of players (2-4): ").strip()
        if players.isdigit():
            players = int(players)
            if 2 <= players <= 4:
                return players
            else:
                print(RED + "Please choose between 2 and 4 players." + RESET)
        else:
            print(RED + "Invalid input. Enter a number (2-4)." + RESET)


def prompt_choice():
    """Ask the player for an action and normalize the response."""
    while True:
        choice = input("Roll or Hold? (r/h) — or 'q' to quit: ").lower().strip()
        if choice in ('r', 'roll'):
            return 'r'
        if choice in ('h', 'hold'):
            return 'h'
        if choice in ('q', 'quit'):
            return 'q'
        print(RED + "Invalid input. Type 'r' to roll, 'h' to hold, or 'q' to quit." + RESET)


def main():
    max_score = 50
    print_title(max_score)

    players = get_num_players()
    players_scores = [0] * players
    print_scoreboard(players_scores)

    game_over = False

    while not game_over:
        for i in range(players):
            print(f"{CYAN}➡️  Player {i+1}'s turn{RESET}")
            turn_score = 0

            while True:
                choice = prompt_choice()
                if choice == 'q':
                    print(RED + "Game aborted by user. Goodbye!" + RESET)
                    return

                if choice == 'r':
                    roll_value = roll()
                    print(f"You rolled a {YELLOW}{roll_value}{RESET}")
                    if roll_value == 1:
                        print(RED + "💥 Rolled a 1! Turn over, no points earned." + RESET)
                        turn_score = 0
                        break
                    else:
                        turn_score += roll_value
                        potential = players_scores[i] + turn_score
                        print(f"Turn score: {GREEN}{turn_score}{RESET} — if held, total would be: {YELLOW}{potential}{RESET}")

                elif choice == 'h':
                    players_scores[i] += turn_score
                    print(f"{GREEN}✅ Player {i+1} banks {turn_score} points. Total: {YELLOW}{players_scores[i]}{RESET}")
                    if players_scores[i] >= max_score:
                        print(f"\n{CYAN}🏆 Player {i+1} wins with a score of {YELLOW}{players_scores[i]}{CYAN}! 🏆{RESET}\n")
                        game_over = True
                    break

            print_scoreboard(players_scores)
            if game_over:
                break

    # Final summary (in case of ties, show the highest scorer(s))
    max_score_value = max(players_scores)
    winners = [i + 1 for i, s in enumerate(players_scores) if s == max_score_value]
    if len(winners) == 1:
        print(f"{GREEN}🎉 Congratulations Player {winners[0]}! Final score: {YELLOW}{max_score_value}{RESET}")
    else:
        print(f"{GREEN}🎉 It's a tie between players {', '.join(map(str, winners))}! Final score: {YELLOW}{max_score_value}{RESET}")


if __name__ == '__main__':
    main()
