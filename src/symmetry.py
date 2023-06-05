from abc import ABC, abstractmethod


class Symmetry(ABC):
    """Abstract base class for defining the structure of Symmetry."""

    def __init__(self, name):
        """Initializes the Symmetry object.

        Args:
            name (str): The name of the Symmetry object.
        """
        self.name = name

    @abstractmethod
    def can_place(self, pointer):
        """
        Determines black square can be placed at the pointer with symmetry.

        Args:
            pointer (tuple[int, int]): The starting (row, col) index of the word.

        Returns:
            bool: True if the black square can be placed, False otherwise.
        """
        pass

    @abstractmethod
    def sym_pointer(self):
        """Returns the symmetrical pointer(s) for a given pointer in a list.

        Args:
            pointer (tuple[int, int]): The (row, col) index of the pointer.

        Returns:
            list[tuple[int, int]]: A list of symmetrical pointers.
        """
        pass

    def __repr__(self):
        """Returns the name of the Symmetry object.

        Returns:
            str: The name of the Symmetry object.
        """
        return self.name


class Asymmetry(Symmetry):
    """
    No symmetry
    """

    def __init__(self, dimensions):
        super().__init__("Asymmetry")
        self.rows, self.columns = dimensions

    def can_place(self, pointer):
        return True

    def sym_pointer(self, pointer):
        return [(pointer)]


class LeftRightSym(Symmetry):
    """
    Also known as mirror symmetry, every white and black square
    has a counterpart across the puzzle's central vertical axis.
    """

    def __init__(self, dimensions):
        super().__init__("Left Right")
        self.rows, self.columns = dimensions

    def can_place(self, pointer):
        row_pointer, col_pointer = pointer
        return col_pointer <= (self.columns - 1) / 2

    def sym_pointer(self, pointer):
        row_pointer, col_pointer = pointer
        return [(row_pointer, self.columns - 1 - col_pointer)]


class UpDownSym(Symmetry):
    """
    Every white and black square has a counterpart
    across the puzzle's central horizontal axis.
    """

    def __init__(self, dimensions):
        super().__init__("Up Down")
        self.rows, self.columns = dimensions

    def can_place(self, pointer):
        row_pointer, col_pointer = pointer
        return row_pointer <= (self.rows - 1) / 2

    def sym_pointer(self, pointer):
        row_pointer, col_pointer = pointer
        return [(self.rows - 1 - row_pointer, col_pointer)]


# uds = UpDownSym((9,9))
# pointer = (4,8)
# print(uds.can_place(pointer))
# print(uds.sym_pointer(pointer))


class RotationalSym(Symmetry):
    """
    Also known as Standard Crossword Symmetry or 180˚ Rotational Symmetry,
    every white and black square has a counterpart by spinning a half turn
    about it's central point.
    """

    def __init__(self, dimensions):
        super().__init__("Rotational")
        self.rows, self.columns = dimensions

    def can_place(self, pointer):
        row_pointer, col_pointer = pointer
        cell_num = row_pointer * self.columns + col_pointer + 1
        return cell_num <= ((self.rows * self.columns) / 2) + 0.5

    def sym_pointer(self, pointer):
        row_pointer, col_pointer = pointer
        return [(self.rows - 1 - row_pointer, self.columns - 1 - col_pointer)]


class DiagonalTLBRSym(Symmetry):
    """
    Every white and black square has a mirror counterpart
    across the puzzle's diagonal axis, from the top left to the bottom right.
    """

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
    """
    Every white and black square has a mirror counterpart
    across the puzzle's diagonal axis, from the top right to the bottom left.
    """

    def __init__(self, dimensions):
        super().__init__("Diagonal TRBL")
        self.rows, self.columns = dimensions

    def can_place(self, pointer):
        row_pointer, col_pointer = pointer
        return col_pointer < self.rows - row_pointer

    def sym_pointer(self, pointer):
        row_pointer, col_pointer = pointer
        return [(self.columns - 1 - col_pointer, self.rows - 1 - row_pointer)]


class DualRotationalSym(Symmetry):
    """
    Building on Rotational Symmetry, every white and black square
    has counterparts by spinning a quarter turn, a half turn,
    and a three quarter turn about it's central point.
    """

    def __init__(self, dimensions):
        super().__init__("Dual Rotational")
        self.rows, self.columns = dimensions

    def can_place(self, pointer):
        row_pointer, col_pointer = pointer
        if (row_pointer <= (self.rows - 1) / 2) and col_pointer <= (
            self.columns - 1
        ) / 2:
            return row_pointer <= col_pointer
        elif (row_pointer <= ((self.rows - 1) / 2) - 1) and col_pointer >= (
            self.columns - 1
        ) / 2:
            return self.columns - col_pointer - 1 > row_pointer
        else:
            return False

    def sym_pointer(self, pointer):
        row_pointer, col_pointer = pointer
        return [
            (col_pointer, self.rows - 1 - row_pointer),
            (self.rows - 1 - row_pointer, self.columns - 1 - col_pointer),
            (self.columns - 1 - col_pointer, row_pointer),
        ]


class ThreeWaySym(Symmetry):
    """
    Left Right, Up Down and Rotational Symmetries, all combined.
    With the exception of the central row and column, every white
    and black square has three symmetrical counterparts.
    """

    def __init__(self, dimensions):
        super().__init__("Three Way")
        self.rows, self.columns = dimensions

    def can_place(self, pointer):
        row_pointer, col_pointer = pointer
        return (
            row_pointer <= (self.rows - 1) / 2 and col_pointer <= (self.columns - 1) / 2
        )

    def sym_pointer(self, pointer):
        row_pointer, col_pointer = pointer
        return [
            (row_pointer, self.columns - 1 - col_pointer),
            (self.rows - 1 - row_pointer, self.columns - 1 - col_pointer),
            (self.rows - 1 - row_pointer, col_pointer),
        ]


class SuperSym(Symmetry):
    """
    Left Right, Up Down, Rotational, Dual Rotational
    and both Diagonal Symmetries, all combined.
    """

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
        return [
            (row_pointer, self.columns - 1 - col_pointer),
            (col_pointer, self.rows - 1 - row_pointer),
            (self.columns - 1 - col_pointer, self.rows - 1 - row_pointer),
            (self.rows - 1 - row_pointer, self.columns - 1 - col_pointer),
            (self.rows - 1 - row_pointer, col_pointer),
            (self.columns - 1 - col_pointer, row_pointer),
            (col_pointer, row_pointer),
        ]
