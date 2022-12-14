inp1 = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

from collections import defaultdict

def read_input(inp):
    rocks = set()
    last_y = defaultdict(int)
    for line in inp.splitlines():
        pairs = map(lambda x: tuple(map(int, x.split(','))), line.split(' -> '))
        prev_x, prev_y = None, None
        for x, y in pairs:
            if prev_x is not None:
                min_x, max_x = sorted((x, prev_x))
                min_y, max_y = sorted((y, prev_y))
                for nx in range(min_x, max_x+1):
                    for ny in range(min_y, max_y+1):
                        rocks.add((nx, ny))
                        last_y[nx] = max(last_y[nx], ny)
            prev_x, prev_y = x, y
    return rocks, last_y

# Part 1
def units_of_sand(inp):
    rocks, last_y = read_input(inp)
    sand = 500, 0
    sx, sy = sand
    units = 0
    while True:
        blocked = True
        for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
            if (sx+dx, sy+dy) not in rocks:
                sx, sy = sx+dx, sy+dy
                blocked = False
        if last_y.get(sx, 0) < sy:
                break
        if blocked:
            rocks.add((sx, sy))
            units += 1
            sx, sy = sand
    return units

print(units_of_sand(inp1))

# Part 2

def units_of_sand2(inp):
    rocks, last_y = read_input(inp)
    max_y = max(last_y.values()) + 2
    min_x, max_x = min(last_y.keys()), max(last_y.keys())
    for x in range(min_x-max_y, max_x+max_y):
        rocks.add((x, max_y))
    
    sand = 500, 0
    sx, sy = sand
    units = 0
    while True:
        blocked = True
        for dx, dy in [(0, 1), (-1, 1), (1, 1)]:
            if (sx+dx, sy+dy) not in rocks:
                sx, sy = sx+dx, sy+dy
                blocked = False
        if (sx, sy) in rocks:
            break
        if blocked:
            rocks.add((sx, sy))
            units += 1
            sx, sy = sand
    return units

print(units_of_sand2(inp1))