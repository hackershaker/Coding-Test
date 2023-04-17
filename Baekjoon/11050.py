from math import factorial
import sys


class Solution:
    def solution(self):
        n, k = map(int, sys.stdin.readline().strip().split(" "))
        print(int(factorial(n) / (factorial(k) * factorial(n - k))))


if __name__ == "__main__":
    s = Solution()
    s.solution()
