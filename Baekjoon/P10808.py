import sys


class Solution:
    def solution(self):
        S = sys.stdin.readline().strip()
        count = [0] * 26
        for s in S:
            count[ord(s) - 97] += 1

        sys.stdout.write(" ".join(map(str, count)) + "\n")


if __name__ == "__main__":
    s = Solution()
    s.solution()
