
class Converter():
    def process_cluestring(self, across_nums, down_nums):
        total_clues = max(across_nums)
        cluestring = ''
        for num in range(1, total_clues+1):
            if num in across_nums and num in down_nums:
                cluestring += 'Z'
            elif num in across_nums:
                cluestring += 'A'
            elif num in down_nums:
                cluestring += 'D'
            else:
                raise IndexError
        return cluestring

    # Not currently using
    def unprocess_cluestring(self, cluestring):
        index = 1
        across_nums = []
        down_nums = []
        for char in cluestring:
            if char in ['Z', 'A']:
                across_nums.append(index)
            if char in ['Z', 'D']:
                down_nums.append(index)
            index += 1
        return across_nums, down_nums
