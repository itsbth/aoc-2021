from itertools import chain
ff = open('../input')


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


draws = [int(n) for n in next(ff).split(',')]
drawn_at = {n: i for i, n in enumerate(draws)}

boards = []


def splitrow(row):
    return [int(n) for n in row.strip().split(' ') if n]


for board in chunker(list(ff), 6):
    ii = iter(board)
    next(ii)  # skip newline
    boards.append([splitrow(row) for row in ii])


def rows(board):
    return board


def columns(board):
    return ([board[n][i] for n in range(5)] for i in range(5))


def rows_and_columns(board):
    return chain(rows(board), columns(board))


def wins_at(board):
    wa = 1024  # arbitrary value greater than any number in the board
    for line in rows_and_columns(board):
        wa = min([wa, max(drawn_at.get(n, 1024) for n in line)])
    return wa


def sum_unmarked(board, drawn):
    return sum(n for row in board for n in row if n not in drawn)


results = []

for b in boards:
    round = wins_at(b)
    drawn = draws[round]
    unmarked = sum_unmarked(b, draws[:round+1])
    results.append((round, drawn, unmarked))

by_won = sorted(results, key=lambda r: r[0])
round, drawn, unmarked = by_won[1]
print(
    f"Part 1: round: {round}, drawn: {drawn}, sum: {unmarked}, answer: {drawn * unmarked}")
round, drawn, unmarked = by_won[-1]
print(
    f"Part 2: round: {round}, drawn: {drawn}, sum: {unmarked}, answer: {drawn * unmarked}")
