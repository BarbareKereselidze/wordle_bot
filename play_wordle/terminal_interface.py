import sys

from play_wordle.user_input_validation import input_validation
from play_wordle.get_feedback import GetFeedback
from utils.helpers import rainbow_output

from wordle_bot.left_guesses import CheckGuesses


def play_wordle(solution: str, allowed_guesses: list, answer_guesses: list) -> None:
    """ function to simulate a game of wordle

        parameters:
        * solution (str) correct word that the player is trying to guess
        * allowed_guesses (list) list of allowed guesses
        * answer_guesses (list) list of previous guesses made by the player
    """

    attempts = 0
    last_guess = None
    left_guess_list = answer_guesses

    # give player 6 attempts to guess the answer
    while attempts < 6:
        guess = input(f"Attempt {attempts + 1}/6: ")
        left_guess_list = CheckGuesses(left_guess_list, last_guess, solution).filter_last_guesses()
        guess = input_validation(guess, allowed_guesses, left_guess_list)

        if guess:
            feedback = GetFeedback(guess, solution).provide_feedback()
            sys.stdout.write(feedback)
            sys.stdout.flush()
            sys.stdout.write("\n")

            # if player guessed the word stop the game
            if guess.lower() == solution:
                smiley_guy = "Congratulations! ٩̋(ˊ•͈ ꇴ •͈ˋ)و"
                rainbow_text = rainbow_output(smiley_guy)

                sys.stdout.write(rainbow_text)
                sys.stdout.flush()
                sys.stdout.write("\n")
                break

            last_guess = guess
            attempts += 1

        else:
            sys.stdout.write("\033[91mInvalid input.\033[0m\n")
            sys.stdout.flush()
    else:
        sys.stdout.write(
            "\033[91mOut of attempts. You lost.\nThe correct word was: {}\033[0m\n".format(solution.upper()))
        sys.stdout.flush()
