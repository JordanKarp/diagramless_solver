from details import PuzzleDetails
from converter import process_cluestring
from util import is_num_between
from value import SYMMETRIES


class PuzzleInput:
    """
    A class to get the input data for a puzzle, including
    dimensions, cluestring, symmetry, and starting square.
    """

    def run(self):
        dimensions = self.get_dimensions()
        cluestring = self.get_cluestring()
        symmetry = self.get_symmetry()
        starting_square = self.get_starting_square()
        return PuzzleDetails(dimensions, cluestring, symmetry, starting_square)

    def get_dimensions(self):
        """Prompt the user for the puzzle dimensions: rows and columns"""
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
        """Prompt the user for the puzzle across and down numbers, and convert to cluestring"""
        while True:
            try:
                across_nums = [
                    int(x)
                    for x in input(
                        "Input the Across clue numbers, separated by a space: "
                    ).split(" ")
                ]
                down_nums = [
                    int(x)
                    for x in input(
                        "Input the Down clue numbers, separated by a space: "
                    ).split(" ")
                ]
                cluestring = process_cluestring(across_nums, down_nums)

            except ValueError:
                print("Invalid input. Please try again!")
            else:
                return cluestring

    def get_symmetry(self):
        """Prompt the user for the puzzle symmetry."""
        while True:
            try:
                sym_string = input("Type of Symmetry: ")
                if sym_string not in SYMMETRIES:
                    raise ValueError
            except ValueError:
                print("Invalid input. Please try again!")
                # If the user messes up the symmetries, list the options before trying again.
                for sym in SYMMETRIES:
                    print(sym, end=", ")
                print()
            else:
                return SYMMETRIES[sym_string]

    def get_starting_square(self):
        """Prompt the user for the puzzle starting square."""
        while True:
            try:
                sq = int(input("Starting square: "))
                if not is_num_between(sq, 1, 25):
                    raise ValueError
            except ValueError:
                print("Invalid input. Please try again!")
            else:
                return sq
