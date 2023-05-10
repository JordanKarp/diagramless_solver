tester = ["1. Songs author", "6. Triangular lyre", "10. Airplane stairway"]


new_list = [int(num) for num, _ in (clue.split('.', 1) for clue in tester)]
print(new_list)
