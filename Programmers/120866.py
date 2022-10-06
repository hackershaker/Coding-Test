def solution(board):
    danger = set()
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                dangerlist = [
                    [i - 1, j - 1],
                    [i, j - 1],
                    [i + 1, j - 1],
                    [i - 1, j],
                    [i, j],
                    [i + 1, j],
                    [i - 1, j + 1],
                    [i, j + 1],
                    [i + 1, j + 1],
                ]
                for dpoint in dangerlist:
                    if (
                        dpoint[0] < 0
                        or dpoint[0] >= n
                        or dpoint[1] < 0
                        or dpoint[1] >= n
                    ):
                        continue
                    else:
                        danger.add(tuple(dpoint))
    return n ** 2 - len(danger)


print(
    solution(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    ),
    16,
)
print(
    solution(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0],
        ]
    ),
    13,
)
