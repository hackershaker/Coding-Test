from collections import defaultdict
import sys


class Solution:
    def solution(self):
        m, n, h = map(int, sys.stdin.readline().strip().split(" "))
        board = []
        rotten = []
        count = defaultdict(int)
        for k in range(h):
            plate = []
            for i in range(n):
                row = list(map(int, sys.stdin.readline().strip().split(" ")))
                plate.append(row)
                for j in range(m):
                    count[row[j]] += 1
                    if row[j] == 1:
                        rotten.append((i, j, k))
            board.append(plate)

        if not count[0]:
            sys.stdout.write("0\n")
            return
        day = 0
        temp = []
        nextord = (
            (1, 0, 0),
            (-1, 0, 0),
            (0, 1, 0),
            (0, -1, 0),
            (0, 0, 1),
            (0, 0, -1),
        )
        while rotten:
            x, y, z = rotten.pop()
            for i, j, k in nextord:
                a, b, c = x + i, y + j, z + k
                if not (0 <= a < n and 0 <= b < m and 0 <= c < h):
                    continue
                if board[c][a][b] == 0:
                    board[c][a][b] = 1
                    temp.append((a, b, c))
                    count[1] += 1
                    count[0] -= 1

            if not rotten:
                day += 1
                if count[0] == 0:
                    print(day)
                    return
                if temp:
                    rotten = temp
                    temp = []
                else:
                    break
        print(-1)


if __name__ == "__main__":
    s = Solution()
    s.solution()
