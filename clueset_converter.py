class CluesetConverter():
    def process(self, across_clues, down_clues):
        # across_clues, down_clues
        clue_set = []
        for number in range(int(max(across_clues))):
            if number in across_clues and number in down_clues:
                clue_set.append('Z')
            if number in across_clues and number not in down_clues:
                clue_set.append('A')
            if number not in across_clues and number in down_clues:
                clue_set.append('D')
        clue_set_str = ''.join(clue_set)
        return clue_set_str


class CluesetInput():
    def process(self):
        input_across_set = [int(x) for x in input(
            'Input the Across clue numbers, separated by a space: ').split(' ')]
        input_down_set = [int(x) for x in input(
            'Input the Down clue numbers, separated by a space: ').split(' ')]
        return CluesetConverter().process(input_across_set, input_down_set)
