from value import Value, SYMBOLS, CLUES


class Grid:
    """Responsible for keeping track of the grid and the different values in each location."""

    def __init__(self, size):
        """
        Initializes a new instance of the Grid class.

        Args:
            size (tuple(int, int)): The dimensions of the grid, in  (rows , columns)

        Attributes:
            grid (dict): A dictionary of pointers, representing the locations, on the grid.
            pRow (int): The current pointer row.
            pCol (int): The current pointer column.
        """
        self.size = size
        self.grid = {}
        self.pRow = 0
        self.pCol = 0
        self.initialize_grid()

    @property
    def pointer(self):
        """The pointer for the grid"""
        return (self.pRow, self.pCol)

    def initialize_grid(self):
        """Fill the grid up with unknown Values."""
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                key = (i, j)
                self.grid[key] = Value.UNKNOWN

    def set(self, value):
        """Set the Value to the current pointer equal to value"""
        self.grid[(self.pRow, self.pCol)] = value

    def set_at(self, value, pointer):
        """Set the Value to the given pointer equal to value"""
        self.grid[pointer] = value

    def is_end_of_grid(self):
        """Return True if the pointer is at the end of the grid"""
        return self.pRow >= self.size[0]

    def is_end_of_row(self):
        """Return True if the pointer is at the end of the row"""
        return self.pCol == self.size[1] - 1

    def is_end_of_col(self):
        """Return True if the pointer is at the end of the column"""
        return self.pRow >= self.size[0] - 1

    def is_interconnected(self):
        """Return True if all of the non-black values are connected."""
        connected_group = []
        row, col = 0, 0
        while self.get_at((row, col)) == Value.BLACK:
            col += 1
        connected_group.append((row, col))
        for (row, col) in connected_group:
            if self.get_at((row-1, col)) != Value.BLACK and (row-1, col) not in connected_group:
                connected_group.append((row-1, col))
            if self.get_at((row+1, col)) != Value.BLACK and (row+1, col) not in connected_group:
                connected_group.append((row+1, col))
            if self.get_at((row, col-1)) != Value.BLACK and (row, col-1) not in connected_group:
                connected_group.append((row, col-1))
            if self.get_at((row, col+1)) != Value.BLACK and (row, col+1) not in connected_group:
                connected_group.append((row, col+1))

        for i in range(self.size[0]):
            for j in range(self.size[1]):
                key = (i, j)
                if self.get_at(key) != Value.BLACK and key not in connected_group:
                    return False
        return True

    def increment(self):
        """Move the pointer to the next square"""
        if self.pCol < self.size[0]-1:
            self.pCol += 1
        else:
            self.pCol = 0
            self.pRow += 1

    def decrement(self):
        """Move the pointer to the previous square"""
        if self.pCol > 0:
            self.pCol -= 1
        else:
            self.pRow -= 1
            self.pCol = self.size[1]-1

    def return_grid(self, with_numbers=False):
        """Return a string representation of the grid, with either the Values or the numbers."""
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
        """Returns all of the unique values in the pointer row"""
        vals = set()
        for i in range(self.size[1]):
            vals.add(self.get_at((self.pRow, i)))
        return vals

    def values_in_col(self):
        """Returns all of the unique values in the pointer column"""
        vals = set()
        for i in range(self.size[0]):
            vals.add(self.get_at((i, self.pCol)))
        return vals

    def at(self):
        """Returns the value of the grid at the pointer"""
        return self.grid.get((self.pRow, self.pCol), Value.BLACK)

    def get_at(self, pointer):
        """Returns the value of the grid at the given pointer"""
        return self.grid.get(pointer, Value.BLACK)

    def equals(self, value):
        """Returns True if the Value at the pointer is equal to the given Value."""
        return value == self.at()

    def u1(self):
        """Return the value of the square one up from the pointer."""
        return self.grid.get((self.pRow-1, self.pCol), Value.BLACK)

    def u2(self):
        """Return the value of the square two up from the pointer."""
        return self.grid.get((self.pRow-2, self.pCol), Value.BLACK)

    def u3(self):
        """Return the value of the square three up from the pointer."""
        return self.grid.get((self.pRow-3, self.pCol), Value.BLACK)

    def d1(self):
        """Return the value of the square one down from the pointer."""
        return self.grid.get((self.pRow+1, self.pCol), Value.BLACK)

    def d2(self):
        """Return the value of the square two down from the pointer."""
        return self.grid.get((self.pRow+2, self.pCol), Value.BLACK)

    def d3(self):
        """Return the value of the square three down from the pointer."""
        return self.grid.get((self.pRow+3, self.pCol), Value.BLACK)

    def l1(self):
        """Return the value of the square one to the left of the pointer."""
        return self.grid.get((self.pRow, self.pCol-1), Value.BLACK)

    def l2(self):
        """Return the value of the square two to the left of the pointer."""
        return self.grid.get((self.pRow, self.pCol-2), Value.BLACK)

    def l3(self):
        """Return the value of the square three to the left of the pointer."""
        return self.grid.get((self.pRow, self.pCol-3), Value.BLACK)

    def r1(self):
        """Return the value of the square one to the right of the pointer."""
        return self.grid.get((self.pRow, self.pCol+1), Value.BLACK)

    def r2(self):
        """Return the value of the square two to the right of the pointer."""
        return self.grid.get((self.pRow, self.pCol+2), Value.BLACK)

    def r3(self):
        """Return the value of the square three to the right of the pointer."""
        return self.grid.get((self.pRow, self.pCol+3), Value.BLACK)
