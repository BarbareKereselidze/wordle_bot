class GetFeedback:
    """ class to provide feedback on a guess in a wordle game

        attributes:
        * guess (str) guess made by the player
        * solution (str) correct word that the player is trying to guess
        """

    def __init__(self, guess: str, solution: str) -> None:
        self.guess = guess
        self.solution = solution

    def colorize_output(self, letter: str, actual_letter: str) -> str:
        """ returns a colorized version of a letter based on whether it is correct or incorrect

            attributes:
            * letter (str) letter from guess
            * actual_letter (str) letter from solution

            returns:
            * colorized_letter (str) colorized letter based on whether it is correct or incorrect
            """

        color_code = "\033[92m" if letter == actual_letter else ("\033[93m" if letter in self.solution else "\033[91m")
        colorized_letter = f"{color_code}{letter.upper()}\033[0m"

        return colorized_letter

    def provide_feedback(self) -> str:
        """ provides feedback on the guess by colorizing each letter based on correctness

            returns:
            * feedback (str) colorized word based on solution correctness
            """

        feedback = ''.join(self.colorize_output(self.guess[i], self.solution[i]) for i in range(len(self.solution)))

        return feedback
