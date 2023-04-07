class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and grid[i][j] == 1:
                    self.dfs((i, j), grid)

        answer = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    answer += 1
        return answer

    def dfs(self, ord, grid):
        if (
            not (0 <= ord[0] < len(grid))
            or not (0 <= ord[1] < len(grid[0]))
            or grid[ord[0]][ord[1]] == 0
        ):
            return

        grid[ord[0]][ord[1]] = 0
        self.dfs((ord[0] + 1, ord[1]), grid)
        self.dfs((ord[0] - 1, ord[1]), grid)
        self.dfs((ord[0], ord[1] + 1), grid)
        self.dfs((ord[0], ord[1] - 1), grid)
