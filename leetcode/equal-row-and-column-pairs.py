class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                a = 0
                while a < len(grid) and a < len(grid):
                    if grid[i][a] != grid[a][j]:
                        break
                    a += 1
                if a == len(grid):
                    answer += 1
        return answer
