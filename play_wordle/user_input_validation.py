def input_validation(attempts, allowed_guess_list):
    guess = input(f"Attempt {attempts + 1}/6: ")

    if guess.lower() in allowed_guess_list:
        return guess.lower()
    else:
        return False
