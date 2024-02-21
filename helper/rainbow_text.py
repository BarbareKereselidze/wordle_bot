import sys


def rainbow_output(text: str) -> None:
    """ function to print a string with rainbow colors to the console

        parameters:
        * text (str) string to be printed in rainbow colors
    """

    colors = ['\033[31m', '\033[33m', '\033[32m', '\033[36m', '\033[34m', '\033[35m']
    for char in text:
        sys.stdout.write(colors[text.index(char) % len(colors)] + char)
        sys.stdout.flush()
