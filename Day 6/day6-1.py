from aocd.models import Puzzle
from itertools import permutations

def isRepeats(s):
    counts = dict()
    for i in s:
        counts[i] = 1
    if len(counts.keys()) == 4:
        return False
    else:
        return True


puzzle = Puzzle(year=2022, day=6)
#lines = puzzle.example_data.split('\n')
lines = puzzle.input_data.split('\n')
f = -1
l = lines[0]
# print(l)
# for i in range(0, len(l)-4):
#     if len(set(permutations(l[i:i+4], 2))) == 12:
#         print(l[i:i+4])
#         f = i + 4
#         break
# ff = -1
for i in range(len(l)-4):
    if not isRepeats(l[i:i+4]):
        ff = i + 4
        break
print(ff)



puzzle.answer_a = ff
# puzzle.answer_b =