def return_feedback(guess: str, solution: str) -> str:
    """ function to provide feedback on a guess in a wordle game
        color mapping: green - 92, yellow - 93, red - 91

        parameters:
        * guess (str) guess made by the player
        * solution (str) correct word that the player is trying to guess

        returns:
        * feedback (str) colorized word based on solution correctness
        """

    guess_map = [91] * 5
    solution_dict = {letter: solution.count(letter) for letter in solution}

    for i in range(5):
        if guess[i] == solution[i]:
            guess_map[i] = 92
            solution_dict[solution[i]] -= 1

    for i in range(5):
        if guess_map[i] == 91 and solution_dict.get(guess[i], 0) > 0:
            guess_map[i] = 93
            solution_dict[guess[i]] -= 1

    feedback = ''.join((f"\033[{guess_map[i]}m" + guess[i] + "\033[0m") for i in range(5))

    return feedback
