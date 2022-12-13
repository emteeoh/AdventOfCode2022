# https://github.com/wimglenn/advent-of-code-data
from aocd.models import Puzzle
from itertools import chain

puzzle = Puzzle(year=2022, day=8)
#lines = puzzle.example_data.split('\n')
lines = puzzle.input_data.split('\n')

trees = []
for line in lines:
    t = [ int(l) for l in line]
    trees.append(t)
forestSizeX, forestSizeY = len(trees), len(trees[0])
visible = [[0 for y in range(forestSizeY)] for x in range(forestSizeX)]


for x in range(forestSizeX):
    visible[x][0] = 1
    visible[x][-1] = 1
visible[0] = [1]*forestSizeY
visible[-1] = [1]*forestSizeY

# scan left to right
for x in range(1, forestSizeX - 1):
    maxYVal = trees[x][0]
    for y in range(1, forestSizeY - 1):
        if trees[x][y] > maxYVal:
            visible[x][y] = 1
            maxYVal = trees[x][y]
# scan right to left
for x in range(1, forestSizeX - 1):
    maxYVal = trees[x][-1]
    for y in range(forestSizeY - 2, 0, -1):
        if trees[x][y] > maxYVal:
            visible[x][y] = 1
            maxYVal = trees[x][y]
# scan top to bottom
for y in range(1, forestSizeY - 1):
    maxXVal = trees[0][y]
    for x in range(1, forestSizeX -1):
        if trees[x][y] > maxXVal:
            visible[x][y] = 1
            maxXVal = trees[x][y]
# scan bottom to top
for y in range(1, forestSizeY - 1):
    maxXVal = trees[-1][y]
    for x in range(forestSizeX - 2, 0, -1):
        if trees[x][y] > maxXVal:
            visible[x][y] = 1
            maxXVal = trees[x][y]
print(sum(chain(*visible)))


puzzle.answer_a = sum(chain(*visible))
# puzzle.answer_b =
