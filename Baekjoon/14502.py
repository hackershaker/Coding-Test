from itertools import combinations
import sys


class Solution:
    def solution(self):
        n, m = map(int, sys.stdin.readline().strip().split(" "))
        lab = []
        for _ in range(n):
            lab.append(list(sys.stdin.readline().strip().split(" ")))

        zeroArea, twoArea = set(), set()
        for i in range(n):
            for j in range(m):
                if lab[i][j] == "0":
                    zeroArea.add((i, j))
                if lab[i][j] == "2":
                    twoArea.add((i, j))

        possible = combinations(zeroArea, 3)
        answer = 0
        for c in possible:
            lab[c[0][0]][c[0][1]], lab[c[1][0]][c[1][1]], lab[c[2][0]][c[2][1]] = (
                "1",
                "1",
                "1",
            )

            stack = list(twoArea)
            visited = set()
            temp = len(zeroArea) - 3
            while stack:
                point = stack.pop()
                for next in (0, 1), (0, -1), (1, 0), (-1, 0):
                    nextpoint = (point[0] + next[0], point[1] + next[1])
                    if nextpoint in visited or not (
                        0 <= nextpoint[0] < n and 0 <= nextpoint[1] < m
                    ):
                        continue
                    value = lab[nextpoint[0]][nextpoint[1]]
                    if value == "1" or value == "2":
                        visited.add(nextpoint)
                    else:
                        temp -= 1
                        visited.add(nextpoint)
                        stack.append(nextpoint)
            answer = max(answer, temp)
            lab[c[0][0]][c[0][1]], lab[c[1][0]][c[1][1]], lab[c[2][0]][c[2][1]] = (
                "0",
                "0",
                "0",
            )
        print(answer)
        return answer


if __name__ == "__main__":
    s = Solution()
    s.solution()
