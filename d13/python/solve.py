# INPUT = '../sample'
INPUT = '../input'

dots = []

grid = set()

ff = open(INPUT)
for line in ff:
    if not line.strip():
        break
    x, y = map(int, line.strip().split(','))
    grid.add((x, y))


def viz(gr):
    mx = max(x for (x, _) in gr)
    my = max(y for (_, y) in gr)
    for y in range(my+1):
        for x in range(mx+1):
            print('##' if (x, y) in gr else '..', end='')
        print("")


first_fold = True

for fi in ff:
    ax, v = fi[len('fold along '):].strip().split('=')
    v = int(v)
    ng = set()
    if ax == 'x':
        for (x, y) in grid:
            if x < v:
                ng.add((x, y))
            else:
                ng.add((-x + 2*v, y))
    elif ax == 'y':
        for (x, y) in grid:
            if y < v:
                ng.add((x, y))
            else:
                ng.add((x, -y + 2*v))
    grid = ng
    if first_fold:
        print("Part 1:", len(ng))
        first_fold = False

print("Part 2:")
viz(ng)
