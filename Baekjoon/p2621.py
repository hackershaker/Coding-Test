from collections import Counter
import sys


class Solution:
    def __init__(self):
        self.cards = [sys.stdin.readline().strip().split(" ") for _ in range(5)]
        self.color = {x[0] for x in self.cards}
        self.number = sorted([int(x[1]) for x in self.cards])
        self.numCounter = Counter(self.number)

    def cardGame(self):
        # 1
        if self.isContinue(self.number) and len(self.color) == 1:
            return self.number[-1] + 900
        # 4
        if len(self.color) == 1:
            return self.number[-1] + 600
        # 5
        if self.isContinue(self.number):
            return self.number[-1] + 500

        c = self.numCounter.most_common()
        # 2
        if c[0][1] == 4:
            return c[0][0] + 800
        # 3
        if c[0][1] == 3 and c[1][1] == 2:
            return c[0][0] * 10 + c[1][0] + 700
        # 6
        if c[0][1] == 3:
            return c[0][0] + 400
        # 7
        if c[0][1] == 2 and c[1][1] == 2:
            return max(c[0][0], c[1][0]) * 10 + min(c[0][0], c[1][0]) + 300
        # 8
        if c[0][1] == 2:
            return c[0][0] + 200
        return self.number[-1] + 100
    
    def solution(self):
        print(self.cardGame())

    def isContinue(self, arr):
        i = 0
        while i < len(arr) - 1:
            if arr[i] + 1 != arr[i + 1]:
                return False
            i += 1
        return True


if __name__ == "__main__":
    s = Solution()
    s.solution()
