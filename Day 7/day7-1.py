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

    def childDirGrew(self, name, size):
        self.size = self.size - self.subdirs[name][1] + size
        self.subdirs[name] = self.subdirs[name][0], size
        if self != self.parent:
            self.parent.childDirGrew(self.name, size)

    def addFile(self, name, size):
        self.files[name] = size
        self.size += size
        if self != self.parent:
            self.parent.childDirGrew(self.name, size)

    def addSubDir(self, name):
        self.subdirs[name] = DirTree(name, self, self.root), 0

    def ls(self):
        d = [f"dir {dd} size {self.subdirs[dd][1]}" for dd in sorted(self.subdirs.keys())]
        f = [f"file {ff} size {self.files[ff]}" for ff in sorted(self.files.keys())]
        return "\n".join(d+f)

    def cd(self, name):
        if name == '..':
            return self.parent
        elif name == '/':
            return self.root
        else:
            return self.subdirs[name][0]


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
# lines = example_data.split('\n')
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



def dfs(wdir):
    tt = 0
    for s in wdir.subdirs.values():
        tt += dfs(s[0])
    for f in wdir.files.values():
        tt += f
    wdir.size = tt
    return tt

def dfs2(wdir):
    tt = 0
    for s in wdir.subdirs.values():
        tt += dfs2(s[0])
    if wdir.size <= 100000:
        tt += wdir.size
    return tt


# puzzle.answer_a = weirdtotal
# puzzle.answer_b =
print(dfs(root))
print(dfs2(root))
puzzle.answer_a = dfs2(root)