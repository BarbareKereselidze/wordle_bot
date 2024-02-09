def input_validation(attempts):
    guess = input(f"Attempt {attempts + 1}/6: ")

    with open('/home/user/PycharmProjects/wordle_bot/wordle_guesses/wordle-allowed-guesses.txt', 'r') as file:
        word_list = [word.strip() for word in file.readlines()]

    if guess.lower() in word_list:
        return guess.lower()
    else:
        return False
