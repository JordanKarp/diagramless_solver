from pathlib import Path

from library import PuzzleLibrary
from puzzle_input import PuzzleInput
from nyt_input import NYTPuzzleInput

# PUZZLE_LIBRARY_CSV = Path('./puzzle_list.csv')
PUZZLE_LIBRARY_CSV = Path(__file__).parent / "puzzle_list.csv"


class PuzzlePicker():
    """
    This class allows the user to choose the puzzle's input source
    and to pass the puzzle details from the source to the solver.
    """
    def __init__(self):
        """
        Initializes a new instance of the SolverPicker class.
        """
        self.source = None
        self.puzzle = None

    def run(self):
        self.print_menu()
        self.choose()
        return self.puzzle

    def print_menu(self):
        print('''
1. See existing puzzle library
2. Manually input a puzzle
3. Choose a standard puzzle from an NYT archive''')

    def choose(self):
        """Prompt the user to pick a puzzle source."""
        while True:
            try:
                choice = input('> ')
                if choice == '1':
                    self.source = PuzzleLibrary(PUZZLE_LIBRARY_CSV)
                elif choice == '2':
                    self.source = PuzzleInput()
                elif choice == '3':
                    self.source = NYTPuzzleInput()
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input. Please try again!")
            else:
                self.puzzle = self.source.run()
                break
