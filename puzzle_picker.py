from library import PuzzleLibrary
from puzzle_input import PuzzleInput
from nyt_input import NYTPuzzleInput


class PuzzlePicker():
    def __init__(self):
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
        while True:
            try:
                choice = input('> ')
                if choice == '1':
                    self.source = PuzzleLibrary()
                elif choice == '2':
                    self.source = PuzzleInput()
                    # self.puzzle = self.source.run()
                elif choice == '3':
                    self.source = NYTPuzzleInput()
                    # self.puzzle = self.source.run()
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input. Please try again!")
            else:
                self.puzzle = self.source.run()
                break
