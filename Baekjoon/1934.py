import functools
import sys


def preprocessArgs(func):
    def wrapper(self, a, b):
        if b > a:
            a, b = b, a
        return func(self, a, b)

    return wrapper


class Solution:
    def solution(self):
        a, b = map(int, sys.stdin.readline().strip().split(" "))
        _gcd = self.gcd(a, b)
        print(_gcd * (a // _gcd) * (b // _gcd))

    @functools.lru_cache(None)
    @preprocessArgs
    def gcd(self, a: int, b: int) -> int:
        while b > 0:
            _, r = divmod(a, b)
            a, b = b, r

        return a


if __name__ == "__main__":
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        s = Solution()
        s.solution()
