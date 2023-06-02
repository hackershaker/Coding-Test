import sys


class Solution:
    def __init__(self):
        self.n, self.m = map(int, sys.stdin.readline().strip().split(" "))
        self.board = [sys.stdin.readline().strip() for _ in range(self.n)]

    def solution(self):
        r, b = self.findBalls()

        move = 1
        stack = [(r, b)]
        visited = set()
        nextStack = []
        while stack:
            cr, cb = stack.pop()
            visited.add((cr, cb))
            for nx in (0, 1), (0, -1), (1, 0), (-1, 0):
                nr, nb, flag = self.rolling(cr, cb, nx)
                if flag == 1:
                    print(move)
                    return
                elif (nr, nb) in visited:
                    continue
                elif flag == 0:
                    nextStack.append((nr, nb))

            if not stack:
                move += 1
                if move > 10:
                    print(-1)
                    return
                stack = nextStack
                nextStack = []
        print(-1)
        return

    # -1: 실패(파란구슬빠짐), 1: 성공, 0: 아무 일도 없음
    def rolling(self, r, b, d):
        r_flag = 0
        nr, nb = r, b
        while True:
            x, y = nr[0] + d[0], nr[1] + d[1]
            if (
                not (0 <= x < self.n and 0 <= y < self.m)
                or (x, y) == nb
                or self.board[x][y] == "#"
            ):
                break
            if self.board[x][y] == "O":
                r_flag = 1
                nr = (-1, -1)
                break
            nr = (x, y)
        while True:
            x, y = nb[0] + d[0], nb[1] + d[1]
            if (
                not (0 <= x < self.n and 0 <= y < self.m)
                or (x, y) == nr
                or self.board[x][y] == "#"
            ):
                break
            if self.board[x][y] == "O":
                return nr, nb, -1
            nb = (x, y)
        while True:
            x, y = nr[0] + d[0], nr[1] + d[1]
            if (
                not (0 <= x < self.n and 0 <= y < self.m)
                or (x, y) == nb
                or self.board[x][y] == "#"
            ):
                break
            nr = (x, y)

        return nr, nb, r_flag

    def findBalls(self):
        r, b = (0, 0), (0, 0)
        for i in range(self.n):
            for j in range(self.m):
                if self.board[i][j] == "R":
                    r = (i, j)
                if self.board[i][j] == "B":
                    b = (i, j)
                if self.board[i][j] == "O":
                    hole = (i, j)
        return r, b


if __name__ == "__main__":
    s = Solution()
    s.solution()
