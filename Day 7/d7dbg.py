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


puzzle = Puzzle(year=2022, day=7)
lines = puzzle.input_data.split('\n')
currd = []
dirs = set()
for l in lines:
    ll = l.split(' ')
    if ll[0] == '$':
        # it's a command
        if ll[1] == 'cd':
            if ll[2] == '..':
                currd.pop()
            elif ll[2] == '/':
                currd = []
            else:
                currd.append(ll[2])
            print('/'+'/'.join(currd))
            dirs.add('/'+'/'.join(currd))
    elif ll[0] == 'dir':
        # currd.addSubDir(ll[1])
        pass
    else:
        # currd.addFile(ll[1], int(ll[0]))
        pass

print(len(dirs))
