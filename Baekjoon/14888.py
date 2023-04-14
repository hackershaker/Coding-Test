from collections import deque
import sys


class Solution:
    def solution(self):
        n = sys.stdin.readline().strip()
        nums = list(map(int, sys.stdin.readline().strip().split(" ")))
        operator = list(map(int, sys.stdin.readline().strip().split(" ")))

        minValue, maxValue = float("inf"), -float("inf")
        stack = deque([(nums, i, operator) for i in range(4)])
        while stack:
            numArray, operatorIndex, operator = stack.popleft()
            if len(numArray) == 1:
                minValue = min(minValue, numArray[0])
                maxValue = max(maxValue, numArray[0])
                continue
            cal = 0
            if operator[operatorIndex]:
                if operatorIndex == 0:
                    cal = numArray[0] + numArray[1]
                if operatorIndex == 1:
                    cal = numArray[0] - numArray[1]
                if operatorIndex == 2:
                    cal = numArray[0] * numArray[1]
                if operatorIndex == 3:
                    if numArray[0] == 0:
                        cal = 0
                    else:
                        cal = (numArray[0] // abs(numArray[0])) * (
                            abs(numArray[0]) // numArray[1]
                        )
                op = operator[:]
                op[operatorIndex] -= 1
                for i in range(4):
                    stack.append(([cal] + numArray[2:], i, op))

        print(maxValue)
        print(minValue)


if __name__ == "__main__":
    s = Solution()
    s.solution()
