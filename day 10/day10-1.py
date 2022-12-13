# https://github.com/wimglenn/advent-of-code-data
from aocd.models import Puzzle
from itertools import accumulate
from example2 import example2_data



puzzle = Puzzle(year=2022, day=10)
# lines = puzzle.example_data.split('\n')
# lines = example2_data.split('\n')
lines = puzzle.input_data.split('\n')
cycles = [1]
for line in lines:
    cycles.append(0)
    if line == 'noop':
        continue
    else:
        print(line, int(line.split(' ')[1]))
        cycles.append(int(line.split(' ')[1]))

x = list(accumulate(cycles))

for count in range(20, 221, 40):
    print(f'cycle {count} X: {x[count]} signalstrength {count * x[count]}')

tot = sum([count * x[count] for count in range(20, 221, 40)])
print(tot)
# puzzle.answer_a = tot


# puzzle.answer_a = signalStrength
# puzzle.answer_b =
