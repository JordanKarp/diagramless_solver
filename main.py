from puzzle import Puzzle
from details import SolverDetails
from puzzle_picker import PuzzlePicker


class SolverApp:
    def __init__(self):
        self.puzzle_picker = PuzzlePicker()
        # self.solver_picker = SolverPicker()

    def run(self):
        puzzle_details = self.puzzle_picker.run()
        solver_details = SolverDetails(use_symmetry=True,
                                       use_starting_square=True,
                                       find_all=False,
                                       use_interconnected=True,
                                       show_numbers=True,
                                       debug=False)
        puzzle = Puzzle(puzzle_details, solver_details)
        solutions = puzzle.solve()
        solutions.print_solutions()


if __name__ == '__main__':
    solver = SolverApp()
    solver.run()
