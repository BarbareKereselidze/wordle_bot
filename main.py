import os

from utils.get_config import return_config_dict
from utils.helpers import get_guess_list

from play_wordle.retrieve_answer import get_wordle_answer
from play_wordle.terminal_interface import play_wordle


def main():
    # read config file as a dictionary
    script_directory = os.path.dirname(os.path.abspath(__file__))
    CONFIG_FILE_PATH = os.path.join(script_directory, 'config.ini')
    config_dict = return_config_dict(CONFIG_FILE_PATH)

    # get today's wordle answer
    solution = get_wordle_answer()

    # get list of allowed guesses and answer list guesses
    allowed_guess_path = config_dict['Paths']['allowed_guesses']
    answer_guess_path = config_dict['Paths']['answer_guesses']

    allowed_guesses = get_guess_list(allowed_guess_path)
    answer_guesses = get_guess_list(answer_guess_path)

    # start playing wordle
    play_wordle(solution, allowed_guesses, answer_guesses)


if __name__ == "__main__":
    main()
