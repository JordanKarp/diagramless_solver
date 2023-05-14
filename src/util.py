import os


def clear_terminal():
    """ Clears the terminal screen depending on the operating system being used."""
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


def is_num_between(val, min, max):
    """
    Determines whether the value 'val' is between the values 'min' and 'max', inclusive.

    Args:
        val: A numerical value to be compared.
        min: The minimum value to compare 'val' with.
        max: The maximum value to compare 'val' with.

    Returns:
        True if 'val' is between 'min' and 'max', False otherwise.
    """
    return min <= val <= max
