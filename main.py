from puzzle import Puzzle
from library import PuzzleLibrary
from details import SolverDetails


class SolverApp:
    def run(self):
        library = PuzzleLibrary()
        puz_details = library.show_and_pick()
        solver_details = SolverDetails(use_symmetry=True,
                                       use_starting_square=True,
                                       find_all=True,
                                       use_interconnected=False,
                                       show_numbers=True,
                                       debug=False)
        puzzle = Puzzle(puz_details, solver_details)
        solutions = puzzle.solve()
        solutions.print_solutions()


if __name__ == '__main__':
    solver = SolverApp()
    solver.run()
