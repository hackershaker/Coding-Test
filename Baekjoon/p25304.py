import sys


class Solution:
    def solution(self):
        x = float(sys.stdin.readline().rstrip())
        n = int(sys.stdin.readline().rstrip())
        for _ in range(n):
            a, b = sys.stdin.readline().rstrip().split(" ")
            a = float(a)
            b = int(b)
            x -= a * b
        print("Yes") if x == 0 else print("No")


if __name__ == "__main__":
    s = Solution()
    s.solution()
