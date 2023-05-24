# Diagramless Crossword Solver

A diagramless crossword puzzle is similar to a (American-style) crossword puzzle and follows all the same rules. However the locations of the clue numbers and shaded (BLACK) squares are unspecified. Essentially, you're provided a blank grid and clues.

A human diagramless crossword solver must deduce two things:

1. The word answers to individual clues
2. The locations to the specific clue numbers, shaded (BLACK) squares, and empty squares.

## This builder tackles ONLY the second part, without considering clues or clue answers whatsoever, in order to build the entire crossword grid

It will soley look at the clue numbers and whether they are an Across (A) clue, a Down (D) clue, or both (Z)

Look at the 3x3 and 4x4 puzzles as examples below, where the only info we have is the clues' orientation and the size of the grid:

~~~text
Across +  Down  +  Empty Grid    ->         Solution
  1         1        _ _ _            1 2 3          Z D D
  4         2        _ _ _       ->   4 - -    or    A - -
  5         3        _ _ _            5 - -          A - -
~~~

~~~text
 Across +  Down  +  Empty Grid   ->         Solution
  1         1        _ _ _ _          ▇ 1 2 3       ▇ Z D D
  4         2        _ _ _ _     ->   4 - - -   or  Z - - -
  5         3        _ _ _ _          5 - - -       A - - -
  6         4        _ _ _ _          6 - - ▇       A - - ▇
~~~

Diagramless crossword puzzles tend to give some hints, which can be added as parameters:
    - Does the puzzle have symmetry?
    - What is the starting location of the first clue?

This program can take these inputs, and return all possible grid solutions for the given puzzle.

There are also solver details, as a way to customize the builder.

## How to use

- Run main.py
- Choose a puzzle from a given library, from an online archive of crosswords, or input one of your own.
- Choose solver details, deciding which rules to enforce.
- Run!

## Solver Details

There are a few options we can toggle while solving a particular puzzle, toggled by a True or False:

| Options             | Explaination |
| ---                 | ------ |
| use_symmetry        | Enforce the puzzle's symmetry. |
| use_starting_square | Enforce the puzzle's starting square. |
| find_all            | Find every single solution. |
| use_interconnected  | Enforce that every clue 'connects' to every other clue. |
| show_numbers        | Show the clue numbers in the final solution (versus the clue values). |
| debug               | Every iteration, print out the grid and some useful info. Can also be used as visualization. |

## More info

- Check out the Tech Breakdown for a bit more info about how this program works.
- Check out the Bbackground for a bit of my personal experience with this problem.

## TODO

- [ ] Clean up documentation
- [ ] Move .is_interconnected call so that it checks more frequently.
- [ ] Add sorting/organization to the puzzle library.
- [ ] Add multiple sources to the puzzle library.
- [ ] Add JPZ import support.
- [ ] Add IPUZ import support.
- [ ] Add PUZ import support.
