from itertools import combinations
import sys


class Solution:
    def solution(self):
        n = int(sys.stdin.readline().strip())
        S = [list(map(int, sys.stdin.readline().strip().split(" "))) for _ in range(n)]

        answer = float("inf")
        team = [i for i in range(n)]
        teamNumber = n // 2
        for comb in combinations(team, teamNumber):
            another = [i for i in range(n) if i not in comb]
            answer = min(
                answer, abs(self.totalStat(S, another) - self.totalStat(S, comb))
            )

        sys.stdout.write(str(answer) + "\n")

    def totalStat(self, S, team):
        result = 0
        for x, y in combinations(team, 2):
            result += S[x][y] + S[y][x]
        return result


if __name__ == "__main__":
    s = Solution()
    s.solution()
