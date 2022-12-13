from aocd.models import Puzzle


def isRepeats(s):
    counts = dict()
    for ii in s:
        counts[ii] = 1
    if len(counts.keys()) == len(s):
        return False
    else:
        return True


puzzle = Puzzle(year=2022, day=6)
#lines = puzzle.example_data.split('\n')
lines = puzzle.input_data.split('\n')
l = lines[0]
mlem = 14
for i in range(len(l)-mlem):
    if not isRepeats(l[i:i+mlem]):
        ff = i + mlem
        break
print(ff)



# puzzle.answer_a = ff
puzzle.answer_b = ff