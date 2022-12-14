inp1 = """noop
noop
addx 5
addx 29
addx -28
addx 5
addx -1
noop
noop
addx 5
addx 12
addx -6
noop
addx 4
addx -1
addx 1
addx 5
addx -31
addx 32
addx 4
addx 1
noop
addx -38
addx 5
addx 2
addx 3
addx -2
addx 2
noop
addx 3
addx 2
addx 5
addx 2
addx 3
noop
addx 2
addx 3
noop
addx 2
addx -32
addx 33
addx -20
addx 27
addx -39
addx 1
noop
addx 5
addx 3
noop
addx 2
addx 5
noop
noop
addx -2
addx 5
addx 2
addx -16
addx 21
addx -1
addx 1
noop
addx 3
addx 5
addx -22
addx 26
addx -39
noop
addx 5
addx -2
addx 2
addx 5
addx 2
addx 23
noop
addx -18
addx 1
noop
noop
addx 2
noop
noop
addx 7
addx 3
noop
addx 2
addx -27
addx 28
addx 5
addx -11
addx -27
noop
noop
addx 3
addx 2
addx 5
addx 2
addx 27
addx -26
addx 2
addx 5
addx 2
addx 4
addx -3
addx 2
addx 5
addx 2
addx 3
addx -2
addx 2
noop
addx -33
noop
noop
noop
noop
addx 31
addx -26
addx 6
noop
noop
addx -1
noop
addx 3
addx 5
addx 3
noop
addx -1
addx 5
addx 1
addx -12
addx 17
addx -1
addx 5
noop
noop
addx 1
noop
noop"""

def read_input(inp):
    X = 1
    values = [X]
    for line in inp.splitlines():
        if line.startswith('noop'):
            values.append(X)
        elif line.startswith('addx'):
            to_add = int(line.split()[-1])
            values.extend([X, X])
            X += to_add
    return values

# Part 1
def sum_signal_strength(inp):
    values = read_input(inp)
    cycles = [20, 60, 100, 140, 180, 220]
    res = 0
    for i, val in enumerate(values):
        if i in cycles:
            res += i* val
    return res

print(sum_signal_strength(inp1))


# Part 2
def crt(inp):
    values = read_input(inp)
    for i in range(240):
        val = values[i+1]
        if val - 1 <= (i%40) <= val + 1:
            print('#', end='')
        else:
            print('.', end='')
        if (i+1) % 40 == 0:
            print('')
    
crt(inp1)
