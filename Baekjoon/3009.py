import sys


class Solution:
    def solution(self):
        x_set, y_set = set(), set()
        x_total, y_total = 0, 0
        for _ in range(3):
            x, y = map(int, sys.stdin.readline().strip().split(" "))
            x_set.add(x)
            y_set.add(y)
            x_total += x
            y_total += y

        print(str(2 * sum(x_set) - x_total) + " " + str(2 * sum(y_set) - y_total))


if __name__ == "__main__":
    s = Solution()
    s.solution()
