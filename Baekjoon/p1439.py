import sys


class Solution:
    def __init__(self):
        self.s = sys.stdin.readline().strip()

    def solution(self):
        comp = ""
        for w in self.s:
            if not comp or comp[-1] != w:
                comp += w
        num0 = comp.count("0")
        print(min(num0, len(comp) - num0))


if __name__ == "__main__":
    s = Solution()
    s.solution()
