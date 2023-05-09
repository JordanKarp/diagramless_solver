from abc import ABC, abstractmethod


class Symmetry(ABC):
    def __init__(self, name):
        self.name = type

    @abstractmethod
    def can_place(self):
        pass

    @abstractmethod
    def sym_pointer(self):
        pass


class Asymmetry(Symmetry):
    def __init__(self, dimensions):
        super().__init__("Asymmetry")
        self.rows, self.columns = dimensions

    def can_place(self, pointer):
        return True

    def sym_pointer(self, pointer):
        return [(pointer)]


class LeftRightSym(Symmetry):
    def __init__(self, dimensions):
        super().__init__("Left Right")
        self.rows, self.columns = dimensions

    def can_place(self, pointer):
        row_pointer, col_pointer = pointer
        return col_pointer <= (self.columns-1) / 2

    def sym_pointer(self, pointer):
        row_pointer, col_pointer = pointer
        return [(row_pointer, self.columns - 1 - col_pointer)]


class UpDownSym(Symmetry):
    def __init__(self, dimensions):
        super().__init__("Up Down")
        self.rows, self.columns = dimensions

    def can_place(self, pointer):
        row_pointer, col_pointer = pointer
        return row_pointer < (self.columns-1) / 2

    def sym_pointer(self, pointer):
        row_pointer, col_pointer = pointer
        return [(self.rows - 1 - row_pointer, col_pointer)]


class RotationalSym (Symmetry):
    def __init__(self, dimensions):
        super().__init__("Rotational")
        self.rows, self.columns = dimensions

    def can_place(self, pointer):
        row_pointer, col_pointer = pointer
        cell_num = row_pointer * self.columns + col_pointer + 1
        return cell_num <= ((self.rows * self.columns) / 2)

    def sym_pointer(self, pointer):
        row_pointer, col_pointer = pointer
        return [(self.rows - 1 - row_pointer,
                 self.columns - 1 - col_pointer)]


class DiagonalTLBRSym (Symmetry):
    def __init__(self, dimensions):
        super().__init__("Diagonal TLBR")
        self.rows, self.columns = dimensions

    def can_place(self, pointer):
        row_pointer, col_pointer = pointer
        return col_pointer >= row_pointer

    def sym_pointer(self, pointer):
        row_pointer, col_pointer = pointer
        return [(col_pointer, row_pointer)]


class DiagonalTRBLSym(Symmetry):
    def __init__(self, dimensions):
        super().__init__("Diagonal TRBL")
        self.rows, self.columns = dimensions

    def can_place(self, pointer):
        row_pointer, col_pointer = pointer
        return col_pointer < self.rows - row_pointer

    def sym_pointer(self, pointer):
        row_pointer, col_pointer = pointer
        return [(self.columns - 1 - col_pointer,
                 self.rows - 1 - row_pointer)]


class DualRotationalSym(Symmetry):
    def __init__(self, dimensions):
        super().__init__("Dual Rotational")
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


class ThreeWaySym(Symmetry):
    '''Left Right Symmetry, Up Down Symmetry, and Rotational Symmetry'''

    def __init__(self, dimensions):
        super().__init__("Three Way")
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


class SuperSym(Symmetry):
    '''Left Right, Up Down, Rotational, Dual Rotational and both Diagonal Symmetries'''

    def __init__(self, dimensions):
        super().__init__("Super")
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
