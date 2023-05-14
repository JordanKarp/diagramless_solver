from value import Value


class ClueSet():
    """Responsible for keeping track of a clue pointer, as well as the associated clue Value."""

    def __init__(self, raw_clue_string):
        """
        Initializes a new instance of the ClueSet class.

        Args:
            clue_string (str): A string representation of the clue set.

        Attributes:
            clueset (list): A list of Value objects, representing the clues.
            clue_pointer (int): The current pointer number.
        """
        self.clue_string = raw_clue_string
        self.clueset = self.process_clueset(self.clue_string)
        self.clue_pointer = 0

    def equals(self, value):
        """
        Determines if the specified value is equal to the current clue value.

        Parameters:
            value (Value): The value to compare to the current clue value.

        Returns:
            bool: True if the specified value is equal to the current clue value, False otherwise.
        """
        return value == self.at()

    def increment(self):
        """Increments the current clue pointer by one."""
        self.clue_pointer += 1

    def decrement(self):
        """
        Decrements the current clue pointer by one.
        """
        self.clue_pointer -= 1

    def at(self):
        """
        Returns the value of the current clue pointer.

        Returns:
            Value: The value of the current clue pointer.
        """
        return self.clueset[self.clue_pointer]

    def process_clueset(self, clue_string):
        """
        Processes the input clue string and converts it to a list of Value objects.

        Parameters:
            clue_string (str): The input clue string to be processed.

        Returns:
            list: A list of Value objects corresponding to the input clue string.
        """
        pre_process = list(clue_string)
        new_clueset = []
        for letter in pre_process:
            if letter == "Z":
                new_clueset.append(Value.ACROSSDOWN)
            elif letter == "A":
                new_clueset.append(Value.ACROSS)
            elif letter == "D":
                new_clueset.append(Value.DOWN)
        new_clueset.append(Value.FINAL)
        return new_clueset
