# Tech Breakdown

## File and Class Overview

| File | Explaination |
| --- | --- |
| clueset.py | contains Clueset, which tracks which clue we are currently analyzing. |
| converter.py | contains Converter, which is responsible for turning accross and down clue numbers into a clue string, and then back.  |
| details.py | contains both PuzzleDetails and SolverDetails, which are dataclasses meant to store this particutlar puzzle and solving information. |
| exclusion_table.py | contains only the exclusion table, which helps to determine a square's potential values. |
| grid.py | contains Grid, which tracks which square we are currently analyzing (pointer), as well as the  current values of all the squares. It can also return the values of the 'neighbors' of the pointer. |
| library.py | contains PuzzleLibrary, which is able to load and display a list of puzzles (through JSON), for the user to choose one to be solved. |
| main.py | contains SolverApp, which is in charge of running the solver at the highest level. |
| nyt_input.py | contains NYTPuzzleInput,  which allows a user to import a puzzle from a github archive of standard NYT puzzles from 1977-2017. |
| puzzle.py |  contains Puzzle, the main solving engine. |
| puzzle_input.py | contains Puzzle Input, which is responsible for prompting and validating a user-input puzzle. |
| puzzle_list.csv | datasource for current puzzle library. |
| puzzle_picker.py | contains PuzzlePicker, which allows the user to chose the puzzle source. |
| solutions.py | contains Solutions, which is in charge of tracking all correct solutions, analyzing the solutions, and printing/logging them afterwards. |
| solver_picker.py | contains SolverPicker, which allows users to taggle the solver parameters. |
| symmetry.py | contains Symmetry and classes for all of the other types of symmetries, including the logic behind each. |
| util.py | contains a few utility functions, such as clear_terminal() and an interger validator. |
| value.py | contains an Enum of the different options for a single square, along with a few other list related constants. |

## Grid

The Grid class is responsible initializing the grid with unknown values, holding all of the updated values in the grid, as well as tracking which square we are currently analyzing (known as the pointer). In the code, the pRow and the pCol represent the pointer's row and column for readability, but are combined as a tuple (through the @property).

The grid is stored in the Grid.grid dictionary, with the pointer being the key. This takes advantage of both the quicker lookup and default values for when the pointer is 'off the grid.'

There are also a few other functions to help the pointer increment and decrement, to help determine if the pointer is at the end of a row, end of a column, or end of the puzzle, and to return all of the values in a particular row or column. Many of these functions are used later to ensure that there are no full rows or columns of black squares.

## Exclusion Table and Puzzle.check_options()

The exclusion table is used to help determine which values are possible for a single square. When used in the Puzzle.check_options(), it analyzes each of the neighbors, one at a time, and determines what is NOT possible for that specific configuration.

For example, if direcly above the pointer (U1) there is a black square, then it is impossible for the pointer to be an across clue or an empty square, based on the rules of crossword puzzles.

A point to note, this exclusion table ONLY looks at the pointer and that specific neighbor, one at a time. So if U2 is black, it does not check what U1 is when determining what is 'impossble'. Because of this, some of the values in this lookup table are empty, meaning that that configuration does not restrict the pointer's possible values.

Puzzle.check_options() continues through every one of the possible pointer neighbors (Up 1, Up 2, Up 3, Down 1, Down 2, Down 3, Left 1, Left 2, Left 3, Right 1, Right 2, Right 3), building a set of impossible values for that square

Some other restrictions are added to the square at this point:

- Prevent a full row of black squares.
- Prevent a full column of black squares.
- If symmetry is enforced and not in the 'can-place' zone, prevent a black square from being placed.

Then the difference between these impossible values and all values results in only the possible values left.

The exclusion table is a bit of a misnomer, as it is actually a dictionary, but this was just done to decrease time complexity.

## Puzzle

Puzzle is the main solving engine, and Puzzle.solve() handles the main algorithm logic.

At a very basic level, it goes through each square, placing the correct value (as determined by the Puzzle.check_options() and the exclusion table). If there are two possible values, it will always be a black square and some other value. A this point the solver will mark a backtracking point, and continue on solving with the other value. This will proceed until there are no possible options, or the puzzle is correct.

The basic psuedocode within Puzzle.solve() is outlined below:
        - While still solving:
            - Increment to the next square.
            - If at the end of puzzle:
                - If correct, add solution.
                - If incorrect, backtrack to previous position.
            - Check possibilities for current square.
            - If there are 0 options, backtrack to previous position.
            - If there are 2 options, mark a backtracking spot and keep going with other option.
            - If there is 1 option:
                - If it's an empty or a black, place it.
                - If it's a clue :
                    - If it's correct, place it.
                    - If it's incorrect, backtrack.

If the puzzles earching for every solution, it will exit this loop once there are no more backtracking spots. Otherwise it will exit after the first solution.

Within the Puzzle class, there are few other methods:

| Method | Explaination |
| --- | --- |
| implement_starting_squares() | If enforced, this will pre-pend the correct values: Black values until the given starting square, then add an Across and Down value. If this is not enforced, adjust the pointer slightly (so that the 'increment to the next square' puts you at the first square). |
| mark_backtrack_spot() | Adds the current pointer to a list of spots (splits) where there were multiple options for a single square. |
| backtrack() | Grab the most recently added backtrack spot, and undo the puzzle up until that point. Then add a black square (instead of whatever value was first implemented) and continue on. |
| set_black_square() | This will place a black square at the pointer. It will also check if symmetry is enforced, and that the pointer is in the 'can place' zone. If so, it will place black squares in the corresponding symetrical location(s). |
| check_options() | described above, is meant to return all the possible options for a single square based on the current grid values. |

## Symmetry

When symmetry is enforced, it tends to speed up the process signficantly. For each black square placed, the solver will be able to place one (or more) symmetrical black squares as well.

So in order to speed up the process during solving, for each type of symmetry we need to determine two different 'zones', one where we place black squares and one where ONLY symmetrically mirrored squares are placed based on the first zone. If the pointer is in the 'can place' zone, then it will place a black square in that zone, and the corresponding black squares in the symetrical location(s).

Each type of symmetry has their own class, initialized with the size of the grid. Each of these classes have two methods:

| Method | Explaination |
| --- | --- |
| can_place(pointer) | returns True or False if the pointer is in the 'can place' zone, the first zone described above. |
| sym_pointer(pointer) | returns a list of the corresponding symmetrical location(s) for the given pointer. |

This solver allows for a few different kinds of symmetry, laid out here:

| Type | Explaination |
|---|---|
| Rotational | Also known as Standard Crossword Symmetry or 180˚ Rotational Symmetry, every white and black square has a counterpart by spinning a half turn about it's central point. |
| Left Right | Also known as mirror symmetry, every white and black square has a counterpart across the puzzle's central vertical axis. |
| Up Down | Every white and black square has a counterpart across the puzzle's central horizontal axis. |
| Diagonal (Top Left Start) | Every white and black square has a mirror counterpart across the puzzle's diagonal axis, from the top left to the bottom right. |
| Diagonal (Top Right Start) | Every white and black square has a mirror counterpart across the puzzle's diagonal axis, from the top right to the bottom left. |
| Dual Rotational | Building on Rotational Symmetry, every white and black square has counterparts by spinning a quarter turn, a half turn, and a three quarter turn about it's central point. |
| Three Way | Left Right, Up Down and Rotational Symmetries, all combined. With the exception of the central row and column, every white and black square has three symmetrical counterparts. |
| Super | Left Right, Up Down, Rotational, Dual Rotational and both Diagonal Symmetries, all combined. |
| Asymmetry | No Symmetry. |
