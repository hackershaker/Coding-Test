from collections import Counter
import sys


class Solution:
    def solution(self):
        n = int(sys.stdin.readline().strip())
        integers = map(int, sys.stdin.readline().strip().split())
        v = int(sys.stdin.readline().strip())
        counter = Counter(integers)
        print(counter[v])
        return counter[v]

if __name__=="__main__":
    s = Solution()
    s.solution()