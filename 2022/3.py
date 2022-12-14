inp1 = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

# Part 1

import string

def sum_priorities(inp):
    score = {ch: i+1 for i, ch in enumerate(string.ascii_letters)}
    res = 0
    for line in inp.splitlines():
        seen = set(line[:len(line)//2])
        for ch in line[len(line)//2:]:
            if ch in seen:
                res += score[ch]
                break
    return res


print(sum_priorities(inp1))


# Part 2

from collections import Counter

def sum_priorities2(inp):
    score = {ch: i+1 for i, ch in enumerate(string.ascii_letters)}
    res = 0
    counts = Counter()
    for i, line in enumerate(inp.splitlines()):
        if (i+1) % 3 == 0:
            for ch in line:
                if counts[ch] == 2:
                    res += score[ch]
                    break
            counts = Counter()
        else:
            counts.update(set(line))

    return res


print(sum_priorities2(inp1))
