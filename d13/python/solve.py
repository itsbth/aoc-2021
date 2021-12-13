from collections import defaultdict

# INPUT = '../sample'
INPUT = '../input'

dots = []

grid = defaultdict(lambda: False)

ff = open(INPUT)
for line in ff:
    if not line.strip():
        break
    x, y = map(int, line.strip().split(','))
    grid[(x, y)] = True


def viz(gr):
    mx = max(x for (x, _) in gr.keys())
    my = max(y for (_, y) in gr.keys())
    for y in range(my+1):
        for x in range(mx+1):
            print('##' if (x, y) in gr else '..', end='')
        print("")


for fi in ff:
    ax, v = fi[len('fold along '):].strip().split('=')
    v = int(v)
    ng = dict()
    if ax == 'x':
        for (x, y), b in grid.items():
            if x < v:
                ng[(x, y)] = b
            else:
                ng[(-x + 2*v, y)] = b
    elif ax == 'y':
        for (x, y), b in grid.items():
            if y < v:
                ng[(x, y)] = b
            else:
                ng[(x, -y + 2*v)] = b
    grid = ng

# viz(grid)
# print('---')
viz(ng)
# print(ng)
print("Part 1:", len(ng))
