from functools import lru_cache
import sys


class Solution:
    def solution(self):
        n = int(sys.stdin.readline().strip())
        for i in range(n):
            self.fibonacci(i)
        print(self.fibonacci(n))

    @lru_cache(maxsize=None)
    def fibonacci(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n >= 2:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)


if __name__ == "__main__":
    s = Solution()
    s.solution()
