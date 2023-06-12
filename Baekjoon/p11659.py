import sys


class Solution:
    def solution(self):
        n, m = map(int, sys.stdin.readline().strip().split(" "))
        arr = list(map(int, sys.stdin.readline().strip().split(" ")))
        prefixSum = [0]
        for element in arr:
            prefixSum.append(element + prefixSum[-1])
        for _ in range(m):
            i, j = map(int, sys.stdin.readline().strip().split(" "))
            sys.stdout.write(str(prefixSum[j] - prefixSum[i - 1]) + "\n")


if __name__ == "__main__":
    s = Solution()
    s.solution()
