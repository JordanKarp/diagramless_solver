import time

from converter import Converter
from util import clear_terminal


class Solutions:
    def __init__(self, puzzle_details, solver_details):
        self.puzzle_details = puzzle_details
        self.solver_details = solver_details
        self.list = []
        self.start_time = 0
        self.end_time = 0
        self.total_checked = 0
        self.converter = Converter()

    def start_timer(self):
        self.start_time = time.time()

    def end_timer(self, total_checked):
        self.end_time = round(time.time() - self.start_time, 3)
        self.total_checked = total_checked

    def add(self, puzzle, debug_counter):
        elapsed_time = round(time.time() - self.start_time, 3)
        if self.solver_details.show_numbers:
            puz = puzzle.grid.return_grid(True)
        else:
            puz = puzzle.grid.return_grid(False)
        entry = (puz, debug_counter, elapsed_time)
        self.list.append(entry)

    def print_solutions(self):
        clear_terminal()
        text = 'Results' + '\n'

        text += '-' * 7 + '\n'
        # Puzzle Details
        for k, v in self.puzzle_details.__dict__.items():
            detail = k.title().replace('_', ' ').ljust(20)
            text += f'{detail}: {v}' + '\n'

        # Puzzle Clue numbers
        acc, down = self.converter.unprocess_cluestring(
            self.puzzle_details.clue_string)
        text += f'{"Across Numbers".ljust(20)}: {" ".join(str(x) for x in acc)}' + '\n'
        text += f'{"Down Numbers".ljust(20)}: {" ".join(str(x) for x in down)}' + '\n'

        # Solver details
        text += '-' + '\n'
        for k, v in self.solver_details.__dict__.items():
            detail = k.title().replace('_', ' ').ljust(20)
            text += f'{detail}: {v}' + '\n'

        text += '-' * 7 + '\n'
        # Solver totals
        text += f'{"Total checked".ljust(20)}: {self.total_checked:,} ' + '\n'
        text += f'{"Total time".ljust(20)}: {self.end_time} seconds.' + '\n'
        text += f'{"Total solution(s)".ljust(20)}: {len(self.list):,}' + \
            '\n' + '\n'

        for num, (puz, debug_counter, elapsed_time) in enumerate(self.list, 1):
            text += f'{num}: {elapsed_time} seconds' + '\n'
            text += f'{debug_counter} squares checked.' + '\n'
            text += f'{puz}' + '\n'

        print(text)
