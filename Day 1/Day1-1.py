# infile = '/home/richard/PycharmProjects/AdventOfCode2022/Day 1/sample-1'
infile = '/home/richard/PycharmProjects/AdventOfCode2022/Day 1/input.txt'
elves = []
with open(infile) as f:
    e = []
    for line in f:
        l = line.strip()
        if l:
            e.append(int(l))
        else:
            elves.append(e)
            e = []
    elves.append(e)

ec = []
for e in elves:
    ec.append(sum(e))

print(sum(sorted(ec)[-3:]))