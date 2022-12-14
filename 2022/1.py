inp1 = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

# Part 1
def max_calories(inp):
    lines = inp.splitlines()
    res = float('-inf')
    count = 0
    for val in lines:
        if val == '':
            res = max(res, count)
            count = 0
        else:
            count += int(val)
    return max(res, count)


print(max_calories(inp1))

# Part 2

import heapq

def sum_top3_calories(inp):
    lines = inp.splitlines()
    count = 0
    h = []
    for val in lines:
        if val == '':
            heapq.heappush(h, count)
            count = 0
        else:
            count += int(val)
        if len(h) > 3:
            heapq.heappop(h)
    heapq.heappush(h, count)
    if len(h) > 3:
        heapq.heappop(h)
    return sum(h)


print(sum_top3_calories(inp1))
