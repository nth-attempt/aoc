inp1 = """$ cd /
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

class Dir():
    def __init__(self, dir_name, parent_dir=None):
        self.dir_name = dir_name
        self.parent_dir = parent_dir
        self.files = []
        self.sub_dirs = {}

    def print_dir(self, level=0):
        print("  "*level, self.dir_name)
        for size, file in self.files:
             print("  "*(level+1), file, size)
        for sub_dir in self.sub_dirs.values():
            sub_dir.print_dir(level+1)
    
    def file_size(self):
        total = 0
        for size, _ in self.files:
            total += int(size)
        for sub_dir in self.sub_dirs.values():
            total += sub_dir.file_size()
        return total

def read_input(inp):
    lines = inp.splitlines()
    root = Dir(lines[0][5:])
    curr = root
    for line in lines[1:]:
        if not line.startswith("$"):
            if line.startswith("dir"):
                curr.sub_dirs[line[4:]] = Dir(line[4:], curr)
            else:
                curr.files.append(line.split())
        elif line.startswith("$ cd"):
            if line == "$ cd ..":
                curr = curr.parent_dir
            else:
                curr = curr.sub_dirs[line[5:]]
    return root

def iter_directories(root):
    yield root
    for sub_dir in root.sub_dirs.values():
        yield from iter_directories(sub_dir)

# Part 1
def sum_sizes(inp):
    root = read_input(inp)
    # root.print_dir()
    res = 0
    for dir in iter_directories(root):
        size = dir.file_size()
        if size <= 100000:
            res += size
    return res


print(sum_sizes(inp1))

# Part 2
def deleted_directory_size(inp):
    root = read_input(inp)
    remaining = next(iter_directories(root)).file_size() - 40000000
    res = 70000000
    for dir in iter_directories(root):
        size = dir.file_size()
        if size >= remaining: 
            res = min(res, size)
    return res


print(deleted_directory_size(inp1))