from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                node = (i, j)

                # if up coordinate is exists
                if 0 <= node[0] - 1 < m and 0 <= node[1] < n:
                    fromUp = grid[node[0]][node[1]] + grid[node[0] - 1][node[1]]
                else:
                    fromUp = -1
                # if left coordinate is exists
                if 0 <= node[0] < m and 0 <= node[1] - 1 < n:
                    fromLeft = grid[node[0]][node[1]] + grid[node[0]][node[1] - 1]
                else:
                    fromLeft = -1

                if fromUp >= 0 and fromLeft >= 0:
                    grid[node[0]][node[1]] = min(fromUp, fromLeft)
                elif (fromUp < 0) ^ (fromLeft < 0):
                    if fromUp < 0:
                        grid[node[0]][node[1]] = fromLeft
                    if fromLeft < 0:
                        grid[node[0]][node[1]] = fromUp
                else:
                    pass

        return grid[m - 1][n - 1]
