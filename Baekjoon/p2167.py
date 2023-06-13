from pprint import pprint
import sys


class Solution:
    def __init__(self):
        self.n, self.m = map(int, sys.stdin.readline().strip().split(" "))
        self.board = [
            list(map(int, sys.stdin.readline().strip().split(" ")))
            for _ in range(self.n)
        ]
        self.k = int(sys.stdin.readline().strip())
        self.query = [
            list(map(int, sys.stdin.readline().strip().split(" ")))
            for _ in range(self.k)
        ]

    def solution(self):
        pfSum = [[0] * (self.m + 1) for _ in range(self.n + 1)]
        for i in range(1, self.n + 1):
            for j in range(1, self.m + 1):
                pfSum[i][j] = (
                    self.board[i - 1][j - 1]
                    + pfSum[i - 1][j]
                    + pfSum[i][j - 1]
                    - pfSum[i - 1][j - 1]
                )
        for i, j, x, y in self.query:
            print(pfSum[x][y] - pfSum[i - 1][y] - pfSum[x][j - 1] + pfSum[i - 1][j - 1])


if __name__ == "__main__":
    s = Solution()
    s.solution()


"""
2 3
1 2 4
8 16 32
4
1 1 2 3
1 2 1 2
1 3 2 3
1 1 1 2
"""
