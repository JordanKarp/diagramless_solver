from value import Value


class ClueSet():
    def __init__(self, clue_string):
        self.clue_string = clue_string
        self.clueset = self.process_clueset(self.clue_string)
        self.clue_pointer = 0

    def equals(self, value):
        return value == self.at()

    def increment(self):
        self.clue_pointer += 1

    def decrement(self):
        self.clue_pointer -= 1

    def at(self):
        return self.clueset[self.clue_pointer]

    def process_clueset(self, clue_string):
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
