import sys


class Solution:
    def __init__(self):
        self.n = int(sys.stdin.readline().strip())

    def solution(self):
        dic = {"ocean": 0, "temperature": -30, "oxygen": 0}
        for _ in range(self.n):
            env, num = sys.stdin.readline().strip().split(" ")
            dic[env] += int(num[1:])
            if dic["ocean"] >= 9 and dic["temperature"] >= 8 and dic["oxygen"] >= 14:
                print("liveable")
                return
        print("not liveable")


if __name__ == "__main__":
    s = Solution()
    s.solution()
