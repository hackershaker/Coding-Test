import sys


class Solution:
    def solution(self):
        n, m = map(int, sys.stdin.readline().strip().split(" "))
        sets = {sys.stdin.readline().strip() for _ in range(n)}
        result = [
            name for _ in range(m) if (name := sys.stdin.readline().strip()) in sets
        ]

        print(len(result))
        for name in sorted(result):
            print(name)


if __name__ == "__main__":
    s = Solution()
    s.solution()
