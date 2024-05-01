def get_guess_list(path: str) -> list:
    """ function to read words from a file and return a list of those words

        parameters:
        * path (str) path to the file containing the list of words

        returns:
        * guess_list (list) list of words in the file
    """

    with open(path, 'r') as file:
        guess_list = [word.strip() for word in file.readlines()]
        return guess_list


def rainbow_output(text: str) -> str:
    """ function to print a string with rainbow colors to the console

        parameters:
        * text (str) string to be printed in rainbow colors
    """

    colors = ['\033[31m', '\033[33m', '\033[32m', '\033[36m', '\033[34m', '\033[35m']
    rainbow_text = ''
    for index, char in enumerate(text):
        rainbow_text += colors[index % len(colors)] + char
    return rainbow_text + '\033[0m'
