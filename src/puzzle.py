from clueset import ClueSet
from exclusion_table import EXCLUSION_TABLE
from grid import Grid
from solutions import Solutions
from util import clear_terminal
from value import Value, OPTIONS, CLUES


class Puzzle():
    '''
    Puzzle - Responsible for the actual solving/builing of a diagramless crossword puzzle.
    '''

    def __init__(self, puzzle_details, solver_details):
        '''
        Initializes a Puzzle object.

        Parameters:
            puzzle_details (PuzzleDetails): Details of the puzzle to be solved.
            solver_details (SolverDetails): Details of the solver to be used.
        '''
        self.puzzle_details = puzzle_details
        self.solver_details = solver_details
        self.grid = Grid(self.puzzle_details.size)
        self.clues = ClueSet(self.puzzle_details.clue_string)
        self.solutions = Solutions(self.puzzle_details, self.solver_details)
        self.solving = True
        self.splits = []
        self.squares_checked = 0

    def solve(self):
        print('Processing.')
        self.solutions.start_timer()

        self.implement_starting_squares()
        while (self.solving):
            self.grid.increment()
            self.squares_checked += 1

            if self.grid.is_end_of_grid():
                if self.clues.equals(Value.FINAL):
                    if self.solver_details.use_interconnected:
                        if not self.grid.is_interconnected():
                            self.backtrack()
                            continue
                    self.solutions.add(self, self.squares_checked)
                    if not self.solver_details.find_all:
                        self.solving = False
                        continue
                self.backtrack()

            if self.grid.equals(Value.BLACK):
                continue

            # Grab all the options for this square
            pointer_opts = self.check_options()

            if len(pointer_opts) == 0:
                self.backtrack()

            # If there is more than one option, it will always be X and black
            # Mark a split, drop the black and keep going with the value
            if len(pointer_opts) == 2:
                self.mark_backtrack_point()
                pointer_opts.remove(Value.BLACK)

            if len(pointer_opts) == 1:
                val = pointer_opts.pop()
                if val is Value.BLACK:
                    self.set_black_square()
                elif val is Value.EMPTY:
                    self.grid.set(val)
                elif val in CLUES:
                    if self.clues.equals(val):
                        self.clues.increment()
                        self.grid.set(val)
                    else:
                        self.backtrack()

            if self.solver_details.debug or self.squares_checked % 1_000_000 == 0:
                clear_terminal()
                print('In progress:')
                print(self.grid.return_grid())
                print(f'Grid: {self.grid.pointer}')
                print(
                    f'Clue: {self.clues.clue_pointer} - {self.clues.at()}')
                print(f'Splits: {len(self.splits)}')
                print(f'Squares Checked: {self.squares_checked:,}')
                print(f'Solutions: {len(self.solutions.list)}')

        self.solutions.end_timer(self.squares_checked)
        return self.solutions

    def implement_starting_squares(self):
        '''
        Set the first few squares manually, if using starting square.
        '''

        # Trick to start at the correct square if we're not using the starting square info
        if not self.solver_details.use_starting_square:
            self.grid.pCol = -1
            return

        # Place Black squares up until the starting square, then place AcrossDown
        for _ in range(self.puzzle_details.starting_square - 1):
            self.set_black_square()
            self.grid.increment()
        self.grid.set(Value.ACROSSDOWN)
        self.clues.increment()

    def mark_backtrack_point(self):
        '''Mark the spot where there are two potential options, for backtracking later on.'''
        self.splits.append((self.grid.pRow, self.grid.pCol))

    def backtrack(self):
        # If there are no backtracking spots left, stop solving
        if len(self.splits) == 0:
            self.solving = False
            return

        # Grag the most recent backtrack pointer, and undo everything until that point.
        backtrack_pointer = self.splits.pop()
        while self.grid.pointer != backtrack_pointer:
            self.grid.decrement()
            cur_val = self.grid.at()
            if cur_val in CLUES:
                self.clues.decrement()
            if cur_val is Value.BLACK and self.solver_details.use_symmetry:
                if self.puzzle_details.symmetry.can_place(self.grid.pointer):
                    for pointer in self.puzzle_details.symmetry.sym_pointer(self.grid.pointer):
                        self.grid.set_at(Value.UNKNOWN, pointer)
                else:
                    continue
            self.grid.set(Value.UNKNOWN)

        # Place a black square and proceed.
        self.set_black_square()

    def set_black_square(self):
        '''Set a black square, and potentially set the symmetrical square(s).'''
        self.grid.set(Value.BLACK)
        if self.solver_details.use_symmetry:
            if self.puzzle_details.symmetry.can_place(self.grid.pointer):
                for pointer in self.puzzle_details.symmetry.sym_pointer(self.grid.pointer):
                    self.grid.set_at(Value.BLACK, pointer)

    def check_options(self):
        '''Check which options are impossible, given each individual neighbor configurations.'''
        impossibles = set()
        impossibles.update(EXCLUSION_TABLE['U1'][self.grid.u1()])
        impossibles.update(EXCLUSION_TABLE['U2'][self.grid.u2()])
        impossibles.update(EXCLUSION_TABLE['U3'][self.grid.u3()])
        impossibles.update(EXCLUSION_TABLE['D1'][self.grid.d1()])
        impossibles.update(EXCLUSION_TABLE['D2'][self.grid.d2()])
        impossibles.update(EXCLUSION_TABLE['D3'][self.grid.d3()])
        impossibles.update(EXCLUSION_TABLE['L1'][self.grid.l1()])
        impossibles.update(EXCLUSION_TABLE['L2'][self.grid.l2()])
        impossibles.update(EXCLUSION_TABLE['L3'][self.grid.l3()])
        impossibles.update(EXCLUSION_TABLE['R1'][self.grid.r1()])
        impossibles.update(EXCLUSION_TABLE['R2'][self.grid.r2()])
        impossibles.update(EXCLUSION_TABLE['R3'][self.grid.r3()])

        # If end of a row, make sure it's a valid row (not all blacks)
        if self.grid.is_end_of_row():
            if self.grid.values_in_row() == {Value.BLACK, Value.UNKNOWN}:
                impossibles.update({Value.BLACK})
        # If end of a column, make sure it's a valid col (no all blacks)
        if self.grid.is_end_of_col():
            if self.grid.values_in_col() == {Value.BLACK, Value.UNKNOWN}:
                impossibles.update({Value.BLACK})

        # If there's symmetry and you're not in the 'can place' zone, can't place black.
        if self.solver_details.use_symmetry:
            if self.puzzle_details.symmetry.can_place(self.grid.pointer) is False:
                impossibles.update({Value.BLACK})

        # Return the difference between all possible options, and what is impossible
        # Leaving only possible options.
        return OPTIONS.difference(impossibles)
