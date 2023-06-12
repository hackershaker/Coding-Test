import sys


class Solution:
    def solution(self):
        burger = {int(sys.stdin.readline().strip()) for _ in range(3)}
        drink = {int(sys.stdin.readline().strip()) for _ in range(2)}
        sys.stdout.write(str(min(burger) + min(drink) - 50) + "\n")


if __name__ == "__main__":
    s = Solution()
    s.solution()
