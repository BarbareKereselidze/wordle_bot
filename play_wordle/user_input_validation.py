from wordle_bot.get_next_guess import MostProbableGuess


def input_validation(attempts: int, allowed_guesses: list, left_guesses: list) -> str or bool:
    """ function to validate the user's input in a wordle game

        parameters:
        * attempts (int) number of attempts the user has made so far
        * allowed_guesses (list) list of allowed guesses
        * left_guesses (list) list of remaining guesses

        Returns:
        - str or bool: the user's input if it is valid, or false otherwise
    """

    guess = input(f"Attempt {attempts + 1}/6: ")
    guess = guess.lower()

    # if guess is valid return guess
    if guess in allowed_guesses:
        return guess

    # if user wants for the bot to make the guess
    if guess == "bot":
        # calculate the most probable guess
        guess = MostProbableGuess(left_guesses).return_guess()
        return guess

    # if guess is not valid return false
    else:
        return False
