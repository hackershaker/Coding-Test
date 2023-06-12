import sys


class Solution:
    def __init__(self) -> None:
        self.answer = []

    def solution(self, k, S):
        self.sequence([], S, k)
        for li in self.answer:
            print(li)
        print("")

    def sequence(self, arr: list, S: list, k: int):
        if len(arr) == 6:
            self.answer.append(" ".join([str(S[element]) for element in arr]))
            return
        result = []
        if not arr:
            for i in range(len(S)):
                arr.append(i)
                self.sequence(arr, S, k)
                arr.pop()
        else:
            for i in range(arr[-1] + 1, len(S)):
                arr.append(i)
                self.sequence(arr, S, k)
                arr.pop()

        return


if __name__ == "__main__":
    while True:
        k, *S = map(int, sys.stdin.readline().strip().split(" "))
        if not k: break
        s = Solution()
        s.solution(k, S)
