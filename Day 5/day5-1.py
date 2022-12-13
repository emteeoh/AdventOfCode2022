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

for (qty,source,destination) in moves:
    for i in range(qty):
        crates[destination].insert(0, crates[source].pop(0))
top = "".join([ crates[t][0] for t in sorted(crates.keys()) ])
print(top)

# for line in puzzle.input_data.split():
puzzle.answer_a = top
# puzzle.answer_b = overlap
