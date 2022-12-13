# https://github.com/wimglenn/advent-of-code-data
from aocd.models import Puzzle
from itertools import chain

puzzle = Puzzle(year=2022, day=8)
# lines = puzzle.example_data.split('\n')
lines = puzzle.input_data.split('\n')

trees = []
for line in lines:
    t = [int(l) for l in line]
    trees.append(t)
forestSizeX, forestSizeY = len(trees), len(trees[0])

scenicPartials = [[[1 for y in range(forestSizeY)] for x in range(forestSizeX)] for direction in "WENS"]
for x in range(forestSizeX):
    scenicPartials[0][x][0] = 0
    scenicPartials[1][x][-1] = 0
for y in range(forestSizeY):
    scenicPartials[2][0][y] = 0
    scenicPartials[3][-1][y] = 0

# look left
for x in range(forestSizeX):
    for y in range(2, forestSizeY):
        see = 0
        yy = y-1
        while yy >= 0:
            see += 1
            if trees[x][y] <= trees[x][yy]:
                break
            yy -= 1
        scenicPartials[0][x][y] = see

# look right
for x in range(forestSizeX):
    for y in range(forestSizeY-3, -1, -1):
        see = 0
        yy = y+1
        while yy < forestSizeY:
            see += 1
            if trees[x][y] <= trees[x][yy]:
                break
            yy += 1
        scenicPartials[1][x][y] = see


# look up
for y in range(forestSizeY):
    for x in range(2, forestSizeX):
        see = 0
        xx = x-1
        while xx >= 0:
            see += 1
            if trees[x][y] <= trees[xx][y]:
                break
            xx -= 1
        scenicPartials[2][x][y] = see

# look down
for y in range(forestSizeY):
    for x in range(forestSizeX-3, -1, -1):
        see = 0
        xx = x+1
        while xx < forestSizeX:
            see += 1
            if trees[x][y] <= trees[xx][y]:
                break
            xx += 1
        scenicPartials[3][x][y] = see
# print()
# for x in range(forestSizeX):
#     print(f"{scenicPartials[0][x]} {scenicPartials[1][x]} {scenicPartials[2][x]} {scenicPartials[3][x]}")

scenicScore = [[1 for y in range(forestSizeY)] for x in range(forestSizeX)]
for x in range(forestSizeX):
    for y in range(forestSizeY):
        for d in range(4):
            scenicScore[x][y] *= scenicPartials[d][x][y]

# for x in range(forestSizeX):
#     print(scenicScore[x])

print(max(chain(*scenicScore)))


puzzle.answer_b = max(chain(*scenicScore))
