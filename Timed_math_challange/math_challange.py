import random
import time
import sys
import os
import operator

OPERATORS = ['+', '-', '*', '%', '//']
OP_FUNCS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '%': operator.mod,
    '//': operator.floordiv,
}

MIN_VALUE = 1
MAX_VALUE = 20
TOTAL_PROBLEM = 10


try:
    from colorama import init as _init_colorama
    from colorama import Fore, Style
    _init_colorama(autoreset=True)
except Exception:
    # Minimal ANSI fallback
    class Fore:
        GREEN = '\033[32m'
        CYAN = '\033[36m'
        YELLOW = '\033[33m'
        RED = '\033[31m'
        MAGENTA = '\033[35m'
        RESET = '\033[39m'

    class Style:
        BRIGHT = '\033[1m'
        RESET_ALL = '\033[0m'


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def colored(text, color):
    return f"{color}{text}{Style.RESET_ALL}"


def generate_problem():
    left = random.randint(MIN_VALUE, MAX_VALUE)
    right = random.randint(MIN_VALUE, MAX_VALUE)
    op = random.choice(OPERATORS)
    # ensure no division/mod by zero (MIN_VALUE is 1 so safe)
    expr = f"{left} {op} {right}"
    # compute answer using safe mapping
    ans = OP_FUNCS[op](left, right)
    return expr, ans


def read_enter_to_continue(prompt="Press Enter to start"):
    try:
        input(colored(prompt + '...', Fore.CYAN))
    except KeyboardInterrupt:
        print('\n' + colored('Interrupted. Exiting.', Fore.RED))
        sys.exit(1)


def main():
    clear_screen()
    print(colored('\nTimed Math Challenge', Fore.MAGENTA + Style.BRIGHT))
    print(colored('Solve a set of math problems as quickly and accurately as you can!\n', Fore.YELLOW))

    print(colored(f'Problems: {TOTAL_PROBLEM}  Range: {MIN_VALUE}-{MAX_VALUE}\n', Fore.CYAN))
    read_enter_to_continue()

    # short countdown
    for s in range(3, 0, -1):
        print(colored(f'Starting in {s}...', Fore.YELLOW))
        time.sleep(1)
    clear_screen()

    wrong_attempts = 0
    attempts = 0
    start_time = time.time()
    times = []

    try:
        for i in range(TOTAL_PROBLEM):
            expr, answer = generate_problem()
            print(colored(f'Problem #{i+1}/{TOTAL_PROBLEM}', Fore.MAGENTA + Style.BRIGHT))
            print(colored(f'  {expr} = ?', Fore.CYAN))

            q_start = time.time()
            per_q_wrong = 0
            while True:
                guess = input(colored('Your answer (or type "skip"): ', Fore.GREEN)).strip()
                attempts += 1
                if guess.lower() == 'skip':
                    print(colored(f'Skipped. Correct answer was: {answer}', Fore.YELLOW))
                    break
                # validate numeric input (integers expected)
                try:
                    g = int(guess)
                except ValueError:
                    print(colored('Please enter an integer or "skip".', Fore.RED))
                    per_q_wrong += 1
                    wrong_attempts += 1
                    continue

                if g == answer:
                    elapsed = round(time.time() - q_start, 2)
                    times.append(elapsed)
                    print(colored(f'Correct! (+)  Time: {elapsed}s\n', Fore.GREEN))
                    break
                else:
                    per_q_wrong += 1
                    wrong_attempts += 1
                    print(colored('Incorrect — try again.', Fore.RED))
                    # offer hint after 2 wrong attempts
                    if per_q_wrong == 2:
                        hint = 'even' if answer % 2 == 0 else 'odd'
                        print(colored(f'Hint: the answer is {hint}.', Fore.YELLOW))

    except KeyboardInterrupt:
        print('\n' + colored('Interrupted. Showing progress so far...', Fore.RED))

    end_time = time.time()
    total_time = round(end_time - start_time, 2)

    clear_screen()
    print(colored('RESULTS', Fore.MAGENTA + Style.BRIGHT))
    print(colored('-' * 40, Fore.MAGENTA))
    solved = len(times)
    avg = round(sum(times) / solved, 2) if solved else 0
    accuracy = round(((TOTAL_PROBLEM - wrong_attempts) / (TOTAL_PROBLEM if TOTAL_PROBLEM else 1)) * 100, 2)

    print(colored(f'Total problems: {TOTAL_PROBLEM}', Fore.CYAN))
    print(colored(f'Problems solved correctly: {solved}', Fore.CYAN))
    print(colored(f'Total attempts made: {attempts}', Fore.CYAN))
    print(colored(f'Wrong attempts: {wrong_attempts}', Fore.RED))
    print(colored(f'Total time: {total_time}s', Fore.YELLOW))
    print(colored(f'Average time per solved problem: {avg}s', Fore.YELLOW))
    print(colored(f'Approx. accuracy: {accuracy}%', Fore.GREEN if accuracy >= 70 else Fore.YELLOW))
    print(colored('-' * 40 + '\n', Fore.MAGENTA))

    print(colored('Thanks for playing! Run the script again to try for a better score.\n', Fore.MAGENTA))


if __name__ == '__main__':
    main()