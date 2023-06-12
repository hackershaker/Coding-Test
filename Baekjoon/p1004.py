import sys


class Solution:
    def __init__(self):
        self.sx, self.sy, self.gx, self.gy = map(
            int, sys.stdin.readline().strip().split(" ")
        )
        self.n = int(input())
        self.planet = [map(int, input().split(" ")) for _ in range(self.n)]

    def solution(self):
        answer = 0
        for cx, cy, r in self.planet:
            ds = ((self.sx - cx) ** 2 + (self.sy - cy) ** 2) ** 0.5
            dg = ((self.gx - cx) ** 2 + (self.gy - cy) ** 2) ** 0.5
            if (ds < r and dg > r) or (ds > r and dg < r):
                answer += 1
        print(answer)


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        s = Solution()
        s.solution()
