import os
from dotenv import load_dotenv
from utils.helpers import get_guess_list
from play_wordle.retrieve_answer import get_wordle_answer
from play_wordle.terminal_interface import play_wordle

load_dotenv()

ALLOWED_PATH = os.getenv("ALLOWED_PATH")
ANSWERS_PATH = os.getenv("ANSWERS_PATH")


def main():
    # get today's wordle answer
    solution = get_wordle_answer()

    # get list of allowed guesses and answer list guesses
    allowed_guesses = get_guess_list(ALLOWED_PATH)
    answer_guesses = get_guess_list(ANSWERS_PATH)

    # start playing wordle
    play_wordle(solution, allowed_guesses, answer_guesses)


if __name__ == "__main__":
    main()
