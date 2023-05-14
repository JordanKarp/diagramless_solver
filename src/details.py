# from value import Value
from dataclasses import dataclass


@dataclass
class PuzzleDetails:
    def __init__(self, size, clue_string, symmetry, starting_square):
        """
        Stores details about a crossword puzzle.

        Parameters / Attributes:
            size (int): The dimensions of the puzzle.
            clue_string (str): A string representation of the clue set.
            symmetry (class): A class that represents the symmetry pattern for the puzzle.
            starting_square (tuple): A tuple containing the row and column of the starting square.
        """
        self.size = size
        self.clue_string = clue_string
        self.symmetry = symmetry(self.size)
        self.starting_square = starting_square


@dataclass
class SolverDetails:
    """
        Stores details about how the solver will build the crossword puzzle.

        Parameters:
            use_symmetry (bool): Whether to use symmetry hint when generating the puzzle.
            use_starting_square (tuple): Whether to use the starting square hint.
            find_all (bool): Whether to find all solutions or just one.
            use_interconnected (bool): Whether to only consider interconnected answers.
            show_numbers (bool): Whether to show clue numbers in the output (or the clue Values).
            debug (bool): Whether to print debug information.
    """

    def __init__(self,
                 use_symmetry=False,
                 use_starting_square=None,
                 find_all=False,
                 use_interconnected=False,
                 show_numbers=False,
                 debug=False):
        self.use_symmetry = use_symmetry
        self.use_starting_square = use_starting_square
        self.find_all = find_all
        self.use_interconnected = use_interconnected
        self.show_numbers = show_numbers
        self.debug = debug
