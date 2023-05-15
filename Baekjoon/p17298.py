import sys


class Solution:
    def __init__(self):
        self.n = int(sys.stdin.readline().strip())
        self.seq = list(map(int, sys.stdin.readline().strip().split(" ")))

    def solution(self):
        answer = [-1] * len(self.seq)
        arr = []
        for i in range(len(self.seq)):
            while arr:
                if self.seq[arr[-1]] < self.seq[i]:
                    answer[arr[-1]] = self.seq[i]
                    arr.pop()
                else:
                    break
            
            arr.append(i)

        print(" ".join(map(str, answer)))


if __name__ == "__main__":
    s = Solution()
    s.solution()
