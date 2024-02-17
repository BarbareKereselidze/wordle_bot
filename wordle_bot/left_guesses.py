class CheckGuesses:
    def __init__(self, guess_list, last_guess, guess):
        self.guess_list = guess_list
        self.last_guess = last_guess
        self.guess = guess
        self.potential_guesses = []

    def validate_guess(self, potential_guess):
        new_guess = potential_guess
        for ind in range(5):
            current_letter = self.last_guess[ind]

            # letter is green
            if current_letter == self.guess[ind]:
                if current_letter != potential_guess[ind]:
                    return False

            # letter is gray
            elif current_letter not in self.guess:
                if current_letter in potential_guess:
                    return False

            # letter is yellow
            elif current_letter == potential_guess[ind]:
                return False

            else:
                if current_letter not in new_guess:
                    return False
                else:
                    new_guess = new_guess.replace(current_letter, '0', 1)

        return True

    def filter_last_guesses(self):
        for potential_guess in self.guess_list:
            if self.validate_guess(potential_guess):
                self.potential_guesses.append(potential_guess)

        return self.potential_guesses
