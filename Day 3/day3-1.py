from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=3)
atoz = ''.join([chr(i) for i in range(ord('a'), ord('z')+1)])
AtoZ = ''.join([chr(i) for i in range(ord('A'), ord('Z')+1)])
priority = ' ' + atoz + AtoZ
score = 0
for line in puzzle.input_data.split():
    score += priority.index(set(line[0:len(line)//2]).intersection(set(line[len(line)//2:])).pop())
print(score)
puzzle.answer_a = score
