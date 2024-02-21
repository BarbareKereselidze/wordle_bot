class MostProbableGuess:
    """ class to provide feedback on a guess in a wordle game

        attributes:
        * guess_probabilities (dict) dictionary for mapping guesses to probabilities
        * left_guesses (list) list of valid guesses that are left, based on the last guess
    """

    def __init__(self, left_guesses: list) -> None:
        self.guess_probabilities = {}
        self.left_guesses = left_guesses

    def get_frequency(self):
        """ calculates the probability of each letter in each position of a guess based on the frequency

            returns:
            * position_frequency (dict) dictionary containing the frequency of each letter in each position of a guess
            """

        letter_frequency = {}
        position_frequency = {}

        for guess in self.left_guesses:
            for i, letter in enumerate(guess):

                if letter not in letter_frequency:
                    letter_frequency[letter] = 1
                    position_frequency[letter] = [0] * 5

                else:
                    letter_frequency[letter] += 1
                position_frequency[letter][i] += 1

        return position_frequency

    def get_each_probability(self, each_guess: str, position_frequency: dict) -> float:
        """ calculates the probability of each word being the correct guess

            parameters:
            * each_guess (str)
            * position_frequency (dict) dictionary containing the frequency of each letter in each position

            returns:
            * final_probability (float) the probability of input guess
            """

        every_letter_len = len(self.left_guesses) * 5
        letter_probability_sum = 0

        for ind in range(5):
            letter = each_guess[ind]
            letter_probability = position_frequency[letter][ind]
            letter_probability_sum += letter_probability

        final_probability = round(letter_probability_sum / every_letter_len, 3)

        return final_probability

    def return_guess(self) -> str:
        """ creates a dict for possible guess probability mapping

            returns:
            * most_probable_guess (str) most probable guess
            """

        position_frequency = self.get_frequency()

        for guess in self.left_guesses:
            probability = self.get_each_probability(guess, position_frequency)
            self.guess_probabilities[guess] = probability

        sorted_dict = sorted(self.guess_probabilities.items(), key=lambda x: x[1], reverse=True)
        most_probable_guess = sorted_dict[0][0]

        return most_probable_guess
