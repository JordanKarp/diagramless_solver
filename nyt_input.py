import requests

from converter import Converter
from details import PuzzleDetails
from util import is_num_between
from value import SYMMETRIES


class NYTPuzzleInput():
    '''This will access github of archived NYT crossword puzzles, and pull the needed info into the solver'''

    def __init__(self):
        self.converter = Converter()

    def run(self):
        date = self.get_user_puzzle_date()
        raw_puzzle = self.pull_puzzle(date)
        puzzle = self.parse_puzzle(raw_puzzle)
        return puzzle

    def get_user_puzzle_date(self):
        while True:
            try:
                print('Please enter a numeric date between 1/1/1977 - 12/31/2018')
                month = int(input("Month: "))
                if not is_num_between(month, 1, 12):
                    raise ValueError
                day = int(input("Day: "))
                if not is_num_between(day, 1, 31):
                    raise ValueError
                year = int(input("Year: "))
                if not is_num_between(year, 1977, 2017):
                    raise ValueError

            except ValueError:
                print("Invalid input. Please try again!")
            else:
                return (str(month).zfill(2), str(day).zfill(2), str(year))

    def pull_puzzle(self, date):
        try:
            month, day, year = date
            url = f'https://raw.githubusercontent.com/doshea/nyt_crosswords/master/{year}/{month.zfill(2)}/{day.zfill(2)}.json'
            response = requests.get(url)
            # print(response.status_code)
            response.raise_for_status()
        except Exception as err:
            print('No Puzzle Found')
            print(err)  # Python 3.6
        else:
            return response.json()

    def parse_puzzle(self, puzzle_json):
        p = puzzle_json

        # Get dimensions
        rows = p['size']['rows']
        cols = p['size']['cols']

        # Get list of across and down numbers
        across_nums = [int(num) for num, _ in (clue.split('.', 1)
                                               for clue in p['clues']['across'])]
        down_nums = [int(num) for num, _ in (clue.split('.', 1)
                                             for clue in p['clues']['down'])]

        # Convert clue numbers into cluestring
        cluestring = self.converter.process_cluestring(across_nums, down_nums)

        # Converty symmetry string into Symmetry class
        symmetry = SYMMETRIES['Rotational']

        # Get starting cell number
        i = 0
        while p['gridnums'][i] != 1:
            i += 1
        starting_square = i + 1

        return PuzzleDetails((rows, cols), cluestring, symmetry, starting_square)
