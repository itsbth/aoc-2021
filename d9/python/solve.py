from functools import reduce
from operator import mul

adj = ((1, 0), (-1, 0), (0, 1), (0, -1))

map = {}

for x, r in enumerate(open('../input')):
    for y, v in enumerate(r.strip()):
        map[(x, y)] = int(v)

s = 0
lp = []
for (x, y), v in map.items():
    if all(map.get((x+dx, y+dy), 10) > v for (dx, dy) in adj):
        s += v + 1
        lp.append((x, y))
print("part 1: ", s)


def floodfill(x, y):
    area = set()
    candidates = [(x, y)]
    while candidates:
        (x, y) = candidates.pop()
        area.add((x, y))
        for (dx, dy) in adj:
            if (x+dx, y+dy) not in area and map.get((x+dx, y+dy), 9) != 9:
                candidates.append((x+dx, y+dy))
    return len(area)


ws = list(sorted((floodfill(x, y) for (x, y) in lp), reverse=True))
print("part 2: ", reduce(mul, ws[:3]))
