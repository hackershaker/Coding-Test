import sys


class Solution:
    def __init__(self):
        self.left = int(sys.stdin.readline().strip())

    def solution(self):
        self.left %= 100
        dist = [5, 10, 15, 20]
        for i in range(len(dist)):
            if self.left >= dist[i] * 2:
                self.left -= dist[i] * 2
                continue

            if self.left <= dist[i]:
                print(-(-self.left // 5))
            else:
                print(-((-dist[i] * 2 + self.left) // 5))
            return


if __name__ == "__main__":
    s = Solution()
    s.solution()
