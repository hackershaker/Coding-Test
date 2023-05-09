class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d_index = 0
        answer = []

        cur = [0, 0]
        m, n = len(matrix), len(matrix[0])
        k = 0
        total = m * n
        while k < total:
            answer.append(matrix[cur[0]][cur[1]])
            x, y = cur[0] + direction[d_index][0], cur[1] + direction[d_index][1]
            if not (0 <= x < m and 0 <= y < n) or matrix[x][y] == "N":
                d_index = (d_index + 1) % 4
                x, y = cur[0] + direction[d_index][0], cur[1] + direction[d_index][1]

            k += 1
            matrix[cur[0]][cur[1]] = "N"
            cur = [x, y]

        return answer
