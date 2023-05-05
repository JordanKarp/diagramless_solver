import requests


def nyt_converter():
    '''This will access github of NYT crossword puzzles, and pull the needed info into the solver'''
    print('This will pull a crossword puzzle from a github of NY Times puzzles.')
    month, day, year = input(
        'Please enter a date from 01/01/1977 - 10/30/2016 in MM/DD/YYYY: ').split('/')
    month = month.zfill(2)
    day = day.zfill(2)

    # Link to the github with NYT crossword puzzles in JSON format
    CROSSWORD_URL = f'https://raw.githubusercontent.com/doshea/nyt_crosswords/master/{year}/{month}/{day}.json'

    request = requests.get(CROSSWORD_URL)
    # If the website exists:
    if request.status_code == 404:
        # If no JSON puzzle is available, quit.
        print('No crossword available, please try again')
        raise SystemExit

    r = request.json()

    # Get the puzzle size
    puzzle_size = (r['size']['rows'], r['size']['cols'])

    # Get list of across numbers
    across_nums = []
    for clue_pair in r['clues']['across']:
        num, _ = clue_pair.split('. ', 1)
        across_nums.append(int(num))

    # Get list of down numbers
    down_nums = []
    for clue_pair in r['clues']['down']:
        num, _ = clue_pair.split('. ', 1)
        down_nums.append(int(num))

    # Convert lists of across and down numbers into a clue set string
    clue_set_str = clue_set_converter(across_nums, down_nums)

    # Get starting cell number
    starting_cell_counter = 0
    while r['gridnums'][starting_cell_counter] != 1:
        starting_cell_counter += 1
    starting_cell = starting_cell_counter + 1

    # Return the puzzle with the given parameters
    puzzle_name = Puzzle(puzzle_size, clue_set_str,
                         input_symmetry, starting_cell, input_find_all)
    return puzzle_name
