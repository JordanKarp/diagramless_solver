from puzzle import Puzzle
from puzzle_picker import PuzzlePicker
from solver_picker import SolverPicker


class SolverApp:
    def __init__(self):
        self.puzzle_picker = PuzzlePicker()
        self.solver_picker = SolverPicker()

    def run(self):
        puzzle_details = self.puzzle_picker.run()
        solver_details = self.solver_picker.run()
        puzzle = Puzzle(puzzle_details, solver_details)
        solutions = puzzle.solve()
        solutions.print_solutions()


if __name__ == "__main__":
    solver = SolverApp()
    solver.run()
