from play_wordle.user_input_validation import input_validation
from play_wordle.get_feedback import GetFeedback
from helper.rainbow_text import rainbow_output


def play_wordle(solution, allowed_guesses):
    attempts = 0

    while attempts < 6:
        guess = input_validation(attempts, allowed_guesses)
        if guess:
            feedback = GetFeedback(guess, solution).provide_feedback()
            print(feedback)
            if guess.lower() == solution:
                smiley_guy = "Congratulations! ٩̋(ˊ•͈ ꇴ •͈ˋ)و"
                return rainbow_output(smiley_guy)
            attempts += 1
        else:
            print("\033[91mInvalid input.\033[0m")
    else:
        print("\033[91mOut of attempts. You lost.\nThe correct word was:", solution.upper(), "\033[0m")
