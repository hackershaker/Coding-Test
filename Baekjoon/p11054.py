from bisect import bisect_left
import sys


class Solution:
    def __init__(self) -> None:
        self.n = int(sys.stdin.readline().strip())
        self.A = list(map(int, sys.stdin.readline().strip().split(" ")))

    def solution(self):
        forward, backward = [], []
        dp_forward, dp_backward = [0] * self.n, [0] * self.n

        for i in range(self.n):
            f, b = i, self.n - i - 1

            if not forward:
                forward.append(self.A[f])
                dp_forward[f] = 1
            else:
                if forward[-1] < self.A[f]:
                    forward.append(self.A[f])
                    dp_forward[f] = len(forward)
                else:
                    idx = bisect_left(forward, self.A[i])
                    forward[idx] = min(forward[idx], self.A[i])
                    dp_forward[f] = idx + 1

            if not backward:
                backward.append(self.A[b])
                dp_backward[b] = 1
            else:
                if backward[-1] < self.A[b]:
                    backward.append(self.A[b])
                    dp_backward[b] = len(backward)
                else:
                    idx = bisect_left(backward, self.A[self.n - i - 1])
                    backward[idx] = min(backward[idx], self.A[self.n - i - 1])
                    dp_backward[b] = idx + 1

        print(max([dp_forward[i] + dp_backward[i] - 1 for i in range(self.n)]))


if __name__ == "__main__":
    s = Solution()
    s.solution()
