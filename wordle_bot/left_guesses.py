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
        self.solution = solution
        self.potential_guesses = []

    def validate_guess(self, potential_guess: str) -> bool:
        """ validates a potential guess based on the feedback from the previous guess

            parameters:
            * potential_guess (str) guess to be checked

            returns:
            * (bool) true if the potential guess is valid, false otherwise
            """

        guess_map = self.last_guess
        solution_map = self.solution
        potential_guess_map = potential_guess

        for ind in range(5):
            current_letter = self.last_guess[ind]

            # if letter is green
            if current_letter == self.solution[ind]:
                if current_letter == potential_guess[ind]:
                    guess_map = guess_map[:ind] + '0' + guess_map[ind + 1:]
                    solution_map = solution_map[:ind] + '1' + solution_map[ind + 1:]
                    potential_guess_map = potential_guess_map[:ind] + '2' + potential_guess_map[ind + 1:]
                else:
                    return False

        for ind in range(5):
            current_letter = guess_map[ind]

            # if letter is yellow
            if current_letter in solution_map:
                if current_letter in potential_guess_map and current_letter != potential_guess_map[ind]:
                    solution_map = solution_map.replace(current_letter, '1', 1)
                    potential_guess_map = potential_guess_map.replace(current_letter, '2', 1)
                    guess_map = guess_map[:ind] + '0' + guess_map[ind + 1:]
                else:
                    return False

        for ind in range(5):
            current_letter = guess_map[ind]

            # if letter is gray
            if current_letter in potential_guess_map:
                return False

        return True

    def filter_last_guesses(self) -> list:
        """ filters out invalid guesses based on guess_list and previous guess

            returns:
            * guess_list / potential_guesses (list) list of potential guesses that are
              valid based on the feedback from the previous guess
            """

        if self.last_guess is None:
            return self.guess_list
        else:
            for potential_guess in self.guess_list:
                if self.validate_guess(potential_guess):
                    self.potential_guesses.append(potential_guess)

            return self.potential_guesses
