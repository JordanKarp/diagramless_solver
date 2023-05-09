
import csv

from details import PuzzleDetails
from symmetry import RotationalSym, UpDownSym, LeftRightSym, \
    DiagonalTLBRSym, DiagonalTRBLSym, DualRotationalSym, \
    ThreeWaySym, SuperSym, Asymmetry


# details =   # Slowish but works
#     (14, 14), 'ZDDZDDDDZDDDAAAAAAADADADAADAADADDDZDDAADAADAAADAAAAAAA', False, 0)
# details = PuzzleDetails(
#     (14, 14), 'ZDDZDDDDZDDDAAAAAAADADADAADAADADDDZDDAADAADAAADAAAAAAA', True, 0)
# details = PuzzleDetails(
#     (15, 15), 'ZDDDZDDDDZDDDAAAADDAAAZZDDDZAZZDDDADDAAAZZZDDZZZDDDADDAAAAAA', True, None)
# details = PuzzleDetails(
# (15, 15), 'ZDDDDZDDDZDDAAZAAAADADADAZDDDAAADZDDAZZAZAZADDZDDDAADADDDAADAAAAAAA', False, None)

# SolverCreated 15x15
# 10.2 mil boards, exits with memory error
# details = PuzzleDetails(
# (15, 15), 'ZDDDZDDDDZDDDAAAAADADAADAAADAAZDADDDAADZDDAZDDADADADAADAAAAAAA', False, None)
# 2.2 mil boards 1 sol - 12/6/1988
# details = PuzzleDetails(

#     (15, 15), 'ZDDDDZDDDZDDAAZAAAADADADAZDDDAAADZDDAZZAZAZADDZDDDAADADDDAADAAAAAAA', True, None)
# # 325k boards 1 sol - 10/17/1988
# details = PuzzleDetails( (15, 15),
# 'ZDDDDZDDDZDDDAAAAAAADDAAZDDADDADDDDADAZADDAAAAZDAADADZDDDDDDDZAAAAAAAA', True, None)
# # 1.09 mil boards, 2 sol - 1/1/2000
# details = PuzzleDetails(
#     (15, 15), 'ZDDDDDDDDZDDDAZAAAAAAZDADAADADAAZDDDADAADAAADADDDADDAZAZAADAAAA', False, None)
# # 3.17 mil boards, 2 sol - 11/30/1994
# details = PuzzleDetails(
#     (15, 15), 'ZDDDZDDDDZDDDAAAADDAAAZZDDDZAZZDDDADDAAAZZZDDZZZDDDADDAAAAAA', False, None)
# # 351k boards, 2 sol - 10/31/1986 - solved with sym
# details = PuzzleDetails( (15, 15),
#   'ZDDDZDDDDDZDDAAAAAAADDZDDAAADAADADAADDZDDAADZDDDDADAADADADAAADDDAAAAAA', True, None)
# # 4.26 mil boards, 1 sol -  6/14/1991
# details = PuzzleDetails(
#     (15, 15), 'ZDDDDDZDDDDZDADAAAADAAZZAZZZADZDAZDZAADZDDAZZAZZADADAAAA', False, None)
# details = PuzzleDetails(
#     (15, 15), 'ZDDDZDDDDZDDDAAAADAAADADAZDDDDADDAADAAZZAZZADADADAZDDADDDDAADAAAAAA', False, None)

