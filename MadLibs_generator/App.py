import re
import os
import sys
from collections import OrderedDict
from datetime import datetime

try:
    from colorama import init as colorama_init
    from colorama import Fore, Style
    colorama_init(autoreset=True)
except Exception:
    # Minimal fallback colors (ANSI). Works on most Unix terminals.
    class Fore:
        CYAN = '\033[36m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        MAGENTA = '\033[35m'
        RED = '\033[31m'
        RESET = '\033[39m'

    class Style:
        BRIGHT = '\033[1m'
        RESET_ALL = '\033[0m'


STORY_PATH = os.path.join(os.path.dirname(__file__), 'story.txt')


def clear_screen():
    # Cross-platform clear
    os.system('cls' if os.name == 'nt' else 'clear')


def load_story():
    with open(STORY_PATH, 'r', encoding='utf-8') as f:
        return f.read()


def find_placeholders(text):
    # returns unique placeholders in order of first appearance (without angle brackets)
    tokens = re.findall(r'<([^<>]+)>', text)
    return list(OrderedDict.fromkeys(tokens))


def colored(text, color):
    return f"{color}{text}{Style.RESET_ALL}"


def prompt_for_words(placeholders):
    answers = {}
    for ph in placeholders:
        prompt = f"Enter a {ph}: "
        try:
            val = input(colored(prompt, Fore.CYAN + Style.BRIGHT))
        except KeyboardInterrupt:
            print('\n' + colored('Input cancelled. Exiting.', Fore.RED))
            sys.exit(1)
        answers[ph] = val.strip() if val.strip() else f'<{ph}>'
    return answers


def apply_answers(text, answers):
    result = text
    for ph, val in answers.items():
        result = result.replace(f'<{ph}>', val)
    return result


def save_story(text):
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    out_name = f'madlibs_{ts}.txt'
    out_path = os.path.join(os.path.dirname(STORY_PATH), out_name)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(text)
    return out_path


def main():
    # Friendly CLI loop
    while True:
        clear_screen()
        print(colored('\n  *** MAD LIBS GENERATOR ***\n', Fore.MAGENTA + Style.BRIGHT))

        try:
            story = load_story()
        except FileNotFoundError:
            print(colored(f"Could not find story file at {STORY_PATH}", Fore.RED))
            return

        placeholders = find_placeholders(story)
        if not placeholders:
            print(colored('No placeholders found in the story (look for <like_this>).', Fore.YELLOW))
            print(story)
            return

        print(colored(f"I found {len(placeholders)} unique placeholders:", Fore.YELLOW))
        print(colored(', '.join(f'<{p}>' for p in placeholders), Fore.CYAN))
        print()

        answers = prompt_for_words(placeholders)

        final = apply_answers(story, answers)

        print('\n' + colored('Here is your story:', Fore.GREEN + Style.BRIGHT))
        print(colored('-' * 40, Fore.MAGENTA))
        print(colored(final, Fore.GREEN))
        print(colored('-' * 40 + '\n', Fore.MAGENTA))

        # Save option
        save = input(colored('Save this story to a file? (Y/n): ', Fore.CYAN)).strip().lower()
        if save in ('', 'y', 'yes'):
            out_path = save_story(final)
            print(colored(f'Story saved to: {out_path}', Fore.YELLOW))

        again = input(colored('Play again with the same story? (Y/n): ', Fore.CYAN)).strip().lower()
        if again not in ('', 'y', 'yes'):
            print(colored('Thanks for playing! Goodbye.', Fore.MAGENTA))
            break


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n' + colored('Interrupted. Bye!', Fore.RED))