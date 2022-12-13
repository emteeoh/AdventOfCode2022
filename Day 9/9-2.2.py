from aocd.models import Puzzle


knots = [(0, 0) for k in range(10)]
spots = [set( (0,0) ) for k in range(10)]


def norm(x):
    if x == 0:
        return 0
    else:
        return x // abs(x)


def mover(dx, dy):
    knots[0] = (knots[0][0] + dx, knots[0][1] + dy)
    spots[0].add(knots[0])
    for k in range(1, 10):
        move = (knots[k-1][0] - knots[k][0], knots[k-1][1] - knots[k][1])
        delta = (norm(move[0]), norm(move[1]))
        if abs(move[0]) > 1 or abs(move[1]) > 1:
            if k == 1 and move == (2,-1):
                print('up-left', end='')
            if k == 1 and move == (2,0):
                print('up', end='')
            if k == 1 and move == (2,1):
                print('upp-right', end='')
            if k == 1 and move == (-2,-1):
                print('down-left', end='')
            if k == 1 and move == (-2,0):
                print('down', end='')
            if k == 1 and move == (-2,1):
                print('down-right', end='')
            if k == 1 and move == (-1,-2):
                print('down-left', end='')
            if k == 1 and move == (0,-2):
                print('down', end='')
            if k == 1 and move == (1,-2):
                print('down-right', end='')
            if k == 1 and move == (-1,2):
                print('up-left', end='')
            if k == 1 and move == (0,2):
                print('up', end='')
            if k == 1 and move == (1,2):
                print('up-right', end='')

            if k == 1 and move == (2,2):
                print('up-right', end='')
            if k == 1 and move == (2,-2):
                print('up-left', end='')
            if k == 1 and move == (-2,2):
                print('down-right', end='')
            if k == 1 and move == (-2,-2):
                print('down-left', end='')
            knots[k] = (knots[k][0] + delta[0], knots[k][1] + delta[1])
            spots[k].add(knots[k])
        else:
            if k == 1:
                print('no move', end='')
        if k == 1:
            print()


def up():
    print('up ', end='')
    mover(0, 1)


def down():
    print('down ', end='')
    mover(0, -1)


def left():
    print('left ', end='')
    mover(-1, 0)


def right():
    print('right ', end='')
    mover(1, 0)


example_data = '''R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2'''

example2_data = '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''


puzzle = Puzzle(year=2022, day=9)
commands = [line.split(' ') for line in puzzle.input_data.split('\n')]
# commands = [line.split(' ') for line in example2_data.split('\n')]
print(commands)
for c in range(len(commands)):
    commands[c][1] = int(commands[c][1])

counts = 0
for c in commands:
    if c[0] == 'U':
        counts += c[1]
        for ii in range(c[1]):
            up()
    if c[0] == 'D':
        counts += c[1]
        for ii in range(c[1]):
            down()
    if c[0] == 'L':
        counts += c[1]
        for ii in range(c[1]):
            left()
    if c[0] == 'R':
        counts += c[1]
        for ii in range(c[1]):
            right()
print(f'head: {len(spots[0])}   Counts: {counts}')
print(f'2 knots: {len(spots[1])}')
print(f'10 knots: {len(spots[9])}')


puzzle.answer_a = len(spots[1])-1
puzzle.answer_b = len(spots[9])
