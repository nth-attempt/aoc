inp1 = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

from itertools import zip_longest
from ast import literal_eval

def read_input(inp):
    pairs = [[]]
    for line in inp.splitlines():
        if line:
            pairs[-1].append(literal_eval(line))
        else:
            pairs.append([])
    return pairs

# Part 1

def is_ordered(left, right, level=0):
    if isinstance(left, int):
        left = [left]
    elif isinstance(right, int):
        right = [right]
    # print(f'{level*" "}- Compare {left} vs {right}')
    for l, r in zip_longest(left, right, fillvalue=-1):
        # print(f'{(level+1)*" "}- Compare {l} vs {r}')
        if l == -1:
            return 0
        elif r == -1:
            return 1
        if isinstance(l, int) and isinstance(r, int) and l != r:
            return 0 if l < r else 1
        if isinstance(l, list) or isinstance(r, list):
            val = is_ordered(l, r, level+1)
            if val != 2: return val
    return 2

def sum_indices(inp):
    pairs = read_input(inp)
    res = 0
    for i, (left, right) in enumerate(pairs, start=1):
        # print(f'== Pair {i} ==')
        if is_ordered(left, right) == 0:
            res += i
        # print()
    return res
        
print(sum_indices(inp1))


# Part 2

from itertools import chain 

class Comparator(tuple):
    def __lt__(self, other):
        return is_ordered(self, other) == 0

def decoder_signal(inp):
    pairs = read_input(inp)
    packets = list(chain.from_iterable(pairs)) + [[[2]]] + [[[6]]]
    packets.sort(key=Comparator)
    # print(*packets, sep='\n')
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

print(decoder_signal(inp1))
