from collections import deque
from heapq import heapify, heappop
from pprint import pprint


class Solution:
    def __init__(self):
        self.n = int(input())
        self.board = [list(map(int, input().split(" "))) for _ in range(self.n)]
        self.time = 0
        self.d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.size = 2
        self.eat = 0

    def solution(self):
        cur = self.findStart()

        while True:
            target = []
            # find target
            stack = deque([(cur, 0)])
            temp = deque([])
            visited = {cur}
            while stack:
                node, dist = stack.popleft()
                for a, b in self.d:
                    x, y = node[0] + a, node[1] + b
                    if (x, y) in visited or not (0 <= x < self.n and 0 <= y < self.n):
                        continue
                    if 0 < self.board[x][y] < self.size:
                        target.append(
                            (
                                dist + 1,
                                x,
                                y,
                            )
                        )
                    elif self.board[x][y] <= self.size:
                        temp.append(((x, y), dist + 1))
                        visited.add((x, y))

                if not stack:
                    if target or not temp:
                        break
                    stack = temp
            if not target:
                break
            heapify(target)
            dist, x, y = heappop(target)
            self.time += dist
            self.eat += 1
            if self.eat == self.size:
                self.size += 1
                self.eat = 0
            self.board[x][y] = self.size
            self.board[cur[0]][cur[1]] = 0
            cur = (x, y)
        print(self.time)

    def findStart(self) -> tuple:
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 9:
                    return (i, j)


if __name__ == "__main__":
    s = Solution()
    s.solution()
