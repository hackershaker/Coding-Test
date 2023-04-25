import sys


class Solution:
    def __init__(self) -> None:
        self.primes = self.getPrimeList()

    def getPrimeList(self):
        p = {x for x in range(2, 10000)}
        for i in range(2, 5001):
            for j in range(2, 10000 // i):
                p.discard(i * j)
        return p

    def solution(self):
        n = int(sys.stdin.readline().strip())
        a, b = 0, 10001
        for k in self.primes:
            if n - k in self.primes:
                x, y = k, n - k
                if x > y:
                    x, y = y, x
                if abs(x - y) < abs(a - b):
                    a, b = x, y
        print(str(a) + " " + str(b))


if __name__ == "__main__":
    s = Solution()
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        s.solution()
