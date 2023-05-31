import sys


class Solution:
    def __init__(self):
        self.k, self.n, self.m = map(int, sys.stdin.readline().strip().split(" "))

    def solution(self):
        print(self.k * self.n - self.m) if self.k * self.n - self.m > 0 else print(0)


if __name__ == "__main__":
    s = Solution()
    s.solution()
