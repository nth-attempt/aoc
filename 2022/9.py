inp1 = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

inp2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

# Part 1
def num_positions(inp):
    directions = {
        'L': (-1, 0),
        'R': (1, 0),
        'U': (0, 1),
        'D': (0, -1),
    }
    hx = hy = tx = ty = 0
    seen = {(tx, ty)}
    for line in inp.splitlines():
        dir, moves = line.split()
        mx, my = directions[dir]
        for _ in range(1, int(moves)+1):
            hx, hy = hx+mx, hy+my
            dx, dy = hx-tx, hy-ty
            if abs(dx) <=1 and abs(dy) <= 1:
                continue
            tx = tx if dx == 0 else tx+dx//abs(dx)
            ty = ty if dy == 0 else ty+dy//abs(dy)
            seen.add((tx, ty))
    return len(seen)

print(num_positions(inp1))
print(num_positions(inp2))

# Part 2
def num_positions2(inp):
    directions = {
        'L': (-1, 0),
        'R': (1, 0),
        'U': (0, 1),
        'D': (0, -1),
    }
    pos = [[0, 0] for _ in range(10)] 
    seen = {tuple(pos[-1])}
    for line in inp.splitlines():
        dir, moves = line.split()
        mx, my = directions[dir]
        for _ in range(1, int(moves)+1):
            pos[0] = [pos[0][0]+mx, pos[0][1]+my]
            for i in range(1, 10):
                dx, dy =  pos[i-1][0] - pos[i][0], pos[i-1][1] - pos[i][1]
                if abs(dx) <= 1 and abs(dy) <= 1:
                    break
                pos[i][0] = pos[i][0] if dx == 0 else (pos[i][0]+dx//abs(dx))
                pos[i][1] = pos[i][1] if dy == 0 else (pos[i][1]+dy//abs(dy))
                if i == 9:
                   seen.add(tuple(pos[-1]))
    return len(seen)

print(num_positions2(inp1))
print(num_positions2(inp2))