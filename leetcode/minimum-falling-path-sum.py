class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(1, n):
            for j in range(n):
                temp = 101
                if j-1 > 0: temp = min(temp, matrix[i-1][j-1])
                if j+1 < n: temp = min(temp, matrix[i-1][j+1])
                temp = min(temp, matrix[i-1][j])
                matrix[i][j] += temp
        
        return min(matrix[-1])