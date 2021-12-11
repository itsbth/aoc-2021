# grid = [[int(ch) for ch in line.strip()] for line in open('../sample')]
grid = {(x, y): int(ch) for y, line in enumerate(open('../input'))
        for x, ch in enumerate(line.strip())}
adj = (
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
)


def bump_and_flash(flashed: set, x: int, y: int):
    grid[(x, y)] += 1
    if grid[(x, y)] <= 9:
        return
    # print("---")
    # for gy in range(10):
    #     for gx in range(10):
    #         v = grid[(gx, gy)]
    #         if (x, y) == (gx, gy):
    #             print(f"\033[1m{v}\033[0m", end="")
    #         else:
    #             print(v, end="")
    #     print()
    if (x, y) in flashed:
        return
    flashed.add((x, y))
    for (dx, dy) in adj:
        nx, ny = x+dx, y+dy
        if (nx, ny) not in grid:
            continue
        bump_and_flash(flashed, nx, ny)


part1 = 0

for step in range(100_000_000):
    flashed = set()
    for x, y in grid.keys():
        bump_and_flash(flashed, x, y)
    for x, y in flashed:
        grid[(x, y)] = 0
    part1 += len(flashed)
    if step == 99:
        print("part 1:", part1)
    if len(flashed) == 100:
        print("part 2:", step + 1)
        break
    # print(f"--- {step} ---")
    # for y in range(10):
    #     for x in range(10):
    #         v = grid[(x, y)]
    #         if v == 0:
    #             print(f"\033[1m{v}\033[0m", end="")
    #         else:
    #             print(v, end="")
    #     print()
