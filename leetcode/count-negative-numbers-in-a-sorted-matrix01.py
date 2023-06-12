class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        answer = 0
        ord = [n - 1, 0]
        while 0 <= ord[0] < n and 0 <= ord[1] < m:
            # move right until find negative number
            if grid[ord[0]][ord[1]] >= 0:
                ord[1] = ord[1] + 1
            # if find, move up
            else:
                answer += m - ord[1]
                ord[0] = ord[0] - 1
        return answer