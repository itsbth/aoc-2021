import sys
from itertools import *
from functools import *
from collections import defaultdict

# INPUT = '../sample'
INPUT = '../input'
# inp = map(int, open(INPUT).read().strip().split(','))
# inp = [[int(n) for n in line.strip()] for line in open(INPUT)]

sys.setrecursionlimit(1624234)

edges = defaultdict(lambda: set())

for line in open(INPUT):
    s, e = line.strip().split('-')
    edges[s].add(e)
    edges[e].add(s)

print(edges)


def dfs(node, seen, hus=False):
    n = 0
    if node == node.lower():
        seen += (node,)
    if node == 'end':
        return 1
    for nn in edges[node]:
        # print(f"{node} -> {nn} [{nn in seen}/{hus}]")
        # print(nn, seen)
        taken = nn in seen
        if taken and (hus or nn in ('start', 'end')):
            continue
        n += dfs(nn, seen, hus or taken)
    return n


print("part 1:", dfs('start', (), True))
print("part 2:", dfs('start', ()))
