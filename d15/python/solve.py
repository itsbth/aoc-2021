from math import inf
from collections import defaultdict
from heapq import heappush, heappop

grid = {(x, y): int(v) for y, line in enumerate(open('../input'))
        for x, v in enumerate(line.strip())}
mx = max(x for x, _ in grid.keys())
my = max(y for _, y in grid.keys())

adj = ((-1, 0), (1, 0), (0, -1), (0, 1))


def risk1(pos):
    return grid[pos]


def risk2(pos):
    xp, xm = divmod(pos[0], mx + 1)
    yp, ym = divmod(pos[1], my + 1)
    return (grid[(xm, ym)] + xp + yp - 1) % 9 + 1


def neighbours1(pos):
    return ((pos[0] + dx, pos[1] + dy) for dx, dy in adj if (pos[0] + dx, pos[1] + dy) in grid)


def neighbours2(pos):
    return ((pos[0] + dx, pos[1] + dy) for dx, dy in adj
            if pos[0] + dx >= 0 and pos[0] + dx < (mx+1) * 5 and pos[1] + dy >= 0 and pos[1] + dy < (my+1) * 5)


def debug(r, t, cf):
    from tc import color
    h = set(t)
    p = t
    while p != (0, 0):
        p = cf[p]
        h.add(p)
    for y in range(t[0] + 1):
        for x in range(t[1] + 1):
            if (x, y) in h or (x, y) == t:
                print(f"{color.BOLD}{risk2((x, y))}{color.END}", end="")
            else:
                print(risk2((x, y)), end="")
        print()


def ds(sp, tgt, risk, neighbours):
    q = [(0, sp)]
    cost = defaultdict(lambda: inf)
    visited = set()
    cf = {}
    while q:
        (d, p) = heappop(q)
        visited.add(p)
        if p == tgt:
            debug(risk, tgt, cf)
            return cost[p]
        for nb in neighbours(p):
            nc = d + risk(nb)
            if nb not in visited and cost[nb] > nc:
                heappush(q, (nc, nb))
                cost[nb] = nc
                cf[nb] = p
    return inf


print("part 1:", ds((0, 0), (mx, my), risk1, neighbours1))
print("part 2:", ds((0, 0), ((mx+1) * 5 - 1, (mx+1) * 5 - 1), risk2, neighbours2))
