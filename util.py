import os


def clear_terminal():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


def is_num_between(val, min, max):
    return min <= val <= max
