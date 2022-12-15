inp1 = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

inp2 = """Sensor at x=2391367, y=3787759: closest beacon is at x=2345659, y=4354867
Sensor at x=1826659, y=2843839: closest beacon is at x=1654342, y=3193298
Sensor at x=980874, y=2369046: closest beacon is at x=31358, y=2000000
Sensor at x=2916267, y=2516612: closest beacon is at x=3064453, y=2107409
Sensor at x=3304786, y=844925: closest beacon is at x=3064453, y=2107409
Sensor at x=45969, y=76553: closest beacon is at x=31358, y=2000000
Sensor at x=2647492, y=1985479: closest beacon is at x=2483905, y=2123337
Sensor at x=15629, y=2015720: closest beacon is at x=31358, y=2000000
Sensor at x=3793239, y=3203486: closest beacon is at x=3528871, y=3361675
Sensor at x=3998240, y=15268: closest beacon is at x=4731853, y=1213406
Sensor at x=3475687, y=3738894: closest beacon is at x=3528871, y=3361675
Sensor at x=3993022, y=3910207: closest beacon is at x=3528871, y=3361675
Sensor at x=258318, y=2150378: closest beacon is at x=31358, y=2000000
Sensor at x=1615638, y=1108834: closest beacon is at x=2483905, y=2123337
Sensor at x=1183930, y=3997648: closest beacon is at x=1654342, y=3193298
Sensor at x=404933, y=3377916: closest beacon is at x=1654342, y=3193298
Sensor at x=3829801, y=2534117: closest beacon is at x=3528871, y=3361675
Sensor at x=2360813, y=2494240: closest beacon is at x=2483905, y=2123337
Sensor at x=2286195, y=3134541: closest beacon is at x=1654342, y=3193298
Sensor at x=15626, y=1984269: closest beacon is at x=31358, y=2000000
Sensor at x=3009341, y=3849969: closest beacon is at x=3528871, y=3361675
Sensor at x=1926292, y=193430: closest beacon is at x=1884716, y=-881769
Sensor at x=3028318, y=3091480: closest beacon is at x=3528871, y=3361675"""

import re

def mh_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def read_input(inp):
    sensors = {}
    for line in inp.splitlines():
        matches = re.findall(r'.*x=(-?\d*), y=(-?\d*).*x=(-?\d*), y=(-?\d*)', line)[0]
        sx, sy, bx, by = list(map(int, matches))
        sensors[(sx, sy)] = (bx, by, mh_dist((sx, sy), (bx, by)))
    return sensors

# Part 1

def num_positions(inp, Y):
    sensors = read_input(inp)
    blocked = set()
    for (sx, sy), (bx, by, dist) in sensors.items():
        remaining = dist - abs(Y-sy)
        if remaining >= 0:
            for x in range(sx-remaining, sx+remaining+1):
                if (x, Y) != (bx, by):
                    blocked.add(x)
        else:
            continue
            
    return len(blocked)

print(num_positions(inp1, 10))
print(num_positions(inp2, 2000000))

# Part 2

def tuning_freq(inp, N):
    sensors = read_input(inp)
    for y in range(N+1):
        intervals = []
        for (sx, sy), (bx, by, dist) in sensors.items():
            remaining = dist - abs(y-sy)
            if remaining >= 0:
                intervals.append([max(sx-remaining, 0), min(sx+remaining, N)])
        intervals.sort()
        prev_e = intervals[0][1]
        for s, e in intervals[1:]:
            if s > prev_e + 1:
                return (s-1)*4000000+y
            prev_e = max(e, prev_e)


print(tuning_freq(inp1, 20))
print(tuning_freq(inp2, 4000000))