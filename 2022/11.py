inp1 = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

inp2 = """Monkey 0:
  Starting items: 50, 70, 89, 75, 66, 66
  Operation: new = old * 5
  Test: divisible by 2
    If true: throw to monkey 2
    If false: throw to monkey 1

Monkey 1:
  Starting items: 85
  Operation: new = old * old
  Test: divisible by 7
    If true: throw to monkey 3
    If false: throw to monkey 6

Monkey 2:
  Starting items: 66, 51, 71, 76, 58, 55, 58, 60
  Operation: new = old + 1
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 79, 52, 55, 51
  Operation: new = old + 6
  Test: divisible by 3
    If true: throw to monkey 6
    If false: throw to monkey 4

Monkey 4:
  Starting items: 69, 92
  Operation: new = old * 17
  Test: divisible by 19
    If true: throw to monkey 7
    If false: throw to monkey 5

Monkey 5:
  Starting items: 71, 76, 73, 98, 67, 79, 99
  Operation: new = old + 8
  Test: divisible by 5
    If true: throw to monkey 0
    If false: throw to monkey 2

Monkey 6:
  Starting items: 82, 76, 69, 69, 57
  Operation: new = old + 7
  Test: divisible by 11
    If true: throw to monkey 7
    If false: throw to monkey 4

Monkey 7:
  Starting items: 65, 79, 86
  Operation: new = old + 5
  Test: divisible by 17
    If true: throw to monkey 5
    If false: throw to monkey 0"""

import heapq 
import math
from collections import defaultdict, deque

class Monkey:
    def __init__(self, id):
        self.id = id
        self.items = deque([])
        self.op = '1'
        self.test = []
        self.inspected = 0

    def __str__(self):
        return f"Monkey {self.id}:\n items: {self.items}\n op: {self.op}\n test: {self.test}"

    def inspect(self):
        old = self.items.popleft()
        self.inspected += 1
        return eval(self.op)

def read_input(inp):
    monkeys = {}
    for line in inp.splitlines():
        if line.strip().startswith('Monkey'):
            curr_monkey = int(line.split()[-1][:-1])
            monkeys[curr_monkey] = Monkey(curr_monkey)
        elif line.strip().startswith('Starting'):
            vals = list(map(int, line.split(':')[-1].strip().split(',')))
            monkeys[curr_monkey].items = deque(vals)
        elif line.strip().startswith('Operation'):
            val = line.split('=')[-1].strip()
            monkeys[curr_monkey].op = val
        elif line:
            val = int(line.split()[-1])
            monkeys[curr_monkey].test.append(val)
    return monkeys

def lcm(*integers):
    it = iter(integers)
    res = next(it)
    for x in it:
        res = res * x // math.gcd(res, x)
    return res

# Part 1 and Part 2
def monkey_business(inp, num_rounds=20, part1=True):
    monkeys = read_input(inp)
    N = len(monkeys)
    # mod = math.lcm(*[monkey.test[0] for monkey in monkeys.values()])
    mod = lcm(*[monkey.test[0] for monkey in monkeys.values()])
    for _ in range(num_rounds):
        for i in range(N):
            # print(monkeys[i])
            k =  len(monkeys[i].items)
            for _ in range(k):
                val = monkeys[i].inspect() % mod
                val = val // 3 if part1 else val
                if val % monkeys[i].test[0] == 0:
                    monkeys[monkeys[i].test[1]].items.append(val)
                else:
                    monkeys[monkeys[i].test[2]].items.append(val)
    heap = []
    for i in range(N):
        heapq.heappush(heap, monkeys[i].inspected)
        if len(heap) > 2:
            heapq.heappop(heap)
    return heap[0] * heap[1]



print(monkey_business(inp1, num_rounds=20,  part1=True))
print(monkey_business(inp2, num_rounds=20,  part1=True))

print(monkey_business(inp1, num_rounds=10000,  part1=False))
print(monkey_business(inp2, num_rounds=10000,  part1=False))