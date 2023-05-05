

class Asymmetry:
    def __init__(self, dimensions):
        self.name = "Asymmetry"
        self.dimensions = dimensions

    def can_place(self, pointer):
        return True

    def sym_pointer(self, pointer):
        return [(pointer)]


class LeftRightSym:
    def __init__(self, dimensions):
        self.name = "Left Right"
        self.rows, self.columns = dimensions

    def can_place(self, pointer):
        row_pointer, col_pointer = pointer
        return col_pointer <= (self.columns-1) / 2

    def sym_pointer(self, pointer):
        row_pointer, col_pointer = pointer
        return [(row_pointer, self.columns - 1 - col_pointer)]


class UpDownSym:
    def __init__(self, dimensions):
        self.name = "Up Down"
        self.rows, self.columns = dimensions

    def can_place(self, pointer):
        row_pointer, col_pointer = pointer
        return row_pointer < (self.columns-1) / 2

    def sym_pointer(self, pointer):
        row_pointer, col_pointer = pointer
        return [(self.rows - 1 - row_pointer, col_pointer)]


class RotationalSym:
    def __init__(self, dimensions):
        self.name = "Rotational"
        self.rows, self.columns = dimensions

    def can_place(self, pointer):
        row_pointer, col_pointer = pointer
        cell_num = row_pointer * self.columns + col_pointer + 1
        return cell_num <= ((self.rows * self.columns) / 2)

    def sym_pointer(self, pointer):
        row_pointer, col_pointer = pointer
        return [(self.rows - 1 - row_pointer,
                 self.columns - 1 - col_pointer)]


class DiagonalTLBRSym:
    def __init__(self, dimensions):
        self.name = "Diagonal TLBR"
        self.rows, self.columns = dimensions

    def can_place(self, pointer):
        row_pointer, col_pointer = pointer
        return col_pointer >= row_pointer

    def sym_pointer(self, pointer):
        row_pointer, col_pointer = pointer
        return [(col_pointer, row_pointer)]


class DiagonalTRBLSym:
    def __init__(self, dimensions):
        self.name = "Diagonal TRBL"
        self.rows, self.columns = dimensions

    def can_place(self, pointer):
        row_pointer, col_pointer = pointer
        return col_pointer < self.rows - row_pointer

    def sym_pointer(self, pointer):
        row_pointer, col_pointer = pointer
        return [(self.columns - 1 - col_pointer,
                 self.rows - 1 - row_pointer)]


class DualRotationalSym:
    def __init__(self, dimensions):
        self.name = "Dual Rotational"
        self.rows, self.columns = dimensions

    def can_place(self, pointer):
        row_pointer, col_pointer = pointer
        if (row_pointer <= (self.rows - 1) / 2) and col_pointer <= (self.columns - 1) / 2:
            return row_pointer <= col_pointer
        elif (row_pointer <= ((self.rows - 1) / 2) - 1) and col_pointer >= (self.columns - 1) / 2:
            return self.columns - col_pointer - 1 > row_pointer
        else:
            return False

    def sym_pointer(self, pointer):
        row_pointer, col_pointer = pointer
        return [(col_pointer, self.rows - 1 - row_pointer),
                (self.rows - 1 - row_pointer, self.columns - 1 - col_pointer),
                (self.columns - 1 - col_pointer, row_pointer)]


class ThreeWaySym:
    '''Left Right Symmetry, Up Down Symmetry, and Rotational Symmetry'''

    def __init__(self, dimensions):
        self.name = "Three Way"

        self.rows, self.columns = dimensions

    def can_place(self, pointer):
        row_pointer, col_pointer = pointer
        if (row_pointer <= (self.rows - 1) / 2) and col_pointer <= (self.columns - 1) / 2:
            return True
        else:
            return False

    def sym_pointer(self, pointer):
        row_pointer, col_pointer = pointer
        return [(row_pointer, self.columns - 1 - col_pointer),
                (self.rows - 1 - row_pointer, self.columns - 1 - col_pointer),
                (self.rows - 1 - row_pointer, col_pointer)]


class SuperSym:
    '''Left Right, Up Down, Rotational, Dual Rotational and both Diagonal Symmetries'''

    def __init__(self, dimensions):
        self.name = "Super"
        self.rows, self.columns = dimensions

    def can_place(self, pointer):
        row_pointer, col_pointer = pointer
        if (row_pointer <= (self.rows - 1) / 2) and col_pointer <= (self.columns - 1) / 2:
            return row_pointer <= col_pointer
        else:
            return False

    def sym_pointer(self, pointer):
        row_pointer, col_pointer = pointer
        return [(row_pointer, self.columns - 1 - col_pointer),
                (col_pointer, self.rows - 1 - row_pointer),
                (self.columns - 1 - col_pointer, self.rows - 1 - row_pointer),
                (self.rows - 1 - row_pointer, self.columns - 1 - col_pointer),
                (self.rows - 1 - row_pointer, col_pointer),
                (self.columns - 1 - col_pointer, row_pointer),
                (col_pointer, row_pointer)]
