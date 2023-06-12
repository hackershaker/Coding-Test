from collections import defaultdict
import sys


class Solution:
    def __init__(self):
        self.a = sys.stdin.readline().strip()
        self.b = sys.stdin.readline().strip()

    def solution(self):
        a_counter, b_counter = defaultdict(int), defaultdict(int)
        for s in self.a:
            a_counter[s] += 1
        for s in self.b:
            b_counter[s] += 1

        answer = 0
        for k in set(self.a + self.b):
            answer += abs(a_counter[k] - b_counter[k])
        print(answer)


if __name__ == "__main__":
    s = Solution()
    s.solution()
