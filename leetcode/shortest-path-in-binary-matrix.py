from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1:
            return -1
        d = [(1, 1), (1, 0), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
        stack = deque([(1, 0, 0)])
        visited = set()
        while stack:
            dist, x, y = stack.popleft()
            if x == n - 1 and y == n - 1:
                return dist
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for next in d:
                a, b = x + next[0], y + next[1]
                if not (0 <= a < n and 0 <= b < n) or (a, b) in visited:
                    continue
                if grid[a][b] == 0:
                    stack.append((dist + 1, a, b))
        return -1
