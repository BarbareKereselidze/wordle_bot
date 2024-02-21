import configparser


def return_config_dict(config_file_path: str) -> dict:
    """ function to read a configuration file in the ini format and return its contents as a dictionary

        parameters:
        * config_file_path (str) path to the configuration file

        returns:
        * output_dict (dict) contents of the configuration file as a dictionary
    """

    config_object = configparser.ConfigParser()

    with open(config_file_path, "r") as file:
        config_object.read_file(file)

    output_dict = {section: dict(config_object.items(section)) for section in config_object.sections()}

    return output_dict
