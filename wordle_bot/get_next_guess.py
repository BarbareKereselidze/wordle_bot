class MostProbableGuess:
    def __init__(self, left_guesses: list):
        self.guess_probabilities = {}
        self.left_guesses = left_guesses

    def get_frequency(self):
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

    def get_each_probability(self, each_guess, position_frequency):
        every_letter_len = len(self.left_guesses) * 5
        letter_probability_sum = 0
        for ind in range(5):
            letter = each_guess[ind]
            letter_probability = position_frequency[letter][ind]
            letter_probability_sum += letter_probability
        return round(letter_probability_sum / every_letter_len, 3)

    def return_guess(self) -> dict:
        position_frequency = self.get_frequency()

        for guess in self.left_guesses:
            probability = self.get_each_probability(guess, position_frequency)
            self.guess_probabilities[guess] = probability

        sorted_dict = sorted(self.guess_probabilities.items(), key=lambda x: x[1], reverse=True)
        return sorted_dict[0][0]
