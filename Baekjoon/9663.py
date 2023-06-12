import sys


class Solution:
    def solution(self):
        n = int(sys.stdin.readline().strip())
        answer = 0
        for i in range(n // 2):
            answer += self.dfs(n, 1, {i}, {-i}, {i}) * 2
        if n % 2:
            k = n // 2
            answer += self.dfs(n, 1, {k}, {-k}, {k})
        sys.stdout.write(str(answer) + "\n")

    def dfs(self, n: int, row: int, col: set, dg45: set, dg135: set):
        if row == n:
            return 1
        answer = 0
        for i in range(n):
            if i not in col and row - i not in dg45 and row + i not in dg135:
                col.add(i)
                dg45.add(row - i)
                dg135.add(row + i)
                answer += self.dfs(n, row + 1, col, dg45, dg135)
                col.remove(i)
                dg45.remove(row - i)
                dg135.remove(row + i)
        return answer


if __name__ == "__main__":
    s = Solution()
    s.solution()
