from details import SolverDetails
from util import clear_terminal


class SolverPicker():
    def __init__(self):
        self.use_symmetry = True
        self.use_starting_square = True
        self.find_all = False
        self.use_interconnected = True
        self.show_numbers = True
        self.debug = False

    def run(self):
        return self.prompt_change()

    def print_details(self):
        clear_terminal()
        print('Solver Details:')
        for num, (k, v) in enumerate(self.__dict__.items(), 1):
            detail = k.title().replace('_', ' ').ljust(20)
            print(f'{num}. {detail}: {v}')

    def prompt_change(self):
        while True:
            self.print_details()
            change = input(
                'Enter option number to toggle, otherwise hit enter to proceed.\n')
            if change == '':
                return SolverDetails(self.use_symmetry,
                                     self.use_starting_square,
                                     self.find_all,
                                     self.use_interconnected,
                                     self.show_numbers,
                                     self.debug)
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
