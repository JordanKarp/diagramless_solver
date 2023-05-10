
import csv

from details import PuzzleDetails
from util import is_num_between
from value import SYMMETRIES


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


PUZZLE_LIST_FILE = 'puzzle_list.csv'


class PuzzleLibrary:
    def __init__(self):
        self.puz_list = self.load_puzzle_list(PUZZLE_LIST_FILE)

    def run(self):
        self.show_library()
        size, clues, sym_str, start = self.choose_puzzle()
        return PuzzleDetails(size, clues, SYMMETRIES[sym_str], start)

    def load_puzzle_list(self, file_path):
        '''Open the puzzle.csv file and print out the possible puzzle choices'''
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
            return puzzle_list

    def show_library(self):
        header = '\tSize \t\t  Sym \t\t  Start\t  Clues'
        print(header)
        print('-' * len(header) * 2)
        for num, (size, clues, sym_str, start) in enumerate(self.puz_list, 1):
            print(
                f'{num}.\t{size[0]}x{size[1]}\t| {sym_str.ljust(12)}\t| {start}\t| {clues}')

    def choose_puzzle(self):
        while True:
            try:
                choice = int(input('Which puzzle? '))
                if not is_num_between(choice, 1, len(self.puz_list)-1):
                    raise ValueError
            except ValueError:
                print("Invalid input. Please try again!")
            else:
                return self.puz_list[int(choice)-1]
