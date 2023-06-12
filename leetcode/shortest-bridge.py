from typing import List


class Solution:
    def __init__(self) -> None:
        self.island = set()

    def shortestBridge(self, grid: List[List[int]]) -> int:
        self.findIsland(grid)
        return self.findBridge(grid)

    def findIsland(self, grid):
        result = set()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1 and (i, j) not in visited:
                    result.add((i, j))
                    stack = [(i, j)]
                    while stack:
                        node = stack.pop()
                        visited.add(node)
                        for next in (0, 1), (0, -1), (1, 0), (-1, 0):
                            x, y = node[0] + next[0], node[1] + next[1]
                            if (
                                0 <= x < len(grid)
                                and 0 <= y < len(grid)
                                and (x, y) not in visited
                                and grid[x][y] == 1
                            ):
                                stack.append((x, y))
                                result.add((x, y))
                    self.island = result
                    return

    def findBridge(self, grid):
        temp = []
        stack = list(self.island)
        visited = set()
        distance = 1
        while stack:
            node = stack.pop()
            visited.add(node)
            for next in (0, 1), (0, -1), (1, 0), (-1, 0):
                x, y = node[0] + next[0], node[1] + next[1]
                if (x, y) in self.island or (x, y) in visited:
                    continue
                if 0 <= x < len(grid) and 0 <= y < len(grid):
                    if grid[x][y] == 1:
                        return distance - 1
                    temp.append((x, y))
                    visited.add((x, y))

            if not stack:
                stack = temp
                temp = []
                distance += 1

        return distance
