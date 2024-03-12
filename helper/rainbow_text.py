import sys


def rainbow_output(text: str) -> None:
    """ function to print a string with rainbow colors to the console

        parameters:
        * text (str) string to be printed in rainbow colors
    """

    colors = ['\033[31m', '\033[33m', '\033[32m', '\033[36m', '\033[34m', '\033[35m']
    rainbow_text = ''
    for index, char in enumerate(text):
        rainbow_text += colors[index % len(colors)] + char
    return rainbow_text + '\033[0m'
