from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=3)
atoz = ''.join([chr(i) for i in range(ord('a'), ord('z')+1)])
AtoZ = ''.join([chr(i) for i in range(ord('A'), ord('Z')+1)])
priority = ' ' + atoz + AtoZ
score = 0
group = []
for line in puzzle.input_data.split():
    group.append(line)
    if len(group)==3:
        badge = set(group[0]).intersection(set(group[1])).intersection(set(group[2])).pop()
        score += priority.index(badge)
        group = []
print(score)
puzzle.answer_b = score
