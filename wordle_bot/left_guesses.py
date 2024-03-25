class CheckGuesses:
    """ class to filter out guesses that are not valid based on
        the feedback from the previous guess

        attributes:
        * guess_list (list) list of potential guess
        * last_guess (str) last guess made by the player
        * guess (str) correct word that the player is trying to guess
        * potential_guesses (list) list to map potential guesses
            that are valid based on the feedback from the previous guess
        """

    def __init__(self, guess_list: list, last_guess: str, solution: str) -> None:
        self.guess_list = guess_list
        self.last_guess = last_guess
        self.guess = solution
        self.potential_guesses = []

    def validate_guess(self, potential_guess: str) -> bool:
        """ validates a potential guess based on the feedback from the previous guess

            parameters:
            * potential_guess (str) guess to be checked

            returns:
            * (bool) true if the potential guess is valid, false otherwise
            """

        new_guess = potential_guess

        for ind in range(5):
            current_letter = self.last_guess[ind]

            # if letter is green
            if current_letter == self.guess[ind]:
                if current_letter != potential_guess[ind]:
                    return False

            # if letter is gray
            elif current_letter not in self.guess:
                if current_letter in potential_guess:
                    return False

            # if letter is yellow
            elif current_letter == potential_guess[ind]:
                return False

            else:
                if current_letter not in new_guess:
                    return False
                else:
                    new_guess = new_guess.replace(current_letter, '0', 1)

        return True

    def filter_last_guesses(self) -> list:
        """ filters out invalid guesses based on guess_list and previous guess

            returns:
            * guess_list / potential_guesses (list) list of potential guesses that are valid based on the feedback from the previous guess
            """

        if self.last_guess is None:
            return self.guess_list
        else:
            for potential_guess in self.guess_list:
                if self.validate_guess(potential_guess):
                    self.potential_guesses.append(potential_guess)

            return self.potential_guesses
