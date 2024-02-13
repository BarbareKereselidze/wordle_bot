import sys


def rainbow_output(text):
    colors = ['\033[31m', '\033[33m', '\033[32m', '\033[36m', '\033[34m', '\033[35m']
    for char in text:
        sys.stdout.write(colors[text.index(char) % len(colors)] + char)
        sys.stdout.flush()
