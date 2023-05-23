def process_cluestring(across_nums, down_nums):
    """
    Processes the lists of across and down numbers and returns a clue string.

    Parameters:
        across_nums (list): A list of integers representing the across clue numbers.
        down_nums (list): A list of integers representing the down clue numbers.

    Returns:
        str: A string representation of the clue set.
    """
    total_clues = max(across_nums)
    cluestring = ""
    for num in range(1, total_clues + 1):
        if num in across_nums and num in down_nums:
            cluestring += "Z"
        elif num in across_nums:
            cluestring += "A"
        elif num in down_nums:
            cluestring += "D"
        else:
            raise IndexError
    return cluestring


def unprocess_cluestring(cluestring):
    """
    Processes the input clue string and returns lists of across and down numbers.

    Parameters:
        cluestring (str): A string representation of the clue set.

    Returns:
        tuple: A tuple containing two lists of integers representing
            the across and down clue numbers.
    """
    across_nums = []
    down_nums = []
    for index, char in enumerate(cluestring, start=1):
        if char in ["Z", "A"]:
            across_nums.append(index)
        if char in ["Z", "D"]:
            down_nums.append(index)
    return across_nums, down_nums
