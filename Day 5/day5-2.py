# https://github.com/wimglenn/advent-of-code-data
from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=5)
lines = puzzle.input_data.split('\n')
lineCount = 0
crates = dict()
while lines[lineCount]:
    for col, char in enumerate(lines[lineCount]):
        if char in '[] ':
            continue
        else:
            try:
                crates[(col-1)//4].append(char)
            except KeyError:
                crates[(col - 1) / 4] = [char]
    lineCount += 1
lineCount += 1
newCrates = dict()
for v in crates.values():
    newCrates[int(v[-1])] = v[:-1]
crates = newCrates
moves = []
for line in lines[lineCount:]:
    ls = line.split()
    moves.append([int(ls[1]), int(ls[3]), int(ls[5])])


for (qty, source, destination) in moves:
    dest = crates[destination]
    src = crates[source]
    tomove = src[0:qty]
    nomove = src[qty:]
    crates[destination] = tomove + dest
    crates[source] = nomove

top = "".join([crates[t][0] for t in sorted(crates.keys())])
print(top)
puzzle.answer_b = top
