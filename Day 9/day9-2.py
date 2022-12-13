# https://github.com/wimglenn/advent-of-code-data
from aocd.models import Puzzle
from statemachine import *
example_data = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''
puzzle = Puzzle(year=2022, day=9)
lines = puzzle.input_data.split('\n')
# lines = example_data.split('\n')

class Rope:
    def __init__(self, knots):
        self.knots = knots
        self.tails = [0 for k in range(knots)]
        self.spots = set()

    def up(self):
        temptails = []
        for k in range(self.knots):
            if k == 0:
                temptails[0] = statemachine[self.tails[k], 'UP']
            else:
                temptails[k] = statemachine[]


state = 0
tailx, taily = 0, 0
spots = set()
direction = ''
for line in lines:
    command = line.split(' ')
    print(command)
    if command[0] == 'U':
        direction = 'UP'
    if command[0] == 'L':
        direction = 'LEFT'
    if command[0] == 'D':
        direction = 'DOWN'
    if command[0] == 'R':
        direction = 'RIGHT'
    count = int(command[1])
    for s in range(count):
        newstate = statemachine[(state, direction)]
        tailx, taily = tailx + tchange[(state, direction)][0], taily + tchange[(state, direction)][1]
        state = newstate
        spots.add((tailx, taily))
        print(f"({tailx},{taily})")
print(len(spots))

puzzle.answer_a = len(spots)
# puzzle.answer_b =
