#!/usr/bin/env python

pa = {'(': ')', '[': ']', '{': '}', '<': '>'}
"""
    ): 3 points.
    ]: 57 points.
    }: 1197 points.
    >: 25137 points.
"""
sc = {')': 3, ']': 57, '}': 1197, '>': 25137}
sc2 = {')': 1, ']': 2, '}': 3, '>': 4}

score = 0
part2 = []
for line in open('../input'):
    stack = []
    for ch in line.strip():
        if ch in pa:
            stack.append(pa[ch])
        elif ch == stack.pop():
            pass
        else:
            score += sc[ch]
            break
    else:
        lc = 0
        for ch in reversed(stack):
            lc *= 5
            lc += sc2[ch]
        if lc:
            part2.append(lc)
part2.sort()
print("part 1:", score)
print("part 2:", part2[len(part2) // 2])
