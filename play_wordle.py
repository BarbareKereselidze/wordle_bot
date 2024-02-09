from helper.input_validation import input_validation
from helper.get_feedback import GetFeedback


def play_wordle(solution):
    attempts = 0

    while attempts < 6:
        guess = input_validation(attempts)
        if guess:
            feedback = GetFeedback(guess, solution).provide_feedback()
            print(feedback)
            if guess.lower() == solution:
                print("\033[92mCongratulations! You've guessed the word!\033[0m")
                break
            attempts += 1
        else:
            print("\033[91mInvalid input.\033[0m")
    else:
        print("\033[91mOut of attempts. You lost.\nThe correct word was:", solution.upper(), "\033[0m")
