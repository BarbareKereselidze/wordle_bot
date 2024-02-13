class GetFeedback:
    def __init__(self, guess, solution):
        self.guess = guess
        self.solution = solution

    def colorize_output(self, letter, actual_letter):
        color_code = "\033[92m" if letter == actual_letter else ("\033[93m" if letter in self.solution else "\033[91m")
        return f"{color_code}{letter.upper()}\033[0m"

    def provide_feedback(self):
        return ''.join(self.colorize_output(self.guess[i], self.solution[i]) for i in range(len(self.solution)))
