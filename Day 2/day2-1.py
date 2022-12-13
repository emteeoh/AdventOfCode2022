#infile = '/home/richard/PycharmProjects/AdventOfCode2022/Day 2/sample'
infile = '/home/richard/PycharmProjects/AdventOfCode2022/Day 2/input.txt'

col1 = {'A':0, 'B':1, 'C':2}
col2 = {'X':1, 'Y':2, 'Z':3}
LOSE = 0
TIE = 3
WIN = 6
score = 0
def rps(p1, p2):
    if p1 == 'A' and p2 == 'X':
        return TIE+1
    if p1 == 'A' and p2 == 'Y':
        return WIN+2
    if p1 == 'A' and p2 == 'Z':
        return LOSE+3
    if p1 == 'B' and p2 == 'X':
        return LOSE+1
    if p1 == 'B' and p2 == 'Y':
        return TIE+2
    if p1 == 'B' and p2 == 'Z':
        return WIN+3
    if p1 == 'C' and p2 == 'X':
        return WIN+1
    if p1 == 'C' and p2 == 'Y':
        return LOSE+2
    if p1 == 'C' and p2 == 'Z':
        return TIE+3

score = 0
with open(infile) as f:
    for line in f:
        l = line.strip().split()
        score += rps(l[0], l[1])
print(score)

