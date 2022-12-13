from statemachine import *

# states = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1]]
states = range(4,9)
combos = [(x, y) for x in states for y in ['UP', 'DOWN', 'LEFT', 'RIGHT']]
print(combos)

for xx, dd in combos:
    print(xx, dd)
    startState = xx
    endState = statemachine[(xx,dd)]
    tdelta = tchange[(xx,dd)]
    print(tdelta)
    print(drawGrids([startState, endState]))
