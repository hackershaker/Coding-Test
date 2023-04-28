import sys


class Solution:
    def solution(self):
        r1, s = map(float, sys.stdin.readline().strip().split(" "))
        print(int(s * 2 - r1))


if __name__ == "__main__":
    s = Solution()
    s.solution()
