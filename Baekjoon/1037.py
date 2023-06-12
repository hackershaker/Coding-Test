import sys


class Solution:
    def solution(self):
        n = int(sys.stdin.readline().strip())
        minvalue, maxvalue = 1000001, 1
        numList = list(map(int, sys.stdin.readline().strip().split(" ")))
        numList.sort()

        originalNum = numList[0] * numList[-1]
        print(originalNum)
        return originalNum


if __name__ == "__main__":
    s = Solution()
    s.solution()
