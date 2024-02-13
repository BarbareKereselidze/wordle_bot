import os

from utils.get_config import return_config_dict
from helper.get_allowed_guess_list import get_allowed_guess_list
from helper.get_answer_list import get_answer_guess_list

from play_wordle.retrieve_answer import get_wordle_answer
from play_wordle.terminal_interface import play_wordle


def main():
    """ read config file as a dictionary """
    script_directory = os.path.dirname(os.path.abspath(__file__))
    CONFIG_FILE_PATH = os.path.join(script_directory, 'config.ini')
    config_dict = return_config_dict(CONFIG_FILE_PATH)

    """ get today's wordle answer """
    solution = get_wordle_answer()

    """ get list of allowed guesses and answer list guesses """
    allowed_guesses = get_allowed_guess_list(config_dict)
    answer_guesses = get_answer_guess_list(config_dict)

    play_wordle(solution, allowed_guesses)


if __name__ == "__main__":
    main()
