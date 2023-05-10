
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
