inp1 = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

def read_input(inp):
    for line in inp.splitlines():
        interval1, interval2 = line.split(",")
        yield list(map(int, interval1.split('-'))) + list(map(int, interval2.split('-')))

# Part 1
def contains_interval(inp):
    res = 0
    for s1, e1, s2, e2 in read_input(inp):
        if (s2 >= s1 and e2 <= e1) or (s1 >= s2 and e1 <= e2):
            res += 1
    return res

print(contains_interval(inp1))


# Part 2
def is_overlap(inp):
    res = 0
    for s1, e1, s2, e2 in read_input(inp):
        if not ((s2 > s1 and s2 > e1) or (s1 > s2 and s1 > e2)):
            res += 1
    return res

print(is_overlap(inp1))