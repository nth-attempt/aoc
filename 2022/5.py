inp1 = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

import re 
def read_input(inp):
    lines = inp.splitlines()
    num_stacks = (len(lines[0]) + 1) // 4
    stacks = [[] for _ in range(num_stacks)]
    moves = []
    pattern = " ".join(["(...)"]*num_stacks)
    for line in inp.splitlines():
        if line.startswith("move"):
            m = re.match(r"move (\d+) from (\d+) to (\d+)", line)
            moves.append(tuple(map(int, m.groups())))
        else:
            m = re.match(pattern, line)
            if m:
                for i, grp in enumerate(m.groups()):
                    if not grp.isspace() and grp[0] == '[':
                        stacks[i].append(grp[1])
    stacks = [list(reversed(stack)) for stack in stacks]
    return stacks, moves

# Part 1

def rearragnge(inp):
    stacks, moves = read_input(inp)
    for num, src, dest in moves:
        src, dest = src - 1, dest - 1
        for _ in range(num):
            stacks[dest].append(stacks[src].pop())
    return "".join(stack[-1] for stack in stacks)

print(rearragnge(inp1))

# Part 2

def rearragnge2(inp):
    stacks, moves = read_input(inp)
    for num, src, dest in moves:
        src, dest = src - 1, dest - 1
        tmp_stack = []
        for _ in range(num):
            tmp_stack.append(stacks[src].pop())
        for _ in range(num):
            stacks[dest].append(tmp_stack.pop())
    return "".join(stack[-1] for stack in stacks)

print(rearragnge2(inp1))