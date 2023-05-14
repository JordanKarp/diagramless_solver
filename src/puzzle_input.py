from details import PuzzleDetails
from converter import Converter
from util import is_num_between
from value import SYMMETRIES


class PuzzleInput():
    '''
    A class to get the input data for a puzzle, including dimensions, cluestring, symmetry, and starting square.
    '''
    def __init__(self):
        """    Initializes the PuzzleInput class by creating an instance of the Converter class."""
        self.converter = Converter()

    def run(self):
        dimensions = self.get_dimensions()
        cluestring = self.get_cluestring()
        symmetry = self.get_symmetry()
        starting_square = self.get_starting_square()
        return PuzzleDetails(dimensions, cluestring, symmetry, starting_square)

    def get_dimensions(self):
        while True:
            try:
                rows = int(input("Number of Rows: "))
                if not is_num_between(rows, 3, 25):
                    raise ValueError

                cols = int(input("Number of Columns: "))
                if not is_num_between(cols, 3, 25):
                    raise ValueError
            except ValueError:
                print("Invalid input. Please try again!")
            else:
                return (rows, cols)

    def get_cluestring(self):
        while True:
            try:
                across_nums = [int(x) for x in input(
                    'Input the Across clue numbers, separated by a space: ').split(' ')]
                down_nums = [int(x) for x in input(
                    'Input the Down clue numbers, separated by a space: ').split(' ')]
                cluestring = self.converter.process_cluestring(
                    across_nums, down_nums)
            except ValueError:
                print("Invalid input. Please try again!")
            else:
                return cluestring

    def get_symmetry(self):
        while True:
            try:
                sym_string = input("Type of Symmetry: ")
                if sym_string not in SYMMETRIES:
                    raise ValueError
            except ValueError:
                print("Invalid input. Please try again!")
            else:
                return SYMMETRIES[sym_string]

    def get_starting_square(self):
        while True:
            try:
                sq = int(input("Starting square: "))
                if not is_num_between(sq, 1, 25):
                    raise ValueError
            except ValueError:
                print("Invalid input. Please try again!")
            else:
                return sq