LIBRARY = [
    ((4, 4), 'ZDDADAA', RotationalSym, 1),
    ((5, 5), 'ZDDZDAAA', RotationalSym, 2),
    ((5, 5), 'ZDDZDAAA', LeftRightSym, 2),
    ((5, 5), 'ZDDADDAAA', UpDownSym, 1),
    ((5, 5), 'ZDDDADAAA', RotationalSym, 1),
    ((6, 6), 'ZDDDZDAAAA', RotationalSym, 3),
    # NonContinguous solution
    ((7, 7), 'ZDDDDDAAAZDDAA', Asymmetry, 1),
    # NonContinguous solution
    ((7, 7), 'ZDDAAZDDDAAA', Asymmetry, 5),
    ((7, 7), 'ZDDDAAADDDAAA', RotationalSym, 1),
    ((7, 7), 'ZDDDAAADDDAAA', Asymmetry, 1),
    ((7, 7), 'ZDDDADZDAAAA', RotationalSym, 3),
    ((7, 7), 'ZDDDADZDAAAA', RotationalSym, 2),
    ((7, 7), 'ZDDADDZDAAAA', RotationalSym, 3),
    ((7, 7), 'ZDDZDDAAADAAAAAA', UpDownSym, 1),

    ((8, 8), 'ZDDDDAAADDDAAAA', RotationalSym, 1),
    ((8, 8), 'ZDDZDDDAAADAADDZDDDAAAA', RotationalSym, 1),

    ((9, 9), 'ZDDZDDAAADDDAZDAADDAAAA', DiagonalTRBLSym, 1),

    ((10, 10), 'ZDDDZDDDDADAAAAZDDDDDAAAA', RotationalSym, 1),
    ((13, 13),
     'ZDDDZDDZDDDAAAAADADAAZZDDZDDDAZAADDZDAZZDDZDDDADAAAAAAA', RotationalSym, 1),
    ((14, 14),
     'ZDDZDDDDZDDDAAAAAAADADADAADAADADDDZDDAADAADAAADAAAAAAA', RotationalSym, 1),
    ((17, 17), 'ZDDDDDDZDZDZADZADAAZADAAAAAAADZADZAAADZZDZDAAAA', LeftRightSym, 6),
    ((11, 11), 'ZDDDDDDZDZDAAAAAAADZADZADAA', RotationalSym, 1),
    ((15, 15), 'ZDDDDZDDDZDDAAZAAAADADADAZDDDAAADZDDAZZAZAZADDZDDDAADADDDAADAAAAAAA',
     RotationalSym, 1),
    ((9, 9), 'ZDDAAZDDADZDDAADAADAA', DualRotationalSym, 3),
    ((17, 17), 'ZDDDDDDDADZDDAZDAAADADAAADAZDDDAADZDADADAADAAZADZDDAZAZADAADAAA',
     DualRotationalSym, 7),
    ((9, 9), 'ZDDZDDADZAAADAZDDDDDAAAAAA', ThreeWaySym, 1),
    ((9, 9), 'ZDDAAZDDDDDAAAAA', SuperSym, 4),
    ((15, 15), 'ZDDDDDDDDDDZDZDAAAAADZADDDDDAZDDDZADZADADZADDDDDAA', ThreeWaySym, 3),
    ((11, 11), 'ZDDZDDDZDAAZADAAADDZDAAADAA', SuperSym, 5)
]

SYM_DICT = {
    None: 'None',
    RotationalSym: 'Rotational',
    UpDownSym: 'Up Down',
    LeftRightSym: 'Left Right',
    DiagonalTRBLSym: 'Diagonal TRBL',
    DiagonalTLBRSym: 'Diagonal TLBR',
    DualRotationalSym: 'Dual Rotation',
    ThreeWaySym: 'Three Way',
    SuperSym: 'Super',
    Asymmetry: 'Asymmetry'
}

PUZZLE_LIST_FILE = 'puzzle_list.csv'


class PuzzleLibrary:
    def __init__(self):
        self.puz_list = LIBRARY
        # self.puz_list = []
        # self.puz_list = self.load_puzzle_list(PUZZLE_LIST_FILE)
        # self.show_and_pick()

    def load_puzzle_list(self, file_path):
        '''Open the puzzle.csv file and print out the possible puzzle choices'''
        puzzle_list = []
        with open(file_path) as csvfile:
            lib_file = csv.reader(csvfile, delimiter=',')
            num_puzzles = 0
            puzzle_list = []
            for row in lib_file:
                num_puzzles += 1
                rows = int(row[0])
                cols = int(row[1])
                clue_str = row[2]
                sym = row[3]
                st_sq = int(row[4])
                puz = ((rows, cols), clue_str, sym, st_sq)
                puzzle_list.append(puz)
                # print(puz)

    def show_and_pick(self):
        header = '\tSize \t\t  Sym \t\t  Start\t  Clues'
        print(header)
        print('-' * len(header) * 2)
        for num, (size, clues, sym, start) in enumerate(self.puz_list, 1):
            print(
                f'{num}.\t{size[0]}x{size[1]}\t| {SYM_DICT[sym].ljust(12)}\t| {start}\t| {clues}')

        # TODO Add validation
        choice = input('Which puzzle? ')
        size, clues, sym, start = self.puz_list[int(choice)-1]
        print(size, clues, sym, start)
        return PuzzleDetails(size, clues, sym, start)


# pl = PuzzleLibrary()
