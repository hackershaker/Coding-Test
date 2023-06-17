import sys


class Solution:
    def solution(self):
        while True:
            a, b = map(int, sys.stdin.readline().strip().split(" "))
            if a == 0 and b == 0:
                return
            if a % b == 0:
                print("multiple")
            elif b % a == 0:
                print("factor")
            else:
                print("neither")


if __name__ == "__main__":
    s = Solution()
    s.solution()
