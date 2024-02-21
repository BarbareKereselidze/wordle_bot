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
