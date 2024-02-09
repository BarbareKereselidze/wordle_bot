from helper.retrieve_answer import get_wordle_answer
from play_wordle import play_wordle


if __name__ == "__main__":
    solution = get_wordle_answer()
    play_wordle(solution)
