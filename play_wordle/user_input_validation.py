from wordle_bot.get_next_guess import MostProbableGuess


def input_validation(attempts, allowed_guess_list, left_guess_list):
    guess = input(f"Attempt {attempts + 1}/6: ")
    guess = guess.lower()

    if guess in allowed_guess_list:
        return guess
    if guess == "bot":
        guess = MostProbableGuess(left_guess_list).return_guess()
        return guess
    else:
        return False
