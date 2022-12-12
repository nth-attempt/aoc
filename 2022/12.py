inp1 = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

inp2 = """abccccaaaaaaacccaaaaaaaccccccccccccccccccccccccccccccccccaaaa
abcccccaaaaaacccaaaaaaaaaaccccccccccccccccccccccccccccccaaaaa
abccaaaaaaaaccaaaaaaaaaaaaaccccccccccccccccccccccccccccaaaaaa
abccaaaaaaaaaaaaaaaaaaaaaaacccccccccaaaccccacccccccccccaaacaa
abaccaaaaaaaaaaaaaaaaaacacacccccccccaaacccaaaccccccccccccccaa
abaccccaaaaaaaaaaaaaaaacccccccccccccaaaaaaaaaccccccccccccccaa
abaccccaacccccccccaaaaaacccccccccccccaaaaaaaacccccccccccccccc
abcccccaaaacccccccaaaaaaccccccccijjjjjjaaaaaccccccaaccaaccccc
abccccccaaaaacccccaaaacccccccciiijjjjjjjjjkkkkkkccaaaaaaccccc
abcccccaaaaacccccccccccccccccciiiirrrjjjjjkkkkkkkkaaaaaaccccc
abcccccaaaaaccccccccccccccccciiiirrrrrrjjjkkkkkkkkkaaaaaccccc
abaaccacaaaaacccccccccccccccciiiqrrrrrrrrrrssssskkkkaaaaacccc
abaaaaacaaccccccccccccccccccciiiqqrtuurrrrrsssssskklaaaaacccc
abaaaaacccccccccccaaccccccccciiqqqttuuuurrssusssslllaaccccccc
abaaaaaccccccccaaaaccccccccciiiqqqttuuuuuuuuuuusslllaaccccccc
abaaaaaacccccccaaaaaaccccccciiiqqqttxxxuuuuuuuusslllccccccccc
abaaaaaaccccaaccaaaaacccccchhiiqqtttxxxxuyyyyvvsslllccccccccc
abaaacacccccaacaaaaaccccccchhhqqqqttxxxxxyyyyvvsslllccccccccc
abaaacccccccaaaaaaaacccccchhhqqqqtttxxxxxyyyvvssqlllccccccccc
abacccccaaaaaaaaaaccaaacchhhpqqqtttxxxxxyyyyvvqqqlllccccccccc
SbaaacaaaaaaaaaaaacaaaaahhhhppttttxxEzzzzyyvvvqqqqlllcccccccc
abaaaaaaacaaaaaacccaaaaahhhppptttxxxxxyyyyyyyvvqqqlllcccccccc
abaaaaaaccaaaaaaaccaaaaahhhppptttxxxxywyyyyyyvvvqqqmmcccccccc
abaaaaaaacaaaaaaacccaaaahhhpppsssxxwwwyyyyyyvvvvqqqmmmccccccc
abaaaaaaaaaaaaaaacccaacahhhpppssssssswyyywwvvvvvqqqmmmccccccc
abaaaaaaaacacaaaacccccccgggppppsssssswwywwwwvvvqqqqmmmccccccc
abcaaacaaaccccaaaccccccccgggppppppssswwwwwrrrrrqqqmmmmccccccc
abcaaacccccccccccccccccccgggggpppoosswwwwwrrrrrqqmmmmddcccccc
abccaacccccccccccccccccccccgggggoooosswwwrrrnnnmmmmmddddccccc
abccccccccccccccccccccccccccgggggooossrrrrrnnnnnmmmddddaccccc
abaccccaacccccccccccccccccccccgggfoossrrrrnnnnndddddddaaacccc
abaccaaaaaaccccccccccccccccccccgffooorrrrnnnneeddddddaaaacccc
abaccaaaaaacccccccccccccccccccccfffooooonnnneeeddddaaaacccccc
abacccaaaaaccccccccaaccaaaccccccffffoooonnneeeeccaaaaaacccccc
abcccaaaaacccccccccaaccaaaaccccccffffoooneeeeeaccccccaacccccc
abaccaaaaaccccccccaaaacaaaaccccccafffffeeeeeaaacccccccccccccc
abacccccccccccccccaaaacaaacccccccccffffeeeecccccccccccccccaac
abaaaacccccccaaaaaaaaaaaaaacccccccccfffeeeccccccccccccccccaaa
abaaaacccccccaaaaaaaaaaaaaaccccccccccccaacccccccccccccccccaaa
abaacccccccccaaaaaaaaaaaaaaccccccccccccaacccccccccccccccaaaaa
abaaaccccccccccaaaaaaaaccccccccccccccccccccccccccccccccaaaaaa"""

import string
import collections
import numpy  as np 

def read_input(inp):
    grid = [list(line) for line in inp.splitlines()]
    R, C = len(grid), len(grid[0])
    src = ()
    dst = ()
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'S':
                src = (r, c)
                grid[r][c] = 'a'
            elif grid[r][c] == 'E':
                dst = (r, c)
                grid[r][c] = 'z'
           
    grid = [[ord(ch) - ord('a') for ch in row] for row in grid]
    return grid, src, dst

# Part 1

def min_steps(inp):
    grid, src, dst = read_input(inp)
    R, C = len(grid), len(grid[0])
    directions = [(-1,0), (0,-1), (1,0), (0,1)]

    def is_valid(r, c):
        return 0 <= r < R and 0 <= c < C

    visited = set([src])
    steps = 0
    queue = collections.deque([src])
    while queue:
        n = len(queue)
        steps += 1
        for j in range(n):
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if (is_valid(nr, nc) 
                and (grid[nr][nc] <= grid[r][c] + 1)
                and (nr, nc) not in visited):
                    if (nr, nc) == dst:
                        return steps
                    visited.add((nr, nc))            
                    queue.append((nr, nc))

    return steps

print(min_steps(inp1))
print(min_steps(inp2))

# Part 2

def min_steps2(inp):
    grid, src, dst = read_input(inp)
    R, C = len(grid), len(grid[0])
    directions = [(-1,0), (0,-1), (1,0), (0,1)]

    def is_valid(r, c):
        return 0 <= r < R and 0 <= c < C

    steps = {}
    queue = collections.deque()

    for r in range(R):
        for c in range(C):
            if grid[r][c] == 0:
                queue.append((r, c))
                steps[(r, c)] = 0

    while queue:
        r, c = queue.popleft()
        if (r, c) == dst:
            break
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if (is_valid(nr, nc) 
            and (grid[nr][nc] <= grid[r][c] + 1)
            and (nr, nc) not in steps):
                steps[(nr, nc)] = steps[(r, c)] + 1           
                queue.append((nr, nc))

    return steps[dst]

print(min_steps2(inp1))
print(min_steps2(inp2))
