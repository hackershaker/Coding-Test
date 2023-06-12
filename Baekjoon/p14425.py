import sys


class Solution:
    def __init__(self):
        self.n, self.m = map(int, sys.stdin.readline().strip().split(" "))
        self.dictionary = {sys.stdin.readline().strip() for _ in range(self.n)}
        self.strings = [sys.stdin.readline().strip() for _ in range(self.m)]

    def solution(self):
        print(len([True for string in self.strings if string in self.dictionary]))


if __name__ == "__main__":
    s = Solution()
    s.solution()
