try:
    import requests

    active = True
except ImportError:
    active = False

from converter import process_cluestring
from details import PuzzleDetails
from util import is_num_between
from value import SYMMETRIES

BASE_URL = "https://raw.githubusercontent.com/doshea/nyt_crosswords/master/"


class NYTPuzzleInput:
    """Access Github of archived NYT crossword puzzles, and pull the needed info into the solver"""

    def run(self):
        while active:
            try:
                date = self.get_user_puzzle_date()
                raw_puzzle = self.pull_puzzle(date)
                if raw_puzzle is False:
                    raise ValueError
            except ValueError:
                print("No puzzle on this date, try again.")
            else:
                return self.parse_puzzle(raw_puzzle)
        else:
            print("Requests library not imported.")
            quit()

    def get_user_puzzle_date(self):
        """Prompt the user for a certain puzzle date"""
        while True:
            try:
                print("Please enter a numeric date between 1/1/1977 - 12/31/2018")
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
        """Pull the puzzle from the archive"""
        try:
            month, day, year = date
            URL = f"{BASE_URL}{year}/{month.zfill(2)}/{day.zfill(2)}.json"
            response = requests.get(URL)
            # print(response.status_code)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            # No puzzle found
            return False
        else:
            return response.json()

    def parse_puzzle(self, puzzle_json):
        """Parse the important information from the JSON of the puzzle."""
        p = puzzle_json

        # Get dimensions
        rows = p["size"]["rows"]
        cols = p["size"]["cols"]

        # Get list of across and down numbers
        across_nums = [
            int(num) for num, _ in (clue.split(".", 1) for clue in p["clues"]["across"])
        ]
        down_nums = [
            int(num) for num, _ in (clue.split(".", 1) for clue in p["clues"]["down"])
        ]

        # Convert clue numbers into cluestring
        cluestring = process_cluestring(across_nums, down_nums)

        # Converty symmetry string into Symmetry class
        symmetry = SYMMETRIES["Rotational"]

        # Get starting cell number
        i = 0
        while p["gridnums"][i] != 1:
            i += 1
        starting_square = i + 1

        # Return details
        return PuzzleDetails((rows, cols), cluestring, symmetry, starting_square)
