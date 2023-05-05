# Tech Breakdown

## File and Class Overview
    - clueset.py - contains Clueset, which tracks which clue we are currently analyzing. This class also can validate and convert a puzzle input by the user to the correct format.
    - details.py - contains both PuzzleDetails and SolverDetails, which are dataclasses meant to store this particutlar puzzle and solving information.
    - exclusion_table.py - contains only the exclusion table, which helps to determine a square's potential values.
    - grid.py - contains Grid, which tracks which square we are currently analyzing (pointer), as well as the  current values of all the squares. It can also return the values of the 'neighbors' of the pointer.
    - library.py - contains PuzzleLibrary, which is able to load and display a list of puzzles (through JSON), for the user to choose one to be solved.
    - main.py - contains SolverApp, which is in charge of running the solver at the highest level.
    - nyt.py - TO BE FIXED: should import a puzzle from a source of older NYT puzzles
    - puzzle.py -  contains Puzzle, the main solving engine.
    - solutions.py = contains Solutions, which is in charge of tracking all correct solutions, analyzing the solutions, and printing/logging them afterwards.
    - symmetry.py - contains all of the types of symmetries and the logic behind them.
    - util.py - contains a few utility functions, such as clear_terminal().
    - value.py - contains an Enum of the different options for a single square, along with a few other list related constants.

## Grid
    The Grid class is responsible initializing the grid with unknown values, holding all of the updated values in the grid, as well as tracking which square we are currently analyzing (known as the pointer). In the code, the pRow and the pCol represent the pointer's row and column for readability, but are combined as a tuple (through the @property).

    The grid is stored in the Grid.grid dictionary, with the pointer being the key. This takes advantage of both the quicker lookup and default values for when the pointer is 'off the grid.'

    There are also a few other functions to help the pointer increment and decrement, to help determine if the pointer is at the end of a row, end of a column, or end of the puzzle, and to return all of the values in a particular row or column. Many of these functions are used later to ensure that there are no full rows or columns of black squares.


## Exclusion Table and Puzzle.check_options()
    The exclusion table is used to help determine which values are possible for a single square. When used in the Puzzle.check_options(), it analyzes each of the neighbors, one at a time, and determines what is NOT possible for that specific configuration.

    For example, if direcly above the pointer (U1) there is a black square, then it is impossible for the pointer to be an across clue or an empty square, based on the rules of crossword puzzles.

    A point to note, this exclusion table ONLY looks at the pointer and that specific neighbor, one at a time. So if U2 is black, it does not check what U1 is when determining what is 'impossble'. Because of this, some of the values in this lookup table are empty, meaning that that configuration does not restrict the pointer's possible values.

    Puzzle.check_options() continues through every one of the possible neighbors (U1, U2, U3, D1, D2, D3, L1, L2, L3, R1, R2, R3), building a set of impossible values for that square

    Some other restrictions are added to the square at this point:
        - Prevent a full row of black squares.
        - Prevent a full column of black squares.
        - If symmetry is enforced and not in the 'can-place' zone prevent a black square from being placed.

    Then the difference between these impossible values and all values results in only the possible values left.

    The exclusion table is a bit of a misnomer, as it is actually a dictionary, but this was just done to decrease time complexity.


## Puzzle
    Puzzle is the main solving engine, and Puzzle.solve() handles the main logic. At a very basic level, it goes through each square, placing the correct value (as determined by the Puzzle.check_options() and the exclusion table). If there are two possible values, it will always be a black square and some other value. A this point the solver will mark a backtracking point, and continue on solving with the other value. This will proceed until there are no possible options, or the puzzle is correct.

    The basic algorithm within Puzzle.solve() is outlined below:
        - While still solving:
            - Increment to the next square
            - If end of puzzle:
                If correct, add solution.
                If incorrect, backgrack.
            - Check possibilities for current square.
            - If there are 0 options, backtrack.
            - If there are 2 options, mark a backtrack spot and keep going.
            - If there is 1 option:
                - If it's an empty or a black, place it.
                - If it's a clue :
                    - If it's correct, place it.
                    - If it's incorrect, backtrack.

    Within the Puzzle class, there are few other methods:
        - implement_starting_squares() - If enforced, this will pre-pend the correct values: Black values until the given starting square, then add an Across and Down value. If this is not enforced, adjust the pointer slightly (so that the 'increment to the next square' puts you at the first square).
        - mark_backtrack_spot() - Adds the current pointer to a list of spots (splits) where there were multiple options for a single square.
        - backtrack() - Grab the most recently added backtrack spot, and undo the puzzle up until that point. Then add a black square (instead of whatever value was first implemented) and continue on.
        - set_black_square() - This will place a black square at the pointer. It will also check if symmetry is enforced, and that the pointer is in the 'can-place' zone. If so, it will place black squares in the corresponding symetrical location(s).
        - check_options() - described above, is meant to return all the possible options for a single square based on the current grid values.

## Symmetry
    When symmetry is enforced, it tends to speed up the process signficantly. For each black square placed, the solver will be able to place one (or more) symmetrical black squares as well.

    So in order to speed up the process during solving, for each type of symmetry we need to determine two different 'zones', one where we place black squares and one where ONLY symmetrically mirrored squares are placed based on the first zone. If the pointer is in the 'can place' zone, then it will place a black square in that zone, and the corresponding black squares in the symetrical location(s).

    Each type of symmetry has their own class, initialized with the size of the grid. Each of these classes have two methods:
        can_place(pointer) - returns True or False if the pointer is in the 'can place' zone, the first zone described above.
        sym_pointer(pointer) - returns a list of the corresponding symmetrical location(s) for the given pointer.