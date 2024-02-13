def get_frequency(answer_list):
    letter_frequency = {}
    position_frequency = {}

    for guess in answer_list:
        for i, letter in enumerate(guess):
            if letter not in letter_frequency:
                letter_frequency[letter] = 1
                position_frequency[letter] = [0] * 5
            else:
                letter_frequency[letter] += 1
            position_frequency[letter][i] += 1

    return letter_frequency, position_frequency
