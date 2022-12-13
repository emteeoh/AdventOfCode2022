# https://github.com/wimglenn/advent-of-code-data
from aocd.models import Puzzle
from itertools import chain


def overlappedRange(start1, end1, start2, end2):
    """do the ranges overlap?"""
    return (start1 <= start2 <= end1) \
        or (start1 <= end2 <= end1) \
        or (start2 <= start1 <= end2) \
        or (start2 <= end1 <= end2)



def containedRange(start1, end1, start2, end2):
    def compare(s1, e1, s2, e2):
        return (s1 <= s2) and (e1 >= e2)

    return compare(start1, end1, start2, end2) or compare(start2, end2, start1, end1)


puzzle = Puzzle(year=2022, day=4)
overlap = 0
for line in puzzle.example_data.split():
    l = map(lambda x: x.split('-'), line.split(','))
    ranges = list(map(lambda x: int(x), chain(*l)))
    if overlappedRange(*ranges):
        overlap += 1
print(overlap)

overlap = 0
for line in puzzle.input_data.split():
    l = map(lambda x: x.split('-'), line.split(','))
    ranges = list(map(lambda x: int(x), chain(*l)))
    if overlappedRange(*ranges):
        overlap += 1
print(overlap)
puzzle.answer_b = overlap
