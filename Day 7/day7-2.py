# https://github.com/wimglenn/advent-of-code-data
from aocd.models import Puzzle


class DirTree:
    def __init__(self, name, parent=None, root=None):
        self.name = name
        self.files = dict()
        self.subdirs = dict()
        if parent:
            self.parent = parent
        else:
            self.parent = self
        if root:
            self.root = root
        else:
            self.root = self
        self.size = 0

    def addFile(self, name, size):
        self.files[name] = size

    def addSubDir(self, name):
        self.subdirs[name] = DirTree(name, self, self.root), 0

    def cd(self, name):
        if name == '..':
            return self.parent
        elif name == '/':
            return self.root
        else:
            return self.subdirs[name][0]

    def calcSizes(self, wdir):
        tt = 0
        for s in wdir.subdirs.values():
            tt += self.calcSizes(s[0])
        for f in wdir.files.values():
            tt += f
        wdir.size = tt
        return tt

root = DirTree('/')
puzzle = Puzzle(year=2022, day=7)
example_data = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
#lines = example_data.split('\n')
lines = puzzle.input_data.split('\n')
currd = root
for l in lines:
    ll = l.split(' ')
    if ll[0] == '$':
        # it's a command
        if ll[1] == 'cd':
            currd = currd.cd(ll[2])
        # ignore ls commands
    elif ll[0] == 'dir':
        currd.addSubDir(ll[1])
    else:
        currd.addFile(ll[1], int(ll[0]))
root.calcSizes(root)




def dfs2(wdir):
    tt = 0
    for s in wdir.subdirs.values():
        tt += dfs2(s[0])
    if wdir.size <= 100000:
        tt += wdir.size
    return tt


def dfs3(wdir):
    dirsizes = []
    for s in wdir.subdirs.values():
        dirsizes += dfs3(s[0])
    dirsizes.append(wdir.size)
    return dirsizes

# puzzle.answer_a = weirdtotal
print(dfs2(root))
freeSpace = 70000000 - root.size
needSpace = 30000000 - freeSpace
print(f"Used space: {root.size}")
print(f"Free space: {freeSpace}")
print(f"needed space: {needSpace}")

d = dfs3(root)
b = min([s for s in d if s >= needSpace])
print(sorted(d))
print(b)
puzzle.answer_b = b
