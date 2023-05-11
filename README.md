# Diagramless Crossword Solver

A diagramless crossword puzzle is similar to a (American-style) crossword puzzle and folllows all the same rules. However the locations of the clue numbers and shaded (BLACK) squares are unspecified. Essentially, you're provided a blank grid and clues.

A human diagramless crossword solver must deduce two things:
1. The word answers to individual clues
2. The locations to the specific clue numbers, shaded (BLACK) squares, and empty squares.

This builder tackles ONLY the second part, without considering clues or clue answers whatsoever. It will soley look at the clue numbers and whether they are an Across (A) clue, a Down (D) clue, or both (Z).

Look at the 3x3 and 4x4 puzzles as examples below, where the only info we have is the clues' orientation and the size of the grid:

~~~
Across +  Down  +  Empty Grid    ->         Solution
  1         1        _ _ _            1 2 3          Z D D
  4         2        _ _ _       ->   4 - -    or    A - -
  5         3        _ _ _            5 - -          A - -
~~~

~~~
 Across +  Down  +  Empty Grid   ->         Solution
  1         1        _ _ _ _          ▇ 1 2 3       ▇ Z D D
  4         2        _ _ _ _     ->   4 - - -   or  Z - - -
  5         3        _ _ _ _          5 - - -       A - - -
  6         4        _ _ _ _          6 - - ▇       A - - ▇
~~~

Diagramless crossword puzzles tend to give some hints, which can be added as parameters:
    - Does the puzzle have symmetry?
    - What is the starting location of the first clue?

There are also solver details, as a way to customize the builder for this puzzle.

## How to use:

Run main.py
Choose a puzzle from a given library, from an online archive of crosswords, or input one of your own.
Choose solver details, deciding which rules to enforce.
Run!

## Solver Details
There are a few options we can toggle while solving a particular puzzle, toggled by a True or False:
- <ins>use_symmetry</ins>:         Enforce the puzzle's symmetry.
- <ins>use_starting_square</ins>:  Enforce the puzzle's starting square.
- <ins>find_all</ins>:             Find every single solution.
- <ins>use_interconnected</ins>:   Enforce that every clue 'connects' to every other clue.
- <ins>show_numbers</ins>:         Show the clue numbers in the final solution (versus the clue values).
- <ins>debug</ins>:                Every iteration, print out the grid and some useful info. Can also be used as visualization.

## Symmetries
Most crosswords exhibit 'Rotational' symmetry, however this solver allows for a few different kinds of symmetry, laid out here:
- Rotational: Also known as Standard Crossword Symmetry or 180˚ Rotational Symmetry, every white and black square has a counterpart by spinning a half turn about it's central point.
- Left Right: Also known as mirror symmetry, every white and black square has a counterpart across the puzzle's central vertical axis.
- Up Down: Every white and black square has a counterpart across the puzzle's central horizontal axis.
- Diagonal (Top Left Start): Every white and black square has a mirror counterpart across the puzzle's diagonal axis, from the top left to the bottom right.
- Diagonal (Top Right Start): Every white and black square has a mirror counterpart across the puzzle's diagonal axis, from the top right to the bottom left.
- Dual Rotational: Building on Rotational Symmetry, every white and black square has counterparts by spinning a quarter turn, a half turn, and a three quarter turn about it's central point.
- Three Way: Left Right, Up Down and Rotational Symmetries, all combined. With the exception of the central row and column, every white and black square has three symmetrical counterparts.
- Super: Left Right, Up Down, Rotational, Dual Rotational and both Diagonal Symmetries, all combined.
- Asymmetry: No Symmetry.

## More info
- Check out the tech_breakdown.md for a bit more info about how this program works.
- Check out the background.md for a bit of my personal experience with this problem.

## TODO
- [ ] Move Grid.is_interconnected so that it checks more frequently.
- [ ] Add JPZ support.
- [ ] Add IPUZ support.
- [ ] Add PUZ support.
- [ ] Add sorting/organization to the puzzle library.
