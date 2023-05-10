class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        answer = [[0] * n for _ in range(n)]

        cur = (0, 0)
        d = (0, 1)
        i = 1
        while (0 <= cur[0] < n and 0 <= cur[1] < n) and answer[cur[0]][cur[1]] == 0:
            answer[cur[0]][cur[1]] = i
            x, y = cur[0] + d[0], cur[1] + d[1]

            if not (0 <= x < n and 0 <= y < n) or answer[x][y] > 0:
                d = (d[1], -d[0])
                x, y = cur[0] + d[0], cur[1] + d[1]
            cur = (x, y)
            i += 1

        return answer
