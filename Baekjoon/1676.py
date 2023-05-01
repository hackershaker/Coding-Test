import sys


input = sys.stdin.readline
print = sys.stdout.write


class Solution:
    def solution(self):
        five = 0
        n = int(input().strip())
        for i in range(1, n + 1):
            if str(i)[-1] == "0" or str(i)[-1] == "5":
                five += self.getNumberOfDivisor(i, 5)

        print(str(five) + "\n")

    def getNumberOfDivisor(self, num, k):
        result = 0
        while True:
            num, r = divmod(num, k)
            if r == 0:
                result += 1
            else:
                return result


if __name__ == "__main__":
    s = Solution()
    s.solution()
