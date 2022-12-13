# https://github.com/wimglenn/advent-of-code-data
from aocd.models import Puzzle
from itertools import chain

'''
def overlap(start1, end1, start2, end2):
    """how much does the range (start1, end1) overlap with (start2, end2)"""
    return max(max((end2-start1), 0) - max((end2-end1), 0) - max((start2-start1), 0), 0)
    '''


def containedRange(start1, end1, start2, end2):
    def compare(s1, e1, s2, e2):
        return (s1 <= s2) and (e1 >= e2)

    return compare(start1, end1, start2, end2) or compare(start2, end2, start1, end1)


puzzle = Puzzle(year=2022, day=4)
# overlap = 0
# for line in puzzle.example_data.split():
#     l = map(lambda x: x.split('-'),line.split(','))
#     ranges = list(chain(*l))
#     if containedRange(*ranges):
#         overlap += 1
# print(overlap)

overlap = 0
for line in puzzle.input_data.split():
    l = map(lambda x: x.split('-'), line.split(','))
    ranges = list(map(lambda x: int(x), chain(*l)))
    if containedRange(*ranges):
        overlap += 1
        print(ranges, containedRange(*ranges))
print(overlap)
puzzle.answer_a = overlap
