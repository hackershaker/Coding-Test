from collections import deque
import sys


class Solution:
    def __init__(self) -> None:
        self.n, self.m = map(int, sys.stdin.readline().strip().split(" "))
        self.board = [list(sys.stdin.readline().strip()) for _ in range(self.n)]

    def solution(self):
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        path = [
            [[float("inf"), float("inf")] for _ in range(self.m)] for _ in range(self.n)
        ]
        path[0][0][0], path[0][0][1] = 1, 1  # 일반경로, 벽뚫경로

        stack = deque([(0, 0, 0, 1)])  # dist, cur ordinate, ,wall break number
        while stack:
            x, y, wall, dist = stack.popleft()
            if x == self.n - 1 and y == self.m - 1:
                path[x][y][wall] = min(path[x][y][wall], dist)
                continue

            for next in d:
                nx, ny = x + next[0], y + next[1]

                if not (0 <= nx < self.n and 0 <= ny < self.m):
                    continue
                if (
                    wall + int(self.board[nx][ny]) <= 1
                    and dist + 1 < path[nx][ny][wall + int(self.board[nx][ny])]
                ):
                    path[nx][ny][wall + int(self.board[nx][ny])] = dist + 1
                    stack.append((nx, ny, wall + int(self.board[nx][ny]), dist + 1))

        print(min(path[self.n - 1][self.m - 1])) if min(
            path[self.n - 1][self.m - 1]
        ) < 1000001 else print(-1)


if __name__ == "__main__":
    s = Solution()
    s.solution()


"""
10 9
011110000
011110110
000000110
011111110
000010000
011111110
011111110
011110000
011110110
000000110
"""
