def get_answer_guess_list(config):
    answer_guesses_path = config['Paths']['answer_guesses']

    with open(answer_guesses_path, 'r') as file:
        answer_guess_list = [word.strip() for word in file.readlines()]

        return answer_guess_list
