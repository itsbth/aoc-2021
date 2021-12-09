#!/usr/bin/env python3
from itertools import permutations

displays = []

with open('../input') as f:
    for line in f:
        head, tail = line.split(' | ')
        displays.append((head.strip().split(' '), tail.strip().split(' ')))

key = ('abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg',
       'abdefg', 'acf', 'abcdefg', 'abcdfg')


def lookup(tr, num):
    fixed = ''.join(sorted(num.translate(tr)))
    return key.index(fixed)


sum = 0

for head, tail in displays:
    for per in permutations('abcdefg'):
        tr = str.maketrans(''.join(per), 'abcdefg')
        # print(head)
        if all(''.join(sorted(v.translate(tr))) in key for v in head):
            val = int(''.join(str(lookup(tr, v)) for v in tail))
            sum += val

print("Part 2:", sum)
