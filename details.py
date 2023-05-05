# from value import Value
from dataclasses import dataclass


@dataclass
class PuzzleDetails:
    def __init__(self, size, clue_string, symmetry, starting_square):
        self.size = size
        self.clue_string = clue_string
        self.symmetry = symmetry(self.size)
        self.starting_square = starting_square


@dataclass
class SolverDetails:
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
