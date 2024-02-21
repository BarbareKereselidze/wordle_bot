def get_allowed_guess_list(config):
    allowed_guess_path = config['Paths']['allowed_guesses']

    with open(allowed_guess_path, 'r') as file:
        allowed_guess_list = [word.strip() for word in file.readlines()]

        return allowed_guess_list
