inp1 ="""30373
25512
65332
33549
35390"""

def construct_grid(inp):
    grid = []
    for line in inp.splitlines():
        grid.append(list(map(int, line)))
    return grid

# Part 1

def num_visible(inp):
    grid = construct_grid(inp)
    R, C = len(grid), len(grid[0])
    top = [[-1]*C for _ in range(R)]
    left = [[-1]*C for _ in range(R)]
    right = [[-1]*C for _ in range(R)]
    bottom = [[-1]*C for _ in range(R)]

    for c in range(1, C):
        top[1][c] = grid[0][c]
        bottom[~1][c] = grid[~0][c]

    for r in range(1, R):
        left[r][1] = grid[r][0]
        right[r][~1] = grid[r][~0]

    for r in range(1, R):
        for c in range(1, C):
            top[r][c] = max(top[r-1][c], grid[r-1][c])
            left[r][c] = max(left[r][c-1], grid[r][c-1])
            bottom[~r][c] = max(bottom[~(r-1)][c], grid[~(r-1)][c])
            right[r][~c] = max(right[r][~(c-1)], grid[r][~(c-1)])

    # print(*grid, sep='\n', end='\n\n')
    # print(*top, sep='\n', end='\n\n')
    # print(*bottom, sep='\n', end='\n\n')
    # print(*left, sep='\n', end='\n\n')
    # print(*right, sep='\n', end='\n\n')

    res = 0
    for r in range(R):
        for c in range(C):
            if any(grid[r][c] > ele for ele in (top[r][c],  left[r][c], bottom[r][c], right[r][c])):
                res += 1
    return res

print(num_visible(inp1))

# Part 2

def highest_score(inp):
    grid = construct_grid(inp)
    R, C = len(grid), len(grid[0])
    res = 0
    for r in range(1, R-1):
        for c in range(1, C-1):
            left = right = top = bottom = 0
            for rr in range(r-1, -1, -1):
                top += 1
                if grid[rr][c] >= grid[r][c]: break
            for rr in range(r+1, R):
                bottom += 1
                if grid[rr][c] >= grid[r][c]: break
            for cc in range(c-1, -1, -1):
                left += 1      
                if grid[r][cc] >= grid[r][c]: break
            for cc in range(c+1, C):
                right += 1       
                if grid[r][cc] >= grid[r][c]: break
            res = max(res, left*right*top*bottom)
    return res

print(highest_score(inp1))

# With numpy

import numpy as np
def solve(inp):
    grid = np.array([list(line) for line in inp.splitlines()], int)
    part1 = np.zeros_like(grid)
    part2 = np.ones_like(grid)
    for _ in range(4):
        for x, y in np.ndindex(grid.shape):
            lower = [val < grid[x, y] for val in grid[x, y+1:]]
            part1[x ,y] |= all(lower)
            part2[x, y] *= next((i+1 for i, l in enumerate(lower) if ~l), len(lower))
        grid, part1, part2 = map(np.rot90, (grid, part1, part2))
    return part1.sum(), part2.max()

print(solve(inp1))