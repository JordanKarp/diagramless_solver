from library import PuzzleLibrary


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
        source = input(': ')
        if source == '1':
            self.source = PuzzleLibrary()
            self.puzzle = self.source.show_and_pick()
