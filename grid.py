from value import Value, SYMBOLS, CLUES


class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = {}
        self.pRow = 0
        self.pCol = 0
        self.initialize_grid()

    @property
    def pointer(self):
        return (self.pRow, self.pCol)

    def initialize_grid(self):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                key = (i, j)
                self.grid[key] = Value.UNKNOWN

    def set(self, value):
        self.grid[(self.pRow, self.pCol)] = value

    def set_at(self, value, pointer):
        self.grid[pointer] = value

    def is_end_of_grid(self):
        return self.pRow >= self.size[0]

    def is_end_of_row(self):
        return self.pCol == self.size[1] - 1

    def is_end_of_col(self):
        return self.pRow >= self.size[0] - 1

    def is_interconnected(self):
        '''
        in_group = set()
        Get first non black square, add to in group
        for value in in_group:
            For U1, D1, L1, R1:
                if val is not black and not in in_group:
                    add pointer to in_group

        for each value in the grid,
            if its a clue,
                if its not in in_group
                    return false

        return True
        '''
        connected_group = set()
        row, col = 0, 0
        while self.get_at((row, col)) != Value.BLACK:
            col += 1

        connected_group.add((row, col))
        print(self.get_at((row, col)))
        return True

    def increment(self):
        if self.pCol < self.size[0]-1:
            self.pCol += 1
        else:
            self.pCol = 0
            self.pRow += 1

    def decrement(self):
        if self.pCol > 0:
            self.pCol -= 1
        else:
            self.pRow -= 1
            self.pCol = self.size[1]-1

    def return_grid(self, with_numbers=False):
        grid_string = ''
        clue_counter = 1
        for r in range(self.size[0]):
            for c in range(self.size[1]):
                if not with_numbers:
                    grid_string += SYMBOLS[self.grid[(r, c)]] + ' '
                else:
                    sym = self.grid[(r, c)]
                    if sym in CLUES:
                        grid_string += str(clue_counter).zfill(2) + ' '
                        clue_counter += 1
                    else:
                        grid_string += SYMBOLS[self.grid[(r, c)]] * 2 + ' '
            grid_string += '\n'

        return grid_string

    def values_in_row(self):
        vals = set()
        for i in range(self.size[1]):
            vals.add(self.get_at((self.pRow, i)))
        return vals

    def values_in_col(self):
        vals = set()
        for i in range(self.size[0]):
            vals.add(self.get_at((i, self.pCol)))
        return vals

    def at(self):
        return self.grid.get((self.pRow, self.pCol))

    def get_at(self, pointer):
        return self.grid.get(pointer)

    def equals(self, value):
        return value == self.at()

    def u1(self):
        return self.grid.get((self.pRow-1, self.pCol), Value.BLACK)

    def u2(self):
        return self.grid.get((self.pRow-2, self.pCol), Value.BLACK)

    def u3(self):
        return self.grid.get((self.pRow-3, self.pCol), Value.BLACK)

    def d1(self):
        return self.grid.get((self.pRow+1, self.pCol), Value.BLACK)

    def d2(self):
        return self.grid.get((self.pRow+2, self.pCol), Value.BLACK)

    def d3(self):
        return self.grid.get((self.pRow+3, self.pCol), Value.BLACK)

    def l1(self):
        return self.grid.get((self.pRow, self.pCol-1), Value.BLACK)

    def l2(self):
        return self.grid.get((self.pRow, self.pCol-2), Value.BLACK)

    def l3(self):
        return self.grid.get((self.pRow, self.pCol-3), Value.BLACK)

    def r1(self):
        return self.grid.get((self.pRow, self.pCol+1), Value.BLACK)

    def r2(self):
        return self.grid.get((self.pRow, self.pCol+2), Value.BLACK)

    def r3(self):
        return self.grid.get((self.pRow, self.pCol+3), Value.BLACK)
