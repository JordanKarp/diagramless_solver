from details import SolverDetails
from util import clear_terminal


class SolverPicker():
    """
    Class to represent how the diagramless solver 'solves' the given
    puzzle, and allows users to adust those details.
    """

    def __init__(self):
        """
        Initializes a new instance of the SolverPicker class.

        Attributes:
            use_symmetry (bool): Whether to use symmetry hint when generating the puzzle.
            use_starting_square (tuple): Whether to use the starting square hint.
            find_all (bool): Whether to find all solutions or just one.
            use_interconnected (bool): Whether to only consider interconnected answers.
            show_numbers (bool): Whether to show clue numbers in the output (or the clue Values).
            debug (bool): Whether to print debug information.
        """
        self.use_symmetry = True
        self.use_starting_square = True
        self.find_all = False
        self.use_interconnected = True
        self.show_numbers = True
        self.debug = False

    def run(self):
        """Runs the SolverPicker, allowing user to toggle options.

        Returns:
            SolverDetails: The SolverDetails object.
        """
        adjusting = True
        while adjusting:
            self.print_details()
            adjusting = self.prompt_change()
        return SolverDetails(self.use_symmetry,
                             self.use_starting_square,
                             self.find_all,
                             self.use_interconnected,
                             self.show_numbers,
                             self.debug)

    def print_details(self):
        """Prints the Solver Options."""
        clear_terminal()
        print('Solver Details:')
        for num, (k, v) in enumerate(self.__dict__.items(), 1):
            detail = k.title().replace('_', ' ').ljust(20)
            print(f'{num}. {detail}: {v}')

    def prompt_change(self):
        """Prompts the user to change the Solver Details."""
        change = input(
            'Enter option number to toggle, otherwise hit enter to proceed.\n')
        if change == '':
            return False
        else:
            try:
                if change == '1':
                    self.use_symmetry = not self.use_symmetry
                elif change == '2':
                    self.use_starting_square = not self.use_starting_square
                elif change == '3':
                    self.find_all = not self.find_all
                elif change == '4':
                    self.use_interconnected = not self.use_interconnected
                elif change == '5':
                    self.show_numbers = not self.show_numbers
                elif change == '6':
                    self.debug = not self.debug
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input. Please try again!")
            return True
